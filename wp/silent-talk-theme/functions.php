<?php
/**
 * Silent Talk theme: setup, customizer links, lead capture (CPT + AJAX + CSV + REST stats).
 */
if (!defined('ABSPATH')) { exit; }

define('ST_VER', '1.3.0');
require_once get_template_directory() . '/inc/quiz.php';
require_once get_template_directory() . '/inc/quiz-pro.php';
require_once get_template_directory() . '/inc/learn.php';

/* ---------- setup ---------- */
add_action('after_setup_theme', function () {
    add_theme_support('title-tag');
    add_theme_support('post-thumbnails');
    add_theme_support('html5', ['search-form', 'comment-form', 'comment-list', 'gallery', 'caption', 'style', 'script']);
});

add_filter('language_attributes', function ($out) {
    $out = preg_replace('/\s(dir|lang)="[^"]*"/', '', $out);
    return trim($out) . ' lang="fa-IR" dir="rtl"';
});

add_action('wp_enqueue_scripts', function () {
    $dir = get_template_directory();
    wp_enqueue_style('silent-talk', get_stylesheet_uri(), [], filemtime($dir . '/style.css'));
    wp_enqueue_script('silent-talk', get_template_directory_uri() . '/assets/js/main.js', [], filemtime($dir . '/assets/js/main.js'), ['in_footer' => true, 'strategy' => 'defer']);
    $st = ['ajax' => admin_url('admin-ajax.php'), 'learnUrl' => st_learn_url(), 'user' => is_user_logged_in()];
    if (is_user_logged_in()) { $st['nonce'] = wp_create_nonce('st_learn'); }
    if (get_query_var('st_quiz')) { $st['quiz'] = st_quiz_data(st_quiz_set()); $st['quizUrl'] = st_quiz_url(st_quiz_set()); }
    wp_localize_script('silent-talk', 'ST', $st);
});

add_action('wp_head', function () {
    if (!is_front_page() && !get_query_var('st_quiz') && !get_query_var('st_learn')) { return; }
    $desc = get_query_var('st_learn') ? 'پروفایل یادگیری، سطح آزمون و دورهٔ کوتاه زبان بدن در ۸ درس.' : (get_query_var('st_quiz') ? 'هشت موقعیت واقعی، دو دقیقه: ببین سطح درک زبان بدنت چقدره.' : 'زبان بدن رو قدم‌به‌قدم و بدون خرافه یاد بگیر: آزمون دو دقیقه‌ای، درس‌های تصویری کوتاه و فهرست انتظار دوره.');
    echo '<meta name="description" content="' . esc_attr($desc) . '">' . "\n";
    echo '<meta property="og:type" content="website"><meta property="og:locale" content="fa_IR">' . "\n";
    echo '<meta property="og:title" content="' . esc_attr(get_bloginfo('name')) . ' | گفتگوهای خاموش">' . "\n";
    echo '<meta property="og:description" content="' . esc_attr($desc) . '">' . "\n";
    echo '<meta property="og:image" content="' . esc_url(get_template_directory_uri() . '/assets/img/og.png') . '">' . "\n";
    $ld = [
        '@context' => 'https://schema.org',
        '@type' => 'Book',
        'name' => 'درک زبان بدن',
        'inLanguage' => 'fa',
        'author' => ['@type' => 'Person', 'name' => 'Scott Rouse'],
        'translator' => ['@type' => 'Person', 'name' => 'حامد کاظمی'],
        'url' => st_opt('st_book_url'),
    ];
    echo '<script type="application/ld+json">' . wp_json_encode($ld, JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES) . '</script>' . "\n";
}, 5);

