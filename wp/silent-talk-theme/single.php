<?php
/** Single article */
if (!defined('ABSPATH')) { exit; }
get_header();
?>
<main id="main" class="article-page">
<?php while (have_posts()) : the_post(); $cat = get_the_category(); $pid = get_the_ID(); ?>
<article <?php post_class('article'); ?>>
  <header class="a-head">
    <div class="wrap narrow">
      <nav class="crumbs" aria-label="مسیر"><a href="<?php echo esc_url(home_url('/')); ?>">خانه</a> › <a href="<?php echo esc_url(st_blog_url()); ?>">وبلاگ</a><?php if ($cat) : ?> › <a href="<?php echo esc_url(get_category_link($cat[0])); ?>"><?php echo esc_html($cat[0]->name); ?></a><?php endif; ?></nav>
      <h1><?php the_title(); ?></h1>
      <p class="a-meta"><?php echo esc_html(st_jdate(get_post_time('U', true))); ?> · <?php echo esc_html(st_fa(st_reading_time())); ?> دقیقه مطالعه · گفتگوهای خاموش</p>
    </div>
  </header>
  <?php if (has_post_thumbnail()) : ?><div class="wrap narrow"><figure class="a-cover"><?php the_post_thumbnail('large', ['alt' => get_the_title()]); ?></figure></div><?php endif; ?>
  <div class="wrap narrow">
    <div class="prose"><?php the_content(); ?></div>

    <aside class="a-cta" aria-label="قدم بعدی">
      <h2>این‌ها را امتحان کن</h2>
      <p>خواندن کافی نیست؛ تمرین لازم است. با یک آزمون دو دقیقه‌ای شروع کن و بعد درس‌های کوتاه دوره را بخوان.</p>
      <p class="a-btns"><a class="btn" href="<?php echo esc_url(st_quiz_url()); ?>">آزمون ۲ دقیقه‌ای</a> <a class="btn ghost" href="<?php echo esc_url(st_learn_url()); ?>">پروفایل و دورهٔ ۸ درسی</a> <a class="btn ghost" href="<?php echo esc_url(home_url('/#gifts')); ?>">🎁 هدیه‌ها</a></p>
    </aside>
  </div>
</article>

<?php
$rel = new WP_Query(['post_type' => 'post', 'posts_per_page' => 3, 'post__not_in' => [$pid], 'ignore_sticky_posts' => true,
    'category__in' => $cat ? [$cat[0]->term_id] : []]);
if ($rel->post_count < 3) { $rel = new WP_Query(['post_type' => 'post', 'posts_per_page' => 3, 'post__not_in' => [$pid], 'ignore_sticky_posts' => true]); }
if ($rel->have_posts()) : ?>
<section class="alt related"><div class="wrap">
  <h2>بخوان <b>بعدی</b></h2>
  <div class="grid g3 posts">
  <?php while ($rel->have_posts()) : $rel->the_post(); ?>
    <article class="card post-card">
      <a class="pc-img" href="<?php the_permalink(); ?>" tabindex="-1" aria-hidden="true"><?php if (has_post_thumbnail()) { the_post_thumbnail('medium_large', ['loading' => 'lazy', 'alt' => '']); } ?></a>
      <div class="pc-body"><h3><a href="<?php the_permalink(); ?>"><?php the_title(); ?></a></h3>
      <div class="pc-meta"><span><?php echo esc_html(st_fa(st_reading_time())); ?> دقیقه مطالعه</span></div></div>
    </article>
  <?php endwhile; wp_reset_postdata(); ?>
  </div>
</div></section>
<?php endif; ?>
<?php endwhile; ?>
</main>
<?php get_footer();
