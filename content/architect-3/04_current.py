# Series 2 · The Solution Architect's Notebook · Vol. 3 · Keeping it current.
# Running case study: Larder (facts in docs/larder-casebook.md).

# ------------------------------------------------------------------ 13 Living Diagrams
ld_problem = Doodle(760, 280, "Doodle of January 2027. The container diagram, kept as code since November, says Customer Care talks to Dispatch only through Kafka. Traces from production show a direct HTTP call from Customer Care to Dispatch's courier-location API, added in December for the support tool. Nobody updated the diagram; the code changed, the intended picture didn't.",
                    "The diagram says “only via Kafka”. Production traces show a direct call nobody drew.")
ld_problem.box(20, 30, 330, 180, None, "paper")
ld_problem.head(185, 60, "the diagram", size=17)
ld_problem.box(40, 90, 120, 50, "Care", "blue", size=15)
ld_problem.box(210, 90, 120, 50, "Dispatch", "blue", size=15)
ld_problem.text(185, 180, "only via Kafka", size=16)
ld_problem.box(410, 30, 330, 180, None, "y")
ld_problem.head(575, 60, "production traces", size=17)
ld_problem.box(430, 90, 120, 50, "Care", "blue", size=15)
ld_problem.box(600, 90, 120, 50, "Dispatch", "blue", size=15)
ld_problem.arrow(554, 115, 596, 115, color="red")
ld_problem.text(575, 180, "+ direct HTTP (Dec)", "t t-red", size=16)
ld_problem.note(380, 262, "docs as code still drift if nobody compares", "red")

ld_analogy = Doodle(760, 250, "Doodle comparing a printed road map with a satnav's live traffic view. The printed map shows the roads as planned; the live view shows where cars actually go today, including the diversion nobody printed.",
                     "A printed road map shows the plan; live traffic shows where cars actually drive today.")
ld_analogy.icon("map", 60, 50, 1.6)
ld_analogy.box(20, 160, 220, 50, "printed map", "paper", size=16)
ld_analogy.icon("phone", 520, 40, 1.8)
ld_analogy.box(450, 160, 260, 50, "live traffic", "green", size=16)
ld_analogy.note(350, 110, "plan vs reality", "pen", size=19)

ld_how = Doodle(760, 360, "Larder's living diagrams from 26 January 2027. Three sources are read automatically: the module dependency graph from the import linter, the infrastructure code, and production traces. CI generates diagrams from each and compares them with the intended model in the Structurizr file. Differences are flagged in a weekly report and, for module dependencies, break the build. The first run found the direct Customer Care to Dispatch call and two unused Kafka topics.",
                 "Generate from what's real, compare with what's intended, and flag the difference.")
for i, (t, s, f) in enumerate([("module graph", "import linter", "blue"), ("infra code", "deployment", "blue"), ("traces", "runtime calls", "blue")]):
    ld_how.box(14, 14 + i * 84, 200, 70, t, f, sub=s, size=16)
    ld_how.arrow(218, 49 + i * 84, 276, 140)
ld_how.box(280, 100, 200, 80, "generated", "y", sub="diagrams")
ld_how.box(280, 230, 200, 80, "intended", "paper", sub="workspace.dsl")
ld_how.arrow(484, 140, 530, 180)
ld_how.arrow(484, 270, 530, 220)
ld_how.box(534, 150, 212, 100, "compare", "pink", sub="flag the difference")
ld_how.note(640, 290, "first run: 1 direct call,", "red", size=16)
ld_how.note(640, 314, "2 unused topics", "red", size=16)

