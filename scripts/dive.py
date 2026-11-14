"""Series 3 · Deep dives: one long, chaptered page per topic, in the "annotated textbook" skin.

Content lives in content/deep-dives/<slug>.py as a DIVE dict (see saga.py). The helpers below are injected
into that module. Styles: public/assets/dive.css; navigation and skim mode: public/assets/dive.js.
"""
import html
import re

from doodle import highlight


def esc(s):
    return html.escape(s, quote=True)


# ---------------------------------------------------------------- content helpers (injected into content files)
def mn(text):
    """A handwritten margin note (right margin on desktop, inline on phones)."""
    return f'<aside class="mn">{text}</aside>'


def full(inner):
    """Wrap blocks that skim mode hides."""
    return f'<div class="full">\n{inner}\n</div>'


def tbl(head, rows, hot=(), mono=()):
    """head: column titles; rows: lists of cells; hot: row indexes to tint; mono: column indexes in monospace."""
    th = "".join(f"<th scope=\"col\">{h}</th>" for h in head)
    trs = []
    for i, r in enumerate(rows):
        tds = "".join(f'<td{" class=mono" if c in mono else ""}>{v}</td>' for c, v in enumerate(r))
        trs.append(f'<tr{" class=hot" if i in hot else ""}>{tds}</tr>')
    return f'<div class="tbl"><table><thead><tr>{th}</tr></thead><tbody>{"".join(trs)}</tbody></table></div>'


def drill(n, title, rows, rule):
    """A failure-drill card. rows: (label, text) or (label, text, True) for rows hidden in skim mode."""
    out = []
    for label, text, *deep in rows:
        c = ' class="full"' if deep and deep[0] else ""
        out.append(f"<dt{c}>{label}</dt><dd{c}>{text}</dd>")
    return (f'<div class="drill" id="drill-{n}"><header><span>Drill {n}</span><h3>{title}</h3></header>'
            f'<dl>{"".join(out)}</dl><p class="rule">Rule: {rule}</p></div>')


def code(file, note, src, plain=False):
    body = esc(src.strip("\n")) if plain else highlight(src.strip("\n"))
    return (f'<div class="card"><div class="card-head"><span>{esc(file)}</span><span>{esc(note)}</span></div>'
            f'<pre><code>{body}</code></pre></div>')


def fig(w, h, label, svg, caption=""):
    cap = f"<figcaption>{caption}</figcaption>" if caption else ""
    return (f'<figure class="fig"><div class="fig-scroll"><svg viewBox="0 0 {w} {h}" role="img" aria-label="{esc(label)}">'
            f'{svg}</svg></div>{cap}</figure>')


def checklist(groups):
    out = []
    for name, items in groups:
        lis = "".join(f"<li>{i}</li>" for i in items)
        out.append(f'<div class="cl"><h3>{name}</h3><ul>{lis}</ul></div>')
    return f'<div class="checklist">{"".join(out)}</div>'


HELPERS = dict(mn=mn, full=full, tbl=tbl, drill=drill, code=code, fig=fig, checklist=checklist)

# ---------------------------------------------------------------- rendering
FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">\n'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
         '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Amatic+SC:wght@700&family=Caveat:wght@500;700'
         '&family=Courier+Prime:wght@400;700&family=Literata:ital,opsz,wght@0,7..72,400;0,7..72,600;0,7..72,700;1,7..72,400&display=swap">')
MARKERS = ('<svg width="0" height="0" style="position:absolute" aria-hidden="true" focusable="false"><defs>'
           '<marker id="a" markerWidth="10" markerHeight="8" refX="9" refY="4" orient="auto"><path class="ah" d="M0 0 L10 4 L0 8z"/></marker>'
           '<marker id="ar" markerWidth="10" markerHeight="8" refX="9" refY="4" orient="auto"><path class="ah-r" d="M0 0 L10 4 L0 8z"/></marker>'
           '</defs></svg>')
WPM = 200


def words(html_text, skim=False):
    if skim:  # drop everything skim mode hides
        html_text = re.sub(r'<div class="full">.*?\n</div>', " ", html_text, flags=re.S)
        html_text = re.sub(r'<(dt|dd|p) class="full[^"]*">.*?</\1>', " ", html_text, flags=re.S)
        html_text = re.sub(r'<aside class="mn">.*?</aside>|<div class="card">.*?</pre></div>', " ", html_text, flags=re.S)
        html_text = re.sub(r'^<p>.*?</p>$', " ", html_text, flags=re.M)
        html_text = re.sub(r'^<(ol|ul)>.*?^</\1>', " ", html_text, flags=re.M | re.S)
    text = re.sub(r"<svg.*?</svg>", " ", html_text, flags=re.S)
    return len(re.sub(r"<[^>]+>", " ", text).split())


def mins(n):
    return max(1, round(n / WPM))


def pdf_name(d):
    return f"{d['slug']}-deep-dive.pdf"


