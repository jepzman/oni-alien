# Series 2 · The Solution Architect's Notebook · Vol. 1 · Validating early.
# Running case study: Larder (facts in docs/larder-casebook.md).

# ------------------------------------------------------------------ 13 Spike vs Prototype vs PoC
sp_problem = Doodle(760, 270, "Doodle of two old Larder experiments that went wrong. The 'temporary' dispatch cron job, written as a quick prototype in 2024, is still assigning every courier in production. A search engine evaluation, never timeboxed, ran for three weeks and ended with no decision.",
                    "One “quick prototype” became production. One “quick look” never ended.")
sp_problem.box(20, 30, 340, 110, None, "pink", stroke="red")
sp_problem.head(190, 62, "“temporary” dispatch cron", size=17, color="red")
sp_problem.text(190, 94, "a prototype from 2024…", size=16)
sp_problem.text(190, 120, "still assigns every courier", size=16)
sp_problem.box(400, 30, 340, 110, None, "pink", stroke="red")
sp_problem.head(570, 62, "search engine “look”", size=17, color="red")
sp_problem.text(570, 94, "no question, no timebox", size=16)
sp_problem.text(570, 120, "3 weeks, no decision", size=16)
sp_problem.icon("hourglass", 558, 168, 1.6)
sp_problem.icon("clock", 160, 166, 1.1)
sp_problem.note(380, 256, "the wrong kind of experiment, with no exit", "red")

sp_analogy = Doodle(760, 270, "Doodle of a wedding caterer preparing. A spike: tasting one spoon of a new spice to answer one question. A prototype: a sample plate shown to the couple to ask if this is what they want. A proof of concept: cooking one full table's meal in the real kitchen at full speed to prove it can be done. Then the real banquet.",
                    "A caterer: taste a spoon, show a sample plate, cook one real table, then the banquet.")
for i, (t, q, ic) in enumerate([("taste a spoon", "does this spice work?", "cup"), ("sample plate", "is this what you want?", "plate"), ("one full table", "can we do it for real?", "kitchen")]):
    x = 20 + i * 190
    sp_analogy.icon(ic, x + 55, 26, 1.1)
    sp_analogy.box(x, 106, 176, 90, t, ["blue", "y", "green"][i], sub=q, size=16, subsize=13)
sp_analogy.arrow(596, 150, 630, 150)
sp_analogy.box(634, 106, 112, 90, "banquet", "paper", sub="the real thing", size=17, subsize=13)
sp_analogy.note(300, 236, "spike → prototype → proof of concept", "pen", size=19)

sp_how = Doodle(760, 400, "Comparing three experiments. A spike answers a technical question for engineers in one to three days; the output is an answer and notes, and the code is thrown away. Larder's: can StockPilot's API serve six cities? A prototype tests whether an idea is right with users or stakeholders in days to two weeks; the output is feedback. Larder's: will pickers accept the offline picking flow? A proof of concept proves something works for real against success criteria in one to four weeks. Larder's: can an open-source routing engine assign 300 couriers in under two seconds?",
                 "Three experiments, three questions. Pick by the question, and set the timebox before you start.")
rows = [("asks", "can X do Y?", "is this the right thing?", "does it work for real, here?"),
        ("for", "engineers", "users, stakeholders", "sponsors, architects"),
        ("timebox", "1–3 days", "days – 2 weeks", "1–4 weeks"),
        ("output", "an answer + notes", "feedback", "evidence vs criteria"),
        ("code", "thrown away", "thrown away", "usually thrown away")]
heads = [("spike", "blue"), ("prototype", "y"), ("proof of concept", "green")]
for k, (h, f) in enumerate(heads):
    x = 150 + k * 204
    larder_ex = ["StockPilot API: 6 cities?", "offline pick flow: OK?", "routing 300 couriers?"][k]
    sp_how.box(x, 14, 192, 48, h, f, size=17)
    sp_how.box(x, 316, 192, 60, None, f)
    sp_how.text(x + 96, 342, "Larder:", "t t-soft", size=13)
    sp_how.text(x + 96, 364, larder_ex, size=13)
for i, row in enumerate(rows):
    y = 72 + i * 48
    sp_how.line(f"M14 {y + 44} H750", thin=True, color="soft")
    sp_how.text(20, y + 28, row[0], "t-head", anchor="start", size=15)
    for k in range(3):
        sp_how.text(246 + k * 204, y + 28, row[k + 1], size=14)

