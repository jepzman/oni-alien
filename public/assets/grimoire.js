/* The Darkside of the Corporation: the look switch (candlelight / parchment) and the difficulty tabs. */
(function () {
  var root = document.documentElement;
  root.classList.add("js");

  function setLook(look) {
    root.dataset.look = look;
    try { localStorage.setItem("grimoire-look", look); } catch (e) { /* private mode: the switch still works for this page */ }
    var meta = document.querySelector('meta[name="theme-color"]');
    if (meta) meta.content = look === "parch" ? "#d9c7a1" : "#120d0b";
  }

  document.addEventListener("DOMContentLoaded", function () {
    var btn = document.querySelector("[data-look-toggle]");
    if (btn) btn.addEventListener("click", function () { setLook(root.dataset.look === "parch" ? "candle" : "parch"); });
    if (root.dataset.look === "parch") setLook("parch");

    document.querySelectorAll("[data-diff]").forEach(function (box) {
      var tabs = Array.prototype.slice.call(box.querySelectorAll('[role="tab"]'));
      function pick(t, focus) {
        tabs.forEach(function (o) {
          var on = o === t;
          o.setAttribute("aria-selected", on ? "true" : "false");
          o.tabIndex = on ? 0 : -1;
          var p = document.getElementById(o.getAttribute("aria-controls"));
          if (on) p.removeAttribute("data-hide"); else p.setAttribute("data-hide", "");
        });
        if (focus) t.focus();
      }
      tabs.forEach(function (t, i) {
        t.addEventListener("click", function () { pick(t); });
        t.addEventListener("keydown", function (e) {
          var d = e.key === "ArrowRight" ? 1 : e.key === "ArrowLeft" ? -1 : 0;
          if (d) { e.preventDefault(); pick(tabs[(i + d + tabs.length) % tabs.length], true); }
        });
      });
    });
  });
})();
