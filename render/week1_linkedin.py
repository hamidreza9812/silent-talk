# -*- coding: utf-8 -*-
"""سه پست لینکدین هفتهٔ اول: کارت ۱۲۰۰×۶۲۷ و متن. اجرا: python3 week1_linkedin.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_v2 as B
from playwright.sync_api import sync_playwright

GEN = os.path.abspath(os.path.join(B.ROOT, "..", "gen3"))
OUT = os.path.abspath(os.path.join(B.ROOT, "..", "content", "week1", "linkedin"))
FONTS = "".join(f"@font-face{{font-family:S;font-weight:{w};src:url(data:font/ttf;base64,{d})}}" for w, d in B.F.items())
CSS = FONTS + """
*{box-sizing:border-box;margin:0}body{width:1200px;height:627px;background:#131f3d;font-family:S;direction:rtl;color:#f6f1ea;position:relative;overflow:hidden}
.img{position:absolute;left:0;top:0;bottom:0;width:470px}.img img{width:100%;height:100%;object-fit:cover;display:block}
.fade{position:absolute;left:300px;top:0;bottom:0;width:170px;background:linear-gradient(90deg,rgba(19,31,61,0),#131f3d)}
.t{position:absolute;right:64px;left:520px;top:0;bottom:0;display:flex;flex-direction:column;justify-content:center;gap:22px}
.k{display:inline-block;align-self:flex-start;background:#e8431f;border-radius:30px;padding:4px 22px 8px;font-size:26px;font-weight:700}
h1{font-size:60px;font-weight:900;line-height:1.55}h1 b{color:#ff7a54}
.brand{position:absolute;right:64px;bottom:34px;font-size:24px;color:#c4cbdc;font-weight:700}
"""
POSTS = [
 dict(id="li04-throat", img="ali-throat.png", pos="50% 25%", kicker="منابع انسانی و مصاحبه",
  title="یک بار گلو صاف کردن، <b>یک حکم نیست</b>",
  text=("در یک مصاحبهٔ شغلی، متقاضی هنگام پاسخ دربارهٔ شرکت قبلی گلویش را صاف کرد و چند بار پشت‌سرهم پلک زد. مصاحبه‌گر یادداشت برداشت: «مضطرب».\n\n"
        "آیا حق داشت؟ شاید. اما همین نشانه‌ها می‌توانند معنای دیگری هم داشته باشند: خشکی گلو، خستگی یا فقط حساسیت موضوع.\n\n"
        "نکتهٔ کاربردی برای مصاحبه‌گرها: نشانه را «سرنخ» ببینید، نه «نتیجه». سرنخ فقط مشخص می‌کند سؤال بعدی چه باشد.\n\n"
        "مثلاً به‌جای نتیجه‌گیری بپرسید: «دربارهٔ آن دوره بیشتر بگویید.» پاسخ این سؤال معمولاً بیشتر از هر تفسیر زبان بدنی به شما اطلاعات می‌دهد.\n\n"
        "شما وقتی در مصاحبه نشانه‌ای می‌بینید، اولین کارتان چیست؟ تجربه‌تان را در کامنت بنویسید.\n\n"
        "#استخدام #منابع_انسانی #مصاحبه_شغلی #زبان_بدن #مهارت_ارتباطی\n\n"
        "— کامنت اول: نسخهٔ الکترونیک کتاب «درک زبان بدن» در طاقچه: https://taaghche.com/book/337335")),
 dict(id="li05-question", img="mina-notes.png", pos="50% 25%", kicker="مدیریت و جلسه",
  title="قبل از قضاوت، <b>یک سؤال باز</b> بپرسید",
  text=("در جلسهٔ تیم، همکارتان می‌گوید «فکر می‌کنم خوب است» و همان لحظه گلویش را صاف می‌کند و نگاهش را می‌دزدد.\n\n"
        "می‌توانید نتیجه بگیرید که موافق نیست. می‌توانید هم نادیده بگیرید. راه سومی هم هست: یک سؤال باز.\n\n"
        "سه جمله‌ای که در این موقعیت‌ها کمک می‌کنند:\n"
        "• «بیشتر توضیح بده.»\n"
        "• «چه چیزی ممکن است سخت باشد؟»\n"
        "• «تو چطور می‌بینی؟»\n\n"
        "نشانهٔ غیرکلامی فقط به شما می‌گوید کِی بپرسید. پاسخ را خود فرد می‌دهد.\n\n"
        "شما در جلسه‌هایتان از چه سؤالی برای باز کردن گفتگو استفاده می‌کنید؟\n\n"
        "#مدیریت #رهبری #جلسه #ارتباط_مؤثر #زبان_بدن\n\n"
        "— کامنت اول: کتاب «درک زبان بدن» در طاقچه: https://taaghche.com/book/337335")),
 dict(id="li06-story", img="handshake.png", pos="50% 35%", kicker="داستان کوتاه",
  title="مصاحبه‌گر خوب، <b>اول می‌پرسد</b>",
  text=("این هفته در صفحهٔ «گفتگوهای خاموش» ماجرایی سه‌قسمتی از مینا و علی گذاشتم.\n\n"
        "علی در مصاحبه همه‌چیز را درست جواب داد، اما وقتی دربارهٔ شرکت قبلی پرسیدند، گلویش را صاف کرد و زیاد پلک زد. مینا مصاحبه‌گر بود و می‌توانست زود نتیجه بگیرد. او به‌جای آن پرسید: «دربارهٔ آن شرکت بیشتر بگو.»\n\n"
        "علی راست گفت: با مدیرش اختلاف داشت و گفتنش کمی خجالتش می‌داد. همین صداقت، تصویر مینا را کامل کرد.\n\n"
        "درس کوتاه: نشانه فرضیه می‌سازد و سؤال آن را می‌آزماید.\n\n"
        "شما تا حالا شده یک سؤال ساده برداشت‌تان را کاملاً عوض کند؟\n\n"
        "#استخدام #مصاحبه_شغلی #منابع_انسانی #زبان_بدن #داستان\n\n"
        "— کامنت اول: ریل‌های این ماجرا در اینستاگرام: https://instagram.com/silenttalk.ir و کتاب در طاقچه: https://taaghche.com/book/337335")),
]

def html(P):
    return (f'<html><head><meta charset="utf-8"><style>{CSS}</style></head><body><div class="img"><img src="file://{GEN}/{P["img"]}" style="object-position:{P["pos"]}"></div><div class="fade"></div>'
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
