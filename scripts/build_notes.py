#!/usr/bin/env python3
"""Builds Margin Notes pages.

- Notes written as data in content/*.py are rendered into public/notes/<slug>.html.
- Hand-made notes (circuit-breaker.html, saga.html) are left as they are.
- index.html (the journal index) and all.html (the whole notebook) are always rebuilt,
  and public/notes.json lists every note for the PDF script.

Usage: python3 scripts/build_notes.py
"""
import html
import importlib.util
import json
import math
import re
from datetime import date, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PUBLIC = ROOT / "public"
CONTENT = ROOT / "content"

# ---------------------------------------------------------------- catalogue
COLLECTIONS = [
    ("resilience", "Resilience", "keep one failure from becoming everyone's failure"),
    ("consistency", "Data consistency", "keep data correct across services and databases"),
    ("communication", "Communication", "how services find and talk to each other"),
    ("data", "Scaling data", "store and read more data, faster"),
    ("coordination", "Coordination", "agree on who does what"),
]
CATALOGUE = [
    # num, slug, title, collection, one-line summary
    (1, "circuit-breaker", "Circuit Breaker", "resilience", "Stop calling a dependency that keeps failing; fail fast with a fallback, then test carefully."),
    (2, "retry-backoff", "Retry with Backoff", "resilience", "Try again after short failures, with timeouts, growing random waits and a limit."),
    (3, "bulkhead", "Bulkhead", "resilience", "Give each dependency its own pool of resources so one leak can't sink the ship."),
    (4, "rate-limiter", "Rate Limiter", "resilience", "Cap how many requests each client can make, so nobody can flood the service."),
    (5, "saga", "Saga", "consistency", "A transaction across services as local steps, with compensating “undo” steps when one fails."),
    (6, "transactional-outbox", "Transactional Outbox", "consistency", "Save the change and the event in one transaction, then publish the event reliably."),
    (7, "idempotent-consumer", "Idempotent Consumer", "consistency", "Handle the same message twice without doing the work twice."),
    (8, "event-sourcing", "Event Sourcing", "consistency", "Store every change as an event and rebuild the current state from the log."),
    (9, "cqrs", "CQRS", "consistency", "Use one model to change data and separate, fast models to read it."),
    (10, "api-gateway", "API Gateway", "communication", "One front door for clients that routes, authenticates and shapes requests."),
    (11, "publish-subscribe", "Publish–Subscribe", "communication", "Announce events once; anyone interested subscribes, nobody calls each other."),
    (12, "competing-consumers", "Competing Consumers", "communication", "Many workers pull from one queue so load is shared and spikes are smoothed."),
    (13, "sidecar", "Sidecar & Service Mesh", "communication", "Move networking chores into a helper process that runs next to every service."),
    (14, "service-discovery", "Service Discovery", "communication", "Look up where a service is running right now instead of hard-coding addresses."),
    (15, "sharding", "Sharding", "data", "Split data across many databases by a key, so each holds only a slice."),
    (16, "replication", "Leader–Follower Replication", "data", "Copy data to followers for reads and failover; one leader takes the writes."),
    (17, "cache-aside", "Cache-Aside", "data", "Check a fast cache first; on a miss, load from the database and keep a copy."),
    (18, "leader-election", "Leader Election", "coordination", "Pick exactly one node to do a job, and safely pick a new one when it dies."),
]
HANDMADE = {"circuit-breaker", "saga"}
START = date(2026, 9, 7)  # first lecture (a Monday)


def lecture_date(num: int) -> date:
    """Mon / Wed / Fri lectures starting on START."""
    week, slot = divmod(num - 1, 3)
    return START + timedelta(weeks=week, days=(0, 2, 4)[slot])


def day_label(num: int) -> str:
    d = lecture_date(num)
    return f"{d.strftime('%a')} · {d.strftime('%d.%m.%y')}"


def coll(key):
    return next(c for c in COLLECTIONS if c[0] == key)


def esc(s):
    return html.escape(s, quote=True)


