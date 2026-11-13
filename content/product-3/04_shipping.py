# Series 2 · Book 2 · The Product Owner's Notebook · Vol. 3 · Shipping.
# Narrator: Grace. Running case study: Larder (facts in docs/larder-casebook.md).

# ------------------------------------------------------------------ 12 Launch Checklist
lc_problem = Doodle(760, 280, "Doodle of the story Grace hears about store Zuid's opening day in November 2024: 340 products had no price, support learnt about the opening from customers, and the first push message went out with the wrong area. Nobody had a list; everybody assumed somebody else had checked.",
                    "Zuid's opening day, 2024: 340 products without prices, support surprised, a push to the wrong area.")
for i, (t, s) in enumerate([("340 products", "no price"), ("support", "heard from customers"), ("push message", "wrong area")]):
    lc_problem.box(20 + i * 250, 40, 220, 90, t, "pink", sub=s, stroke="red")
lc_problem.note(380, 190, "everybody assumed somebody had checked", "red", size=20)
lc_problem.note(380, 250, "Rotterdam opens on 27 April 2026", "pen")

lc_analogy = Doodle(760, 250, "Doodle of a pilot and co-pilot running the pre-flight checklist: one reads each item aloud, the other checks it and answers. Fuel, flaps, doors, instruments. Experienced pilots still use it, because memory fails under pressure.",
                     "Pilots still read the pre-flight checklist aloud, item by item, because memory fails under pressure.")
lc_analogy.icon("ledger", 40, 50, 1.5)
for i, t in enumerate(["fuel ✓", "flaps ✓", "doors ✓", "gauges ✓"]):
    lc_analogy.box(170 + i * 146, 70, 132, 56, t, "green", size=16)
lc_analogy.note(450, 200, "read aloud · checked · answered", "pen")

lc_how = Doodle(760, 370, "Grace's Rotterdam launch checklist, built 30 March 2026, with an owner per area. Product: zones, slots, prices and VAT checked by Joost. Test orders: five real addresses per zone, paid and refunded. Support: macros and Dutch help pages, two extra agents. Comms: push to the waitlist, email, local offer. Tracking: dashboards for Rotterdam. Rollback: close slots and show coming soon. People: on-call rota, Grace at the store. Go or no-go on 24 April: two items red, fixed by the 26th; go.",
                 "Areas, owners, a status per item, and a go / no-go two days before, with time to fix the reds.")
areas = [("product config", "Joost", "green"), ("test orders", "Ben", "green"), ("support", "Sam", "pink"), ("comms", "Grace", "green"),
         ("tracking", "Dee", "green"), ("rollback", "Eli", "green"), ("people", "Sanne", "green"), ("store", "Joost", "pink")]
for i, (a, o, f) in enumerate(areas):
    r, c = divmod(i, 4)
    x, y = 14 + c * 184, 14 + r * 100
    lc_how.box(x, y, 172, 86, a, f, sub=o, size=16)
lc_how.box(14, 230, 732, 70, None, "y")
lc_how.text(380, 260, "go / no-go, 24 Apr: 2 reds (Saturday slots, help pages)", "t-head", size=15)
lc_how.text(380, 286, "fixed by 26 Apr → go", size=15)
lc_how.note(380, 340, "every item has one owner and a status", "pen", size=17)

