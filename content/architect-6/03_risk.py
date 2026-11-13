# Series 2 · The Solution Architect's Notebook · Vol. 6 · Risk & transition.
# Running case study: Larder (facts in docs/larder-casebook.md).

# ------------------------------------------------------------------ 08 Risk Register
rr_problem = Doodle(760, 280, "Doodle of April 2028. The 2028 plan has Ghent opening in June, Haarlem in September, Ordering's database split, Larder Plus growing fast, and Ana as the only architect. Risks come up in every meeting, get nodded at, and vanish. The December 2025 risk-storm wall photo is the last time anyone listed them.",
                    "Risks raised in every meeting, nodded at, and gone. The last list is a 2025 wall photo.")
for i, (t, f) in enumerate([("Ghent, June", "paper"), ("Haarlem, Sep", "paper"), ("Ordering split", "y"), ("one architect", "pink")]):
    rr_problem.box(14 + i * 184, 40, 174, 70, t, f, size=15)
rr_problem.note(380, 190, "nodded at, then gone", "red", size=20)

rr_analogy = Doodle(760, 250, "Doodle of a ship's captain's list of dangers on the chart table: shallows, a storm forecast, a tired crew. Each with how likely, how bad, what we're doing, and who's watching it. Read every watch.",
                     "The captain's list of dangers: likelihood, harm, what we're doing, who's watching. Read every watch.")
rr_analogy.icon("ship", 30, 70, 1.1)
for i, (t, f) in enumerate([("shallows", "y"), ("storm", "pink"), ("tired crew", "blue")]):
    rr_analogy.box(150 + i * 200, 60, 186, 70, t, f, size=16)
rr_analogy.note(450, 200, "read every watch", "pen")

rr_how = Doodle(760, 400, "Larder's 2028 risk register, started 24 April 2028, twelve risks, reviewed every fortnight in fifteen minutes. Each: likelihood and impact from 1 to 5, an owner, actions, a review date. Top risks: Ordering split corrupts orders during the switch, 2 by 5, Ben, rehearse and keep rollback for two weeks. Ana is a single point of failure for architecture, 4 by 4, Ana, grow two more architects by September. Ghent store fit-out late, 3 by 4, Joost, weekly check with the builder. Plus orders beat capacity on Fridays, 3 by 3, Eli, capacity plan monthly.",
                 "Twelve risks: likelihood × impact, an owner, actions, a review date. Fifteen minutes a fortnight.")
rr_how.head(20, 30, "risk", anchor="start", size=15)
rr_how.head(390, 30, "L × I", anchor="start", size=15)
rr_how.head(480, 30, "owner", anchor="start", size=15)
rr_how.head(580, 30, "action", anchor="start", size=15)
for i, (r, li, o, a, f) in enumerate([("Ana: single point", "4 × 4", "Ana", "grow 2 architects", "pink"), ("Ghent fit-out late", "3 × 4", "Joost", "weekly builder check", "y"),
                                      ("Plus beats capacity", "3 × 3", "Eli", "monthly capacity", "y"), ("split corrupts orders", "2 × 5", "Ben", "rehearse, rollback", "y")]):
    y = 44 + i * 50
    rr_how.box(12, y, 736, 42, None, f, rx=4)
    rr_how.text(20, y + 27, r, "t-head", anchor="start", size=14)
    rr_how.text(390, y + 27, li, anchor="start", size=14)
    rr_how.text(480, y + 27, o, anchor="start", size=14)
    rr_how.text(580, y + 27, a, anchor="start", size=13)
rr_how.box(12, 254, 736, 50, "+ 8 more · reviewed every fortnight, 15 minutes", "paper", size=15)
rr_how.note(380, 344, "each risk: owner, action, date to look again", "pen", size=16)

