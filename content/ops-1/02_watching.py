# Series 2 · Book 5 · The IT Operations Notebook · Vol. 1 · Watching it.
# Narrator: Eli (he/him). Facts: docs/larder-casebook.md, "Book 5, Vol. 1".

# ------------------------------------------------------------------ 06 Who Gets Woken Up?
oc_problem = Doodle(760, 250, "Doodle of Larder's on-call before April 2026: one phone, Eli's, on for 52 weeks a year. In the week of 23 March he was on call and at 160 percent, so Ana swapped in. Nobody had a list of who could take a page, what they'd need, or who to call if they got stuck.",
                    "One phone, 52 weeks a year. When it was Eli's 160 % week, Ana stepped in, with no handover.")
oc_problem.icon("phone", 60, 30, 1.8)
oc_problem.box(170, 40, 300, 90, "on call: Eli", "pink", sub="52 weeks a year", size=21, subsize=15)
oc_problem.box(500, 40, 246, 90, "backup", "paper", sub="nobody", dash=True, size=20, subsize=15)
oc_problem.note(380, 190, "week of 23 March: Ana swaps in, no handover", "red", size=18)

oc_analogy = Doodle(760, 230, "Doodle of a village doctors' practice with a weekend rota pinned to the door. Six doctors take turns, one weekend in six. On Friday afternoon the doctor going off call tells the next one about the two patients to watch. If the on-call doctor is stuck, there's a named senior to phone. After a night of call-outs, they start late on Monday.",
                    "Six doctors, one weekend in six, a Friday handover, and a senior to phone if stuck.")
oc_analogy.row([("Dr A", "wk 1", "green"), ("Dr B", "wk 2", "paper"), ("Dr C", "wk 3", "paper"), ("Dr D", "wk 4", "paper"), ("Dr E", "wk 5", "paper"), ("Dr F", "wk 6", "paper")], y=30, h=70, gap=10, size=17, subsize=14)
oc_analogy.note(380, 140, "Friday: “watch these two patients”", "pen", size=18)
oc_analogy.note(380, 180, "stuck? phone the senior · bad night? start late", "pen", size=17)

oc_how = Doodle(760, 340, "Larder's on-call rota v1, from Monday 20 April 2026. Five people take a week each in turn: Eli, Ben, Cho, Dee and Ana. Each week has a primary and a secondary; the secondary is next week's primary. The handover is Monday at 10:00 for 15 minutes. Eli is the escalation point for the first two months. Paid: 200 euros a week, and if you're paged after midnight you start at noon. The rota covers the critical and important services in the catalogue.",
                "Primary, secondary, Monday handover, a named escalation, and rest after a bad night.")
for i, (n, f) in enumerate([("Eli", "green"), ("Ben", "paper"), ("Cho", "paper"), ("Dee", "paper"), ("Ana", "paper")]):
    oc_how.box(14 + i * 148, 14, 136, 70, n, f, sub=f"from {['20 Apr', '27 Apr', '4 May', '11 May', '18 May'][i]}", size=19, subsize=13)
oc_how.box(14, 112, 360, 80, "primary + secondary", "blue", sub="secondary = next week's primary", size=17, subsize=14)
oc_how.box(386, 112, 360, 80, "handover Mon 10:00", "y", sub="15 min · open issues · changes", size=17, subsize=14)
oc_how.box(14, 214, 360, 80, "€200 a week", "green", sub="paged after midnight → start at noon", size=17, subsize=14)
oc_how.box(386, 214, 360, 80, "stuck? call Eli", "pink", sub="first two months", size=17, subsize=14)
oc_how.note(380, 326, "one week in five each", "pen", size=17)

