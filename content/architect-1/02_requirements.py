# Series 2 · The Solution Architect's Notebook · Vol. 1 · Requirements that shape architecture.
# Running case study: Larder (facts in docs/larder-casebook.md).

# ------------------------------------------------------------------ 05 Architecturally Significant Requirements
asr_problem = Doodle(760, 280, "Doodle of Larder's backlog: 340 user stories, all treated the same. The loudest request, recipe recommendations with machine learning, gets design time. The one that shapes the architecture, the picker app must work when the store Wi-Fi drops, is buried in support ticket 4127.",
                     "340 stories, all the same size on the board. The one that shapes the system is buried in a ticket.")
for i in range(6):
    asr_problem.box(20 + i * 8, 30 + i * 10, 200, 120, None, "paper")
asr_problem.head(165, 120, "340 stories", size=20)
asr_problem.text(165, 146, "all “priority: high”", size=16)
asr_problem.box(300, 30, 220, 70, "recipe ideas (ML)", "y", sub="loudest · 3 meetings", size=17, subsize=15)
asr_problem.note(410, 124, "gets the design time", "pen")
asr_problem.box(300, 160, 220, 80, "ticket #4127", "pink", sub="“Noord Wi-Fi drops weekly”", stroke="red", size=17, subsize=14)
asr_problem.arrow(526, 200, 586, 200, color="red")
asr_problem.box(592, 160, 156, 80, "shapes the", "pink", sub="picker app", stroke="red", size=17, subsize=16)
asr_problem.note(670, 266, "nobody saw it", "red")

asr_analogy = Doodle(760, 260, "Doodle of a house being designed. Most wishes, like paint colour, curtains and taps, can change any time. A few decide the structure: a lift for grandma needs a shaft, a recording studio needs soundproof walls and a strong floor, a basement must be dug first. Those must reach the architect before the foundation is poured.",
                     "Paint can change any day. A lift shaft can't. Tell the architect before the concrete is poured.")
asr_analogy.box(20, 30, 230, 190, None, "paper")
asr_analogy.head(135, 60, "change any time", size=18)
for i, t in enumerate(["paint colour", "curtains", "taps", "door handles"]):
    asr_analogy.text(135, 96 + i * 30, t, size=16)
asr_analogy.box(280, 30, 300, 190, None, "y")
asr_analogy.head(430, 60, "decide the structure", size=18)
for i, t in enumerate(["lift for grandma → shaft", "studio → floor load", "basement → dig first"]):
    asr_analogy.text(430, 100 + i * 34, t, size=16)
asr_analogy.arrow(586, 125, 636, 125)
asr_analogy.icon("bricks", 646, 96, 1.2)
asr_analogy.note(688, 180, "foundation", "pen")
asr_analogy.note(688, 204, "poured", "pen")

asr_how = Doodle(760, 360, "The ASR filter. Every candidate requirement passes four questions: is it costly to change later, does it touch many parts, is it high value or high risk, is it an unusual or demanding quality? If yes, it is architecturally significant. At Larder, five pass: a new city is configuration, the picker app works 30 minutes offline, checkout under 800 milliseconds at five times peak, no order lost or charged twice, and EU data with Belgian VAT. Wishlists, recipe pages and dark mode don't.",
                  "Four questions filter 340 stories down to five that shape the design.")
asr_how.box(14, 20, 230, 230, None, "blue")
asr_how.head(129, 48, "the four questions", size=17)
for i, q in enumerate(["costly to change later?", "touches many parts?", "high value or risk?", "tough or unusual quality?"]):
    asr_how.text(26, 86 + i * 42, f"{i + 1}. {q}", anchor="start", size=15)
asr_how.arrow(250, 135, 300, 135, label="any yes", lx=275, ly=121)
asrs = ["ASR 1 · a city is config", "ASR 2 · picker 30 min offline", "ASR 3 · checkout < 800 ms at 5×", "ASR 4 · never lost or double", "ASR 5 · EU data, Belgian VAT"]
for i, t in enumerate(asrs):
    asr_how.box(306, 14 + i * 48, 290, 40, None, "green")
    asr_how.text(320, 40 + i * 48, "✓ " + t, anchor="start", size=16)
asr_how.box(616, 40, 130, 170, None, "paper", dash=True)
asr_how.head(681, 66, "not ASRs", size=16)
for i, t in enumerate(["wishlists", "recipe pages", "dark mode", "new filters"]):
    asr_how.text(681, 100 + i * 28, t, "t t-soft", size=15)
asr_how.note(380, 300, "5 of 340: design for these first; the other 335 fit inside", "pen")
asr_how.note(380, 330, "each one has a source, a measure and an owner", "pen", size=18)

