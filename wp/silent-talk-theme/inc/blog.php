<?php
/**
 * Blog: /blog/ index, single articles, SEO meta + JSON-LD, one-time idempotent importer of the starter articles,
 * Jalali dates, and the gifts helper (first-20 counter).
 */
if (!defined('ABSPATH')) { exit; }

require_once get_template_directory() . '/inc/articles-data.php';

/* ---------- helpers ---------- */
function st_fa($n) { return strtr((string) $n, ['0'=>'۰','1'=>'۱','2'=>'۲','3'=>'۳','4'=>'۴','5'=>'۵','6'=>'۶','7'=>'۷','8'=>'۸','9'=>'۹']); }
function st_blog_url() { return get_option('permalink_structure') ? home_url('/blog/') : home_url('/?st_blog=1'); }
function st_jdate($ts) {
    $g = [31,28,31,30,31,30,31,31,30,31,30,31]; $gy = (int) gmdate('Y', $ts); $gm = (int) gmdate('n', $ts); $gd = (int) gmdate('j', $ts);
    $jm = ['فروردین','اردیبهشت','خرداد','تیر','مرداد','شهریور','مهر','آبان','آذر','دی','بهمن','اسفند'];
    $gy2 = $gy - 1600; $gm2 = $gm - 1; $gd2 = $gd - 1;
    $gdn = 365 * $gy2 + intdiv($gy2 + 3, 4) - intdiv($gy2 + 99, 100) + intdiv($gy2 + 399, 400);
    for ($i = 0; $i < $gm2; $i++) { $gdn += $g[$i]; }
    if ($gm2 > 1 && (($gy % 4 == 0 && $gy % 100 != 0) || ($gy % 400 == 0))) { $gdn++; }
    $gdn += $gd2; $jdn = $gdn - 79; $jnp = intdiv($jdn, 12053); $jdn %= 12053;
    $jy = 979 + 33 * $jnp + 4 * intdiv($jdn, 1461); $jdn %= 1461;
    if ($jdn >= 366) { $jy += intdiv($jdn - 1, 365); $jdn = ($jdn - 1) % 365; }
    for ($i = 0; $i < 11 && $jdn >= ($i < 6 ? 31 : 30); $i++) { $jdn -= ($i < 6 ? 31 : 30); }
    return st_fa($jdn + 1) . ' ' . $jm[$i] . ' ' . st_fa($jy);
}
function st_reading_time($post = null) {
    $t = trim(wp_strip_all_tags(get_post_field('post_content', $post)));
    $w = $t === '' ? 0 : count(preg_split('/\s+/u', $t));
    return max(1, (int) ceil($w / 180));
}
function st_post_desc($id) {
    $d = get_post_meta($id, '_st_desc', true);
    if (!$d) { $d = has_excerpt($id) ? get_the_excerpt($id) : wp_trim_words(wp_strip_all_tags(get_post_field('post_content', $id)), 30, '…'); }
    return wp_strip_all_tags($d);
}

/* ---------- routes ---------- */
add_action('init', function () {
    add_rewrite_rule('^blog/page/([0-9]+)/?$', 'index.php?st_blog=1&paged=$matches[1]', 'top');
    add_rewrite_rule('^blog/?$', 'index.php?st_blog=1', 'top');
});
add_filter('query_vars', function ($v) { $v[] = 'st_blog'; return $v; });
add_filter('template_include', function ($t) {
    if (get_query_var('st_blog')) { return get_template_directory() . '/blog.php'; }
    return $t;
});
add_filter('pre_get_document_title', function ($t) {
    if (get_query_var('st_blog')) { return 'وبلاگ زبان بدن و ارتباط غیرکلامی | گفتگوهای خاموش'; }
    return $t;
}, 12);
add_filter('body_class', function ($c) { if (get_query_var('st_blog')) { $c[] = 'st-blog-page'; } return $c; });
add_action('pre_get_posts', function ($q) {
    if ($q->is_main_query() && !is_admin() && $q->get('st_blog')) { $q->set('post_type', 'post'); $q->set('ignore_sticky_posts', true); $q->set('posts_per_page', 9); }
});
add_filter('excerpt_length', function () { return 32; });
add_filter('excerpt_more', function () { return '…'; });

// posts live under /blog/<slug>/ (one-time; pages and the custom routes are unaffected)
add_action('init', function () {
    if (get_option('st_blog_perma') === '1') { return; }
    global $wp_rewrite;
    $cur = get_option('permalink_structure');
    if ($cur && strpos($cur, '/blog/') !== 0) { $wp_rewrite->set_permalink_structure('/blog/%postname%/'); }
    update_option('st_blog_perma', '1', false);
    update_option('st_rewrite_v', '', false); // force one rewrite flush at priority 99 (see inc/quiz.php)
}, 5);

