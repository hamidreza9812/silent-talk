<?php
/** Quiz: data, /quiz/ route, anonymous funnel counters. */
if (!defined('ABSPATH')) { exit; }

function st_quiz_data($set = 'basic') {
    if ($set === 'pro') { return st_quiz_pro_data(); }
    $img = get_template_directory_uri() . '/assets/img/';
    $q = [
        ['img' => 'quiz-1.jpg', 'alt' => 'سارا با لب‌های به‌هم‌فشرده و نگاه پایین',
         't' => 'دوستت می‌گه «خوبم!» ولی لب‌هاش به‌هم فشرده‌ست و نگاهش رو به پایینه. چی می‌گی؟',
         'o' => [
            ['باشه، پس بریم یه چیز بخوریم!', 1, 'مهربونانه‌ست، ولی سرنخ‌ها رو نادیده گرفتی. بد نیست یه در باز بذاری.'],
            ['مطمئنی؟ دروغ نگو‌ها!', 0, 'فشار می‌ذاره و آدم رو می‌بنده. سرنخ فقط یه فرضیه‌ست، نه حکم.'],
            ['اگه خواستی حرف بزنی، من هستم.', 2, 'عالی! بدون بازجویی، در رو باز گذاشتی.']]],
        ['img' => 'quiz-2.jpg', 'alt' => 'کاندیدایی که فنجان را با دو دست محکم گرفته',
         't' => 'تو مصاحبه‌ای. کاندیدا فنجان رو با هر دو دست محکم گرفته و ابروهاش نگرانه. نتیجه‌ات؟',
         'o' => [
            ['این آدم صلاحیت نداره.', 0, 'عجله‌ای بود. استرس با ناتوانی فرق داره.'],
            ['احتمالاً استرس داره. یه کم فضا می‌دم و سؤال رو راحت‌تر می‌پرسم.', 2, 'دقیقاً. نشونه‌ها رو «استرس» خوندی و واکنش آروم انتخاب کردی.'],
            ['نشونهٔ ضعفه؛ ولی بقیهٔ جواب‌هاش رو هم می‌بینم.', 1, 'خوبه که صبر می‌کنی. فقط «ضعف» برچسب سنگینیه.']]],
        ['img' => 'quiz-3.jpg', 'alt' => 'مردی که فقط با دهان لبخند می‌زند',
         't' => 'مشتری می‌گه «جالبه!» و این‌جوری لبخند می‌زنه: فقط دهان، بدون چین کنار چشم. چیکار می‌کنی؟',
         'o' => [
            ['حتماً می‌خره! قیمت رو بالا می‌برم.', 0, 'زود بود. این لبخند اغلب مودبانه‌ست.'],
            ['نتیجه نمی‌گیرم؛ یه سؤال باز می‌پرسم: «کدوم بخشش هنوز مبهمه؟»', 2, 'آفرین! فرضیه ساختی و با سؤال امتحانش می‌کنی.'],
            ['پس دروغ می‌گه.', 0, 'بعضی‌ها ذاتاً کم‌لبخندن. «دروغ» حکم سنگینیه.']]],
        ['img' => 'quiz-4.jpg', 'alt' => 'همان مرد با لبخند واقعی و چین کنار چشم',
         't' => 'حالا همین مرد این‌جوری لبخند می‌زنه. چه فرقی با قبلی داره؟',
         'o' => [
            ['هیچ فرقی نداره.', 0, 'فرق داره: چشم‌ها هم می‌خندن.'],
            ['چشم‌ها هم می‌خندن (چین کنار چشم) و تغییر چهره نرم و تدریجیه.', 2, 'درسته! این معمولاً لبخند واقعی‌تره. اما هنوز یه سرنخه، نه حکم.'],
            ['فقط دندون‌هاش بیشتر پیداست.', 1, 'نصفه‌نیمه. اصل ماجرا، چشم‌ها و نرمیِ تغییره.']]],
        ['img' => 'quiz-5.jpg', 'alt' => 'دو همکار در جلسه؛ یکی دست‌هایش را در هم قفل کرده',
         't' => 'مشتری توی جلسه دست‌هاش رو توی هم قفل کرده و آروم نشسته. چی می‌تونی نتیجه بگیری؟',
         'o' => [
            ['حتماً مخالفه.', 0, 'دست‌های قفل‌شده می‌تونه یعنی تمرکز، عادت یا احتیاط.'],
            ['هنوز چیزی نمی‌شه گفت؛ ببینم بقیهٔ حالتش با این هماهنگه یا نه.', 2, 'همینه! یه نشونه کافی نیست؛ دنبال «خوشه» باش.'],
            ['شاید تردید داره.', 1, 'ممکنه، ولی تا نشونهٔ دوم نیاد فقط یه فرضیه‌ست.']]],
        ['img' => 'quiz-6.jpg', 'alt' => 'سارا و نیما کنار هم',
         't' => 'اولین قدم برای خوندن نشونه‌های یه نفر چیه؟',
         'o' => [
            ['یه حرکت خاصش رو بگیرم و نتیجه بگیرم.', 0, 'یه حرکت تنها معنای روشنی نداره.'],
            ['ببینم رفتار همیشگیِ خودِ همین آدم چه‌جوریه.', 2, 'عالی! به این می‌گن «خط پایه»؛ مهم‌ترین قدم.'],
            ['ببینم چقدر لبخند می‌زنه.', 1, 'لبخند یه نشونه‌ست، ولی باید با رفتار عادی خودش مقایسه بشه.']]],
        ['img' => 'quiz-7.jpg', 'alt' => 'دو همکار؛ یکی دست‌ها را روی هم گذاشته',
         't' => 'همکارت دست‌هاش رو روی هم گذاشته و کمی عقب وایساده. ولی اتاق سرده! چی فکر می‌کنی؟',
         'o' => [
            ['حتماً حالت دفاعی داره.', 0, 'زمینه رو فراموش کردی؛ سرما هم همین حالت رو می‌سازه.'],
            ['شاید فقط سردشه. شرایط رو هم می‌بینم.', 2, 'آفرین! «زمینه» رو دیدی.'],
            ['نمی‌شه هیچی گفت.', 1, 'محتاط بودی، ولی می‌شه با کمی دقت بیشتر فرضیه ساخت.']]],
        ['img' => 'quiz-8.jpg', 'alt' => 'دو دوست در کافه',
         't' => 'آخرین سؤال! به نظرت زبان بدن می‌تونه ذهن آدم‌ها رو بخونه؟',
         'o' => [
            ['آره، دروغ رو صددرصد می‌گیره.', 0, 'نه! هیچ نشونه‌ای قطعی نیست.'],
            ['نه؛ سرنخ می‌ده و باید با یه سؤال خوب امتحانش کنم.', 2, 'دقیقاً همین نگاه، فرق آدم دقیق و آدم عجول رو می‌سازه.'],
            ['نمی‌دونم.', 1, 'اشکال نداره! همین‌جاست که یادگیری شروع می‌شه.']]],
    ];
    foreach ($q as &$x) { $x['img'] = $img . $x['img']; }
    $levels = [
        'seed'   => ['min' => 0,  'icon' => '🌱', 'title' => 'کنجکاوِ تازه‌کار',
                     'text' => 'تازه شروع کردی و این عالیه! بیشتر وقت‌ها اولین حدس رو باور می‌کنی. با سه تا سؤال ساده می‌شه خیلی دقیق‌تر شد.',
                     'tip'  => 'قدم بعدی: قبل از هر قضاوت بپرس «رفتار همیشگیِ این آدم چه‌جوریه؟»'],
        'grow'   => ['min' => 6,  'icon' => '👀', 'title' => 'ناظرِ در حال رشد',
                     'text' => 'چشمت باز شده و نشونه‌ها رو می‌بینی. گاهی هنوز یه نشونهٔ تنها رو بزرگ می‌کنی یا زمینه رو کم می‌بینی.',
                     'tip'  => 'قدم بعدی: دنبال «خوشهٔ نشونه‌ها» باش، نه یه حرکت تنها.'],
        'sharp'  => ['min' => 11, 'icon' => '🎯', 'title' => 'خوانندهٔ دقیق',
                     'text' => 'نگاهت دقیق و محتاطه. نشونه‌ها رو فرضیه می‌بینی و با سؤال امتحانشون می‌کنی. فقط کمی تمرین روی موقعیت‌های سخت‌تر مونده.',
                     'tip'  => 'قدم بعدی: تمرین روی موقعیت‌های واقعی مثل مصاحبه و جلسه.'],
        'master' => ['min' => 15, 'icon' => '🦎', 'title' => 'آفتاب‌پرستِ مهربان',
                     'text' => 'عالی! دقیق می‌بینی، عجله نمی‌کنی و مهربون می‌پرسی. دقیقاً همون چیزی که ما دنبالشیم.',
                     'tip'  => 'قدم بعدی: به بقیه هم یاد بده و موقعیت‌های پیچیده‌تر رو تمرین کن.'],
    ];
    return ['questions' => $q, 'levels' => $levels, 'max' => 16];
}