# ---------------------------------------------------------------- doodles
class Doodle:
    """Tiny helper for hand-drawn SVG: shapes go in a wobbly group, text stays crisp."""

    def __init__(self, w, h, label, caption="", small=False):
        self.w, self.h, self.label, self.caption, self.small = w, h, label, caption, small
        self.shapes, self.texts, self.defs = [], [], []

    # shapes ------------------------------------------------------
    def raw(self, svg):
        self.shapes.append(svg)
        return self

    def rawtext(self, svg):
        self.texts.append(svg)
        return self

    def box(self, x, y, w, h, label=None, fill="blue", sub=None, stroke="", dash=False, size=None, rx=10, subsize=17):
        cls = f"d f-{fill}" + (f" d-{stroke}" if stroke else "") + (" d-dash" if dash else "")
        self.shapes.append(f'<rect class="{cls}" x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}"/>')
        cx = x + w / 2
        if label:
            ly = y + h / 2 + (7 if not sub else -4)
            fs = f' font-size="{size}"' if size else ""
            tcls = "t-head" + (f" t-{stroke}" if stroke in ("red", "green", "pen") else "")
            self.texts.append(f'<text class="{tcls}" x="{cx:g}" y="{ly:g}" text-anchor="middle"{fs}>{esc(label)}</text>')
        if sub:
            self.texts.append(f'<text class="t" x="{cx:g}" y="{y + h / 2 + 20:g}" text-anchor="middle" font-size="{subsize}">{esc(sub)}</text>')
        return self

    def circle(self, cx, cy, r, fill="paper", stroke="", label=None, sub=None):
        cls = f"d f-{fill}" + (f" d-{stroke}" if stroke else "")
        self.shapes.append(f'<circle class="{cls}" cx="{cx}" cy="{cy}" r="{r}"/>')
        if label:
            self.texts.append(f'<text class="t-head" x="{cx}" y="{cy + (7 if not sub else -4)}" text-anchor="middle">{esc(label)}</text>')
        if sub:
            self.texts.append(f'<text class="t" x="{cx}" y="{cy + 20}" text-anchor="middle" font-size="16">{esc(sub)}</text>')
        return self

    def db(self, cx, y, label=None, w=68, h=40, fill="paper", stroke=""):
        rx = w / 2
        cls = f"d d-thin f-{fill}" + (f" d-{stroke}" if stroke else "")
        self.shapes.append(
            f'<path class="{cls}" d="M{cx - rx:g} {y} v{h} a{rx:g} 9 0 0 0 {w} 0 v-{h}"/>'
            f'<ellipse class="{cls}" cx="{cx}" cy="{y}" rx="{rx:g}" ry="9"/>')
        if label:
            self.texts.append(f'<text class="t t-soft" x="{cx}" y="{y + h + 30}" text-anchor="middle" font-size="16">{esc(label)}</text>')
        return self

    def msgs(self, x, y, n, fill="y", size=18, gap=6, stroke=""):
        """A row of little message envelopes / queue items."""
        for i in range(n):
            xx = x + i * (size + gap)
            cls = f"d d-thin f-{fill}" + (f" d-{stroke}" if stroke else "")
            self.shapes.append(f'<rect class="{cls}" x="{xx}" y="{y}" width="{size}" height="{size * .72:g}" rx="2"/>'
                               f'<path class="d d-thin" d="M{xx} {y} l{size / 2:g} {size * .4:g} l{size / 2:g} -{size * .4:g}"/>')
        return self

    def line(self, d, color="", dash=False, thin=False):
        cls = "d" + (f" d-{color}" if color else "") + (" d-dash" if dash else "") + (" d-thin" if thin else "")
        self.shapes.append(f'<path class="{cls}" d="{d}"/>')
        return self

    def arrow(self, x1, y1, x2, y2, color="", dash=False, label=None, lx=None, ly=None, anchor="middle",
              curve=None, both=False, lcls="t-s"):
        cls = "d" + (f" d-{color}" if color else "") + (" d-dash" if dash else "")
        if curve:
            cx, cy = curve
            d = f"M{x1} {y1} Q{cx} {cy} {x2} {y2}"
            fx, fy = cx, cy
            bx, by = cx, cy
        else:
            d = f"M{x1} {y1} L{x2} {y2}"
            fx, fy, bx, by = x1, y1, x2, y2
        self.shapes.append(f'<path class="{cls}" d="{d}"/>')
        solid = "d" + (f" d-{color}" if color else "")
        self.shapes.append(f'<path class="{solid}" d="{self._head(fx, fy, x2, y2)}"/>')
        if both:
            self.shapes.append(f'<path class="{solid}" d="{self._head(bx, by, x1, y1)}"/>')
        if label:
            if lx is None:
                lx, ly = (x1 + x2) / 2, (y1 + y2) / 2 - 10
            tc = lcls + (f" t-{color}" if color in ("red", "green") else "")
            self.texts.append(f'<text class="{tc}" x="{lx:g}" y="{ly:g}" text-anchor="{anchor}">{esc(label)}</text>')
        return self

    @staticmethod
    def _head(fx, fy, x, y, size=12):
        a = math.atan2(y - fy, x - fx)
        p1 = (x - size * math.cos(a - .45), y - size * math.sin(a - .45))
        p2 = (x - size * math.cos(a + .45), y - size * math.sin(a + .45))
        return f"M{p1[0]:.1f} {p1[1]:.1f} L{x} {y} L{p2[0]:.1f} {p2[1]:.1f}"

    def text(self, x, y, s, cls="t", anchor="middle", size=None):
        fs = f' font-size="{size}"' if size else ""
        self.texts.append(f'<text class="{cls}" x="{x}" y="{y}" text-anchor="{anchor}"{fs}>{esc(s)}</text>')
        return self

    def note(self, x, y, s, color="", anchor="middle", size=None):
        return self.text(x, y, s, "t-s" + (f" t-{color}" if color else ""), anchor, size)

    def head(self, x, y, s, anchor="middle", size=None, color=""):
        return self.text(x, y, s, "t-head" + (f" t-{color}" if color else ""), anchor, size)

    def icon(self, name, x, y, s=1.0, color="", fill=None):
        body = ICONS[name]
        cls = "d" + (f" d-{color}" if color else "")
        if fill:
            body = body.replace('class="F"', f'class="f-{fill}"')
        body = body.replace('class="F"', 'class="f-paper"')
        self.shapes.append(f'<g transform="translate({x} {y}) scale({s})"><g class="{cls}">{body}</g></g>')
        return self

    def html(self):
        shapes = "".join(self.shapes)
        texts = "".join(self.texts)
        swipe = "" if self.small else '<p class="swipe">← swipe to see the whole drawing →</p>'
        cap = f"<figcaption>{self.caption}</figcaption>" if self.caption else ""
        cls = "fig fig--small" if self.small else "fig"
        return (f'<figure class="{cls}"><div class="fig-scroll"><svg viewBox="0 0 {self.w} {self.h}" role="img" '
                f'aria-label="{esc(self.label)}"><g class="rough">{shapes}</g>{texts}</svg></div>{swipe}{cap}</figure>')


