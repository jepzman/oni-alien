# Series 2 · The Solution Architect's Notebook · Vol. 6 · Governance.
# Running case study: Larder (facts in docs/larder-casebook.md).

# ------------------------------------------------------------------ 04 Architecture Principles
ap_problem = Doodle(760, 280, "Doodle of April 2028. Larder now has five product teams and thirty engineers, eight of them hired this year. They keep asking Ana the same questions: can we read another module's table? which database? sync call or event? Ana is the bottleneck, and her answers live only in her head and in 26 ADRs nobody new has read.",
                    "Thirty engineers asking Ana the same questions. The answers live in her head and 26 ADRs.")
ap_problem.box(20, 40, 320, 90, "5 teams · 30 engineers", "paper", sub="8 new this year")
ap_problem.box(400, 40, 340, 90, "Ana", "pink", sub="the bottleneck", stroke="red")
ap_problem.note(380, 200, "the same questions, every week", "red", size=20)

ap_analogy = Doodle(760, 250, "Doodle of a family's house rules on the fridge: shoes off at the door, whoever cooks doesn't wash up, screens off at dinner. A babysitter can follow them without phoning the parents.",
                     "House rules on the fridge: the babysitter can follow them without phoning the parents.")
ap_analogy.icon("fridge", 30, 60, 1.2)
for i, (t, f) in enumerate([("shoes off", "y"), ("cook ≠ washer", "blue"), ("screens off", "green")]):
    ap_analogy.box(170 + i * 190, 60, 176, 70, t, f, size=16)
ap_analogy.note(450, 200, "decide alike without asking", "pen")

ap_how = Doodle(760, 420, "Larder's eight architecture principles, agreed with the tech leads on 3 April 2028. Each has a statement, the reason, and what it means in practice. One: a city is configuration, not code. Two: events for facts, APIs for commands. Three: one owner per kind of data; never read another module's tables. Four: protect the critical windows. Five: boring technology by default. Six: cost per order is a feature. Seven: decide one-way doors in writing. Eight: privacy by default. Questions to Ana fell from about fifteen a week to four.",
                 "Eight principles, each with a reason and implications. Questions to Ana: about fifteen a week → four.")
for i, t in enumerate(["a city is configuration", "events for facts, APIs for commands", "one owner per kind of data", "protect the critical windows",
                       "boring technology by default", "cost per order is a feature", "one-way doors in writing", "privacy by default"]):
    r, c = divmod(i, 2)
    ap_how.box(14 + c * 372, 14 + r * 66, 360, 56, f"{i + 1}. {t}", "y" if i % 3 == 0 else ("blue" if i % 3 == 1 else "green"), size=13, rx=6)
ap_how.note(380, 300, "each: statement · reason · implications", "pen", size=16)
ap_how.note(380, 336, "questions to Ana: ≈ 15 a week → 4", "green", size=16)

