# Series 2 · The Solution Architect's Notebook · Vol. 5 · Size & speed.
# Running case study: Larder (facts in docs/larder-casebook.md).

# ------------------------------------------------------------------ 01 Back-of-the-Envelope Estimation
be_problem = Doodle(760, 280, "Doodle of 4 October 2027. Femke asks the leadership meeting: will Christmas hold, now that Antwerp and Eindhoven open this autumn? Eli says it should be fine, Ben says Kafka worries him, Joost remembers last Christmas's 38-minute outage. Nobody has a number; the debate is all feelings.",
                    "“Will Christmas hold?” Three opinions, one bad memory, and not a single number.")
be_problem.box(20, 30, 220, 90, "Eli", "blue", sub="“should be fine”")
be_problem.box(270, 30, 220, 90, "Ben", "y", sub="“Kafka worries me”")
be_problem.box(520, 30, 220, 90, "Joost", "pink", sub="“last Christmas…”")
be_problem.box(200, 160, 360, 60, "Femke: “will it hold?”", "paper", size=17)
be_problem.note(380, 258, "opinions, no numbers", "red", size=20)

be_analogy = Doodle(760, 250, "Doodle of a family planning a road trip on a napkin: 900 kilometres, about 100 an hour, so nine hours of driving; the car does 600 on a tank, so one stop for fuel; two drivers, so swap at the fuel stop. Rough, quick, and enough to see that fuel isn't the problem but the driving hours are.",
                     "A road trip on a napkin: 900 km at about 100 an hour is nine hours. Rough, and enough to see what matters.")
be_analogy.icon("map", 30, 60, 1.3)
for i, (t, s, f) in enumerate([("900 km ÷ 100", "≈ 9 hours", "y"), ("tank: 600 km", "1 fuel stop", "green"), ("2 drivers", "swap at the stop", "blue")]):
    be_analogy.box(150 + i * 200, 50, 186, 90, t, f, sub=s, size=16)
be_analogy.note(450, 205, "fuel isn't the problem; driving hours are", "pen")

be_how = Doodle(760, 400, "Ana's estimate for Christmas 2027, one page, twenty minutes. Forecast 27,000 orders a day by December. Friday peak is about 0.045 percent of the day's orders each second: about 12 orders a second. Design for five times: 60 orders a second. About 400 API requests per order: 24,000 requests a second, 80 percent browsing that a cache can serve. About 30 database writes per order: 1,800 writes a second, against about 2,400 measured on the current primary. Dispatch: 900 couriers every 5 seconds is 180 messages a second, trivial. Conclusion: the database and checkout matter; Kafka and Dispatch don't.",
                 "Five known numbers, multiplied out. The database is the thing to watch; Kafka and Dispatch aren't.")
rows = [("orders / day (Dec)", "27,000", "forecast", "paper"), ("Friday peak", "≈ 12 / s", "0.045 % of the day per second", "paper"),
        ("design point ×5", "60 orders / s", "ASR 3", "y"), ("API requests", "24,000 / s", "80 % browsing → cache", "blue"),
        ("database writes", "1,800 / s", "limit ≈ 2,400: watch", "pink"), ("Dispatch messages", "180 / s", "trivial", "green")]
for i, (k, v, n, f) in enumerate(rows):
    y = 14 + i * 50
    be_how.box(14, y, 732, 42, None, f, rx=4)
    be_how.text(28, y + 28, k, "t-head", anchor="start", size=15)
    be_how.text(330, y + 28, v, "t-head", anchor="start", size=15)
    be_how.text(500, y + 28, n, anchor="start", size=13)
be_how.note(380, 345, "→ the database and checkout matter; Kafka doesn't", "red", size=16)
be_how.note(380, 378, "one page · twenty minutes · round numbers", "pen", size=15)

