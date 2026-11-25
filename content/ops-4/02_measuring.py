# Series 2 · Book 5 · The IT Operations Notebook · Vol. 4 · Measuring honestly.
# Narrator: Eli (he/him). Facts: docs/larder-casebook.md, "Book 5, Vol. 4".

# ------------------------------------------------------------------ 06 How Available Were We, Really?
av_problem = Doodle(760, 260, "Doodle of three numbers for business ordering in October 2027, all called 'availability'. The servers' own logs: 99.95 percent. The request-success SLI: 99.86 percent. The outside checks counting down minutes, the way the new contract counts: 99.79 percent. Ruben will read the third. The difference: minutes when DNS or the content network failed outside Larder's servers, and minutes where a few percent of requests failed.",
                    "Three “availability” numbers for the same month: 99.95, 99.86, 99.79. The contract uses the lowest.")
av_problem.row([("server logs", "99.95 %", "green"), ("request SLI", "99.86 %", "y"), ("outside, per minute", "99.79 %", "pink")], y=30, h=110, gap=20, size=19, subsize=22)
av_problem.note(380, 190, "Ruben reads the third", "red", size=19)
av_problem.note(380, 226, "failures outside the servers never reach the server logs", "pen", size=16)

av_analogy = Doodle(760, 220, "Doodle of a shop measuring how often it was open. The shop's own clock says the door was unlocked from 08:00 to 18:00 every day. But on three mornings the road outside was closed, and customers couldn't get in. Asked how available the shop was, the honest answer counts the road too, because the customer's trip does.",
                    "The door was unlocked all day, but the road was closed for three mornings. Customers count the road.")
av_analogy.icon("store", 60, 40, 1.5)
av_analogy.box(170, 40, 270, 100, "door unlocked", "green", sub="100 %, by our clock", size=18, subsize=14)
av_analogy.box(470, 40, 276, 100, "road closed", "pink", sub="3 mornings, no customers", size=18, subsize=14)
av_analogy.note(450, 190, "measure the customer's trip, not the shop door", "pen", size=18)

av_how = Doodle(760, 400, "Larder's availability rules from November 2027. Two measurements: real requests at the load balancer, and outside checks every 60 seconds from two locations in different countries that log in and place a test business order. A minute counts as down if more than 5 percent of requests fail or both outside checks fail. Partial outages count by share in the SLI and as down minutes in the contract measure. Planned maintenance counts internally even when the contract excludes it. Both numbers are published side by side every month with an explanation of the gap. November: request SLI 99.92, contract minutes 99.81 percent, matching Ana's measurement.",
                "Real requests plus outside checks; precise rules for down minutes; both numbers published with the gap explained.")
av_how.box(14, 14, 360, 120, "real requests", "blue", sub="load balancer · good ÷ valid", size=19, subsize=13)
av_how.box(386, 14, 360, 120, "outside checks", "green", sub="every 60 s · 2 countries · test order", size=19, subsize=13)
av_how.box(14, 160, 732, 110, None, "paper")
av_how.text(380, 190, "down minute: > 5 % of requests fail, or both outside checks fail", size=15)
av_how.text(380, 218, "partial outage: by share (SLI) · as a down minute (contract)", size=15)
av_how.text(380, 246, "planned maintenance: always counted internally", size=15)
av_how.row([("Nov request SLI", "99.92 %", "y"), ("Nov contract minutes", "99.81 %", "green")], x=110, y=294, h=80, w=250, gap=40, size=17, subsize=20)