ASR = dict(
    slug="asr",
    kicker="a.k.a. “the lift shaft, not the paint”",
    tldr="Most requirements fit into almost any architecture. A <b>few</b> don't: they're <b>costly to change later</b>, touch <b>many parts</b>, carry <b>high value or risk</b>, or demand an <b>unusual quality</b>. Those are <b>architecturally significant requirements (ASRs)</b>. Find them early, often buried in support tickets and side remarks rather than the backlog, write each one with a <b>measure and an owner</b>, and design for them first. The rest will fit inside.",
    chips=[("Family", "requirements that shape architecture"), ("Origin", "Len Bass et al., <i>Software Architecture in Practice</i>; Eoin Woods, Rozanski"), ("Lives in", "a short list at the top of the architecture overview"), ("Pairs with", "business drivers, quality attribute scenarios, ADRs")],
    problem_side="Larder, 340 stories",
    problem="""  <p class="lead">Larder's backlog has <b>340 user stories</b>, nearly all marked “high”. The loudest one, ML-powered recipe ideas, gets three design meetings. Meanwhile ticket <b>#4127</b> from the Noord store says the Wi-Fi drops about once a week and pickers stand idle for 20 minutes. That one quietly <span class="hl-pink">decides how the picker app must be built</span>, and nobody in the design meetings has read it.</p>
  <ul>
    <li>A flat backlog hides which requirements shape the structure and which are decoration.</li>
    <li>The significant ones often come from operations, legal or support, not from product.</li>
    <li>Found late, they mean rework of the foundations, not a new feature.</li>
  </ul>""",
    problem_figs=[asr_problem],
    analogy_side="the lift shaft",
    analogy="""  <p>When you design a house, most wishes can change any time: paint, curtains, taps. A <b>few</b> decide the structure: a <b>lift</b> for grandma needs a shaft, a recording studio needs a stronger floor, a basement must be dug first. Mention those after the concrete is poured and they cost ten times more, or can't happen at all.</p>""",
    analogy_figs=[asr_analogy],
    map=[("Paint, curtains, taps", "Ordinary features: they fit almost any architecture"),
         ("The lift for grandma", "An ASR: changes the structure if added late"),
         ("Pouring the foundation", "Early architecture decisions: datastores, boundaries, deployment"),
         ("Telling the architect first", "Finding ASRs before the first big decisions"),
         ("The building inspector", "Compliance, security and data-residency rules")],
    how_side="filter, then design for the few",
    how="""  <p>Run every candidate through four questions. If any answer is <b>yes</b>, it's a candidate ASR. Then hunt where they hide: <b>support tickets, incident reports, contracts, legal advice, operations complaints</b>, and the answers to “what would make this project fail?”</p>""",
    how_figs=[asr_how],
    steps=[("Gather widely", "Backlog, drivers, incident reviews, support tickets, contracts, legal and security advice, stakeholder interviews."),
           ("Apply the four questions", "Costly to change? Touches many parts? High value or risk? Tough or unusual quality? Any yes → candidate."),
           ("Make each one measurable", "“Works offline” becomes “picker app keeps working 30 minutes without Wi-Fi”."),
           ("Name the source and owner", "Where it came from (ticket #4127) and who can confirm it (Tomás)."),
           ("Keep the list short", "Usually 5–10. If everything is significant, nothing is."),
           ("Design for them first", "Each ASR should be traceable to a decision (an ADR) and, later, a test.")],
    vocab=[("ASR", "Architecturally significant requirement: one that shapes the architecture."),
           ("Functional requirement", "What the system does (“customer can reorder”)."),
           ("Quality attribute", "How well it does it (fast, available, secure)."),
           ("Constraint", "A fixed rule the design must obey."),
           ("Traceability", "Linking each ASR to its source, decision and test."),
           ("Utility tree", "A ranked tree of quality goals and scenarios, from ATAM.")],
    code=dict(file="docs/architecture/02-asrs.md", note="Larder's significant requirements, v1", plain=True, src="""
# Architecturally significant requirements                  v1 · 2025-11-03

| ID    | Requirement                                   | Source                 | Why significant            | Owner |
|-------|-----------------------------------------------|------------------------|----------------------------|-------|
| ASR-1 | A new city is configuration, not code:        | Driver 1; Noord store  | touches every module       | Joost |
|       | stores, zones, hours, prices, VAT             | took 5 months          |                            |       |
| ASR-2 | Picker app keeps working 30 min offline        | ticket #4127, Tomás    | changes app + sync design  | Tomás |
| ASR-3 | Checkout p95 < 800 ms at 5× normal peak        | King's Day 2025 outage | datastore, caching, scale  | Priya |
| ASR-4 | No order lost or charged twice, even on crash  | Driver 4; support data | integration + transactions | Ben   |
| ASR-5 | Customer data stays in the EU; Belgian VAT     | Lena (DPO), Antwerp    | hosting, vendors, invoices | Lena  |

Considered, not significant: wishlists, recipe pages, dark mode, new search filters.
Each ASR → a quality attribute scenario (docs/architecture/03-scenarios.md) → an ADR.
"""),
    tools="tools: a short Markdown list is enough. Requirements tools (Jira, Azure DevOps) can tag ASRs with a label so they stand out; Structurizr and arc42 both have a place for them.",
    gains=["<b>Focus</b>: design effort goes to the few requirements that shape the system.",
           "<b>Hidden needs found early</b>: offline stores, legal rules, peak days.",
           "<b>Simpler designs</b>: everything else just has to fit inside.",
           "<b>Traceable decisions</b>: each big choice points to the ASR it serves.",
           "<b>Better conversations</b>: stakeholders see why their need changes the design."],
    losses=["<b>Judgement call</b>: what counts as significant can be argued.",
            "<b>Digging takes time</b>: tickets, incidents, contracts and interviews.",
            "<b>False confidence</b>: a missed ASR is still missed.",
            "<b>Can be gamed</b>: everyone wants their request labelled significant."],
    baseline="Each line compares <b>designing from a flat backlog where every story looks the same</b> to <b>a short, measurable list of ASRs with sources and owners, designed for first</b>.",
    ratings=[(2, 4, "Anyone can see which few needs shape the system."),
             (2, 4, "Stakeholders agree which of their needs are structural."),
             (2, 4, "Design debates focus on five items, not 340."),
             (2, 5, "Structural needs are found before the foundations are poured."),
             (3, 4, "Designing for the right few keeps the rest cheap to change."),
             (2, 5, "Each ASR links to its source, its decision and its test."),
             (2, 3, "Expensive needs (5× peak) are visible early."),
             (3, 3, "A few days of digging; a short list to maintain."),
             (2, 3, "Teams can build features freely inside the agreed structure.")],
    pitfalls=[("Only reading the backlog", "The significant needs live in tickets, incidents and contracts.", "read support, incident and legal sources, and ask operations."),
              ("Everything is significant", "The list has 40 items and decides nothing.", "apply the four questions strictly; aim for 5–10."),
              ("Vague ASRs", "“Must be scalable” is on the list.", "make each one measurable with a quality attribute scenario."),
              ("Found, then forgotten", "The list exists but no decision points to it.", "link each ASR to an ADR and, later, a fitness function.")],
    use=["A new system, a rebuild, or a big change of scale or market.",
         "When the backlog is long and flat.",
         "Before choosing datastores, boundaries, hosting or vendors.",
         "When incidents keep coming from the same structural weakness."],
    skip=["Small features inside an established architecture.",
          "Prototypes meant to be thrown away.",
          "When the list exists: review it at each big change instead."],
    related=["<b>Business drivers &amp; goals</b> (this volume)", "<b>Quality attribute scenarios</b> (this volume)", "<b>Constraints vs assumptions</b> (this volume)", "<b>Architecture decision records</b> (Vol. 2)"],
    quiz=[("Name the four questions that flag an ASR.", "Is it costly to change later? Does it touch many parts? Is it high value or high risk? Is it an unusual or demanding quality?"),
          ("Where do ASRs often hide?", "In support tickets, incident reports, contracts, legal advice and operations complaints, not just the backlog."),
          ("Why is “must be scalable” a poor ASR?", "It isn't measurable; turn it into a scenario with a load, a context and a response measure."),
          ("Why keep the list to five to ten?", "If everything is significant, nothing guides the design.")],
    try_it="Read the last 30 support tickets or incident reports for your system. List every need that the current architecture makes hard to meet. Run each through the four questions. Did any of them make it into your backlog?",
    remember="Find the <span class=\"hl\">lift shafts</span> before the concrete is poured. The paint can wait.",
    sources=["Len Bass, Paul Clements &amp; Rick Kazman, <i>Software Architecture in Practice</i>, 4th ed. (2021).",
             "Lianping Chen, Muhammad Ali Babar &amp; Bashar Nuseibeh, “Characterizing Architecturally Significant Requirements” (IEEE Software, 2013).",
             "Nick Rozanski &amp; Eoin Woods, <i>Software Systems Architecture</i>, 2nd ed. (2011).",
             "Michael Keeling, <i>Design It!</i> (2017), chapter on architecturally significant requirements."],
)

