# Series 2 · The Solution Architect's Notebook · Vol. 6 · Architecture in delivery.
# Running case study: Larder (facts in docs/larder-casebook.md).

# ------------------------------------------------------------------ 01 Just-Enough Up-Front Design
jd_problem = Doodle(760, 280, "Doodle of April 2028. The utility tree says checkout must handle 60,000 orders a day, which means giving Ordering its own database. Ben's team wants to start coding on Monday; Eli wants a three-month design phase first. One side risks a costly wrong turn, the other risks designing for months what code would teach in weeks.",
                    "Ben: “start Monday.” Eli: “three months of design first.” Both are expensive in different ways.")
jd_problem.box(20, 40, 320, 90, "Ben", "y", sub="“start coding Monday”")
jd_problem.box(400, 40, 340, 90, "Eli", "blue", sub="“three months of design”")
jd_problem.note(380, 200, "too little or too much, both cost", "red", size=20)

jd_analogy = Doodle(760, 250, "Doodle of planning a long hike: you decide in advance the things you can't change on the trail, the route's start and end, the hut bookings, the water points. You don't plan every step; you choose those on the path.",
                     "A long hike: fix what you can't change on the trail (route, huts, water); choose the steps as you walk.")
jd_analogy.icon("map", 30, 60, 1.3)
for i, (t, s, f) in enumerate([("route", "decide now", "pink"), ("huts", "book now", "pink"), ("each step", "on the trail", "green")]):
    jd_analogy.box(150 + i * 200, 50, 186, 90, t, f, sub=s, size=16)
jd_analogy.note(450, 205, "plan what's hard to change", "pen")

jd_how = Doodle(760, 400, "Ana's two-week design for the Ordering split, 10 April 2028. Decided up front, because they are hard to change: Ordering owns its own database; other modules get order data only from events and the Ordering API, never from tables; money amounts in integer cents; order ids stay the same. Left to learn while building: the exact schema, the caching, the number of service instances, the batch sizes. A two-page design note, one ADR, a spike on the hardest part, data copying, then build.",
                 "Decide the one-way doors in two weeks; leave the two-way doors to the code.")
jd_how.box(14, 14, 360, 230, None, "pink")
jd_how.head(194, 46, "decide now", size=17)
for i, t in enumerate(["own database", "events + API only", "ids unchanged", "money in cents"]):
    jd_how.text(194, 90 + i * 38, t, size=15)
jd_how.box(386, 14, 360, 230, None, "green")
jd_how.head(566, 46, "learn while building", size=17)
for i, t in enumerate(["exact schema", "caching", "instances", "batch sizes"]):
    jd_how.text(566, 90 + i * 38, t, size=15)
jd_how.box(14, 266, 732, 56, "2 weeks · 2-page note · ADR 0027 · a spike on data copying", "blue", size=15)
jd_how.note(380, 360, "then build, in small steps", "pen", size=17)

