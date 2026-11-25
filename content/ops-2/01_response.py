# Series 2 · Book 5 · The IT Operations Notebook · Vol. 2 · Responding.
# Narrator: Eli (he/him). Facts: docs/larder-casebook.md, "Book 5, Vol. 2".

# ------------------------------------------------------------------ 01 How Bad Is It?
sv_problem = Doodle(760, 260, "Doodle of Friday 12 June 2026, 18:02. About 30 percent of iDEAL payments fail at the payment provider. Cho, on call, thinks it's small: cards still work. Ben thinks it's huge: iDEAL is how most Dutch customers pay, at the Friday peak. They spend 14 minutes arguing in the chat about whether to wake Eli, tell Sam and call the provider. Meanwhile about 160 orders fail.",
                    "14 minutes arguing about how big it is, at the Friday peak.")
sv_problem.box(14, 30, 230, 100, "Cho: “small”", "y", sub="cards still work", size=19, subsize=15)
sv_problem.box(264, 30, 230, 100, "Ben: “huge”", "pink", sub="iDEAL, Friday peak", size=19, subsize=15)
sv_problem.box(514, 30, 232, 100, "14 minutes", "paper", sub="of arguing", size=21, subsize=15)
sv_problem.note(380, 180, "≈ 160 orders fail while the size is debated", "red", size=19)

sv_analogy = Doodle(760, 230, "Doodle of a hospital emergency department's triage colours. A nurse decides in a minute: red, seen now; orange, within ten minutes; yellow, within an hour; green, can wait. The rules are written on the wall and based on what the patient has, not how loudly they complain. Nobody debates it at the door.",
                    "Triage at the door: four colours, decided in a minute, by rules on the wall.")
for i, (c, t, f) in enumerate([("red", "now", "pink"), ("orange", "10 min", "y"), ("yellow", "1 hour", "y"), ("green", "can wait", "green")]):
    sv_analogy.box(14 + i * 186, 40, 172, 90, c, f, sub=t, size=20, subsize=16)
sv_analogy.note(380, 186, "by what the patient has, not how loudly they shout", "pen", size=18)

sv_how = Doodle(760, 380, "Larder's severity levels, agreed on Monday 15 June 2026. SEV1: a city can't order, pay, pick or dispatch, or more than 10 percent of orders are failing; page everyone needed, incident lead at once, Femke told within 15 minutes, updates every 15 minutes. SEV2: one store, one payment method or one business client's delivery at risk, or 2 to 10 percent of orders failing; on-call leads, updates every 30 minutes. SEV3: degraded with a workaround; fix in working hours. SEV4: no customer impact; a ticket. Rule: when unsure, pick the higher one; you can always go down.",
                "Four levels by customer harm. When unsure, go higher; lowering it later is cheap.")
rows = [("SEV1", "a city can't order · pay · pick · dispatch, or > 10 % failing", "pink"),
        ("SEV2", "one store · one payment method · a client's delivery, or 2–10 %", "y"),
        ("SEV3", "degraded, with a workaround", "blue"),
        ("SEV4", "no customer impact", "paper")]
for i, (s, t, f) in enumerate(rows):
    sv_how.box(14, 14 + i * 74, 110, 62, s, f, size=20)
    sv_how.box(134, 14 + i * 74, 612, 62, t, f, size=15)
sv_how.note(380, 330, "unsure? pick the higher one", "red", size=19)
sv_how.note(380, 362, "12 June would have been SEV2 in one minute", "pen", size=16)

SEVERITY = dict(
    slug="severity-levels",
    kicker="a.k.a. “incident priority”",
    tldr="A <b>severity level</b> says how bad an incident is, and therefore <b>who is called, how fast, and who must be told</b>. Define three or four levels <b>in advance</b>, by <b>customer harm</b> (not by which system broke or how busy people feel), write down what each level triggers, and agree one rule: <b>when unsure, pick the higher one</b>. Then nobody spends the first fifteen minutes of an incident arguing about its size.",
    chips=[("Family", "responding"), ("Lives in", "ops/incidents/severity.md, linked from every alert"), ("Pairs with", "incident roles, communication, major incidents")],
    itil=dict(groups=["service"], chain=["deliver", "engage"], practices=["incident management"],
              sre="“severity”, agreed before the incident", principles=["Focus on value", "Keep it simple and practical"],
              older="ITIL v3: incident prioritisation (impact × urgency)"),
    pager=dict(when="Fri 12 Jun 2026 · Cho on call", lines=[
        ("18:02", "<b>ALERT</b> checkout_errors 6.1 % (5 min) · payments step"),
        ("18:03", "Cho ack · PSP status page: “iDEAL degraded”"),
        ("18:05", "Cho: cards fine, small? · Ben: it's iDEAL on a Friday, huge"),
        ("18:16", "still discussing: wake Eli? tell Sam? call PSP?"),
        ("18:16", "Eli joins from the tram: call the PSP, tell Sam, now"),
        ("19:10", "PSP: fixed on their side · ≈ 160 failed orders")]),
    problem_side="Larder, Friday 12 June 2026",
    problem="""  <p class="lead">At 18:02 on a Friday about <b>30 % of iDEAL payments</b> start failing at the payment provider. Cho, on call, sees that cards still work and calls it small. Ben points out that iDEAL is how most Dutch customers pay, and it's the Friday peak. <span class="hl-pink">They argue for 14 minutes</span> about whether to wake Eli, tell Sam and call the provider. About <b>160 orders</b> fail before the provider fixes it at 19:10.</p>
  <ul>
    <li>Everyone judges size by their own corner.</li>
    <li>What to do follows from the size, so arguing about the size means nothing gets done.</li>
    <li>Support and the stores hear about it last.</li>
  </ul>""",
    problem_figs=[sv_problem],
    analogy_side="triage at the emergency department",
    analogy="""  <p>An emergency department has <b>four triage colours on the wall</b>: red is seen now, orange within ten minutes, yellow within an hour, green can wait. A nurse decides in about a minute, <b>by what the patient has</b>, not by how loudly they complain or which doctor is free. Nobody debates it at the door, and the colour decides everything that follows.</p>""",
    analogy_figs=[sv_analogy],
    map=[("The triage colours", "SEV1 to SEV4"),
         ("By what the patient has", "By customer harm: orders failing, a city or store stopped"),
         ("Seen now / in ten minutes", "Who is paged, how fast, who is told"),
         ("Decided at the door in a minute", "Set by whoever acknowledges the alert"),
         ("Re-triaged if they get worse", "Raise or lower the level as you learn more")],
    how_side="four levels by customer harm, and what each one triggers",
    how="""  <p>On Monday <b>15 June</b> Eli brings a one-page draft to tech leads, and Femke and Sam join for it. The levels are set <b>by customer harm</b>:</p>
  <ul>
    <li><b>SEV1</b>: a city can't order, pay, pick or dispatch, or <b>more than 10 %</b> of orders are failing. An incident lead at once, Femke told within 15 minutes, updates every 15 minutes.</li>
    <li><b>SEV2</b>: one store, one payment method or one business client's delivery at risk, or <b>2–10 %</b> failing. On-call leads, Sam is told, updates every 30 minutes.</li>
    <li><b>SEV3</b>: degraded, with a workaround. Fixed in working hours.</li>
    <li><b>SEV4</b>: no customer impact. A ticket.</li>
  </ul>
  <p>Two rules go with it: whoever acknowledges the alert <b>sets the level within 5 minutes</b>, and <b>when unsure, pick the higher one</b>, because lowering it later is cheap. 12 June would have been SEV2 in one minute: call the provider, tell Sam, update every 30 minutes. In the next four months Larder has 2 SEV1s, 9 SEV2s and about 30 SEV3s, and nobody argues about size again.</p>""",
    how_figs=[sv_how],
    steps=[("Describe harm in customers' terms", "Orders failing, a city or store stopped, a client's delivery."),
           ("Use three or four levels, no more", "Each one must trigger something different."),
           ("Write what each level triggers", "Who is paged, who is told, how often to update."),
           ("Let the first responder set it", "Within 5 minutes, without asking permission."),
           ("When unsure, go higher", "It's cheap to lower; expensive to be late."),
           ("Re-check the level as you learn", "And note every change in the timeline.")],
    vocab=[("Severity", "How bad an incident is for customers."),
           ("Impact", "How many people or orders are affected."),
           ("Urgency", "How fast the harm grows if nothing is done."),
           ("Incident", "An unplanned interruption or loss of quality of a service."),
           ("Escalating the severity", "Raising the level when it turns out worse."),
           ("Declaring", "Saying out loud, in the incident channel, that an incident is on and at what level.")],
    code=dict(file="ops/incidents/severity.md", note="agreed Mon 15 June 2026 (tech leads + Femke + Sam)", plain=True, src="""
level  customer harm                                   triggers
SEV1   a city can't order / pay / pick / dispatch,      incident lead now · Femke told ≤ 15 min
       or > 10 % of orders failing                      updates every 15 min · review always
SEV2   one store, one payment method, a business        on-call leads · Sam told · updates 30 min
       client's delivery at risk, or 2–10 % failing     review always
SEV3   degraded, workaround exists                      fix in working hours · review if repeated
SEV4   no customer impact                               ticket

set by   whoever acknowledges the alert, within 5 minutes
unsure?  pick the higher level. Lowering it later is cheap.
"""),
    tools="tools: one page, linked from every alert and pinned in the incident channel.",
    ladder=[("size argued each time", ["Each person judges from their corner.", "Action waits."]),
            ("four written levels", ["Set by the first responder.", "Each level triggers known steps."]),
            ("level drives tooling", ["Choosing SEV1 pages the lead and opens the channel.", "Updates reminded automatically."]),
            ("level from signals", ["Orders-affected numbers suggest the level.", "People confirm it."])],
    ladder_now=1,
    baseline="Each line compares <b>arguing about size during the incident</b> to <b>four levels by customer harm, set in five minutes</b>.",
    ratings=[(2, 4, "Big incidents get big responses at once."),
             (3, 3, "Neutral on its own."),
             (2, 4, "Minutes of debate become minutes of fixing."),
             (3, 3, "Neutral."),
             (2, 4, "Everyone knows how bad it is from one word."),
             (3, 3, "Neutral."),
             (3, 4, "Small things stay small: SEV3 waits for morning."),
             (2, 3, "Clear rules for when to wake someone."),
             (4, 4, "One page.")],
    pitfalls=[("Levels by system", "“Database = SEV1” even when nobody notices.", "levels by customer harm."),
              ("Too many levels", "People argue about SEV3 vs SEV4.", "three or four, each triggering something different."),
              ("Asking permission to declare", "The first responder waits for a senior.", "whoever acknowledges sets it."),
              ("Never lowering it", "Everything stays SEV1 for the record.", "change it as you learn, and note why.")],
    use=["Incidents start with an argument about size.", "Support or leaders hear about outages late.", "Before sharing on-call with new people.", "You need to decide who is woken up for what."],
    skip=["Never: even a two-person team gains from one shared definition."],
    related=["<b>Who Is in Charge?</b> (next note)", "<b>When Is It a Major Incident?</b> (this volume)", "<b>Incident Response & Postmortems</b> (cloud, vol. 6)"],
    quiz=[("What should severity be based on?", "Customer harm: how many orders, stores or clients are affected, and how badly."),
          ("Who sets the severity, and how fast?", "Whoever acknowledges the alert, within 5 minutes."),
          ("What's the rule when you're unsure?", "Pick the higher level; lowering it later is cheap."),
          ("What level would 12 June have been?", "SEV2: one payment method failing for part of the customers."),
          ("Why only four levels?", "Each level must trigger something different; more levels just add arguments.")],
    quiz_sit=[("At 08:10 on a Tuesday Rotterdam's handhelds can't sync, but the offline mode is working and orders are being picked. What level, and why?", "SEV3 (degraded with a workaround), but watch it: offline mode lasts about two hours, so if it isn't fixed by then it becomes SEV2 (a store stopped). Note the time.")],
    try_it="Write your own four levels in one sentence each, by customer harm. For your last three incidents, which level would each have been, and what would that have changed in the first fifteen minutes?",
    remember="Decide <span class=\"hl\">how bad it is</span> before the incident, by <span class=\"hl\">customer harm</span>. When unsure, go higher.",
    sources=["AXELOS, <i>ITIL 4: Incident management</i> practice guide (2020).",
             "PagerDuty, <i>Incident Response documentation</i> (open source): severity levels.",
             "Betsy Beyer et al., <i>Site Reliability Engineering</i> (2016): chapter 14, managing incidents."],
)