# ------------------------------------------------------------------ 06 Quality Attribute Scenarios
qa_problem = Doodle(760, 270, "Doodle of a requirements document that says the system must be fast and highly available. Four people read 'fast' four ways: under 2 seconds, under 200 milliseconds, faster than the competitor, and fast on a good day. On King's Day 2025 checkout timed out for 40 minutes, and everyone said the requirement had been met.",
                    "“Fast and highly available.” Four readers, four meanings, and one 40-minute outage that “met the requirement”.")
qa_problem.box(20, 30, 230, 110, None, "paper")
qa_problem.head(135, 62, "requirements v3", size=17)
qa_problem.text(135, 96, "“the system must be", size=16)
qa_problem.text(135, 120, "fast and highly available”", size=16)
for i, (who, t) in enumerate([("Priya", "< 2 seconds"), ("Ben", "< 200 ms"), ("Marco", "faster than rivals"), ("Eli", "fast on a normal day")]):
    y = 20 + i * 44
    qa_problem.line(f"M256 85 L300 {y + 18}", thin=True)
    qa_problem.box(304, y, 230, 36, None, "blue")
    qa_problem.text(316, y + 24, f"{who}: {t}", anchor="start", size=15)
qa_problem.box(570, 40, 176, 100, "King's Day", "pink", sub="checkout down 40 min", stroke="red", size=18, subsize=14)
qa_problem.note(380, 228, "“but it was fast!” (on a normal day)", "red")

qa_analogy = Doodle(760, 240, "Doodle of a car spec sheet. Not 'a fast car', but: from standstill, flooring the pedal, with two passengers on a dry road, it reaches 100 kilometres an hour in 7.5 seconds. The stimulus, the conditions and the measure are all stated, so anyone can test it.",
                     "Not “a fast car”: 0–100 km/h in 7.5 s, two passengers, dry road. Anyone can test that.")
qa_analogy.icon("chassis", 20, 70, 1.6)
qa_analogy.box(180, 24, 170, 54, "“a fast car”", "pink", stroke="red", size=17)
qa_analogy.note(265, 100, "✗ can't test it", "red")
qa_analogy.box(400, 24, 340, 170, None, "green")
for i, (k, v) in enumerate([("stimulus", "floor the pedal"), ("from", "standstill"), ("conditions", "2 passengers, dry road"), ("measure", "100 km/h in 7.5 s")]):
    qa_analogy.text(416, 60 + i * 36, k, "t t-soft", anchor="start", size=15)
    qa_analogy.text(530, 60 + i * 36, v, anchor="start", size=16)
qa_analogy.note(570, 224, "✓ anyone can test it", "green")

qa_how = Doodle(760, 330, "The six parts of a quality attribute scenario, for Larder's King's Day checkout. Source: customers on King's Day. Stimulus: three thousand checkout requests per second, five times normal peak. Artifact: the checkout and payment path. Environment: normal operation, one of two app servers lost. Response: the order is confirmed and the payment taken once. Response measure: 95 percent confirmed within 800 milliseconds, zero lost orders.",
                 "Six parts make “fast” testable. This is ASR 3 written as a scenario.")
parts = [("source", "customers", "on King's Day"), ("stimulus", "3,000 req/s", "5× normal peak"), ("artifact", "checkout", "and payment path"),
         ("environment", "normal ops", "1 of 2 servers lost"), ("response", "order confirmed", "charged once"), ("measure", "p95 < 800 ms", "0 lost orders")]
for i, (k, v, sub) in enumerate(parts):
    col, row = i % 3, i // 3
    x, y = 14 + col * 250, 40 + row * 140
    fill = "green" if i == 5 else ("y" if i == 1 else "blue")
    qa_how.note(x + 112, y - 8, k, "pen", size=17)
    qa_how.box(x, y, 224, 80, v, fill, sub=sub, size=17, subsize=14)
    if col < 2:
        qa_how.arrow(x + 228, y + 40, x + 248, y + 40)
qa_how.note(380, 300, "if you can't write the measure, you can't test it, so you haven't agreed it", "pen")

QA_SCENARIOS = dict(
    slug="quality-attribute-scenarios",
    kicker="a.k.a. “0–100 in 7.5 seconds, not ‘fast’”",
    tldr="Words like <b>fast, available, secure, scalable</b> mean different things to everyone. Rewrite each one as a <b>quality attribute scenario</b>: a <b>source</b> sends a <b>stimulus</b> to part of the system (the <b>artifact</b>) in a given <b>environment</b>; the system gives a <b>response</b> that you can check with a <b>response measure</b>. Now “fast” is a sentence you can agree on, design for and test.",
    chips=[("Family", "requirements that shape architecture"), ("Origin", "SEI, Bass, Clements &amp; Kazman; used in ATAM (2000)"), ("Lives in", "a scenario table next to the ASRs"), ("Pairs with", "ASRs, NFR checklist, fitness functions, utility tree")],
    problem_side="Larder, “fast and highly available”",
    problem="""  <p class="lead">Larder's old requirements document says the system “must be fast and highly available”. Priya reads that as under two seconds, Ben as under 200 ms, Marco as faster than the competition, Eli as fast on a normal day. On <b>King's Day 2025</b> checkout timed out for <span class="hl-pink">40 minutes</span>, and in the review, everyone could argue the requirement had been met.</p>
  <ul>
    <li>Adjectives can't be designed for, tested or signed off.</li>
    <li>The hard part, <i>under what conditions?</i>, is always missing.</li>
    <li>Without a measure there's no way to tell when you've done enough.</li>
  </ul>""",
    problem_figs=[qa_problem],
    analogy_side="the car spec sheet",
    analogy="""  <p>No carmaker prints “a fast car” on the spec sheet. They print <b>0–100 km/h in 7.5 seconds</b>, measured from standstill, flooring the pedal, with two people on board, on a dry road. The stimulus, the conditions and the measure are all there, so a magazine can test it and prove it wrong.</p>""",
    analogy_figs=[qa_analogy],
    map=[("Flooring the pedal", "Stimulus: 3,000 checkout requests per second"),
         ("The driver", "Source: customers on King's Day"),
         ("The engine and gearbox", "Artifact: the checkout and payment path"),
         ("Two passengers, dry road", "Environment: normal operation, one server down"),
         ("0–100 in 7.5 s", "Response measure: p95 under 800 ms, no lost orders")])