LIVING = dict(
    slug="living-diagrams",
    kicker="a.k.a. “live traffic, not the printed map”",
    tldr="Diagrams drawn by hand, even as code, show what someone <i>intended</i>. <b>Living diagrams</b> are <b>generated from what's real</b>: the code's dependency graph, the infrastructure code, production traces. Then <b>compare</b> the generated picture with the intended model and <b>flag the differences</b>: a dependency nobody drew, a service nobody uses. The intended diagram explains; the generated one checks.",
    chips=[("Family", "keeping it current"), ("Origin", "Cyrille Martraire, <i>Living Documentation</i> (2019); architecture recovery tools"), ("Lives in", "CI jobs and a weekly diff report"), ("Pairs with", "docs as code, fitness functions, C4 model")],
    problem_side="Larder, 26 January 2027",
    problem="""  <p class="lead">Since November the C4 model lives as code, and teams update it in their pull requests. It says <b>Customer Care</b> talks to <b>Dispatch</b> only through Kafka. Then Eli looks at the production <b>traces</b>: there's a <b>direct HTTP call</b> from Customer Care to Dispatch's courier-location API, added in December for the support tool. <span class="hl-pink">The code changed; the intended picture didn't</span>, and nobody noticed for six weeks.</p>
  <ul>
    <li>Docs as code relies on people remembering to update the diagram.</li>
    <li>Unplanned dependencies are the ones most worth knowing about.</li>
    <li>Nobody compares the picture with reality until an incident does.</li>
  </ul>""",
    problem_figs=[ld_problem],
    analogy_side="the printed map and live traffic",
    analogy="""  <p>A <b>printed road map</b> shows the roads as planned. A satnav's <b>live traffic</b> view shows where cars actually drive today, including the diversion nobody printed. You need both: the printed map to understand the region, the live view to see what's really happening, and the difference tells you where the map is wrong.</p>""",
    analogy_figs=[ld_analogy],
    map=[("The printed map", "The intended model: workspace.dsl"),
         ("Live traffic", "Generated diagrams from code, infra and traces"),
         ("The unprinted diversion", "Customer Care calling Dispatch directly"),
         ("Roads nobody drives", "Two unused Kafka topics"),
         ("Updating the map", "Fixing the model or the code, on purpose")],
    how_side="generate, compare, flag",
    how="""  <p>Eli and Ana set up three generators: the <b>module graph</b> from the import linter (already used as a fitness function), a <b>deployment</b> picture from the infrastructure code, and a <b>runtime service map</b> from traces. A weekly CI job compares them with the intended model. The first run found the direct call (now a documented exception, with an ADR to replace it by an event) and <b>two Kafka topics</b> nobody had consumed since October.</p>""",
    how_figs=[ld_how],
    steps=[("Keep an intended model", "The C4 model as code: what the architecture should be."),
           ("Generate from code", "Module and package dependencies (import linter, dependency tools)."),
           ("Generate from infrastructure", "What's deployed, from the infrastructure code or cloud APIs."),
           ("Generate from runtime", "Who calls whom, from traces (OpenTelemetry) or service meshes."),
           ("Compare and flag", "A weekly diff report; module rules break the build."),
           ("Resolve each difference", "Fix the code, update the model, or record an exception with an ADR.")],
    vocab=[("Living diagram", "A diagram generated from the running system or its code."),
           ("Intended model", "What the architecture should be, kept as code."),
           ("Service map", "Calls between services, built from traces."),
           ("Drift", "The gap between the intended model and reality."),
           ("Architecture recovery", "Rebuilding the architecture from code and runtime data."),
           ("Exception", "An accepted difference, recorded with a reason.")],
    code=dict(file=".github/workflows/architecture-drift.yml", note="weekly drift check (shortened)", plain=True, src="""
name: architecture-drift
on:
  schedule: [{ cron: "0 6 * * 1" }]          # Mondays 06:00
  pull_request: { paths: ["core/**", "dispatch/**", "infra/**", "docs/architecture/**"] }
jobs:
  drift:
    steps:
      - run: lint-imports                      # module rules: fail the build (ADR 0002)
      - run: tools/module-graph > out/modules.json
      - run: tools/deployed-from-infra infra/ > out/deployed.json
      - run: tools/service-map --from traces --days 7 > out/calls.json
      - run: tools/compare docs/architecture/c4/workspace.dsl out/*.json > out/drift.md
      - run: tools/post-report out/drift.md   # to #architecture, every Monday
# First run, 26 Jan 2027: Care → Dispatch HTTP (undocumented) · 2 unused topics
"""),
    tools="tools: import-linter, deptry or ArchUnit for code; Structurizr (with its import tools), cloud inventory tools for infrastructure; OpenTelemetry with a service-map view (Jaeger, Grafana Tempo, your APM) for runtime.",
    gains=["<b>Drift found in a week</b>, not at the next incident.",
           "<b>Unplanned dependencies</b> become visible.",
           "<b>Unused parts</b> show up for removal.",
           "<b>Trust in the intended diagram</b> returns.",
           "<b>Builds on existing tools</b>: linter, traces, infra code."],
    losses=["<b>Setup work</b>: generators and a compare step.",
            "<b>Noise</b> until the model and reality are aligned.",
            "<b>Generated diagrams are ugly</b>: they check, they don't explain.",
            "<b>Traces need good coverage</b> to be complete."],
    baseline="Each line compares <b>intended diagrams that rely on people remembering to update them</b> to <b>diagrams generated from code, infrastructure and traces, compared with the intended model every week</b>.",
    ratings=[(3, 4, "The intended diagram stays true, so it stays useful."),
             (3, 3, "Mostly for engineers."),
             (3, 3, "Neutral."),
             (2, 5, "Undocumented couplings found in a week."),
             (3, 4, "Unused parts can be removed safely."),
             (2, 5, "Every difference is resolved and recorded."),
             (3, 4, "Unused topics and services cost money; now they're visible."),
             (3, 3, "Setup, then a weekly report."),
             (3, 4, "Teams see drift in their own areas.")],
    pitfalls=[("Generated only", "Unreadable auto-diagrams replace the intended one.", "keep both: intended to explain, generated to check."),
              ("Report nobody reads", "A weekly diff in a channel nobody opens.", "an owner resolves each difference."),
              ("Everything breaks the build", "Teams disable the check.", "break the build only for agreed rules; report the rest."),
              ("Partial traces", "Half the services aren't instrumented.", "instrument first, or label the map as partial.")],
    use=["Systems with more than a handful of services or modules.",
         "After moving docs to code, as the next step.",
         "When incidents reveal surprise dependencies.",
         "Audits that need evidence of the real architecture."],
    skip=["Small systems where one person sees every change.",
          "Before an intended model exists: write that first."],
    related=["<b>Docs as code</b> (this volume)", "<b>C4 model</b> (this volume)", "<b>Fitness functions</b> (Vol. 1)", "<b>Logs, metrics &amp; traces</b> (patterns, Vol. 6)"],
    quiz=[("What's the difference between an intended and a generated diagram?", "Intended shows what should be and explains it; generated shows what is and checks it."),
          ("Name three sources for generated diagrams.", "Code dependencies, infrastructure code, production traces."),
          ("What did Larder's first run find?", "A direct HTTP call from Customer Care to Dispatch, and two unused Kafka topics."),
          ("What happens to each difference?", "Fix the code, update the model, or record an exception with an ADR.")],
    try_it="Generate one picture of your system from reality: a dependency graph from your code, or a service map from a week of traces. Put it next to your intended diagram and list every difference. Decide, for each one, whether the code or the diagram is wrong.",
    remember="Keep the <span class=\"hl\">printed map</span>, and check it against <span class=\"hl\">live traffic</span> every week.",
    sources=["Cyrille Martraire, <i>Living Documentation</i> (2019).",
             "Simon Brown, “Diagrams as code 2.0” (talks, 2020–).",
             "OpenTelemetry documentation, “Traces” and service graphs.",
             "Neal Ford et al., <i>Building Evolutionary Architectures</i>, 2nd ed. (2022)."],
)

