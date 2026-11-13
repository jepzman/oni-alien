# Series 2 · The Solution Architect's Notebook · Vol. 3 · Documents.
# Running case study: Larder (facts in docs/larder-casebook.md).

# ------------------------------------------------------------------ 05 Architecture One-Pager
op_problem = Doodle(760, 280, "Doodle of November 2026. Femke needs to tell the board whether the platform is ready for four new cities in 2027. Ana's architecture document is thirty pages long. Femke has ten minutes before the board pack is due and reads the table of contents.",
                    "Thirty pages for a ten-minute question: “is the platform ready for four cities?”")
for i in range(6):
    op_problem.box(30 + i * 16, 30 + i * 10, 170, 200, None, "paper", rx=4)
op_problem.text(195, 150, "30 pages", "t-head", size=18)
op_problem.box(380, 40, 360, 90, "Femke", "y", sub="“ready for four cities? 10 minutes”")
op_problem.icon("clock", 530, 160, 1.0)
op_problem.note(560, 260, "she reads the table of contents", "red")

op_analogy = Doodle(760, 260, "Doodle of a property listing sheet: one photo, the key facts (rooms, size, price, energy label), the three things to know (new roof, busy street, garden faces north) and the next step: book a viewing. One sheet, and you know whether to go further.",
                     "A property sheet: a photo, the key facts, three things to know, the next step. One sheet decides if you look further.")
op_analogy.icon("store", 40, 40, 1.4)
for i, (t, s, f) in enumerate([("key facts", "4 rooms · 110 m² · €465k", "blue"), ("know this", "new roof · busy street", "y"), ("next step", "book a viewing", "green")]):
    x = 150 + i * 200
    op_analogy.box(x, 50, 186, 90, t, f, sub=s, size=17, subsize=13)
op_analogy.note(380, 220, "one sheet, then the details if you want them", "pen")

op_how = Doodle(760, 370, "Larder's architecture one-pager, 10 November 2026. Purpose: groceries in 30 minutes in six cities by end 2027. A small context picture. Five key decisions: modular monolith, a city is configuration, offline picker app, outbox and Kafka, Dispatch with Engine A. Numbers today: about 5,800 orders a day, peak 2.6 orders a second, express on time 94 percent in Amsterdam and 92 in Rotterdam, cost per order 3.60 euros. Top risks: StockPilot renewal, three hard-coded Rotterdam settings, one database at five times peak. Next six months: Utrecht in April, the warehouse decision in December.",
                 "Purpose, picture, five decisions, today's numbers, three risks, what's next. The board read it to the end.")
op_how.box(14, 14, 732, 50, "purpose: 30-minute groceries, six cities by end 2027", "paper", size=16)
op_how.box(14, 78, 250, 150, "context", "blue", sub="(small C4 picture)")
op_how.box(278, 78, 468, 150, None, "y")
op_how.head(512, 106, "5 key decisions", size=16)
for i, t in enumerate(["modular monolith · city = config", "offline picker · outbox + Kafka", "Dispatch + Engine A (ADRs 0002–0012)"]):
    op_how.text(512, 140 + i * 28, t, size=15)
op_how.box(14, 242, 360, 110, None, "green")
op_how.head(194, 268, "today", size=16)
op_how.text(194, 298, "5,800 orders/day · peak 2.6/s", size=14)
op_how.text(194, 324, "on time 94 / 92 % · €3.60 an order", size=14)
op_how.box(386, 242, 360, 110, None, "pink")
op_how.head(566, 268, "risks · next", size=16)
op_how.text(566, 298, "StockPilot renewal · TD-1 · one DB", size=14)
op_how.text(566, 324, "Utrecht Apr 2027 · warehouse: Dec", size=14)