RISKS = dict(
    slug="risk-register",
    kicker="a.k.a. “the captain's list of dangers”",
    tldr="A <b>risk register</b> is a short list of the things that could go wrong, each with <b>likelihood</b> and <b>impact</b>, an <b>owner</b>, <b>actions</b> that reduce it, and a <b>date to look again</b>. Keep it small (ten to fifteen), review it briefly and often, and close risks when they're gone. It turns worries raised in meetings into work someone owns, and shows leaders the few things that could really hurt.",
    chips=[("Family", "risk &amp; transition"), ("Origin", "project and enterprise risk management (ISO 31000)"), ("Lives in", "one page reviewed every fortnight"), ("Pairs with", "risk-storming, failure mode analysis, migration planning")],
    problem_side="Larder, 24 April 2028",
    problem="""  <p class="lead">The 2028 plan has <b>Ghent</b> opening in June, <b>Haarlem</b> in September, <b>Ordering's database split</b>, Larder Plus growing fast, and <b>Ana as the only architect</b>. Risks come up in every meeting, get nodded at, and vanish. <span class="hl-pink">The last list is a wall photo from the December 2025 risk-storm.</span></p>
  <ul>
    <li>Risks without owners don't get reduced.</li>
    <li>Old lists go stale; new risks go unlisted.</li>
    <li>Leaders hear about risks only when they happen.</li>
  </ul>""",
    problem_figs=[rr_problem],
    analogy_side="the captain's list of dangers",
    analogy="""  <p>On the chart table a captain keeps a <b>list of dangers</b>: shallows ahead, a storm forecast, a tired crew. Each has <b>how likely</b>, <b>how bad</b>, <b>what we're doing</b>, and <b>who's watching it</b>. It's read <b>every watch</b>, and crossed off when the ship is past.</p>""",
    analogy_figs=[rr_analogy],
    map=[("Shallows ahead", "The Ordering split corrupting orders"),
         ("A tired crew", "Ana as the only architect"),
         ("Who's watching", "An owner per risk"),
         ("Read every watch", "Fifteen minutes every fortnight"),
         ("Crossed off when past", "Risks closed after Ghent opened")],
    how_side="likelihood, impact, owner, action, date",
    how="""  <p>Ana started a register with <b>twelve risks</b>, scored 1–5 for likelihood and impact, each with an <b>owner</b>, <b>actions</b> and a <b>review date</b>. Top: <b>Ana as a single point of failure</b> (4 × 4; grow two more architects by September); <b>Ghent's fit-out late</b> (3 × 4, Joost; weekly builder check); <b>Plus orders beating Friday capacity</b> (3 × 3, Eli); the <b>Ordering split corrupting orders</b> (2 × 5, Ben; rehearse, keep rollback two weeks). Fifteen minutes every fortnight; the top five go into Femke's monthly report.</p>""",
    how_figs=[rr_how],
    steps=[("List the risks", "From the plan, risk-storms, incidents, people."),
           ("Score likelihood and impact", "1–5 each; impact in the business's terms."),
           ("Give each an owner", "Someone who can act on it."),
           ("Write the actions", "Reduce likelihood, reduce impact, or accept."),
           ("Review briefly and often", "Fortnightly, fifteen minutes."),
           ("Close and report", "Close what's past; top five to leaders.")],
    vocab=[("Risk", "Something that might happen and would hurt a goal."),
           ("Likelihood", "How probable it is."),
           ("Impact", "How bad it would be."),
           ("Mitigation", "An action that reduces likelihood or impact."),
           ("Risk owner", "The person responsible for watching and acting."),
           ("Single point of failure", "One part (or person) whose loss stops everything.")],
    code=dict(file="planning/risk-register-2028.md", note="the top of the register, 24 April 2028", plain=True, src="""
# Risk register 2028 · reviewed every other Monday, 15 min · top 5 to Femke monthly

| # | Risk                                          | L | I | Owner | Actions                                   | Review |
|---|-----------------------------------------------|---|---|-------|-------------------------------------------|--------|
| 1 | Architecture depends on one person (Ana)       | 4 | 4 | Ana   | grow 2 architects (Cho, Dee) by Sep; principles, guardrails | 8 May |
| 2 | Ghent store fit-out late (opening 19 Jun)      | 3 | 4 | Joost | weekly check with builder; fallback: van from Antwerp | 1 May |
| 3 | Plus orders exceed Friday capacity             | 3 | 3 | Eli   | monthly capacity plan; Plus slots capped at 30 % | 8 May |
| 4 | Ordering split corrupts orders during switch   | 2 | 5 | Ben   | rehearse per city; compare counts; rollback 2 wks | 22 May |
| 5 | Haarlem date (Sep) slips past the board plan   | 2 | 3 | Sanne | city playbook; config only (ADR 0003)     | 5 Jun  |
… 7 more · closed this year: 0
"""),
    tools="tools: a one-page table in the docs or planning tool, a fortnightly slot, the monthly leadership report.",
    gains=["<b>Owned risks</b>, actually reduced.",
           "<b>New risks</b> listed early.",
           "<b>Leaders see</b> the few that matter.",
           "<b>People risks</b> on the list too.",
           "<b>Closed risks</b> show progress."],
    losses=["<b>Scores are judgments</b>.",
            "<b>Can become</b> a bureaucratic list.",
            "<b>Fortnightly upkeep</b>.",
            "<b>Uncomfortable</b> to list people risks."],
    baseline="Each line compares <b>risks raised in meetings and forgotten</b> to <b>a short register with scores, owners, actions and fortnightly review</b>.",
    ratings=[(2, 4, "Twelve risks on one page."),
             (2, 4, "Femke sees the top five monthly."),
             (3, 4, "Owners act without waiting."),
             (1, 5, "Risks reduced before they hit."),
             (3, 4, "New risks added each fortnight."),
             (2, 4, "Actions and dates recorded."),
             (3, 3, "Neutral."),
             (3, 3, "Fifteen minutes a fortnight."),
             (3, 4, "Owners in each team.")],
    pitfalls=[("Hundreds of risks", "Every worry listed.", "ten to fifteen that matter."),
              ("No owners", "“The team” owns it.", "one named person."),
              ("Write once", "A list from January.", "fortnightly review."),
              ("Only technical risks", "People and suppliers missing.", "people, suppliers, dates too.")],
    use=["Programmes with several launches or migrations.",
         "When risks keep coming up and nothing changes.",
         "Reporting to leadership.",
         "Before go/no-go decisions."],
    skip=["Small, short pieces of work (a risk-storm is enough)."],
    related=["<b>Risk-storming</b> (vol. 1)", "<b>Failure mode analysis</b> (vol. 5)", "<b>Migration planning</b> (this volume)", "<b>Go-live readiness</b> (this volume)"],
    quiz=[("What does each risk need?", "Likelihood, impact, an owner, actions and a review date."),
          ("What was Larder's top risk?", "Architecture depending on one person, Ana."),
          ("How often is it reviewed?", "Every fortnight, for fifteen minutes."),
          ("Who sees the top five?", "Femke, monthly.")],
    try_it="List the ten things most likely to hurt your next release or quarter. Score each, name an owner who can act, write one action each, and book fifteen minutes every two weeks.",
    remember="Keep the <span class=\"hl\">captain's list</span>, and read it every <span class=\"hl\">watch</span>.",
    sources=["ISO 31000:2018, <i>Risk management — Guidelines</i>.",
             "Tom DeMarco and Timothy Lister, <i>Waltzing with Bears</i> (2003).",
             "Project Management Institute, <i>PMBOK Guide</i>, 7th ed. (2021), risk.",
             "Simon Brown, risk-storming (riskstorming.com)."],
)