ON_CALL = dict(
    slug="on-call-rota",
    kicker="a.k.a. “who carries the pager”",
    tldr="An <b>on-call rota</b> shares the job of answering alerts out of hours. Each week has a <b>primary</b> who is paged and a <b>secondary</b> who backs them up. There's a short <b>handover</b>, a named person to <b>escalate</b> to, and <b>rest and pay</b> for the disruption. The aim is that the business is covered and that no single person <b>is</b> the pager.",
    chips=[("Family", "watching it"), ("Lives in", "ops/on-call.md and the paging tool's schedule"), ("Pairs with", "alert hygiene, runbooks, escalation (vol. 2)")],
    itil=dict(groups=["service", "general"], chain=["deliver"], practices=["incident management (readiness)", "workforce and talent management"],
              sre="“on-call”: a primary and a secondary, at most a quarter of time on call", principles=["Collaborate and promote visibility"],
              older="ITIL v3: operations management, the service desk's out-of-hours cover"),
    problem_side="Larder, April 2026",
    problem="""  <p class="lead">Until April 2026 Larder's on-call is <b>one phone, Eli's, 52 weeks a year</b>. In the week of 23 March he was on call and loaded at 160 %, so Ana swapped in. <span class="hl-pink">She had no list of what she was covering, no runbooks and nobody to call but Eli.</span> Rotterdam opens on 27 April and will add a third store to the night.</p>
  <ul>
    <li>One person can't be reachable forever without burning out.</li>
    <li>Swaps happen in a hurry, with no handover.</li>
    <li>Everyone else stays unable to help.</li>
  </ul>""",
    problem_figs=[oc_problem],
    analogy_side="the village doctors' weekend rota",
    analogy="""  <p>A village practice has six doctors and <b>a weekend rota on the door</b>: one weekend in six each. On Friday afternoon the doctor going off duty tells the next one about <b>the two patients to watch</b>. If the on-call doctor is stuck, there's a <b>named senior</b> to phone. After a night of call-outs, they start late on Monday. Nobody thinks this is luxury. It's how the village keeps its doctors.</p>""",
    analogy_figs=[oc_analogy],
    map=[("Six doctors on a rota", "Eli, Ben, Cho, Dee and Ana, a week each"),
         ("Friday handover", "Monday 10:00, 15 minutes"),
         ("Patients to watch", "Open issues, changes this week, known weak spots"),
         ("The senior to phone", "Eli, as escalation, for the first two months"),
         ("Start late after a bad night", "Paged after midnight → start at noon")],
    how_side="a rota, a pair, a handover, an escalation and rest",
    how="""  <p>Eli asks for volunteers at tech leads on <b>16 April</b> and gets four: Ben, Cho, Dee and Ana. With him that's five, <b>one week in five</b> each, starting <b>Monday 20 April</b>, a week before Rotterdam opens. Each week has a <b>primary</b> (paged first) and a <b>secondary</b> (next week's primary, who learns along the way). Eli is the escalation point for the first two months, until the runbooks exist.</p>
  <p>The handover is <b>Monday 10:00, 15 minutes</b>: open issues, changes planned this week, anything flaky. Marco agrees <b>€200 a week</b> for the primary. The rule everyone likes best: <b>paged after midnight, start at noon</b>. The rota covers the critical and important tiers in the catalogue. Normal-tier services wait for office hours.</p>""",
    how_figs=[oc_how],
    steps=[("Decide what on-call covers", "The critical and important tiers, not everything."),
           ("Find at least four people", "Fewer than four, and it isn't a rota."),
           ("Pair a primary with a secondary", "The secondary is next week's primary."),
           ("Hold a short handover", "Open issues, changes, weak spots: 15 minutes."),
           ("Name an escalation", "Who to call when stuck, and that calling is fine."),
           ("Pay for it and protect rest", "Money for the week, time back after a bad night.")],
    vocab=[("On-call", "Being reachable to respond to alerts outside working hours."),
           ("Primary", "The person paged first."),
           ("Secondary", "The backup if the primary doesn't answer, or needs help."),
           ("Handover", "A short meeting where one on-call person briefs the next."),
           ("Escalation", "Calling in someone more senior or more specialised."),
           ("Time off in lieu", "Rest given back after out-of-hours work.")],
    code=dict(file="ops/on-call.md", note="rota v1 · from Mon 20 April 2026", plain=True, src="""
# On-call at Larder

covers      critical + important services (ops/catalogue.md)
rota        Eli · Ben · Cho · Dee · Ana   (one week in five, Mon 10:00 → Mon 10:00)
roles       primary (paged first) · secondary (= next week's primary)
handover    Mon 10:00, 15 min: open issues · changes this week · flaky things
escalate    Eli, any time, until 20 June; calling is never a failure
pay         €200 / week as primary (agreed with Marco, 17 Apr)
rest        paged after 00:00 → start at 12:00; two bad nights → swap out
swaps       arrange it yourselves, then update the schedule (not just the chat)
"""),
    tools="tools: a paging tool with schedules and escalation (many have a free tier for small teams), a shared calendar, ops/on-call.md.",
    ladder=[("one person, always", ["No backup.", "Swaps in a panic."]),
            ("a written rota", ["Primary, secondary, handover.", "Pay and rest agreed."]),
            ("schedules in the paging tool", ["Escalation is automatic.", "Swaps in the tool."]),
            ("load measured", ["Pages per shift tracked.", "Rota adjusted when it's too heavy."])],
    ladder_now=2,
    baseline="Each line compares <b>one engineer on call all year</b> to <b>a paid five-person rota with a handover and escalation</b>.",
    ratings=[(2, 3, "Someone always answers."),
             (3, 3, "Neutral."),
             (2, 3, "Faster acknowledgement; slower fixes until runbooks exist."),
             (3, 3, "Neutral."),
             (2, 3, "The handover makes open issues visible."),
             (3, 3, "Neutral."),
             (3, 3, "€200 a week, cheaper than losing Eli."),
             (1, 4, "One week in five, with rest."),
             (3, 3, "15 minutes a week.")],
    pitfalls=[("A rota of two", "That's 26 weeks a year each: still burnout.", "at least four people."),
              ("No runbooks yet", "New people are paged into things only one person understands.", "write runbooks for every paging alert (this volume)."),
              ("Unpaid, unspoken", "Resentment grows, then people leave.", "agree pay and rest before the first week."),
              ("Swaps only in chat", "The tool pages the wrong person.", "swap in the schedule.")],
    use=["One person carries the pager.", "Before a launch that adds load at night.", "Someone has swapped in without a handover.", "People are afraid to take a week."],
    skip=["Nothing you run needs a response before morning: say so and write it down."],
    related=["<b>Which Alerts Deserve a Human?</b> (this volume)", "<b>What Do I Do at 3 a.m.?</b> (this volume)", "<b>Who's Next If Nobody Answers?</b> (vol. 2)", "<b>Who Is Overloaded?</b> (Sanne, vol. 4)"],
    quiz=[("What does the secondary do?", "Backs up the primary if they don't answer or need help, and learns, since they're next week's primary."),
          ("Why at least four people?", "Fewer means being on call a quarter of the year or more: too much to last."),
          ("What goes into the handover?", "Open issues, changes planned this week, and anything flaky."),
          ("What's Larder's rule after a bad night?", "Paged after midnight → start at noon."),
          ("Which services does Larder's rota cover?", "The critical and important tiers in the catalogue; normal waits for office hours.")],
    quiz_sit=[("Ben is primary and gets paged three nights in a row. What should happen?", "He swaps out after the second bad night, as agreed, and the alerts that paged him go to the next alert review: three nights in a row is a signal, not bad luck.")],
    try_it="Write down who can be called tonight if your most important service stops. How many names are there? Draft a rota with a primary, a secondary, a handover time and a rule for rest.",
    remember="On-call is a <span class=\"hl\">rota</span>, not a person. If one name is always on it, the system depends on one person's sleep.",
    sources=["Betsy Beyer et al., <i>Site Reliability Engineering</i> (2016): chapter 11, being on-call.",
             "AXELOS, <i>ITIL 4: Incident management</i> and <i>Workforce and talent management</i> practice guides (2020).",
             "PagerDuty, <i>Incident Response documentation</i> (open source): on-call roles."],
)