ONE_PAGER = dict(
    slug="architecture-one-pager",
    kicker="a.k.a. “the property sheet”",
    tldr="Most people who need to understand the architecture have <b>ten minutes</b>, not an afternoon. Give them <b>one page</b>: the <b>purpose</b> (what the system is for, in business terms), a <b>small picture</b> (C4 context), the <b>five decisions</b> that shape everything, today's <b>numbers</b>, the <b>top risks</b>, and <b>what's next</b>. Link the details; never paste them. Update it every quarter, and use it as the cover page for every longer document.",
    chips=[("Family", "documents"), ("Origin", "architecture practice; “architecture on a page” (Gregor Hohpe, Ruth Malan and others)"), ("Lives in", "docs/architecture/README.md, the first page anyone opens"), ("Pairs with", "C4 model, presenting to executives, arc42")],
    problem_side="Larder, 10 November 2026",
    problem="""  <p class="lead">Before the November board meeting, Femke needs to answer one question: <i>is the platform ready for four more cities in 2027?</i> Ana has a good answer, spread across a <b>30-page architecture document</b>, fifteen ADRs and four diagrams. Femke has <b>ten minutes</b> before the board pack is due. She <span class="hl-pink">reads the table of contents</span>, then calls Ana.</p>
  <ul>
    <li>Long documents are written for completeness; readers need the gist first.</li>
    <li>Executives, new hires and partners each need the same short summary.</li>
    <li>Without a summary, every reader builds their own, differently.</li>
  </ul>""",
    problem_figs=[op_problem],
    analogy_side="the property sheet",
    analogy="""  <p>An estate agent's <b>property sheet</b> has one photo, the <b>key facts</b> (rooms, size, price), the <b>things to know</b> (new roof, busy street, garden faces north) and the <b>next step</b>: book a viewing. One sheet tells you whether to look further. The survey report exists too, for the people who get that far.</p>""",
    analogy_figs=[op_analogy],
    map=[("The photo", "A small context picture"),
         ("Rooms, size, price", "Purpose and today's numbers"),
         ("New roof, busy street", "Key decisions and top risks"),
         ("Book a viewing", "What's next, and who to ask"),
         ("The survey report", "arc42 documents, ADRs and views, linked")],
    how_side="six boxes, linked details",
    how="""  <p>Ana wrote it that afternoon from what already existed: the drivers from Vol. 1, the ADR list, the latest dashboard numbers and the risk list. It went into the board pack as one page; the board asked about one risk (StockPilot) and nothing else. It now sits at the top of <code>docs/architecture/</code> and is the first link in every new hire's onboarding.</p>""",
    how_figs=[op_how],
    steps=[("Write the purpose in business words", "What the system is for, from the drivers: “30-minute groceries, six cities by end 2027”."),
           ("Add a small picture", "The C4 context diagram, shrunk; no more than eight boxes."),
           ("Pick five decisions", "The ones that shape everything, with ADR numbers to follow."),
           ("Show today's numbers", "Volume, peak, quality, cost, from the dashboards, with a date."),
           ("Name the top three risks and what's next", "With owners and dates."),
           ("Link, don't paste; update quarterly", "Every box links to the detail. Date the page.")],
    vocab=[("One-pager", "The whole architecture summarised on one page."),
           ("Purpose", "What the system is for, in business terms."),
           ("Key decision", "A choice that shapes most of the system."),
           ("Fitness numbers", "The few metrics that show the architecture is working."),
           ("Cover page", "The one-pager used as the start of longer documents."),
           ("Progressive disclosure", "Short first, details one click away.")],
    code=dict(file="docs/architecture/README.md", note="Larder's one-pager, 10 November 2026 (text version)", plain=True, src="""
# Larder platform · on one page                         Ana · 10 Nov 2026 · quarterly

PURPOSE    Groceries in 30 minutes (or a chosen hour), six cities by end 2027.
PICTURE    [context diagram: customers · pickers · couriers · offices → Larder ·
            StockPilot · PSP ×2 · billing · helpdesk]
DECISIONS  1 Modular monolith; services only where needed (0002, Dispatch)
           2 A city is configuration, not code (0003)
           3 Picker app works 30 min offline (0004)
           4 Orders leave via an outbox to Kafka (0006, 0007)
           5 Dispatch assigns with routing Engine A (0012)
TODAY      ~5,800 orders/day · peak 2.6 orders/s · express on time 94 % AMS,
           92 % RTM · cost per order €3.60 (target €2.80 by end 2027)
RISKS      StockPilot renewal (decide by 31 Dec) · 3 hard-coded Rotterdam
           settings (TD-1) · one Postgres at 5× peak (load test in Jan)
NEXT       Utrecht (Apr 2027) · warehouse decision (Dec) · C4 + arc42 docs (Nov)
More       arc42 docs · ADR log · views · runbooks
"""),
    tools="tools: a Markdown page in the repo, rendered in the wiki or docs site; a one-slide version for decks. The C4 context diagram can be embedded from the diagrams-as-code source.",
    gains=["<b>Read in ten minutes</b> by anyone.",
           "<b>Same summary for everyone</b>: board, new hires, partners.",
           "<b>Forces priorities</b>: only five decisions fit.",
           "<b>Entry point</b> to the detailed documents.",
           "<b>Quarterly snapshot</b> of how the architecture is doing."],
    losses=["<b>Hard to write short</b>; easy to cram.",
            "<b>Hides nuance</b> some readers need.",
            "<b>Goes stale</b> without the quarterly update.",
            "<b>Numbers need a source</b> that's kept current."],
    baseline="Each line compares <b>a long architecture document as the only description</b> to <b>a dated one-pager (purpose, picture, five decisions, numbers, risks, next) linking to the details</b>.",
    ratings=[(1, 5, "The whole architecture in ten minutes."),
             (2, 5, "The board and the team read the same page."),
             (3, 4, "Questions start from shared facts."),
             (2, 4, "The top three risks are in front of the board."),
             (3, 3, "Doesn't change adaptability."),
             (2, 4, "Every box links to its ADR or view."),
             (2, 4, "Cost per order is one of the numbers."),
             (3, 4, "An afternoon; an hour each quarter."),
             (2, 4, "New hires orient themselves without the architect.")],
    pitfalls=[("Cramming", "Two pages in small type.", "five decisions, three risks; link the rest."),
              ("Technology list", "“Python, Postgres, Kafka.”", "decisions and why, not just tools."),
              ("No numbers", "A page of claims.", "today's volume, quality and cost, dated."),
              ("Never updated", "June's page in November.", "date it and update it every quarter.")],
    use=["Board packs, investor questions, partner due diligence.",
         "Onboarding: the first page a new hire reads.",
         "The cover page of every longer architecture document.",
         "Quarterly architecture check-ins."],
    skip=["Detailed design discussions: use the full views.",
          "Single-component changes: an ADR is enough."],
    related=["<b>Presenting to executives</b> (this volume)", "<b>arc42 template</b> (this volume)", "<b>C4 model</b> (this volume)", "<b>Business drivers &amp; goals</b> (Vol. 1)"],
    quiz=[("What six things go on the one-pager?", "Purpose, a small picture, five key decisions, today's numbers, top risks, what's next."),
          ("Why link rather than paste?", "To keep it to one page; the details live in the ADRs, views and arc42 documents."),
          ("How often should it be updated?", "Every quarter, with a date on the page."),
          ("Who reads it?", "Executives, the board, new hires, partners: anyone with ten minutes.")],
    try_it="Write your system's one-pager in 90 minutes: purpose, a picture with at most eight boxes, five decisions, four numbers, three risks, what's next. Give it to someone outside engineering and ask them to explain the system back to you in two minutes.",
    remember="One <span class=\"hl\">sheet</span>, like a property listing. The survey report is <span class=\"hl\">one click</span> away.",
    sources=["Gregor Hohpe, <i>The Software Architect Elevator</i> (2020).",
             "Ruth Malan and Dana Bredemeyer, “Architecture Resources” (bredemeyer.com).",
             "Simon Brown, <i>Software Architecture for Developers</i>, vol. 2 (2018).",
             "Barbara Minto, <i>The Pyramid Principle</i> (1987)."],
)

