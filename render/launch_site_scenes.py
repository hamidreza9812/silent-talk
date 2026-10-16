# -*- coding: utf-8 -*-
"""Scenes (1080x1920) for the site-intro reel + story: real site screenshots in a phone frame, plus designed cards.
Run: python3 launch_site_scenes.py  -> gen5/site-*.png"""
import os, asyncio
from playwright.async_api import async_playwright

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
SRC = os.path.join(ROOT, "gen5", "src")
OUT = os.path.join(ROOT, "gen5")
FONT = "file://" + os.path.join(ROOT, "wp", "silent-talk-theme", "assets", "fonts", "Vazirmatn.woff2")

BASE = """
@font-face{font-family:V;src:url('%s');font-weight:100 900}
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:1080px;height:1920px;overflow:hidden;font-family:V,sans-serif;direction:rtl;color:#fff;
background:radial-gradient(900px 900px at 80% 8%,#2a3f6b 0,transparent 60%),radial-gradient(900px 900px at 10% 95%,#4a2a2a 0,transparent 55%),#121B33}
.o{color:#FF7A57}.y{color:#FFD84D}
.phone{position:absolute;left:150px;top:130px;width:780px;height:1090px;border-radius:64px;background:#0b1224;padding:18px;
box-shadow:0 40px 120px rgba(0,0,0,.55),0 0 0 3px #2b3a5f}
.phone .scr{width:100%%;height:100%%;border-radius:48px;overflow:hidden;background:#fff}
.phone img{width:100%%;display:block}
.tag{position:absolute;right:90px;top:1245px;background:#E8431F;color:#fff;font-weight:800;font-size:38px;padding:12px 34px;border-radius:99px}
"""

def phone(img, shift=0):
    return (f"<div class='phone'><div class='scr'><img src='file://{SRC}/{img}' style='margin-top:-{shift}px'></div></div>")

SCENES = {}
SCENES["hero"] = phone("hero.png")
SCENES["path"] = phone("path.png")
SCENES["pro"] = phone("pro.png")
SCENES["course"] = phone("course.png", 190)

# designed cards -------------------------------------------------------
SCENES["profile"] = """
<style>
.card{position:absolute;left:110px;top:200px;width:860px;background:#F6F1E7;border-radius:56px;padding:56px;color:#121B33;box-shadow:0 40px 120px rgba(0,0,0,.5)}
.hi{display:flex;justify-content:space-between;align-items:center}
.hi b{font-size:56px;font-weight:900}.av{width:120px;height:120px;border-radius:50%;background:#121B33;color:#fff;font-size:56px;display:flex;align-items:center;justify-content:center;font-weight:800}
.badge{display:inline-block;background:#2E7D5B;color:#fff;border-radius:99px;font-size:30px;padding:8px 26px;margin-top:14px;font-weight:700}
.row{background:#fff;border-radius:36px;padding:38px;margin-top:34px;box-shadow:0 8px 0 #e4dccb}
.row h4{font-size:40px;font-weight:900;margin-bottom:8px}.row p{font-size:32px;color:#58607a;line-height:1.7}
.bar{height:26px;border-radius:99px;background:#e9e1d0;margin-top:22px;overflow:hidden;direction:rtl}.bar i{display:block;height:100%;width:38%;background:#E8431F;border-radius:99px}
.lv{display:flex;gap:14px;margin-top:20px}.lv span{flex:1;text-align:center;border-radius:99px;padding:12px 0;font-size:30px;font-weight:800;background:#efe7d6;color:#8a8369}.lv span.on{background:#121B33;color:#fff}
</style>
<div class='card'>
 <div class='hi'><div><b>سلام 👋</b><br><span class='badge'>✅ خریدار کتاب · همهٔ دوره برات بازه</span></div><div class='av'>س</div></div>
 <div class='row'><h4>سطح درک زبان بدنت</h4><p>بعد از آزمون، سطحت اینجا ثبت می‌شود.</p>
  <div class='lv'><span>مبتدی</span><span class='on'>میانی</span><span>پیشرفته</span></div></div>
 <div class='row'><h4>پیشرفت دوره</h4><p>۳ از ۸ درس</p><div class='bar'><i></i></div></div>
 <div class='row'><h4>درس بعدی</h4><p>چهره و لبخند: لبخند مودبانه با لبخند واقعی چه فرقی دارد؟</p></div>
</div>"""