MEASURING_AVAILABILITY = dict(
    slug="measuring-availability",
    kicker="a.k.a. “availability management, measured”",
    tldr="“Availability” can mean very different numbers depending on <b>where and how you count</b>. Server logs miss failures outside your servers, request counts treat a slow minute differently from a dead one, and a contract may count whole minutes. Measure with <b>real requests and outside checks</b>, write precise rules for <b>partial outages and maintenance</b>, publish the numbers <b>side by side</b>, and explain the gap. The honest number is the one your customer would compute.",
    chips=[("Family", "measuring honestly"), ("Lives in", "ops/slo/availability.md; the monthly service review"), ("Pairs with", "SLIs, SLAs, Ana's availability maths")],
    itil=dict(groups=["service"], chain=["deliver", "improve"], practices=["availability management", "measurement and reporting"],
              sre="(SLIs measured as close to the user as possible; probes)", principles=["Focus on value", "Collaborate and promote visibility"],
              older="ITIL v3: availability management (agreed service time, downtime)"),
    problem_side="Larder, October–November 2027",
    problem="""  <p class="lead">For October, Eli has three numbers for business ordering, all called “availability”. The servers' own logs say <b>99.95 %</b>. The request-success SLI says <b>99.86 %</b> (the month the budget ran out). The outside checks, counting down minutes the way the new contract does, say <b>99.79 %</b>, just under the 99.8 % Ruben is about to sign. <span class="hl-pink">Ruben will read the third.</span> The gap is made of minutes when DNS or the content network failed outside Larder's servers, and minutes when a few percent of requests failed.</p>
  <ul>
    <li>The flattering number is the one nobody outside sees.</li>
    <li>Failures outside your servers never reach your server logs.</li>
    <li>Without written rules, every month's number is a negotiation.</li>
  </ul>""",
    problem_figs=[av_problem],
    meanwhile=[("architect-5", "availability-maths", "Ana's availability maths for the business ordering path: 99.69 % → 99.79 % by taking billing off the path (ADR 0025); measured 99.81 % in November.",
                "Eli's side: how that 99.81 % is counted (outside checks every minute, precise rules for down minutes) and why it differs from the server logs' 99.95 %.")],
    analogy_side="the open shop on a closed road",
    analogy="""  <p>A shop's own clock says the door was <b>unlocked from 08:00 to 18:00</b> every day: 100 % open. But on three mornings <b>the road outside was closed</b>, and no customer could get in. Asked how available the shop was, the honest answer counts the road too, because <b>the customer's trip</b> does.</p>""",
    analogy_figs=[av_analogy],
    map=[("The shop's own clock", "Server logs: 99.95 %"),
         ("The closed road", "DNS and the content network failing outside the servers"),
         ("A customer trying to get in", "An outside check placing a test order every minute"),
         ("Counting the trip", "The contract's down minutes: 99.81 %"),
         ("Writing down what counts", "Rules for partial outages and maintenance")],
    how_side="real requests plus outside checks, precise rules, both numbers published",
    how="""  <p>From <b>November</b>, availability is measured two ways:</p>
  <ul>
    <li><b>Real requests</b> at the load balancer: good ÷ valid, the SLI.</li>
    <li><b>Outside checks</b> every <b>60 seconds</b> from <b>two locations in different countries</b>. Each one logs in as a test office manager and places a test business order, like a real customer would.</li>
  </ul>
  <p>The rules are written down. A minute is <b>down</b> if more than <b>5 %</b> of requests fail, or if both outside checks fail. A <b>partial outage</b> counts by its share in the SLI, and as a down minute in the contract measure. <b>Planned maintenance always counts internally</b>, even where the contract excludes it, so nobody is tempted to call an outage “maintenance”.</p>
  <p>Both numbers go side by side on the monthly review, with <b>the gap explained</b>. November: <b>request SLI 99.92 %, contract minutes 99.81 %</b>, matching Ana's measurement. October's DNS minutes lead to a second DNS provider in December.</p>""",
    how_figs=[av_how],
    steps=[("List every “availability” number you have", "And where each is counted."),
           ("Add outside checks that act like a customer", "Two locations, every minute, a real flow."),
           ("Write the rules", "Down minute, partial outage, maintenance."),
           ("Count maintenance internally", "Always, whatever the contract says."),
           ("Publish the numbers side by side", "With the gap explained."),
           ("Fix what the gap shows", "Often outside your servers: DNS, CDN, vendors.")],
    vocab=[("Availability", "The share of time (or requests) a service works for its users."),
           ("Probe / synthetic check", "A robot that uses the service like a customer, on a schedule."),
           ("Down minute", "A minute counted as unavailable under written rules."),
           ("Partial outage", "Some requests or users fail while others work."),
           ("Agreed service time", "The hours a service is promised (24/7, or 06:00–23:00)."),
           ("Measurement gap", "The difference between numbers counted in different places.")],
    code=dict(file="ops/slo/availability.md", note="rules from November 2027", plain=True, src="""
# How Larder counts availability (business ordering)

measure 1   real requests · load balancer · good ÷ valid (SLI)
measure 2   outside checks · every 60 s · Frankfurt + Paris probes
            log in as test office manager → place test order → cancel
down minute > 5 % of requests fail, OR both outside checks fail
partial     SLI: counted by share · contract: a down minute if > 5 %
maintenance always counted internally; excluded in the contract only if
            announced ≥ 5 working days ahead, outside 06:00–20:00

            server logs   request SLI   contract minutes   gap explained
Oct 2027    99.95 %       99.86 %       99.79 %            DNS minutes (2 × 9 min)
Nov 2027    99.97 %       99.92 %       99.81 %            one slow PSP hour
action      second DNS provider (Dec 2027)
"""),
    tools="tools: load balancer logs, an outside synthetic-check service with two locations, and one page of rules.",
    ladder=[("the flattering number", ["Server logs only.", "Gaps unexplained."]),
            ("real requests + outside checks", ["Written rules.", "Both numbers published."]),
            ("customer-identical measurement", ["The client can see the same numbers live.", "Disputes rare."]),
            ("gaps designed out", ["Outside failures (DNS, CDN) made redundant.", "Numbers converge."])],
    ladder_now=1,
    baseline="Each line compares <b>server-log availability</b> to <b>real requests plus outside checks, written rules, and both numbers with the gap explained</b>.",
    ratings=[(2, 4, "Failures outside the servers become visible and get fixed."),
             (3, 3, "Neutral on its own."),
             (3, 3, "Neutral."),
             (3, 3, "Neutral."),
             (1, 4, "Numbers the client would compute, explained."),
             (3, 3, "Neutral."),
             (2, 3, "A second DNS provider bought for a measured reason."),
             (3, 3, "Neutral."),
             (3, 3, "A day to set up the checks.")],
    pitfalls=[("Reporting the flattering number", "The client computes a lower one.", "publish the customer's number."),
              ("Checks from inside the cloud", "They fail with you, or succeed while users can't reach you.", "outside, two locations."),
              ("Maintenance as an excuse", "Outages relabelled.", "count it internally, always."),
              ("A check that only pings", "The home page loads; ordering doesn't.", "check a real flow.")],
    use=["You promise availability in a contract.", "Different numbers circulate for the same thing.", "Customers report outages your logs don't show.", "Before signing an SLA."],
    skip=["Internal tools without promises: the SLI is enough."],
    related=["<b>Availability Maths</b> (Ana, vol. 5)", "<b>What Did We Sign?</b> (this volume)", "<b>What Do Users Count as Working?</b> (this volume)", "<b>How Do We Know It's Broken?</b> (vol. 1)"],
    quiz=[("Why did the server logs say 99.95 % when the contract measure said 99.79 %?", "Failures outside the servers (DNS, content network) and minutes with partial failures never reached the server logs."),
          ("What do Larder's outside checks do?", "Every 60 s from two countries, they log in as a test office manager and place a test business order."),
          ("When is a minute down?", "When more than 5 % of requests fail, or both outside checks fail."),
          ("Why count maintenance internally even when the contract excludes it?", "So outages can't be relabelled as maintenance, and the internal picture stays honest."),
          ("What did the October gap lead to?", "A second DNS provider in December.")],
    quiz_sit=[("A client's IT team says your availability last month was 99.6 %, but your report says 99.85 %. What do you do?", "Compare how each was counted: where, how often, what counts as down. Share your rules and raw down minutes. If their measure is closer to what users felt, learn from it; if not, agree one method together.")],
    try_it="Collect every availability number you report and write where it's counted. Set up one outside check that performs a real user flow every minute. How does its number compare with the others?",
    remember="Count availability the way <span class=\"hl\">the customer would</span>: their trip, not your door. Publish the numbers <span class=\"hl\">side by side</span> and explain the gap.",
    sources=["AXELOS, <i>ITIL 4: Availability management</i> practice guide (2020).",
             "Betsy Beyer et al., <i>The Site Reliability Workbook</i> (2018): chapter 2, choosing an SLI implementation.",
             "Alex Hidalgo, <i>Implementing Service Level Objectives</i> (2020): measuring from the client side."],
)

# ------------------------------------------------------------------ 07 Will Christmas Fit?
cp_problem = Doodle(760, 260, "Doodle of 16 December 2026: the database primary resized in a hurry, two days before the Christmas peak, because connections had run out at Friday's peak. Nobody had watched the database connections' headroom; the dashboard showed them, but no one looked at it until it hit the limit. For Christmas 2027, Ana's capacity plan of 18 October says the connections would run out at 1.3 times today's peak.",
                    "Christmas 2026: the database resized in a hurry because nobody watched the headroom. 2027's plan: out at 1.3× peak.")
cp_problem.box(14, 30, 350, 100, "16 Dec 2026", "pink", sub="primary resized in a hurry", size=20, subsize=14)
cp_problem.box(396, 30, 350, 100, "Ana, 18 Oct 2027", "y", sub="connections 310 / 400 → out at 1.3×", size=19, subsize=13)
cp_problem.note(380, 180, "the dashboard showed it · nobody looked until the limit", "red", size=17)

cp_analogy = Doodle(760, 220, "Doodle of a ferry company before the summer holidays. It knows its limits: cars per crossing, crossings per day, staff per shift. It watches bookings against those limits every week from April, adds crossings when a week passes 80 percent, and never finds out on the first Saturday of July that the boat is full.",
                    "The ferry watches bookings against its limits from April, and adds crossings at 80 %.")
cp_analogy.icon("ship", 40, 50, 1.0)
cp_analogy.row([("cars per crossing", None, "paper"), ("crossings per day", None, "paper"), ("staff per shift", None, "paper")], x=150, y=40, h=56, w=190, gap=10, size=15)
cp_analogy.box(150, 110, 590, 50, "weekly from April · add crossings at 80 %", "green", size=16)
cp_analogy.note(450, 196, "never discover a full boat on the first Saturday", "pen", size=17)

cp_how = Doodle(760, 400, "Larder's capacity watch from October 2027. Six limits, each with headroom shown at the busiest hour of the week: database connections (310 of 400, before the pooler), database CPU, Dispatch copies, the WMS B rate limit (20 requests a second, Larder queues at 15), the payment provider's rate limit, and each store's line. A ticket alert at 70 percent of a limit during the peak hour, a page at 85 percent. A 15-minute look every Monday. Ana's plan executed as changes: pooler 1 November, a browse replica 8 November, primary one size up 15 November; load test at five times peak passed on 15 November. December peak hour: connections at 41 percent of the new limit.",
                "Six limits, headroom at the peak hour, alerts at 70 and 85 %, a Monday look, and Ana's plan done by 15 November.")