/* ---------- customizer: links shown on the landing page ---------- */
function st_defaults() {
    return [
        'st_book_url'   => 'https://taaghche.com/book/337335/%D8%AF%D8%B1%DA%A9-%D8%B2%D8%A8%D8%A7%D9%86-%D8%A8%D8%AF%D9%86',
        'st_instagram'  => '',
        'st_linkedin'   => '',
        'st_telegram'   => '',
        'st_magnet_url' => '',
        'st_contact'    => '',
    ];
}
function st_opt($key) {
    $d = st_defaults();
    return get_theme_mod($key, isset($d[$key]) ? $d[$key] : '');
}
add_action('customize_register', function ($wp) {
    $wp->add_section('st_links', ['title' => 'لینک‌های گفتگوهای خاموش', 'priority' => 30]);
    $fields = [
        'st_book_url'   => 'لینک کتاب در طاقچه',
        'st_instagram'  => 'لینک صفحهٔ اینستاگرام',
        'st_linkedin'   => 'لینک صفحهٔ لینکدین',
        'st_telegram'   => 'لینک کانال تلگرام/ایتا (اختیاری)',
        'st_magnet_url' => 'لینک دانلود هدیهٔ رایگان (PDF) پس از عضویت',
        'st_contact'    => 'ایمیل یا شمارهٔ تماس برای کارگاه سازمانی',
    ];
    foreach ($fields as $id => $label) {
        $wp->add_setting($id, ['default' => st_defaults()[$id], 'sanitize_callback' => 'sanitize_text_field']);
        $wp->add_control($id, ['label' => $label, 'section' => 'st_links', 'type' => 'text']);
    }
});

/* ---------- lead post type (not public; admin UI only) ---------- */
add_action('init', function () {
    register_post_type('st_lead', [
        'labels' => ['name' => 'لیدها', 'singular_name' => 'لید', 'menu_name' => 'لیدها', 'all_items' => 'همهٔ لیدها'],
        'public' => false, 'show_ui' => true, 'show_in_menu' => true, 'menu_icon' => 'dashicons-email-alt',
        'supports' => ['title'], 'capability_type' => 'post', 'capabilities' => ['create_posts' => 'do_not_allow'], 'map_meta_cap' => true,
    ]);
});

add_filter('manage_st_lead_posts_columns', function ($c) {
    return ['cb' => $c['cb'], 'title' => 'نام', 'st_contact' => 'تماس', 'st_interest' => 'علاقه', 'st_quiz' => 'آزمون', 'st_source' => 'منبع / کمپین', 'date' => 'تاریخ'];
});
add_action('manage_st_lead_posts_custom_column', function ($col, $id) {
    if ($col === 'st_contact') { echo esc_html(get_post_meta($id, 'contact', true)); }
    if ($col === 'st_interest') { echo esc_html(st_interest_label(get_post_meta($id, 'interest', true))); }
    if ($col === 'st_quiz') {
        $lv = get_post_meta($id, 'quiz_level', true); $d = st_quiz_levels();
        echo $lv && isset($d[$lv]) ? esc_html($d[$lv]['title'] . ' (' . get_post_meta($id, 'quiz_score', true) . ')') : '';
    }
    if ($col === 'st_source') {
        echo esc_html(trim(get_post_meta($id, 'utm_source', true) . ' / ' . get_post_meta($id, 'utm_campaign', true), ' /'));
    }
}, 10, 2);
add_filter('views_edit-st_lead', function ($views) {
    $url = wp_nonce_url(admin_url('admin-post.php?action=st_export'), 'st_export');
    $views['st_export'] = '<a href="' . esc_url($url) . '">⬇ خروجی CSV</a>';
    return $views;
});

function st_interest_label($k) {
    $m = ['quiz' => 'آزمون', 'book' => 'کتاب', 'course' => 'دورهٔ تعاملی', 'workshop' => 'کارگاه', 'corporate' => 'کارگاه سازمانی'];
    return isset($m[$k]) ? $m[$k] : '';
}

