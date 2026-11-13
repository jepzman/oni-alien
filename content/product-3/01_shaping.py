# Series 2 · Book 2 · The Product Owner's Notebook · Vol. 3 · Shaping work.
# Narrator: Grace. Running case study: Larder (facts in docs/larder-casebook.md).

# ------------------------------------------------------------------ 01 Story Mapping
sm_problem = Doodle(760, 290, "Doodle of the approvals backlog on 16 February 2026: forty-one tickets in a flat list, ordered by when they were written. Nobody can see the customer's journey, the picker's part, or what the first release should contain. Ben asks which tickets make the Noord staff test.",
                    "Forty-one tickets in a flat list. “Which of these make the first release?” Nobody can tell.")
for i in range(9):
    sm_problem.box(30, 20 + i * 26, 300, 20, None, ["paper", "blue", "y"][i % 3], rx=3)
sm_problem.note(180, 270, "41 tickets, oldest first", "red")
sm_problem.box(400, 60, 340, 90, "Ben", "y", sub="“which ones for the Noord test?”")
sm_problem.note(570, 210, "no journey, no slices", "red")

sm_analogy = Doodle(760, 260, "Doodle of planning a road trip on a big map: the stops along the top in order (pack, drive, ferry, campsite, beach), and under each stop, the things to sort out, most important first. A line across says what's needed for the first, shortest trip.",
                     "A road-trip plan: the stops across the top, the things to sort out underneath, and a line for the first, short trip.")
for i, t in enumerate(["pack", "drive", "ferry", "campsite", "beach"]):
    x = 20 + i * 148
    sm_analogy.box(x, 20, 132, 46, t, "y", size=16)
    for k in range(2 + (i % 2)):
        sm_analogy.box(x + 10, 84 + k * 46, 112, 34, None, "paper", rx=4)
sm_analogy.line("M10 170 H750", dash=True, color="red")
sm_analogy.note(590, 240, "first trip: above the line", "red", size=17)
sm_analogy.note(190, 240, "stops across, details down", "pen")

sm_how = Doodle(760, 380, "Grace's story map for approvals, built with Noor and Ben on 16 February 2026. The backbone along the top follows the swap: the item runs out, the picker picks a substitute, the customer is told, the customer decides, the picker packs, the customer receives. Under each step, the stories, most important first. Release lines: R1, the Noord staff test, the thinnest version of every step; R2, all Amsterdam express; R3, slots and Rotterdam.",
                 "The backbone is the swap's journey; stories hang underneath; release lines cut across.")
steps = [("item", "runs out"), ("picker", "picks a swap"), ("customer", "is told"), ("customer", "decides"), ("picker", "packs"), ("customer", "receives")]
for i, (a, b) in enumerate(steps):
    x = 10 + i * 124
    sm_how.box(x, 14, 116, 56, None, "y")
    sm_how.text(x + 58, 38, a, "t-head", size=14)
    sm_how.text(x + 58, 60, b, size=14)
    for k, fill in enumerate(["blue", "paper", "paper"]):
        sm_how.box(x + 6, 80 + k * 72, 104, 32, None, fill, rx=4)
for y, label, c in [(140, "R1 · Noord staff test", "red"), (212, "R2 · Amsterdam express", "pen"), (284, "R3 · slots, Rotterdam", "pen")]:
    sm_how.line(f"M6 {y} H754", dash=True, color="red" if c == "red" else "")
    sm_how.note(750, y - 4, label, c, anchor="end", size=14)
sm_how.note(380, 360, "41 tickets, now in 3 slices across 6 steps", "green", size=17)

