# Series 2 · Book 5 · The IT Operations Notebook · Vol. 4 · Making promises.
# Narrator: Eli (he/him). Facts: docs/larder-casebook.md, "Book 5, Vol. 4".

# ------------------------------------------------------------------ 01 What Do Users Count as Working?
sl_problem = Doodle(760, 260, "Doodle of Femke's question at the board prep on Monday 5 July 2027: 'How reliable are we, actually?' Eli has server uptime (99.98 percent), incident counts and the orders-affected line. Each answers a different question. Server uptime says nothing about a checkout that fails at the payment step, a business order that times out, or a packed order waiting for a courier.",
                    "“How reliable are we?” Server uptime 99.98 %, but that isn't what customers count.")
sl_problem.box(14, 30, 230, 100, "server uptime", "green", sub="99.98 %", size=19, subsize=16)
sl_problem.box(264, 30, 230, 100, "incidents", "y", sub="by severity", size=19, subsize=16)
sl_problem.box(514, 30, 232, 100, "orders affected", "y", sub="per month", size=19, subsize=16)
sl_problem.note(380, 180, "none of them is “did it work for the person using it?”", "red", size=18)

sl_analogy = Doodle(760, 220, "Doodle of a train company measuring punctuality. It could count trains that left the depot, or engines that started. Passengers count one thing: did my train arrive within five minutes of the timetable? That's the number printed on the station wall.",
                    "Engines that started vs trains that arrived on time. Passengers only count the second.")
sl_analogy.icon("traffic", 50, 30, 1.2)
sl_analogy.box(140, 40, 290, 100, "engines started", "paper", sub="the operator's view", size=18, subsize=14)
sl_analogy.box(456, 40, 290, 100, "arrived ≤ 5 min late", "green", sub="the passenger's view", size=18, subsize=14)
sl_analogy.note(450, 190, "measure what the user counts, as good ÷ total", "pen", size=18)

sl_how = Doodle(760, 400, "Larder's service level indicators, written in July 2027. Each one is good events divided by all events, measured where the user meets the service. Checkout: successful checkouts divided by attempts, not counting card declines. Checkout speed: checkouts faster than 800 milliseconds divided by all. Business ordering: portal and API requests that succeed divided by all. Dispatch: packed orders assigned a courier within 90 seconds divided by all packed orders. Store sync: store-minutes with stock less than 2 minutes old divided by all store-minutes in opening hours. June 2027: 99.86, 96.1, 99.74, 98.9 and 99.6 percent.",
                "Five SLIs, each good ÷ total, measured where the user meets the service. June 2027 values on the right.")
rows = [("checkout success", "successful ÷ attempts (no card declines)", "99.86 %"), ("checkout speed", "< 800 ms ÷ all", "96.1 %"),
        ("business ordering", "portal + API ok ÷ all requests", "99.74 %"), ("Dispatch", "assigned < 90 s ÷ packed orders", "98.9 %"), ("store sync", "fresh (< 2 min) ÷ store-minutes", "99.6 %")]
for i, (n, d, v) in enumerate(rows):
    y = 14 + i * 62
    sl_how.box(14, y, 200, 52, n, "blue", size=15)
    sl_how.box(224, y, 380, 52, d, "paper", size=13)
    sl_how.box(614, y, 132, 52, v, "green", size=16)
sl_how.note(380, 348, "measured at the load balancer and in the apps, not on the servers", "pen", size=15)
sl_how.note(380, 382, "good events ÷ all events, always", "red", size=16)

SLIS = dict(
    slug="slis",
    kicker="a.k.a. “service level indicators”",
    tldr="A <b>service level indicator (SLI)</b> measures one thing users care about, as <b>good events divided by all events</b>: successful checkouts over attempts, fast requests over all requests, orders assigned in time over all orders. Measure it <b>where the user meets the service</b> (the load balancer, the app), not on the servers. A few SLIs per service turn “how reliable are we?” into numbers the business recognises.",
    chips=[("Family", "making promises"), ("Lives in", "ops/slo/&lt;service&gt;.yml, computed from request logs and app events"), ("Pairs with", "SLOs, error budgets, measuring availability")],
    itil=dict(groups=["service"], chain=["plan", "improve"], practices=["service level management", "measurement and reporting"],
              sre="“SLI”: good events ÷ valid events", principles=["Focus on value"],
              older="ITIL v3: service level requirements, KPIs"),
    problem_side="Larder, Monday 5 July 2027",
    problem="""  <p class="lead">At the board prep on <b>5 July</b> Femke asks: <b>“How reliable are we, actually?”</b> Korenwolf's renewal is in the autumn, and Ruben wants a number in the contract. Eli has <b>server uptime (99.98 %)</b>, incident counts and the orders-affected line from his monthly page. <span class="hl-pink">None of them answers “did it work for the person using it?”</span> Server uptime says nothing about a checkout failing at the payment step, a business order timing out, or a packed order waiting for a courier.</p>
  <ul>
    <li>Machines can be up while customers fail.</li>
    <li>Every team measures something different.</li>
    <li>A contract number needs a precise definition first.</li>
  </ul>""",
    problem_figs=[sl_problem],
    analogy_side="the train company's punctuality",
    analogy="""  <p>A train company could count <b>trains that left the depot</b>, or engines that started. Passengers count one thing: <b>did my train arrive within five minutes of the timetable?</b> That's the number on the station wall, worked out as trains on time divided by all trains. It's the operator's job to make that number good, whatever the engines did.</p>""",
    analogy_figs=[sl_analogy],
    map=[("Engines that started", "Server uptime"),
         ("Trains on time ÷ all trains", "Successful checkouts ÷ attempts"),
         ("Within five minutes", "Faster than 800 ms; assigned within 90 s"),
         ("Measured at the platform", "Measured at the load balancer and in the apps"),
         ("The number on the wall", "The SLI on the service's page")],
    how_side="a few good ÷ total numbers per service, where the user is",
    how="""  <p>In July Eli writes <b>five SLIs</b> with the service owners, each as <b>good events ÷ all events</b>:</p>
  <ul>
    <li><b>Checkout success</b>: successful checkouts ÷ attempts. Card declines don't count, because a declined card isn't Larder failing.</li>
    <li><b>Checkout speed</b>: checkouts faster than <b>800 ms</b> ÷ all checkouts (Ana's performance budget).</li>
    <li><b>Business ordering</b>: portal and API requests that succeed ÷ all requests.</li>
    <li><b>Dispatch</b>: packed orders assigned a courier within <b>90 s</b> ÷ all packed orders.</li>
    <li><b>Store sync</b>: store-minutes with stock less than <b>2 minutes</b> old ÷ all store-minutes in opening hours.</li>
  </ul>
  <p>They're measured <b>where the user meets the service</b>: at the load balancer, in the apps and in the store heartbeat, not on the servers. June's values are 99.86 %, 96.1 %, 99.74 %, 98.9 % and 99.6 %. Femke's answer now fits on one line per service. The next question, how good is good enough, is the next note.</p>""",
    how_figs=[sl_how],
    steps=[("Ask what users count as working", "Per service, in their words."),
           ("Write it as good ÷ all", "Define both: what's an event, what's good."),
           ("Exclude what isn't your failure", "Card declines; requests from tests."),
           ("Measure where the user is", "Load balancer, app, device, not the server."),
           ("Keep it to a few per service", "Success and speed are usually enough."),
           ("Compute a baseline", "Last month's value, before setting any target.")],
    vocab=[("SLI (service level indicator)", "A measured share of good events: what users experience, as a number."),
           ("Good event", "An event that met the user's need: a success, fast enough, on time."),
           ("Valid event", "An event that counts at all (tests and card declines excluded)."),
           ("Latency SLI", "Share of requests faster than a threshold."),
           ("Freshness SLI", "Share of time data is newer than a threshold."),
           ("Measurement point", "Where an SLI is counted; closer to the user is better.")],
    code=dict(file="ops/slo/checkout.yml", note="SLIs · July 2027", plain=True, src="""
service: checkout                     owner: Ben           tier: critical
slis:
  success:
    good:   checkout requests with status ok (2xx)
    valid:  all checkout attempts, excluding card declines and test baskets
    where:  load balancer logs + app event checkout_completed
    june:   99.86 %
  speed:
    good:   checkout completed in < 800 ms (server side) and < 2.5 s (app side)
    valid:  all completed checkouts
    june:   96.1 %
not an SLI: server uptime (99.98 %) · CPU · number of incidents
"""),
    tools="tools: request logs at the load balancer, app events, a small job that computes good ÷ valid per minute.",
    ladder=[("machine numbers", ["Uptime and CPU.", "“Reliable?” unanswerable."]),
            ("a few SLIs per service", ["Good ÷ valid, where the user is.", "Baselines known."]),
            ("SLIs computed live", ["Per minute, per city.", "Shown on each service's page."]),
            ("SLIs everywhere", ["Every new service launches with its SLIs.", "Used in planning."])],
    ladder_now=2,
    baseline="Each line compares <b>server uptime and incident counts</b> to <b>a few good ÷ valid SLIs per service, measured where the user is</b>.",
    ratings=[(2, 4, "Measures what customers actually feel."),
             (3, 3, "Neutral on its own."),
             (3, 3, "Neutral."),
             (3, 3, "Neutral."),
             (2, 4, "One number per service that the business recognises."),
             (3, 3, "Neutral."),
             (3, 3, "Neutral."),
             (3, 3, "Neutral."),
             (3, 3, "A day per service to define.")],
    pitfalls=[("Measuring the servers", "Up machines, failing customers.", "measure where the user is."),
              ("Counting what isn't yours", "Card declines make checkout look broken.", "define valid events."),
              ("Too many SLIs", "Nobody knows which one matters.", "success and speed, mostly."),
              ("Averages instead of shares", "An average speed hides the slow tail.", "share of requests under a threshold.")],
    use=["Someone asks how reliable you are.", "A client wants a number in a contract.", "Teams argue about whether a service is “fine”.", "Before setting any target."],
    skip=["Internal tools nobody depends on: a heartbeat is enough."],
    related=["<b>How Good Is Good Enough?</b> (next note)", "<b>SLOs & Error Budgets</b> (cloud, vol. 6)", "<b>Performance Budgets</b> (Ana, vol. 5)", "<b>How Do We Know It's Broken?</b> (vol. 1)"],
    quiz=[("What is an SLI?", "A measured share of good events among valid events, for something users care about."),
          ("Why exclude card declines from checkout success?", "A declined card isn't Larder failing; counting it would hide real failures."),
          ("Where should SLIs be measured?", "Where the user meets the service: load balancer, apps, devices."),
          ("Why share-under-a-threshold rather than average speed?", "Averages hide the slow tail that users feel."),
          ("Why isn't server uptime an SLI?", "Servers can be up while customers fail.")],
    quiz_sit=[("Sam says customers complain about slow checkout, but the checkout speed SLI looks fine. What do you check?", "Where it's measured: the server-side number may miss slow networks and the app. Add (or look at) the app-side measure, and split by city and device.")],
    try_it="Pick your most important service and write two SLIs as good ÷ valid: one for success, one for speed. Where would you measure them? Compute last month's values.",
    remember="Measure what users count, as <span class=\"hl\">good ÷ all</span>, and measure it <span class=\"hl\">where they meet the service</span>.",
    sources=["Betsy Beyer et al., <i>Site Reliability Engineering</i> (2016): chapter 4, service level objectives.",
             "Betsy Beyer et al., <i>The Site Reliability Workbook</i> (2018): chapter 2, implementing SLOs.",
             "AXELOS, <i>ITIL 4: Service level management</i> practice guide (2020)."],
)