/* ---------- lead capture ---------- */
function st_client_hash() {
    $ip = isset($_SERVER['REMOTE_ADDR']) ? sanitize_text_field(wp_unslash($_SERVER['REMOTE_ADDR'])) : '';
    return wp_hash($ip);
}
function st_digits_en($s) {
    return strtr($s, ['۰'=>'0','۱'=>'1','۲'=>'2','۳'=>'3','۴'=>'4','۵'=>'5','۶'=>'6','۷'=>'7','۸'=>'8','۹'=>'9','٠'=>'0','١'=>'1','٢'=>'2','٣'=>'3','٤'=>'4','٥'=>'5','٦'=>'6','٧'=>'7','٨'=>'8','٩'=>'9']);
}
function st_normalize_contact($raw) {
    $raw = trim(st_digits_en(sanitize_text_field($raw)));
    if (is_email($raw)) { return strtolower(sanitize_email($raw)); }
    $n = preg_replace('/[\s\-()]/', '', $raw);
    if (preg_match('/^(?:\+98|0098|98|0)?(9\d{9})$/', $n, $m)) { return '0' . $m[1]; }
    return '';
}
function st_fail($msg, $code = 400) { wp_send_json(['ok' => false, 'msg' => $msg], $code); }

add_action('wp_ajax_nopriv_st_submit_lead', 'st_submit_lead');
add_action('wp_ajax_st_submit_lead', 'st_submit_lead');
function st_submit_lead() {
    // honeypot + minimum fill time (stops most bots; no nonce so page caching cannot break the form)
    if (!empty($_POST['website'])) { wp_send_json(['ok' => true, 'msg' => 'ثبت شد.']); }
    $ms = isset($_POST['elapsed']) ? (int) $_POST['elapsed'] : 0;
    if ($ms < 2000) { st_fail('چند ثانیه صبر کن و دوباره امتحان کن.'); }
    $ref = isset($_SERVER['HTTP_REFERER']) ? wp_parse_url(wp_unslash($_SERVER['HTTP_REFERER']), PHP_URL_HOST) : '';
    $self = wp_parse_url(home_url(), PHP_URL_HOST);
    if ($ref && $self && strcasecmp($ref, $self) !== 0) { st_fail('درخواست نامعتبر است.', 403); }

    $key = 'st_rl_' . md5(st_client_hash());
    $count = (int) get_transient($key);
    if ($count >= 8) { st_fail('تعداد تلاش‌ها زیاد بود. کمی بعد دوباره امتحان کن.', 429); }
    set_transient($key, $count + 1, HOUR_IN_SECONDS);

    $name = mb_substr(sanitize_text_field(wp_unslash(isset($_POST['name']) ? $_POST['name'] : '')), 0, 60);
    $contact = st_normalize_contact(wp_unslash(isset($_POST['contact']) ? $_POST['contact'] : ''));
    $interest = isset($_POST['interest']) ? sanitize_key($_POST['interest']) : 'book';
    if (!in_array($interest, ['quiz', 'book', 'course', 'workshop', 'corporate'], true)) { $interest = 'course'; }
    if ($name === '') { st_fail('اسمت رو بنویس.'); }
    if ($contact === '') { st_fail('ایمیل یا شمارهٔ موبایل معتبر بنویس (مثل ۰۹۱۲۱۲۳۴۵۶۷).'); }
    if (empty($_POST['consent'])) { st_fail('برای ادامه، تیک موافقت رو بزن.'); }

    $qs = isset($_POST['quiz_score']) ? max(0, min(20, (int) $_POST['quiz_score'])) : -1;
    $ql = isset($_POST['quiz_level']) ? sanitize_key($_POST['quiz_level']) : '';
    if (!in_array($ql, array_keys(st_quiz_levels()), true)) { $ql = ''; $qs = -1; }
    $existing = get_posts(['post_type' => 'st_lead', 'post_status' => 'any', 'numberposts' => 1, 'fields' => 'ids',
        'meta_key' => 'contact', 'meta_value' => $contact]);
    $magnet = esc_url_raw(st_opt('st_magnet_url'));
    $done = ['ok' => true, 'msg' => 'ثبت شد! ممنون 🙌 به‌زودی برات می‌فرستیم.', 'download' => $magnet];
    if ($existing) {
        if ($ql !== '') { update_post_meta($existing[0], 'quiz_score', $qs); update_post_meta($existing[0], 'quiz_level', $ql); }
        wp_send_json($done);
    }

    $id = wp_insert_post(['post_type' => 'st_lead', 'post_status' => 'publish', 'post_title' => $name], true);
    if (is_wp_error($id)) { st_fail('خطای موقت. دوباره تلاش کنید.', 500); }
    $meta = ['contact' => $contact, 'interest' => $interest, 'consent_at' => gmdate('c'), 'ip_hash' => st_client_hash()];
    foreach (['utm_source', 'utm_medium', 'utm_campaign', 'utm_content'] as $u) {
        $meta[$u] = mb_substr(sanitize_text_field(wp_unslash(isset($_POST[$u]) ? $_POST[$u] : '')), 0, 80);
    }
    $meta['landing'] = mb_substr(esc_url_raw(wp_unslash(isset($_POST['landing']) ? $_POST['landing'] : '')), 0, 200);
    if ($ql !== '') { $meta['quiz_score'] = $qs; $meta['quiz_level'] = $ql; }
    foreach ($meta as $k => $v) { update_post_meta($id, $k, $v); }
    wp_send_json($done);
}

