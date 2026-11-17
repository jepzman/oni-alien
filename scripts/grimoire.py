"""Series 4 · The Darkside of the Corporation: a survival grimoire, in the "grimoire" skin.

Content lives in content/darkside/act-<n>.py as an ACT dict (see act-2.py). This module renders:
  public/darkside/index.html              the series page (all eight Acts)
  public/darkside/act-<n>/index.html      an Act's contents (the bestiary page)
  public/darkside/act-<n>/<slug>.html     one entry
Styles: public/assets/grimoire.css (two looks: candlelight and parchment); script: public/assets/grimoire.js
(the look switch and the difficulty tabs). Plan: docs/HANDOFF-darkside.md.
"""
import html
import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONTENT = ROOT / "content" / "darkside"
PUBLIC = ROOT / "public" / "darkside"

SERIES = "The Darkside of the Corporation"
SUBTITLE = "A Survival Grimoire for the Cursed Employed"
COMPANY = "MetroVolt Electric Corporation"

# Survival stats (all "high = good for you"); see docs/HANDOFF-darkside.md section 5.
STATS = [
    ("Sanity kept", "Emotional toll. High = little toll."),
    ("Career XP", "Visibility, skills and progress gained."),
    ("Mana saved", "Political capital it costs. High = cheap."),
    ("Armor", "Protects you later: paper trail, witnesses."),
    ("Stealth", "Low drama, little visibility risk."),
    ("Allies won", "Relationships gained, not spent."),
    ("Soul intact", "Could you explain it to your gran?"),
    ("Time drain", "How long it takes. High = quick."),
    ("Backfire safety", "A failed attempt costs little."),
]

# The eight Acts. Live ones have a content file; the rest show as planned.
ACTS = [
    (1, "The Court of Whispers", "Office politics", "Where power really lives: hidden thrones, the meeting before the meeting, ring-kissing and favouritism."),
    (2, "The Bestiary", "Difficult people", "Twelve creatures of the open plan, from the Credit Vampire to the Boundary Goblin, and the counter-spells that work."),
    (3, "The Throne Room", "Bad managers", "You cannot slay your lord. But you can manage them: micromanagers, absent lords, seagulls and the escape portal."),
    (4, "The Ascension", "Promotions and recognition", "How promotions are really decided, the invisible work curse, the raise duel and the rival for the throne."),
    (5, "The Famine", "Layoffs, budget cuts and reorgs", "Reading the omens, the budget bloodletting, the day of the calendar invite and the survivor's haunting."),
    (6, "The Outer Realms", "Clients, vendors and rival guilds", "The client demon, the eleven-headed hydra, the bake-off arena and the incumbent dragon."),
    (7, "The New Plagues", "The modern workplace", "Return-to-office decrees, the green dot of doom, the AI replacement prophecy and the cult of family."),
    (8, "The Inner Sanctum", "Keeping your soul", "Burnout, boundaries, the dark pact and knowing when to leave the dungeon."),
]
ROMAN = {1: "I", 2: "II", 3: "III", 4: "IV", 5: "V", 6: "VI", 7: "VII", 8: "VIII", 9: "IX", 10: "X", 11: "XI", 12: "XII"}

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">\n'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
         '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Pirata+One&family=IM+Fell+English+SC'
         '&family=EB+Garamond:ital,wght@0,400;0,600;0,700;1,400&family=Caveat:wght@500;700&family=Courier+Prime&display=swap">')
# Set the look before first paint, so a parchment reader never sees a flash of candlelight.
EARLY = ("<script>try{var l=localStorage.getItem('grimoire-look');if(l)document.documentElement.dataset.look=l}catch(e){}</script>")
DISCLAIMER = ("Satire with practical tips. Every company, person and creature in this grimoire is invented. "
              "For layoffs, contracts, harassment or discrimination, check your local law and get proper advice.")


def esc(s):
    return html.escape(s, quote=True)