# Icons are drawn in a ~60×60 box at the origin. class="F" marks a fill that can be recoloured.
ICONS = {
    "envelope": '<rect class="F" x="0" y="10" width="60" height="40" rx="3"/><path d="M0 12 L30 34 L60 12"/>',
    "truck": '<rect class="F" x="0" y="10" width="40" height="30" rx="3"/><path class="F" d="M40 20 h12 l8 10 v10 h-20 z"/><circle class="F" cx="12" cy="44" r="6"/><circle class="F" cx="48" cy="44" r="6"/>',
    "clock": '<circle class="F" cx="30" cy="30" r="26"/><path d="M30 14 V30 H42"/>',
    "lock": '<rect class="F" x="8" y="26" width="44" height="32" rx="4"/><path d="M18 26 v-8 a12 12 0 0 1 24 0 v8 M30 38 v8"/>',
    "key": '<circle class="F" cx="14" cy="30" r="11"/><path d="M25 30 h32 M48 30 v9 M55 30 v6"/>',
    "crown": '<path class="F" d="M4 46 L8 14 L20 30 L30 8 L40 30 L52 14 L56 46 z"/><path d="M4 52 h52"/>',
    "server": '<rect class="F" x="0" y="0" width="58" height="22" rx="3"/><rect class="F" x="0" y="28" width="58" height="22" rx="3"/><path d="M8 11 h14 M8 39 h14"/><circle cx="48" cy="11" r="2"/><circle cx="48" cy="39" r="2"/>',
    "phone": '<rect class="F" x="16" y="0" width="30" height="56" rx="6"/><path d="M26 48 h10"/>',
    "cup": '<path class="F" d="M6 16 h40 v20 a20 20 0 0 1 -40 0 z"/><path d="M46 22 h6 a7 7 0 0 1 0 14 h-7 M14 4 q4 5 0 9 M26 2 q4 5 0 9"/>',
    "bell": '<path class="F" d="M10 44 q0 -30 20 -30 q20 0 20 30 z"/><path d="M4 46 h52 M30 8 v6 M26 50 a4 4 0 0 0 8 0"/>',
    "ledger": '<rect class="F" x="4" y="0" width="52" height="60" rx="3"/><path d="M14 12 h32 M14 22 h32 M14 32 h32 M14 42 h22"/>',
    "parcel": '<rect class="F" x="4" y="14" width="52" height="40" rx="2"/><path d="M4 26 h52 M30 14 v40"/>',
    "ship": '<path class="F" d="M0 30 h80 l-10 22 h-60 z"/><path d="M20 30 v22 M40 30 v22 M60 30 v22 M34 30 v-18 h14 v18"/>',
    "tower": '<path d="M30 60 L22 20 h16 L30 60 M24 40 h12"/><circle class="F" cx="30" cy="14" r="5"/><path d="M18 6 a16 16 0 0 0 0 16 M42 6 a16 16 0 0 1 0 16 M10 0 a26 26 0 0 0 0 28 M50 0 a26 26 0 0 1 0 28"/>',
    "board": '<rect class="F" x="0" y="0" width="70" height="46" rx="3"/><path d="M14 46 v14 M56 46 v14"/><rect x="8" y="8" width="20" height="14" class="F"/><rect x="38" y="10" width="22" height="12" class="F"/><path d="M10 32 h48"/>',
    "turnstile": '<rect class="F" x="0" y="20" width="16" height="40" rx="2"/><path d="M16 34 h30 M16 34 l18 -18 M16 34 l18 18"/><circle class="F" cx="16" cy="34" r="5"/>',
    "bucket": '<path class="F" d="M6 18 h48 l-6 38 h-36 z"/><path d="M6 18 q24 -22 48 0"/><circle class="F" cx="22" cy="34" r="5"/><circle class="F" cx="36" cy="40" r="5"/><circle class="F" cx="28" cy="46" r="5"/>',
    "fridge": '<rect class="F" x="6" y="0" width="44" height="64" rx="5"/><path d="M6 24 h44 M14 8 v10 M14 30 v14"/>',
    "store": '<rect class="F" x="4" y="22" width="60" height="38"/><path class="F" d="M0 22 l8 -16 h52 l8 16 z"/><rect x="26" y="38" width="16" height="22"/>',
    "book": '<path class="F" d="M4 6 h22 a6 6 0 0 1 6 6 v44 a6 6 0 0 0 -6 -6 h-22 z"/><path class="F" d="M60 6 h-22 a6 6 0 0 0 -6 6 v44 a6 6 0 0 1 6 -6 h22 z"/>',
    "copier": '<rect class="F" x="0" y="18" width="60" height="34" rx="4"/><path class="F" d="M8 18 l6 -12 h32 l6 12"/><rect class="F" x="16" y="52" width="28" height="8"/><path d="M10 30 h16"/>',
    "ticket": '<path class="F" d="M0 8 h60 v14 a6 6 0 0 0 0 12 v14 h-60 v-14 a6 6 0 0 0 0 -12 z"/><path d="M42 8 v40" stroke-dasharray="4 4"/>',
    "sidecar": '<circle class="F" cx="12" cy="46" r="10"/><circle class="F" cx="56" cy="46" r="10"/><path d="M12 46 L26 26 h18 l12 20 M26 26 l-4 -10 h-8 M44 26 l6 -10"/><path class="F" d="M66 30 h30 a12 12 0 0 1 0 24 h-30 z"/><circle class="F" cx="84" cy="56" r="7"/>',
    "directory": '<rect class="F" x="0" y="0" width="56" height="60" rx="3"/><path d="M8 12 h28 M8 22 h40 M8 32 h34 M8 42 h40 M8 52 h26"/><rect class="F" x="56" y="6" width="8" height="12"/><rect class="F" x="56" y="22" width="8" height="12"/>',
    "lanes": '<path d="M0 0 v60 M30 0 v60 M60 0 v60 M90 0 v60"/><rect class="F" x="6" y="10" width="18" height="12"/><rect class="F" x="36" y="26" width="18" height="12"/><rect class="F" x="66" y="6" width="18" height="12"/>',
    "baton": '<path class="F" d="M6 50 L46 10 l8 8 L14 58 z"/><path d="M40 16 l8 8"/>',
    "door": '<rect class="F" x="6" y="0" width="44" height="64" rx="2"/><circle cx="40" cy="34" r="3"/>',
    "shield": '<path class="F" d="M30 2 L54 10 v18 c0 16 -10 26 -24 32 c-14 -6 -24 -16 -24 -32 v-18 z"/><path d="M20 30 l7 8 l14 -16"/>',
    "map": '<path class="F" d="M0 8 l20 -6 l20 6 l20 -6 v50 l-20 6 l-20 -6 l-20 6 z"/><path d="M20 2 v50 M40 8 v50"/>',
    "pin": '<path class="F" d="M20 56 C 6 36 0 28 0 20 a20 20 0 0 1 40 0 c0 8 -6 16 -20 36 z"/><circle cx="20" cy="20" r="7"/>',
    "kitchen": '<rect class="F" x="0" y="20" width="70" height="36" rx="3"/><path d="M14 20 v-8 h14 v8 M42 20 v-12 h12 v12 M8 34 h54"/>',
    "menu": '<rect class="F" x="0" y="0" width="48" height="62" rx="3"/><path d="M10 12 h28 M10 22 h20 M10 32 h26 M10 42 h18 M10 52 h24"/>',
    "megaphone": '<path class="F" d="M6 24 h10 l28 -16 v44 l-28 -16 h-10 z"/><path d="M16 36 l4 16 h8 l-4 -16 M52 20 q8 10 0 20"/>',
    "fuse": '<rect class="F" x="0" y="0" width="40" height="60" rx="4"/><rect x="12" y="10" width="16" height="16"/><rect x="12" y="34" width="16" height="16"/>',
    "hourglass": '<path class="F" d="M0 0 h24 M0 34 h24 M3 0 q0 13 9 17 q-9 4 -9 17 M21 0 q0 13 -9 17 q9 4 9 17"/>',
    "check": '<path d="M4 30 l16 18 l36 -40"/>',
    "cross": '<path d="M8 8 L52 52 M52 8 L8 52"/>',
    "calendar": '<rect class="F" x="0" y="8" width="56" height="50" rx="4"/><path d="M0 22 h56 M14 2 v12 M42 2 v12"/><path d="M10 32 h8 M24 32 h8 M38 32 h8 M10 44 h8 M24 44 h8"/>',
}