for i, (t, v, f) in enumerate([("DB connections", "310 / 400 → pooler", "pink"), ("DB CPU", "55 %", "y"), ("Dispatch copies", "4 of 6", "y"),
                               ("WMS B rate", "queue at 15 of 20 / s", "y"), ("PSP rate", "40 %", "green"), ("store lines", "max 35 %", "green")]):
    r, c = divmod(i, 3)
    cp_how.box(14 + c * 248, 14 + r * 86, 236, 74, t, f, sub=v, size=16, subsize=13)
cp_how.box(14, 196, 732, 56, "alerts at the peak hour: 70 % → ticket · 85 % → page · Monday 15-min look", "blue", size=15)
cp_how.row([("1 Nov", "pooler", "paper"), ("8 Nov", "browse replica", "paper"), ("15 Nov", "primary +1 size · 5× test ✓", "green")], x=14, y=274, h=70, gap=40, size=16, subsize=12, arrows=True)
cp_how.note(380, 380, "December peak hour: connections at 41 % of the new limit", "green", size=16)

CAPACITY = dict(
    slug="capacity-headroom",
    kicker="a.k.a. “capacity and performance management, in operation”",
    tldr="Capacity planning predicts what you'll need; <b>capacity management</b> watches whether you still have room, every week. Pick the <b>few limits that actually stop you</b> (connections, rate limits, links), show <b>headroom at the busiest hour</b>, alert as a ticket at 70 % and a page at 85 %, look at them weekly, and turn the plan for the next peak into <b>dated changes done well before it</b>. Never resize in a hurry two days before Christmas again.",
    chips=[("Family", "measuring honestly"), ("Lives in", "the “headroom” dashboard; a Monday 15-minute look"), ("Pairs with", "Ana's capacity plan, the change calendar, running a peak")],
    itil=dict(groups=["service"], chain=["plan", "deliver"], practices=["capacity and performance management"],
              sre="“saturation”, the fourth golden signal; demand forecasting", principles=["Think and work holistically", "Optimise and automate"],
              older="ITIL v3: capacity management (business, service, component)"),
    problem_side="Larder, October 2027",
    problem="""  <p class="lead">On <b>16 December 2026</b> the database primary was resized in a hurry, two days before the Christmas peak, because connections had run out at Friday's peak. The dashboard showed connections the whole time, but <span class="hl-pink">nobody looked at it until it hit the limit</span>. For Christmas 2027, Ana's capacity plan of <b>18 October</b> says database connections are at <b>310 of 400</b> at today's peak, and would run out at <b>1.3×</b>. December is forecast at about 27,000 orders a day.</p>
  <ul>
    <li>A plan predicts; somebody still has to watch.</li>
    <li>Limits are spread across the database, vendors and stores.</li>
    <li>Changes needed for the peak must land before the freeze on 13 December.</li>
  </ul>""",
    problem_figs=[cp_problem],
    meanwhile=[("architect-5", "capacity-planning", "Ana's capacity plan of 18 October 2027: connections out at 1.3×, CPU at 1.8×; pooler 1 Nov, browse replica 8 Nov, primary one size up 15 Nov, freeze 13 Dec–3 Jan.",
                "Eli's weekly watch on the same limits: headroom at the busiest hour, alerts at 70 % and 85 %, and the plan carried out as dated changes before the freeze.")],
    analogy_side="the ferry before the summer",
    analogy="""  <p>A ferry company knows its limits: <b>cars per crossing, crossings per day, staff per shift</b>. From April it watches bookings against those limits <b>every week</b>, and adds crossings when a week passes <b>80 %</b>. It never finds out on the first Saturday of July that the boat is full.</p>""",
    analogy_figs=[cp_analogy],
    map=[("Cars per crossing", "Database connections, rate limits, store lines"),
         ("Bookings against the limit", "Headroom at the busiest hour"),
         ("Weekly from April", "A Monday 15-minute look"),
         ("Add crossings at 80 %", "Ticket at 70 %, page at 85 %"),
         ("The extra summer crossings", "Pooler, replica, bigger primary by 15 November")],
    how_side="six limits, headroom at the peak hour, alerts, a weekly look, dated changes",
    how="""  <p>From <b>October</b> Eli watches <b>six limits</b>, each shown as headroom at the <b>busiest hour of the week</b> (Friday 18:00–19:00), not as a daily average:</p>
  <ul>
    <li><b>Database connections</b> (310 of 400 before the pooler) and <b>database CPU</b>.</li>
    <li><b>Dispatch copies</b> (4 of 6 at peak).</li>
    <li>The <b>WMS B rate limit</b> (20 requests a second; Larder queues at 15) and the <b>payment provider's</b> rate limit.</li>
    <li>Each <b>store's line</b>.</li>
  </ul>
  <p>Alerts: <b>70 %</b> of a limit at the peak hour makes a ticket; <b>85 %</b> pages. Every Monday, 15 minutes, Eli and Bram look at the trend. Ana's plan is carried out as dated normal changes: the <b>pooler on 1 November</b>, a <b>browse replica on 8 November</b>, the <b>primary one size up on 15 November</b>, all well before the freeze. The <b>load test at 5× peak passes on 15 November</b>. In December's peak hour, connections sit at <b>41 %</b> of the new limit.</p>""",
    how_figs=[cp_how],
    steps=[("Find the limits that actually stop you", "Connections, rate limits, links, copies."),
           ("Show headroom at the busiest hour", "Not daily averages."),
           ("Alert before the edge", "Ticket at 70 %, page at 85 %."),
           ("Look weekly", "Trends, not just alerts."),
           ("Turn the peak plan into dated changes", "Done well before the freeze."),
           ("Test at the peak's size", "A load test, at a quiet hour.")],
    vocab=[("Capacity", "The maximum a component or service can handle."),
           ("Headroom", "How much room is left before a limit."),
           ("Saturation", "How full a resource is; the golden signal for capacity."),
           ("Peak hour", "The busiest hour of the week, where limits bite."),
           ("Connection pooler", "Software that shares a few database connections among many clients."),
           ("Load test", "Deliberately sending heavy traffic to see where limits are.")],
    code=dict(file="ops/capacity/headroom.md", note="weekly look · from October 2027", plain=True, src="""
limit                   at Fri 18–19 peak     alert 70 % / 85 %   note
DB connections          310 / 400  (78 %)     ticket ✓           → pooler 1 Nov
DB CPU                  55 %                  —                  → primary +1 size 15 Nov
Dispatch copies         4 / 6                 —                  scale to 6 (recipe R6)
WMS B API               12 / s (limit 20)     queue at 15        ok
PSP rate                40 %                  —                  ok
store lines (max)       35 % (Antwerp)        —                  ok

plan (Ana, 18 Oct) as changes: pooler 1 Nov · browse replica 8 Nov · primary +1 15 Nov
load test 5× peak:     15 Nov 05:00 · passed · checkout p95 640 ms
December peak hour:    DB connections 41 % of the new limit
"""),
    tools="tools: the metrics you already have, one headroom dashboard at the peak hour, two alert thresholds, a calendar for the changes.",
    ladder=[("resize in a hurry", ["Limits found at the peak.", "Dashboards nobody reads."]),
            ("headroom watched weekly", ["Six limits, two alert levels.", "Peak plan as dated changes."]),
            ("forecast-driven", ["Headroom projected from order forecasts.", "Changes scheduled automatically."]),
            ("elastic where possible", ["Autoscaling for what can scale.", "Watch only the hard limits."])],
    ladder_now=1,
    baseline="Each line compares <b>finding the limit at the peak</b> to <b>six limits watched weekly at the peak hour, with the plan done before the freeze</b>.",
    ratings=[(2, 4, "No checkout failures from full connections at Christmas."),
             (2, 4, "Limits raised before they're hit."),
             (3, 3, "Neutral."),
             (2, 4, "Capacity changes made calmly, weeks early."),
             (2, 4, "Headroom at the peak hour on one page."),
             (3, 3, "Neutral."),
             (3, 3, "≈ €2,100 a month more, planned."),
             (2, 3, "No hurried resizes two days before Christmas."),
             (3, 3, "15 minutes a week.")],
    pitfalls=[("Daily averages", "Peaks hide in averages.", "headroom at the busiest hour."),
              ("Watching only your servers", "The vendor's rate limit stops you.", "include vendor and store limits."),
              ("A plan without changes", "The plan is right and nothing happens.", "dated changes, before the freeze."),
              ("Alerting only at the edge", "No time to act.", "ticket at 70 %, page at 85 %.")],
    use=["A peak is coming.", "A limit surprised you once.", "Growth is steady (new cities).", "Vendors have rate limits on your critical path."],
    skip=["Fully elastic services with no hard limits: watch costs instead."],
    related=["<b>Capacity Planning</b> (Ana, vol. 5)", "<b>Load Profiles</b> (Ana, vol. 5)", "<b>Running a Peak</b> (this volume)", "<b>Autoscaling</b> (cloud, vol. 6)"],
    quiz=[("Why show headroom at the busiest hour, not a daily average?", "Limits bite at the peak; averages hide it."),
          ("What are Larder's alert levels?", "70 % of a limit at the peak hour → ticket; 85 % → page."),
          ("Which limits are outside Larder's servers?", "The WMS B and payment provider rate limits, and each store's line."),
          ("How was Ana's plan carried out?", "As dated changes: pooler 1 Nov, browse replica 8 Nov, primary one size up 15 Nov, before the 13 Dec freeze."),
          ("What happened on 16 December 2026, and why?", "The primary was resized in a hurry: nobody watched the connections' headroom until they hit the limit.")],
    quiz_sit=[("On a Monday look in November, the WMS B rate is at 75 % of its limit at the peak hour and climbing. What do you do?", "It's above the 70 % ticket line: talk to Ana and the WMS B vendor about a higher limit or batching, plan it as a change before the freeze, and watch it weekly until it's resolved.")],
    try_it="List the five limits that would stop your main service first. For each, find its value at last week's busiest hour. Which one is above 70 %? Put a dated change on the calendar for it.",
    remember="Watch the <span class=\"hl\">few limits that stop you</span>, at the <span class=\"hl\">busiest hour</span>, every week, and finish the peak's changes before the freeze.",
    sources=["AXELOS, <i>ITIL 4: Capacity and performance management</i> practice guide (2020).",
             "Betsy Beyer et al., <i>Site Reliability Engineering</i> (2016): chapter 18, software engineering in SRE (capacity planning).",
             "Brendan Gregg, <i>Systems Performance</i> (2nd ed., 2020): the USE method."],
)