LAUNCH = dict(
    slug="launch-checklist",
    kicker="a.k.a. “the pre-flight checklist”",
    tldr="Code is the smallest part of a launch. Everything around it (configuration, test orders, support, communication, tracking, rollback, people on the day) fails quietly unless someone checks it. Keep a <b>launch checklist</b> grouped by <b>area</b>, with <b>one owner</b> and a <b>status</b> per item, and hold a <b>go / no-go</b> a few days before, early enough to <b>fix the reds</b>. Reuse it for every launch, and add whatever went wrong last time.",
    chips=[("Family", "shipping"), ("Origin", "aviation checklists; Atul Gawande, <i>The Checklist Manifesto</i> (2009)"), ("Lives in", "a shared checklist, reviewed at go / no-go"), ("Pairs with", "pre-mortem, definition of done, hypercare")],
    problem_side="Larder, 30 March 2026",
    problem="""  <p class="lead">Four weeks before Rotterdam opens, Joost tells Grace about store <b>Zuid's opening day</b> in November 2024: <b>340 products had no price</b>, support <b>learnt about the opening from customers</b>, and the first push message went to the wrong area. Nobody had a list; <span class="hl-pink">everybody assumed somebody else had checked</span>. Rotterdam is a whole new city, with a fixed date and a signed lease.</p>
  <ul>
    <li>Launch work outside the code has no home in the backlog.</li>
    <li>Each person checks their own part and assumes the rest is fine.</li>
    <li>Problems surface on launch day, in front of customers.</li>
  </ul>""",
    problem_figs=[lc_problem],
    meanwhile=[("architect-2", "one-way-two-way-doors", "Grace's launch checklist covers the product side of the same Rotterdam launch these 31 decisions were sorted for.", "In the same weeks, Grace runs the Rotterdam launch checklist: eight areas, eight owners, a go / no-go on 24 April.")],
    analogy_side="the pre-flight checklist",
    analogy="""  <p>Pilots with thousands of hours still run the <b>pre-flight checklist</b>: one reads each item aloud, the other <b>checks it and answers</b>. Fuel, flaps, doors, instruments. Not because they don't know how to fly, but because <b>memory fails under pressure</b>, and a forgotten item is expensive at 10,000 metres.</p>""",
    analogy_figs=[lc_analogy],
    map=[("The checklist", "Areas and items for the launch"),
         ("Read aloud, answered", "Each item has one owner who confirms it"),
         ("Fuel, flaps, doors", "Prices, test orders, support macros, rollback"),
         ("The pre-flight check", "Go / no-go on 24 April"),
         ("Not taking off", "No-go if a must-fix item is red")],
    how_side="areas, owners, a go / no-go",
    how="""  <p>Grace built the checklist from Zuid's story, the pre-mortem and Ana's open decisions: <b>eight areas</b>, one owner each. Joost's team checked every Rotterdam price; Ben placed five test orders per zone with real payments; Sam wrote Dutch help pages. At the <b>go / no-go on 24 April</b> two items were red (Saturday slot capacity too low, help pages unfinished); both were fixed by the 26th. Rotterdam opened on time, with every price.</p>""",
    how_figs=[lc_how],
    steps=[("Start from past failures", "Zuid's opening day, the pre-mortem, last launch's surprises."),
           ("Group by area", "Product config, test orders, support, comms, tracking, rollback, people, store."),
           ("One owner per item", "A name, not a team; they confirm it's done."),
           ("Track status openly", "Green, amber, red, visible to everyone."),
           ("Hold a go / no-go", "Two or three days before, so reds can be fixed."),
           ("Keep it for next time", "Add what went wrong; reuse it for Utrecht.")],
    vocab=[("Launch checklist", "Everything a launch needs, beyond the code, with owners."),
           ("Go / no-go", "The decision meeting before a launch."),
           ("Owner", "The one person who confirms an item."),
           ("Rollback plan", "How to undo or pause the launch."),
           ("Test order", "A real order placed to check the whole flow."),
           ("Launch day", "When customers first see it: not the time to discover gaps.")],
    code=dict(file="product/rotterdam/launch-checklist.md", note="Rotterdam launch checklist, status on 24 April 2026 (excerpt)", plain=True, src="""
# Rotterdam launch · 27 Apr 2026          go / no-go: Fri 24 Apr 14:00 · owner: Grace

PRODUCT CONFIG (Joost)   zones + postcodes loaded ✓ · slots per day ✗ Saturday too low
                         prices checked, 2,480 products ✓ · VAT ✓ · opening hours ✓
TEST ORDERS (Ben)        5 addresses per zone, paid and refunded ✓ · iDEAL + cards ✓
SUPPORT (Sam)            macros ✓ · Dutch help pages ✗ 3 of 7 · +2 agents on 27–30 Apr ✓
COMMS (Grace)            push to waitlist (4,100) Mon 07:00 ✓ · email ✓ · local offer ✓
TRACKING (Dee)           Rotterdam dashboards ✓ · alerts on failed payments ✓
ROLLBACK (Eli)           close slots + "coming soon" page, tested ✓
PEOPLE (Sanne)           on-call rota ✓ · Grace and Ben at the store 06:30–14:00 ✓
STORE (Joost)            4G router until the line is live (mid-May) ✓

Decision 24 Apr: GO, if Saturday slots and help pages are fixed by Sun 26 Apr → both ✓
"""),
    tools="tools: a shared doc or board with owners and statuses; a launch template reused per city. Your project tool's checklist feature works if everyone can see it.",
    gains=["<b>Nothing forgotten</b>: prices, support, rollback.",
           "<b>Clear owners</b>: no “I thought you checked”.",
           "<b>Reds found days early</b>, not on launch day.",
           "<b>Calm launch days</b>.",
           "<b>Reusable</b> for every new city."],
    losses=["<b>Upkeep</b>: statuses need chasing.",
            "<b>Can become box-ticking</b> without real checks.",
            "<b>Long lists</b> hide what matters most.",
            "<b>No-go is hard</b> on a fixed date."],
    baseline="Each line compares <b>launching on everyone's assumption that the rest is checked</b> to <b>a checklist by area with one owner per item and a go / no-go with time to fix the reds</b>.",
    ratings=[(2, 5, "Rotterdam's first customers saw every price and a working flow."),
             (2, 4, "The launch on a fixed date went to plan."),
             (2, 4, "Test orders prove the flow before customers do."),
             (3, 3, "Neutral."),
             (3, 4, "The reds get attention first."),
             (2, 5, "Everyone sees every area's status."),
             (2, 5, "Joost, Sam and Sanne see their items owned."),
             (2, 4, "Launch day without firefighting."),
             (3, 3, "A list and a go / no-go meeting.")],
    pitfalls=[("Code-only checklist", "“All stories done.”", "include config, support, comms, rollback, people."),
              ("Team owners", "“Support” owns help pages.", "one named person per item."),
              ("Go / no-go the day before", "No time to fix reds.", "two or three days before."),
              ("Starting from zero each time", "A new list for Utrecht.", "reuse and extend the last checklist.")],
    use=["Any launch customers will notice: new city, big feature, pricing change.",
         "Launches with operations and support involved.",
         "Fixed-date launches.",
         "Repeated launches (cities, countries)."],
    skip=["Small changes behind a flag with no customer-visible effect.",
          "Experiments with a handful of users."],
    related=["<b>Pre-mortem</b> (this volume)", "<b>Hypercare after launch</b> (this volume)", "<b>Go-live readiness</b> (Ana, book 1 vol. 6)", "<b>MoSCoW and its traps</b> (Vol. 2)"],
    quiz=[("What does a launch checklist cover besides code?", "Configuration, test orders, support, comms, tracking, rollback, people and the store."),
          ("Why one owner per item?", "So nobody assumes somebody else checked it."),
          ("When should go / no-go happen?", "Two or three days before, so reds can still be fixed."),
          ("What were the two reds for Rotterdam?", "Saturday slot capacity and the Dutch help pages.")],
    try_it="For your next launch, list eight areas beyond the code. Under each, write three items and one owner's name. Hold a 30-minute go / no-go three days before launch and fix every red before the day.",
    remember="Read it <span class=\"hl\">aloud</span>, item by item. <span class=\"hl\">Go / no-go</span> with time to fix.",
    sources=["Atul Gawande, <i>The Checklist Manifesto</i> (2009).",
             "Daniel Boorman, “Today's electronic checklists reduce likelihood of crew errors” (ICAO Journal, 2001).",
             "Atlassian Team Playbook, “Go/No-Go”.",
             "Marty Cagan, <i>Inspired</i>, 2nd ed. (2017), on product launches."],
)