# ------------------------------------------------------------------ 14 Architecture Roadmap
ar_problem = Doodle(760, 280, "Doodle of the February 2027 board meeting. The board asks what has to change in the platform for four new cities and a new country this year. Ana's backlog has 60 architecture items, unordered. The board can't see a plan, only a pile.",
                    "“What has to change for four cities and a new country?” Sixty architecture items, in no order.")
for i in range(18):
    r, c = divmod(i, 6)
    ar_problem.box(20 + c * 60, 30 + r * 54, 48, 40, None, ["paper", "blue", "y"][i % 3], rx=4)
ar_problem.note(200, 210, "60 items, no order", "red")
ar_problem.box(440, 50, 300, 90, "the board", "y", sub="“what changes, when?”")
ar_problem.note(590, 210, "a pile, not a plan", "red")

ar_analogy = Doodle(760, 250, "Doodle of renovating a house while living in it: first the roof, then the kitchen, then the bathrooms, then the garden. After each stage the house is fully livable, and the order follows what each stage needs from the last.",
                     "Renovating while you live in the house: every stage leaves it livable, and each one prepares the next.")
for i, (t, s, f) in enumerate([("roof", "stage 1", "green"), ("kitchen", "stage 2", "y"), ("bathrooms", "stage 3", "blue"), ("garden", "stage 4", "paper")]):
    x = 20 + i * 186
    ar_analogy.icon("store", x + 50, 20, 0.9)
    ar_analogy.box(x, 100, 166, 70, t, f, sub=s, size=17)
    if i < 3:
        ar_analogy.arrow(x + 170, 135, x + 182, 135)
ar_analogy.note(380, 226, "livable after every stage", "pen")

