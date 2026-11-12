# Series 2 · The Solution Architect's Notebook · Vol. 1 · First shapes.
# Running case study: Larder (facts in docs/larder-casebook.md).

# ------------------------------------------------------------------ 09 Architecture Styles Compared
st_problem = Doodle(760, 270, "Doodle of the team splitting into camps. Ben wants microservices because of a conference talk. Eli wants serverless because it sounds cheap. Cho wants everything event-driven on Kafka. Each argues from a favourite, with no shared criteria, and the meeting series runs for three weeks without a decision.",
                    "Three favourites, no shared yardstick, three weeks of meetings.")
for i, (who, style, why) in enumerate([("Ben", "microservices", "“Netflix does it”"), ("Eli", "serverless", "“pay per use!”"), ("Cho", "event-driven", "“Kafka for everything”")]):
    x = 20 + i * 246
    st_problem.box(x, 24, 226, 90, style, "blue", sub=f"{who}: {why}", size=18, subsize=15)
for x in (133, 379, 625):
    st_problem.line(f"M{x} 120 L380 166", dash=True, thin=True, color="red")
st_problem.box(240, 170, 280, 60, "meeting #6, no decision", "pink", stroke="red", size=17)
st_problem.note(380, 258, "nobody asked: which one serves our drivers?", "red")

st_analogy = Doodle(760, 260, "Doodle of four vehicles, each best at one job: a cargo bike for a florist in the city centre, a van for a plumber, a lorry for a removal company, a train for moving coal across the country. Nobody asks which vehicle is best; they ask what the job is.",
                    "Nobody asks “which vehicle is best?” They ask what the job is.")
for i, (ic, name, job) in enumerate([("chassis", "cargo bike", "florist, city centre"), ("truck", "van", "plumber, a few tools"), ("container", "lorry", "removals, one-off"), ("ship", "train", "coal, every day")]):
    x = 20 + i * 186
    sc = 1.3 if ic != "ship" else 1.0
    st_analogy.icon(ic, x + 40, 30, sc)
    st_analogy.box(x, 130, 170, 80, name, "y" if i == 0 else "paper", sub=job, size=18, subsize=14)
st_analogy.note(380, 246, "load · distance · streets · budget · who drives it", "pen")

st_how = Doodle(760, 380, "Comparing five architecture styles against Larder's needs. Rows: layered monolith, modular monolith, microservices, event-driven, serverless. Columns: simple to run, fits 14 engineers, teams deploy alone, scale parts separately, low run cost. The modular monolith scores well on simplicity, team fit and cost, medium on independent deploys; microservices score high on independence and scaling but low on simplicity and team fit. Larder chooses the modular monolith, with one part, Dispatch, as a separate service.",
                 "Score styles against your drivers, not against each other. Larder's fit: modular monolith + one service.")
cols = [("simple", "to run"), ("fits", "14 eng."), ("deploy", "alone"), ("scale", "parts"), ("low", "cost")]
rows = [("layered monolith", [3, 3, 1, 1, 3]), ("modular monolith", [3, 3, 2, 2, 3]), ("microservices", [1, 1, 3, 3, 1]),
        ("event-driven", [1, 2, 3, 3, 2]), ("serverless", [2, 2, 3, 3, 2])]
for k, c in enumerate(cols):
    st_how.head(270 + k * 100, 22, c[0], size=15)
    st_how.head(270 + k * 100, 44, c[1], size=15)
for i, (name, sc) in enumerate(rows):
    y = 60 + i * 54
    hl = i == 1
    st_how.box(14, y, 732 if hl else 186, 46, None, "green" if hl else "paper", rx=6)
    st_how.text(26, y + 30, name, "t-head" if hl else "t", anchor="start", size=16)
    for k, v in enumerate(sc):
        cx = 270 + k * 100
        for d in range(3):
            fill = "f-ink" if d < v else "f-paper"
            st_how.raw(f'<circle class="d d-thin {fill}" cx="{cx - 18 + d * 18}" cy="{y + 23}" r="6"/>')
st_how.note(380, 348, "+ Dispatch as its own service: real-time, scales differently", "pen")
st_how.note(380, 374, "●●● good fit · ●○○ poor fit, for Larder in 2025", "pen", size=17)

