/* Jef’s Notes — small helpers, no dependencies.
   1. Rating dots drawn from data-before / data-after.
   2. "Export as PDF" buttons (the print dialog's "Save as PDF").
   3. Quiz answers open while printing.
   4. all.html pulls every note into one printable notebook.
   5. Landing page: book spines that pull a volume out. */
(function () {
  var NAMES = ['', 'very low', 'low', 'medium', 'high', 'very high'];

  function renderRatings(root) {
    root.querySelectorAll('tr[data-after]').forEach(function (tr) {
      if (tr.dataset.done) return;
      tr.dataset.done = '1';
      var before = +tr.dataset.before, after = +tr.dataset.after;
      var cell = tr.querySelector('.dcell');
      var score = tr.querySelector('.score');
      var dots = document.createElement('span');
      dots.className = 'dots';
      dots.setAttribute('role', 'img');
      dots.setAttribute('aria-label', after + ' out of 5 with the pattern, ' + before + ' without it');
      for (var i = 1; i <= 5; i++) {
        var d = document.createElement('span');
        d.className = 'dot';
        if (i <= after && i <= before) d.className += ' on';
        else if (i <= after) d.className += ' gain';
        else if (i <= before) d.className += ' lost';
        dots.appendChild(d);
      }
      cell.appendChild(dots);
      if (score) {
        var cls = after > before ? 'up' : after < before ? 'down' : 'same';
        var sign = after > before ? '▲ +' + (after - before) : after < before ? '▼ −' + (before - after) : '= no change';
        score.innerHTML = before + ' → <b>' + after + '</b> <span class="delta ' + cls + '">' + sign + '</span>';
        score.title = NAMES[before] + ' → ' + NAMES[after];
      }
    });
  }

  var opened = [];
  function openAnswers() {
    document.querySelectorAll('.quiz details:not([open])').forEach(function (d) { d.open = true; opened.push(d); });
  }
  function restoreAnswers() { opened.forEach(function (d) { d.open = false; }); opened = []; }
  window.addEventListener('beforeprint', openAnswers);
  window.addEventListener('afterprint', restoreAnswers);

  function wirePrint(root) {
    root.querySelectorAll('[data-print]').forEach(function (btn) {
      btn.addEventListener('click', function () { openAnswers(); window.print(); });
    });
  }

  async function collect(main) {
    var urls = main.getAttribute('data-collect').trim().split(/\s+/);
    var status = document.querySelector('[data-collect-status]');
    for (var i = 0; i < urls.length; i++) {
      try {
        var res = await fetch(urls[i]);
        var html = await res.text();
        var doc = new DOMParser().parseFromString(html, 'text/html');
        var art = doc.querySelector('article.sheet');
        if (art) {
          art.querySelectorAll('[href^="../"]').forEach(function (a) { a.setAttribute('href', a.getAttribute('href').slice(3)); });
          main.appendChild(document.importNode(art, true));
        }
      } catch (e) { console.warn('Could not load', urls[i], e); }
      if (status) status.textContent = 'Loaded ' + (i + 1) + ' of ' + urls.length + ' notes…';
    }
    renderRatings(main);
    document.querySelectorAll('[data-print][disabled]').forEach(function (b) { b.disabled = false; });
    if (status) status.textContent = 'All ' + urls.length + ' notes are ready. Press “Export as PDF”.';
    if (new URLSearchParams(location.search).has('print')) {
      (document.fonts ? document.fonts.ready : Promise.resolve()).then(function () {
        setTimeout(function () { openAnswers(); window.print(); }, 300);
      });
    }
  }

  /* 5. Landing page: books stored spine-out. Click or arrow keys pull a volume out. */
  function wireSpines() {
    document.querySelectorAll('[data-spines]').forEach(function (shelf) {
      var tabs = Array.prototype.slice.call(shelf.querySelectorAll('.spine'));
      function pick(tab, focus) {
        tabs.forEach(function (t) {
          var on = t === tab;
          t.setAttribute('aria-selected', on ? 'true' : 'false');
          t.tabIndex = on ? 0 : -1;
          document.getElementById(t.getAttribute('aria-controls')).hidden = !on;
        });
        if (focus) tab.focus();
        if (tab.scrollIntoView) tab.scrollIntoView({ block: 'nearest', inline: 'nearest' });
      }
      tabs.forEach(function (t, i) {
        t.addEventListener('click', function () { pick(t, false); });
        t.addEventListener('keydown', function (e) {
          if (e.key === 'ArrowRight') { pick(tabs[(i + 1) % tabs.length], true); e.preventDefault(); }
          if (e.key === 'ArrowLeft') { pick(tabs[(i + tabs.length - 1) % tabs.length], true); e.preventDefault(); }
        });
      });
    });
  }


  /* 6. Landing page: the bookcase. Tap a series tile and its panel, with every volume, comes down.
     The choice follows the address (#deep-dives, #series-2 …) and is remembered for the next visit. */
  function wireBookcase() {
    var cases = document.querySelector('[data-bookcase]');
    if (!cases) return;
    var tabs = Array.prototype.slice.call(cases.querySelectorAll('.series-tile'));
    var panelOf = function (t) { return document.getElementById(t.getAttribute('aria-controls')); };
    function tabFor(hash) {
      if (!hash || hash.length < 2) return null;
      var el = document.getElementById(decodeURIComponent(hash.slice(1)));
      if (!el) return null;
      if (el.id === 'shelf') return null;
      var panel = el.closest ? el.closest('.series-panel') : null;
      return panel ? tabs.filter(function (t) { return panelOf(t) === panel; })[0] || null : null;
    }
    function pick(tab, opts) {
      opts = opts || {};
      tabs.forEach(function (t) {
        var on = t === tab;
        t.setAttribute('aria-selected', on ? 'true' : 'false');
        t.tabIndex = on ? 0 : -1;
        panelOf(t).hidden = !on;
      });
      try { localStorage.setItem('jef-shelf', tab.getAttribute('aria-controls')); } catch (e) {}
      if (opts.focus) tab.focus();
      if (opts.hash && history.replaceState) history.replaceState(null, '', '#' + tab.getAttribute('aria-controls'));
      if (opts.scroll) panelOf(tab).scrollIntoView({ block: 'start', behavior: 'smooth' });
    }
    tabs.forEach(function (t, i) {
      t.addEventListener('click', function () {
        pick(t, { hash: true });
        // on a phone the panel starts below the fold: bring its heading up
        var top = panelOf(t).getBoundingClientRect().top;
        if (top > window.innerHeight * 0.75) panelOf(t).scrollIntoView({ block: 'start', behavior: 'smooth' });
      });
      t.addEventListener('keydown', function (e) {
        var n = null;
        if (e.key === 'ArrowRight' || e.key === 'ArrowDown') n = tabs[(i + 1) % tabs.length];
        if (e.key === 'ArrowLeft' || e.key === 'ArrowUp') n = tabs[(i + tabs.length - 1) % tabs.length];
        if (e.key === 'Home') n = tabs[0];
        if (e.key === 'End') n = tabs[tabs.length - 1];
        if (n) { pick(n, { focus: true, hash: true }); e.preventDefault(); }
      });
    });
    function fromHash(scroll) {
      var t = tabFor(location.hash);
      if (t) { pick(t, { scroll: scroll }); return true; }
      return false;
    }
    window.addEventListener('hashchange', function () { fromHash(true); });
    if (!fromHash(true)) {
      var saved = null;
      try { saved = localStorage.getItem('jef-shelf'); } catch (e) {}
      var t = saved && tabs.filter(function (x) { return x.getAttribute('aria-controls') === saved; })[0];
      if (t) pick(t);
    }
  }

  document.addEventListener('DOMContentLoaded', function () {
    wireSpines();
    wireBookcase();
    renderRatings(document);
    wirePrint(document);
    var main = document.querySelector('[data-collect]');
    if (main) collect(main);
  });
})();
