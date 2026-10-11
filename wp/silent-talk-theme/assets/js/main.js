(function () {
  'use strict';
  var t0 = Date.now();

  /* UTM capture (kept for the session so later page views still attribute the lead) */
  var KEYS = ['utm_source', 'utm_medium', 'utm_campaign', 'utm_content'];
  var utm = {};
  try {
    var qs = new URLSearchParams(location.search);
    KEYS.forEach(function (k) { if (qs.get(k)) { sessionStorage.setItem(k, qs.get(k).slice(0, 80)); } });
    KEYS.forEach(function (k) { utm[k] = sessionStorage.getItem(k) || ''; });
  } catch (e) { KEYS.forEach(function (k) { utm[k] = ''; }); }

  /* lead forms */
  document.querySelectorAll('.st-form').forEach(function (form) {
    KEYS.forEach(function (k) { var i = form.querySelector('[name=' + k + ']'); if (i) { i.value = utm[k]; } });
    var land = form.querySelector('[name=landing]'); if (land) { land.value = location.pathname; }
    var msg = form.querySelector('.msg'), btn = form.querySelector('button[type=submit]');
    form.addEventListener('submit', function (ev) {
      ev.preventDefault();
      msg.className = 'msg'; msg.textContent = '';
      var name = form.name.value.trim(), contact = form.contact.value.trim();
      if (!name) { msg.className = 'msg err'; msg.textContent = 'اسمت رو بنویس.'; form.name.focus(); return; }
      if (!contact) { msg.className = 'msg err'; msg.textContent = 'ایمیل یا شمارهٔ موبایلت رو بنویس.'; form.contact.focus(); return; }
      if (!form.consent.checked) { msg.className = 'msg err'; msg.textContent = 'برای ادامه، تیک موافقت رو بزن.'; return; }
      form.elapsed.value = Date.now() - t0;
      btn.disabled = true;
      fetch(ST.ajax, { method: 'POST', body: new FormData(form), credentials: 'same-origin' })
        .then(function (r) { return r.json(); })
        .then(function (d) {
          msg.className = 'msg ' + (d.ok ? 'ok' : 'err');
          msg.textContent = d.msg || '';
          if (d.ok) {
            form.reset();
            if (d.download) {
              var a = document.createElement('a');
              a.href = d.download; a.target = '_blank'; a.rel = 'noopener'; a.className = 'btn sm'; a.textContent = 'دانلود هدیه';
              a.style.marginTop = '10px'; msg.appendChild(document.createElement('br')); msg.appendChild(a);
            }
          }
        })
        .catch(function () { msg.className = 'msg err'; msg.textContent = 'اتصال برقرار نشد. دوباره امتحان کن.'; })
        .then(function () { btn.disabled = false; });
    });
  });


  /* ---------- /quiz/ ---------- */
  var QD = window.ST && window.ST.quiz;
  if (QD && document.getElementById('q-intro')) {
    var $ = function (id) { return document.getElementById(id); };
    var screens = { intro: $('q-intro'), play: $('q-play'), result: $('q-result') };
    var i = 0, score = 0, locked = false, level = 'seed';
    var show = function (k) {
      Object.keys(screens).forEach(function (n) { screens[n].hidden = (n !== k); });
      window.scrollTo({ top: 0, behavior: 'smooth' });
    };
    var ping = function (ev, lv) {
      try {
        var fd = new FormData(); fd.append('action', 'st_quiz_event'); fd.append('ev', ev); if (lv) { fd.append('level', lv); }
        fetch(ST.ajax, { method: 'POST', body: fd, credentials: 'same-origin', keepalive: true });
      } catch (e) {}
    };
    var persian = function (n) { return String(n).replace(/\d/g, function (d) { return '۰۱۲۳۴۵۶۷۸۹'[d]; }); };
    var render = function () {
      var q = QD.questions[i]; locked = false;
      $('q-bar').style.width = ((i) / QD.questions.length * 100) + '%';
      $('q-count').textContent = 'سؤال ' + persian(i + 1) + ' از ' + persian(QD.questions.length);
      var im = $('q-img'); im.src = q.img; im.alt = q.alt;
      $('q-text').textContent = q.t;
      $('q-fb').textContent = ''; $('q-fb').className = 'fb';
      $('q-next').hidden = true;
      $('q-next').textContent = (i === QD.questions.length - 1) ? 'نتیجه رو ببین' : 'بعدی';
      var box = $('q-opts'); box.innerHTML = '';
      q.o.forEach(function (o, idx) {
        var b = document.createElement('button'); b.type = 'button'; b.className = 'opt'; b.textContent = o[0];
        b.addEventListener('click', function () { pick(idx, b); });
        box.appendChild(b);
      });
      $('q-text').focus({ preventScroll: true });
    };
    var pick = function (idx, btn) {
      if (locked) { return; } locked = true;
      var q = QD.questions[i], o = q.o[idx];
      score += o[1];
      var all = $('q-opts').querySelectorAll('.opt');
      all.forEach(function (b) { b.disabled = true; });
      var best = 0; q.o.forEach(function (x, k) { if (x[1] > q.o[best][1]) { best = k; } });
      btn.classList.add(o[1] === 2 ? 'right' : (o[1] === 1 ? 'mid' : 'wrong'));
      if (idx !== best) { all[best].classList.add('right'); }
      $('q-fb').textContent = o[2]; $('q-fb').className = 'fb show';
      $('q-next').hidden = false; $('q-next').focus({ preventScroll: true });
    };
    var finish = function () {
      var lv = QD.levels, keys = Object.keys(lv).sort(function (a, b) { return lv[a].min - lv[b].min; });
      level = keys[0]; keys.forEach(function (k) { if (score >= lv[k].min) { level = k; } });
      var L = lv[level];
      $('r-icon').textContent = L.icon;
      $('r-score').textContent = 'امتیازت: ' + persian(score) + ' از ' + persian(QD.max);
      $('r-title').textContent = L.title; $('r-text').textContent = L.text; $('r-tip').textContent = L.tip;
      var f = document.querySelector('#q-lead form');
      f.quiz_score.value = score; f.quiz_level.value = level;
      $('q-bar').style.width = '100%';
      show('result'); ping('done', level);
      var saveT = $('q-save-t'), saveA = $('q-save-a');
      try { sessionStorage.setItem('st_qs', String(score)); sessionStorage.setItem('st_ql', level); } catch (e) {}
      if (ST.user && ST.nonce) {
        var sf = new FormData(); sf.append('action', 'st_quiz_save'); sf.append('nonce', ST.nonce); sf.append('score', score); sf.append('level', level);
        fetch(ST.ajax, { method: 'POST', body: sf, credentials: 'same-origin' }).catch(function () {});
        saveT.textContent = 'نتیجه توی پروفایلت ذخیره شد ✓'; saveA.textContent = 'پروفایل و دوره'; 
      } else { saveT.textContent = 'می‌خوای نتیجه‌ات ذخیره بشه و دورهٔ کوتاه رو رایگان شروع کنی؟'; }
    };
    $('q-start').addEventListener('click', function () { i = 0; score = 0; show('play'); render(); ping('start'); });
    $('q-next').addEventListener('click', function () { i++; if (i >= QD.questions.length) { finish(); } else { render(); window.scrollTo({ top: 0, behavior: 'smooth' }); } });
    $('q-again').addEventListener('click', function () { show('intro'); });
    $('q-share').addEventListener('click', function () {
      var L = QD.levels[level], text = 'من تو آزمون زبان بدن شدم «' + L.title + '» ' + L.icon + ' تو چی می‌شی؟';
      var base = (ST && ST.quizUrl) ? ST.quizUrl : (location.origin + '/quiz/');
      var url = base + (base.indexOf('?') > -1 ? '&' : '?') + 'utm_source=share&utm_medium=quiz&utm_campaign=result';
      if (navigator.share) { navigator.share({ title: document.title, text: text, url: url }).catch(function () {}); }
      else if (navigator.clipboard) { navigator.clipboard.writeText(text + ' ' + url).then(function () { $('q-share').textContent = 'لینک کپی شد ✓'; }); }
    });
  }


  /* /learn/ : auth tabs, register/login, book claim, lesson checks */
  var auth = document.getElementById('auth');
  if (auth) {
    var tabs = auth.querySelectorAll('.tab'), forms = auth.querySelectorAll('form[data-form]');
    tabs.forEach(function (tb) {
      tb.addEventListener('click', function () {
        tabs.forEach(function (x) { var on = x === tb; x.classList.toggle('on', on); x.setAttribute('aria-selected', on ? 'true' : 'false'); });
        forms.forEach(function (f) { f.hidden = f.getAttribute('data-form') !== tb.getAttribute('data-tab'); });
      });
    });
    var qs0 = '', ql0 = '';
    try { qs0 = sessionStorage.getItem('st_qs') || ''; ql0 = sessionStorage.getItem('st_ql') || ''; } catch (e) {}
    auth.querySelectorAll('form').forEach(function (form) {
      KEYS.forEach(function (k) { var i = form.querySelector('[name=' + k + ']'); if (i) { i.value = utm[k]; } });
      if (form.quiz_score) { form.quiz_score.value = qs0; form.quiz_level.value = ql0; }
      var msg = form.querySelector('.msg'), btn = form.querySelector('button[type=submit]');
      form.addEventListener('submit', function (ev) {
        ev.preventDefault(); msg.className = 'msg'; msg.textContent = '';
        var reg = form.getAttribute('data-form') === 'reg';
        if (reg && !form.name.value.trim()) { msg.className = 'msg err'; msg.textContent = 'اسمت رو بنویس.'; form.name.focus(); return; }
        var idf = reg ? form.email : form.email;
        if (!idf.value.trim()) { msg.className = 'msg err'; msg.textContent = 'ایمیلت رو بنویس.'; idf.focus(); return; }
        if (!form.password.value) { msg.className = 'msg err'; msg.textContent = 'رمز عبور رو بنویس.'; form.password.focus(); return; }
        if (reg && form.password.value.length < 8) { msg.className = 'msg err'; msg.textContent = 'رمز عبور حداقل ۸ نویسه باشد.'; return; }
        if (reg && !form.consent.checked) { msg.className = 'msg err'; msg.textContent = 'برای ادامه، تیک موافقت رو بزن.'; return; }
        form.elapsed.value = Date.now() - t0; btn.disabled = true;
        fetch(ST.ajax, { method: 'POST', body: new FormData(form), credentials: 'same-origin' })
          .then(function (r) { return r.json(); })
          .then(function (d) {
            msg.className = 'msg ' + (d.ok ? 'ok' : 'err'); msg.textContent = d.msg || (d.ok ? 'انجام شد' : 'خطا');
            if (d.ok && d.redirect) { location.href = d.redirect; }
          })
          .catch(function () { msg.className = 'msg err'; msg.textContent = 'اتصال برقرار نشد. دوباره امتحان کن.'; })
          .then(function () { btn.disabled = false; });
      });
    });
  }
  document.querySelectorAll('.to-auth').forEach(function (a) { a.addEventListener('click', function () { var t = document.getElementById('auth'); if (t) { t.scrollIntoView({ behavior: 'smooth' }); } }); });

  var claim = document.querySelector('form.st-claim');
  if (claim) {
    var cm = claim.querySelector('.msg');
    claim.addEventListener('submit', function (ev) {
      ev.preventDefault(); cm.className = 'msg';
      var fd = new FormData(claim); fd.append('nonce', ST.nonce || '');
      fetch(ST.ajax, { method: 'POST', body: fd, credentials: 'same-origin' }).then(function (r) { return r.json(); })
        .then(function (d) { cm.className = 'msg ' + (d.ok ? 'ok' : 'err'); cm.textContent = d.msg || ''; })
        .catch(function () { cm.className = 'msg err'; cm.textContent = 'اتصال برقرار نشد.'; });
    });
  }

  document.querySelectorAll('.check').forEach(function (box) {
    var fbx = box.querySelector('.fb'), btns = box.querySelectorAll('.opt'), lesson = box.getAttribute('data-lesson');
    btns.forEach(function (b) {
      b.addEventListener('click', function () {
        var fd = new FormData(); fd.append('action', 'st_lesson_check'); fd.append('nonce', ST.nonce || ''); fd.append('lesson', lesson); fd.append('answer', b.getAttribute('data-idx'));
        btns.forEach(function (x) { x.disabled = true; });
        fetch(ST.ajax, { method: 'POST', body: fd, credentials: 'same-origin' }).then(function (r) { return r.json(); })
          .then(function (d) {
            if (!d.ok) { fbx.className = 'fb err'; fbx.textContent = d.msg || 'خطا'; btns.forEach(function (x) { x.disabled = false; }); return; }
            fbx.className = 'fb ' + (d.correct ? 'ok' : 'err'); fbx.textContent = (d.correct ? '✓ ' : '✗ ') + d.feedback;
            b.classList.add(d.correct ? 'right' : 'wrong');
            if (d.correct) {
              var det = box.closest('details'); det.classList.add('done'); var s = det.querySelector('.l-s'); if (s) { s.textContent = '✓'; }
              var pc = document.getElementById('p-count'), pb = document.getElementById('p-bar'), pm = document.getElementById('p-msg');
              var P = String(d.done).replace(/\d/g, function (x) { return '۰۱۲۳۴۵۶۷۸۹'[x]; });
              if (pc) { pc.textContent = P; } if (pb) { pb.style.width = Math.round(d.done / d.total * 100) + '%'; }
              if (pm && d.done >= d.total) { pm.textContent = '🎉 کل دوره رو تموم کردی!'; }
            } else { btns.forEach(function (x) { x.disabled = false; x.classList.remove('wrong'); }); }
          })
          .catch(function () { fbx.className = 'fb err'; fbx.textContent = 'اتصال برقرار نشد.'; btns.forEach(function (x) { x.disabled = false; }); });
      });
    });
  });

  /* sample lesson quiz */
  var quiz = document.getElementById('quiz');
  if (quiz) {
    var correct = parseInt(quiz.getAttribute('data-correct'), 10);
    var fb = document.getElementById('quiz-fb');
    var opts = quiz.querySelectorAll('.opt');
    opts.forEach(function (o, i) {
      o.addEventListener('click', function () {
        opts.forEach(function (x) { x.disabled = true; });
        o.classList.add(i === correct ? 'right' : 'wrong');
        if (i !== correct) { opts[correct].classList.add('right'); }
        fb.textContent = o.getAttribute('data-fb');
      });
    });
  }

  /* gentle reveal */
  var els = document.querySelectorAll('.rv');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } });
    }, { threshold: .12 });
    els.forEach(function (e) { io.observe(e); });
  } else { els.forEach(function (e) { e.classList.add('in'); }); }
})();