SPIKES = dict(
    slug="spike-prototype-poc",
    kicker="a.k.a. “taste a spoon before you cook the banquet”",
    tldr="When the next decision depends on something you don't know, run a <b>small, timeboxed experiment</b>, and pick the right kind. A <b>spike</b> answers a <b>technical question</b> (“can X do Y?”) in a few days. A <b>prototype</b> tests whether an <b>idea is right</b> with real users. A <b>proof of concept</b> proves something <b>works for real</b> against agreed success criteria. Write the question, the timebox and the success criteria <b>before</b> you start, and decide up front that the code will be <b>thrown away</b>.",
    chips=[("Family", "validating early"), ("Origin", "“spike” from Extreme Programming (Kent Beck, 1999); prototyping in design practice"), ("Lives in", "an experiment card, then an ADR"), ("Pairs with", "constraints vs assumptions, risk-storming, walking skeleton")],
    problem_side="Larder, two old experiments",
    problem="""  <p class="lead">Larder has been burned by experiments twice. In 2024 someone wrote a quick <b>prototype</b> cron job to assign couriers; it's <span class="hl-pink">still running in production</span>, assigning every courier every 30 seconds. Last spring a “quick look” at search engines had <b>no question and no timebox</b>; it ran for three weeks and ended without a decision. Now Ana has three real unknowns, and she wants each one answered in days, not weeks.</p>
  <ul>
    <li>Using the wrong kind of experiment answers the wrong question.</li>
    <li>Experiments without a timebox drift; experiments without criteria never “finish”.</li>
    <li>Prototype code that works “well enough” quietly becomes production.</li>
  </ul>""",
    problem_figs=[sp_problem],
    analogy_side="the wedding caterer",
    analogy="""  <p>A caterer preparing a wedding <b>tastes a spoon</b> of a new spice (does it work?), shows the couple a <b>sample plate</b> (is this what you want?), and cooks <b>one full table</b> in the real kitchen at full speed (can we do this for 200?). Each answers a different question, none of them is the banquet, and nobody serves the tasting spoon to the guests.</p>""",
    analogy_figs=[sp_analogy],
    map=[("Tasting a spoon", "Spike: can StockPilot's API serve six cities?"),
         ("The sample plate for the couple", "Prototype: will pickers accept the offline picking flow?"),
         ("Cooking one full table", "Proof of concept: routing 300 couriers in under 2 s"),
         ("The banquet", "Production: built properly, after the decision"),
         ("Not serving the tasting spoon", "Throwing experiment code away")],
    how_side="pick by the question, timebox first",
    how="""  <p>Start from the <b>question</b>, not the technology. If it's “can it?”, spike. If it's “should we?” or “will they like it?”, prototype. If it's “will it work here, at our scale, with our data?”, run a proof of concept with written success criteria. Every experiment ends in a <b>decision</b>, usually an ADR.</p>""",
    how_figs=[sp_how],
    steps=[("Write the question", "One sentence that the experiment will answer with yes, no or a number."),
           ("Pick the kind", "Technical question → spike. Is it right? → prototype. Works for real? → proof of concept."),
           ("Set the timebox", "Days for a spike, up to two weeks for a prototype, up to four for a PoC. Stop when it's up."),
           ("Agree the success criteria", "“≥ 50 req/s per store”, “4 of 5 pickers finish without help”, “p95 < 2 s for 300 couriers”."),
           ("Run it, cheaply", "Hard-code, skip tests, use sandboxes. It's a question, not a product."),
           ("Decide and throw away", "Write the result and the decision (an ADR); delete or archive the code.")],
    vocab=[("Spike", "A short, timeboxed investigation to answer a technical question."),
           ("Prototype", "A rough version of an idea, built to get feedback."),
           ("Proof of concept (PoC)", "An experiment proving an approach works for real, against criteria."),
           ("MVP", "Minimum viable product: the smallest real product for real users. Not an experiment."),
           ("Timebox", "A fixed amount of time; when it's up, you stop and decide."),
           ("Success criteria", "Measurable conditions agreed before the experiment starts.")],
    code=dict(file="docs/experiments/2025-11-stockpilot-spike.md", note="experiment card, filled in", plain=True, src="""
# Experiment: can StockPilot's API serve six cities?             SPIKE

Question      Can we read and update stock for 12 stores (6 cities × 2) through
              StockPilot's API fast enough to stay within 1 minute of reality?
Why now       Assumption A-1; the Rotterdam plan depends on it.
Owner         Ben (+ Cho)           Timebox: 2 days, 19–20 Nov 2025
Success       ≥ 50 req/s sustained per account, with no throttling; p95 < 300 ms
Approach      Script against the StockPilot sandbox; ask their support about limits.
              Throwaway code in spikes/stockpilot/ (not merged to main).

Result        ✗ Hard limit 10 req/s per account (HTTP 429 above it), confirmed by
              StockPilot support. Bulk endpoint: 500 items per call, 1 call/s.
              p95 at 10 req/s: 180 ms.
Decision      Cache stock per store in our Stock module; sync from StockPilot by
              bulk calls and its webhooks. → ADR 0005 (proposed 2025-11-24)
Code          Deleted. Notes and numbers kept here.
"""),
    tools="tools: whatever is quickest: scripts, notebooks, vendor sandboxes, Figma or paper prototypes, a load-test tool for PoCs. Keep experiment cards in the repo next to the ADRs they lead to.",
    gains=["<b>Decisions on evidence</b>, not opinion or vendor slides.",
           "<b>Bad news early</b>: StockPilot's limit found in November, not April.",
           "<b>Cheap</b>: days of effort against months of building on a guess.",
           "<b>Right question, right method</b>: users test ideas, load tests test scale.",
           "<b>No accidental production code</b> when throwaway is agreed up front."],
    losses=["<b>Time away from delivery</b>, which can feel slow.",
            "<b>Partial answers</b>: a sandbox isn't production.",
            "<b>Throwing away working code</b> feels wasteful.",
            "<b>Can become procrastination</b>: one more spike instead of deciding."],
    baseline="Each line compares <b>untimeboxed “quick looks” and prototypes that drift into production</b> to <b>the right kind of experiment, with a question, timebox and success criteria, ending in an ADR</b>.",
    ratings=[(2, 4, "Each experiment card says what was asked, found and decided."),
             (2, 4, "Sponsors see evidence instead of arguments."),
             (2, 4, "Timeboxes force a decision in days."),
             (2, 5, "The riskiest unknowns are tested before the plan depends on them."),
             (3, 4, "Learning early keeps more options open."),
             (2, 5, "Cards and ADRs record the evidence behind each choice."),
             (2, 4, "Days of experiment against months of rework."),
             (3, 3, "Writing the card takes 15 minutes; the experiment, days."),
             (2, 4, "Teams can run their own spikes with the same card.")],
    pitfalls=[("No timebox", "The “quick look” runs for three weeks.", "set the timebox first; when it's up, decide with what you have."),
              ("Prototype goes to production", "The demo worked, so it shipped.", "agree up front it will be thrown away; rebuild properly."),
              ("Criteria after the fact", "The PoC “succeeded” because the criteria were written to fit.", "write success criteria before starting, with the sponsor."),
              ("Wrong kind", "A load test to find out if pickers like the flow.", "pick by the question: can it, should we, will it work here?")],
    use=["Any assumption the plan depends on.",
         "Choosing between options when the deciding fact is unknown.",
         "New technologies, vendors or user flows.",
         "Before committing a date or budget that depends on an unknown."],
    skip=["When the answer is cheap to look up (docs, a vendor call).",
          "Decisions that are easy to reverse: just try it in the product.",
          "When you already know and are seeking comfort: decide."],
    related=["<b>Constraints vs assumptions</b> (this volume)", "<b>Walking skeleton</b> (this volume)", "<b>Risk-storming</b> (this volume)", "<b>Technology evaluation</b> (Vol. 2)"],
    quiz=[("Which experiment answers “can StockPilot's API handle our load?”", "A spike: a short technical investigation."),
          ("How is a prototype different from an MVP?", "A prototype tests an idea and is thrown away; an MVP is a real product for real users."),
          ("What must be written before a proof of concept starts?", "The question, the timebox and measurable success criteria agreed with the sponsor."),
          ("What happens to experiment code?", "It's thrown away or archived; the result and the decision are kept.")],
    try_it="Pick the biggest unknown in your current plan. Write an experiment card: the question, the kind (spike, prototype or PoC), a timebox, success criteria and an owner. Show it to your lead and ask for the timebox, not more.",
    remember="Pick the experiment by the <span class=\"hl\">question</span>. Set the <span class=\"hl\">timebox</span> first. Never serve the tasting spoon.",
    sources=["Kent Beck, <i>Extreme Programming Explained</i> (1999), on spikes.",
             "Mike Cohn, <i>Agile Estimating and Planning</i> (2005), spikes.",
             "Marty Cagan, <i>Inspired</i>, 2nd ed. (2017), on prototypes.",
             "Michael Keeling, <i>Design It!</i> (2017), “Prototype to learn or decide”."],
)

