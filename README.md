# گفتگوهای خاموش (Silent Talk)

منبع اصلی تولید و انتشار محتوای اینستاگرام و لینکدین «گفتگوهای خاموش» و پوستهٔ وردپرس سایت.

## جریان کار

1. **ساخت:** هر شب Claude متن‌ها و اسکریپت ساخت را می‌نویسد. ریل‌ها و پست‌ها خروجی `content/` هستند (اجرای محلی یا کار «ساخت ریل و پست» در Actions).
2. **صف:** هر مورد در `queue/queue.json` با وضعیت `draft` ثبت می‌شود.
3. **تأیید:** تو مورد را می‌بینی و تأیید می‌کنی (پایین را ببین). گذاشتن در این صف همان تأیید انتشار است.
4. **انتشار:** Claude (کار شبانهٔ ساعت ۲۱:۵۰، یا هر وقت در گفتگو بخواهی) موردهای `approved` را با اتصال Metricool در بهترین ساعت زمان‌بندی می‌کند و وضعیت را `scheduled` می‌گذارد. این مسیر به توکن API نیاز ندارد.
5. **لینکدین:** با API زمان‌بندی نمی‌شود. Claude آن را از مرورگر داخلی در ابزار زمان‌بندی خود لینکدین می‌گذارد؛ تو در لینکدین می‌بینی و اگر نپسندیدی پاک می‌کنی.

وضعیت‌ها: `draft` ← `approved` ← `scheduled` (یا `failed` / `expired`، یعنی خطا یا گذشتن زمان؛ ساعت تازه لازم است).

## تأیید

برگهٔ **Actions** ← «تأیید و زمان‌بندی انتشار» ← **Run workflow**:
- `action = approve` و `ids = w1-reel1,w1-postA` (یا `all`) ← تأیید
- `action = reject` ← برگرداندن به پیش‌نویس
- `action = status` ← فهرست وضعیت‌ها

یا در `queue/queue.json` مقدار `status` را به `approved` تغییر بده، یا در گفتگو به Claude بگو کدام موردها را تأیید می‌کنی.

## فایل‌ها باید عمومی باشند

Metricool فایل را از یک نشانی **عمومی** می‌خواند. نشانی فایل‌ها: `https://raw.githubusercontent.com/hamidreza9812/silent-talk/main/<مسیر فایل>`. این نشانی‌ها فقط وقتی کار می‌کنند که مخزن عمومی باشد (چیز محرمانه‌ای در آن نیست). اگر مخزن خصوصی بماند، فایل‌ها از Drive (لینک «هر کسی که لینک دارد») داده می‌شوند.

## اختیاری: زمان‌بندی با API

اگر روزی دسترسی API Metricool را داشتی، در **Settings ← Secrets and variables ← Actions** این‌ها را بگذار تا خود گیت‌هاب هم زمان‌بندی کند: Secret با نام `METRICOOL_TOKEN` و `METRICOOL_USER_ID`، و Variable با نام `METRICOOL_BLOG_ID` (`7349365`) و `MEDIA_BASE_URL`. بدون آن‌ها، این بخش غیرفعال است.

## ساختار پوشه‌ها

- `render/` اسکریپت‌های ساخت (ریل، کروسل، کارت لینکدین). ریل‌های جدید در `render/jobs/` بگذار تا با push خودکار ساخته شوند.
- `fonts/` فونت Sahel. `gen2/` و `gen3/` تصویرهای مینا و علی. `render/cover.png` جلد کتاب.
- `content/` خروجی‌های هر هفته. `queue/` صف انتشار. `scripts/publish.py` ابزار صف.
- `wp/silent-talk-theme/` پوستهٔ وردپرس. `docs/` راهنماها (`NIGHTLY.md`، `OPERATIONS.md`).

## اجرای محلی

```
pip install numpy pillow playwright && python -m playwright install chromium
cd render && python3 reel_w1_r1.py texts && python3 reel_w1_r1.py     # ریل
cd render && python3 week1_posts.py                                  # پست‌ها
python3 scripts/publish.py status
```

لینک همهٔ محتوا تا راه‌افتادن دوره‌های سایت: طاقچه https://taaghche.com/book/337335
