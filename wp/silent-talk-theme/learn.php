<?php
/** /learn/ : learner profile + course (template loaded by inc/learn.php) */
if (!defined('ABSPATH')) { exit; }
get_header();
$img = get_template_directory_uri() . '/assets/img/';
$uid = get_current_user_id();
$lessons = st_course_data();
$total = count($lessons);
$progress = $uid ? st_progress($uid) : [];
$done = count($progress);
$pct = $total ? (int) round($done / $total * 100) : 0;
$levels = st_quiz_levels();
$last = $uid ? get_user_meta($uid, 'st_quiz_last', true) : null;
$lv = (is_array($last) && isset($levels[$last['level']])) ? $levels[$last['level']] : null;
$user = $uid ? wp_get_current_user() : null;
$claim = $uid ? get_user_meta($uid, 'st_book_claim', true) : null;
$persian = function ($n) { return strtr((string) $n, ['0'=>'۰','1'=>'۱','2'=>'۲','3'=>'۳','4'=>'۴','5'=>'۵','6'=>'۶','7'=>'۷','8'=>'۸','9'=>'۹']); };
$hp = '<div class="hp" aria-hidden="true"><label>وب‌سایت<input type="text" name="website" tabindex="-1" autocomplete="off"></label></div>';
?>
<main id="main" class="learn-page">

<?php if (!$uid) : ?>
<section class="hero learn-hero">
  <div class="wrap">
    <div>
      <span class="kicker">پروفایل یادگیری</span>
      <h1>پروفایلت رو بساز و <b>پیشرفتت</b> رو ببین</h1>
      <p class="lead">نتیجهٔ آزمون نگه‌داری می‌شه، درس‌های کوتاه ۴ تا ۶ دقیقه‌ای رو دنبال می‌کنی و هر درس یه تمرین کوچیک و یه سؤال داره. فعلاً همه‌چی رایگانه.</p>
      <ul class="perks">
        <li>🎯 سطح آزمونت همیشه توی پروفایلته</li>
        <li>📘 ۸ درس کوتاه با تمرین و سؤال</li>
        <li>📈 پیشرفتت ذخیره می‌شه و از هر جا ادامه می‌دی</li>
        <li>🎁 خوانندگان کتاب «درک زبان بدن» در طاقچه: همهٔ دوره و آزمون‌ها همیشه رایگان + نسخهٔ چاپی هدیه</li>
        <li>📖 ۲۰ نفر اول ثبت‌نام: نسخهٔ چاپی کتاب هدیه (<a href="<?php echo esc_url(home_url('/#gifts')); ?>" style="color:#FF7A57">جزئیات</a>)</li>
      </ul>
    </div>
    <div class="auth-card" id="auth">
      <div class="tabs" role="tablist">
        <button type="button" class="tab on" data-tab="reg" role="tab" aria-selected="true">ساخت پروفایل</button>
        <button type="button" class="tab" data-tab="login" role="tab" aria-selected="false">ورود</button>
      </div>
      <form class="f st-auth" data-form="reg" novalidate>
        <?php echo $hp; // phpcs:ignore ?>
        <input type="hidden" name="action" value="st_register">
        <input type="hidden" name="elapsed" value="0">
        <input type="hidden" name="quiz_score" value=""><input type="hidden" name="quiz_level" value="">
        <?php foreach (['utm_source', 'utm_medium', 'utm_campaign', 'utm_content'] as $h) : ?><input type="hidden" name="<?php echo esc_attr($h); ?>" value=""><?php endforeach; ?>
        <div><label for="r-name">اسمت</label><input id="r-name" type="text" name="name" autocomplete="given-name" required maxlength="60"></div>
        <div><label for="r-email">ایمیل</label><input id="r-email" type="email" name="email" autocomplete="email" required dir="ltr" style="text-align:right"></div>
        <div><label for="r-pass">رمز عبور (حداقل ۸ نویسه)</label><input id="r-pass" type="password" name="password" autocomplete="new-password" required minlength="8" dir="ltr" style="text-align:right"></div>
        <label class="chk"><input type="checkbox" name="consent" value="1" required><span>موافقم که نام و ایمیلم برای پروفایل یادگیری و ارسال درس‌های کوتاه استفاده شود. هر زمان می‌توانم انصراف دهم.</span></label>
        <button class="btn" type="submit">پروفایلم رو بساز</button>
        <div class="msg" role="status" aria-live="polite"></div>
      </form>
      <form class="f st-auth" data-form="login" novalidate hidden>
        <?php echo $hp; // phpcs:ignore ?>
        <input type="hidden" name="action" value="st_login">
        <input type="hidden" name="elapsed" value="0">
        <input type="hidden" name="quiz_score" value=""><input type="hidden" name="quiz_level" value="">
        <div><label for="l-email">ایمیل</label><input id="l-email" type="text" name="email" autocomplete="username" required dir="ltr" style="text-align:right"></div>
        <div><label for="l-pass">رمز عبور</label><input id="l-pass" type="password" name="password" autocomplete="current-password" required dir="ltr" style="text-align:right"></div>
        <button class="btn" type="submit">ورود</button>
        <div class="msg" role="status" aria-live="polite"></div>
        <p class="micro"><a href="<?php echo esc_url(wp_lostpassword_url(st_learn_url())); ?>">رمزم رو فراموش کردم</a></p>
      </form>
    </div>
  </div>