# ------------------------------------------------------------------ 06 arc42 Template
a42_problem = Doodle(760, 280, "Doodle of a new engineer's search in November 2026: architecture information in the wiki, in the repository, in shared documents and in slides. Quality requirements, risks and cross-cutting rules are nowhere obvious. Each document has its own structure.",
                     "Four places, every document shaped differently, and “where are the quality requirements?” has no answer.")
for i, (t, f) in enumerate([("wiki", "paper"), ("repo", "blue"), ("shared docs", "y"), ("slides", "pink")]):
    a42_problem.box(20 + i * 186, 30, 166, 64, t, f, size=17)
a42_problem.box(150, 140, 460, 70, "new hire: “where are the risks?”", "y", size=16)
a42_problem.note(380, 254, "every document a different shape", "red")

a42_analogy = Doodle(760, 250, "Doodle of a cookbook where every recipe has the same layout: serves, time, ingredients, method, tips. You know where to look on any page, and a missing section is easy to spot.",
                      "A good cookbook: every recipe laid out the same, so you know where to look, and spot what's missing.")
a42_analogy.icon("recipe", 40, 50, 1.6)
for i, t in enumerate(["serves · time", "ingredients", "method", "tips"]):
    a42_analogy.box(170 + i * 146, 70, 134, 60, t, ["paper", "y", "blue", "green"][i], size=15)
a42_analogy.note(450, 200, "same shape on every page", "pen")

a42_how = Doodle(760, 380, "The twelve arc42 sections and where Larder's existing material goes. 1 introduction and goals: drivers. 2 constraints. 3 context: C4 context. 4 solution strategy: the one-pager's five decisions. 5 building blocks: C4 containers and components. 6 runtime: sequence diagrams. 7 deployment: the deployment diagram. 8 cross-cutting concepts: outbox, offline, city configuration. 9 decisions: the ADR log. 10 quality requirements: the quality scenarios. 11 risks and technical debt: the risk list and debt register. 12 glossary. Larder fills nine fully and links three.",
                  "Twelve fixed sections. Most of Larder's material already existed; arc42 gave it one shape and one place.")
secs = [("1 goals", "drivers"), ("2 constraints", "Vol. 1"), ("3 context", "C4 L1"), ("4 strategy", "one-pager"),
        ("5 building blocks", "C4 L2–3"), ("6 runtime", "sequences"), ("7 deployment", "deploy view"), ("8 concepts", "outbox, offline…"),
        ("9 decisions", "ADR log"), ("10 quality", "scenarios"), ("11 risks, debt", "TD register"), ("12 glossary", "Feb 2027")]
for i, (t, s) in enumerate(secs):
    r, c = divmod(i, 4)
    x, y = 14 + c * 184, 14 + r * 110
    a42_how.box(x, y, 172, 94, t, ["blue", "y", "green"][r], sub=s, size=15, subsize=14, rx=8)
a42_how.note(380, 360, "fill what's needed · link what exists · never copy", "pen", size=18)