ENVELOPE = dict(
    slug="back-of-envelope",
    kicker="a.k.a. “the road trip on a napkin”",
    tldr="<b>Back-of-the-envelope estimation</b> turns a few known numbers (users, orders, requests per order, bytes per record) into rough totals in minutes, using round numbers and simple multiplication. The aim isn't precision; it's to find <b>which part of the design matters</b> and which doesn't, by an order of magnitude, before anyone argues or builds. Write the assumptions down so others can check and change them.",
    chips=[("Family", "size &amp; speed"), ("Origin", "Fermi estimation; Jeff Dean's “numbers everyone should know”"), ("Lives in", "a one-page estimate next to the design or ADR"), ("Pairs with", "capacity planning, load profiles, quality attribute scenarios")],
    problem_side="Larder, 4 October 2027",
    problem="""  <p class="lead">Antwerp opens on 18 October and Eindhoven in November. At the leadership meeting Femke asks: <b>“Will Christmas hold?”</b> Eli says it should; Ben worries about Kafka; Joost remembers last Christmas's <b>38-minute outage</b>. <span class="hl-pink">Nobody has a number</span>, so the debate is all feelings, and the meeting ends with “let's keep an eye on it”.</p>
  <ul>
    <li>Opinions about scale can't be compared without numbers.</li>
    <li>Worry goes to the familiar parts, not the risky ones.</li>
    <li>A full load test takes weeks; the question needs an answer this week.</li>
  </ul>""",
    problem_figs=[be_problem],
    analogy_side="the road trip on a napkin",
    analogy="""  <p>A family plans a road trip on a napkin: <b>900 km</b> at about <b>100 an hour</b> is nine hours of driving; the car does <b>600 km on a tank</b>, so one fuel stop; two drivers can swap there. Nobody needs a route planner to see that <b>fuel isn't the problem</b>, but nine hours of driving is.</p>""",
    analogy_figs=[be_analogy],
    map=[("900 km at 100 an hour", "27,000 orders a day, 0.045 % per second at peak"),
         ("The tank's range", "The database's measured write limit"),
         ("Fuel isn't the problem", "Kafka and Dispatch have plenty of room"),
         ("Nine hours of driving", "1,800 writes a second against about 2,400"),
         ("The napkin", "A one-page estimate with its assumptions")],
    how_side="five known numbers, multiplied out",
    how="""  <p>Ana took twenty minutes and one page. <b>27,000 orders a day</b> forecast for December; Friday's peak second carries about <b>0.045 %</b> of the day: <b>12 orders a second</b>; designed for <b>five times</b> that (ASR 3): <b>60</b>. At about 400 API calls per order, <b>24,000 requests a second</b>, 80 % browsing a cache can serve. At about 30 writes per order, <b>1,800 database writes a second</b> against roughly <b>2,400</b> measured on the current primary. Dispatch: 180 messages a second, trivial. The answer for Femke: <b>the database and checkout</b>, not Kafka.</p>""",
    how_figs=[be_how],
    steps=[("Write the question", "“Can checkout take Christmas at 5× Friday peak?”"),
           ("List known numbers", "Orders, peak share, requests per order, writes per order, sizes."),
           ("Use round numbers", "One or two significant figures; powers of ten."),
           ("Multiply it out", "Per day → per second → per component."),
           ("Compare with limits", "Measured or documented limits of each part."),
           ("Write the assumptions", "So anyone can check and change one number.")],
    vocab=[("Fermi estimate", "A quick estimate from rough, reasoned assumptions."),
           ("Order of magnitude", "A factor of ten: 100 vs 1,000."),
           ("Peak factor", "How much busier the peak is than the average."),
           ("Design point", "The load the design must handle (here 5× Friday peak)."),
           ("Throughput", "Work done per second: orders, requests, writes."),
           ("Headroom", "The gap between the expected load and the limit.")],
    code=dict(file="docs/estimates/2027-christmas.md", note="the one-page estimate, 4 October 2027", plain=True, src="""
# Will Christmas 2027 hold?  (Ana, 4 Oct 2027 · round numbers · check my assumptions)

Orders/day, December (5 cities + Eindhoven)     27,000          forecast, Marco's model
Friday peak second = 0.045 % of the day         ≈ 12 orders/s   from Nov 2026: 2.6/s at 5,800/day
Design point (ASR 3: 5× Friday peak)            ≈ 60 orders/s
API requests per order (browse, basket, pay)    ≈ 400   →  24,000 req/s, ~80 % browsing (cacheable)
DB writes per order (order, lines, events…)     ≈ 30    →   1,800 writes/s   vs ≈ 2,400 measured  ← WATCH
Kafka: ≈ 10 events per order                    →     600 msg/s    vs > 50,000 capacity
Dispatch: 900 couriers × 1 update / 5 s         →     180 msg/s    trivial

Answer: the database (writes, connections) and the checkout path. Not Kafka, not Dispatch.
Next: capacity plan for Postgres; a load test with the real traffic mix.
"""),
    tools="tools: a spreadsheet or a markdown page; latency and throughput reference tables; your own monitoring for the measured limits.",
    gains=["<b>Answers in minutes</b>, not weeks.",
           "<b>Worry goes to the right part</b>.",
           "<b>Assumptions in the open</b>, easy to challenge.",
           "<b>A shared number</b> ends feelings-based debates.",
           "<b>Tells you what to test</b> properly next."],
    losses=["<b>Rough</b>: an order of magnitude, not a promise.",
            "<b>Only as good as the inputs</b>.",
            "<b>Misses non-linear effects</b> (locks, queues).",
            "<b>Can look more certain</b> than it is."],
    baseline="Each line compares <b>debating scale by opinion</b> to <b>a one-page estimate from round numbers with written assumptions</b>.",
    ratings=[(2, 5, "One page, five numbers, one answer."),
             (2, 4, "Femke, Eli, Ben and Joost argue about one table."),
             (2, 5, "Twenty minutes instead of a meeting series."),
             (2, 4, "The real risk (the database) found early."),
             (3, 4, "Change one assumption and recompute."),
             (2, 4, "The estimate sits next to the capacity plan."),
             (3, 4, "Shows where money would and wouldn't help."),
             (2, 5, "No tools needed."),
             (3, 4, "Teams can check their own part.")],
    pitfalls=[("False precision", "“1,847.3 writes per second.”", "round numbers, ranges."),
              ("Averages only", "Daily average hides the peak.", "always compute the peak second."),
              ("Hidden assumptions", "Nobody can check the maths.", "write each assumption on its own line."),
              ("Treating it as a test", "“The estimate says it's fine.”", "use it to choose what to test.")],
    use=["Early in a design, before choosing technology.",
         "When someone asks “will it scale?”",
         "Before a peak season or a launch.",
         "Checking a vendor's or a team's claims."],
    skip=["When you already have real load test results for the same question."],
    related=["<b>Capacity planning</b> (this volume)", "<b>Load profiles</b> (this volume)", "<b>Quality attribute scenarios</b> (vol. 1)", "<b>Architecturally significant requirements</b> (vol. 1)"],
    quiz=[("What is a back-of-the-envelope estimate for?", "Finding which part of a design matters, by an order of magnitude, quickly."),
          ("Why compute the peak second, not the daily average?", "Systems fail at the peak; averages hide it."),
          ("What did Ana's estimate point at?", "The database's writes and the checkout path, not Kafka or Dispatch."),
          ("Why write the assumptions down?", "So others can check them and change one number at a time.")],
    try_it="Take your system's busiest day. From orders (or users) per day, work out the peak second, the requests and database writes per second, and compare each with a measured limit. Write each assumption on its own line and circle the smallest headroom.",
    remember="Plan the trip on a <span class=\"hl\">napkin</span>: find out whether it's the <span class=\"hl\">fuel</span> or the driving hours.",
    sources=["Jon Bentley, <i>Programming Pearls</i>, 2nd ed. (1999), “Back of the Envelope”.",
             "Jeff Dean, “Numbers Everyone Should Know” (2009 talk).",
             "Lawrence Weinstein and John Adam, <i>Guesstimation</i> (2008).",
             "Alex Xu, <i>System Design Interview</i> (2020), estimation chapter."],
)