# ------------------------------------------------------------------ 14 Fitness Functions
ff_problem = Doodle(760, 280, "Doodle of three slow drifts at Larder, found in January 2026, two months after the architecture decisions. Twenty-three new imports go from ordering straight into payments internals. Checkout p95 crept from 420 to 690 milliseconds over six weeks. A log line with customer addresses came back. Nothing checked the decisions, so they quietly eroded.",
                    "Decided in December, eroded by January, and nobody noticed, because nothing was checking.")
ff_problem.box(20, 30, 220, 100, "23 imports", "pink", sub="ordering → payments", stroke="red", size=18, subsize=14)
ff_problem.box(270, 30, 220, 100, None, "pink", stroke="red")
ff_problem.head(380, 56, "checkout p95", size=18, color="red")
ff_problem.line("M290 116 L330 112 L370 104 L410 96 L450 80 L470 70", color="red")
ff_problem.text(300, 112, "420", anchor="start", size=13)
ff_problem.text(482, 104, "690", anchor="end", size=13)
ff_problem.box(520, 30, 220, 100, "addresses", "pink", sub="back in the logs", stroke="red", size=18, subsize=14)
ff_problem.note(130, 160, "breaks ADR 0002", "red")
ff_problem.note(380, 160, "breaks QAS-1, slowly", "red")
ff_problem.note(630, 160, "breaks GDPR rule", "red")
ff_problem.box(170, 200, 420, 54, "6 weeks of drift, found by accident", "pink", stroke="red", size=17)

ff_analogy = Doodle(760, 250, "Doodle of a bricklayer checking every row of bricks with a spirit level as the wall goes up. A wall checked only at the end can be leaning badly by the time anyone looks; a wall checked every row never leans more than one brick.",
                     "A bricklayer checks every row with a spirit level, not the finished wall.")
for row in range(5):
    for k in range(4):
        x = 40 + k * 60 + (30 if row % 2 else 0)
        ff_analogy.box(x, 190 - row * 30, 58, 28, None, "y", rx=2)