# ---------------------------------------------------------------- code highlighter
KEYWORDS = r"\b(const|let|var|async|await|function|return|if|else|for|of|in|new|class|type|export|import|from|throw|try|catch|finally|private|while|interface|true|false|null|undefined|SELECT|FROM|WHERE|INSERT|INTO|VALUES|UPDATE|SET|BEGIN|COMMIT|ON|CONFLICT|DO|NOTHING|DELETE|AND|ORDER|BY|LIMIT|FOR|SKIP|LOCKED|RETURNING|CREATE|TABLE|PRIMARY|KEY|def|yield|break|continue|switch|case|default)\b"


def highlight(code: str) -> str:
    out = []
    for line in code.split("\n"):
        parts = re.split(r'(//.*$|--\s.*$|#\s.*$|"(?:[^"\\]|\\.)*"|\'(?:[^\'\\]|\\.)*\'|`[^`]*`)', line)
        buf = []
        for i, p in enumerate(parts):
            if not p:
                continue
            e = html.escape(p, quote=False)
            if i % 2 == 1:
                if p.startswith(("//", "--", "#")):
                    buf.append(f'<span class="c">{e}</span>')
                else:
                    buf.append(f'<span class="s">{e}</span>')
            else:
                buf.append(re.sub(KEYWORDS, r'<span class="k">\1</span>', e))
        out.append("".join(buf))
    return "\n".join(out)