# ------------------------------------------------------------------ 07 How Do We Know It's Broken?
mo_problem = Doodle(760, 260, "Doodle of Larder's dashboards in April 2026: twelve graphs of CPU, memory and disk for three virtual machines and the database. All green. Meanwhile Sam's support team gets six chats in ten minutes saying payment fails with iDEAL. The graphs watch the machines; nothing watches the orders.",
                    "Twelve green graphs, and customers telling support that payment fails.")
for i in range(6):
    r, c = divmod(i, 3)
    mo_problem.box(14 + c * 150, 20 + r * 96, 138, 80, ["CPU", "memory", "disk", "CPU db", "IOPS", "load"][i], "green", sub="ok", size=16, subsize=14)
mo_problem.box(484, 40, 262, 140, "support chat", "pink", sub="“iDEAL fails” × 6", size=19, subsize=15)
mo_problem.note(380, 236, "the machines are fine; the orders aren't", "red", size=19)

mo_analogy = Doodle(760, 220, "Doodle of a bakery owner who watches the queue and the shelves, not the oven thermometer. If the queue is long and the shelves are empty, something's wrong, whatever the oven says. The oven thermometer helps her find out why.",
                    "Watch the queue and the shelves first. The oven thermometer tells you why, not whether.")
mo_analogy.icon("store", 70, 40, 1.6)
mo_analogy.box(200, 40, 260, 100, "queue + shelves", "green", sub="is it working?", size=19, subsize=15)
mo_analogy.box(490, 40, 256, 100, "oven thermometer", "paper", sub="why isn't it?", size=19, subsize=15)
mo_analogy.note(380, 190, "symptoms first, causes second", "pen", size=18)

mo_how = Doodle(760, 380, "Larder's monitoring from 14 April 2026, in two layers. Top layer, what customers and stores feel: orders per five minutes per city compared with the same time last week; checkout error rate; checkout speed (95th percentile); Dispatch assignment delay; store heartbeat (the picker app's last sync from each store). Bottom layer, what explains it: CPU, memory, disk, database connections, queue length. On opening day, 27 April, at 12:10, the Rotterdam store heartbeat alert fired: the 4G router had dropped for 6 minutes. The picker app kept working offline and orders continued.",
                "Two layers: what users feel on top, what explains it below. Rotterdam's heartbeat caught the 4G drop on opening day.")
mo_how.head(380, 30, "what users feel (alerts come from here)", size=17)
for i, (t, s) in enumerate([("orders / 5 min", "vs last week"), ("checkout errors", "%"), ("checkout p95", "ms"), ("Dispatch delay", "s"), ("store heartbeat", "last sync")]):
    mo_how.box(14 + i * 148, 46, 136, 80, t, "green" if i < 4 else "y", sub=s, size=14, subsize=13)
mo_how.line("M14 160 h732", thin=True, dash=True)
mo_how.head(380, 190, "what explains it (look here next)", size=17)
for i, t in enumerate(["CPU", "memory", "disk", "DB connections", "queue length"]):
    mo_how.box(14 + i * 148, 206, 136, 56, t, "paper", size=14)
mo_how.box(110, 290, 540, 64, "27 Apr 12:10 · Rotterdam heartbeat: 6 min · picker app offline-first", "y", size=15)

