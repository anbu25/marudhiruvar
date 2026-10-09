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
  label(); body.appendChild(btn);
})();
