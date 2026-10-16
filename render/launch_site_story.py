# -*- coding: utf-8 -*-
"""استوری معرفی سایت: ۴ فریم ۱۰۸۰×۱۹۲۰ -> content/launch/site-story/{1..4}.png"""
import os, asyncio
from playwright.async_api import async_playwright
ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
FONT = "file://" + os.path.join(ROOT, "wp", "silent-talk-theme", "assets", "fonts", "Vazirmatn.woff2")
OUT = os.path.join(ROOT, "content", "launch", "site-story"); os.makedirs(OUT, exist_ok=True)
G5 = "file://" + os.path.join(ROOT, "gen5")
CSS = """
@font-face{font-family:V;src:url('FONT');font-weight:100 900}
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:1080px;height:1920px;overflow:hidden;font-family:V,sans-serif;direction:rtl;color:#fff;
background:radial-gradient(900px 900px at 80% 8%,#2a3f6b 0,transparent 60%),radial-gradient(900px 900px at 10% 95%,#4a2a2a 0,transparent 55%),#121B33}
.o{color:#FF7A57}.y{color:#FFD84D}
.top{position:absolute;top:210px;left:70px;right:70px;text-align:center;font-size:84px;font-weight:900;line-height:1.35}
.sub{position:absolute;left:80px;right:80px;text-align:center;font-size:44px;color:#cfd6ea;line-height:1.7}
.pill{position:absolute;left:50%;transform:translateX(-50%);background:#E8431F;color:#fff;font-size:70px;font-weight:900;padding:26px 66px;border-radius:99px;direction:ltr;box-shadow:0 10px 0 #a82d10;white-space:nowrap}
.sc{position:absolute;left:50%;transform:translateX(-50%) scale(.82);transform-origin:top center;width:1080px;height:1920px;overflow:hidden}
.sc img{width:1080px;height:1920px;display:block}
.safe{position:absolute;bottom:0;left:0;right:0;height:250px}
"""
def page(body): return f"<!doctype html><meta charset=utf-8><style>{CSS.replace('FONT',FONT)}</style>{body}"
FR = {}
FR[1] = f"""<div class='top' style='top:150px;font-size:76px'>سایت <span class='o'>گفتگوهای خاموش</span><br>باز شد!</div>
<div style='position:absolute;left:0;top:470px;width:1080px;height:980px;overflow:hidden'><img src='{G5}/site-hero.png' style='width:1080px;margin-top:-100px'></div>
<div class='pill' style='top:1490px'>silenttalk.ir</div>
<div class='sub' style='top:1640px;font-size:38px'>آزمون ۲ دقیقه‌ای · دورهٔ ۸ درسی · وبلاگ</div>"""
FR[2] = f"""<div style='position:absolute;inset:0'><img src='{G5}/site-gifts.png' style='width:1080px;height:1920px;transform:translateY(110px)'></div>
<div class='sub' style='top:1170px;font-size:46px;color:#fff'>ثبت‌نام در سایت، رایگان است</div>
<div class='pill' style='top:1310px'>silenttalk.ir</div>"""
FR[3] = f"""<div class='top' style='top:240px'>۲۰ نفر اول که<br>در سایت <span class='y'>ثبت‌نام</span> کنند</div>
<div style='position:absolute;left:110px;right:110px;top:640px;background:linear-gradient(135deg,#E8431F,#ff7a57);border-radius:72px;padding:90px 60px;text-align:center;box-shadow:0 30px 90px rgba(0,0,0,.5)'>
<div style='font-size:190px;line-height:1'>📖</div><div style='font-size:78px;font-weight:900;margin-top:30px;line-height:1.4'>نسخهٔ چاپی کتاب<br>«درک زبان بدن»</div><div style='font-size:52px;margin-top:20px'>هدیه از طرف ما</div></div>
<div class='pill' style='top:1480px'>silenttalk.ir</div>"""
FR[4] = f"""<div class='top' style='top:200px'>دو هدیهٔ <span class='y'>دیگر</span></div>
<div style='position:absolute;left:90px;right:90px;top:380px;display:flex;flex-direction:column;gap:34px'>
<div style='background:rgba(255,255,255,.08);border:2px solid rgba(255,255,255,.2);border-radius:56px;padding:44px;text-align:center'>
<div style='font-size:100px'>🎓</div><div style='font-size:62px;font-weight:900;line-height:1.5'>کتاب را در <span class='o'>طاقچه</span> خوانده‌ای؟</div>
<div style='font-size:44px;color:#cfd6ea;margin-top:14px;line-height:1.7'>کل دوره برات رایگان می‌شود<br>و نسخهٔ چاپی هم هدیه می‌گیری</div></div>
<div style='background:rgba(255,255,255,.08);border:2px solid rgba(255,255,255,.2);border-radius:56px;padding:44px;text-align:center'>
<div style='font-size:100px'>🎁</div><div style='font-size:62px;font-weight:900;line-height:1.5'>فالوئرهای <span class='o'>اینستاگرام و لینکدین</span></div>
<div style='font-size:44px;color:#cfd6ea;margin-top:14px;line-height:1.7'>برای شرکت در قرعه‌کشی نسخهٔ چاپی،<br>زیر همین پست/استوری عدد <b class='y'>۷</b> را بفرست<br>(جزئیات قرعه‌کشی را اعلام می‌کنیم)</div></div></div>
<div class='pill' style='top:1600px'>silenttalk.ir</div>"""
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(); pg = await b.new_page(viewport=dict(width=1080, height=1920))
        for k, body in FR.items():
            f = os.path.join(ROOT, "gen5", "src", f"_story{k}.html"); open(f, "w", encoding="utf-8").write(page(body))
            await pg.goto("file://" + f); await pg.wait_for_timeout(500)
            await pg.screenshot(path=os.path.join(OUT, f"{k}.png")); print("ok", k)
        await b.close()
asyncio.run(main())