PRINCIPLES = dict(
    slug="architecture-principles",
    kicker="a.k.a. “the house rules on the fridge”",
    tldr="<b>Architecture principles</b> are a handful (five to ten) of short rules that capture how the organisation builds, each with a <b>statement</b>, the <b>reason</b>, and the <b>implications</b> (what it means you do and don't do). They let teams make consistent decisions <b>without asking</b> the architect, and they make reviews faster because the reasoning is shared. Write them with the people who'll use them, from decisions you've already made, and retire the ones nobody needs.",
    chips=[("Family", "governance"), ("Origin", "TOGAF's principle format (statement, rationale, implications)"), ("Lives in", "one page in the architecture docs, linked from templates and reviews"), ("Pairs with", "guardrails not gates, ADRs, golden paths")],
    problem_side="Larder, 3 April 2028",
    problem="""  <p class="lead">Larder now has <b>five product teams</b> and <b>thirty engineers</b>, eight hired this year. They keep asking Ana the same questions: can we read another module's table? which database? sync call or event? <span class="hl-pink">Ana is the bottleneck</span>, and her answers live only in her head and in <b>26 ADRs</b> nobody new has read.</p>
  <ul>
    <li>One architect can't answer for thirty engineers.</li>
    <li>ADRs record decisions, not the rules behind them.</li>
    <li>New people repeat old mistakes.</li>
  </ul>""",
    problem_figs=[ap_problem],
    analogy_side="the house rules on the fridge",
    analogy="""  <p>A family's <b>house rules</b> hang on the fridge: shoes off at the door, whoever cooks doesn't wash up, screens off at dinner. A <b>babysitter</b> can follow them without phoning the parents, and the reasons are obvious enough that nobody argues.</p>""",
    analogy_figs=[ap_analogy],
    map=[("The fridge", "One page in the architecture docs"),
         ("Shoes off at the door", "One owner per kind of data"),
         ("The babysitter", "A new engineer in week two"),
         ("Not phoning the parents", "Deciding without asking Ana"),
         ("The obvious reasons", "Each principle's rationale, from real ADRs")],
    how_side="eight rules, each with a reason and implications",
    how="""  <p>Ana drafted <b>eight principles</b> from 26 ADRs and agreed them with the tech leads: a city is <b>configuration</b>; <b>events for facts, APIs for commands</b>; <b>one owner per kind of data</b>; protect the <b>critical windows</b>; <b>boring technology</b> by default; <b>cost per order</b> is a feature; <b>one-way doors in writing</b>; <b>privacy by default</b>. Each has a reason and implications, and links to its ADRs. The design-note and review templates now ask which principles apply. Questions to Ana fell from about <b>fifteen a week to four</b>.</p>""",
    how_figs=[ap_how],
    steps=[("Mine your decisions", "ADRs and incidents show the real rules."),
           ("Write five to ten", "Short statements people can remember."),
           ("Add reason and implications", "Why, and what you do and don't do."),
           ("Agree with the people who'll use them", "Tech leads, product, operations."),
           ("Wire them into templates", "Design notes, reviews, golden paths."),
           ("Review yearly", "Retire, rewrite or add.")],
    vocab=[("Principle", "A rule with a reason that guides decisions."),
           ("Rationale", "Why the principle exists."),
           ("Implication", "What following it means in practice."),
           ("Boring technology", "Proven tools the team knows well."),
           ("Governance", "How decisions are guided and checked."),
           ("Exception", "A recorded, reasoned case of not following a principle.")],
    code=dict(file="docs/architecture/principles.md", note="principle 3 of 8, April 2028", plain=True, src="""
# Larder architecture principles (8) · agreed 3 Apr 2028 · reviewed yearly · owner: Ana

3. One owner per kind of data
   Statement     Every kind of data has one owning module and one master copy.
   Rationale     Shared tables tied seven modules to Core's schema (2025–26); 212 products
                 disagreed across systems before Antwerp (ADR 0024).
   Implications  - Never read or write another module's tables (FF-11 checks it).
                 - Get data from the owner's events or API; keep a local copy if needed.
                 - New data: name the owner in the design note before building.
   ADRs          0002, 0023, 0024, 0027
   Exceptions    recorded in an ADR; reviewed at the yearly principles review
"""),
    tools="tools: one page in the docs, the TOGAF statement/rationale/implications format, links from design-note and review templates, fitness functions for the checkable ones.",
    gains=["<b>Consistent decisions</b> without asking.",
           "<b>Faster onboarding</b>.",
           "<b>Shorter reviews</b>: shared reasoning.",
           "<b>The architect isn't the bottleneck</b>.",
           "<b>Some principles become checks</b>."],
    losses=["<b>Vague principles</b> are useless.",
            "<b>Rules can harden</b> into dogma.",
            "<b>Exceptions</b> need a process.",
            "<b>A yearly review</b> to keep them true."],
    baseline="Each line compares <b>answers living in the architect's head and old ADRs</b> to <b>eight principles with reasons and implications, wired into templates</b>.",
    ratings=[(2, 5, "Eight rules on one page."),
             (2, 5, "Agreed with all five tech leads."),
             (2, 5, "Teams decide without waiting."),
             (2, 4, "Old mistakes not repeated."),
             (3, 4, "Reviewed and changed yearly."),
             (2, 4, "Each principle links its ADRs."),
             (3, 4, "Cost per order is principle 6."),
             (2, 4, "One page, read once."),
             (1, 5, "Teams decide alike, alone.")],
    pitfalls=[("Platitudes", "“We value quality.”", "a rule you could break, with implications."),
              ("Too many", "Thirty principles.", "five to ten."),
              ("No reasons", "Rules without why.", "a rationale from real decisions."),
              ("Carved in stone", "Never revisited.", "yearly review, recorded exceptions.")],
    use=["Growing teams where the architect becomes a bottleneck.",
         "Onboarding many new engineers.",
         "Before replacing reviews with guardrails.",
         "When decisions are inconsistent across teams."],
    skip=["One small team that decides together daily."],
    related=["<b>Guardrails not gates</b> (this volume)", "<b>Architecture decision records</b> (vol. 2)", "<b>Writing product principles</b> (Grace, book 2 vol. 6)", "<b>Fitness functions</b> (vol. 1)"],
    quiz=[("What three parts does each principle have?", "Statement, rationale and implications."),
          ("Where did Larder's principles come from?", "26 ADRs and past incidents, agreed with the tech leads."),
          ("What changed after they were agreed?", "Questions to Ana fell from about fifteen a week to four."),
          ("How do principles stay true?", "A yearly review, with recorded exceptions.")],
    try_it="Read your last ten architecture decisions and write the three rules behind them as principles: statement, reason, implications. Show them to two team leads and ask which they'd follow without asking you.",
    remember="Put the <span class=\"hl\">house rules</span> on the fridge, so nobody has to phone the <span class=\"hl\">parents</span>.",
    sources=["The Open Group, <i>TOGAF Standard</i>, “Architecture Principles” (format: statement, rationale, implications).",
             "Dan McKinley, “Choose Boring Technology” (2015).",
             "Gregor Hohpe, <i>The Software Architect Elevator</i> (2020).",
             "Eltjo Poort, “Architecture principles” (writing, 2010s)."],
)

