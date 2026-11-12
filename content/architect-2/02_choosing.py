# Series 2 · The Solution Architect's Notebook · Vol. 2 · Choosing well.
# Running case study: Larder (facts in docs/larder-casebook.md).

# ------------------------------------------------------------------ 05 Options Analysis
oa_problem = Doodle(760, 285, "Doodle of the first meeting about the Korenwolf pilot in April 2026. Femke says just make it work, Ben wants a new business-to-business service, Mo says Hanna wants it in three weeks, Grace says don't touch checkout. Four favourites, no criteria, and nobody mentions doing nothing.",
                    "Four people, four favourite answers, no criteria, and nobody suggests doing nothing.")
for i, (who, says, f) in enumerate([("Femke", "“just make it work”", "paper"), ("Ben", "“a new B2B service”", "blue"), ("Mo", "“Hanna: in 3 weeks”", "paper"), ("Grace", "“don't touch checkout”", "y")]):
    x = 20 + i * 185
    oa_problem.box(x, 24, 165, 70, who, f, sub=says, size=17, subsize=14)
    oa_problem.arrow(x + 82, 98, 270 + i * 74, 166, dash=True)
oa_problem.box(200, 170, 360, 60, "Korenwolf pilot: how?", "y", size=18)
oa_problem.note(380, 266, "four favourites, no criteria, no “do nothing”", "red")

oa_analogy = Doodle(760, 280, "Doodle of a family scoring three homes on a sheet: staying put, a flat in town and a house in the suburbs. Criteria are commute (weight 5), space (weight 3) and price (weight 4). Each option is scored 1 to 5 and multiplied by the weight. Staying put scores 41, the flat 39, the house 37. The scorecard starts the conversation; it doesn't end it.",
                     "Choosing a home: weights first, then scores, and “stay put” is one of the options.")
cols = [("stay put", 380), ("town flat", 510), ("suburb house", 650)]
oa_analogy.head(30, 40, "what matters", anchor="start", size=16)
oa_analogy.head(250, 40, "weight", size=16)
for name, x in cols:
    oa_analogy.head(x, 40, name, size=16)
for i, (crit, w, sc) in enumerate([("commute", 5, (3, 5, 2)), ("space", 3, (2, 2, 5)), ("price", 4, (5, 2, 3))]):
    y = 84 + i * 40
    oa_analogy.text(30, y, crit, anchor="start", size=17)
    oa_analogy.text(250, y, f"× {w}", size=17)
    for (name, x), v in zip(cols, sc):
        oa_analogy.text(x, y, str(v), size=17)
oa_analogy.line("M20 186 H730", thin=True)
oa_analogy.text(30, 214, "total", "t-head", anchor="start", size=17)
for (name, x), t in zip(cols, (41, 39, 37)):
    oa_analogy.text(x, 214, str(t), "t-head", size=18)
oa_analogy.box(345, 192, 70, 34, None, "hl", rx=6)
oa_analogy.note(380, 262, "the scorecard starts the conversation; it doesn't end it", "pen")

oa_how = Doodle(760, 360, "Larder's weighted options matrix for the Korenwolf pilot, 13 April 2026. Options: 0, manual orders entered by support; A, normal orders with a business flag; B, scheduled orders on business accounts; C, a new business ordering service. Criteria and weights: ready for 4 May (5), safe for consumer checkout (4), grows to three offices (3), effort during the Rotterdam launch (4), easy to undo (2). Totals: manual 74, flag 56, scheduled 68, new service 48. Decision: manual for the pilot; build B once a contract for more offices is signed.",
                "The matrix the team expected to back a new service. “Do nothing (by hand)” won the pilot; B waits for a contract.")
opts = [("0", "by hand", 360), ("A", "a flag", 460), ("B", "scheduled", 560), ("C", "new service", 670)]
oa_how.head(250, 44, "weight", size=14)
for letter, sub, x in opts:
    oa_how.head(x, 36, letter, size=22)
    oa_how.text(x, 58, sub, "t t-soft", size=14)
rows = [("Ready for 4 May", 5, (5, 4, 4, 1)), ("Safe for checkout (ASR 4)", 4, (5, 2, 4, 5)), ("Grows to 3 offices", 3, (1, 2, 4, 5)),
        ("Effort during Rotterdam", 4, (4, 4, 3, 1)), ("Easy to undo", 2, (5, 3, 4, 2))]
for i, (crit, w, sc) in enumerate(rows):
    y = 100 + i * 38
    oa_how.text(20, y, crit, anchor="start", size=15)
    oa_how.text(250, y, f"× {w}", size=15)
    for (letter, sub, x), v in zip(opts, sc):
        oa_how.text(x, y, str(v), size=15)
oa_how.line("M14 284 H746", thin=True)
oa_how.text(20, 310, "weighted total", "t-head", anchor="start", size=16)
oa_how.box(325, 288, 70, 34, None, "green", rx=6)
for (letter, sub, x), t in zip(opts, (74, 56, 68, 48)):
    oa_how.text(x, 312, str(t), "t-head", size=17)
oa_how.note(380, 348, "decided: by hand for the pilot · B once more offices sign", "green", size=18)