def skulls(n, of=5):
    return f'<span class="skulls" role="img" aria-label="threat {n} of {of}">' + "".join(
        f'<svg class="skull {"on" if i < n else "off"}" aria-hidden="true"><use href="#g-skull"/></svg>' for i in range(of)) + "</span>"


def flames(n, of=5):
    """Soul cost, as drops of blood."""
    return f'<span class="cost" role="img" aria-label="soul cost {n} of {of}">' + "".join(
        f'<svg class="{"on" if i < n else "off"}" aria-hidden="true"><use href="#g-drop"/></svg>' for i in range(of)) + "</span>"


OMEN_EYE = ('<svg class="omen-eye" viewBox="0 0 30 18" aria-hidden="true"><g class="lid"><path d="M1 9 Q15 -3 29 9 Q15 21 1 9Z"/>'
            '<circle class="iris" cx="15" cy="9" r="4.6"/><ellipse cx="15" cy="9" rx="1.1" ry="3.8"/></g></svg>')


def thorns(seed=0):
    """A thorned divider under a heading; drips fall from it at slightly different places each time."""
    xs = [(60 + (seed * 97 + k * 151) % 600) for k in range(3)]
    tips = "".join(f'<path d="M{x} {8 + k % 2 * 3} l{6 if k % 2 else -5} -7 {1 if k % 2 else 8} {8 if k % 2 else 6}z"/>'
                   for k, x in enumerate(range(50 + seed * 13 % 40, 700, 85)))
    drips = "".join(f'<path class="drip d{k + 1}" d="M{x} 11 q-3 9 0 13 q3 -4 0 -13z"/>' for k, x in enumerate(xs[: 1 + seed % 3]))
    return ('<svg class="thorns" viewBox="0 0 700 34" preserveAspectRatio="none" aria-hidden="true">'
            '<path d="M0 10 C 120 2, 230 18, 350 10 S 580 2, 700 10" fill="none" stroke="currentColor" stroke-width="2"/>'
            '<path d="M0 13 C 140 8, 230 20, 350 13 S 600 6, 700 13" fill="none" stroke="currentColor" stroke-width=".8" opacity=".6"/>'
            f'<g fill="currentColor">{tips}{drips}</g></svg>')


def sigil(ring, label):
    """A slowly turning seal: the creature's favourite phrases around an eye that blinks."""
    return f'''<svg class="sigil" viewBox="0 0 200 200" role="img" aria-label="{esc(label)}">
      <defs><path id="rp" d="M100 100 m-78 0 a78 78 0 1 1 156 0 a78 78 0 1 1 -156 0"/><path id="rp2" d="M100 100 m-58 0 a58 58 0 1 1 116 0 a58 58 0 1 1 -116 0"/></defs>
      <circle cx="100" cy="100" r="94" class="sg-line" stroke-width="2"/><circle cx="100" cy="100" r="88" class="sg-line" stroke-width=".8"/>
      <g class="ring"><text class="sg-text" font-size="13" letter-spacing="1.6" textLength="480"><textPath href="#rp">{esc(ring)}</textPath></text></g>
      <circle cx="100" cy="100" r="68" class="sg-line" stroke-width="1.4"/>
      <g class="ring2"><text class="sg-runes" font-size="10" letter-spacing="3"><textPath href="#rp2">ᛗ ᛖ ᛏ ᚱ ᛟ · ᚹ ᛟ ᛚ ᛏ · ᛞ ᚨ ᚱ ᚲ · ᛋ ᛁ ᛞ ᛖ · ᚷ ᚱ ᛁ ᛞ ·</textPath></text></g>
      <path d="M100 52 L141 124 L59 124 Z" class="sg-line" stroke-width="1.6"/><path d="M100 148 L59 76 L141 76 Z" class="sg-line" stroke-width="1" opacity=".55"/>
      <g class="lid"><path d="M70 100 Q100 76 130 100 Q100 124 70 100Z" class="sg-eye"/><circle cx="100" cy="100" r="11" class="sg-iris"/><ellipse cx="100" cy="100" rx="2.6" ry="9"/></g>
    </svg>'''