STORY_MAP = dict(
    slug="story-mapping",
    kicker="a.k.a. “the road-trip map”",
    tldr="A flat backlog hides the journey. A <b>story map</b> lays out the <b>backbone</b> (the steps a user takes, left to right), hangs the <b>stories</b> under each step (most important at the top), and draws <b>release lines</b> across: everything above the first line is the <b>thinnest version of the whole journey</b>. Build it together, with the team, on a wall; then the backlog is just the map read from the top.",
    chips=[("Family", "shaping work"), ("Origin", "Jeff Patton, <i>User Story Mapping</i> (2014)"), ("Lives in", "a wall or a board, then the backlog"), ("Pairs with", "thin slices, walking skeleton, user stories")],
    problem_side="Larder, 16 February 2026",
    problem="""  <p class="lead">The business case for approvals was approved on 12 February. By the 16th the backlog holds <b>41 tickets</b> in a flat list, ordered by when someone wrote them: “countdown timer”, “picker swap screen”, “push notification copy”, “refund logic”… Ben asks the obvious question: <i>which of these make the Noord staff test?</i> <span class="hl-pink">Nobody can tell</span>, because the list doesn't show the journey they belong to.</p>
  <ul>
    <li>A flat list hides which tickets belong to which step of the journey.</li>
    <li>Teams build one step fully before the next exists at all.</li>
    <li>“What's in the first release?” becomes an argument instead of a line.</li>
  </ul>""",
    problem_figs=[sm_problem],
    analogy_side="the road-trip map",
    analogy="""  <p>Planning a road trip, you lay the <b>stops</b> along the top in order (pack, drive, ferry, campsite, beach), and under each, the <b>things to sort out</b>, most important first. Then you draw a line: for the <b>first, short trip</b>, you need just the top item under every stop. A trip with perfect packing and no ferry booking goes nowhere.</p>""",
    analogy_figs=[sm_analogy],
    map=[("The stops, in order", "The backbone: the swap's journey, step by step"),
         ("Things to sort out per stop", "Stories under each step"),
         ("Most important at the top", "Ordered by need, top to bottom"),
         ("The first, short trip", "Release 1: the Noord staff test"),
         ("Every stop covered", "The thinnest version of the whole journey")],
    how_side="backbone across, stories down, lines across",
    how="""  <p>Grace, Noor (the new product designer) and Ben built the map on a wall in 90 minutes. The backbone follows a swap from <b>item runs out</b> to <b>customer receives</b>, including the picker's steps. The 41 tickets found their places, nine new ones appeared (nobody had written “picker packs with the answer”), and the first release line answered Ben's question: the thinnest version of all six steps, for Noord's staff.</p>""",
    how_figs=[sm_how],
    steps=[("Name the user and the goal", "Here: a customer whose item ran out, and the picker who handles it."),
           ("Lay out the backbone", "The steps, left to right, in the order they happen. Verbs on cards."),
           ("Hang stories under each step", "Everything you might build, most important at the top."),
           ("Walk it together", "With engineering and design: what's missing? Nine cards appeared."),
           ("Draw release lines", "Release 1 = the thinnest version of every step; then R2, R3."),
           ("Read the backlog from the map", "Top to bottom, left to right; keep the map on the wall.")],
    vocab=[("Backbone", "The user's steps across the top of the map."),
           ("Walking skeleton (product)", "The thinnest release that covers every step."),
           ("Release line", "A line across the map: what ships in each release."),
           ("Story", "A small piece of value under a step."),
           ("Narrative flow", "Reading the map left to right as a story."),
           ("Activity", "A group of steps, above the backbone, for big maps.")],
    code=dict(file="product/approvals/story-map.md", note="the approvals story map, 16 February 2026 (top rows)", plain=True, src="""
BACKBONE   item runs out │ picker picks  │ customer told  │ customer      │ picker packs  │ customer
                         │ a swap        │                │ decides       │               │ receives
───────────────────────────────────────────────────────────────────────────────────────────────────
R1 Noord   out-of-stock  │ suggest 1 swap│ push to app    │ yes / no,     │ apply answer  │ order shows
staff test from scanner  │ on handheld   │                │ 2-min timer   │ at packing    │ the swap
──────────────────────── R1 line ───────────────────────────────────────────────────────────────────
R2 AMS     partial stock │ choose from 3 │ banner if app  │ price diff    │ glove-friendly│ refund for
express    (2 of 3)      │               │ closed         │ shown         │ buttons       │ "no", auto
──────────────────────── R2 line ───────────────────────────────────────────────────────────────────
R3 slots,  —             │ remember past │ SMS fallback   │ "never swap   │ —             │ receipt
Rotterdam                │ choices       │ (opt-in)       │ this" inline  │               │ email
"""),
    tools="tools: a wall and sticky notes first; then Miro, FigJam, StoriesOnBoard, Easy Agile or Avion for a shared map linked to the backlog.",
    gains=["<b>The whole journey is visible</b>, not just tickets.",
           "<b>Missing steps show up</b> (nine new cards).",
           "<b>Release 1 is obvious</b>: the thinnest version of every step.",
           "<b>Shared understanding</b>, built together on a wall.",
           "<b>Easy to re-slice</b> when plans change."],
    losses=["<b>Time</b>: a 90-minute session, sometimes two.",
            "<b>Hard to keep in sync</b> with the tracker.",
            "<b>Big maps get unwieldy</b>.",
            "<b>Needs the team in the room</b> to work."],
    baseline="Each line compares <b>a flat backlog ordered by when tickets were written</b> to <b>a story map with the user's journey across the top, stories underneath and release lines across</b>.",
    ratings=[(2, 4, "The map follows the customer's real journey."),
             (3, 4, "Release 1 tests the whole idea, not one screen."),
             (3, 3, "Built from the journey map and the prototype findings."),
             (2, 4, "A thin end-to-end release learns sooner."),
             (2, 5, "One line says what's in release 1."),
             (2, 5, "Everyone sees where each ticket fits."),
             (3, 4, "Stakeholders read the release lines at a glance."),
             (2, 4, "Slices flow end to end."),
             (3, 3, "A 90-minute session, then light upkeep.")],
    pitfalls=[("Building it alone", "Grace's map, handed over.", "build it with engineering and design, on a wall."),
              ("Screens as the backbone", "The backbone lists screens, not steps.", "use the user's verbs: “customer decides”."),
              ("A fat first release", "Release 1 completes step one perfectly.", "release 1 is the thinnest version of every step."),
              ("Map then forget", "The wall is cleaned after a week.", "keep it up; re-read it at each release.")],
    use=["New features with a multi-step journey.",
         "When a backlog has grown into a flat list.",
         "Planning the first release of something new.",
         "Onboarding a team to a feature."],
    skip=["Single-step changes and bug fixes.",
          "Work with no user journey (pure infrastructure)."],
    related=["<b>Thin slices of value</b> (this volume)", "<b>User stories that work</b> (this volume)", "<b>Customer journey map</b> (Vol. 1)", "<b>Walking skeleton</b> (Ana, book 1 vol. 1)"],
    quiz=[("What runs across the top of a story map?", "The backbone: the user's steps, in order."),
          ("What goes above the first release line?", "The thinnest version of every step of the journey."),
          ("Why build it together?", "Engineers and designers spot missing steps and share the picture."),
          ("How does the backlog relate to the map?", "It's the map read top to bottom, left to right.")],
    try_it="Take a feature with a long backlog. On a wall, write the user's steps as verbs across the top, place every ticket under its step, and draw one line: the thinnest version of every step. Do it with one engineer and one designer, in 90 minutes.",
    remember="<span class=\"hl\">Stops</span> across, details down. The first trip covers <span class=\"hl\">every stop</span>.",
    sources=["Jeff Patton, <i>User Story Mapping</i> (2014).",
             "Jeff Patton, “The New User Story Backlog Is a Map” (2008).",
             "Mike Cohn, <i>User Stories Applied</i> (2004).",
             "Alistair Cockburn, on the walking skeleton (2004)."],
)

