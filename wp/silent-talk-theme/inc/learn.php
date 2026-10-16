<?php
/** Learner profile + course (/learn/): register, login, saved quiz level, lesson progress, book-owner approval. */
if (!defined('ABSPATH')) { exit; }

require_once get_template_directory() . '/inc/course.php';

/* ---------- route ---------- */
add_action('init', function () {
    add_rewrite_rule('^learn/?$', 'index.php?st_learn=1', 'top');
});
add_filter('query_vars', function ($v) { $v[] = 'st_learn'; return $v; });
add_filter('template_include', function ($t) {
    if (get_query_var('st_learn')) { nocache_headers(); return get_template_directory() . '/learn.php'; }
    return $t;
});
add_filter('pre_get_document_title', function ($t) {
    return get_query_var('st_learn') ? 'پروفایل یادگیری و دوره | گفتگوهای خاموش' : $t;
}, 11);
add_filter('body_class', function ($c) { if (get_query_var('st_learn')) { $c[] = 'st-learn-page'; } return $c; });

function st_learn_url() {
    return get_option('permalink_structure') ? home_url('/learn/') : home_url('/?st_learn=1');
}

/* ---------- access rules ---------- */
/** Course is open to every member while we are growing the audience; flip in Customizer to gate it. */
function st_course_gated() { return (bool) get_theme_mod('st_course_gated', false); }
function st_has_book($uid) { return $uid && (get_user_meta($uid, 'st_book_owner', true) === '1' || user_can($uid, 'manage_options')); }
function st_lesson_unlocked($index, $uid) {
    if (!$uid) { return false; }
    if (!st_course_gated()) { return true; }
    return $index < 3 || st_has_book($uid);
}
function st_progress($uid) {
    $p = get_user_meta($uid, 'st_progress', true);
    $p = is_array($p) ? $p : [];
    return array_intersect_key($p, array_flip(st_course_lesson_ids()));
}

add_action('customize_register', function ($wp) {
    $wp->add_setting('st_course_gated', ['default' => false, 'sanitize_callback' => function ($v) { return (bool) $v; }]);
    $wp->add_control('st_course_gated', ['label' => 'قفل‌کردن درس ۴ تا ۸ (فقط برای خریداران کتاب)', 'section' => 'st_links', 'type' => 'checkbox']);
});

/* ---------- keep learners out of wp-admin ---------- */
add_filter('show_admin_bar', function ($show) { return current_user_can('edit_posts') ? $show : false; });
add_action('admin_init', function () {
    if (wp_doing_ajax() || current_user_can('edit_posts')) { return; }
    wp_safe_redirect(st_learn_url()); exit;
});
add_filter('login_redirect', function ($to, $req, $user) {
    if ($user instanceof WP_User && !user_can($user, 'edit_posts')) { return st_learn_url(); }
    return $to;
}, 10, 3);

/* ---------- shared guards ---------- */
function st_guard_public($bucket, $limit) {
    if (!empty($_POST['website'])) { wp_send_json(['ok' => true, 'msg' => 'انجام شد.']); }
    $ms = isset($_POST['elapsed']) ? (int) $_POST['elapsed'] : 0;
    if ($ms < 1500) { st_fail('چند ثانیه صبر کن و دوباره امتحان کن.'); }
    $ref = isset($_SERVER['HTTP_REFERER']) ? wp_parse_url(wp_unslash($_SERVER['HTTP_REFERER']), PHP_URL_HOST) : '';
    $self = wp_parse_url(home_url(), PHP_URL_HOST);
    if ($ref && $self && strcasecmp($ref, $self) !== 0) { st_fail('درخواست نامعتبر است.', 403); }
    $key = 'st_rl_' . $bucket . '_' . md5(st_client_hash());
    $n = (int) get_transient($key);
    if ($n >= $limit) { st_fail('تعداد تلاش‌ها زیاد بود. کمی بعد دوباره امتحان کن.', 429); }
    set_transient($key, $n + 1, HOUR_IN_SECONDS);
}
function st_guard_user() {
    if (!is_user_logged_in()) { st_fail('اول وارد شو.', 401); }
    if (!check_ajax_referer('st_learn', 'nonce', false)) { st_fail('صفحه را دوباره باز کن و امتحان کن.', 403); }
    return get_current_user_id();
}
function st_clean_level($l) {
    $l = sanitize_key($l);
    return in_array($l, array_keys(st_quiz_levels()), true) ? $l : '';
}
function st_store_quiz($uid, $score, $level) {
    $level = st_clean_level($level);
    if ($level === '') { return; }
    $score = max(0, min(20, (int) $score));
    update_user_meta($uid, 'st_quiz_last', ['score' => $score, 'level' => $level, 'at' => gmdate('c')]);
    $h = get_user_meta($uid, 'st_quiz_hist', true); $h = is_array($h) ? $h : [];
    $h[] = ['score' => $score, 'level' => $level, 'at' => gmdate('c')];
    update_user_meta($uid, 'st_quiz_hist', array_slice($h, -20));
}