QA_SCENARIOS.update(
    how_side="six parts, one testable sentence",
    how="""  <p>The six parts force the missing questions: <i>who</i> triggers it, <i>how much</i>, <i>to which part</i>, <i>under what conditions</i>, and <i>how we'll know</i>. Write two or three per important quality; the environment (“on King's Day”, “during a deploy”, “with one zone down”) is usually where the real requirement hides.</p>""",
    how_figs=[qa_how],
    steps=[("Pick the qualities that matter", "Use the drivers and ASRs: performance, availability, modifiability, security, privacy…"),
           ("Write the stimulus and source", "Who or what triggers it, and how much: “3,000 checkouts/s from customers”."),
           ("State the environment", "Normal day, peak, during a deploy, a zone down, a new city being added."),
           ("Define the response and measure", "What should happen and the number that proves it: p95, %, minutes, euros, days."),
           ("Rank them", "With stakeholders, rate each by business value and technical difficulty (H/M/L)."),
           ("Make them tests", "High-value scenarios become load tests, chaos drills and fitness functions.")],
    vocab=[("Stimulus", "The event that arrives: a request, a failure, a change request."),
           ("Source", "Who or what produces the stimulus."),
           ("Artifact", "The part of the system that is stimulated."),
           ("Environment", "The conditions: normal, peak, degraded, during a deploy."),
           ("Response measure", "The number that shows the response was good enough."),
           ("p95", "95 % of requests are faster than this.")],
    code=dict(file="docs/architecture/03-scenarios.md", note="three of Larder's scenarios", plain=True, src="""
# Quality attribute scenarios                                    v1 · 2025-11-05

QAS-1 Performance (ASR-3)                               value H · difficulty M
  Source:      customers on King's Day
  Stimulus:    3,000 checkout requests/s (5× normal peak) for 2 hours
  Artifact:    checkout and payment path
  Environment: normal operation; one of two app servers lost
  Response:    order confirmed, payment taken exactly once
  Measure:     p95 < 800 ms · 0 lost or double-charged orders

QAS-2 Availability (ASR-2)                              value H · difficulty M
  Source:      the dark store network
  Stimulus:    store Wi-Fi drops
  Artifact:    picker app
  Environment: Friday peak, 40 open pick lists
  Response:    pickers keep picking; changes sync when Wi-Fi returns
  Measure:     30 min offline with no lost picks · sync done < 2 min after

QAS-3 Modifiability (ASR-1)                             value H · difficulty H
  Source:      operations team
  Stimulus:    “open Utrecht”
  Artifact:    stores, zones, hours, prices, VAT configuration
  Environment: normal week, no developer involved
  Response:    the city is set up and testable
  Measure:     ≤ 1 day of configuration · 0 code changes or deploys
"""),
    tools="tools: a Markdown table or the arc42 “quality requirements” section. k6, Gatling or Locust turn performance scenarios into tests; chaos tools (Chaos Mesh, AWS FIS) test availability scenarios.",
    gains=["<b>One meaning</b> for “fast” and “available”, agreed by business and engineering.",
           "<b>Testable</b>: scenarios become load tests, drills and fitness functions.",
           "<b>Know when to stop</b>: the measure says when the design is good enough.",
           "<b>Conditions made explicit</b>: peak days and failures stop being surprises.",
           "<b>Better trade-offs</b>: ranked scenarios show which quality wins a conflict."],
    losses=["<b>Effort</b>: good scenarios take discussion and real numbers.",
            "<b>False precision</b>: early numbers are guesses and need revisiting.",
            "<b>Easy to write too many</b>: dozens of low-value scenarios.",
            "<b>Hard for some qualities</b>: usability or evolvability resist a single number."],
    baseline="Each line compares <b>quality requirements written as adjectives (“fast, highly available”)</b> to <b>a ranked set of six-part scenarios with measures, turned into tests</b>.",
    ratings=[(1, 5, "“p95 under 800 ms at 5× peak” means one thing to everyone."),
             (2, 4, "Stakeholders agree the numbers and the ranking."),
             (2, 4, "Debates end with “does it meet QAS-1?”"),
             (2, 5, "Peak days and failures are designed for, not discovered."),
             (3, 3, "Neutral; modifiability scenarios help, but don't change the design themselves."),
             (2, 4, "Each scenario links an ASR to a test."),
             (2, 4, "Measures show when more spending stops paying off."),
             (3, 3, "A few hours per scenario; they need updating."),
             (2, 4, "Teams can check their own work against the measures.")],
    pitfalls=[("Missing the environment", "“p95 under 800 ms”, but on which day, under what load?", "always state the conditions: peak, degraded, during a deploy."),
              ("Numbers from nowhere", "“99.999 %” because it sounds good.", "derive measures from drivers and data; ask what each nine costs."),
              ("Scenarios that never become tests", "A beautiful table nobody checks.", "turn the high-value ones into load tests, drills and fitness functions."),
              ("Only performance", "Ten latency scenarios, none for change, security or operations.", "cover the qualities your drivers care about, including modifiability.")],
    use=["Any quality that drives the architecture: performance, availability, security, change.",
         "When requirements say “fast”, “robust” or “scalable” with no numbers.",
         "Before choosing between options with different quality trade-offs.",
         "As input to an architecture review (ATAM, risk-storming)."],
    skip=["Qualities nobody is worried about for this system.",
          "Tiny internal tools where “good enough” is obvious.",
          "When you can't get any data yet: write a hypothesis and revisit after a spike."],
    related=["<b>Architecturally significant requirements</b> (this volume)", "<b>NFR checklist</b> (this volume)", "<b>Fitness functions</b> (this volume)", "<b>Quality attribute utility tree</b> (Vol. 5)"],
    quiz=[("Name the six parts of a quality attribute scenario.", "Source, stimulus, artifact, environment, response, response measure."),
          ("Which part most often hides the real requirement?", "The environment: peak day, degraded mode, during a deploy."),
          ("Write “the picker app must be reliable” as a scenario.", "When store Wi-Fi drops during Friday peak, pickers keep picking; 30 minutes offline with no lost picks, synced within 2 minutes after."),
          ("Why rank scenarios by value and difficulty?", "So the team focuses on high-value, hard ones first and knows which quality wins a conflict.")],
    try_it="Find one adjective in your project's requirements (“fast”, “secure”, “scalable”). Rewrite it as a six-part scenario. Then ask two stakeholders separately what the response measure should be. If their numbers differ, you've just found a conversation that needed to happen.",
    remember="Not “fast”: <span class=\"hl\">who, how much, where, under what conditions, measured how</span>.",
    sources=["Len Bass, Paul Clements &amp; Rick Kazman, <i>Software Architecture in Practice</i>, 4th ed. (2021), chapters 4–14.",
             "Rick Kazman, Mark Klein &amp; Paul Clements, “ATAM: Method for Architecture Evaluation” (SEI, 2000).",
             "arc42 template, section 10 “Quality Requirements” (arc42.org).",
             "ISO/IEC 25010, Systems and software quality models."],
)