MONITORING = dict(
    slug="monitoring",
    kicker="a.k.a. “monitoring and event management”",
    tldr="Monitoring answers two questions: <b>is it working for users?</b> and, if not, <b>why?</b> Watch the first one directly: orders per minute, errors, speed, and whether each store's devices are syncing. Alert on that. Then keep machine graphs (CPU, disk, connections) to <b>explain</b> what you see. Green machines with failing orders is the most common blind spot.",
    chips=[("Family", "watching it"), ("Lives in", "one dashboard per critical service, the alert rules in the repo"), ("Pairs with", "alert hygiene, the dependency map, SLOs (vol. 4)")],
    itil=dict(groups=["service"], chain=["deliver", "improve"], practices=["monitoring and event management"],
              sre="the four golden signals: latency, traffic, errors, saturation", principles=["Focus on value"],
              older="ITIL v3: event management"),
    problem_side="Larder, 9 April 2026",
    problem="""  <p class="lead">Larder's dashboards in April 2026 show twelve graphs: CPU, memory and disk for the three VMs and the database. On Thursday <b>9 April</b> at 18:20 they are all green. At the same moment Sam's support team gets <b>six chats in ten minutes</b>: iDEAL payment fails. <span class="hl-pink">The graphs watch the machines; nothing watches the orders.</span> Support found out first, and Eli found out from Sam.</p>
  <ul>
    <li>Customers are the alarm.</li>
    <li>Failures outside our machines (the PSP, a store's Wi-Fi) are invisible.</li>
    <li>Rotterdam's store, on a 4G router, has no monitoring at all.</li>
  </ul>""",
    problem_figs=[mo_problem],
    analogy_side="the bakery queue",
    analogy="""  <p>A bakery owner doesn't stare at the oven thermometer to know if the morning is going well. She watches <b>the queue and the shelves</b>. A long queue and empty shelves means trouble, whatever the oven says. When that happens, the thermometer helps her find out <b>why</b>.</p>""",
    analogy_figs=[mo_analogy],
    map=[("Queue length", "Orders per 5 minutes, per city, vs last week"),
         ("Empty shelves", "Checkout errors, slow checkout, Dispatch falling behind"),
         ("Each shop's lights on", "Store heartbeat: each picker app's last sync"),
         ("The oven thermometer", "CPU, memory, disk, DB connections"),
         ("Asking customers how it went", "Support chats: still useful, but not as the alarm")],
    how_side="watch what users feel; keep the rest to explain it",
    how="""  <p>Eli builds a top row of five signals for the critical services. He uses the <b>four golden signals</b> (traffic, errors, latency, saturation) and adds one of Larder's own:</p>
  <ul>
    <li><b>Orders per 5 minutes per city</b>, against the same 5 minutes last week. A sudden gap means something is wrong, wherever it is: in Core, at the PSP or in DNS.</li>
    <li><b>Checkout error rate</b> and <b>checkout p95</b> (95 % of checkouts are faster than this).</li>
    <li><b>Dispatch assignment delay</b>: how long a packed order waits for a courier.</li>
    <li><b>Store heartbeat</b>: the last sync from each store's picker app. No sync for 5 minutes means a store is cut off.</li>
  </ul>
  <p>Machine graphs move to a second row, to look at <b>after</b> an alert. On opening day, <b>27 April</b>, at <b>12:10</b>, the Rotterdam heartbeat alert fires: the 4G router has dropped for 6 minutes. The picker app keeps working offline (ADR 0004) and orders continue. This time Eli knows before Yara calls.</p>""",
    how_figs=[mo_how],
    steps=[("Start from the catalogue's critical services", "One dashboard each."),
           ("Pick the signals users feel", "Traffic, errors, latency, plus your own (orders, heartbeat)."),
           ("Compare with a normal baseline", "Same time last week beats a fixed threshold for traffic."),
           ("Watch from outside too", "A check from outside the cloud catches DNS and certificates."),
           ("Keep machine graphs for explaining", "Second row, not the alarm."),
           ("Test that alerts reach someone", "Fire a fake one before you rely on it.")],
    vocab=[("Monitoring", "Collecting signals about a system and watching them."),
           ("Event", "Any change of state worth noticing; some events become alerts."),
           ("Golden signals", "Latency, traffic, errors and saturation."),
           ("Symptom vs cause", "What users feel (slow checkout) vs why (DB connections full)."),
           ("Heartbeat", "A regular “I'm alive” signal; silence is the alarm."),
           ("Synthetic check", "A robot that uses the service from outside, like a customer.")],
    code=dict(file="ops/monitoring/checkout.yml", note="top-row signals · 14 April 2026", plain=True, src="""
service: checkout          owner: Ben         tier: critical
signals:
  orders_per_5min:   by city · compare with same 5 min last week
                     alert if < 50 % for 10 min (17:00–20:00: < 70 % for 5 min)
  checkout_errors:   alert if > 2 % for 5 min
  checkout_p95:      alert if > 1,500 ms for 10 min   (target 800 ms at 5× peak)
  synthetic_order:   every 5 min from outside the cloud, test basket, no payment
explain (no alerts):
  core CPU · memory · disk · db connections · db CPU · queue length
stores:
  heartbeat:         picker app last sync per store; alert if > 5 min, 07:00–23:00
"""),
    tools="tools: whatever metrics stack you have (most clouds include one), an outside synthetic check, and the paging tool. The tool matters less than which signals you choose.",
    ladder=[("customers are the alarm", ["Support finds out first.", "Machine graphs only."]),
            ("user-facing signals on a dashboard", ["Orders, errors, speed, heartbeats.", "Alerts on those."]),
            ("monitoring as code", ["Signals and alerts in the repo.", "Every new service starts with them."]),
            ("SLOs drive it", ["Alerts on error budget burn (vol. 4).", "Dashboards generated per service."])],
    ladder_now=2,
    baseline="Each line compares <b>twelve machine graphs</b> to <b>user-facing signals with machine graphs underneath</b>.",
    ratings=[(1, 3, "Problems found before customers report them."),
             (3, 3, "Neutral on its own."),
             (2, 4, "Alerts point at the symptom straight away."),
             (2, 3, "A drop in orders after a change shows up at once."),
             (1, 4, "Stores and outside services become visible."),
             (3, 3, "Neutral."),
             (3, 3, "A few hours; existing tools."),
             (2, 3, "Fewer surprises at night."),
             (3, 3, "Two days to set up.")],
    pitfalls=[("Watching only machines", "Green graphs, broken checkout.", "alert on what users feel."),
              ("Fixed thresholds for traffic", "Sunday morning looks like an outage.", "compare with the same time last week."),
              ("Monitoring from inside only", "If the region or DNS fails, the monitor fails with it.", "add a check from outside."),
              ("Never testing the alert", "The first real alert goes to an old phone number.", "fire a test alert monthly.")],
    use=["Customers or support find problems first.", "You have dashboards but no user-facing signals.", "A new site or service is going live.", "Outside services sit on your critical path."],
    skip=["A batch job nobody waits for: check it in the morning instead."],
    related=["<b>Which Alerts Deserve a Human?</b> (next note)", "<b>Logs, Metrics & Traces</b> (cloud, vol. 6)", "<b>Health Checks & Probes</b> (cloud, vol. 6)", "<b>Performance Budgets</b> (Ana, vol. 5)"],
    quiz=[("What are the four golden signals?", "Latency, traffic, errors and saturation."),
          ("Why compare orders with the same time last week?", "Traffic changes with the hour and day; a fixed threshold would alarm every Sunday morning."),
          ("What is a heartbeat, and why does Larder use one per store?", "A regular “I'm alive” signal. Silence from a store's picker app means the store is cut off, even though our servers are fine."),
          ("What are machine graphs for, if not alerts?", "Explaining why a user-facing signal went bad."),
          ("Why add a check from outside the cloud?", "If DNS, a certificate or the whole region fails, inside monitoring fails with it.")],
    quiz_sit=[("Orders in Amsterdam drop by 60 % at 18:30 on a Friday, and every machine graph is green. Where do you look first?", "Outside our machines: the PSP's status, DNS, the certificate, the address lookup service. Follow the checkout dependency map, and look at errors by step.")],
    try_it="Write down how you learned about your last three problems. If any came from a customer or a colleague, choose one signal that would have told you first, and set it up this week.",
    remember="Watch the <span class=\"hl\">queue and the shelves</span>, not the oven. Alert on what users feel; use the machines to explain it.",
    sources=["Betsy Beyer et al., <i>Site Reliability Engineering</i> (2016): chapter 6, monitoring distributed systems.",
             "AXELOS, <i>ITIL 4: Monitoring and event management</i> practice guide (2020).",
             "Charity Majors, Liz Fong-Jones and George Miranda, <i>Observability Engineering</i> (2022)."],
)