# ------------------------------------------------------------------ 05 Guardrails Not Gates
gn_problem = Doodle(760, 280, "Doodle of April 2028. Since 2026 every significant change passes Ana's architecture review board, every other Thursday. With five teams the queue is two weeks long; teams wait, or quietly skip it. Most reviewed changes are reversible and get waved through; the board catches almost nothing a check couldn't.",
                    "Every change through Ana's board: a two-week queue, mostly waved through, sometimes quietly skipped.")
gn_problem.box(20, 40, 320, 90, "review board", "paper", sub="every other Thursday")
gn_problem.box(400, 40, 340, 90, "2-week queue", "pink", sub="waved through · or skipped", stroke="red")
gn_problem.note(380, 200, "a gate everyone queues at, and few need", "red", size=19)

gn_analogy = Doodle(760, 250, "Doodle of a mountain road: instead of a checkpoint every kilometre where a guard inspects each car, there are guardrails along the edge and a few signs. Drivers go at their own speed; the guardrails stop the ones who'd go over. A checkpoint only at the border.",
                     "A mountain road: guardrails along the edge, not a checkpoint every kilometre. A checkpoint only at the border.")
gn_analogy.icon("traffic", 30, 60, 1.2)
gn_analogy.box(150, 50, 280, 100, "checkpoint per km", "pink", sub="everyone waits")
gn_analogy.box(460, 50, 280, 100, "guardrails", "green", sub="everyone drives")
gn_analogy.note(450, 210, "a checkpoint only at the border", "pen")

gn_how = Doodle(760, 400, "Larder's switch from gates to guardrails, 17 April 2028. Automated guardrails on every change: the nine fitness functions, policy checks on infrastructure (EU regions only, encryption on, tags present), the golden-path templates, and a cost alert. Human review only for one-way doors: new data stores, new external vendors, new trust boundaries, changes to the published events. The board was replaced by a lightweight review on request. Waiting time for teams: two weeks to zero for most changes; three to five days for one-way doors.",
                 "Automate the checks; review only the one-way doors. Most changes: two weeks of waiting → none.")
gn_how.head(194, 30, "guardrails (automatic)", size=16)
for i, t in enumerate(["9 fitness functions", "policy as code", "golden-path templates", "cost alerts"]):
    gn_how.box(14, 44 + i * 52, 360, 44, t, "green", size=14)
gn_how.head(566, 30, "reviews (one-way doors)", size=16)
for i, t in enumerate(["new data store", "new vendor", "new trust boundary", "published events"]):
    gn_how.box(386, 44 + i * 52, 360, 44, t, "y", size=14)
gn_how.box(14, 262, 360, 60, "most changes", "blue", sub="2 weeks → 0 waiting", size=16)
gn_how.box(386, 262, 360, 60, "one-way doors", "blue", sub="3–5 days", size=16)
gn_how.note(380, 362, "the board replaced by a lightweight review on request", "pen", size=15)

