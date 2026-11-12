#!/usr/bin/env python3
"""Builds the Jef’s Notes bookshelf.

Each journal (see JOURNALS) lives in public/<key>/:
  - notes written as data in content/<key>/*.py are rendered into public/<key>/notes/<slug>.html
  - hand-made notes listed in `handmade` are left alone
  - index.html (the journal index) and all.html (the whole journal, for PDF) are rebuilt
public/index.html is the landing page (the shelf + future log), public/journals.json lists
everything for the PDF script, and a few redirect pages keep old links working.

Usage: python3 scripts/build_notes.py
"""
import importlib.util
import json
import sys
from datetime import date, timedelta
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from doodle import Doodle, esc, highlight  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
PUBLIC = ROOT / "public"
CONTENT = ROOT / "content"
AUTHOR = "Jefrey Romel Tagunicar"

# ---------------------------------------------------------------- the nine ratings, per journal
DISTRIBUTED_ATTRS = [
    ("Simplicity", "easy to understand?", "Fewer moving parts, fewer surprises."),
    ("Low cost", "cheap to build &amp; run?", "Infrastructure, tooling and people. High = cheap."),
    ("Deployability", "safe, easy releases?", "Small, independent, safe releases."),
    ("Testability", "test with confidence?", "Isolated parts with clear contracts."),
    ("Scalability", "more users &amp; data?", "Handles more users and data by adding machines."),
    ("Elasticity", "sudden spikes?", "Scales up and back down quickly for spikes."),
    ("Fault tolerance", "failure stays contained?", "One failure stays contained."),
    ("Performance", "fast typical request?", "How fast a typical request is."),
    ("Evolvability", "easy to change?", "How easily the system can change shape."),
]
FRONTEND_ATTRS = [
    ("Simplicity", "easy to follow?", "A new teammate can read it and predict what happens."),
    ("Reusability", "use it in many places?", "The same piece works across screens, apps or brands."),
    ("Testability", "test with confidence?", "Logic and UI can be tested without a browser full of mocks."),
    ("Maintainability", "safe to change?", "A change in one place doesn't break five others."),
    ("Performance", "fast to load &amp; respond?", "Time to first content, time to interactive, smooth updates."),
    ("Bundle size", "ships little JS?", "How much code users download. High = small."),
    ("Accessibility", "works for everyone?", "Keyboard, screen readers, focus, motion and contrast."),
    ("Developer experience", "pleasant to build with?", "Fast feedback, clear errors, little boilerplate."),
    ("Team scalability", "many devs at once?", "Teams can work in parallel without stepping on each other."),
]