# ------------------------------------------------------------------ 02 How Good Is Good Enough?
so_problem = Doodle(760, 250, "Doodle of the first answer to 'what target should checkout have?', in July 2027. Priya says 100 percent. Femke remembers Christmas and says 99.99. Ben says the SLI was 99.86 last month and asks what it would cost to get to 99.99. Nobody has said what customers would actually notice, or what the business would give up to get there.",
                    "Priya: 100 %. Femke: 99.99 %. Last month: 99.86 %. Nobody asked what customers notice, or what it costs.")
so_problem.row([("Priya", "100 %", "pink"), ("Femke", "99.99 %", "pink"), ("June actual", "99.86 %", "paper")], y=30, h=100, gap=20, size=20, subsize=20)
so_problem.note(380, 180, "100 % means no changes, ever", "red", size=18)
so_problem.note(380, 216, "99.99 % ≈ 4 minutes a month, and a second region", "pen", size=17)

so_analogy = Doodle(760, 220, "Doodle of a pizza place promising delivery within 30 minutes. It could promise 20, but then it would need twice the drivers and still miss sometimes. It chose a promise customers are happy with and it can keep almost always, and it checks every month.",
                    "Promise 30 minutes, not 20: what customers are happy with, and what you can keep.")
so_analogy.icon("truck", 60, 50, 1.3)
so_analogy.box(170, 40, 270, 100, "20 minutes", "pink", sub="twice the drivers, still missed", size=18, subsize=13)
so_analogy.box(470, 40, 276, 100, "30 minutes", "green", sub="customers happy · kept 97 %", size=18, subsize=13)
so_analogy.note(450, 190, "good enough is a choice, and it has a price", "pen", size=18)

so_how = Doodle(760, 400, "Larder's service level objectives, agreed on Monday 2 August 2027 with Femke, Priya, Joost and Mo, over a rolling 28 days. Checkout success 99.9 percent (about 40 minutes' worth of failures a month). Checkout speed 95 percent under 800 milliseconds. Business ordering 99.9 percent, higher than the 99.8 Ruben will be offered. Dispatch 99 percent assigned within 90 seconds. Store sync 99.5 percent fresh. Each target sits just above what customers notice, not at 100. Reviewed every quarter; raising one requires saying what it costs.",
                "Five SLOs over 28 days, chosen with the business, each below 100 % on purpose, reviewed quarterly.")
rows = [("checkout success", "99.9 %", "≈ 40 min of failures / 28 days"), ("checkout speed", "95 %", "under 800 ms"),
        ("business ordering", "99.9 %", "SLA offered: 99.8 %"), ("Dispatch", "99 %", "assigned within 90 s"), ("store sync", "99.5 %", "stock < 2 min old")]
for i, (n, t, d) in enumerate(rows):
    y = 14 + i * 62
    so_how.box(14, y, 220, 52, n, "blue", size=15)
    so_how.box(244, y, 130, 52, t, "green", size=18)
    so_how.box(384, y, 362, 52, d, "paper", size=13)
so_how.note(380, 348, "agreed Mon 2 Aug with Femke, Priya, Joost, Mo · reviewed quarterly", "pen", size=15)
so_how.note(380, 382, "raising a target means saying what it costs", "red", size=16)