GUARDRAILS = dict(
    slug="guardrails-not-gates",
    kicker="a.k.a. “guardrails on the mountain road”",
    tldr="<b>Gates</b> stop every change for a human check; with many teams they become queues people wait at or skip. <b>Guardrails</b> are automated checks and good defaults that keep every change within safe limits while teams move at their own speed: fitness functions, policy as code, templates, alerts. Keep <b>human review only for one-way doors</b> (new data stores, vendors, trust boundaries, public contracts), and make that review fast.",
    chips=[("Family", "governance"), ("Origin", "DevOps and platform engineering practice; “guardrails, not gates” (e.g. Thoughtworks Technology Radar)"), ("Lives in", "CI checks, policy as code, templates and a short list of review triggers"), ("Pairs with", "architecture principles, fitness functions, golden paths, lightweight review")],
    problem_side="Larder, 17 April 2028",
    problem="""  <p class="lead">Since 2026 every significant change goes through Ana's <b>architecture review board</b>, every other Thursday. With five teams the queue is <b>two weeks long</b>; teams wait, or quietly skip it. Most reviewed changes are reversible and get waved through; <span class="hl-pink">the board catches almost nothing a check couldn't</span>.</p>
  <ul>
    <li>Gates slow everyone to catch a few.</li>
    <li>Long queues teach people to go around them.</li>
    <li>Humans checking routine rules miss things machines don't.</li>
  </ul>""",
    problem_figs=[gn_problem],
    analogy_side="the mountain road",
    analogy="""  <p>A mountain road doesn't put a <b>checkpoint every kilometre</b> where a guard inspects each car. It has <b>guardrails</b> along the edge and a few signs; drivers go at their own speed, and the guardrails stop the ones who'd go over. There's a checkpoint only at the <b>border</b>.</p>""",
    analogy_figs=[gn_analogy],
    map=[("A checkpoint every kilometre", "The review board for every change"),
         ("Guardrails along the edge", "Fitness functions, policy as code, alerts"),
         ("Signs", "Principles and golden-path templates"),
         ("The border checkpoint", "Review only for one-way doors"),
         ("Driving at your own speed", "Most changes ship without waiting")],
    how_side="automate the checks, review the one-way doors",
    how="""  <p>Ana and Eli turned the board's routine questions into <b>guardrails</b> on every change: the nine <b>fitness functions</b>, <b>policy as code</b> on infrastructure (EU regions only, encryption on, tags present), the <b>golden-path templates</b>, and cost alerts. Human review stays only for <b>one-way doors</b>: a new data store, a new vendor, a new trust boundary, a change to published events. The board was replaced by a <b>lightweight review on request</b>. Waiting: <b>two weeks to none</b> for most changes; three to five days for one-way doors.</p>""",
    how_figs=[gn_how],
    steps=[("List what the gate checks", "Every question the board asks."),
           ("Automate the routine ones", "Fitness functions, policy as code, templates."),
           ("Define the one-way doors", "The few changes that still need people."),
           ("Make that review fast", "Written-first, days not weeks."),
           ("Remove the gate", "Announce what replaced it."),
           ("Watch what slips through", "Add a guardrail when something does.")],
    vocab=[("Gate", "A required human approval before a change proceeds."),
           ("Guardrail", "An automatic limit or default that keeps changes safe."),
           ("Policy as code", "Rules written as code and checked automatically."),
           ("Review trigger", "A kind of change that needs human review."),
           ("Lead time", "Time from idea or commit to production."),
           ("Paved road", "The supported, easy way to do something.")],
    code=dict(file="docs/architecture/governance.md", note="what replaced the board, April 2028", plain=True, src="""
# How architecture is governed at Larder · from 17 Apr 2028

GUARDRAILS (every change, automatic)
  Fitness functions FF-01 … FF-12 in CI and production
  Policy as code (infrastructure): EU regions only · encryption at rest · cost tags · no public buckets
  Golden-path templates: logging, metrics, SLOs, data class, deploy pipeline built in
  Alerts: cost per 1,000 orders, new external domains called from production

REVIEW TRIGGERS (one-way doors → lightweight review, 3–5 days)
  a new data store · a new external vendor or SaaS · a new trust boundary ·
  a change to a published event or public API · leaving a principle (exception)

Everything else: decide in the team, record an ADR if it's significant.
"""),
    tools="tools: CI fitness functions, policy as code (Open Policy Agent, cloud policies), service templates, cost and dependency alerts, a request form for reviews.",
    gains=["<b>No queue</b> for most changes.",
           "<b>Checks every change</b>, not just reviewed ones.",
           "<b>People's time</b> on the hard decisions.",
           "<b>Nobody goes around</b> the process.",
           "<b>Teams own</b> their decisions."],
    losses=["<b>Building guardrails</b> takes effort.",
            "<b>Some things slip</b> until a guardrail exists.",
            "<b>Policy code</b> to maintain.",
            "<b>Less visibility</b> for the architect."],
    baseline="Each line compares <b>a review board for every change</b> to <b>automated guardrails on every change and fast human review only for one-way doors</b>.",
    ratings=[(2, 4, "Teams know exactly what triggers a review."),
             (2, 4, "Tech leads agreed the triggers."),
             (1, 5, "Two weeks of waiting gone."),
             (2, 4, "Every change checked, automatically."),
             (2, 4, "Guardrails added as gaps appear."),
             (3, 4, "ADRs and check results recorded."),
             (3, 4, "Cost alerts among the guardrails."),
             (1, 5, "No board meeting every other Thursday."),
             (1, 5, "Teams decide inside the guardrails.")],
    pitfalls=[("Removing the gate first", "Nothing replaces it.", "guardrails before removing the gate."),
              ("Reviewing everything", "One-way doors undefined.", "a short list of triggers."),
              ("Slow reviews", "One-way doors wait weeks.", "written-first, days."),
              ("Flaky guardrails", "Checks ignored when red.", "keep them reliable, or remove them.")],
    use=["Growing organisations with review queues.",
         "When teams go around architecture processes.",
         "Platforms with many teams shipping daily.",
         "After writing principles."],
    skip=["Highly regulated changes that legally need human sign-off (keep those gates, make them fast)."],
    related=["<b>Architecture principles</b> (this volume)", "<b>Lightweight architecture review</b> (this volume)", "<b>Golden paths</b> (this volume)", "<b>Fitness functions</b> (vol. 1)"],
    quiz=[("What's the difference between a gate and a guardrail?", "A gate stops changes for human approval; a guardrail automatically keeps changes within safe limits."),
          ("What still gets human review at Larder?", "One-way doors: new data stores, vendors, trust boundaries, published events."),
          ("What did waiting time become?", "None for most changes; three to five days for one-way doors."),
          ("What happens when something slips through?", "A new guardrail is added.")],
    try_it="List every question your architecture review asks. Mark which could be an automated check, write one this month, and define the three kinds of change that still need a person.",
    remember="<span class=\"hl\">Guardrails</span> on the road; a <span class=\"hl\">checkpoint</span> only at the border.",
    sources=["Thoughtworks Technology Radar, “Guardrails over gates” themes (2010s–2020s).",
             "Nicole Forsgren, Jez Humble and Gene Kim, <i>Accelerate</i> (2018), change approval.",
             "Open Policy Agent documentation.",
             "Neal Ford et al., <i>Building Evolutionary Architectures</i>, 2nd ed. (2022)."],
)