# ------------------------------------------------------------------ 08 Which Alerts Deserve a Human?
ah_problem = Doodle(760, 260, "Doodle of March 2026's pages: 410 pages from 63 alert rules. Of those, 9 needed a human to do something. The rest were CPU spikes during the nightly backup, a disk at 81 percent that had been at 81 percent for a year, and the same stock-sync warning every 20 minutes. People had started muting the phone.",
                    "410 pages in March. Nine of them needed a person. People had started muting the phone.")
ah_problem.box(14, 30, 230, 110, "410 pages", "pink", sub="63 rules · March", size=24, subsize=15)
ah_problem.box(264, 30, 230, 110, "9", "green", sub="needed a human", size=34, subsize=15)
ah_problem.box(514, 30, 232, 110, "401", "paper", sub="noise", size=34, subsize=15)
ah_problem.note(380, 190, "backup CPU spikes · disk at 81 % for a year · stock-sync × every 20 min", "pen", size=15)
ah_problem.note(380, 230, "the phone goes on mute", "red", size=19)

ah_analogy = Doodle(760, 230, "Doodle of a smoke alarm that goes off every time someone makes toast. After a week the family takes the battery out. Then there's a real fire. The fix isn't to ignore the alarm; it's to move it away from the toaster and make it ring only for smoke that matters.",
                    "A smoke alarm that rings for toast ends up with its battery out.")
ah_analogy.icon("bell", 80, 40, 1.6)
ah_analogy.row([("toast", "rings", "y"), ("toast", "rings", "y"), ("battery out", None, "pink"), ("real fire", "silence", "pink")], x=200, y=40, h=90, gap=40, size=17, subsize=14, arrows=True)
ah_analogy.note(470, 190, "move the alarm, don't remove it", "pen", size=18)

ah_how = Doodle(760, 360, "Eli's alert review, 15 April 2026 (the half-day alert fix from Sanne's levelling). Every one of the 63 rules goes through four questions: does it mean customers are hurt now or soon? does it need a human? is the action urgent? is there a runbook? Result: 6 rules page, 8 become tickets for the morning, 49 are deleted or moved to dashboards. In May: 22 pages, 17 of them needed action.",
                "Four questions per alert. 63 rules → 6 that page, 8 that wait for morning.")
for i, q in enumerate(["customers hurt now?", "needs a human?", "urgent?", "runbook exists?"]):
    ah_how.box(14 + i * 186, 14, 172, 70, q, "paper", size=15)
    if i:
        ah_how.arrow(14 + i * 186 - 12, 49, 14 + i * 186 - 2, 49)
ah_how.box(14, 120, 230, 100, "page", "pink", sub="6 rules", size=22, subsize=16)
ah_how.box(264, 120, 230, 100, "ticket", "y", sub="8 rules · next morning", size=22, subsize=15)
ah_how.box(514, 120, 232, 100, "dashboard / delete", "paper", sub="49 rules", size=19, subsize=16)
ah_how.row([("March", "410 pages · 9 useful", "pink"), ("May", "22 pages · 17 useful", "green")], x=110, y=256, h=72, w=250, gap=40, size=18, subsize=14, arrows=True)