# ------------------------------------------------------------------ 02 Thin Slices of Value
ts_problem = Doodle(760, 280, "Doodle of two ways to build approvals. Layer by layer: eight weeks of backend, then app screens, then picker screens, and nothing works for anyone until week eight. Slice by slice: a thin version of everything that a Noord picker and a customer can use in week three.",
                    "Layers deliver nothing until week eight. A thin slice works end to end in week three.")
ts_problem.head(20, 40, "layers", anchor="start", size=17)
for i, (t, f) in enumerate([("backend", "blue"), ("app screens", "y"), ("picker screens", "paper")]):
    ts_problem.box(130 + i * 196, 20, 186, 40, t, f, size=15, rx=4)
ts_problem.note(380, 90, "nothing usable until week 8", "red", size=18)
ts_problem.head(20, 160, "slices", anchor="start", size=17)
for i in range(4):
    ts_problem.box(130 + i * 152, 130, 140, 60, f"slice {i + 1}", "green" if i == 0 else "paper", size=15, rx=4)
ts_problem.note(380, 230, "slice 1 usable in week 3", "green", size=18)

ts_analogy = Doodle(760, 250, "Doodle of a layer cake. Cutting it horizontally gives someone only the sponge, someone else only the cream. Cutting a thin vertical slice gives everyone a little of every layer: a real taste of the cake.",
                     "Cut a cake in layers and nobody tastes the cake. Cut a thin slice and everyone gets every layer.")
for i, f in enumerate(["y", "pink", "blue", "y"]):
    ts_analogy.box(60, 40 + i * 40, 260, 36, None, f, rx=4)
ts_analogy.box(240, 36, 30, 166, None, "green", stroke="green", rx=2)
ts_analogy.note(190, 230, "a thin slice: every layer", "green", size=17)
ts_analogy.box(440, 70, 300, 90, "a layer each", "pink", sub="nobody tastes the cake")

ts_how = Doodle(760, 360, "How Grace and Ben sliced approvals, 23 February 2026. Slice 1: express orders, one swap per order, Noord staff accounts only, live on 30 March. Slice 2: all Amsterdam express, up to three swaps, price difference shown, live on 13 April. Slice 3: slot orders and the never-swap toggle inline. Slice 4: Rotterdam and the web shop. Each slice works end to end, from picker to customer, and teaches something before the next.",
                 "Four slices, each end to end, each a release that teaches something. Thin enough to ship in weeks.")
rows = [("slice 1", "express · 1 swap · Noord staff", "30 Mar", "green"), ("slice 2", "all AMS express · 3 swaps · price diff", "13 Apr", "y"),
        ("slice 3", "slot orders · “never swap” inline", "May", "paper"), ("slice 4", "Rotterdam · web shop", "Jun", "paper")]
for i, (s, what, when, f) in enumerate(rows):
    y = 16 + i * 74
    ts_how.box(14, y, 732, 62, None, f, rx=8)
    ts_how.text(30, y + 38, s, "t-head", anchor="start", size=16)
    ts_how.text(150, y + 38, what, anchor="start", size=15)
    ts_how.text(730, y + 38, when, "t-head", anchor="end", size=15)
ts_how.note(380, 340, "each slice: picker → customer → packing, working", "pen", size=17)