OPTIONS = dict(
    slug="options-analysis",
    kicker="a.k.a. “stay put is on the list too”",
    tldr="Before choosing, write down <b>three or four real options</b>, always including <b>“do nothing”</b> (or the simplest thing by hand). Take the <b>criteria from the drivers and constraints</b>, give them <b>weights before you score</b>, score each option, and look at the totals. The matrix doesn't decide; it makes the reasoning <b>visible and arguable</b>. When the result surprises you, find out why: either a criterion is missing, or your favourite wasn't as good as you thought.",
    chips=[("Family", "choosing well"), ("Origin", "decision matrices (Pugh, 1981); ATAM and trade-off analysis (SEI)"), ("Lives in", "the Options section of an ADR or RFC"), ("Pairs with", "business drivers, ADRs, trade-off sliders")],
    problem_side="Larder, 13 April 2026",
    problem="""  <p class="lead">Mo has a pilot: Korenwolf's Amsterdam HQ gets a <b>weekly pantry restock</b>, delivered 07:00–09:00 by van, invoiced monthly, from <b>4 May</b>. In the first meeting <b>Femke</b> says “just make it work”, <b>Ben</b> sketches a new B2B ordering service, <b>Mo</b> says Hanna wants it in three weeks, and <b>Grace</b> says “don't touch checkout”. Everyone argues for their <span class="hl-pink">favourite answer</span>. Nobody has listed the options, and nobody has asked what “good” means.</p>
  <ul>
    <li>Debates between favourites go round in circles: each person scores by different criteria.</li>
    <li>“Do nothing” or “do it by hand” is rarely on the list, though it often wins.</li>
    <li>Rotterdam opens in two weeks; the team can't afford the wrong big build.</li>
  </ul>""",
    problem_figs=[oa_problem],
    analogy_side="choosing a home",
    analogy="""  <p>A family thinking about moving writes down what matters (<b>commute, space, price</b>) and how much, <b>before</b> the viewings, or the nicest kitchen wins. Each home gets a score per criterion. And <b>staying put</b> goes on the sheet too: sometimes it wins, and that's a fine answer. The totals don't buy the house; they make the family's reasoning visible, so they can argue about the right thing.</p>""",
    analogy_figs=[oa_analogy],
    map=[("The homes you view", "Options A, B, C"),
         ("Staying put", "Option 0: do nothing, or do it by hand"),
         ("What matters, and how much", "Criteria from the drivers and constraints, weighted first"),
         ("Scores per home", "1–5 per option per criterion"),
         ("Talking it over at the kitchen table", "Discussing surprises before deciding")],
    how_side="options, weights, scores, then talk",
    how="""  <p>The team expected the matrix to back a new service. Instead <b>option 0</b> (Mo's spreadsheet, with support entering one standing order a week by hand) won: the pilot is <b>one office for twelve weeks</b>, and the team's effort belongs to Rotterdam. The real insight wasn't the number; it was the trigger it exposed: <b>build B when a second office signs</b>.</p>""",
    how_figs=[oa_how],
    steps=[("Frame the question", "One sentence, with its deadline: “How do Korenwolf's weekly orders reach the store by 4 May?”"),
           ("List 3–4 real options", "Including 0: do nothing, or do it by hand. Each option described in two lines."),
           ("Pick criteria from the drivers", "Deadlines, ASRs, constraints, effort, reversibility. Five or six, no more."),
           ("Weight before scoring", "Agree the weights with the approver first, so nobody tunes them to a favourite."),
           ("Score and total", "1–5 each, with one line of reasoning per score; multiply by the weight."),
           ("Discuss, decide, record", "Ask why the result surprises anyone; then decide and write the ADR, with the triggers for revisiting.")],
    vocab=[("Option 0", "Do nothing, or the simplest manual way: the baseline every option must beat."),
           ("Criterion", "A thing that makes an option better or worse, taken from the drivers."),
           ("Weight", "How much a criterion matters, agreed before scoring."),
           ("Weighted score", "Score × weight, summed per option."),
           ("Must-have", "A criterion that rules an option out if it fails, before scoring."),
           ("Sensitivity check", "Changing a weight a little: does the winner change?")],
    code=dict(file="docs/adr/0011-korenwolf-pilot-manual-orders.md", note="the Options section of ADR 0011", plain=True, src="""
# 11. Run the Korenwolf pilot on manual standing orders

Status: Accepted · 2026-04-15 · Approver: Femke · Driver: Ana · with Mo, Ben, Grace

## Question
How do Korenwolf's weekly pantry orders reach store Zuid, from 4 May,
for a 12-week pilot at one office?

## Options                                        weights: 5   4   3   4   2
0. Support enters one standing order a week                 5   5   1   4   5 = 74
1. (A) Normal orders with a "business" flag                 4   2   2   4   3 = 56
2. (B) Scheduled orders on business accounts, in Ordering   4   4   4   3   4 = 68
3. (C) A new Business Ordering service                      1   5   5   1   2 = 48
Criteria: ready by 4 May · safe for consumer checkout (ASR 4) · grows to
3 offices · effort during the Rotterdam launch · easy to undo

## Decision
Option 0 for the pilot: ~3 h/week of support time, invoices from Mo's sheet.
Sensitivity: B wins only if "grows to 3 offices" weighs 5 or more.

## Revisit when
Korenwolf (or any client) signs for more than one office → build B.
"""),
    tools="tools: a table in the ADR is enough; a spreadsheet for a sensitivity check. Heavier methods: ATAM and CBAM (SEI), Pugh matrices, AHP for many criteria. Most architecture tools don't add much here.",
    gains=["<b>Visible reasoning</b>: people argue about criteria, not favourites.",
           "<b>“Do nothing” gets a fair hearing</b>, and often wins.",
           "<b>Criteria tie back to the drivers</b>, not to taste.",
           "<b>Triggers fall out of it</b>: what would change the answer.",
           "<b>Feeds the ADR</b> directly: the Options section is written."],
    losses=["<b>False precision</b>: 68 vs 74 looks exact; it isn't.",
            "<b>Gameable</b>: weights tuned to a favourite.",
            "<b>Time</b>: an hour or two with the right people.",
            "<b>Misses what isn't a criterion</b>: politics, morale, timing."],
    baseline="Each line compares <b>debating favourite answers until someone gives up</b> to <b>three or four options, including doing nothing, scored against weighted criteria from the drivers</b>.",
    ratings=[(2, 4, "The choice and why it won are written down."),
             (2, 4, "Everyone agrees the criteria before the scores."),
             (2, 4, "One session instead of a week of circling."),
             (2, 4, "Weak options fail on criteria, not after building."),
             (3, 4, "The triggers say when to switch to another option."),
             (2, 5, "The scored table goes straight into the ADR."),
             (2, 4, "Effort and cost are criteria, weighed openly."),
             (3, 3, "An hour or two per big decision."),
             (2, 3, "Teams can run it themselves; the approver still decides.")],
    pitfalls=[("Weights after scores", "The weights are adjusted until the favourite wins.", "agree weights with the approver before anyone scores."),
              ("No option 0", "Every option is a build.", "always score “do nothing” or “do it by hand”."),
              ("Trusting decimals", "68 vs 74 treated as a verdict.", "run a sensitivity check; close totals mean talk, not tally."),
              ("Straw-man options", "Two silly options next to the real one.", "only options someone would seriously defend.")],
    use=["Decisions with three or more defensible options.",
         "When a meeting has gone round in circles.",
         "Anything going into an ADR or RFC.",
         "When stakeholders weigh things differently and need to see it."],
    skip=["Two-way doors: try one and see.",
          "When one option fails a must-have: no matrix needed.",
          "Tiny decisions: a line in the decision log."],
    related=["<b>Architecture decision records</b> (this volume)", "<b>Trade-off sliders</b> (this volume)", "<b>Business drivers &amp; goals</b> (Vol. 1)", "<b>Build vs buy vs open source</b> (this volume)"],
    quiz=[("Which option should always be on the list?", "Option 0: do nothing, or the simplest manual way."),
          ("Why agree the weights before scoring?", "So nobody tunes the weights until their favourite wins."),
          ("Where should the criteria come from?", "The business drivers, ASRs and constraints, not personal taste."),
          ("The totals are 68 and 74. What next?", "Check sensitivity and discuss why; close totals mean the criteria need talking about, not that 74 wins automatically.")],
    try_it="Take a decision your team is debating now. Write the question in one sentence, list three options plus option 0, and pick five criteria from your goals. Get the approver to set the weights before anyone scores. Score it in 30 minutes with two colleagues and note whether option 0 surprised you.",
    remember="Weights <span class=\"hl\">before</span> scores. And <span class=\"hl\">stay put</span> is always on the list.",
    sources=["Stuart Pugh, <i>Total Design</i> (1991), on decision matrices.",
             "Rick Kazman, Mark Klein, Paul Clements, “ATAM: Method for Architecture Evaluation” (SEI, 2000).",
             "Neal Ford, Mark Richards et al., <i>Software Architecture: The Hard Parts</i> (2021), on trade-off analysis.",
             "Michael Keeling, <i>Design It!</i> (2017), “Make decisions with a decision matrix”."],
)