ARC42 = dict(
    slug="arc42",
    kicker="a.k.a. “every recipe laid out the same”",
    tldr="Architecture documents are hard to use when every one has a different shape. <b>arc42</b> is a free template with <b>twelve fixed sections</b>: goals, constraints, context, solution strategy, building blocks, runtime, deployment, cross-cutting concepts, decisions, quality requirements, risks and glossary. Use it as a <b>skeleton</b>, not a form: <b>fill what's needed, link what already exists</b> (ADRs, diagrams, debt register), and leave a one-line “not needed, because…” where a section doesn't apply.",
    chips=[("Family", "documents"), ("Origin", "Gernot Starke and Peter Hruschka, arc42 (2005–), arc42.org"), ("Lives in", "docs/architecture/, one file per section"), ("Pairs with", "architecture one-pager, docs as code, C4 model")],
    problem_side="Larder, 17 November 2026",
    problem="""  <p class="lead">A new engineer spends her first week looking for Larder's architecture. It's in the <b>wiki</b>, the <b>repo</b>, <b>shared documents</b> and a few <b>slide decks</b>, each shaped differently. She finds the ADRs and the new C4 diagrams, but asks Ana: <i>where are the quality requirements? the risks? the rules everyone follows, like the outbox?</i> They exist, <span class="hl-pink">somewhere</span>.</p>
  <ul>
    <li>Every author structures documents their own way.</li>
    <li>Some topics (quality goals, cross-cutting rules) have no obvious home.</li>
    <li>Readers can't tell what's missing from what's elsewhere.</li>
  </ul>""",
    problem_figs=[a42_problem],
    analogy_side="the cookbook",
    analogy="""  <p>In a good cookbook every recipe is laid out the same way: <b>serves and time</b>, <b>ingredients</b>, <b>method</b>, <b>tips</b>. On any page you know where to look, and if a recipe has no cooking time, you notice at once. The layout doesn't make the food better; it makes the book usable.</p>""",
    analogy_figs=[a42_analogy],
    map=[("Serves and time", "Sections 1–3: goals, constraints, context"),
         ("Ingredients", "Sections 4–5: strategy and building blocks"),
         ("Method", "Sections 6–8: runtime, deployment, cross-cutting concepts"),
         ("Tips and warnings", "Sections 9–11: decisions, quality, risks"),
         ("The index", "Section 12: glossary")],
    how_side="twelve sections, mostly links",
    how="""  <p>Ana mapped what Larder already had onto the twelve sections in an afternoon. Most were <b>links</b>: drivers, constraints, C4 diagrams, sequence diagrams, the ADR log, the debt register. Two sections needed new writing: <b>cross-cutting concepts</b> (outbox, offline-first, city configuration, idempotency) and <b>quality requirements</b> (the scenarios from Vol. 1, gathered in one place). The glossary was scheduled for February.</p>""",
    how_figs=[a42_how],
    steps=[("Create the twelve files", "<code>docs/architecture/01-goals.md</code> … <code>12-glossary.md</code>, each with its arc42 heading."),
           ("Link what exists", "ADRs, diagrams, the debt register: link, never copy."),
           ("Write the gaps", "Usually cross-cutting concepts and quality requirements."),
           ("Mark what's not needed", "One line: “not needed, because…”, so readers know it's not missing."),
           ("Start with the one-pager", "The README is the one-pager; arc42 is the next layer."),
           ("Review with changes", "When an ADR or diagram changes, check its section.")],
    vocab=[("arc42", "A free, twelve-section template for architecture documentation."),
           ("Solution strategy", "The few fundamental decisions and approaches."),
           ("Building block view", "The static structure: containers and components."),
           ("Cross-cutting concepts", "Rules and patterns used everywhere (logging, outbox, security)."),
           ("Quality requirements", "Measurable quality goals, often as scenarios."),
           ("arc42 lite", "Using only the sections you need, linking the rest.")],
    code=dict(file="docs/architecture/08-concepts.md", note="arc42 section 8, the part Larder had to write", plain=True, src="""
# 8. Cross-cutting concepts                              arc42 · Larder · Nov 2026

8.1 Events leave a transaction through the outbox
    Every module that publishes writes to its outbox in the same transaction;
    the relay sends to Kafka. Consumers dedupe on the event id. (ADR 0007)
8.2 A city is configuration
    Stores, zones, hours, prices and VAT live in the city config, never in code.
    Exceptions are technical debt (TD-1). (ADR 0003)
8.3 Offline-first in the store
    The picker app works 30 minutes without Wi-Fi; answers sync at packing. (ADR 0004)
8.4 Idempotent commands
    Every payment and order command carries a client key; retries are safe.
8.5 Personal data
    Customer data stays in the EU; see the data view and Lena's register.

Sections not needed yet: none. Section 12 (glossary): planned February 2027.
"""),
    tools="tools: the arc42 templates (Markdown, AsciiDoc, Confluence) from arc42.org; docToolchain to build arc42 docs from the repo; Structurizr can embed diagrams into the sections.",
    gains=["<b>A known shape</b>: readers know where to look.",
           "<b>Gaps are visible</b>: empty sections stand out.",
           "<b>Homes for orphan topics</b>: concepts, quality, risks.",
           "<b>Free and widely known</b>, with tooling.",
           "<b>Reuses existing work</b> through links."],
    losses=["<b>Can become form-filling</b> if every section is forced.",
            "<b>Twelve files</b> feel heavy for small systems.",
            "<b>Duplication</b> if people copy instead of link.",
            "<b>Unfamiliar names</b> at first."],
    baseline="Each line compares <b>architecture information scattered across tools, each document shaped differently</b> to <b>arc42's twelve sections in the repo, mostly linking what exists</b>.",
    ratings=[(2, 4, "Readers know where every topic lives."),
             (3, 3, "Mostly for engineers and reviewers."),
             (3, 3, "Doesn't speed decisions directly."),
             (2, 4, "The risks section collects them in one place."),
             (3, 3, "Neutral."),
             (2, 5, "Decisions, quality and risks have fixed homes."),
             (3, 3, "Neutral."),
             (3, 3, "An afternoon to map; light upkeep if linking."),
             (2, 4, "New hires find answers without asking.")],
    pitfalls=[("Form-filling", "Every section filled with filler.", "write only what helps; mark the rest “not needed, because…”."),
              ("Copying", "The ADRs pasted into section 9, then edited separately.", "link, never copy."),
              ("A separate tool", "arc42 in a wiki nobody updates with code changes.", "keep it in the repo, next to the code."),
              ("No entry point", "Twelve files and no summary.", "the one-pager is the README.")],
    use=["Systems with more than one team.",
         "When architecture information is scattered.",
         "Audits and partner due diligence.",
         "Long-lived systems with turnover."],
    skip=["Small, short-lived projects: a one-pager and ADRs are enough.",
          "As a substitute for talking: documents support conversations."],
    related=["<b>Architecture one-pager</b> (this volume)", "<b>Docs as code</b> (this volume)", "<b>Views &amp; viewpoints (4+1)</b> (this volume)", "<b>Quality attribute scenarios</b> (Vol. 1)"],
    quiz=[("How many sections does arc42 have?", "Twelve."),
          ("Which two sections did Larder have to write from scratch?", "Cross-cutting concepts and quality requirements."),
          ("What do you do with a section that doesn't apply?", "Write one line: “not needed, because…”."),
          ("Copy or link?", "Link: ADRs, diagrams and registers stay in one place.")],
    try_it="Create the twelve arc42 headings for your system in one document. Under each, paste only links to what already exists. Count the sections with nothing to link: those are your documentation gaps. Write the most important one this week.",
    remember="Lay out every page the <span class=\"hl\">same</span> way. <span class=\"hl\">Link</span>, don't copy.",
    sources=["Gernot Starke and Peter Hruschka, <i>arc42 by Example</i> (2019), and arc42.org.",
             "Gernot Starke, <i>Effektive Softwarearchitekturen</i> (various editions).",
             "docToolchain documentation (doctoolchain.org).",
             "Paul Clements et al., <i>Documenting Software Architectures</i>, 2nd ed. (2010)."],
)

