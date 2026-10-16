# -*- coding: utf-8 -*-
"""ریل معرفی کامل سایت silenttalk.ir. اجرا: python3 launch_site_reel.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import reel_engine as R
from reel_engine import block, end_card
ROOT = R.ROOT
Y = (255, 216, 77); RED = (255, 90, 70)
SPEC = dict(
    name="reel-site", out=os.path.join(ROOT, "content", "launch", "site-reel"), gen=ROOT, dur=31.0, end_at=27.4, seed=41,
    images=dict(hero="gen5/site-hero.png", path="gen5/site-path.png", pro="gen5/site-pro.png", course="gen5/site-course.png",
                profile="gen5/site-profile.png", blog="gen5/site-blog.png", gifts="gen5/site-gifts.png"),
    shots=[
        dict(img="hero", t0=0.0, t1=3.8, cam=(0.5, 0.5, 1.0, 0.5, 0.40, 1.12)),
        dict(img="path", t0=3.8, t1=7.4, cam=(0.5, 0.5, 1.0, 0.5, 0.38, 1.12)),
        dict(img="pro", t0=7.4, t1=11.0, cam=(0.5, 0.5, 1.0, 0.5, 0.38, 1.12)),
        dict(img="course", t0=11.0, t1=14.6, cam=(0.5, 0.5, 1.0, 0.5, 0.38, 1.12)),
        dict(img="profile", t0=14.6, t1=18.4, cam=(0.5, 0.45, 1.0, 0.5, 0.40, 1.12)),
        dict(img="blog", t0=18.4, t1=22.4, cam=(0.5, 0.45, 1.0, 0.5, 0.42, 1.10)),
        dict(img="gifts", t0=22.4, t1=27.4, cam=(0.5, 0.42, 1.0, 0.5, 0.40, 1.10)),
    ],
    flashes=[], whooshes=[3.9, 7.5, 11.1, 14.7, 18.5, 22.5], dings=[22.9, 24.0, 25.1],
    texts=[
        ("t1", block("یه سایت برای *دیدن* حرف‌های بی‌صدا", size=66, sub="silenttalk.ir"), 0.5, 3.6),
        ("t2", block("مسیر یادگیری، *پله‌پله*", size=68, sub="از آزمون کوچیک شروع کن و بالا برو"), 4.2, 7.2),
        ("t3", block("آزمون *پیشرفته*", size=68, sub="۱۰ موقعیت سخت‌تر: خط پایه، خوشه، زمینه"), 7.8, 10.8),
        ("t4", block("دورهٔ *۸ درسی*", size=68, sub="توضیح کوتاه، تمرین و یک سؤال"), 11.4, 14.4),
        ("t5", block("پروفایل یادگیری", size=68, sub="سطح و *پیشرفتت* همیشه همراهته"), 15.0, 18.2),
        ("t6", block("و یک *وبلاگ* تازه", size=68, sub="مقاله‌های کوتاه دربارهٔ زبان بدن"), 18.8, 22.2),
        ("t7", block("سه *هدیه* منتظر توئه", size=68, sub="۲۰ نفر اول: *کتاب چاپی* رایگان<br>خوانندگان طاقچه: دوره و کتاب چاپی<br>فالوئرها: قرعه‌کشی؛ کامنت کن «۷»", subsize=40, top=1130), 22.8, 27.2),
    ],
    end_html=end_card("ثبت‌نام رایگان در silenttalk.ir", "آزمون ۲ دقیقه‌ای · دوره · وبلاگ · هدیه"),
)
if __name__ == "__main__": R.main(SPEC)
