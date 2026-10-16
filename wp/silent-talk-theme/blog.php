<?php
/** /blog/ index, category and tag archives (template loaded by inc/blog.php; archive.php reuses it) */
if (!defined('ABSPATH')) { exit; }
get_header();
$is_arch = is_category() || is_tag();
$title = $is_arch ? single_term_title('', false) : 'وبلاگ زبان بدن';
$cats = get_categories(['hide_empty' => true, 'orderby' => 'count', 'order' => 'DESC', 'exclude' => [get_option('default_category')]]);
?>
<main id="main" class="blog-page">
<section class="blog-hero">
  <div class="wrap">
    <span class="kicker">وبلاگ گفتگوهای خاموش</span>
    <h1><?php echo $is_arch ? esc_html($title) : 'زبان بدن، <b>بدون خرافه</b>'; ?></h1>
    <p class="lead"><?php echo $is_arch ? 'مقاله‌های این موضوع' : 'مقاله‌های کوتاه با مثال‌های واقعی دربارهٔ ارتباط غیرکلامی: جلسه، مصاحبه، قرار و گفتگوی روزمره. هیچ نشانه‌ای قطعی نیست؛ دقیق‌تر ببین و مهربان‌تر بپرس.'; ?></p>
    <?php if ($cats) : ?>
    <nav class="chips" aria-label="دسته‌بندی">
      <a class="chip<?php echo !$is_arch ? ' on' : ''; ?>" href="<?php echo esc_url(st_blog_url()); ?>">همه</a>
      <?php foreach ($cats as $c) : ?><a class="chip<?php echo (is_category($c->term_id)) ? ' on' : ''; ?>" href="<?php echo esc_url(get_category_link($c)); ?>"><?php echo esc_html($c->name); ?></a><?php endforeach; ?>
    </nav>
    <?php endif; ?>
  </div>
</section>
<section class="blog-list">
  <div class="wrap">
  <?php if (have_posts()) : ?>
    <div class="grid g3 posts">
    <?php while (have_posts()) : the_post(); $cat = get_the_category(); ?>
      <article <?php post_class('card post-card'); ?>>
        <a class="pc-img" href="<?php the_permalink(); ?>" tabindex="-1" aria-hidden="true"><?php if (has_post_thumbnail()) { the_post_thumbnail('large', ['loading' => 'lazy', 'alt' => '']); } ?></a>
        <div class="pc-body">
          <?php if ($cat) : ?><a class="pc-cat" href="<?php echo esc_url(get_category_link($cat[0])); ?>"><?php echo esc_html($cat[0]->name); ?></a><?php endif; ?>
          <h2><a href="<?php the_permalink(); ?>"><?php the_title(); ?></a></h2>
          <p><?php echo esc_html(get_the_excerpt()); ?></p>
          <div class="pc-meta"><span><?php echo esc_html(st_jdate(get_post_time('U', true))); ?></span><span><?php echo esc_html(st_fa(st_reading_time())); ?> دقیقه مطالعه</span></div>
        </div>
      </article>
    <?php endwhile; ?>
    </div>
    <?php
    $links = paginate_links(['prev_text' => 'قبلی', 'next_text' => 'بعدی', 'type' => 'array']);
    if ($links) { echo '<nav class="pager" aria-label="صفحه‌بندی">' . implode('', $links) . '</nav>'; }
    ?>
  <?php else : ?>
    <p>هنوز مقاله‌ای منتشر نشده. به‌زودی!</p>
  <?php endif; ?>
  </div>
</section>
<section class="alt cta-final">
  <div class="wrap">
    <h2>بخوانی یا <b>امتحان کنی؟</b></h2>
    <p class="sec-sub" style="margin-inline:auto">آزمون ۲ دقیقه‌ای ببین سطحت کجاست؛ بعد با دورهٔ ۸ درسی پله‌پله جلو برو.</p>
    <p><a class="btn big" href="<?php echo esc_url(st_quiz_url()); ?>">شروع آزمون</a> <a class="btn big ghost" href="<?php echo esc_url(home_url('/#gifts')); ?>">هدیه‌ها را ببین</a></p>
  </div>
</section>
</main>
<?php get_footer();