STYLES = dict(
    slug="architecture-styles",
    kicker="a.k.a. “pick the vehicle for the job”",
    tldr="Every architecture style (<b>layered monolith, modular monolith, microservices, event-driven, serverless</b>) is great at some things and costly at others. Don't argue favourites. List the qualities your <b>drivers and ASRs</b> need, add your real <b>team size, skills and budget</b>, score each style against them, and pick the <b>simplest one that fits</b>. Most systems mix styles: a main shape plus a few parts that need something different.",
    chips=[("Family", "first shapes"), ("Origin", "Mark Richards &amp; Neal Ford, <i>Fundamentals of Software Architecture</i> (2020), style ratings"), ("Lives in", "an options table in the decision's ADR"), ("Pairs with", "options analysis, modular monolith, ASRs")],
    problem_side="Larder, meeting number six",
    problem="""  <p class="lead">The question is simple: what shape should the six-city platform have? The team splits into camps. Ben wants <b>microservices</b> (“Netflix does it”), Eli wants <b>serverless</b> (“we only pay for use”), Cho wants everything <b>event-driven</b> on Kafka. Each argues from a favourite and a conference talk. Three weeks and <span class="hl-pink">six meetings</span> later, there's no decision.</p>
  <ul>
    <li>Styles are compared to each other, not to the system's needs.</li>
    <li>Team size, skills and budget are left out, though they often decide it.</li>
    <li>Without shared criteria, the most confident voice wins, or nobody does.</li>
  </ul>""",
    problem_figs=[st_problem],
    analogy_side="choosing a vehicle",
    analogy="""  <p>A florist in the city centre uses a <b>cargo bike</b>, a plumber a <b>van</b>, a removals firm a <b>lorry</b>, a coal mine a <b>train</b>. None of them is the “best vehicle”. Each is the right one for a <b>load, a distance, the streets, a budget and whoever drives it</b>. Buying a lorry to deliver flowers is expensive and slow.</p>""",
    analogy_figs=[st_analogy],
    map=[("The load and the distance", "Your qualities: scale, availability, change"),
         ("Narrow city streets", "Constraints: one region, compliance, legacy systems"),
         ("Who drives it", "Team size and skills: 14 engineers, Python and Postgres"),
         ("Fuel and insurance", "Run cost and operational effort"),
         ("A van plus a cargo bike for the centre", "A main style plus a different style for one part")],
    how_side="score against drivers, pick the simplest fit",
    how="""  <p>Use the qualities from your drivers and ASRs as columns, add <b>team fit</b> and <b>cost</b>, and score each style roughly (good / medium / poor). The aim isn't a precise number; it's a conversation <b>about the system</b> instead of about favourites. Then check: is one part different enough to deserve its own style?</p>""",
    how_figs=[st_how],
    steps=[("List the deciding qualities", "From drivers and ASRs: simplicity, deployability, scalability, availability, cost, team fit."),
           ("Add the people and money facts", "Team size, skills, hiring budget, ops maturity. These often decide."),
           ("Score each style", "Good / medium / poor for each quality, using a shared reference (Richards &amp; Ford's ratings help)."),
           ("Pick the simplest that fits", "When two fit, take the one with fewer moving parts."),
           ("Look for the odd part out", "A part with very different needs (real-time, huge spikes) may deserve its own style."),
           ("Record it as an ADR", "The table, the choice and when to revisit (e.g. “at 30 engineers”).")],
    vocab=[("Layered monolith", "One deployable app, split into technical layers (UI, logic, data)."),
           ("Modular monolith", "One deployable app, split into business modules with strict boundaries."),
           ("Microservices", "Many small services, each deployed and owning data separately."),
           ("Event-driven", "Parts react to events on a broker instead of calling each other."),
           ("Serverless", "Functions and managed services; the provider runs the servers."),
           ("Architecture quantum", "A part that can be deployed independently with its own qualities.")],
    code=dict(file="docs/adr/0002-modular-monolith-extract-dispatch.md", note="the options table from ADR 0002", plain=True, src="""
## Options: shape of the six-city platform               (3 good · 2 medium · 1 poor)

| Quality (weight)          | Layered  | Modular  | Micro-   | Event-   | Server- |
|                           | monolith | monolith | services | driven   | less    |
|---------------------------|----------|----------|----------|----------|---------|
| Simple to run (×3)        | 3        | 3        | 1        | 1        | 2       |
| Fits 14 engineers (×3)    | 3        | 3        | 1        | 2        | 2       |
| City = config (ASR-1, ×2) | 2        | 3        | 2        | 2        | 2       |
| Teams deploy alone (×1)   | 1        | 2        | 3        | 3        | 3       |
| Scale parts apart (×1)    | 1        | 2        | 3        | 3        | 3       |
| Low run cost (×2)         | 3        | 3        | 1        | 2        | 2       |
| Weighted total            | 31       | 36       | 21       | 26       | 28      |

Decision: modular monolith. Dispatch (courier locations every 5 s, real-time)
is extracted as a separate service. Revisit when we pass ~30 engineers.
"""),
    tools="tools: a spreadsheet or Markdown table. Richards &amp; Ford's style rating charts are a good shared starting point; the ThoughtWorks Technology Radar shows how others rate specific approaches.",
    gains=["<b>Decisions end</b>: criteria replace favourites.",
           "<b>Fit to the real team</b>: size, skills and budget are part of the choice.",
           "<b>Simpler systems</b>: the simplest fit usually wins.",
           "<b>Mixing on purpose</b>: odd parts get a different style, deliberately.",
           "<b>A record</b>: the table goes into the ADR, with a revisit trigger."],
    losses=["<b>Scores are rough</b> and can be argued.",
            "<b>Weights can be gamed</b> to favour a chosen answer.",
            "<b>Takes a workshop</b> to agree the qualities and scores.",
            "<b>Hides detail</b>: “microservices” covers many very different designs."],
    baseline="Each line compares <b>choosing a style by favourite or fashion</b> to <b>scoring styles against the drivers, ASRs, team and budget, and recording the result in an ADR</b>.",
    ratings=[(2, 4, "The reasons for the shape are written in one table."),
             (2, 4, "Engineers and sponsors agree on the criteria first."),
             (1, 4, "One workshop instead of six meetings."),
             (2, 4, "Mismatches (team too small, ops too heavy) show up before building."),
             (3, 4, "A revisit trigger (“at 30 engineers”) plans the next change."),
             (2, 4, "The ADR keeps the table and the weights."),
             (2, 4, "Run cost and ops effort are columns, not afterthoughts."),
             (3, 3, "Half a day to agree criteria and score."),
             (3, 3, "Neutral; the chosen style decides that.")],
    pitfalls=[("Fashion-driven", "“Everyone uses microservices now.”", "score against your drivers and team, not other companies'."),
              ("Ignoring the team", "A 14-person team picks a style built for 400.", "make team size and skills a weighted column."),
              ("Reverse-engineered weights", "Weights tweaked until the favourite wins.", "agree the qualities and weights before scoring any style."),
              ("One style for everything", "A real-time part is forced into a batch-friendly shape.", "check for the odd part out and give it its own style.")],
    use=["Choosing the shape of a new system or a rebuild.",
         "When a team is split between favourite styles.",
         "When the team, scale or business has changed a lot since the last choice.",
         "Explaining the choice to sponsors and new joiners."],
    skip=["Small systems where a plain monolith is obviously enough.",
          "When the organisation has a standard platform that already decides it.",
          "Detailed design inside one module: that's a different decision."],
    related=["<b>Modular monolith first</b> (this volume)", "<b>Options analysis</b> (Vol. 2)", "<b>Architecture decision records</b> (Vol. 2)", "<b>Publish–subscribe</b> (patterns, Vol. 1)"],
    quiz=[("Why score styles against drivers rather than against each other?", "Because no style is best in general; the right one depends on the system's qualities, team and budget."),
          ("Which non-technical facts often decide the style?", "Team size, skills, hiring budget and how mature the operations are."),
          ("When two styles fit, which should you pick?", "The simpler one, with fewer moving parts."),
          ("What's the “odd part out” check?", "Looking for a part with very different needs that deserves its own style, like Larder's real-time Dispatch.")],
    try_it="List five qualities your system needs most, plus “fits our team” and “low run cost”. Score three styles against them in 20 minutes with a colleague who disagrees with you. Did the scores change either of your minds?",
    remember="No <span class=\"hl\">best vehicle</span>, only the right one for <span class=\"hl\">this load and this driver</span>.",
    sources=["Mark Richards &amp; Neal Ford, <i>Fundamentals of Software Architecture</i> (2020), part II.",
             "Martin Fowler, “MonolithFirst” and “Microservice Premium” (martinfowler.com, 2015).",
             "Sam Newman, <i>Building Microservices</i>, 2nd ed. (2021), chapter 1.",
             "ThoughtWorks Technology Radar (thoughtworks.com/radar)."],
)