# ------------------------------------------------------------------ 09 Migration Planning
mg_problem = Doodle(760, 280, "Doodle of May 2028. Ordering's data must move from Larder Core's shared database to its own, while 30,000 orders a day keep flowing in six cities. The first draft plan is one weekend: copy everything on Saturday night, switch on Sunday, hope. If anything goes wrong on Monday, there's no way back.",
                    "Move Ordering's data while 30,000 orders a day flow. Draft plan: one weekend, and hope.")
mg_problem.box(20, 40, 320, 90, "Sat night", "pink", sub="copy everything")
mg_problem.box(400, 40, 340, 90, "Sun", "pink", sub="switch · no way back", stroke="red")
mg_problem.note(380, 200, "one weekend, one chance", "red", size=20)

mg_analogy = Doodle(760, 250, "Doodle of moving a hospital ward to a new building: not all patients in one night. One room at a time, with the old room kept ready until the new one is proven, and a checklist at each step.",
                     "Moving a hospital ward: one room at a time, the old room kept ready until the new one is proven.")
mg_analogy.icon("bricks", 30, 60, 1.2)
for i, (t, f) in enumerate([("one room", "y"), ("proven", "green"), ("old room ready", "blue")]):
    mg_analogy.box(170 + i * 190, 60, 176, 70, t, f, size=16)
mg_analogy.note(450, 200, "never a night with no way back", "pen")

mg_how = Doodle(760, 420, "Larder's migration plan for the Ordering database, 29 May 2028, five reversible steps. One, expand: new database, change data capture copies every order, checked daily. Two, shadow reads: Ordering reads both and compares, 0.01 percent differences fixed. Three, switch writes city by city, starting with Eindhoven, the smallest; the old database is kept in sync backwards. Four, all six cities, then Ghent and Haarlem born on the new one. Five, contract: stop the backwards sync after two quiet weeks, remove the old tables. Each step: a test, a rollback and a stop point. Done by 21 August.",
                 "Five reversible steps, city by city. Each with a test, a rollback and a stop point.")
for i, (t, s, f) in enumerate([("1 expand", "new DB, CDC", "y"), ("2 shadow", "compare both", "blue"), ("3 one city", "Eindhoven first", "green"),
                               ("4 all cities", "+ Ghent, Haarlem", "green"), ("5 contract", "old removed", "paper")]):
    x = 14 + i * 148
    mg_how.box(x, 14, 138, 100, t, f, sub=s, size=15, subsize=12)
    if i:
        mg_how.arrow(x - 8, 64, x - 2, 64)
mg_how.head(380, 152, "every step:", size=16)
for i, (t, f) in enumerate([("a test", "y"), ("a rollback", "pink"), ("a stop point", "blue")]):
    mg_how.box(14 + i * 248, 170, 236, 60, t, f, size=16)
mg_how.note(380, 272, "backwards sync keeps the old DB current until step 5", "pen", size=15)
mg_how.note(380, 306, "29 May plan → 21 Aug done · 0 orders lost", "green", size=16)

