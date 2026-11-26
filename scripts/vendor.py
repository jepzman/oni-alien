"""Series 5 · On the Client's Floor: the note page (skin `theme-vendor`, styles in public/assets/vendor.css).

A vendor note keeps the Series 2 parts (the situation, analogy, how it works, template card, ratings, pitfalls, when to
use it, quiz, try it) and adds: a visitor pass, an optional timesheet strip, both sides of the table, what the contract
says, account health (green / amber / red), a pressure gauge, “seen in the Grimoire” and the 23:00 note.
Plan and field list: docs/PLAN-vendor-side.md, section 10; facts: docs/lodestar-casebook.md.

Note fields (beyond the Series 2 ones):
  date         datetime.date of the scene (the page date)
  meta         short text after the date, e.g. "bid day 37 of 42" or "day 9 on site"
  pass_no      optional fixed pass number (default: by date)
  pass_kind    "visitor" (default) or "contractor" (from 4 Aug 2027, when the team gets its own badges)
  where        pass footer place, default "FL 19"
  timesheet    optional dict(week, label, booked=[7], worked=[7], note)
  sides        dict(client=(who, html, thought), vendor=(who, html, thought)), sides_after (html, optional)
  contract     dict(doc, date, stamp, clauses=[(no, html, margin or "")], plain)
  health       dict(now="g"|"a"|"r", g=(when, [items]), a=(...), r=(...))
  pressure     dict(level=1..5, title, cost, items=[...])
  grimoire     optional [(act, slug, name, html line)]
  late         dict(when, lines=[...])
"""
PASS_NO = 400


def visitor_pass(n):
    d = n["date"]
    kind = n.get("pass_kind", "visitor")
    band = "VISITOR · ESCORT REQUIRED" if kind == "visitor" else "CONTRACTOR · LODESTAR"
    cls = "vpass" + (" vpass--contractor" if kind != "visitor" else "")
    where = n.get("where", "FL 19")
    no = n.get("pass_no", PASS_NO + d.timetuple().tm_yday)
    return f'''  <div class="{cls}" aria-label="{'Visitor' if kind == 'visitor' else 'Contractor'} pass">
    <div class="vpass-in">
      <div class="vpass-top"><span>METROVOLT</span><small>THE GRID</small></div>
      <div class="vpass-body">
        <div class="vpass-photo" aria-hidden="true"><svg viewBox="0 0 52 62" width="40" height="48"><circle cx="26" cy="22" r="11" fill="#9AA2A6"/><path d="M6 60 q20 -30 40 0" fill="#9AA2A6"/></svg></div>
        <div><div class="vpass-name">Ines Duarte</div><div class="vpass-firm">Wrenfield Digital</div></div>
      </div>
      <div class="vpass-esc">{band}</div>
      <div class="vpass-foot"><span>{d.strftime("%d %b %y").upper()} · {where}</span><span>No. {no:04d}</span></div>
    </div>
  </div>'''


def timesheet(n):
    t = n.get("timesheet")
    if not t:
        return ""
    days = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")
    th = "".join(f'<th scope="col">{x}</th>' for x in days)
    num = lambda v: "–" if not v else (f"{v:.1f}" if isinstance(v, float) else str(v))
    row = lambda vals: "".join(f"<td>{num(v)}</td>" for v in vals) + f"<td>{sum(vals):.1f}</td>"
    return f'''  <div class="timesheet-scroll">
  <div class="timesheet">
    <table>
      <caption>Timesheet · {t["week"]} · {t["label"]}</caption>
      <thead><tr><th scope="col">{t.get("who", "Ines")}</th>{th}<th scope="col">Total</th></tr></thead>
      <tbody>
        <tr><td>booked</td>{row(t["booked"])}</tr>
        <tr class="worked"><td>worked</td>{row(t["worked"])}</tr>
      </tbody>
    </table>
    <p class="gap">{t["note"]}</p>
  </div>
  </div>'''


def sides_block(n):
    s = n["sides"]
    (cw, ch, ct), (vw, vh, vt) = s["client"], s["vendor"]
    after = f'\n  <p>{n["sides_after"]}</p>' if n.get("sides_after") else ""
    return f'''  <div class="sides">
    <div class="client">
      <h3><span class="who">MetroVolt</span> {cw}</h3>
      {ch}
      <p class="thought">“{ct}”</p>
    </div>
    <div class="vendor">
      <h3><span class="who">Wrenfield</span> {vw}</h3>
      {vh}
      <p class="thought">“{vt}”</p>
    </div>
  </div>{after}'''