# ------------------------------------------------------------------ 02 Capacity Planning
cp_problem = Doodle(760, 280, "Doodle of last year's capacity story: the Postgres primary was resized in a hurry on 16 December 2026, two days before Christmas peak, and the change itself needed a failover. Every resource has a different lead time, and nobody tracked how close each one was to its limit.",
                    "Last year: the database resized in a hurry, two days before the peak. Nobody tracked how close anything was.")
cp_problem.box(20, 40, 300, 90, "16 Dec 2026", "pink", sub="emergency resize", stroke="red")
cp_problem.arrow(326, 85, 430, 85, label="2 days", lx=378, ly=72)
cp_problem.box(436, 40, 304, 90, "18 Dec", "pink", sub="peak + failover")
cp_problem.note(380, 200, "the first thing to run out, found too late", "red", size=19)

cp_analogy = Doodle(760, 250, "Doodle of a school planning for next September: count the children starting, check each resource (classrooms, teachers, desks, lunch places), note how long each takes to add (desks a week, a teacher three months, a classroom a year), and start with the slowest.",
                     "A school counts next year's children, checks every resource, and starts with the one that takes longest to add.")
cp_analogy.icon("calendar", 30, 60, 1.2)
for i, (t, s, f) in enumerate([("desks", "a week", "green"), ("teachers", "three months", "y"), ("classroom", "a year", "pink")]):
    cp_analogy.box(150 + i * 200, 50, 186, 90, t, f, sub=s, size=16)
cp_analogy.note(450, 205, "start with the slowest to add", "pen")

cp_how = Doodle(760, 400, "Larder's capacity plan, 18 October 2027, for Friday peak growing to about 2.2 times today's by December. For each resource: usage at today's peak, the multiple of today's peak at which it runs out, and the lead time to add more. Postgres connections: 310 of 400, out at 1.3 times, a pooler takes two weeks. Postgres CPU: 55 percent, out at 1.8 times, resizing takes a failover in a quiet window. Core VMs: 48 percent, autoscaling, minutes. Kafka: 20 percent, plenty. Dispatch: autoscaling. Actions with dates: pooler by 1 November, read replica for browsing by 8 November, primary one size up on 15 November, freeze from 13 December.",
                 "Each resource: used at peak, when it runs out, how long to add more. Fix the slowest first, with dates.")
cp_how.head(20, 30, "resource", anchor="start", size=15)
cp_how.head(250, 30, "at peak", anchor="start", size=15)
cp_how.head(390, 30, "out at", anchor="start", size=15)
cp_how.head(520, 30, "lead time", anchor="start", size=15)
for i, (r, u, o, l, f) in enumerate([("DB connections", "310 / 400", "1.3×", "2 weeks", "pink"), ("DB CPU", "55 %", "1.8×", "a quiet window", "y"),
                                     ("Core VMs", "48 %", "2.0×", "minutes", "green"), ("Kafka", "20 %", "5×+", "—", "green"), ("Dispatch", "autoscale", "—", "minutes", "green")]):
    y = 44 + i * 46
    cp_how.box(12, y, 736, 38, None, f, rx=4)
    cp_how.text(20, y + 25, r, "t-head", anchor="start", size=14)
    cp_how.text(250, y + 25, u, anchor="start", size=14)
    cp_how.text(390, y + 25, o, "t-head", anchor="start", size=14)
    cp_how.text(520, y + 25, l, anchor="start", size=14)
cp_how.box(12, 284, 736, 50, "pooler 1 Nov · replica 8 Nov · resize 15 Nov · freeze 13 Dec", "blue", size=15)
cp_how.note(380, 370, "December peak forecast: ≈ 2.2× today's Friday", "pen", size=16)

