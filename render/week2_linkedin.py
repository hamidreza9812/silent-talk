# -*- coding: utf-8 -*-
"""سه پست لینکدین هفتهٔ دوم: کارت ۱۲۰۰×۶۲۷ و متن. اجرا: python3 week2_linkedin.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_v2 as B
from playwright.sync_api import sync_playwright

GEN = os.path.abspath(os.path.join(B.ROOT, "..", "gen4"))
OUT = os.path.abspath(os.path.join(B.ROOT, "..", "content", "week2", "linkedin"))
FONTS = "".join(f"@font-face{{font-family:S;font-weight:{w};src:url(data:font/ttf;base64,{d})}}" for w, d in B.F.items())
CSS = FONTS + """
*{box-sizing:border-box;margin:0}body{width:1200px;height:627px;background:#131f3d;font-family:S;direction:rtl;color:#f6f1ea;position:relative;overflow:hidden}
.img{position:absolute;left:0;top:0;bottom:0;width:470px;overflow:hidden}.img img{width:100%;height:100%;object-fit:cover;display:block}
.fade{position:absolute;left:300px;top:0;bottom:0;width:170px;background:linear-gradient(90deg,rgba(19,31,61,0),#131f3d)}
.t{position:absolute;right:64px;left:520px;top:0;bottom:0;display:flex;flex-direction:column;justify-content:center;gap:22px}
.k{display:inline-block;align-self:flex-start;background:#e8431f;border-radius:30px;padding:4px 22px 8px;font-size:26px;font-weight:700}
h1{font-size:60px;font-weight:900;line-height:1.55}h1 b{color:#ff7a54}
.brand{position:absolute;right:64px;bottom:34px;font-size:24px;color:#c4cbdc;font-weight:700}
"""
POSTS = [
 dict(id="li07-feet", img="cafe-feet.png", pos="50% 60%", kicker="فروش و مذاکره",
  title="بدن <b>پیش از حرف‌ها</b> می‌رود",
  text=("در یک جلسهٔ فروش، مشتری سر تکان می‌داد و می‌گفت «جالب است». اما نوک پاهایش به سمت در بود.\n\n"
        "یعنی علاقه ندارد؟ شاید. شاید هم ده دقیقهٔ دیگر جلسهٔ دیگری دارد. جهت پاها یک سرنخ است، نه یک حکم.\n\n"
        "نکتهٔ کاربردی: به‌جای نتیجه‌گیری، به او راه خروج آبرومندانه بدهید: «اگر وقتتان محدود است، کوتاهش کنیم یا زمان دیگری صحبت کنیم.» این جمله فشار را کم می‌کند و معمولاً اعتماد را بیشتر می‌کند.\n\n"
        "شما در جلسه‌ها به کدام نشانه بیشتر توجه می‌کنید؟ تجربه‌تان را در کامنت بنویسید.\n\n"
        "نسخهٔ الکترونیک کتاب «درک زبان بدن» در طاقچه: https://taaghche.com/book/337335\n\n"
        "#فروش #مذاکره #زبان_بدن #مهارت_ارتباطی #ارتباط_مؤثر")),
 dict(id="li08-yawn", img="dinner-yawn.png", pos="50% 30%", kicker="مدیریت و جلسه",
  title="خمیازه، <b>یعنی بی‌حوصلگی؟</b>", raw="position:absolute;left:0;top:-150px;width:900px;height:1599px;max-width:none;transform:scaleX(-1)",
  text=("ساعت چهار بعدازظهر است و یکی از همکاران وسط ارائه خمیازه می‌کشد. اولین فکر شما چیست؟ «حوصله‌اش سر رفته؟»\n\n"
        "خمیازه معناهای مختلفی دارد: خستگی، هوای بسته، کم‌خوابی، یا تلاش بدن برای آرام شدن. اگر فقط به همین یک نشانه تکیه کنید، ممکن است ارائه‌دهنده را اشتباه بخوانید.\n\n"
        "سه سؤال پیش از برداشت:\n"
        "• ساعت و شرایط جلسه چطور است؟\n"
        "• این فرد معمولاً هم همین‌طور است؟\n"
        "• نشانهٔ دیگری هم هست، یا فقط همین یکی؟\n\n"
        "اگر تردید داشتید، یک استراحت کوتاه پیشنهاد کنید. هم به تمرکز کمک می‌کند و هم برداشت شما را می‌آزماید.\n\n"
        "شما کِی به یک نشانهٔ غیرکلامی بیش از حد اعتماد کرده‌اید؟ در کامنت بنویسید.\n\n"
        "کتاب «درک زبان بدن» در طاقچه: https://taaghche.com/book/337335\n\n"
        "#مدیریت #رهبری #جلسه #زبان_بدن #ارتباط_مؤثر")),
 dict(id="li09-story", img="cafe-ask.png", pos="50% 35%", kicker="داستان کوتاه",
  title="قبل از نتیجه‌گیری، <b>موقعیت را ببین</b>",
  text=("این هفته در صفحهٔ «گفتگوهای خاموش» ماجرایی سه‌قسمتی از مینا و علی گذاشتم.\n\n"
        "مینا در کافه لبخند می‌زد، اما نوک پاهایش به سمت در بود. علی می‌توانست نتیجه بگیرد که او می‌خواهد برود. به‌جای آن پرسید: «اگر امروز روز شلوغی بوده، کوتاهش کنیم؟» مینا خندید. صبح زود پرواز داشت، ولی دلش نمی‌خواست برود.\n\n"
        "شب، سر شام، نوبت مینا بود: علی خمیازه کشید. این بار مینا پیش از قضاوت، موقعیت را دید و پرسید.\n\n"
        "درس کوتاه: یک نشانه حکم نیست. چند نشانه به‌علاوهٔ موقعیت تصویر دقیق‌تری می‌دهد، و یک سؤال مهربان تصویر را کامل می‌کند.\n\n"
        "شما این هفته چند بار به‌جای حدس زدن پرسیده‌اید؟\n\n"
        "ریل‌های این ماجرا در اینستاگرام: https://instagram.com/silenttalk.ir\n"
        "کتاب در طاقچه: https://taaghche.com/book/337335\n\n"
        "#زبان_بدن #داستان #ارتباط_مؤثر #مهارت_ارتباطی")),
]

def html(P):
    return (f'<html><head><meta charset="utf-8"><style>{CSS}</style></head><body><div class="img"><img src="file://{GEN}/{P["img"]}" style="{P["raw"] if "raw" in P else "object-position:" + P["pos"]}"></div><div class="fade"></div>'
            f'<div class="t"><span class="k">{P["kicker"]}</span><h1>{P["title"]}</h1></div><div class="brand">گفتگوهای خاموش · @silenttalk.ir</div></body></html>')

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    with sync_playwright() as p:
        br = p.chromium.launch(); pg = br.new_page(viewport={"width": 1200, "height": 627})
        for P in POSTS:
            f = "/tmp/_li.html"; open(f, "w", encoding="utf-8").write(html(P)); pg.goto("file://" + f); pg.wait_for_timeout(300)
            pg.screenshot(path=os.path.join(OUT, P["id"] + ".png"))
            open(os.path.join(OUT, P["id"] + ".txt"), "w", encoding="utf-8").write(P["text"])
        br.close()