ar_how = Doodle(760, 370, "Larder's architecture roadmap for 2027 as transition states, 2 February 2027. T0, today: two cities, StockPilot, one region. T1, by Utrecht in April: Rotterdam's hard-coded settings removed so a city is fully configuration, vans in Dispatch. T2, by The Hague in June and Antwerp in September: WMS B live store by store, French and Dutch in the apps, Belgian VAT and Bancontact refunds, the critical windows protected. T3, by Eindhoven in November: load-tested for 40,000 orders a day at five times peak, cost per order heading for 2.80 euros. Each state is a working platform; each lists what must be true and the ADRs behind it.",
                 "Transition states, each a working platform tied to a city launch, each with what must be true by then.")
states = [("T0 · now", "2 cities · StockPilot", "paper"), ("T1 · Apr", "city = config", "blue"),
          ("T2 · Jun–Sep", "WMS B · FR/NL", "y"), ("T3 · Nov", "40k orders/day", "green")]
for i, (t, s, f) in enumerate(states):
    x = 10 + i * 188
    ar_how.box(x, 30, 172, 100, t, f, sub=s, size=17, subsize=14)
    if i < 3:
        ar_how.arrow(x + 174, 80, x + 186, 80)
for i, (t, s) in enumerate([("must be true", "TD-1 paid, vans"), ("must be true", "WMS B, Bancontact"), ("must be true", "5× peak load test")]):
    x = 198 + i * 188
    ar_how.box(x, 160, 172, 90, t, "paper", sub=s, dash=True, size=14, subsize=13)
ar_how.box(10, 160, 172, 90, "planning dates", "pink", sub="not commitments", size=14, subsize=12)
ar_how.note(380, 296, "The Hague Jun · Antwerp Sep · Eindhoven Nov (planning)", "pen", size=16)
ar_how.note(380, 330, "each state is a working platform", "green", size=18)

