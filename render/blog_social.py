# -*- coding: utf-8 -*-
"""Instagram carousels (3 slides, 1080x1350) + captions from the blog articles -> content/blog/<slug>/"""
import os, asyncio, html
from playwright.async_api import async_playwright
from PIL import Image
from blog_articles import ARTICLES
ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
FONT = "file://" + os.path.join(ROOT, "wp", "silent-talk-theme", "assets", "fonts", "Vazirmatn.woff2")
TMP = os.path.join(ROOT, "gen5", "src")
BASE = f"""@font-face{{font-family:V;src:url('{FONT}');font-weight:100 900}}
*{{box-sizing:border-box;margin:0;padding:0}}html,body{{width:1080px;height:1350px;overflow:hidden;font-family:V,sans-serif;direction:rtl;color:#fff;background:#14213D}}
.o{{color:#FF7A57}}.pill{{position:absolute;left:50%;transform:translateX(-50%);background:#E8431F;color:#fff;font-weight:900;border-radius:99px;direction:ltr;box-shadow:0 8px 0 #a82d10;white-space:nowrap}}"""
TAGS = {"محل کار": "#جلسه_کاری #محیط_کار", "چهره": "#لبخند #زبان_بدن_چهره", "مصاحبه": "#مصاحبه_شغلی #استخدام", "مهارت پایه": "#خط_پایه #تفسیر_رفتار",
        "دست‌ها و بازوها": "#دست_به_سینه #حرکات_دست", "افسانه‌ها": "#مهربیان #افسانه_زبان_بدن", "دروغ و صداقت": "#تشخیص_دروغ #صداقت", "فضا و فاصله": "#فضای_شخصی #پروکسمیکس"}
COMMON = "#زبان_بدن #ارتباط_غیرکلامی #گفتگوهای_خاموش #سایلنت_تاک #مهارت_ارتباطی #روانشناسی_کاربردی #درک_زبان_بدن"

def slide1(a):
    im = Image.open(os.path.join(ROOT, a["cover_src"])).convert("RGB"); w, h = im.size
    th = int(w * 1350 / 1080)
    if th <= h: y = int(a["cover_y"] * (h - th)); im = im.crop((0, y, w, y + th))
    else: nw = int(h * 1080 / 1350); im = im.crop(((w - nw) // 2, 0, (w - nw) // 2 + nw, h))
    im = im.resize((1080, 1350), Image.LANCZOS); p = os.path.join(TMP, f"_s1_{a['slug']}.jpg"); im.save(p, quality=92)
    return f"""<style>{BASE}
.bg{{position:absolute;inset:0;background:url('file://{p}') center/cover}}.bg:after{{content:'';position:absolute;inset:0;background:linear-gradient(180deg,rgba(20,33,61,.15) 30%,rgba(20,33,61,.93) 72%)}}
.c{{position:absolute;left:0;right:0;bottom:0;padding:0 80px 150px}}.cat{{display:inline-block;background:#E8431F;font-weight:800;font-size:34px;padding:6px 30px;border-radius:99px}}
h1{{font-size:72px;line-height:1.45;font-weight:900;margin-top:24px}}.sw{{position:absolute;left:80px;bottom:60px;font-size:34px;opacity:.9}}</style>
<div class=bg></div><div class=c><span class=cat>{html.escape(a['cat'])}</span><h1>{html.escape(a['title'])}</h1></div><div class=sw>بکش و بخوان ◀</div>"""

def slide2(a):
    n = len(a["points"]); fs = 44 if n <= 5 else 38
    li = "".join(f"<li><b>{'۰۱۲۳۴۵۶۷۸۹'[i+1]}</b><span>{html.escape(t)}</span></li>" for i, t in enumerate(a["points"]))
    return f"""<style>{BASE}
html,body{{background:#F6F1E7;color:#14213D}}.w{{padding:90px 70px}}.k{{font-size:34px;font-weight:800;color:#E8431F}}h2{{font-size:78px;font-weight:900;line-height:1.35;margin:8px 0 40px}}
ul{{list-style:none;display:flex;flex-direction:column;gap:20px}}li{{display:flex;align-items:center;gap:26px;background:#fff;border-radius:34px;padding:22px 34px;box-shadow:0 8px 0 #e2d8c3;font-size:{fs}px;font-weight:700;line-height:1.5}}
li b{{flex:none;width:74px;height:74px;border-radius:50%;background:#14213D;color:#fff;display:flex;align-items:center;justify-content:center;font-size:40px}}
.f{{position:absolute;left:70px;right:70px;bottom:60px;display:flex;justify-content:space-between;font-size:30px;font-weight:700}}.f span{{direction:ltr;color:#E8431F}}</style>
<div class=w><div class=k>خلاصهٔ مقاله</div><h2>{html.escape(a['info_title'])}</h2><ul>{li}</ul></div><div class=f><div>● گفتگوهای خاموش</div><span>silenttalk.ir/blog</span></div>"""

def slide3(a):
    return f"""<style>{BASE}
html,body{{background:radial-gradient(900px 800px at 80% 5%,#2a3f6b,transparent 60%),radial-gradient(900px 800px at 10% 95%,#4a2a2a,transparent 55%),#14213D}}
.c{{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;gap:42px;padding:0 90px}}
h2{{font-size:88px;line-height:1.4;font-weight:900}}p{{font-size:46px;line-height:1.7;color:#cfd6ea}}.pill{{position:static;transform:none;font-size:62px;padding:24px 60px}}</style>
<div class=c><h2>مقالهٔ کامل را <span class=o>بخوان</span></h2><p>مثال‌های بیشتر و قدم‌های عملی در وبلاگ سایت<br>سطح خودت را هم با آزمون ۲ دقیقه‌ای ببین</p><div class=pill>silenttalk.ir/blog</div><p style="font-size:38px">ذخیره کن و برای کسی بفرست که به این موضوع علاقه دارد 🔖</p></div>"""

def caption(a):
    bl = "\n".join(f"▪️ {t}" for t in a["points"][:5])
    return (f"{a['title']}\n\n{a['excerpt']}\n\nخلاصه:\n{bl}\n\n📝 مقالهٔ کامل: silenttalk.ir/blog\n"
            f"🧠 آزمون ۲ دقیقه‌ای: silenttalk.ir/quiz\n\n{TAGS.get(a['cat'], '')} {COMMON}\n")

async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(); pg = await b.new_page(viewport=dict(width=1080, height=1350))
        for a in ARTICLES:
            out = os.path.join(ROOT, "content", "blog", a["slug"]); os.makedirs(out, exist_ok=True)
            for i, fn in enumerate((slide1, slide2, slide3), 1):
                f = os.path.join(TMP, f"_b{i}_{a['slug']}.html"); open(f, "w", encoding="utf-8").write(f"<!doctype html><meta charset=utf-8>{fn(a)}")
                await pg.goto("file://" + f); await pg.wait_for_timeout(300); await pg.screenshot(path=os.path.join(out, f"{i}.png"))
            open(os.path.join(out, "caption.txt"), "w", encoding="utf-8").write(caption(a)); print("ok", a["slug"])
        await b.close()
asyncio.run(main())
