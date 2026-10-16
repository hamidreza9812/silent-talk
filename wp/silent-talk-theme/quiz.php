<?php
/** /quiz/ : "How well do you read body language?" (template loaded by inc/quiz.php) */
if (!defined('ABSPATH')) { exit; }
get_header();
$img = get_template_directory_uri() . '/assets/img/';
$ig = st_opt('st_instagram');
$pro = st_quiz_set() === 'pro';
?>
<main id="main" class="quiz-page">
<div class="wrap qwrap">
  <section class="qscreen" id="q-intro">
    <img class="q-host" src="<?php echo esc_url($img . 'host.jpg'); ?>" width="360" height="360" alt="مجری گفتگوهای خاموش" loading="eager">
    <?php if ($pro) : ?>
    <span class="kicker">آزمون پیشرفته · ۳ دقیقه</span>
    <h1>آزمون <b>پیشرفتهٔ</b> زبان بدن</h1>
    <p class="lead">۱۰ موقعیت سخت‌تر دربارهٔ خط پایه، خوشهٔ نشونه‌ها، زمینه، فرهنگ و پرسش خوب. اگه آزمون اول رو زدی و می‌خوای دقیق‌تر بشی، این‌جاست.</p>
    <?php else : ?>
    <span class="kicker">آزمون ۲ دقیقه‌ای</span>
    <h1>سطح <b>درک زبان بدنت</b> چقدره؟</h1>
    <p class="lead">۸ موقعیت واقعی، ۳ گزینه برای هر کدوم. آخرش می‌فهمی چه‌جور نگاه می‌کنی و قدم بعدیت چیه. نمره دادن نداریم؛ فقط یه آینهٔ کوچیک!</p>
    <?php endif; ?>
    <button class="btn big" type="button" id="q-start">شروع آزمون</button>
    <p class="micro">بدون ثبت‌نام. فقط آخرش اگه خواستی تحلیل کامل برات بیاد، اسمت رو می‌نویسی.</p>
  </section>

  <section class="qscreen" id="q-play" hidden>
    <div class="bar" aria-hidden="true"><i id="q-bar"></i></div>
    <p class="count" id="q-count"></p>
    <figure class="q-fig"><img id="q-img" src="" alt="" width="900" height="1125"></figure>
    <h2 id="q-text" tabindex="-1"></h2>
    <div class="opts" id="q-opts"></div>
    <p class="fb" id="q-fb" aria-live="polite"></p>
    <button class="btn" type="button" id="q-next" hidden>بعدی</button>
  </section>

  <section class="qscreen" id="q-result" hidden>
    <div class="res-badge" id="r-icon" aria-hidden="true"></div>
    <p class="micro" id="r-score"></p>
    <h1 id="r-title"></h1>
    <p class="lead" id="r-text"></p>
    <p class="tip" id="r-tip"></p>

    <div class="lead-card" id="q-lead">
      <h2>تحلیل کامل رو برات بفرستیم؟</h2>
      <p class="sub">با نکته‌های مخصوص سطح خودت و درس‌های کوتاه بعدی. اسم و راه تماس‌ات رو بذار:</p>
      <form class="f st-form" novalidate data-quiz="1">
        <div class="hp" aria-hidden="true"><label>وب‌سایت<input type="text" name="website" tabindex="-1" autocomplete="off"></label></div>
        <input type="hidden" name="action" value="st_submit_lead">
        <input type="hidden" name="elapsed" value="0">
        <input type="hidden" name="interest" value="quiz">
        <input type="hidden" name="quiz_score" value="">
        <input type="hidden" name="quiz_level" value="">
        <?php foreach (['utm_source', 'utm_medium', 'utm_campaign', 'utm_content', 'landing'] as $h) : ?>
          <input type="hidden" name="<?php echo esc_attr($h); ?>" value="">
        <?php endforeach; ?>
        <div><label for="ql-n">اسمت</label><input id="ql-n" type="text" name="name" autocomplete="given-name" required maxlength="60"></div>
        <div><label for="ql-c">ایمیل یا شمارهٔ موبایل</label><input id="ql-c" type="text" name="contact" inputmode="email" autocomplete="email" required dir="ltr" style="text-align:right"></div>
        <label class="chk"><input type="checkbox" name="consent" value="1" required><span>موافقم که تحلیل آزمون و درس‌های کوتاه برام فرستاده بشه. هر وقت خواستم می‌تونم انصراف بدم.</span></label>
        <button class="btn" type="submit">برام بفرست</button>
        <div class="msg" role="status" aria-live="polite"></div>
      </form>
    </div>

    <p class="save-cta" id="q-save"><span id="q-save-t"></span> <a class="btn sm" id="q-save-a" href="<?php echo esc_url(st_learn_url()); ?>">ساخت پروفایل</a></p>
    <div class="r-links">
      <?php if ($ig) : ?><a class="btn ghost sm" href="<?php echo esc_url($ig); ?>" target="_blank" rel="noopener">پیج رو فالو کن</a><?php endif; ?>
      <button class="btn ghost sm" type="button" id="q-share">برای یه دوست بفرست</button>
      <button class="btn ghost sm" type="button" id="q-again">دوباره امتحان کن</button>
      <?php if ($pro) : ?><a class="btn ghost sm" href="<?php echo esc_url(st_quiz_url()); ?>">آزمون پایه</a>
      <?php else : ?><a class="btn ghost sm" href="<?php echo esc_url(st_quiz_url('pro')); ?>">آزمون پیشرفته</a><?php endif; ?>
    </div>
    <p class="micro" style="margin-top:22px">می‌خوای عمیق‌تر یاد بگیری؟ <a href="<?php echo esc_url(home_url('/#path')); ?>">مسیر یادگیری</a> رو ببین.</p>
  </section>
</div>
</main>
<?php get_footer();