/** Save/refresh the lead record for a registered member (dedupe by contact). */
function st_save_member_lead($name, $email, $utm) {
    $ex = get_posts(['post_type' => 'st_lead', 'post_status' => 'any', 'numberposts' => 1, 'fields' => 'ids', 'meta_key' => 'contact', 'meta_value' => $email]);
    $id = $ex ? $ex[0] : wp_insert_post(['post_type' => 'st_lead', 'post_status' => 'publish', 'post_title' => $name]);
    if (!$id || is_wp_error($id)) { return; }
    update_post_meta($id, 'contact', $email);
    update_post_meta($id, 'member', '1');
    if (!$ex) {
        update_post_meta($id, 'interest', 'course');
        update_post_meta($id, 'consent_at', gmdate('c'));
        update_post_meta($id, 'ip_hash', st_client_hash());
        foreach ($utm as $k => $v) { update_post_meta($id, $k, $v); }
    }
}

/* ---------- register / login ---------- */
add_action('wp_ajax_nopriv_st_register', 'st_register');
function st_register() {
    st_guard_public('reg', 6);
    $name = mb_substr(sanitize_text_field(wp_unslash(isset($_POST['name']) ? $_POST['name'] : '')), 0, 60);
    $email = sanitize_email(wp_unslash(isset($_POST['email']) ? $_POST['email'] : ''));
    $pass = isset($_POST['password']) ? (string) wp_unslash($_POST['password']) : '';
    if ($name === '') { st_fail('اسمت رو بنویس.'); }
    if (!is_email($email)) { st_fail('ایمیل معتبر بنویس.'); }
    if (mb_strlen($pass) < 8) { st_fail('رمز عبور حداقل ۸ نویسه باشد.'); }
    if (empty($_POST['consent'])) { st_fail('برای ادامه، تیک موافقت رو بزن.'); }
    if (email_exists($email)) { st_fail('با این ایمیل قبلاً پروفایل ساخته شده. از تب «ورود» وارد شو.'); }

    $base = sanitize_user(strstr($email, '@', true), true); $base = $base !== '' ? $base : 'learner';
    $login = $base; $i = 1;
    while (username_exists($login)) { $login = $base . $i++; }
    $uid = wp_insert_user(['user_login' => $login, 'user_email' => $email, 'user_pass' => $pass, 'display_name' => $name,
        'first_name' => $name, 'nickname' => $name, 'role' => 'subscriber', 'show_admin_bar_front' => 'false']);
    if (is_wp_error($uid)) { st_fail('خطای موقت. دوباره تلاش کن.', 500); }
    if (isset($_POST['quiz_level'])) { st_store_quiz($uid, isset($_POST['quiz_score']) ? $_POST['quiz_score'] : 0, wp_unslash($_POST['quiz_level'])); }
    $utm = [];
    foreach (['utm_source', 'utm_medium', 'utm_campaign', 'utm_content'] as $u) {
        $utm[$u] = mb_substr(sanitize_text_field(wp_unslash(isset($_POST[$u]) ? $_POST[$u] : '')), 0, 80);
    }
    st_save_member_lead($name, strtolower($email), $utm);
    wp_set_current_user($uid);
    wp_set_auth_cookie($uid, true);
    wp_send_json(['ok' => true, 'msg' => 'پروفایلت ساخته شد! 🎉', 'redirect' => st_learn_url()]);
}

add_action('wp_ajax_nopriv_st_login', 'st_login');
function st_login() {
    st_guard_public('login', 12);
    $id = sanitize_text_field(wp_unslash(isset($_POST['email']) ? $_POST['email'] : ''));
    $pass = isset($_POST['password']) ? (string) wp_unslash($_POST['password']) : '';
    if ($id === '' || $pass === '') { st_fail('ایمیل و رمز عبور رو بنویس.'); }
    $user = wp_signon(['user_login' => $id, 'user_password' => $pass, 'remember' => true], is_ssl());
    if (is_wp_error($user)) { st_fail('ایمیل یا رمز عبور درست نیست.', 401); }
    if (isset($_POST['quiz_level'])) { st_store_quiz($user->ID, isset($_POST['quiz_score']) ? $_POST['quiz_score'] : 0, wp_unslash($_POST['quiz_level'])); }
    wp_send_json(['ok' => true, 'msg' => 'خوش اومدی!', 'redirect' => st_learn_url()]);
}

/* ---------- logged-in actions ---------- */
add_action('wp_ajax_st_quiz_save', function () {
    $uid = st_guard_user();
    st_store_quiz($uid, isset($_POST['score']) ? $_POST['score'] : 0, isset($_POST['level']) ? wp_unslash($_POST['level']) : '');
    wp_send_json(['ok' => true]);
});