THIN = dict(
    slug="thin-slices",
    kicker="a.k.a. “a slice of the cake, not a layer”",
    tldr="Building a feature <b>layer by layer</b> (all the backend, then all the screens) means nothing works until the end, and you learn nothing until then. Cut it into <b>thin vertical slices</b> instead: each one a little of every layer, <b>working end to end</b> for some real user, small enough to ship in a week or two. Order the slices so each one <b>teaches you something</b> before the next, and make the first one embarrassingly small.",
    chips=[("Family", "shaping work"), ("Origin", "vertical slicing in agile practice (Bill Wake, Mike Cohn); Gojko Adzic, “hamburger method”"), ("Lives in", "the release lines on the story map"), ("Pairs with", "story mapping, MVP vs MLP, dark launches")],
    problem_side="Larder, 23 February 2026",
    problem="""  <p class="lead">Ben's first plan for approvals is sensible engineering: <b>backend first</b> (two weeks), then the <b>customer app</b>, then the <b>picker screens</b>, then refunds. It's eight weeks before a picker and a customer can try anything together, and the riskiest question (<i>will pickers keep going while customers decide?</i>) is answered last. <span class="hl-pink">Nothing usable until week eight</span>, and the business case's clock is ticking at €30k a month.</p>
  <ul>
    <li>Layered plans deliver nothing usable until the last layer lands.</li>
    <li>The riskiest assumptions are tested last.</li>
    <li>Partial layers can't be shown to users for feedback.</li>
  </ul>""",
    problem_figs=[ts_problem],
    analogy_side="the layer cake",
    analogy="""  <p>Cut a layer cake <b>horizontally</b> and one guest gets sponge, another cream, another jam: nobody tastes the cake. Cut a <b>thin vertical slice</b> and every guest gets a little of every layer, a real taste of the whole thing. If the recipe's wrong, you find out from the first slice, not after serving the whole cake.</p>""",
    analogy_figs=[ts_analogy],
    map=[("The layers", "Backend, customer app, picker screens, refunds"),
         ("A thin vertical slice", "One swap, express only, Noord staff: every layer, a little"),
         ("Tasting the cake", "A picker and a customer using it end to end"),
         ("A wrong recipe found early", "Learning at slice 1, not week 8"),
         ("More slices", "Slices 2–4: more orders, more cases, more cities")],
    how_side="each slice end to end, each one teaches",
    how="""  <p>Grace and Ben cut four slices. <b>Slice 1</b>: express orders, <b>one swap</b> per order, Noord <b>staff accounts</b> only: ugly-but-working, live on 30 March, three weeks in. It taught the big lesson: pickers waiting for answers slowed packing, so “answer applied at packing” moved into slice 2. <b>Slice 2</b> went to all Amsterdam express on 13 April; slices 3 and 4 follow with slots, Rotterdam and the web shop.</p>""",
    how_figs=[ts_how],
    steps=[("Find the end-to-end path", "From the story map: the top card under every step."),
           ("Cut by case, not by layer", "Fewer order types, fewer swaps, fewer users, one store, one city."),
           ("Make slice 1 tiny", "Staff only, one case, rough edges: but working end to end."),
           ("Put the riskiest question first", "The slice that answers it ships first."),
           ("Size each slice to a week or two", "If it's longer, cut by another case."),
           ("Learn, then re-slice", "Each release changes what the next slice should be.")],
    vocab=[("Vertical slice", "A thin piece of a feature that works through every layer."),
           ("Horizontal layer", "One technical part (backend, UI) built on its own."),
           ("Splitting by case", "Fewer order types, users, stores or rules per slice."),
           ("Hamburger method", "Gojko Adzic's way of picking one option per layer."),
           ("Risk-first", "Ordering slices to answer the riskiest question soonest."),
           ("Increment", "A slice released to some real users.")],
    code=dict(file="product/approvals/slices.md", note="Grace and Ben's slicing, 23 February 2026", plain=True, src="""
# Approvals · slices                                         riskiest question first

Riskiest   Will pickers keep going while customers decide? (prototype: unsure)

Slice 1    Express only · 1 swap per order · Noord staff accounts · rough UI
           Ships 30 Mar (R1). Learn: picker flow, answer rate, packing time.
Slice 2    All Amsterdam express · up to 3 swaps · price difference shown ·
           answer applied at packing (from slice 1!) · Ships 13 Apr (R2), flag ramp.
Slice 3    Slot orders · "never swap this" inline · banner if the app is closed
           Ships May. Learn: do slot customers answer at all?
Slice 4    Rotterdam · web shop (~20 % of orders)      Ships June (R3).

Not sliced by layer: no "backend sprint", no "UI sprint".
"""),
    tools="tools: the story map's release lines; feature flags to release slices to staff or a percentage; Gojko Adzic's “hamburger method” and Richard Lawrence's story-splitting patterns as guides.",
    gains=["<b>Something works in weeks</b>, not months.",
           "<b>Risk tested first</b>: the picker flow in week three.",
           "<b>Real feedback</b> from real users at every slice.",
           "<b>Value starts sooner</b>: refunds fall from slice 2.",
           "<b>Easy to stop or turn</b> after any slice."],
    losses=["<b>Some rework</b>: early slices get rebuilt.",
            "<b>Engineers may feel it's messy</b> at first.",
            "<b>Needs feature flags</b> and good release habits.",
            "<b>Hard to slice</b> some technical foundations."],
    baseline="Each line compares <b>building a feature layer by layer, usable only at the end</b> to <b>thin vertical slices, each working end to end, riskiest first</b>.",
    ratings=[(2, 4, "Customers use a real version in weeks."),
             (2, 4, "Refunds start falling from slice 2."),
             (2, 4, "Each slice brings real usage data."),
             (1, 5, "The riskiest question answered in week three."),
             (2, 4, "One slice at a time, each small."),
             (3, 4, "Everyone knows what this slice is for."),
             (2, 4, "Stakeholders see working software early."),
             (2, 5, "Small releases, every week or two."),
             (3, 3, "Release habits and flags needed.")],
    pitfalls=[("Slicing by layer", "“Sprint 1: the backend.”", "every slice crosses every layer."),
              ("Slice 1 too big", "A complete feature for one city.", "staff only, one case, rough edges."),
              ("Risk last", "The easy slices first.", "the slice that answers the riskiest question goes first."),
              ("Never re-slicing", "The plan from February, unchanged in May.", "re-slice after every release.")],
    use=["Any feature that takes more than two weeks.",
         "When the riskiest assumption isn't tested yet.",
         "When stakeholders want to see progress early.",
         "Paired with feature flags."],
    skip=["Truly indivisible changes (a legal deadline switch).",
          "One-day tasks."],
    related=["<b>Story mapping</b> (this volume)", "<b>MVP vs MLP</b> (this volume)", "<b>Dark launches &amp; rollouts</b> (this volume)", "<b>Walking skeleton</b> (Ana, book 1 vol. 1)"],
    quiz=[("What's a vertical slice?", "A thin piece of a feature that works through every layer, end to end."),
          ("How do you make a slice thinner?", "Cut by case: fewer order types, swaps, users, stores or cities."),
          ("Which slice goes first?", "The one that answers the riskiest question."),
          ("What did slice 1 teach Larder?", "Pickers waiting slowed packing, so answers moved to packing time in slice 2.")],
    try_it="Take the next feature on your roadmap. Write down its riskiest question, then describe a first slice that works end to end for five internal users and could ship in two weeks. Show it to an engineer and ask what else could be cut.",
    remember="A <span class=\"hl\">slice</span> of the cake, not a layer. The first one, <span class=\"hl\">tiny</span>.",
    sources=["Jeff Patton, <i>User Story Mapping</i> (2014).",
             "Gojko Adzic, “Splitting user stories: the hamburger method” (gojko.net, 2012).",
             "Richard Lawrence and Peter Green, “The Humanizing Work Guide to Splitting User Stories”.",
             "Bill Wake, “INVEST in Good Stories, and SMART Tasks” (2003)."],
)

