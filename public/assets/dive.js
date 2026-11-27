/* Jef’s Notes · deep dives: chapter tracking, the phone dock and chapter sheet, skim mode. No dependencies.
   The page works without this file: the contents list and the "next chapter" links are plain anchors. */
(function () {
  function init() {
    var root = document.querySelector('.dive');
    if (!root) return;
    var secs = Array.prototype.slice.call(root.querySelectorAll('section[id]'));
    var q = function (s) { return Array.prototype.slice.call(root.querySelectorAll(s)); };
    var sheet = root.querySelector('[data-sheet]'), back = root.querySelector('.sheet-back');
    var opener = root.querySelector('[data-open]');
    var prev = root.querySelector('[data-prev]'), next = root.querySelector('[data-next]');
    var count = root.querySelector('[data-count]'), current = root.querySelector('[data-current]');
    var active = -2;

    function setActive(i) {
      if (i === active) return;
      active = i;
      var shown = Math.max(i, 0);
      q('a[data-ch]').forEach(function (a) {
        if (+a.dataset.ch === i) a.setAttribute('aria-current', 'true'); else a.removeAttribute('aria-current');
      });
      var pill = root.querySelector('.strip a[aria-current]');
      if (pill && pill.scrollIntoView) pill.scrollIntoView({ block: 'nearest', inline: 'center' });
      if (count) count.textContent = i < 0 ? 'Start' : (i + 1) + ' / ' + secs.length;
      if (current) current.textContent = i < 0 ? 'Contents' : secs[shown].dataset.title;
      if (prev) { prev.href = i > 0 ? '#' + secs[i - 1].id : '#top'; prev.setAttribute('aria-disabled', i < 0 ? 'true' : 'false'); }
      if (next) {
        var last = i >= secs.length - 1;
        next.href = last ? '#' + secs[secs.length - 1].id : '#' + secs[i + 1].id;
        next.setAttribute('aria-disabled', last ? 'true' : 'false');
      }
    }

    function onScroll() {
      var line = Math.min(window.innerHeight * 0.35, 220), i = -1;
      for (var k = 0; k < secs.length; k++) { if (secs[k].getBoundingClientRect().top <= line) i = k; }
      setActive(i);
      var doc = document.documentElement, max = doc.scrollHeight - window.innerHeight;
      var pct = max > 0 ? Math.min(100, Math.max(0, (window.scrollY / max) * 100)) : 0;
      q('[data-progress]').forEach(function (b) { b.style.width = pct + '%'; });
    }
    var ticking = false;
    window.addEventListener('scroll', function () {
      if (ticking) return;
      ticking = true;
      requestAnimationFrame(function () { ticking = false; onScroll(); });
    }, { passive: true });
    window.addEventListener('resize', onScroll);
    onScroll();

    /* chapter sheet (phones) */
    function openSheet(open) {
      if (!sheet) return;
      sheet.hidden = !open; back.hidden = !open;
      opener.setAttribute('aria-expanded', open ? 'true' : 'false');
      if (open) {
        var cur = sheet.querySelector('a[aria-current]') || sheet.querySelector('a');
        if (cur) { cur.focus({ preventScroll: true }); cur.scrollIntoView({ block: 'center' }); }
      } else { opener.focus({ preventScroll: true }); }
    }
    if (opener) opener.addEventListener('click', function () { openSheet(sheet.hidden); });
    q('[data-close]').forEach(function (el) { el.addEventListener('click', function () { openSheet(false); }); });
    if (sheet) sheet.addEventListener('click', function (e) { if (e.target.closest('a')) openSheet(false); });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && sheet && !sheet.hidden) openSheet(false); });

    /* skim mode: remembered per reader; keeps your place when the page gets shorter or longer */
    function setSkim(on, keepPlace) {
      var anchor = keepPlace && active >= 0 ? secs[active] : null;
      var before = anchor ? anchor.getBoundingClientRect().top : 0;
      root.classList.toggle('skim', on);
      q('[data-skim]').forEach(function (b) {
        b.setAttribute('aria-pressed', on ? 'true' : 'false');
        b.textContent = on ? 'Full read' : 'Skim mode';
      });
      if (anchor) window.scrollBy({ top: anchor.getBoundingClientRect().top - before, behavior: 'instant' });
      try { localStorage.setItem('dive-skim', on ? '1' : '0'); } catch (e) { /* private window */ }
      onScroll();
    }
    q('[data-skim]').forEach(function (b) {
      b.addEventListener('click', function () { setSkim(!root.classList.contains('skim'), true); });
    });
    try { if (localStorage.getItem('dive-skim') === '1') setSkim(true, false); } catch (e) { /* no storage */ }

    /* printing always shows the full text with answers open */
    window.addEventListener('beforeprint', function () { q('.quiz details').forEach(function (d) { d.open = true; }); });
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init); else init();
})();