ART = Path(__file__).resolve().parent.parent / "content" / "darkside" / "art"


def plate(e, no):
    f = ART / f"{e['slug']}.svg"
    if not f.exists():
        return ""
    cap = e.get("plate_caption", "")
    return (f'<figure class="plate">{f.read_text(encoding="utf-8")}'
            f'<figcaption><b>Plate {no}</b>{cap}</figcaption></figure>')


def load_act(n):
    f = CONTENT / f"act-{n}.py"
    if not f.exists():
        return None
    spec = importlib.util.spec_from_file_location(f"darkside_act_{n}", f)
    mod = importlib.util.module_from_spec(spec)
    mod.__dict__["note"] = note   # the Annotator's margin note helper
    spec.loader.exec_module(mod)
    return mod.ACT


# ---------------------------------------------------------------- page frame
def page(title, desc, depth, body, crumb=""):
    a = "../" * depth
    return f'''<!doctype html>
<html lang="en" data-look="candle">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<meta name="theme-color" content="#120d0b">
{EARLY}
{FONTS}
<link rel="stylesheet" href="{a}{ASSET("grimoire.css")}">
<link rel="icon" href="{a}assets/favicon.svg" type="image/svg+xml">
<script src="{a}{ASSET("grimoire.js")}" defer></script>
</head>
<body class="grimoire">
{SYMBOLS}
<div class="room" aria-hidden="true"><div class="fog"></div><div class="fog f2"></div></div>
<div class="watcher w1" aria-hidden="true"></div><div class="watcher w2" aria-hidden="true"></div><div class="watcher w3" aria-hidden="true"></div>
<a class="skip-link" href="#main">Skip to the text</a>
<header class="bar">
  <a class="brand" href="{a}darkside/index.html"><b>The Darkside</b><small>of the Corporation</small></a>
  <nav class="crumbs" aria-label="Breadcrumb">{crumb}</nav>
  <button class="look" type="button" data-look-toggle aria-label="Switch the page look">
    <span class="look-candle">🕯 Candlelight</span><span class="look-parch">📜 Parchment</span>
  </button>
</header>
<main id="main" class="tome">
{body}
</main>
<footer class="foot">
  <p>{SERIES} · a series in Jef’s Notes · <a href="{a}index.html">back to the shelf</a></p>
  <p class="disclaimer">{DISCLAIMER}</p>
</footer>
</body>
</html>
'''


SYMBOLS = ('<svg width="0" height="0" style="position:absolute" aria-hidden="true" focusable="false"><defs>'
  '<linearGradient id="g-flame" x1="0" y1="1" x2="0" y2="0"><stop offset="0" stop-color="#7d0d0f"/><stop offset=".6" stop-color="#e2361f"/><stop offset="1" stop-color="#ffc861"/></linearGradient>'
  '<symbol id="g-skull" viewBox="0 0 22 24"><path fill="currentColor" d="M11 1C5.5 1 2 4.8 2 9.6c0 3 1.4 5 3.2 6.2V20c0 1 .8 1.8 1.8 1.8h1.2v-2.4h1.4v2.4h2.8v-2.4h1.4v2.4H15c1 0 1.8-.8 1.8-1.8v-4.2C18.6 14.6 20 12.6 20 9.6 20 4.8 16.5 1 11 1z"/>'
  '<ellipse class="eye" cx="7.6" cy="10.4" rx="2.3" ry="2.6"/><ellipse class="eye" cx="14.4" cy="10.4" rx="2.3" ry="2.6"/><path fill="#000" d="M11 13.2l-1.3 2.6h2.6z"/></symbol>'
  '<symbol id="g-drop" viewBox="0 0 13 18"><path d="M6.5 0C6.5 0 0 8 0 11.6A6.5 6.5 0 0 0 13 11.6C13 8 6.5 0 6.5 0z"/></symbol>'
  '<symbol id="g-corner" viewBox="0 0 110 110"><g fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"><path d="M6 104 C6 50 20 20 104 6"/>'
  '<path d="M14 104 C16 60 34 30 104 14" stroke-width="1" opacity=".6"/><path d="M22 60 l-12 -6 M34 38 l-10 -12 M52 24 l-4 -14 M74 14 l2 -10 M14 82 l-9 2"/></g>'
  '<g fill="currentColor"><path d="M20 61 l-10 -9 12 4z"/><path d="M32 39 l-9 -13 11 9z"/><path d="M50 25 l-3 -15 6 13z"/><path d="M73 15 l3 -11 1 12z"/><circle cx="9" cy="104" r="3.4"/><circle cx="104" cy="9" r="3.4"/></g></symbol>'
  '</defs></svg>')
