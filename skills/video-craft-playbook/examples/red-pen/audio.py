# 《红笔》声音：全部代码合成，时间点取自 film.html 的同一套常数。
# 用法：python3 audio.py  → audio.wav（48 kHz 立体声）和 cues.txt（事件时间表，供质检对照）
import numpy as np
from scipy.signal import butter, sosfilt
from scipy.io import wavfile

SR, DUR = 48000, 30.0
N = int(SR * DUR)
rng = np.random.default_rng(7)                      # 固定种子：每次生成完全一样
music, sfx = np.zeros(N), np.zeros(N)
cues = []

def bp(x, lo, hi): return sosfilt(butter(2, [lo, hi], 'bandpass', fs=SR, output='sos'), x)
def lp(x, f): return sosfilt(butter(2, f, 'lowpass', fs=SR, output='sos'), x)
def hp(x, f): return sosfilt(butter(2, f, 'highpass', fs=SR, output='sos'), x)
def tt(d): return np.arange(int(SR * d)) / SR
def env(d, a, dec): t = tt(d); return np.minimum(t / max(a, 1e-4), 1) * np.exp(-t / dec)
def sweep(f0, f1, d):
    t = tt(d); f = f0 * (f1 / f0) ** (t / d); return np.sin(2 * np.pi * np.cumsum(f) / SR)
def add(bus, sig, t0, gain=1.0, name=None):
    i = int(t0 * SR)
    if i >= N: return
    j = min(N, i + len(sig)); bus[i:j] += sig[:j - i] * gain
    if name: cues.append((round(t0, 3), name))
noise = lambda d: rng.standard_normal(int(SR * d))
mtof = lambda m: 440 * 2 ** ((m - 69) / 12)

# ---------- 乐器 ----------
def kick(): d = .3; return sweep(120, 45, d) * env(d, .002, .12)
def bass(m): d = .6; t = tt(d); f = mtof(m); return (np.sin(2*np.pi*f*t) + .3*np.sin(4*np.pi*f*t)) * env(d, .005, .28)
def marimba(m, dec=.3):
    d = dec * 4; t = tt(d); f = mtof(m)
    return np.sin(2*np.pi*f*t) * env(d, .002, dec) + .25 * np.sin(2*np.pi*4*f*t) * env(d, .001, dec * .25)
def shaker(): return hp(noise(.08), 5000) * env(.08, .004, .025)

# ---------- 音乐：120 BPM，每小节 2 秒，C–Am–F–G ----------
CHORDS = [(48, [60, 64, 67]), (45, [60, 64, 69]), (41, [60, 65, 69]), (43, [59, 62, 67])]
SPLASH_T = None   # 下面算出后回填
def music_on(t): return t < SPLASH_T or 11.0 <= t < 28.0

# ---------- 与画面共用的常数 ----------
X0, X1, RUN_T, JUMP, VY, GR, WATER, GROUND = 150, 880, 3.6, 6.0, 855, 2444, 822, 760
T_ENTER = (VY + np.sqrt(VY**2 + 2*GR*(WATER-GROUND))) / GR
SPLASH_T = JUMP + T_ENTER                                   # 约 6.675 秒
def t_of_tw2(tw): return 18 + (tw - .3) / 1.6 if tw < 6 else 18 + 5.7 / 1.6 + (tw - 6)
JUMP2 = t_of_tw2(6.0)                                       # 约 21.56 秒
LAND2 = JUMP2 + 2 * VY * np.sqrt(1.4) / GR                           # 约 22.40 秒

for b in range(15):
    tb = 2 * b; root, tones = CHORDS[b % 4]
    for k, t in enumerate([tb, tb + 1.0]):
        if music_on(t): add(music, bass(root + 12 * k), t, .5)
        if (t < SPLASH_T or 17.0 <= t < 28.0): add(music, kick(), t, .55)
    for t in [tb + .5, tb + 1.5]:
        if music_on(t):
            g = .16 if t < 16 and t >= 11 else .22
            for i, m in enumerate(tones): add(music, marimba(m), t + i * .012, g)
    for i in range(4):
        t = tb + .25 + .5 * i
        if t < SPLASH_T or 18.0 <= t < 28.0: add(music, shaker(), t, .12)
# 落地时的重音和片尾和弦
for i, m in enumerate([60, 64, 67, 72]): add(music, marimba(m, .5), LAND2 + i * .01, .26)
add(music, kick(), LAND2, .6)
add(music, bass(36), 28.0, .6, 'end chord')
for i, m in enumerate([60, 64, 67, 72]): add(music, marimba(m, .9), 28.0 + i * .02, .24)
# 落水时音乐刹住，11.0 回来
gate = np.ones(N); ts = np.arange(N) / SR
gate[(ts >= SPLASH_T + .04) & (ts < 11.0)] = 0
fade = (ts >= SPLASH_T) & (ts < SPLASH_T + .04); gate[fade] = 1 - (ts[fade] - SPLASH_T) / .04
music *= gate
cues += [(round(SPLASH_T, 3), 'music stop'), (11.0, 'music back')]