# ------------------------------------------------------------------ 08 The Monthly Service Review
sr_problem = Doodle(760, 260, "Doodle of August 2027. Larder now has SLOs for five services, error budgets, OLAs coming, an incident page, delivery numbers, a capacity watch and soon a contract report. Each lives somewhere different. Service owners like Ben and Joost see some of it, sometimes. Decisions about reliability happen in corridors, or not at all.",
                    "SLOs, budgets, incidents, changes, capacity: all measured, all in different places, and decided in corridors.")
for i, t in enumerate(["SLOs", "budgets", "incidents", "changes", "capacity"]):
    sr_problem.box(14 + i * 148, 40, 136, 80, t, "y", size=17)
sr_problem.note(380, 170, "each in a different place · owners see some of it, sometimes", "red", size=17)
sr_problem.note(380, 206, "decisions: in corridors, or not at all", "pen", size=17)

sr_analogy = Doodle(760, 220, "Doodle of a GP's annual check-up. One sheet with the same measurements every year: blood pressure, weight, cholesterol, compared with last year. Twenty minutes with the doctor, ending with one or two decisions: change the dose, come back in six months. The value isn't the numbers; it's the decisions.",
                    "One sheet, the same numbers every time, twenty minutes, and it ends in a decision.")
sr_analogy.icon("ledger", 60, 40, 1.4)
sr_analogy.box(170, 40, 270, 100, "one sheet", "paper", sub="same numbers, vs last time", size=18, subsize=13)
sr_analogy.box(470, 40, 276, 100, "20 minutes", "green", sub="ends in 1–2 decisions", size=18, subsize=14)
sr_analogy.note(450, 190, "the value is the decision, not the numbers", "pen", size=18)

sr_how = Doodle(760, 400, "Larder's monthly service review from September 2027. One page per service, generated on the first working day: SLOs and error budget, incidents and orders affected, changes and change failures, capacity headroom, OLAs and vendor issues, open problems and actions. A 30-minute meeting per critical service on the first Thursday, with the owner (Ben for ordering, Joost's lead for Dispatch, Cho for payments), Eli and the people affected. It ends with at most three decisions, logged. For business ordering the same data produces Korenwolf's monthly report in the portal. October's ordering review decided the portal pause and the second DNS provider.",
                "One generated page per service, 30 minutes with its owner, and at most three logged decisions.")
for i, t in enumerate(["SLO + budget", "incidents", "changes", "capacity", "OLAs + vendors", "problems + actions"]):
    r, c = divmod(i, 3)
    sr_how.box(14 + c * 248, 14 + r * 74, 236, 62, t, "blue", size=16)
sr_how.box(14, 176, 732, 64, "first Thursday · 30 min per critical service · owner + Eli + affected", "y", size=15)
sr_how.box(14, 256, 732, 64, "ends with ≤ 3 decisions, logged · Korenwolf's report from the same data", "green", size=15)
sr_how.note(380, 356, "October, ordering: portal pause · second DNS provider", "pen", size=16)
sr_how.note(380, 388, "the page is generated; the meeting is for deciding", "red", size=15)