CORNERS = "".join(f'<svg class="corner {c}" aria-hidden="true"><use href="#g-corner"/></svg>' for c in ("tl", "tr", "bl", "br"))
TALLY = ('<svg class="tally" viewBox="0 0 150 40" aria-hidden="true"><g stroke="currentColor" stroke-width="2.4" stroke-linecap="round" fill="none">'
         '<path d="M6 6 v28 M13 5 v29 M20 6 v28 M27 5 v29 M2 28 L32 10"/><path d="M48 6 v28 M55 5 v29 M62 6 v28 M69 5 v29 M44 28 L74 10"/>'
         '<path d="M90 6 v28 M97 5 v29 M104 6 v28 M111 5 v29 M86 28 L116 10"/><path d="M130 6 v28 M137 5 v29"/></g></svg>')

ASSET = lambda name: f"assets/{name}"   # replaced by build_notes.asset (content-hash version tag)


# ---------------------------------------------------------------- an entry
def note(text):
    """The Annotator's margin note."""
    return f'<aside class="annot"><span class="annot-by">— the Annotator</span>{text}</aside>'


def render_entry(act, i, e):
    entries = act["entries"]
    no = i + 1
    omens = "".join(f"<li>{OMEN_EYE}<span>{o}</span></li>" for o in e["omens"])
    counters = "".join(
        f'<li><h4><span class="cn">{k}</span>{name}</h4><p>{how}</p>'
        + (f'<blockquote class="incant"><span>incantation</span>{inc}</blockquote>' if inc else "") + "</li>"
        for k, (name, how, inc) in enumerate(e["counters"], 1))
    forbidden = "".join(
        f'<li><h4>{name} {flames(cost)}</h4><p>{backfire}</p></li>' for name, cost, backfire in e["forbidden"])
    diff = e["difficulty"]
    tabs = "".join(
        f'<button type="button" role="tab" id="d-{k}" aria-controls="dp-{k}" aria-selected="{"true" if k == "normal" else "false"}"'
        f' tabindex="{0 if k == "normal" else -1}" class="dt dt-{k}">{label}</button>'
        for k, label in (("normal", "Normal"), ("nightmare", "Nightmare"), ("hell", "Hell")))
    def diff_body(d):
        """Old format: one paragraph. New format: dict(who=, know=[], do=[], avoid=, next=)."""
        if isinstance(d, str):
            return f"<p>{d}</p>"
        li = lambda xs: "".join(f"<li>{x}</li>" for x in xs)
        return (f'<p class="dp-who">{d["who"]}</p>'
                f'<div class="dp-grid"><div><h4>You’ll know it’s this level when</h4><ul>{li(d["know"])}</ul></div>'
                f'<div><h4>Do</h4><ol>{li(d["do"])}</ol></div></div>'
                f'<p class="dp-avoid"><b>Don’t:</b> {d["avoid"]}</p>'
                + (f'<p class="dp-next"><b>If it gets worse:</b> {d["next"]}</p>' if d.get("next") else ""))
    panels = "".join(
        f'<div class="dp dp-{k}" role="tabpanel" id="dp-{k}" aria-labelledby="d-{k}"{"" if k == "normal" else " data-hide"}>'
        f'<p class="dp-h">{label}</p>{diff_body(diff[k])}</div>'
        for k, label in (("normal", "Normal"), ("nightmare", "Nightmare"), ("hell", "Hell")))
    v2 = "mirror" in e   # the new format: no stats or loot; a mirror and a rehearsal instead
    stats = "" if v2 else "".join(
        f'<li><span class="sn" title="{esc(m)}">{name}</span><span class="pips" aria-label="{v} of 5">'
        + "".join(f'<i class="{"on" if p < v else "off"}"></i>' for p in range(5)) + f'</span><span class="sv">{v}</span></li>'
        for (name, m), v in zip(STATS, e["stats"]))
    loot_name, loot_desc, loot_body = e["loot"] if not v2 else ("", "", "")
    if v2:
        mirror = "".join(f"<li>{OMEN_EYE}<span>{m}</span></li>" for m in e["mirror"]["signs"])
        lines = "".join(
            (f'<p class="dir">{t}</p>' if who == "" else f'<p class="ln"><b>{who}</b><span>{t}</span></p>')
            for who, t in e["rehearsal"]["lines"])
        tail = f'''<section class="sec" id="mirror"><h2><span class="rn">VII</span>Are you the creature?</h2>
  {thorns(7)}
  <p class="lede">{e["mirror"]["intro"]}</p>
  <ul class="omens mirror">{mirror}</ul>
  <p class="mirror-cure"><b>The cure, if you ticked two:</b> {e["mirror"]["cure"]}</p>
  </section>

  <section class="sec" id="rehearsal"><h2><span class="rn">VIII</span>The rehearsal</h2>
  {thorns(8)}
  <p class="lede">{e["rehearsal"]["intro"]}</p>
  <div class="script"><p class="script-h">{e["rehearsal"]["title"]}</p>{lines}</div>
  {note(e["rehearsal"]["note"]) if e["rehearsal"].get("note") else ""}
  </section>'''
    else:
        tail = None
    trial = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in e["trial"])
    prev = entries[i - 1] if i > 0 else None
    nxt = entries[i + 1] if i + 1 < len(entries) else None
    pager = ('<nav class="pager" aria-label="Entries">'
             + (f'<a class="prev" href="{prev["slug"]}.html"><small>← entry {i}</small>{prev["name"]}</a>' if prev else
                '<a class="prev" href="index.html"><small>←</small>The contents</a>')
             + (f'<a class="next" href="{nxt["slug"]}.html"><small>entry {no + 1} →</small>{nxt["name"]}</a>' if nxt else
                '<a class="next" href="index.html"><small>the end of the Act →</small>Back to the bestiary</a>')
             + "</nav>")
    star = '<span class="flag">★ flagship entry</span>' if e.get("flagship") else ""
    body = f'''<article class="leaf entry">
  {CORNERS}{TALLY}<span class="scrawl" aria-hidden="true">{e.get("scrawl", "")}</span>
  <header class="entry-head">
    {sigil(e.get("ring", "PER MY LAST EMAIL ✠ CIRCLE BACK ✠ SYNERGY ✠"), "Sigil of " + e["name"])}
    <p class="eyebrow">Act {ROMAN[act["no"]]} · {act["title"]} · entry {no} of {len(entries)} {star}</p>
    <h1>{e["name"]}</h1>
    <p class="epithet">{e["epithet"]}</p>
    <dl class="tags">
      <div><dt>Threat</dt><dd>{skulls(e["threat"])}</dd></div>
      <div><dt>Habitat</dt><dd>{e["habitat"]}</dd></div>
      <div><dt>Weakness</dt><dd>{e["weakness"]}</dd></div>
    </dl>
  </header>
  {plate(e, ROMAN[no] if no in ROMAN else no)}

  <section class="sec" id="sighting"><h2><span class="rn">I</span>A sighting</h2>
  {thorns(1)}
  {e["sighting"]}
  </section>

  <section class="sec" id="know"><h2><span class="rn">II</span>Know thy enemy</h2>
  {thorns(2)}
  {e["know"]}
  </section>

  <section class="sec" id="omens"><h2><span class="rn">III</span>Signs and omens</h2>
  {thorns(3)}
  <p class="lede">Tick two or more and you are in its lair.</p>
  <ul class="omens">{omens}</ul>
  </section>

  <section class="sec" id="counter"><h2><span class="rn">IV</span>Counter-spells</h2>
  {thorns(4)}
  <ol class="counters">{counters}</ol>
  </section>

  <section class="sec" id="forbidden"><h2><span class="rn">V</span>Forbidden spells</h2>
  {thorns(5)}
  <p class="lede">Tempting. Effective for about a day. Each one has a soul cost <span class="flames-key">{flames(1, 1)} = one ember of your soul</span>.</p>
  <ul class="forbidden">{forbidden}</ul>
  </section>

  <section class="sec" id="difficulty"><h2><span class="rn">VI</span>Difficulty</h2>
  {thorns(6)}
  <p class="lede">The same creature at three strengths. Pick the one you're facing.</p>
  <div class="diff" data-diff><div class="dtabs" role="tablist" aria-label="Difficulty">{tabs}</div>{panels}</div>
  </section>

  {tail if v2 else ""}{"" if v2 else f'''<section class="sec" id="stats"><h2><span class="rn">VII</span>Survival stats</h2>
  {thorns(7)}
  <p class="lede">For the counter-spell <b>{e["stats_for"]}</b>. All stats: high = good for you.</p>
  <ul class="stats">{stats}</ul>
  </section>

  <section class="sec" id="loot"><h2><span class="rn">VIII</span>Loot drop</h2>
  {thorns(8)}
  <div class="loot"><p class="loot-h"><span class="chest" aria-hidden="true">⚿</span><b>{loot_name}</b></p><p>{loot_desc}</p>
  <pre>{esc(loot_body.strip(chr(10)))}</pre></div>
  </section>'''}

  <section class="sec" id="trial"><h2><span class="rn">IX</span>The trial</h2>
  {thorns(9)}
  <p class="lede">What would you do? Tap a question for the answer.</p>
  <div class="trial">{trial}</div>
  <p class="last-word"><span>The Annotator's last word</span>{e["last_word"]}</p>
  </section>
  {pager}
</article>'''
    crumb = (f'<a href="../index.html">Grimoire</a><span>›</span><a href="index.html">Act {ROMAN[act["no"]]}</a>'
             f'<span>›</span><b>{e["name"]}</b>')
    return page(f'{e["name"]} · {SERIES}', e["summary"], 2, body, crumb)