# ------------------------------------------------------------------ 07 Docs as Code
dc_problem = Doodle(760, 280, "Doodle of the C4 container diagram, drawn in a drawing tool on 6 October 2026. Seven weeks later it's already wrong: a new service for business accounts is missing, and Engine A's box has the wrong name. Nobody remembers to update the drawing when the code changes; the source file sits in someone's personal folder.",
                    "Drawn in October, wrong by November. The diagram lives in a drawing tool; the code changes in the repo.")
dc_problem.box(20, 30, 300, 180, None, "paper")
dc_problem.head(170, 62, "containers.png", size=16)
dc_problem.box(50, 90, 110, 46, "Core", "blue", size=15)
dc_problem.box(180, 90, 110, 46, "Dispatch", "blue", size=15)
dc_problem.box(50, 150, 240, 40, "?", "pink", dash=True, stroke="red", size=16)
dc_problem.arrow(326, 120, 420, 120, dash=True)
dc_problem.box(426, 40, 314, 160, None, "y")
dc_problem.head(583, 74, "the repo, 7 weeks on", size=16)
for i, t in enumerate(["+ business accounts", "~ Engine A renamed", "source: Ana's laptop"]):
    dc_problem.text(583, 112 + i * 30, t, size=16)
dc_problem.note(380, 258, "nobody updates a drawing they can't find", "red")

dc_analogy = Doodle(760, 250, "Doodle of a ship's chart kept up to date with official notices: each change, a new buoy or a moved wreck, arrives as a numbered correction, is applied to the chart and logged in its margin. The chart is trusted because every change is recorded.",
                     "A ship's chart is trusted because every change arrives as a numbered correction, applied and logged.")
dc_analogy.icon("map", 40, 50, 1.6)
dc_analogy.icon("ship", 150, 140, 0.9)
for i, (t, f) in enumerate([("notice no. 412", "y"), ("applied", "blue"), ("logged in margin", "green")]):
    dc_analogy.box(236 + i * 176, 70, 166, 60, t, f, size=13)
    if i < 2:
        dc_analogy.arrow(236 + i * 176 + 168, 100, 236 + i * 176 + 174, 100)
dc_analogy.note(500, 200, "every change reviewed and recorded", "pen")

dc_how = Doodle(760, 340, "Larder's docs as code, from 24 November 2026. Markdown pages and diagrams as text (Structurizr DSL and Mermaid) live in the repository next to the code. A change to the architecture comes as one pull request with code, diagram and ADR together, reviewed together. CI builds the docs site, checks links and renders diagrams. The published site is always the main branch.",
                "Docs and diagrams as text, in the repo, changed in the same pull request as the code, published by CI.")
for i, (t, s, f) in enumerate([("text in repo", "Markdown, DSL", "y"), ("one pull request", "code + diagram + ADR", "blue"), ("CI", "render · check links", "paper"), ("docs site", "always main", "green")]):
    x = 10 + i * 190
    dc_how.box(x, 60, 170, 100, t, f, sub=s, size=16, subsize=13)
    if i < 3:
        dc_how.arrow(x + 174, 110, x + 186, 110)
dc_how.box(150, 210, 460, 70, "review the diagram like code", "pink", sub="“this PR adds a container: is it on the diagram?”", subsize=14)
dc_how.note(380, 318, "a PR checklist line, not a heroic tidy-up", "pen", size=17)

