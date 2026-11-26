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

  document.addEventListener('DOMContentLoaded', function () {
    wireSpines();
    renderRatings(document);
    wirePrint(document);
    var main = document.querySelector('[data-collect]');
    if (main) collect(main);
  });
})();