# ------------------------------------------------------------------ 03 MVP vs MLP
mv_problem = Doodle(760, 280, "Doodle of a disagreement on 2 March 2026. Dee wants the minimum: a grey pop-up with yes and no. Noor wants it lovable: a photo, the price difference, a big countdown. Both use the word minimum. Grace's question: minimum for what?",
                    "A grey pop-up or a lovable screen? Both sides say “minimum”. Minimum for what?")
mv_problem.box(20, 30, 330, 160, None, "paper")
mv_problem.head(185, 62, "Dee's MVP", size=17)
mv_problem.box(70, 90, 230, 70, "swap? yes / no", "blue", size=15)
mv_problem.box(410, 30, 330, 160, None, "y")
mv_problem.head(575, 62, "Noor's version", size=17)
for i, t in enumerate(["photo of the swap", "+ €0.40 difference", "big 2:00 countdown"]):
    mv_problem.text(575, 100 + i * 28, t, size=15)
mv_problem.note(380, 250, "minimum for what?", "red", size=20)

mv_analogy = Doodle(760, 250, "Doodle of a first date at a food truck. Minimum viable: a sandwich in a paper bag, it feeds you. Minimum lovable: the same sandwich, warm, with a napkin and a smile. Same cost, very different second date.",
                     "Minimum viable feeds you. Minimum lovable is the same sandwich, warm, with a napkin and a smile.")
mv_analogy.icon("kitchen", 40, 60, 1.3)
mv_analogy.box(190, 50, 260, 90, "viable", "paper", sub="a cold sandwich in a bag")
mv_analogy.box(480, 50, 260, 90, "lovable", "green", sub="warm, a napkin, a smile")
mv_analogy.note(465, 210, "same cost, very different second date", "pen")

mv_how = Doodle(760, 360, "How Grace split it. The customer's moment of trust, the swap screen, gets the lovable treatment: a photo, the price difference, a big countdown, one tap to answer; prototype tests showed these mattered. Internal tools get the viable treatment: support sees answers in a plain admin table, reports come from a query. Rule: lovable where customers feel it; viable where only staff see it.",
                 "Lovable where the customer feels it, viable where only staff see it. Decide per screen, not per feature.")
mv_how.box(14, 20, 360, 250, None, "green")
mv_how.head(194, 54, "lovable", size=19)
for i, t in enumerate(["photo of the substitute", "price difference, clear", "big 2-minute countdown", "one tap, glove-friendly (pickers)"]):
    mv_how.text(194, 96 + i * 36, t, size=15)
mv_how.note(194, 250, "the customer's moment of trust", "green", size=16)
mv_how.box(386, 20, 360, 250, None, "paper")
mv_how.head(566, 54, "viable", size=19)
for i, t in enumerate(["support: a plain admin table", "reports: a saved query", "settings: a config file", "no animations"]):
    mv_how.text(566, 96 + i * 36, t, size=15)
mv_how.note(566, 250, "only staff see it", "pen", size=16)
mv_how.note(380, 320, "decide per screen, using what the prototype showed", "pen", size=17)

