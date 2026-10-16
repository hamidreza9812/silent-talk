<?php
/** Landing page */
get_header();
$img = get_template_directory_uri() . '/assets/img/';
$book = st_opt('st_book_url');
?>
<main id="main">

<section class="hero">
  <div class="wrap">
    <div>
      <span class="kicker">گفتگوهای خاموش · Silent Talk</span>
      <h1>قبل از اینکه حرف بزنن، <b>بدنشون</b> گفته!</h1>
      <p class="lead">زبان بدن رو با داستون‌های تصویری و تمرین‌های کوتاه یاد بگیر؛ برای گپ روزمره، قرار اول، مصاحبه و جلسه‌های کاری. بدون خرافه و بدون ذهن‌خوانی.</p>
      <div class="hero-cta">
        <a class="btn big" href="<?php echo esc_url(st_quiz_url()); ?>" id="hero-quiz">آزمون ۲ دقیقه‌ای رو شروع کن</a>
        <a class="btn ghost" href="#try">یه نمونه سؤال</a>
      </div>
      <p class="micro">۸ موقعیت واقعی · بدون ثبت‌نام · می‌فهمی سطحت چیه</p>
    </div>
    <div class="hero-art rv"><img src="<?php echo esc_url($img . 'hero.jpg'); ?>" width="1100" height="1375" alt="دو دوست در کافه؛ یکی می‌گوید «خوبم» ولی لب‌هایش فشرده و دستش روی بازویش است"></div>
  </div>
</section>

<section class="alt" id="where">
  <div class="wrap">
    <h2>این مهارت کجا <b>به کارت میاد؟</b></h2>
    <p class="sec-sub">هر گفتگو دو لایه داره: چیزی که گفته می‌شه و چیزی که بدن‌ها می‌گن. لایهٔ دوم رو که یاد بگیری، تصمیم‌هات دقیق‌تر می‌شه.</p>
    <div class="grid g4">
      <div class="card rv"><div class="ico">☕</div><h3>گپ روزمره</h3><p>بفهم کِی «خوبم» واقعاً یعنی خوب، و کِی وقتشه مهربون بپرسی.</p></div>
      <div class="card rv"><div class="ico">💬</div><h3>قرار و رابطه</h3><p>نشونه‌های علاقه و ناراحتی رو ببین و واکنش مناسب رو انتخاب کن.</p></div>
      <div class="card rv"><div class="ico">🎯</div><h3>مصاحبهٔ شغلی</h3><p>چه مصاحبه‌گر باشی چه مصاحبه‌شونده: استرس رو از ناتوانی جدا کن.</p></div>
      <div class="card rv"><div class="ico">🤝</div><h3>جلسه و فروش</h3><p>موافقت رو از تعارف تشخیص بده و لبخند مودبانه رو از علاقهٔ واقعی.</p></div>
    </div>
  </div>
</section>

<section id="method">
  <div class="wrap">
    <h2>قبل از قضاوت، <b>سه تا سؤال</b> بپرس</h2>
    <p class="sec-sub">هیچ نشونه‌ای قطعی نیست. قرار نیست ذهن‌خوانی کنیم؛ قراره بهتر ببینیم و مهربون‌تر بپرسیم.</p>
    <div class="grid g3">
      <div class="card rv"><span class="n">۱</span><h3>معمولاً چه‌جوریه؟</h3><p>رفتار همیشگیِ خودِ همین آدم رو در نظر بگیر. تغییر نسبت به همون معنا داره، نه یه حرکت تنها.</p></div>
      <div class="card rv"><span class="n">۲</span><h3>فقط یه نشونه‌ست؟</h3><p>یه نشونه کافی نیست. دنبال چند تا نشونهٔ هم‌جهت باش.</p></div>
      <div class="card rv"><span class="n">۳</span><h3>شرایط چیه؟</h3><p>سرما، خستگی، فرهنگ و عادت رو کنار بذار؛ بعد نتیجه بگیر.</p></div>
    </div>
  </div>
</section>

<section class="alt" id="try">
  <div class="wrap quiz">
    <figure class="rv"><img src="<?php echo esc_url($img . 'quiz-3.jpg'); ?>" width="900" height="1125" alt="مردی که فقط با دهان لبخند می‌زند" loading="lazy"></figure>
    <div>
      <h2>یه سؤال نمونه؛ <b>همین الان</b></h2>
      <p class="q-t">جلسهٔ فروشه. مشتری می‌گه «جالبه!» و این‌جوری لبخند می‌زنه. چیکار می‌کنی؟</p>
      <div class="opts" id="quiz" data-correct="1">
        <button class="opt" type="button" data-fb="زوده! لبخندِ فقط روی دهان همیشه علاقه نیست؛ ممکنه تعارف باشه.">«حتماً می‌خره!» و قیمت رو بالا می‌برم</button>
        <button class="opt" type="button" data-fb="درسته! لبخند فقط روی دهانه و چین کنار چشم‌ها نیست؛ فرضیه می‌سازه، نه حکم. با یه سؤال باز امتحانش کن: «کدوم بخشش هنوز مبهمه؟»">نتیجه نمی‌گیرم؛ یه سؤال باز می‌پرسم</button>
        <button class="opt" type="button" data-fb="خیلی سریع! بعضی‌ها ذاتاً کم‌لبخندن. قبل از قضاوت، رفتار عادی و شرایط رو هم ببین.">«پس دروغ می‌گه» و جلسه رو تموم می‌کنم</button>
      </div>
      <p class="fb" id="quiz-fb" aria-live="polite"></p>
      <a class="btn" href="<?php echo esc_url(st_quiz_url()); ?>">۷ سؤال دیگه هم داریم</a>
    </div>
  </div>
