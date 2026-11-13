# Series 2 · The Solution Architect's Notebook · Vol. 5 · Availability.
# Running case study: Larder (facts in docs/larder-casebook.md).

# ------------------------------------------------------------------ 05 Availability Maths
am_problem = Doodle(760, 280, "Doodle of 29 November 2027. Korenwolf's renewal draft asks for 99.95 percent availability for business ordering. Mo wants to sign; Femke asks Ana whether Larder can promise it. Nobody knows what Larder's ordering path actually achieves, or what 99.95 means in minutes.",
                    "Korenwolf's renewal asks for 99.95 %. Can Larder sign? Nobody knows what it achieves today, or what that means in minutes.")
am_problem.box(20, 40, 320, 100, "renewal draft", "paper", sub="“99.95 % availability”")
am_problem.box(400, 40, 340, 100, "Mo: “let's sign”", "y", sub="Femke: “can we?”")
am_problem.note(380, 200, "a promise nobody has done the maths on", "red", size=19)

am_analogy = Doodle(760, 250, "Doodle of a string of old Christmas lights wired in series: if any one bulb fails, the whole string goes dark, so more bulbs means a darker December. A string wired in parallel keeps shining when one bulb fails.",
                     "Old Christmas lights in series: one bulb fails, the whole string goes dark. In parallel, the rest keep shining.")
am_analogy.icon("lamp", 30, 60, 1.3)
am_analogy.box(150, 50, 280, 100, "in series", "pink", sub="one fails, all go dark")
am_analogy.box(460, 50, 280, 100, "in parallel", "green", sub="one fails, the rest shine")
am_analogy.note(450, 210, "more bulbs in series, darker December", "pen")

am_how = Doodle(760, 400, "Ana's maths for business ordering, 29 November 2027. In series, availabilities multiply: CDN 99.99, portal backend 99.95, Larder Core 99.9, database 99.95, billing service 99.9: about 99.69 percent, two hours sixteen minutes a month. Taking billing off the ordering path (orders accepted, invoices queued) gives about 99.79. Measured over twelve months: 99.81. In minutes a month: 99.95 is 22 minutes, 99.9 is 43, 99.8 is 1 hour 28. Offer: 99.8 per month for ordering, measured, with service credits; 99.9 as a joint goal for 2028.",
                 "In series, availabilities multiply. Take billing off the path, measure, and promise what the numbers support.")
for i, (t, v) in enumerate([("CDN", "99.99"), ("portal BFF", "99.95"), ("Core", "99.9"), ("database", "99.95"), ("billing", "99.9")]):
    am_how.box(14 + i * 148, 16, 136, 74, t, "pink" if t == "billing" else "paper", sub=v, size=15)
    if i:
        am_how.text(10 + i * 148, 58, "×", "t-head", size=18)
am_how.box(14, 110, 732, 50, "= 99.69 % · 2 h 16 min down a month", "pink", size=16)
am_how.box(14, 176, 732, 50, "billing off the path (queued) → 99.79 % · measured 99.81 %", "y", size=15)
am_how.head(20, 262, "99.95 % = 22 min", anchor="start", size=15)
am_how.head(280, 262, "99.9 % = 43 min", anchor="start", size=15)
am_how.head(520, 262, "99.8 % = 1 h 28", anchor="start", size=15)
am_how.box(14, 286, 732, 50, "offer: 99.8 % for ordering, measured, with credits", "green", size=16)
am_how.note(380, 374, "99.9 % as a joint goal for 2028", "pen", size=16)