CAPACITY = dict(
    slug="capacity-planning",
    kicker="a.k.a. “next September's classrooms”",
    tldr="<b>Capacity planning</b> forecasts demand, checks every resource against it, and adds capacity <b>before</b> the first one runs out. For each resource, write three numbers: <b>usage at today's peak</b>, the <b>multiple of today's peak where it runs out</b>, and the <b>lead time</b> to add more. Act on the smallest gap and the longest lead time first, with dates, and keep headroom (around 30 %) for surprises.",
    chips=[("Family", "size &amp; speed"), ("Origin", "operations and SRE practice; queueing basics"), ("Lives in", "a capacity sheet reviewed monthly, and before every peak"), ("Pairs with", "back-of-the-envelope estimation, load profiles, cost-aware architecture")],
    problem_side="Larder, 18 October 2027",
    problem="""  <p class="lead">Last year Larder's database was <b>resized in a hurry</b> on 16 December, two days before the Christmas peak; the resize itself needed a failover. Every resource has a different <b>lead time</b> (minutes for VMs, weeks for a connection pooler, a quiet window for a database resize), and <span class="hl-pink">nobody tracked how close each was to its limit</span>. The estimate says the database matters again this year.</p>
  <ul>
    <li>The first resource to run out is often not the one people watch.</li>
    <li>Slow-to-change resources get found last.</li>
    <li>Changes made just before a peak are risks themselves.</li>
  </ul>""",
    problem_figs=[cp_problem],
    analogy_side="next September's classrooms",
    analogy="""  <p>A school counts next September's children and checks each resource: <b>desks</b> (a week to order), <b>teachers</b> (three months to hire), <b>classrooms</b> (a year to build). It starts with the one that takes longest to add, not the one that runs out first, and keeps a few spare places for late arrivals.</p>""",
    analogy_figs=[cp_analogy],
    map=[("Next September's children", "December's forecast: 2.2× today's Friday peak"),
         ("Desks, teachers, classrooms", "VMs, database connections and CPU, Kafka, Dispatch"),
         ("Time to add each", "Lead time: minutes, two weeks, a quiet window"),
         ("Start with the slowest", "Pooler and resize planned first, with dates"),
         ("Spare places", "About 30 % headroom at the design point")],
    how_side="used, out at, lead time, then dates",
    how="""  <p>Ana and Eli filled one table. <b>Database connections</b>: 310 of 400 at Friday peak, out at <b>1.3×</b> today, a pooler takes two weeks. <b>Database CPU</b>: 55 %, out at <b>1.8×</b>, a resize needs a failover in a quiet window. VMs, Kafka and Dispatch had room or autoscaled. December's forecast is <b>2.2×</b>, so: pooler by <b>1 November</b>, a read replica for browsing by <b>8 November</b>, the primary one size up on <b>15 November</b>, and a change freeze from <b>13 December</b>. Extra cost: about <b>€2,100 a month</b>.</p>""",
    how_figs=[cp_how],
    steps=[("Forecast demand", "By month, from the business plan; peak, not average."),
           ("List every resource", "Compute, database (CPU, connections, storage), queues, third-party limits."),
           ("Measure usage at peak", "From monitoring, at the real peak hour."),
           ("Find where each runs out", "As a multiple of today's peak, with headroom."),
           ("Note the lead time", "Minutes, weeks, a quiet window, a contract."),
           ("Plan with dates", "Slowest and smallest-gap first; freeze before the peak.")],
    vocab=[("Capacity", "The most load a resource can handle while meeting its targets."),
           ("Utilisation", "How much of a resource is used at a moment."),
           ("Headroom", "Spare capacity kept for surprises."),
           ("Lead time", "How long it takes to add capacity."),
           ("Saturation", "When a resource is full and work starts queueing."),
           ("Change freeze", "No risky changes in the weeks before a peak.")],
    code=dict(file="docs/capacity/2027-q4.md", note="the capacity plan, 18 October 2027", plain=True, src="""
# Capacity plan · Q4 2027 · owner: Eli, with Ana · reviewed monthly, weekly from December
Demand: Friday peak today ≈ 5.4 orders/s · December forecast ≈ 12/s (2.2×) · design point 5×

| Resource           | At peak today | Runs out at | Lead time        | Action (date)                     |
|--------------------|---------------|-------------|------------------|-----------------------------------|
| DB connections     | 310 / 400     | 1.3×        | 2 weeks          | connection pooler (1 Nov)         |
| DB CPU (primary)   | 55 %          | 1.8×        | quiet window     | browse reads → replica (8 Nov)    |
|                    |               |             |                  | one size up (15 Nov, Tue 05:00)   |
| Core VMs           | 48 %          | 2.0×        | minutes (auto)   | max 12 → 16                       |
| Kafka              | 20 %          | > 5×        | —                | none                              |
| PSP rate limit     | 8 req/s       | 50 req/s    | contract         | confirmed in writing (Cho)        |
Change freeze: 13 Dec – 3 Jan · extra cost ≈ €2,100/month
"""),
    tools="tools: the monitoring stack's peak dashboards, a capacity sheet (spreadsheet or markdown), cloud quotas pages, vendors' documented limits.",
    gains=["<b>No emergency resizes</b> before peaks.",
           "<b>The first bottleneck</b> found in time.",
           "<b>Lead times respected</b>.",
           "<b>Spending planned</b>, not panicked.",
           "<b>Freeze dates</b> everyone knows."],
    losses=["<b>Forecasts are wrong</b>, sometimes badly.",
            "<b>Headroom costs money</b>.",
            "<b>Needs good peak data</b>.",
            "<b>Monthly upkeep</b>."],
    baseline="Each line compares <b>resizing when something hurts</b> to <b>a capacity sheet with usage, limit and lead time per resource, acted on with dates</b>.",
    ratings=[(2, 5, "One table shows every resource and its limit."),
             (2, 4, "Marco sees the cost before it's spent."),
             (2, 4, "Actions follow the table directly."),
             (1, 5, "No resize two days before Christmas."),
             (3, 4, "Monthly review adjusts to new forecasts."),
             (2, 4, "Decisions dated in the sheet."),
             (2, 4, "Spending planned: €2,100 a month."),
             (3, 3, "An hour a month to keep up."),
             (3, 4, "Teams own their rows.")],
    pitfalls=[("Watching averages", "50 % average, 100 % at peak.", "measure at the peak hour."),
              ("Forgetting hidden limits", "Connections, quotas, vendor rate limits.", "list every limit, not just CPU."),
              ("Ignoring lead times", "A two-week job started two days before.", "plan slowest first."),
              ("No headroom", "Planned to exactly 100 %.", "keep around 30 % spare.")],
    use=["Before peak seasons and launches.",
         "Monthly, for growing systems.",
         "When a forecast changes (a new city, a new client).",
         "Before signing capacity-based contracts."],
    skip=["Fully serverless parts with high limits (check the quotas once)."],
    related=["<b>Back-of-the-envelope estimation</b> (this volume)", "<b>Load profiles</b> (this volume)", "<b>Cost-aware architecture</b> (this volume)", "<b>Autoscaling</b> (patterns, Vol. 6)"],
    quiz=[("What three numbers does each resource need?", "Usage at peak, where it runs out, and the lead time to add more."),
          ("What ran out first at Larder?", "Database connections, at 1.3× today's peak."),
          ("Why plan by lead time?", "Slow-to-add resources must start first."),
          ("Why a change freeze?", "Changes made just before a peak are risks themselves.")],
    try_it="List every resource your system needs at peak, including connections, quotas and vendor limits. For each, write usage at peak, where it runs out, and lead time. Put a date on the one with the smallest gap and the longest lead time.",
    remember="Count next <span class=\"hl\">September's</span> children; build the <span class=\"hl\">classroom</span> first.",
    sources=["Betsy Beyer et al., <i>Site Reliability Engineering</i> (2016), capacity planning.",
             "John Allspaw, <i>The Art of Capacity Planning</i> (2008; 2nd ed. 2017 with Arun Kejariwal).",
             "Neil Gunther, <i>Guerrilla Capacity Planning</i> (2007).",
             "Brendan Gregg, <i>Systems Performance</i>, 2nd ed. (2020), the USE method."],
)