JUSTENOUGH = dict(
    slug="just-enough-design",
    kicker="a.k.a. “plan the huts, not the steps”",
    tldr="<b>Just-enough up-front design</b> means deciding before building only the things that are <b>expensive to change later</b> (one-way doors: data ownership, contracts, identifiers, technology commitments), and leaving the rest to be learned <b>while building</b>. Timebox it (often one to two weeks), write it short (a design note and an ADR), and spike the riskiest unknown. Too little design costs wrong turns; too much costs months of guessing what code would teach.",
    chips=[("Family", "architecture in delivery"), ("Origin", "George Fairbanks, <i>Just Enough Software Architecture</i> (2010); agile architecture practice"), ("Lives in", "a short design note and an ADR per big change"), ("Pairs with", "one-way vs two-way doors, spike vs prototype vs PoC, walking skeleton")],
    problem_side="Larder, 10 April 2028",
    problem="""  <p class="lead">The utility tree put <b>checkout at 60,000 orders a day</b> first, and that means giving <b>Ordering its own database</b>. Ben's team wants to <b>start coding on Monday</b>; Eli wants a <b>three-month design phase</b>. <span class="hl-pink">One side risks a costly wrong turn; the other risks designing for months what code would teach in weeks.</span></p>
  <ul>
    <li>Some decisions are cheap to change later; some aren't.</li>
    <li>Long design phases guess at things building would show.</li>
    <li>No design at all leaves the expensive decisions to chance.</li>
  </ul>""",
    problem_figs=[jd_problem],
    analogy_side="planning a long hike",
    analogy="""  <p>Before a long hike you decide what you <b>can't change on the trail</b>: the <b>route</b>, the <b>hut bookings</b>, the <b>water points</b>. You don't plan every step; you choose those <b>on the path</b>, looking at the ground in front of you.</p>""",
    analogy_figs=[jd_analogy],
    map=[("The route", "Ordering owns its own database"),
         ("Hut bookings", "Other modules use events and the API, never tables"),
         ("Water points", "Order ids unchanged; money in cents"),
         ("Each step", "Schema details, caching, instance counts"),
         ("Two weeks of planning", "A two-page note and ADR 0027")],
    how_side="decide the one-way doors, timeboxed",
    how="""  <p>Ana gave the design <b>two weeks</b>. Decided up front, because they're hard to undo: <b>Ordering owns its database</b>; other modules get order data <b>only from events and the Ordering API</b>; <b>order ids</b> stay the same; money in <b>integer cents</b>. Left to learn while building: the exact schema, caching, instance counts, batch sizes. Output: a <b>two-page design note</b>, <b>ADR 0027</b>, and a <b>spike</b> on the riskiest part, copying live data. Ben's team started in week three.</p>""",
    how_figs=[jd_how],
    steps=[("List the decisions", "Everything the design needs to settle."),
           ("Sort into one-way and two-way doors", "Expensive to change later, or cheap."),
           ("Timebox the design", "One to two weeks for most changes."),
           ("Decide the one-way doors", "In an ADR, with options."),
           ("Spike the riskiest unknown", "Code to answer one question."),
           ("Leave the rest to building", "And record decisions as they're made.")],
    vocab=[("Up-front design", "Design done before building starts."),
           ("Just enough", "Only what's costly to change later."),
           ("One-way door", "A decision that's hard or expensive to reverse."),
           ("Spike", "Short, throwaway code to answer one question."),
           ("Timebox", "A fixed amount of time for an activity."),
           ("Big design up front", "Designing everything before building (the anti-pattern).")],
    code=dict(file="docs/design/ordering-split.md", note="the two-page design note, April 2028", plain=True, src="""
# Ordering gets its own database · design note · Ana with Ben, Eli · 10–21 Apr 2028

Why        utility tree (H, H): checkout at 5× with 60k orders/day; Core DB shared by 7 modules
Decided (one-way doors, ADR 0027)
  1  Ordering owns its database; nobody else reads its tables
  2  Others use order events (published language, ADR 0023) or the Ordering API
  3  Order ids unchanged; money as integer cents
  4  Move with expand/contract + change data capture; switch per city
Left to building (two-way doors)
  schema details · caching · instance counts · batch sizes · index choices
Spike      copy 18 months of orders with CDC, measure lag at Friday peak (Eli, 1 week)
Not in scope   splitting Payments or Fulfilment (later, same pattern)
"""),
    tools="tools: a short design-note template, ADRs, the one-way/two-way door test, a spike branch.",
    gains=["<b>The expensive decisions</b> made deliberately.",
           "<b>Weeks, not months</b>, before building.",
           "<b>Learning from code</b> for the rest.",
           "<b>A short note</b> people actually read.",
           "<b>Spikes reduce</b> the biggest unknown."],
    losses=["<b>Some rework</b> on two-way doors.",
            "<b>Judging</b> one-way vs two-way takes experience.",
            "<b>Pressure</b> to extend the timebox.",
            "<b>Not every risk</b> shows in a spike."],
    baseline="Each line compares <b>either no design or a long design phase</b> to <b>a timeboxed design of the one-way doors, a spike, then building</b>.",
    ratings=[(2, 4, "Two pages, four decisions."),
             (2, 4, "Ben and Eli agreed the split."),
             (2, 5, "Two weeks instead of three months."),
             (2, 4, "The riskiest part spiked first."),
             (2, 5, "Two-way doors stay open."),
             (2, 4, "ADR 0027 records the one-way doors."),
             (3, 3, "Neutral."),
             (2, 4, "Light on paperwork."),
             (2, 4, "Ben's team decides the rest.")],
    pitfalls=[("Designing everything", "Schema in a 40-page document.", "only the one-way doors."),
              ("Designing nothing", "Data ownership decided by accident.", "two weeks on what's hard to change."),
              ("No timebox", "Design drifts into month three.", "fix the time, then decide."),
              ("No spike", "The risky part assumed.", "code to answer it.")],
    use=["Big changes: new services, data moves, new platforms.",
         "When teams disagree on how much design is needed.",
         "Before committing to a vendor or technology.",
         "When a mistake would be costly to undo."],
    skip=["Small, reversible changes inside one module."],
    related=["<b>One-way vs two-way doors</b> (vol. 2)", "<b>Spike vs prototype vs PoC</b> (vol. 1)", "<b>Evolutionary architecture</b> (this volume)", "<b>Migration planning</b> (this volume)"],
    quiz=[("What does just-enough design decide up front?", "Only what's expensive to change later: the one-way doors."),
          ("How long did Larder's design take?", "Two weeks, timeboxed."),
          ("What was left to building?", "Schema details, caching, instance counts and batch sizes."),
          ("What did the spike test?", "Copying live orders with change data capture, and the lag at peak.")],
    try_it="Take your next big change. List every decision it needs, mark each one-way or two-way, and give yourself one week to decide only the one-way ones, with one spike for the biggest unknown.",
    remember="Book the <span class=\"hl\">huts</span>; choose the <span class=\"hl\">steps</span> on the trail.",
    sources=["George Fairbanks, <i>Just Enough Software Architecture</i> (2010).",
             "Simon Brown, <i>Software Architecture for Developers</i> (2018), “just enough up front design”.",
             "Jeff Bezos, Amazon shareholder letter (2015), one-way and two-way doors.",
             "Mary and Tom Poppendieck, <i>Lean Software Development</i> (2003), the last responsible moment."],
)