# ------------------------------------------------------------------ 06 Trade-off Sliders
ts_problem = Doodle(760, 290, "Doodle of five sliders, every one pushed to maximum, in a Rotterdam planning meeting in March 2026: the launch date for Femke, reliability for Joost, substitution approvals for Grace, cost for Marco and polished internal tools for Dee. With everything at maximum, nobody knows what gives when two collide.",
                    "Everything at maximum is the same as no priorities: nobody knows what gives.")
for i, label in enumerate(["launch date (Femke)", "reliability (Joost)", "approvals (Grace)", "cost (Marco)", "polish (Dee)"]):
    y = 46 + i * 44
    ts_problem.text(20, y + 6, label, anchor="start", size=16)
    ts_problem.line(f"M240 {y} H640", thin=True)
    ts_problem.circle(640, y, 12, fill="pink", stroke="red")
    ts_problem.note(692, y + 6, "max", "red", size=18)
ts_problem.note(380, 272, "five priorities, all number one", "red")

ts_analogy = Doodle(760, 280, "Doodle of a sound engineer's mixing desk with five faders: vocals, drums, bass, guitar and keys. Pushing every fader to the top just makes everything loud and distorted. In a good mix the singer is on top and every other instrument has its own, lower place.",
                    "A mixing desk: push every fader up and it just distorts. Give each one its place.")
for i, (name, lvl) in enumerate([("vocals", 1.0), ("drums", 0.75), ("bass", 0.55), ("guitar", 0.4), ("keys", 0.2)]):
    x = 110 + i * 135
    ts_analogy.line(f"M{x} 40 V190", thin=True)
    y = 190 - lvl * 150
    ts_analogy.box(x - 22, y - 10, 44, 20, None, "y" if i else "green", rx=4)
    ts_analogy.text(x, 220, name, size=17)
ts_analogy.note(380, 262, "the singer on top; the rest make room", "green")

ts_how = Doodle(760, 330, "Larder's agreed sliders for the Rotterdam launch, 31 March 2026, each on a different notch. Launch date 27 April: fixed, the lease is signed. Orders safe and paid once: no shortcuts, it's ASR 4. A city as configuration: a little hard-coding is allowed but logged as debt. Feature scope: substitution approvals go to Amsterdam first. Internal tool polish: after launch.",
                "Five sliders, five different notches. When two collide, the higher one wins, and nobody needs a meeting.")
for k, t in enumerate(["give", "", "", "", "hold"]):
    if t:
        ts_how.note(232 + k * 60, 26, t, "pen", size=16)
for i, (label, pos, why) in enumerate([("launch date 27 Apr", 5, "fixed: the lease is signed"), ("orders safe, paid once", 4, "ASR 4: no shortcuts"),
                                       ("city as configuration", 3, "some hard-coding, logged as debt"), ("feature scope", 2, "approvals: Amsterdam first"),
                                       ("internal tool polish", 1, "after launch")]):
    y = 62 + i * 50
    ts_how.text(20, y + 6, label, anchor="start", size=15)
    ts_how.line(f"M232 {y} H472", thin=True)
    for k in range(5):
        ts_how.line(f"M{232 + k * 60} {y - 6} V{y + 6}", thin=True)
    ts_how.circle(232 + (pos - 1) * 60, y, 12, fill="green" if pos == 5 else "y")
    ts_how.text(494, y + 6, why, anchor="start", size=14)
ts_how.note(380, 314, "one slider per notch: no ties allowed", "green")

