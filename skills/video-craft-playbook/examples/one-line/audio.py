# 《回家的线》声音：笔划纸声由笔速驱动，独奏旋律的音落在拐角上、音高跟着笔尖高度走。
# 输入 track.json（film.html 导出的每帧笔尖与拐角）；输出 audio.wav（48 kHz 立体声）和 cues.txt
import json, numpy as np
from scipy.signal import butter, sosfilt
from scipy.io import wavfile

SR, DUR, FPS = 48000, 30.0, 30
N = int(SR * DUR); ts = np.arange(N) / SR
rng = np.random.default_rng(11)
D = json.load(open('track.json')); TR, CO = D['track'], D['corners']
END_T, LIGHT_T = 26.2, 26.75
BULB = next(c for c in D['chapters'] if c['name'] == 'bulb')
cues = []
def bp(x, lo, hi): return sosfilt(butter(2, [lo, hi], 'bandpass', fs=SR, output='sos'), x)
def lp(x, f): return sosfilt(butter(2, f, 'lowpass', fs=SR, output='sos'), x)
def tt(d): return np.arange(int(SR * d)) / SR
mtof = lambda m: 440 * 2 ** ((m - 69) / 12)

# ---------- 笔划纸声 ----------
fr = np.array([f['t'] for f in TR]); vv = np.array([f['v'] for f in TR]); sx = np.array([f['sx'] for f in TR])
v = np.interp(ts, fr, vv); pan = np.clip(np.interp(ts, fr, sx) * 1.2, -.8, .8)
k = np.clip(v / 600, 0, 1)
amp = np.clip(v / 520, 0, 1.4) ** .5
amp = lp(amp, 30)                                       # 平滑包络，避免咔哒声
wn = rng.standard_normal(N)
pen = (bp(wn, 2200, 7500) * k * .7 + bp(wn, 700, 2400) * (1 - k * .7)) * amp * (1 - .3 * np.clip((v - 450) / 300, 0, 1))
ticks = np.zeros(N)                                     # 纸纤维的细小颗粒声，密度随速度
p_tick = np.clip(v / 520, 0, 1.5) * 90 / SR
ticks[rng.random(N) < p_tick] = rng.uniform(.3, 1, (rng.random(N) < p_tick).sum()) if False else 0
idx = np.where(rng.random(N) < p_tick)[0]
for i in idx:
    n = 60; ticks[i:i + n] += rng.uniform(.3, 1) * np.exp(-np.arange(min(n, N - i)) / 8)
ticks = bp(ticks, 1500, 9000)
pen = pen * .55 + ticks * .35
pen[ts > END_T + .02] *= np.exp(-(ts[ts > END_T + .02] - END_T - .02) / .03)
cues.append((0.0, 'pen scratch (speed-driven) whole film'))

sfx = np.zeros(N)
def add(bus, sig, t0, gain=1.0, name=None):
    i = int(t0 * SR); j = min(N, i + len(sig)); bus[i:j] += sig[:j - i] * gain
    if name: cues.append((round(t0, 3), name))
d = .12; t = tt(d); add(sfx, (np.sin(2*np.pi*520*t) * .6 + lp(rng.standard_normal(len(t)), 1800)) * np.exp(-t / .018), 0.0, .5, 'first touch (wood tap)')
d = .9; t = tt(d); add(sfx, lp(rng.standard_normal(len(t)), 500) * np.sin(np.pi * t / d) ** 2, END_T, .06, 'blot swell')

# ---------- 独奏旋律（类单簧管：奇次谐波 + 颤音） ----------
PENTA = [0, 2, 4, 7, 9]                                  # D 大调五声
def deg2midi(dg): return 62 + 12 * (dg // 5) + PENTA[dg % 5]
def y2midi(y): return deg2midi(int(np.clip(round((300 - y) / 62), 0, 12)))
def reed(m, d, vel=1.0, swell=False):
    t = tt(d); f = mtof(m) * (1 + .004 * np.sin(2*np.pi*5.2*t) * np.clip(t / .3, 0, 1))
    ph = 2 * np.pi * np.cumsum(f) / SR
    s = np.sin(ph) + .32 * np.sin(3 * ph) + .14 * np.sin(5 * ph) + .05 * np.sin(7 * ph)
    att = .25 if swell else .05
    e = np.clip(t / att, 0, 1) * np.clip((d - t) / .12, 0, 1)
    if swell: e *= .7 + .3 * np.sin(np.pi * t / d)
    return lp(s, 3200) * e * vel
music = np.zeros(N)
notes = [c for c in CO if not c['acc'] and c['t'] < END_T - .1]
for i, c in enumerate(notes):
    nxt = notes[i + 1]['t'] if i + 1 < len(notes) else END_T
    if BULB['t0'] - .1 < c['t'] < BULB['t1'] + .1: continue
    d = min(max(nxt - c['t'] + .12, .25), 1.4)            # 连奏：音符相互搭 0.12 秒
    add(music, reed(y2midi(c['y']), d, .8), c['t'], .16, f"note {y2midi(c['y'])} @corner")
SL = next(c for c in D['chapters'] if c['name'] == 'slopeL'); WL = next(c for c in D['chapters'] if c['name'] == 'wallL')
for tq in np.linspace(SL['t0'] + .6, WL['t1'] - 1.1, 6):          # 回程：音随笔尖下降
    yq = np.interp(tq, fr, np.array([f['y'] for f in TR])); add(music, reed(y2midi(yq), .9, .7), tq, .14, f'descent note {y2midi(yq)}')
add(music, reed(deg2midi(13), BULB['t1'] - BULB['t0'] + .1, 1, swell=True), BULB['t0'], .18, 'bulb: highest note, held')
add(music, reed(62, 1.4, .9), END_T - .9, .16, 'tonic D4 → silence')
gate = np.ones(N); gate[(ts > END_T + .45) & (ts < LIGHT_T)] = 0            # 真正的静音
fade = (ts > END_T + .25) & (ts <= END_T + .45); gate[fade] = 1 - (ts[fade] - END_T - .25) / .2
music *= gate
cues.append((END_T + .45, 'music silent (literal)'))
d = 3.0; t = tt(d); f = mtof(86)                         # 灯亮：一声钟片（唯一的第二音色）
chime = (np.sin(2*np.pi*f*t) + .4 * np.sin(2*np.pi*f*2.76*t) * np.exp(-t / .4)) * np.exp(-t / 1.1) * np.clip(t / .004, 0, 1)
add(music, chime, LIGHT_T, .22, 'light on: chime')
add(music, reed(62, 3.0, .8, swell=True), 26.9, .2, 'last low D under the title')
add(music, reed(69, 2.8, .7, swell=True), 27.15, .14)
add(music, reed(74, 2.4, .6, swell=True), 27.6, .1)

room = lp(rng.standard_normal(N), 900) * .004
room[(ts > END_T + .45) & (ts < LIGHT_T)] *= .15
L = music * .9 + sfx + room + pen * (1 - pan) * .5
R = music * .9 + sfx + room + pen * (1 + pan) * .5
st = np.stack([L, R], 1); st *= 10 ** (-3 / 20) / np.abs(st).max()
wavfile.write('audio.wav', SR, (st * 32767).astype(np.int16))
with open('cues.txt', 'w') as f:
    for t0, n in sorted(cues): f.write(f'{t0:7.3f}  {n}\n')
print('notes', len(notes), 'cues', len(cues))
