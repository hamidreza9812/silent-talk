# -*- coding: utf-8 -*-
"""ریل ۳ هفتهٔ سوم: «لبخند علی مؤدبانه بود» (قسمت ۳ ماجرای جلسه). اجرا: python3 reel_w3_r3.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import reel_engine as R
from reel_engine import block, end_card
ROOT = R.ROOT
Y = (255, 216, 77); RED = (255, 90, 70)
SPEC = dict(
    name="reel-3-labkhand", out=os.path.join(ROOT, "content", "week3", "reel-3"), gen=ROOT, dur=24.0, end_at=19.4, seed=33,
    images=dict(wide="gen2/scene-wide.png", mina="gen3/mina-notes.png", fake="gen2/ali-fake.png", real="gen2/ali-real.png"),
    shots=[
        dict(img="wide", t0=0.0, t1=4.8, cam=(0.5, 0.45, 1.0, 0.36, 0.36, 1.45)),
        dict(img="fake", t0=4.8, t1=10.2, cam=(0.45, 0.42, 1.0, 0.45, 0.40, 1.25), rings=[(0.50, 0.45, 6.4, 9.8, Y, 150)]),
        dict(img="mina", t0=10.2, t1=14.8, cam=(0.5, 0.46, 1.0, 0.56, 0.40, 1.3)),
        dict(img="fake", t0=14.8, t1=19.4, cam=(0.45, 0.40, 1.15, 0.47, 0.40, 1.1), morph_to="real", morph=(16.0, 16.9), xfade=0.01,
             rings=[(0.47, 0.45, 17.2, 19.0, Y, 150)]),
    ],
    flashes=[(16.0, 16.8)], whooshes=[4.7, 10.1, 15.9], dings=[6.4, 17.2],
    texts=[
        ("t1", block("این بار نوبت *مینا* بود", size=70, sub="گفت: «تحویل پروژه جمعه است.»"), 0.6, 4.6),
        ("t2", block("علی لبخند زد", size=74, sub="ولی لبخندش *مؤدبانه* بود، نه گرم", top=1150), 5.4, 9.9),
        ("t3", block("مینا *حکم نداد*", size=74, sub="پرسید: «جمعه برایت سخت است؟»", top=1150), 10.6, 14.5),
        ("t4", block("علی راست گفت:", size=72, sub="«کمی. با یک روز اضافه حل می‌شود.»", top=1150), 15.2, 19.2),
    ],
    end_html=end_card("مینا و علی برمی‌گردند", "هفتهٔ بعد ماجرای تازه · دنبال کن"),
)
if __name__ == "__main__": R.main(SPEC)