def contract_block(n):
    c = n["contract"]
    stamp = f'\n    <span class="stamp">{c["stamp"]}</span>' if c.get("stamp") else ""
    clauses = ""
    for no, text, margin in c["clauses"]:
        clauses += f'\n    <p class="clause"><b>{no}</b> {text}</p>'
        if margin:
            clauses += f'\n    <span class="margin">{margin}</span>'
    return f'''  <div class="contract">
    <div class="doc"><span>{c["doc"]}</span><span>{c["date"]}</span></div>{stamp}{clauses}
    <p class="plain"><b>In plain words:</b> {c["plain"]}</p>
  </div>'''


HEALTH = (("g", "Green", "green"), ("a", "Amber", "amber"), ("r", "Red", "red"))


def health_block(n, li):
    h = n["health"]
    cols = ""
    for k, name, _ in HEALTH:
        when, items = h[k]
        now = h.get("now") == k
        tag = ' <span class="now-tag">Lodestar now</span>' if now else ""
        cols += (f'    <div class="{k}{" is-now" if now else ""}"><h3>{name}{tag} <span class="lamp"></span></h3>'
                 f'<p class="when">{when}</p>{li(items)}</div>\n')
    return f'  <div class="health">\n{cols}  </div>'


def pressure_block(n, li):
    p = n["pressure"]
    return f'''  <div class="pressure" style="--p: {p["level"]}">
    <svg viewBox="0 0 170 104" aria-hidden="true"><g class="rough">
      <path class="d d-thin" d="M15 88 A70 70 0 0 1 155 88"/>
      <path d="M15 88 A70 70 0 0 1 28 48" stroke="#8FD19E" stroke-width="10" fill="none"/>
      <path d="M28 48 A70 70 0 0 1 63 21" stroke="#CDE38A" stroke-width="10" fill="none"/>
      <path d="M63 21 A70 70 0 0 1 107 21" stroke="#F5C84C" stroke-width="10" fill="none"/>
      <path d="M107 21 A70 70 0 0 1 142 48" stroke="#F2A15A" stroke-width="10" fill="none"/>
      <path d="M142 48 A70 70 0 0 1 155 88" stroke="#F08A80" stroke-width="10" fill="none"/>
      <path class="d needle" d="M85 88 L85 30"/><circle class="f-ink" cx="85" cy="88" r="6"/>
    </g></svg>
    <div>
      <h3>{p["level"]} of 5 · {p["title"]}</h3>
      <p class="lvl">{p["cost"]}</p>
      {li(p["items"])}
    </div>
  </div>'''


def grimoire_block(n):
    g = n.get("grimoire")
    if not g:
        return ""
    names = " · ".join(f'<a href="../../darkside/act-{act}/{slug}.html">{name}</a>' for act, slug, name, _ in g)
    lines = " ".join(line for *_, line in g)
    return (f'  <div class="grimoire-aside">\n    <div class="sk" aria-hidden="true">☠</div>\n'
            f'    <div><small>Seen in the Grimoire</small><b>{names}</b>: {lines}</div>\n  </div>')


def late_block(n):
    t = n["late"]
    lines = "".join(f"\n    <p>{x}</p>" for x in t["lines"])
    return f'''  <div class="late">
    <span class="time">{t["when"]}</span>{lines}
    <p class="sign">— I.</p>
  </div>'''