# ------------------------------------------------------------------ 07 Constraints vs Assumptions
ca_problem = Doodle(760, 270, "Doodle of Larder's kick-off document. It mixes facts and beliefs in one list. 'We use StockPilot until June 2027' is a fixed constraint. 'StockPilot's API can serve six cities' is only a belief, but it is written the same way. The Rotterdam plan relies on it. A spike in November finds the API allows only ten requests per second per account.",
                    "Facts and beliefs in one list, written the same way. One belief was holding up the Rotterdam plan.")
ca_problem.box(20, 20, 330, 200, None, "paper")
ca_problem.head(185, 50, "kick-off doc · “facts”", size=17)
for i, (t, bad) in enumerate([("Rotterdam opens 27 April", False), ("StockPilot until June 2027", False), ("StockPilot API: 6 cities OK", True), ("couriers' phones have data", True)]):
    ca_problem.text(36, 90 + i * 34, "• " + t, "t t-red" if bad else "t", anchor="start", size=16)
ca_problem.arrow(356, 158, 420, 158, color="red")
ca_problem.box(426, 120, 320, 76, "spike, November:", "pink", sub="API limit 10 req/s per account", stroke="red", size=17, subsize=15)
ca_problem.note(586, 230, "the plan rested on a guess", "red")
ca_problem.note(586, 60, "Rotterdam plan", "pen")
ca_problem.arrow(586, 70, 586, 114, dash=True)

ca_analogy = Doodle(760, 260, "Doodle of planning a mountain hike. Constraints are fixed: the park gate closes at 20:00 and the permit is for six people, so the plan fits around them. Assumptions are beliefs: the bridge on the trail is open, and there will be water at the hut. Check them before leaving, or carry a backup.",
                     "A hike: the gate closes at 20:00 (plan around it). The bridge is open (check before you go).")
ca_analogy.box(20, 30, 330, 190, None, "blue")
ca_analogy.head(185, 60, "constraints: fixed", size=18)
ca_analogy.icon("clock", 34, 78, 0.9)
ca_analogy.text(98, 110, "gate closes 20:00", anchor="start", size=16)
ca_analogy.icon("ticket", 34, 128, 0.9)
ca_analogy.text(98, 158, "permit: 6 people", anchor="start", size=16)
ca_analogy.box(410, 30, 330, 190, None, "y")
ca_analogy.head(575, 60, "assumptions: check!", size=18)
ca_analogy.text(430, 110, "? bridge is open", anchor="start", size=16)
ca_analogy.text(430, 150, "? water at the hut", anchor="start", size=16)
ca_analogy.note(575, 200, "call the ranger · carry water", "pen")
ca_analogy.note(185, 206, "plan around them", "pen")

ca_how = Doodle(760, 340, "Sorting statements into two lists. Constraints are given: record the source and who could change them, then design within them. Assumptions are beliefs: each gets an owner, a way to test it and a date. When tested, an assumption either becomes a fact, or it is wrong and becomes a risk or a design change. At Larder the StockPilot assumption was tested by a spike, proved wrong, and led to ADR 0005: cache stock per store.",
                 "Constraints are designed within; assumptions are tested by a date, then become facts or changes.")
ca_how.box(14, 20, 200, 60, "a statement", "paper", size=18)
ca_how.arrow(220, 40, 296, 30, label="given", lx=252, ly=24)
ca_how.arrow(220, 62, 296, 186, label="believed", lx=246, ly=150, anchor="end")
ca_how.box(302, 10, 260, 90, "constraint", "blue", sub="source · who could change it", size=18, subsize=14)
ca_how.arrow(566, 55, 616, 55)
ca_how.box(620, 18, 128, 74, "design", "blue", sub="within it", size=17, subsize=14)
ca_how.box(302, 150, 260, 90, "assumption", "y", sub="owner · test · by when", size=18, subsize=14)
ca_how.arrow(566, 180, 616, 150, color="green", label="true", lx=584, ly=150, anchor="end")
ca_how.box(620, 116, 128, 54, "fact", "green", size=17)
ca_how.arrow(566, 214, 616, 240, color="red", label="false", lx=584, ly=250, anchor="end")
ca_how.box(620, 210, 128, 66, "risk or", "pink", sub="design change", stroke="red", size=16, subsize=13)
ca_how.note(380, 298, "StockPilot can serve 6 cities? → spike, Nov → ✗ 10 req/s → ADR 0005: cache stock per store", "pen", size=17)