# ------------------------------------------------------------------ 02 Evolutionary Architecture
ea_problem = Doodle(760, 280, "Doodle of May 2028. Larder's architecture has changed every year: a modular monolith, then Dispatch, then events, then a new warehouse system, and now Ordering's database. Each change risked breaking qualities nobody was watching. Femke asks: will we have to rebuild everything at 60,000 orders a day?",
                    "Every year a big change, each risking qualities nobody watched. Femke: “will we have to rebuild everything?”")
for i, (y, t) in enumerate([("2025", "monolith"), ("2026", "Dispatch out"), ("2027", "WMS B"), ("2028", "Ordering DB")]):
    ea_problem.box(14 + i * 184, 40, 174, 80, y, "paper", sub=t, size=17)
ea_problem.note(380, 190, "“will we have to rebuild everything?”", "red", size=19)

ea_analogy = Doodle(760, 250, "Doodle of an old city: streets added, buildings replaced, a tram line threaded through, over centuries, without ever being demolished. What holds it together are a few rules everyone keeps: building lines, heights, the canals stay open.",
                     "An old city changes for centuries without being demolished; a few kept rules hold it together.")
ea_analogy.icon("castle", 30, 60, 1.2)
for i, (t, f) in enumerate([("building lines", "y"), ("heights", "blue"), ("canals open", "green")]):
    ea_analogy.box(170 + i * 190, 60, 176, 70, t, f, size=16)
