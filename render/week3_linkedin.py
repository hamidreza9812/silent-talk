# -*- coding: utf-8 -*-
"""سه پست لینکدین هفتهٔ سوم: کارت ۱۲۰۰×۶۲۷ و متن. اجرا: python3 week3_linkedin.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_v2 as B
from playwright.sync_api import sync_playwright

GEN = os.path.abspath(os.path.join(B.ROOT, ".."))
OUT = os.path.abspath(os.path.join(B.ROOT, "..", "content", "week3", "linkedin"))
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
 dict(id="li10-eyes", img="gen3/mina-notes.png", pos="50% 0%", kicker="مدیریت و جلسه",
  title="نگاهِ بالا،<br><b>یعنی بی‌اعتمادی؟</b>",
  text=("وسط ارائه‌تان همکارتان یک لحظه چشم‌هایش را بالا می‌برد. اولین فکر شما چیست؟ «باور نکرد؟»\n\n"
        "نگاهِ بالا معناهای مختلفی دارد: بی‌حوصلگی، فکر کردن، یادآوری یک عدد یا حتی خستگی. اگر فقط به همین یک نشانه تکیه کنید، ممکن است همکارتان را اشتباه بخوانید.\n\n"
        "سه سؤال پیش از برداشت:\n"
        "• این نگاه هم‌زمان با کدام جمله بود؟\n"
        "• این فرد معمولاً هم همین‌طور است؟\n"
        "• نشانهٔ دیگری هم هست، یا فقط همین یکی؟\n\n"
        "اگر تردید داشتید، به‌جای حدس زدن بپرسید: «اگر جایی مبهم بود، بگویید.» این جمله هم فضا را باز می‌کند و هم برداشت شما را می‌آزماید.\n\n"
        "شما کِی نگاهِ کسی را در جلسه اشتباه خوانده‌اید؟ در کامنت بنویسید.\n\n"
        "کتاب «درک زبان بدن» در طاقچه: https://taaghche.com/book/337335\n\n"
        "#مدیریت #جلسه #زبان_بدن #ارتباط_مؤثر #رهبری")),
 dict(id="li11-smile", img="gen2/ali-fake.png", pos="50% 0%", kicker="فروش و مذاکره",
  title="لبخند مؤدبانه،<br><b>یعنی موافقت؟</b>",
  text=("در جلسهٔ مذاکره، طرف مقابل لبخند می‌زند و می‌گوید «بررسی می‌کنیم». یعنی موافق است؟\n\n"
        "لبخند می‌تواند مؤدبانه، عصبی یا گرم باشد. با دیدن فقط لب‌ها نمی‌شود فرقش را فهمید. به حالت کلی صورت، لحن و موقعیت هم نگاه کنید.\n\n"
        "نکتهٔ کاربردی: به‌جای نتیجه‌گیری، یک سؤال مهربان بپرسید: «کدام بخش را باید بیشتر توضیح بدهم؟» این سؤال به او فرصت می‌دهد نگرانی‌اش را بگوید.\n\n"
        "شما در مذاکره‌ها به کدام نشانه بیشتر توجه می‌کنید؟ تجربه‌تان را در کامنت بنویسید.\n\n"
        "نسخهٔ الکترونیک کتاب «درک زبان بدن» در طاقچه: https://taaghche.com/book/337335\n\n"
        "#فروش #مذاکره #زبان_بدن #مهارت_ارتباطی #ارتباط_مؤثر")),
 dict(id="li12-story", img="gen2/scene-wide.png", pos="50% 0%", kicker="داستان کوتاه",
  title="به‌جای حدس زدن،<br><b>بپرسید</b>",
  text=("این هفته در صفحهٔ «گفتگوهای خاموش» ماجرایی سه‌قسمتی از یک جلسهٔ کاری گذاشتم.\n\n"
        "وسط ارائهٔ علی، مینا چشم‌هایش را بالا برد. علی می‌توانست نتیجه بگیرد که مینا باور نکرده. به‌جای آن پرسید: «اگر جایی مبهم بود، بگویید.» مینا خندید. داشت عدد فصل قبل را یادش می‌آورد.\n\n"
        "بعد نوبت مینا بود: گفت «تحویل پروژه جمعه است» و علی مؤدبانه لبخند زد. مینا حکم نداد. پرسید و فهمید علی فقط یک روز بیشتر لازم دارد.\n\n"
        "درس کوتاه: نگاهِ بالا و لبخند مؤدبانه هر کدام چند معنا دارند. موقعیت را ببینید و اگر مطمئن نشدید، بپرسید.\n\n"
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
