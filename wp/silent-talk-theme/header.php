<?php if (!defined('ABSPATH')) { exit; } ?><!doctype html>
<html <?php language_attributes(); ?>>
<head>
<meta charset="<?php bloginfo('charset'); ?>">
<meta name="viewport" content="width=device-width, initial-scale=1">
<?php wp_head(); ?>
</head>
<body <?php body_class(); ?>>
<?php wp_body_open(); ?>
<header class="site-header">
  <div class="wrap">
    <a class="brand" href="<?php echo esc_url(home_url('/')); ?>"><i></i>گفتگوهای خاموش</a>
    <nav class="nav" aria-label="منوی اصلی">
      <a href="<?php echo esc_url(home_url('/#method')); ?>">روش</a>
      <a href="<?php echo esc_url(home_url('/#try')); ?>">سؤال نمونه</a>
      <a href="<?php echo esc_url(home_url('/#path')); ?>">مسیر یادگیری</a>
      <a href="<?php echo esc_url(home_url('/#faq')); ?>">پرسش‌ها</a>
      <a class="keep" href="<?php echo esc_url(st_learn_url()); ?>"><?php echo is_user_logged_in() ? 'پروفایل من' : 'ورود / ثبت‌نام'; ?></a>
      <a class="btn sm" href="<?php echo esc_url(st_quiz_url()); ?>">آزمون سطح‌سنج</a>
    </nav>
  </div>
</header>