SCENES["gifts"] = """
<style>
.g{position:absolute;left:90px;right:90px;top:150px;display:flex;flex-direction:column;gap:34px}
.gi{background:rgba(255,255,255,.07);border:2px solid rgba(255,255,255,.18);border-radius:48px;padding:46px;display:flex;gap:34px;align-items:center}
.gi .em{font-size:110px;line-height:1;flex:none}
.gi h3{font-size:54px;font-weight:900;line-height:1.35}.gi p{font-size:36px;color:#cfd6ea;margin-top:10px;line-height:1.6}
.gi.big{background:linear-gradient(135deg,#E8431F,#ff7a57);border:none}.gi.big p{color:#fff}
.hd{font-size:92px;font-weight:900;line-height:1.25;margin-bottom:12px}
</style>
<div class='g'>
 <div class='hd'>سه <span class='y'>هدیه</span> برای شروع</div>
 <div class='gi big'><div class='em'>📖</div><div><h3>۲۰ نفر اول که ثبت‌نام کنند</h3><p>نسخهٔ چاپی کتاب رایگان</p></div></div>
 <div class='gi'><div class='em'>🎓</div><div><h3>کتاب را در طاقچه خوانده‌ای؟</h3><p>کل دوره برات رایگان + نسخهٔ چاپی هدیه</p></div></div>
 <div class='gi'><div class='em'>🎁</div><div><h3>فالوئرهای اینستاگرام و لینکدین</h3><p>قرعه‌کشی نسخهٔ چاپی · کامنت کن «۷»</p></div></div>
</div>"""

SCENES["blog"] = """
<style>
.b{position:absolute;left:90px;right:90px;top:150px;display:flex;flex-direction:column;gap:30px}
.hd{font-size:92px;font-weight:900;line-height:1.25;margin-bottom:8px}
.bp{background:#F6F1E7;color:#121B33;border-radius:44px;padding:40px 46px;box-shadow:0 8px 0 #cfc6b2}
.bp small{font-size:28px;color:#E8431F;font-weight:800}.bp h3{font-size:50px;font-weight:900;line-height:1.4;margin-top:6px}
</style>
<div class='b'>
 <div class='hd'>وبلاگ <span class='o'>گفتگوهای خاموش</span></div>
 <div class='bp'><small>محل کار</small><h3>زبان بدن در جلسه‌های کاری: ۷ نشانه‌ای که باید دید</h3></div>
 <div class='bp'><small>چهره</small><h3>لبخند واقعی یا مؤدبانه؟ راهنمای دیدن فرق</h3></div>
 <div class='bp'><small>مصاحبه</small><h3>زبان بدن در مصاحبهٔ شغلی: از ورود تا دست دادن</h3></div>
 <div class='bp'><small>دست‌ها و بازوها</small><h3>دست‌به‌سینه یعنی چه؟ همیشه «بسته» نیست</h3></div>
</div>"""

SCENES["url"] = """
<style>
.u{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:50px;text-align:center}
.pill{background:#E8431F;color:#fff;font-size:92px;font-weight:900;padding:34px 80px;border-radius:99px;direction:ltr;box-shadow:0 12px 0 #a82d10}
.hd{font-size:100px;font-weight:900;line-height:1.3}.sub{font-size:48px;color:#cfd6ea;line-height:1.7}
</style>
<div class='u'><div class='hd'>همین حالا <span class='o'>شروع کن</span></div><div class='pill'>silenttalk.ir</div><div class='sub'>آزمون ۲ دقیقه‌ای · دورهٔ ۸ درسی · وبلاگ<br>ثبت‌نام رایگان</div></div>"""

async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport=dict(width=1080, height=1920))
        for k, html in SCENES.items():
            f = os.path.join(OUT, "src", f"_{k}.html")
            open(f, "w", encoding="utf-8").write(f"<!doctype html><meta charset=utf-8><style>{BASE.replace('%s',FONT).replace('%%','%')}</style>{html}")
            await pg.goto("file://" + f)
            await pg.wait_for_timeout(500)
            await pg.screenshot(path=os.path.join(OUT, f"site-{k}.png"))
            print("ok", k)
        await b.close()

asyncio.run(main())