# ---------------------------------------------------------------- journals
JOURNALS = [
    dict(
        key="distributed", vol=1, title="Distributed Design Patterns", short="distributed design patterns",
        theme="", subject="distributed systems", term="Fall term · 2026", weekdays=(0, 2, 4), start=date(2026, 9, 7),
        kicker="property of a very caffeinated student",
        lead="My class notes on <span class=\"hl\">distributed design patterns</span>, written up properly. {n} patterns in {c} collections. Each note covers the problem a pattern solves, a real-life analogy with doodles, how it works, what you gain and lose, how it scores on nine architecture characteristics, and the mistakes people make with it.",
        blurb="Resilience, data consistency, communication, scaling data and coordination for systems that run on more than one machine.",
        attrs=DISTRIBUTED_ATTRS, attrs_title="The nine ratings", attrs_side="architecture characteristics",
        handmade={"circuit-breaker", "saga"},
        collections=[
            ("resilience", "Resilience", "keep one failure from becoming everyone's failure"),
            ("consistency", "Data consistency", "keep data correct across services and databases"),
            ("communication", "Communication", "how services find and talk to each other"),
            ("data", "Scaling data", "store and read more data, faster"),
            ("coordination", "Coordination", "agree on who does what"),
        ],
        catalogue=[
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
        ],
    ),
    dict(
        key="frontend", vol=2, title="Frontend Design Patterns", short="frontend design patterns",
        theme="theme-frontend", subject="web frontend", term="Fall term · 2026", weekdays=(1, 3), start=date(2026, 9, 8),
        kicker="sketched between lectures and code reviews",
        lead="My notes on <span class=\"hl\">frontend design patterns</span>: the shapes that keep UIs fast, accessible and easy to change. {n} patterns in {c} collections, with the same eight sections as volume 1, rated on nine <b>frontend</b> qualities like bundle size, accessibility and developer experience. Examples use React + TypeScript, but the ideas travel.",
        blurb="Components, state and data, rendering and performance, and architecture for UIs that stay fast and easy to change.",
        attrs=FRONTEND_ATTRS, attrs_title="The nine frontend ratings", attrs_side="qualities that matter in the browser",
        handmade=set(),
        collections=[
            ("components", "Components", "split the UI into pieces that are easy to reuse"),
            ("state", "State &amp; data", "where data lives and how it changes"),
            ("rendering", "Rendering &amp; performance", "get pixels on screen fast and keep them smooth"),
            ("architecture", "Architecture &amp; resilience", "scale the codebase, the teams and the failures"),
        ],
        catalogue=[
            (1, "container-presentational", "Container & Presentational", "components", "Split components that fetch and decide from components that only display."),
            (2, "compound-components", "Compound Components", "components", "A set of components that work together and share state, like select and option."),
            (3, "custom-hooks", "Custom Hooks", "components", "Pull reusable stateful logic out of components into small, testable functions."),
            (4, "headless-components", "Headless Components", "components", "Ship behaviour and accessibility without markup or styles; you bring the looks."),
            (5, "global-store", "Global Store (Flux)", "state", "One store for shared app state, changed only through named actions."),
            (6, "server-state-cache", "Server-State Cache", "state", "Treat API data as a cache: show it instantly, revalidate in the background."),
            (7, "optimistic-ui", "Optimistic UI", "state", "Show the result before the server confirms, and roll back if it fails."),
            (8, "state-machines", "State Machines", "state", "Model UI as explicit states and allowed transitions, so impossible states can't happen."),
            (9, "ssr-hydration", "SSR & Hydration", "rendering", "Render HTML on the server for a fast first view, then make it interactive in the browser."),
            (10, "islands", "Islands Architecture", "rendering", "Ship static HTML and hydrate only the small interactive parts of the page."),
            (11, "code-splitting", "Code Splitting & Lazy Loading", "rendering", "Load only the code a screen needs now; fetch the rest when it's needed."),
            (12, "virtualization", "List Virtualization", "rendering", "Render only the rows on screen, even when the list has 100,000 items."),
            (13, "micro-frontends", "Micro-Frontends", "architecture", "Split a big frontend into apps owned and deployed by separate teams."),
            (14, "design-tokens", "Design Tokens", "architecture", "Name every colour, size and font once, and use those names everywhere."),
            (15, "error-boundaries", "Error Boundaries", "architecture", "Catch a crashing part of the UI and show a fallback, instead of a blank page."),
        ],
    ),
]

# Planned journals and other work, shown on the landing page.
PLANNED = [
    (3, "Testing Patterns", "Test doubles, contract tests, property-based tests, test pyramids and flaky-test hunting."),
    (4, "Security Patterns", "Zero trust, secrets handling, OAuth flows, input validation and threat modelling for builders."),
    (5, "Cloud &amp; DevOps Patterns", "Blue–green and canary releases, infrastructure as code, GitOps, observability and cost control."),
    (6, "Data &amp; Database Patterns", "Indexing, migrations, soft deletes, multitenancy, change data capture and analytics pipelines."),
    (7, "AI App Patterns", "Retrieval-augmented generation, agents and tools, evaluation, guardrails and cost-aware LLM apps."),
]
FUTURE_LOG = [
    ("Dec 2026", [("•", "Vol. 3 · Testing Patterns: first notes"), ("•", "Vol. 2 extra notes: Debounce &amp; Throttle, Progressive Enhancement")]),
    ("Jan 2027", [("•", "Vol. 4 · Security Patterns"), ("•", "Search across every journal")]),
    ("Feb 2027", [("•", "Vol. 5 · Cloud &amp; DevOps Patterns"), ("•", "One-page printable cheat sheet per collection")]),
    ("Mar 2027", [("•", "Vol. 6 · Data &amp; Database Patterns"), ("•", "Vol. 1 extra notes: Strangler Fig, Backpressure, Consistent Hashing")]),
    ("Apr 2027", [("•", "Vol. 7 · AI App Patterns"), ("•", "Quiz mode that remembers your score")]),
    ("Someday", [("•", "Static Generation &amp; ISR, Offline-first, Feature Flags (Vol. 2)"), ("•", "A “compare two patterns” page")]),
]