/* ---------- CSV export (admin only) ---------- */
add_action('admin_post_st_export', function () {
    if (!current_user_can('manage_options')) { wp_die('دسترسی ندارید.', 403); }
    check_admin_referer('st_export');
    nocache_headers();
    header('Content-Type: text/csv; charset=utf-8');
    header('Content-Disposition: attachment; filename="silent-talk-leads-' . gmdate('Ymd') . '.csv"');
    $out = fopen('php://output', 'w');
    fwrite($out, "\xEF\xBB\xBF");
    $safe = function ($v) { $v = (string) $v; return ($v !== '' && strpos('=+-@', $v[0]) !== false) ? "'" . $v : $v; };
    fputcsv($out, ['name', 'contact', 'interest', 'quiz_score', 'quiz_level', 'utm_source', 'utm_medium', 'utm_campaign', 'utm_content', 'landing', 'date']);
    $q = new WP_Query(['post_type' => 'st_lead', 'post_status' => 'any', 'posts_per_page' => -1, 'fields' => 'ids', 'orderby' => 'date', 'order' => 'DESC']);
    foreach ($q->posts as $id) {
        fputcsv($out, [$safe(get_the_title($id)), $safe(get_post_meta($id, 'contact', true)), st_interest_label(get_post_meta($id, 'interest', true)), get_post_meta($id, 'quiz_score', true), $safe(get_post_meta($id, 'quiz_level', true)),
            $safe(get_post_meta($id, 'utm_source', true)), $safe(get_post_meta($id, 'utm_medium', true)), $safe(get_post_meta($id, 'utm_campaign', true)),
            $safe(get_post_meta($id, 'utm_content', true)), $safe(get_post_meta($id, 'landing', true)), get_the_date('c', $id)]);
    }
    fclose($out);
    exit;
});