MVP_MLP = dict(
    slug="mvp-vs-mlp",
    kicker="a.k.a. “the warm sandwich”",
    tldr="“Minimum viable product” is often read as “the least we can get away with”. For moments where customers <b>judge you</b>, that can kill the idea before it's tested. A <b>minimum lovable product</b> keeps the scope small but makes the <b>few things customers feel</b> genuinely good. The question isn't MVP or MLP for the whole feature; it's <b>minimum for what, per screen</b>: lovable where customers form trust, viable where only staff see it.",
    chips=[("Family", "shaping work"), ("Origin", "MVP: Frank Robinson (2001), Eric Ries, <i>The Lean Startup</i> (2011); MLP: Brian de Haaff (2013)"), ("Lives in", "the slice plan and the design brief"), ("Pairs with", "thin slices, prototype testing, Kano model")],
    problem_side="Larder, 2 March 2026",
    problem="""  <p class="lead">Slice 1 is planned; now: what should the swap screen look like? <b>Dee</b> argues for the minimum: a grey pop-up, “swap? yes / no”. <b>Noor</b>, the product designer who joined in February, wants a photo of the substitute, the price difference and a big countdown. Both say “minimum”. Both are right about something. <span class="hl-pink">Minimum for what?</span></p>
  <ul>
    <li>“Viable” gets read as “ugly is fine”, even at moments of trust.</li>
    <li>“Lovable” gets read as “polish everything”, blowing up scope.</li>
    <li>The team argues taste instead of evidence.</li>
  </ul>""",
    problem_figs=[mv_problem],
    analogy_side="the food truck on a first date",
    analogy="""  <p>On a first date at a food truck, a <b>cold sandwich in a paper bag</b> is viable: it feeds you. The <b>same sandwich, warm, with a napkin and a smile</b>, costs about the same and gets a second date. Nobody needs a five-course meal; but the few things your date notices should be good.</p>""",
    analogy_figs=[mv_analogy],
    map=[("The cold sandwich", "A grey yes/no pop-up"),
         ("Warm, a napkin, a smile", "Photo, price difference, countdown"),
         ("What your date notices", "The swap screen: the customer's moment of trust"),
         ("What they don't see", "Support tables, reports, settings"),
         ("The second date", "Customers who answer, and trust the next swap")],
    how_side="lovable per screen, where it's felt",
    how="""  <p>Grace settled it with the January <b>prototype test</b>: customers hesitated without the price difference and missed small timers; pickers needed big buttons for gloves. So the <b>customer's swap screen</b> and the <b>picker's buttons</b> got the lovable treatment; <b>support's view</b> became a plain admin table and the reports a saved query. The scope barely grew; the moment of trust got what it needed.</p>""",
    how_figs=[mv_how],
    steps=[("Ask “minimum for what?”", "What must this release prove, and to whom?"),
           ("Find the moments of trust", "Screens where customers judge you: first use, money, bad news."),
           ("Use evidence for “lovable”", "Prototype findings, interviews, Kano: what customers noticed."),
           ("Make those few things good", "Clear, kind, fast, accessible: not more features."),
           ("Keep everything else viable", "Staff tools, reports, settings: plain and working."),
           ("Decide per screen, write it down", "In the slice plan, so the debate isn't repeated.")],
    vocab=[("MVP", "Minimum viable product: the smallest thing that tests the idea."),
           ("MLP", "Minimum lovable product: small, but good where customers feel it."),
           ("Moment of trust", "A point where customers decide whether to trust you."),
           ("Polish", "Care beyond working: copy, layout, feedback, speed."),
           ("Scope", "How much is built; separate from how well."),
           ("Gold-plating", "Polish where nobody notices it.")],
    code=dict(file="product/approvals/design-brief.md", note="design brief for slice 1–2, 2 March 2026", plain=True, src="""
# Approvals · design brief (Noor, Grace, Dee)        lovable vs viable, per screen

Customer swap screen      LOVABLE   photo of the substitute · price difference
                                    (+ €0.40) · big 2:00 countdown · one tap
                                    evidence: prototype test (6 customers, Jan)
Picker swap buttons       LOVABLE   glove-sized buttons · continue picking
                                    evidence: prototype test (3 pickers)
Customer order screen     viable    shows the swap and its answer, plain text
Support view (Sam)        viable    admin table: order, swap, answer, time
Reports                   viable    a saved query, weekly
Settings (2-min window)   viable    config value; no UI

Rule: lovable where customers or pickers feel it; viable where only office staff see it.
"""),
    tools="tools: the prototype test findings; a design brief per slice; accessibility checks (contrast, tap targets) as part of “lovable”.",
    gains=["<b>The idea gets a fair test</b>: users don't reject it for being ugly.",
           "<b>Scope stays small</b>: polish only where felt.",
           "<b>Evidence-based design calls</b>, not taste.",
           "<b>Faster internal tools</b>: plain is fine.",
           "<b>Designer and engineer agree</b> per screen."],
    losses=["<b>Lovable takes design time</b> early.",
            "<b>Hard to judge</b> without user evidence.",
            "<b>Staff tools stay rough</b>; support may grumble.",
            "<b>“Lovable” can creep</b> into everything."],
    baseline="Each line compares <b>“minimum” argued as a matter of taste for a whole feature</b> to <b>lovable where customers form trust and viable elsewhere, decided per screen with evidence</b>.",
    ratings=[(2, 5, "The swap screen is clear and kind where it matters."),
             (3, 4, "A fair test of the idea protects the business case."),
             (2, 4, "Prototype findings decide what's lovable."),
             (3, 4, "Slice 1 still ships in three weeks."),
             (2, 4, "Polish only on two screens."),
             (2, 4, "The brief settles the debate for everyone."),
             (3, 3, "Neutral."),
             (3, 4, "Plain internal tools ship fast."),
             (3, 3, "A short brief per slice.")],
    pitfalls=[("Ugly at the moment of trust", "A grey pop-up asking about money.", "make the customer's few key screens lovable."),
              ("Polish everywhere", "Animated admin tables.", "viable where only staff see it."),
              ("Taste, not evidence", "Designer vs engineer, round three.", "use prototype and interview findings."),
              ("MVP as an excuse", "“It's just an MVP” for a broken flow.", "viable still means it works end to end.")],
    use=["First releases of customer-facing features.",
         "Moments involving money, bad news or first use.",
         "Debates between “ship ugly” and “polish first”.",
         "Planning a slice's design scope."],
    skip=["Internal tools only staff use.",
          "Pure experiments like fake doors."],
    related=["<b>Thin slices of value</b> (this volume)", "<b>Prototype testing with users</b> (Vol. 1)", "<b>Kano model</b> (Vol. 2)", "<b>Release notes &amp; customer comms</b> (this volume)"],
    quiz=[("What does “minimum for what?” ask?", "What this release must prove, and to whom, before deciding how much polish."),
          ("Where should a product be lovable?", "At moments of trust customers feel: money, bad news, first use."),
          ("Where is viable enough?", "Where only staff see it: admin tables, reports, settings."),
          ("What decided Larder's lovable list?", "The prototype test findings from January.")],
    try_it="List every screen in your next release. Mark each one: does a customer judge us here? For the two that matter most, write three things that would make them lovable, based on evidence. Make the rest plain.",
    remember="Same sandwich, <span class=\"hl\">warm</span>, with a napkin. Lovable where it's <span class=\"hl\">felt</span>.",
    sources=["Eric Ries, <i>The Lean Startup</i> (2011).",
             "Brian de Haaff, “Sorry, Minimum Viable Products Are Not Enough” (Aha!, 2013).",
             "Henrik Kniberg, “Making sense of MVP” (2016), the skateboard drawing.",
             "Laura Klein, <i>Build Better Products</i> (2016)."],
)

