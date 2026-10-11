# -*- coding: utf-8 -*-
"""موتور عمومی ساخت ریل عمودی ۱۰۸۰×۱۹۲۰ از چند تصویر.

هر ریل با یک «spec» توصیف می‌شود (نمونه در reel_w1_*.py):
  shots:  [{img, t0, t1, cam:(cx0,cy0,z0, cx1,cy1,z1), rings:[(nx,ny,t_start,t_end,(r,g,b),R)], morph_to:img2?}]
  texts:  [(id, html, start, end)]
  end_at: زمان شروع کادر آخر (جلد کتاب)
  whooshes, dings: زمان‌های افکت صوتی
مختصات rings نسبت به خود تصویر (۰ تا ۱) است.
"""
import os, sys, math, subprocess, random, wave
import numpy as np
from PIL import Image, ImageDraw, ImageFilter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_v2 as B

ROOT = os.path.abspath(os.path.join(B.ROOT, ".."))
W, H, FPS = 1080, 1920, 30
CSS = B.CSS.replace("height:1350px", "height:1920px") + "html,body{background:transparent!important}"
COVER = B.COVER[7:]


def hi(t):
    p = t.split("*")
    return "".join(f'<span style="color:#ffd84d">{x}</span>' if i % 2 else x for i, x in enumerate(p))


def block(t, size=78, top=1200, sub=None, subsize=46):
    s = f'<div style="margin-top:26px;font-size:{subsize}px;font-weight:600;color:#f1e9d8">{hi(sub)}</div>' if sub else ''
    return (f'<html><head><meta charset="utf-8"><style>{CSS}</style></head><body><div style="position:absolute;left:60px;right:60px;'
            f'top:{top}px;text-align:center;font-size:{size}px;font-weight:900;line-height:1.5;text-shadow:0 4px 20px rgba(0,0,0,.9)">{hi(t)}{s}</div></body></html>')


def end_card(line1="این درس‌ها از کتاب <span class=\"o\">درک زبان بدن</span> است", line2="کتاب را در طاقچه ببین · لینک در بیو"):
    return (f'<html><head><meta charset="utf-8"><style>{CSS}</style></head><body><div style="position:absolute;inset:0;background:radial-gradient(circle at 50% 30%,#22376b,#131f3d 70%)"></div>'
            f'<div style="position:absolute;top:220px;left:50%;margin-left:-250px;width:500px;transform:rotate(-3deg);border-radius:12px;overflow:hidden;box-shadow:0 30px 70px rgba(0,0,0,.6),0 0 0 6px #fff"><img src="{COVER}" style="width:100%;display:block"></div>'
            f'<div style="position:absolute;top:1050px;right:60px;left:60px;text-align:center"><div style="font-size:62px;font-weight:900;margin-bottom:34px;line-height:1.5">{line1}</div>'
            f'<div style="background:#e8431f;border-radius:60px;padding:24px;font-size:46px;font-weight:900">{line2}</div>'
            f'<div style="margin-top:30px;font-size:36px;color:#c4cbdc">گفتگوهای خاموش · @silenttalk.ir</div></div></body></html>')


def render_texts(spec):
    from playwright.sync_api import sync_playwright
    out = spec["out"]; os.makedirs(out, exist_ok=True)
    with sync_playwright() as p:
        br = p.chromium.launch(); pg = br.new_page(viewport={"width": W, "height": H})
        for k, h, a, b in spec["texts"]:
            open("/tmp/_te.html", "w").write(h); pg.goto("file:///tmp/_te.html"); pg.wait_for_timeout(300)
            pg.screenshot(path=f"{out}/{k}.png", omit_background=True)
        open("/tmp/_te.html", "w").write(spec.get("end_html") or end_card()); pg.goto("file:///tmp/_te.html"); pg.wait_for_timeout(300)
        pg.screenshot(path=f"{out}/end.png"); br.close()


def load(path):
    im = Image.open(path).convert("RGB")
    return im.resize((im.size[0] * 2, im.size[1] * 2), Image.LANCZOS)


def ease(u):
    u = min(max(u, 0), 1); return u * u * (3 - 2 * u)


def lerp(a, b, u): return a + (b - a) * u


def cam(im, cx, cy, z, t, sway=1.0):
    iw, ih = im.size
    vw = iw / z; vh = vw * 16 / 9
    if vh > ih:
        vh = ih / z if z > 1 else ih; vw = vh * 9 / 16
    x0 = cx * iw - vw / 2 + sway * 7 * math.sin(t * 0.9) * iw / 1080 / z
    y0 = cy * ih - vh / 2 + sway * 6 * math.sin(t * 1.3 + 1) * ih / 1920 / z
    x0 = min(max(0, x0), iw - vw); y0 = min(max(0, y0), ih - vh)
    return im.resize((W, H), Image.BICUBIC, box=(x0, y0, x0 + vw, y0 + vh)), (x0, y0, vw, vh)