ff_analogy.box(60, 26, 220, 22, None, "green", rx=4)
ff_analogy.raw('<rect class="d f-paper" x="150" y="31" width="40" height="12" rx="6"/><circle class="d d-thin f-green" cx="170" cy="37" r="4"/>')
ff_analogy.note(296, 44, "every row", "green", anchor="start")
ff_analogy.raw('<path class="d d-dash d-soft" d="M470 220 L470 60"/>')
for row in range(5):
    ff_analogy.raw(f'<rect class="d f-pink" x="{460 + row * 10}" y="{190 - row * 30}" width="110" height="28" rx="2"/>')
ff_analogy.note(680, 90, "checked only", "red")
ff_analogy.note(680, 116, "at the end", "red")

ff_how = Doodle(760, 360, "Larder's fitness functions in the delivery pipeline. On every merge: module boundaries checked by import-linter, which enforces ADR 0002; a log scanner for personal data, enforcing the GDPR rule; and a database query count per request. Nightly: a load test at five times peak, enforcing QAS-1, checkout p95 under 800 milliseconds. Weekly: dependency licence and freshness checks. A failure breaks the build or opens a ticket for the owner.",
                 "Each architecture rule becomes a check, linked to the decision it protects, run on every merge or every night.")
ff_how.box(14, 20, 120, 60, "merge", "paper", size=18)
ff_how.arrow(140, 50, 180, 50)
checks = [("module boundaries", "import-linter · ADR 0002"), ("no personal data in logs", "log scanner · GDPR"), ("≤ 25 queries / request", "test helper · ASR-3")]
for i, (t, s) in enumerate(checks):
    ff_how.box(186, 14 + i * 74, 330, 62, t, "green", sub=s, size=16, subsize=13)
ff_how.box(14, 250, 120, 60, "nightly", "paper", size=18)
ff_how.arrow(140, 280, 180, 280)
ff_how.box(186, 248, 330, 62, "checkout p95 < 800 ms at 5×", "blue", sub="k6 load test · QAS-1", size=15, subsize=13)
ff_how.arrow(522, 90, 572, 120, color="red")
ff_how.arrow(522, 280, 572, 230, color="red")
ff_how.box(578, 120, 170, 110, "fails?", "pink", sub="build breaks", stroke="red", size=19, subsize=15)
ff_how.note(663, 260, "or a ticket", "red")
ff_how.note(663, 284, "for the owner", "red")
ff_how.note(380, 344, "every check names the ADR or ASR it protects", "pen")