add_action('init', function () {
    add_rewrite_rule('^quiz/pro/?$', 'index.php?st_quiz=2', 'top');
    add_rewrite_rule('^quiz/?$', 'index.php?st_quiz=1', 'top');
});

/** Which quiz set the current request shows: 'pro' for /quiz/pro/, otherwise 'basic'. */
function st_quiz_set() { return (string) get_query_var('st_quiz') === '2' ? 'pro' : 'basic'; }
/** Every level of every quiz set (used to validate stored results). */
function st_quiz_levels() { return st_quiz_data('basic')['levels'] + st_quiz_data('pro')['levels']; }
add_filter('query_vars', function ($v) { $v[] = 'st_quiz'; return $v; });
add_filter('template_include', function ($t) {
    if (get_query_var('st_quiz')) { nocache_headers(); return get_template_directory() . '/quiz.php'; }
    return $t;
});
add_filter('pre_get_document_title', function ($t) {
    if (!get_query_var('st_quiz')) { return $t; }
    return st_quiz_set() === 'pro' ? 'آزمون پیشرفته: خوشه‌ها، زمینه و پرسش | گفتگوهای خاموش' : 'آزمون: سطح درک زبان بدنت چقدره؟ | گفتگوهای خاموش';
});
add_action('after_switch_theme', function () { flush_rewrite_rules(); });
add_action('init', function () {
    // self-heal once if the theme was uploaded without re-activation
    if (get_option('st_rewrite_v') !== ST_VER) { flush_rewrite_rules(false); update_option('st_rewrite_v', ST_VER, false); }
}, 99);
add_filter('body_class', function ($c) { if (get_query_var('st_quiz')) { $c[] = 'st-quiz-page'; } return $c; });