# ---------------------------------------------------------------- an Act's contents
def render_act(act):
    def thumb(e):
        f = ART / f"{e['slug']}.svg"
        if f.exists():
            return f'<span class="card-art" aria-hidden="true">{f.read_text(encoding="utf-8")}</span>'
        return (f'<span class="card-art card-art--sigil" aria-hidden="true">{sigil(e.get("ring", ""), e["name"])}'
                f'<span class="card-glyph">{e["sigil"]}</span></span>')
    rows = "".join(
        f'<li><a href="{e["slug"]}.html">{thumb(e)}'
        f'<span class="card-t"><small class="card-n">{ROMAN.get(i, i)}</small><b>{e["name"]}{" ★" if e.get("flagship") else ""}</b>'
        f'<i>{e["epithet"]}</i></span><span class="card-m">{skulls(e["threat"])}</span></a></li>'
        for i, e in enumerate(act["entries"], 1))
    cast = "".join(f'<li><b>{name}</b> <i>({pron})</i> {who}</li>' for name, pron, who in act["cast"])
    body = f'''<article class="leaf">
  {CORNERS}
  <p class="eyebrow">{SERIES} · Act {ROMAN[act["no"]]}</p>
  <h1>{act["title"]}</h1>
  <p class="epithet">{act["sub"]}</p>
  {act["intro"]}
  <h2 class="plain">{act.get("contents_title", "The creatures")} <small>{len(act["entries"])} entries · ★ flagship</small></h2>
  <ul class="bestiary-cards">{rows}</ul>
  <h2 class="plain">The souls you will meet</h2>
  <ul class="cast">{cast}</ul>
  <h2 class="plain">How to read an entry</h2>
  <ol class="howto">
    <li><b>A sighting</b>: the creature in the wild, at {COMPANY}.</li>
    <li><b>Know thy enemy</b>: why it behaves like this. Most monsters are just scared people with calendars.</li>
    <li><b>Signs and omens</b>, <b>counter-spells</b> (with the exact words: the <i>incantation</i>) and the <b>forbidden spells</b> you must not cast.</li>
    <li><b>Difficulty</b> (Normal, Nightmare, Hell), <b>survival stats</b>, a <b>loot drop</b> to copy, and <b>the trial</b>.</li>
  </ol>
</article>'''
    crumb = f'<a href="../index.html">Grimoire</a><span>›</span><b>Act {ROMAN[act["no"]]}</b>'
    return page(f'Act {ROMAN[act["no"]]} · {act["title"]} · {SERIES}', act["summary"], 2, body, crumb)