/* ---------- SEO: description, Open Graph, JSON-LD ---------- */
add_action('wp_head', function () {
    $name = get_bloginfo('name') ?: 'گفتگوهای خاموش';
    $logo = get_template_directory_uri() . '/assets/img/og.png';
    if (is_singular('post')) {
        $id = get_the_ID(); $desc = st_post_desc($id); $title = get_the_title($id); $url = get_permalink($id);
        $img = get_the_post_thumbnail_url($id, 'large') ?: $logo;
        echo '<meta name="description" content="' . esc_attr($desc) . '">' . "\n";
        echo '<meta property="og:type" content="article"><meta property="og:locale" content="fa_IR">' . "\n";
        echo '<meta property="og:title" content="' . esc_attr($title) . '"><meta property="og:description" content="' . esc_attr($desc) . '">' . "\n";
        echo '<meta property="og:url" content="' . esc_url($url) . '"><meta property="og:image" content="' . esc_url($img) . '">' . "\n";
        echo '<meta property="article:published_time" content="' . esc_attr(get_post_time('c', true, $id)) . '">' . "\n";
        echo '<meta name="twitter:card" content="summary_large_image">' . "\n";
        $cats = get_the_category($id);
        $ld = ['@context' => 'https://schema.org', '@graph' => [
            ['@type' => 'Article', 'headline' => $title, 'description' => $desc, 'inLanguage' => 'fa', 'image' => [$img],
             'datePublished' => get_post_time('c', true, $id), 'dateModified' => get_post_modified_time('c', true, $id),
             'author' => ['@type' => 'Organization', 'name' => $name, 'url' => home_url('/')],
             'publisher' => ['@type' => 'Organization', 'name' => $name, 'logo' => ['@type' => 'ImageObject', 'url' => $logo]],
             'mainEntityOfPage' => $url, 'articleSection' => $cats ? $cats[0]->name : 'زبان بدن'],
            ['@type' => 'BreadcrumbList', 'itemListElement' => [
                ['@type' => 'ListItem', 'position' => 1, 'name' => 'خانه', 'item' => home_url('/')],
                ['@type' => 'ListItem', 'position' => 2, 'name' => 'وبلاگ', 'item' => st_blog_url()],
                ['@type' => 'ListItem', 'position' => 3, 'name' => $title, 'item' => $url]]],
        ]];
        echo '<script type="application/ld+json">' . wp_json_encode($ld, JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES) . '</script>' . "\n";
    } elseif (get_query_var('st_blog') || is_category() || is_tag()) {
        $desc = 'مقاله‌های کوتاه و بدون خرافه دربارهٔ زبان بدن، ارتباط غیرکلامی، لبخند، مصاحبهٔ شغلی، جلسه و قرار؛ با مثال‌های واقعی و روش «خط پایه».';
        echo '<meta name="description" content="' . esc_attr($desc) . '">' . "\n";
        echo '<meta property="og:type" content="website"><meta property="og:locale" content="fa_IR"><meta property="og:title" content="وبلاگ زبان بدن | ' . esc_attr($name) . '">' . "\n";
        echo '<meta property="og:description" content="' . esc_attr($desc) . '"><meta property="og:image" content="' . esc_url($logo) . '">' . "\n";
        $ld = ['@context' => 'https://schema.org', '@type' => 'Blog', 'name' => 'وبلاگ ' . $name, 'url' => st_blog_url(), 'inLanguage' => 'fa', 'description' => $desc];
        echo '<script type="application/ld+json">' . wp_json_encode($ld, JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES) . '</script>' . "\n";
    }
}, 5);

/* ---------- gifts helper: how many of the first-20 slots are taken ---------- */
function st_gift_info() {
    $max = 20; $start = (int) get_option('st_gift_start', 0);
    if (!$start) { return ['max' => $max, 'taken' => 0, 'left' => $max, 'live' => false]; }
    $ids = get_users(['role__not_in' => ['administrator', 'editor', 'author'], 'fields' => 'ID', 'number' => 200,
        'date_query' => [['after' => gmdate('Y-m-d H:i:s', $start), 'inclusive' => true]]]);
    $taken = min($max, count($ids));
    return ['max' => $max, 'taken' => $taken, 'left' => $max - $taken, 'live' => true];
}