MIGRATION = dict(
    slug="migration-planning",
    kicker="a.k.a. “one room at a time”",
    tldr="<b>Migration planning</b> moves a live system (data, traffic, users) in <b>small, reversible steps</b> instead of one big switch. A common shape: <b>expand</b> (build the new, copy data), <b>shadow</b> (run both, compare), <b>switch in slices</b> (one city, store or customer group at a time), then <b>contract</b> (remove the old once proven). Every step has a <b>test</b>, a <b>rollback</b> and a <b>stop point</b>, so there's never a night with no way back.",
    chips=[("Family", "risk &amp; transition"), ("Origin", "expand/contract (parallel change); strangler fig; database migration practice"), ("Lives in", "a migration plan per move, with each step's test and rollback"), ("Pairs with", "strangler fig migration, transition architectures, expand &amp; contract migrations")],
    problem_side="Larder, 29 May 2028",
    problem="""  <p class="lead">Ordering's data must move from Larder Core's shared database to <b>its own</b> (ADR 0027), while <b>30,000 orders a day</b> keep flowing in six cities. The first draft is one weekend: <b>copy everything on Saturday night, switch on Sunday</b>. <span class="hl-pink">If anything's wrong on Monday, there's no way back.</span></p>
  <ul>
    <li>Big-bang switches turn small mistakes into outages.</li>
    <li>Problems often show only under real traffic.</li>
    <li>Without a rollback, every surprise is a crisis.</li>
  </ul>""",
    problem_figs=[mg_problem],
    analogy_side="moving a hospital ward",
    analogy="""  <p>A hospital moving a ward to a new building doesn't move every patient in one night. It moves <b>one room at a time</b>, keeps the <b>old room ready</b> until the new one is proven, and uses a <b>checklist</b> at each step. There's never a moment when a patient has nowhere to go.</p>""",
    analogy_figs=[mg_analogy],
    map=[("One room at a time", "One city at a time, smallest first"),
         ("The old room kept ready", "Backwards sync to the old database"),
         ("Proving the new room", "Shadow reads comparing both"),
         ("The checklist", "A test, a rollback and a stop point per step"),
         ("Closing the old ward", "Contract: old tables removed after two quiet weeks")],
    how_side="expand, shadow, slice, contract",
    how="""  <p>Ben, Eli and Ana planned <b>five steps</b>. <b>Expand</b>: a new database, change data capture copying every order, checked daily. <b>Shadow</b>: Ordering reads both and compares (0.01 % differences found and fixed). <b>Switch writes city by city</b>, Eindhoven first, with the old database kept in sync <b>backwards</b>. <b>All cities</b>; Ghent and Haarlem are born on the new database. <b>Contract</b> after two quiet weeks. Each step had a <b>test</b>, a <b>rollback</b> and a <b>stop point</b>. Done by <b>21 August</b>, no orders lost.</p>""",
    how_figs=[mg_how],
    steps=[("Choose the slices", "Cities, stores, customer groups: smallest first."),
           ("Expand", "Build the new; copy data continuously."),
           ("Shadow", "Run both; compare results; fix differences."),
           ("Switch slice by slice", "Keep the old in sync backwards."),
           ("Define test, rollback, stop", "For every step, before starting."),
           ("Contract when proven", "Remove the old after quiet weeks.")],
    vocab=[("Expand/contract", "Add the new alongside, then remove the old."),
           ("Change data capture", "Streaming database changes to another system."),
           ("Shadow read", "Reading both old and new and comparing."),
           ("Slice", "A part of traffic or data moved at once."),
           ("Rollback", "Returning to the previous state."),
           ("Stop point", "A moment to decide whether to continue.")],
    code=dict(file="docs/migrations/ordering-db.md", note="the migration plan, 29 May 2028", plain=True, src="""
# Migration: Ordering to its own database (ADR 0027) · owner: Ben · plan 29 May 2028

| Step            | What                                   | Test                       | Rollback                 | Stop if            |
|-----------------|----------------------------------------|----------------------------|--------------------------|--------------------|
| 1 Expand        | new DB; CDC copies orders (5 Jun)      | daily count + checksum     | drop new DB              | lag > 60 s at peak |
| 2 Shadow        | read both, compare (12–26 Jun)         | diff < 0.01 %              | read old only            | diff > 0.1 %       |
| 3 Eindhoven     | writes to new; sync back (3 Jul)       | orders, payments reconcile | flip city flag back      | any lost order     |
| 4 All cities    | Utrecht … Amsterdam last (to 7 Aug)  | same, per city             | flag per city            | P1 incident        |
| 5 Contract      | stop sync back; drop old tables (21 Aug) | two quiet weeks          | (none after this)        | —                  |
Ghent (19 Jun) and Haarlem (Sep) are born on the new database.
Result: done 21 Aug · 0 orders lost · 3 rollbacks used (all in step 2–3, minutes each)
"""),
    tools="tools: change data capture (Debezium or the cloud's own), feature flags per city, comparison jobs, dashboards per slice.",
    gains=["<b>Always a way back</b>.",
           "<b>Problems found</b> in one city, not six.",
           "<b>Real traffic</b> tests each step.",
           "<b>No big weekend</b>.",
           "<b>Calm</b> for operations and support."],
    losses=["<b>Takes weeks</b>, not a weekend.",
            "<b>Two databases</b> to run for a while.",
            "<b>Sync code</b> to build and remove.",
            "<b>Coordination</b> across teams."],
    baseline="Each line compares <b>a one-weekend big-bang switch</b> to <b>expand, shadow, switch city by city and contract, each step reversible</b>.",
    ratings=[(2, 4, "Each step written with its test and rollback."),
             (2, 4, "Joost and Sam knew which city moved when."),
             (3, 4, "Stop points made decisions quick."),
             (1, 5, "Zero orders lost; three quick rollbacks."),
             (2, 4, "Plans changed per city as we learned."),
             (2, 4, "Every step logged in the plan."),
             (3, 3, "Two databases for twelve weeks."),
             (3, 3, "More steps, more coordination."),
             (2, 4, "Ben's team ran it.")],
    pitfalls=[("Big bang", "Everything Saturday night.", "slices, smallest first."),
              ("No rollback", "“We'll fix forward.”", "a way back for every step."),
              ("Skipping shadow", "Differences found by customers.", "compare before switching."),
              ("Never contracting", "Old tables forever.", "remove them when proven.")],
    use=["Moving data between databases or systems.",
         "Replacing a system with live traffic.",
         "Splitting a monolith's database.",
         "Changing providers (payments, hosting)."],
    skip=["Systems you can take offline with no harm."],
    related=["<b>Strangler fig migration</b> (vol. 4)", "<b>Transition architectures</b> (vol. 4)", "<b>Expand &amp; contract migrations</b> (patterns, Vol. 3)", "<b>Change data capture</b> (patterns, Vol. 3)"],
    quiz=[("What are the four phases?", "Expand, shadow, switch in slices, contract."),
          ("What does every step need?", "A test, a rollback and a stop point."),
          ("Which city moved first, and why?", "Eindhoven, the smallest, to limit any harm."),
          ("How did Ghent and Haarlem fit?", "They were born on the new database.")],
    try_it="Take a migration you're facing. Split it into slices, smallest first, and write each step's test, rollback and stop condition in a table before you start.",
    remember="Move the ward <span class=\"hl\">one room</span> at a time; keep the <span class=\"hl\">old room</span> ready.",
    sources=["Danilo Sato, “Parallel Change” (martinfowler.com, 2014).",
             "Martin Fowler, “Strangler Fig Application” (2004, updated 2019).",
             "Pramod Sadalage and Scott Ambler, <i>Refactoring Databases</i> (2006).",
             "Sam Newman, <i>Monolith to Microservices</i> (2019)."],
)