add_action('wp_ajax_st_lesson_check', function () {
    $uid = st_guard_user();
    $lid = isset($_POST['lesson']) ? sanitize_key($_POST['lesson']) : '';
    $ans = isset($_POST['answer']) ? (int) $_POST['answer'] : -1;
    foreach (st_course_data() as $idx => $l) {
        if ($l['id'] !== $lid) { continue; }
        if (!st_lesson_unlocked($idx, $uid)) { st_fail('این درس هنوز برای تو باز نشده.', 403); }
        $opts = $l['check']['o'];
        if (!isset($opts[$ans])) { st_fail('گزینه نامعتبر است.'); }
        $ok = (int) $opts[$ans][1] === 1;
        $p = st_progress($uid);
        if ($ok && !isset($p[$lid])) { $p[$lid] = gmdate('c'); update_user_meta($uid, 'st_progress', $p); }
        wp_send_json(['ok' => true, 'correct' => $ok, 'feedback' => $opts[$ans][2], 'done' => count($p), 'total' => count(st_course_data())]);
    }
    st_fail('درس پیدا نشد.', 404);
});

add_action('wp_ajax_st_book_claim', function () {
    $uid = st_guard_user();
    if (st_has_book($uid)) { wp_send_json(['ok' => true, 'msg' => 'قبلاً تأیید شده 🎉']); }
    $note = mb_substr(sanitize_text_field(wp_unslash(isset($_POST['note']) ? $_POST['note'] : '')), 0, 160);
    if ($note === '') { st_fail('ایمیل یا شمارهٔ حساب طاقچه‌ات (یا کد سفارش) رو بنویس.'); }
    update_user_meta($uid, 'st_book_claim', ['note' => $note, 'at' => gmdate('c')]);
    $u = get_userdata($uid);
    wp_mail(get_option('admin_email'), 'درخواست تأیید خرید کتاب', $u->display_name . ' (' . $u->user_email . ")\n" . $note . "\n\n" . admin_url('users.php?s=' . rawurlencode($u->user_email)));
    wp_send_json(['ok' => true, 'msg' => 'درخواستت ثبت شد. بعد از بررسی، همهٔ دوره برات باز می‌شه.']);
});

/* ---------- admin: users list column + approve action ---------- */
add_filter('manage_users_columns', function ($c) { $c['st_learn'] = 'یادگیری'; return $c; });
add_filter('manage_users_custom_column', function ($out, $col, $uid) {
    if ($col !== 'st_learn') { return $out; }
    $q = get_user_meta($uid, 'st_quiz_last', true);
    $lv = is_array($q) && isset(st_quiz_levels()[$q['level']]) ? st_quiz_levels()[$q['level']]['title'] . ' (' . (int) $q['score'] . ')' : '—';
    $d = count(st_progress($uid));
    $b = st_has_book($uid) ? '✅ کتاب' : (get_user_meta($uid, 'st_book_claim', true) ? '⏳ درخواست کتاب' : '');
    $html = esc_html($lv . ' · ' . $d . '/' . count(st_course_data()) . ' ' . $b);
    $claim = get_user_meta($uid, 'st_book_claim', true);
    if (is_array($claim) && !st_has_book($uid) && current_user_can('edit_users')) {
        $url = wp_nonce_url(admin_url('admin-post.php?action=st_book_approve&user=' . (int) $uid), 'st_book_approve_' . $uid);
        $html .= '<br><small>' . esc_html($claim['note']) . '</small> <a href="' . esc_url($url) . '">تأیید خرید</a>';
    }
    return $html;
}, 10, 3);
add_action('admin_post_st_book_approve', function () {
    $uid = isset($_GET['user']) ? (int) $_GET['user'] : 0;
    if (!current_user_can('edit_users')) { wp_die('دسترسی ندارید.', 403); }
    check_admin_referer('st_book_approve_' . $uid);
    if ($uid && get_userdata($uid)) { update_user_meta($uid, 'st_book_owner', '1'); }
    wp_safe_redirect(admin_url('users.php')); exit;
});

/* ---------- stats for the weekly review (no personal data) ---------- */
function st_learner_stats() {
    $ids = get_users(['role' => 'subscriber', 'fields' => 'ID', 'number' => 5000]);
    $out = ['members' => count($ids), 'with_quiz' => 0, 'book_owners' => 0, 'by_level' => [], 'lesson_done' => []];
    foreach (st_course_lesson_ids() as $l) { $out['lesson_done'][$l] = 0; }
    foreach ($ids as $uid) {
        $q = get_user_meta($uid, 'st_quiz_last', true);
        if (is_array($q)) { $out['with_quiz']++; $out['by_level'][$q['level']] = isset($out['by_level'][$q['level']]) ? $out['by_level'][$q['level']] + 1 : 1; }
        if (st_has_book($uid)) { $out['book_owners']++; }
        foreach (array_keys(st_progress($uid)) as $l) { $out['lesson_done'][$l]++; }
    }
    return $out;
}