# ------------------------------------------------------------------ 03 Load Profiles
lp_problem = Doodle(760, 280, "Doodle of the 2026 load test: a flat line of 1,000 requests a second on checkout only, for thirty minutes. It passed. Real traffic looks nothing like that: a Friday ramp, a spike when a campaign push goes out, mostly browsing. Nobody had tested the shape.",
                    "Last year's test: a flat line on checkout only. It passed. Real traffic has a ramp, a spike and mostly browsing.")
lp_problem.line("M30 160 L330 160", color="blue")
lp_problem.text(180, 140, "the test: flat, checkout only", size=15)
lp_problem.line("M420 200 L520 170 L560 60 L600 150 L730 140", color="red")
lp_problem.text(580, 40, "push spike", "t t-red", size=15)
lp_problem.text(470, 220, "Friday ramp", size=15)
lp_problem.note(380, 262, "it passed, and proved nothing", "red", size=19)

lp_analogy = Doodle(760, 250, "Doodle of a bridge load test: engineers don't just park one heavy lorry in the middle. They test the morning rush, a marathon crossing in step, wind gusts, and a traffic jam that sits for hours, because each shape stresses the bridge differently.",
                     "A bridge isn't tested with one parked lorry: rush hour, marching feet, gusts and a long jam each stress it differently.")
lp_analogy.icon("traffic", 30, 60, 1.2)
for i, (t, f) in enumerate([("rush hour", "y"), ("in step", "pink"), ("gusts", "blue"), ("long jam", "paper")]):
    lp_analogy.box(140 + i * 152, 60, 140, 70, t, f, size=16)
lp_analogy.note(450, 200, "each shape finds a different weakness", "pen")

lp_how = Doodle(760, 400, "Larder's load profiles from 1 November 2027. The mix: 78 percent browsing and search, 12 percent basket, 6 percent checkout, 4 percent picker, dispatch and business API. Four shapes: the Friday ramp, four times in sixty minutes; the push spike, three times in two minutes after a campaign push to 300,000 customers; the business morning, standing orders released at 06:30; and a four-hour soak. Test on 8 November on production-sized staging: the push spike exhausted Larder Core's worker pool at 2.6 times. Fixes: cache the home screen, send pushes in waves of 50,000.",
                 "The real mix and four real shapes. The push spike found what a flat line never would.")
lp_how.box(14, 14, 732, 50, "mix: 78 % browse · 12 % basket · 6 % checkout · 4 % ops + business", "paper", size=14)
for i, (t, s, f) in enumerate([("Friday ramp", "4× in 60 min", "y"), ("push spike", "3× in 2 min", "pink"), ("business morning", "06:30 release", "blue"), ("soak", "4 hours", "green")]):
    lp_how.box(14 + i * 184, 84, 174, 80, t, f, sub=s, size=15)
lp_how.box(14, 190, 732, 70, None, "pink", stroke="red")
lp_how.head(380, 220, "8 Nov: push spike → workers exhausted at 2.6×", size=16)
lp_how.text(380, 246, "fix: cache the home screen · pushes in waves of 50,000", size=14)
lp_how.note(380, 300, "re-run 15 Nov: 5× Friday peak, checkout p95 640 ms", "green", size=16)
lp_how.note(380, 332, "every profile stored as code, re-run before each peak", "pen", size=15)

