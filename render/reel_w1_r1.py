# -*- coding: utf-8 -*-
"""ریل ۱ هفتهٔ اول: «علی سه بار گلویش را صاف کرد» (قسمت ۱ ماجرای مصاحبه). اجرا: python3 reel_w1_r1.py texts ; python3 reel_w1_r1.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import reel_engine as R
from reel_engine import block, end_card

ROOT = R.ROOT
Y = (255, 216, 77); RED = (255, 90, 70)
SPEC = dict(
    name="reel-1-gelu", out=os.path.join(ROOT, "content", "week1", "reel-1"), gen=os.path.join(ROOT, "gen3"), dur=24.0, end_at=19.4, seed=11,
    images=dict(wide="interview-wide.png", mina="mina-notes.png", throat="ali-throat.png", blink="ali-blink.png"),
    shots=[
        dict(img="wide", t0=0.0, t1=4.6, cam=(0.5, 0.62, 1.0, 0.45, 0.30, 1.45)),
        dict(img="mina", t0=4.6, t1=9.8, cam=(0.5, 0.46, 1.0, 0.5, 0.40, 1.12)),
        dict(img="throat", t0=9.8, t1=15.2, cam=(0.5, 0.50, 1.0, 0.5, 0.42, 1.15), rings=[(0.47, 0.56, 11.0, 14.6, RED, 135)]),
        dict(img="throat", t0=15.2, t1=19.4, cam=(0.5, 0.42, 1.15, 0.5, 0.44, 1.05), morph_to="blink", morph=(15.4, 16.3), xfade=0.01,
             rings=[(0.38, 0.345, 16.6, 19.0, Y, 100), (0.58, 0.335, 16.8, 19.0, Y, 100)]),
    ],
    flashes=[(15.4, 16.2)], whooshes=[15.3], dings=[11.0, 16.6],
    texts=[
        ("t1", block("مصاحبه *عالی* بود…"), 0.5, 2.6),
        ("t2", block("علی همه‌چیز را *درست* جواب داد", size=70), 2.7, 4.5),
        ("t3", block("ولی وقتی مینا پرسید:", size=70, sub="«چرا شرکت قبلی را ترک کردی؟»"), 5.0, 9.6),
        ("t4", block("علی *گلویش را صاف کرد*", size=72, sub="ممکن است یعنی تنش…<br>یا فقط خشکی گلو"), 10.2, 15.0),
        ("t5", block("بعد *چند بار پلک زد*", size=72, sub="یک نشانه… دو نشانه… ولی حکم؟"), 16.0, 19.2),
    ],
    end_html=end_card("قسمت ۲: مینا چه کرد؟", "فردا ادامهٔ ماجرا · دنبال کن"),
)
if __name__ == "__main__": R.main(SPEC)
