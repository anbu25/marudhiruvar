/* Shared theme: ?theme=dark|light in the URL, else the saved choice, else dark.
   Only pages with <body data-theme-toggle> (the landing page) show the switch; other pages just follow it. */
(function () {
  var KEY = 'marudhiruvar-theme', body = document.body;
  var q = new URLSearchParams(location.search).get('theme'), saved = null;
  try { saved = localStorage.getItem(KEY); } catch (e) {}
  function norm(t) { return t === 'light' || t === 'parchment' ? 'parchment' : 'dark'; }
  var theme = norm(q || saved || 'dark');
  if (q) { try { localStorage.setItem(KEY, theme); } catch (e) {} }
  function apply() { body.classList.toggle('parchment', theme === 'parchment'); }
  apply();

  // Language: ?lang=en|ta|both in the URL, else the saved choice, else both (keeps PDFs bilingual)
  var LKEY = 'marudhiruvar-lang', lq = new URLSearchParams(location.search).get('lang'), lsaved = null;
  try { lsaved = localStorage.getItem(LKEY); } catch (e) {}
  function lnorm(l) { return l === 'en' || l === 'ta' ? l : 'both'; }
  var lang = lnorm(lq || lsaved || 'both');
  if (lq) { try { localStorage.setItem(LKEY, lang); } catch (e) {} }
  function applyLang() {
    ['en', 'ta', 'both'].forEach(function (l) { body.classList.toggle('lang-' + l, l === lang); });
    document.documentElement.lang = lang === 'ta' ? 'ta' : 'en';
  }
  applyLang();
  if (!body.hasAttribute('data-theme-toggle')) return;

  var btn = document.createElement('button');
  btn.type = 'button'; btn.className = 'theme-btn';
  function label() {
    btn.textContent = theme === 'parchment' ? '🌙' : '☀️';
    var next = theme === 'parchment' ? 'dark' : 'light';
    btn.setAttribute('aria-label', 'Switch to ' + next + ' theme'); btn.title = 'Switch to ' + next + ' theme';
  }
  btn.onclick = function () {
    theme = theme === 'parchment' ? 'dark' : 'parchment';
    try { localStorage.setItem(KEY, theme); } catch (e) {}
    apply(); label();
  };
  label();
  var bar = document.querySelector('.topbar') || body;
  var sw = document.createElement('div');
  sw.className = 'lang-sw'; sw.setAttribute('role', 'radiogroup'); sw.setAttribute('aria-label', 'Language / மொழி');
  [['en', 'English'], ['ta', 'தமிழ்'], ['both', 'EN+த']].forEach(function (o) {
    var lb = document.createElement('label'), r = document.createElement('input');
    r.type = 'radio'; r.name = 'lang'; r.value = o[0]; r.checked = lang === o[0];
    r.onchange = function () { lang = o[0]; try { localStorage.setItem(LKEY, lang); } catch (e) {} applyLang(); };
    lb.appendChild(r); lb.appendChild(document.createTextNode(o[1])); sw.appendChild(lb);
  });
  bar.appendChild(sw); bar.appendChild(btn);
})();