SERVICE_REVIEWS = dict(
    slug="service-reviews",
    kicker="a.k.a. “service reporting and review”",
    tldr="All the numbers about a service (SLOs, budget, incidents, changes, capacity, OLAs, vendors) belong on <b>one page, generated, the same every month</b>. Then hold a <b>short meeting with the service's owner</b> that ends in <b>a few logged decisions</b>. The report is for seeing; the review is for deciding. Where a client has an SLA, the same data produces <b>their report</b> too.",
    chips=[("Family", "measuring honestly"), ("Lives in", "ops/reviews/monthly/&lt;service&gt;-YYYY-MM.md; first Thursday"), ("Pairs with", "SLOs, error budgets, OLAs, the client report")],
    itil=dict(groups=["general", "service"], chain=["improve", "engage"], practices=["measurement and reporting", "relationship management", "service level management"],
              sre="(SLO reviews; production reviews)", principles=["Collaborate and promote visibility", "Progress iteratively with feedback"],
              older="ITIL v3: service reporting, service review meetings"),
    problem_side="Larder, August 2027",
    problem="""  <p class="lead">By August Larder measures a lot: SLOs and error budgets for five services, an incident page, delivery numbers, a capacity watch, and soon OLAs and a contract report. <span class="hl-pink">Each lives somewhere different.</span> Service owners like Ben and Joost see some of it, sometimes. Decisions about reliability happen in corridors, or don't happen at all.</p>
  <ul>
    <li>Numbers without a decision are just reporting.</li>
    <li>Owners can't own what they don't see together.</li>
    <li>Each report is assembled by hand, slightly differently each time.</li>
  </ul>""",
    problem_figs=[sr_problem],
    analogy_side="the annual check-up",
    analogy="""  <p>At an annual check-up a GP looks at <b>one sheet</b> with the same measurements every year: blood pressure, weight, cholesterol, each compared with last year. Twenty minutes with the doctor end in <b>one or two decisions</b>: change the dose, come back in six months. The value isn't the numbers. It's the decisions.</p>""",
    analogy_figs=[sr_analogy],
    map=[("The same measurements every year", "The same sections on every service's page"),
         ("Compared with last year", "Trend vs last month and last quarter"),
         ("Twenty minutes with the doctor", "30 minutes with the service owner"),
         ("“Change the dose”", "At most three logged decisions"),
         ("A copy for the patient", "Korenwolf's report from the same data")],
    how_side="one generated page per service, a short review, a few decisions",
    how="""  <p>From <b>September</b>, on the first working day of each month, a script generates <b>one page per service</b> with the same sections every time: SLO status and error budget, incidents and orders affected, changes and change failures, capacity headroom, OLAs and vendor issues, open problems and actions.</p>
  <p>On the <b>first Thursday</b>, each critical service gets a <b>30-minute review</b> with its owner (Ben for ordering, Joost's lead for Dispatch, Cho for payments), Eli, and whoever is affected that month. Nobody presents slides. Everyone has read the page, and the meeting ends with <b>at most three decisions</b>, logged in the page itself.</p>
  <p>For business ordering, the same data produces <b>Korenwolf's monthly report</b> in the portal, so the client and Larder see the same numbers. October's ordering review decides the <b>portal pause</b> (the budget was spent) and the <b>second DNS provider</b>. November's decides to retire two flaky API endpoints.</p>""",
    how_figs=[sr_how],
    steps=[("Put every measure for a service on one page", "SLO, budget, incidents, changes, capacity, OLAs."),
           ("Generate it, don't assemble it", "Same sections, every month."),
           ("Hold a short review with the owner", "Read beforehand; no slides."),
           ("End with at most three decisions", "Logged on the page."),
           ("Reuse the data for client reports", "One truth, two audiences."),
           ("Check last month's decisions first", "Did they happen?")],
    vocab=[("Service report", "A regular summary of a service's performance against its targets."),
           ("Service review", "A meeting with the owner and stakeholders to decide what to change."),
           ("Decision log", "The record of decisions made, with owners and dates."),
           ("Single source of truth", "One set of data used for every report."),
           ("Trend", "How a number moves over months; often more useful than its level."),
           ("Read-ahead", "Reading the page before the meeting, so the meeting can decide.")],
    code=dict(file="ops/reviews/monthly/ordering-2027-10.md", note="generated 1 Nov 2027 · reviewed Thu 4 Nov", plain=True, src="""
# Ordering · October 2027                          owner: Ben · review: Thu 4 Nov

SLOs          checkout success 99.91 % (≥ 99.9 ✓) · speed 95.6 % (≥ 95 ✓)
              business ordering 99.86 % → budget SPENT (policy: features paused 9 days)
incidents     SEV2 ×2 (API retries 12 Oct · DNS 21 Oct) · ≈ 140 orders affected
changes       241 · failed 7 (2.9 %) · 0 in windows
capacity      DB connections 78 % at peak (→ pooler 1 Nov)
OLAs/vendors  billing silence alerts: 0 · DNS provider: 2 × 9 min
open          PRB-011 API retry storm (fixed 25 Oct) · A-41 second DNS provider

decisions     1 portal feature releases resume when ≥ 99.9 % for 7 days (Grace) ✓
(≤ 3)         2 second DNS provider in December (Eli)
              3 retire /business/v1/legacy-search by Jan (Ben)
"""),
    tools="tools: a script that builds the page from the SLO, incident, change and capacity data; a monthly calendar slot per service.",
    ladder=[("numbers everywhere, decisions nowhere", ["Hand-made reports.", "Corridor decisions."]),
            ("one generated page, a short review", ["Same sections every month.", "Three logged decisions."]),
            ("reviews feed planning", ["Decisions become backlog items automatically.", "Quarterly roll-up for leaders."]),
            ("clients see it live", ["The client's view and Larder's are the same pages.", "Reviews shared."])],
    ladder_now=1,
    baseline="Each line compares <b>measures scattered across tools and decisions in corridors</b> to <b>one generated page per service and a monthly review that decides</b>.",
    ratings=[(2, 3, "Reliability decisions are made on time."),
             (2, 3, "Problems get owners at the review."),
             (3, 3, "Neutral."),
             (3, 3, "Neutral."),
             (2, 4, "Owners see everything about their service together."),
             (2, 3, "Reports generated, not assembled."),
             (2, 3, "Spending decided with numbers."),
             (3, 3, "Neutral."),
             (3, 3, "30 minutes a month per critical service.")],
    pitfalls=[("Reports without reviews", "Read by nobody.", "a short meeting that ends in decisions."),
              ("Slides", "The meeting is spent presenting.", "everyone reads the page first."),
              ("Different numbers for the client", "Two truths, endless disputes.", "one data source, two reports."),
              ("Too many decisions", "None get done.", "at most three, owned.")],
    use=["You measure a lot and decide little.", "Owners don't see their service as a whole.", "Clients get reports built by hand.", "After setting SLOs and OLAs."],
    skip=["Services with no targets yet: set SLOs first."],
    related=["<b>When Do We Stop Shipping Features?</b> (this volume)", "<b>What Do Teams Promise Each Other?</b> (this volume)", "<b>The Quarterly Product Review</b> (Grace, vol. 5)", "<b>Dashboards People Actually Open</b> (next note)"],
    quiz=[("What's on each service's monthly page?", "SLO and budget, incidents and orders affected, changes and failures, capacity, OLAs and vendors, open problems and actions."),
          ("How long is a service review, and who's there?", "30 minutes, with the owner, Eli and whoever was affected."),
          ("How does a review end?", "With at most three logged decisions."),
          ("Why generate the page rather than assemble it?", "Same sections every month, no hand-work, and the same data for client reports."),
          ("What did October's ordering review decide?", "Resume portal features after 7 days above SLO, a second DNS provider, and retiring a legacy API endpoint.")],
    quiz_sit=[("A service review runs over because people debate October's numbers. What should change for November?", "The page is sent out earlier and read beforehand; questions about the numbers go in comments before the meeting; the meeting itself is only for the decisions.")],
    try_it="For one service, put every number you have about it on one page, the same sections as Larder's. Book 30 minutes with its owner. What three decisions come out?",
    remember="A report is for <span class=\"hl\">seeing</span>, a review is for <span class=\"hl\">deciding</span>. One generated page, thirty minutes, three decisions.",
    sources=["AXELOS, <i>ITIL 4: Measurement and reporting</i> and <i>Relationship management</i> practice guides (2020).",
             "Betsy Beyer et al., <i>The Site Reliability Workbook</i> (2018): chapter on SLO engineering and reviews.",
             "Andy Grove, <i>High Output Management</i> (1983): on meetings that decide."],
)

# ------------------------------------------------------------------ 09 Dashboards People Actually Open
db_problem = Doodle(760, 260, "Doodle of Eli's count of dashboards in October 2027: 74 in the monitoring tool. In the last 90 days, 9 were opened by more than one person. Three different 'checkout' dashboards disagree about the error rate because they count differently. On-call opens the wrong one during an incident in September.",
                    "74 dashboards, 9 opened by more than one person in 90 days, and three “checkout” ones that disagree.")
for i in range(20):
    r, c = divmod(i, 10)
    db_problem.box(14 + c * 74, 20 + r * 56, 64, 44, None, "green" if i in (2, 7, 11) else "paper", rx=3)
db_problem.note(380, 150, "74 dashboards · 9 used by more than one person", "pen", size=17)
db_problem.box(110, 176, 540, 56, "3 × “checkout”, 3 different error rates", "pink", stroke="red", size=16)