# ------------------------------------------------------------------ 13 Dark Launches & Rollouts
dl_problem = Doodle(760, 280, "Doodle of the alternative Grace wanted to avoid in April 2026: switching approvals on for all of Amsterdam at once, on a Monday, with no way to tell if picking slows down at the Friday peak until it does, in front of every customer.",
                    "All of Amsterdam at once, on a Monday, and the first real test is Friday's peak.")
dl_problem.box(20, 40, 330, 100, "100 % on day 1", "pink", sub="all Amsterdam express", stroke="red")
dl_problem.box(410, 40, 330, 100, "Friday peak", "y", sub="first real load")
dl_problem.arrow(356, 90, 404, 90, color="red")
dl_problem.note(380, 200, "if picking slows, every customer feels it", "red", size=19)

dl_analogy = Doodle(760, 250, "Doodle of a restaurant's soft opening: the kitchen cooks the full menu for staff only first, then a friends-and-family night, then half the tables, then full service. Each step watches how long dishes take.",
                     "A soft opening: staff meal, friends and family, half the tables, full service, watching the kitchen at each step.")
for i, (t, f) in enumerate([("staff meal", "paper"), ("friends & family", "blue"), ("half the tables", "y"), ("full service", "green")]):
    x = 14 + i * 186
    dl_analogy.box(x, 60, 172, 70, t, f, size=14)
    if i < 3:
        dl_analogy.arrow(x + 174, 95, x + 184, 95)
dl_analogy.note(380, 190, "watch the kitchen at every step", "pen")

dl_how = Doodle(760, 360, "The approvals rollout in Amsterdam, April 2026. Dark launch from 6 April: the picker side live in every store, customers not asked yet, picking time measured. Then the customer side by flag: 10 percent on 13 April, 25 percent on the 15th, 50 percent on the 17th, 100 percent on the 20th. Guardrails: extra picking time per swap order at most 15 seconds, answer rate at least 70 percent, crash-free sessions at least 99.5 percent. At 50 percent, Friday's peak showed 18 seconds at Zuid: held over the weekend, handheld lag fixed, then 100 percent on Monday.",
                 "Dark first, then a percentage ramp with guardrails. When one guardrail tripped at 50 %, the ramp held.")
dl_how.line("M60 260 H720")
dl_how.line("M60 260 V40")
for x, pct, day in [(220, 10, "13 Apr"), (360, 25, "15 Apr"), (500, 50, "17 Apr"), (650, 100, "20 Apr")]:
    h = pct * 2
    dl_how.box(x - 40, 260 - h, 80, h, None, "green" if pct != 50 else "y", rx=3)
    dl_how.text(x, 252 - h, f"{pct} %", "t-head", size=15)
    dl_how.text(x, 282, day, size=14)
dl_how.box(64, 200, 60, 58, "dark", "paper", size=13, rx=3)
dl_how.text(94, 282, "6 Apr", size=14)
dl_how.note(440, 120, "Fri peak: +18 s at Zuid → hold", "red", size=16)
dl_how.note(380, 318, "guardrails: picking +≤15 s · answers ≥70 % · crash-free ≥99.5 %", "pen", size=15)
dl_how.note(380, 344, "kill switch: one flag, tested", "green", size=16)

