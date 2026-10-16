# -*- coding: utf-8 -*-
"""LinkedIn image for the site-launch post (1200x627) -> content/launch/linkedin/site.png"""
import os, asyncio
from playwright.async_api import async_playwright
ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
FONT = "file://" + os.path.join(ROOT, "wp", "silent-talk-theme", "assets", "fonts", "Vazirmatn.woff2")
HTML = f"""<!doctype html><meta charset=utf-8><style>
@font-face{{font-family:V;src:url('{FONT}');font-weight:100 900}}
*{{box-sizing:border-box;margin:0;padding:0}}
html,body{{width:1200px;height:627px;overflow:hidden;font-family:V,sans-serif;direction:rtl;color:#fff;background:radial-gradient(700px 500px at 85% 0,#2a3f6b,transparent 60%),#121B33}}
.t{{position:absolute;right:70px;top:80px;width:660px}}
.k{{display:inline-block;background:#E8431F;font-weight:800;font-size:24px;padding:5px 22px;border-radius:99px}}
h1{{font-size:54px;line-height:1.4;font-weight:900;margin:18px 0 14px}}h1 b{{color:#FF7A57}}
p{{font-size:30px;line-height:1.7;color:#cfd6ea}}
.u{{position:absolute;right:70px;bottom:48px;background:#E8431F;font-size:38px;font-weight:900;padding:12px 40px;border-radius:99px;direction:ltr;box-shadow:0 6px 0 #a82d10}}
.ph{{position:absolute;left:90px;top:48px;width:330px;height:640px;border-radius:44px;background:#0b1224;padding:12px;box-shadow:0 30px 80px rgba(0,0,0,.55),0 0 0 3px #2b3a5f}}
.ph div{{width:100%;height:100%;border-radius:34px;overflow:hidden}}.ph img{{width:100%;display:block}}
.g{{position:absolute;left:470px;top:95px;font-size:90px}}
</style>
<div class=t><span class=k>سایت جدید</span><h1>«گفتگوهای خاموش» <b>باز شد</b></h1><p>آزمون ۲ دقیقه‌ای، دورهٔ ۸ درسی، پروفایل یادگیری و وبلاگ؛ برای دیدن دقیق‌تر زبان بدن.</p></div>
<div class=u>silenttalk.ir</div>
<div class=ph><div><img src="file://{ROOT}/gen5/src/hero.png"></div></div>"""
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(); pg = await b.new_page(viewport=dict(width=1200, height=627))
        f = os.path.join(ROOT, "gen5", "src", "_li.html"); open(f, "w", encoding="utf-8").write(HTML)
        await pg.goto("file://" + f); await pg.wait_for_timeout(400)
        await pg.screenshot(path=os.path.join(ROOT, "content", "launch", "linkedin", "site.png")); await b.close()
asyncio.run(main())
