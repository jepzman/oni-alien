# Series 2 · Book 5 · The IT Operations Notebook · Vol. 3 · Moving big things.
# Narrator: Eli (he/him). Facts: docs/larder-casebook.md, "Book 5, Vol. 3".

# ------------------------------------------------------------------ 10 Cutting Over a Store
co_problem = Doodle(760, 260, "Doodle of the warehouse move in March 2027. Ana's plan moves each store from StockPilot to WMS B with a router per store: Zuid first on 19 April, then Noord, Rotterdam and Utrecht. The architecture is clear. What isn't written down is the night itself: who does what at 23:00 on a Sunday, how the store lead knows it worked at 06:00 on Monday, and what makes someone say 'go back'.",
                    "The architecture is clear. The night itself, who does what at 23:00 and when to go back, isn't written down.")
co_problem.box(14, 30, 230, 100, "StockPilot", "paper", sub="since 2024", size=19, subsize=14)
co_problem.arrow(250, 80, 300, 80, label="router per store", ly=66)
co_problem.box(306, 30, 200, 100, "WMS B", "blue", sub="Zuid first, 19 Apr", size=19, subsize=14)
co_problem.box(536, 30, 210, 100, "the night", "pink", sub="who? when? go back if?", size=19, subsize=14)
co_problem.note(380, 190, "a migration plan isn't a cutover plan", "red", size=19)

co_analogy = Doodle(760, 220, "Doodle of a railway switching a line to a new signalling system over a weekend. Weeks of the new system running alongside the old, silently, comparing. A timetable for the switch night by the minute, a named person deciding go or no-go at a set time, a first train with engineers on board, and the old system kept ready to switch back until Wednesday.",
                    "Weeks running side by side, a switch night by the minute, a go / no-go at a set time, and the old system kept ready.")
co_analogy.icon("traffic", 50, 30, 1.2)
co_analogy.row([("side by side", "weeks, comparing", "blue"), ("go / no-go", "a set time, a name", "y"), ("first train", "engineers on board", "green"), ("old kept", "until Wednesday", "paper")], x=130, y=40, h=96, w=140, gap=14, size=16, subsize=12)
co_analogy.note(450, 190, "the night is planned to the minute", "pen", size=18)

co_how = Doodle(760, 400, "Eli's cutover plan for Zuid, used on Sunday 18 April 2027. T minus 7 days: shadow week, WMS B receives every change and the difference with StockPilot is checked daily; Zuid's was 0.3 percent, under the 0.5 limit. Sunday 21:00: go or no-go, decided by Eli with Tomás, on four criteria. 23:15, after the store closes: the router for Zuid switches to WMS B; first test pick list printed at 23:40. Monday 06:00: Tomás and Eli in the store for the first real picks. Way back until 2 May: switch the router back; StockPilot stays read-only for two weeks. Not on the calendar's windows or the King's Day freeze. Noord on Monday 24 May used the same plan; one surprise: the pick-list label format, fixed at 06:40.",
                "Shadow week, go / no-go at 21:00, switch at 23:15, people in the store at 06:00, a way back for two weeks.")
for i, (t, s, f) in enumerate([("T−7 shadow", "diff 0.3 % (≤ 0.5)", "blue"), ("Sun 21:00", "go / no-go · 4 criteria", "y"), ("Sun 23:15", "router → WMS B · test pick 23:40", "pink"), ("Mon 06:00", "Tomás + Eli in store", "green"), ("to 2 May", "way back: router", "paper")]):
    co_how.box(14 + i * 148, 14, 136, 120, t, f, sub=s, size=16, subsize=11)
co_how.box(14, 160, 732, 110, None, "paper")
co_how.head(380, 188, "go only if", size=17)
co_how.text(380, 218, "diff ≤ 0.5 % · test pick list prints · on-call + Eli + store lead available", size=14)
co_how.text(380, 244, "no SEV1/2 open · not in a window or freeze", size=14)
co_how.note(380, 310, "Noord, Mon 24 May: label format surprise, fixed 06:40", "pen", size=16)
co_how.note(380, 346, "Rotterdam 21 Jun · Utrecht 26 Jul: same plan, shorter each time", "green", size=16)