# ------------------------------------------------------------------ 10 Go-Live Readiness
gl_problem = Doodle(760, 280, "Doodle of June 2028. Ghent opens on 19 June, Larder's seventh city and second in Belgium. A week before, the go-live meeting is a round of “we're fine”: each team reports green on its own part. Nobody has agreed what ready means, and the last two city launches each had a surprise on day one.",
                    "Ghent in a week. Every team says “we're fine”. Nobody has agreed what “ready” means.")
gl_problem.box(20, 40, 320, 90, "every team", "green", sub="“we're fine”")
gl_problem.box(400, 40, 340, 90, "last two launches", "pink", sub="a day-one surprise each")
gl_problem.note(380, 200, "green by opinion", "red", size=20)

gl_analogy = Doodle(760, 250, "Doodle of a pilot's pre-take-off checklist: each item read aloud and confirmed by looking, not by memory. Agreed long before the flight; if any item fails, the plane doesn't go, whoever is in a hurry.",
                     "A pre-take-off checklist: agreed in advance, confirmed by looking, and any failed item stops the plane.")
gl_analogy.icon("check", 40, 60, 1.3)
for i, (t, f) in enumerate([("agreed early", "y"), ("by looking", "blue"), ("any fail: wait", "pink")]):
    gl_analogy.box(170 + i * 190, 60, 176, 70, t, f, size=15)
gl_analogy.note(450, 200, "not by memory, not by hurry", "pen")

gl_how = Doodle(760, 400, "Ghent's readiness criteria, agreed on 12 June 2028, a week before the go or no-go call on 16 June. Each criterion with evidence, not opinion. Store configured from the city playbook, checked by a test order end to end. Load: 3 times expected orders on the new Ordering database. Payments: Bancontact live in production with a real 1-euro order. Picker app offline mode tested in the store. Rules: age checks set to 16 and 18. Support macros in Dutch. On-call and rollback rehearsed. One criterion was red on 16 June: Dutch help pages. Fixed by the 18th; go.",
                 "Criteria agreed a week before, evidence for each, one red fixed in time. Go.")
for i, (t, f) in enumerate([("test order end to end", "green"), ("3× load on new DB", "green"), ("Bancontact: real €1", "green"), ("picker offline in store", "green"),
                            ("age rules 16 / 18", "green"), ("Dutch support macros", "green"), ("on-call + rollback", "green"), ("Dutch help pages", "pink")]):
    r, c = divmod(i, 2)
    gl_how.box(14 + c * 372, 14 + r * 60, 360, 50, t, f, size=14, rx=6, stroke="red" if f == "pink" else "")
gl_how.note(380, 282, "16 Jun: one red · fixed 18 Jun · go", "pen", size=16)
gl_how.note(380, 318, "19 Jun: Ghent opens, no day-one surprise", "green", size=16)