# ------------------------------------------------------------------ 02 Who Is in Charge?
ir_problem = Doodle(760, 250, "Doodle of Friday 3 July 2026, 17:40. The stock sync stops and the app shows wrong stock. Four engineers jump into the chat and all debug at once: two restart the same service, one changes a setting nobody else knows about. Nobody tells the stores. Tomás finds out when pickers at Noord start finding empty shelves for items the app says are in stock. The incident lasts 70 minutes; nobody can say afterwards who did what, or when.",
                    "Four people fixing, nobody leading, nobody telling the stores, nobody writing it down.")
for i, t in enumerate(["Eli", "Ben", "Cho", "Dee"]):
    ir_problem.box(14 + i * 128, 30, 116, 70, t, "blue", sub="debugging", size=18, subsize=13)
ir_problem.box(540, 30, 206, 70, "the stores", "pink", sub="nobody told them", size=17, subsize=13)
ir_problem.note(270, 136, "two restarts of the same thing · one secret setting change", "red", size=16)
ir_problem.box(110, 166, 540, 56, "70 minutes · no timeline · Tomás finds out from empty shelves", "paper", size=15)

ir_analogy = Doodle(760, 230, "Doodle of a kitchen fire drill in a busy restaurant: the head chef takes charge and doesn't cook; one cook handles the fire; the floor manager tells the guests; someone writes down the times for the insurance. Everyone else keeps their station. Before the drill, all eight cooks ran to the same pan.",
                    "One leads (and doesn't cook), some fix, one tells the guests, one writes the times.")
for i, (t, s, f) in enumerate([("head chef", "leads, doesn't cook", "y"), ("one cook", "the fire", "pink"), ("floor manager", "the guests", "green"), ("someone", "writes times", "paper")]):
    ir_analogy.box(14 + i * 186, 40, 172, 96, t, f, sub=s, size=18, subsize=14)
ir_analogy.note(380, 190, "everyone else keeps their station", "pen", size=18)

ir_how = Doodle(760, 360, "Larder's incident roles from 13 July 2026. Incident lead: by default the on-call primary; coordinates, decides, doesn't type commands. Fixers: one or two people working on the problem, reporting to the lead. Communication: tells Sam, the stores and, for SEV1, Femke, on the fixed schedule. Scribe: writes the timeline as it happens. In a small incident one person can hold two roles, but never lead and fix at the same time. Handover of the lead role is said out loud. First used on Friday 17 July.",
                "Four roles, named in the first five minutes. The lead doesn't fix.")
for i, (t, s, f) in enumerate([("incident lead", "coordinates · decides", "y"), ("fixers", "1–2 · work the problem", "blue"), ("communication", "Sam · stores · Femke", "green"), ("scribe", "timeline as it happens", "paper")]):
    ir_how.box(14 + i * 186, 14, 172, 110, t, f, sub=s, size=17, subsize=13)
ir_how.box(14, 150, 732, 60, "small incident? one person may hold two roles, but never lead + fix", "pink", size=16)
ir_how.box(14, 230, 732, 60, "handing over the lead: said out loud, written in the timeline", "paper", size=16)
ir_how.note(380, 330, "first used Fri 17 July · 23 minutes, stores told at minute 6", "green", size=17)