STORE_CUTOVER = dict(
    slug="store-cutover",
    kicker="a.k.a. “a cutover plan”",
    tldr="A migration plan says <b>what</b> moves; a <b>cutover plan</b> says <b>how the night goes</b>. It covers a shadow run that proves the new system first, <b>go / no-go criteria</b> decided at a set time by a named person, the switch in the <b>quietest hour</b> with steps and times, people on site for the first real work, and a <b>way back</b> kept open for a fixed period. Reuse the same plan for each site, and make it shorter each time.",
    chips=[("Family", "moving big things"), ("Lives in", "ops/cutovers/&lt;store&gt;.md, on the change calendar"), ("Pairs with", "rollback plans, the change calendar, Ana's strangler migration")],
    itil=dict(groups=["service", "technical"], chain=["design", "build", "deliver"], practices=["deployment management", "change enablement", "service validation and testing"],
              sre="(a progressive migration with a shadow phase)", principles=["Progress iteratively with feedback"],
              older="ITIL v3: transition planning and support, the cutover"),
    problem_side="Larder, March–April 2027",
    problem="""  <p class="lead">Ana's plan moves each store from StockPilot to <b>WMS B</b> through a router per store: Zuid on <b>19 April</b>, then Noord, Rotterdam and Utrecht, with StockPilot off by September. The architecture is clear. <span class="hl-pink">The night itself isn't written down</span>: who does what at 23:00 on a Sunday, how Tomás knows it worked at 06:00 on Monday, and what makes someone say “go back”.</p>
  <ul>
    <li>A migration that's clear on a diagram can still go wrong at 23:40.</li>
    <li>“Go” decided by mood, late at night, is a bad decision.</li>
    <li>The store opens at 07:00 whatever happens.</li>
  </ul>""",
    problem_figs=[co_problem],
    meanwhile=[("architect-4", "strangler-fig", "Ana's strangler migration: a router per store; shadow week (≤ 0.5 % difference), switch, two weeks of StockPilot read-only; Zuid 19 Apr, Noord 24 May, Rotterdam 21 Jun, Utrecht 26 Jul.",
                "Eli's cutover plan for each of those nights: go / no-go at 21:00, the switch at 23:15, people in the store at 06:00, a way back for two weeks.")],
    analogy_side="the railway's signalling weekend",
    analogy="""  <p>When a railway switches a line to new signalling, the new system runs <b>alongside the old for weeks</b>, silently, comparing. The switch night has a <b>timetable to the minute</b>, a named person decides <b>go or no-go at a set time</b>, the <b>first train carries engineers</b>, and the old system is kept ready to switch back until Wednesday.</p>""",
    analogy_figs=[co_analogy],
    map=[("Running side by side", "Shadow week: WMS B receives every change; difference checked daily"),
         ("Go / no-go at a set time", "Sunday 21:00, Eli with Tomás, four criteria"),
         ("The switch night timetable", "23:15 router switch, 23:40 test pick list"),
         ("Engineers on the first train", "Eli and Tomás in the store at 06:00"),
         ("Old system ready until Wednesday", "StockPilot read-only; router back until 2 May")],
    how_side="shadow, go / no-go, switch, first shift, way back",
    how="""  <p>Eli writes one cutover plan, used first for <b>Zuid</b>:</p>
  <ul>
    <li><b>T−7: shadow week.</b> WMS B gets every stock change, and the difference from StockPilot is checked daily. Zuid's is <b>0.3 %</b>, under the 0.5 % limit.</li>
    <li><b>Sunday 18 April, 21:00: go / no-go</b>, decided by Eli with Tomás against <b>four written criteria</b>: difference ≤ 0.5 %, the test pick list prints, on-call plus Eli and the store lead are available, and no SEV1 or SEV2 is open.</li>
    <li><b>23:15</b>, after the store closes: Zuid's router switches to WMS B. A test pick list prints at <b>23:40</b>.</li>
    <li><b>Monday 06:00</b>: Tomás and Eli are in the store for the first real picks.</li>
    <li><b>Way back until 2 May</b>: switch the router back. StockPilot stays read-only.</li>
  </ul>
  <p>The dates sit on the change calendar, clear of King's Day (26–28 April). <b>Noord</b>, on Monday <b>24 May</b>, uses the same plan. Its one surprise is the pick-list label format, fixed by <b>06:40</b>, and that becomes a criterion: “a real label prints”. Rotterdam (21 June) and Utrecht (26 July) follow, each plan a page shorter.</p>""",
    how_figs=[co_how],
    steps=[("Prove the new system in a shadow run", "Compare daily; set a limit."),
           ("Write go / no-go criteria in advance", "Checked at a set time by a named person."),
           ("Switch in the quietest hour", "Steps and times, written down."),
           ("Be there for the first real work", "On site, at opening time."),
           ("Keep a way back for a fixed period", "And say when it closes."),
           ("Reuse and shorten the plan", "Each site adds a criterion and removes a step.")],
    vocab=[("Cutover", "The moment work moves from the old system to the new."),
           ("Shadow run", "The new system runs alongside the old, without being used, to compare."),
           ("Go / no-go", "A decision at a set time, against written criteria."),
           ("Way back", "How to return to the old system, and until when."),
           ("Hypercare", "A period of close watching just after a cutover or launch."),
           ("Read-only", "The old system can be looked at but no longer changed.")],
    code=dict(file="ops/cutovers/zuid.md", note="used Sun 18 – Mon 19 April 2027 · reused for Noord 24 May", plain=True, src="""
# Zuid → WMS B · cutover plan

T−7  Mon 12 Apr   shadow: WMS B receives all stock changes · diff checked 09:00 daily
                  result 0.3 % (limit 0.5 %)
Sun 18 Apr 21:00  GO / NO-GO (Eli + Tomás)
                  [✓] diff ≤ 0.5 %   [✓] test pick list prints   [✓] a real label prints (added after Noord)
                  [✓] on-call, Eli, store lead available   [✓] no SEV1/2 open
           23:15  router zuid → WMS B (change feed) · StockPilot read-only for Zuid
           23:40  test pick list, 5 products, checked against the shelf
Mon 19 Apr 06:00  Tomás + Eli in store · first real picks · watch stock_sync_lag, pick errors
way back          router zuid → StockPilot · ≈ 5 min · until Sun 2 May 23:00
calendar          not in a window · not King's Day freeze (26–28 Apr)
"""),
    tools="tools: the router's per-store switch, a daily difference report, a one-page plan, and an alarm clock.",
    ladder=[("“we'll switch it on Sunday”", ["Decided by mood.", "No way back written."]),
            ("a cutover plan per site", ["Shadow, go / no-go, switch, first shift, way back.", "Reused and shortened."]),
            ("scripted cutover", ["Shadow comparison and switch by script.", "Go / no-go checks automatic."]),
            ("routine", ["Moving a site is a standard change.", "The plan is a recipe."])],
    ladder_now=1,
    baseline="Each line compares <b>a migration plan with no plan for the night</b> to <b>a cutover plan with shadow, go / no-go, people on site and a way back</b>.",
    ratings=[(2, 4, "Stores open normally on the Monday."),
             (2, 4, "Problems found in the shadow week."),
             (2, 4, "A way back in five minutes."),
             (2, 4, "Go decided against criteria, not mood."),
             (2, 4, "Everyone knows the night's timetable."),
             (3, 3, "Neutral."),
             (3, 3, "Neutral."),
             (2, 3, "A planned late night beats an unplanned one."),
             (3, 4, "One plan, reused four times.")],
    pitfalls=[("No shadow run", "The first real comparison is Monday's picks.", "compare for a week first."),
              ("Go / no-go by mood", "Tired people say go at midnight.", "written criteria, a set time, a name."),
              ("Nobody on site", "The store finds problems alone at 06:00.", "be there for the first shift."),
              ("A way back with no end", "Two systems run forever.", "say when the way back closes.")],
    use=["Moving a site, team or customer group to a new system.", "Any switch where the old and new can run side by side.", "When the business can't stop for the switch.", "Repeated migrations, store by store."],
    skip=["Changes behind a flag that can be turned off in seconds."],
    related=["<b>Strangler Fig Migration</b> (Ana, vol. 4)", "<b>How Do We Undo It?</b> (this volume)", "<b>Hypercare after Launch</b> (Grace, vol. 3)", "<b>A New City by Checklist</b> (next note)"],
    quiz=[("What does a cutover plan add to a migration plan?", "How the night goes: shadow run, go / no-go, the switch with times, people on site, a way back."),
          ("What were Zuid's go / no-go criteria?", "Difference ≤ 0.5 %, a test pick list prints, the right people available, no SEV1 or SEV2 open (and after Noord: a real label prints)."),
          ("Why switch at 23:15 on a Sunday?", "It's the quietest hour, after closing, with the whole night before the 07:00 opening."),
          ("What was Zuid's way back, and until when?", "Switch the router back to StockPilot (≈ 5 minutes), until Sunday 2 May 23:00."),
          ("What did Noord add to the plan?", "A criterion: a real label prints (the label format surprise).")],
    quiz_sit=[("At 21:00 on cutover night the shadow difference is 0.7 %. Everyone is ready and keen. What happens?", "No-go: the criterion is ≤ 0.5 %. Find the cause, fix it, and pick a new night from the calendar. Going on enthusiasm is exactly what the criteria exist to stop.")],
    try_it="For your next migration or big switch, write the night's plan on one page: shadow, go / no-go criteria and time, the switch steps, who's there for the first real work, and when the way back closes.",
    remember="Plan <span class=\"hl\">the night</span>, not just the architecture: shadow first, go / no-go <span class=\"hl\">by criteria at a set time</span>, people on site, a way back with an end date.",
    sources=["AXELOS, <i>ITIL 4: Deployment management</i> and <i>Change enablement</i> practice guides (2020).",
             "Martin Fowler, “StranglerFigApplication” (martinfowler.com, 2004, updated 2024).",
             "Betsy Beyer et al., <i>The Site Reliability Workbook</i> (2018): chapter on data migrations and launches."],
)