</section>

<section id="path" class="ladder">
  <div class="wrap">
    <h2>مسیر یادگیری، <b>پله‌پله</b></h2>
    <p class="sec-sub">از یه آزمون کوچیک شروع کن؛ هر وقت آماده بودی، بالاتر برو.</p>
    <div class="grid g4">
      <div class="card rv"><span class="tag">آماده</span><h3>آزمون سطح‌سنج</h3><p>۸ موقعیت واقعی، ۲ دقیقه. می‌فهمی الان کجایی و قدم بعدی چیه.</p><a class="btn sm" href="<?php echo esc_url(st_quiz_url()); ?>">شروع آزمون</a> <a class="btn sm ghost" href="<?php echo esc_url(st_quiz_url('pro')); ?>">نسخهٔ پیشرفته</a></div>
      <div class="card rv"><span class="tag">آماده</span><h3>داستان‌های تصویری</h3><p>داستون‌های کوتاه با سه تا سرنخ و یه درس؛ هر هفته توی پیج.</p><?php if (st_opt('st_instagram')) : ?><a class="btn sm" href="<?php echo esc_url(st_opt('st_instagram')); ?>" rel="noopener" target="_blank">ببین توی اینستاگرام</a><?php else : ?><a class="btn sm ghost" href="#join">خبرم کن</a><?php endif; ?></div>
      <div class="card rv"><span class="tag">آماده</span><h3>دورهٔ ۸ درسی</h3><p>درس‌های کوتاه با تمرین و سؤال، با پروفایل یادگیری. فعلاً رایگان.</p><a class="btn sm" href="<?php echo esc_url(st_learn_url()); ?>">ورود به دوره</a></div>
      <div class="card rv"><span class="tag">به‌زودی</span><h3>کارگاه زندهٔ آنلاین</h3><p>تمرین گروهی روی موقعیت‌های واقعی؛ برای تیم‌ها و شرکت‌ها هم برگزار می‌شه.</p><a class="btn sm ghost" href="#join">اطلاع‌رسانی</a></div>
    </div>
  </div>
</section>

<section class="dark" id="inside">
  <div class="wrap book">
    <img class="rv" src="<?php echo esc_url($img . 'book-cover.png'); ?>" width="538" height="867" alt="جلد کتاب درک زبان بدن">
    <div>
      <h2>کتابی که <b>همهٔ این ماجرا</b> ازش شروع شد</h2>
      <p class="sec-sub" style="opacity:.85">«درک زبان بدن» نوشتهٔ اسکات رُز (Scott Rouse) با ترجمهٔ حامد کاظمی. اگه بعد از آزمون دوست داشتی عمیق‌تر بری، این‌جا هر فصل یه موقعیت واقعیه.</p>
      <ol class="ch" style="color:var(--ink)">
        <li><b>۱</b> درک موارد پایه‌ای</li>
        <li><b>۲</b> آماده‌سازی: مشاهده‌ی درست</li>
        <li><b>۳</b> تمرین روی دوستان و اعضای خانواده</li>
        <li><b>۴</b> رمزگشایی پیام‌های پنهان یک قرار ملاقات عاشقانه</li>
        <li><b>۵</b> تفسیر زبان بدن در یک مصاحبه‌ی کاری</li>
        <li><b>۶</b> تسلط بر منظره‌ی محل کار</li>
      </ol>
      <a class="btn" href="<?php echo esc_url($book); ?>" rel="noopener" target="_blank">کتاب رو توی طاقچه ببین</a>
    </div>
  </div>
</section>

<section class="faq" id="faq">
  <div class="wrap">
    <h2>سؤال‌های <b>پرتکرار</b></h2>
    <details><summary>با زبان بدن می‌شه دروغ رو قطعی فهمید؟</summary><p>نه. نشونه‌ها فرضیه می‌سازن، نه حکم. برای همین روش ما سه تا سؤال داره: رفتار همیشگی، چند نشونهٔ هم‌جهت و شرایط. و آخرش یه سؤال خوب، فرضیه رو امتحان می‌کنه.</p></details>
    <details><summary>آزمون چقدر طول می‌کشه؟ باید ثبت‌نام کنم؟</summary><p>حدود ۲ دقیقه و بدون ثبت‌نام. فقط اگه آخرش خواستی تحلیل کامل برات بیاد، اسمت رو می‌نویسی.</p></details>
    <details><summary>دورهٔ تعاملی کی میاد؟</summary><p>داریم می‌سازیمش. با عضویت توی فهرست انتظار، اولین نفراتی هستی که خبردار می‌شی.</p></details>
    <details><summary>برای شرکت‌ها هم کارگاه دارید؟</summary><p>بله! از فرم پایین صفحه «کارگاه برای تیم یا شرکت» رو انتخاب کن<?php if (st_opt('st_contact')) : ?> یا با <?php echo esc_html(st_opt('st_contact')); ?> تماس بگیر<?php endif; ?>.</p></details>
  </div>
</section>

<section class="alt cta-final" id="join">
  <div class="wrap">
    <h2>هنوز <b>آزمون</b> رو نزدی؟</h2>
    <p class="sec-sub" style="margin-inline:auto">دو دقیقه وقت بذار و ببین سطحت چیه. اگه هم دوست داشتی، درس‌های کوتاه و خبر دوره رو برات بفرستیم:</p>
    <p style="margin-bottom:28px"><a class="btn big" href="<?php echo esc_url(st_quiz_url()); ?>">شروع آزمون</a></p>
    <?php st_lead_form('lead-final', 'درس‌های کوتاه و خبر دوره', 'اسم و راه تماست رو بنویس.', 'عضویت رایگان'); ?>
  </div>
</section>

</main>
<?php get_footer();