DARK = dict(
    slug="dark-launches",
    kicker="a.k.a. “the soft opening”",
    tldr="Don't switch a big change on for everyone at once. <b>Dark launch</b> it first: live in production but invisible, or visible only on one side (here: pickers), so you can watch real load. Then <b>roll it out by percentage</b> behind a feature flag (10 %, 25 %, 50 %, 100 %), with <b>guardrail metrics</b> agreed in advance, a <b>kill switch</b>, and permission to <b>hold</b> when a guardrail trips.",
    chips=[("Family", "shipping"), ("Origin", "dark launches at Facebook (2008) and Flickr; progressive delivery (James Governor, 2018)"), ("Lives in", "the release plan and the flag tool"), ("Pairs with", "thin slices, guardrail metrics, feature flags")],
    problem_side="Larder, 6 April 2026",
    problem="""  <p class="lead">Slice 1 worked with Noord's staff. Now approvals goes to all of Amsterdam's express customers. The simplest plan: switch it on for <b>everyone on Monday 13 April</b>. But nobody knows what happens to <b>picking time at the Friday peak</b> with hundreds of swaps waiting for answers, and if it slows, <span class="hl-pink">every customer feels it at once</span>, on the busiest evening of the week.</p>
  <ul>
    <li>Big-bang releases test real load in front of every customer.</li>
    <li>Without agreed guardrails, nobody knows when to stop.</li>
    <li>Rolling back everything is slow and visible.</li>
  </ul>""",
    problem_figs=[dl_problem],
    analogy_side="the soft opening",
    analogy="""  <p>A new restaurant does a <b>soft opening</b>: the kitchen cooks the full menu for <b>staff</b> first, then a <b>friends-and-family</b> night, then <b>half the tables</b>, then full service. At each step the chef watches how long dishes take. If the kitchen falls behind at half the tables, they stay at half until it doesn't.</p>""",
    analogy_figs=[dl_analogy],
    map=[("The staff meal", "Dark launch: pickers' side live, customers not asked"),
         ("Friends and family", "10 % of Amsterdam's express customers"),
         ("Half the tables", "50 %, including a Friday peak"),
         ("Watching dish times", "Guardrails: picking time, answer rate, crashes"),
         ("Staying at half", "Holding the ramp when a guardrail trips")],
    how_side="dark first, then a ramp with guardrails",
    how="""  <p>From <b>6 April</b> the picker side ran dark in every Amsterdam store: pickers chose substitutes as if customers were asked, and Larder measured picking time. On <b>13 April</b> customers joined at 10 %, then 25 % and 50 %. On Friday 17 April, Zuid's picking time per swap order rose <b>18 seconds</b>, over the 15-second guardrail. The ramp <b>held at 50 %</b> over the weekend; Dee fixed a handheld lag; <b>100 %</b> on Monday 20 April.</p>""",
    how_figs=[dl_how],
    steps=[("Put it behind a flag", "On/off per user, per store, per percentage; test the kill switch."),
           ("Dark launch first", "Run it in production without showing it (or one side only) and measure."),
           ("Agree guardrails in advance", "Two or three numbers that must not get worse, with thresholds."),
           ("Ramp by percentage", "10 → 25 → 50 → 100 %, including at least one peak at 50 %."),
           ("Hold or roll back on a trip", "A tripped guardrail stops the ramp; no debate needed."),
           ("Remove the flag after", "Once at 100 % for a while, delete the old path.")],
    vocab=[("Dark launch", "Running new code in production without users seeing it."),
           ("Progressive rollout", "Increasing exposure step by step."),
           ("Feature flag", "A switch that turns a feature on for chosen users."),
           ("Guardrail metric", "A number that must not get worse during the rollout."),
           ("Kill switch", "Turning the feature off for everyone, instantly."),
           ("Canary", "A small group that sees the change first.")],
    code=dict(file="delivery/rollouts/approvals-amsterdam.md", note="rollout plan and log, April 2026", plain=True, src="""
# Rollout · approvals, Amsterdam express                 flag: approvals.customer

Dark    6 Apr   picker side live in Noord + Zuid; customers not asked; measure picking time
Ramp    13 Apr  10 %  · 15 Apr  25 %  · 17 Apr  50 %  · next  100 %
Guard-  picking time per swap order   ≤ +15 s vs dark baseline
rails   answered within 2 min         ≥ 70 %
        crash-free app sessions       ≥ 99.5 %
Kill    approvals.customer = off → swaps go back to "keep" (tested 10 Apr)

Log     13 Apr 10 %   answers 79 %, picking +6 s          continue
        15 Apr 25 %   answers 77 %, picking +8 s          continue
        17 Apr 50 %   Fri peak: Zuid picking +18 s ✗     HOLD (Dee: handheld lag)
        20 Apr 100 %  fix shipped Sat; picking +7 s       done; remove old path in May
"""),
    tools="tools: a feature-flag service (Unleash, LaunchDarkly, Flagsmith, Statsig) or a config table; dashboards for the guardrails; alerts when a guardrail trips.",
    gains=["<b>Real load tested</b> before customers depend on it.",
           "<b>Problems hit a few</b>, not everyone.",
           "<b>Clear stop rules</b>: guardrails decide.",
           "<b>Instant off</b> with a kill switch.",
           "<b>Calmer launches</b> for team and operations."],
    losses=["<b>Slower to reach everyone</b>: a week, not a day.",
            "<b>Flag code</b> to maintain and remove.",
            "<b>Two paths</b> to test while ramping.",
            "<b>Mixed experiences</b> for customers during the ramp."],
    baseline="Each line compares <b>switching a feature on for everyone at once</b> to <b>a dark launch, then a percentage ramp with agreed guardrails and a kill switch</b>.",
    ratings=[(2, 4, "Customers are protected from a slow Friday."),
             (2, 4, "The business case starts paying without a risky big bang."),
             (2, 5, "Guardrail numbers decide each step."),
             (2, 5, "Real-load problems found at 50 %, not 100 %."),
             (3, 4, "Exposure can grow or shrink in minutes."),
             (2, 4, "Everyone knows the ramp and the stop rules."),
             (2, 4, "Joost sees picking time protected."),
             (2, 4, "Small steps, each watched."),
             (3, 3, "Flags and dashboards to run.")],
    pitfalls=[("Ramping without guardrails", "“Looks fine” at each step.", "agree numbers and thresholds before 10 %."),
              ("Skipping the peak", "100 % before any Friday at 50 %.", "include a real peak at a middle step."),
              ("Untested kill switch", "It doesn't work when needed.", "test it before the ramp starts."),
              ("Flags forever", "Old paths and flags pile up.", "remove the flag once stable.")],
    use=["Features that change operations or load.",
         "Anything risky at peak times.",
         "Big changes to a high-traffic flow.",
         "When you need real data before full exposure."],
    skip=["Tiny copy or style changes.",
          "Legal changes that must apply to everyone at once."],
    related=["<b>Thin slices of value</b> (this volume)", "<b>Launch checklist</b> (this volume)", "<b>Feature flags</b> (patterns, Vol. 6)", "<b>Canary releases</b> (patterns, Vol. 6)"],
    quiz=[("What's a dark launch?", "Running new code in production without users seeing it, to measure real load."),
          ("What are guardrails for?", "Agreed numbers that stop the ramp when they get worse."),
          ("What happened at 50 %?", "Friday's peak pushed Zuid's picking time +18 s, over the 15 s guardrail, so the ramp held until a fix."),
          ("What should happen to the flag afterwards?", "Remove it and the old path once the feature is stable.")],
    try_it="For your next risky feature, write the rollout: what runs dark first, the percentage steps, three guardrails with thresholds, and how the kill switch works. Test the kill switch before the first step.",
    remember="<span class=\"hl\">Soft opening</span> first. Hold at half the tables if the <span class=\"hl\">kitchen</span> falls behind.",
    sources=["Facebook Engineering, on dark launches (Chuck Rossi and others, 2008–).",
             "James Governor, “Towards Progressive Delivery” (RedMonk, 2018).",
             "Pete Hodgson, “Feature Toggles (aka Feature Flags)” (martinfowler.com, 2017).",
             "Ronny Kohavi et al., <i>Trustworthy Online Controlled Experiments</i> (2020), on guardrail metrics."],
)