ea_analogy.note(450, 200, "change everything except the rules", "pen")

ea_how = Doodle(760, 400, "How Larder evolves its architecture, written down on 22 May 2028. Small steps, each released on its own and reversible. Fitness functions that guard the qualities that matter, run in CI and in production: module boundaries, checkout p95 under 800 milliseconds at load, cost per thousand orders, data classes declared, no direct reads of another module's tables. Room to turn: decisions recorded with their triggers. Answer to Femke: no rebuild; the Ordering split is the next step of the same evolution, guarded by nine fitness functions.",
                 "Small reversible steps, fitness functions guarding what matters, decisions with triggers. No rebuild needed.")
ea_how.box(14, 14, 732, 50, "small steps · each released alone · reversible", "y", size=15)
ea_how.head(380, 98, "fitness functions (9), in CI and production", size=16)
for i, t in enumerate(["module boundaries", "checkout p95 at load", "cost / 1,000 orders", "data classes", "no foreign tables"]):
    r, c = divmod(i, 3)
    ea_how.box(14 + c * 248, 114 + r * 70, 236, 58, t, "green", size=14)
ea_how.box(14, 262, 732, 50, "decisions recorded with triggers: room to turn", "blue", size=15)
ea_how.note(380, 352, "Femke: no rebuild; the next step, guarded", "pen", size=16)