LOAD = dict(
    slug="load-profiles",
    kicker="a.k.a. “rush hour, not a parked lorry”",
    tldr="A load test is only as good as its <b>load profile</b>: the <b>mix</b> of requests (mostly browsing? mostly writes?) and the <b>shape</b> over time (a steady ramp, a sudden spike, a long soak). Build profiles from <b>production traffic</b>, add the known special events (campaign pushes, morning batches), test on production-sized infrastructure, and keep the profiles as code to re-run before every peak.",
    chips=[("Family", "size &amp; speed"), ("Origin", "performance engineering; workload modelling"), ("Lives in", "load-test scripts in the repo (k6, Gatling, Locust)"), ("Pairs with", "capacity planning, performance budgets, back-of-the-envelope estimation")],
    problem_side="Larder, 1 November 2027",
    problem="""  <p class="lead">Last year's load test sent a <b>flat 1,000 requests a second</b> to checkout for thirty minutes. <b>It passed.</b> Real traffic looks nothing like it: mostly <b>browsing</b>, a <b>Friday ramp</b>, and a sharp <b>spike</b> when a campaign push goes to every customer at once. <span class="hl-pink">The test proved checkout works on a quiet, imaginary day.</span></p>
  <ul>
    <li>A flat line misses spikes, ramps and queues building up.</li>
    <li>Testing one endpoint misses contention between them.</li>
    <li>Special events (pushes, batches) cause the real peaks.</li>
  </ul>""",
    problem_figs=[lp_problem],
    analogy_side="testing a bridge",
    analogy="""  <p>Engineers don't test a bridge by parking <b>one heavy lorry</b> in the middle. They model <b>rush hour</b>, a crowd crossing <b>in step</b>, <b>wind gusts</b> and a <b>traffic jam</b> that sits for hours, because each shape stresses the bridge differently. The parked lorry tells them almost nothing about Monday morning.</p>""",
    analogy_figs=[lp_analogy],
    map=[("The parked lorry", "A flat 1,000 requests a second on checkout"),
         ("Rush hour", "The Friday ramp: 4× in sixty minutes"),
         ("Crossing in step", "The push spike: 3× in two minutes"),
         ("The long jam", "A four-hour soak"),
         ("The mix of vehicles", "78 % browse, 12 % basket, 6 % checkout, 4 % ops")],
    how_side="the real mix, the real shapes",
    how="""  <p>Eli took a month of production logs: <b>78 %</b> browsing and search, <b>12 %</b> basket, <b>6 %</b> checkout, <b>4 %</b> picker, Dispatch and business API. Ana added four shapes: the <b>Friday ramp</b>, the <b>push spike</b> after a campaign to 300,000 customers, the <b>business morning</b> release at 06:30, and a <b>four-hour soak</b>. On 8 November the push spike <b>exhausted Larder Core's workers at 2.6×</b>. Fixes: a cached home screen and pushes in waves of 50,000. Re-run on 15 November: 5× Friday peak, checkout p95 <b>640 ms</b>.</p>""",
    how_figs=[lp_how],
    steps=[("Take the mix from production", "Requests by type from a real peak period."),
           ("Model the shapes", "Ramps, spikes, batches, soaks; from real events."),
           ("Add the special events", "Campaign pushes, morning batches, sales."),
           ("Test production-sized", "Same instance sizes, data volumes and limits."),
           ("Watch the whole system", "Queues, pools, connections, not just response times."),
           ("Keep profiles as code", "Re-run before every peak and after big changes.")],
    vocab=[("Load profile", "The mix and shape of traffic in a test."),
           ("Traffic mix", "The share of each kind of request."),
           ("Ramp", "Load rising steadily over time."),
           ("Spike", "A sudden jump in load."),
           ("Soak test", "Steady load for hours, to find leaks and slow build-ups."),
           ("Thundering herd", "Many clients acting at the same moment, e.g. after a push.")],
    code=dict(file="loadtests/profiles/push-spike.md", note="the push spike profile, November 2027", plain=True, src="""
# Profile: push spike (campaign push to all customers)       owner: Eli · code: push_spike.js (k6)

Mix         78 % browse/search · 12 % basket · 6 % checkout · 4 % picker/dispatch/business API
Baseline    Friday 18:00 level (≈ 2,200 req/s today)
Shape       t=0 push sent to 300,000 devices
            0–2 min   ramp to 3× baseline (app opens → home screen → offers)
            2–12 min  decay back to baseline
Data        production-sized staging: 2.6 M customers, 9,000 products × 7 stores
Pass        checkout p95 < 800 ms (ASR 3) · errors < 0.1 % · no pool exhaustion
Result 8 Nov    FAIL at 2.6×: Core worker pool exhausted (home screen built per request)
Result 15 Nov   PASS at 5× Friday peak: checkout p95 640 ms (home cached 60 s, pushes in 50k waves)
"""),
    tools="tools: k6, Gatling, Locust or JMeter; production logs or analytics for the mix; a production-sized staging environment; dashboards for pools and queues.",
    gains=["<b>Finds the real failure</b>: the push spike.",
           "<b>Tests contention</b> between request types.",
           "<b>Repeatable</b> before every peak.",
           "<b>Confidence</b> grounded in real shapes.",
           "<b>Fixes found weeks early</b>."],
    losses=["<b>Production-sized staging</b> costs money.",
            "<b>Profiles go stale</b> as behaviour changes.",
            "<b>Takes days</b> to build well.",
            "<b>Test data</b> needs care (privacy)."],
    baseline="Each line compares <b>a flat load test on one endpoint</b> to <b>tests with the production mix and real shapes, on production-sized infrastructure</b>.",
    ratings=[(2, 4, "Each profile says what it simulates and why."),
             (3, 4, "Joost and Femke hear “tested at 5×, with a push”."),
             (3, 3, "Days to build, then quick to re-run."),
             (1, 5, "The push spike found before Christmas."),
             (2, 4, "Profiles change as traffic changes."),
             (2, 4, "Results stored with the profiles."),
             (3, 3, "A production-sized staging costs a few days' bill."),
             (3, 3, "Upkeep before each peak."),
             (3, 4, "Teams add their own request types.")],
    pitfalls=[("Flat lines", "Constant load for thirty minutes.", "ramps, spikes, soaks."),
              ("One endpoint", "Only checkout tested.", "the production mix."),
              ("Toy environment", "Small database, no limits.", "production-sized, with real quotas."),
              ("Response times only", "Pools and queues not watched.", "watch saturation everywhere.")],
    use=["Before peak seasons, launches and campaigns.",
         "After big architecture changes.",
         "When capacity plans need evidence.",
         "Checking a fix for a past incident."],
    skip=["Internal tools with tiny, steady traffic."],
    related=["<b>Capacity planning</b> (this volume)", "<b>Performance budgets</b> (this volume)", "<b>Connection pooling</b> (patterns, Vol. 3)", "<b>Rate limiter</b> (patterns, Vol. 1)"],
    quiz=[("What two things make up a load profile?", "The mix of requests and the shape of traffic over time."),
          ("What did the push spike reveal?", "Larder Core's workers ran out at 2.6× because the home screen was built per request."),
          ("Why test on production-sized infrastructure?", "Limits, data volumes and pools behave differently at small size."),
          ("Why keep profiles as code?", "To re-run them before every peak and after changes.")],
    try_it="Pull a week of production traffic and write down the mix by request type. Sketch the busiest hour's shape, mark any special events (pushes, batches, sales), and write one test profile that reproduces it.",
    remember="Test the <span class=\"hl\">rush hour</span>, not a parked <span class=\"hl\">lorry</span>.",
    sources=["Ian Molyneaux, <i>The Art of Application Performance Testing</i>, 2nd ed. (2014).",
             "Grafana k6 documentation, “Test types” (load, stress, spike, soak).",
             "Brendan Gregg, <i>Systems Performance</i>, 2nd ed. (2020).",
             "Martin Kleppmann, <i>Designing Data-Intensive Applications</i> (2017), describing load."],
)