def render_note(j, n, back, g):
    """g: build_notes' globals (the shared page helpers)."""
    esc, li, h2, entry, coll = g["esc"], g["li"], g["h2"], g["entry"], g["coll"]
    num, slug, title, ckey, summary = entry(j, n["slug"])
    cname = coll(j, ckey)[1]
    vocab = "\n".join(f"    <div><dt>{t}</dt><dd>{d}</dd></div>" for t, d in n["vocab"])
    maprows = "\n".join(f"      <tr><td>{a}</td><td>{b}</td></tr>" for a, b in n["map"])
    steps = "\n".join(f"    <li><b>{t}</b><p>{d}</p></li>" for t, d in n["steps"])
    pits = "\n".join(f'    <li><h3>{t}</h3><p>{d} <span class="fix">Fix →</span> {f}</p></li>' for t, d, f in n["pitfalls"])
    quiz = "\n".join(f"    <details><summary>{q}</summary><p>{a}</p></details>" for q, a in n["quiz"])
    related = g["related_items"](j, n["slug"], n["related"])
    chips = "".join(f"<li><b>{k}:</b> {v}</li>" for k, v in n["chips"])
    sources = "".join(f"<li>{s}</li>" for s in n["sources"])
    code = n["code"]
    figs = lambda key: "\n".join(f.html() for f in n.get(key, []))
    d = n["date"]
    day = f'{d.strftime("%a")} · {d.strftime("%d.%m.%y")}' + (f' · {n["meta"]}' if n.get("meta") else "")
    k = iter(range(1, 30))
    sec = lambda id_, t, side="": h2(next(k), id_, t, side)
    DL = g["DL"]
    parts = [
        g["head"](f"{title} · Jef’s Notes", summary, 2, j.get("fonts"), j.get("css", ())),
        g["body_open"](j),
        '<a class="skip-link" href="#main">Skip to the notes</a>',
        g["bar"](j, 2),
        '',
        '<main id="main" class="desk">',
        f'<article class="sheet" id="{slug}">',
        f'  {g["ROUGH"]}',
        visitor_pass(n),
        f'  <div class="page-meta"><span class="day">{day}</span><span class="topic">collection · <b>{cname.lower()}</b></span></div>',
        g["revised_stamp"](n),
        f'  <p class="kicker">{n["kicker"]}</p>',
        f'  <h1><span class="hl">{esc(title)}</span></h1>',
        f'  <div class="tldr">\n    <span class="tag">TL;DR</span>\n    <p>{n["tldr"]}</p>\n  </div>',
        f'  <ul class="chips" aria-label="At a glance">{chips}</ul>',
        timesheet(n),
        sec("problem", j.get("problem_h2", "The situation"), n.get("problem_side", "")),
        n["problem"], figs("problem_figs"), n.get("problem_after", ""), g["meanwhile_box"](j, n, back),
        sec("sides", "Both sides of the table", n.get("sides_side", "the same moment, seen twice")),
        sides_block(n),
        sec("analogy", "Real-life analogy", n["analogy_side"]),
        n["analogy"], figs("analogy_figs"),
        f'''  <div class="table-scroll">
  <table class="map">
    <caption>{j.get("map_caption", "Translating it to the job")}</caption>
    <thead><tr><th scope="col">In real life</th><th scope="col">{j.get("map_col", "On the job")}</th></tr></thead>
    <tbody>
{maprows}
    </tbody>
  </table>
  </div>''',
        sec("how", "How it works", n["how_side"]),
        n["how"], figs("how_figs"),
        f'  <ol class="steps">\n{steps}\n  </ol>',
        n.get("how_after", ""),
        f'  <h3>Vocabulary</h3>\n  <dl class="vocab">\n{vocab}\n  </dl>',
        f'''  <div class="card">
    <div class="card-head"><span>{esc(code["file"])}</span><span>{esc(code["note"])}</span></div>
<pre><code>{esc(code["src"].strip(chr(10)))}</code></pre>
  </div>''',
        f'  <p class="aside">{n["tools"]}</p>' if n.get("tools") else "",
        sec("contract", "What the contract says", n["contract"].get("side", "")),
        contract_block(n),
        sec("health", "Account health", "the same move, green, amber and red"),
        health_block(n, li),
        sec("pressure", "Pressure gauge", "how hard this is on the team"),
        pressure_block(n, li),
        sec("ratings", j["ratings_h2"], "1 = poor · 5 = great"),
        f'  <p>{n["baseline"]}</p>',
        g["ratings_table"](j, n["ratings"]).replace("for a typical app", "for a typical vendor engagement").replace(">With the pattern<", ">With the move<"),
        sec("pitfalls", "Common pitfalls", n.get("pitfalls_side", "the usual ways this goes wrong")),
        f'  <ul class="pits">\n{pits}\n  </ul>',
        grimoire_block(n),
        sec("when", "When to use it (and when not)"),
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
        f'  <h3>{j.get("related_h3", "Related notes")}</h3>\n  <ul class="related">{related}</ul>',
        g["extra_links"](j, slug),
        sec("quiz", "Self-check quiz"),
        f'  <div class="quiz">\n{quiz}\n  </div>',
        f'  <div class="tryit">\n    <span class="tag">try it</span>\n    <p>{n["try_it"]}</p>\n  </div>' if n.get("try_it") else "",
        f'  <div class="remember">\n    <span class="tag">remember!!</span>\n    <p>{n["remember"]}</p>\n  </div>',
        late_block(n),
        f'''  <div class="export no-print">
    <button class="btn" type="button" data-print>{DL}Export this note as PDF</button>
    {"" if j.get("draft") else f'<a class="btn btn--ghost" href="../pdf/{g["pdf_name"](num, slug)}">Download ready-made PDF</a>'}
    <span class="hint">In the print window choose “Save as PDF”. On a phone, the ready-made PDF is easiest.</span>
  </div>''',
        f'  <div class="sources">\n    <h3>Further reading</h3>\n    <ul>{sources}</ul>\n  </div>',
        g["title_block"](j, num, n),
        f'  <p class="folio">{num:02d}</p>',
        '</article>',
        '',
        g["pager"](j, num),
        g["foot"](j),
        '</main>',
        '</body>',
        '</html>',
        '',
    ]
    return "\n".join(p for p in parts if p)
