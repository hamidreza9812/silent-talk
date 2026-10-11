# گفتگوهای خاموش (Silent Talk)

منبع اصلی تولید و انتشار محتوای اینستاگرام و لینکدین «گفتگوهای خاموش» و پوستهٔ وردپرس سایت.

## جریان کار

1. **ساخت:** هر شب Claude متن‌ها و اسکریپت ساخت را می‌نویسد. ریل‌ها و پست‌ها خروجی `content/` هستند (اجرای محلی یا کار «ساخت ریل و پست» در Actions).
2. **صف:** هر مورد در `queue/queue.json` با وضعیت `draft` ثبت می‌شود.
3. **تأیید:** تو مورد را می‌بینی و تأیید می‌کنی (پایین را ببین). گذاشتن در این صف همان تأیید انتشار است.
4. **انتشار:** کار «تأیید و زمان‌بندی انتشار» موردهای `approved` را در بهترین ساعت به Metricool می‌دهد و وضعیت را `scheduled` می‌کند. هر ساعت هم خودکار اجرا می‌شود.
5. **لینکدین:** با API زمان‌بندی نمی‌شود. Claude آن را از مرورگر داخلی در ابزار زمان‌بندی خود لینکدین می‌گذارد؛ تو در لینکدین می‌بینی و اگر نپسندیدی پاک می‌کنی.

وضعیت‌ها: `draft` ← `approved` ← `scheduled` (یا `failed` / `expired`، یعنی خطا یا گذشتن زمان؛ ساعت تازه لازم است).

## تأیید از گیت‌هاب (حتی با موبایل)

برگهٔ **Actions** ← «تأیید و زمان‌بندی انتشار» ← **Run workflow**:
- `action = approve` و `ids = w1-reel1,w1-postA` (یا `all`) ← تأیید و زمان‌بندی فوری
- `action = reject` ← برگرداندن به پیش‌نویس
- `action = status` ← فهرست وضعیت‌ها

یا در `queue/queue.json` مقدار `status` را به `approved` تغییر بده.

## تنظیم یک‌باره (فقط تو می‌توانی)

در **Settings ← Secrets and variables ← Actions**:

| نوع | نام | مقدار |
| --- | --- | --- |
| Secret | `METRICOOL_TOKEN` | توکن API از Metricool (Account settings ← API) |
| Secret | `METRICOOL_USER_ID` | شناسهٔ کاربری Metricool (در همان صفحه) |
| Variable | `METRICOOL_BLOG_ID` | `7349365` |
| Variable | `MEDIA_BASE_URL` | `https://raw.githubusercontent.com/hamidreza9812/silent-talk/main` |

نکته: Metricool فایل را از یک نشانی **عمومی** می‌خواند. پس تا مخزن خصوصی است، `MEDIA_BASE_URL` کار نمی‌کند و کار انتشار خطای «فایل در دسترس عمومی نیست» می‌دهد. راه‌حل: مخزن را عمومی کن (چیز محرمانه‌ای در آن نیست و توکن‌ها فقط در Secrets می‌مانند)، یا فایل‌ها را از مسیر Drive بده.

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