DOCS_CODE = dict(
    slug="docs-as-code",
    kicker="a.k.a. “corrections to the chart”",
    tldr="Documentation goes stale when it lives somewhere the code doesn't. <b>Docs as code</b> means writing docs and diagrams as <b>plain text in the repository</b> (Markdown, Structurizr DSL, Mermaid), changing them in the <b>same pull request</b> as the code they describe, <b>reviewing</b> them like code, and letting <b>CI</b> render diagrams, check links and publish the site. The docs then change when the system changes, because it's the same change.",
    chips=[("Family", "documents"), ("Origin", "Write the Docs community (2013–); Anne Gentle, <i>Docs Like Code</i> (2017)"), ("Lives in", "docs/ in the main repo, published by CI"), ("Pairs with", "C4 model, arc42, living diagrams")],
    problem_side="Larder, 24 November 2026",
    problem="""  <p class="lead">The C4 container diagram from 6 October was drawn in a drawing tool and exported as an image. Seven weeks later it's <b>already wrong</b>: the new business-accounts work isn't on it, and Engine A's box has an old name. The source file is <span class="hl-pink">on Ana's laptop</span>. Nobody else can update it, and nobody remembers to when the code changes.</p>
  <ul>
    <li>Diagrams in separate tools aren't part of any code review.</li>
    <li>Exported images can't be diffed, reviewed or searched.</li>
    <li>Updating docs becomes a heroic tidy-up, done twice a year.</li>
  </ul>""",
    problem_figs=[dc_problem],
    analogy_side="corrections to the chart",
    analogy="""  <p>A ship's navigator trusts the <b>chart</b> because it's kept current by numbered <b>Notices to Mariners</b>: each change (a new buoy, a moved wreck) is published, <b>applied</b> to the chart, and <b>logged</b> in its margin. Nobody redraws the chart from memory once a year; every change is a small, reviewed correction.</p>""",
    analogy_figs=[dc_analogy],
    map=[("The chart", "The docs and diagrams in the repo"),
         ("A Notice to Mariners", "A pull request that changes the system"),
         ("Applying the correction", "Updating the diagram in the same PR"),
         ("The log in the margin", "Git history of the docs"),
         ("Trusting the chart", "Engineers trusting the docs again")],
    how_side="same repo, same PR, same review",
    how="""  <p>Ana moved the C4 model into <b>Structurizr DSL</b> and the flows into <b>Mermaid</b>, all in <code>docs/</code>. The pull request template gained one line: <i>does this change the architecture? update the diagram and link the ADR</i>. CI renders the diagrams, checks links and publishes the site from main. Within two weeks Ben's team had updated the container diagram themselves, in the PR that added business accounts.</p>""",
    how_figs=[dc_how],
    steps=[("Pick text formats", "Markdown for pages; Structurizr DSL or Mermaid for diagrams."),
           ("Move docs into the repo", "Next to the code they describe; archive the old copies with a pointer."),
           ("Add a PR checklist line", "“Changes the architecture? Update the diagram, link the ADR.”"),
           ("Render and check in CI", "Diagrams to images, link checks, spelling if you like."),
           ("Publish from main", "A docs site (or the repo's own rendering) that's always current."),
           ("Review docs like code", "Reviewers look at the diagram diff too.")],
    vocab=[("Docs as code", "Docs written, reviewed and published with the same tools as code."),
           ("Diagrams as code", "Diagrams described in text and rendered by a tool."),
           ("Structurizr DSL", "A text language for C4 models and views."),
           ("Mermaid", "A text syntax for diagrams that GitHub renders."),
           ("Docs site", "The published, browsable version of the docs."),
           ("Link check", "A CI step that finds broken links.")],
    code=dict(file="docs/architecture/c4/workspace.dsl", note="Structurizr DSL for the container view (excerpt)", plain=True, src="""
workspace "Larder" {
  model {
    customer = person "Customer"
    larder = softwareSystem "Larder platform" {
      apps     = container "Customer apps" "Order, approve swaps, track" "React Native"
      core     = container "Larder Core" "Modular monolith" "Python, Django"
      dispatch = container "Dispatch" "Couriers, vans, assignment" "Python + Engine A"
      db       = container "Core database" "" "Managed Postgres" "Database"
      kafka    = container "Event bus" "" "Managed Kafka" "Queue"
    }
    customer -> apps "Orders groceries"
    apps -> core "HTTPS / JSON"
    core -> kafka "order.ready_for_dispatch (outbox)"
    kafka -> dispatch "Consumes order events"
  }
  views {
    container larder "containers" { include * ; autoLayout lr }
  }
}
"""),
    tools="tools: Structurizr (DSL, Lite, CLI), Mermaid, PlantUML, MkDocs or Docusaurus for the site, docToolchain for arc42, a link checker (lychee) in CI.",
    gains=["<b>Docs change with the code</b>, in the same PR.",
           "<b>Reviewable diffs</b> for diagrams.",
           "<b>Anyone can update</b>, not just the author.",
           "<b>History for free</b> in git.",
           "<b>Published automatically</b>, always current."],
    losses=["<b>Text diagrams look plainer</b> than hand-drawn ones.",
            "<b>Layout control is limited</b> with auto-layout.",
            "<b>Non-engineers</b> may find the repo harder to edit.",
            "<b>Setup time</b> for CI and the site."],
    baseline="Each line compares <b>docs and diagrams in separate tools, exported as images</b> to <b>text docs and diagrams in the repo, changed in the same PR as the code and published by CI</b>.",
    ratings=[(3, 4, "Current docs are clearer than pretty, stale ones."),
             (3, 3, "Mostly engineering-facing."),
             (3, 4, "Docs changes don't wait for the architect."),
             (3, 3, "Neutral."),
             (3, 3, "Neutral."),
             (2, 5, "Every diagram change is in git history."),
             (3, 3, "Neutral."),
             (2, 4, "Small updates in each PR, no big tidy-ups."),
             (2, 5, "Teams update the diagrams themselves.")],
    pitfalls=[("Docs in a separate repo", "Same staleness, different place.", "keep docs next to the code they describe."),
              ("No checklist line", "Nobody remembers to update.", "add it to the PR template."),
              ("Pixel-perfect obsession", "Hours tuning auto-layout.", "accept plain; clarity beats beauty."),
              ("Locking out non-engineers", "Lena can't fix a typo.", "offer the web editor, or accept suggestions via comments.")],
    use=["Any team that works in pull requests.",
         "Diagrams that keep going stale.",
         "Architecture docs that several teams edit.",
         "Regulated settings that need a change history."],
    skip=["One-off presentations and sketches.",
          "Documents mainly written by non-engineers: a shared doc may suit better."],
    related=["<b>C4 model</b> (this volume)", "<b>Living diagrams</b> (this volume)", "<b>arc42 template</b> (this volume)", "<b>Architecture decision records</b> (Vol. 2)"],
    quiz=[("What does docs as code mean?", "Docs and diagrams as text in the repo, changed in the same PR as the code, reviewed and published by CI."),
          ("Why do exported images go stale?", "They're outside code review, can't be diffed, and only their author can edit the source."),
          ("What one line did Larder add to the PR template?", "“Changes the architecture? Update the diagram and link the ADR.”"),
          ("Name two text formats for diagrams.", "Structurizr DSL and Mermaid (also PlantUML).")],
    try_it="Take your most-used architecture diagram and redraw it as Mermaid or Structurizr DSL in the repo. Add one line to your PR template asking whether a change affects it. After a month, count how many PRs updated it without you.",
    remember="Every change is a numbered <span class=\"hl\">correction</span>. Same repo, same <span class=\"hl\">pull request</span>.",
    sources=["Anne Gentle, <i>Docs Like Code</i> (2017).",
             "Write the Docs, “Docs as Code” (writethedocs.org).",
             "Simon Brown, Structurizr DSL documentation.",
             "Ralf D. Müller, docToolchain (doctoolchain.org)."],
)

