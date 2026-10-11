# -*- coding: utf-8 -*-
import base64, os
from playwright.sync_api import sync_playwright
ROOT=os.path.dirname(os.path.abspath(__file__)); GEN=os.path.abspath(os.path.join(ROOT,"..","gen2"))
FD=os.path.join(ROOT,"..","fonts")+"/"
def b(p): return base64.b64encode(open(p,"rb").read()).decode()
F={w:b(FD+n) for w,n in [(400,"Sahel.ttf"),(700,"Sahel-Bold.ttf"),(900,"Sahel-Black.ttf")]}
COVER="file://"+os.path.join(ROOT,"cover.png")
CSS="".join(f"@font-face{{font-family:S;font-weight:{w};src:url(data:font/ttf;base64,{d})}}" for w,d in F.items())+"""
*{box-sizing:border-box;margin:0}body{width:1080px;height:1350px;background:#131f3d;font-family:S;direction:rtl;color:#f6f1ea;position:relative;overflow:hidden}
.top{position:absolute;top:48px;left:64px;right:64px;display:flex;justify-content:space-between;font-size:28px;color:#c4cbdc;font-weight:700}
.dot{display:inline-block;width:14px;height:14px;border-radius:50%;background:#ff7a54;margin-left:10px}
.pill{display:inline-block;background:#e8431f;border-radius:40px;padding:6px 30px 10px;font-size:34px;font-weight:700}
h1,h2{font-weight:900;line-height:1.5}.o{color:#ff7a54}
.card{position:absolute;border-radius:44px;overflow:hidden;box-shadow:0 24px 60px rgba(0,0,0,.45)}
.card img{width:100%;height:100%;object-fit:cover;display:block}
.row{display:flex;gap:28px;align-items:flex-start;margin-bottom:46px}
.num{flex:none;width:76px;height:76px;border-radius:50%;background:#e8431f;font-size:44px;font-weight:900;display:flex;align-items:center;justify-content:center;padding-bottom:6px}
.row b{font-size:50px;font-weight:900;display:block;line-height:1.5}.row span{font-size:38px;color:#c4cbdc;line-height:1.7}
.body{font-size:50px;line-height:1.9;font-weight:400}
.hint{position:absolute;bottom:52px;left:0;right:0;text-align:center;font-size:32px;color:#c4cbdc;font-weight:700}
"""
def top(n): return f'<div class="top"><span><i class="dot"></i>گفتگوهای خاموش</span><span>{'۰۱۲۳۴۵۶۷۸۹'[n]} / ۵</span></div>'
def page(x): return f'<html><head><meta charset="utf-8"><style>{CSS}</style></head><body>{x}</body></html>'
def slides(P):
    img="file://"+os.path.join(GEN,P["img"])
    S=[]
    S.append(page(f'''<div class="card" style="inset:0;border-radius:0;box-shadow:none"><img src="{img}" style="object-position:{P.get("pos","50% 20%")}"></div>
<div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(19,31,61,.7) 0%,rgba(19,31,61,0) 16%,rgba(19,31,61,0) 48%,rgba(19,31,61,.94) 74%,rgba(19,31,61,.98) 100%)"></div>
{top(1)}<div style="position:absolute;top:112px;right:64px"><span class="pill">{P["tag"]}</span></div>
<div style="position:absolute;bottom:140px;right:64px;left:64px"><h1 style="font-size:80px">{P["hook"]}</h1></div><div class="hint" style="color:#fff">◀ بکش و ادامه را ببین</div>'''))
    S.append(page(f'''{top(2)}<div style="position:absolute;top:130px;right:70px;left:70px"><div style="font-size:34px;color:#ff7a54;font-weight:700;margin-bottom:10px">{P.get("l2","نکتهٔ هفته")}</div><h2 style="font-size:84px;margin-bottom:34px">{P["t2"]}</h2><div class="body">{P["b2"]}</div></div>
<div class="card" style="left:70px;right:70px;bottom:70px;height:430px"><img src="{img}" style="object-position:{P.get("pos2","50% 25%")}"></div>'''))
    rows="".join(f'<div class="row"><div class="num">{i}</div><div><b>{a}</b><span>{c}</span></div></div>' for i,(a,c) in zip("۱۲۳",P["rows"]))
    S.append(page(f'''{top(3)}<div style="position:absolute;top:130px;right:70px;left:70px"><h2 style="font-size:84px">{P.get("h3","سه چیز را <span class='o'>بررسی کن</span>")}</h2><div style="font-size:38px;color:#c4cbdc;margin-top:6px">{P.get("h3s","قبل از اینکه قضاوت کنی")}</div></div>
<div style="position:absolute;top:470px;right:70px;left:70px">{rows}</div>
<div style="position:absolute;bottom:64px;right:70px;left:70px;font-size:34px;color:#c4cbdc;line-height:1.8">{P.get("fn","هیچ نشانه‌ای به‌تنهایی قطعی نیست. هدف ذهن‌خوانی نیست؛ بهتر دیدن و مهربان‌تر پرسیدن است.")}</div>'''))
    S.append(page(f'''{top(4)}<div style="position:absolute;top:130px;right:70px;left:70px"><span class="pill">تمرین امروز</span><div class="body" style="margin-top:44px;font-size:56px;font-weight:700">{P["ex"]}</div></div>
<div style="position:absolute;bottom:110px;right:70px;left:70px;background:#1d2d57;border-radius:40px;padding:48px 52px"><div style="font-size:34px;color:#ff7a54;font-weight:700;margin-bottom:12px">نظرت را بنویس</div><div style="font-size:50px;font-weight:900;line-height:1.7">{P["q"]}</div></div>'''))
    S.append(page(f'''{top(5)}<div style="position:absolute;inset:0;background:radial-gradient(circle at 50% 30%,#22376b,#131f3d 70%)"></div>
<div style="position:absolute;top:130px;left:50%;margin-left:-200px;width:400px;transform:rotate(-3deg);border-radius:12px;overflow:hidden;box-shadow:0 30px 70px rgba(0,0,0,.6),0 0 0 6px #fff"><img src="{COVER}" style="width:100%;display:block"></div>
<div style="position:absolute;top:850px;right:60px;left:60px;text-align:center"><div style="font-size:60px;font-weight:900;margin-bottom:10px">{P.get("l5","این درس‌ها از کتاب <span class='o'>درک زبان بدن</span> است")}</div><div style="font-size:36px;color:#c4cbdc;margin-bottom:34px">نوشتهٔ اسکات رز · ترجمهٔ حامد کاظمی</div>
<div style="background:#e8431f;border-radius:60px;padding:22px;font-size:44px;font-weight:900">کتاب را در طاقچه ببین · لینک در بیو</div>
<div style="margin-top:26px;font-size:34px;color:#c4cbdc">برای تمرین‌های بعدی، صفحه را دنبال کن</div></div>'''))
    return S