# ------------------------------------------------------------------ 06 Lightweight Architecture Review
lr_problem = Doodle(760, 280, "Doodle of May 2028. The first one-way-door review under the new rules: the business team wants a new search database for the product catalogue. The old board would have taken two weeks and a 30-slide presentation. Without a format, the new review risks being a hallway chat that nobody records.",
                    "The first one-way door under the new rules: a new search database. Two-week board, or a hallway chat?")
lr_problem.box(20, 40, 320, 90, "old board", "paper", sub="2 weeks · 30 slides")
lr_problem.box(400, 40, 340, 90, "hallway chat", "pink", sub="nothing recorded")
lr_problem.note(380, 200, "neither is a review", "red", size=20)

lr_analogy = Doodle(760, 250, "Doodle of a paper's peer review: the author writes it down first, reviewers read it before meeting, comment in the margins, and the editor gives one of three outcomes: accept, revise, reject. Short, written, with a clear answer.",
                     "Peer review: written first, read before meeting, comments in the margin, one of three outcomes.")
lr_analogy.icon("book", 40, 60, 1.3)
for i, (t, f) in enumerate([("accept", "green"), ("revise", "y"), ("reject", "pink")]):
    lr_analogy.box(170 + i * 190, 60, 176, 70, t, f, size=16)
lr_analogy.note(450, 200, "written first, clear answer", "pen")

lr_how = Doodle(760, 400, "Larder's lightweight review from 15 May 2028. One: the team writes a draft ADR with options, using the principles. Two: two reviewers, Ana and a tech lead from another team, comment in writing within three days. Three: a 45-minute call only if needed. Four: one of three outcomes: go, go with changes, or not yet with what's missing. First case: the search database. Outcome: go with changes: use the managed search service in the EU region, feed it from catalogue events, add it to the DR tiers as tier 2.",
                 "Written first, two reviewers, 45 minutes if needed, three possible outcomes. Days, not weeks.")
for i, (t, s, f) in enumerate([("draft ADR", "options + principles", "y"), ("2 reviewers", "written, 3 days", "blue"), ("45 min", "only if needed", "paper"), ("outcome", "go · changes · not yet", "green")]):
    lr_how.box(14 + i * 184, 14, 174, 90, t, f, sub=s, size=16, subsize=13)
lr_how.box(14, 126, 732, 70, None, "green")
lr_how.head(380, 154, "search database: go with changes", size=16)
lr_how.text(380, 182, "managed, EU region · fed by catalogue events · DR tier 2", size=14)
lr_how.note(380, 236, "four working days from draft to decision", "pen", size=16)
lr_how.note(380, 270, "reviewer rotation: every tech lead reviews twice a quarter", "green", size=15)

