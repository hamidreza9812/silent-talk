# -*- coding: utf-8 -*-
"""ریل ۳ هفتهٔ اول: «علی استخدام شد؟» (قسمت ۳ و پایان)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import reel_engine as R
from reel_engine import block, end_card
ROOT = R.ROOT
Y = (255, 216, 77)
SPEC = dict(
    name="reel-3-payan", out=os.path.join(ROOT, "content", "week1", "reel-3"), gen=os.path.join(ROOT, "gen3"), dur=24.0, end_at=19.4, seed=13,
    images=dict(relaxed="ali-relaxed.png", hand="handshake.png", mina="mina-notes.png"),
    shots=[
        dict(img="relaxed", t0=0.0, t1=4.6, cam=(0.5, 0.48, 1.0, 0.5, 0.40, 1.15)),
        dict(img="hand", t0=4.6, t1=10.4, cam=(0.34, 0.22, 1.7, 0.70, 0.19, 1.7)),
        dict(img="mina", t0=10.4, t1=15.0, cam=(0.5, 0.44, 1.1, 0.5, 0.40, 1.0)),
        dict(img="relaxed", t0=15.0, t1=19.4, cam=(0.5, 0.42, 1.12, 0.5, 0.44, 1.02)),
    ],
    flashes=[], whooshes=[4.5], dings=[10.6],
    texts=[
        ("t1", block("علی *استخدام* شد؟", size=78), 0.6, 4.3),
        ("t2", block("بله! مینا گفت:", size=70, sub="«صداقتت از استرسِ آن لحظه مهم‌تر بود.»"), 5.0, 10.0),
        ("t3", block("مینا چه یاد گرفته بود؟", size=70, sub="نشانه *فرضیه* می‌سازد، نه حکم"), 10.9, 14.8),
        ("t4", block("*سؤال* فرضیه را می‌آزماید", size=68, sub="این هفته یک بار به‌جای حدس زدن،<br>یک سؤال باز بپرس"), 15.5, 19.2),
    ],
)
if __name__ == "__main__": R.main(SPEC)