SLIDERS = dict(
    slug="trade-off-sliders",
    kicker="a.k.a. “the mixing desk”",
    tldr="Qualities collide: date against scope, cost against reliability, speed against polish. Decide <b>in advance</b> which gives way. List the <b>four to six things</b> people care about as sliders, and put each on a <b>different notch</b>, with the business in the room: one is fixed, one is most flexible, <b>no ties</b>. Then every later trade-off has an answer that doesn't need a meeting: when two collide, the <b>higher slider wins</b>.",
    chips=[("Family", "choosing well"), ("Origin", "project trade-off sliders (Rob Thomsett; Mike Cohn; Microsoft Solutions Framework)"), ("Lives in", "the project one-pager, next to the drivers"), ("Pairs with", "business drivers, quality attribute scenarios, technical debt register")],
    problem_side="Larder, 31 March 2026",
    problem="""  <p class="lead">Four weeks before Rotterdam opens, the planning meeting stalls. <b>Femke</b> says the date is non-negotiable. <b>Joost</b> says reliability is. <b>Grace</b> wants substitution approvals live in Rotterdam from day one. <b>Marco</b> wants no extra cost. <b>Dee</b> wants the internal tools polished. Sanne's plan can't satisfy all five, and every collision is <span class="hl-pink">escalated to Femke</span>, one at a time.</p>
  <ul>
    <li>Everything is priority one, so nothing is.</li>
    <li>Each trade-off becomes a fresh negotiation, often with whoever shouts loudest.</li>
    <li>Teams make the call alone, differently from each other.</li>
  </ul>""",
    problem_figs=[ts_problem],
    analogy_side="the mixing desk",
    analogy="""  <p>A sound engineer can't push every fader to the top: the mix just gets loud and <b>distorts</b>. A good mix puts <b>the singer on top</b>, and every other instrument gets its own, lower place. The engineer decides that before the concert, not during each song.</p>""",
    analogy_figs=[ts_analogy],
    map=[("A fader", "A slider: one thing people care about"),
         ("The singer on top", "The fixed slider: Rotterdam's date"),
         ("Each instrument at its own level", "Each slider on its own notch, no ties"),
         ("Distortion from everything at max", "Plans that can't be met, escalations"),
         ("Set before the concert", "Agreed once, with the business, before the trade-offs come")],
    how_side="one notch each, agreed with the business",
    how="""  <p>The sliders worked within a week. When Rotterdam's store setup needed <b>three values hard-coded</b> to make the date, nobody escalated: the date slider is above “city as configuration”, so the team did it and <b>logged it as debt</b>. Substitution approvals went to Amsterdam first, as agreed.</p>""",
    how_figs=[ts_how],
    steps=[("List what people care about", "Four to six things: date, scope, quality attributes, cost, polish. Use their words."),
           ("Get the business in the room", "The people who'd escalate later must agree now: here, Femke, Joost, Priya, Sanne."),
           ("One notch each", "Rank them: one fixed, one most flexible, no ties. Arguments here are the point."),
           ("Say what “give” means", "For each lower slider, what may give: “approvals: Amsterdam first”, “hard-coding, logged as debt”."),
           ("Publish it", "On the project one-pager, next to the drivers. Read it at planning."),
           ("Re-rank when the world changes", "After launch, the date slider drops; reliability and cost rise.")],
    vocab=[("Trade-off slider", "One concern, placed on a scale from “holds” to “gives”."),
           ("Fixed", "The slider that doesn't move: everything else bends around it."),
           ("Give", "What may slip, shrink or wait when sliders collide."),
           ("Iron triangle", "The old trio: scope, time, cost (quality in the middle)."),
           ("Escalation", "Sending a trade-off up because nobody may decide it."),
           ("Re-ranking", "Moving sliders on purpose when the situation changes.")],
    code=dict(file="docs/rotterdam/one-pager.md", note="trade-off sliders, as agreed on 31 March 2026", plain=True, src="""
## Trade-off sliders · Rotterdam launch    agreed: Femke, Joost, Priya, Sanne, Ana, Grace

                         gives  1   2   3   4   5  holds
Launch date 27 Apr                              ●      the lease is signed
Orders safe, paid once                      ●          ASR 4; never traded
City as configuration                   ●              hard-coding allowed only
                                                       if logged as debt (TD-1)
Feature scope                       ●                  substitution approvals:
                                                       Amsterdam first, RTM in June
Internal tool polish            ●                      after launch

Rule: when two collide, the higher one wins. No ties.
Review: after launch (week of 11 May): expect date ↓, reliability and cost ↑.
"""),
    tools="tools: a drawing on the project one-pager is enough. Variants: Mike Cohn's project sliders, the Microsoft Solutions Framework trade-off triangle, Basecamp's “fixed time, variable scope” (Shape Up).",
    gains=["<b>Fewer escalations</b>: most trade-offs answer themselves.",
           "<b>Shared priorities</b> agreed by the people who'd argue later.",
           "<b>Faster team decisions</b> that match each other.",
           "<b>Honest plans</b>: something is allowed to give.",
           "<b>Debt is deliberate</b>, because “give” is defined."],
    losses=["<b>An awkward meeting</b>: ranking forces disagreements out.",
            "<b>Too coarse</b> for subtle trade-offs inside one slider.",
            "<b>Goes stale</b> if not re-ranked after launch.",
            "<b>Can be ignored</b> by a senior person in a hurry."],
    baseline="Each line compares <b>“everything is priority one” and escalating each collision</b> to <b>four to six sliders on different notches, agreed with the business before the trade-offs come</b>.",
    ratings=[(2, 4, "Everyone can read what gives first."),
             (1, 5, "The business ranks its own priorities, out loud."),
             (2, 5, "Collisions resolve without a meeting."),
             (2, 4, "What may give is decided before it's under pressure."),
             (3, 4, "Re-ranking is a known step, not a crisis."),
             (2, 3, "The sliders explain why a shortcut was taken."),
             (2, 4, "Cost is a slider, ranked against the rest."),
             (3, 4, "One meeting, one drawing; a review after launch."),
             (2, 5, "Teams make trade-offs alone, in the agreed direction.")],
    pitfalls=[("Ties", "Two sliders on 5.", "one notch each; the argument about which goes higher is the value."),
              ("Only engineers in the room", "The business re-ranks it in the first escalation.", "the people who'd overrule it must agree it."),
              ("No meaning for “give”", "“Scope gives” means nothing at 17:00 on a Friday.", "write what giving looks like for each slider."),
              ("Never re-ranked", "The date slider still rules three months after launch.", "set a review date when you agree them.")],
    use=["A launch or project with a fixed date.",
         "When the same trade-off keeps escalating.",
         "Kick-offs, next to the business drivers.",
         "When teams make conflicting shortcuts."],
    skip=["Purely technical choices inside one team.",
          "When one driver dwarfs all others and everyone already knows it."],
    related=["<b>Options analysis</b> (this volume)", "<b>Technical debt register</b> (this volume)", "<b>Business drivers &amp; goals</b> (Vol. 1)", "<b>Quality attribute utility tree</b> (Vol. 5)"],
    quiz=[("Why must every slider sit on a different notch?", "Ties hide the real priority; the next collision gets escalated instead of answered."),
          ("Who must agree the sliders?", "The people who'd overrule them later, usually the business sponsors, with the team."),
          ("Rotterdam needs three values hard-coded to make the date. What do the sliders say?", "The date is above “city as configuration”, so hard-code them and log the debt."),
          ("When should sliders be re-ranked?", "When the situation changes, e.g. after the launch date has passed.")],
    try_it="Write five things your stakeholders care about on your current project. Rank them yourself, one per notch, then ask your sponsor to rank them without seeing yours. Compare the two in a 20-minute conversation and publish the agreed version on the project page.",
    remember="Not every fader at the top. <span class=\"hl\">One notch each</span>, and the <span class=\"hl\">singer</span> on top.",
    sources=["Mike Cohn, <i>Agile Estimating and Planning</i> (2005), on project trade-off sliders.",
             "Rob Thomsett, <i>Radical Project Management</i> (2002), project sliders.",
             "Ryan Singer, <i>Shape Up</i> (Basecamp, 2019): fixed time, variable scope.",
             "Microsoft Solutions Framework, “Trade-off triangle and matrix”."],
)