INCIDENT_ROLES = dict(
    slug="incident-roles",
    kicker="a.k.a. “incident command”",
    tldr="In an incident, name <b>four roles</b> in the first five minutes: an <b>incident lead</b> who coordinates and decides but <b>doesn't fix</b>; one or two <b>fixers</b>; someone on <b>communication</b>; and a <b>scribe</b> who writes the timeline. It looks like overhead for a team of six. It isn't: without a lead, four people fix the same thing, nobody tells the stores, and afterwards nobody knows what happened.",
    chips=[("Family", "responding"), ("Lives in", "ops/incidents/roles.md, pinned in the incident channel"), ("Pairs with", "severity levels, communication, post-incident review")],
    itil=dict(groups=["service"], chain=["deliver", "engage"], practices=["incident management"],
              sre="“incident command”: commander, operations, communications, planning", principles=["Collaborate and promote visibility"],
              older="ITIL v3: incident management roles; (from emergency services) the incident command system"),
    pager=dict(when="Fri 3 Jul 2026 · Eli on call", lines=[
        ("17:40", "<b>TICKET→PAGE</b> stock_sync stale 25 min · all stores"),
        ("17:42", "Eli, Ben, Cho, Dee all in #ops; all reading logs"),
        ("17:48", "Ben restarts sync · 17:49 Cho restarts sync"),
        ("17:55", "Dee changes batch size (not said in chat)"),
        ("18:20", "Tomás: “app says in stock, shelves empty, what's going on?”"),
        ("18:50", "sync running · nobody sure which change fixed it")]),
    problem_side="Larder, Friday 3 July 2026",
    problem="""  <p class="lead">At 17:40 the stock sync stops, and the app starts showing items in stock that aren't. Eli, Ben, Cho and Dee all jump into the chat and all debug at once. <b>Two of them restart the same service</b> a minute apart, and one changes a batch size without saying so. <span class="hl-pink">Nobody tells the stores</span>: Tomás finds out at 18:20, when Noord's pickers keep finding empty shelves. It's over at 18:50, and nobody can say which change fixed it.</p>
  <ul>
    <li>Everyone fixes; nobody coordinates.</li>
    <li>Changes collide and can't be undone, because nobody knows what was changed.</li>
    <li>The people affected are told last, or not at all.</li>
  </ul>""",
    problem_figs=[ir_problem],
    analogy_side="the kitchen fire drill",
    analogy="""  <p>When a pan catches fire in a busy restaurant, the <b>head chef takes charge and stops cooking</b>. <b>One cook</b> deals with the fire. The <b>floor manager</b> calms and informs the guests. <b>Someone writes down the times</b> for the insurance. Everyone else stays at their station. Before they practised it, all eight cooks ran to the same pan.</p>""",
    analogy_figs=[ir_analogy],
    map=[("Head chef, not cooking", "Incident lead: coordinates, decides, doesn't type commands"),
         ("The cook with the fire", "Fixers: one or two, working the problem"),
         ("Floor manager and the guests", "Communication: Sam, the stores, Femke"),
         ("Writing down the times", "Scribe: the timeline as it happens"),
         ("Everyone else at their station", "Everyone else stays out unless asked")],
    how_side="four roles, named in five minutes; the lead doesn't fix",
    how="""  <p>From <b>13 July</b> every SEV1 and SEV2 starts the same way. The first responder <b>declares</b> it in <code>#incident</code> with a level, and names four roles:</p>
  <ul>
    <li><b>Incident lead</b>: by default the on-call primary. Keeps the picture, decides, asks “what do we know, what are we trying next, who's doing it?” every 10 minutes. <b>Doesn't type commands.</b></li>
    <li><b>Fixers</b>: one or two people working the problem, who say every change in the channel <b>before</b> making it.</li>
    <li><b>Communication</b>: tells Sam, the stores and (for SEV1) Femke, on the schedule for that level.</li>
    <li><b>Scribe</b>: writes the timeline with times, as it happens.</li>
  </ul>
  <p>In a small incident one person can hold two roles, <b>but never lead and fix at once</b>. Handing over the lead is said out loud. The first use is Friday <b>17 July</b>: the same kind of sync failure, Dee as lead, Ben fixing, Cho on communication. The stores are told at minute 6, and it's fixed in 23 minutes.</p>""",
    how_figs=[ir_how],
    steps=[("Declare the incident and its level", "In one channel, with a time."),
           ("Name the lead", "By default the on-call primary."),
           ("Name fixers, communication, scribe", "Small incidents can double up, never lead + fix."),
           ("Fixers say each change before making it", "No secret changes."),
           ("The lead asks three questions every 10 minutes", "What do we know? What next? Who's doing it?"),
           ("Hand over the lead out loud", "“Dee, you have the lead.” Written in the timeline.")],
    vocab=[("Incident lead (commander)", "The person coordinating the response and making decisions."),
           ("Fixer (operations)", "A person working directly on the problem."),
           ("Communication lead", "The person keeping everyone affected informed."),
           ("Scribe", "The person writing the timeline during the incident."),
           ("Declare", "Officially start an incident, with a level, in a known place."),
           ("Freelancing", "Fixing without telling the lead: the cause of colliding changes.")],
    code=dict(file="ops/incidents/roles.md", note="from 13 July 2026 · pinned in #incident", plain=True, src="""
# Incident roles (SEV1 and SEV2)

lead        on-call primary by default · coordinates, decides · does NOT fix
            every 10 min: what do we know? what are we trying? who's doing it?
fixers      1–2 people · say each change BEFORE making it · report to the lead
comms       Sam + affected stores (SEV2: every 30 min) · Femke (SEV1: every 15 min)
scribe      timeline in the incident doc: time · what happened · who · why

small incident: one person may hold two roles, never lead + fix
handover:  "Dee, you have the lead." → scribe writes it down
everyone else: stay out of #incident unless the lead asks
"""),
    tools="tools: one incident channel, an incident doc template, and the habit of saying the role names out loud.",
    ladder=[("everyone fixes", ["No lead, no timeline.", "Stores told late."]),
            ("four named roles", ["Lead doesn't fix.", "Changes said before they're made."]),
            ("tool-assisted", ["Declaring opens the channel and doc and pages the roles.", "Timeline drafted from the chat."]),
            ("practised", ["Roles rehearsed in game days (vol. 5).", "Anyone on the rota can lead."])],
    ladder_now=1,
    baseline="Each line compares <b>four engineers debugging at once</b> to <b>four named roles with a lead who doesn't fix</b>.",
    ratings=[(2, 4, "Stores are told at minute 6, not minute 40."),
             (3, 3, "Neutral."),
             (2, 4, "70 minutes → 23 for the same kind of failure."),
             (2, 4, "No colliding or secret changes."),
             (1, 4, "A lead keeps the picture; a scribe writes it down."),
             (3, 3, "Neutral."),
             (3, 3, "Neutral."),
             (2, 3, "Fewer people pulled in for nothing."),
             (3, 3, "A minute to name roles.")],
    pitfalls=[("The lead fixes too", "Heads down in logs, nobody keeps the picture.", "the lead doesn't type commands."),
              ("Silent changes", "Two fixes collide; nobody knows what worked.", "say it in the channel before you do it."),
              ("Seniority decides the lead", "The CTO-equivalent turns up and takes over without saying so.", "the lead changes only by an explicit handover."),
              ("Roles for SEV4", "Process for nothing.", "roles for SEV1 and SEV2 only.")],
    use=["More than one person is working an incident.", "Changes have collided before.", "The people affected heard late.", "Afterwards, nobody can reconstruct what happened."],
    skip=["SEV3 and SEV4: one person fixes it and writes a line."],
    related=["<b>How Bad Is It?</b> (this volume)", "<b>Who Needs to Know?</b> (next note)", "<b>What Can We Learn from It?</b> (this volume)", "<b>Incident Response & Postmortems</b> (cloud, vol. 6)"],
    quiz=[("What are the four roles?", "Incident lead, fixers, communication, scribe."),
          ("Why doesn't the lead fix?", "Someone has to keep the whole picture and decide; heads-down fixing makes that impossible."),
          ("What must fixers do before changing something?", "Say it in the channel, so changes don't collide and can be undone."),
          ("Who is lead by default at Larder?", "The on-call primary."),
          ("What changed between 3 July and 17 July?", "Same kind of failure: stores told at minute 6 instead of minute 40, fixed in 23 minutes instead of 70.")],
    quiz_sit=[("During a SEV2, Eli joins the channel and starts suggesting fixes directly to the fixer, while Dee is lead. What should happen?", "Eli gives his suggestions to Dee, the lead, or asks her for the lead in an explicit handover. Two people steering the fixer is how changes collide.")],
    try_it="Replay your last incident on paper. Who was leading? Who told the people affected, and when? Was there a timeline? Write who would have held each of the four roles.",
    remember="Someone has to <span class=\"hl\">lead and not fix</span>. Name the roles in the first five minutes, and say each change <span class=\"hl\">before</span> you make it.",
    sources=["Betsy Beyer et al., <i>Site Reliability Engineering</i> (2016): chapter 14, managing incidents.",
             "PagerDuty, <i>Incident Response documentation</i> (open source): roles.",
             "AXELOS, <i>ITIL 4: Incident management</i> practice guide (2020)."],
)

# ------------------------------------------------------------------ 03 Who Needs to Know?
ic_problem = Doodle(760, 250, "Doodle of the communication around the 3 July stock sync incident. Sam's support team learned from customers' complaints; the stores learned from empty shelves; Femke learned on Monday, from a customer's tweet. Three groups, three different stories, all of them late.",
                    "Support, stores and the CEO each heard a different story, from a different place, late.")
for i, (t, s) in enumerate([("Sam's team", "from complaints"), ("the stores", "from empty shelves"), ("Femke", "Monday, from a tweet")]):
    ic_problem.box(14 + i * 248, 40, 236, 100, t, "pink", sub=s, size=19, subsize=15)
ic_problem.note(380, 190, "three stories · all late · none from us", "red", size=19)

ic_analogy = Doodle(760, 220, "Doodle of a railway station's departure board during a delay: a short message at fixed times ('Train to Utrecht delayed, next update 18:30'), the same message on the board, the app and the speakers. Passengers can live with a delay; what they can't stand is silence.",
                    "“Delayed. Next update 18:30.” Same words on the board, the app and the speaker.")
ic_analogy.icon("board", 60, 40, 1.6)
ic_analogy.box(180, 40, 566, 100, "Utrecht 18:12 · delayed", "y", sub="cause: signal failure · next update 18:30", size=20, subsize=15)
ic_analogy.note(450, 186, "people forgive delays; they don't forgive silence", "pen", size=18)

ic_how = Doodle(760, 380, "Larder's incident communication from August 2026. Four audiences, each in a fixed place: support (Sam's team) in the incident channel's pinned update; stores by a message to store leads; Femke and leaders by a short message for SEV1; and business customers on a status page launched on 1 September for office managers. Every update uses the same four lines: what customers see; what we're doing; what they should do; next update at. SEV1 every 15 minutes, SEV2 every 30, even if nothing changed.",
                "Four audiences, fixed places, four lines, a promised next update.")
for i, (t, s, f) in enumerate([("support", "pinned in #incident", "blue"), ("stores", "message to store leads", "green"), ("Femke", "SEV1 only", "y"), ("business clients", "status page · from 1 Sep", "paper")]):
    ic_how.box(14 + i * 186, 14, 172, 96, t, f, sub=s, size=17, subsize=13)