POSTS={
"A":dict(img="img1.jpg",tag="تمرین ۱",hook="دست‌هایش روی سینه است.<br>یعنی مخالف است؟",pos="50% 50%",pos2="50% 50%",
 t2="همیشه این‌طور نیست",b2="دست‌به‌سینه ایستادن می‌تواند نشانهٔ مخالفت باشد. اما گاهی فقط راحتی، سرما یا عادت است. کتاب می‌گوید: یک نشانه را تنها نخوان.",
 rows=[("رفتار همیشگی‌اش چگونه است؟","ببین خودِ این آدم معمولاً هم همین‌طور می‌ایستد یا نه"),("نشانهٔ دیگری هم هست؟","چهره، پاها و صدا را کنار دست‌ها بگذار"),("شرایط چیست؟","اتاق سرد است؟ خسته است؟")],
 ex="امروز یک نفر را انتخاب کن و فقط ببین دست‌هایش در حالت عادی کجاست. هنوز قضاوت نکن؛ فقط ببین.",
 q="تا حالا دست‌به‌سینه را اشتباه خوانده‌ای؟"),
"B":dict(img="img0.jpg",tag="تمرین ۲",hook="لبخند زد.<br>پس راضی است؟",pos="60% 50%",pos2="70% 40%",
 t2="همهٔ لبخندها یکی نیستند",b2="لبخند واقعی چشم‌ها را هم درگیر می‌کند. لبخند مؤدبانه فقط دهان را تکان می‌دهد. تفاوت را در چشم‌ها پیدا کن.",
 rows=[("گوشهٔ چشم‌ها چین می‌خورد؟","در لبخند واقعی، دور چشم‌ها هم می‌خندد"),("لبخند ناگهانی آمد و رفت؟","لبخند واقعی آرام می‌آید و آرام می‌رود"),("بقیهٔ صورت چه می‌گوید؟","ابروها و گونه‌ها را هم نگاه کن")],
 ex="در گفتگوی بعدی، وقتی کسی لبخند زد، فقط به چشم‌هایش نگاه کن و ببین با دهانش هماهنگ است یا نه.",
 q="آخرین لبخند مؤدبانه‌ای که دیدی چه بود؟"),
"C":dict(img="img2.jpg",tag="تمرین ۳",hook="اعتمادبه‌نفس را<br>از دست‌ها بخوان",pos="50% 50%",pos2="40% 60%",
 t2="دست‌های باز، حس اطمینان می‌دهند",b2="کتاب می‌گوید دست‌های باز و آرام نشانهٔ اطمینان‌اند. دست‌های گره‌خورده یا پنهان، بیشتر از نگرانی خبر می‌دهند.",
 rows=[("دست‌ها دیده می‌شوند؟","دست روی میز یعنی بازبودن؛ دست در جیب یعنی پنهان‌کاری یا تردید"),("با حرف‌ها هماهنگ‌اند؟","حرکت دست باید با کلمات هم‌جهت باشد"),("شانه‌ها آرام‌اند؟","شانهٔ بالا رفته یعنی فشار")],
 ex="در جلسهٔ بعدی، دست‌های خودت را بررسی کن: روی میز، باز و آرام. ببین حس‌ات چه فرقی می‌کند.",
 q="دست‌های تو در جلسه معمولاً کجاست؟"),
"D":dict(img="img3.jpg",tag="پشت‌صحنه",hook="چرا این کتاب را<br>ترجمه کردم؟",pos="55% 50%",pos2="70% 40%",
 t2="خواندن کافی نیست",b2="زبان بدن یک مهارت است، نه فقط یک اطلاعات. مثل شنا کردن باید تمرینش کرد. برای همین کتاب را به تمرین‌های کوتاه تبدیل می‌کنم.",
 rows=[("هر روز یک نشانهٔ کوچک","نه چیز زیاد، فقط یکی"),("یک تمرین دو دقیقه‌ای","همان روز امتحانش کن"),("سؤال به‌جای قضاوت","یاد می‌گیری مهربان‌تر بپرسی")],
 ex="اگر کتاب را خوانده‌ای، یک نشانه را که از آن یاد گرفتی امروز در یک گفتگو پیدا کن.",
 q="کدام بخش کتاب بیشتر به کارت آمد؟"),
}
CAP={
"A":"دست‌هایش روی سینه است. یعنی مخالف است؟\n\nنه همیشه. دست‌به‌سینه بودن گاهی نشانهٔ مخالفت است و گاهی فقط سرما، راحتی یا عادت. کتاب «درک زبان بدن» می‌گوید یک نشانه را تنها قضاوت نکن؛ رفتار همیشگی، نشانه‌های دیگر و شرایط را هم ببین.\n\nتمرین امروز: یک نفر را انتخاب کن و فقط حالت عادی دست‌هایش را ببین، بدون قضاوت.\n\nتا حالا دست‌به‌سینه را اشتباه خوانده‌ای؟ زیر همین پست بنویس.\n\nکتاب را در طاقچه ببین (لینک در بیو). برای تمرین‌های بعدی صفحه را دنبال کن.\n",
"B":"لبخند زد. پس راضی است؟\n\nهمهٔ لبخندها یکی نیستند. لبخند واقعی چشم‌ها را هم درگیر می‌کند، اما لبخند مؤدبانه فقط دهان را تکان می‌دهد. سه چیز را ببین: چین گوشهٔ چشم، آرام آمدن و رفتن لبخند، و بقیهٔ صورت.\n\nتمرین امروز: در گفتگوی بعدی، وقتی کسی لبخند زد، فقط به چشم‌هایش نگاه کن.\n\nآخرین لبخند مؤدبانه‌ای که دیدی چه بود؟ بنویس.\n\nکتاب را در طاقچه ببین (لینک در بیو). برای تمرین‌های بعدی صفحه را دنبال کن.\n",
"C":"اعتمادبه‌نفس را از دست‌ها بخوان.\n\nکتاب «درک زبان بدن» می‌گوید دست‌های باز و آرام حس اطمینان می‌دهند و دست‌های گره‌خورده یا پنهان بیشتر از نگرانی خبر می‌دهند. سه چیز را بررسی کن: دیده‌شدن دست‌ها، هماهنگی با حرف‌ها و آرام بودن شانه‌ها.\n\nتمرین امروز: در جلسهٔ بعدی دست‌های خودت را روی میز، باز و آرام نگه دار و فرقش را حس کن.\n\nدست‌های تو در جلسه معمولاً کجاست؟ بنویس.\n\nکتاب را در طاقچه ببین (لینک در بیو). برای تمرین‌های بعدی صفحه را دنبال کن.\n",
"D":"پشت‌صحنه: چرا این کتاب را ترجمه کردم؟\n\nچون خواندن کافی نیست. زبان بدن یک مهارت است و باید تمرینش کرد، مثل شنا کردن. برای همین از کتاب «درک زبان بدن» تمرین‌های کوتاه می‌سازم: هر روز یک نشانهٔ کوچک، یک تمرین دو دقیقه‌ای و یک سؤال به‌جای قضاوت.\n\nاگر کتاب را خوانده‌ای، کدام بخشش بیشتر به کارت آمد؟ بنویس.\n\nکتاب را در طاقچه ببین (لینک در بیو). برای تمرین‌های بعدی صفحه را دنبال کن.\n",
}
TAGS="\n#زبان_بدن #ارتباط_غیرکلامی #گفتگوهای_خاموش #مهارت_ارتباطی #درک_زبان_بدن"
if __name__=="__main__":
    out=os.path.join(ROOT,"..","content","v2");os.makedirs(out,exist_ok=True)
    with sync_playwright() as p:
        br=p.chromium.launch();pg=br.new_page(viewport={"width":1080,"height":1350})
        for k,P in POSTS.items():
            for i,h in enumerate(slides(P),1):
                f=os.path.join(out,f"_t.html");open(f,"w").write(h)
                pg.goto("file://"+os.path.abspath(f));pg.wait_for_timeout(300)
                pg.screenshot(path=os.path.join(out,f"{k}-{i}.png"))
            open(os.path.join(out,f"{k}-caption.txt"),"w").write(CAP[k]+TAGS)
        br.close()
    os.remove(os.path.join(out,"_t.html"))