AVAILABILITY = dict(
    slug="availability-maths",
    kicker="a.k.a. “Christmas lights in series”",
    tldr="When a request needs several parts <b>in series</b>, their availabilities <b>multiply</b>: five parts at 99.9 % give about 99.5 %. Parts <b>in parallel</b> (a spare that takes over) combine the other way: two at 99.9 % give about 99.9999 %, if the switch-over is automatic. Turn every target into <b>minutes a month</b>, compare with what you <b>measure</b>, and take parts off the critical path before promising more nines.",
    chips=[("Family", "availability"), ("Origin", "reliability engineering; SRE practice"), ("Lives in", "the availability sheet and every SLA you sign"), ("Pairs with", "failure mode analysis, DR tiers, SLOs and error budgets")],
    problem_side="Larder, 29 November 2027",
    problem="""  <p class="lead">Korenwolf's renewal draft asks for <b>99.95 % availability</b> for business ordering. Mo wants to sign; Femke asks Ana whether Larder can promise it. <span class="hl-pink">Nobody knows what the ordering path achieves today</span>, nor that 99.95 % allows only <b>22 minutes</b> of downtime a month.</p>
  <ul>
    <li>Nines sound similar; the minutes are very different.</li>
    <li>Every part a request touches lowers the total.</li>
    <li>Promises made without maths become penalties.</li>
  </ul>""",
    problem_figs=[am_problem],
    analogy_side="Christmas lights in series",
    analogy="""  <p>Old <b>Christmas lights</b> were wired in <b>series</b>: one bulb fails, the whole string goes dark, so the longer the string, the darker December. Newer strings are wired in <b>parallel</b>: one bulb fails and the rest keep shining. Same bulbs, very different evenings.</p>""",
    analogy_figs=[am_analogy],
    map=[("Bulbs in series", "CDN, portal backend, Core, database, billing: all needed"),
         ("A longer string, darker", "Five parts at 99.9–99.99 % give 99.69 %"),
         ("Wired in parallel", "Two payment providers with automatic switch-over"),
         ("Taking a bulb off the string", "Billing off the ordering path, invoices queued"),
         ("A dark evening", "Two hours sixteen minutes down a month")],
    how_side="multiply, convert to minutes, measure",
    how="""  <p>Ana multiplied the business ordering chain: CDN <b>99.99</b>, portal backend <b>99.95</b>, Core <b>99.9</b>, database <b>99.95</b>, billing <b>99.9</b>: about <b>99.69 %</b>, over two hours a month. Taking <b>billing off the path</b> (orders accepted, invoices queued) lifts it to <b>99.79 %</b>; twelve months of measurements say <b>99.81 %</b>. Mo and Ana offered Ruben <b>99.8 % a month</b> for ordering, measured, with service credits, and <b>99.9 %</b> as a joint goal for 2028. Ruben accepted.</p>""",
    how_figs=[am_how],
    steps=[("Draw the request's path", "Every part a request must pass through."),
           ("Multiply in series", "A × B × C …; the weakest part dominates."),
           ("Combine spares in parallel", "1 − (1 − A)²; only if switch-over is automatic."),
           ("Convert to minutes", "Per month: 99.9 % = 43 min; 99.95 % = 22 min."),
           ("Compare with measurements", "Twelve months of real data, per path."),
           ("Shorten the path, then promise", "Remove parts from the critical path before adding nines.")],
    vocab=[("Availability", "The share of time a service works as expected."),
           ("Nines", "Shorthand: three nines = 99.9 %."),
           ("In series", "All parts are needed; availabilities multiply."),
           ("In parallel", "Any one part is enough; failures must coincide."),
           ("SLA", "A promise in a contract, usually with penalties or credits."),
           ("Critical path", "The parts a request can't succeed without.")],
    code=dict(file="docs/availability/business-ordering.md", note="the maths behind the Korenwolf offer, 29 November 2027", plain=True, src="""
# Availability: business ordering (portal + Business API)          Ana · 29 Nov 2027

Path today (series):  CDN 99.99 × portal BFF 99.95 × Core 99.9 × Postgres 99.95 × billing 99.9
                      = 99.69 %   ≈ 2 h 16 min down per month
Billing off the path (orders accepted, invoice lines queued, ADR 0025):
                      = 99.79 %   ≈ 1 h 32 min
Measured, Dec 2026 – Nov 2027 (synthetic order every minute):   99.81 %

Minutes per month:   99.95 % = 22 · 99.9 % = 43 · 99.8 % = 1 h 28 · 99.5 % = 3 h 39
Payments, for comparison: PSP A 99.9 ∥ PSP B 99.9 → 99.9999 % only if switch-over is
automatic; today it's manual (≈ 15 min) → see failure mode analysis.

Offer to Korenwolf: 99.8 %/month for ordering, measured as above, service credits;
99.9 % as a joint goal for 2028.
"""),
    tools="tools: a spreadsheet; synthetic checks (a test order every minute) for measured availability; the SLO dashboards.",
    gains=["<b>Honest promises</b> backed by numbers.",
           "<b>Minutes, not nines</b>: everyone understands.",
           "<b>Shows where to invest</b>: the weakest link.",
           "<b>Shorter paths</b> beat more spares.",
           "<b>Better contracts</b>: measured, with credits."],
    losses=["<b>Component figures are estimates</b>.",
            "<b>Ignores correlated failures</b> (one zone down).",
            "<b>Partial outages</b> are hard to count.",
            "<b>Can disappoint</b> salespeople."],
    baseline="Each line compares <b>promising availability by feel</b> to <b>multiplying the path, converting to minutes, checking measurements, and promising what they support</b>.",
    ratings=[(2, 5, "One line of maths everyone can follow."),
             (2, 4, "Mo, Femke and Ruben agree on 99.8 % with a 2028 goal."),
             (3, 4, "An afternoon instead of a debate."),
             (1, 5, "No penalty clause Larder can't meet."),
             (3, 4, "Recalculate when the path changes."),
             (2, 4, "The sheet sits next to the contract."),
             (2, 4, "Shows where money buys nines."),
             (3, 4, "A spreadsheet and a synthetic check."),
             (3, 3, "Neutral.")],
    pitfalls=[("Nines without minutes", "“Only 0.05 % more.”", "always convert to minutes a month."),
              ("Parallel without automation", "A manual switch counted as parallel.", "count switch-over time as downtime."),
              ("Vendor figures only", "The SLA page, not reality.", "measure the path yourself."),
              ("More spares first", "A second region before shortening the path.", "remove parts from the path first.")],
    use=["Before signing an SLA.",
         "Comparing designs for a critical path.",
         "When leaders ask for “more nines”.",
         "Deciding where to add redundancy."],
    skip=["Internal tools where a few hours down costs little."],
    related=["<b>Failure mode analysis</b> (this volume)", "<b>When to go multi-region</b> (this volume)", "<b>SLOs &amp; error budgets</b> (patterns, Vol. 6)", "<b>Explaining trade-offs to non-engineers</b> (vol. 3)"],
    quiz=[("How do availabilities combine in series?", "They multiply, so the total is lower than any one part."),
          ("How many minutes a month is 99.9 %?", "About 43."),
          ("What lifted business ordering from 99.69 % to 99.79 %?", "Taking billing off the ordering path, queueing invoice lines."),
          ("When does a spare in parallel really help?", "When switch-over is automatic and quick.")],
    try_it="Draw the path of your most important request. Write each part's availability (measured if you can), multiply them, and convert to minutes a month. Then find one part you could take off the path.",
    remember="Fewer <span class=\"hl\">bulbs in series</span> before more <span class=\"hl\">nines</span>.",
    sources=["Betsy Beyer et al., <i>Site Reliability Engineering</i> (2016), “Embracing Risk”.",
             "Ben Treynor Sloss et al., “The Calculus of Service Availability”, ACM Queue (2017).",
             "Michael Nygard, <i>Release It!</i>, 2nd ed. (2018).",
             "Alex Hidalgo, <i>Implementing Service Level Objectives</i> (2020)."],
)