ALERT_HYGIENE = dict(
    slug="alert-hygiene",
    kicker="a.k.a. “actionable alerting”",
    tldr="An alert that wakes someone up must mean <b>customers are hurt now (or will be soon), a human must act, and it can't wait until morning</b>. Everything else becomes a ticket for daylight, or a graph. Too many pages teaches people to ignore the phone, and then the real one gets missed too. Review every alert rule against those questions, <b>delete without guilt</b>, and keep counting how many pages were useful.",
    chips=[("Family", "watching it"), ("Lives in", "the alert rules in the repo, reviewed monthly"), ("Pairs with", "monitoring, runbooks, the on-call rota")],
    itil=dict(groups=["service"], chain=["deliver", "improve"], practices=["monitoring and event management"],
              sre="“every page should be actionable”; symptom-based alerting", principles=["Keep it simple and practical"],
              older="ITIL v3: event management (informational, warning, exception)"),
    problem_side="Larder, March 2026",
    problem="""  <p class="lead">In March 2026 Larder's <b>63 alert rules</b> sent <b>410 pages</b>. Eli went through them: <b>9</b> needed a human to do something. The rest were CPU spikes during the nightly backup, a disk that had sat at 81 % for a year, and the same stock-sync warning every 20 minutes. <span class="hl-pink">People had started muting the phone at night.</span> Sanne's levelling found him half a day for an “alert fix”, and he takes it on 15 April.</p>
  <ul>
    <li>Noise hides the real page.</li>
    <li>New people on the rota can't tell which alerts matter.</li>
    <li>Every page costs sleep, even the useless ones.</li>
  </ul>""",
    problem_figs=[ah_problem],
    analogy_side="the smoke alarm by the toaster",
    analogy="""  <p>A smoke alarm that goes off <b>every time someone makes toast</b> ends up with its battery out within a week. Then there's a real fire. The answer isn't to ignore it or to buy a louder one. You <b>move it away from the toaster</b>, so that it rings only for smoke that matters.</p>""",
    analogy_figs=[ah_analogy],
    map=[("Toast smoke", "CPU spikes during the backup, a stable disk at 81 %"),
         ("Battery out", "Phone on mute at night"),
         ("The real fire", "Checkout errors at 21:00"),
         ("Moving the alarm", "Alerting on symptoms customers feel"),
         ("A quiet kitchen check", "A morning ticket instead of a page")],
    how_side="four questions per rule, and count what was useful",
    how="""  <p>Eli takes each of the 63 rules through four questions:</p>
  <ol>
    <li>Does it mean <b>customers are hurt now</b>, or will be within the hour?</li>
    <li>Does it need a <b>human</b>, or could a script fix it?</li>
    <li>Is the action <b>urgent</b>, or can it wait until morning?</li>
    <li>Is there a <b>runbook</b> that says what to do?</li>
  </ol>
  <p>Four yeses means it pages. If it fails on urgency, it becomes a <b>ticket for the morning</b>. Anything else goes to a dashboard or is deleted. The result is <b>6 rules that page</b> (the five top-row signals plus the database running out of connections), <b>8 that make tickets</b>, and 49 gone. The stock-sync warning becomes a ticket, and a problem to fix (vol. 2). In May there are <b>22 pages, 17 useful</b>. Every month he writes down the share of useful pages, and any alert that pages twice without needing action goes to the next review.</p>""",
    how_figs=[ah_how],
    steps=[("Export every alert rule and last month's pages", "Count pages per rule."),
           ("Ask the four questions of each rule", "Hurt now? Human? Urgent? Runbook?"),
           ("Page only on four yeses", "Everything else is a ticket or a graph."),
           ("Delete without guilt", "Rules can always come back; sleep can't."),
           ("Count useful pages monthly", "Pages that needed action ÷ all pages."),
           ("Review any alert that pages twice for nothing", "Fix it, demote it or delete it.")],
    vocab=[("Page", "An alert that interrupts a person immediately, day or night."),
           ("Ticket", "An alert that waits in a queue for working hours."),
           ("Actionable", "Someone can and must do something about it."),
           ("Alert fatigue", "So many alerts that people stop reacting to them."),
           ("Flapping", "An alert that fires and clears again and again."),
           ("Symptom-based alerting", "Alerting on what users feel, not on every possible cause.")],
    code=dict(file="ops/alerts/review-2026-04.md", note="the half-day alert fix · Wed 15 April 2026", plain=True, src="""
rule                          pages/Mar  hurt? human? urgent? runbook?  → now
checkout_errors > 2 %             3       y     y      y       write    page
orders_per_5min < 50 %           (new)    y     y      y       write    page
checkout_p95 > 1.5 s              2       y     y      y       write    page
dispatch_delay > 90 s             1       y     y      y       write    page
store_heartbeat > 5 min          (new)    y     y      y       write    page
db_connections > 90 %             3       y     y      y       write    page
stock_sync_warning              131       n     y      n       —        ticket + problem
disk > 80 % (db, at 81 % 1 yr)   62       n     y      n       —        ticket at 90 %
cpu > 80 % (backup window)      118       n     n      n       —        deleted
…49 more                         90                                     deleted / graph

March: 410 pages, 9 useful (2 %).   Target: more than half useful.
May:    22 pages, 17 useful (77 %).
"""),
    tools="tools: the alert rules in your repo, a spreadsheet of last month's pages, and the courage to delete.",
    ladder=[("everything pages", ["Hundreds of pages a month.", "Phones muted."]),
            ("reviewed against four questions", ["Few pages, each with a runbook.", "Useful share counted monthly."]),
            ("alerts as code with tests", ["New alerts need a runbook link to merge.", "Noisy rules flagged automatically."]),
            ("error-budget alerts", ["Pages come from SLO burn rates (vol. 4).", "Causes stay on dashboards."])],
    ladder_now=1,
    baseline="Each line compares <b>63 rules and 410 pages</b> to <b>6 paging rules, 8 morning tickets, and a monthly count of useful pages</b>.",
    ratings=[(2, 4, "Real problems aren't lost in the noise."),
             (3, 3, "Neutral on its own."),
             (2, 4, "People react to pages again."),
             (3, 3, "Neutral."),
             (2, 4, "Each page means something, and the monthly count shows it."),
             (2, 4, "Hundreds of interruptions gone."),
             (3, 3, "Neutral."),
             (1, 4, "From 13 pages a night to under one."),
             (3, 4, "Half a day, then an hour a month.")],
    pitfalls=[("Alerting on every cause", "CPU, memory and disk alerts fire for things users never feel.", "alert on symptoms; keep causes on dashboards."),
              ("Afraid to delete", "“What if we need it?”", "rules live in the repo; you can always bring one back."),
              ("Pages without runbooks", "The person woken up doesn't know what to do.", "no runbook, no page."),
              ("Raising thresholds to silence noise", "The alert stops firing even when it should.", "ask whether it should page at all.")],
    use=["People mute their phones or ignore pages.", "More than a few pages a week, most for nothing.", "New people are joining on-call.", "After every incident: did the right alert fire?"],
    skip=["You get one or two pages a month and each one matters: just keep counting."],
    related=["<b>How Do We Know It's Broken?</b> (this volume)", "<b>What Do I Do at 3 a.m.?</b> (next note)", "<b>SLOs & Error Budgets</b> (cloud, vol. 6)", "<b>Why Am I Always Busy?</b> (this volume)"],
    quiz=[("What are Eli's four questions for a paging alert?", "Are customers hurt now or soon? Does it need a human? Is it urgent? Is there a runbook?"),
          ("What happens to an alert that's real but not urgent?", "It becomes a ticket for working hours instead of a page."),
          ("What is alert fatigue?", "So many alerts, mostly noise, that people stop reacting, and miss the real one."),
          ("Why not just raise the threshold on a noisy alert?", "It may stop firing when it should; the question is whether it should page at all."),
          ("How does Larder track alert quality?", "The share of pages that needed action, every month (2 % in March, 77 % in May).")],
    quiz_sit=[("A new engineer wants to add an alert for “memory above 85 %” that pages. What do you ask?", "What do customers feel when memory is above 85 %, what would the person do, and can it wait until morning? If there's no user symptom and no clear action, it goes on a dashboard.")],
    try_it="Export last month's pages. For each alert rule count the pages and how many needed someone to act. Pick the three noisiest rules and decide: page, ticket or delete.",
    remember="A page is a <span class=\"hl\">promise</span>: customers are hurt and you must act now. Every other alert should <span class=\"hl\">wait for daylight</span>.",
    sources=["Rob Ewaschuk, “My Philosophy on Alerting” (2013), in <i>Site Reliability Engineering</i> (2016), chapter 6.",
             "AXELOS, <i>ITIL 4: Monitoring and event management</i> practice guide (2020).",
             "Betsy Beyer et al., <i>The Site Reliability Workbook</i> (2018): chapter 5, alerting on SLOs."],
)