# ------------------------------------------------------------------ 07 One-way vs Two-way Doors
od_problem = Doodle(760, 290, "Doodle of a queue of decisions waiting for Ana's Thursday architecture meeting in April 2026: which log library, a cache timeout, the picker screen layout, and a two-year payment provider contract. Thirty-one decisions wait, two weeks in the queue, and the small ones wait as long as the big one.",
                    "Thirty-one decisions in one queue: the log library waits as long as the two-year contract.")
for i, (t, f) in enumerate([("log library?", "paper"), ("cache timeout: 60 or 120 s?", "paper"), ("picker screen layout?", "paper"), ("2-year payment contract?", "pink")]):
    y = 30 + i * 52
    od_problem.box(20, y, 320, 42, t, f, size=15, rx=6)
    od_problem.arrow(346, y + 21, 484, 120, dash=True)
od_problem.box(490, 70, 250, 100, "Ana's Thursday meeting", "y", sub="8 decisions a week", size=16)
od_problem.note(380, 272, "31 waiting · 2 weeks in the queue", "red")

od_analogy = Doodle(760, 270, "Doodle of two doors at an airport. A shop door in the terminal: walk in, look around, walk out again. The passport-control exit marked 'no re-entry': once through, you can't come back. You walk through shop doors without thinking; you check your bag before the one-way door.",
                    "At the airport: wander through shop doors; check your bag before the one marked “no re-entry”.")
od_analogy.icon("door", 130, 40, 1.6)
od_analogy.arrow(80, 120, 120, 120)
od_analogy.arrow(220, 120, 260, 120)
od_analogy.arrow(260, 150, 220, 150)
od_analogy.box(40, 200, 290, 48, "shop door: in and out", "green", size=16)
od_analogy.icon("door", 500, 40, 1.6)
od_analogy.box(560, 30, 170, 36, "no re-entry", "pink", stroke="red", size=15)
od_analogy.arrow(590, 120, 660, 120, color="red")
od_analogy.box(420, 200, 320, 48, "passport exit: one way", "pink", size=16)

od_how = Doodle(760, 330, "Larder sorts its 31 open decisions in April 2026. Twenty-four are two-way doors: decide in the team this week, for example the substitution window behind a flag, the cache timeout, the picker screen layout and the log library. Seven are one-way doors: slow down, write an RFC or ADR and involve the right people, for example the two-year payment provider contract, storing customer data outside the EU, the event schemas other teams consume and deleting old order data. Warning: event schemas look two-way but aren't once others depend on them.",
                "Sort first. Two-way doors go back to the teams, today; one-way doors get the slow, careful treatment.")
od_how.box(20, 20, 350, 250, None, "green")
od_how.head(195, 54, "two-way: 24", size=19)
od_how.text(195, 80, "decide in the team, this week", "t t-soft", size=15)
for i, t in enumerate(["substitution window (a flag)", "cache timeout", "picker screen layout", "log library"]):
    od_how.text(40, 120 + i * 36, "• " + t, anchor="start", size=16)
od_how.box(390, 20, 350, 250, None, "pink")
od_how.head(565, 54, "one-way: 7", size=19)
od_how.text(565, 80, "slow down: RFC or ADR, right people", "t t-soft", size=15)
for i, t in enumerate(["2-year payment contract", "customer data outside the EU", "event schemas others consume", "deleting old order data"]):
    od_how.text(410, 120 + i * 36, "• " + t, anchor="start", size=16)
od_how.note(380, 310, "careful: a schema is two-way until someone else depends on it", "red", size=18)