SLOS = dict(
    slug="slos",
    kicker="a.k.a. “service level objectives”",
    tldr="A <b>service level objective (SLO)</b> is a target for an SLI over a time window: “99.9 % of checkouts succeed over 28 days”. It's set <b>with the business</b>, <b>just above what customers notice</b>, and <b>never 100 %</b>, because 100 % means never changing anything and still failing. Every extra nine costs a lot more than the last, so raising a target means saying what it costs. Review SLOs <b>every quarter</b>.",
    chips=[("Family", "making promises"), ("Lives in", "ops/slo/&lt;service&gt;.yml, signed off by the business"), ("Pairs with", "SLIs, error budgets, SLAs")],
    itil=dict(groups=["service"], chain=["plan", "engage"], practices=["service level management"],
              sre="“SLO”: a target for an SLI over a window; 100 % is the wrong target", principles=["Focus on value", "Collaborate and promote visibility"],
              older="ITIL v3: service level targets in a service level agreement"),
    problem_side="Larder, July 2027",
    problem="""  <p class="lead">With SLIs in place, Eli asks what the target for checkout should be. <b>Priya</b> says 100 %. <b>Femke</b>, remembering Christmas, says 99.99 %. <b>Ben</b> points out that June was <b>99.86 %</b> and asks what 99.99 would cost: Ana's options page from January said a second region, about €9,000 a month and two engineers. <span class="hl-pink">Nobody has said what customers would actually notice, or what the business would give up to get there.</span></p>
  <ul>
    <li>100 % sounds right and means no changes, ever.</li>
    <li>Each extra nine costs much more than the last.</li>
    <li>A target nobody chose with the business becomes an engineering wish.</li>
  </ul>""",
    problem_figs=[so_problem],
    analogy_side="the pizza place's 30 minutes",
    analogy="""  <p>A pizza place could promise delivery in <b>20 minutes</b>, but it would need twice the drivers and would still miss sometimes. It promises <b>30 minutes</b>: customers are happy with that, and the shop keeps it almost every time. It checks the share every month, and if customers start leaving for a faster rival, it rethinks. <b>Good enough is a choice, and it has a price.</b></p>""",
    analogy_figs=[so_analogy],
    map=[("30 minutes", "99.9 % of checkouts succeed over 28 days"),
         ("What customers are happy with", "Just above what they notice"),
         ("Twice the drivers for 20 minutes", "A second region for 99.99 %"),
         ("Checking the share monthly", "SLO status on the monthly service review"),
         ("Rethinking if customers leave", "Quarterly review with the business")],
    how_side="targets just above what customers notice, chosen with the business",
    how="""  <p>On <b>Monday 2 August</b> Eli meets Femke, Priya, Joost and Mo with one page per service: the SLI, last six months' values, what customers notice (from Sam's tickets and Grace's numbers), and what each extra nine would cost. They agree <b>five SLOs</b> over a <b>rolling 28 days</b>:</p>
  <ul>
    <li><b>Checkout success 99.9 %</b>: about 40 minutes' worth of failures a month. Customers barely notice below that, and they do notice above.</li>
    <li><b>Checkout speed 95 % under 800 ms.</b></li>
    <li><b>Business ordering 99.9 %</b>, deliberately higher than the <b>99.8 %</b> Mo will offer Ruben in the contract.</li>
    <li><b>Dispatch 99 %</b> assigned within 90 seconds, and <b>store sync 99.5 %</b> fresh.</li>
  </ul>
  <p>None is 100 %. Raising a target later requires saying <b>what it costs</b>, in money, people and slower change. They're reviewed every quarter, the first time in November.</p>""",
    how_figs=[so_how],
    steps=[("Show the SLI's history", "Six months of values."),
           ("Find what customers notice", "Tickets, complaints, churn around bad days."),
           ("Price each extra nine", "Money, people, slower change."),
           ("Agree the target with the business", "Owners sign it."),
           ("Choose a window", "Rolling 28 days is common."),
           ("Review quarterly", "And when the business changes.")],
    vocab=[("SLO (service level objective)", "A target value for an SLI over a time window."),
           ("Nines", "99.9 % is three nines; each extra nine is ten times stricter."),
           ("Rolling window", "The last 28 days, recalculated every day."),
           ("Aspirational SLO", "A target you aim for but don't yet promise or enforce."),
           ("Over-reliability", "Being more reliable than users need, at a cost to speed of change."),
           ("Target vs promise", "An SLO is internal; an SLA is a promise with consequences.")],
    code=dict(file="ops/slo/README.md", note="agreed Mon 2 August 2027 · window: rolling 28 days", plain=True, src="""
service            SLI                         SLO      signed by       allowed failure / 28 days
checkout           success                     99.9 %   Femke, Priya    ≈ 40 min of failed checkouts
checkout           speed (< 800 ms)            95 %     Priya           5 % slower than 800 ms
business ordering  success (portal + API)      99.9 %   Femke, Mo       (SLA offered: 99.8 %)
Dispatch           assigned < 90 s             99 %     Joost           1 % assigned later
store sync         fresh (< 2 min)             99.5 %   Joost           ≈ 3.5 h of stale store-minutes
                                                                        per store
review   quarterly (first: Nov 2027) · raising a target = saying what it costs
never    100 %
"""),
    tools="tools: the SLI history, a cost page per extra nine (Ana's options page helps), and an hour with the business.",
    ladder=[("“as reliable as possible”", ["100 % or nothing.", "No agreed target."]),
            ("SLOs agreed with the business", ["Below 100 %, priced.", "Reviewed quarterly."]),
            ("SLOs drive alerts", ["Paging from budget burn (next note).", "Status shown live."]),
            ("SLOs drive planning", ["Reliability work prioritised by SLO risk.", "New services launch with SLOs."])],
    ladder_now=1,
    baseline="Each line compares <b>“100 %” or “99.99 %” as wishes</b> to <b>five SLOs chosen with the business, just above what customers notice</b>.",
    ratings=[(2, 4, "Targets set at what customers notice."),
             (3, 3, "Neutral on its own."),
             (3, 3, "Neutral."),
             (2, 3, "A target below 100 % leaves room to change."),
             (2, 4, "Everyone knows what “good enough” is."),
             (3, 3, "Neutral."),
             (2, 4, "No second region bought for a number nobody needed."),
             (3, 3, "Neutral."),
             (3, 3, "One meeting, then quarterly.")],
    pitfalls=[("100 % as a target", "No change is ever safe enough.", "just above what customers notice."),
              ("Engineers choose alone", "A target the business doesn't own.", "agree it with the business, signed."),
              ("No price per nine", "Raising targets looks free.", "say what each nine costs."),
              ("Never reviewing", "The target outlives the business it served.", "quarterly.")],
    use=["You have SLIs and someone asks “is that good?”", "A client wants a promise.", "Leaders ask for “four nines”.", "Teams disagree about how much reliability work is enough."],
    skip=["Services with no real users: no target needed."],
    related=["<b>What Do Users Count as Working?</b> (this volume)", "<b>When Do We Stop Shipping Features?</b> (next note)", "<b>Explaining Trade-offs to Non-Engineers</b> (Ana, vol. 3)", "<b>Availability Maths</b> (Ana, vol. 5)"],
    quiz=[("What is an SLO?", "A target for an SLI over a time window, like 99.9 % of checkouts succeeding over 28 days."),
          ("Why never 100 %?", "It means no changes are ever safe enough, and it still can't be met."),
          ("Why is the business ordering SLO (99.9 %) higher than the SLA (99.8 %)?", "So Larder notices and acts before a contract promise is at risk."),
          ("Who signs the SLOs?", "The business owners: Femke, Priya, Joost, Mo, per service."),
          ("What must accompany a request to raise a target?", "What it costs: money, people and slower change.")],
    quiz_sit=[("After a bad week, Femke asks to raise checkout to 99.99 %. What do you bring to the conversation?", "What 99.99 % means (≈ 4 minutes a month), what customers noticed in the bad week, and the cost (Ana's second-region numbers or cheaper options). Then she decides with the price in front of her.")],
    try_it="For one service, put six months of its SLI on one page with what customers noticed and what one extra nine would cost. Propose a target and ask a business owner to agree or change it.",
    remember="Good enough is a <span class=\"hl\">choice with a price</span>. Set it with the business, just above what customers notice, and <span class=\"hl\">never at 100 %</span>.",
    sources=["Betsy Beyer et al., <i>Site Reliability Engineering</i> (2016): chapter 3, embracing risk; chapter 4, SLOs.",
             "Alex Hidalgo, <i>Implementing Service Level Objectives</i> (O'Reilly, 2020).",
             "AXELOS, <i>ITIL 4: Service level management</i> practice guide (2020)."],
)