</section>

<?php else : ?>
<section class="learn-top">
  <div class="wrap">
    <div class="profile-card">
      <div class="p-head">
        <span class="p-av" aria-hidden="true"><?php echo esc_html(mb_substr($user->display_name, 0, 1)); ?></span>
        <div>
          <h1>سلام <?php echo esc_html($user->display_name); ?> 👋</h1>
          <p class="micro"><?php echo st_has_book($uid) ? '✅ خریدار کتاب · همهٔ دوره برات بازه' : 'عضو رایگان'; ?> · <a href="<?php echo esc_url(wp_logout_url(st_learn_url())); ?>">خروج</a></p>
        </div>
      </div>
      <div class="p-grid">
        <div class="p-box">
          <h2>سطح درک زبان بدنت</h2>
          <?php if ($lv) : ?>
            <p class="lv"><span class="lv-ic"><?php echo esc_html($lv['icon']); ?></span> <b><?php echo esc_html($lv['title']); ?></b> <small>(نمرهٔ <?php echo esc_html($persian((int) $last['score'])); ?> از <?php echo esc_html($persian(16)); ?>)</small></p>
            <p class="tip"><?php echo esc_html($lv['tip']); ?></p>
            <a class="btn ghost sm" href="<?php echo esc_url(st_quiz_url()); ?>">دوباره آزمون بده</a>
          <?php else : ?>
            <p>هنوز آزمون ندادی. ۲ دقیقه وقت بذار و سطحت رو بفهم.</p>
            <a class="btn sm" href="<?php echo esc_url(st_quiz_url()); ?>">شروع آزمون</a>
          <?php endif; ?>
        </div>
        <div class="p-box">
          <h2>پیشرفت دوره</h2>
          <p class="lv"><b id="p-count"><?php echo esc_html($persian($done)); ?></b> از <?php echo esc_html($persian($total)); ?> درس</p>
          <div class="pbar" aria-hidden="true"><i id="p-bar" style="width:<?php echo (int) $pct; ?>%"></i></div>
          <p class="micro" id="p-msg"><?php echo $done >= $total ? '🎉 کل دوره رو تموم کردی!' : 'هر درس رو که باز کنی، با یه سؤال کوتاه تموم می‌شه.'; ?></p>
        </div>
      </div>
      <?php if (!st_has_book($uid)) : ?>
      <div class="claim">
        <h2>📘 کتاب «درک زبان بدن» رو از طاقچه خریدی؟</h2>
        <?php if (is_array($claim)) : ?>
          <p class="micro">درخواستت ثبت شده و در حال بررسیه. بعد از تأیید، همهٔ دوره و آزمون‌ها همیشه برات رایگانه.</p>
        <?php else : ?>
          <p class="micro">ایمیل/شمارهٔ حساب طاقچه‌ات (یا کد سفارش) رو بنویس تا تأیید کنیم. خریداران کتاب همیشه دوره و آزمون‌ها رو رایگان می‌گیرن.</p>
          <form class="f st-claim" novalidate>
            <input type="hidden" name="action" value="st_book_claim">
            <div class="row"><input type="text" name="note" maxlength="160" placeholder="مثلاً ایمیل حساب طاقچه یا کد سفارش" aria-label="مشخصات خرید کتاب" dir="ltr" style="text-align:right"><button class="btn sm" type="submit">ثبت درخواست</button></div>
            <div class="msg" role="status" aria-live="polite"></div>
          </form>
        <?php endif; ?>
      </div>
      <?php endif; ?>
    </div>
  </div>