DOORS = dict(
    slug="one-way-two-way-doors",
    kicker="a.k.a. “the passport exit”",
    tldr="Most decisions are <b>two-way doors</b>: if you're wrong, you walk back out at low cost. Make those <b>fast, close to the work</b>, by the team, without an architecture meeting. A few are <b>one-way doors</b>: contracts, data you can't un-share or un-delete, interfaces others depend on, deadlines you can't move. Slow down only for those: an RFC or ADR, the right people, a careful look. The skill is <b>sorting</b> them, and spotting doors that <b>look two-way but lock behind you</b>.",
    chips=[("Family", "choosing well"), ("Origin", "Jeff Bezos, Amazon shareholder letter (2015): “Type 1 and Type 2 decisions”"), ("Lives in", "a door check in the decision log"), ("Pairs with", "decision rights, last responsible moment, exit plans")],
    problem_side="Larder, 9 April 2026",
    problem="""  <p class="lead">Since the decision log started, every open question has gone to <b>Ana's Thursday architecture meeting</b>. It decides about eight a week. Now there are <span class="hl-pink">31 in the queue</span>, two weeks deep, and the log library waits as long as a <b>two-year payment contract</b>. Ben's question, whether the stock cache should expire after 60 or 120 seconds, has waited nine days, though it's one line of configuration.</p>
  <ul>
    <li>Treating every decision as big makes the small ones slow and the architect a bottleneck.</li>
    <li>Treating every decision as small lets an irreversible one slip through in a chat.</li>
    <li>The team has stopped deciding things it's perfectly able to decide.</li>
  </ul>""",
    problem_figs=[od_problem],
    analogy_side="doors at the airport",
    analogy="""  <p>In an airport terminal you walk in and out of <b>shop doors</b> without thinking: if it's the wrong shop, you leave. But at the door marked <b>“no re-entry”</b> you stop, check your passport, your bag and your gate, because once you're through, there's <b>no coming back</b>. Nobody checks their passport before entering a bookshop.</p>""",
    analogy_figs=[od_analogy],
    map=[("A shop door", "A two-way door: a flag, a setting, a library inside one module"),
         ("Walking out of the wrong shop", "Reverting, at low cost"),
         ("The “no re-entry” door", "A one-way door: contracts, data, shared interfaces"),
         ("Checking your bag first", "RFC or ADR, the right people, a careful look"),
         ("Wandering freely", "Teams deciding two-way doors themselves, this week")],
    how_side="sort first, then pick the speed",
    how="""  <p>Ana and Sanne sorted the 31 in one hour: <b>24 two-way</b>, back to the teams by Friday; <b>7 one-way</b>, each with an owner and an RFC or ADR. The Thursday meeting shrank to the seven. The tricky ones were in the middle: an event schema is two-way <b>until another team consumes it</b>; then it's a contract.</p>""",
    how_figs=[od_how],
    steps=[("Ask: what does undoing cost?", "Time, money, data, trust. Hours or days → two-way. Months, lost data or a contract → one-way."),
           ("Look for hidden locks", "Other teams depending on it, customers seeing it, data leaving your hands, a long contract."),
           ("Two-way: decide fast, near the work", "The team decides, logs one line, and watches the result. Use a flag to make it even cheaper to undo."),
           ("One-way: slow down", "RFC or ADR, options analysis, the approver, legal or finance if they're affected."),
           ("Make doors two-way where you can", "Feature flags, a trial period in the contract, a versioned API, a data export."),
           ("Re-sort as things change", "A schema becomes one-way when a second team starts consuming it.")],
    vocab=[("Two-way door", "A decision that's cheap to reverse; decide fast."),
           ("One-way door", "A decision that's costly or impossible to reverse; decide carefully."),
           ("Type 1 / Type 2", "Bezos's names for one-way and two-way decisions."),
           ("Hidden lock", "Something that makes a door one-way: dependants, data, contracts."),
           ("Feature flag", "A switch that makes a change two-way."),
           ("Cost of reversal", "What it takes to undo: time, money, data, trust.")],
    code=dict(file="docs/decisions/door-check.md", note="door check, used for every new line in the decision log", plain=True, src="""
# Door check                               (2 minutes, before a decision is queued)

1. If we're wrong, what does undoing it cost?
   [ ] hours or days of work            → two-way
   [ ] weeks of work                    → probably one-way: ask Ana
   [ ] money we can't get back, a contract, a public promise   → one-way
2. Does anyone outside the team depend on it? (consumers of an event or API,
   customers who'll see it, Korenwolf, StockPilot)              yes → one-way
3. Does data leave our control, or get deleted?                 yes → one-way
4. Can we make it two-way? (flag, trial period, versioned API, export)

Two-way → the team decides, one line in the log, review the result in 2 weeks.
One-way → owner + RFC/ADR + approver; Thursday architecture meeting.

Examples (Apr 2026): D-24 substitution window → two-way (flag, Grace decided)
                     D-22 second PSP contract (24 months) → one-way (Marco)
                     order.ready_for_dispatch v1 schema → one-way since Dispatch reads it
"""),
    tools="tools: a checklist in the decision log is enough. Feature flags (Unleash, LaunchDarkly, a config table) make many doors two-way; contract trial periods and data exports make vendor doors less one-way.",
    gains=["<b>Small decisions go fast</b>: days, not weeks in a queue.",
           "<b>The architect focuses</b> on the few decisions that matter.",
           "<b>Teams own more</b>, inside their areas.",
           "<b>Big decisions get real care</b>, not a rushed slot.",
           "<b>Designs that stay reversible</b>: flags, trials, versions."],
    losses=["<b>Misjudged doors</b>: a hidden lock slips through as two-way.",
            "<b>Many small reversals</b> if teams treat two-way as “don't think”.",
            "<b>Disagreement about the sort</b> itself.",
            "<b>Making doors two-way costs</b>: flags and versions need upkeep."],
    baseline="Each line compares <b>every decision through one architecture meeting, at one speed</b> to <b>sorting decisions by reversibility: two-way to the teams, fast; one-way slowly, with care</b>.",
    ratings=[(3, 4, "The door check explains why a decision went where it did."),
             (3, 4, "Big, irreversible decisions involve the right people."),
             (2, 5, "24 of 31 decisions went back to teams the same week."),
             (2, 4, "One-way doors get spotted and slowed down."),
             (2, 5, "Flags and trials make more decisions reversible."),
             (3, 4, "One-way doors get ADRs; two-way ones a line."),
             (3, 4, "Costly-to-reverse is often costly, full stop: it gets attention."),
             (2, 4, "A two-minute check; fewer meetings."),
             (2, 5, "Teams decide two-way doors alone.")],
    pitfalls=[("Hidden locks", "“Just a schema” that three teams already consume.", "ask who depends on it before calling it two-way."),
              ("Everything is one-way", "Fear turns every decision into a committee.", "most decisions are two-way; prove otherwise."),
              ("Two-way, never reversed", "A bad two-way decision lives on because nobody checks.", "review two-way decisions after two weeks."),
              ("No way to make it two-way", "A big-bang launch with no flag.", "spend a little to add a flag, a trial or a version.")],
    use=["When decisions queue for one person or meeting.",
         "When teams wait for permission they don't need.",
         "Before contracts, data changes and shared interfaces.",
         "Designing for change: making doors two-way on purpose."],
    skip=["Emergencies: make the call, then review.",
          "When the team already sorts instinctively and nothing queues."],
    related=["<b>Decision rights (RACI/DACI)</b> (this volume)", "<b>Last responsible moment</b> (this volume)", "<b>Exit plans &amp; reversibility</b> (this volume)", "<b>Feature flags</b> (patterns, Vol. 6)"],
    quiz=[("What makes a door one-way?", "Undoing it is costly or impossible: contracts, lost or shared data, interfaces others depend on, public promises."),
          ("Who should decide two-way doors?", "The team closest to the work, quickly, with one line in the log."),
          ("When does an event schema become a one-way door?", "When other teams consume it: changing it then breaks them."),
          ("How can you turn a one-way door into a two-way one?", "Feature flags, trial periods in contracts, versioned APIs, data exports.")],
    try_it="List every decision waiting on someone in your team right now. Run the four-question door check on each. Send the two-way ones back to the people doing the work today, with a date to review the result, and see how long your queue is afterwards.",
    remember="Walk through <span class=\"hl\">shop doors</span>. Check your bag at <span class=\"hl\">no re-entry</span>.",
    sources=["Jeff Bezos, Amazon shareholder letter (2015), on Type 1 and Type 2 decisions.",
             "Neal Ford, Rebecca Parsons, Patrick Kua, <i>Building Evolutionary Architectures</i> (2017), on reversibility.",
             "Martin Fowler, “Who Needs an Architect?” (IEEE Software, 2003): architecture as the decisions that are hard to change.",
             "Pete Hodgson, “Feature Toggles (aka Feature Flags)” (martinfowler.com, 2017)."],
)