def to_screen(nx, ny, box, size):
    x0, y0, vw, vh = box; iw, ih = size
    return ((nx * iw - x0) / vw * W, (ny * ih - y0) / vh * H)


def shot_frame(sh, imgs, t):
    """تصویر و کادر دوربین برای یک نما در لحظهٔ t."""
    u = ease((t - sh["t0"]) / max(0.01, sh["t1"] - sh["t0"]))
    c = sh["cam"]
    cx, cy, z = lerp(c[0], c[3], u), lerp(c[1], c[4], u), lerp(c[2], c[5], u)
    base = imgs[sh["img"]]
    img, box = cam(base, cx, cy, z, t)
    if sh.get("morph_to"):
        a, b = sh["morph"]
        k = ease((t - a) / (b - a))
        if k > 0:
            img2, _ = cam(imgs[sh["morph_to"]], cx, cy, z, t)
            img = Image.blend(img, img2, k)
    return img, box, base.size


def make_music(path, D, bpm=92, chords=None, whooshes=(), dings=(), seed=1):
    SR = 44100; n = int(SR * D); L = np.zeros(n); R = np.zeros(n)
    np.random.seed(seed)

    def note(f, t0, dur, amp, pan=0.5, tone=1.0):
        i0 = int(t0 * SR)
        if i0 >= n: return
        m = min(int(dur * SR), n - i0); t = np.arange(m) / SR
        w = np.sin(2 * np.pi * f * t) + 0.35 * tone * np.sin(2 * np.pi * 2 * f * t) + 0.12 * np.sin(2 * np.pi * 3 * f * t)
        s = w * np.exp(-t * 2.6) * (1 - np.exp(-t * 60)) * amp
        L[i0:i0 + m] += s * (1 - pan); R[i0:i0 + m] += s * pan

    def pad(f, t0, dur, amp):
        i0 = int(t0 * SR); m = min(int(dur * SR), n - i0)
        if m <= 0: return
        t = np.arange(m) / SR
        env = np.minimum(1, t / 1.2) * np.minimum(1, (dur - t) / 1.2).clip(0)
        s = (np.sin(2 * np.pi * f * t) + np.sin(2 * np.pi * f * 1.004 * t)) * 0.5 * env * amp
        L[i0:i0 + m] += s; R[i0:i0 + m] += s
    mid = lambda m: 440 * 2 ** ((m - 69) / 12)
    beat = 60 / bpm
    chords = chords or [(57, [57, 60, 64]), (53, [53, 57, 60]), (48, [48, 52, 55]), (55, [55, 59, 62])]
    for b in range(int(D / (beat * 4)) + 1):
        root, tri = chords[b % len(chords)]; t0 = b * beat * 4
        pad(mid(root - 12), t0, beat * 4 + 0.5, 0.05)
        for k in range(8):
            note(mid(tri[[0, 1, 2, 1, 0, 1, 2, 1][k]] + 12), t0 + k * beat / 2, 1.1, 0.10, pan=0.35 + 0.3 * (k % 2))
        if b % 2 == 0: note(mid(tri[0] + 24), t0 + beat * 2, 1.6, 0.05, 0.7)
    for w0 in whooshes:
        i0 = int(w0 * SR); m = int(1.2 * SR)
        if i0 + m > n: continue
        t = np.arange(m) / SR; nz = np.random.randn(m) * np.sin(np.pi * t / 1.2) ** 2 * 0.07
        k = int(0.004 * SR); nz = np.convolve(nz, np.ones(k) / k, 'same'); L[i0:i0 + m] += nz; R[i0:i0 + m] += nz
    for tt in dings: note(1318.5, tt, 1.4, 0.07, 0.5, 0.6)

    def echo(x, dl, g):
        y = x.copy(); d = int(dl * SR); y[d:] += x[:-d] * g; return y
    L = echo(L, 0.28, 0.35); R = echo(R, 0.37, 0.35)
    fade = np.ones(n); fade[:int(.5 * SR)] = np.linspace(0, 1, int(.5 * SR)); fade[-int(1.5 * SR):] = np.linspace(1, 0, int(1.5 * SR))
    st = np.stack([L * fade, R * fade], 1); st /= np.abs(st).max() / 0.8
    with wave.open(path, 'wb') as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes((st * 32767).astype(np.int16).tobytes())