# ------------------------------------------------------------------ 03 When Do We Stop Shipping Features?
eb_problem = Doodle(760, 260, "Doodle of September 2027. The business ordering SLO is 99.9 percent, but the 28-day value has slid to 99.86 percent: a slow API release here, a flaky portal deploy there, none of them an incident. Grace's team has three more portal features planned for the autumn. Eli thinks reliability should come first; Grace thinks the features are what Korenwolf is asking for. They have no agreed rule for who wins.",
                    "The SLO quietly missed, three features planned, and no rule for who wins.")
eb_problem.box(14, 30, 230, 100, "SLO 99.9 %", "green", sub="business ordering", size=19, subsize=14)
eb_problem.box(264, 30, 230, 100, "now 99.86 %", "pink", sub="28 days, no incident", size=19, subsize=14)
eb_problem.box(514, 30, 232, 100, "3 features", "y", sub="planned for the autumn", size=19, subsize=14)
eb_problem.note(380, 186, "Eli: reliability first · Grace: features first · rule: none", "red", size=17)

eb_analogy = Doodle(760, 220, "Doodle of a family's monthly budget for eating out. As long as there's money left in the envelope, they eat out when they like. When it's empty, they cook at home until next month, without arguing about it, because they agreed the rule in advance.",
                    "Money left in the envelope: eat out. Empty: cook at home until next month. Agreed in advance.")
eb_analogy.icon("envelope", 60, 50, 1.3)
eb_analogy.box(170, 40, 270, 100, "money left", "green", sub="eat out when you like", size=19, subsize=14)
eb_analogy.box(470, 40, 276, 100, "envelope empty", "pink", sub="cook at home until next month", size=19, subsize=13)
eb_analogy.note(450, 190, "the rule was agreed before anyone was hungry", "pen", size=18)

eb_how = Doodle(760, 400, "Larder's error budget policy, signed on Monday 13 September 2027 by Priya and Femke. The error budget is what the SLO allows to fail: for business ordering, 0.1 percent of requests over 28 days. More than half left: ship as normal. Less than a quarter left: high-risk changes need Eli's agreement and every release goes through a canary. Budget spent: feature releases for that service pause; the team works on reliability until the 28-day value is back above the SLO; exceptions only by Femke, written down. Burn-rate alerts: 2 percent of the month's budget in one hour pages on-call; 10 percent in six hours makes a ticket. In October business ordering spent its budget; the portal paused for 9 working days, the team fixed retries and a slow query, and the value went back to 99.93.",
                "Above half: ship. Below a quarter: care. Spent: features pause until it's back. Signed before anyone argued.")
eb_how.row([("> 50 % left", "ship as normal", "green"), ("< 25 % left", "high-risk needs Eli · canaries", "y"), ("spent", "features pause · reliability first", "pink")], y=14, h=110, gap=16, size=20, subsize=13)
eb_how.box(14, 150, 732, 64, "burn alerts: 2 % of budget in 1 h → page · 10 % in 6 h → ticket", "blue", size=15)
eb_how.box(14, 234, 732, 70, "Oct: business ordering spent its budget · portal paused 9 days · back to 99.93 %", "paper", size=15)
eb_how.note(380, 338, "signed Mon 13 Sep by Priya and Femke · exceptions by Femke, written", "pen", size=15)
eb_how.note(380, 372, "the budget isn't a punishment; it's permission to take risk", "red", size=16)