# ------------------------------------------------------------------ 06 Failure Mode Analysis
fm_problem = Doodle(760, 280, "Doodle of the December 2027 risk talk: everyone remembers last year's database failover, so all the worry goes there. But the failover now takes under two minutes. The parts nobody thinks about, a payment provider that slows down without failing, or push notifications arriving late, have never been looked at.",
                    "All the worry goes to last year's failover, now fixed. The quiet failures nobody has looked at.")
fm_problem.box(20, 40, 340, 90, "database failover", "y", sub="everyone's worry · now < 2 min")
fm_problem.box(400, 40, 340, 90, "PSP slow, not down", "pink", sub="nobody's looked", stroke="red")
fm_problem.note(380, 200, "we fear what happened last time", "red", size=20)

fm_analogy = Doodle(760, 250, "Doodle of a pilot's pre-flight checklist built from how planes actually fail: for each part, what can go wrong, what happens then, how likely, how you'd notice. The worst combinations get a drill.",
                     "A pilot's checklist comes from how planes fail: each part, what goes wrong, what happens, how you'd notice.")
fm_analogy.icon("check", 40, 60, 1.3)
for i, (t, f) in enumerate([("what fails", "paper"), ("what then", "y"), ("how likely", "blue"), ("noticed?", "green")]):
    fm_analogy.box(140 + i * 152, 60, 140, 70, t, f, size=16)
fm_analogy.note(450, 200, "the worst combinations get a drill", "pen")

fm_how = Doodle(760, 400, "Larder's failure mode analysis of the checkout path, 6 December 2027. Each failure mode scored for severity, likelihood and how hard it is to detect, from 1 to 10, multiplied. Payment provider slow, not down: 9 by 4 by 6, 216, the top. Push notifications delayed: 5 by 4 by 7, 140. Store Wi-Fi down: 6 by 5 by 3, 90. Database failover: 8 by 3 by 2, 48. Kafka broker lost: 4 by 3 by 2, 24. Actions for the top: a 3-second timeout, a circuit breaker and automatic switch to the second provider; an alert on provider latency. On 17 December, provider A slowed for 22 minutes; the breaker switched in 40 seconds.",
                 "Severity × likelihood × detection. The top risk was a provider that slows, not one that fails.")
fm_how.head(20, 30, "failure mode", anchor="start", size=15)
fm_how.head(420, 30, "S × L × D", anchor="start", size=15)
fm_how.head(640, 30, "score", anchor="start", size=15)
for i, (m, sld, sc, f) in enumerate([("PSP slow, not down", "9 × 4 × 6", "216", "pink"), ("push delayed", "5 × 4 × 7", "140", "y"),
                                     ("store Wi-Fi down", "6 × 5 × 3", "90", "paper"), ("database failover", "8 × 3 × 2", "48", "paper"), ("Kafka broker lost", "4 × 3 × 2", "24", "green")]):
    y = 44 + i * 46
    fm_how.box(12, y, 736, 38, None, f, rx=4)
    fm_how.text(20, y + 25, m, "t-head", anchor="start", size=14)
    fm_how.text(420, y + 25, sld, anchor="start", size=14)
    fm_how.text(640, y + 25, sc, "t-head", anchor="start", size=15)
fm_how.box(12, 284, 736, 46, "3 s timeout · circuit breaker · automatic switch to PSP B", "blue", size=15)
fm_how.note(380, 366, "17 Dec: PSP A slow for 22 min; switched in 40 s", "green", size=16)