# ------------------------------------------------------------------ 04 Performance Budgets
pb_problem = Doodle(760, 280, "Doodle of November 2027: after the Antwerp launch added French, the web shop's home page on a mid-range Android phone over 4G slowed from 1.9 to 3.4 seconds, and the app bundle grew to 410 kilobytes. Each change was small and reasonable. Nobody had agreed a limit, so nothing failed.",
                    "Antwerp added French: the home page went from 1.9 to 3.4 s, one small change at a time. Nothing failed, because nothing had a limit.")
pb_problem.box(20, 40, 220, 90, "1.9 s", "green", sub="September")
pb_problem.arrow(244, 85, 300, 85)
pb_problem.box(304, 40, 220, 90, "3.4 s", "pink", sub="November", stroke="red")
pb_problem.box(560, 40, 180, 90, "bundle", "y", sub="410 KB")
pb_problem.note(380, 200, "each change small, no limit anywhere", "red", size=19)

pb_analogy = Doodle(760, 250, "Doodle of an airline's baggage allowance: 23 kilos, checked at the desk. Every traveller adds just one more thing; the scale stops it at the desk, not when the plane is too heavy to take off.",
                     "A baggage allowance: 23 kg, checked at the desk, not when the plane can't take off.")
pb_analogy.icon("gauge", 40, 60, 1.3)
pb_analogy.box(170, 50, 270, 90, "23 kg", "y", sub="agreed in advance")
pb_analogy.box(470, 50, 270, 90, "the scale", "green", sub="checked at the desk")
pb_analogy.note(450, 205, "stopped early, every time", "pen")

pb_how = Doodle(760, 380, "Larder's performance budgets from 15 November 2027, each with an owner and a check in CI. Home page largest paint at most 2.5 seconds on a mid-range Android over 4G, Dee. Web and app JavaScript at most 300 kilobytes compressed, Dee. Checkout API p95 at most 800 milliseconds at five times peak, Ben. Search p95 at most 300 milliseconds, Ben. Picker scan to next item at most 1 second, Eli. A breach fails the build like a failing test. Lazy-loading the language files brought the home page back to 2.2 seconds.",
                 "Five budgets, five owners, checked in CI. A breach fails the build.")
pb_how.head(20, 30, "budget", anchor="start", size=15)
pb_how.head(470, 30, "limit", anchor="start", size=15)
pb_how.head(650, 30, "owner", anchor="start", size=15)
for i, (b, l, o, f) in enumerate([("home page, mid Android 4G", "≤ 2.5 s", "Dee", "y"), ("JavaScript, compressed", "≤ 300 KB", "Dee", "y"),
                                  ("checkout API p95 at 5×", "≤ 800 ms", "Ben", "blue"), ("search p95", "≤ 300 ms", "Ben", "blue"), ("picker: scan → next item", "≤ 1 s", "Eli", "green")]):
    y = 44 + i * 46
    pb_how.box(12, y, 736, 38, None, f, rx=4)
    pb_how.text(20, y + 25, b, "t-head", anchor="start", size=14)
    pb_how.text(470, y + 25, l, anchor="start", size=14)
    pb_how.text(650, y + 25, o, anchor="start", size=14)
pb_how.box(12, 284, 736, 46, "a breach fails the build, like a failing test", "pink", size=15)
pb_how.note(380, 362, "lazy-loaded language files: 3.4 s → 2.2 s", "green", size=16)