# ------------------------------------------------------------------ 09 What Do I Do at 3 a.m.?
rb_problem = Doodle(760, 250, "Doodle of a night in late April 2026, imagined by Eli: Cho is on call, the phone says 'db_connections above 90 percent' at 02:40. Cho knows payments, not the database. The only instructions are in Eli's head, and Eli is asleep. Cho has two choices: wake Eli, or guess.",
                    "02:40, an alert Cho has never seen, and the instructions are asleep.")
rb_problem.icon("phone", 40, 40, 1.6)
rb_problem.box(120, 40, 330, 80, "db_connections > 90 %", "pink", sub="02:40", size=18, subsize=15)
rb_problem.box(480, 40, 266, 80, "Cho: payments", "blue", sub="never seen this one", size=18, subsize=14)
rb_problem.row([("wake Eli", None, "y"), ("guess", None, "pink")], x=170, y=160, h=56, w=190, gap=40, size=18)

rb_analogy = Doodle(760, 230, "Doodle of an aeroplane's quick-reference checklist for an engine fire. Short numbered steps in big print, the first ones to be done from memory, then the rest read out. It's written for a stressed pilot, not for an engineer at a desk, and it was tested in the simulator.",
                    "A pilot's engine-fire checklist: short, numbered, tested in the simulator, written for someone under stress.")
ah = rb_analogy
ah.icon("book", 70, 50, 1.6)
ah.box(200, 30, 546, 150, None, "paper")
for i, t in enumerate(["1. throttle → idle", "2. fuel → off", "3. fire handle → pull", "4. if still on fire after 30 s → second bottle"]):
    ah.text(220, 62 + i * 32, t, anchor="start", size=17)
ah.note(470, 212, "written for a stressed person · tested", "pen", size=17)

rb_how = Doodle(760, 360, "Larder's runbook template, May 2026. Every paging alert links to one page with six parts: what this alert means for customers; check first (two or three quick looks); the fix (numbered commands to copy); if that doesn't work, who to call; how to tell it's fixed; and when this page was last tested. On Saturday 9 May at 02:40 Cho was paged for database connections, followed the runbook alone, and had it fixed in 11 minutes.",
                "Six parts, written for a tired person. Cho, on 9 May: 11 minutes, Eli still asleep.")
for i, (t, f) in enumerate([("what it means", "pink"), ("check first", "y"), ("the fix", "blue"), ("still broken? call…", "paper"), ("how to tell it's fixed", "green"), ("last tested", "paper")]):
    r, c = divmod(i, 3)
    rb_how.box(14 + c * 248, 14 + r * 100, 236, 84, f"{i + 1}. {t}", f, size=16)
rb_how.box(110, 236, 540, 72, "Sat 9 May, 02:40 · Cho · runbook RB-06 · fixed in 11 min", "green", size=16)
rb_how.note(380, 340, "8 runbooks, one per paging alert, by 8 May", "pen", size=17)