# ---------- 音效 ----------
def step(): d = .09; return (lp(noise(d), 500) * .8 + np.sin(2*np.pi*140*tt(d))) * env(d, .002, .03)
def whoosh(d, peak):
    t = tt(d); e = np.where(t < peak, (t / peak) ** 2, np.exp(-(t - peak) / (d * .25)))
    return bp(noise(d), 300, 2600) * e
def splash():
    d = .7; return lp(noise(d), 2500) * env(d, .004, .16) * 1.4 + lp(noise(d), 600) * env(d, .002, .3)
def blip(f0, f1, d=.07): return sweep(f0, f1, d) * env(d, .004, d / 3)
def scratch(d, mod):
    t = tt(d); return bp(noise(d), 2200, 6500) * mod(t / d)
def thump(): d = .35; return sweep(95, 42, d) * env(d, .002, .14) + lp(noise(d), 400) * env(d, .001, .04)

# 第一次：跑步、急停、蓄力、起跳、落水
def steps(tw_list, to_t, gain):
    for k in range(1, int((X1 - X0) / 120) + 1):
        tw = RUN_T * (1 - np.sqrt(1 - 120 * k / (X1 - X0)))
        if tw > tw_list: add(sfx, step(), to_t(tw), gain, f'step {k}')
steps(0, lambda tw: tw, .5)
add(sfx, lp(noise(.3), 1500) * env(.3, .01, .08), 3.55, .35, 'skid')
d = 1.6; add(sfx, (np.sin(2*np.pi*np.cumsum(220 * 1.5 ** (tt(d)/d))/SR) * (.6 + .4*np.sin(2*np.pi*9*tt(d)))) * env(d, .5, 3) * np.minimum(1, (d - tt(d)) / .1), 4.4, .05, 'crouch tension')
add(sfx, whoosh(.35, .27), JUMP - .27 + 2/30 * 0, .5, 'jump whoosh peak@6.0')
add(sfx, splash(), SPLASH_T, .7, 'splash')
for i in range(3): add(sfx, blip(300 + i * 80, 900 + i * 100), 6.9 + i * .22 + .3, .2, f'bubble {i}')
add(sfx, blip(200, 520, .14), 7.8, .35, 'pop up')
add(sfx, sweep(330, 220, .55) * env(.55, .05, .3), 8.8, .12, 'droop')
add(sfx, blip(1400, 2400, .05), 9.15, .18, 'drip')
# 镜头拉远的"呼"
d = 1.6; t = tt(d); add(sfx, lp(np.cumsum(noise(d)) * .02, 260) * np.where(t < .25, t / .25, np.exp(-(t - .25) / .45)), 9.4, 2.2, 'pull whoosh')
# 红笔
add(sfx, whoosh(.5, .4) * .5, 11.9, .3, 'pen in')
add(sfx, scratch(1.0, lambda u: np.sin(np.pi * u) ** .5 * (.7 + .3 * np.sin(2*np.pi*6*u))), 12.4, .22, 'circle scratch')
add(sfx, scratch(1.0, lambda u: np.abs(np.sin(2*np.pi*4.5*u)) ** 1.5), 14.3, .22, 'note scratch')
# 格子重画：12 声，五声音阶往上走，落在十六分音符
PENTA = [72, 74, 76, 79, 81, 84, 86, 88, 91, 93, 96, 98]
for k in range(12): add(sfx, marimba(PENTA[k], .08), 16.25 + k * .125, .14, f'redraw {k}')
add(sfx, whoosh(1.0, .8) * .6, 18.0, .35, 'push in')
# 第二次：跑、起跳、落地、蹦一下
for k in range(1, int((X1 - X0) / 120) + 1):
    tw = RUN_T * (1 - np.sqrt(1 - 120 * k / (X1 - X0)))
    if tw > .3: add(sfx, step(), t_of_tw2(tw), .5, f'step2 {k}')
add(sfx, whoosh(.35, .27), JUMP2 - .27, .55, 'jump2 whoosh')
add(sfx, thump(), LAND2, .9, 'land2')
add(sfx, blip(300, 620, .16), JUMP2 + 1.45, .25, 'hop')
add(sfx, thump() * .5, JUMP2 + 1.85, .5, 'hop land')
add(sfx, scratch(.5, lambda u: np.sin(np.pi * u)), 26.6, .25, 'check scratch')
add(sfx, hp(noise(.12), 3000) * env(.12, .002, .03), 27.08, .4, 'check snap')

# 房间底噪：全片不断，桌面段更暗一点
room = lp(noise(DUR), 1200) * .012
room[ts >= 9.5] = lp(noise(DUR), 700)[ts >= 9.5] * .010

mix = music * .9 + sfx + room
mix *= 10 ** (-3 / 20) / np.max(np.abs(mix))                # 峰值 -3 dBFS，后面 loudnorm 再统一
st = np.stack([mix, mix], 1)
wavfile.write('audio.wav', SR, (st * 32767).astype(np.int16))
with open('cues.txt', 'w') as f:
    for t, n in sorted(cues): f.write(f'{t:7.3f}  {n}\n')
print('splash', round(SPLASH_T, 3), 'jump2', round(JUMP2, 3), 'land2', round(LAND2, 3), 'cues', len(cues))