# ------------------------------------------------------------------ 08 Solution Design Document Done Right
sd_problem = Doodle(760, 280, "Doodle of Korenwolf's IT department's solution design template, December 2026: forty sections, including mainframe interfaces, disaster recovery sites and a printer inventory. Most of it doesn't apply to a pantry delivery service. Ruben forwards it to Mo: we need this before the three-office service starts in January.",
                    "A forty-section template, half of it about mainframes and printers, due before January.")
sd_problem.box(20, 20, 300, 230, None, "paper")
sd_problem.head(170, 52, "SDD template v7", size=17)
for i, t in enumerate(["§ 12 mainframe interfaces", "§ 19 DR site location", "§ 27 printer inventory", "… 40 sections"]):
    sd_problem.text(40, 92 + i * 36, t, "t t-soft" if i < 3 else "t", anchor="start", size=15)
sd_problem.box(380, 50, 360, 90, "Ruben → Mo", "y", sub="“needed before January”")
sd_problem.note(560, 200, "most of it doesn't apply", "red")

sd_analogy = Doodle(760, 250, "Doodle of a job application. A weak one sends a whole life story. A good one answers the employer's questions, for this job, with evidence, and says clearly where something doesn't apply.",
                     "A good job application answers their questions, for this job, with evidence. Not your whole life story.")
sd_analogy.box(20, 40, 320, 110, "the life story", "pink", sub="everything, 12 pages")
sd_analogy.box(420, 40, 320, 110, "their questions", "green", sub="answered, with evidence, 2 pages")
sd_analogy.note(380, 210, "answer what they need to decide", "pen")

sd_how = Doodle(760, 360, "How Ana wrote Korenwolf's solution design document, 1 to 18 December 2026. First, a call with Korenwolf's IT to learn their real questions: what data, how secured, how available, how integrated, who supports it, how to leave. Then the document: a one-page summary, the context and data views, security and single sign-on for office managers, service levels (98 percent complete, by 09:00), support and exit, and one line for each template section that doesn't apply, with the reason. Fourteen pages instead of forty. Approved on 18 December.",
                 "Ask what they need to decide, answer that with existing views, and say “not applicable, because…” for the rest.")
sd_how.box(14, 20, 220, 90, "1 · call their IT", "blue", sub="their real questions")
sd_how.arrow(238, 65, 270, 65)
sd_how.box(274, 20, 472, 90, None, "y")
sd_how.head(510, 50, "2 · answer those, with views", size=16)
sd_how.text(510, 80, "data · security & SSO · 98 % by 09:00 · support · exit", size=14)
sd_how.box(14, 140, 350, 100, "3 · the rest: one line", "paper", sub="“n/a: no mainframe; SaaS + cloud”", subsize=14)
sd_how.box(396, 140, 350, 100, "4 · summary on top", "green", sub="the one-pager, for their CIO", subsize=14)
sd_how.box(180, 268, 400, 60, "14 pages · approved 18 Dec", "green", size=17)