db_analogy = Doodle(760, 220, "Doodle of a car's dashboard: speed, fuel, a few warning lights. It doesn't show the engine's 200 sensors; those are for the mechanic's laptop. Each screen answers one person's question while they're doing one job.",
                    "The car shows speed, fuel and warning lights. The 200 sensors are for the mechanic's laptop.")
dba = db_analogy
dba.icon("gauge", 60, 40, 1.5)
dba.box(170, 40, 270, 100, "driver", "green", sub="speed · fuel · warnings", size=19, subsize=14)
dba.box(470, 40, 276, 100, "mechanic", "paper", sub="200 sensors, on a laptop", size=19, subsize=14)
dba.note(450, 190, "one question, one audience, one screen", "pen", size=18)

db_how = Doodle(760, 380, "Larder's dashboards after the clean-up in October 2027. One page 'Larder now' on the office screen and phones: orders per city against last week, SLO status per service, open incidents. One dashboard per critical service for on-call and owners, linked from every alert, with the top row being the SLIs and the rows below explaining them. A weekly SLO page for Femke. Stores use the status page. 74 dashboards became 11; the rest archived, not deleted, and restored on request (2 in three months). Each dashboard has an owner and a 'question it answers' line at the top; one unopened for 90 days is flagged for archiving.",
                "74 → 11: one “Larder now”, one per critical service, one for Femke. Each with an owner and its question at the top.")
for i, (t, s, f) in enumerate([("Larder now", "orders · SLOs · incidents", "green"), ("per service", "SLIs on top, causes below", "blue"), ("Femke weekly", "SLO status", "y"), ("stores", "status page", "paper")]):
    db_how.box(14 + i * 186, 14, 172, 110, t, f, sub=s, size=18, subsize=12)
db_how.row([("before", "74 dashboards", "pink"), ("after", "11 · 63 archived", "green")], x=110, y=160, h=80, w=250, gap=40, size=19, subsize=15, arrows=True)
db_how.box(14, 266, 732, 64, "each: an owner · “the question it answers” on top · 90 days unopened → archive", "paper", size=14)
db_how.note(380, 362, "archived, not deleted: 2 restored in three months", "pen", size=15)

DASHBOARDS = dict(
    slug="dashboards",
    kicker="a.k.a. “dashboards with a purpose”",
    tldr="Dashboards multiply because making one is easy and deleting one feels risky. Most are never opened, and several disagree. Keep <b>few dashboards, each answering one question for one audience</b>: a “now” page for everyone, one per critical service for on-call (SLIs on top, causes below), one for leaders. Give each an <b>owner</b> and its <b>question written at the top</b>, and <b>archive</b> anything nobody opens.",
    chips=[("Family", "measuring honestly"), ("Lives in", "the monitoring tool, 11 dashboards, each with an owner"), ("Pairs with", "monitoring (vol. 1), SLIs, service reviews")],
    itil=dict(groups=["general", "service"], chain=["deliver", "engage"], practices=["measurement and reporting", "monitoring and event management"],
              sre="(SLO dashboards; one page per service)", principles=["Keep it simple and practical", "Focus on value"],
              older="ITIL v3: service reporting"),
    problem_side="Larder, October 2027",
    problem="""  <p class="lead">Eli counts the dashboards in October: <b>74</b>. In the last 90 days only <b>9</b> were opened by more than one person. <b>Three</b> different “checkout” dashboards disagree about the error rate, because each counts differently. <span class="hl-pink">During a September incident, on-call opened the wrong one</span> and spent ten minutes chasing a number that wasn't real.</p>
  <ul>
    <li>Nobody knows which dashboard is the right one.</li>
    <li>Old dashboards quietly show wrong numbers as systems change.</li>
    <li>Leaders get screenshots of whichever one someone had open.</li>
  </ul>""",
    problem_figs=[db_problem],
    analogy_side="the car's dashboard",
    analogy="""  <p>A car's dashboard shows <b>speed, fuel and a few warning lights</b>. It doesn't show the engine's 200 sensors; those are for <b>the mechanic's laptop</b>. Each screen answers <b>one person's question</b> while they do one job. Nobody wants the mechanic's view while driving.</p>""",
    analogy_figs=[db_analogy],
    map=[("Speed and fuel", "“Larder now”: orders per city, SLO status, open incidents"),
         ("Warning lights", "SLIs on top of each service dashboard"),
         ("The mechanic's laptop", "The rows below: causes, machines"),
         ("The driver", "On-call, Femke, stores: one audience each"),
         ("200 sensors nobody reads", "63 archived dashboards")],
    how_side="few dashboards, one question each, owned, and archived when unused",
    how="""  <p>In <b>October</b> Eli and Bram cut <b>74 dashboards to 11</b>:</p>
  <ul>
    <li><b>“Larder now”</b>, on the office screen and on phones: orders per city against last week, SLO status per service, open incidents.</li>
    <li><b>One per critical service</b>, linked from every alert: <b>SLIs on the top row</b>, the rows that explain them below (connections, queues, vendors). The three checkout dashboards become one, with the SLI's definition.</li>
    <li><b>A weekly SLO page for Femke</b>, and the <b>status page</b> for stores and clients.</li>
  </ul>
  <p>Every dashboard has an <b>owner</b>, and <b>“the question it answers”</b> written at the top. Anything unopened for <b>90 days</b> is flagged and archived: kept, but out of the list. Only <b>2</b> are restored in three months. New dashboards are welcome, as long as they answer a question none of the 11 does.</p>""",
    how_figs=[db_how],
    steps=[("Count dashboards and their views", "Last 90 days, by distinct people."),
           ("Write the question each one answers", "If you can't, it's a candidate to go."),
           ("Keep one per audience and job", "Now, on-call per service, leaders."),
           ("Put SLIs on top, causes below", "Symptoms first, like alerts."),
           ("Give each an owner", "Who keeps it right as systems change."),
           ("Archive the unopened", "Kept, out of sight, restorable.")],
    vocab=[("Dashboard", "A screen of graphs and numbers for watching something."),
           ("Audience", "Who looks at a dashboard, and for what job."),
           ("Dashboard sprawl", "Many overlapping, unowned dashboards."),
           ("Top row", "The first thing seen: the SLIs."),
           ("Archive", "Remove from the list but keep for restoring."),
           ("Single definition", "One agreed way to compute a number, used everywhere.")],
    code=dict(file="ops/dashboards.md", note="after the clean-up · October 2027", plain=True, src="""
dashboard            audience        question it answers                                owner
Larder now           everyone        are customers getting their orders right now?     Eli
checkout             on-call, Ben    is checkout working, and if not, why?             Ben
business ordering    on-call, Mo     can offices order, and if not, why?               Ben
Dispatch             on-call, Joost  are packed orders getting couriers?               Ben
payments             on-call, Cho    are payments succeeding, per provider?            Cho
store sync / stores  on-call, leads  is every store's stock fresh and online?          Eli
capacity headroom    Eli, Bram       which limit runs out first at the peak?           Bram
delivery numbers     Marco, leads    are changes getting safer?                        Bram
Femke weekly         Femke           are we keeping our promises?                      Eli
(+ 2 vendor views)
rules  question on top · owner · SLIs first · 90 days unopened → archive
"""),
    tools="tools: the monitoring tool's view counts, a naming rule, and an archive folder.",
    ladder=[("dashboard sprawl", ["Dozens, unowned.", "Conflicting numbers."]),
            ("few, owned, one question each", ["SLIs on top.", "Unused ones archived."]),
            ("generated from the catalogue", ["Each service's dashboard built from its SLO file.", "Links in every alert."]),
            ("dashboards rarely needed", ["Alerts and reviews carry the information.", "Dashboards for digging."])],
    ladder_now=1,
    baseline="Each line compares <b>74 unowned, overlapping dashboards</b> to <b>11 owned dashboards, one question each</b>.",
    ratings=[(3, 3, "Neutral."),
             (3, 3, "Neutral."),
             (2, 3, "On-call opens the right one from the alert."),
             (3, 3, "Neutral."),
             (2, 4, "One agreed number for each thing."),
             (2, 3, "No more keeping 74 dashboards right."),
             (3, 3, "Neutral."),
             (3, 3, "Neutral."),
             (3, 4, "A day to clean up; a rule to keep it clean.")],
    pitfalls=[("Deleting outright", "Someone's quarterly view vanishes.", "archive, restorable."),
              ("A dashboard per person", "Sprawl returns.", "one per audience and job."),
              ("Different definitions", "Numbers disagree across screens.", "one definition per SLI, everywhere."),
              ("Causes on top", "On-call stares at CPU.", "SLIs first.")],
    use=["Nobody knows which dashboard is right.", "Numbers disagree between screens.", "On-call wastes time choosing where to look.", "After setting SLIs."],
    skip=["You have three dashboards and everyone uses them."],
    related=["<b>How Do We Know It's Broken?</b> (vol. 1)", "<b>The Monthly Service Review</b> (this volume)", "<b>Logs, Metrics & Traces</b> (cloud, vol. 6)", "<b>Vanity vs Actionable Metrics</b> (Grace, vol. 4)"],
    quiz=[("What did Eli find in October?", "74 dashboards, 9 used by more than one person in 90 days, and three checkout dashboards that disagreed."),
          ("What's at the top of every dashboard now?", "The question it answers, and (for services) the SLIs."),
          ("What are the three main kinds of dashboard at Larder?", "“Larder now” for everyone, one per critical service for on-call and owners, and a weekly SLO page for Femke."),
          ("What happens to a dashboard nobody opens for 90 days?", "It's flagged and archived: kept, but out of the list."),
          ("Why one definition per SLI?", "So numbers agree on every screen and in every report.")],
    quiz_sit=[("Marketing asks for a new dashboard of orders by campaign. Should it exist?", "If it answers a question none of the 11 does, yes: with an owner, the question at the top, and the same order definitions. If it duplicates “Larder now”, add a filter instead.")],
    try_it="Count your dashboards and how many people opened each in the last 90 days. For each one you keep, write the question it answers at the top. Archive the rest and see who notices.",
    remember="One dashboard, <span class=\"hl\">one question, one audience</span>, one owner. Archive what nobody opens; <span class=\"hl\">SLIs on top</span>.",
    sources=["Stephen Few, <i>Information Dashboard Design</i> (2nd ed., 2013).",
             "Betsy Beyer et al., <i>Site Reliability Engineering</i> (2016): chapter 6, monitoring (dashboards).",
             "AXELOS, <i>ITIL 4: Measurement and reporting</i> practice guide (2020)."],
)