FMEA = dict(
    slug="failure-mode-analysis",
    kicker="a.k.a. “the pilot's checklist”",
    tldr="<b>Failure mode analysis</b> (FMEA) lists, for each part of a design, <b>how it can fail</b> (not just “down”: slow, wrong, partial, late), <b>what happens</b> then, and scores <b>severity</b>, <b>likelihood</b> and <b>how hard it is to detect</b>. Multiplying the three ranks the risks; you fix the top ones first. It moves attention from the failure everyone remembers to the quiet ones nobody has looked at.",
    chips=[("Family", "availability"), ("Origin", "FMEA, US military (1949), then aerospace and automotive"), ("Lives in", "a table per critical path, reviewed before peaks"), ("Pairs with", "availability maths, risk-storming, circuit breaker")],
    problem_side="Larder, 6 December 2027",
    problem="""  <p class="lead">With Christmas three weeks away, the risk talk goes straight to last year's <b>database failover</b>, which now takes under two minutes. <span class="hl-pink">Nobody looks at the quiet failures</span>: a payment provider that <b>slows down</b> without failing, push notifications arriving <b>late</b>, a store's Wi-Fi at peak. Teams fear what happened last time, not what might happen next.</p>
  <ul>
    <li>“Down” is only one way to fail; slow and wrong are worse.</li>
    <li>Recent incidents get all the attention.</li>
    <li>Failures that are hard to detect last longest.</li>
  </ul>""",
    problem_figs=[fm_problem],
    analogy_side="the pilot's checklist",
    analogy="""  <p>A pilot's <b>checklist</b> comes from how planes actually fail: for each part, <b>what can go wrong</b>, <b>what happens then</b>, <b>how likely</b> it is, and <b>how you'd notice</b>. The worst combinations (severe, likely, hard to notice) get a drill in the simulator, whether or not they happened last month.</p>""",
    analogy_figs=[fm_analogy],
    map=[("Each part of the plane", "Each part of the checkout path"),
         ("What can go wrong", "Slow, down, late, wrong, partial"),
         ("How you'd notice", "The detection score"),
         ("The worst combinations", "The highest severity × likelihood × detection"),
         ("A drill in the simulator", "A circuit breaker, switch-over and an alert, tested")],
    how_side="severity × likelihood × detection",
    how="""  <p>Ana, Cho and Eli walked the checkout path part by part, scoring each failure mode 1–10 for severity, likelihood and detection. Top: the <b>payment provider slowing down</b> (216): threads wait, checkout stalls, no alarm fires. Then <b>delayed pushes</b> (140) and <b>store Wi-Fi</b> (90); the famous failover came fourth (48). Cho added a <b>3-second timeout</b>, a <b>circuit breaker</b> and <b>automatic switch-over</b> to the second provider, plus a latency alert. On <b>17 December</b> provider A slowed for 22 minutes; the breaker switched in <b>40 seconds</b>.</p>""",
    how_figs=[fm_how],
    steps=[("Pick a critical path", "Checkout, picking, dispatch: one at a time."),
           ("List each part's failure modes", "Down, slow, wrong, late, partial, duplicated."),
           ("Write the effect", "What the customer, picker or courier sees."),
           ("Score S, L and D", "1–10 each; multiply into a priority number."),
           ("Act on the top few", "Reduce severity, likelihood, or improve detection."),
           ("Re-score after fixes", "And before each peak season.")],
    vocab=[("Failure mode", "One specific way a part can fail."),
           ("Effect", "What happens downstream when it does."),
           ("Severity", "How bad the effect is."),
           ("Detection", "How hard the failure is to notice (10 = invisible)."),
           ("RPN", "Risk priority number: severity × likelihood × detection."),
           ("Grey failure", "A part that's partly broken: slow or flaky, not down.")],
    code=dict(file="docs/availability/fmea-checkout.md", note="the checkout FMEA, 6 December 2027", plain=True, src="""
# FMEA · checkout path · 6 Dec 2027 · Ana, Cho, Eli · scores 1–10, RPN = S × L × D

| Part        | Failure mode        | Effect                                  | S | L | D | RPN | Action (owner)                         |
|-------------|---------------------|-----------------------------------------|---|---|---|-----|----------------------------------------|
| PSP A       | slow (> 5 s)        | checkout stalls, workers tied up, no alarm | 9 | 4 | 6 | 216 | 3 s timeout, breaker, auto-switch to B (Cho) |
| Push provider | delayed (> 2 min) | swap answers missed, defaults applied   | 5 | 4 | 7 | 140 | delivery-lag alert; in-app banner (Dee) |
| Store Wi-Fi | down at peak        | picker offline mode, sync later         | 6 | 5 | 3 | 90  | 4G backup check weekly (Eli)            |
| Postgres    | failover            | checkout errors < 2 min                 | 8 | 3 | 2 | 48  | none (ADR 0017)                         |
| Kafka       | one broker lost     | none (3 brokers)                        | 4 | 3 | 2 | 24  | none                                   |

17 Dec 2027: PSP A p95 9 s for 22 min → breaker opened, switched to B in 40 s, 0 failed orders.
"""),
    tools="tools: a spreadsheet or table in the docs; incident history; chaos or fault-injection tests to check the effects; the circuit breaker and timeout patterns.",
    gains=["<b>Quiet failures found</b>: slow, late, wrong.",
           "<b>Attention by risk</b>, not memory.",
           "<b>Detection improved</b>, not just prevention.",
           "<b>A ranked list</b> for limited time.",
           "<b>Proved on 17 December</b>."],
    losses=["<b>Scores are subjective</b>.",
            "<b>Time-consuming</b> for long paths.",
            "<b>Misses combinations</b> of failures.",
            "<b>Goes stale</b> as the design changes."],
    baseline="Each line compares <b>worrying about the last incident</b> to <b>scoring each part's failure modes by severity, likelihood and detection, and fixing the top first</b>.",
    ratings=[(2, 4, "One table per path."),
             (3, 4, "Cho, Eli and Dee agree what comes first."),
             (3, 4, "The ranking ends the debate."),
             (1, 5, "The top risk fixed before it struck."),
             (3, 4, "Re-scored before each peak."),
             (2, 4, "Actions and owners in the table."),
             (3, 3, "Neutral."),
             (3, 3, "Half a day per path."),
             (3, 4, "Teams score their own parts.")],
    pitfalls=[("Only “down”", "Every row says “service unavailable”.", "slow, late, wrong, partial too."),
              ("Recency bias", "Last incident ranked first by default.", "score every mode the same way."),
              ("No detection score", "Silent failures rank low.", "make invisible failures score high."),
              ("Write and forget", "A table from two years ago.", "re-score before peaks and after changes.")],
    use=["Critical paths before peaks or launches.",
         "After an incident, to look beyond it.",
         "New designs with external dependencies.",
         "Deciding where to add timeouts and fallbacks."],
    skip=["Non-critical internal tools."],
    related=["<b>Availability maths</b> (this volume)", "<b>Risk-storming</b> (vol. 1)", "<b>Circuit breaker</b> (patterns, Vol. 1)", "<b>Retry with backoff</b> (patterns, Vol. 1)"],
    quiz=[("What are the three scores in FMEA?", "Severity, likelihood and detection (how hard it is to notice)."),
          ("What was Larder's top failure mode?", "The payment provider slowing down without failing."),
          ("Why score detection?", "Failures nobody notices last longest and do most harm."),
          ("What happened on 17 December?", "Provider A slowed for 22 minutes; the breaker switched to B in 40 seconds.")],
    try_it="Take your most important path. For each part, write three failure modes (down, slow, wrong), their effect, and S, L, D scores. Fix the top one, and add an alert if its detection score is above 5.",
    remember="Fly by the <span class=\"hl\">checklist</span>, not by last month's <span class=\"hl\">scare</span>.",
    sources=["IEC 60812, <i>Failure modes and effects analysis (FMEA and FMECA)</i> (2018).",
             "D. H. Stamatis, <i>Failure Mode and Effect Analysis</i>, 2nd ed. (2003).",
             "Peng Huang et al., “Gray Failure: The Achilles' Heel of Cloud-Scale Systems” (HotOS 2017).",
             "Michael Nygard, <i>Release It!</i>, 2nd ed. (2018), stability patterns."],
)