# ---------------------------------------------------------------- page pieces
FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">\n'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
         '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Amatic+SC:wght@700&family=Caveat:wght@500;700&family=Courier+Prime:wght@400;700&family=Kalam:wght@400;700&family=Patrick+Hand&display=swap">')
DL = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" '
      'stroke-linejoin="round" aria-hidden="true"><path d="M12 3v12"/><path d="m7 10 5 5 5-5"/><path d="M5 21h14"/></svg>')
ROUGH = ('<svg width="0" height="0" style="position:absolute" aria-hidden="true" focusable="false">'
         '<filter id="rough" x="-5%" y="-5%" width="110%" height="110%"><feTurbulence type="fractalNoise" '
         'baseFrequency="0.028" numOctaves="2" seed="7" result="n"/><feDisplacementMap in="SourceGraphic" in2="n" '
         'scale="3.2"/></filter></svg>')
KEY = '''  <aside class="key" aria-label="Key to the signifiers on this page">
    <h3>Key</h3>
    <ul>
      <li><span class="sig">–</span> note</li>
      <li><span class="sig">★</span> key idea</li>
      <li><span class="sig">!</span> watch out</li>
      <li><span class="sig">→</span> fix / leads to</li>
      <li><span class="sig">×</span> avoid</li>
      <li><span class="sig">✓</span> do this</li>
    </ul>
  </aside>
'''
FOOT = '<footer class="foot"><span>Margin Notes · a student\'s bullet journal on distributed design patterns</span><span>by Jefrey Romel Tagunicar</span></footer>'


def head(title, desc, prefix):
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<meta name="theme-color" content="#E6E3DC">
{FONTS}
<link rel="stylesheet" href="{prefix}assets/notebook.css">
<link rel="stylesheet" href="{prefix}assets/bujo.css">
<link rel="icon" href="{prefix}assets/favicon.svg" type="image/svg+xml">
<script src="{prefix}assets/notebook.js" defer></script>
</head>'''


def bar(prefix, current=None, print_button=True, disabled=False):
    cur = lambda k: ' aria-current="page"' if current == k else ""
    if print_button:
        btn = f'<button class="btn" type="button" data-print{" disabled" if disabled else ""}>{DL}Export as PDF</button>'
    else:
        btn = f'<a class="btn" href="{prefix}all.html?print">{DL}Export as PDF</a>'
    return f'''<header class="bar">
  <div class="bar-in">
    <a class="brand" href="{prefix}index.html"><b>Margin<span>.</span>Notes</b><small>distributed design patterns</small></a>
    <nav aria-label="Main">
      <a href="{prefix}index.html#index"{cur("index")}>Index</a>
      <a class="hide-sm" href="{prefix}all.html"{cur("all")}>Whole notebook</a>
      {btn}
    </nav>
  </div>