REVIEW = dict(
    slug="lightweight-review",
    kicker="a.k.a. “peer review, not a tribunal”",
    tldr="A <b>lightweight architecture review</b> is for decisions that are hard to undo. It's <b>written first</b> (a draft ADR with options), read by <b>two reviewers</b> (the architect and a peer from another team) who comment in writing within days, followed by a short call <b>only if needed</b>, ending in one of <b>three outcomes</b>: go, go with changes, or not yet (with what's missing). Days, not weeks; recorded, not hallway chat.",
    chips=[("Family", "governance"), ("Origin", "ADR review practice; RFC processes; peer review"), ("Lives in", "the ADR pull request and the review triggers list"), ("Pairs with", "guardrails not gates, RFCs and design docs, ADRs")],
    problem_side="Larder, 15 May 2028",
    problem="""  <p class="lead">The first <b>one-way door</b> under the new rules: the business team wants a <b>new search database</b> for the catalogue. The old board would have taken <b>two weeks and thirty slides</b>. Without a format, the new review risks becoming a <span class="hl-pink">hallway chat that nobody records</span>.</p>
  <ul>
    <li>Heavy reviews get avoided.</li>
    <li>Informal reviews leave no record and no clear outcome.</li>
    <li>The architect alone becomes the bottleneck again.</li>
  </ul>""",
    problem_figs=[lr_problem],
    analogy_side="peer review",
    analogy="""  <p>A paper's <b>peer review</b> starts with the author writing it down. Reviewers <b>read it before meeting</b>, comment in the margins, and the editor gives one of <b>three outcomes</b>: accept, revise, reject. Short, written, with a clear answer, and the reasons kept with the paper.</p>""",
    analogy_figs=[lr_analogy],
    map=[("The paper", "A draft ADR with options"),
         ("Reviewers reading first", "Two reviewers, written comments in three days"),
         ("Accept, revise, reject", "Go, go with changes, not yet"),
         ("The editor", "Ana, with a tech lead from another team"),
         ("Kept with the paper", "Comments on the ADR pull request")],
    how_side="written first, two reviewers, three outcomes",
    how="""  <p>The team writes a <b>draft ADR</b> with options and the principles it touches. <b>Two reviewers</b> (Ana and a tech lead from another team) comment <b>in writing within three days</b>; a <b>45-minute call</b> only if needed; then one of <b>three outcomes</b>. The search database got <b>go with changes</b>: the managed search service in the EU region, fed by catalogue events, added to the DR tiers as tier 2. <b>Four working days</b> from draft to decision. Every tech lead now reviews twice a quarter.</p>""",
    how_figs=[lr_how],
    steps=[("Trigger only on one-way doors", "The review list, nothing else."),
           ("Write first", "A draft ADR: context, options, principles touched."),
           ("Two reviewers", "The architect and a peer from another team."),
           ("Comment in writing, fast", "Within three working days."),
           ("Meet only if needed", "Forty-five minutes, to resolve open points."),
           ("Give one of three outcomes", "Go; go with changes; not yet, with what's missing.")],
    vocab=[("Lightweight review", "A short, written review for important decisions."),
           ("Draft ADR", "A decision record written before the decision."),
           ("Reviewer rotation", "Sharing review work across leads."),
           ("Go with changes", "Approved if specific changes are made."),
           ("Not yet", "Not approved until named gaps are filled."),
           ("Async-first", "Written comments before any meeting.")],
    code=dict(file="docs/adr/0028-catalogue-search.md", note="the review outcome on ADR 0028, 19 May 2028", plain=True, src="""
# 28. Managed search for the catalogue
Status: Accepted (go with changes) · 2028-05-19 · Team: business ordering (Jonas, Dee)
Reviewers: Ana, Ben · written comments 15–17 May · no call needed

Options      A Postgres full-text (today) · B managed search service · C self-hosted search
Principles   5 boring technology (B is managed) · 3 one owner (Catalogue stays master) · 8 privacy
Outcome      GO WITH CHANGES
  1  EU region only (data class: public + internal; no customer data in the index)
  2  fed only from catalogue events; never written by other modules
  3  DR tier 2: rebuild the index from events within 1 h
Time         draft to decision: 4 working days
"""),
    tools="tools: ADRs in pull requests, a review-trigger list, a reviewer rotation, a 45-minute calendar slot when needed.",
    gains=["<b>Days, not weeks</b>.",
           "<b>Written record</b> of reasons.",
           "<b>Clear outcomes</b>.",
           "<b>Peers learn</b> by reviewing.",
           "<b>The architect isn't alone</b>."],
    losses=["<b>Writing first</b> takes effort.",
            "<b>Reviewers' time</b>.",
            "<b>Written comments</b> can feel cold.",
            "<b>Needs discipline</b> about deadlines."],
    baseline="Each line compares <b>a slow review board or an unrecorded chat</b> to <b>a written-first review by two reviewers with one of three outcomes in days</b>.",
    ratings=[(2, 5, "Draft, comments and outcome in one place."),
             (2, 4, "A peer from another team reviews."),
             (2, 5, "Four days from draft to decision."),
             (2, 4, "One-way doors still get people."),
             (3, 4, "“Go with changes” keeps options open."),
             (1, 5, "Every review recorded on the ADR."),
             (3, 4, "Managed service chosen with cost in view."),
             (2, 4, "No slides, no board meeting."),
             (2, 4, "Teams write and own the ADR.")],
    pitfalls=[("Reviewing everything", "Reversible changes queued.", "only one-way doors."),
              ("Meeting first", "Nobody read anything.", "written first."),
              ("Vague outcomes", "“Looks fine, but…”", "go, go with changes, not yet."),
              ("One reviewer", "Always the architect.", "a peer too, on rotation.")],
    use=["New data stores, vendors, trust boundaries, public contracts.",
         "Exceptions to principles.",
         "Big migrations' key decisions.",
         "When teams want a second opinion."],
    skip=["Two-way doors: decide in the team."],
    related=["<b>Guardrails not gates</b> (this volume)", "<b>RFCs &amp; design docs</b> (vol. 2)", "<b>Architecture decision records</b> (vol. 2)", "<b>Security architecture review</b> (vol. 5)"],
    quiz=[("When is a lightweight review needed?", "For one-way doors on the review-trigger list."),
          ("Who reviews?", "The architect and a tech lead from another team."),
          ("What are the three outcomes?", "Go; go with changes; not yet, with what's missing."),
          ("How long did the search review take?", "Four working days.")],
    try_it="Take a decision your team is about to make that's hard to undo. Write it as a draft ADR with options, ask two people to comment in writing within three days, and end with one of the three outcomes.",
    remember="<span class=\"hl\">Peer review</span>, not a tribunal: written first, <span class=\"hl\">three outcomes</span>.",
    sources=["Michael Nygard, “Documenting Architecture Decisions” (2011).",
             "Joel Parker Henderson, ADR templates and practice (github.com/joelparkerhenderson/architecture-decision-record).",
             "Andrew Harmel-Law, “Scaling the Practice of Architecture, Conversationally” (martinfowler.com, 2021).",
             "Olaf Zimmermann, architectural decision guidance (2010s)."],
)