ic_how.box(14, 136, 732, 160, None, "paper")
for i, t in enumerate(["what customers see: iDEAL payments fail for some customers", "what we're doing: provider contacted, switching to backup route",
                       "what they should do: suggest card payment; no refunds needed", "next update: 18:45 (every 15 min SEV1 · 30 min SEV2)"]):
    ic_how.text(30, 170 + i * 34, t, anchor="start", size=15)
ic_how.note(380, 340, "even “no change, next update 19:15” counts", "pen", size=17)

INCIDENT_COMMS = dict(
    slug="incident-communication",
    kicker="a.k.a. “keeping people informed”",
    tldr="During an incident, the people affected need <b>short, regular updates from you</b>, before they make up their own story. Decide <b>who needs to know</b> (support, the front line, leaders, customers), <b>where</b> each group reads it, and a <b>fixed format</b>: what customers see, what we're doing, what you should do, <b>when the next update is</b>. Send it on schedule even when nothing has changed. Silence is the worst update.",
    chips=[("Family", "responding"), ("Lives in", "ops/incidents/comms.md, the status page, store leads' group"), ("Pairs with", "incident roles, telling a business client, major incidents")],
    itil=dict(groups=["service", "general"], chain=["engage", "deliver"], practices=["incident management", "relationship management"],
              sre="“communications lead”; status pages", principles=["Collaborate and promote visibility"],
              older="ITIL v3: incident communication, the service desk's role"),
    problem_side="Larder, 3–6 July 2026",
    problem="""  <p class="lead">After the 3 July stock sync incident Eli asks how each group heard about it. Sam's support team heard from <b>customers complaining</b>. The stores heard from <b>empty shelves</b>. Femke heard on Monday, from <b>a customer's tweet</b>. <span class="hl-pink">Three groups, three different stories, all late, and none of them from us.</span> And from September, Korenwolf's three office managers will need to know too.</p>
  <ul>
    <li>Support can't help customers without knowing what's happening.</li>
    <li>Stores lose time working around a problem nobody has named.</li>
    <li>Leaders lose trust when they hear it from outside.</li>
  </ul>""",
    problem_figs=[ic_problem],
    analogy_side="the station departure board",
    analogy="""  <p>When a train is delayed, a good station shows <b>the same short message</b> on the board, in the app and over the speakers: “Utrecht 18:12 delayed, signal failure, <b>next update 18:30</b>”. At 18:30 there's an update, even if all it says is “no change”. Passengers can live with a delay. What they can't stand is <b>silence</b>.</p>""",
    analogy_figs=[ic_analogy],
    map=[("Passengers", "Support, stores, Femke, office managers"),
         ("The board, the app, the speakers", "#incident pin, store leads' group, the status page"),
         ("“Signal failure”", "What customers see, in plain words"),
         ("“Next update 18:30”", "The promised time of the next update"),
         ("An update even with no change", "On schedule: 15 min for SEV1, 30 for SEV2")],
    how_side="four audiences, fixed places, four lines, on schedule",
    how="""  <p>Eli and Sam write the communication part of the incident process in August:</p>
  <ul>
    <li><b>Support</b> reads the <b>pinned update</b> in <code>#incident</code>, and Sam's team can copy it straight into replies.</li>
    <li><b>Stores</b> get a message in the store leads' group from the communication person.</li>
    <li><b>Femke and the leaders</b> get a short direct message for SEV1, within 15 minutes.</li>
    <li><b>Business customers</b> see a <b>status page</b>, launched on <b>1 September</b> for office managers before Korenwolf's contract starts. It shows incidents that affect business ordering or deliveries.</li>
  </ul>
  <p>Every update has the <b>same four lines</b>: what customers see · what we're doing · what you should do · <b>next update at</b>. It goes out every 15 minutes for SEV1 and every 30 for SEV2, even when nothing has changed. Templates are pinned, so the communication person fills in blanks rather than writing prose under stress.</p>""",
    how_figs=[ic_how],
    steps=[("List who is affected by your services", "Support, front line, leaders, customers."),
           ("Give each audience one place to read", "A channel, a group, a page. Not all of them."),
           ("Use a four-line format", "Customers see · we're doing · you should do · next update."),
           ("Write in their words", "“Payment fails for some customers”, not “PSP 502s”."),
           ("Send on schedule, even with no change", "The promised time is the promise."),
           ("Close it clearly", "“Fixed at 19:10; what we'll do next: review on Tuesday.”")],
    vocab=[("Status page", "A public or customer-facing page showing current incidents and their status."),
           ("Update cadence", "How often updates are sent: 15 or 30 minutes."),
           ("Holding statement", "A first short message when you don't know much yet."),
           ("Audience", "A group that needs updates: support, stores, leaders, clients."),
           ("Resolution notice", "The last update: fixed, when, what happens next."),
           ("Jargon", "Words only engineers use; keep them out of updates.")],
    code=dict(file="ops/incidents/comms.md", note="templates · August 2026", plain=True, src="""
# Incident updates · same four lines, every time

[SEV2 · 18:15]  iDEAL payments
Customers see    iDEAL payment fails for about 1 in 3 customers. Cards work.
We're doing      Payment provider contacted; switching iDEAL to the backup route.
You should do    Support: suggest card payment. No refunds needed, failed
                 payments aren't charged. Stores: nothing.
Next update      18:45

where   support → #incident (pinned) · stores → store leads' group
        Femke → direct message (SEV1, ≤ 15 min) · offices → status page
cadence SEV1 every 15 min · SEV2 every 30 min · even if "no change"
"""),
    tools="tools: a pinned template, a store leads' group, and a hosted status page (several are cheap or free for small teams).",
    ladder=[("people find out by themselves", ["From complaints, shelves, tweets.", "Different stories."]),
            ("four audiences, four lines", ["Fixed places and cadence.", "A status page for clients."]),
            ("templated from the tool", ["Declaring an incident drafts the first update.", "Reminders at each cadence."]),
            ("customers told automatically", ["Affected customers notified in the app.", "Status page updated from the incident."])],
    ladder_now=1,
    baseline="Each line compares <b>people finding out on their own</b> to <b>four audiences with fixed places, four lines and a promised next update</b>.",
    ratings=[(2, 4, "Support can tell customers what to do."),
             (3, 3, "Neutral."),
             (3, 3, "Fixers are interrupted less."),
             (3, 3, "Neutral."),
             (1, 4, "Everyone gets one story at the same time."),
             (3, 3, "Neutral."),
             (3, 3, "A cheap status page."),
             (2, 3, "Fewer “what's going on?” calls to on-call."),
             (3, 3, "A template and a habit.")],
    pitfalls=[("Updating only when there's news", "Silence reads as “nobody's on it”.", "promise a time and keep it."),
              ("Jargon", "“502s from the PSP gateway”.", "write what customers see."),
              ("Too many places", "Some people read the old one.", "one place per audience."),
              ("The fixer writes the updates", "Fixing slows down; updates stop.", "a separate communication role.")],
    use=["People affected hear from someone other than you.", "Support doesn't know what to tell customers.", "Business clients depend on you.", "Every SEV1 and SEV2."],
    skip=["SEV3 and SEV4 with no customer impact: a line in the ticket."],
    related=["<b>Who Is in Charge?</b> (this volume)", "<b>Telling a Business Client</b> (this volume)", "<b>Delivering Bad News</b> (Grace, vol. 5)", "<b>Who Hears What, and When?</b> (Sanne, vol. 5)"],
    quiz=[("What are the four lines of every update?", "What customers see, what we're doing, what you should do, next update at."),
          ("Why send an update when nothing changed?", "Silence reads as nobody being on it; the promised time is the promise."),
          ("Who should write updates during an incident?", "The communication person, not the fixer or the lead."),
          ("What was Larder's status page for?", "Business customers (office managers) to see incidents affecting business ordering or deliveries."),
          ("How did Femke hear about 3 July?", "On Monday, from a customer's tweet: the thing the new process prevents.")],
    quiz_sit=[("At 18:45 the next update is due, but the fixers have found nothing new. What does the communication person send?", "The same four lines, updated: still affected, still working on it (what's being tried now), same advice, next update at 19:15. Short, on time.")],
    try_it="For your most important service, list who needs to know when it breaks, where each group would read an update, and write your own four-line template. When did your last incident's first update go out?",
    remember="People forgive <span class=\"hl\">delays</span>; they don't forgive <span class=\"hl\">silence</span>. Four lines, one place each, and a promised next time.",
    sources=["Betsy Beyer et al., <i>Site Reliability Engineering</i> (2016): chapter 14, managing incidents.",
             "Atlassian, <i>Incident Management Handbook</i> (2020): incident communication.",
             "AXELOS, <i>ITIL 4: Incident management</i> and <i>Relationship management</i> practice guides (2020)."],
)

# ------------------------------------------------------------------ 04 Who's Next If Nobody Answers?
es_problem = Doodle(760, 250, "Doodle of Sunday 2 August 2026, 07:20. Rotterdam's store heartbeat goes silent just as the store opens. The page goes to Ana, on call; her phone had updated overnight and the update had switched on a do-not-disturb mode that silenced the paging app. Nobody else is paged. At 07:42 Yara calls Eli's personal number. Twenty-two minutes with nobody on it.",
                    "A page into a silent phone, and no second name. 22 minutes until Yara phones Eli.")