# ------------------------------------------------------------------ 10 Modular Monolith First
mm_problem = Doodle(760, 290, "Two bad options for Larder Core. On the left, today: one Django app where every part reads every table, so changing pricing broke the picking export. On the right, the proposal: split into eight microservices with fourteen engineers, under two engineers per service, and boundaries nobody is sure of yet.",
                    "Today: a ball of mud. The proposal: eight services for fourteen people, cut along guesses.")
mm_problem.box(20, 20, 330, 200, None, "paper")
mm_problem.head(185, 48, "Larder Core today", size=17)
pts = [(75, 90), (185, 80), (290, 100), (85, 172), (190, 160), (295, 182)]
names = ["shop", "pricing", "orders", "picking", "stock", "support"]
for (x, y), n in zip(pts, names):
    mm_problem.box(x - 48, y - 16, 96, 32, n, "blue", size=13, rx=6)
for a in range(6):
    for b in range(a + 1, 6):
        if (a + b) % 2 == 0 or b - a == 1:
            mm_problem.line(f"M{pts[a][0]} {pts[a][1] + 16} L{pts[b][0]} {pts[b][1] - 16}", thin=True, color="red")
mm_problem.note(185, 250, "pricing change broke picking", "red")
mm_problem.box(410, 20, 330, 200, None, "paper", dash=True)
mm_problem.head(575, 48, "proposal: 8 services", size=17)
for i in range(8):
    mm_problem.box(430 + (i % 4) * 76, 70 + (i // 4) * 60, 64, 44, None, "y", rx=6)
mm_problem.text(575, 206, "14 engineers · 8 pipelines · 8 on-calls", size=15)
mm_problem.note(575, 250, "and the boundaries are guesses", "red")

mm_analogy = Doodle(760, 250, "Doodle of a bento box: one box you carry as a whole, with separate compartments that don't mix. Rice, fish, salad and fruit each have their own space. If one day the fruit needs to be cold, you lift that compartment out into its own container.",
                    "A bento box: carried as one, but nothing leaks between compartments. One can be lifted out later.")
mm_analogy.icon("bento", 40, 40, 2.4)
mm_analogy.note(124, 222, "one box, separate compartments", "pen")
mm_analogy.arrow(250, 110, 330, 110, dash=True, label="later", lx=290, ly=96)
mm_analogy.box(340, 70, 150, 80, "fruit", "green", sub="own cold box", size=18, subsize=14)
mm_analogy.box(530, 40, 210, 140, None, "pink", stroke="red")
mm_analogy.head(635, 70, "one big pot", size=17, color="red")
mm_analogy.text(635, 104, "everything mixed:", size=15)
mm_analogy.text(635, 128, "the ball of mud", size=15)

mm_how = Doodle(760, 360, "Larder's target shape. One deployable app, Larder Core, contains modules: Catalogue, Pricing, Ordering, Payments, Stock, Fulfilment and Customer Care. Each module owns its own tables and exposes a small public API; modules may only call each other's public APIs, never each other's tables. A CI check enforces the rules. Dispatch runs outside as a separate service because it is real-time and scales differently, and Ordering talks to it through events.",
                 "One deployable, strict modules that own their data, and one service extracted for a reason.")
mm_how.box(14, 14, 560, 300, None, "paper")
mm_how.head(294, 42, "Larder Core · one deploy", size=18)
mods = ["Catalogue", "Pricing", "Ordering", "Payments", "Stock", "Fulfilment", "Care"]
for i, m in enumerate(mods):
    col, row = i % 4, i // 4
    x, y = 30 + col * 136, 66 + row * 120
    mm_how.box(x, y, 122, 96, None, "blue" if m != "Ordering" else "y")
    mm_how.head(x + 61, y + 40, m, size=16)
    mm_how.db(x + 61, y + 60, w=40, h=14)
    mm_how.box(x + 40, y - 8, 42, 14, None, "green", rx=3)
mm_how.box(438, 186, 122, 96, "api ports", "green", sub="the only door", size=15, subsize=13)
mm_how.arrow(580, 120, 640, 120, dash=True, label="events", lx=610, ly=106)
mm_how.box(644, 74, 104, 100, "Dispatch", "y", sub="own service", size=17, subsize=13)
mm_how.note(696, 200, "real-time", "pen", size=17)
mm_how.note(696, 224, "scales apart", "pen", size=17)
mm_how.note(294, 344, "rules: own your tables · call only public APIs · CI check fails if broken", "pen", size=17)

MODULAR_MONOLITH = dict(
    slug="modular-monolith",
    kicker="a.k.a. “the bento box”",
    tldr="Start as <b>one deployable application</b>, but split it inside into <b>business modules</b> with hard rules: each module <b>owns its data</b>, others reach it only through a small <b>public API</b>, and a <b>CI check</b> fails the build when someone breaks a boundary. You get most of the structure of microservices without the network, the eight pipelines and the eight on-call rotas. When one module really needs to be separate, it's ready to <b>lift out</b>.",
    chips=[("Family", "first shapes"), ("Origin", "Simon Brown, “modular monoliths” (2015); Martin Fowler, “MonolithFirst” (2015)"), ("Lives in", "one repo and one deploy, folders per module"), ("Pairs with", "bounded contexts, fitness functions, strangler fig")],
    problem_side="Larder, two bad options",
    problem="""  <p class="lead">Larder Core is one Django app where every part reads every table. Last month a change to pricing <span class="hl-pink">broke the picking export</span>. Ben's answer is to split it into <b>eight microservices</b>. But Larder has <b>14 engineers</b>: under two per service, each needing its own pipeline, monitoring and on-call. And the event storming was three weeks ago: <b>nobody is sure yet where the boundaries are</b>.</p>
  <ul>
    <li>A tangled monolith makes every change risky.</li>
    <li>Microservices fix the tangle but add a network, distributed data and heavy operations.</li>
    <li>Cutting services along wrong boundaries is the most expensive mistake to undo.</li>
  </ul>""",
    problem_figs=[mm_problem],
    analogy_side="the bento box",
    analogy="""  <p>A <b>bento box</b> is carried as one thing, but rice, fish, salad and fruit each have their <b>own compartment</b> and nothing leaks between them. If the fruit one day needs to stay cold, you lift that compartment out into its own container. Compare a <b>pot of stew</b>, where everything has mixed, or <b>eight separate takeaway boxes</b>, which are a lot to carry for one lunch.</p>""",
    analogy_figs=[mm_analogy],
    map=[("One box you carry", "One deployable application, one pipeline"),
         ("Compartments", "Business modules: Ordering, Payments, Fulfilment…"),
         ("Nothing leaks between them", "Each module owns its tables; others use its public API"),
         ("Lifting one compartment out", "Extracting a module as a service when it needs to be separate"),
         ("A pot of stew", "The big ball of mud you're trying to avoid")],
    how_side="one deploy, hard walls inside",
    how="""  <p>The value is in the <b>rules</b>, not the folders. Without enforcement, a modular monolith decays back into mud within months. With it, the boundaries can be <b>moved cheaply</b> while you learn: moving code between folders is a refactor; moving it between services is a migration.</p>""",
    how_figs=[mm_how],
    steps=[("Draw modules from the domain", "Use bounded contexts from the event storming, not technical layers."),
           ("Give each module its data", "Its own schema or table prefix. No other module reads or writes it."),
           ("Expose a small public API", "One interface per module (functions or events). Everything else is internal."),
           ("Enforce it in CI", "An import or architecture test fails the build on a forbidden dependency."),
           ("Communicate by events where possible", "In-process events today become messages tomorrow, if a module moves out."),
           ("Extract only with a reason", "Different scaling, availability, release pace or team: write an ADR for each extraction.")],
    vocab=[("Modular monolith", "One deployable app made of strictly separated business modules."),
           ("Module", "A business area with its own code, data and public API."),
           ("Public API (of a module)", "The only way other modules may use it."),
           ("Big ball of mud", "A system with no clear structure; everything depends on everything."),
           ("Extraction", "Moving a module out into its own service."),
           ("Distributed monolith", "Microservices that must all be deployed together: the worst of both.")],
    code=dict(file="larder_core/ (layout) + README", note="module layout and the three rules", plain=True, src="""
larder_core/
  catalogue/      api.py   events.py   models.py   _internal/...
  pricing/        api.py   events.py   models.py   _internal/...
  ordering/       api.py   events.py   models.py   _internal/...
  payments/       api.py   events.py   models.py   _internal/...
  stock/          api.py   events.py   models.py   _internal/...
  fulfilment/     api.py   events.py   models.py   _internal/...
  care/           api.py   events.py   models.py   _internal/...
  shared/         money.py   ids.py   clock.py        (tiny, no business logic)

Rules (ADR 0002), checked by CI (see .importlinter):
 1. A module's tables are its own. Table names start with the module name.
 2. Other modules import only <module>.api and <module>.events.
 3. No module imports another's _internal, models or tables.

Dispatch is a separate service (repo: dispatch/). Ordering publishes
OrderReadyForDispatch; Dispatch publishes CourierAssigned and OrderDelivered.
"""),
    tools="tools: import-linter (Python), ArchUnit (Java), dependency-cruiser (JS/TS), Spring Modulith, Packwerk (Ruby), .NET NetArchTest. Each turns the module rules into a failing test.",
    gains=["<b>Simple to run</b>: one deploy, one database, one on-call.",
           "<b>Clear ownership</b>: each module has an owner and its own data.",
           "<b>Cheap to fix boundaries</b>: moving code between modules is a refactor.",
           "<b>Ready to extract</b>: a well-kept module can become a service later.",
           "<b>Fast local calls</b>: no network between modules."],
    losses=["<b>One deploy for all</b>: a bad change in one module ships with the rest.",
            "<b>Scaling together</b>: you can't scale one module alone (until you extract it).",
            "<b>Discipline needed</b>: without CI rules, it decays into mud.",
            "<b>One tech stack</b>: every module uses the same language and runtime."],
    baseline="Each line compares <b>Larder Core as a tangled monolith</b> to <b>a modular monolith with module-owned data, public APIs and CI-enforced rules, plus Dispatch as one extracted service</b>.",
    ratings=[(2, 4, "Each module's job and data are obvious from the layout."),
             (3, 3, "Mostly an engineering matter; sponsors see faster delivery."),
             (2, 4, "Teams decide inside their module without a cross-team meeting."),
             (2, 4, "A change in pricing can no longer silently break picking."),
             (2, 5, "Boundaries can move cheaply while the domain is still being learned."),
             (2, 4, "Module rules and extractions are recorded in ADRs."),
             (3, 5, "One deploy and one database cost far less than eight."),
             (3, 4, "One pipeline and on-call; a few CI rules to maintain."),
             (2, 4, "Each team owns a module end to end.")],
    pitfalls=[("Folders without rules", "Modules exist on paper; imports cross everywhere.", "enforce boundaries with a failing CI check from day one."),
              ("Shared tables", "Two modules write the same orders table.", "one owner per table; others go through the owner's API or events."),
              ("Technical modules", "Modules named controllers, services, repositories.", "split by business area (bounded contexts), not by layer."),
              ("Extracting for fashion", "A module becomes a service because services are “better”.", "extract only for a written reason: scaling, availability, team, release pace.")],
    use=["New systems or rebuilds with teams under about 30 engineers.",
         "When the domain boundaries aren't settled yet.",
         "Untangling a ball-of-mud monolith step by step.",
         "When operations capacity is small."],
    skip=["Parts with very different scaling or availability needs: extract those.",
          "Large organisations where many teams need fully independent releases.",
          "When parts must use different languages or runtimes."],
    related=["<b>Architecture styles compared</b> (this volume)", "<b>Bounded contexts</b> (this volume)", "<b>Fitness functions</b> (this volume)", "<b>Strangler fig migration</b> (Vol. 4)"],
    quiz=[("What are the three rules of a modular monolith?", "Each module owns its data; others use only its public API; the rules are enforced by an automated check."),
          ("Why is it cheaper to fix boundaries in a modular monolith than between services?", "Moving code between modules is a refactor in one repo; moving it between services is a data and network migration."),
          ("What's a distributed monolith?", "Services that must be deployed together because they're tightly coupled: all the costs of both styles."),
          ("Why did Larder extract Dispatch?", "It's real-time (courier locations every 5 s) and scales differently from the rest.")],
    try_it="Pick two areas in your codebase that should be separate (for example, billing and notifications). Count how many places one reaches into the other's tables or internals. Write the one rule that would stop it, and find the tool that could check it in CI.",
    remember="<span class=\"hl\">One box</span>, <span class=\"hl\">hard walls</span>. Lift a compartment out only when you have a reason.",
    sources=["Simon Brown, “Modular Monoliths” (talk, 2015) and <i>Software Architecture for Developers</i>.",
             "Martin Fowler, “MonolithFirst” (martinfowler.com, 2015).",
             "Kamil Grzybek, “Modular Monolith: A Primer” (kamilgrzybek.com, 2019).",
             "Sam Newman, <i>Monolith to Microservices</i> (2019)."],
)

# ------------------------------------------------------------------ 11 Bounded Contexts
bc_problem = Doodle(760, 280, "Doodle of Larder's single orders table with 64 columns, used by everyone. Ordering adds a courier tip column; the picking export, which also reads the table, breaks. Three teams mean three different things by 'order': a basket with prices, a pick list with shelf positions, and a drop with an address and a time slot.",
                    "One word, one table, three meanings, and a 64-column table everyone is afraid to touch.")
bc_problem.table(270, 20, "orders (64 cols)", ["id", "customer_id", "total_eur", "shelf_pos", "picker_id", "courier_id", "tip_eur  ← new", "…57 more"], w=220, hl=(6,), soft=(7,))
for i, (who, means, y) in enumerate([("Ordering", "basket + prices", 30), ("Fulfilment", "pick list + shelves", 120), ("Dispatch", "drop + address", 210)]):
    x = 20 if i == 0 else (530 if i == 1 else 20)
    bc_problem.box(x, y, 210, 60, who, "blue", sub=f"“order” = {means}", size=16, subsize=14)
bc_problem.line("M234 60 L266 80", thin=True)
bc_problem.line("M234 240 L266 200", thin=True)
bc_problem.line("M526 150 L494 150", thin=True)
bc_problem.box(530, 210, 216, 54, "picking export", "pink", sub="broke on tip_eur", stroke="red", size=16, subsize=13)

bc_analogy = Doodle(760, 260, "Doodle of a hospital. The word 'patient' means different things in different departments. Reception keeps appointments and insurance. The ward keeps the bed, medication and charts. Billing keeps invoices and payments. Each department keeps its own file with only what it needs, linked by the patient number.",
                    "In a hospital, reception, the ward and billing each keep their own file on “the patient”, linked by one number.")
for i, (dep, keeps, ic) in enumerate([("reception", "appointments, insurance", "calendar"), ("ward", "bed, medication, charts", "bell"), ("billing", "invoices, payments", "receipt")]):
    x = 20 + i * 250
    bc_analogy.box(x, 30, 220, 150, None, ["blue", "green", "y"][i])
    bc_analogy.icon(ic, x + 14, 44, 0.9)
    bc_analogy.head(x + 140, 74, dep, size=18)
    bc_analogy.text(x + 110, 130, "patient =", size=15)
    bc_analogy.text(x + 110, 156, keeps, size=14)
bc_analogy.line("M130 186 V214 H630 V186 M380 186 V214", dash=True, thin=True)
bc_analogy.note(380, 244, "linked by patient no. 48213, not one giant shared file", "pen")

bc_how = Doodle(760, 360, "Larder's context map, part of it. Ordering owns the Order: the basket, prices and payment status. Fulfilment owns the PickList: items, shelf positions and substitutions. Dispatch owns the Drop: the address, time slot and courier. They share only the order id and talk through events: Ordering publishes OrderPlaced, Fulfilment publishes OrderPacked, Dispatch publishes OrderDelivered. Each context has its own team and its own model.",
                 "Three contexts, three models of “an order”, one shared id, and events between them.")
ctx = [("Ordering", "Order", ["basket, prices", "payment status"], "orders team", 14),
       ("Fulfilment", "PickList", ["items, shelves", "substitutions"], "store team", 270),
       ("Dispatch", "Drop", ["address, slot", "courier, route"], "dispatch team", 526)]
for name, model, fields, team, x in ctx:
    bc_how.box(x, 20, 220, 210, None, "paper", dash=True, rx=40)
    bc_how.head(x + 110, 52, name + " context", size=17)
    bc_how.box(x + 30, 70, 160, 104, None, "y")
    bc_how.head(x + 110, 100, model, size=18)
    for k, f in enumerate(fields):
        bc_how.text(x + 110, 132 + k * 24, f, size=14)
    bc_how.note(x + 110, 206, team, "pen", size=17)
bc_how.arrow(234, 130, 296, 130)
bc_how.arrow(490, 130, 552, 130)
bc_how.note(265, 262, "OrderPlaced", "pen", size=16)
bc_how.note(521, 262, "OrderPacked", "pen", size=16)
bc_how.arrow(636, 236, 636, 290, dash=True)
bc_how.note(636, 312, "OrderDelivered → Ordering, Care", "pen", size=16)
bc_how.note(250, 330, "shared: order_id only · each team owns its model and its words", "pen", size=17)

BOUNDED_CONTEXTS = dict(
    slug="bounded-contexts",
    kicker="a.k.a. “reception, the ward and billing”",
    tldr="In a real business, one word means different things in different places: an “order” is a <b>basket</b> to sales, a <b>pick list</b> to the warehouse, a <b>drop</b> to delivery. Don't force one model on everyone. Draw a <b>boundary</b> wherever the meaning changes; inside it, one team owns <b>one consistent model</b> and its own words. Contexts share <b>ids and events</b>, not tables. Those boundaries are your best first guess for modules, services and team ownership.",
    chips=[("Family", "first shapes"), ("Origin", "Eric Evans, <i>Domain-Driven Design</i> (2003)"), ("Lives in", "a context map and one canvas per context"), ("Pairs with", "event storming, modular monolith, anti-corruption layer")],
    problem_side="Larder, the 64-column table",
    problem="""  <p class="lead">Larder Core has one <code>orders</code> table with <b>64 columns</b>, used by everyone. When Ordering adds a <code>tip_eur</code> column for couriers, the <span class="hl-pink">picking export breaks</span>, because it reads the same table. Ask three teams what an order is and you get three answers: a <b>basket with prices</b>, a <b>pick list with shelf positions</b>, a <b>drop with an address and a slot</b>. One table is trying to be all three.</p>
  <ul>
    <li>One shared model grows until nobody understands or dares change it.</li>
    <li>Words drift: “product” means a catalogue item to one team and a shelf SKU to another.</li>
    <li>Every change needs every team's agreement, so everything slows down.</li>
  </ul>""",
    problem_figs=[bc_problem],
    analogy_side="the hospital",
    analogy="""  <p>In a hospital, “the patient” means something different in each department. <b>Reception</b> keeps appointments and insurance. The <b>ward</b> keeps the bed, medication and charts. <b>Billing</b> keeps invoices. Each keeps its <b>own file</b> with only what it needs, in its own words, linked by the <b>patient number</b>. One giant shared file would be unreadable and dangerous.</p>""",
    analogy_figs=[bc_analogy],
    map=[("A department", "A bounded context: Ordering, Fulfilment, Dispatch"),
         ("Its own file on the patient", "Its own model: Order, PickList, Drop"),
         ("The patient number", "The shared id: order_id"),
         ("A discharge note sent to billing", "An event between contexts: OrderPacked"),
         ("Each department's jargon", "The context's ubiquitous language")],
    how_side="draw boundaries where meaning changes",
    how="""  <p>The event storming gives you the hints: <b>clusters of events</b>, <b>different actors</b>, and places where people <b>use the same word differently</b>. Draw a boundary there. Then draw a <b>context map</b>: how contexts relate, who is upstream, and what crosses the border (ids and events, never tables).</p>""",
    how_figs=[bc_how],
    steps=[("Start from the event storm", "Group events that change together and are done by the same people."),
           ("Listen for words that change meaning", "“Order”, “product”, “customer”: each meaning hints at a separate context."),
           ("Name each context and its model", "Ordering → Order. Fulfilment → PickList. Dispatch → Drop."),
           ("Give each one owner", "One team per context (a team can own several; a context never has two owners)."),
           ("Draw the context map", "Arrows for upstream/downstream, labelled with events or APIs; only ids cross."),
           ("Make them modules", "Each bounded context becomes a module in the modular monolith, or later a service.")],
    vocab=[("Bounded context", "A boundary inside which one model and its words are consistent."),
           ("Ubiquitous language", "The shared words of a context, used by experts and code alike."),
           ("Context map", "A diagram of contexts and how they relate."),
           ("Upstream / downstream", "Who publishes and who depends on what is published."),
           ("Anti-corruption layer", "A translator that protects a context from another's model."),
           ("Subdomain", "A part of the business problem (core, supporting, generic).")],
    code=dict(file="docs/contexts/fulfilment.md", note="bounded context canvas (DDD Crew style)", plain=True, src="""
# Bounded context: Fulfilment                    owner: store team (Tomás, Dee)

Purpose       Turn a paid order into a packed bag at the right store, fast and correct.
Domain type   Core (picking speed and substitutions are why customers come back)

Language      PickList   the items to pick for one order, in shelf order
              Pick       one item taken from a shelf (or reported out of stock)
              Substitute an alternative item offered when one is out of stock
              Tote       the crate a picker fills

Inbound       OrderPlaced (Ordering) · StockLevelChanged (Stock)
Outbound      ItemOutOfStock · SubstituteOffered · OrderPacked
Owns data     pick_lists, picks, substitutions, totes        (fulfilment_* tables)
Does NOT own  prices, payments, addresses, couriers

Rules         Offer a substitute within 2 minutes of ItemOutOfStock.
              A pick list works offline for 30 min (ASR-2).
"""),
    tools="tools: the DDD Crew's Bounded Context Canvas and Context Mapper (GitHub: ddd-crew), Context Mapper DSL, or a whiteboard. Event storming output is the best input.",
    gains=["<b>Smaller, clearer models</b>: each team understands its own.",
           "<b>Changes stay local</b>: a courier tip doesn't break picking.",
           "<b>Clear ownership</b>: one team per context.",
           "<b>Natural seams</b> for modules, services and teams.",
           "<b>Better conversations</b>: code uses the same words as the business."],
    losses=["<b>Duplication</b>: the same order id and some data appear in several contexts.",
            "<b>Integration work</b>: events and translations between contexts.",
            "<b>Hard to get right</b>: early boundaries are guesses and will move.",
            "<b>Learning curve</b>: DDD vocabulary can put people off."],
    baseline="Each line compares <b>one shared model and a 64-column orders table</b> to <b>bounded contexts with their own models, owners and events, sharing only ids</b>.",
    ratings=[(2, 4, "Each context's model is small enough to understand."),
             (2, 4, "Domain experts and engineers share the same words."),
             (2, 4, "Teams change their model without asking every other team."),
             (2, 4, "Accidental breakage between areas becomes rare."),
             (2, 4, "A context can change, or be extracted, on its own."),
             (2, 3, "The context map shows who owns what and why."),
             (3, 3, "Some duplication and integration cost; less coordination cost."),
             (3, 2, "Boundaries, maps and events take ongoing care."),
             (1, 5, "Each team owns a context end to end.")],
    pitfalls=[("Contexts by technology", "“Database context”, “API context”.", "draw boundaries by business meaning and people, not tech."),
              ("One context per entity", "Order context, Product context, Customer context: CRUD in disguise.", "group by business capability and language, not by noun."),
              ("Sharing tables anyway", "Contexts on the diagram, one orders table in the database.", "each context owns its data; others get ids and events."),
              ("Set in stone", "The first map is treated as final.", "revisit boundaries as you learn; cheap in a modular monolith.")],
    use=["A business with several departments using the same words differently.",
         "Splitting a monolith into modules or services.",
         "Deciding team ownership.",
         "When one shared model has become too big to change safely."],
    skip=["Small apps with one simple model and one team.",
          "Generic subdomains you buy (helpdesk, email): use the vendor's model behind a translator.",
          "When the domain isn't understood yet: event-storm first."],
    related=["<b>Domain discovery (event storming)</b> (this volume)", "<b>Modular monolith first</b> (this volume)", "<b>Anti-corruption layer</b> (Vol. 4)", "<b>Glossary &amp; ubiquitous language</b> (Vol. 3)"],
    quiz=[("What signals a boundary between two contexts?", "The same word changes meaning, different people do the work, and events cluster separately."),
          ("What may cross a context boundary?", "Ids, events and API calls; never shared tables or internal models."),
          ("Why can “order” be three different models at Larder?", "Ordering, Fulfilment and Dispatch need different data and rules: a basket, a pick list, a drop."),
          ("How do bounded contexts relate to the modular monolith?", "Each bounded context becomes a module; later, some may become services.")],
    try_it="Pick the most-used noun in your system (order, account, booking). Ask three people from different teams to define it in one sentence each. Write down how many different meanings you get, and which tables or classes are trying to hold all of them.",
    remember="Draw the line where the <span class=\"hl\">word changes meaning</span>. Share the <span class=\"hl\">patient number</span>, not the file.",
    sources=["Eric Evans, <i>Domain-Driven Design</i> (2003), part IV “Strategic Design”.",
             "Vaughn Vernon, <i>Implementing Domain-Driven Design</i> (2013), chapters 2–3.",
             "Martin Fowler, “BoundedContext” (martinfowler.com, 2014).",
             "DDD Crew, “Bounded Context Canvas” (github.com/ddd-crew)."],
)

# ------------------------------------------------------------------ 12 Walking Skeleton
ws_problem = Doodle(760, 270, "Doodle of how Larder opened its second Amsterdam store in 2024: layer by layer. The store app was finished in month two, the stock sync in month three, payments in month four. Only in month five were the parts connected, and integration broke for weeks: wrong ids, a missing field, a timeout nobody had tested.",
                    "Each part finished alone, connected at the end, and the end is where it all broke.")
for i, (t, m) in enumerate([("store app", "month 2"), ("stock sync", "month 3"), ("payments", "month 4")]):
    x = 20 + i * 170
    ws_problem.box(x, 40, 150, 80, t, "green", sub="✓ " + m, size=17, subsize=15)
ws_problem.arrow(530, 80, 570, 80)
ws_problem.box(576, 30, 170, 100, "connect", "pink", sub="month 5…", stroke="red", size=18, subsize=15)
for i, t in enumerate(["wrong ids", "missing field", "untested timeout"]):
    ws_problem.note(661, 162 + i * 26, "✗ " + t, "red", size=17)
ws_problem.note(260, 186, "each part “done”, nothing working", "red")

ws_analogy = Doodle(760, 260, "Doodle of a suspension bridge being started. First a kite carries a thin line across the river. The line pulls a rope across, the rope pulls a cable, and the cables carry the bridge. From day one something connects both banks, and every later step makes it stronger.",
                    "First a kite carries a thread across the river. Then a rope, then a cable, then the bridge.")
ws_analogy.raw('<path class="d f-blue" d="M0 200 Q380 236 760 200 V260 H0 Z"/>')
ws_analogy.box(10, 120, 80, 80, None, "paper")
ws_analogy.box(670, 120, 80, 80, None, "paper")
ws_analogy.raw('<path class="d f-y" d="M380 20 l26 26 l-26 26 l-26 -26 z"/>')
ws_analogy.line("M90 130 Q235 60 380 72", thin=True, color="pen")
ws_analogy.line("M380 72 Q525 60 670 130", thin=True, color="pen")
ws_analogy.line("M90 150 Q380 178 670 150", dash=True)
ws_analogy.note(380, 112, "day 1: a thread", "pen", size=18)
ws_analogy.note(380, 240, "then rope → cable → bridge", "pen", size=18)

ws_how = Doodle(760, 360, "Larder's walking skeleton for Rotterdam. One thin line runs through every part: the customer app, Ordering, Payments with a test payment provider account, Fulfilment and the picker app, Dispatch and the courier app, all deployed by the real pipeline to a production-like environment. One test product in test store RTM-0 can be ordered, paid, picked and delivered end to end by 15 January. After that, each week adds flesh: real catalogue, substitutions, slots, promotions.",
                 "The thinnest end-to-end path through every part, deployed by the real pipeline, before any part is “finished”.")
parts = [("customer", "app"), ("Ordering", ""), ("Payments", "+ PSP test"), ("Fulfilment", ""), ("picker", "app"), ("Dispatch", ""), ("courier", "app")]
for i, (p, q) in enumerate(parts):
    x = 14 + i * 106
    ws_how.box(x, 44, 94, 146, None, "paper")
    ws_how.text(x + 47, 72, p, "t-head", size=13)
    if q:
        ws_how.text(x + 47, 94, q, size=13)
ws_how.line("M30 130 H730", color="red")
for i in range(7):
    ws_how.raw(f'<circle class="d f-y" cx="{61 + i * 106}" cy="130" r="9"/>')
ws_how.note(380, 26, "1 test product · store RTM-0 · by 15 Jan", "red", size=17)
ws_how.note(380, 222, "real pipeline · production-like environment · automated end-to-end test", "pen", size=17)
weeks = [("wk 1–6", "skeleton", "y"), ("wk 7", "real catalogue", "blue"), ("wk 8", "substitutions", "blue"), ("wk 9", "slots", "blue"), ("wk 10", "promotions", "blue")]
for i, (w, t, f) in enumerate(weeks):
    x = 14 + i * 148
    ws_how.box(x, 250, 136, 62, t, f, size=14)
    ws_how.note(x + 68, 336, w, "pen", size=16)

WALKING_SKELETON = dict(
    slug="walking-skeleton",
    kicker="a.k.a. “the kite string across the river”",
    tldr="Before building any part fully, build the <b>thinnest possible end-to-end path through every part</b> of the architecture: one tiny feature that goes from the user's screen through every service, store and integration, <b>deployed by the real pipeline</b> to a production-like environment, with an <b>automated end-to-end test</b>. Then add flesh slice by slice. Integration problems show up in <b>week two, not month five</b>, and the architecture is proven by running code, not slides.",
    chips=[("Family", "first shapes"), ("Origin", "Alistair Cockburn, <i>Crystal Clear</i> (2004); Freeman &amp; Pryce, <i>Growing Object-Oriented Software</i> (2009)"), ("Lives in", "the first weeks of the delivery plan"), ("Pairs with", "spike vs PoC, fitness functions, build once deploy many")],
    problem_side="Larder, the second Amsterdam store",
    problem="""  <p class="lead">When Larder opened its second Amsterdam store in 2024, the team built it <b>layer by layer</b>: the store app was done in month two, the stock sync in month three, payments in month four. Each part passed its own tests. In month five they connected them, and <span class="hl-pink">integration broke for weeks</span>: ids that didn't match, a missing field, a timeout nobody had tested. For Rotterdam, with a fixed opening date, that can't happen again.</p>
  <ul>
    <li>Parts built alone look finished, but the risk sits in the connections.</li>
    <li>Deployment, environments and pipelines are left for “later”, and later is launch week.</li>
    <li>Nobody can see the architecture working until it's too late to change it cheaply.</li>
  </ul>""",
    problem_figs=[ws_problem],
    analogy_side="the kite and the bridge",
    analogy="""  <p>To start a suspension bridge across a wide river, engineers once flew a <b>kite</b> across with a thin thread. The thread pulled a <b>rope</b>, the rope pulled a <b>cable</b>, and the cables carried the bridge. From the first day <b>something connected both banks</b>, and every step after that made the connection stronger, never started a new one.</p>""",
    analogy_figs=[ws_analogy],
    map=[("The kite's thread", "The walking skeleton: one tiny end-to-end feature"),
         ("Both river banks", "The customer's screen and the courier's doorstep"),
         ("Rope, then cable", "Slices of real features added week by week"),
         ("Testing the line holds", "An automated end-to-end test on every change"),
         ("Building the towers separately first", "Layer-by-layer delivery: the mistake to avoid")],
    how_side="thin, complete, deployed, tested",
    how="""  <p>“Thin” means <b>almost no features</b>: one test product, one payment method, one courier. “Complete” means <b>every part and every integration</b> is touched, including the pipeline, environments, monitoring and the real third-party sandboxes. If a part isn't in the skeleton, its risk isn't retired.</p>""",
    how_figs=[ws_how],
    steps=[("Pick the thinnest real journey", "One that touches every part: “order one item, pay, pick, deliver”."),
           ("Include the boring parts", "Pipeline, environments, config, logging, the real vendor sandboxes."),
           ("Stub nothing you can reach", "Use the payment provider's test account and StockPilot's sandbox, not mocks."),
           ("Automate one end-to-end test", "It runs on every change; it's the thread you never cut."),
           ("Deploy it like production", "Same pipeline, same infrastructure-as-code, a production-like environment."),
           ("Add flesh slice by slice", "Each week: one more real feature through all the layers, never one layer alone.")],
    vocab=[("Walking skeleton", "A tiny end-to-end implementation through every architectural part."),
           ("Vertical slice", "A feature that goes through every layer, from UI to data."),
           ("Tracer bullet", "Similar idea (<i>The Pragmatic Programmer</i>): code that lights up the path end to end."),
           ("Integration risk", "The risk that parts that work alone fail together."),
           ("Sandbox", "A vendor's test environment that behaves like production."),
           ("Production-like", "Same pipeline, config and infrastructure as production, without real customers.")],
    code=dict(file="docs/plans/rotterdam-walking-skeleton.md", note="definition of done for the skeleton", plain=True, src="""
# Walking skeleton: Rotterdam                         due: 15 Jan 2026 · owner: Ana

Journey   A tester orders 1 × “Test Banana” from test store RTM-0, pays with
          the PSP's test card, a picker picks it on the picker app, a courier
          accepts it in the courier app and marks it delivered.

Must touch
  [x] customer app (TestFlight / internal track)   [x] Ordering module
  [x] Payments module + PSP test account          [x] Stock module + StockPilot sandbox
  [x] Fulfilment module + picker app              [x] Dispatch service + courier app
  [x] events: OrderPlaced → OrderPacked → OrderDelivered
  [x] city config for “Rotterdam” (ASR-1: no code change)

Must run on
  [x] the real CI/CD pipeline, infrastructure as code
  [x] staging-rtm (production-like), logs and dashboards on
  [x] one automated end-to-end test, run on every merge (≈ 4 min)

Out of scope (flesh, weeks 7+): real catalogue, substitutions, slots, promotions,
refunds, Bancontact, more than one picker.
"""),
    tools="tools: Playwright or Detox for the end-to-end test, your CI/CD system, infrastructure as code, and the vendors' sandbox accounts. The skeleton is code like any other; it just comes first.",
    gains=["<b>Integration risk retired early</b>: broken connections show up in week two.",
           "<b>The architecture is proven</b> by running code, not slides.",
           "<b>Pipeline and environments ready</b> from the start.",
           "<b>Always shippable</b>: every slice after it is end to end.",
           "<b>Visible progress</b> stakeholders can watch: “the banana got delivered”."],
    losses=["<b>Slow-looking start</b>: weeks of work with “only one banana” to show.",
            "<b>Touches every team</b> at once, so it needs coordination.",
            "<b>Vendor sandboxes</b> can be slow to get and unlike production.",
            "<b>Temptation to skip</b> the boring parts (pipeline, monitoring)."],
    baseline="Each line compares <b>building each part fully and integrating at the end</b> to <b>a deployed, tested end-to-end skeleton first, then slices of real features</b>.",
    ratings=[(2, 4, "Everyone can see the whole path working, not just their part."),
             (2, 4, "Sponsors see a real order delivered weeks before launch."),
             (3, 3, "Slower first weeks, much faster and calmer end."),
             (1, 5, "Integration and deployment risks are retired first."),
             (2, 4, "Weak spots in the shape are found while they're cheap to change."),
             (3, 3, "The skeleton's scope and test are documented."),
             (2, 3, "Early environments cost a little; late rework costs more."),
             (3, 3, "Needs coordination across teams for a few weeks."),
             (3, 3, "Teams depend on each other early; later slices are smoother.")],
    pitfalls=[("Mocking the scary parts", "The skeleton calls a fake payment provider.", "use the real sandbox: the real integration is the risk you're retiring."),
              ("Too much flesh", "The “skeleton” has 12 features and takes three months.", "one journey, one item, one of everything; add features after."),
              ("Skipping deployment", "It runs on a laptop.", "it must ship through the real pipeline to a production-like environment."),
              ("Cutting the thread", "The end-to-end test is disabled when it gets flaky.", "fix it first; it's the only proof the parts still connect.")],
    use=["New systems, new architectures and big rebuilds.",
         "When several teams or vendors must integrate.",
         "When a launch date is fixed and integration risk is high.",
         "Proving a chosen architecture really works."],
    skip=["Small features inside a working system: it already walks.",
          "Pure research spikes where no product will follow.",
          "When the only risk is in one component: spike that component instead."],
    related=["<b>Spike vs prototype vs PoC</b> (this volume)", "<b>Fitness functions</b> (this volume)", "<b>Modular monolith first</b> (this volume)", "<b>Build once, deploy many</b> (patterns, Vol. 6)"],
    quiz=[("What makes a walking skeleton “complete”?", "It touches every architectural part and integration, and ships through the real pipeline with an automated end-to-end test."),
          ("Why use vendor sandboxes instead of mocks?", "The real integration is the risk; a mock hides exactly what you need to find."),
          ("What comes after the skeleton?", "Vertical slices: each adds one real feature through all layers."),
          ("How is it different from a prototype?", "A prototype tests an idea and is thrown away; the skeleton is production code that becomes the system.")],
    try_it="For your next new feature or system, write a one-paragraph “skeleton journey” that touches every part, and a checklist of the parts it must pass through. Count how many of those parts you'd normally connect only at the end.",
    remember="Fly the <span class=\"hl\">thread</span> across the river first. Then make it <span class=\"hl\">stronger</span>, never start again.",
    sources=["Alistair Cockburn, <i>Crystal Clear</i> (2004), “Walking Skeleton”.",
             "Steve Freeman &amp; Nat Pryce, <i>Growing Object-Oriented Software, Guided by Tests</i> (2009), chapter 4.",
             "Andrew Hunt &amp; David Thomas, <i>The Pragmatic Programmer</i> (1999), “Tracer Bullets”.",
             "Jez Humble &amp; David Farley, <i>Continuous Delivery</i> (2010)."],
)

NOTES = [STYLES, MODULAR_MONOLITH, BOUNDED_CONTEXTS, WALKING_SKELETON]