EVOLUTIONARY = dict(
    slug="evolutionary-architecture",
    kicker="a.k.a. “the old city”",
    tldr="An <b>evolutionary architecture</b> is designed to change: it moves in <b>small, reversible steps</b>, it protects the qualities that matter with <b>fitness functions</b> (automated checks in CI and production), and it keeps <b>room to turn</b> by recording decisions with the conditions that would change them. The aim isn't to predict the future but to make the next change safe, so the system never needs a big rewrite.",
    chips=[("Family", "architecture in delivery"), ("Origin", "Neal Ford, Rebecca Parsons and Patrick Kua, <i>Building Evolutionary Architectures</i> (2017)"), ("Lives in", "the fitness-function suite, small releases and ADRs with triggers"), ("Pairs with", "fitness functions, strangler fig migration, guardrails not gates")],
    problem_side="Larder, 22 May 2028",
    problem="""  <p class="lead">Larder's architecture has changed <b>every year</b>: a modular monolith, then Dispatch as a service, then events, then a new warehouse system, and now Ordering's own database. Each change risked breaking <b>qualities nobody was watching</b>. Femke asks: <span class="hl-pink">will we have to rebuild everything at 60,000 orders a day?</span></p>
  <ul>
    <li>Architectures that can't change get rewritten, expensively.</li>
    <li>Changes break qualities that aren't checked.</li>
    <li>Big-bang changes are hard to undo.</li>
  </ul>""",
    problem_figs=[ea_problem],
    analogy_side="the old city",
    analogy="""  <p>An <b>old city</b> changes for centuries without being demolished: streets are added, buildings replaced, a tram line threaded through. What holds it together are a few rules everyone keeps: <b>building lines</b>, <b>heights</b>, the <b>canals stay open</b>. Change everything else, one building at a time.</p>""",
    analogy_figs=[ea_analogy],
    map=[("One building at a time", "Small, reversible releases"),
         ("Building lines and heights", "Fitness functions: boundaries, p95, cost"),
         ("The canals stay open", "No direct reads of another module's tables"),
         ("A tram line threaded through", "Ordering's own database, city by city"),
         ("Never demolished", "No big rewrite")],
    how_side="small steps, fitness functions, room to turn",
    how="""  <p>Ana wrote down how Larder evolves: <b>small steps</b>, each released on its own and reversible; <b>nine fitness functions</b> in CI and production guarding module boundaries, checkout p95 at load, cost per 1,000 orders, declared data classes and <b>no reads of another module's tables</b>; and decisions recorded <b>with triggers</b>, so there's room to turn. Her answer to Femke: <b>no rebuild</b>. The Ordering split is the next step of the same evolution, city by city, guarded by the same checks.</p>""",
    how_figs=[ea_how],
    steps=[("Name the qualities that matter", "From the utility tree."),
           ("Guard each with a fitness function", "Automated, in CI or production."),
           ("Change in small steps", "Each releasable and reversible."),
           ("Record decisions with triggers", "So you know when to turn."),
           ("Review the fitness functions", "Add, tighten or retire as priorities change."),
           ("Avoid big bangs", "Strangler and expand/contract instead.")],
    vocab=[("Evolutionary architecture", "Architecture that supports guided, incremental change."),
           ("Fitness function", "An automated check that a quality holds."),
           ("Incremental change", "Changing in small, safe steps."),
           ("Reversibility", "How easily a change can be undone."),
           ("Architectural quantum", "The smallest part that can be deployed on its own."),
           ("Big bang", "Changing everything at once.")],
    code=dict(file="docs/architecture/fitness-functions.md", note="the fitness functions, May 2028", plain=True, src="""
# Fitness functions · reviewed quarterly · owner: Ana (each check has a team owner)

FF-01  module boundaries (import-linter)                         CI        since 2025
FF-03  checkout p95 < 800 ms at 5× (load profile)                weekly    since 2027
FF-05  no new direct HTTP between modules outside the catalogue  CI        since 2027
FF-07  WMS B client only inside the Stock adapter                CI        since 2027
FF-08  event schema changes compatible (registry)                CI        since 2027
FF-09  new tables and topics declare a data class                CI        since 2027
FF-10  cloud cost per 1,000 orders ≤ €70 (alert)                 daily     since 2028
FF-11  no reads of another module's tables (DB grants + scan)    CI + prod since May 2028
FF-12  bundle ≤ 300 KB, home ≤ 2.5 s (performance budgets)       CI        since 2027
"""),
    tools="tools: import-linter or ArchUnit, load tests with thresholds, cost alerts, schema registry checks, database grants; ADRs with triggers.",
    gains=["<b>No rewrites</b>: each change is a step.",
           "<b>Qualities guarded</b> automatically.",
           "<b>Reversible releases</b>.",
           "<b>Confidence</b> for big changes.",
           "<b>Decisions that can turn</b> on evidence."],
    losses=["<b>Fitness functions</b> to build and keep.",
            "<b>Small steps</b> can feel slow.",
            "<b>Temporary states</b> to manage.",
            "<b>Discipline</b> across teams."],
    baseline="Each line compares <b>big changes with qualities checked by hand</b> to <b>small reversible steps guarded by fitness functions, with decisions that can turn</b>.",
    ratings=[(2, 4, "Nine checks name what must hold."),
             (2, 4, "Femke hears “no rebuild” with reasons."),
             (2, 4, "Teams change without asking, inside the checks."),
             (1, 5, "Breakages caught by checks, not customers."),
             (1, 5, "Built to change."),
             (2, 4, "Each check linked to an ADR."),
             (3, 4, "A cost check among the nine."),
             (3, 3, "Checks need upkeep."),
             (2, 5, "Teams move freely inside the guardrails.")],
    pitfalls=[("Predicting the future", "Designing for every possible need.", "make the next change safe."),
              ("Unguarded qualities", "Boundaries erode quietly.", "a fitness function per quality."),
              ("Big bangs", "Everything switched in one night.", "small, reversible steps."),
              ("Too many checks", "Fifty flaky checks.", "a few that matter, kept green.")],
    use=["Systems that will keep growing for years.",
         "Before and during big migrations.",
         "When qualities have broken unnoticed.",
         "When leaders fear a rewrite."],
    skip=["Short-lived systems and prototypes."],
    related=["<b>Fitness functions</b> (vol. 1)", "<b>Strangler fig migration</b> (vol. 4)", "<b>Guardrails not gates</b> (this volume)", "<b>Just-enough up-front design</b> (this volume)"],
    quiz=[("What are the three parts of evolutionary architecture here?", "Small reversible steps, fitness functions, and decisions with triggers."),
          ("What is a fitness function?", "An automated check that an important quality still holds."),
          ("What did FF-11 add?", "No reads of another module's tables, checked in CI and production."),
          ("What was the answer to Femke?", "No rebuild: the Ordering split is the next guarded step.")],
    try_it="Pick the three qualities your system can't lose. For each, write an automated check you could run in CI or production, and add one this sprint.",
    remember="Change the city one <span class=\"hl\">building</span> at a time; keep the <span class=\"hl\">canals</span> open.",
    sources=["Neal Ford, Rebecca Parsons, Patrick Kua and Pramod Sadalage, <i>Building Evolutionary Architectures</i>, 2nd ed. (2022).",
             "Martin Fowler, “Sacrificial Architecture” (2014).",
             "Stewart Brand, <i>How Buildings Learn</i> (1994).",
             "Mark Richards and Neal Ford, <i>Fundamentals of Software Architecture</i> (2020)."],
)