# ------------------------------------------------------------------ 11 A New City by Checklist
nc_problem = Doodle(760, 260, "Doodle of Utrecht in February 2027, eight weeks from lease to opening on 12 April. The store IT kit from May 2026 covers the store. But the city itself also has to be set up in the platform: delivery zones and slots, the store in the router, monitoring and the heartbeat, the catalogue and on-call, vendor settings, the status page. For Rotterdam that took Eli about three weeks of scattered work, written down nowhere.",
                    "The store has a kit. Setting up the city in the platform took three weeks of scattered work, written nowhere.")
nc_problem.box(14, 30, 300, 100, "store IT kit v1", "green", sub="34 items ✓", size=19, subsize=14)
nc_problem.box(346, 30, 400, 100, "the city in the platform", "pink", sub="zones · slots · router · monitoring · vendors", size=18, subsize=13)
nc_problem.note(380, 180, "Rotterdam: ≈ 3 weeks, in Eli's head", "red", size=19)
nc_problem.note(380, 216, "Utrecht: 8 weeks from lease to opening", "pen", size=17)

nc_analogy = Doodle(760, 220, "Doodle of a pilot's pre-flight checklist that has been flown thousands of times. It started long and handwritten; every flight crossed out a step that was never needed and added one that was missed. Today it's a short laminated card, in order, with nothing on it that hasn't earned its place.",
                    "A checklist that started long, and got shorter and better with every flight.")
