# -*- coding: utf-8 -*-
"""ریل ۱ هفتهٔ سوم: «مینا چشم‌هایش را بالا برد» (قسمت ۱ ماجرای جلسه). اجرا: python3 reel_w3_r1.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import reel_engine as R
from reel_engine import block, end_card
ROOT = R.ROOT
Y = (255, 216, 77); RED = (255, 90, 70)
SPEC = dict(
    name="reel-1-chashm", out=os.path.join(ROOT, "content", "week3", "reel-1"), gen=ROOT, dur=24.0, end_at=19.4, seed=31,
    images=dict(wide="gen2/scene-wide.png", mina="gen3/mina-notes.png", fake="gen2/ali-fake.png"),
    shots=[
        dict(img="wide", t0=0.0, t1=4.8, cam=(0.5, 0.45, 1.0, 0.70, 0.33, 1.6)),
        dict(img="mina", t0=4.8, t1=10.0, cam=(0.5, 0.46, 1.0, 0.56, 0.38, 1.35), rings=[(0.60, 0.32, 6.4, 9.8, RED, 190)]),
        dict(img="fake", t0=10.0, t1=14.8, cam=(0.45, 0.42, 1.0, 0.45, 0.38, 1.25), rings=[(0.43, 0.34, 11.6, 14.6, Y, 170)]),
        dict(img="wide", t0=14.8, t1=19.4, cam=(0.5, 0.45, 1.0, 0.36, 0.36, 1.45)),
    ],
    flashes=[], whooshes=[4.9, 14.9], dings=[6.4, 11.6],
    texts=[
        ("t1", block("جلسه *شروع* شد", size=76, sub="علی گزارش سه‌ماههٔ پروژه را ارائه می‌داد"), 0.6, 4.6),
        ("t2", block("وسط حرفش، مینا", size=72, sub="*چشم‌هایش را بالا برد*<br>فقط برای یک لحظه", top=1150), 5.4, 9.8),
        ("t3", block("علی لبخند زد…", size=72, sub="ولی توی ذهنش پرسید:<br>«چشم‌غره بود؟ باور نکرد؟»", top=1150), 10.6, 14.6),
        ("t4", block("یعنی مینا قبول ندارد؟", size=70, sub="نه لزوماً؛ یک نشانه *حکم* نیست"), 15.4, 19.2),
    ],
    end_html=end_card("قسمت ۲: علی چه کرد؟", "فردا ادامهٔ ماجرا · دنبال کن"),
)
if __name__ == "__main__": R.main(SPEC)