SDD = dict(
    slug="solution-design-document",
    kicker="a.k.a. “answer the employer's questions”",
    tldr="Clients and big partners often ask for a <b>solution design document</b> (SDD) on their own template, usually long and written for a different kind of system. Don't fight the template, and don't fill it blindly. <b>Ask what they need to decide</b> (data, security, availability, integration, support, exit), answer <b>those</b> clearly with your existing views, put a <b>one-page summary</b> on top, and for every section that doesn't apply write <b>one line: “not applicable, because…”</b>.",
    chips=[("Family", "documents"), ("Origin", "enterprise IT practice; vendor due diligence and security questionnaires"), ("Lives in", "a document for the client, built from docs/architecture/"), ("Pairs with", "architecture one-pager, views &amp; viewpoints, exit plans")],
    problem_side="Larder, 1 December 2026",
    problem="""  <p class="lead">Korenwolf's three-office service starts in January. Their IT department sends Ruben a <b>solution design template</b>: forty sections, including mainframe interfaces, the location of the disaster-recovery site and a printer inventory. Ruben forwards it to Mo: “needed before January”. Mo asks Ana. <span class="hl-pink">Most of the template doesn't apply</span> to a pantry delivery service, but leaving sections blank looks evasive.</p>
  <ul>
    <li>Client templates are written for big internal IT projects, not for a SaaS-like service.</li>
    <li>Filling every section produces forty pages nobody reads.</li>
    <li>Blank sections look like hiding something.</li>
  </ul>""",
    problem_figs=[sd_problem],
    analogy_side="the job application",
    analogy="""  <p>A weak job application sends the <b>whole life story</b>. A good one reads the advert, works out what the employer needs to decide, and answers <b>their questions</b>, for this job, with evidence. Where something doesn't apply (no driving licence needed), it says so in a line, so nobody wonders.</p>""",
    analogy_figs=[sd_analogy],
    map=[("The employer's advert", "Korenwolf's 40-section template"),
         ("What they need to decide", "Data, security, availability, integration, support, exit"),
         ("Evidence", "Larder's existing views: data, deployment, the one-pager"),
         ("“Not required for this role”", "“Not applicable, because…”, one line each"),
         ("The cover letter", "A one-page summary for their CIO")],
    how_side="ask, answer, summarise, say n/a",
    how="""  <p>Mo set up a 30-minute call with Korenwolf's IT lead. Their real questions were six: <b>what data</b> Larder holds (office managers' names and emails, office addresses; no staff data), <b>how it's secured</b> (single sign-on for office managers), <b>availability</b> (98 % complete, by 09:00), <b>integration</b> (invoices from the billing service, a monthly report), <b>support</b>, and <b>exit</b>. Ana answered those with existing views, put the one-pager on top, and wrote one line for each other section. <b>Fourteen pages</b>; approved on 18 December.</p>""",
    how_figs=[sd_how],
    steps=[("Ask what they must decide", "A short call with their IT or security lead: which questions really matter?"),
           ("Map their sections to your docs", "Most answers already exist: one-pager, views, deployment, exit plan."),
           ("Answer the real questions fully", "With diagrams, numbers and named owners."),
           ("Write “n/a, because…” for the rest", "One line each, so nothing looks hidden."),
           ("Put a summary on top", "The one-pager, adapted to their service."),
           ("Keep the source", "Build it from docs/architecture/ so next year's update is quick.")],
    vocab=[("SDD", "Solution design document: how a solution meets a client's needs."),
           ("Due diligence", "A client's checks before relying on a supplier."),
           ("Security questionnaire", "A client's list of security questions for suppliers."),
           ("SSO", "Single sign-on: users log in with their own company's account."),
           ("Service level", "A promised measure of service, like 98 % complete by 09:00."),
           ("Not applicable", "A section that doesn't fit, with the reason.")],
    code=dict(file="clients/korenwolf/sdd-2026-12.md", note="contents of the SDD sent to Korenwolf (excerpt)", plain=True, src="""
# Larder for Business · Solution Design for Korenwolf Group      v1.0 · 18 Dec 2026

0  Summary (one page)                    service, picture, five facts, contacts
1  Scope                                 weekly pantry restock, 3 offices, from Jan 2027
2  Data                                  office managers' names + emails, office addresses,
                                         order history. No Korenwolf staff data. EU only.
3  Security                              SSO with Korenwolf's identity provider for office
                                         managers · TLS · access reviewed quarterly
4  Availability and service levels       98 % of lines delivered · by 09:00 · monthly report
5  Integration                           invoices from our billing service (PDF + UBL);
                                         monthly report by email; no system-to-system link
6  Support                               Mo (account), support desk 07:00–18:00, incidents
7  Exit                                  order history and invoices exported on request
...
12 Mainframe interfaces                  n/a: no mainframe; cloud service + SaaS
19 Disaster recovery site                n/a as a site; see 4 and our backup policy
27 Printer inventory                     n/a: no printers involved
"""),
    tools="tools: build it from your docs-as-code sources (docToolchain, Pandoc to PDF or Word); keep a reusable answer bank for security questionnaires; the one-pager as the summary.",
    gains=["<b>The client gets what they need to decide</b>, quickly.",
           "<b>Nothing looks hidden</b>: n/a lines explain gaps.",
           "<b>Reuses existing docs</b> instead of writing from scratch.",
           "<b>Shorter review cycles</b> with the client's IT.",
           "<b>Reusable</b> for the next business client."],
    losses=["<b>A call to arrange</b> before writing.",
            "<b>Some clients insist</b> on every section, in full.",
            "<b>Commitments in writing</b>: service levels must be real.",
            "<b>Another version</b> to keep in step with the docs."],
    baseline="Each line compares <b>filling a client's long template section by section</b> to <b>answering the client's real questions with existing views, a summary on top and one-line n/a's</b>.",
    ratings=[(2, 4, "Korenwolf's IT got clear answers to its questions."),
             (2, 5, "Mo, Ruben and Korenwolf's IT agreed on one document."),
             (2, 4, "Approved in two and a half weeks."),
             (2, 4, "Data and exit questions answered up front."),
             (3, 3, "Neutral."),
             (2, 4, "The SDD is built from the repo's docs."),
             (3, 3, "Neutral."),
             (2, 4, "Fourteen pages instead of forty."),
             (3, 3, "Still mostly Ana's work.")],
    pitfalls=[("Filling every box", "Forty pages about printers.", "ask what they must decide; n/a the rest with a reason."),
              ("Blank sections", "Gaps look like hiding.", "one line: “not applicable, because…”."),
              ("Promises you can't keep", "“99.99 % availability” to sound good.", "state real service levels, measured."),
              ("Writing from scratch", "A new document unrelated to your docs.", "build it from the one-pager and views.")],
    use=["Enterprise clients and partners with procurement rules.",
         "Security and due-diligence reviews.",
         "Any time a client's template arrives.",
         "Before signing contracts with service levels."],
    skip=["Internal design work: use arc42, ADRs and views.",
          "When a standard security questionnaire answer bank covers it."],
    related=["<b>Architecture one-pager</b> (this volume)", "<b>Views &amp; viewpoints (4+1)</b> (this volume)", "<b>Exit plans &amp; reversibility</b> (Vol. 2)", "<b>Identity federation &amp; SSO</b> (Vol. 4)"],
    quiz=[("What's the first step with a client's SDD template?", "Ask what they actually need to decide."),
          ("What do you write for a section that doesn't apply?", "One line: “not applicable, because…”."),
          ("What were Korenwolf's six real questions?", "Data, security, availability, integration, support and exit."),
          ("Where should the SDD's content come from?", "Your existing docs: the one-pager, views, deployment, exit plan.")],
    try_it="Find the last long template a client or partner asked you to fill in. List the six questions it really needed answered. Write those answers in two pages from your existing docs, plus one line for every other section, and compare with what you sent.",
    remember="Answer the <span class=\"hl\">employer's questions</span>, not your life story. And say <span class=\"hl\">n/a, because…</span>",
    sources=["Gregor Hohpe, <i>The Software Architect Elevator</i> (2020), on writing for the reader.",
             "Shared Assessments, Standardized Information Gathering (SIG) questionnaire.",
             "Cloud Security Alliance, Consensus Assessments Initiative Questionnaire (CAIQ).",
             "Barbara Minto, <i>The Pyramid Principle</i> (1987)."],
)

NOTES = [ONE_PAGER, ARC42, DOCS_CODE, SDD]