ERROR_BUDGETS = dict(
    slug="error-budgets",
    kicker="a.k.a. “error budget policy”",
    tldr="If the SLO is 99.9 %, the other <b>0.1 % is the error budget</b>: the unreliability you've agreed to accept. While there's budget left, ship features and take risks. When it's spent, a <b>policy written in advance</b> says what happens: features pause for that service, and the team works on reliability until it's back. <b>Burn-rate alerts</b> warn while there's still time. It turns “features or reliability?” from an argument into a rule both sides signed.",
    chips=[("Family", "making promises"), ("Lives in", "ops/slo/error-budget-policy.md, signed by Priya and Femke"), ("Pairs with", "SLOs, the monthly service review, change risk")],
    itil=dict(groups=["service", "general"], chain=["plan", "improve"], practices=["service level management", "continual improvement"],
              sre="“error budget” and an “error budget policy”; burn-rate alerting", principles=["Focus on value", "Collaborate and promote visibility"],
              older="(no ITIL v3 equivalent; closest: service improvement plans)"),
    problem_side="Larder, September 2027",
    problem="""  <p class="lead">The business ordering SLO is <b>99.9 %</b>, but the 28-day value has slid to <b>99.86 %</b>: a slow API release here, a flaky portal deploy there, none of them big enough to be an incident. Grace's team has <b>three more portal features</b> planned for the autumn. Eli thinks reliability should come first, with Korenwolf's renewal coming up. Grace thinks the features are what Korenwolf is asking for. <span class="hl-pink">They have no agreed rule for who wins.</span></p>
  <ul>
    <li>An SLO without consequences is just a number on a page.</li>
    <li>Reliability work loses to features, until there's an incident.</li>
    <li>The decision ends up with whoever argues hardest.</li>
  </ul>""",
    problem_figs=[eb_problem],
    analogy_side="the eating-out envelope",
    analogy="""  <p>A family keeps a monthly <b>envelope for eating out</b>. While there's money in it, they eat out when they like, no questions. When it's empty, they <b>cook at home until next month</b>. Nobody argues about it, because the rule was agreed <b>before anyone was hungry</b>.</p>""",
    analogy_figs=[eb_analogy],
    map=[("The money in the envelope", "The error budget: 0.1 % of requests over 28 days"),
         ("Eating out", "Shipping features, taking risks"),
         ("Envelope empty", "Budget spent"),
         ("Cook at home until next month", "Feature releases pause; reliability work first"),
         ("Agreed before anyone was hungry", "Policy signed by Priya and Femke, 13 September")],
    how_side="a budget, a signed policy, and alerts while there's time",
    how="""  <p>Eli drafts the <b>error budget policy</b> with Grace, and <b>Priya and Femke sign it on Monday 13 September</b>. It applies per service:</p>
  <ul>
    <li><b>More than half the budget left</b>: ship as normal.</li>
    <li><b>Less than a quarter left</b>: high-risk changes need Eli's agreement, and every release goes through a canary.</li>
    <li><b>Budget spent</b>: <b>feature releases for that service pause</b>, and the team works on reliability until the 28-day value is back above the SLO. Exceptions are made only by Femke, in writing.</li>
  </ul>
  <p><b>Burn-rate alerts</b> come with it. Spending <b>2 %</b> of the month's budget in one hour pages on-call; <b>10 %</b> in six hours makes a ticket. Most of the old threshold alerts are retired.</p>
  <p>In <b>October</b> business ordering spends its budget. The portal pauses for <b>9 working days</b>. Ben's team fixes the API's retries and a slow query, and the value goes back to <b>99.93 %</b>. Grace ships the next portal feature afterwards, and tells Mo the pause was the reason Korenwolf's mornings got calmer. Nobody had to argue.</p>""",
    how_figs=[eb_how],
    steps=[("Compute the budget from the SLO", "100 % − SLO, over the window."),
           ("Write what happens at each level", "Plenty, low, spent."),
           ("Have the business sign it", "Product and the CEO, before the first fight."),
           ("Alert on burn rate", "Fast burn pages; slow burn makes a ticket."),
           ("Apply it when it hurts", "That's when it matters."),
           ("Review it with the SLOs", "Quarterly.")],
    vocab=[("Error budget", "The amount of failure an SLO allows over its window."),
           ("Error budget policy", "Written, signed rules for what happens as the budget is used up."),
           ("Burn rate", "How fast the budget is being spent, relative to the window."),
           ("Fast burn / slow burn", "A sudden big spend (page) vs a steady leak (ticket)."),
           ("Feature freeze", "Pausing feature releases for a service while reliability recovers."),
           ("Budget exception", "A documented decision to ship anyway, by a named leader.")],
    code=dict(file="ops/slo/error-budget-policy.md", note="signed Mon 13 September 2027 · Priya, Femke", plain=True, src="""
# Error budget policy (per service, rolling 28 days)

budget        100 % − SLO   e.g. business ordering: 0.1 % of requests
> 50 % left   ship as normal
< 25 % left   high-risk changes need Eli's agreement · every release via a canary
spent         feature releases for this service PAUSE
              team works on the top reliability items until the 28-day value
              is back above the SLO
exceptions    Femke only, in writing, in the change feed
alerts        2 % of budget in 1 h → page · 10 % in 6 h → ticket

Oct 2027      business ordering spent → portal paused 9 working days
              → API retries + one slow query fixed → 99.93 % · feature work resumed
"""),
    tools="tools: the SLI data, a budget calculation per service, burn-rate alerts in the monitoring tool, and a signed page.",
    ladder=[("features vs reliability by argument", ["Whoever argues hardest wins.", "Reliability waits for incidents."]),
            ("a signed policy and burn alerts", ["Three levels, a pause when spent.", "Exceptions by name."]),
            ("budget in planning", ["Each team sees its budget weekly.", "Risky work planned when budget is high."]),
            ("budget as permission", ["Teams spend it on purpose: experiments, migrations.", "Rarely spent by accident."])],
    ladder_now=1,
    baseline="Each line compares <b>arguing features vs reliability</b> to <b>an error budget with a signed policy and burn-rate alerts</b>.",
    ratings=[(2, 4, "Korenwolf's mornings calmer after the pause."),
             (2, 4, "Reliability work happens before incidents."),
             (3, 3, "Neutral."),
             (2, 3, "Risky changes need agreement when the budget is low."),
             (2, 4, "Everyone sees how much budget is left."),
             (3, 3, "Neutral."),
             (2, 3, "Reliability effort goes where the budget says."),
             (2, 3, "Burn alerts replace noisy thresholds."),
             (3, 3, "One signed page.")],
    pitfalls=[("A policy nobody signed", "Ignored the first time it costs a feature.", "product and the CEO sign it."),
              ("Budget as punishment", "Teams hide failures.", "it's permission to take risk, not a scorecard."),
              ("Exceptions by habit", "Every pause gets overruled.", "Femke only, in writing, visible."),
              ("Alerting on thresholds still", "Pages for blips that don't touch the budget.", "burn-rate alerts.")],
    use=["Features and reliability compete for the same team.", "An SLO is being missed without consequences.", "You want fewer, better pages.", "Before a contract promise depends on a service."],
    skip=["Services without SLOs: set those first."],
    related=["<b>How Good Is Good Enough?</b> (this volume)", "<b>SLOs & Error Budgets</b> (cloud, vol. 6)", "<b>Disagree and Commit</b> (Grace, vol. 5)", "<b>Which Alerts Deserve a Human?</b> (vol. 1)"],
    quiz=[("What is an error budget?", "The amount of failure the SLO allows over its window (100 % − SLO)."),
          ("What happens when the budget is spent?", "Feature releases for that service pause; the team works on reliability until it's back above the SLO."),
          ("Who can make an exception?", "Only Femke, in writing."),
          ("What are Larder's burn-rate alerts?", "2 % of the budget in one hour pages; 10 % in six hours makes a ticket."),
          ("What happened in October?", "Business ordering spent its budget; the portal paused 9 working days; fixes brought it back to 99.93 %.")],
    quiz_sit=[("The checkout budget is spent with two days of the window left, and marketing has a campaign feature due tomorrow. What happens?", "The policy says features pause. Marketing can ask Femke for a written exception; she decides with the budget status in front of her. Otherwise the feature waits until checkout is back above its SLO.")],
    try_it="For one service with an SLO, compute its error budget and how much of it you've used this month. Write three sentences: what happens with plenty left, with little left, and when it's spent. Ask your product owner to sign them.",
    remember="The budget is <span class=\"hl\">permission to take risk</span>. When it's spent, features wait, and the rule was <span class=\"hl\">agreed before anyone was hungry</span>.",
    sources=["Betsy Beyer et al., <i>The Site Reliability Workbook</i> (2018): chapter 2 and appendix B, an example error budget policy.",
             "Betsy Beyer et al., <i>The Site Reliability Workbook</i> (2018): chapter 5, alerting on SLOs (burn rates).",
             "Alex Hidalgo, <i>Implementing Service Level Objectives</i> (2020)."],
)

# ------------------------------------------------------------------ 04 What Did We Sign?
sa_problem = Doodle(760, 260, "Doodle of Ruben's first draft for the Korenwolf renewal, October 2027: 'Larder guarantees 99.9 percent availability of ordering.' It doesn't say what ordering means, how it's measured, over what period, what counts as down, whether announced maintenance counts, or what happens if it's missed. And 99.9 percent is exactly Larder's own internal target, with no room between them.",
                    "“99.9 % availability of ordering.” No definition, no measurement, no consequence, and no room below the SLO.")
sa_problem.box(14, 30, 732, 70, "“Larder guarantees 99.9 % availability of ordering.”", "y", size=18)
for i, q in enumerate(["what is ordering?", "measured how?", "per month?", "what if missed?"]):
    sa_problem.box(14 + i * 186, 120, 172, 60, q, "pink", size=15)
sa_problem.note(380, 222, "and 99.9 % = Larder's own SLO: no room between promise and target", "red", size=16)

sa_analogy = Doodle(760, 220, "Doodle of a parcel company's guarantee: delivered by 12:00 the next working day, measured by the time of the delivery scan, for parcels handed in before 18:00; if late, the shipping fee is refunded. Its own internal target is 11:00, so it has room before it owes anyone money.",
                    "“By 12:00, by the scan, if handed in before 18:00; late = fee back.” The internal target is 11:00.")
sa_analogy.icon("parcel", 60, 50, 1.3)
sa_analogy.box(170, 30, 576, 120, None, "paper")
for i, t in enumerate(["promise: by 12:00 next working day", "measured: the delivery scan · handed in before 18:00", "if missed: the fee back · internal target: 11:00"]):
    sa_analogy.text(190, 64 + i * 32, t, anchor="start", size=16)
sa_analogy.note(450, 190, "precise, measurable, with a consequence, and a buffer", "pen", size=18)

sa_how = Doodle(760, 400, "The service levels in Korenwolf's renewal, agreed by Mo, Eli and Lena with Ruben in November 2027 and signed in December. Ordering availability 99.8 percent per calendar month: the portal and the business API, counted per minute; a minute is down if more than 5 percent of requests fail, measured by Larder's outside checks every minute plus real requests. Announced maintenance doesn't count if announced 5 working days ahead and outside 06:00 to 20:00. If missed: a 5 percent credit on that month's service fee; under 99.5 percent, 10 percent. Delivery: 98 percent of deliveries complete by 09:00, as in 2026, with 10 percent of a missed delivery credited automatically. Reported automatically every month in the portal. Internal SLO 99.9 percent, so there's room. A joint goal of 99.9 percent for 2028, not a promise.",
                "Precise definitions, a monthly report, credits, and room: SLA 99.8 % under an SLO of 99.9 %.")
