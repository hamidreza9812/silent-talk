# -*- coding: utf-8 -*-
"""ریل ۲ هفتهٔ اول: «مینا قضاوت نکرد؛ پرسید» (قسمت ۲)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import reel_engine as R
from reel_engine import block, end_card
ROOT = R.ROOT
Y = (255, 216, 77); RED = (255, 90, 70)
SPEC = dict(
    name="reel-2-porside", out=os.path.join(ROOT, "content", "week1", "reel-2"), gen=os.path.join(ROOT, "gen3"), dur=24.0, end_at=19.4, seed=12,
    images=dict(mina="mina-notes.png", throat="ali-throat.png", relaxed="ali-relaxed.png", wide="interview-wide.png"),
    shots=[
        dict(img="mina", t0=0.0, t1=4.8, cam=(0.5, 0.50, 1.0, 0.5, 0.40, 1.18)),
        dict(img="throat", t0=4.8, t1=9.6, cam=(0.5, 0.46, 1.1, 0.5, 0.42, 1.0)),
        dict(img="mina", t0=9.6, t1=14.4, cam=(0.5, 0.42, 1.12, 0.5, 0.38, 1.0)),
        dict(img="throat", t0=14.4, t1=19.4, cam=(0.5, 0.44, 1.05, 0.5, 0.42, 1.12), morph_to="relaxed", morph=(15.0, 16.0),
             rings=[(0.40, 0.335, 17.0, 19.0, Y, 100), (0.60, 0.325, 17.2, 19.0, Y, 100)]),
    ],
    flashes=[(15.0, 15.9)], whooshes=[14.9], dings=[17.0],
    texts=[
        ("t1", block("مینا یک لحظه *تردید* کرد", size=72, sub="گلو صاف کردن… پلک زدن…"), 0.6, 4.4),
        ("t2", block("ولی یک نشانه *حکم نیست*", size=72, sub="شاید تشنه بود؛ شاید فقط خجالت می‌کشید"), 5.2, 9.3),
        ("t3", block("پس به‌جای قضاوت… *پرسید*", size=70, sub="«دربارهٔ شرکت قبلی بیشتر بگو.»"), 10.0, 14.2),
        ("t4", block("علی نفس عمیقی کشید<br>و *راست گفت*", size=70, sub="«با مدیرم اختلاف داشتم؛<br>گفتنش کمی خجالتم می‌داد.»"), 15.4, 19.2),
    ],
    end_html=end_card("قسمت ۳: نتیجهٔ مصاحبه", "پنج‌شنبه ادامهٔ ماجرا · دنبال کن"),
)
if __name__ == "__main__": R.main(SPEC)
