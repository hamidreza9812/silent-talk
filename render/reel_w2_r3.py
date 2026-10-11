# -*- coding: utf-8 -*-
"""ریل ۳ هفتهٔ دوم: «علی خمیازه کشید» (قسمت ۳)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import reel_engine as R
from reel_engine import block, end_card
ROOT = R.ROOT
Y = (255, 216, 77); RED = (255, 90, 70)
SPEC = dict(
    name="reel-3-khamyaze", out=os.path.join(ROOT, "content", "week2", "reel-3"), gen=os.path.join(ROOT, "gen4"), dur=24.0, end_at=19.4, seed=23,
    images=dict(dinner="dinner-yawn.png"),
    shots=[
        dict(img="dinner", t0=0.0, t1=4.8, cam=(0.5, 0.42, 1.0, 0.62, 0.28, 1.3)),
        dict(img="dinner", t0=4.8, t1=9.8, cam=(0.62, 0.28, 1.3, 0.80, 0.22, 1.7), rings=[(0.82, 0.26, 6.2, 8.6, Y, 130)]),
        dict(img="dinner", t0=9.8, t1=14.6, cam=(0.60, 0.27, 1.3, 0.22, 0.27, 1.7)),
        dict(img="dinner", t0=14.6, t1=19.4, cam=(0.45, 0.60, 1.2, 0.62, 0.737, 1.5), rings=[(0.67, 0.77, 16.0, 18.8, RED, 150)]),
    ],
    flashes=[], whooshes=[4.7, 14.5], dings=[6.2, 16.0],
    texts=[
        ("t1", block("شب، سر شام…", size=74, sub="علی *خمیازه* کشید"), 0.6, 4.6),
        ("t2", block("مینا یک لحظه فکر کرد", size=68, sub="حوصله‌اش سر رفته؟"), 5.4, 9.6),
        ("t3", block("ولی او یاد گرفته بود:", size=70, sub="یک نشانه *حکم* نیست"), 10.4, 14.4),
        ("t4", block("خمیازه + بدنِ رو به در", size=66, sub="دو نشانه… ولی مینا *موقعیت* را هم دید", top=140), 15.2, 19.2),
    ],
    end_html=end_card("ماجرای هفتهٔ بعد: جلسهٔ کاری", "هفتهٔ بعد ادامه · دنبال کن"),
)
if __name__ == "__main__": R.main(SPEC)