nc_analogy.row([("v1", "61 steps, handwritten", "pink"), ("v2", "48 steps", "y"), ("v3", "39 steps, laminated", "green")], x=60, y=40, h=96, w=190, gap=50, size=20, subsize=14, arrows=True)
nc_analogy.note(380, 190, "every run adds what was missed and removes what wasn't needed", "pen", size=17)

nc_how = Doodle(760, 380, "Eli's city IT runbook, written for Utrecht in February 2027. Three parts. The store: the store IT kit, line ordered on 16 February (live 30 March). The platform: city configuration file with zones, slots and opening hours (city as configuration, Ana); the store in the WMS router; payment and address vendor settings; the status page. Operations: monitoring and heartbeat, the catalogue, on-call handover, store leads in the service desk, known errors shared. Version 1 had 61 steps; Utrecht opened on Monday 12 April. Version 2, after Utrecht, 48 steps (11 scripted). Version 3 for The Hague, opened 14 June on WMS B: 39 steps, IT ready in 9 working days.",
                "Store, platform, operations: one versioned runbook. 61 steps for Utrecht, 39 for The Hague.")
for i, (t, s, f) in enumerate([("store", "the IT kit · line 16 Feb → 30 Mar", "green"), ("platform", "city config · router · vendors · status page", "blue"), ("operations", "monitoring · catalogue · on-call · desk", "y")]):
    nc_how.box(14 + i * 248, 14, 236, 120, t, f, sub=s, size=20, subsize=12)
nc_how.row([("Utrecht v1", "61 steps · opened 12 Apr", "pink"), ("v2", "48 steps · 11 scripted", "y"), ("The Hague v3", "39 steps · 9 days · 14 Jun", "green")], x=14, y=170, h=96, gap=40, size=17, subsize=13, arrows=True)
nc_how.note(380, 310, "each launch: add what was missed, script what repeated, remove what wasn't needed", "pen", size=15)
nc_how.note(380, 346, "Utrecht week 1: 2.9 tickets per 100 orders (Rotterdam 7.1)", "green", size=16)

