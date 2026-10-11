# -*- coding: utf-8 -*-
"""ریل ۲ هفتهٔ سوم: «علی پرسید» (قسمت ۲ ماجرای جلسه). اجرا: python3 reel_w3_r2.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import reel_engine as R
from reel_engine import block, end_card
ROOT = R.ROOT
Y = (255, 216, 77); RED = (255, 90, 70)
SPEC = dict(
    name="reel-2-porsid", out=os.path.join(ROOT, "content", "week3", "reel-2"), gen=ROOT, dur=24.0, end_at=19.4, seed=32,
    images=dict(wide="gen2/scene-wide.png", mina="gen3/mina-notes.png", fake="gen2/ali-fake.png", real="gen2/ali-real.png"),
    shots=[
        dict(img="fake", t0=0.0, t1=4.8, cam=(0.45, 0.42, 1.0, 0.45, 0.38, 1.2)),
        dict(img="wide", t0=4.8, t1=9.8, cam=(0.5, 0.45, 1.0, 0.70, 0.33, 1.6)),
        dict(img="mina", t0=9.8, t1=14.6, cam=(0.5, 0.46, 1.0, 0.56, 0.40, 1.3), rings=[(0.60, 0.32, 11.0, 14.2, Y, 190)]),
        dict(img="real", t0=14.6, t1=19.4, cam=(0.5, 0.42, 1.0, 0.48, 0.38, 1.2), rings=[(0.45, 0.35, 16.2, 19.0, Y, 170)]),
    ],
    flashes=[], whooshes=[4.7, 9.7], dings=[11.0, 16.2],
    texts=[
        ("t1", block("علی *نتیجه نگرفت*", size=76, sub="ارائه را تمام کرد و نفس عمیقی کشید"), 0.6, 4.6),
        ("t2", block("بعد پرسید:", size=72, sub="«اگر جایی مبهم بود، بگویید.»"), 5.4, 9.6),
        ("t3", block("مینا خندید:", size=72, sub="«ببخشید! داشتم عدد فصل قبل را<br>یادم می‌آوردم.»", top=1150), 10.4, 14.4),
        ("t4", block("نگاهِ بالا = *بی‌اعتمادی*؟", size=66, sub="نه؛ این بار فقط *یادآوری* بود.<br>یک سؤال، حدس را تمام کرد", top=1130), 15.2, 19.2),
    ],
    end_html=end_card("قسمت ۳: لبخند علی", "پنج‌شنبه ادامهٔ ماجرا · دنبال کن"),
)
if __name__ == "__main__": R.main(SPEC)
