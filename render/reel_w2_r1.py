# -*- coding: utf-8 -*-
"""ریل ۱ هفتهٔ دوم: «پاهای مینا به سمت در بود» (قسمت ۱). اجرا: python3 reel_w2_r1.py texts ; python3 reel_w2_r1.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import reel_engine as R
from reel_engine import block, end_card
ROOT = R.ROOT
Y = (255, 216, 77); RED = (255, 90, 70)
SPEC = dict(
    name="reel-1-pa", out=os.path.join(ROOT, "content", "week2", "reel-1"), gen=os.path.join(ROOT, "gen4"), dur=24.0, end_at=19.4, seed=21,
    images=dict(cafe="cafe-feet.png"),
    shots=[
        dict(img="cafe", t0=0.0, t1=4.8, cam=(0.5, 0.34, 1.0, 0.42, 0.29, 1.4)),
        dict(img="cafe", t0=4.8, t1=10.0, cam=(0.42, 0.29, 1.4, 0.27, 0.74, 1.9), rings=[(0.23, 0.745, 8.4, 9.9, RED, 150)]),
        dict(img="cafe", t0=10.0, t1=14.8, cam=(0.27, 0.74, 1.9, 0.17, 0.40, 1.4), rings=[(0.06, 0.36, 12.2, 14.5, Y, 120)]),
        dict(img="cafe", t0=14.8, t1=19.4, cam=(0.5, 0.45, 1.0, 0.5, 0.38, 1.12)),
    ],
    flashes=[], whooshes=[4.9, 10.0], dings=[8.4, 12.2],
    texts=[
        ("t1", block("مینا *لبخند* می‌زد", size=76, sub="سر تکان می‌داد و گوش می‌کرد"), 0.6, 4.5),
        ("t2", block("ولی نوک پاهایش…", size=72, sub="به سمت *در* بود", top=1150), 5.4, 9.8),
        ("t3", block("یعنی می‌خواهد برود؟", size=70, sub="نه لزوماً؛ یک نشانه *حکم* نیست"), 10.5, 14.6),
        ("t4", block("علی نتیجه نگرفت", size=74, sub="فقط یک *سؤال* کوچک پرسید"), 15.3, 19.2),
    ],
    end_html=end_card("قسمت ۲: مینا چه جوابی داد؟", "فردا ادامهٔ ماجرا · دنبال کن"),
)
if __name__ == "__main__": R.main(SPEC)