ROADMAP = dict(
    slug="architecture-roadmap",
    kicker="a.k.a. “renovating while you live in it”",
    tldr="A list of architecture work isn't a plan. An <b>architecture roadmap</b> describes a few <b>transition states</b> between today and where the business needs to be, each one a <b>working platform</b>, each tied to a <b>business milestone</b> (a city launch, a contract), each with <b>what must be true</b> by then and the decisions behind it. It answers the board's question, “what has to change, and when?”, and it tells teams why their item is in this quarter.",
    chips=[("Family", "keeping it current"), ("Origin", "TOGAF transition architectures; capability-based planning"), ("Lives in", "one page linked from the one-pager; reviewed quarterly"), ("Pairs with", "architecture one-pager, now / next / later roadmap, migration planning")],
    problem_side="Larder, 2 February 2027",
    problem="""  <p class="lead">At the February board meeting, an investor asks Ana: <i>what has to change in the platform for four new cities and a new country this year?</i> Ana's architecture backlog has <b>60 items</b>: TD-1, the WMS B migration, Belgian VAT, French in the apps, load tests, vans… all real, <span class="hl-pink">none in any order</span>. The board sees a pile, not a plan, and teams can't tell which of their items matter for which launch.</p>
  <ul>
    <li>Architecture work is listed, not sequenced.</li>
    <li>Nothing ties technical work to the business milestones it enables.</li>
    <li>Big-bang targets (“the 2027 architecture”) hide what must be true by each launch.</li>
  </ul>""",
    problem_figs=[ar_problem],
    analogy_side="renovating while you live in it",
    analogy="""  <p>A family renovating the house they live in doesn't rip everything out at once. <b>Roof</b> first (nothing else is safe without it), then the <b>kitchen</b>, then the <b>bathrooms</b>, then the <b>garden</b>. After every stage the house is <b>livable</b>, and each stage prepares the next. The plan isn't the list of jobs; it's the order and the livable states in between.</p>""",
    analogy_figs=[ar_analogy],
    map=[("Livable after each stage", "Each transition state is a working platform"),
         ("Roof first", "TD-1 and city configuration before Utrecht"),
         ("Kitchen, then bathrooms", "WMS B, then languages and Belgian VAT for Antwerp"),
         ("The garden last", "Scale for 40,000 orders a day by Eindhoven"),
         ("The list of jobs", "The 60 backlog items, now sorted under states")],
    how_side="a few states, each tied to a launch",
    how="""  <p>Ana drew <b>four states</b>, each tied to a city launch (planning dates, not commitments): <b>T1</b> for Utrecht in April (a city is fully configuration, vans in Dispatch), <b>T2</b> for The Hague in June and Antwerp in September (WMS B, French and Dutch, Belgian VAT and Bancontact refunds), <b>T3</b> for Eindhoven in November (load-tested for 40,000 orders a day). Under each, <b>what must be true</b>, and the ADRs behind it. The 60 items found their homes; eleven belonged to no state and were parked.</p>""",
    how_figs=[ar_how],
    steps=[("Describe today honestly", "T0: what the platform is and can't do yet."),
           ("Anchor states to milestones", "City launches, contracts, peaks: dates the business already has."),
           ("Write what must be true", "For each state: capabilities and quality targets, not tasks."),
           ("Link the decisions", "ADRs and debt items that make each state possible."),
           ("Sort the backlog under states", "Items that fit no state get questioned or parked."),
           ("Review quarterly", "Move dates with the business; keep each state a working platform.")],
    vocab=[("Transition state", "A planned, working version of the architecture on the way to the target."),
           ("Target architecture", "Where the business needs the platform to be."),
           ("Baseline", "The architecture as it is today (T0)."),
           ("Milestone", "A business date a state is tied to."),
           ("Capability", "Something the platform must be able to do."),
           ("Planning date", "A date to plan by, not a promise.")],
    code=dict(file="docs/architecture/roadmap-2027.md", note="Larder's architecture roadmap, 2 February 2027", plain=True, src="""
# Architecture roadmap 2027              planning dates, not commitments · reviewed quarterly

T0  now (Feb)          2 cities (AMS, RTM) · StockPilot · one region · vans in Dispatch
T1  Utrecht (Apr)      a city is fully configuration: TD-1 paid (ADR 0003)
                       Engine A plans vans the evening before (ADR 0015)
                       critical windows protected (ADR 0017)
T2  The Hague (Jun),   WMS B live, store by store; StockPilot off by Sep (ADR 0016)
    Antwerp (Sep)      French and Dutch in the apps · Belgian VAT via billing (0013)
                       Bancontact payments and refunds · data stays in the EU
T3  Eindhoven (Nov)    load test passed: 40,000 orders/day at 5× peak
                       cost per order on track for €2.80 · decision on a 2nd region
Parked (no state)      11 items, e.g. GraphQL for the apps, a second database type
"""),
    tools="tools: one page in the repo; a timeline view in a planning tool if leadership wants it. Enterprise frameworks (TOGAF, ArchiMate's implementation and migration views) formalise the same idea.",
    gains=["<b>The board sees a plan</b>, tied to launches it knows.",
           "<b>Teams see why</b> their item is this quarter.",
           "<b>Each step is safe</b>: a working platform every time.",
           "<b>Backlog clean-up</b>: items with no state get questioned.",
           "<b>Early warning</b> when a state slips behind its launch."],
    losses=["<b>Dates move</b> with the business; the page needs care.",
            "<b>Hard to place</b> enabling work with no visible milestone.",
            "<b>Can look like a promise</b> if the planning dates aren't labelled.",
            "<b>Coarse</b>: states hide the weekly detail."],
    baseline="Each line compares <b>an unordered list of architecture work</b> to <b>a few transition states, each a working platform tied to a business milestone, with what must be true by then</b>.",
    ratings=[(2, 5, "The board and teams read the same plan."),
             (2, 5, "Each state is tied to a city launch."),
             (2, 4, "Teams know which items matter now."),
             (2, 4, "Missing work for a launch shows up months ahead."),
             (3, 4, "Each state is reviewed and can change quarterly."),
             (2, 4, "Each state links its ADRs and debt items."),
             (3, 4, "Cost per order is part of T3."),
             (3, 3, "One page, reviewed quarterly."),
             (2, 4, "Teams plan their own work under the states.")],
    pitfalls=[("A big-bang target", "“The 2027 architecture” with nothing in between.", "two to four working states, tied to milestones."),
              ("Tasks, not states", "A Gantt chart of jobs.", "describe what must be true, then sort tasks under it."),
              ("Dates as promises", "Planning dates read as commitments.", "label them; review quarterly."),
              ("No parking", "Every item squeezed into a state.", "items that fit no state get questioned or parked.")],
    use=["Multi-quarter change tied to business milestones.",
         "Board and investor questions about the platform.",
         "Migrations and new markets.",
         "When the architecture backlog has become a pile."],
    skip=["Small systems with a single next step.",
          "Week-to-week planning: that's the teams' backlogs."],
    related=["<b>Architecture one-pager</b> (this volume)", "<b>Transition architectures</b> (Vol. 4)", "<b>Migration planning</b> (Vol. 6)", "<b>Now / next / later roadmap</b> (Grace, book 2 vol. 2)"],
    quiz=[("What's a transition state?", "A working version of the architecture, on the way to the target, tied to a milestone."),
          ("What goes under each state?", "What must be true by then, and the ADRs and debt items that make it so."),
          ("What happens to items that fit no state?", "They're questioned or parked."),
          ("Why tie states to launches?", "So technical work is anchored to dates the business already cares about.")],
    try_it="Write your platform's today (T0) in three lines. Pick the next two business milestones and, for each, write three things that must be true of the platform by then. Sort your architecture backlog under them and count what fits nowhere.",
    remember="Renovate <span class=\"hl\">room by room</span>, and keep the house <span class=\"hl\">livable</span> after each.",
    sources=["The Open Group, <i>TOGAF Standard</i>, “Transition Architecture” and migration planning.",
             "Gregor Hohpe, <i>The Software Architect Elevator</i> (2020).",
             "Neal Ford et al., <i>Building Evolutionary Architectures</i>, 2nd ed. (2022).",
             "Martin Fowler, “StranglerFigApplication” (martinfowler.com, 2004)."],
)