# ------------------------------------------------------------------ 10 Asking the Users
us_problem = Doodle(760, 260, "Doodle of November 2027. Every SLO is green: checkout, Dispatch, store sync, business ordering. Then Inès, the new Antwerp store manager, says in a call that her pickers hate the handhelds. Tomás agrees: by 21:00 half the older handhelds at Noord are on their last bar of battery, and pickers queue at the chargers. None of this shows in any SLO.",
                    "Every SLO green, and the pickers hate the handhelds. Batteries die by 21:00; it shows up nowhere.")
for i, t in enumerate(["checkout", "Dispatch", "store sync", "business"]):
    us_problem.box(14 + i * 186, 30, 172, 70, t, "green", sub="SLO ✓", size=17, subsize=14)
us_problem.box(110, 130, 540, 70, "“my pickers hate the handhelds” · batteries dead by 21:00", "pink", stroke="red", size=16)
us_problem.note(380, 236, "green numbers, unhappy people", "red", size=18)

us_analogy = Doodle(760, 220, "Doodle of a hotel whose systems all say fine: the lifts work, the Wi-Fi is up, the rooms are clean. But guests complain the shower takes five minutes to get hot. Only asking them finds it; no system measures it. The best hotels ask a few questions after every stay.",
                    "Lifts fine, Wi-Fi fine, rooms clean, and guests wait five minutes for hot water. Only asking finds it.")
usa = us_analogy
usa.row([("lifts ✓", None, "green"), ("Wi-Fi ✓", None, "green"), ("rooms ✓", None, "green"), ("shower: 5 min", None, "pink")], y=40, h=70, gap=14, size=17)
usa.note(380, 150, "found only by asking: three questions after every stay", "pen", size=18)

us_how = Doodle(760, 400, "Larder's IT pulse, from November 2027: three questions every quarter to store staff, support agents and office managers, in their language, on a phone, two minutes. How well does IT help you do your job, 1 to 5? What's the most annoying thing this quarter? One thing we should fix first? November: 214 answers. Handhelds 3.1 (older model slow, batteries by evening); service desk 4.2; Antwerp Wi-Fi 2.8; portal 4.0 from office managers. Actions: spare batteries and a mid-shift swap at every store from December; the older handheld model moved up in the lifecycle register for replacement in 2028; a Wi-Fi survey in Antwerp. Results and 'you said, we did' posted in every store.",
                "Three questions a quarter, in people's language. 214 answers; handhelds 3.1, desk 4.2, Antwerp Wi-Fi 2.8. Then act and say so.")
for i, (t, v, f) in enumerate([("handhelds", "3.1 / 5", "pink"), ("service desk", "4.2 / 5", "green"), ("Antwerp Wi-Fi", "2.8 / 5", "pink"), ("portal (offices)", "4.0 / 5", "green")]):
    us_how.box(14 + i * 186, 14, 172, 96, t, f, sub=v, size=17, subsize=18)
us_how.box(14, 136, 732, 110, None, "paper")
us_how.text(380, 168, "spare batteries + mid-shift swap, every store, December", size=15)
us_how.text(380, 196, "older handhelds up the lifecycle register: replace in 2028", size=15)
us_how.text(380, 224, "Wi-Fi survey in Antwerp, December", size=15)
us_how.note(380, 286, "“you said, we did” on every store's wall", "green", size=17)
us_how.note(380, 322, "uptime measures the system; asking measures the experience", "pen", size=16)