# ------------------------------------------------------------------ 07 DR Tiers
dr_problem = Doodle(760, 280, "Doodle of January 2028. Every system's runbook says recovery in one hour. On 10 January Eli runs the first full restore drill: rebuilding the main database from backup takes 3 hours 40 minutes. Meanwhile the CRM, which could wait a day, has the same expensive setup as checkout.",
                    "Every runbook says “one hour”. The first real restore drill took 3 h 40. And the CRM is protected like checkout.")
dr_problem.box(20, 40, 300, 90, "runbooks", "paper", sub="“recovery: 1 hour”")
dr_problem.arrow(326, 85, 430, 85, label="drill", lx=378, ly=72)
dr_problem.box(436, 40, 304, 90, "3 h 40 min", "pink", sub="main database restore", stroke="red")
dr_problem.note(380, 200, "same promise for everything, kept by nothing", "red", size=19)

dr_analogy = Doodle(760, 250, "Doodle of a hospital's emergency power: operating theatres and intensive care switch to generators in seconds; the wards within minutes; the offices and the café wait until the mains come back. And the generators are tested monthly, under load.",
                     "A hospital's emergency power: theatres in seconds, wards in minutes, the café waits. Generators tested monthly.")
dr_analogy.icon("plug", 30, 60, 1.3)
for i, (t, s, f) in enumerate([("theatres", "seconds", "pink"), ("wards", "minutes", "y"), ("café", "when mains return", "paper")]):
    dr_analogy.box(150 + i * 200, 50, 186, 90, t, f, sub=s, size=16)
dr_analogy.note(450, 205, "tested monthly, under load", "pen")

dr_how = Doodle(760, 400, "Larder's disaster recovery tiers from 10 January 2028. Tier 1, checkout, orders, payments and Dispatch: recovery time 15 minutes, data loss at most 1 minute; a standby database in another zone, point-in-time recovery. Tier 2, picker app, stock, business portal: 1 hour and 15 minutes. Tier 3, reporting, CRM, analytics: 1 day and 24 hours, nightly backups. Tier 4, internal tools: rebuild from code. Backups copied to a second region. Restore drills every quarter; the next drill restored the main database to a fresh standby in 22 minutes.",
                 "Four tiers, each with RTO and RPO, and quarterly drills that prove them.")
dr_how.head(20, 30, "tier", anchor="start", size=15)
dr_how.head(330, 30, "RTO", anchor="start", size=15)
dr_how.head(450, 30, "RPO", anchor="start", size=15)
dr_how.head(570, 30, "how", anchor="start", size=15)
for i, (t, rto, rpo, how, f) in enumerate([("1 checkout, orders, pay", "15 min", "≤ 1 min", "standby + PITR", "pink"), ("2 picker, stock, portal", "1 h", "15 min", "replicas", "y"),
                                           ("3 reporting, CRM", "1 day", "24 h", "nightly backup", "blue"), ("4 internal tools", "rebuild", "—", "from code", "green")]):
    y = 44 + i * 50
    dr_how.box(12, y, 736, 42, None, f, rx=4)
    dr_how.text(20, y + 27, t, "t-head", anchor="start", size=14)
    dr_how.text(330, y + 27, rto, anchor="start", size=14)
    dr_how.text(450, y + 27, rpo, anchor="start", size=14)
    dr_how.text(570, y + 27, how, anchor="start", size=13)
dr_how.box(12, 260, 736, 46, "backups copied to a second region · drills every quarter", "paper", size=15)
dr_how.note(380, 344, "April drill: main database restored in 22 minutes", "green", size=16)