def run(spec):
    out = spec["out"]; D = spec["dur"]; G = spec["gen"]
    imgs = {k: load(os.path.join(G, v)) for k, v in spec["images"].items()}
    end = Image.open(f"{out}/end.png").convert("RGB")
    tx = {k: (Image.open(f"{out}/{k}.png").convert("RGBA"), a, b) for k, h, a, b in spec["texts"]}
    yy, xx = np.mgrid[0:H, 0:W]
    vig = 1 - 0.38 * np.clip(((xx - W / 2) / (W / 2)) ** 2 + ((yy - H / 2) / (H / 2)) ** 2 - 0.35, 0, 1)
    grad = 1 - 0.62 * np.clip((yy - 950) / 700, 0, 1)
    shade = (vig * grad)[..., None].astype(np.float32)
    random.seed(spec.get("seed", 4))
    parts = [(random.random() * W, random.random() * H, random.uniform(1.5, 4.5), random.uniform(20, 60), random.random() * 6.28) for _ in range(45)]
    silent = f"{out}/silent.mp4"
    DBG = [float(x) for x in os.environ.get("ST_FRAMES", "").split(",") if x]
    class _Null:
        def write(self, b): pass
        def close(self): pass
    ff = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
                           "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-pix_fmt", "yuv420p", silent], stdin=subprocess.PIPE)
    shots = spec["shots"]; E = spec["end_at"]
    frames = [int(x * FPS) for x in DBG] if DBG else range(int(D * FPS))
    for f in frames:
        t = f / FPS
        if t < E:
            cur = next((s for s in shots if s["t0"] <= t < s["t1"]), shots[-1])
            idx = shots.index(cur)
            img, box, size = shot_frame(cur, imgs, t)
            # برش متقاطع از نمای قبلی
            xf = cur.get("xfade", 0.5)
            if idx > 0 and t < cur["t0"] + xf:
                prev = shots[idx - 1]
                pimg, _, _ = shot_frame(prev, imgs, min(t, prev["t1"]))
                img = Image.blend(pimg, img, ease((t - cur["t0"]) / xf))
            arr = np.asarray(img, dtype=np.float32) * shade
            arr = arr * (1 + 0.035 * math.sin(2 * math.pi * t / 2.3) + 0.015 * math.sin(2 * math.pi * t / 0.9))
            for (a, b) in spec.get("flashes", []):
                if a < t < b: arr = arr + 28 * math.sin((t - a) / (b - a) * math.pi)
            fr = Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8)).convert("RGBA")
            ov = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(ov)
            for (px, py, r, sp, ph) in parts:
                y = (py - sp * t) % H; x = (px + 25 * math.sin(t * 0.6 + ph)) % W
                d.ellipse((x - r, y - r, x + r, y + r), fill=(255, 236, 200, max(0, int(70 + 50 * math.sin(t * 1.7 + ph)))))
            for (nx, ny, a, b, col, R) in cur.get("rings", []):
                if a <= t <= b:
                    k = (t - a) / (b - a); al = int(255 * min(1, k * 6, (1 - k) * 4)); r = R * (1 + 0.08 * math.sin((t - a) * 7))
                    cx, cy = to_screen(nx, ny, box, size)
                    for w in range(7): d.ellipse((cx - r - w, cy - r - w, cx + r + w, cy + r + w), outline=tuple(col) + (max(0, al - w * 10),))
            ov = ov.filter(ImageFilter.GaussianBlur(1.2)); fr.alpha_composite(ov)
            for k, (im_, a, b) in tx.items():
                if a <= t <= b:
                    fi = ease((t - a) / 0.45); al = min(fi, ease((b - t) / 0.35))
                    if al > 0:
                        lay = im_.copy(); lay.putalpha(lay.getchannel("A").point(lambda v: int(v * al)))
                        fr.alpha_composite(lay, (0, int(40 * (1 - fi))))
            frame = fr.convert("RGB")
        else:
            u = (t - E) / (D - E); z = 1 + 0.05 * u; ew, eh = int(W * z), int(H * z)
            e = end.resize((ew, eh), Image.LANCZOS).crop(((ew - W) // 2, (eh - H) // 2, (ew - W) // 2 + W, (eh - H) // 2 + H))
            last = shots[-1]; prev, _, _ = shot_frame(last, imgs, min(E - 0.01, last["t1"]))
            frame = Image.blend(prev, e, ease((t - E) / 0.6))
        if DBG: frame.resize((540, 960)).save(f"{out}/dbg_{t:.1f}.png")
        else: ff.stdin.write(np.asarray(frame).tobytes())
    ff.stdin.close(); ff.wait()
    if DBG: return "debug frames"
    wav = f"{out}/music.wav"
    make_music(wav, D, whooshes=spec.get("whooshes", ()), dings=spec.get("dings", ()), seed=spec.get("seed", 1), bpm=spec.get("bpm", 92))
    final = f"{out}/{spec['name']}.mp4"
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", silent, "-i", wav, "-map", "0:v", "-map", "1:a", "-c:v", "copy", "-c:a", "aac", "-b:a", "160k", "-shortest", final], check=True)
    return final


def main(spec):
    if len(sys.argv) > 1 and sys.argv[1] == "texts": render_texts(spec)
    else: print(run(spec))