USER_SATISFACTION = dict(
    slug="user-satisfaction",
    kicker="a.k.a. “experience beyond uptime”",
    tldr="SLOs measure whether systems work; they can't measure whether <b>using them is any good</b>. Batteries that die by evening, slow screens, a Wi-Fi that's “up” but weak: none of it breaks an SLO. <b>Ask the people who use IT</b>, regularly and briefly (three questions, in their language, on a phone), <b>act on the top answers</b>, and tell them what you changed. Green numbers and unhappy people means you're measuring the wrong thing.",
    chips=[("Family", "measuring honestly"), ("Lives in", "a quarterly pulse to stores, support and office managers; “you said, we did” posters"), ("Pairs with", "the service desk, SLIs, the asset register")],
    itil=dict(groups=["general", "service"], chain=["engage", "improve"], practices=["relationship management", "measurement and reporting", "service desk"],
              sre="(user happiness is the real SLO; SLIs are a proxy)", principles=["Focus on value", "Collaborate and promote visibility"],
              older="ITIL v3: customer satisfaction surveys; experience level agreements (XLAs) in newer thinking"),
    problem_side="Larder, November 2027",
    problem="""  <p class="lead">In November <b>every SLO is green</b>: checkout, Dispatch, store sync, business ordering. Then <b>Inès</b>, the new Antwerp store manager, says on a call that her pickers <b>hate the handhelds</b>. Tomás agrees: by 21:00 half of Noord's older handhelds are on their last bar of battery, and pickers queue at the chargers. <span class="hl-pink">None of this shows in any SLO.</span></p>
  <ul>
    <li>A system can work perfectly and still be miserable to use.</li>
    <li>Staff stop reporting what they think IT can't fix.</li>
    <li>Annoyances cost picking speed long before they cause incidents.</li>
  </ul>""",
    problem_figs=[us_problem],
    analogy_side="the hotel's hot water",
    analogy="""  <p>A hotel's systems all say fine: the lifts work, the Wi-Fi is up, the rooms are cleaned on time. But guests complain that <b>the shower takes five minutes to get hot</b>. No system measures that. The best hotels <b>ask three questions after every stay</b>, fix the top answer, and tell the next guests what changed.</p>""",
    analogy_figs=[us_analogy],
    map=[("Lifts, Wi-Fi, clean rooms", "Green SLOs"),
         ("Five minutes for hot water", "Batteries dead by 21:00; slow older handhelds"),
         ("Three questions after every stay", "A quarterly three-question pulse"),
         ("Guests", "Pickers, store leads, support agents, office managers"),
         ("“We fixed the boiler” at reception", "“You said, we did” on every store's wall")],
    how_side="three questions a quarter, act on the top answers, say what changed",
    how="""  <p>From <b>November</b> a quarterly <b>IT pulse</b> goes to store staff, support agents and office managers: <b>three questions</b>, in Dutch, French or English, on a phone, about two minutes.</p>
  <ol>
    <li>How well does IT help you do your job? (1–5, per thing: handhelds, Wi-Fi, desk, portal)</li>
    <li>What's the most annoying thing this quarter?</li>
    <li>What should we fix first?</li>
  </ol>
  <p>November brings <b>214 answers</b>. Handhelds score <b>3.1</b> (the older model is slow, and batteries die by evening). The service desk gets <b>4.2</b>, <b>Antwerp's Wi-Fi 2.8</b>, and office managers give the portal <b>4.0</b>. The actions: <b>spare batteries and a mid-shift swap</b> at every store from December, the older handheld model moved up the lifecycle register for <b>replacement in 2028</b>, and a <b>Wi-Fi survey in Antwerp</b>. The results go on a <b>“you said, we did”</b> poster in every store, in the same format as Grace's operations feedback loop.</p>""",
    how_figs=[us_how],
    steps=[("Ask the people who use IT, not their managers", "Pickers, agents, office managers."),
           ("Keep it to three questions", "Two minutes, on a phone, in their language."),
           ("Ask regularly", "Quarterly is enough to see trends."),
           ("Act on the top answers", "Even small fixes: batteries."),
           ("Tell them what changed", "Or they stop answering."),
           ("Put the scores next to the SLOs", "Experience and reliability together.")],
    vocab=[("User satisfaction", "How people feel about using a service, asked directly."),
           ("Pulse survey", "A short, regular survey with a few fixed questions."),
           ("XLA (experience level agreement)", "A newer idea: targets based on user experience, not only system metrics."),
           ("Proxy metric", "A number that stands in for what you really care about (SLIs stand in for happiness)."),
           ("Watermelon effect", "Green on the outside (metrics), red on the inside (experience)."),
           ("Closing the loop", "Telling people what you did with their feedback.")],
    code=dict(file="ops/pulse/2027-11.md", note="IT pulse · November 2027 · 214 answers", plain=True, src="""
                     score (1–5)   top annoyance                         action
handhelds            3.1           older model slow · battery by 21:00    spare batteries + mid-shift
                                                                         swap (Dec) · replace HH-2024
                                                                         in 2028 (lifecycle register)
store Wi-Fi          3.6 (Antwerp 2.8)  drops in the back aisle (Antwerp)  survey Antwerp (Dec)
service desk         4.2           "answers fast, fixes slower"          known errors → stores (vol. 4)
portal (offices)     4.0           "can't change an order after 16:00"   → Grace (product decision)
helpdesk (agents)    3.7           two logins                            SSO in Q1 (identity)

languages nl · fr · en  ·  next pulse: February 2028  ·  "you said, we did" posted 6 Dec
"""),
    tools="tools: a simple form tool, a QR code on the store poster, and a poster template for “you said, we did”.",
    ladder=[("metrics only", ["Green SLOs, unhappy people.", "Annoyances unspoken."]),
            ("a quarterly pulse, acted on", ["Three questions, in people's language.", "“You said, we did.”"]),
            ("experience in the service review", ["Scores next to SLOs monthly.", "Experience targets for key tools."]),
            ("experience-led", ["Experience level agreements for the stores.", "Fixes prioritised by experience."])],
    ladder_now=1,
    baseline="Each line compares <b>green SLOs alone</b> to <b>a quarterly three-question pulse with actions and “you said, we did”</b>.",
    ratings=[(2, 4, "Pickers' daily annoyances fixed."),
             (3, 3, "Neutral."),
             (3, 3, "Neutral."),
             (3, 3, "Neutral."),
             (2, 4, "The experience is visible next to the SLOs."),
             (3, 3, "Neutral."),
             (2, 3, "Spending on what people actually feel (batteries, not servers)."),
             (3, 3, "Neutral."),
             (3, 3, "Two minutes per person a quarter.")],
    pitfalls=[("Asking managers instead of users", "You hear about the managers' problems.", "ask the pickers and agents."),
              ("Long surveys", "Nobody answers.", "three questions."),
              ("Asking without acting", "Answers stop after one round.", "act and say what you did."),
              ("Trusting only green metrics", "The watermelon effect.", "experience next to reliability.")],
    use=["Metrics are green and people still complain.", "Staff stopped reporting annoyances.", "A new site or country (Antwerp).", "Before a big device or tool replacement."],
    skip=["When you already talk to every user weekly: just write it down."],
    related=["<b>Feedback Loops with Operations</b> (Grace, vol. 4)", "<b>What Do Users Count as Working?</b> (this volume)", "<b>Where Do People Report Problems?</b> (vol. 1)", "<b>The Database Runs Out of Support</b> (vol. 3)"],
    quiz=[("Why did no SLO show the handheld problem?", "SLOs measured whether systems worked; batteries and slowness made them miserable to use without failing."),
          ("What are the three pulse questions?", "How well IT helps you (1–5 per thing), the most annoying thing, and what to fix first."),
          ("What were the lowest scores in November?", "Antwerp Wi-Fi 2.8 and handhelds 3.1."),
          ("What's the watermelon effect?", "Green metrics on the outside, red experience on the inside."),
          ("Why post “you said, we did”?", "So people see their answers lead to changes, and keep answering.")],
    quiz_sit=[("The pulse says the portal is annoying because orders can't be changed after 16:00. Is that IT's to fix?", "Not alone: it's a product decision (Grace), maybe for good operational reasons. Pass it on with the numbers, and report back in “you said, we did” what was decided and why.")],
    try_it="Ask ten people who use your systems daily the three questions this week. What's the top annoyance? Fix the smallest version of it, and tell them.",
    remember="Uptime measures <span class=\"hl\">the system</span>; asking measures <span class=\"hl\">the experience</span>. Three questions, act, and say what changed.",
    sources=["AXELOS, <i>ITIL 4: Relationship management</i> and <i>Service desk</i> practice guides (2020).",
             "Betsy Beyer et al., <i>The Site Reliability Workbook</i> (2018): SLIs as proxies for user happiness.",
             "Gartner and others, writing on experience level agreements (XLAs), as background."],
)

NOTES = [MEASURING_AVAILABILITY, CAPACITY, SERVICE_REVIEWS, DASHBOARDS, USER_SATISFACTION]