es_problem.icon("phone", 50, 30, 1.6)
es_problem.box(130, 30, 260, 90, "page → Ana", "pink", sub="phone silenced by an update", size=18, subsize=14)
es_problem.arrow(396, 75, 452, 75, dash=True)
es_problem.box(456, 30, 290, 90, "next: nobody", "paper", sub="no escalation set", dash=True, size=18, subsize=14)
es_problem.note(380, 170, "07:42 Yara calls Eli's personal number", "red", size=19)
es_problem.note(380, 210, "22 minutes with nobody on it", "pen", size=17)

es_analogy = Doodle(760, 220, "Doodle of a school's list for when a child is sick: call mum; if no answer in five minutes, call dad; if no answer, call grandma. The list is on file, so the school doesn't have to guess and doesn't have to wait.",
                    "Mum, then dad after five minutes, then grandma. The school doesn't guess, and doesn't wait.")
es_analogy.row([("mum", "first", "green"), ("dad", "after 5 min", "y"), ("grandma", "after 10 min", "y")], x=100, y=40, h=96, w=170, gap=50, size=20, subsize=15, arrows=True)
es_analogy.note(380, 190, "a written order, with times", "pen", size=18)

es_how = Doodle(760, 360, "Larder's escalation policy from Monday 3 August 2026. A page goes to the primary. If not acknowledged within 5 minutes, it also pages the secondary. If not acknowledged within 15 minutes, it pages Eli as escalation and phones him. Separately, the incident lead can pull in a specialist from a short list: payments, Cho; mobile and handhelds, Dee; database, Eli; stores, the store lead on duty. Each rota member tests their phone with a test page on their first on-call morning.",
                "5 minutes → secondary; 15 → Eli by phone call. Specialists by name. A test page every Monday.")
es_how.row([("primary", "page", "green"), ("secondary", "after 5 min", "y"), ("Eli", "after 15 min · phone call", "pink")], x=14, y=14, h=96, w=220, gap=36, size=19, subsize=13, arrows=True)
es_how.box(14, 136, 732, 110, None, "paper")
es_how.head(380, 164, "specialists the lead can pull in", size=17)
es_how.text(380, 198, "payments: Cho · mobile + handhelds: Dee · database: Eli", size=16)
es_how.text(380, 226, "a store: its lead on duty · vendors: ops/vendors.md", size=16)
es_how.box(110, 272, 540, 64, "first on-call morning: send yourself a test page", "green", size=16)

ESCALATION = dict(
    slug="escalation",
    kicker="a.k.a. “escalation policies”",
    tldr="An <b>escalation policy</b> says who is paged <b>next, and after how long</b>, when the first person doesn't answer: primary → secondary after 5 minutes → a named escalation after 15, by phone call. Alongside it, keep a short list of <b>specialists</b> the incident lead can pull in. And <b>test the chain</b>: phones change, updates switch on silent modes, numbers go stale. A single page into a silent phone shouldn't mean nobody comes.",
    chips=[("Family", "responding"), ("Lives in", "the paging tool's escalation policy, ops/on-call.md"), ("Pairs with", "the on-call rota, incident roles, vendor escalation")],
    itil=dict(groups=["service"], chain=["deliver"], practices=["incident management"],
              sre="“escalation policy”; acknowledgement timeouts", principles=["Think and work holistically"],
              older="ITIL v3: functional and hierarchical escalation"),
    pager=dict(when="Sun 2 Aug 2026 · Ana on call", lines=[
        ("07:20", "<b>PAGE</b> store_heartbeat Rotterdam silent 5 min → Ana"),
        ("07:25", "no acknowledgement · no escalation configured"),
        ("07:35", "Rotterdam pickers working offline (≈ 2 h of grace)"),
        ("07:42", "Yara phones Eli's personal number"),
        ("07:44", "Eli: router rebooted after a power blip, stuck on 4G setup"),
        ("08:01", "router fixed remotely · heartbeat green")]),
    problem_side="Larder, Sunday 2 August 2026",
    problem="""  <p class="lead">At 07:20 on a Sunday, just as the store opens, Rotterdam's store heartbeat goes silent. The page goes to Ana, who is on call. Overnight, her phone had installed an update that <b>switched on a do-not-disturb mode and silenced the paging app</b>. No one else is paged: the paging tool has no escalation set. <span class="hl-pink">For 22 minutes nobody is on it</span>, until Yara phones Eli's personal number at 07:42.</p>
  <ul>
    <li>One silent phone means no response at all.</li>
    <li>The secondary exists on paper, but the tool doesn't know about them.</li>
    <li>In the end the front line works around the process, by calling Eli.</li>
  </ul>""",
    problem_figs=[es_problem],
    analogy_side="the school's sick-child list",
    analogy="""  <p>When a child is sick, the school has a <b>list on file</b>: call mum; if there's no answer in five minutes, call dad; then grandma. The school doesn't guess who might be free, and it doesn't wait an hour for mum to call back. The order and the times were decided <b>before anyone was sick</b>.</p>""",
    analogy_figs=[es_analogy],
    map=[("Mum, then dad, then grandma", "Primary, then secondary, then Eli"),
         ("Five minutes before the next call", "Acknowledgement timeout: 5 and 15 minutes"),
         ("The list on file", "The escalation policy in the paging tool"),
         ("A specialist (the family doctor)", "Cho for payments, Dee for handhelds"),
         ("Checking the numbers each year", "A test page on the first on-call morning")],
    how_side="a chain with timeouts, a specialist list, and a test page",
    how="""  <p>On <b>Monday 3 August</b> the escalation policy goes into the paging tool:</p>
  <ul>
    <li>A page goes to the <b>primary</b>.</li>
    <li>If it isn't acknowledged in <b>5 minutes</b>, it pages the <b>secondary</b> as well.</li>
    <li>After <b>15 minutes</b> it pages <b>Eli</b> as escalation <b>and phones him</b>, because a phone call gets through settings that a push notification doesn't.</li>
  </ul>
  <p>Separately, the incident lead has a <b>specialist list</b> to pull people in on purpose: payments → Cho, mobile and handhelds → Dee, database → Eli, a store → its lead on duty, vendors → <code>ops/vendors.md</code>.</p>
  <p>The last change is the cheapest: on their <b>first on-call morning</b>, each primary sends themselves a <b>test page</b> and checks it rings. Ana's phone setting is in the review as what it was, a phone setting and not a person failing, and the test page catches it in two more phones in August.</p>""",
    how_figs=[es_how],
    steps=[("Set an acknowledgement timeout", "5 minutes is common for paging alerts."),
           ("Escalate to the secondary, then a named person", "Each step in the tool, not just on paper."),
           ("Use a phone call at the last step", "It gets through more silent modes than a push notification."),
           ("Keep a short specialist list", "For the lead to pull people in on purpose."),
           ("Test the chain every rota week", "A test page on the first morning."),
           ("Review every missed page without blame", "It's usually a setting, not a person.")],
    vocab=[("Acknowledge (ack)", "Telling the paging tool “I've got it”, which stops escalation."),
           ("Acknowledgement timeout", "How long before the page goes to the next person."),
           ("Escalation policy", "The ordered chain of who is paged, with timeouts."),
           ("Functional escalation", "Pulling in someone with the right skills (a specialist)."),
           ("Hierarchical escalation", "Telling someone more senior because of impact or risk."),
           ("Test page", "A deliberate page to check that phone and settings work.")],
    code=dict(file="ops/on-call.md#escalation", note="from Mon 3 August 2026", plain=True, src="""
# Escalation

paging alert →  primary
  no ack 5 min  →  + secondary
  no ack 15 min →  + Eli (escalation) · page AND phone call

specialists (the lead pulls them in on purpose, any hour for SEV1)
  payments ............ Cho
  mobile + handhelds .. Dee
  database ............ Eli (until a second platform engineer joins)
  a store ............. its lead on duty (rota in the store leads' group)
  vendors ............. ops/vendors.md (support hours + emergency lines)

first on-call morning:  send yourself a test page; fix your phone if it doesn't ring
"""),
    tools="tools: the paging tool's escalation policies (even free tiers have them), a phone-call step, a Monday test page.",
    ladder=[("one page, hope it's seen", ["No timeout, no next person.", "Front line calls personal numbers."]),
            ("a chain with timeouts", ["Secondary at 5 min, escalation at 15.", "Test page each rota week."]),
            ("policies per service", ["Each critical service has its own chain.", "Specialists paged from the tool."]),
            ("measured", ["Time to acknowledge tracked per person and hour.", "Gaps fixed before they bite."])],
    ladder_now=1,
    baseline="Each line compares <b>one page into one phone</b> to <b>an escalation chain with timeouts, a specialist list and weekly test pages</b>.",
    ratings=[(2, 3, "A store doesn't wait 22 minutes."),
             (3, 3, "Neutral."),
             (2, 4, "Someone always acknowledges within 15 minutes."),
             (3, 3, "Neutral."),
             (2, 3, "Who comes next is written in the tool."),
             (3, 3, "Neutral."),
             (3, 3, "Neutral."),
             (2, 4, "Nobody carries the whole risk of one silent phone."),
             (4, 4, "An hour to set up.")],
    pitfalls=[("The chain only on paper", "The secondary is never actually paged.", "set it in the tool."),
              ("Push notifications only", "Silent modes swallow them.", "phone call at the last step."),
              ("Blaming the person", "Ana gets the blame for a phone update.", "review the setting, test everyone's phone."),
              ("Specialists by guesswork", "The lead calls whoever answered last time.", "a short named list.")],
    use=["Pages have gone unanswered.", "The front line calls people's personal numbers.", "A new person joins the rota.", "After a phone or tool change."],
    skip=["Never, if anything pages at night."],
    related=["<b>Who Gets Woken Up?</b> (vol. 1)", "<b>Who Is in Charge?</b> (this volume)", "<b>The Vendor Is Down at Peak</b> (next note)"],
    quiz=[("What does an acknowledgement do?", "Tells the tool someone has it, which stops further escalation."),
          ("What is Larder's chain?", "Primary; after 5 minutes also the secondary; after 15 also Eli, by page and phone call."),
          ("Why a phone call at the last step?", "It gets through silent modes and notification settings that push notifications don't."),
          ("What's the difference between functional and hierarchical escalation?", "Functional pulls in skills (a specialist); hierarchical informs someone senior because of impact."),
          ("What did the review conclude about Ana?", "Nothing about Ana: a phone update changed a setting. The fix was the chain and a weekly test page.")],
    quiz_sit=[("Your test page doesn't ring on Monday morning. What do you do?", "Fix the phone settings now, send another test, and tell the secondary in the handover in case it happens again. It's much better to find out on Monday at 10:00 than on Sunday at 07:20.")],
    try_it="Look at your paging setup: if the first person doesn't answer, who is paged next, and after how long? Send yourself a test page today. Does it ring with your phone's current settings?",
    remember="A page into <span class=\"hl\">one silent phone</span> is a page to nobody. Set a <span class=\"hl\">chain with timeouts</span>, and test it weekly.",
    sources=["PagerDuty, <i>Incident Response documentation</i> (open source): escalation policies.",
             "AXELOS, <i>ITIL 4: Incident management</i> practice guide (2020): escalation.",
             "Betsy Beyer et al., <i>Site Reliability Engineering</i> (2016): chapter 11, being on-call."],
)