GOLIVE = dict(
    slug="go-live-readiness",
    kicker="a.k.a. “the pre-take-off checklist”",
    tldr="<b>Go-live readiness</b> means agreeing, well before the date, what <b>ready</b> means (criteria for the product, the platform, operations, support and rollback), checking each with <b>evidence</b> rather than opinion, and making a clear <b>go / no-go</b> decision with named decision makers. If a criterion is red, you fix it, accept it in writing, or wait. It turns a round of “we're fine” into a decision.",
    chips=[("Family", "risk &amp; transition"), ("Origin", "operational readiness reviews; aviation checklists"), ("Lives in", "a readiness checklist per launch and a go/no-go meeting"), ("Pairs with", "launch checklist (Grace), risk register, handover to operations")],
    problem_side="Larder, 12 June 2028",
    problem="""  <p class="lead"><b>Ghent</b> opens on <b>19 June</b>, Larder's seventh city and second in Belgium. A week before, the go-live meeting is a round of <b>“we're fine”</b>: each team reports green on its own part. <span class="hl-pink">Nobody has agreed what ready means</span>, and the last two city launches each had a surprise on day one.</p>
  <ul>
    <li>Each team checks its own part; nobody checks the whole.</li>
    <li>“Green” by opinion hides untested things.</li>
    <li>Without criteria, go/no-go becomes a mood.</li>
  </ul>""",
    problem_figs=[gl_problem],
    analogy_side="the pre-take-off checklist",
    analogy="""  <p>Before take-off a pilot reads a <b>checklist</b>: each item read aloud and <b>confirmed by looking</b>, not by memory. It was <b>agreed long before</b> the flight, and if any item fails, the plane doesn't go, however late it's running.</p>""",
    analogy_figs=[gl_analogy],
    map=[("The checklist", "Ghent's readiness criteria"),
         ("Confirmed by looking", "A real €1 Bancontact order, a test order end to end"),
         ("Agreed before the flight", "Criteria agreed a week before the go/no-go"),
         ("Any item fails", "Dutch help pages red on 16 June"),
         ("Take-off", "Ghent opening on 19 June")],
    how_side="criteria early, evidence for each, a clear decision",
    how="""  <p>Ana and Sanne agreed <b>criteria</b> a week before the go/no-go call, each needing <b>evidence</b>: a test order end to end in the configured store; <b>3× expected load</b> on the new Ordering database; <b>Bancontact</b> live with a real €1 order; picker offline mode tested in the store; age rules set to 16 and 18; Dutch support macros; on-call and rollback rehearsed. On <b>16 June</b> one was red: Dutch help pages. Fixed by the 18th; <b>go</b>. Ghent opened on 19 June with no day-one surprise.</p>""",
    how_figs=[gl_how],
    steps=[("Agree criteria early", "Product, platform, operations, support, rollback."),
           ("Require evidence", "A test, a real transaction, a rehearsal."),
           ("Name the decision makers", "Who says go or no-go."),
           ("Check a few days before", "Time to fix reds."),
           ("Decide clearly", "Go, go with accepted risks in writing, or wait."),
           ("Review after launch", "Update the criteria for next time.")],
    vocab=[("Readiness criteria", "What must be true to go live."),
           ("Go / no-go", "The decision to launch or wait."),
           ("Evidence", "Proof that a criterion is met."),
           ("Accepted risk", "A known gap, accepted in writing by a named person."),
           ("Operational readiness", "Operations and support prepared to run it."),
           ("Dress rehearsal", "A full practice run.")],
    code=dict(file="launches/ghent/readiness.md", note="the readiness checklist, 16 June 2028", plain=True, src="""
# Ghent go-live readiness · go/no-go 16 Jun 2028 · opening 19 Jun · deciders: Joost, Priya, Ana

| Area      | Criterion                                         | Evidence                              | Status |
|-----------|---------------------------------------------------|---------------------------------------|--------|
| Product   | store, zones, slots, prices from playbook (config) | test order end to end, 14 Jun         | green  |
| Platform  | 3× expected orders on the new Ordering DB          | load test 13 Jun, p95 590 ms          | green  |
| Payments  | Bancontact live in production                      | real €1 order, refunded               | green  |
| Store     | picker app offline mode                            | Wi-Fi pulled for 20 min, 15 Jun       | green  |
| Rules     | age checks 16/18 (BE)                              | city setting + courier app test       | green  |
| Support   | Dutch macros and help pages                        | macros ✓ · help pages missing         | RED → fixed 18 Jun |
| Run       | on-call, rollback (city flag) rehearsed            | rehearsal 15 Jun                      | green  |
Decision 16 Jun: GO, on condition help pages live by 18 Jun (owner: Sam) · met
"""),
    tools="tools: a readiness checklist template, test orders and real payments in production, rehearsals, a short go/no-go meeting.",
    gains=["<b>Ready by evidence</b>, not opinion.",
           "<b>The whole checked</b>, not just parts.",
           "<b>Reds found</b> with time to fix.",
           "<b>A clear decision</b> with named owners.",
           "<b>Better each launch</b>."],
    losses=["<b>Preparation work</b> before launch.",
            "<b>Real tests</b> in production need care.",
            "<b>A no-go</b> can be unpopular.",
            "<b>Checklists can grow</b> too long."],
    baseline="Each line compares <b>a round of “we're fine” before launch</b> to <b>criteria agreed early, evidence for each, and a clear go/no-go</b>.",
    ratings=[(2, 5, "One page: criteria, evidence, status."),
             (2, 4, "Joost, Priya and Ana decided together."),
             (2, 4, "A short meeting with a clear answer."),
             (1, 5, "The red found three days before opening."),
             (3, 4, "Criteria improved after each launch."),
             (2, 5, "Evidence recorded per criterion."),
             (3, 3, "Neutral."),
             (3, 3, "A week of checks."),
             (3, 4, "Teams produce their own evidence.")],
    pitfalls=[("Green by opinion", "“We're fine.”", "evidence per criterion."),
              ("Criteria the day before", "No time to fix reds.", "agree a week or more ahead."),
              ("Parts, not the whole", "Each team checks itself.", "an end-to-end test order."),
              ("Nobody decides", "A mood, not a decision.", "named deciders.")],
    use=["City or market launches.",
         "Big migrations' switch days.",
         "New products and client go-lives.",
         "Any launch that's had day-one surprises."],
    skip=["Small, flag-protected releases (the flag is the rollback)."],
    related=["<b>Launch checklist</b> (Grace, book 2 vol. 3)", "<b>Risk register</b> (this volume)", "<b>Handover to operations</b> (this volume)", "<b>Launching a new city</b> (Grace, book 2 vol. 6)"],
    quiz=[("What makes a criterion trustworthy?", "Evidence: a test, a real transaction, a rehearsal."),
          ("When were Ghent's criteria agreed?", "A week before the go/no-go call."),
          ("What was red on 16 June?", "Dutch help pages; fixed by the 18th."),
          ("What are the decision options?", "Go, go with accepted risks in writing, or wait.")],
    try_it="For your next launch, write eight readiness criteria across product, platform, operations, support and rollback, with the evidence each needs. Name who decides, and check them three days early.",
    remember="Read the <span class=\"hl\">checklist</span> aloud; any red keeps the plane on the <span class=\"hl\">ground</span>.",
    sources=["Atul Gawande, <i>The Checklist Manifesto</i> (2009).",
             "Betsy Beyer et al., <i>The Site Reliability Workbook</i> (2018), launch reviews.",
             "Google SRE, “Reliable Product Launches at Scale” (SRE book, 2016).",
             "AWS, “Operational Readiness Reviews” (Well-Architected guidance)."],
)