# ------------------------------------------------------------------ 08 Last Responsible Moment
lrm_problem = Doodle(760, 290, "Doodle of two timing mistakes at Larder in spring 2026. Too early: in April, people want to choose Antwerp's Belgian invoicing system now, though the facts arrive in 2027. Too late: Rotterdam's store internet line was ordered on 30 March with a six-week lead time, so it goes live in mid-May, after the store opens on 27 April.",
                     "One decision rushed a year early, one left until after its lead time ran out.")
lrm_problem.box(20, 30, 340, 170, None, "paper")
lrm_problem.head(190, 62, "too early", size=19, color="red")
lrm_problem.text(190, 98, "Antwerp invoicing, chosen", size=16)
lrm_problem.text(190, 122, "in April 2026?", size=16)
lrm_problem.note(190, 168, "the facts arrive in 2027", "pen")
lrm_problem.box(400, 30, 340, 170, None, "pink", stroke="red")
lrm_problem.head(570, 62, "too late", size=19, color="red")
lrm_problem.text(570, 98, "Rotterdam internet ordered 30 Mar", size=16)
lrm_problem.text(570, 122, "6-week lead time → mid-May", size=16)
lrm_problem.note(570, 168, "store opens 27 Apr", "red")
lrm_problem.note(380, 262, "two failures of timing, not of judgement", "red")

lrm_analogy = Doodle(760, 260, "Doodle of a kitchen renovation timeline. Too early to choose tiles at the start, before you know the room. The plumbing gets done. The last responsible moment to order tiles is six weeks before the tiler is booked, because tiles take six weeks to arrive. After that, the tiler waits.",
                     "Renovating a kitchen: choose the tiles once you know the room, but before their six-week delivery runs out.")
lrm_analogy.line("M30 130 H730")
for x, t, c in [(60, "start", "pen"), (260, "plumbing done", "pen"), (690, "tiler booked", "pen")]:
    lrm_analogy.line(f"M{x} 120 V140")
    lrm_analogy.note(x, 168, t, c)
lrm_analogy.circle(460, 130, 12, fill="green")
lrm_analogy.head(460, 100, "order tiles", size=17, color="green")
lrm_analogy.arrow(472, 200, 680, 200, label="6 weeks delivery", lx=576, ly=190)
lrm_analogy.note(160, 60, "too early: no room yet", "red", size=18)
lrm_analogy.note(620, 60, "too late: tiler waits", "red", size=18)
lrm_analogy.note(300, 230, "← keep options open", "pen", size=18)

lrm_how = Doodle(760, 350, "Larder's decision calendar for Antwerp, made on 20 April 2026, assuming a September 2027 opening. Each decision's lead time is drawn back from the opening to give its last responsible moment: store lease, nine months, decide by December 2026; Belgian invoices and VAT, five months, by March 2027; French in the apps, four months, by May 2027; Bancontact, six weeks, by July 2027. Until then, keep options open: make all app text translatable and choose billing that supports Belgian VAT.",
                 "Work back from the date: lead time gives each decision its last responsible moment. Until then, keep options open.")
x0, per = 300, 440 / 17
lrm_how.line(f"M{x0} 40 V280", dash=True, thin=True)
lrm_how.note(x0, 30, "today · Apr 2026", "pen", size=16)
lrm_how.line("M740 40 V280", thin=True)
lrm_how.note(744, 30, "Antwerp · Sep 2027", "green", anchor="end", size=16)
for i, (name, lead, m, by) in enumerate([("store lease", "9 months", 8, "Dec 2026"), ("Belgian invoices, VAT", "5 months", 11, "Mar 2027"),
                                         ("French in the apps", "4 months", 13, "May 2027"), ("Bancontact", "6 weeks", 15, "Jul 2027")]):
    y = 70 + i * 54
    xm = x0 + m * per
    lrm_how.text(20, y + 6, name, "t-head", anchor="start", size=15)
    lrm_how.text(20, y + 28, f"lead {lead} · by {by}", anchor="start", size=14)
    lrm_how.box(xm, y - 8, 740 - xm, 24, None, "y", rx=4)
    lrm_how.circle(xm, y + 4, 9, fill="green")
lrm_how.text(380, 310, "until then: all app text translatable · billing must support BE VAT", size=15)
lrm_how.note(380, 338, "the dot is the last responsible moment", "green", size=18)

