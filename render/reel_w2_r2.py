# -*- coding: utf-8 -*-
"""ریل ۲ هفتهٔ دوم: «مینا چه جوابی داد؟» (قسمت ۲)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import reel_engine as R
from reel_engine import block, end_card
ROOT = R.ROOT
Y = (255, 216, 77)
SPEC = dict(
    name="reel-2-javab", out=os.path.join(ROOT, "content", "week2", "reel-2"), gen=os.path.join(ROOT, "gen4"), dur=24.0, end_at=19.4, seed=22,
    images=dict(ask="cafe-ask.png"),
    shots=[
        dict(img="ask", t0=0.0, t1=4.8, cam=(0.55, 0.30, 1.1, 0.70, 0.24, 1.45)),
        dict(img="ask", t0=4.8, t1=9.8, cam=(0.34, 0.28, 1.4, 0.26, 0.27, 1.8)),
        dict(img="ask", t0=9.8, t1=14.6, cam=(0.30, 0.55, 1.5, 0.40, 0.737, 1.9), rings=[(0.36, 0.84, 12.0, 14.3, Y, 140)]),
        dict(img="ask", t0=14.6, t1=19.4, cam=(0.5, 0.42, 1.0, 0.5, 0.36, 1.12)),
    ],
    flashes=[], whooshes=[4.7, 9.7], dings=[7.0, 12.0],
    texts=[
        ("t1", block("علی پرسید:", size=74, sub="«اگر امروز روز شلوغی بوده،<br>می‌توانیم کوتاهش کنیم.»"), 0.6, 4.6),
        ("t2", block("مینا *خندید*", size=76, sub="«صبح زود پرواز دارم…<br>ولی دلم نمی‌خواست بروم!»"), 5.4, 9.6),
        ("t3", block("و پاهایش؟", size=74, sub="حالا به سمت *علی* بود", top=140), 10.4, 14.4),
        ("t4", block("پاها دربارهٔ *فردا* حرف می‌زدند", size=66, sub="نشانه فرضیه می‌سازد،<br>سؤال آن را می‌آزماید"), 15.2, 19.2),
    ],
    end_html=end_card("قسمت ۳: علی خمیازه کشید", "پنج‌شنبه ادامهٔ ماجرا · دنبال کن"),
)
if __name__ == "__main__": R.main(SPEC)