sa_how.box(14, 14, 360, 160, None, "blue")
sa_how.head(194, 44, "ordering availability", size=17)
sa_how.text(194, 76, "99.8 % per calendar month", size=16)
sa_how.text(194, 104, "down minute: > 5 % requests fail", size=13)
sa_how.text(194, 128, "outside checks + real requests", size=13)
sa_how.text(194, 152, "announced maintenance excluded", size=13)
sa_how.box(386, 14, 360, 160, None, "green")
sa_how.head(566, 44, "deliveries", size=17)
sa_how.text(566, 76, "98 % complete by 09:00", size=16)
sa_how.text(566, 104, "10 % of a missed one credited", size=13)
sa_how.text(566, 128, "automatically, in the portal", size=13)
sa_how.box(14, 196, 732, 60, "missed: 5 % credit on the month's fee · below 99.5 %: 10 %", "pink", size=15)
sa_how.box(14, 270, 732, 60, "internal SLO 99.9 % > SLA 99.8 % · joint goal 99.9 % for 2028 (not a promise)", "y", size=15)
sa_how.note(380, 366, "monthly report from the portal · nobody computes it by hand", "pen", size=15)

SLAS = dict(
    slug="slas",
    kicker="a.k.a. “service level agreements”",
    tldr="A <b>service level agreement (SLA)</b> is a promise to a customer with <b>consequences</b> if it's missed. It needs a precise definition: <b>what's covered, how it's measured, over what period, what counts as down, what's excluded, and what happens</b> if it's missed. Keep it <b>looser than your internal SLO</b>, so you notice and act before you owe anything, and <b>report it automatically</b> from the same data you run on.",
    chips=[("Family", "making promises"), ("Lives in", "the Korenwolf contract, schedule 2; the portal's monthly report"), ("Pairs with", "SLOs, OLAs, telling a business client (vol. 2)")],
    itil=dict(groups=["service", "general"], chain=["engage", "plan"], practices=["service level management", "relationship management", "supplier management (from the client's side)"],
              sre="“SLA”: SLOs with consequences; set SLAs looser than SLOs", principles=["Focus on value", "Collaborate and promote visibility"],
              older="ITIL v3: the service level agreement"),
    problem_side="Larder, October 2027",
    problem="""  <p class="lead">For the Korenwolf renewal, Ruben's first draft says: <b>“Larder guarantees 99.9 % availability of ordering.”</b> It doesn't say what “ordering” means, how it's measured, over what period, what counts as down, whether announced maintenance counts, or what happens if it's missed. <span class="hl-pink">And 99.9 % is exactly Larder's own internal target, with no room between the promise and the target.</span></p>
  <ul>
    <li>A vague SLA becomes an argument every time something goes wrong.</li>
    <li>An SLA equal to the SLO means owing money the moment the target slips.</li>
    <li>A report computed by hand each month is slow, and easy to dispute.</li>
  </ul>""",
    problem_figs=[sa_problem],
    analogy_side="the parcel company's guarantee",
    analogy="""  <p>A parcel company guarantees <b>delivery by 12:00 the next working day</b>, measured by the time of the delivery scan, for parcels handed in before 18:00. If it's late, <b>the shipping fee comes back</b>. Its own internal target is <b>11:00</b>, so it has room before it owes anyone money. Every word in the guarantee is there to stop an argument later.</p>""",
    analogy_figs=[sa_analogy],
    map=[("By 12:00 next working day", "99.8 % ordering availability per calendar month"),
         ("Measured by the delivery scan", "Outside checks every minute plus real requests"),
         ("Handed in before 18:00", "Announced maintenance excluded (5 days' notice, outside 06–20)"),
         ("The fee back", "A 5 % credit, 10 % below 99.5 %"),
         ("The internal 11:00 target", "The internal SLO of 99.9 %")],
    how_side="precise words, a buffer below the SLO, and an automatic report",
    how="""  <p>Mo, Eli and Lena rewrite the service levels with Ruben in <b>November</b>. They're signed with the renewal in <b>December</b>:</p>
  <ul>
    <li><b>Ordering availability: 99.8 % per calendar month.</b> Covers the portal and the business API, counted <b>per minute</b>. A minute is down if <b>more than 5 % of requests fail</b>, measured by Larder's outside checks every minute plus real requests. Maintenance announced <b>5 working days</b> ahead and outside 06:00–20:00 doesn't count.</li>
    <li><b>If missed</b>: a <b>5 %</b> credit on that month's service fee; below 99.5 %, <b>10 %</b>.</li>
    <li><b>Deliveries</b>: as in 2026, <b>98 % complete by 09:00</b>, with <b>10 % of a missed delivery credited</b> automatically.</li>
    <li><b>Reported automatically</b> every month in the portal (Grace's service levels, live since 4 October), from the same data Larder uses for its SLOs.</li>
  </ul>
  <p>The internal SLO stays at <b>99.9 %</b>, so the error budget policy kicks in long before a credit is owed. Ruben still wanted 99.9 %. It became a <b>joint goal for 2028</b>: worked on together, not promised. Ana's availability work (measured 99.81 % on the business path in November) shows the 99.8 % is safe to sign.</p>""",
    how_figs=[sa_how],
    steps=[("Define what's covered", "Which services, which users."),
           ("Define how it's measured", "Which data, how often, what's a down minute."),
           ("Set the period and the exclusions", "Calendar month; announced maintenance."),
           ("Agree the consequences", "Credits, simple and capped."),
           ("Keep it below your SLO", "Room to act before you owe."),
           ("Report it automatically", "From the data you run on.")],
    vocab=[("SLA (service level agreement)", "A promise to a customer about service levels, with consequences."),
           ("Service credit", "Money back (or off the next invoice) when an SLA is missed."),
           ("Exclusion", "Something agreed not to count, such as announced maintenance."),
           ("Measurement period", "The window an SLA is judged over: a calendar month here."),
           ("Buffer", "The room between the internal SLO and the external SLA."),
           ("Joint goal", "A shared aim worked on together, without contractual consequences.")],
    code=dict(file="contracts/korenwolf-2028/schedule-2-service-levels.md", note="signed December 2027 · Mo, Lena, Ruben", plain=True, src="""
2.1 Ordering availability     ≥ 99.8 % per calendar month
    covered     business portal + business API (/business/v1, /v2)
    down minute > 5 % of requests fail, by Larder's outside checks (every 60 s,
                two locations) and real requests; whichever is worse
    excluded    maintenance announced ≥ 5 working days ahead, outside 06:00–20:00
    credit      < 99.8 %: 5 % of the month's service fee · < 99.5 %: 10 %
2.2 Deliveries                ≥ 98 % complete by 09:00 per month
    credit      10 % of each missed delivery, automatic
2.3 Reporting   monthly, in the portal, by the 3rd working day
2.4 Goal 2028   99.9 % ordering availability, a joint goal (not a commitment)
internal (not in the contract): SLO 99.9 % · error budget policy applies
"""),
    tools="tools: the SLI data, outside checks from two locations, the portal's automatic report, Lena for the wording.",
    ladder=[("a number in a sentence", ["Vague, disputed.", "Equal to the internal target."]),
            ("a precise SLA with a buffer", ["Definitions, exclusions, credits.", "Reported automatically."]),
            ("SLAs from a catalogue", ["Standard service levels per offer.", "Credits computed automatically."]),
            ("SLAs rarely tested", ["SLOs and budgets keep service well above the promise.", "Credits almost never paid."])],
    ladder_now=1,
    baseline="Each line compares <b>“99.9 % availability of ordering”</b> to <b>a precise 99.8 % SLA with exclusions, credits, an automatic report and a buffer below the SLO</b>.",
    ratings=[(3, 4, "The client knows exactly what's promised."),
             (3, 3, "Neutral on its own."),
             (3, 3, "Neutral."),
             (3, 3, "Neutral."),
             (2, 4, "Monthly report from the same data, in the portal."),
             (2, 4, "No hand-computed reports."),
             (2, 4, "A buffer before credits are owed."),
             (3, 3, "Neutral."),
             (3, 4, "Written once, reported automatically.")],
    pitfalls=[("SLA equal to SLO", "You owe money whenever the target slips.", "keep the SLA looser."),
              ("No definition of down", "Every incident becomes a dispute.", "a down minute, precisely."),
              ("Hand-made reports", "Slow and easy to argue with.", "automatic, from the same data."),
              ("Promising the stretch goal", "Today's hope becomes tomorrow's penalty.", "a joint goal, not a commitment.")],
    use=["A client asks for guarantees.", "A renewal or a new contract.", "Disputes about whether something was “down”.", "Before promising a number in a sales deck."],
    skip=["Consumers who use the app without a contract: SLOs are enough."],
    related=["<b>How Good Is Good Enough?</b> (this volume)", "<b>What Do Teams Promise Each Other?</b> (next note)", "<b>Service Levels as Features</b> (Grace, vol. 6)", "<b>Availability Maths</b> (Ana, vol. 5)"],
    quiz=[("What must an SLA define?", "What's covered, how it's measured, the period, what counts as down, exclusions, and consequences."),
          ("Why is Larder's SLA 99.8 % when the SLO is 99.9 %?", "To leave room: Larder notices and acts on its error budget before owing credits."),
          ("What counts as a down minute in Korenwolf's SLA?", "A minute in which more than 5 % of portal and API requests fail, by outside checks and real requests."),
          ("What happens if the SLA is missed?", "A 5 % credit on the month's fee; 10 % below 99.5 %."),
          ("What happened to Ruben's 99.9 %?", "It became a joint goal for 2028, not a contractual promise.")],
    quiz_sit=[("A sales colleague wants to offer a new office client “99.95 % availability” to win the deal. What do you say?", "Larder's SLO is 99.9 %, so promising more means owing credits often. Offer the standard 99.8 % with precise definitions, and a joint goal if they want ambition, or price the extra reliability honestly.")],
    try_it="Find a promise your team has made to a customer (in a contract, a sales deck or an email). Rewrite it with what's covered, how it's measured, the period, what's down, exclusions and consequences. Is it looser than your internal target?",
    remember="An SLA is a promise <span class=\"hl\">with consequences</span>: define every word, report it automatically, and keep it <span class=\"hl\">looser than your SLO</span>.",
    sources=["AXELOS, <i>ITIL 4: Service level management</i> practice guide (2020).",
             "Betsy Beyer et al., <i>Site Reliability Engineering</i> (2016): chapter 4, SLAs vs SLOs.",
             "Alex Hidalgo, <i>Implementing Service Level Objectives</i> (2020): SLAs."],
)