# ------------------------------------------------------------------ 15 Glossary & Ubiquitous Language
gl_problem = Doodle(760, 280, "Doodle of January 2027's monthly report for Korenwolf. The report says 96.1 percent complete deliveries, below the 98 percent in the contract, because it counted each crate as a delivery. The contract defines a delivery as everything for one office on one morning: by that measure it was 98.6 percent. Mo has an uncomfortable call with Ruben over one word.",
                    "One word, two meanings: 96.1 % by crate, 98.6 % by office-morning, and an uncomfortable call.")
gl_problem.box(20, 30, 330, 100, "report: 96.1 %", "pink", sub="“delivery” = a crate", stroke="red")
gl_problem.box(410, 30, 330, 100, "contract: 98 %", "green", sub="“delivery” = office + morning")
gl_problem.box(170, 170, 420, 64, "Mo ↔ Ruben, a hard call", "y", size=17)
gl_problem.note(380, 264, "real figure: 98.6 %", "pen")

gl_analogy = Doodle(760, 250, "Doodle of a football rulebook's definitions page: what counts as a goal, what counts as offside, what a handball is. Players, referees and commentators argue about the game, not about the words, because the words are defined.",
                     "A rulebook defines “goal” and “offside”, so everyone argues about the game, not the words.")
gl_analogy.icon("book", 40, 60, 1.6)
for i, (t, s, f) in enumerate([("goal", "ball over the line", "green"), ("offside", "the defined position", "y"), ("handball", "arm, deliberate…", "blue")]):
    x = 170 + i * 196
    gl_analogy.box(x, 60, 180, 84, t, f, sub=s, size=17, subsize=13)
gl_analogy.note(450, 210, "argue about the game, not the words", "pen")

gl_how = Doodle(760, 370, "Larder's glossary, 9 February 2027: one row per word that matters, with its meaning in each context, what not to confuse it with, and its name in the code. Examples: delivery means a courier drop in Dispatch, but everything for one office on one morning in Larder for Business; order means a basket in Ordering, a pick list in Fulfilment, a drop in Dispatch; standing order means a business account's weekly order; account means a customer login, a business account, or a client in Mo's CRM. The glossary is used in code, docs, contracts and reports.",
                 "Each word, its meaning in each context, what not to confuse it with, and its name in the code.")
gl_how.head(20, 34, "word", anchor="start", size=15)
gl_how.head(170, 34, "means (in context)", anchor="start", size=15)
gl_how.head(590, 34, "in code", anchor="start", size=15)
rows = [("delivery", "Dispatch: a drop · Business: office + morning", "Drop · OfficeDelivery", "pink"),
        ("order", "a basket · a pick list · a drop", "Order · PickList · Drop", "y"),
        ("standing order", "a business account's weekly order", "StandingOrder", "paper"),
        ("account", "login · business account · CRM client", "CustomerAccount …", "blue")]
for i, (w, m, c, f) in enumerate(rows):
    y = 52 + i * 66
    gl_how.box(12, y, 736, 56, None, f, rx=6)
    gl_how.text(22, y + 34, w, "t-head", anchor="start", size=15)
    gl_how.text(170, y + 34, m, anchor="start", size=14)
    gl_how.text(590, y + 34, c, anchor="start", size=12)