DR = dict(
    slug="dr-tiers",
    kicker="a.k.a. “the hospital's emergency power”",
    tldr="<b>Disaster recovery tiers</b> sort systems by how fast they must come back (<b>RTO</b>, recovery time objective) and how much data they may lose (<b>RPO</b>, recovery point objective). Each tier gets matching protection and cost: standby databases for the top, nightly backups for the bottom. Then you <b>prove</b> each tier with <b>restore drills</b>, because a recovery time nobody has tested is a guess.",
    chips=[("Family", "availability"), ("Origin", "business continuity planning; ISO 22301"), ("Lives in", "the DR page, every runbook and the drill calendar"), ("Pairs with", "availability maths, backups &amp; disaster recovery, when to go multi-region")],
    problem_side="Larder, 10 January 2028",
    problem="""  <p class="lead">Every runbook says <b>“recovery: one hour”</b>. On 10 January Eli runs Larder's first full <b>restore drill</b>: rebuilding the main database from backup takes <b>3 hours 40 minutes</b>. Meanwhile the CRM, which could easily wait a day, is protected as expensively as checkout. <span class="hl-pink">The same promise for everything, kept by nothing.</span></p>
  <ul>
    <li>Recovery times nobody has tested are wishes.</li>
    <li>Equal protection overspends on some systems and underspends on others.</li>
    <li>In a real disaster, people need to know what comes back first.</li>
  </ul>""",
    problem_figs=[dr_problem],
    analogy_side="the hospital's emergency power",
    analogy="""  <p>When the mains fail, a hospital's <b>operating theatres</b> switch to generators in seconds, the <b>wards</b> within minutes, and the <b>café</b> waits until the mains come back. Nobody pays for instant power in the café. And the generators are <b>tested every month, under load</b>, because an untested generator is a hope.</p>""",
    analogy_figs=[dr_analogy],
    map=[("Operating theatres", "Tier 1: checkout, orders, payments, Dispatch"),
         ("Wards", "Tier 2: picker app, stock, business portal"),
         ("The café", "Tier 3: reporting, CRM, analytics"),
         ("Seconds, minutes, later", "RTO 15 min, 1 h, 1 day"),
         ("Monthly generator test", "Quarterly restore drills")],
    how_side="tiers with RTO and RPO, proved by drills",
    how="""  <p>Ana and Eli sorted every system with Joost and Sam: <b>Tier 1</b> (checkout, orders, payments, Dispatch) RTO <b>15 min</b>, RPO <b>≤ 1 min</b>, with a standby database in another zone and point-in-time recovery; <b>Tier 2</b> (picker app, stock, business portal) <b>1 h</b> / 15 min; <b>Tier 3</b> (reporting, CRM, analytics) <b>1 day</b> / 24 h; <b>Tier 4</b> rebuilt from code. Backups are copied to a second region. The April drill restored the main database to a fresh standby in <b>22 minutes</b>.</p>""",
    how_figs=[dr_how],
    steps=[("List every system", "From the application portfolio."),
           ("Ask the business", "How long can it be down? How much data can we lose?"),
           ("Group into tiers", "Three or four, each with RTO and RPO."),
           ("Match protection to tier", "Standby, replicas, backups, rebuild."),
           ("Drill each tier", "Restore for real, timed, on a calendar."),
           ("Fix what the drill finds", "And write the real time in the runbook.")],
    vocab=[("RTO", "Recovery time objective: how long until it works again."),
           ("RPO", "Recovery point objective: how much data may be lost."),
           ("Standby", "A copy ready to take over."),
           ("Point-in-time recovery", "Restoring a database to any moment, from logs."),
           ("Restore drill", "Actually restoring a system, timed."),
           ("Business continuity", "Keeping the business running during a disaster.")],
    code=dict(file="docs/availability/dr-tiers.md", note="the DR tiers page, January 2028", plain=True, src="""
# Disaster recovery tiers                     agreed 10 Jan 2028 · Ana, Eli, Joost, Sam, Marco

| Tier | Systems                                   | RTO     | RPO     | Protection                              |
|------|-------------------------------------------|---------|---------|-----------------------------------------|
| 1    | checkout, Ordering, Payments, Dispatch     | 15 min  | ≤ 1 min | standby in 2nd zone, PITR, auto failover |
| 2    | picker app, Stock (+ WMS B), business portal | 1 h   | 15 min  | replicas, vendor DR (WMS B: 4 h, contract) |
| 3    | reporting, CRM, analytics, helpdesk export | 1 day   | 24 h    | nightly backups                          |
| 4    | internal tools, test environments          | rebuild | —       | infrastructure as code                    |

All backups copied to a second EU region (Paris) daily.
Drills: quarterly, one tier-1 restore each time. 10 Jan: 3 h 40 (full restore) → standby + PITR.
          18 Apr: main database restored to a fresh standby in 22 min.
"""),
    tools="tools: managed database standby and point-in-time recovery, cross-region backup copies, infrastructure as code for rebuilds, a drill calendar and timed runbooks.",
    gains=["<b>Clear order of recovery</b> in a crisis.",
           "<b>Spending matched</b> to importance.",
           "<b>Proved recovery times</b>, not wishes.",
           "<b>Gaps found</b> in drills, not disasters.",
           "<b>Contracts checked</b> (WMS B's own DR)."],
    losses=["<b>Drills take time</b> and some risk.",
            "<b>Tier 1 is expensive</b>.",
            "<b>Tiers drift</b> as systems change.",
            "<b>Business owners</b> must agree the numbers."],
    baseline="Each line compares <b>the same untested “one hour” for every system</b> to <b>tiers with RTO and RPO agreed with the business, matched protection and quarterly drills</b>.",
    ratings=[(2, 5, "Four tiers, two numbers each."),
             (2, 5, "Joost and Sam agreed what comes back first."),
             (3, 4, "In an incident, the order is already decided."),
             (1, 5, "3 h 40 found in a drill, not a disaster."),
             (3, 4, "Systems move between tiers as they matter more."),
             (2, 4, "Drill results recorded in the runbook."),
             (2, 4, "Tier 3 got cheaper; Tier 1 got stronger."),
             (3, 3, "A drill a quarter."),
             (3, 3, "Neutral.")],
    pitfalls=[("Untested numbers", "RTO copied from a template.", "drill and record the real time."),
              ("Everything Tier 1", "Every owner says “critical”.", "ask what an hour down really costs."),
              ("Forgetting vendors", "WMS B's recovery not in the plan.", "check vendors' DR in the contract."),
              ("Backups in the same place", "One region, one account.", "copy them somewhere else.")],
    use=["Any system the business depends on.",
         "Before signing availability promises.",
         "After moving to new infrastructure.",
         "When backups have never been restored."],
    skip=["Throwaway prototypes and test environments (Tier 4: rebuild)."],
    related=["<b>Availability maths</b> (this volume)", "<b>When to go multi-region</b> (this volume)", "<b>Backups &amp; disaster recovery</b> (patterns, Vol. 6)", "<b>Application portfolio</b> (vol. 4)"],
    quiz=[("What do RTO and RPO mean?", "How long until it works again, and how much data may be lost."),
          ("Why tiers instead of one target?", "To match protection and cost to how much each system matters."),
          ("What did the first drill find?", "A full database restore took 3 h 40, not one hour."),
          ("How was it fixed?", "A standby with point-in-time recovery; the April drill took 22 minutes.")],
    try_it="List your five most important systems. Ask their business owners how long each can be down and how much data it can lose, group them into tiers, and book a timed restore drill for the top one this quarter.",
    remember="Power the <span class=\"hl\">theatres</span> first, and test the <span class=\"hl\">generator</span>.",
    sources=["ISO 22301:2019, <i>Business continuity management systems</i>.",
             "AWS Well-Architected Framework, “Disaster recovery options in the cloud” (whitepaper, 2021).",
             "Betsy Beyer et al., <i>Site Reliability Engineering</i> (2016), data integrity.",
             "Google Cloud, “Disaster recovery planning guide”."],
)