# ------------------------------------------------------------------ 04 Pre-mortem
pm_problem = Doodle(760, 280, "Doodle of the approvals launch plan in March 2026: everyone is optimistic. The concierge test worked, the prototype test worked, the business case was approved. Nobody has asked what could make the Amsterdam launch fail.",
                    "Every test passed, everyone's optimistic, and nobody has asked how it could fail.")
for i, (t, f) in enumerate([("concierge ✓", "green"), ("prototype ✓", "green"), ("business case ✓", "green")]):
    pm_problem.box(20 + i * 250, 40, 220, 70, t, f, size=17)
pm_problem.box(170, 150, 420, 70, "how could it fail?", "pink", sub="nobody asked", stroke="red")
pm_problem.note(380, 262, "optimism is not a plan", "red")

pm_analogy = Doodle(760, 250, "Doodle of a mountain guide's briefing the evening before a climb: imagine it's tomorrow afternoon and we had to turn back. Why? The weather turned, someone's boots failed, we started late. Each reason becomes a check for the morning.",
                     "The guide's question the night before: “we turned back tomorrow. Why?” Each answer becomes a morning check.")
pm_analogy.icon("pyramid", 40, 60, 1.6)
for i, (t, f) in enumerate([("weather turned", "pink"), ("boots failed", "pink"), ("started late", "pink")]):
    pm_analogy.box(180 + i * 190, 50, 176, 60, t, f, size=16)
    pm_analogy.arrow(268 + i * 190, 116, 268 + i * 190, 150)
    pm_analogy.box(180 + i * 190, 154, 176, 50, ["forecast 05:00", "boot check", "leave 04:30"][i], "green", size=14)

pm_how = Doodle(760, 360, "Grace's pre-mortem for the Amsterdam launch, 16 March 2026, with Ben, Noor, Dee, Sam and Tomás. It's mid-May and approvals failed: why? Ten minutes writing alone, then sharing. Top reasons: 37 percent of customers have notifications switched off and never see the question; pickers wait for answers at the Friday peak; customers accept a swap that contains an allergen; the price difference confuses people. Actions: an in-app banner and a default when there's no answer; answers applied at packing; an allergen warning on the swap; clearer price wording. Each with an owner before the launch.",
                 "“It's May and it failed. Why?” Ten minutes alone, then share, then turn the top reasons into actions with owners.")
pm_how.box(14, 14, 732, 56, "“It's mid-May. Approvals failed. Why?”", "y", size=17)
for i, (why, fix, f) in enumerate([("37 % have notifications off", "banner + default if no answer", "pink"),
                                   ("pickers wait at peak", "answer applied at packing", "pink"),
                                   ("swap contains an allergen", "allergen warning on the swap", "pink"),
                                   ("price difference confuses", "“+ €0.40 more” wording", "y")]):
    y = 88 + i * 62
    pm_how.box(14, y, 330, 50, why, f, size=14, rx=6)
    pm_how.arrow(348, y + 25, 404, y + 25)
    pm_how.box(408, y, 338, 50, fix, "green", size=14, rx=6)
pm_how.note(380, 344, "each action with an owner, before 13 April", "pen", size=17)