# ------------------------------------------------------------------ 05 The Vendor Is Down at Peak
ve_problem = Doodle(760, 260, "Doodle of Friday 21 August 2026, 17:30. StockPilot's API stops answering. Its status page says 'all systems operational' for the first 40 minutes. StockPilot's support works 09:00 to 17:00 on weekdays; the email gets an automatic reply. The stock in Larder's app goes stale, and customers order items that ran out, which become substitutions and refunds. It lasts 2 hours 10 minutes, across the Friday peak.",
                    "The vendor is down, its status page says it isn't, and its support went home at 17:00.")
ve_problem.box(14, 30, 230, 100, "StockPilot API", "pink", sub="down 17:30", size=19, subsize=15)
ve_problem.box(264, 30, 230, 100, "status page", "green", sub="“operational” 40 min", size=19, subsize=15)
ve_problem.box(514, 30, 232, 100, "support", "paper", sub="09:00–17:00 · auto-reply", size=19, subsize=14)
ve_problem.box(110, 160, 540, 60, "stale stock → swaps and refunds · 2 h 10 min, across the peak", "y", size=16)

ve_analogy = Doodle(760, 220, "Doodle of a bakery that buys its flour from one mill. The baker keeps the mill's emergency number on the wall, knows the mill closes at five, keeps two days of flour in the back, and has a second supplier she could phone if she had to. She worked all this out on a quiet Tuesday, not during the Saturday rush.",
                    "The mill's number on the wall, two days of flour in the back, and a plan made on a quiet Tuesday.")
ve_analogy.icon("bucket", 60, 40, 1.3)
ve_analogy.row([("mill's number", "on the wall", "green"), ("closes at 5", "known", "y"), ("2 days' flour", "in the back", "blue"), ("plan B mill", "just in case", "paper")], x=150, y=40, h=96, gap=14, size=16, subsize=13)
ve_analogy.note(450, 190, "work it out on a quiet day", "pen", size=18)

ve_how = Doodle(760, 380, "Larder's vendor sheet, written in the week after 21 August 2026. For each vendor on a critical or important path: what it does for us, support hours, emergency line or not, status page, contract owner, and what we do when it's down. StockPilot: business hours only, no emergency line; when the sync is stale for more than 15 minutes, a switch marks low-stock items as unavailable, so customers can't order what may have run out. The switch was built in September. The payment provider has a 24/7 emergency line. Larder doesn't pay for StockPilot's premium support because the contract ends in June 2027.",
                "Know the hours, the line and plan B before the Friday. StockPilot's plan B is a switch on our side.")
ve_how.box(14, 14, 732, 40, "vendor · does · support hours · emergency line · status page · owner · when it's down", "paper", size=14)
rows = [("StockPilot", "09–17 weekdays · no line", "stale > 15 min → low-stock items unavailable", "pink"),
        ("PSP A", "24/7 line", "switch to the backup route; support suggests cards", "green"),
        ("address lookup", "email only", "manual address entry allowed", "y"),
        ("helpdesk SaaS", "24/7 status page", "email inbox fallback for Sam", "y")]
for i, (v, h, b, f) in enumerate(rows):
    y = 66 + i * 66
    ve_how.box(14, y, 170, 56, v, f, size=15)
    ve_how.box(194, y, 200, 56, h, "paper", size=13)
    ve_how.box(404, y, 342, 56, b, "paper", size=13)
ve_how.note(380, 350, "the plan is on our side; the vendor's hours are a fact", "pen", size=16)