# ------------------------------------------------------------------ 03 The Architecture Backlog
ab_problem = Doodle(760, 280, "Doodle of August 2028. Architecture work is everywhere: 23 open items in the debt register, follow-ups from six ADRs, two failing fitness functions, the remaining Ordering split steps, and Grace's and the new business product owner's feature backlogs. Every planning meeting, architecture work loses to features, item by item.",
                    "Debt, ADR follow-ups, failing checks, the split: scattered, and losing to features item by item.")
for i, (t, f) in enumerate([("debt register", "paper"), ("ADR follow-ups", "paper"), ("failing checks", "pink"), ("split steps", "y")]):
    ab_problem.box(14 + i * 184, 40, 174, 70, t, f, size=15)
ab_problem.note(380, 190, "everywhere, so nowhere", "red", size=20)

ab_analogy = Doodle(760, 250, "Doodle of a household's home maintenance list next to the holiday plans: roof, boiler, windows, ordered by risk, with a fixed share of the budget each year. Without the list, every year's money goes to holidays until the roof leaks.",
                     "A home maintenance list with a fixed share of the budget, or every year's money goes to holidays until the roof leaks.")
ab_analogy.icon("bricks", 30, 60, 1.2)
ab_analogy.box(150, 50, 280, 100, "maintenance list", "y", sub="roof, boiler, windows")
ab_analogy.box(460, 50, 280, 100, "fixed share", "green", sub="every year's budget")
ab_analogy.note(450, 210, "or the roof leaks", "pen")

ab_how = Doodle(760, 400, "Larder's architecture backlog from 21 August 2028: one ordered list in the same tool as the feature backlogs. Sources: the debt register, ADR follow-ups, failing fitness functions, migration steps, incident actions. Each item says the quality it protects and the cost of waiting. Ordered quarterly with the product owners, using the same cost-of-delay language. Capacity: 20 percent of each team, agreed with Priya. Top three for Q4: finish Ordering's switch in the last two cities, fix FF-03 at Friday peak, retire the old order export.",
                 "One ordered list, each item with the quality it protects and the cost of waiting; 20 % of capacity, planned with product.")
for i, t in enumerate(["debt", "ADRs", "checks", "migrations", "incidents"]):
    ab_how.box(14 + i * 148, 14, 138, 60, t, "paper", size=13)
    ab_how.arrow(83 + i * 148, 78, 380, 104)
ab_how.box(14, 108, 732, 60, "one ordered list · quality protected · cost of waiting", "y", size=15)
ab_how.box(14, 188, 360, 70, "20 % of each team", "green", sub="agreed with Priya", size=16)
ab_how.box(386, 188, 360, 70, "ordered quarterly", "blue", sub="with the product owners", size=16)
ab_how.note(380, 300, "Q4: Ordering's last two cities · FF-03 at peak · old export", "pen", size=15)