def lecture_date(j, num):
    week, slot = divmod(num - 1, len(j["weekdays"]))
    wd = j["weekdays"][slot]
    return j["start"] + timedelta(weeks=week, days=wd - j["start"].weekday())


def day_label(j, num):
    d = lecture_date(j, num)
    return f"{d.strftime('%a')} · {d.strftime('%d.%m.%y')}"


def coll(j, key):
    return next(c for c in j["collections"] if c[0] == key)


def entry(j, slug):
    return next(c for c in j["catalogue"] if c[1] == slug)


def pdf_name(num, slug):
    return f"{num:02d}-{slug}.pdf"


def journal_pdf(j):
    return f"{j['key']}-journal.pdf"


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


def foot(j=None):
    what = f"Vol. {j['vol']} · a student's bullet journal on {j['short']}" if j else "a shelf of student bullet journals on software design"
    return f'<footer class="foot"><span>Jef’s Notes · {what}</span><span>by {AUTHOR}</span></footer>'


def head(title, desc, depth):
    a = "../" * depth
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<meta name="theme-color" content="#E6E3DC">
{FONTS}
<link rel="stylesheet" href="{a}assets/notebook.css">
<link rel="stylesheet" href="{a}assets/bujo.css">
<link rel="icon" href="{a}assets/favicon.svg" type="image/svg+xml">
<script src="{a}assets/notebook.js" defer></script>
</head>'''


def body_open(j=None):
    cls = "bujo" + (f" {j['theme']}" if j and j["theme"] else "")
    return f'<body class="{cls}">'


def bar(j, depth, current=None, print_button=True, disabled=False):
    """depth: 0 = landing, 1 = journal index/all, 2 = a note."""
    root = "../" * depth
    cur = lambda k: ' aria-current="page"' if current == k else ""
    if j is None:
        nav = (f'<a href="{root}index.html#shelf"{cur("shelf")}>Journals</a>\n'
               f'      <a class="hide-sm" href="{root}index.html#future">Future log</a>')
        brand_small = "a shelf of design-pattern journals"
        btn = ""
    else:
        jp = "" if depth == 1 else "../"
        nav = (f'<a href="{root}index.html#shelf">Shelf</a>\n'
               f'      <a href="{jp}index.html#index"{cur("index")}>Index</a>\n'
               f'      <a class="hide-sm" href="{jp}all.html"{cur("all")}>Whole journal</a>')
        brand_small = f"vol. {j['vol']} · {j['short']}"
        if print_button:
            btn = f'\n      <button class="btn" type="button" data-print{" disabled" if disabled else ""}>{DL}Export as PDF</button>'
        else:
            btn = f'\n      <a class="btn" href="{jp}all.html?print">{DL}Export as PDF</a>'
    return f'''<header class="bar">
  <div class="bar-in">
    <a class="brand" href="{root}index.html"><b>Jef’s<span>.</span>Notes</b><small>{brand_small}</small></a>
    <nav aria-label="Main">
      {nav}{btn}
    </nav>
  </div>