# ------------------------------------------------------------------ 14 Hypercare after Launch
hc_problem = Doodle(760, 280, "Doodle of the first days after Rotterdam opened on 27 April 2026: problems arrive through five channels: support tickets, the store manager's phone, couriers, a dashboard, a tweet. Nobody owns the whole picture; each problem is fixed by whoever hears about it first, or not at all.",
                    "Problems arrive through five channels after launch, and nobody owns the whole picture.")
for i, t in enumerate(["tickets", "store phone", "couriers", "dashboard", "social"]):
    hc_problem.box(20 + i * 148, 30, 132, 50, t, "paper", size=15)
    hc_problem.arrow(86 + i * 148, 84, 380, 150, dash=True)
hc_problem.box(230, 154, 300, 64, "who's on it?", "pink", stroke="red", size=18)
hc_problem.note(380, 262, "fixed by whoever hears first, or not at all", "red")

hc_analogy = Doodle(760, 250, "Doodle of a patient's path after surgery: intensive care with constant watching, then the ward with daily rounds, then home with a check-up. Each move happens when clear criteria are met.",
                     "After surgery: intensive care, then the ward, then home, each move on clear criteria.")
for i, (t, s, f) in enumerate([("intensive care", "constant watch", "pink"), ("the ward", "daily rounds", "y"), ("home", "a check-up", "green")]):
    x = 20 + i * 250
    hc_analogy.box(x, 60, 220, 84, t, f, sub=s, size=17)
    if i < 2:
        hc_analogy.arrow(x + 224, 102, x + 246, 102)
hc_analogy.note(380, 200, "move on when the criteria are met", "pen")

hc_how = Doodle(760, 360, "Rotterdam's hypercare, 27 April to 11 May 2026. Every day at 09:00, fifteen minutes: Grace, Sanne, Joost, Sam, Ben and Eli. One board: orders per day, express on time, tickets per 100 orders, top three issues with owners. Found and fixed: three streets missing from a zone, Saturday slots sold out by Thursday, an iDEAL error for one bank. Exit criteria: tickets under 3 per 100 orders two days running and no serious incident for five days. Met on 11 May; back to normal on-call.",
                 "Daily, short, one board, owners for each issue, and exit criteria agreed on day one.")
hc_how.box(14, 14, 360, 200, None, "y")
hc_how.head(194, 44, "09:00 · 15 min · daily", size=16)
for i, t in enumerate(["orders/day · on time (84 %)", "tickets per 100 orders", "top 3 issues + owners"]):
    hc_how.text(194, 84 + i * 36, t, size=15)
hc_how.text(194, 192, "Grace · Sanne · Joost · Sam · Ben · Eli", size=13)
hc_how.box(386, 14, 360, 200, None, "paper")
hc_how.head(566, 44, "found and fixed", size=16)
for i, t in enumerate(["3 streets missing from a zone", "Saturday slots full by Thursday", "iDEAL error, one bank"]):
    hc_how.text(566, 84 + i * 36, "✓ " + t, size=15)
hc_how.box(14, 236, 732, 70, "exit: tickets < 3 per 100, 2 days · no P1 for 5 days", "green", size=15)
hc_how.note(380, 340, "met on 11 May → normal on-call", "pen", size=17)