CONSTRAINTS = dict(
    slug="constraints-assumptions",
    kicker="a.k.a. “the gate closes at 20:00; is the bridge open?”",
    tldr="Split everything you “know” about a project into two lists. <b>Constraints</b> are fixed rules you must design within: a date, a contract, a law, a budget, a skill set; record where each comes from and who could change it. <b>Assumptions</b> are things you <b>believe but haven't checked</b>; give each an owner, a test and a deadline. Plans fail on assumptions written as if they were facts.",
    chips=[("Family", "requirements that shape architecture"), ("Origin", "project and risk management (RAID logs); TOGAF, arc42 constraints"), ("Lives in", "a constraints & assumptions log next to the ASRs"), ("Pairs with", "spike vs PoC, risk-storming, risk register")],
    problem_side="Larder, the kick-off document",
    problem="""  <p class="lead">Larder's kick-off document lists “facts”: <i>Rotterdam opens 27 April</i> (true: the store lease is signed), <i>StockPilot stays until June 2027</i> (true: the contract), and <i>StockPilot's API can serve six cities</i>. That last one is <b>a belief</b>, written exactly like the facts, and the Rotterdam plan rests on it. A spike in November finds the API allows <span class="hl-pink">10 requests per second per account</span>. Three weeks of plan, built on a guess.</p>
  <ul>
    <li>Beliefs written as facts never get checked.</li>
    <li>Real constraints are sometimes softer than they look (“we must use X”: says who?).</li>
    <li>When an assumption fails late, it fails during delivery, the most expensive moment.</li>
  </ul>""",
    problem_figs=[ca_problem],
    analogy_side="planning a hike",
    analogy="""  <p>Planning a mountain hike, some things are <b>fixed</b>: the park gate closes at 20:00, the permit is for six people. You plan around them. Other things you <b>believe</b>: the bridge on the trail is open, there's water at the hut. A good hiker <b>calls the ranger</b> about the bridge and carries water anyway.</p>""",
    analogy_figs=[ca_analogy],
    map=[("The gate closes at 20:00", "Constraint: Rotterdam opens 27 April (lease signed)"),
         ("The permit for six", "Constraint: no more than four new hires in 2026"),
         ("“The bridge is open”", "Assumption: StockPilot's API can serve six cities"),
         ("Calling the ranger", "A spike, a vendor call, a test: checking the assumption"),
         ("Carrying water anyway", "A fallback plan in case the assumption is wrong")],
    how_side="two lists, two different treatments",
    how="""  <p>For every statement ask: <b>is this given, or do we believe it?</b> Constraints get a <b>source</b> (the lease, the contract, GDPR) and the name of whoever could relax them. Assumptions get an <b>owner, a test and a date</b>. Every assumption either becomes a fact, or becomes a risk or a design change.</p>""",
    how_figs=[ca_how],
    steps=[("List what you “know”", "Dates, budgets, vendors, laws, skills, volumes, user behaviour, partner capabilities."),
           ("Ask “given or believed?”", "Given → constraint. Believed, even strongly → assumption."),
           ("Challenge the constraints", "“Says who?” Some are preferences. Record the source and who could change it."),
           ("Give every assumption a test", "An owner, how to check (spike, vendor call, data), and the date it must be known by."),
           ("Rank by impact if wrong", "Test first the assumptions that would sink the plan."),
           ("Review weekly", "Move checked assumptions to facts, failed ones to risks or decisions (ADRs).")],
    vocab=[("Constraint", "A fixed rule the design must obey: law, date, contract, budget."),
           ("Technical constraint", "A fixed technical choice: “must run in the EU region”."),
           ("Organisational constraint", "Team size, skills, budget, process."),
           ("Assumption", "Something believed true but not yet checked."),
           ("Validated assumption", "Checked and confirmed: now a fact."),
           ("RAID log", "Risks, Assumptions, Issues, Dependencies: a common project log.")],
    code=dict(file="docs/architecture/04-constraints-assumptions.md", note="log, as of 2025-11-24", plain=True, src="""
# Constraints
| ID  | Constraint                                  | Source               | Could change it   |
|-----|---------------------------------------------|----------------------|-------------------|
| C-1 | Rotterdam opens 27 April 2026               | store lease signed   | Femke (costly)    |
| C-2 | StockPilot is the WMS until June 2027       | contract             | Marco (penalty)   |
| C-3 | ≤ 4 new engineering hires in 2026           | budget               | Marco, board      |
| C-4 | Customer data stays in the EU               | GDPR, Lena           | nobody            |
| C-5 | Team skills: Python, Postgres, React Native | today's team         | hiring, training  |

# Assumptions
| ID  | We believe…                              | Impact if wrong | Owner | Test                    | By     | Status        |
|-----|------------------------------------------|-----------------|-------|-------------------------|--------|---------------|
| A-1 | StockPilot API can serve six cities      | high            | Ben   | spike: load its API     | 21 Nov | ✗ 10 req/s → ADR 0005 |
| A-2 | Rotterdam orders look like Amsterdam's   | medium          | Priya | compare first 4 weeks   | May    | open          |
| A-3 | Couriers' phones have data all shift     | medium          | Joost | survey + 1-week logs    | 12 Dec | ✓ 97 % of time |
| A-4 | Bancontact works via our current PSP     | high (Antwerp)  | Cho   | ask PSP, test account   | 15 Jan | open          |
"""),
    tools="tools: a table in the repo or wiki; many teams keep it in a RAID log alongside risks, issues and dependencies. arc42 has a “constraints” section; assumptions often sit in the risk register.",
    gains=["<b>Beliefs get checked</b> before the plan depends on them.",
           "<b>False constraints exposed</b>: “we must use X” sometimes turns out to be a preference.",
           "<b>Clear design space</b>: the real limits are written down, with their source.",
           "<b>Earlier bad news</b>: a failed assumption in November beats one in April.",
           "<b>Honest plans</b>: stakeholders see what the plan rests on."],
    losses=["<b>Upkeep</b>: the log needs a weekly look.",
            "<b>Uncomfortable</b>: challenging a “constraint” can step on toes.",
            "<b>Testing costs</b>: spikes and vendor calls take time.",
            "<b>Can't list everything</b>: unknown unknowns remain."],
    baseline="Each line compares <b>a kick-off document that mixes facts and beliefs</b> to <b>separate constraint and assumption logs, with sources, owners, tests and dates, reviewed weekly</b>.",
    ratings=[(2, 4, "Everyone can see what's fixed and what's a guess."),
             (3, 4, "Sponsors confirm constraints and own assumptions."),
             (3, 3, "Testing takes time; avoiding a re-plan saves more."),
             (2, 5, "The plan's weak points are tested before they fail."),
             (2, 4, "Knowing which constraints are soft opens more options."),
             (2, 4, "Each constraint has a source; each assumption a result."),
             (3, 4, "Costly constraints (penalties, leases) are visible."),
             (4, 3, "A log and a weekly look."),
             (3, 3, "Teams know the limits, but tests often need the architect.")],
    pitfalls=[("Assumptions written as facts", "“The API supports six cities.” Nobody asks how we know.", "for every statement ask “given or believed?”"),
              ("Never testing", "The assumptions list is long and every status is “open”.", "owner, test and date for each; test the high-impact ones first."),
              ("Accepting fake constraints", "“We must use microservices” turns out to be one person's preference.", "ask “says who?” and record the source."),
              ("Logging, not acting", "A failed assumption is marked ✗ and the plan carries on.", "every failed assumption becomes a risk, a decision or a re-plan.")],
    use=["The start of any project with dates, vendors, contracts or legal rules.",
         "When the plan depends on a partner or vendor you don't control.",
         "Before committing to a date or a budget.",
         "Whenever someone says “obviously” or “surely”."],
    skip=["Small, internal changes with nothing external.",
          "When an existing RAID log already covers it: use that.",
          "Trivial assumptions with no impact if wrong."],
    related=["<b>Architecturally significant requirements</b> (this volume)", "<b>Spike vs prototype vs PoC</b> (this volume)", "<b>Risk-storming</b> (this volume)", "<b>Risk register</b> (Vol. 6)"],
    quiz=[("What's the difference between a constraint and an assumption?", "A constraint is a given rule you must design within; an assumption is something believed but not yet checked."),
          ("What four things does every assumption need?", "An owner, a way to test it, a date to know it by, and its impact if wrong."),
          ("What do you record for each constraint?", "Its source and who could change it."),
          ("What happens when an assumption fails?", "It becomes a risk, a design decision (an ADR) or a re-plan, never just a ✗ in the log.")],
    try_it="Take your project's plan or kick-off deck and highlight every sentence that's a belief rather than a fact. Pick the one with the highest impact if wrong, and find a way to test it this week: a call, a spike, a query on real data.",
    remember="Plan <span class=\"hl\">around</span> constraints. <span class=\"hl\">Test</span> assumptions before the plan leans on them.",
    sources=["arc42 template, section 2 “Constraints” (arc42.org).",
             "The Open Group, TOGAF Standard, “Architecture principles, constraints and assumptions”.",
             "Gregor Hohpe, <i>The Software Architect Elevator</i> (2020), on challenging constraints.",
             "PMI, <i>PMBOK Guide</i>, assumption logs and RAID."],
)