PRE_MORTEM = dict(
    slug="pre-mortem",
    kicker="a.k.a. “we turned back tomorrow: why?”",
    tldr="When a launch looks good, people stop looking for problems. A <b>pre-mortem</b> flips the question: <b>imagine it's after the launch and it failed</b>. Everyone writes down, <b>alone, for ten minutes</b>, why it failed. Share, cluster, pick the <b>most likely and most damaging</b> reasons, and turn each into an <b>action with an owner</b> before the launch. It makes doubt safe to say out loud, and finds the risks optimism hides.",
    chips=[("Family", "shaping work"), ("Origin", "Gary Klein, “Performing a Project Premortem” (Harvard Business Review, 2007)"), ("Lives in", "a one-hour session, then actions in the launch checklist"), ("Pairs with", "assumption mapping, launch checklist, risk-storming")],
    problem_side="Larder, 16 March 2026",
    problem="""  <p class="lead">Approvals has everything going for it: the concierge test, the prototype test, an approved business case, slice 1 in two weeks. The team is <b>optimistic</b>, and that's the danger. Nobody has asked how the Amsterdam launch on 13 April could fail; <span class="hl-pink">doubts feel like disloyalty</span> when everyone's excited.</p>
  <ul>
    <li>Success so far makes people stop looking for problems.</li>
    <li>Junior team members don't raise doubts in an excited room.</li>
    <li>Risks are discussed generally (“adoption”) instead of specifically.</li>
  </ul>""",
    problem_figs=[pm_problem],
    analogy_side="the mountain guide's briefing",
    analogy="""  <p>The evening before a climb, a good mountain guide asks the group: <b>“Imagine it's tomorrow afternoon and we turned back. Why?”</b> The weather turned. Someone's boots failed. We started late. Each answer becomes a <b>check for the morning</b>: forecast at 05:00, a boot check, leave at 04:30. Nobody is being negative; they're planning.</p>""",
    analogy_figs=[pm_analogy],
    map=[("“We turned back. Why?”", "“It's mid-May and approvals failed. Why?”"),
         ("The weather turned", "37 % of customers have notifications off"),
         ("Boots failed", "Pickers wait for answers at the Friday peak"),
         ("Forecast at 05:00", "A banner and a default when there's no answer"),
         ("The morning checks", "Actions with owners in the launch checklist")],
    how_side="imagine failure, write alone, act",
    how="""  <p>Grace ran it with Ben, Noor, Dee, Sam and Tomás: ten minutes writing alone, then round the table. Sam's reason surprised everyone: <b>37 % of app users have notifications switched off</b>, so they'd never see the question. Tomás worried about pickers waiting at the Friday peak; Noor about <b>allergens</b> in a substitute. Four actions, each with an owner, went into the launch checklist; all four shipped before 13 April.</p>""",
    how_figs=[pm_how],
    steps=[("Set the scene", "“It's [date after launch]. It failed. Why?” Make failure certain, not hypothetical."),
           ("Write alone, ten minutes", "Everyone, including the quietest; no discussion yet."),
           ("Share round the table", "One reason each, round and round, until all are out."),
           ("Cluster and rank", "Most likely × most damaging; pick the top four or five."),
           ("Turn each into an action", "A change, a check or a fallback, with an owner and a date."),
           ("Put actions in the plan", "In the launch checklist, reviewed at go/no-go.")],
    vocab=[("Pre-mortem", "Imagining a future failure to find its causes now."),
           ("Post-mortem", "Analysing a failure after it happened."),
           ("Prospective hindsight", "Imagining an event has happened makes causes easier to name."),
           ("Fallback", "What happens when the main path fails (a default answer)."),
           ("Go / no-go", "The decision meeting before launch."),
           ("Optimism bias", "The tendency to underestimate what can go wrong.")],
    code=dict(file="product/approvals/pre-mortem.md", note="pre-mortem, 16 March 2026", plain=True, src="""
# Pre-mortem · approvals in Amsterdam (launch 13 Apr)
Prompt: "It's 15 May. Approvals failed and was switched off. Why?"
With: Grace, Ben, Noor, Dee, Sam, Tomás · 10 min alone, then share · 23 reasons

Top reasons (likely × damaging)              Action                              Owner  By
1 37 % of app users have notifications off   in-app banner when the app opens;   Dee    6 Apr
  → never see the question                   no answer in 2 min → default rule
2 Pickers wait for answers at Friday peak    answer applied at packing, never    Ben    6 Apr
                                             block picking
3 A substitute contains an allergen          allergen warning on the swap card;  Noor   10 Apr
                                             "never swap" for flagged items
4 "+€0.40" read as a charge for answering    wording: "€0.40 more than ordered"  Noor   10 Apr
Also noted: support doesn't know the feature (→ Sam's macros, launch checklist)
"""),
    tools="tools: a room, sticky notes and a timer; or a shared doc with everyone writing in silence first. Gary Klein's original article is two pages and worth reading.",
    gains=["<b>Hidden risks found</b>: notifications off for 37 %.",
           "<b>Doubt becomes safe</b> to say.",
           "<b>Specific risks</b>, not “adoption”.",
           "<b>Actions with owners</b> before launch.",
           "<b>Quiet people contribute</b> by writing alone first."],
    losses=["<b>An hour</b> of the team's time.",
            "<b>Can feel negative</b> if framed badly.",
            "<b>Long lists</b> need ruthless ranking.",
            "<b>Only as good as who's in the room</b>."],
    baseline="Each line compares <b>launching on the momentum of passed tests</b> to <b>a pre-mortem that imagines failure, ranks the reasons and turns the top ones into owned actions</b>.",
    ratings=[(2, 4, "Customers with notifications off still get asked."),
             (2, 4, "The launch protects the business case."),
             (2, 4, "Sam's data turned a worry into a number."),
             (2, 4, "Risks found a month before launch, not after."),
             (3, 3, "Neutral."),
             (2, 4, "Everyone hears everyone's doubts."),
             (2, 4, "The go/no-go has evidence behind it."),
             (3, 3, "Neutral."),
             (3, 3, "One hour, one list of actions.")],
    pitfalls=[("Discussing before writing", "The loudest voice sets the list.", "ten minutes alone, in silence, first."),
              ("“If it fails…”", "Hypothetical framing; people hedge.", "it failed: say why."),
              ("A list with no actions", "23 worries, no owners.", "top four or five become actions with owners and dates."),
              ("Only the core team", "No support, no operations.", "invite the people who'll feel the launch.")],
    use=["Before any launch the team is excited about.",
         "Big bets with a business case behind them.",
         "Launches that touch operations or support.",
         "When nobody is raising concerns."],
    skip=["Tiny, easily reversed changes.",
          "Experiments designed to fail cheaply."],
    related=["<b>Launch checklist</b> (this volume)", "<b>Assumption mapping</b> (Vol. 1)", "<b>Risk-storming</b> (Ana, book 1 vol. 1)", "<b>Dark launches &amp; rollouts</b> (this volume)"],
    quiz=[("What's the pre-mortem prompt?", "It's after the launch and it failed: why?"),
          ("Why write alone first?", "So everyone's reasons come out, not just the loudest voice's."),
          ("What did Sam's reason reveal?", "37 % of app users have notifications off and would never see the question."),
          ("What happens to the top reasons?", "Each becomes an action with an owner and a date, in the launch checklist.")],
    try_it="Before your next launch, gather the team and support for 45 minutes. Say: “It's a month after launch and it failed. Write why, alone, for ten minutes.” Share, rank, and leave with four actions, each with an owner and a date.",
    remember="“We turned back <span class=\"hl\">tomorrow</span>. Why?” Then fix it <span class=\"hl\">tonight</span>.",
    sources=["Gary Klein, “Performing a Project Premortem” (Harvard Business Review, 2007).",
             "Daniel Kahneman, <i>Thinking, Fast and Slow</i> (2011), on the pre-mortem.",
             "Deborah Mitchell, J. Edward Russo, Nancy Pennington, “Back to the future: temporal perspective in the explanation of events” (1989).",
             "Atlassian Team Playbook, “Pre-mortem”."],
)

NOTES = [STORY_MAP, THIN, MVP_MLP, PRE_MORTEM]