HYPERCARE = dict(
    slug="hypercare",
    kicker="a.k.a. “intensive care, then the ward”",
    tldr="The first weeks after a launch are when most problems show up, through many channels at once. Run a short <b>hypercare</b> period: a <b>daily 15-minute stand-up</b> with product, delivery, operations, support and engineering; <b>one board</b> with the few numbers that matter and the top issues, each with an <b>owner</b>; fast fixes; and <b>exit criteria agreed on day one</b>, so hypercare ends on purpose and hands over to normal operations.",
    chips=[("Family", "shipping"), ("Origin", "IT service management practice (early-life support in ITIL); go-live support in enterprise launches"), ("Lives in", "a daily stand-up and one board, for two weeks"), ("Pairs with", "launch checklist, dark launches, post-launch review")],
    problem_side="Larder, 28 April 2026",
    problem="""  <p class="lead">Rotterdam opened on 27 April. By the second morning, problems were arriving through <b>five channels</b>: support tickets, the store manager's phone, couriers, a dashboard alert, a tweet. Three customers were told “we don't deliver to your street” in the middle of a zone. <span class="hl-pink">Nobody owned the whole picture</span>; each problem was fixed by whoever heard about it first, or not at all.</p>
  <ul>
    <li>Post-launch problems scatter across channels and teams.</li>
    <li>Without one board, the same issue is reported three times or never.</li>
    <li>Without exit criteria, “launch mode” either ends too soon or never.</li>
  </ul>""",
    problem_figs=[hc_problem],
    meanwhile=[("architect-2", "technology-evaluation", "Grace's hypercare board is where Rotterdam's 84 % on time first showed up.", "Grace's Rotterdam hypercare board showed the 84 % on-time rate that made this evaluation urgent.")],
    analogy_side="intensive care, then the ward",
    analogy="""  <p>After surgery a patient goes to <b>intensive care</b> (constant watching), then the <b>ward</b> (daily rounds), then <b>home</b> with a check-up. Each move happens when <b>clear criteria</b> are met: stable for a day, eating, walking. Nobody stays in intensive care for a month “to be safe”, and nobody goes home from the operating table.</p>""",
    analogy_figs=[hc_analogy],
    map=[("Intensive care", "Hypercare: daily stand-up, one board, fast fixes"),
         ("Daily rounds", "09:00, 15 minutes, every day"),
         ("The patient's chart", "Orders, on time, tickets per 100 orders, top issues"),
         ("Criteria to move", "Tickets under 3 per 100 for two days, no P1 for five"),
         ("Home with a check-up", "Normal on-call, and a review a month later")],
    how_side="daily, one board, exit criteria",
    how="""  <p>From day two, Grace ran a <b>15-minute stand-up at 09:00</b> with Sanne, Joost, Sam, Ben and Eli, around one board. Three issues were found and fixed in the first week: <b>three streets missing from a zone</b> (postcode table), <b>Saturday slots sold out by Thursday</b> (capacity raised), and an <b>iDEAL error for one bank</b> (provider setting). The board also showed express on time at <b>84 %</b>, which went to Ana. Exit criteria were met on <b>11 May</b>; Rotterdam moved to normal on-call.</p>""",
    how_figs=[hc_how],
    steps=[("Agree exit criteria on day one", "Measurable: tickets per 100 orders, incidents, key flows working."),
           ("Daily, short, cross-team", "15 minutes: product, delivery, operations, support, engineering."),
           ("One board", "Three or four numbers and the top issues, each with one owner."),
           ("One way in", "All channels feed the board; no side fixes without a line."),
           ("Fix fast, decide fast", "Small fixes the same day; bigger ones go to the backlog with a date."),
           ("End on purpose", "When criteria are met, hand over to normal on-call; review in a month.")],
    vocab=[("Hypercare", "A short period of extra attention right after a launch."),
           ("Exit criteria", "Measurable conditions for ending hypercare."),
           ("P1", "The most serious kind of incident."),
           ("Early-life support", "ITIL's name for support right after go-live."),
           ("Handover", "Moving the service to normal operations."),
           ("Tickets per 100 orders", "Support load normalised by volume.")],
    code=dict(file="delivery/rotterdam/hypercare.md", note="Rotterdam hypercare board, end of week 1", plain=True, src="""
# Rotterdam hypercare · 27 Apr → (exit criteria met)           daily 09:00, 15 min

Exit criteria  tickets < 3 per 100 orders for 2 days in a row · no P1 for 5 days
               · payments, slots and tracking working in every zone

Numbers        Mon  Tue  Wed  Thu  Fri  Sat
orders           310  355  402  430  515  540
on time (%)       82   84   83   85   84   86
tickets /100     7.1  5.2  4.0  3.4  2.9  2.6

Issues         #1 3 streets in zone RTM-2 missing from postcode table   Ben   fixed Tue
               #2 Saturday slots full by Thursday                       Joost fixed Wed
               #3 iDEAL fails for one bank                              Cho   fixed Thu
               #4 express on time ~84 % (target 95 %)                   Eli   → Ana, routing (May)
Ended 11 May: criteria met; normal on-call; review on 8 June.
"""),
    tools="tools: one shared board (a doc, a Jira board, a Notion page), the launch dashboards, a channel all reports go to; a 15-minute recurring meeting.",
    gains=["<b>One picture</b> of every post-launch problem.",
           "<b>Owners and fast fixes</b>, days not weeks.",
           "<b>Calm for support and operations</b>.",
           "<b>Ends on purpose</b>, with criteria.",
           "<b>Bigger issues surface</b> (on-time) for the right people."],
    losses=["<b>Six people, 15 minutes a day</b>, for two weeks.",
            "<b>Can drag on</b> without exit criteria.",
            "<b>Side channels</b> creep back.",
            "<b>Fixes in a hurry</b> can add debt."],
    baseline="Each line compares <b>post-launch problems fixed by whoever hears first</b> to <b>a daily 15-minute hypercare stand-up with one board, owners and agreed exit criteria</b>.",
    ratings=[(2, 5, "Rotterdam's customers got fixes within a day."),
             (2, 4, "The new city reached normal quickly."),
             (2, 4, "Tickets per 100 orders tracked daily."),
             (2, 4, "Problems found and fixed in days."),
             (2, 4, "Top three issues, one owner each."),
             (2, 5, "Everyone sees the same board."),
             (2, 5, "Joost and Sam see their problems owned."),
             (2, 4, "Issues flow to owners, not to whoever hears."),
             (3, 3, "Fifteen minutes a day, two weeks.")],
    pitfalls=[("No exit criteria", "Hypercare for six weeks “to be safe”.", "measurable criteria on day one."),
              ("Side fixes", "Problems fixed in DMs, never on the board.", "every channel feeds one board."),
              ("Long stand-ups", "An hour every morning.", "15 minutes: numbers, top issues, owners."),
              ("No handover", "Hypercare ends; nobody owns what's left.", "hand remaining issues to normal on-call with owners.")],
    use=["New cities, stores or countries.",
         "Big launches touching operations and support.",
         "The first weeks of a migration.",
         "Any launch with a fixed date and many channels."],
    skip=["Small feature releases behind a flag.",
          "Launches with few users and one team."],
    related=["<b>Launch checklist</b> (this volume)", "<b>Dark launches &amp; rollouts</b> (this volume)", "<b>Handover to operations</b> (Ana, book 1 vol. 6)", "<b>Post-launch review</b> (Vol. 4)"],
    quiz=[("When should exit criteria be agreed?", "On day one of hypercare."),
          ("What's on the hypercare board?", "A few key numbers and the top issues, each with one owner."),
          ("What did Rotterdam's hypercare find?", "Missing streets in a zone, Saturday slots too low, an iDEAL error, and the 84 % on-time rate."),
          ("How does hypercare end?", "When the exit criteria are met, with a handover to normal on-call.")],
    try_it="For your next launch, write three exit criteria with numbers before the day. Book a 15-minute daily stand-up for two weeks with product, operations, support and engineering, and make one board the only place issues are tracked.",
    remember="<span class=\"hl\">Intensive care</span>, then the ward, then home, on <span class=\"hl\">criteria</span>.",
    sources=["AXELOS, <i>ITIL 4</i>, “Service validation and testing” and early-life support.",
             "Betsy Beyer et al., <i>Site Reliability Engineering</i> (2016), launch coordination.",
             "Gene Kim et al., <i>The DevOps Handbook</i> (2016), on post-release monitoring.",
             "Atul Gawande, <i>The Checklist Manifesto</i> (2009)."],
)