NEW_CITY = dict(
    slug="new-city-it",
    kicker="a.k.a. “a repeatable service transition”",
    tldr="Opening a new site is a <b>repeated service transition</b>: the same kinds of IT work every time, in the same order. Write it once as a <b>versioned runbook</b> in three parts (the site, the platform, operations) and run it for each launch. After every launch, add what was missed, <b>script what repeated</b> and remove what wasn't needed. The runbook should get <b>shorter</b> each time, and so should the launch.",
    chips=[("Family", "moving big things"), ("Lives in", "ops/cities/runbook.md (versioned), linked from the launch playbook"), ("Pairs with", "the store IT kit (vol. 1), the launch playbook, city as configuration")],
    itil=dict(groups=["service", "general"], chain=["design", "build", "deliver"], practices=["deployment management", "service configuration management", "knowledge management"],
              sre="(launch coordination checklists)", principles=["Progress iteratively with feedback", "Optimise and automate"],
              older="ITIL v3: service transition, transition planning and support"),
    problem_side="Larder, February 2027",
    problem="""  <p class="lead">Utrecht has <b>eight weeks</b> from lease (15 February) to opening on <b>12 April</b>. The store IT kit from May 2026 covers the store. But the city also has to be <b>set up in the platform</b>: delivery zones and slots, the store in the new WMS router, vendor settings, monitoring, the catalogue, on-call and the status page. <span class="hl-pink">For Rotterdam that was about three weeks of Eli's scattered work, written down nowhere.</span></p>
  <ul>
    <li>Steps are remembered, or forgotten, by one person.</li>
    <li>The order of work matters (the line, the router) and isn't recorded.</li>
    <li>Four more cities are planned for 2027.</li>
  </ul>""",
    problem_figs=[nc_problem],
    meanwhile=[("product-6", "launching-new-city", "Grace's city playbook for the product side: configuration vs local, a launch rhythm, five daily numbers; Utrecht's app work 6 days (Rotterdam 6 weeks).",
                "Eli's city IT runbook for the same launches: 61 steps for Utrecht, 39 for The Hague, IT ready in 9 working days.")],
    analogy_side="the pre-flight checklist",
    analogy="""  <p>A pilot's <b>pre-flight checklist</b> started long and handwritten. Every flight crossed out a step that was never needed and added one that had been missed. After thousands of flights it's a <b>short laminated card</b>, in order, with nothing on it that hasn't earned its place. Nobody flies from memory, however experienced they are.</p>""",
    analogy_figs=[nc_analogy],
    map=[("The handwritten first checklist", "City IT runbook v1, 61 steps"),
         ("Crossing out what wasn't needed", "Removing steps after each launch"),
         ("Adding what was missed", "Utrecht's missed step: store leads in the service desk"),
         ("The laminated card", "v3 for The Hague, 39 steps"),
         ("Nobody flies from memory", "Nobody opens a city from Eli's head")],
    how_side="one versioned runbook in three parts, shorter every launch",
    how="""  <p>Eli writes the <b>city IT runbook</b> in February, in three parts:</p>
  <ul>
    <li><b>The store</b>: the store IT kit. Utrecht's line is ordered on <b>16 February</b> and live on <b>30 March</b>.</li>
    <li><b>The platform</b>: the city configuration file (zones, slots, opening hours: Ana's city as configuration), the store in the WMS router, payment and address vendor settings, the status page.</li>
    <li><b>Operations</b>: monitoring and the store heartbeat, the catalogue, the on-call handover, store leads in the service desk, known errors shared with the new store.</li>
  </ul>
  <p>Version 1 has <b>61 steps</b>. Utrecht opens on Monday <b>12 April</b> with <b>2.9 tickets per 100 orders</b> in week 1 (Rotterdam: 7.1). After Utrecht, <b>v2</b> has 48 steps, 11 of them now scripts (zones from a file, monitoring and on-call from the catalogue). <b>v3</b>, for The Hague, has <b>39 steps</b>. The Hague opens on <b>14 June</b>, born on WMS B, with its IT ready in <b>9 working days</b>. The runbook is workstream 8 in Sanne's launch playbook.</p>""",
    how_figs=[nc_how],
    steps=[("Write everything the last launch needed", "From tickets, the issue log, the change feed."),
           ("Group it: site, platform, operations", "And order it by lead time."),
           ("Run it for the next launch", "Tick each step; note what was missed."),
           ("After the launch, change the runbook", "Add, script, remove; bump the version."),
           ("Script what repeated", "Config files over clicking."),
           ("Track how long IT takes per launch", "It should fall every time.")],
    vocab=[("Service transition", "Moving a new or changed service into live use."),
           ("Runbook (launch)", "The ordered steps to bring a new site or service live."),
           ("City as configuration", "A new city is mostly data in a file, not new code (Ana's principle)."),
           ("Versioned", "Numbered, with dated changes, so everyone uses the latest."),
           ("Early life support", "Close support just after go-live (vol. 6)."),
           ("Lead-time ordering", "Doing the slowest-to-arrive steps first.")],
    code=dict(file="ops/cities/runbook.md", note="v3 · for The Hague · June 2027", plain=True, src="""
# City IT runbook v3                         (v1 Utrecht 61 steps · v2 48 · v3 39)

store       store IT kit v2 (ops/store-it-kit.md) · line ordered day 1
platform    [ ] cities/the-hague.yml: zones, slots, hours      (script: check-city)
            [ ] store in WMS router (born on WMS B)              Eli
            [ ] PSP + address lookup: new city enabled           Cho, Ben
            [ ] status page component                            (script)
operations  [ ] monitoring + heartbeat from catalogue            (script: ops-onboard)
            [ ] catalogue, on-call handover, store leads in desk Eli
            [ ] known errors shared · poster + QR                Eli
tests       [ ] test order end to end · line failover · a real label prints

added after Utrecht   store leads in the service desk (missed!)
scripted              zones, monitoring, on-call, status page
IT ready in           Utrecht 21 working days · The Hague 9
"""),
    tools="tools: a versioned runbook in the repo, the city config file, a few scripts, and a retrospective after each launch.",
    ladder=[("from memory", ["Scattered work, one person.", "Steps forgotten."]),
            ("a versioned runbook", ["Three parts, ordered by lead time.", "Changed after each launch."]),
            ("mostly scripted", ["Config files and onboarding scripts.", "People do the judgement steps."]),
            ("a city is a pull request", ["Merging the city file sets up the platform and operations.", "People check, not click."])],
    ladder_now=2,
    baseline="Each line compares <b>Rotterdam's three weeks of scattered city set-up</b> to <b>a versioned, partly scripted city IT runbook</b>.",
    ratings=[(2, 4, "Utrecht week 1: 2.9 tickets per 100 (Rotterdam 7.1)."),
             (2, 4, "Every city set up the same way."),
             (3, 3, "Neutral."),
             (2, 3, "Fewer last-minute changes before opening."),
             (2, 4, "Progress visible step by step."),
             (2, 4, "11 steps scripted after Utrecht."),
             (3, 4, "IT ready in 9 days, not 21."),
             (2, 3, "Launches don't depend on Eli's memory."),
             (3, 4, "Gets lighter each time.")],
    pitfalls=[("A runbook that only grows", "Every launch adds steps, none are removed.", "remove what wasn't needed; script what repeated."),
              ("Not ordered by lead time", "The line arrives after opening, again.", "the slowest steps first."),
              ("Operations last, or forgotten", "The store opens before on-call knows it exists.", "operations is one of the three parts."),
              ("Nobody owns the runbook", "Changes after launch never happen.", "one owner: workstream 8.")],
    use=["You'll open similar sites, cities or customers again.", "A launch depended on one person's memory.", "Launches take longer than they should.", "Before a planned series (four cities in 2027)."],
    skip=["A one-off site you'll never repeat."],
    related=["<b>How Does a New Store Get Its IT?</b> (vol. 1)", "<b>Launching a New City</b> (Grace, vol. 6)", "<b>Can a Launch Be a Recipe?</b> (Sanne, vol. 6)", "<b>Cutting Over a Store</b> (this volume)"],
    quiz=[("What are the three parts of the city IT runbook?", "The store (the IT kit), the platform (config, router, vendors, status page), operations (monitoring, catalogue, on-call, desk)."),
          ("How did the runbook change from Utrecht to The Hague?", "61 steps → 48 (11 scripted) → 39; IT ready in 21 working days → 9."),
          ("What step was missed at Utrecht?", "Adding the store leads to the service desk."),
          ("Why order steps by lead time?", "The slowest things (the line) decide the earliest possible date."),
          ("What should happen to the runbook after each launch?", "Add what was missed, script what repeated, remove what wasn't needed, bump the version.")],
    quiz_sit=[("After The Hague, the team wants to add six new checks to the runbook. Nothing was removed. What do you ask?", "Which existing steps weren't needed this time, and which of the six can be a script instead of a step? A runbook that only grows stops being read.")],
    try_it="Take the last time you set up something new (a site, an office, a customer). Write the steps in three parts and order them by lead time. Mark which three could be scripted before the next one.",
    remember="Nobody should open a city <span class=\"hl\">from memory</span>. One versioned runbook, and every launch makes it <span class=\"hl\">shorter</span>.",
    sources=["AXELOS, <i>ITIL 4: Deployment management</i> and <i>Knowledge management</i> practice guides (2020).",
             "Betsy Beyer et al., <i>Site Reliability Engineering</i> (2016): chapter 27, reliable product launches at scale.",
             "Atul Gawande, <i>The Checklist Manifesto</i> (2009)."],
)