</header>'''


def ratings_table(j, rows):
    assert len(rows) == 9, "nine ratings per note"
    trs = "\n".join(
        f'      <tr data-before="{b}" data-after="{a}"><td>{n}<small>{q}</small></td><td class="dcell"></td>'
        f'<td class="score"></td><td class="why">{why}</td></tr>'
        for (n, q, _), (b, a, why) in zip(j["attrs"], rows))
    return f'''  <div class="ratings-wrap table-scroll">
  <table class="ratings">
    <thead><tr><th scope="col">Quality</th><th scope="col">With the pattern</th><th scope="col">Before → after</th><th scope="col">Why</th></tr></thead>
    <tbody>
{trs}
    </tbody>
  </table>
  </div>
  <div class="legend"><span><i class="dot on"></i> kept</span><span><i class="dot gain"></i> gained</span><span><i class="dot lost"></i> lost</span><span>ratings are relative guidance for a typical app, not laws</span></div>'''


def li(items, cls=""):
    c = f' class="{cls}"' if cls else ""
    return f"<ul{c}>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


def h2(n, id_, title, side):
    return f'  <h2 id="{id_}"><span class="num">{n}</span>{title} <span class="side">{side}</span></h2>'


def pager(j, num):
    cat = j["catalogue"]
    prev = cat[num - 2] if num > 1 else None
    nxt = cat[num] if num < len(cat) else None
    a = (f'<a href="{prev[1]}.html"><small>← previous note</small>{prev[0]:02d} · {esc(prev[2])}</a>' if prev
         else '<a href="../index.html"><small>← back to</small>Index</a>')
    b = (f'<a href="{nxt[1]}.html"><small>Next note →</small>{nxt[0]:02d} · {esc(nxt[2])}</a>' if nxt
         else '<a href="../index.html"><small>back to →</small>Index</a>')
    return f'<nav class="pager" aria-label="Notes">\n  {a}\n  {b}\n</nav>'


def render_note(j, n):
    num, slug, title, ckey, summary = entry(j, n["slug"])
    cname = coll(j, ckey)[1]
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
        head(f"{title} · Jef’s Notes", summary, 2),
        body_open(j),
        '<a class="skip-link" href="#main">Skip to the notes</a>',
        bar(j, 2),
        '',
        '<main id="main" class="desk">',
        f'<article class="sheet" id="{slug}">',
        f'  {ROUGH}',
        f'  <div class="page-meta"><span class="day">{day_label(j, num)}</span><span class="topic">collection · <b>{cname.lower()}</b></span></div>',
        f'  <p class="kicker">{n["kicker"]}</p>',
        f'  <h1><span class="hl">{esc(title)}</span></h1>',
        f'  <div class="tldr">\n    <span class="tag">TL;DR</span>\n    <p>{n["tldr"]}</p>\n  </div>',
        f'  <ul class="chips" aria-label="At a glance">{chips}</ul>',
        KEY,
        h2(1, "problem", "The problem", n.get("problem_side", "why do we even need this?")),
        n["problem"], figs("problem_figs"), n.get("problem_after", ""),
        h2(2, "analogy", "Real-life analogy", n["analogy_side"]),
        n["analogy"], figs("analogy_figs"),
        f'''  <div class="table-scroll">
  <table class="map">
    <caption>Translating it to software</caption>
    <thead><tr><th scope="col">In real life</th><th scope="col">In your code</th></tr></thead>
    <tbody>
{maprows}
    </tbody>
  </table>
  </div>''',
        n.get("analogy_after", ""),
        h2(3, "how", "How it solves it", n["how_side"]),
        n["how"], figs("how_figs"),
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
        h2(5, "ratings", "Ratings" if j["key"] == "frontend" else "Architecture ratings", "1 = poor · 5 = great"),
        f'  <p>{n["baseline"]}</p>',
        ratings_table(j, n["ratings"]),
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
        pager(j, num),
        foot(j),
        '</main>',
        '</body>',
        '</html>',
        '',
    ]
    return "\n".join(p for p in parts if p)


def index_list(j, anchors=False):
    out = []
    for key, name, blurb in j["collections"]:
        items = []
        for num, slug, title, ckey, summary in j["catalogue"]:
            if ckey != key:
                continue
            href = f"#{slug}" if anchors else f"notes/{slug}.html"
            items.append(f'<li><a href="{href}"><span class="toc-n">{num:02d}</span><span class="toc-t">{esc(title)}'
                         f'<small>{esc(summary)}</small></span><span class="toc-p">p. {num:02d}</span></a></li>')
        out.append(f'  <h3 class="toc-coll">{name} <span>{esc(blurb)}</span></h3>\n  <ol class="toc">{"".join(items)}</ol>')
    return "\n".join(out)


def attrs_block(j):
    dl = "\n".join(f"    <div><dt>{n}</dt><dd>{d}</dd></div>" for n, _, d in j["attrs"])
    return f'''  <dl class="vocab">
{dl}
  </dl>
  <div class="legend"><span><i class="dot on"></i> kept</span><span><i class="dot gain"></i> gained with the pattern</span><span><i class="dot lost"></i> lost with the pattern</span></div>'''


def counts(j):
    return dict(n=len(j["catalogue"]), c=["zero", "one", "two", "three", "four", "five", "six"][len(j["collections"])])


def render_index(j):
    return "\n".join([
        head(f"{j['title']} · Jef’s Notes", j["blurb"], 1),
        body_open(j),
        '<a class="skip-link" href="#main">Skip to the index</a>',
        bar(j, 1, "index", print_button=False),
        '<main id="main" class="desk">',
        '<article class="sheet">',
        f'  <div class="page-meta"><span class="day">{j["term"]}</span><span class="topic">vol. {j["vol"]} · <b>{j["subject"]}</b></span></div>',
        f'  <p class="kicker">{j["kicker"]}</p>',
        f'  <h1 class="cover-title"><span class="hl">{esc(j["title"])}</span></h1>',
        f'  <p class="lead">{j["lead"].format(**counts(j))}</p>',
        KEY,
        '  <h2 id="index"><span class="num">✎</span>Index <span class="side">tap a note to open it</span></h2>',
        index_list(j),
        '  <h2 id="how-to-read"><span class="num">?</span>How every note is laid out <span class="side">same eight sections, every time</span></h2>',
        '''  <ol class="how-to">
    <li><b>The problem</b>: what breaks without the pattern, with a doodle.</li>
    <li><b>Real-life analogy</b>: an everyday version, plus a “translate to code” table.</li>
    <li><b>How it solves it</b>: diagrams, steps, vocabulary and a code card.</li>
    <li><b>Gains vs losses</b>: the trade-off spread.</li>
    <li><b>Ratings</b>: nine qualities, before → after.</li>
    <li><b>Common pitfalls</b>: each with its fix.</li>
    <li><b>When to use it</b>: and when to skip it.</li>
    <li><b>Self-check quiz</b>: tap a question to see the answer.</li>
  </ol>''',
        f'  <h2 id="ratings-key"><span class="num">★</span>{j["attrs_title"]} <span class="side">{j["attrs_side"]}</span></h2>',
        '  <p>Every note scores the pattern from 1 (poor) to 5 (great) on the same nine things, comparing an app <b>without</b> the pattern to the same app <b>with</b> it.</p>',
        attrs_block(j),
        '''  <div class="remember">
    <span class="tag">first law</span>
    <p>Everything in architecture is a trade-off. If you think you've found one that isn't, you haven't found the cost yet.</p>
  </div>''',
        f'''  <div class="export no-print">
    <a class="btn" href="all.html?print">{DL}Export the whole journal as PDF</a>
    <a class="btn btn--ghost" href="pdf/{journal_pdf(j)}">Download ready-made PDF</a>
    <span class="hint">On a phone, the ready-made PDF is the easiest way to save or share.</span>
  </div>''',
        '  <p class="folio">i</p>',
        '</article>',
        foot(j),
        '</main>',
        '</body>',
        '</html>',
        '',
    ])


def render_all(j):
    collect = " ".join(f"notes/{c[1]}.html" for c in j["catalogue"])
    return "\n".join([
        head(f"{j['title']} · Whole journal", "Every note on one page, ready to export as PDF.", 1),
        body_open(j),
        '<a class="skip-link" href="#main">Skip to the notes</a>',
        bar(j, 1, "all", print_button=True, disabled=True),
        f'<main id="main" class="desk" data-collect="{collect}">',
        '<section class="sheet">',
        f'  <div class="page-meta"><span class="day">{j["term"]}</span><span class="topic">vol. {j["vol"]} · <b>{j["subject"]}</b></span></div>',
        '  <p class="kicker">the whole journal, one note per page</p>',
        f'  <h1 class="cover-title"><span class="hl">{esc(j["title"])}</span></h1>',
        f'  <p class="lead">{j["blurb"]}</p>',
        KEY,
        '  <h2 id="index"><span class="num">✎</span>Index <span class="side">page numbers match the notes</span></h2>',
        index_list(j, anchors=True),
        f'''  <div class="export no-print">
    <button class="btn" type="button" data-print disabled>{DL}Export as PDF</button>
    <span class="hint" data-collect-status role="status">Loading notes…</span>
  </div>
  <p class="aside no-print">in the print window pick “Save as PDF” as the destination. Each note starts on a new page.</p>''',
        '</section>',
        '</main>',
        f'<footer class="foot desk" style="padding-block:0 40px"><span>Jef’s Notes · Vol. {j["vol"]} · by {AUTHOR}</span></footer>',
        '</body>',
        '</html>',
        '',
    ])


AUTHOR_NOTE = """  <h2 id="author"><span class="num">✎</span>A note from the author <span class="side">why I made these journals</span></h2>
  <aside class="author-note" aria-labelledby="author">
    <p class="lead">Your AI agent can write a saga orchestrator in eleven seconds. It cannot tell you whether you needed one.</p>
    <p>These notebooks are for that second part. They're for new developers learning what all the arrows mean, and for experienced ones who've been nodding along in design reviews since 2019. They're short on purpose. Read one on the train, in a tunnel with no signal, or while the progress bar says “Thinking…” for the fourth minute.</p>
    <p>Each note gives you three things:</p>
    <ul>
      <li><b>Better questions for the code review.</b> When the agent says “Done! ✅”, you'll know to ask: <i>is this idempotent? Where's the timeout? What happens when it runs twice?</i> Ask before you tell your boss it's done. Not after.</li>
      <li><b>Better prompts for the next ticket.</b> “Add retries” gets you a loop. “Add capped retries with jitter and an idempotency key, only on 5xx” gets you a pattern. Vocabulary is leverage.</li>
      <li><b>A sense of the trade-offs.</b> Every pattern here has a “what we lose” column. The agent rarely volunteers that column. Somebody in the room should know it exists.</li>
    </ul>
    <p>The honest origin story: I had usage left before my weekly limit reset, and wasting it felt worse than wasting snacks. So I asked the agent to help me write notes about what agents get wrong. It found this very relatable.</p>
    <p class="author-sign">Read one note a day. Argue with the ratings. Doodle in the margins.<br><span>by Jefrey Romel Tagunicar</span></p>
  </aside>"""


def render_landing():
    books = []
    for j in JOURNALS:
        k = j["key"]
        books.append(f'''    <li class="book book--{k}">
      <a class="book-cover" href="{k}/index.html" aria-label="Open Vol. {j['vol']}: {esc(j['title'])}">
        <span class="book-band" aria-hidden="true"></span>
        <span class="book-label"><small>vol. {j['vol']}</small><b>{esc(j['title'])}</b><i>{len(j['catalogue'])} notes · {len(j['collections'])} collections</i></span>
      </a>
      <div class="book-meta">
        <p>{j['blurb']}</p>
        <p class="book-actions"><a class="btn" href="{k}/index.html">Open journal</a><a class="btn btn--ghost" href="{k}/pdf/{journal_pdf(j)}">{DL}PDF</a></p>
      </div>
    </li>''')
    for vol, title, blurb in PLANNED:
        books.append(f'''    <li class="book book--planned">
      <div class="book-cover" aria-hidden="true"><span class="book-label"><small>vol. {vol}</small><b>{title}</b><i>planned</i></span></div>
      <div class="book-meta"><p><b>Vol. {vol} · {title}.</b> {blurb}</p></div>
    </li>''')
    months = []
    for month, items in FUTURE_LOG:
        lis = "".join(f'<li><span class="sig">{s}</span> {t}</li>' for s, t in items)
        months.append(f'    <div class="month"><h3>{month}</h3><ul>{lis}</ul></div>')
    total = sum(len(j["catalogue"]) for j in JOURNALS)
    return "\n".join([
        head("Jef’s Notes", "A shelf of student bullet journals on software design patterns, with doodles, analogies, trade-offs and ratings.", 0),
        body_open(),
        '<a class="skip-link" href="#main">Skip to the shelf</a>',
        bar(None, 0, "shelf"),
        '<main id="main" class="desk">',
        '<article class="sheet landing">',
        '  <div class="page-meta"><span class="day">The shelf · 2026</span><span class="topic">series · <b>software design</b></span></div>',
        '  <p class="kicker">hand-written field journals, one subject per volume</p>',
        '  <h1 class="cover-title"><span class="hl">Jef’s Notes</span></h1>',
        f'  <p class="lead">A student\'s bullet journals on software design patterns: what problem each pattern solves, an everyday analogy with doodles, how it works, what it costs, how it rates, and how people get it wrong. <b>{len(JOURNALS)} volumes, {total} notes</b> so far, more on the way.</p>',
        '  <h2 id="shelf"><span class="num">✎</span>The shelf <span class="side">pick a journal</span></h2>',
        f'  <ul class="shelf">\n{chr(10).join(books)}\n  </ul>',
        AUTHOR_NOTE,
        '  <h2 id="future"><span class="num">→</span>Future log <span class="side">plans, not promises</span></h2>',
        '  <p>In a bullet journal the <b>future log</b> is where next months\' plans go. Here\'s what I\'m planning to write next.</p>',
        f'  <div class="future">\n{chr(10).join(months)}\n  </div>',
        '  <h2 id="inside"><span class="num">?</span>What\'s inside every note <span class="side">same eight sections</span></h2>',
        '''  <ol class="how-to">
    <li><b>The problem</b> the pattern solves, with a doodle.</li>
    <li><b>A real-life analogy</b> and a “translate to code” table.</li>
    <li><b>How it works</b>: diagrams, steps, vocabulary, a code card.</li>
    <li><b>Gains vs losses</b>, side by side.</li>
    <li><b>Nine ratings</b> picked for each journal's subject.</li>
    <li><b>Common pitfalls</b> and their fixes.</li>
    <li><b>When to use it</b>, and when not to.</li>
    <li><b>A self-check quiz.</b></li>
  </ol>''',
        '  <p class="folio">✦</p>',
        '</article>',
        foot(),
        '</main>',
        '</body>',
        '</html>',
        '',
    ])


def redirect(to):
    return (f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Moved</title>'
            f'<meta http-equiv="refresh" content="0; url={to}"><link rel="canonical" href="{to}"></head>'
            f'<body><p>This page moved to <a href="{to}">{to}</a>.</p></body></html>\n')


def load_content(key):
    notes = {}
    for f in sorted((CONTENT / key).glob("*.py")):
        spec = importlib.util.spec_from_file_location(f"{key}_{f.stem}", f)
        mod = importlib.util.module_from_spec(spec)
        mod.__dict__["Doodle"] = Doodle
        spec.loader.exec_module(mod)
        for n in getattr(mod, "NOTES", []):
            notes[n["slug"]] = n
    return notes


def main():
    listing = []
    for j in JOURNALS:
        key = j["key"]
        out = PUBLIC / key
        (out / "notes").mkdir(parents=True, exist_ok=True)
        notes = load_content(key)
        missing = [c[1] for c in j["catalogue"] if c[1] not in notes and c[1] not in j["handmade"]]
        if missing:
            print(f"[{key}] no content yet for:", ", ".join(missing))
        for slug, n in notes.items():
            (out / "notes" / f"{slug}.html").write_text(render_note(j, n), encoding="utf-8")
        print(f"[{key}] wrote {len(notes)} notes")
        (out / "index.html").write_text(render_index(j), encoding="utf-8")
        (out / "all.html").write_text(render_all(j), encoding="utf-8")
        ready = [c for c in j["catalogue"] if c[1] in notes or c[1] in j["handmade"]]
        listing.append(dict(key=key, title=j["title"], all=f"{key}/all.html", pdf=f"{key}/pdf/{journal_pdf(j)}",
                            notes=[dict(num=c[0], slug=c[1], title=c[2], page=f"{key}/notes/{c[1]}.html",
                                        pdf=f"{key}/pdf/{pdf_name(c[0], c[1])}") for c in ready]))
    (PUBLIC / "index.html").write_text(render_landing(), encoding="utf-8")
    (PUBLIC / "journals.json").write_text(json.dumps(listing, indent=1), encoding="utf-8")
    # old links from before the shelf existed (everything was the distributed journal)
    old = PUBLIC / "notes"
    old.mkdir(exist_ok=True)
    for c in JOURNALS[0]["catalogue"]:
        (old / f"{c[1]}.html").write_text(redirect(f"../distributed/notes/{c[1]}.html"), encoding="utf-8")
    (PUBLIC / "all.html").write_text(redirect("distributed/all.html"), encoding="utf-8")
    print("wrote landing page, journals.json and redirects")


if __name__ == "__main__":
    main()