# ---------------------------------------------------------------- the series page
def render_series(acts):
    items = []
    for no, title, theme, blurb in ACTS:
        act = acts.get(no)
        if act:
            items.append(f'<li class="act act--live"><a href="act-{no}/index.html"><span class="act-no">Act {ROMAN[no]}</span>'
                         f'<b>{title}</b><small>{theme} · {len(act["entries"])} entries</small><p>{blurb}</p>'
                         f'<span class="act-go">Open the Act →</span></a></li>')
        else:
            items.append(f'<li class="act act--sealed"><div><span class="act-no">Act {ROMAN[no]}</span><b>{title}</b>'
                         f'<small>{theme} · sealed</small><p>{blurb}</p><span class="act-go">not yet unsealed</span></div></li>')
    body = f'''<article class="leaf cover">
  {CORNERS}
  {sigil("THE DARKSIDE ✠ OF THE CORPORATION ✠ A SURVIVAL GRIMOIRE ✠", "The seal of the grimoire")}
  <p class="eyebrow">a series in Jef’s Notes · found on Floor 13</p>
  <h1>{SERIES}</h1>
  <p class="epithet">{SUBTITLE}</p>
  <p class="lead">This book was found in a supply cupboard on Floor 13 of <b>The Grid</b>, the 31-storey glass tower of
  <b>{COMPANY}</b> (“Powering Tomorrow, Today™”). Floor 13 does not officially exist. Neither, officially, do the
  things in this book.</p>
  <p>It is written by <b>the Chronicler</b>, who has survived nineteen years, seven reorgs, four CEOs and one
  “transformation journey”. The margins belong to <b>the Annotator</b>, who left. Read it as a field guide to the
  parts of working life no onboarding deck mentions: politics, difficult people, bad managers, layoffs, promotions,
  rival vendors and impossible clients. The jokes are the wrapping paper. The advice inside is real.</p>
  {note("Every counter-spell in here worked for somebody. The forbidden spells also worked, for about a day.")}
  <h2 class="plain">The eight Acts</h2>
  <ul class="acts">{"".join(items)}</ul>
</article>'''
    return page(f"{SERIES}: {SUBTITLE}", "A funny, practical survival grimoire for office politics, difficult people, bad managers, layoffs and promotions.",
                1, body, "<b>Grimoire</b>")


def build(asset):
    """asset: build_notes.asset (adds the ?v= content hash). Returns the live Acts for the landing page."""
    global ASSET
    ASSET = asset
    acts = {no: a for no in range(1, 9) if (a := load_act(no))}
    PUBLIC.mkdir(parents=True, exist_ok=True)
    (PUBLIC / "index.html").write_text(render_series(acts), encoding="utf-8")
    for no, act in acts.items():
        out = PUBLIC / f"act-{no}"
        out.mkdir(exist_ok=True)
        (out / "index.html").write_text(render_act(act), encoding="utf-8")
        for i, e in enumerate(act["entries"]):
            (out / f'{e["slug"]}.html').write_text(render_entry(act, i, e), encoding="utf-8")
        print(f"[darkside] wrote act {no} ({len(act['entries'])} entries)")
    return acts