/* ---------- REST: aggregated stats for the weekly review (no personal data) ---------- */
add_action('rest_api_init', function () {
    register_rest_route('silent-talk/v1', '/stats', [
        'methods' => 'GET',
        'permission_callback' => function () { return current_user_can('manage_options'); },
        'callback' => function () {
            $q = new WP_Query(['post_type' => 'st_lead', 'post_status' => 'any', 'posts_per_page' => 5000, 'fields' => 'ids']);
            $now = time();
            $out = ['total' => 0, 'last7' => 0, 'last30' => 0, 'by_interest' => [], 'by_source' => [], 'by_campaign' => [], 'by_content' => [], 'by_quiz_level' => [], 'quiz_funnel' => get_option('st_quiz_counts', ['start' => 0, 'done' => 0, 'levels' => []]), 'learners' => st_learner_stats(), 'daily30' => []];
            for ($i = 29; $i >= 0; $i--) { $out['daily30'][gmdate('Y-m-d', $now - $i * DAY_IN_SECONDS)] = 0; }
            foreach ($q->posts as $id) {
                $t = (int) get_post_time('U', true, $id);
                $out['total']++;
                if ($now - $t <= 7 * DAY_IN_SECONDS) { $out['last7']++; }
                if ($now - $t <= 30 * DAY_IN_SECONDS) { $out['last30']++; $d = gmdate('Y-m-d', $t); if (isset($out['daily30'][$d])) { $out['daily30'][$d]++; } }
                foreach (['by_quiz_level' => 'quiz_level', 'by_interest' => 'interest', 'by_source' => 'utm_source', 'by_campaign' => 'utm_campaign', 'by_content' => 'utm_content'] as $bucket => $meta) {
                    $v = get_post_meta($id, $meta, true); $v = $v === '' ? '(direct)' : $v;
                    $out[$bucket][$v] = isset($out[$bucket][$v]) ? $out[$bucket][$v] + 1 : 1;
                }
            }
            return $out;
        },
    ]);
});

/* ---------- helper: lead form markup (used twice on the landing page) ---------- */
function st_lead_form($id, $title, $sub, $btn = 'عضویت رایگان') {
    ?>
    <div class="lead-card" id="<?php echo esc_attr($id); ?>">
        <h2><?php echo esc_html($title); ?></h2>
        <p class="sub"><?php echo esc_html($sub); ?></p>
        <form class="f st-form" novalidate>
            <div class="hp" aria-hidden="true"><label>وب‌سایت<input type="text" name="website" tabindex="-1" autocomplete="off"></label></div>
            <input type="hidden" name="action" value="st_submit_lead">
            <input type="hidden" name="elapsed" value="0">
            <?php foreach (['utm_source', 'utm_medium', 'utm_campaign', 'utm_content', 'landing'] as $h) : ?>
                <input type="hidden" name="<?php echo esc_attr($h); ?>" value="">
            <?php endforeach; ?>
            <div><label for="<?php echo esc_attr($id); ?>-n">نام</label>
                <input id="<?php echo esc_attr($id); ?>-n" type="text" name="name" autocomplete="given-name" required maxlength="60"></div>
            <div><label for="<?php echo esc_attr($id); ?>-c">ایمیل یا شمارهٔ موبایل</label>
                <input id="<?php echo esc_attr($id); ?>-c" type="text" name="contact" inputmode="email" autocomplete="email" required dir="ltr" style="text-align:right"></div>
            <div><label for="<?php echo esc_attr($id); ?>-i">بیشتر دنبال چه هستی؟</label>
                <select id="<?php echo esc_attr($id); ?>-i" name="interest">
                    <option value="book">کتاب «درک زبان بدن»</option>
                    <option value="course" selected>دورهٔ تعاملی (فهرست انتظار)</option>
                    <option value="workshop">کارگاه زندهٔ آنلاین</option>
                    <option value="corporate">کارگاه برای تیم یا شرکت</option>
                </select></div>
            <label class="chk"><input type="checkbox" name="consent" value="1" required>
                <span>موافقم که نام و راه تماسم برای ارسال درس‌های کوتاه و خبر دوره‌ها استفاده شود. هر زمان می‌توانم انصراف دهم.</span></label>
            <button class="btn" type="submit"><?php echo esc_html($btn); ?></button>
            <div class="msg" role="status" aria-live="polite"></div>
            <p class="micro">اسپم نمی‌فرستیم. اطلاعات شما فقط برای همین منظور نگه‌داری می‌شود.</p>
        </form>
    </div>
    <?php
}