RUNBOOKS = dict(
    slug="runbooks",
    kicker="a.k.a. “playbooks”, “standard operating procedures”",
    tldr="A <b>runbook</b> tells the person who was paged <b>what the alert means, what to check, what to do, who to call if that fails, and how to know it's fixed</b>, in short numbered steps that can be copied and pasted. Write one for every paging alert, for someone <b>tired, stressed and new to this system</b>, and test it by having someone else follow it.",
    chips=[("Family", "watching it"), ("Lives in", "ops/runbooks/, linked from each alert"), ("Pairs with", "alert hygiene, knowledge management, the on-call rota")],
    itil=dict(groups=["general", "service"], chain=["deliver"], practices=["knowledge management", "incident management"],
              sre="“playbooks”: they cut mean time to repair by about three times (Google's estimate)", principles=["Keep it simple and practical", "Optimise and automate"],
              older="ITIL v3: standard operating procedures, the knowledge base"),
    problem_side="Larder, late April 2026",
    problem="""  <p class="lead">The rota started on 20 April, and in May Cho, Dee and Ana take their first weeks. Eli pictures the first night: Cho, a payments engineer, gets “db_connections > 90 %” at 02:40. <span class="hl-pink">The only instructions are in Eli's head, and Eli is asleep.</span> Cho's choices are to wake Eli, which means the rota hasn't really shared anything, or to guess.</p>
  <ul>
    <li>A shared rota needs shared knowledge.</li>
    <li>Guessing on a production database at night is how small incidents get big.</li>
    <li>Eli is still the escalation for everything.</li>
  </ul>""",
    problem_figs=[rb_problem],
    analogy_side="the pilot's engine-fire checklist",
    analogy="""  <p>An aeroplane has a <b>quick-reference checklist</b> for an engine fire: short numbered steps in big print, the first few done from memory. It's written for <b>a stressed pilot at 3 a.m. over the ocean</b>, not for an engineer at a desk. It's tested in the simulator, and every pilot has practised it.</p>""",
    analogy_figs=[rb_analogy],
    map=[("The engine fire", "The paging alert"),
         ("Big print, numbered steps", "Copy-paste commands, one per line"),
         ("“If still on fire after 30 s”", "“Still broken after 10 minutes? Call…”"),
         ("Tested in the simulator", "Someone else follows it on a quiet afternoon"),
         ("Every pilot has practised it", "Every rota member walks through each runbook once")],
    how_side="one page per paging alert, six parts, then test it",
    how="""  <p>Eli writes one runbook for each of the 6 paging alerts, plus two for known weak spots (the price script on VM 2 and the Rotterdam 4G router). That's <b>8 by Friday 8 May</b>. Each page has the same six parts:</p>
  <ol>
    <li><b>What it means</b> for customers, in one line.</li>
    <li><b>Check first</b>: two or three quick looks with links.</li>
    <li><b>The fix</b>: numbered steps with commands to copy.</li>
    <li><b>Still broken?</b> Who to call, and after how long.</li>
    <li><b>How to tell it's fixed</b>: which graph goes back to normal.</li>
    <li><b>Last tested</b>: by whom and when.</li>
  </ol>
  <p>Then the test. Each rota member follows two runbooks on a quiet afternoon <b>without Eli in the room</b>, and every step they stumble on gets rewritten. On <b>Saturday 9 May at 02:40</b> Cho is paged for database connections, follows RB-06 alone and has it fixed in <b>11 minutes</b>. Eli finds out at breakfast.</p>""",
    how_figs=[rb_how],
    steps=[("One runbook per paging alert", "No runbook, no page."),
           ("Use the same six parts every time", "People find their place quickly under stress."),
           ("Write commands to copy, not prose", "Exact commands, with the environment named."),
           ("Say when to give up and call", "“After 10 minutes, call the secondary.”"),
           ("Test it with someone else", "They follow it; you watch and say nothing."),
           ("Update it after every use", "If it was wrong at 3 a.m., fix it by noon.")],
    vocab=[("Runbook", "Step-by-step instructions for handling one alert or task."),
           ("Playbook", "Another word for runbook; sometimes a wider set of plays."),
           ("Copy-paste step", "A command written exactly so it can be pasted safely."),
           ("Escalation step", "The point at which you stop and call someone."),
           ("Runbook test", "Someone other than the author follows it while the author watches."),
           ("Automation candidate", "A runbook step done so often it should become a script.")],
    code=dict(file="ops/runbooks/RB-06-db-connections.md", note="tested by Cho, Tue 5 May 2026 · used for real Sat 9 May", plain=True, src="""
# RB-06 · Postgres connections above 90 %                  pages: yes · tier: critical
1 What it means   New requests will soon fail to get a DB connection: checkout errors next.
2 Check first     a) dashboard "core / db": which app holds most connections?
                  b) any deploy in the last hour?  (#deploys channel)
                  c) Dispatch's copies: more than 6 running?
3 The fix         a) if one Core VM holds > 150: restart its app (not the VM):
                     ssh core-2 'sudo systemctl restart larder-core'   # one VM at a time
                  b) if Dispatch scaled up: set copies back to 4 (ops/dispatch.md)
4 Still broken?   after 10 min → call the secondary; after 20 → Eli (+31 6 …)
5 Fixed when      connections < 70 % for 5 min and checkout errors < 1 %
6 Last tested     Cho, 5 May (step 3a took 2 tries: wording fixed)
"""),
    tools="tools: a folder of markdown pages linked from each alert. Some paging tools can show the runbook in the alert itself.",
    ladder=[("in one person's head", ["Wake that person, or guess.", "Every night depends on one person."]),
            ("a tested page per alert", ["Six parts, copy-paste steps.", "Updated after every use."]),
            ("scripted steps", ["The common fix is one command.", "The runbook calls the script."]),
            ("self-healing", ["The system runs the fix itself and tells you after.", "People handle only the new."])],
    ladder_now=1,
    baseline="Each line compares <b>instructions in Eli's head</b> to <b>eight tested runbooks linked from the alerts</b>.",
    ratings=[(2, 3, "Incidents stay small."),
             (3, 3, "Neutral."),
             (2, 4, "11 minutes, alone, at 02:40."),
             (3, 3, "Neutral."),
             (2, 4, "What to do is written next to the alert."),
             (3, 3, "Steps done often become scripts later."),
             (3, 3, "Neutral."),
             (1, 4, "Others can be on call without waking Eli."),
             (3, 3, "About two days for eight runbooks.")],
    pitfalls=[("Written for the author", "“Restart the usual thing.”", "write for someone new and tired."),
              ("Never tested", "The command has a typo you find at 3 a.m.", "someone else follows it first."),
              ("No point to stop", "People keep trying for an hour alone.", "say when to call, in minutes."),
              ("Stale after the first change", "The runbook describes last year's system.", "update it after every use and every change.")],
    use=["You're sharing on-call.", "An alert pages and only one person knows what to do.", "After an incident where people guessed.", "Before a launch that adds new failure modes."],
    skip=["Alerts that shouldn't page at all: fix the alert instead."],
    related=["<b>Which Alerts Deserve a Human?</b> (this volume)", "<b>Where Is That Written Down?</b> (this volume)", "<b>Handover to Operations</b> (Ana, vol. 6)", "<b>Incident Response & Postmortems</b> (cloud, vol. 6)"],
    quiz=[("What are the six parts of Larder's runbooks?", "What it means, check first, the fix, still broken? call…, how to tell it's fixed, last tested."),
          ("Who should a runbook be written for?", "A tired, stressed person who has never seen this alert before."),
          ("How do you test a runbook?", "Someone other than the author follows it, while the author watches and says nothing; fix every stumble."),
          ("Why give a time limit before calling for help?", "So nobody struggles alone for an hour while customers wait."),
          ("When is a runbook step a candidate for a script?", "When it's run often and is always the same.")],
    quiz_sit=[("Dee follows RB-02 at night and step 3 doesn't work, but she fixes it another way. What happens next?", "She updates RB-02 the next day with what actually worked, and notes it in the handover, so the next person doesn't hit the same wall.")],
    try_it="Pick the alert that last woke someone up. Write its runbook in the six parts. Then ask a colleague who has never handled it to follow it while you watch. What did you have to explain out loud?",
    remember="If the fix lives in <span class=\"hl\">one head</span>, the rota is shared on paper only. Write it for someone <span class=\"hl\">tired and new</span>, then test it.",
    sources=["Betsy Beyer et al., <i>Site Reliability Engineering</i> (2016): chapter 1 (playbooks) and chapter 11.",
             "Atul Gawande, <i>The Checklist Manifesto</i> (2009).",
             "AXELOS, <i>ITIL 4: Knowledge management</i> practice guide (2020)."],
)

NOTES = [ON_CALL, MONITORING, ALERT_HYGIENE, RUNBOOKS]