# ------------------------------------------------------------------ 11 Handover to Operations
ho_problem = Doodle(760, 280, "Doodle of September 2028. The Ordering database split is done, and Ben's team wants to move on to Grace's next bets. From October the new reliability team will run Ordering on call. Last time a system changed hands, Dispatch in 2026, the runbook was a wiki page from the build, and the first incident took four hours because nobody knew the failover.",
                    "Ben's team moves on; the reliability team takes Ordering on call. Last handover: a stale wiki page and a four-hour incident.")
ho_problem.box(20, 40, 320, 90, "Ben's team", "y", sub="on to the next bets")
ho_problem.box(400, 40, 340, 90, "last time (Dispatch)", "pink", sub="first incident: 4 hours")
ho_problem.note(380, 200, "a handover by wiki page", "red", size=20)

ho_analogy = Doodle(760, 250, "Doodle of a nurse's shift handover at the bedside: what's wrong, what's been done, what to watch for, what to do if it happens, and the outgoing nurse stays reachable for the first hours of the next shift.",
                     "A bedside shift handover: what's wrong, what's done, what to watch, what to do, and the outgoing nurse stays reachable.")
ho_analogy.icon("badge", 40, 60, 1.3)
for i, (t, f) in enumerate([("at the bedside", "y"), ("what to watch", "blue"), ("reachable", "green")]):
    ho_analogy.box(170 + i * 190, 60, 176, 70, t, f, size=16)
ho_analogy.note(450, 200, "the patient never notices", "pen")

ho_how = Doodle(760, 400, "Larder's handover of Ordering to the reliability team, from 4 September 2028. Acceptance criteria agreed with the receiving team: runbooks for the top ten alerts, tested; SLOs and dashboards; two game days where the reliability team ran failovers while Ben's team watched; known issues and debt listed; a warranty period of four weeks where Ben's team is second line. On 1 October the reliability team took the pager. First incident, 9 October: a replica lagging; fixed in 18 minutes from the runbook.",
                 "Acceptance criteria set by the receivers, game days, and a warranty period. First incident: 18 minutes.")
for i, (t, s, f) in enumerate([("runbooks", "top 10 alerts, tested", "y"), ("SLOs + dashboards", "agreed with them", "blue"), ("2 game days", "they drive, we watch", "green"),
                               ("known issues", "debt listed", "paper"), ("4-week warranty", "Ben's team second line", "green"), ("1 Oct", "pager handed over", "y")]):
    r, c = divmod(i, 3)
    ho_how.box(14 + c * 248, 14 + r * 110, 236, 96, t, f, sub=s, size=16, subsize=13)
ho_how.note(380, 270, "acceptance criteria set by the receiving team", "pen", size=16)
ho_how.note(380, 306, "9 Oct: replica lag fixed in 18 min from the runbook", "green", size=16)