/* ---------- one-time importer: starter articles (idempotent, runs from wp-admin) ---------- */
function st_sideload_theme_image($file, $title) {
    $src = get_template_directory() . '/assets/img/blog/' . $file;
    if (!file_exists($src)) { return 0; }
    $up = wp_upload_dir();
    if (!empty($up['error'])) { return 0; }
    $name = wp_unique_filename($up['path'], $file);
    $dest = trailingslashit($up['path']) . $name;
    if (!copy($src, $dest)) { return 0; }
    $att = wp_insert_attachment(['post_mime_type' => 'image/jpeg', 'post_title' => $title, 'post_status' => 'inherit', 'post_content' => ''], $dest);
    if (is_wp_error($att) || !$att) { return 0; }
    require_once ABSPATH . 'wp-admin/includes/image.php';
    wp_update_attachment_metadata($att, wp_generate_attachment_metadata($att, $dest));
    update_post_meta($att, '_wp_attachment_image_alt', $title);
    return (int) $att;
}
function st_import_articles() {
    if (get_option('st_articles_v') === '1' || !function_exists('st_articles_data')) { return 0; }
    if (!get_option('st_gift_start')) { update_option('st_gift_start', time(), false); }
    $made = 0; $all = true; $list = st_articles_data(); $n = count($list);
    foreach ($list as $i => $a) {
        $exists = get_posts(['post_type' => 'post', 'name' => $a['slug'], 'post_status' => 'any', 'numberposts' => 1, 'fields' => 'ids']);
        if ($exists) { continue; }
        $cover = st_sideload_theme_image($a['slug'] . '-cover.jpg', $a['title']);
        $info = st_sideload_theme_image($a['slug'] . '-info.jpg', $a['title'] . ' (خلاصه)');
        $imgtag = $info ? '<img src="' . esc_url(wp_get_attachment_url($info)) . '" alt="' . esc_attr($a['title'] . ' (خلاصه)') . '" width="1200" height="900" loading="lazy">' : '';
        $body = strtr($a['body'], ['{{img}}' => $imgtag, '{{quiz}}' => st_quiz_url(), '{{pro}}' => st_quiz_url('pro'), '{{learn}}' => st_learn_url(), '{{blog}}' => st_blog_url()]);
        $term = term_exists($a['cat'], 'category');
        if (!$term) { $term = wp_insert_term($a['cat'], 'category'); }
        $cid = is_array($term) ? (int) $term['term_id'] : (int) $term;
        $ts = time() - ($n - $i) * 2 * DAY_IN_SECONDS + $i * 3600;
        $id = wp_insert_post(['post_type' => 'post', 'post_status' => 'publish', 'post_name' => $a['slug'], 'post_title' => $a['title'],
            'post_content' => $body, 'post_excerpt' => $a['excerpt'], 'post_category' => $cid ? [$cid] : [], 'tags_input' => $a['tags'],
            'post_date_gmt' => gmdate('Y-m-d H:i:s', $ts), 'post_date' => get_date_from_gmt(gmdate('Y-m-d H:i:s', $ts)), 'comment_status' => 'closed'], true);
        if (is_wp_error($id) || !$id) { $all = false; continue; }
        update_post_meta($id, '_st_desc', $a['desc']);
        update_post_meta($id, '_st_article', $a['slug']);
        if ($cover) { set_post_thumbnail($id, $cover); }
        $made++;
    }
    // the default sample post would show up on the blog: move it to drafts (reversible)
    foreach (['hello-world', 'سلام-دنیا'] as $sample) {
        foreach (get_posts(['post_type' => 'post', 'post_status' => 'publish', 'numberposts' => 1, 'name' => $sample, 'fields' => 'ids']) as $hid) {
            if (!get_post_meta($hid, '_st_article', true)) { wp_update_post(['ID' => $hid, 'post_status' => 'draft']); }
        }
    }
    if ($all) { update_option('st_articles_v', '1', false); }
    if ($made) { set_transient('st_articles_notice', $made, 300); flush_rewrite_rules(false); }
    return $made;
}
add_action('admin_init', function () { if (current_user_can('manage_options')) { st_import_articles(); } });
add_action('after_switch_theme', function () { st_import_articles(); });
add_action('admin_notices', function () {
    $n = get_transient('st_articles_notice');
    if ($n) { delete_transient('st_articles_notice'); echo '<div class="notice notice-success is-dismissible"><p>قالب گفتگوهای خاموش: ' . esc_html(st_fa($n)) . ' مقالهٔ آموزشی منتشر شد (بخش «نوشته‌ها»). هر زمان خواستید از همان‌جا ویرایش یا پیش‌نویس‌شان کنید.</p></div>'; }
});