FITNESS = dict(
    slug="fitness-functions",
    kicker="a.k.a. “the spirit level on every row”",
    tldr="Architecture decisions decay quietly: an import here, 20 ms there. A <b>fitness function</b> turns an architecture rule into an <b>automated check</b>: module boundaries, latency at peak, no personal data in logs, dependency rules. Run them in the <b>pipeline</b> (on every merge or nightly), link each one to the <b>ADR or requirement</b> it protects, and let a failure <b>break the build or open a ticket</b>. The architecture then defends itself, without the architect reviewing every pull request.",
    chips=[("Family", "validating early"), ("Origin", "Neal Ford, Rebecca Parsons &amp; Patrick Kua, <i>Building Evolutionary Architectures</i> (2017)"), ("Lives in", "the CI pipeline, next to the tests"), ("Pairs with", "quality attribute scenarios, modular monolith, ADRs")],
    problem_side="Larder, January 2026",
    problem="""  <p class="lead">Two months after deciding on a modular monolith, Ana looks at the code. There are <b>23 new imports</b> from ordering straight into payments' internals. Checkout p95 has crept from <b>420 to 690 ms</b> over six weeks, still “fine”, but heading for the 800 ms limit. And a log line with <b>customer addresses</b> is back. Every decision is still in its ADR. None of them is <span class="hl-pink">being checked</span>.</p>
  <ul>
    <li>Decisions written down aren't decisions enforced.</li>
    <li>Drift is slow: each change is small and looks reasonable.</li>
    <li>An architect reviewing every pull request doesn't scale, and becomes a bottleneck.</li>
  </ul>""",
    problem_figs=[ff_problem],
    analogy_side="the spirit level",
    analogy="""  <p>A good bricklayer puts a <b>spirit level</b> on every row as the wall goes up. If a row is off, it's one row to fix. A wall checked only when it's finished can be leaning badly, and by then the fix is <b>knocking it down</b>. The level is cheap, fast, and used constantly.</p>""",
    analogy_figs=[ff_analogy],
    map=[("The spirit level", "A fitness function: an automated architecture check"),
         ("Every row", "Every merge (or every night for slow checks)"),
         ("“Straight” and “plumb”", "The rules: module boundaries, p95 at peak, no PII in logs"),
         ("Fixing one row", "Fixing one pull request, while it's small"),
         ("Checking the finished wall", "An architecture review months later")],
    how_side="rules become checks in the pipeline",
    how="""  <p>Go through your ADRs and quality scenarios and ask: <b>“how would we know if this stopped being true?”</b> Whatever you can measure automatically becomes a check. Fast ones run on every merge; slow ones (load tests) nightly. Each check names the <b>decision it protects</b>, so a failure explains itself.</p>""",
    how_figs=[ff_how],
    steps=[("List the rules", "From ADRs, ASRs and scenarios: boundaries, latency, data rules, dependencies."),
           ("Ask “how would we know?”", "For each rule, what can be measured automatically?"),
           ("Pick the trigger", "Fast and cheap → every merge. Slow (load, security scans) → nightly or weekly."),
           ("Link to the decision", "The check's name or message points to ADR 0002 or QAS-1."),
           ("Decide what failure does", "Break the build for hard rules; open a ticket for trends."),
           ("Review them", "When an ADR is superseded, update or delete its fitness function.")],
    vocab=[("Fitness function", "An objective, automated check of an architectural characteristic."),
           ("Atomic / holistic", "Checks one thing alone / checks how several interact."),
           ("Triggered / continual", "Runs on an event (a merge) / runs all the time (monitoring)."),
           ("Architecture test", "A unit-test-style check of structure (imports, layers)."),
           ("Evolutionary architecture", "An architecture designed to change, guarded by fitness functions."),
           ("Threshold", "The limit a check enforces (p95 < 800 ms).")],
    code=dict(file=".importlinter + load/checkout.js", note="two of Larder's fitness functions", plain=True, src="""
# .importlinter: protects ADR 0002 (modular monolith)          runs on every merge
[importlinter]
root_package = larder_core

[importlinter:contract:modules-use-public-api]
name = Modules talk only through api and events (ADR 0002)
type = forbidden
source_modules = larder_core.ordering
forbidden_modules =
    larder_core.payments._internal
    larder_core.payments.models
    larder_core.fulfilment._internal
    larder_core.fulfilment.models

# load/checkout.js (k6): protects QAS-1                         runs nightly
export const options = {
  scenarios: { kings_day: { executor: "constant-arrival-rate", rate: 3000,
                            timeUnit: "1s", duration: "10m", preAllocatedVUs: 400 } },
  thresholds: {
    "http_req_duration{journey:checkout}": ["p(95)<800"],   // QAS-1
    "checks{check:order_confirmed}": ["rate==1.0"],          // ASR-4: nothing lost
  },
};
"""),
    tools="tools: import-linter, ArchUnit, dependency-cruiser and NetArchTest for structure; k6, Gatling or Locust for performance; Semgrep and log scanners for data rules; Dependabot or Renovate plus licence checkers for dependencies; SLO alerts for continual checks.",
    gains=["<b>Decisions defend themselves</b>: drift is caught in the pull request that causes it.",
           "<b>The architect isn't a bottleneck</b>: no need to review every change.",
           "<b>Trends are visible</b>: 420 → 690 ms shows up before 800.",
           "<b>Safe to change</b>: teams refactor boldly, knowing the checks will catch a break.",
           "<b>Living documentation</b>: the checks say what really matters."],
    losses=["<b>Building and maintaining checks</b> takes engineering time.",
            "<b>Slow checks</b> (load tests) cost infrastructure and CI minutes.",
            "<b>False alarms</b>: flaky load tests erode trust.",
            "<b>Not everything is measurable</b>: some qualities still need human review."],
    baseline="Each line compares <b>architecture decisions recorded in ADRs and checked by occasional reviews</b> to <b>the same decisions guarded by automated fitness functions in the pipeline</b>.",
    ratings=[(3, 4, "The checks show which rules really matter."),
             (3, 3, "Mostly engineering; sponsors see fewer surprises."),
             (3, 4, "No waiting for an architecture review to merge."),
             (2, 5, "Drift is caught in the change that causes it."),
             (2, 5, "Teams refactor safely; rules change by updating a check."),
             (3, 4, "Each check names the decision it protects."),
             (3, 3, "CI minutes and load-test infrastructure cost money."),
             (3, 3, "Checks need building and maintaining."),
             (2, 5, "Teams act without asking the architect; the pipeline checks.")],
    pitfalls=[("Checks with no reason", "A rule fails the build and nobody knows why it exists.", "name the ADR or ASR in every check's message."),
              ("Flaky thresholds", "The load test fails one night in four, so people ignore it.", "stable environments and margins; alert on trends, not single runs."),
              ("Everything breaks the build", "Teams spend days fighting checks for minor trends.", "hard rules break the build; trends open a ticket."),
              ("Outliving the decision", "ADR 0002 is superseded but its check still blocks merges.", "update or delete checks when their decision changes.")],
    use=["Any architecture rule that has been broken once already.",
         "Module boundaries in a modular monolith.",
         "Quality scenarios with clear measures (latency, error rate, size).",
         "Data rules (no personal data in logs, residency)."],
    skip=["Rules that can't be measured: keep them in reviews.",
          "One-off decisions with nothing to drift (a vendor choice).",
          "Very early prototypes where the rules aren't settled yet."],
    related=["<b>Quality attribute scenarios</b> (this volume)", "<b>Modular monolith first</b> (this volume)", "<b>Evolutionary architecture</b> (Vol. 6)", "<b>Guardrails not gates</b> (Vol. 6)"],
    quiz=[("What is a fitness function?", "An automated, objective check of an architectural rule or quality, usually run in the pipeline."),
          ("Which question turns a decision into a fitness function?", "“How would we know if this stopped being true?”"),
          ("When should a check break the build, and when open a ticket?", "Hard rules (boundaries, data rules) break the build; slow trends (latency creep) open a ticket."),
          ("Why link each check to an ADR or ASR?", "So a failure explains itself, and the check is updated when the decision changes.")],
    try_it="Pick one ADR from your project. Write down how you'd know automatically if it stopped being true, and find the tool that could check it. Add it to CI as a warning first; after a week of no false alarms, make it fail the build.",
    remember="Check <span class=\"hl\">every row</span>, not the finished wall. A decision nobody checks is a <span class=\"hl\">wish</span>.",
    sources=["Neal Ford, Rebecca Parsons, Patrick Kua &amp; Pramod Sadalage, <i>Building Evolutionary Architectures</i>, 2nd ed. (2022).",
             "ThoughtWorks Technology Radar, “Architectural fitness function” (Adopt).",
             "import-linter documentation (import-linter.readthedocs.io).",
             "k6 documentation, thresholds (grafana.com/docs/k6)."],
)