</header>'''


def pdf_name(num, slug):
    return f"{num:02d}-{slug}.pdf"


def ratings_table(rows):
    names = [("Simplicity", "easy to understand?"), ("Low cost", "cheap to build &amp; run?"),
             ("Deployability", "safe, easy releases?"), ("Testability", "test with confidence?"),
             ("Scalability", "more users &amp; data?"), ("Elasticity", "sudden spikes?"),
             ("Fault tolerance", "failure stays contained?"), ("Performance", "fast typical request?"),
             ("Evolvability", "easy to change?")]
    assert len(rows) == 9
    trs = "\n".join(
        f'      <tr data-before="{b}" data-after="{a}"><td>{n}<small>{q}</small></td><td class="dcell"></td>'
        f'<td class="score"></td><td class="why">{why}</td></tr>'
        for (n, q), (b, a, why) in zip(names, rows))
    return f'''  <div class="ratings-wrap table-scroll">
  <table class="ratings">
    <thead><tr><th scope="col">Characteristic</th><th scope="col">With the pattern</th><th scope="col">Before → after</th><th scope="col">Why</th></tr></thead>
    <tbody>
{trs}
    </tbody>
  </table>
  </div>
  <div class="legend"><span><i class="dot on"></i> kept</span><span><i class="dot gain"></i> gained</span><span><i class="dot lost"></i> lost</span><span>ratings are relative guidance for a typical system, not laws</span></div>'''


def li(items, cls=""):
    c = f' class="{cls}"' if cls else ""
    return f"<ul{c}>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


def h2(n, id_, title, side):
    return f'  <h2 id="{id_}"><span class="num">{n}</span>{title} <span class="side">{side}</span></h2>'


def neighbours(num):
    order = [c for c in CATALOGUE]
    i = num - 1
    prev = order[i - 1] if i > 0 else None
    nxt = order[i + 1] if i + 1 < len(order) else None
    return prev, nxt


def pager(num, prefix_notes=""):
    prev, nxt = neighbours(num)
    a = (f'<a href="{prev[1]}.html"><small>← previous note</small>{prev[0]:02d} · {esc(prev[2])}</a>' if prev
         else '<a href="../index.html"><small>← back to</small>Index</a>')
    b = (f'<a href="{nxt[1]}.html"><small>Next note →</small>{nxt[0]:02d} · {esc(nxt[2])}</a>' if nxt
         else '<a href="../index.html"><small>back to →</small>Index</a>')
    return f'<nav class="pager" aria-label="Notes">\n  {a}\n  {b}\n</nav>'


def render_note(n):
    num, slug, title, ckey, summary = next(c for c in CATALOGUE if c[1] == n["slug"])
    cname = coll(ckey)[1]
    vocab = "\n".join(f"    <div><dt>{t}</dt><dd>{d}</dd></div>" for t, d in n["vocab"])
    maprows = "\n".join(f"      <tr><td>{a}</td><td>{b}</td></tr>" for a, b in n["map"])
    steps = "\n".join(f"    <li><b>{t}</b><p>{d}</p></li>" for t, d in n["steps"])
    pits = "\n".join(f'    <li><h3>{t}</h3><p>{d} <span class="fix">Fix →</span> {f}</p></li>' for t, d, f in n["pitfalls"])
    quiz = "\n".join(f"    <details><summary>{q}</summary><p>{a}</p></details>" for q, a in n["quiz"])
    related = "".join(f"<li>{r}</li>" for r in n["related"])
    chips = "".join(f"<li><b>{k}:</b> {v}</li>" for k, v in n["chips"])
    sources = "".join(f"<li>{s}</li>" for s in n["sources"])
    code = n["code"]
    figs = lambda key: "\n".join(f.html() for f in n.get(key, []))
    parts = [
        head(f"{title} · Margin Notes", summary, "../"),
        '<body class="bujo">',
        '<a class="skip-link" href="#main">Skip to the notes</a>',
        bar("../"),
        '',
        '<main id="main" class="desk">',
        f'<article class="sheet" id="{slug}">',
        f'  {ROUGH}',
        f'  <div class="page-meta"><span class="day">{day_label(num)}</span><span class="topic">collection · <b>{esc(cname.lower())}</b></span></div>',
        f'  <p class="kicker">{n["kicker"]}</p>',
        f'  <h1><span class="hl">{esc(title)}</span></h1>',
        f'  <div class="tldr">\n    <span class="tag">TL;DR</span>\n    <p>{n["tldr"]}</p>\n  </div>',
        f'  <ul class="chips" aria-label="At a glance">{chips}</ul>',
        KEY,
        h2(1, "problem", "The problem", n.get("problem_side", "why do we even need this?")),
        n["problem"],
        figs("problem_figs"),
        n.get("problem_after", ""),
        h2(2, "analogy", "Real-life analogy", n["analogy_side"]),
        n["analogy"],
        figs("analogy_figs"),
        f'''  <div class="table-scroll">
  <table class="map">
    <caption>Translating it to software</caption>
    <thead><tr><th scope="col">In real life</th><th scope="col">In your system</th></tr></thead>
    <tbody>
{maprows}
    </tbody>
  </table>
  </div>''',
        n.get("analogy_after", ""),
        h2(3, "how", "How it solves it", n["how_side"]),
        n["how"],
        figs("how_figs"),
        f'  <ol class="steps">\n{steps}\n  </ol>',
        n.get("how_after", ""),
        f'  <h3>Vocabulary for the exam</h3>\n  <dl class="vocab">\n{vocab}\n  </dl>',
        f'''  <div class="card">
    <div class="card-head"><span>{esc(code["file"])}</span><span>{esc(code["note"])}</span></div>