# ------------------------------------------------------------------ 15 Release Notes & Customer Comms
rn_problem = Doodle(760, 280, "Doodle of the first week of approvals in Amsterdam, April 2026: a pop-up nobody had explained. 140 support tickets: what is this pop-up? why are you charging me 40 cents? is this a scam? Sam's team had no prepared answers.",
                    "A pop-up nobody explained: 140 tickets in a week, one of them asking if it's a scam.")
for i, t in enumerate(["“what is this pop-up?”", "“why charge me €0.40?”", "“is this a scam?”"]):
    rn_problem.box(20 + (i % 2) * 20, 24 + i * 62, 380, 50, t, "pink", size=15, rx=6)
rn_problem.box(470, 50, 270, 110, "140 tickets", "y", sub="first week, Amsterdam")
rn_problem.note(380, 262, "the feature worked; the explanation didn't exist", "red")

rn_analogy = Doodle(760, 250, "Doodle of a train station announcement before a platform change: the train to Utrecht now leaves from platform 7, five minutes later, because of works; follow the yellow signs. Said before people go to the wrong platform, not after.",
                     "A platform change announced before people walk to the wrong platform: what, why, what to do.")
rn_analogy.icon("megaphone", 40, 60, 1.4)
for i, (t, s, f) in enumerate([("what", "platform 7", "y"), ("why", "works on the line", "paper"), ("what to do", "follow the signs", "green")]):
    rn_analogy.box(170 + i * 196, 60, 180, 84, t, f, sub=s, size=17, subsize=14)
rn_analogy.note(450, 210, "before, not after", "pen")

rn_how = Doodle(760, 360, "How approvals reached Rotterdam on 8 June 2026. To customers: an email the day before, a one-screen intro card on their first swap, a What's new note in the app. To staff: Sam's macros and a help article, a two-minute briefing for pickers at the Rotterdam store. Result in the first week: 1.4 support tickets per 1,000 approvals, against 6.1 in Amsterdam's first week.",
                 "Customers and staff, before the change: what, why, what to do. Tickets per 1,000 approvals fell from 6.1 to 1.4.")
rn_how.box(14, 14, 360, 210, None, "y")
rn_how.head(194, 46, "customers", size=17)
for i, t in enumerate(["email, the day before", "intro card on the first swap", "“What's new” in the app"]):
    rn_how.text(194, 88 + i * 40, t, size=15)
rn_how.box(386, 14, 360, 210, None, "blue")
rn_how.head(566, 46, "staff", size=17)
for i, t in enumerate(["Sam's macros + help article", "2-min briefing for pickers", "FAQ in the support tool"]):
    rn_how.text(566, 88 + i * 40, t, size=15)
rn_how.box(14, 244, 360, 70, "Amsterdam, wk 1", "pink", sub="6.1 tickets / 1,000 approvals")
rn_how.box(386, 244, 360, 70, "Rotterdam, wk 1", "green", sub="1.4 tickets / 1,000 approvals")