# ------------------------------------------------------------------ 15 Risk-Storming
rs_problem = Doodle(760, 270, "Doodle of Ana's own risk list before the Rotterdam plan is committed: six items, all technical, written alone at her desk. The risks other people know about are missing: the picker Wi-Fi known to Tomás, the payment provider's Friday outages known to Cho, the dispatch cron job Joost worries about, and the Rotterdam date colliding with the StockPilot contract.",
                    "The architect's risk list, written alone: six risks, all technical. The worst ones are in other people's heads.")
rs_problem.box(20, 20, 280, 220, None, "paper")
rs_problem.head(160, 48, "Ana's risk list", size=17)
for i, t in enumerate(["DB schema migration", "Django upgrade", "test coverage", "Kafka skills", "cache invalidation", "CI speed"]):
    rs_problem.text(40, 82 + i * 26, f"{i + 1}. {t}", anchor="start", size=15)
for i, (who, t) in enumerate([("Tomás", "store Wi-Fi drops"), ("Cho", "PSP down on Fridays"), ("Joost", "the dispatch cron"), ("Lena + Marco", "date vs contract")]):
    y = 20 + i * 56
    rs_problem.box(380, y, 360, 46, None, "pink", stroke="red")
    rs_problem.text(396, y + 30, f"{who}: “{t}”", anchor="start", size=15)
rs_problem.line("M306 130 L374 130", dash=True, color="red")
rs_problem.note(560, 258, "not on the list: nobody asked", "red")

rs_analogy = Doodle(760, 260, "Doodle of a family doing a home safety walk before a baby arrives. Everyone walks the house with stickers and marks what they see. The toddler's-eye view finds sockets and sharp corners, grandma finds the loose rug, the cook finds pan handles sticking out. Each person sees different dangers; together they find most of them.",
                     "A home safety walk: everyone marks the dangers they see. The toddler, grandma and the cook see different ones.")
rs_analogy.icon("store", 300, 70, 2.4)
for (x, y, who, what) in [(40, 40, "toddler's eye", "sockets, corners"), (40, 150, "grandma", "loose rug, stairs"), (560, 40, "the cook", "pan handles"), (560, 150, "dad", "smoke alarm battery")]:
    rs_analogy.box(x, y, 170, 70, who, "y", sub=what, size=16, subsize=14)
for (x1, y1, x2, y2) in [(214, 75, 300, 120), (214, 185, 300, 190), (556, 75, 450, 120), (556, 185, 450, 190)]:
    rs_analogy.line(f"M{x1} {y1} L{x2} {y2}", dash=True, thin=True)
rs_analogy.note(380, 246, "same house, different eyes", "pen")

rs_how = Doodle(760, 400, "Larder's risk-storming result. Nine people put red, amber and green stickies on the container diagram on their own, then compare. Clusters form on StockPilot sync, the single Postgres, the payment provider, the dispatch cron job and the Rotterdam date. Plotted on a likelihood and impact grid, the top five each get an owner and an action: cache stock (ADR 0005), load test at five times peak, a payment fallback plan, extract Dispatch, and a fixed scope for Rotterdam.",
                 "Stickies on the diagram, clusters, then likelihood × impact. The top five get owners and actions.")
rs_how.box(14, 20, 420, 300, None, "paper")
rs_how.head(224, 46, "container diagram", size=16)
for (x, y, w, t) in [(34, 70, 120, "apps"), (184, 70, 120, "Larder Core"), (318, 70, 104, "Dispatch"), (34, 200, 120, "Postgres"), (184, 200, 120, "StockPilot"), (318, 200, 104, "PSP")]:
    rs_how.box(x, y, w, 60, t, "blue", size=14)
sticky = [(150, 186, "red"), (160, 192, "red"), (296, 186, "red"), (302, 194, "red"), (310, 182, "red"), (402, 188, "red"), (410, 196, "y"), (402, 58, "red"), (410, 64, "red"), (290, 60, "y"), (146, 60, "green"), (30, 300, "y")]
cls = {"red": "f-pink d-red", "y": "f-y", "green": "f-green"}
for (x, y, c) in sticky:
    rs_how.raw(f'<rect class="d d-thin {cls[c]}" x="{x}" y="{y}" width="18" height="18" rx="2"/>')