# ------------------------------------------------------------------ 07 Golden Paths
gp_problem = Doodle(760, 280, "Doodle of May 2028. Starting a new service at Larder takes about three weeks: copy an old repository, fix its pipeline, set up logging, metrics and alerts, ask Eli for a database, find out about data classes and the cost tags. Each new service ends up slightly different, and some skip the parts that the guardrails now require.",
                    "A new service takes three weeks of copying and asking. Each ends up different; some skip the required parts.")
gp_problem.box(20, 40, 320, 90, "3 weeks", "pink", sub="copy, fix, ask Eli", stroke="red")
gp_problem.box(400, 40, 340, 90, "each different", "paper", sub="some skip SLOs, tags, classes")
gp_problem.note(380, 200, "the right way is the hard way", "red", size=20)

gp_analogy = Doodle(760, 250, "Doodle of a park where people kept cutting across the grass. The gardeners paved the paths people actually walked and lit them at night. Now the easy way is also the right way.",
                     "Pave the paths people actually walk, and light them. The easy way becomes the right way.")
gp_analogy.icon("lamp", 30, 60, 1.2)
gp_analogy.box(150, 50, 280, 100, "worn grass", "pink", sub="everyone cuts across")
gp_analogy.box(460, 50, 280, 100, "paved and lit", "green", sub="the easy way is right")
gp_analogy.note(450, 210, "pave where people walk", "pen")

gp_how = Doodle(760, 400, "Larder's golden path for a new service, from 8 May 2028, built by Eli's platform team. One command creates a repository with the pipeline, logging, metrics and tracing, health checks, a default SLO and dashboard, a data-class declaration, cost tags, and a managed database if asked for. It passes every guardrail on day one. Optional, not mandatory: teams can leave the path, but then own what it gave them. New service time: three weeks to one day. Four of the next five new services used it.",
                 "One command, every guardrail passed on day one. Three weeks → one day. Optional, and still chosen.")
gp_how.box(14, 14, 732, 50, "larder new-service orders-search --db postgres", "paper", size=15)
for i, t in enumerate(["pipeline", "logs · metrics · traces", "SLO + dashboard", "data class", "cost tags", "managed DB"]):
    r, c = divmod(i, 3)
    gp_how.box(14 + c * 248, 84 + r * 70, 236, 58, t, "green", size=15)
gp_how.box(14, 234, 360, 60, "3 weeks → 1 day", "y", size=17)
gp_how.box(386, 234, 360, 60, "optional; 4 of 5 chose it", "blue", size=15)
gp_how.note(380, 334, "leave the path, own what it gave you", "pen", size=16)