<pre><code>{highlight(code["src"].strip(chr(10)))}</code></pre>
  </div>''',
        f'  <p class="aside">{n["tools"]}</p>' if n.get("tools") else "",
        h2(4, "tradeoffs", "Gains vs losses", "nothing is free"),
        f'''  <div class="tchart">
    <div class="gain">
      <h3>What we gain</h3>
      {li(n["gains"])}
    </div>
    <div class="loss">
      <h3>What we lose</h3>
      {li(n["losses"])}
    </div>
  </div>''',
        h2(5, "ratings", "Architecture ratings", "1 = poor · 5 = great"),
        f'  <p>{n["baseline"]}</p>',
        ratings_table(n["ratings"]),
        h2(6, "pitfalls", "Common pitfalls", n.get("pitfalls_side", "the usual ways this goes wrong")),
        f'  <ul class="pits">\n{pits}\n  </ul>',
        h2(7, "when", "When to use it (and when not)", ""),
        f'''  <div class="grid2">
    <div>
      <h3 class="green">Use it when…</h3>
      {li(n["use"], "check yes")}
    </div>
    <div>
      <h3 class="red">Skip it when…</h3>
      {li(n["skip"], "check no")}
    </div>
  </div>''',
        f'  <h3>Related patterns</h3>\n  <ul class="related">{related}</ul>',
        h2(8, "quiz", "Self-check quiz", ""),
        f'  <div class="quiz">\n{quiz}\n  </div>',
        f'  <div class="remember">\n    <span class="tag">remember!!</span>\n    <p>{n["remember"]}</p>\n  </div>',
        f'''  <div class="export no-print">
    <button class="btn" type="button" data-print>{DL}Export this note as PDF</button>
    <a class="btn btn--ghost" href="../pdf/{pdf_name(num, slug)}">Download ready-made PDF</a>
    <span class="hint">In the print window choose “Save as PDF”. On a phone, the ready-made PDF is easiest.</span>
  </div>''',
        f'  <div class="sources">\n    <h3>Further reading</h3>\n    <ul>{sources}</ul>\n  </div>',
        f'  <p class="folio">{num:02d}</p>',
        '</article>',
        '',
        pager(num),
        FOOT,
        '</main>',
        '</body>',
        '</html>',
        '',
    ]
    return "\n".join(p for p in parts if p is not None)


def index_list(link_prefix, anchors=False):
    out = []
    for key, name, blurb in COLLECTIONS:
        items = []
        for num, slug, title, ckey, summary in CATALOGUE:
            if ckey != key:
                continue
            href = f"#{slug}" if anchors else f"{link_prefix}notes/{slug}.html"
            items.append(f'<li><a href="{href}"><span class="toc-n">{num:02d}</span><span class="toc-t">{esc(title)}'
                         f'<small>{esc(summary)}</small></span><span class="toc-p">p. {num:02d}</span></a></li>')
        out.append(f'  <h3 class="toc-coll">{esc(name)} <span>{esc(blurb)}</span></h3>\n  <ol class="toc">{"".join(items)}</ol>')
    return "\n".join(out)


def render_index():
    return "\n".join([
        head("Margin Notes", "A student's bullet journal on distributed design patterns: problems, real-life analogies, doodles, trade-offs, ratings and pitfalls.", ""),
        '<body class="bujo">',
        '<a class="skip-link" href="#main">Skip to the index</a>',
        bar("", "index", print_button=False),
        '<main id="main" class="desk">',
        '<article class="sheet">',
        '  <div class="page-meta"><span class="day">Fall term · 2026</span><span class="topic">subject · <b>distributed systems</b></span></div>',
        '  <p class="kicker">property of a very caffeinated student</p>',
        '  <h1 class="cover-title"><span class="hl">Margin Notes</span></h1>',
        f'  <p class="lead">My class notes on <span class="hl">distributed design patterns</span>, written up properly. {len(CATALOGUE)} patterns in five collections. Each note covers the problem a pattern solves, a real-life analogy with doodles, how it works, what you gain and lose, how it scores on nine architecture characteristics, and the mistakes people make with it.</p>',
        KEY,
        '  <h2 id="index"><span class="num">✎</span>Index <span class="side">tap a note to open it</span></h2>',
        index_list(""),
        '  <h2 id="how-to-read"><span class="num">?</span>How every note is laid out <span class="side">same eight sections, every time</span></h2>',
        '''  <ol class="how-to">
    <li><b>The problem</b>: what breaks without the pattern, with a doodle.</li>
    <li><b>Real-life analogy</b>: an everyday version, plus a “translate to software” table.</li>
    <li><b>How it solves it</b>: diagrams, steps, vocabulary and a code card.</li>
    <li><b>Gains vs losses</b>: the trade-off spread.</li>
    <li><b>Architecture ratings</b>: nine characteristics, before → after.</li>
    <li><b>Common pitfalls</b>: each with its fix.</li>
    <li><b>When to use it</b>: and when to skip it.</li>
    <li><b>Self-check quiz</b>: tap a question to see the answer.</li>
  </ol>''',
        '  <h2 id="ratings-key"><span class="num">★</span>The nine ratings <span class="side">my tracker key</span></h2>',
        '  <p>Every note scores the pattern from 1 (poor) to 5 (great) on the same nine things, comparing a system <b>without</b> the pattern to the same system <b>with</b> it.</p>',
        '''  <dl class="vocab">
    <div><dt>Simplicity</dt><dd>Fewer moving parts, fewer surprises.</dd></div>
    <div><dt>Low cost</dt><dd>Infrastructure, tooling and people. High = cheap.</dd></div>
    <div><dt>Deployability</dt><dd>Small, independent, safe releases.</dd></div>
    <div><dt>Testability</dt><dd>Isolated parts with clear contracts.</dd></div>
    <div><dt>Scalability</dt><dd>Handles more users and data by adding machines.</dd></div>
    <div><dt>Elasticity</dt><dd>Scales up and back down quickly for spikes.</dd></div>
    <div><dt>Fault tolerance</dt><dd>One failure stays contained.</dd></div>
    <div><dt>Performance</dt><dd>How fast a typical request is.</dd></div>
    <div><dt>Evolvability</dt><dd>How easily the system can change shape.</dd></div>
  </dl>
  <div class="legend"><span><i class="dot on"></i> kept</span><span><i class="dot gain"></i> gained with the pattern</span><span><i class="dot lost"></i> lost with the pattern</span></div>''',
        '''  <div class="remember">
    <span class="tag">first law</span>
    <p>Everything in architecture is a trade-off. If you think you've found one that isn't, you haven't found the cost yet.</p>
  </div>''',
        f'''  <div class="export no-print">
    <a class="btn" href="all.html?print">{DL}Export the whole notebook as PDF</a>
    <a class="btn btn--ghost" href="pdf/margin-notes.pdf">Download ready-made PDF</a>
    <span class="hint">On a phone, the ready-made PDF is the easiest way to save or share.</span>
  </div>''',
        '  <p class="folio">i</p>',
        '</article>',
        FOOT,
        '</main>',
        '</body>',
        '</html>',
        '',
    ])


def render_all():
    collect = " ".join(f"notes/{c[1]}.html" for c in CATALOGUE)
    return "\n".join([
        head("Margin Notes · Whole notebook", "Every note on one page, ready to export as PDF.", ""),
        '<body class="bujo">',
        '<a class="skip-link" href="#main">Skip to the notes</a>',
        bar("", "all", print_button=True, disabled=True),
        f'<main id="main" class="desk" data-collect="{collect}">',
        '<section class="sheet">',
        '  <div class="page-meta"><span class="day">Fall term · 2026</span><span class="topic">subject · <b>distributed systems</b></span></div>',
        '  <p class="kicker">the whole notebook, one note per page</p>',
        '  <h1 class="cover-title"><span class="hl">Margin Notes</span></h1>',
        '  <p class="lead">Distributed design patterns, explained with problems, analogies, doodles, trade-offs, ratings and pitfalls.</p>',
        KEY,
        '  <h2 id="index"><span class="num">✎</span>Index <span class="side">page numbers match the notes</span></h2>',
        index_list("", anchors=True),
        f'''  <div class="export no-print">
    <button class="btn" type="button" data-print disabled>{DL}Export as PDF</button>
    <span class="hint" data-collect-status role="status">Loading notes…</span>
  </div>
  <p class="aside no-print">in the print window pick “Save as PDF” as the destination. Each note starts on a new page.</p>''',
        '</section>',
        '</main>',
        '<footer class="foot desk" style="padding-block:0 40px"><span>Margin Notes · by Jefrey Romel Tagunicar</span></footer>',
        '</body>',
        '</html>',
        '',
    ])


def load_content():
    notes = {}
    for f in sorted(CONTENT.glob("*.py")):
        spec = importlib.util.spec_from_file_location(f.stem, f)
        mod = importlib.util.module_from_spec(spec)
        mod.__dict__["Doodle"] = Doodle
        spec.loader.exec_module(mod)
        for n in getattr(mod, "NOTES", []):
            notes[n["slug"]] = n
    return notes


def main():
    notes = load_content()
    missing = [c[1] for c in CATALOGUE if c[1] not in notes and c[1] not in HANDMADE]
    if missing:
        print("No content yet for:", ", ".join(missing))
    for slug, n in notes.items():
        (PUBLIC / "notes" / f"{slug}.html").write_text(render_note(n), encoding="utf-8")
        print("wrote notes/" + slug + ".html")
    (PUBLIC / "index.html").write_text(render_index(), encoding="utf-8")
    (PUBLIC / "all.html").write_text(render_all(), encoding="utf-8")
    listing = [{"num": c[0], "slug": c[1], "title": c[2], "pdf": "pdf/" + pdf_name(c[0], c[1])}
               for c in CATALOGUE if c[1] in notes or c[1] in HANDMADE]
    (PUBLIC / "notes.json").write_text(json.dumps(listing, indent=1), encoding="utf-8")
    print("wrote index.html, all.html, notes.json")


if __name__ == "__main__":
    main()