# ------------------------------------------------------------------ 08 When to Go Multi-Region
mr_problem = Doodle(760, 280, "Doodle of 24 January 2028. ADR 0017 promised to revisit a second region when Antwerp opened. Femke assumes the answer is yes: Larder is international now, and two regions sound safer. Nobody has put a number on what a region outage would cost, or what a second region would.",
                    "ADR 0017 said “revisit at Antwerp”. Femke assumes yes: two regions sound safer. Nobody has the numbers.")
mr_problem.box(20, 40, 320, 100, "ADR 0017", "paper", sub="“revisit at Antwerp”")
mr_problem.box(400, 40, 340, 100, "Femke", "y", sub="“we're international now”")
mr_problem.note(380, 200, "safer, says the gut; at what cost, says nobody", "red", size=18)

mr_analogy = Doodle(760, 250, "Doodle of a family deciding whether to buy a second car. A second car costs every month, insurance, parking, upkeep, whether it's used or not. They agree: we'll buy one when both of us commute by car, or the first car leaves us stranded twice in a year. Until then, a taxi number on the fridge.",
                     "A second car costs every month. Agree when you'd buy one; until then, a taxi number on the fridge.")
mr_analogy.icon("truck", 30, 60, 1.2)
mr_analogy.box(150, 50, 280, 100, "second car", "pink", sub="costs every month")
mr_analogy.box(460, 50, 280, 100, "taxi number", "green", sub="until the triggers hit")
mr_analogy.note(450, 210, "agree the triggers in advance", "pen")

mr_how = Doodle(760, 400, "Ana's numbers, 24 January 2028. Cost of a second active region: about 9,000 euros a month plus two engineers, about 300,000 euros a year. Expected loss from region outages: one regional incident in two years, 34 minutes at night; a peak hour is worth about 120,000 euros of orders, so expected loss is well under 100,000 euros a year. Belgian rules don't require another region. Decision, ADR 0026: stay in one region across three zones; a pilot light in a second region for tier 1, about 1,200 euros a month, recovery in four hours. Revisit when any trigger fires: 60,000 orders a day, a region outage over an hour, a contract requiring it, or a city outside the EU.",
                 "≈ €300k a year to avoid well under €100k of expected loss. Not yet: a pilot light, and four agreed triggers.")
mr_how.box(14, 14, 360, 110, None, "pink")
mr_how.head(194, 46, "second region", size=16)
mr_how.text(194, 78, "≈ €9k / month + 2 engineers", size=14)
mr_how.text(194, 104, "≈ €300k a year", "t-head", size=15)
mr_how.box(386, 14, 360, 110, None, "y")
mr_how.head(566, 46, "expected loss", size=16)
mr_how.text(566, 78, "1 incident in 2 yrs · 34 min", size=14)
mr_how.text(566, 104, "well under €100k a year", "t-head", size=15)
mr_how.box(14, 144, 732, 56, "ADR 0026: one region, three zones + pilot light (≈ €1.2k/mo, RTO 4 h)", "green", size=14)
for i, t in enumerate(["60k orders / day", "outage > 1 h", "contract needs it", "city outside EU"]):
    mr_how.box(14 + i * 184, 222, 174, 60, t, "blue", size=13)
mr_how.note(380, 318, "revisit when any trigger fires", "pen", size=17)