# ------------------------------------------------------------------ 05 What Do Teams Promise Each Other?
ol_problem = Doodle(760, 260, "Doodle of the chain behind Korenwolf's 99.8 percent, drawn by Eli in November 2027. The business portal and API (Ben's team) depend on the database and its failover (platform: Eli and Bram), on billing (a vendor, owned by Cho), on single sign-on (Eli), and on stores picking business orders the evening before (Joost's operations). The SLA is a promise from Larder, but each link is a different team, and none of them has promised anything to the others.",
                    "Larder promised Korenwolf 99.8 %. Inside, five teams hold the links, and none has promised anything to the others.")
ol_problem.box(260, 14, 240, 60, "Korenwolf SLA 99.8 %", "green", size=16)
for i, (t, s) in enumerate([("portal + API", "Ben"), ("database", "Eli, Bram"), ("billing", "Cho + vendor"), ("SSO", "Eli"), ("evening picks", "Joost")]):
    ol_problem.box(14 + i * 148, 120, 136, 80, t, "y", sub=s, size=15, subsize=13)
    ol_problem.arrow(380, 76, 82 + i * 148, 118, dash=True)
ol_problem.note(380, 240, "no internal promises behind the external one", "red", size=18)

ol_analogy = Doodle(760, 220, "Doodle of a wedding caterer promising a dinner at 19:00. Behind the promise: the kitchen promises plates at the pass by 18:50; the bakery promises the cake by 15:00; the drinks supplier promises delivery by 14:00. If any of those slip, the caterer knows early, because each was a promise, not a hope.",
                    "Dinner at 19:00 rests on plates by 18:50, cake by 15:00, drinks by 14:00: promises, not hopes.")
ol_analogy.box(14, 40, 200, 100, "dinner 19:00", "green", sub="to the couple", size=18, subsize=14)
for i, (t, s) in enumerate([("kitchen", "plates 18:50"), ("bakery", "cake 15:00"), ("drinks", "delivery 14:00")]):
    ol_analogy.box(260 + i * 166, 40, 152, 100, t, "y", sub=s, size=18, subsize=14)
ol_analogy.note(380, 190, "the outside promise rests on the inside ones", "pen", size=18)

ol_how = Doodle(760, 400, "Larder's operational level agreements, written in November 2027, six of them, one page each. Platform to ordering: database failover under 2 minutes, tested monthly; backups restorable within 1 hour. Ordering to business: portal and API changes never in the 07:00 to 09:00 window. Payments (Cho) to business: billing vendor silence detected within 15 minutes, invoices regenerated within one working day. Identity (Eli): SSO for office managers 99.9 percent. Operations (Joost): business orders picked the evening before, by 22:00. Support (Sam): business tickets answered within 30 minutes in office hours. Each OLA has an internal measure and is on the monthly service review. Vendor contracts are the outer ring: underpinning contracts.",
                "Six one-page internal promises, each measured, behind the one external promise.")
items = [("platform → ordering", "failover < 2 min · restore < 1 h"), ("ordering → business", "no changes 07–09"),
         ("payments → business", "billing silence found < 15 min"), ("identity", "office SSO 99.9 %"),
         ("operations", "business orders picked by 22:00"), ("support", "business tickets < 30 min")]
for i, (t, s) in enumerate(items):
    r, c = divmod(i, 2)
    ol_how.box(14 + c * 372, 14 + r * 86, 360, 74, t, "y", sub=s, size=16, subsize=13)
ol_how.box(14, 278, 732, 56, "vendors (underpinning contracts): billing SaaS · PSP · cloud · WMS B", "paper", size=14)
ol_how.note(380, 370, "every OLA has an internal measure, on the monthly service review", "pen", size=15)