# ------------------------------------------------------------------ 12 Updating 120 Handhelds
dr_problem = Doodle(760, 260, "Doodle of Tuesday 16 February 2027. Since January Dee's team ships the picker app every week, as a product. Version 3.4 is pushed to every handheld at 23:30 on Monday, all stores at once. At 06:00 on Tuesday the barcode scanner doesn't work on Zuid's older model, bought in 2024: 31 devices. Pickers type product codes by hand for 40 minutes until 3.3 is pushed back.",
                    "One version to every handheld at once. Zuid's 31 older devices couldn't scan at 06:00.")
dr_problem.box(14, 30, 230, 100, "v3.4 → all", "pink", sub="Mon 23:30, every store", size=20, subsize=14)
dr_problem.arrow(250, 80, 290, 80)
dr_problem.box(296, 30, 220, 100, "06:00 Zuid", "pink", sub="31 older devices: no scan", size=19, subsize=13)
dr_problem.arrow(522, 80, 562, 80)
dr_problem.box(568, 30, 178, 100, "40 minutes", "y", sub="codes typed by hand", size=19, subsize=14)
dr_problem.note(380, 186, "a weekly product, pushed like a one-off", "red", size=19)

dr_analogy = Doodle(760, 220, "Doodle of a restaurant chain changing a recipe. First the head chef cooks it in the test kitchen, then one restaurant serves it for a night, then all restaurants. If guests at the first restaurant complain, the change stops there, and the old recipe is still in every kitchen's book.",
                    "Test kitchen, then one restaurant for a night, then all. If the first complains, it stops there.")
dr_analogy.row([("test kitchen", "the chef", "blue"), ("one restaurant", "one night", "y"), ("all restaurants", "next night", "green")], x=60, y=40, h=96, w=190, gap=50, size=18, subsize=14, arrows=True)
dr_analogy.note(380, 190, "the old recipe stays in the book", "pen", size=18)

dr_how = Doodle(760, 380, "Larder's device rollout rings from 22 February 2027. Ring 0: five test devices, one of each model, at Noord, given to Tomás's most experienced pickers, on the day of release. Ring 1: one whole store, overnight at 23:30. Ring 2: all other stores the next night at 23:30. Between rings: crash-free rate at least 99.5 percent, scan errors no higher than last week, and Tomás's go. Stop rule: any ring fails and the rollout halts; the previous version is kept on the device management server and pushed back in 10 minutes. The device list now has a 'model' column. In April ring 0 caught version 3.9 failing on the same older model; no store noticed.",
                "Ring 0: five devices, every model. Ring 1: one store. Ring 2: the rest. Stop if a ring fails; the old version is kept.")