gl_how.note(380, 340, "used in code, docs, contracts and reports", "green", size=18)

GLOSSARY = dict(
    slug="glossary",
    kicker="a.k.a. “the rulebook's definitions page”",
    tldr="Most expensive misunderstandings are about <b>words</b>, not technology. Keep a <b>glossary</b> of the words that matter: each with its <b>meaning in each context</b> (a word can mean different things in different bounded contexts, and that's fine if it's written down), what <b>not to confuse it with</b>, and its <b>name in the code</b>. Use the same words in code, docs, contracts and reports: Domain-Driven Design calls it a <b>ubiquitous language</b>.",
    chips=[("Family", "keeping it current"), ("Origin", "Eric Evans, <i>Domain-Driven Design</i> (2003): ubiquitous language; arc42 section 12"), ("Lives in", "docs/architecture/12-glossary.md, linked from contracts and reports"), ("Pairs with", "bounded contexts, event storming, arc42")],
    problem_side="Larder, 9 February 2027",
    problem="""  <p class="lead">January's first monthly report for Korenwolf's three offices says <b>96.1 % complete deliveries</b>, below the <b>98 %</b> in the contract. Ruben calls Mo, unhappy. The cause: the report counted each <b>crate</b> as a delivery. The contract defines a delivery as <b>everything for one office on one morning</b>. By that measure, January was <b>98.6 %</b>. <span class="hl-pink">One word, two meanings</span>, and a client's trust dented over arithmetic.</p>
  <ul>
    <li>The same word means different things to Dispatch, Fulfilment, sales and the contract.</li>
    <li>Reports and code pick a meaning silently.</li>
    <li>Every new hire and every new client learns the words by accident.</li>
  </ul>""",
    problem_figs=[gl_problem],
    analogy_side="the rulebook's definitions page",
    analogy="""  <p>A football rulebook defines <b>“goal”</b> (the whole ball over the whole line), <b>“offside”</b> and <b>“handball”</b>. Players, referees and commentators still argue, but about the <b>game</b>, not about what the words mean. A league where every referee had their own definition of a goal wouldn't last a season.</p>""",
    analogy_figs=[gl_analogy],
    map=[("“Goal”", "“Delivery”: a drop in Dispatch; office + morning in the contract"),
         ("“Offside”", "“Order”: a basket, a pick list or a drop, by context"),
         ("The definitions page", "docs/architecture/12-glossary.md"),
         ("Referees using it", "Reports, code and contracts using the same terms"),
         ("Arguing about the game", "Talking about service levels, not about words")],
    how_side="each word, per context, in the code too",
    how="""  <p>Ana and Mo wrote the glossary in an afternoon, starting from the words in the Korenwolf contract and the bounded contexts from Vol. 1. Each row says what the word means <b>in each context</b>, what not to confuse it with, and its <b>name in the code</b>, so the report now uses <code>OfficeDelivery</code>, not a count of crates. Mo sent Ruben the corrected report (98.6 %) with the definition attached. The glossary became arc42 section 12, and the contract template links to it.</p>""",
    how_figs=[gl_how],
    steps=[("Start from a misunderstanding", "The word that just caused trouble, then the contract's and the domain's key words."),
           ("One row per word", "Meaning, in each bounded context; what not to confuse it with."),
           ("Add the code name", "The class, table or event name, so code and words match."),
           ("Use it everywhere", "Reports, contracts, docs, tickets; rename code where it disagrees."),
           ("Add words as they appear", "New client, new country, new feature: new rows."),
           ("Review with outsiders", "Sales, legal, a client: do they read the words the same way?")],
    vocab=[("Ubiquitous language", "The shared words used by business and code alike."),
           ("Bounded context", "An area where a word has one meaning."),
           ("Glossary", "The list of words that matter and what they mean."),
           ("Homonym", "One word with several meanings (delivery)."),
           ("Synonym", "Several words for one thing (drop, stop, delivery)."),
           ("Context map", "How bounded contexts relate and translate words.")],
    code=dict(file="docs/architecture/12-glossary.md", note="arc42 section 12, February 2027 (excerpt)", plain=True, src="""
# 12. Glossary                                          owners: Ana, Mo · Feb 2027

| Word           | Context            | Means                                     | Not to confuse with      | In code          |
|----------------|--------------------|-------------------------------------------|--------------------------|------------------|
| Delivery       | Dispatch           | one drop at one address by one courier    | office delivery          | Drop             |
| Delivery       | Larder for Business| everything for one office, one morning;   | a crate, a drop          | OfficeDelivery   |
|                | (contracts)        | "complete" = all lines delivered by 09:00 |                          |                  |
| Order          | Ordering           | a customer's basket, from checkout        | pick list, drop          | Order            |
| Order          | Fulfilment         | the pick list for one store               | basket                   | PickList         |
| Standing order | Ordering           | a business account's repeating weekly order| subscription            | StandingOrder    |
| Account        | Ordering           | a customer's login                        | business account         | CustomerAccount  |
| Business acct  | Ordering           | an office that orders on invoice          | Mo's CRM client          | BusinessAccount  |

Korenwolf report, Jan 2027: 96.1 % (by crate, wrong) → 98.6 % (by OfficeDelivery).
"""),
    tools="tools: a Markdown table in the repo (arc42 section 12); context maps from DDD; linters or code review for naming; a link to the glossary from contract templates and report definitions.",
    gains=["<b>Fewer expensive misunderstandings</b> with clients and teams.",
           "<b>Code and business speak alike</b>.",
           "<b>Faster onboarding</b> for new hires and new clients.",
           "<b>Reports that match contracts</b>.",
           "<b>Bounded contexts made visible</b> in plain words."],
    losses=["<b>Upkeep</b>: new words, new contexts.",
            "<b>Renaming code</b> to match costs effort.",
            "<b>Can turn pedantic</b> if every word gets a row.",
            "<b>Doesn't help</b> if nobody links to it."],
    baseline="Each line compares <b>words used loosely, with meanings picked silently in code and reports</b> to <b>a glossary of key words per context, with code names, used in docs, contracts and reports</b>.",
    ratings=[(2, 5, "One definition per word, per context."),
             (2, 5, "Mo, Ruben, the report and the code mean the same thing."),
             (3, 4, "Fewer arguments about words."),
             (2, 4, "Contract and report mismatches caught early."),
             (3, 3, "Neutral."),
             (2, 4, "The definitions behind every report are on record."),
             (3, 3, "Neutral."),
             (3, 4, "An afternoon, then a row now and then."),
             (2, 4, "Teams and sales check words without asking Ana.")],
    pitfalls=[("One meaning forced everywhere", "“Order” must mean the same in every context.", "write the meaning per context; that's what bounded contexts are."),
              ("A glossary nobody links", "A page in a corner.", "link it from contracts, reports and onboarding."),
              ("Code disagrees", "The docs say OfficeDelivery; the code says Delivery.", "rename the code, or note the mapping."),
              ("Every word", "A dictionary of 400 terms.", "only words that matter or have caused trouble.")],
    use=["Client contracts with measured service levels.",
         "Systems with several bounded contexts.",
         "Onboarding new hires and new clients.",
         "After any misunderstanding about a word."],
    skip=["Tiny teams in one domain where words never collide.",
          "Generic technical terms: link to an external glossary."],
    related=["<b>Bounded contexts</b> (Vol. 1)", "<b>arc42 template</b> (this volume)", "<b>Domain discovery (event storming)</b> (Vol. 1)", "<b>Canonical data model (and its traps)</b> (Vol. 4)"],
    quiz=[("Why did January's report show 96.1 %?", "It counted crates as deliveries; the contract defines a delivery per office per morning."),
          ("Can a word mean different things?", "Yes, in different bounded contexts, as long as each meaning is written down."),
          ("What columns does a good glossary have?", "Word, context, meaning, not to confuse with, name in code."),
          ("What's a ubiquitous language?", "Shared words used the same way by the business and in the code.")],
    try_it="List the ten words your team and your customers use most. For each, ask three people (an engineer, a product person, a salesperson) what it means. Write the glossary rows where they disagree, and link it from your contracts or reports.",
    remember="Define the <span class=\"hl\">goal</span> before the match. One word, <span class=\"hl\">per context</span>, in the code too.",
    sources=["Eric Evans, <i>Domain-Driven Design</i> (2003), ubiquitous language.",
             "Vaughn Vernon, <i>Domain-Driven Design Distilled</i> (2016).",
             "arc42, section 12 “Glossary” (arc42.org).",
             "Alberto Brandolini, <i>Introducing EventStorming</i> (Leanpub)."],
)

NOTES = [LIVING, ROADMAP, GLOSSARY]