RELEASE_NOTES = dict(
    slug="release-notes",
    kicker="a.k.a. “the platform change announcement”",
    tldr="A feature customers don't understand looks like a bug, or a scam. For every change they'll notice, tell them <b>before</b> they meet it: <b>what</b> changed, <b>why</b> it's good for them, and <b>what to do</b>. Use the channels they already see (email, an intro card at the moment of use, a “what's new” note), and prepare the <b>staff</b> who'll be asked (support macros, help articles, a briefing for operations). Measure it: <b>tickets per 1,000 uses</b> in the first week.",
    chips=[("Family", "shipping"), ("Origin", "product marketing and change communication practice"), ("Lives in", "the launch checklist's comms area"), ("Pairs with", "launch checklist, MVP vs MLP, dark launches")],
    problem_side="Larder, 8 June 2026",
    problem="""  <p class="lead">When approvals reached all of Amsterdam in April, customers met a new pop-up with a countdown and a price, <b>unexplained</b>. In the first week Sam's team got <b>140 tickets</b>: <i>what is this pop-up?</i>, <i>why are you charging me €0.40?</i>, and one <i>is this a scam?</i> Support had no prepared answers. <span class="hl-pink">The feature worked; the explanation didn't exist.</span> Now approvals is going to Rotterdam.</p>
  <ul>
    <li>Changes customers notice without context feel like errors.</li>
    <li>Support learns about features from customers.</li>
    <li>The first impression of a good feature is confusion.</li>
  </ul>""",
    problem_figs=[rn_problem],
    analogy_side="the platform change",
    analogy="""  <p>A good station announces a <b>platform change</b> before people walk to the wrong platform: <b>what</b> (platform 7, five minutes later), <b>why</b> (works on the line), and <b>what to do</b> (follow the yellow signs). Staff on the platform know it too. Announced after the train has gone, it's just an apology.</p>""",
    analogy_figs=[rn_analogy],
    map=[("“Now from platform 7”", "What changed: you can approve swaps in the app"),
         ("“Because of works”", "Why: so you're never surprised at the door"),
         ("“Follow the yellow signs”", "What to do: tap yes or no within 2 minutes"),
         ("Staff on the platform", "Sam's team, with macros and a help article"),
         ("Announced before", "An email the day before, a card on the first swap")],
    how_side="before the change, customers and staff",
    how="""  <p>For Rotterdam on <b>8 June</b>, Grace and Noor prepared both sides. Customers got an <b>email the day before</b>, a <b>one-screen intro card</b> on their first swap (“we'll ask before we swap; the price difference is shown”), and a “what's new” note. Staff got <b>Sam's macros</b>, a help article, and a two-minute <b>briefing for Rotterdam's pickers</b>. First week: <b>1.4 tickets per 1,000 approvals</b>, against 6.1 in Amsterdam's first week.</p>""",
    how_figs=[rn_how],
    steps=[("List who'll notice", "Customers, pickers, couriers, support, business clients."),
           ("Write what, why, what to do", "Three short sentences, in the customer's words."),
           ("Use the moment of use", "An intro card the first time they meet it; not just an email."),
           ("Prepare staff first", "Macros, help article, a briefing, before customers ask."),
           ("Put it in the launch checklist", "Comms is an area with an owner."),
           ("Measure tickets per 1,000 uses", "In the first week; compare with the last launch.")],
    vocab=[("Release note", "A short description of what changed, for users."),
           ("Intro card", "A one-time explanation shown at first use."),
           ("Support macro", "A prepared answer for a common question."),
           ("Help article", "A page explaining a feature in detail."),
           ("Change communication", "Telling people about a change before they meet it."),
           ("Tickets per 1,000 uses", "Support questions normalised by usage.")],
    code=dict(file="product/approvals/comms-rotterdam.md", note="comms plan for approvals in Rotterdam, 8 June 2026", plain=True, src="""
# Approvals in Rotterdam · comms                       owner: Grace · with Noor, Sam

What     We'll ask before we swap. If an item runs out, you can say yes or no
         to the substitute in the app, within 2 minutes.
Why      So you're never surprised at the door.
Do       Tap yes or no. The price difference is shown; no answer = we keep the
         swap (or refund, if you've set that).

Customers  7 Jun  email to Rotterdam customers (NL, EN)
           8 Jun  intro card on the first swap (once) · "What's new" in the app
Staff      5 Jun  Sam: 4 macros + help article · 6 Jun briefing for RTM pickers (2 min)
Measure    tickets per 1,000 approvals, week 1   AMS (Apr): 6.1   RTM target: < 2
Result     RTM week 1: 1.4
"""),
    tools="tools: your email tool, in-app messaging (Intercom, Braze, a simple feature-intro component), the help centre, and the support tool's macros; the launch checklist to track it.",
    gains=["<b>Fewer confused customers</b> and tickets.",
           "<b>A better first impression</b> of good features.",
           "<b>Support ready</b> before the first question.",
           "<b>Trust</b>: no “is this a scam?”.",
           "<b>A number to improve</b>: tickets per 1,000 uses."],
    losses=["<b>Writing and translating</b> takes time.",
            "<b>Intro cards annoy</b> if overused.",
            "<b>Emails get ignored</b>; the moment of use matters more.",
            "<b>Easy to forget</b> without an owner."],
    baseline="Each line compares <b>shipping a visible change without explaining it</b> to <b>telling customers and staff before: what, why, what to do, at the moment of use</b>.",
    ratings=[(2, 5, "Customers understand the new step the first time."),
             (2, 4, "Fewer tickets, better adoption of approvals."),
             (2, 4, "Tickets per 1,000 uses compared across launches."),
             (3, 3, "Neutral."),
             (3, 3, "Neutral."),
             (2, 4, "Support and pickers know before customers ask."),
             (2, 5, "Sam's team is ready on day one."),
             (3, 4, "Fewer tickets interrupting the team."),
             (3, 3, "A few hours of writing per launch.")],
    pitfalls=[("No explanation", "A pop-up appears; customers guess.", "what, why, what to do, at the moment of use."),
              ("Email only", "Nobody reads it.", "an intro card the first time they meet it."),
              ("Staff last", "Support learns from customers.", "brief staff before customers see it."),
              ("Intro cards for everything", "Every small tweak gets a card.", "only changes customers will notice and wonder about.")],
    use=["Any change customers will notice.",
         "New steps in a flow, new prices, new rules.",
         "Launches in new cities or languages.",
         "Changes that support will be asked about."],
    skip=["Invisible improvements (speed, fixes).",
          "Experiments to a small group: a lighter note."],
    related=["<b>Launch checklist</b> (this volume)", "<b>MVP vs MLP</b> (this volume)", "<b>Hypercare after launch</b> (this volume)", "<b>Product update that gets read</b> (Vol. 5)"],
    quiz=[("What three things should every change message say?", "What changed, why it's good for them, and what to do."),
          ("Why an intro card, not just an email?", "Customers meet the change at the moment of use; emails are often ignored."),
          ("Who should be prepared before customers?", "Support, pickers and anyone customers will ask."),
          ("What measure did Grace use?", "Support tickets per 1,000 approvals in the first week.")],
    try_it="For your next visible change, write three sentences (what, why, what to do) and test them on two people outside the team. Prepare support with macros a day before, add a one-time intro card, and count tickets per 1,000 uses in week one.",
    remember="Announce the <span class=\"hl\">platform change</span> before people walk to the wrong one. Staff <span class=\"hl\">first</span>.",
    sources=["Intercom, <i>Intercom on Onboarding</i> (2016).",
             "Kathy Sierra, <i>Badass: Making Users Awesome</i> (2015).",
             "Nielsen Norman Group, “Onboarding Tutorials vs. Contextual Help” (2020).",
             "Martina Lauchengco, <i>Loved</i> (2022), on product marketing."],
)

NOTES = [LAUNCH, DARK, HYPERCARE, RELEASE_NOTES]