VENDOR_ESCALATION = dict(
    slug="vendor-escalation",
    kicker="a.k.a. “supplier management in an incident”",
    tldr="Every vendor on a critical path is part of your service, including its <b>support hours, its emergency line (or lack of one) and its status page</b>. Find these out <b>on a quiet day</b> and write them down. More important, decide <b>what you will do on your side</b> when the vendor is down, because their fix is out of your hands. Watch the vendor yourself instead of trusting their status page.",
    chips=[("Family", "responding"), ("Lives in", "ops/vendors.md, linked from every dependency map"), ("Pairs with", "the dependency map, escalation, supplier management (vol. 4)")],
    itil=dict(groups=["general", "service"], chain=["engage", "deliver"], practices=["supplier management", "incident management"],
              sre="“your dependencies' reliability is your reliability”", principles=["Think and work holistically"],
              older="ITIL v3: supplier management, underpinning contracts"),
    pager=dict(when="Fri 21 Aug 2026 · Cho on call", lines=[
        ("17:30", "<b>PAGE</b> stock_sync stale 15 min · all stores"),
        ("17:34", "Cho: StockPilot API timing out · their status: operational"),
        ("17:41", "Cho restarts sync (RB-09) · still timing out"),
        ("17:52", "email to StockPilot support → auto-reply: “back Monday 09:00”"),
        ("18:10", "StockPilot status page: “investigating”"),
        ("19:40", "StockPilot recovers · ≈ 140 orders with out-of-stock items")]),
    problem_side="Larder, Friday 21 August 2026",
    problem="""  <p class="lead">At 17:30 on a Friday, StockPilot's API stops answering. For the first 40 minutes its status page says <b>“all systems operational”</b>. Its support works <b>09:00–17:00 on weekdays</b>, and Cho's email gets an automatic reply. Larder's app keeps showing stock from 17:30, customers order items that have run out, and they turn into substitutions and refunds. <span class="hl-pink">It lasts 2 hours 10 minutes, across the Friday peak, and there is nothing on Larder's side to do except wait.</span></p>
  <ul>
    <li>Nobody knew StockPilot's support hours until that evening.</li>
    <li>The vendor's status page was later than our own alert.</li>
    <li>There was no plan for “the vendor is down”, only for “our sync is stuck”.</li>
  </ul>""",
    problem_figs=[ve_problem],
    analogy_side="the bakery's flour mill",
    analogy="""  <p>A bakery buys its flour from one mill. The baker keeps the <b>mill's emergency number on the wall</b>, knows the mill <b>closes at five</b>, keeps <b>two days of flour in the back</b>, and knows a second mill she could phone if she had to. She worked all this out <b>on a quiet Tuesday</b>, not during the Saturday rush.</p>""",
    analogy_figs=[ve_analogy],
    map=[("The mill", "StockPilot, the PSP, the address lookup service"),
         ("Closes at five", "Support 09:00–17:00 on weekdays"),
         ("The emergency number on the wall", "ops/vendors.md: lines, status pages, owners"),
         ("Two days of flour in the back", "The low-stock switch on Larder's side"),
         ("Worked out on a quiet Tuesday", "The vendor sheet, written before the next Friday")],
    how_side="a sheet per vendor, our own plan B, and our own eyes",
    how="""  <p>In the week after, Eli writes <code>ops/vendors.md</code>. For every vendor on a critical or important path it lists what the vendor does for us, its <b>support hours</b>, whether there's an <b>emergency line</b>, its <b>status page</b>, the <b>contract owner</b> at Larder, and <b>what we do when it's down</b>.</p>
  <ul>
    <li><b>StockPilot</b>: business hours only, no emergency line. Premium support would cost more than it's worth, because the contract ends in June 2027 (ADR 0016's exit plan). So plan B is on Larder's side: if the sync is stale for <b>more than 15 minutes</b>, a switch marks <b>low-stock items as unavailable</b>, so customers can't order what may have run out. Ben builds it in September.</li>
    <li><b>PSP A</b>: a 24/7 emergency line, now written down, and the backup route.</li>
    <li><b>Address lookup</b>: email support only; plan B is to allow manual address entry.</li>
  </ul>
  <p>Larder's own alert on the sync caught the outage <b>40 minutes before</b> StockPilot's status page did. So the rule is: <b>trust your own monitoring, and use the vendor's status page as confirmation</b>.</p>""",
    how_figs=[ve_how],
    steps=[("List vendors on critical paths", "From the dependency maps."),
           ("Find support hours and emergency lines", "From the contract, on a quiet day."),
           ("Name a contract owner per vendor", "Who can push the vendor, and who pays."),
           ("Decide plan B on your side", "Degrade, switch, or tell customers."),
           ("Watch the vendor yourself", "Your alert is usually earlier than their status page."),
           ("Review vendors after their incidents", "Is the contract still right?")],
    vocab=[("Vendor (supplier)", "A company whose service is part of yours."),
           ("Support hours", "When the vendor will answer; often not when you need them."),
           ("Underpinning contract", "The contract that makes a vendor's part of your service possible."),
           ("Graceful degradation", "Doing less, safely, when a part is missing."),
           ("Status page", "The vendor's own report of its incidents, often late."),
           ("Exit plan", "How you would leave the vendor; it affects how much to invest in them.")],
    code=dict(file="ops/vendors.md", note="written 24–28 August 2026", plain=True, src="""
vendor          does for us          support         emergency  status page   owner   when it's down (our side)
StockPilot      stock per store      09–17 weekdays  none       yes (late)    Eli     stale > 15 min → low-stock
                                                                                       items unavailable (switch, Sep)
PSP A           cards + iDEAL        24/7            +31 …      yes           Cho     backup route · suggest cards
address lookup  checkout addresses   email, 1 day    none       no            Ben     allow manual address entry
push service    "on its way"         email           none       yes           Dee     nothing: checkout unaffected
helpdesk SaaS   support + IT queue   24/7            chat       yes           Sam     email inbox fallback
cloud           everything           24/7 (plan)     console    yes           Eli     see continuity (vol. 5)

rule: our alert first, their status page as confirmation.
StockPilot premium support: not bought (contract ends Jun 2027, ADR 0016).
"""),
    tools="tools: the contracts, one table, and your own monitoring on every vendor call.",
    ladder=[("find out during the incident", ["Hours and numbers unknown.", "Wait for the vendor."]),
            ("a vendor sheet and plan B", ["Hours, lines, owners.", "A switch on our side."]),
            ("vendors monitored like our own services", ["Per-vendor error rates and alerts.", "Plan B triggered by the alert."]),
            ("plan B automatic", ["Degrades by itself when the vendor fails.", "People confirm, not act."])],
    ladder_now=1,
    baseline="Each line compares <b>discovering the vendor's hours mid-incident</b> to <b>a vendor sheet with our own plan B and our own monitoring</b>.",
    ratings=[(2, 4, "Customers can't order what may have run out."),
             (3, 3, "The vendor is as reliable as it was."),
             (2, 3, "Plan B starts in 15 minutes, not after the vendor."),
             (3, 3, "Neutral."),
             (2, 4, "Who to call, and when they answer, is written down."),
             (3, 3, "Neutral."),
             (3, 4, "No premium support for a contract that's ending."),
             (2, 3, "On-call knows what to do instead of waiting."),
             (3, 3, "Two days, then a review per vendor incident.")],
    pitfalls=[("Trusting their status page", "It's often the last to know.", "monitor the vendor yourself."),
              ("Plan B is “call the vendor”", "At 17:30 on a Friday nobody answers.", "decide what you do on your side."),
              ("Buying premium support by reflex", "Paying for a vendor you're leaving.", "match it to the contract's future."),
              ("No contract owner", "Nobody can push the vendor or check the terms.", "one owner per vendor.")],
    use=["A vendor sits on a critical path.", "A vendor's outage caught you out.", "Before a peak (Christmas, King's Day).", "When choosing or renewing a vendor."],
    skip=["Vendors nobody would notice for a day."],
    related=["<b>What Is Connected to What?</b> (vol. 1)", "<b>SaaS & Vendor Integration</b> (Ana, vol. 4)", "<b>Circuit Breaker</b> (distributed, vol. 1)", "<b>Was It a Change?</b> (this volume)"],
    quiz=[("What should a vendor sheet contain?", "What it does for us, support hours, emergency line, status page, contract owner, and what we do when it's down."),
          ("What was StockPilot's plan B?", "A switch on Larder's side: if the sync is stale over 15 minutes, low-stock items become unavailable."),
          ("Why not buy StockPilot's premium support?", "The contract ends in June 2027; plan B on Larder's side is cheaper and works out of hours."),
          ("Who found the outage first?", "Larder's own alert, 40 minutes before StockPilot's status page."),
          ("What's graceful degradation?", "Doing less, safely, when a part is missing, instead of failing or misleading customers.")],
    quiz_sit=[("The PSP's status page says “operational” but your checkout errors at the payment step are at 8 %. What do you do?", "Trust your own signal: declare SEV2, call the PSP's 24/7 line, switch to the backup route if errors continue, and tell support to suggest cards.")],
    try_it="Pick the vendor your most important service depends on most. Find its support hours, emergency line and status page in the contract. Then write what you would do on your side if it were down for two hours on your busiest evening.",
    remember="The vendor's hours are <span class=\"hl\">a fact</span>; your plan B is <span class=\"hl\">a choice</span>. Make it on a quiet day, and watch them with your own eyes.",
    sources=["AXELOS, <i>ITIL 4: Supplier management</i> practice guide (2020).",
             "Betsy Beyer et al., <i>The Site Reliability Workbook</i> (2018): chapter on third-party dependencies.",
             "Michael T. Nygard, <i>Release It!</i> (2nd ed., 2018): integration points and stability patterns."],
)

# ------------------------------------------------------------------ 06 Who Fixes What?
ts_problem = Doodle(760, 260, "Doodle of a ticket's journey in early September 2026. Rotterdam reports that a label printer prints blank labels. Sam's team, now the first line for store tickets, passes it to on-call; on-call passes it to Dee because printers talk to the picker app; Dee passes it back to Eli because it's the network. Four hops, two days, and the fix was a known one: power-cycle and reload the label roll.",
                    "Four hops, two days, for a fix that was already known.")
ts_problem.row([("Sam's team", "first line", "paper"), ("on-call", "…", "paper"), ("Dee", "“printers?”", "paper"), ("Eli", "“network?”", "paper")], x=14, y=30, h=84, gap=40, size=16, subsize=13, arrows=True)
ts_problem.box(110, 150, 540, 64, "fix: power-cycle + reload the roll (known since May)", "pink", stroke="red", size=16)
ts_problem.note(380, 240, "two days · four hops", "red", size=18)

ts_analogy = Doodle(760, 230, "Doodle of a hospital: a nurse at the front treats common things straight away from a protocol card; anything unusual gets a doctor; a truly strange case gets three specialists in one room at once, instead of being sent from department to department for a week.",
                    "Common things fixed at the front from a card; strange things get the specialists in one room.")
ts_analogy.box(14, 40, 340, 100, "the common", "green", sub="nurse + protocol card, at once", size=19, subsize=14)
ts_analogy.box(406, 40, 340, 100, "the strange", "y", sub="specialists in one room, together", size=19, subsize=14)
ts_analogy.note(380, 190, "not: from department to department for a week", "red", size=18)

ts_how = Doodle(760, 380, "Larder's rules for store tickets from 14 September 2026. Step one: Sam's team checks the known-error list; if there's a match, they fix it or guide the store through it at once. Step two: if it's not known, no passing on: the ticket goes into the #help-stores channel where on-call and whoever knows (Dee, Eli, the store lead) look at it together, and one person takes it by name. Step three: when it's fixed, if it could happen again, it's added to the known-error list. In October, 38 percent of store tickets were fixed by Sam's team alone; median hops per ticket fell from 2.4 to 1.1.",
                "Known → fixed at the first line from the list. New → swarmed in one place, one named owner. Then add it to the list.")