/* anonymous funnel counters (no personal data): started / completed per level */
add_action('wp_ajax_nopriv_st_quiz_event', 'st_quiz_event');
add_action('wp_ajax_st_quiz_event', 'st_quiz_event');
function st_quiz_event() {
    $key = 'st_qe_' . md5(st_client_hash());
    $n = (int) get_transient($key);
    if ($n >= 30) { wp_send_json(['ok' => true]); }
    set_transient($key, $n + 1, HOUR_IN_SECONDS);
    $ev = isset($_POST['ev']) ? sanitize_key($_POST['ev']) : '';
    $lv = isset($_POST['level']) ? sanitize_key($_POST['level']) : '';
    $levels = array_keys(st_quiz_levels());
    $c = get_option('st_quiz_counts', ['start' => 0, 'done' => 0, 'levels' => []]);
    if ($ev === 'start') { $c['start']++; }
    elseif ($ev === 'done' && in_array($lv, $levels, true)) { $c['done']++; $c['levels'][$lv] = (isset($c['levels'][$lv]) ? $c['levels'][$lv] : 0) + 1; }
    else { wp_send_json(['ok' => false], 400); }
    update_option('st_quiz_counts', $c, false);
    wp_send_json(['ok' => true]);
}

/** Quiz URL that also works when pretty permalinks are off. */
function st_quiz_url($set = 'basic') {
    if ($set === 'pro') { return get_option('permalink_structure') ? home_url('/quiz/pro/') : home_url('/?st_quiz=2'); }
    return get_option('permalink_structure') ? home_url('/quiz/') : home_url('/?st_quiz=1');
}
