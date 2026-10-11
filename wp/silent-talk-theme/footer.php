<?php if (!defined('ABSPATH')) { exit; } ?>
<footer class="site-footer">
  <div class="wrap">
    <div>© <?php echo esc_html(date_i18n('Y')); ?> گفتگوهای خاموش · Silent Talk</div>
    <div>
      <?php
      $links = ['اینستاگرام' => st_opt('st_instagram'), 'لینکدین' => st_opt('st_linkedin'), 'تلگرام/ایتا' => st_opt('st_telegram'), 'طاقچه' => st_opt('st_book_url')];
      $out = [];
      foreach ($links as $label => $url) {
          if ($url) { $out[] = '<a href="' . esc_url($url) . '" rel="noopener" target="_blank">' . esc_html($label) . '</a>'; }
      }
      echo implode(' · ', $out); // phpcs:ignore WordPress.Security.EscapeOutput
      ?>
    </div>
  </div>
</footer>
<?php wp_footer(); ?>
</body>
</html>
