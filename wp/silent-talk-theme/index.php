<?php
/** Fallback template (blog/posts/pages). The landing page is front-page.php. */
get_header(); ?>
<main class="page-body"><div class="wrap">
<?php if (have_posts()) : while (have_posts()) : the_post(); ?>
  <article <?php post_class(); ?> style="margin-bottom:48px">
    <h1 style="font-size:34px;margin-bottom:16px"><a href="<?php the_permalink(); ?>" style="text-decoration:none"><?php the_title(); ?></a></h1>
    <div><?php is_singular() ? the_content() : the_excerpt(); ?></div>
  </article>
<?php endwhile; else : ?>
  <h1 style="font-size:34px">صفحه پیدا نشد</h1>
  <p style="margin-top:12px"><a class="btn sm" href="<?php echo esc_url(home_url('/')); ?>">بازگشت به خانه</a></p>
<?php endif; ?>
</div></main>
<?php get_footer();