GOLDEN = dict(
    slug="golden-paths",
    kicker="a.k.a. “pave where people walk”",
    tldr="A <b>golden path</b> (or paved road) is a supported, ready-made way to do a common job, like starting a new service, that already includes everything the organisation expects: pipeline, observability, security, data classes, cost tags, guardrails. Make it the <b>easiest</b> option rather than a rule: optional, documented, maintained by a platform team. When the right way is the easy way, governance mostly takes care of itself.",
    chips=[("Family", "governance"), ("Origin", "Spotify's golden paths; Netflix's paved road; platform engineering"), ("Lives in", "a service template and a command, owned by the platform team"), ("Pairs with", "guardrails not gates, platform thinking, architecture principles")],
    problem_side="Larder, 8 May 2028",
    problem="""  <p class="lead">Starting a new service at Larder takes about <b>three weeks</b>: copy an old repository, fix its pipeline, set up logging, metrics and alerts, ask Eli for a database, find out about data classes and cost tags. Each new service ends up <b>slightly different</b>, and some skip the parts the guardrails now require. <span class="hl-pink">The right way is the hard way.</span></p>
  <ul>
    <li>Rules without help get skipped.</li>
    <li>Copying old services copies old mistakes.</li>
    <li>Every team re-solves the same setup.</li>
  </ul>""",
    problem_figs=[gp_problem],
    analogy_side="paving the paths people walk",
    analogy="""  <p>In a park where everyone cut across the grass, the gardeners stopped putting up signs. They <b>paved the paths people actually walked</b> and <b>lit them at night</b>. Now the easy way is also the right way, and the grass grows back.</p>""",
    analogy_figs=[gp_analogy],
    map=[("Worn grass", "Three weeks of copying and asking"),
         ("Paving the path", "One command that creates a complete service"),
         ("Lighting it at night", "Logs, metrics, SLOs and dashboards built in"),
         ("Signs nobody reads", "A wiki page of required steps"),
         ("The gardeners", "Eli's platform team")],
    how_side="one command, everything built in, optional",
    how="""  <p>Eli's platform team built the golden path for a new service: <b>one command</b> creates a repository with the <b>pipeline</b>, logs, metrics and traces, health checks, a <b>default SLO and dashboard</b>, a <b>data-class declaration</b>, <b>cost tags</b>, and a managed database if asked. It passes every guardrail on day one. It's <b>optional</b>: teams can leave the path, but then they own what it gave them. New service time: <b>three weeks to one day</b>. Four of the next five services used it.</p>""",
    how_figs=[gp_how],
    steps=[("Pick the most common job", "Usually a new service or a new data pipeline."),
           ("Include everything expected", "Pipeline, observability, security, guardrails."),
           ("Make it one step", "A command or a template."),
           ("Keep it optional", "Teams may leave, and then own the rest."),
           ("Give it an owner", "A platform team keeps it current."),
           ("Measure adoption and time", "Days to first deploy; share of services on it.")],
    vocab=[("Golden path", "A supported, opinionated way to do a common job."),
           ("Paved road", "Netflix's name for the same idea."),
           ("Service template", "A starting repository with everything built in."),
           ("Platform team", "A team whose product is other teams' tooling."),
           ("Developer experience", "How easy it is for engineers to do their work."),
           ("Internal developer portal", "A catalogue of services, templates and docs (e.g. Backstage).")],
    code=dict(file="platform/golden-path/README.md", note="the golden path, May 2028", plain=True, src="""
# Golden path: a new service at Larder                       owner: platform team (Eli)

    larder new-service <name> [--db postgres] [--events consume|publish]

You get, passing every guardrail on day one:
  - repository + pipeline (build once, deploy many; canary to production)
  - logs, metrics, traces; health checks; default SLO (99.9 %, p95 500 ms) + dashboard
  - data-class declaration (FF-09) · cost tags · EU region only (policy as code)
  - managed Postgres (optional) with backups in DR tier 2 by default
  - event contracts registered (FF-08) if --events

Optional. Leaving the path is fine; you then own what it would have given you.
Measured: new service to first production deploy 3 weeks → 1 day; 4 of 5 new services on it.
"""),
    tools="tools: a service template and CLI (cookiecutter, Backstage software templates), the platform's managed databases, CI templates, the internal developer portal.",
    gains=["<b>Three weeks to one day</b>.",
           "<b>Guardrails passed</b> from day one.",
           "<b>Consistent services</b>, easier to run.",
           "<b>Teams choose it</b>; no policing.",
           "<b>Improvements reach everyone</b>."],
    losses=["<b>A platform team</b> to fund.",
            "<b>Templates age</b> without care.",
            "<b>Old services</b> aren't on it.",
            "<b>One size</b> won't fit every case."],
    baseline="Each line compares <b>copying old services and following a wiki of rules</b> to <b>an optional golden path that builds in everything expected</b>.",
    ratings=[(2, 4, "New services look and run alike."),
             (2, 4, "Teams chose it; nobody was forced."),
             (2, 5, "One day instead of three weeks."),
             (2, 4, "Guardrails passed on day one."),
             (3, 4, "Leave the path when needed."),
             (2, 4, "Every service declares its class and SLO."),
             (2, 4, "Cost tags built in."),
             (1, 5, "No setup weeks, no wiki checklist."),
             (2, 5, "Teams start alone.")],
    pitfalls=[("Mandatory path", "Forced, then resented.", "optional and better."),
              ("No owner", "The template rots.", "a platform team owns it."),
              ("Too clever", "Magic nobody understands.", "plain, documented defaults."),
              ("Only for new services", "Old ones drift.", "a migration path for existing services.")],
    use=["Organisations creating new services or pipelines regularly.",
         "After introducing guardrails.",
         "When setup takes weeks.",
         "When services drift apart."],
    skip=["Very small systems with one or two services."],
    related=["<b>Guardrails not gates</b> (this volume)", "<b>Platform thinking</b> (Grace, book 2 vol. 6)", "<b>Build once, deploy many</b> (patterns, Vol. 6)", "<b>SLOs &amp; error budgets</b> (patterns, Vol. 6)"],
    quiz=[("What is a golden path?", "A supported, ready-made way to do a common job, with everything expected built in."),
          ("Why keep it optional?", "So teams choose it because it's easier; leaving means owning what it gave."),
          ("What did it change at Larder?", "New service to first deploy: three weeks to one day."),
          ("Who owns it?", "Eli's platform team.")],
    try_it="Time how long it takes your team to go from “new service” to first production deploy. List every step, and turn the three slowest into a template or a command.",
    remember="<span class=\"hl\">Pave</span> where people walk, and <span class=\"hl\">light</span> the path.",
    sources=["Spotify Engineering, “How We Use Golden Paths to Solve Fragmentation” (2020).",
             "Netflix Technology Blog, on the “paved road” (2010s).",
             "Backstage documentation, software templates.",
             "Matthew Skelton and Manuel Pais, <i>Team Topologies</i> (2019), platform teams."],
)

NOTES = [PRINCIPLES, GUARDRAILS, REVIEW, GOLDEN]
