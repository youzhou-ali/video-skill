// 最小渲染器：scene.html 暴露 window.renderAt(t) 和 window.SCENE={W,H,FPS,DURATION}
//   审片  node render.cjs scene.html --sheet=0.2,0.8,1.6,2.4 --out=out/sheet.jpg
//   成片  node render.cjs scene.html --out=out/video.mp4 [--from=0 --to=3] [--audio=a.mp3]
const { chromium } = require('playwright');
const { spawn, execFileSync } = require('child_process');
const fs = require('fs'), path = require('path');

const arg = k => (process.argv.find(a => a.startsWith(`--${k}=`)) || '').split('=').slice(1).join('=') || null;
const scene = path.resolve(process.argv[2]);
const out = arg('out') || 'out/video.mp4';
fs.mkdirSync(path.dirname(path.resolve(out)), { recursive: true });

(async () => {
  const opts = { args: ['--no-sandbox', '--force-color-profile=srgb'] };
  const browser = await chromium.launch(opts).catch(() => chromium.launch({ ...opts, channel: 'chrome' }));
  const page = await browser.newPage();
  page.on('pageerror', e => { console.error('PAGE ERROR:', e.message); process.exitCode = 1; });
  await page.goto('file://' + scene + '?render=1' + (arg('q') ? '&' + arg('q') : ''));
  await page.waitForFunction(() => window.renderAt && window.SCENE);
  await page.evaluate(() => document.fonts.ready);          // 字体就绪后再画第一帧
  const S = await page.evaluate(() => window.SCENE);
  await page.setViewportSize({ width: S.W, height: S.H });
  const shot = async t => { await page.evaluate(t => window.renderAt(t), t); return page.screenshot({ type: 'jpeg', quality: 92 }); };

  if (arg('sheet')) {                                        // 接触表：指定时刻的帧拼成一张图
    const ts = arg('sheet').split(',').map(Number), dir = fs.mkdtempSync(path.join(path.dirname(path.resolve(out)), 'sheet-'));
    for (let i = 0; i < ts.length; i++) fs.writeFileSync(path.join(dir, `${String(i).padStart(3, '0')}.jpg`), await shot(ts[i]));
    const cols = Math.min(4, ts.length), rows = Math.ceil(ts.length / cols);
    execFileSync('ffmpeg', ['-y', '-v', 'error', '-i', path.join(dir, '%03d.jpg'), '-vf', `scale=640:-1,tile=${cols}x${rows}`, '-frames:v', '1', out]);
    fs.rmSync(dir, { recursive: true });
  } else {                                                   // 成片：JPEG 帧直接管道给 ffmpeg，不落盘
    const from = +(arg('from') || 0), to = +(arg('to') || S.DURATION), n = Math.round((to - from) * S.FPS);
    const tmp = out.replace(/\.mp4$/, '.part.mp4');
    const a = arg('audio') ? ['-ss', String(from), '-i', arg('audio'), '-map', '0:v', '-map', '1:a', '-c:a', 'aac', '-t', String(to - from)] : [];
    const ff = spawn('ffmpeg', ['-y', '-v', 'error', '-f', 'image2pipe', '-c:v', 'mjpeg', '-framerate', String(S.FPS), '-i', '-', ...a,
      '-c:v', 'libx264', '-crf', '18', '-preset', 'veryfast', '-pix_fmt', 'yuv420p', tmp], { stdio: ['pipe', 'inherit', 'inherit'] });
    const done = new Promise(r => ff.on('close', r));
    for (let i = 0; i < n; i++) if (!ff.stdin.write(await shot(from + i / S.FPS))) await new Promise(r => ff.stdin.once('drain', r));
    ff.stdin.end();
    if (await done !== 0) throw new Error('ffmpeg failed');
    fs.renameSync(tmp, out);                                 // ffmpeg 正常退出才改成正式文件名
  }
  await browser.close();
  console.log('wrote', out);
})().catch(e => { console.error(e); process.exit(1); });