rs_how.note(224, 300, "9 people · 10 min silent · then compare", "pen", size=15)
rs_how.raw('<rect class="f-hl" x="530" y="46" width="200" height="124" rx="8" style="stroke:none;opacity:.5"/>')
rs_how.line("M470 190 V40 M470 190 H740", thin=True)
rs_how.text(456, 30, "impact ↑", "t-s", anchor="start", size=15)
rs_how.note(690, 212, "likelihood →", "pen", size=15)
for (x, y, n) in [(690, 70, "1"), (630, 90, "2"), (560, 80, "3"), (680, 150, "4"), (590, 140, "5")]:
    rs_how.circle(x, y, 16, "pink", "red", n)
rs_how.box(470, 226, 276, 100, None, "y")
for i, a in enumerate(["1 cache stock (ADR 0005)", "2 fix Rotterdam scope", "3 load test at 5×, Jan", "4 PSP fallback · 5 extract Dispatch"]):
    rs_how.text(482, 250 + i * 22, a, anchor="start", size=13)
rs_how.note(380, 384, "each top risk: an owner, an action and a date", "pen")

RISK_STORMING = dict(
    slug="risk-storming",
    kicker="a.k.a. “the home safety walk”",
    tldr="Don't write the risk list alone. Put the <b>architecture diagram</b> on a wall, gather <b>everyone</b> who builds, runs or depends on the system, and have each person <b>silently</b> stick coloured notes on the parts they think are risky (red = high, amber = medium, green = low). Then <b>compare</b>: clusters and disagreements are where the conversation goes. Rank by likelihood and impact, and give the top few an <b>owner, an action and a date</b>.",
    chips=[("Family", "validating early"), ("Origin", "Simon Brown, risk-storming (riskstorming.com, ~2014)"), ("Lives in", "a 60–90 minute workshop; results in the risk register"), ("Pairs with", "system context &amp; C4 diagrams, constraints vs assumptions, risk register")],
    problem_side="Larder, before committing to Rotterdam",
    problem="""  <p class="lead">Before committing to the Rotterdam plan, Ana writes a risk list at her desk. Six items, all technical: schema migrations, a Django upgrade, test coverage. Missing: Tomás knows the store <b>Wi-Fi drops</b>; Cho knows the payment provider has <b>short outages on Friday evenings</b>; Joost lies awake over the <b>dispatch cron job</b>; and Lena and Marco know the Rotterdam date collides with the <b>StockPilot contract talks</b>. The worst risks are <span class="hl-pink">in other people's heads</span>.</p>
  <ul>
    <li>One person sees risks through one lens, usually their own speciality.</li>
    <li>In open discussion, the first or loudest voice anchors everyone else.</li>
    <li>Risks that nobody owns stay on the list and never get handled.</li>
  </ul>""",
    problem_figs=[rs_problem],
    analogy_side="the home safety walk",
    analogy="""  <p>Before a baby arrives, a family walks through the house with <b>stickers</b>, each marking the dangers they see. Get down to <b>toddler height</b> and you find sockets and sharp corners; <b>grandma</b> spots the loose rug on the stairs; the <b>cook</b> sees pan handles sticking out. Nobody alone finds them all. Together, in an hour, they find most.</p>""",
    analogy_figs=[rs_analogy],
    map=[("The house", "The architecture diagram (context or container view)"),
         ("Each family member's view", "Each role's view: dev, ops, store, payments, legal"),
         ("Stickers on the dangers", "Coloured stickies on the risky parts"),
         ("Several stickers on one spot", "A cluster: a risk many people see"),
         ("Fixing the worst first", "Owners and actions for the top risks")],
    how_side="diagram, silence, compare, act",
    how="""  <p>The key is the <b>silent, individual</b> first round: ten minutes where everyone marks risks <b>before</b> hearing anyone else. Only then compare. Clusters show shared worries; a single red sticky from the one person who runs the stores is often the most important finding of the day.</p>""",
    how_figs=[rs_how],
    steps=[("Draw the diagram", "A context or container diagram everyone can read, printed big or on a shared board."),
           ("Invite the mix", "Engineers, operations, security, product, and the people who run the business process."),
           ("Silent round (10 min)", "Each person writes risks on red, amber or green stickies and places them on the diagram."),
           ("Compare and cluster (20 min)", "Group duplicates, discuss differences: “why did you mark that red?”"),
           ("Rank (15 min)", "Place the clusters on likelihood × impact. Pick the top five."),
           ("Assign and track (15 min)", "Each top risk gets an owner, an action, a date, and goes into the risk register.")],
    vocab=[("Risk", "Something that might happen and would hurt the goals if it did."),
           ("Likelihood", "How probable the risk is."),
           ("Impact", "How badly it would hurt if it happened."),
           ("Mitigation", "An action that lowers likelihood or impact."),
           ("Risk owner", "The person responsible for watching and handling one risk."),
           ("Risk register", "The tracked list of risks, owners, actions and status.")],
    code=dict(file="docs/workshops/2025-12-04-risk-storming.md", note="session result, top five", plain=True, src="""
# Risk-storming: Rotterdam plan                    Thu 4 Dec 2025, 14:00–15:30
Diagram   container view v3 (docs/architecture/containers.dsl)
People    Ana, Ben, Cho, Dee, Eli, Joost, Tomás, Lena, Priya          (9)
Stickies  47 (21 red, 18 amber, 8 green) → 11 clusters

| # | Risk                                      | L | I | Owner | Action                              | By     |
|---|-------------------------------------------|---|---|-------|-------------------------------------|--------|
| 1 | StockPilot API limit (10 req/s) at 6 cities| H | H | Ben   | cache stock per store (ADR 0005)    | 26 Jan |
| 2 | Rotterdam date slips (lease fixed)        | M | H | Ana   | fixed scope list, weekly check      | weekly |
| 3 | One Postgres at 5× peak                   | M | H | Eli   | load test at 5× (QAS-1)             | 23 Jan |
| 4 | Payment provider down on Friday peak      | M | H | Cho   | fallback: queue + retry, status msg | 13 Feb |
| 5 | Dispatch cron (30 s) too slow for 2 cities| H | M | Ben   | extract Dispatch service (ADR 0002) | Mar    |

Surprise of the day: Tomás's single red sticky on the picker app (Wi-Fi) → ASR-2.
Next session: after the walking skeleton (late January).
"""),
    tools="tools: a printed diagram and coloured stickies, or a Miro / FigJam board with the diagram as background; Simon Brown's riskstorming.com has the method and printable materials. Results go into the risk register.",
    gains=["<b>More risks found</b>: every role sees different ones.",
           "<b>Less anchoring</b>: the silent round stops the loudest voice steering.",
           "<b>Shared ownership</b>: people own the risks they raised.",
           "<b>Quick</b>: 60–90 minutes for a whole-system view.",
           "<b>Visible on the design</b>: risks sit on the parts they affect."],
    losses=["<b>Needs a good diagram</b> first, readable by non-engineers.",
            "<b>A busy room</b>: an hour or more of many people's time.",
            "<b>Subjective ratings</b>: likelihood and impact are guesses.",
            "<b>Easy to stop at the wall</b> without owners and actions."],
    baseline="Each line compares <b>a risk list written by the architect alone</b> to <b>a risk-storming session with every role, ending in owners, actions and dates in the risk register</b>.",
    ratings=[(3, 4, "The diagram shows where the risks sit."),
             (2, 5, "Every role's worries are heard and weighed together."),
             (3, 4, "Ninety minutes to a ranked, owned list."),
             (2, 5, "Risks from operations, payments and legal are found early."),
             (3, 4, "Early mitigation keeps the plan flexible."),
             (2, 4, "The session note and register record who raised what."),
             (3, 3, "Some risks have a cost attached; not the focus."),
             (3, 3, "A workshop of 6–10 people, repeated at milestones."),
             (2, 4, "Teams own and handle their own risks.")],
    pitfalls=[("Talking before marking", "The architect explains the risks first, and everyone agrees.", "silent individual round first; discuss only after."),
              ("Only engineers", "All the stickies are technical.", "invite operations, security, legal and the business."),
              ("No owners", "A beautiful wall of stickies and no next step.", "top five each get an owner, action and date before people leave."),
              ("Once only", "Run at kick-off, never again.", "repeat at milestones: after the skeleton, before go-live.")],
    use=["Before committing to a plan, date or budget.",
         "After the first architecture diagram exists.",
         "At milestones: after the walking skeleton, before go-live.",
         "When a team is new to the system or the domain."],
    skip=["Tiny changes with obvious risks.",
          "When there's no diagram yet: draw the context diagram first.",
          "As a replacement for threat modelling: security needs its own deep dive."],
    related=["<b>System context diagram</b> (this volume)", "<b>Constraints vs assumptions</b> (this volume)", "<b>Risk register</b> (Vol. 6)", "<b>Threat modelling</b> (patterns, Vol. 5)"],
    quiz=[("Why start with a silent, individual round?", "So everyone marks their own risks before being anchored by the first or loudest voice."),
          ("What do the sticky colours mean?", "Red = high risk, amber = medium, green = low."),
          ("What should every top risk leave the room with?", "An owner, an action and a date, recorded in the risk register."),
          ("Why put risks on the diagram rather than in a list?", "They sit on the parts they affect, so clusters and blind spots are visible.")],
    try_it="Print your system's context or container diagram. Ask three people from different roles to spend five minutes, separately, marking risks on their own copy. Lay the copies side by side. Which risk appears on only one copy, and who marked it?",
    remember="Same house, <span class=\"hl\">different eyes</span>. Mark in <span class=\"hl\">silence</span>, then compare, then assign.",
    sources=["Simon Brown, “Risk-storming” (riskstorming.com) and <i>Software Architecture for Developers</i>.",
             "Simon Brown, <i>The C4 Model for Visualising Software Architecture</i> (Leanpub).",
             "ISO 31000:2018, Risk management guidelines.",
             "Len Bass et al., <i>Software Architecture in Practice</i>, 4th ed. (2021), architecture evaluation."],
)

NOTES = [SPIKES, FITNESS, RISK_STORMING]
