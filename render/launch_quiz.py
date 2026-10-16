# -*- coding: utf-8 -*-
"""اسلاید ۷ پست آزمون با آدرس سایت (به‌جای «لینک تو بیو»)."""
import base64, os
from playwright.sync_api import sync_playwright
R = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(R, ".."))
FONT = base64.b64encode(open(f"{ROOT}/wp/silent-talk-theme/assets/fonts/Vazirmatn.woff2", "rb").read()).decode()
IMG = "file:///home/claude/silent-talk/gen/host-portrait.png"
CSS = """@font-face{font-family:V;src:url(data:font/woff2;base64,%s);font-weight:100 900}
*{box-sizing:border-box;margin:0}body{width:1080px;height:1350px;background:#14213D;font-family:V;direction:rtl;color:#F5F0E6;position:relative;overflow:hidden}
.top{position:absolute;top:44px;left:60px;right:60px;display:flex;justify-content:space-between;font-size:26px;color:#C9CFDD;font-weight:600}
.dot{display:inline-block;width:14px;height:14px;border-radius:50%%;background:#F5832F;margin-left:10px}.o{color:#FF7A57}h2{font-weight:900;line-height:1.35}""" % FONT
html = f'''<html><head><meta charset="utf-8"><style>{CSS}</style></head><body>
<img src="{IMG}" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:50% 0">
<div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(20,33,61,.55) 0%,rgba(20,33,61,0) 14%,rgba(20,33,61,0) 40%,rgba(20,33,61,.94) 66%,rgba(20,33,61,.98) 100%)"></div>
<div class="top"><span><i class="dot"></i>گفتگوهای خاموش</span><span>7 / 7</span></div>
<div style="position:absolute;bottom:64px;left:60px;right:60px"><h2 style="font-size:66px;margin-bottom:20px;white-space:nowrap">فکر می‌کنی چقدر <span class="o">زبان بدن</span> بلدی؟</h2>
<div style="font-size:38px;line-height:1.7;margin-bottom:28px">آزمون ۲ دقیقه‌ای حالا روی سایت آمده: ۸ موقعیت واقعی، و آخرش می‌فهمی سطحت چیه.</div>
<div style="background:#E8431F;border-radius:60px;padding:24px;text-align:center;font-size:44px;font-weight:900;direction:ltr">silenttalk.ir/quiz</div>
<div style="text-align:center;margin-top:22px;font-size:32px;color:#C9CFDD">لینک را در استوری و بیو هم می‌بینی 👀</div></div></body></html>'''
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={"width":1080,"height":1350}); open("/tmp/lq.html","w",encoding="utf-8").write(html); pg.goto("file:///tmp/lq.html"); pg.wait_for_timeout(800)
    pg.screenshot(path=f"{ROOT}/content/launch/quiz/7.png"); b.close()
print("ok")