MULTI = dict(
    slug="multi-region",
    kicker="a.k.a. “the second car”",
    tldr="Running in <b>more than one cloud region</b> protects against a whole region failing, but it is one of the most expensive and complex steps in architecture: double infrastructure, data replication, harder deployments, more people. Decide with numbers: <b>what a region outage would cost</b>, <b>how often</b> it happens, <b>what a second region costs</b>, and any <b>legal need</b>. If the answer is “not yet”, agree the <b>triggers</b> that would change it, and keep a cheaper fallback (backups or a pilot light) meanwhile.",
    chips=[("Family", "availability"), ("Origin", "cloud architecture practice (AWS, Azure, Google well-architected frameworks)"), ("Lives in", "an ADR with triggers, revisited when one fires"), ("Pairs with", "availability maths, DR tiers, total cost of ownership")],
    problem_side="Larder, 24 January 2028",
    problem="""  <p class="lead">ADR 0017 promised to <b>revisit a second region when Antwerp opened</b>. Antwerp has been live for three months; Femke assumes the answer is yes: Larder is international now, and <b>two regions sound safer</b>. <span class="hl-pink">Nobody has put a number</span> on what a region outage would cost, how often one happens, or what a second region would cost every month.</p>
  <ul>
    <li>“Safer” is easy to agree with and expensive to buy.</li>
    <li>Multi-region changes deployments, data and on-call for good.</li>
    <li>A decision without triggers gets re-argued every quarter.</li>
  </ul>""",
    problem_figs=[mr_problem],
    analogy_side="the second car",
    analogy="""  <p>A family wonders whether to buy a <b>second car</b>. It costs every month (insurance, parking, upkeep) whether it's driven or not. They agree: we'll buy one <b>when both of us commute by car</b>, or <b>the first car leaves us stranded twice in a year</b>. Until then, there's a <b>taxi number on the fridge</b>.</p>""",
    analogy_figs=[mr_analogy],
    map=[("The second car", "A second active region"),
         ("Insurance, parking, upkeep", "≈ €9k a month plus two engineers"),
         ("Stranded twice a year", "A region outage longer than an hour"),
         ("Both commuting by car", "60,000 orders a day, or a contract requiring it"),
         ("The taxi number", "A pilot light in a second region: RTO 4 hours")],
    how_side="the cost, the loss, the law, the triggers",
    how="""  <p>Ana put four numbers on a page. A second active region: about <b>€9,000 a month plus two engineers</b>, roughly <b>€300k a year</b>. Region outages: <b>one incident in two years</b>, 34 minutes at night; a peak hour is worth about €120k of orders, so the expected loss is <b>well under €100k a year</b>. Lena confirmed Belgian rules <b>don't require</b> another region. ADR 0026: stay in <b>one region across three zones</b>, add a <b>pilot light</b> for Tier 1 in a second region (≈ €1,200 a month, RTO 4 hours), and revisit when any of <b>four triggers</b> fires.</p>""",
    how_figs=[mr_how],
    steps=[("Price the second region", "Infrastructure, data transfer, people, slower delivery."),
           ("Price the outage", "Revenue per hour at peak, contract penalties, reputation."),
           ("Estimate how often", "Your provider's history in your region."),
           ("Check the law and contracts", "Data residency, client requirements."),
           ("Choose the cheapest fallback that fits", "Backups, pilot light, warm standby, active-active."),
           ("Write the triggers", "Numbers that would reopen the decision.")],
    vocab=[("Region", "A geographic area of a cloud provider, with several zones."),
           ("Availability zone", "A separate data centre within a region."),
           ("Active-active", "Both regions serve traffic all the time."),
           ("Pilot light", "A minimal copy (mostly data) ready to be scaled up."),
           ("Warm standby", "A smaller running copy that can take over."),
           ("Trigger", "A condition agreed in advance that reopens a decision.")],
    code=dict(file="docs/adr/0026-single-region-with-triggers.md", note="ADR 0026, 24 January 2028", plain=True, src="""
# 26. Stay in one region (three zones), pilot light in a second, with triggers
Status: Accepted · 2028-01-24 · Driver: Ana · with Eli, Marco, Lena, Femke · revisits ADR 0017

Second active region   ≈ €9,000/month + 2 engineers ≈ €300k/year; slower deploys; data replication
Expected outage loss   1 regional incident in 2 years (34 min, 03:10, Mar 2027)
                       peak hour ≈ €120k of orders → expected loss well under €100k/year
Law and contracts      EU only (GDPR); Belgium adds no residency rule; Korenwolf: 99.8 %/month

Decision   one region, three zones (as now) + pilot light in Paris for Tier 1:
           database replica + infrastructure as code, ≈ €1,200/month, RTO 4 h, RPO 5 min
Triggers   any one → reopen: 60,000 orders/day · a region outage > 1 h ·
           a client contract requiring regional failover · a city outside the EU
"""),
    tools="tools: the cloud provider's status history, the availability sheet and TCO model, cross-region replication and infrastructure as code for the pilot light.",
    gains=["<b>No €300k a year</b> spent on a feeling.",
           "<b>A cheaper fallback</b> in place now.",
           "<b>Triggers end the re-arguing</b>.",
           "<b>Simpler operations</b> for the team.",
           "<b>Legal question settled</b> with Lena."],
    losses=["<b>A region outage</b> means hours, not minutes.",
            "<b>The pilot light</b> must be drilled too.",
            "<b>Estimates of rare events</b> are shaky.",
            "<b>Femke's instinct</b> overruled by numbers."],
    baseline="Each line compares <b>going multi-region because it sounds safer</b> to <b>pricing the cost, the loss and the law, choosing the cheapest fitting fallback, and agreeing triggers</b>.",
    ratings=[(2, 5, "Four numbers on one page."),
             (2, 4, "Femke, Marco and Lena signed the triggers."),
             (2, 4, "Decided once, revisited only on a trigger."),
             (3, 4, "A pilot light covers the worst case."),
             (2, 5, "Triggers say exactly when to change course."),
             (2, 5, "ADR 0026 revisits ADR 0017 explicitly."),
             (1, 5, "≈ €300k a year not spent."),
             (2, 4, "One region keeps operations simple."),
             (3, 3, "Neutral.")],
    pitfalls=[("Multi-region by default", "“Serious companies do it.”", "price the outage and the cure."),
              ("Active-active or nothing", "No middle option considered.", "backups, pilot light, warm standby."),
              ("No triggers", "Re-argued every quarter.", "write the conditions that reopen it."),
              ("Untested fallback", "A pilot light never lit.", "drill it with the DR tiers.")],
    use=["When leaders ask for “more resilience”.",
         "Expanding into new countries.",
         "Before signing contracts with regional failover clauses.",
         "Revisiting an earlier region decision."],
    skip=["When law or a contract already requires it: then decide how, not whether."],
    related=["<b>DR tiers</b> (this volume)", "<b>Availability maths</b> (this volume)", "<b>Revisiting decisions</b> (vol. 2)", "<b>Total cost of ownership</b> (this volume)"],
    quiz=[("What four things decide multi-region?", "The cost of a second region, the cost and frequency of outages, and legal or contract needs."),
          ("What did Larder choose?", "One region across three zones, a pilot light in a second region, and four triggers."),
          ("What is a pilot light?", "A minimal copy, mostly data, ready to be scaled up in another region."),
          ("Why write triggers?", "So the decision is reopened when the facts change, not every quarter.")],
    try_it="Estimate what one hour of your platform being down at peak would cost, how often your region has had a serious outage, and what a second region would cost a year. Write a one-paragraph decision with at least two triggers.",
    remember="Don't buy the <span class=\"hl\">second car</span> on a feeling; keep a <span class=\"hl\">taxi number</span> on the fridge.",
    sources=["AWS Well-Architected Framework, Reliability Pillar (2023).",
             "Microsoft Azure Architecture Center, “Multi-region deployment”.",
             "Seth Eliot, “Disaster Recovery of Workloads on AWS” (AWS whitepaper, 2021).",
             "Michael Nygard, “Documenting Architecture Decisions” (2011)."],
)

NOTES = [AVAILABILITY, FMEA, DR, MULTI]
