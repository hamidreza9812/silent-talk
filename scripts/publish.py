# -*- coding: utf-8 -*-
"""صف انتشار «گفتگوهای خاموش».

دستورها:
  python3 scripts/publish.py approve w1-reel1,w1-postA     # تأیید چند مورد (یا all)
  python3 scripts/publish.py reject  w1-postB              # برگرداندن به پیش‌نویس
  python3 scripts/publish.py schedule [--dry-run]          # زمان‌بندی موردهای تأییدشدهٔ اینستاگرام در Metricool
  python3 scripts/publish.py status                        # خلاصهٔ صف

وضعیت هر مورد: draft ← approved ← scheduled | failed | expired
لینکدین با این اسکریپت زمان‌بندی نمی‌شود (handled_by = browser).

متغیرهای محیطی برای schedule:
  METRICOOL_TOKEN     توکن API (secret)
  METRICOOL_USER_ID   شناسهٔ کاربر Metricool (secret یا variable)
  METRICOOL_BLOG_ID   پیش‌فرض 7349365
  MEDIA_BASE_URL      نشانی عمومی ریشهٔ مخزن، مثلاً https://raw.githubusercontent.com/<user>/<repo>/main
"""
import json, os, sys, urllib.request, urllib.error, urllib.parse
from datetime import datetime
from zoneinfo import ZoneInfo

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
QF = os.path.join(ROOT, "queue", "queue.json")
API = "https://app.metricool.com/api/v2/scheduler/posts"


def load():
    return json.load(open(QF, encoding="utf-8"))


def save(d):
    json.dump(d, open(QF, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    open(QF, "a").write("\n")


def pick(d, ids):
    if ids == "all":
        return [i for i in d["items"] if i["status"] == "draft"]
    want = {x.strip() for x in ids.split(",") if x.strip()}
    got = [i for i in d["items"] if i["id"] in want]
    miss = want - {i["id"] for i in got}
    if miss:
        sys.exit("شناسهٔ نامعتبر: " + ", ".join(sorted(miss)))
    return got


def set_status(ids, new, allowed):
    d = load()
    for it in pick(d, ids):
        if it["status"] in allowed:
            print(f'{it["id"]}: {it["status"]} → {new}'); it["status"] = new
        else:
            print(f'{it["id"]}: وضعیت {it["status"]} است و تغییر نکرد')
    save(d)


def media_url(path):
    base = os.environ.get("MEDIA_BASE_URL", "").rstrip("/")
    return f"{base}/" + urllib.parse.quote(path)


def reachable(url):
    try:
        req = urllib.request.Request(url, method="HEAD")
        return urllib.request.urlopen(req, timeout=30).status == 200
    except Exception:
        return False


def build_body(it, tz, text):
    kind = {"reel": "REEL", "carousel": "POST", "image": "POST", "story": "STORY"}[it["type"]]
    return {
        "publicationDate": {"dateTime": it["publish_at"], "timezone": tz},
        "text": text,
        "providers": [{"network": "instagram"}],
        "autoPublish": True, "draft": False, "shortener": False,
        "saveExternalMediaFiles": True,
        "media": [media_url(m) for m in it["media"]],
        "instagramData": {"type": kind, "showReelOnFeed": True, "isAiGenerated": bool(it.get("ai_generated", False))},
    }


def schedule(dry):
    tok = os.environ.get("METRICOOL_TOKEN"); uid = os.environ.get("METRICOOL_USER_ID")
    blog = os.environ.get("METRICOOL_BLOG_ID", "7349365")
    if not dry and not (tok and uid and os.environ.get("MEDIA_BASE_URL")):
        sys.exit("تنظیمات ناقص است: METRICOOL_TOKEN و METRICOOL_USER_ID و MEDIA_BASE_URL لازم‌اند. راهنما در README.md")
    d = load(); tz = d.get("timezone", "Asia/Tehran"); now = datetime.now(ZoneInfo(tz)).replace(tzinfo=None)
    todo = [i for i in d["items"] if i["status"] == "approved" and i["network"] == "instagram"]
    if not todo:
        print("چیزی برای زمان‌بندی نیست."); return
    for it in todo:
        when = datetime.fromisoformat(it["publish_at"])
        if when <= now:
            it["status"] = "expired"; print(f'{it["id"]}: زمانش گذشته؛ ساعت تازه لازم است'); continue
        text = open(os.path.join(ROOT, it["caption_file"]), encoding="utf-8").read().strip()
        body = build_body(it, tz, text)
        if dry:
            print(f'[dry-run] {it["id"]} → {it["publish_at"]}\n{json.dumps(body, ensure_ascii=False)[:600]}'); continue
        bad = [u for u in body["media"] if not reachable(u)]
        if bad:
            print(f'{it["id"]}: فایل در دسترس عمومی نیست (مخزن خصوصی است؟): {bad[0]}'); it["status"] = "failed"; it["error"] = "media-unreachable"; continue
        url = f"{API}?blogId={blog}&userId={uid}"
        req = urllib.request.Request(url, data=json.dumps(body).encode(), method="POST",
                                     headers={"Content-Type": "application/json", "X-Mc-Auth": tok})
        try:
            resp = json.loads(urllib.request.urlopen(req, timeout=120).read().decode() or "{}")
            it["status"] = "scheduled"; it["metricool"] = (resp.get("data") or resp) if isinstance(resp, dict) else resp
            it.pop("error", None); print(f'{it["id"]}: زمان‌بندی شد برای {it["publish_at"]}')
        except urllib.error.HTTPError as e:
            it["status"] = "failed"; it["error"] = f"HTTP {e.code}: {e.read().decode()[:300]}"; print(it["id"], it["error"])
    if not dry:
        save(d)


def status():
    for it in load()["items"]:
        print(f'{it["status"]:10} {it["network"]:9} {it["publish_at"]}  {it["id"]}  {it["title"]}')


if __name__ == "__main__":
    a = sys.argv[1:]
    if not a: sys.exit(__doc__)
    if a[0] == "approve": set_status(a[1], "approved", {"draft", "failed", "expired"})
    elif a[0] == "reject": set_status(a[1], "draft", {"approved", "failed", "expired"})
    elif a[0] == "schedule": schedule("--dry-run" in a)
    elif a[0] == "status": status()
    else: sys.exit(__doc__)