def render_body(d, home="../../index.html"):
    """Everything inside <body>: used by the site page and by the standalone preview."""
    chs = d["chapters"]
    n = len(chs)
    for c in chs:
        c["_w"] = words(c["gist"] + c["body"])
    total = sum(c["_w"] for c in chs)
    skim = sum(words(c["gist"] + c["body"], skim=True) for c in chs)
    pills = "".join(f'<a href="#{c["id"]}" data-ch="{i}"><b>{i + 1}</b> {c["nav"]}</a>' for i, c in enumerate(chs))
    rows = "".join(f'<li><a href="#{c["id"]}" data-ch="{i}"><span class="n">{i + 1}</span><span class="t">{c["title"]}</span>'
                   f'<span class="m">{mins(c["_w"])} min</span></a></li>' for i, c in enumerate(chs))
    facts = "".join(f"<li><b>{k}</b> {v}</li>" for k, v in
                    [("Full read", f"about {mins(total)} min"), ("Skim", f"about {mins(skim)} min: yellow boxes, tables and drill rules")] + d["facts"])
    sections = []
    for i, c in enumerate(chs):
        quiz = ""
        if c.get("check"):
            qs = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in c["check"])
            quiz = f'<div class="check quiz"><h3>checkpoint</h3>{qs}</div>'
        nxt = (f'<a class="next" href="#{chs[i + 1]["id"]}"><small>next · chapter {i + 2}</small>{chs[i + 1]["title"]} →</a>'
               if i + 1 < n else f'<a class="next" href="#top"><small>the end</small>Back to the top ↑</a>')
        sections.append(f'''<section id="{c["id"]}" data-title="{esc(c["nav"])}">
<p class="ch">chapter {i + 1} <span>· {mins(c["_w"])} min</span></p>
<h2>{c["title"]}</h2>
<div class="gist"><p><b>Gist</b> {c["gist"]}</p></div>
{c["body"]}
{quiz}
{nxt}
</section>''')
    src = "".join(f'<a href="{href}">{label}</a>' for label, href in d.get("builds_on_links", []))
    return f'''{MARKERS}
<a class="skip-link" href="#main">Skip to the text</a>
<header class="site" id="top">
  <a class="brand" href="{home}"><b>Jef’s<span>.</span>Notes</b><small>deep dive {d["no"]:02d}</small></a>
  <a class="site-link" href="{home}#deep-dives">Shelf</a>
</header>
<div class="strip" data-strip>
  <div class="strip-in">
    <nav aria-label="Chapters">{pills}</nav>
    <button class="skim-btn" type="button" data-skim aria-pressed="false">Skim mode</button>
  </div>
  <div class="progress" aria-hidden="true"><i data-progress></i></div>
</div>

<main id="main" class="wrap"><article class="page"><div class="col">
<p class="eyebrow">Deep dive {d["no"]:02d} · builds on {d["builds_on"]}</p>
<h1><span>{esc(d["title"])}</span></h1>
<p class="sub">{d["sub"]}</p>
<ul class="facts">{facts}</ul>
<nav class="toc" aria-label="Contents">
  <h2 class="toc-h">In this deep dive</h2>
  <ol>{rows}</ol>
  {f'<p class="toc-src">Read first: {src}</p>' if src else ""}
</nav>
{chr(10).join(sections)}
<p class="sources"><b>Sources.</b> {d["sources"]}</p>
</div></article>
<footer class="foot"><span>Jef’s Notes · deep dive {d["no"]:02d} · {esc(d["title"])}</span></footer>
</main>

<div class="dock" data-dock>
  <div class="progress" aria-hidden="true"><i data-progress></i></div>
  <div class="dock-in">
    <a class="dock-arrow" data-prev href="#top" aria-label="Previous chapter">‹</a>
    <button class="dock-mid" type="button" data-open aria-haspopup="dialog" aria-expanded="false">
      <small data-count>1 / {n}</small><span data-current>{chs[0]["nav"]}</span><i aria-hidden="true">☰</i>
    </button>
    <a class="dock-arrow" data-next href="#{chs[1]["id"]}" aria-label="Next chapter">›</a>
  </div>
</div>
<div class="sheet-back" data-close hidden></div>
<div class="sheet" data-sheet role="dialog" aria-modal="true" aria-label="Chapters" hidden>
  <div class="sheet-head"><b>Chapters</b><button type="button" data-close aria-label="Close">×</button></div>
  <ol>{rows}</ol>
  <div class="sheet-foot">
    <button class="skim-btn" type="button" data-skim aria-pressed="false">Skim mode</button>
    <a href="#top" data-close>Top of page ↑</a>
  </div>
</div>'''


def render_dive(d, asset):
    """asset: build_notes.asset (adds the ?v= content hash)."""
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{esc(d["title"])} · Deep dive · Jef’s Notes</title>
<meta name="description" content="{esc(d["summary"])}">
<meta name="theme-color" content="#E4E1D9">
{FONTS}
<link rel="stylesheet" href="../../{asset("dive.css")}">
<link rel="icon" href="../../assets/favicon.svg" type="image/svg+xml">
<script src="../../{asset("dive.js")}" defer></script>
</head>
<body class="dive">
{render_body(d)}
</body>
</html>
'''


def render_preview(d, css, js):
    """A single self-contained file (styles and script inline) for sharing a draft outside the site."""
    return (f'<title>{esc(d["title"])} Deep Dive Draft</title>\n<meta name="claude:viewport-fit-sides" content="cover">\n'
            f'{FONTS}\n<style>\n{css}\n</style>\n<div class="dive">\n{render_body(d, home="#top")}\n</div>\n<script>\n{js}\n</script>\n')