ts_how.box(14, 14, 230, 110, "1. known?", "green", sub="first line fixes it from the list", size=18, subsize=13)
ts_how.arrow(250, 69, 290, 69)
ts_how.box(296, 14, 220, 110, "2. new?", "y", sub="swarm in #help-stores · one owner", size=18, subsize=13)
ts_how.arrow(522, 69, 562, 69)
ts_how.box(568, 14, 178, 110, "3. add it", "blue", sub="to the known-error list", size=18, subsize=13)
ts_how.row([("38 %", "fixed at the first line (Oct)", "green"), ("2.4 → 1.1", "hops per ticket", "green")], x=110, y=170, h=96, w=250, gap=40, size=24, subsize=14)
ts_how.note(380, 310, "no passing on without a conversation", "red", size=18)
ts_how.note(380, 350, "swarming for the new · tiers for the known", "pen", size=17)

TIERS_SWARMING = dict(
    slug="tiers-swarming",
    kicker="a.k.a. “tiered support vs swarming”",
    tldr="<b>Tiers</b> (first line, second line, specialists) work well for <b>known</b> problems: the first line fixes them from a list. For <b>new</b> problems, passing a ticket from tier to tier is slow, and everyone guesses. <b>Swarming</b> works better there: the people who might know look at it together, in one place, and one of them takes it by name. Use both, and make every new fix a known one for next time.",
    chips=[("Family", "responding"), ("Lives in", "the service desk process, #help-stores, the known-error list"), ("Pairs with", "the service desk, known errors, service requests")],
    itil=dict(groups=["service"], chain=["deliver", "improve"], practices=["service desk", "incident management"],
              sre="(interrupt handling; a single owner per issue)", principles=["Collaborate and promote visibility", "Optimise and automate"],
              older="ITIL v3: functional escalation through first, second and third line"),
    problem_side="Larder, early September 2026",
    problem="""  <p class="lead">From 1 September Sam's support team is the <b>first line</b> for store tickets, so on-call isn't interrupted for every printer. In the first week Rotterdam reports a label printer printing blank labels. Sam's team passes it to on-call, on-call passes it to Dee (“printers talk to the picker app”), and Dee passes it to Eli (“probably the network”). <span class="hl-pink">Four hops and two days</span>, and the fix had been known since May: power-cycle the printer and reload the roll.</p>
  <ul>
    <li>Each hop adds hours, and each person starts again from zero.</li>
    <li>The first line can't fix what nobody has written down for them.</li>
    <li>“Not mine” becomes a way of handling tickets.</li>
  </ul>""",
    problem_figs=[ts_problem],
    analogy_side="the nurse's card and the specialists' room",
    analogy="""  <p>At a good clinic, a nurse at the front <b>treats common things straight away</b>, from a protocol card. Unusual cases see a doctor. A <b>truly strange case</b> gets the specialists into <b>one room together</b>, instead of being sent from department to department for a week while each one says “not ours”.</p>""",
    analogy_figs=[ts_analogy],
    map=[("The nurse and the protocol card", "Sam's team and the known-error list"),
         ("Common things treated at once", "Known store problems fixed at the first line"),
         ("Specialists in one room", "#help-stores: on-call, Dee, Eli, the store lead"),
         ("Department to department", "Passing a ticket from tier to tier"),
         ("A new card after a strange case", "Each new fix added to the known-error list")],
    how_side="tiers for the known, swarming for the new, then make it known",
    how="""  <p>Eli and Sam agree three steps on <b>14 September</b>:</p>
  <ol>
    <li><b>Known?</b> Sam's team checks the <b>known-error list</b> (next notes). If there's a match, they fix it or guide the store through it at once.</li>
    <li><b>New?</b> No passing on. The ticket goes into <code>#help-stores</code>, where on-call and anyone who might know (Dee for devices, Eli for networks, the store lead) look at it <b>together</b>. <b>One person takes it by name</b> and keeps it until it's fixed or deliberately handed over with a conversation.</li>
    <li><b>Fixed, and could it happen again?</b> The fix is added to the known-error list, so next time it's step 1.</li>
  </ol>
  <p>In October Sam's team fixes <b>38 %</b> of store tickets alone, and the median number of hops per ticket drops from <b>2.4 to 1.1</b>. Incidents keep their own roles (this volume). This is for everyday tickets.</p>""",
    how_figs=[ts_how],
    steps=[("Give the first line a list of known fixes", "Short, searchable, kept current."),
           ("Let them fix, not just forward", "With the access and the steps they need."),
           ("Swarm the new in one place", "The people who might know look together."),
           ("One owner by name", "Keeps it until it's fixed or handed over in a conversation."),
           ("Turn new fixes into known ones", "Each fix that could recur is added to the list."),
           ("Measure hops and first-line fixes", "Fewer hops, more fixed at the front.")],
    vocab=[("First line", "The first people to handle a ticket; at Larder, Sam's team."),
           ("Tiered support", "Tickets move up through levels of skill."),
           ("Swarming", "The people who might know work on a new problem together, at once."),
           ("Ticket hop", "Passing a ticket to another person or group."),
           ("Ownership", "One named person responsible for a ticket until it's closed."),
           ("Shift left", "Moving fixes closer to the user: first line, or the user themselves.")],
    code=dict(file="ops/desk/store-tickets.md", note="agreed with Sam · Mon 14 September 2026", plain=True, src="""
# Store tickets: who fixes what

1 known?   first line (Sam's team) searches ops/known-errors.md
           match → fix or guide the store · note the KE number on the ticket
2 new?     no forwarding. Post in #help-stores with the ticket link.
           on-call + Dee (devices) + Eli (network) + store lead look together
           ONE person takes it: "mine" · keeps it until fixed or handed over
           by a conversation, not a reassignment
3 after    could it happen again? → add to ops/known-errors.md (owner: fixer)

measures (monthly): fixed at first line · hops per ticket · time to fix
Oct 2026: 38 % at first line · median hops 2.4 → 1.1
"""),
    tools="tools: the helpdesk, one chat channel for swarming, and the known-error list.",
    ladder=[("pass it on", ["Tickets hop for days.", "Everyone starts from zero."]),
            ("tiers for the known, swarm the new", ["Known-error list at the first line.", "One owner per new problem."]),
            ("suggested fixes", ["The helpdesk suggests known errors from the ticket text.", "Hops tracked automatically."]),
            ("self-service", ["Stores fix known things themselves (vol. 4).", "Desk and swarm see only the new."])],
    ladder_now=1,
    baseline="Each line compares <b>passing tickets from tier to tier</b> to <b>known fixes at the first line and swarming the new</b>.",
    ratings=[(2, 4, "Stores get known fixes at once."),
             (3, 3, "Neutral."),
             (2, 4, "Hours instead of days for new problems."),
             (3, 3, "Neutral."),
             (2, 3, "One owner, one place for each new problem."),
             (2, 4, "Repeat problems handled without engineers."),
             (3, 3, "Neutral."),
             (2, 4, "On-call interrupted only by the new."),
             (3, 3, "A short agreement and a list.")],
    pitfalls=[("Forwarding as a reflex", "“Not mine” is a way of closing tickets.", "no forwarding: swarm, then one owner."),
              ("A first line without a list", "They can only pass things on.", "give them known fixes and the access to apply them."),
              ("Swarming everything", "Five people on every printer.", "swarm the new; tiers for the known."),
              ("New fixes never written down", "The same swarm next month.", "add it to the list before closing.")],
    use=["Tickets hop between people for days.", "A first line exists but rarely fixes things.", "The same problems keep coming back.", "Engineers are interrupted by known issues."],
    skip=["During an incident: use incident roles instead."],
    related=["<b>Where Do People Report Problems?</b> (vol. 1)", "<b>We Know the Bug, Now What?</b> (this volume)", "<b>Can I Have a New Handheld?</b> (vol. 1)"],
    quiz=[("When do tiers work well?", "For known problems: the first line fixes them from a list."),
          ("What is swarming?", "The people who might know work on a new problem together, in one place, and one takes it by name."),
          ("What's Larder's rule about forwarding?", "No forwarding of new problems: swarm in #help-stores, then one owner."),
          ("What happens after a new problem is fixed?", "If it could recur, it's added to the known-error list so the first line can fix it next time."),
          ("What changed in October?", "38 % fixed at the first line; median hops 2.4 → 1.1.")],
    quiz_sit=[("A ticket arrives that looks like the network but might be the device. Nobody is sure. What happens?", "It goes to #help-stores; Dee and Eli look together; one of them says “mine” and keeps it. No forwarding back and forth.")],
    try_it="Take your last ten tickets that were reassigned. How many hops did each take, and how many ended with a fix someone already knew? Write those fixes into a list your first line can use.",
    remember="<span class=\"hl\">Tiers for the known</span>, <span class=\"hl\">swarming for the new</span>, one owner by name, and every new fix becomes a known one.",
    sources=["AXELOS, <i>ITIL 4: Service desk</i> and <i>Incident management</i> practice guides (2020): swarming.",
             "Consortium for Service Innovation, <i>Intelligent Swarming</i> (2017).",
             "Consortium for Service Innovation, <i>KCS v6 Practices Guide</i> (2016)."],
)

NOTES = [SEVERITY, INCIDENT_ROLES, INCIDENT_COMMS, ESCALATION, VENDOR_ESCALATION, TIERS_SWARMING]