# ------------------------------------------------------------------ 08 NFR Checklist
nfr_problem = Doodle(760, 270, "Doodle of what Larder forgot at its 2024 launch. Backups were never tested. Logs kept customer addresses for two years. The app couldn't be used with a screen reader. There was no alerting, so when the database disk filled up on a Saturday night, nobody was paged and orders failed for three hours. None of these were hard to do; they were simply never asked.",
                     "Nothing here was hard. It just wasn't on anyone's list.")
for i, (t, s) in enumerate([("backups", "never test-restored"), ("logs", "2 years of addresses"), ("screen reader", "app unusable"), ("alerting", "none at all")]):
    x = 20 + (i % 2) * 260
    y = 20 + (i // 2) * 100
    nfr_problem.box(x, y, 240, 80, "✗ " + t, "pink", sub=s, stroke="red", size=18, subsize=15)
nfr_problem.arrow(540, 120, 590, 120, color="red")
nfr_problem.box(596, 60, 150, 120, "Saturday", "pink", sub="disk full · 3 h down", stroke="red", size=18, subsize=13)
nfr_problem.note(380, 248, "Amsterdam launch, 2024: all “we'll do it later”", "red")

nfr_analogy = Doodle(760, 250, "Doodle of a pilot's pre-flight checklist on a clipboard. Experienced pilots still read it every time: fuel, flaps, instruments, doors. It doesn't teach flying; it stops a skilled crew forgetting something under time pressure.",
                      "Pilots with 10,000 hours still read the checklist. It's not about skill; it's about pressure.")
nfr_analogy.box(30, 20, 220, 210, None, "paper")
nfr_analogy.box(100, 10, 80, 22, None, "blue", rx=4)
for i, t in enumerate(["fuel", "flaps", "instruments", "doors"]):
    nfr_analogy.text(60, 76 + i * 40, "✓ " + t, anchor="start", size=18)
nfr_analogy.raw('<path class="d f-blue" d="M300 120 L540 110 Q580 116 540 130 L300 128 Z"/>'
               '<path class="d f-blue" d="M420 114 L380 40 L410 40 L470 113 Z M420 128 L380 200 L410 200 L470 129 Z M312 120 L296 84 L314 84 L336 119 Z"/>')
nfr_analogy.note(660, 70, "doesn't teach", "pen")
nfr_analogy.note(660, 96, "flying", "pen")
nfr_analogy.note(660, 160, "stops the crew", "green")
nfr_analogy.note(660, 186, "forgetting", "green")
nfr_analogy.note(660, 212, "under pressure", "green")

nfr_how = Doodle(760, 360, "Larder's NFR checklist on one card, in six groups. Run: availability, performance, capacity. Protect: security, privacy, compliance. Change: deployability, testability, modifiability. Operate: observability, backup and recovery, support. People: accessibility, usability, languages. Cost: build, run, and per order. Each item is marked answered, open or not applicable at kick-off.",
                  "Six groups, one question each, marked at kick-off: ✓ answered · ? open · – not relevant.")
groups = [("run", ["availability ✓", "performance ✓", "capacity ?"]), ("protect", ["security ?", "privacy ✓", "compliance ?"]),
          ("change", ["deployability ✓", "testability ?", "modifiability ✓"]), ("operate", ["observability ?", "backup & DR ?", "support ✓"]),
          ("people", ["accessibility ?", "usability ✓", "languages ✓"]), ("cost", ["build ✓", "run ?", "per order ✓"])]
for i, (g, items) in enumerate(groups):
    col, row = i % 3, i // 3
    x, y = 14 + col * 248, 20 + row * 160
    nfr_how.box(x, y, 232, 144, None, ["blue", "pink", "green", "y", "paper", "blue"][i])
    nfr_how.head(x + 116, y + 30, g, size=19)
    for k, it in enumerate(items):
        nfr_how.text(x + 18, y + 64 + k * 26, it, anchor="start", size=16)
nfr_how.note(380, 348, "the “?” items become ASRs, scenarios or tasks with an owner", "pen")

NFR_CHECKLIST = dict(
    slug="nfr-checklist",
    kicker="a.k.a. “the pre-flight checklist”",
    tldr="Non-functional requirements (NFRs) are the <b>qualities</b> nobody asks for until they're missing: backups, logging, accessibility, alerting, privacy, cost. Keep a <b>short checklist</b> of quality questions, grouped (run, protect, change, operate, people, cost), and walk it with stakeholders <b>at every kick-off</b>. Each item gets an answer, an owner, or a reason it doesn't apply. It isn't the requirements; it's how you <b>avoid forgetting</b> them.",
    chips=[("Family", "requirements that shape architecture"), ("Origin", "ISO/IEC 25010 quality model; Atul Gawande, <i>The Checklist Manifesto</i> (2009)"), ("Lives in", "a reusable template; one filled copy per project"), ("Pairs with", "ASRs, quality attribute scenarios, go-live readiness")],
    problem_side="Larder, the 2024 launch",
    problem="""  <p class="lead">When Larder launched in 2024, the team built the shop, orders and delivery, and did it well. What they didn't build was everything nobody had asked for: backups were <b>never test-restored</b>, logs kept customer addresses for <b>two years</b>, the app was <b>unusable with a screen reader</b>, and there was <b>no alerting</b>. One Saturday the database disk filled up and orders failed for <span class="hl-pink">three hours</span> before anyone noticed.</p>
  <ul>
    <li>Product backlogs are full of features; qualities have no natural owner.</li>
    <li>Each gap is cheap to fix early and painful to fix after an incident.</li>
    <li>Experienced teams forget too: under deadline pressure, “we'll do it later” wins.</li>
  </ul>""",
    problem_figs=[nfr_problem],
    analogy_side="the pre-flight checklist",
    analogy="""  <p>A pilot with 10,000 hours still reads the <b>pre-flight checklist</b> before every take-off: fuel, flaps, instruments, doors. The checklist doesn't teach anyone to fly. It's there because skilled people <b>forget simple things under pressure</b>, and in aviation simple things kill. Checklists are short, grouped, and read out loud.</p>""",
    analogy_figs=[nfr_analogy],
    map=[("The checklist on the clipboard", "The NFR checklist template"),
         ("Read before every flight", "Walked at every project kick-off and big change"),
         ("Fuel, flaps, doors", "Availability, privacy, backups, accessibility…"),
         ("“Checked” out loud", "Each item answered, owned or marked not relevant"),
         ("Updating the checklist after an incident", "Adding a question after each postmortem")],
    how_side="short, grouped, walked out loud",
    how="""  <p>Keep it to about <b>20 questions</b> in six groups, each phrased as a question with a default answer (“backups: restored in a test at least monthly?”). At kick-off, walk it with product, operations and security in an hour. <b>Open items</b> become ASRs, quality scenarios or plain tasks with owners.</p>""",
    how_figs=[nfr_how],
    steps=[("Start from a quality model", "ISO 25010 or your own: performance, reliability, security, maintainability, usability, portability…"),
           ("Phrase each as a question", "“Who is paged when checkout fails?” beats “observability”."),
           ("Group and trim to ~20", "Run, protect, change, operate, people, cost. Short enough to finish in an hour."),
           ("Walk it at kick-off", "With product, operations, security, support. Mark ✓ answered, ? open, – not relevant (with why)."),
           ("Turn open items into work", "Significant ones become ASRs and scenarios; the rest become tasks with owners."),
           ("Improve after incidents", "Every postmortem asks: which question would have caught this? Add it.")],
    vocab=[("NFR", "Non-functional requirement: a quality, not a feature."),
           ("Quality model", "A standard list of qualities, such as ISO/IEC 25010."),
           ("Operability", "How easy the system is to run, watch and fix."),
           ("Accessibility", "Usable by people with disabilities (WCAG)."),
           ("RPO / RTO", "How much data you can lose / how long recovery may take."),
           ("Retention", "How long data and logs are kept before deletion.")],
    code=dict(file="templates/nfr-checklist.md", note="Larder's checklist, kick-off copy", plain=True, src="""
# NFR checklist · six-city platform · kick-off 2025-11-10      ✓ answered  ? open  – n/a

RUN
 ✓ Availability   What uptime per month? Planned maintenance windows?    99.9 % · none at peak
 ✓ Performance    p95 for key journeys, normal and peak?                QAS-1 (800 ms at 5×)
 ? Capacity       Peak load in 2 years? Campaign days?                  owner: Eli · 1 Dec
PROTECT
 ? Security       Threat model done? Who reviews auth changes?          owner: Cho
 ✓ Privacy        What personal data, kept how long, where?             EU only · logs 30 days
 ? Compliance     PCI scope? Belgian VAT invoices?                      owner: Lena · Antwerp
CHANGE
 ✓ Deployability  How often, how safely, who can deploy?                daily, canary
 ? Testability    Can each module be tested alone?                      fitness function, Q1
OPERATE
 ? Observability  Who is paged when checkout fails? Dashboards?         owner: Eli
 ? Backup & DR    RPO / RTO? Last test restore?                         never → task, Dec
PEOPLE
 ? Accessibility  WCAG 2.2 AA for the apps?                             owner: Dee
 ✓ Languages      Dutch, English; French for Antwerp?                   NL + EN now, FR in 2027
COST
 ? Run cost       Cloud cost per order, alert on drift?                 owner: Marco + Eli
"""),
    tools="tools: a Markdown template in a shared repo works best. ISO/IEC 25010 and the arc42 quality tree are good starting lists; the AWS, Azure and Google Cloud Well-Architected frameworks have long question sets to borrow from.",
    gains=["<b>Fewer forgotten basics</b>: backups, alerting, retention, accessibility.",
           "<b>Shared ownership</b>: each quality gets a named owner at kick-off.",
           "<b>Cheap</b>: an hour per project, reused every time.",
           "<b>Learns</b>: every incident can add a question.",
           "<b>Feeds the design</b>: open items become ASRs and scenarios."],
    losses=["<b>Can become box-ticking</b>: “✓” without a real answer.",
            "<b>Bloat</b>: lists grow to 200 items and nobody finishes them.",
            "<b>Not a design</b>: it finds questions; someone still has to answer them.",
            "<b>One size doesn't fit all</b>: needs trimming per project."],
    baseline="Each line compares <b>relying on the team to remember qualities</b> to <b>a short, grouped NFR checklist walked at every kick-off, with owners for open items</b>.",
    ratings=[(3, 4, "One page shows which qualities are covered and which are open."),
             (2, 4, "Ops, security and support review the list with product."),
             (3, 4, "An hour at kick-off settles many small questions at once."),
             (2, 4, "Forgotten basics surface before launch, not after an incident."),
             (3, 3, "Neutral on the design's flexibility."),
             (2, 4, "Each quality has an answer or an owner on record."),
             (2, 4, "Run cost is on the list from day one."),
             (4, 4, "Reused template; about an hour per project."),
             (3, 4, "Teams can run the checklist themselves, without the architect.")],
    pitfalls=[("A 200-item checklist", "Nobody finishes it, so it's skipped.", "about 20 questions; link to longer lists for specialists."),
              ("Ticking without answering", "“Backups ✓” but nobody has ever restored one.", "each ✓ needs a short answer or evidence."),
              ("Only engineers walk it", "Privacy and accessibility get guessed.", "walk it with operations, security, legal and support."),
              ("A static list", "The same incident happens twice.", "after every postmortem, add the question that would have caught it.")],
    use=["Every project kick-off and every major change of scope.",
         "Before go-live, as a final check (with the go-live readiness list).",
         "When onboarding a new team to architecture work.",
         "After incidents, to improve the list itself."],
    skip=["Prototypes that won't see real users or data.",
          "As a replacement for real scenarios: it finds questions, it doesn't answer them.",
          "Tiny changes inside a system that already passed it."],
    related=["<b>Quality attribute scenarios</b> (this volume)", "<b>Architecturally significant requirements</b> (this volume)", "<b>Go-live readiness</b> (Vol. 6)", "<b>Backups &amp; disaster recovery</b> (patterns, Vol. 6)"],
    quiz=[("What is an NFR checklist for?", "To make sure quality questions are asked and owned at kick-off, so nothing important is forgotten."),
          ("Why phrase items as questions?", "A question (“who is paged when checkout fails?”) forces a real answer; a word (“observability”) invites a tick."),
          ("How long should the checklist be?", "About 20 questions in a few groups, short enough to finish in an hour."),
          ("How does the checklist improve over time?", "After every incident, add the question that would have caught it.")],
    try_it="Take the six groups above and write one question per group for your current system. Answer them honestly with ✓, ? or –. For every “?”, write a name next to it. Which one would hurt most if it happened this weekend?",
    remember="It's not about skill. It's about <span class=\"hl\">pressure</span>. Read the <span class=\"hl\">checklist</span> every time.",
    sources=["ISO/IEC 25010:2023, Systems and software quality models.",
             "Atul Gawande, <i>The Checklist Manifesto</i> (2009).",
             "AWS Well-Architected Framework, the six pillars (docs.aws.amazon.com).",
             "arc42 quality model (quality.arc42.org)."],
)

NOTES = [ASR, QA_SCENARIOS, CONSTRAINTS, NFR_CHECKLIST]