HANDOVER = dict(
    slug="handover-to-operations",
    kicker="a.k.a. “the bedside shift handover”",
    tldr="When a system passes from the team that built it to the team that will run it, <b>hand it over</b> properly: acceptance criteria <b>set by the receiving team</b> (runbooks tested, alerts and SLOs, dashboards, known issues), <b>practice</b> (game days where the new owners drive), and a <b>warranty period</b> where the builders stay reachable as second line. The receivers take the pager only when they're ready; the customers never notice the change.",
    chips=[("Family", "risk &amp; transition"), ("Origin", "service transition (ITIL); SRE production readiness"), ("Lives in", "a handover checklist owned by the receiving team"), ("Pairs with", "go-live readiness, DR tiers, incident response &amp; postmortems")],
    problem_side="Larder, 4 September 2028",
    problem="""  <p class="lead">The Ordering database split is done; Ben's team wants to move on to Grace's next bets. From October the new <b>reliability team</b> will run Ordering on call. Last time a system changed hands (Dispatch, 2026), the runbook was a <b>wiki page from the build</b>, and the first incident took <b>four hours</b> because nobody knew the failover. <span class="hl-pink">A handover by wiki page.</span></p>
  <ul>
    <li>Builders know things that aren't written down.</li>
    <li>Runbooks written during the build go stale.</li>
    <li>The first incident is a bad time to learn.</li>
  </ul>""",
    problem_figs=[ho_problem],
    analogy_side="the bedside shift handover",
    analogy="""  <p>A good nurse hands over a patient <b>at the bedside</b>: what's wrong, what's been done, <b>what to watch for</b>, what to do if it happens. And the outgoing nurse stays <b>reachable</b> for the first hours of the next shift. The patient never notices the change.</p>""",
    analogy_figs=[ho_analogy],
    map=[("At the bedside", "Game days on the real system"),
         ("What to watch for", "Alerts, SLOs and dashboards"),
         ("What to do if it happens", "Runbooks for the top ten alerts, tested"),
         ("Staying reachable", "A four-week warranty, Ben's team second line"),
         ("The patient never notices", "Customers see no change on 1 October")],
    how_side="receivers' criteria, practice, warranty",
    how="""  <p>The reliability team wrote the <b>acceptance criteria</b>: runbooks for the top ten alerts, <b>tested</b>; SLOs and dashboards they agreed; <b>two game days</b> where they ran failovers while Ben's team watched; known issues and debt listed. Then a <b>four-week warranty</b> with Ben's team as second line. On <b>1 October</b> the reliability team took the pager. First incident, <b>9 October</b>: a lagging replica, fixed in <b>18 minutes</b> from the runbook.</p>""",
    how_figs=[ho_how],
    steps=[("Let the receivers set criteria", "What they need to run it."),
           ("Write and test runbooks", "For the alerts that will actually fire."),
           ("Agree SLOs and dashboards", "With the people who'll watch them."),
           ("Practise with game days", "The new owners drive."),
           ("List known issues", "Debt, quirks, workarounds."),
           ("Give a warranty period", "Builders as second line for weeks.")],
    vocab=[("Handover", "Passing responsibility for a system to another team."),
           ("Runbook", "Steps to diagnose and fix a known problem."),
           ("Game day", "A planned exercise that simulates failures."),
           ("Warranty period", "Time when the builders support the new owners."),
           ("Production readiness", "A system's fitness to be run in production."),
           ("Second line", "The people the first responders escalate to.")],
    code=dict(file="ops/handover/ordering.md", note="the handover checklist, September 2028", plain=True, src="""
# Handover: Ordering (own database) → reliability team · criteria set by the receivers

[x] Runbooks for the top 10 alerts, each tested by the reliability team (12–19 Sep)
[x] SLOs: availability 99.9 %, checkout p95 < 800 ms; dashboards agreed
[x] Game day 1 (14 Sep): database failover, run by reliability, watched by Ben's team
[x] Game day 2 (21 Sep): CDC lag + rollback of a bad deploy
[x] Known issues: 6 listed (TD-31…TD-36), with workarounds
[x] Access, alerts routed, escalation paths
Warranty   1–28 Oct: Ben's team second line · weekly check-in
Pager      reliability team from 1 Oct 2028
First incident 9 Oct: replica lag → runbook R-04 → fixed in 18 min
"""),
    tools="tools: runbooks next to the alerts, SLO dashboards, game-day plans, the on-call tool, a handover checklist.",
    gains=["<b>A smooth first incident</b>.",
           "<b>Knowledge passed on</b>, not lost.",
           "<b>Builders freed</b> for new work.",
           "<b>Receivers confident</b>.",
           "<b>Customers notice nothing</b>."],
    losses=["<b>Weeks of preparation</b>.",
            "<b>Builders' time</b> during the warranty.",
            "<b>Game days</b> carry some risk.",
            "<b>Receivers may push back</b> on gaps."],
    baseline="Each line compares <b>a handover by wiki page</b> to <b>acceptance criteria set by the receivers, game days and a warranty period</b>.",
    ratings=[(2, 4, "Runbooks and known issues written down."),
             (2, 4, "Both teams agreed the criteria."),
             (3, 4, "The pager moved on the planned date."),
             (1, 5, "First incident fixed in 18 minutes."),
             (3, 4, "Second line for four weeks."),
             (2, 4, "Checklist kept with the system."),
             (3, 3, "Neutral."),
             (3, 3, "Weeks of preparation."),
             (2, 4, "Each team owns its part.")],
    pitfalls=[("Builders set the criteria", "“Looks done to us.”", "the receivers decide."),
              ("Untested runbooks", "Written, never tried.", "game days."),
              ("Clean break", "Builders vanish on day one.", "a warranty period."),
              ("Hidden debt", "Quirks discovered at 3 a.m.", "list known issues.")],
    use=["Systems moving from a build team to a run team.",
         "New on-call rotations.",
         "Contractors handing over to staff.",
         "Before builders move to other work."],
    skip=["Teams that build and run their own systems (you build it, you run it)."],
    related=["<b>Go-live readiness</b> (this volume)", "<b>DR tiers</b> (vol. 5)", "<b>Incident response &amp; postmortems</b> (patterns, Vol. 6)", "<b>Handing over a product area</b> (Grace, book 2 vol. 6)"],
    quiz=[("Who sets the acceptance criteria?", "The receiving team."),
          ("What's a game day for?", "Letting the new owners practise failures while the builders watch."),
          ("What's the warranty period?", "Four weeks with the builders as second line."),
          ("How did the first incident go?", "A lagging replica, fixed in 18 minutes from the runbook.")],
    try_it="Pick a system your team built that someone else runs (or will). Ask them what they'd need to be confident, run one game day where they drive, and agree a warranty period.",
    remember="Hand over at the <span class=\"hl\">bedside</span>, and stay <span class=\"hl\">reachable</span>.",
    sources=["Betsy Beyer et al., <i>Site Reliability Engineering</i> (2016), production readiness.",
             "AXELOS, <i>ITIL 4: Service Transition</i> practices (2019).",
             "Jesse Robbins et al., “Resilience Engineering: Learning to Embrace Failure”, ACM Queue (2012), game days.",
             "Susan Fowler, <i>Production-Ready Microservices</i> (2016)."],
)

NOTES = [RISKS, MIGRATION, GOLIVE, HANDOVER]