</section>
<?php endif; ?>

<section class="course" id="course">
  <div class="wrap">
    <h2>دورهٔ «زبان بدن در <b><?php echo esc_html($persian($total)); ?> درس کوتاه</b>»</h2>
    <p class="sec-sub">هر درس: توضیح کوتاه، یه تمرین کوچیک و یه سؤال. با جواب درست، درس ثبت می‌شه.</p>
    <div class="lessons">
    <?php foreach ($lessons as $i => $l) :
        $open = $uid && st_lesson_unlocked($i, $uid);
        $isDone = isset($progress[$l['id']]);
    ?>
      <details class="lesson<?php echo $isDone ? ' done' : ''; ?><?php echo $open ? '' : ' locked'; ?>" data-lesson="<?php echo esc_attr($l['id']); ?>">
        <summary>
          <span class="l-n"><?php echo esc_html($persian($i + 1)); ?></span>
          <span class="l-t"><b><?php echo esc_html($l['title']); ?></b><small><?php echo esc_html($l['summary']); ?></small></span>
          <span class="l-m"><?php echo esc_html($persian($l['min'])); ?> دقیقه <i class="l-s" aria-hidden="true"><?php echo $isDone ? '✓' : ($open ? '' : '🔒'); ?></i></span>
        </summary>
        <div class="l-body">
        <?php if (!$uid) : ?>
          <p>برای دیدن درس، <a href="#auth" class="to-auth">پروفایلت رو بساز</a> یا وارد شو. رایگانه.</p>
        <?php elseif (!$open) : ?>
          <p>این درس برای خریداران کتاب بازه. اگه کتاب رو از طاقچه خریدی، بالای صفحه درخواستت رو ثبت کن.</p>
        <?php else : ?>
          <?php foreach ($l['body'] as $p) : ?><p><?php echo esc_html($p); ?></p><?php endforeach; ?>
          <div class="practice"><b>🧪 تمرین</b><p><?php echo esc_html($l['practice']); ?></p></div>
          <div class="check" data-lesson="<?php echo esc_attr($l['id']); ?>">
            <b>✅ یه سؤال</b>
            <p class="q"><?php echo esc_html($l['check']['q']); ?></p>
            <div class="opts">
              <?php foreach ($l['check']['o'] as $k => $o) : ?>
                <button class="opt" type="button" data-idx="<?php echo (int) $k; ?>"><?php echo esc_html($o[0]); ?></button>
              <?php endforeach; ?>
            </div>
            <p class="fb" aria-live="polite"></p>
          </div>
        <?php endif; ?>
        </div>
      </details>
    <?php endforeach; ?>
    </div>
  </div>
</section>

</main>
<?php get_footer();