dr_how.row([("ring 0", "5 devices · every model · Noord", "blue"), ("ring 1", "one store · 23:30", "y"), ("ring 2", "all stores · next night", "green")], y=14, h=110, gap=40, size=20, subsize=13, arrows=True)
dr_how.box(14, 150, 732, 100, None, "paper")
dr_how.text(380, 180, "between rings: crash-free ≥ 99.5 % · scan errors ≤ last week · store lead says go", size=14)
dr_how.text(380, 210, "stop: any ring fails → halt · previous version pushed back in 10 min", size=14)
dr_how.note(380, 290, "April: ring 0 caught v3.9 on the older model; no store noticed", "green", size=16)
dr_how.note(380, 330, "≈ 120 handhelds in 4 stores · two models · one rollout plan", "pen", size=16)

DEVICE_ROLLOUTS = dict(
    slug="device-rollouts",
    kicker="a.k.a. “staged rollouts to a fleet”",
    tldr="Pushing an app update to every device at once turns one bad version into a whole-company problem. Roll out in <b>rings</b>: a few test devices <b>covering every model</b>, then one site, then the rest. Leave time and a check between rings, do it <b>outside working hours</b>, keep the <b>previous version</b> ready to push back, and give the people at the first site a say in going on.",
    chips=[("Family", "moving big things"), ("Lives in", "the device management tool's rollout groups, ops/devices/rollouts.md"), ("Pairs with", "release vs deploy, known errors, the store IT kit")],
    itil=dict(groups=["service", "technical"], chain=["build", "deliver"], practices=["release management", "deployment management", "IT asset management"],
              sre="“canarying” for a device fleet", principles=["Progress iteratively with feedback"],
              older="ITIL v3: release and deployment management, pilot releases"),
    problem_side="Larder, Tuesday 16 February 2027",
    problem="""  <p class="lead">Since January Dee's team treats the picker app as a product and ships it <b>every week</b>. Version 3.4 is pushed to <b>every handheld at 23:30 on Monday</b>, all stores at once. At 06:00 on Tuesday the barcode scanner doesn't work on <b>Zuid's older model</b>, bought in 2024: <b>31 devices</b>. <span class="hl-pink">Pickers type product codes by hand for 40 minutes</span> until version 3.3 is pushed back.</p>
  <ul>
    <li>A weekly product is still being pushed like a one-off.</li>
    <li>Nobody had tested on the older model, because nobody knew which stores had it.</li>
    <li>The first test was every store's first shift.</li>
  </ul>""",
    problem_figs=[dr_problem],
    meanwhile=[("product-5", "operations-as-customer", "Grace's picker app as a product, from 18 January 2027: 20 % of Dee's team, Tomás as the stores' representative, weekly releases.",
                "Eli's rollout rings for those weekly releases: five devices of every model, one store, then the rest, with Tomás's go between rings.")],
    analogy_side="the chain's new recipe",
    analogy="""  <p>When a restaurant chain changes a recipe, the head chef cooks it first in the <b>test kitchen</b>, then <b>one restaurant</b> serves it for a night, then <b>all of them</b>. If guests at the first restaurant complain, the change stops there, and <b>the old recipe is still in every kitchen's book</b>.</p>""",
    analogy_figs=[dr_analogy],
    map=[("Test kitchen", "Ring 0: five devices, one of each model, at Noord"),
         ("One restaurant for a night", "Ring 1: one store, overnight"),
         ("All restaurants", "Ring 2: all other stores, the next night"),
         ("Guests complain, it stops", "A failed check halts the rollout"),
         ("The old recipe in the book", "The previous version kept, pushed back in 10 minutes")],
    how_side="rings, checks between them, and the old version kept",
    how="""  <p>From <b>22 February</b> every picker app release goes out in three rings through the device management tool:</p>
  <ul>
    <li><b>Ring 0</b>: <b>five test devices covering every model</b>, at Noord, in the hands of Tomás's most experienced pickers, on release day.</li>
    <li><b>Ring 1</b>: one whole store, overnight at <b>23:30</b>. The store rotates week by week.</li>
    <li><b>Ring 2</b>: all other stores, the next night at 23:30.</li>
  </ul>
  <p>Between rings there are three checks: crash-free rate <b>≥ 99.5 %</b>, scan errors no higher than last week, and the store lead's <b>go</b>. If a check fails, the rollout halts, and the <b>previous version</b>, always kept on the server, is pushed back in <b>10 minutes</b>. The asset list gets a <b>model</b> column, so “every model” is checkable. In April <b>ring 0 catches version 3.9</b> failing on the same older model. No store notices.</p>""",
    how_figs=[dr_how],
    steps=[("Know your fleet's models", "A model column in the asset list."),
           ("Ring 0: one device of every model", "Used by experienced people, on release day."),
           ("Ring 1: one site, outside working hours", "Rotate which site goes first."),
           ("Check between rings", "Crashes, errors, and the site's own go."),
           ("Keep the previous version ready", "Pushed back in minutes."),
           ("Halt on any failed check", "And note it as a known error if needed.")],
    vocab=[("Ring (deployment ring)", "A group of devices or users that gets a release at the same stage."),
           ("Staged rollout", "Releasing to growing groups, with checks between them."),
           ("Fleet", "All the devices of one kind you manage."),
           ("Crash-free rate", "Share of sessions without an app crash."),
           ("Halt", "Stopping a rollout part-way when a check fails."),
           ("Device model coverage", "Making sure each model is tested before wide release.")],
    code=dict(file="ops/devices/rollouts.md", note="picker app releases · from 22 February 2027", plain=True, src="""
# Picker app rollout (weekly)

ring 0  release day     5 devices at Noord: models HH-2024 ×2, HH-2026 ×3
                        experienced pickers · Tomás signs off by 16:00
ring 1  23:30 night 1   one store (rotates: Zuid, Rotterdam, Utrecht, Noord)
ring 2  23:30 night 2   all other stores
checks  crash-free ≥ 99.5 % · scan errors ≤ last week · store lead: go
halt    any check fails → stop · push previous version (kept on MDM) ≈ 10 min
        → known error if stores are affected

16 Feb  v3.4 to all at once → 31 HH-2024 at Zuid couldn't scan (40 min)
Apr     v3.9 failed on HH-2024 in ring 0 → halted → fixed in v3.9.1
"""),
    tools="tools: the device management tool's groups and scheduled pushes, the asset list with models, crash reporting in the app.",
    ladder=[("all devices at once", ["The first test is every store's morning.", "Rollback by hand."]),
            ("rings with checks", ["Every model in ring 0.", "Previous version kept."]),
            ("automatic progression", ["Rings advance when checks pass.", "Halt automatic."]),
            ("release without fear", ["Weekly releases nobody notices.", "Stores choose their own ring."])],
    ladder_now=1,
    baseline="Each line compares <b>pushing every version to every device at once</b> to <b>rings that cover every model, with checks and a kept previous version</b>.",
    ratings=[(2, 4, "Problems stay in ring 0; stores don't notice."),
             (2, 4, "Every model tested before it reaches a store."),
             (2, 4, "Old version back in 10 minutes."),
             (2, 4, "A bad version can't reach every store at once."),
             (2, 3, "Models and rollout status visible."),
             (3, 3, "Neutral."),
             (3, 3, "Neutral."),
             (2, 3, "No 06:00 surprises for on-call."),
             (3, 3, "Two extra nights per release.")],
    pitfalls=[("Ring 0 of one model", "The old model is the one that breaks.", "one of every model."),
              ("Rolling out in working hours", "Updates freeze devices mid-shift.", "overnight, at 23:30."),
              ("No way back", "The old version isn't kept.", "keep it on the server, test pushing it back."),
              ("Same first store every week", "One store always carries the risk.", "rotate ring 1.")],
    use=["You push updates to many devices.", "A release broke devices at one site.", "Your fleet has more than one model.", "Releases are frequent."],
    skip=["A handful of identical devices: test one, then update the rest."],
    related=["<b>Release or Deploy?</b> (this volume)", "<b>Operations as a Customer</b> (Grace, vol. 5)", "<b>Canary Releases</b> (cloud, vol. 6)", "<b>What Do We Own, and Where Is It?</b> (vol. 1)"],
    quiz=[("What went wrong on 16 February?", "v3.4 was pushed to every handheld at once; the scanner failed on Zuid's older model."),
          ("What is ring 0 at Larder?", "Five test devices covering every model, at Noord, used by experienced pickers on release day."),
          ("What checks happen between rings?", "Crash-free ≥ 99.5 %, scan errors no higher than last week, and the store lead's go."),
          ("What's the way back?", "The previous version, kept on the device management server, pushed back in about 10 minutes."),
          ("Why rotate the ring 1 store?", "So one store doesn't always carry the risk.")],
    quiz_sit=[("Ring 1 at Rotterdam looks fine on the numbers, but Yara says pickers find the new screen slower. Do you go on to ring 2?", "Not yet: the store lead's go is one of the checks. Talk to Dee's team; maybe it's a habit that settles, maybe a real slowdown. Measure picking time for a day before deciding.")],
    try_it="List your device fleet by model. For your next update, choose a ring 0 that covers every model, a ring 1 site and a time outside working hours. Where is the previous version kept, and how fast can you push it back?",
    remember="Never make <span class=\"hl\">every store's first shift</span> the test. Rings that cover <span class=\"hl\">every model</span>, checks between them, and the old version kept.",
    sources=["AXELOS, <i>ITIL 4: Release management</i> and <i>Deployment management</i> practice guides (2020).",
             "Betsy Beyer et al., <i>The Site Reliability Workbook</i> (2018): chapter 16, canarying releases.",
             "Microsoft, “Deployment rings” (Windows client deployment documentation)."],
)

NOTES = [STORE_CUTOVER, NEW_CITY, DEVICE_ROLLOUTS]