BACKLOG = dict(
    slug="architecture-backlog",
    kicker="a.k.a. “the home maintenance list”",
    tldr="Architecture work (debt, ADR follow-ups, failing fitness functions, migration steps, incident actions) gets lost when it's scattered and loses to features one item at a time. Keep <b>one ordered architecture backlog</b> in the same tool as the feature backlogs; give each item the <b>quality it protects</b> and the <b>cost of waiting</b>; order it <b>with the product owners</b> in the same language; and agree a <b>fixed share of capacity</b>.",
    chips=[("Family", "architecture in delivery"), ("Origin", "agile architecture practice; technical debt management"), ("Lives in", "the team planning tool, next to the feature backlogs"), ("Pairs with", "technical debt register, cost of delay, tech-debt talks with the product owner")],
    problem_side="Larder, 21 August 2028",
    problem="""  <p class="lead">Architecture work is <b>everywhere</b>: 23 open items in the debt register, follow-ups from six ADRs, two failing fitness functions, the remaining Ordering split steps, incident actions. At every planning meeting it competes with features <b>item by item</b>, and <span class="hl-pink">loses each time</span>.</p>
  <ul>
    <li>Scattered work can't be compared or ordered.</li>
    <li>Architecture items rarely say why they matter in product terms.</li>
    <li>Without agreed capacity, urgent features always win.</li>
  </ul>""",
    problem_figs=[ab_problem],
    analogy_side="the home maintenance list",
    analogy="""  <p>A household keeps a <b>maintenance list</b> (roof, boiler, windows), ordered by risk, with a <b>fixed share of the budget</b> each year. Without the list, every year's money goes on holidays, until the roof leaks in the middle of winter.</p>""",
    analogy_figs=[ab_analogy],
    map=[("The maintenance list", "One ordered architecture backlog"),
         ("Roof, boiler, windows", "Debt, failing checks, migration steps"),
         ("Ordered by risk", "Quality protected and cost of waiting"),
         ("A fixed share of the budget", "20 % of each team's capacity"),
         ("The holidays", "Feature backlogs")],
    how_side="one list, product language, fixed capacity",
    how="""  <p>Ana merged every source into <b>one ordered list</b>, in the same tool as the feature backlogs. Each item names the <b>quality it protects</b> and the <b>cost of waiting</b> (in money, risk or hours), the same cost-of-delay language Grace uses. It's ordered <b>quarterly with the product owners</b>, inside <b>20 % of each team's capacity</b> agreed with Priya. Top three for Q4: Ordering's switch in the last two cities, FF-03 failing at Friday peak, and retiring the old order export.</p>""",
    how_figs=[ab_how],
    steps=[("Gather every source", "Debt register, ADRs, failing checks, migrations, incidents."),
           ("Write each item in product terms", "Quality protected, cost of waiting."),
           ("Keep it in the same tool", "Next to the feature backlogs."),
           ("Agree a capacity share", "With product leadership."),
           ("Order it with the product owners", "Quarterly, in cost-of-delay terms."),
           ("Report what it bought", "Incidents avoided, costs cut, checks green.")],
    vocab=[("Architecture backlog", "An ordered list of architecture work."),
           ("Technical debt", "Shortcuts that make future change harder."),
           ("Cost of waiting", "What delay costs: money, risk, time."),
           ("Capacity allocation", "A fixed share of team time for a kind of work."),
           ("Enabler", "Work that enables future features (SAFe term)."),
           ("Follow-up", "Work an ADR committed to after the decision.")],
    code=dict(file="planning/architecture-backlog-2028-q4.md", note="the top of the backlog, Q4 2028", plain=True, src="""
# Architecture backlog · Q4 2028 · 20 % of each team · ordered with Grace and Jonas, 21 Aug

| # | Item                                        | Protects                  | Cost of waiting                    | Team   |
|---|---------------------------------------------|---------------------------|------------------------------------|--------|
| 1 | Ordering DB switch: Ghent, Haarlem          | checkout at 60k/day       | Core DB at 70 % on Fridays         | Ben    |
| 2 | FF-03 failing at Friday peak (p95 860 ms)    | ASR 3                     | slow checkouts, ≈ 1 % conversion   | Ben    |
| 3 | Retire the old order export (TD-21)          | data ownership (ADR 0024) | 2 teams read Core tables nightly   | Eli    |
| 4 | Upgrade Postgres 14 → 16 (support ends 2026!) | security, cost            | unsupported since Nov 2026         | Eli    |
| 5 | Picker app offline sync v2                   | ASR 2                     | 1 wrong item/week at Ghent         | Dee    |
… 18 more, ordered
"""),
    tools="tools: the team planning tool, the debt register as a source, fitness-function results, a quarterly planning slot with product.",
    gains=["<b>Architecture work done</b>, not just listed.",
           "<b>Comparable with features</b> in product terms.",
           "<b>Capacity protected</b>.",
           "<b>Product owners</b> help order it.",
           "<b>Results reported</b>."],
    losses=["<b>20 % less</b> for features.",
            "<b>Writing items in product terms</b> takes effort.",
            "<b>Quarterly ordering</b> needs discipline.",
            "<b>Some items</b> still wait."],
    baseline="Each line compares <b>architecture work scattered and competing item by item</b> to <b>one ordered backlog in product terms, with agreed capacity, planned with product</b>.",
    ratings=[(2, 4, "One list everyone can read."),
             (2, 5, "Ordered with Grace and Jonas."),
             (2, 4, "Quarterly ordering, then just do it."),
             (2, 4, "Risky items rise to the top."),
             (3, 4, "Re-ordered each quarter."),
             (2, 4, "Each item links to its source."),
             (2, 4, "Cost of waiting in money."),
             (3, 3, "A quarterly session."),
             (2, 4, "Teams own their items.")],
    pitfalls=[("Separate tool", "A wiki page nobody plans from.", "the same tool as features."),
              ("Engineer language", "“Refactor OrderService.”", "the quality protected and cost of waiting."),
              ("No capacity", "Fighting every sprint.", "an agreed share."),
              ("Never reporting", "Work invisible.", "say what it bought.")],
    use=["Any team with debt, migrations or architecture follow-ups.",
         "When architecture work keeps losing to features.",
         "Quarterly planning.",
         "After an architecture review or incident."],
    skip=["Teams with no architecture work outstanding (rare)."],
    related=["<b>Technical debt register</b> (vol. 2)", "<b>Cost of delay</b> (Grace, book 2 vol. 2)", "<b>Tech-debt talks</b> (Grace, book 2 vol. 3)", "<b>Evolutionary architecture</b> (this volume)"],
    quiz=[("What goes into the architecture backlog?", "Debt, ADR follow-ups, failing fitness functions, migration steps, incident actions."),
          ("How is each item written?", "With the quality it protects and the cost of waiting."),
          ("How much capacity does it get?", "20 % of each team, agreed with Priya."),
          ("Who orders it?", "Ana with the product owners, quarterly.")],
    try_it="Collect all your team's architecture work into one list. Rewrite each item with the quality it protects and the cost of waiting, and ask your product owner to order the top five with you.",
    remember="Keep the <span class=\"hl\">maintenance list</span>, and a fixed share for the <span class=\"hl\">roof</span>.",
    sources=["Philippe Kruchten, Robert Nord and Ipek Ozkaya, <i>Managing Technical Debt</i> (2019).",
             "Donald Reinertsen, <i>The Principles of Product Development Flow</i> (2009).",
             "Scaled Agile, “Enablers” (SAFe documentation).",
             "Martin Fowler, “Technical Debt Quadrant” (2009)."],
)

NOTES = [JUSTENOUGH, EVOLUTIONARY, BACKLOG]