BUDGETS = dict(
    slug="performance-budgets",
    kicker="a.k.a. “the baggage allowance”",
    tldr="A <b>performance budget</b> is an agreed limit on something users feel (load time, response time) or something that causes it (bundle size, number of calls), with an <b>owner</b> and an <b>automatic check</b>. Without one, performance erodes by small, reasonable changes until it's bad. With one, a breach <b>fails the build</b> and is fixed while it's small.",
    chips=[("Family", "size &amp; speed"), ("Origin", "web performance practice (Tim Kadlec, Addy Osmani); SLOs for APIs"), ("Lives in", "CI checks and a budgets page"), ("Pairs with", "quality attribute scenarios, load profiles, fitness functions")],
    problem_side="Larder, 15 November 2027",
    problem="""  <p class="lead">Antwerp brought French to the apps and the web shop. On a <b>mid-range Android phone over 4G</b>, the web home page went from <b>1.9 to 3.4 seconds</b> between September and November; the app's JavaScript grew to <b>410 KB</b>. Each change (translations, a new font, a promotions banner) was small and reasonable. <span class="hl-pink">Nobody had agreed a limit, so nothing failed.</span></p>
  <ul>
    <li>Performance erodes in small steps nobody notices.</li>
    <li>Developers test on fast laptops and fast Wi-Fi.</li>
    <li>“Fast” means something different to everyone.</li>
  </ul>""",
    problem_figs=[pb_problem],
    analogy_side="the baggage allowance",
    analogy="""  <p>An airline agrees a <b>baggage allowance</b> (23 kilos) and checks it <b>at the desk</b>. Every traveller wants to add just one more thing; the scale stops it at the desk, early and cheaply, not when the plane is too heavy to take off.</p>""",
    analogy_figs=[pb_analogy],
    map=[("23 kilos", "2.5 s home page, 300 KB JavaScript"),
         ("Checked at the desk", "Checked in CI on every change"),
         ("One more thing in the bag", "A font, a banner, a translation file"),
         ("The plane too heavy", "Customers leaving a slow app"),
         ("The airline's rule", "Budgets agreed with owners")],
    how_side="limits users feel, owners, CI checks",
    how="""  <p>Ana, Dee and Ben agreed <b>five budgets</b>, each with an <b>owner</b>: home page ≤ <b>2.5 s</b> on a mid-range Android over 4G, JavaScript ≤ <b>300 KB</b> compressed (Dee); checkout API p95 ≤ <b>800 ms</b> at 5× (ASR 3) and search ≤ <b>300 ms</b> (Ben); picker scan to next item ≤ <b>1 s</b> (Eli). Lighthouse CI and the load-test thresholds check them; a breach <b>fails the build</b>. Dee lazy-loaded the language files: home page <b>2.2 s</b>.</p>""",
    how_figs=[pb_how],
    steps=[("Pick what users feel", "Load time, response time, time to the next task."),
           ("Set limits on real devices", "Mid-range phones, real networks, peak load."),
           ("Add cause budgets", "Bundle size, image weight, calls per screen."),
           ("Give each an owner", "Who decides when it's breached."),
           ("Check automatically", "In CI, on every change; fail the build."),
           ("Review quarterly", "Tighten as you improve; never loosen silently.")],
    vocab=[("Performance budget", "An agreed limit with an owner and a check."),
           ("Largest contentful paint", "When the main content of a page appears."),
           ("p95", "The time 95 % of requests are faster than."),
           ("Bundle size", "How much code the app or page downloads."),
           ("Lighthouse CI", "A tool that checks web performance in CI."),
           ("Regression", "Something that used to be fine getting worse.")],
    code=dict(file="docs/architecture/performance-budgets.md", note="the budgets page, November 2027", plain=True, src="""
# Performance budgets                                   agreed 15 Nov 2027 · reviewed quarterly

| Budget                                   | Limit     | Measured on                  | Check          | Owner |
|------------------------------------------|-----------|------------------------------|----------------|-------|
| Web home page, largest contentful paint  | ≤ 2.5 s   | mid-range Android, 4G profile | Lighthouse CI  | Dee   |
| App + web JavaScript (compressed)        | ≤ 300 KB  | release build                | bundle check   | Dee   |
| Checkout API p95                         | ≤ 800 ms  | 5× Friday peak (ASR 3)        | k6 thresholds  | Ben   |
| Search API p95                           | ≤ 300 ms  | Friday peak                  | k6 thresholds  | Ben   |
| Picker: scan → next item shown            | ≤ 1 s     | store handheld, store Wi-Fi  | device test    | Eli   |

A breach fails the build. Exceptions: the owner decides, in writing, for one release only.
"""),
    tools="tools: Lighthouse CI or WebPageTest, bundle-size checks, k6 or Gatling thresholds, real-device testing; a budgets page in the docs.",
    gains=["<b>Erosion stopped</b> at the first step.",
           "<b>“Fast” defined</b> in numbers.",
           "<b>Real devices</b>, not laptops.",
           "<b>Owners decide</b> exceptions.",
           "<b>Cheap fixes</b>, caught early."],
    losses=["<b>Builds fail</b> for performance.",
            "<b>Setting good limits</b> takes data.",
            "<b>Measurement noise</b> can be annoying.",
            "<b>Pressure to loosen</b> budgets."],
    baseline="Each line compares <b>noticing slowness when customers complain</b> to <b>agreed budgets with owners, checked in CI</b>.",
    ratings=[(2, 5, "Five numbers, five owners."),
             (2, 4, "Product and engineering agree what fast means."),
             (2, 4, "A breach is a red build, not a debate."),
             (2, 4, "Slow releases never reach customers."),
             (3, 4, "Budgets tighten as things improve."),
             (2, 4, "Exceptions written down by the owner."),
             (3, 3, "Neutral."),
             (3, 4, "Automatic once set up."),
             (2, 4, "Teams own their budgets.")],
    pitfalls=[("Fast-laptop limits", "Measured on the developer's Mac.", "mid-range phones, real networks."),
              ("No owner", "Breaches argued in chat.", "one owner decides."),
              ("Warnings only", "Yellow warnings everyone ignores.", "fail the build."),
              ("Too many budgets", "Thirty numbers.", "a handful users feel, plus key causes.")],
    use=["Customer-facing apps and web shops.",
         "APIs with response-time requirements.",
         "Before adding languages, markets or features that add weight.",
         "Operational tools where seconds matter (pickers)."],
    skip=["Batch jobs where only the end time matters (use a deadline instead)."],
    related=["<b>Load profiles</b> (this volume)", "<b>Fitness functions</b> (vol. 1)", "<b>Quality attribute scenarios</b> (vol. 1)", "<b>Code splitting &amp; lazy loading</b> (patterns, Vol. 2)"],
    quiz=[("What makes a performance budget work?", "An agreed limit, an owner and an automatic check that fails the build."),
          ("Why measure on mid-range phones over 4G?", "That's what many customers use; laptops on Wi-Fi hide slowness."),
          ("What went wrong at Larder?", "Small changes for Antwerp made the home page 3.4 s with no limit to stop them."),
          ("What fixed it?", "Lazy-loading language files: back to 2.2 s.")],
    try_it="Pick the screen or API your customers use most. Measure it on a mid-range phone or at peak load, set a budget slightly better than today, name an owner, and add a check to CI that fails the build when it's broken.",
    remember="Weigh the <span class=\"hl\">bag</span> at the desk, not on the <span class=\"hl\">runway</span>.",
    sources=["Tim Kadlec, “Setting a Performance Budget” (2013).",
             "Addy Osmani, “Start Performance Budgeting” (2019).",
             "web.dev, “Performance budgets 101” and Lighthouse CI documentation.",
             "Steve Souders, <i>High Performance Web Sites</i> (2007)."],
)

NOTES = [ENVELOPE, CAPACITY, LOAD, BUDGETS]