OLAS = dict(
    slug="olas",
    kicker="a.k.a. “operational level agreements”",
    tldr="An external promise (an SLA) is only as strong as the internal links behind it. <b>Operational level agreements (OLAs)</b> are the <b>promises teams make to each other</b> so the external one can be kept: the platform promises failover in under two minutes, payments promises to notice a silent billing vendor within fifteen. Keep them short, <b>measurable</b>, owned, and reviewed alongside the SLA. Vendor contracts that support them are the outer ring: <b>underpinning contracts</b>.",
    chips=[("Family", "making promises"), ("Lives in", "ops/ola/*.md, one page each"), ("Pairs with", "SLAs, the dependency map (vol. 1), vendor management")],
    itil=dict(groups=["service", "general"], chain=["plan", "engage"], practices=["service level management", "supplier management"],
              sre="(internal SLOs between services)", principles=["Think and work holistically", "Collaborate and promote visibility"],
              older="ITIL v3: operational level agreements, underpinning contracts"),
    problem_side="Larder, November 2027",
    problem="""  <p class="lead">With the Korenwolf SLA drafted, Eli draws the chain behind the <b>99.8 %</b>. The portal and API belong to Ben's team. They depend on the <b>database and its failover</b> (Eli and Bram), <b>billing</b> (a vendor, owned by Cho), <b>single sign-on</b> (Eli), and stores <b>picking business orders the evening before</b> (Joost's operations). <span class="hl-pink">Larder made one promise outside, and inside five teams hold the links. None of them has promised the others anything.</span></p>
  <ul>
    <li>A weak link is found when the SLA is missed, not before.</li>
    <li>Teams don't know what others rely on them for.</li>
    <li>Vendor contracts were signed without the SLA in mind.</li>
  </ul>""",
    problem_figs=[ol_problem],
    analogy_side="the wedding caterer's timings",
    analogy="""  <p>A wedding caterer promises the couple <b>dinner at 19:00</b>. Behind that: the kitchen promises <b>plates at the pass by 18:50</b>, the bakery <b>the cake by 15:00</b>, the drinks supplier <b>delivery by 14:00</b>. If any of those slip, the caterer knows early, because each one was a promise with a time, not a hope.</p>""",
    analogy_figs=[ol_analogy],
    map=[("Dinner at 19:00", "Korenwolf's 99.8 % SLA"),
         ("Plates at the pass by 18:50", "Platform: failover under 2 minutes"),
         ("Cake by 15:00", "Operations: business orders picked by 22:00"),
         ("Drinks by 14:00", "Vendors: underpinning contracts"),
         ("Knowing early", "OLA measures on the monthly service review")],
    how_side="one page per link, measurable, reviewed with the SLA",
    how="""  <p>In <b>November</b> Eli writes <b>six OLAs</b>, one page each, agreed with each team lead:</p>
  <ul>
    <li><b>Platform → ordering</b>: database failover under 2 minutes, tested monthly; backups restorable within 1 hour.</li>
    <li><b>Ordering → business</b>: no portal or API changes in the 07:00–09:00 window.</li>
    <li><b>Payments → business</b> (Cho): a silent billing vendor is detected within <b>15 minutes</b>; invoices are regenerated within one working day.</li>
    <li><b>Identity</b> (Eli): SSO for office managers at 99.9 %.</li>
    <li><b>Operations</b> (Joost): business orders picked the evening before, by 22:00 (ADR 0017).</li>
    <li><b>Support</b> (Sam): business tickets answered within 30 minutes in office hours.</li>
  </ul>
  <p>Each OLA has an <b>internal measure</b> that appears on the monthly service review. The vendors behind them (billing SaaS, PSP, cloud, WMS B) are the outer ring, the <b>underpinning contracts</b>. At the next renewal of each, the contract owner checks that the vendor's terms still support the OLA. The OLAs aren't legal documents. They're how one team learns what another relies on it for.</p>""",
    how_figs=[ol_how],
    steps=[("Draw the chain behind the SLA", "Every team and vendor it depends on."),
           ("Write one page per link", "What, measured how, owned by whom."),
           ("Agree it with the team lead", "Not imposed; negotiated."),
           ("Make it measurable", "A number on the monthly review."),
           ("Check vendor contracts against it", "Underpinning contracts at renewal."),
           ("Review OLAs with the SLA", "When the outside promise changes, so do the inside ones.")],
    vocab=[("OLA (operational level agreement)", "An internal agreement between teams that supports an external SLA."),
           ("Underpinning contract", "A contract with a vendor that supports an SLA or OLA."),
           ("Internal SLO", "A target one service sets for the services that use it."),
           ("Dependency chain", "The links an outside promise rests on."),
           ("Weakest link", "The link whose failure most often breaks the promise."),
           ("Service owner", "Accountable for a service and its promises (vol. 1).")],
    code=dict(file="ops/ola/payments-business.md", note="one of six · November 2027", plain=True, src="""
# OLA · payments → business ordering                     owner: Cho · agreed with Ben, Mo

Promise      Billing vendor silence (no webhook for 15 min in business hours,
             or poll finds missing events) is detected within 15 minutes.
             Invoices affected are regenerated within one working day.
Measured     silence alerts (from 6 Sep) · time to detect · invoices regenerated
Why          Korenwolf SLA 2.3 (monthly report) and trust: 31 Aug 2027,
             9 hours of silence showed Korenwolf as unpaid.
Depends on   billing SaaS (underpinning contract, renews Jun 2028: check terms)
Review       monthly service review · with the SLA every quarter
"""),
    tools="tools: the dependency map, a one-page template, and a line per OLA on the monthly service review.",
    ladder=[("an outside promise only", ["Weak links found by missing the SLA.", "Teams unaware."]),
            ("an OLA per link", ["Measurable, agreed, reviewed.", "Vendor terms checked."]),
            ("internal SLOs", ["Each service publishes SLOs for its users.", "Budgets between teams."]),
            ("promises composed", ["The SLA computed from the internal ones.", "Gaps visible before signing."])],
    ladder_now=1,
    baseline="Each line compares <b>an outside promise with no inside ones</b> to <b>six measurable OLAs behind the SLA</b>.",
    ratings=[(2, 3, "The outside promise rests on known links."),
             (2, 3, "Weak links fixed before they break the SLA."),
             (3, 3, "Neutral."),
             (2, 3, "No changes in the business window, by agreement."),
             (2, 4, "Teams see what others rely on them for."),
             (3, 3, "Neutral."),
             (3, 3, "Vendor terms checked at renewal."),
             (3, 3, "Neutral."),
             (3, 3, "Six pages.")],
    pitfalls=[("OLAs as legal documents", "Teams argue clauses instead of fixing things.", "one page, negotiated, practical."),
              ("Not measurable", "“Best effort” promises.", "a number on the monthly review."),
              ("Forgetting vendors", "The weakest link is outside the company.", "underpinning contracts checked at renewal."),
              ("Writing them once", "The SLA changes; the OLAs don't.", "review together.")],
    use=["You've signed an SLA.", "Several teams hold the links behind a promise.", "A miss came from a team or vendor nobody thought about.", "Teams don't know what others depend on them for."],
    skip=["One team owns everything behind a promise."],
    related=["<b>What Did We Sign?</b> (this volume)", "<b>What Is Connected to What?</b> (vol. 1)", "<b>The Vendor Went Quiet</b> (this volume)", "<b>Dependencies across Teams</b> (Grace, vol. 5)"],
    quiz=[("What is an OLA?", "An internal agreement between teams that supports an external SLA."),
          ("What is an underpinning contract?", "A vendor contract that supports an SLA or OLA."),
          ("Give one of Larder's six OLAs.", "E.g. platform → ordering: failover under 2 minutes, tested monthly; or payments: billing silence detected within 15 minutes."),
          ("How are OLAs kept honest?", "Each has a measure on the monthly service review."),
          ("Why aren't OLAs legal documents?", "Their job is to make dependencies visible and fixable, not to win arguments.")],
    quiz_sit=[("Joost's team can't always pick business orders by 22:00 on Sundays, because of staffing. What do you do with the OLA?", "Talk to Joost: change the OLA (e.g. by 06:00 on Mondays with a stock reservation) and check it still supports the SLA, rather than leave a promise nobody keeps.")],
    try_it="Take one promise you make to a customer. Draw every team and vendor it depends on. For the weakest link, write a one-page OLA: what, measured how, owned by whom.",
    remember="An outside promise is only as strong as <span class=\"hl\">the inside ones behind it</span>. One page per link, measured, and reviewed with the SLA.",
    sources=["AXELOS, <i>ITIL 4: Service level management</i> and <i>Supplier management</i> practice guides (2020).",
             "Betsy Beyer et al., <i>The Site Reliability Workbook</i> (2018): SLOs for dependencies.",
             "Matthew Skelton and Manuel Pais, <i>Team Topologies</i> (2019): team interaction modes."],
)

NOTES = [SLIS, SLOS, ERROR_BUDGETS, SLAS, OLAS]