LRM = dict(
    slug="last-responsible-moment",
    kicker="a.k.a. “order the tiles in time, not on day one”",
    tldr="Decide <b>too early</b> and you decide with the least information you'll ever have. Decide <b>too late</b> and the lead time has run out. The <b>last responsible moment</b> is in between: the point where <b>waiting starts to cost more than it saves</b>, usually the target date minus the decision's <b>lead time</b>. Work out that date for each big decision, put it in a <b>decision calendar</b>, and until then do the cheap things that <b>keep options open</b>.",
    chips=[("Family", "choosing well"), ("Origin", "Lean construction; Mary and Tom Poppendieck, <i>Lean Software Development</i> (2003)"), ("Lives in", "a decision calendar, linked from the decision log"), ("Pairs with", "one-way vs two-way doors, decision log, exit plans")],
    problem_side="Larder, 20 April 2026",
    problem="""  <p class="lead">A week before Rotterdam opens, Ana sees both failure modes at once. <b>Too late:</b> Rotterdam's store internet line was ordered on 30 March, with a <b>six-week lead time</b>; it goes live in mid-May, so the store opens on a 4G router (the offline-first picker app, ADR 0004, earns its keep). <b>Too early:</b> in the same week Lena and Marco want to choose a <b>Belgian invoicing system for Antwerp</b>, a city planned for 2027, <span class="hl-pink">before anyone knows</span> what Larder for Business will need in Belgium.</p>
  <ul>
    <li>Early decisions lock in guesses that later facts would have corrected.</li>
    <li>Late decisions run into lead times: contracts, hardware, hiring, translations.</li>
    <li>“Decide later” without a date is just “forget”.</li>
  </ul>""",
    problem_figs=[lrm_problem],
    analogy_side="renovating a kitchen",
    analogy="""  <p>You don't choose the kitchen tiles on day one: you don't know the room yet. But the tiles take <b>six weeks to arrive</b>, and the tiler is booked. So the moment to choose is <b>six weeks before the tiler</b>, not earlier and not later. Until then you keep options open: you measure the walls, you don't glue anything.</p>""",
    analogy_figs=[lrm_analogy],
    map=[("The tiler's booking", "The target date: Antwerp opens (planned Sep 2027)"),
         ("Six weeks' delivery", "Lead time: contracts, translation, a store lease"),
         ("Six weeks before the tiler", "The last responsible moment for each decision"),
         ("Measuring, not gluing", "Keeping options open: translatable text, billing with Belgian VAT"),
         ("The tiler standing idle", "A launch waiting on a decision made too late")],
    how_side="work back from the date",
    how="""  <p>For each big decision, ask two questions: <b>when do we need the answer in place</b>, and <b>how long does it take</b> once decided? The difference is the last responsible moment. Put it in the decision log as a due date. And list the cheap moves that keep options open until then.</p>""",
    how_figs=[lrm_how],
    steps=[("List the decisions a date depends on", "For Antwerp: store, invoicing and VAT, language, payment methods, couriers."),
           ("Find each lead time", "Ask the people who know: legal, finance, vendors, operations. Add a buffer."),
           ("Work back from the date", "Target date − lead time − buffer = last responsible moment. Put it in the log."),
           ("Keep options open meanwhile", "Cheap moves that don't commit: translatable strings, a billing vendor that supports Belgian VAT."),
           ("Learn while you wait", "What would make the decision easier? Collect it before the date."),
           ("Decide on the date", "Waiting past it is the last irresponsible moment.")],
    vocab=[("Last responsible moment", "The latest point where deciding still leaves enough time to act."),
           ("Lead time", "How long it takes from deciding to having it in place."),
           ("Decision calendar", "Big decisions with their last responsible moments."),
           ("Option value", "The worth of keeping a choice open while facts arrive."),
           ("Premature commitment", "Deciding before you need to, on guesses."),
           ("Last irresponsible moment", "Waiting until the lead time no longer fits.")],
    code=dict(file="docs/antwerp/decision-calendar.md", note="Larder's decision calendar for Antwerp, 20 April 2026", plain=True, src="""
# Antwerp decision calendar          planning date: opening Sep 2027 (not committed)

| Decision                   | Lead time  | Last responsible moment | Owner | Meanwhile (keep options open)           |
|----------------------------|------------|-------------------------|-------|-----------------------------------------|
| Store location and lease   | 9 months   | Dec 2026                | Femke | Joost shortlists areas from Rotterdam data |
| Belgian invoices, VAT      | 5 months   | Mar 2027                | Marco | Billing vendor must support BE VAT (Jun)|
| French and Dutch in apps   | 4 months   | May 2027                | Grace | All app text translatable from now on   |
| Bancontact payments        | 6 weeks    | Jul 2027                | Cho   | Current provider supports it: confirm   |
| Courier contracts (BE law) | 3 months   | May 2027                | Joost | Lena checks Belgian rules by Dec 2026   |

Every row is a line in the decision log with its due date.
Lesson from Rotterdam: the internet line (6 weeks) was ordered 4 weeks out.
"""),
    tools="tools: due dates in the decision log are enough; a timeline on the project plan helps. Related techniques: real options thinking, Lean's set-based design, critical path planning for the lead times.",
    gains=["<b>Better-informed decisions</b>: made with more facts.",
           "<b>No lead-time surprises</b>: dates are worked back, not guessed.",
           "<b>Options stay open</b> cheaply, on purpose.",
           "<b>Less rework</b> from early commitments that turned out wrong.",
           "<b>“Later” has a date</b>, so it doesn't mean “never”."],
    losses=["<b>Needs lead-time knowledge</b> people may not have.",
            "<b>Feels uncomfortable</b>: open questions look like indecision.",
            "<b>Easy to slide</b> into the last irresponsible moment.",
            "<b>Keeping options open costs a little</b> (translatable strings, flexible vendors)."],
    baseline="Each line compares <b>deciding whenever it comes up, early or late</b> to <b>a decision calendar with each big decision's last responsible moment, keeping options open until then</b>.",
    ratings=[(3, 4, "The calendar shows what's decided when, and why then."),
             (2, 4, "Stakeholders see that “later” is planned, not avoided."),
             (3, 3, "Some decisions get faster, some deliberately slower."),
             (2, 5, "Lead times are found before they bite."),
             (2, 5, "Options stay open until facts arrive."),
             (3, 4, "Due dates and reasons sit in the decision log."),
             (2, 4, "Avoids paying for early guesses that turn out wrong."),
             (3, 3, "Finding lead times takes some asking around."),
             (3, 3, "Owners know their dates; not about autonomy.")],
    pitfalls=[("No date", "“We'll decide later” and nobody does.", "every deferred decision gets its last responsible moment in the log."),
              ("Unknown lead times", "The internet line takes six weeks; nobody asked.", "ask suppliers and operations for lead times, add a buffer."),
              ("Deferring two-way doors", "A reversible choice waits months for “more information”.", "two-way doors: decide now, change later."),
              ("Options that cost too much", "Supporting three billing vendors “just in case”.", "keep options open cheaply, or decide.")],
    use=["Dated launches with long-lead items: contracts, hardware, hiring, legal.",
         "One-way doors where facts are still arriving.",
         "When people push to decide everything up front.",
         "Planning new markets or cities."],
    skip=["Two-way doors: just decide.",
          "When the information won't improve with time."],
    related=["<b>One-way vs two-way doors</b> (this volume)", "<b>Decision log</b> (this volume)", "<b>Constraints vs assumptions</b> (Vol. 1)", "<b>Migration planning</b> (Vol. 6)"],
    quiz=[("How do you find a decision's last responsible moment?", "Target date minus its lead time (and a buffer)."),
          ("What's wrong with deciding as early as possible?", "You decide with the least information, and lock in guesses."),
          ("What do you do until the last responsible moment?", "Keep options open with cheap moves and learn what would make the decision easier."),
          ("Does this apply to two-way doors?", "Rarely: reversible decisions can be made now and changed later.")],
    try_it="Pick your next big date. List five decisions it depends on, and ask the right person for each one's lead time. Write a decision calendar with the last responsible moment for each and one cheap way to keep options open until then. Add the dates to your decision log.",
    remember="Not on day one, not after the <span class=\"hl\">lead time</span>. Measure the walls; order the tiles <span class=\"hl\">in time</span>.",
    sources=["Mary and Tom Poppendieck, <i>Lean Software Development</i> (2003), “Decide as late as possible”.",
             "Jeff Atwood, “The Last Responsible Moment” (Coding Horror, 2006).",
             "Glenn Ballard, “The Last Planner System” (Lean Construction Institute, 2000).",
             "Neal Ford et al., <i>Building Evolutionary Architectures</i> (2017)."],
)

NOTES = [OPTIONS, SLIDERS, DOORS, LRM]
