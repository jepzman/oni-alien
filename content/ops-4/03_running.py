# Series 2 · Book 5 · The IT Operations Notebook · Vol. 4 · Running the year.
# Narrator: Eli (he/him). Facts: docs/larder-casebook.md, "Book 5, Vol. 4".

# ------------------------------------------------------------------ 11 The Vendor Went Quiet
vs_problem = Doodle(760, 260, "Doodle of Tuesday 31 August 2027. The billing vendor stops sending payment webhooks at 08:10. No errors anywhere: Larder's systems just receive nothing, so nothing alerts. In the portal Korenwolf's invoices show as unpaid. At 17:20 Ruben emails Mo asking why Larder says Korenwolf hasn't paid. Nine hours of silence, found by the client.",
                    "Nine hours of silence from the billing vendor. No errors, so no alerts. The client found it.")
vs_problem.box(14, 30, 230, 100, "08:10", "y", sub="webhooks stop", size=22, subsize=14)
vs_problem.box(264, 30, 230, 100, "no errors", "paper", sub="nothing to alert on", size=20, subsize=14)
vs_problem.box(514, 30, 232, 100, "17:20 Ruben", "pink", sub="“why do you say we haven't paid?”", size=19, subsize=12)
vs_problem.note(380, 186, "a failure that makes no noise", "red", size=19)

vs_analogy = Doodle(760, 220, "Doodle of a parent waiting for the school bus that always arrives at 15:40. Nobody calls to say it's late. The parent notices because it's 15:55 and the bus isn't there: the alarm is the absence. A good parent also has the bus company's number, and a note of how often the bus has been late this term.",
                    "Nobody phones when the bus is late. The alarm is that it's 15:55 and the bus isn't there.")
vs_analogy.icon("clock", 60, 50, 1.3)
vs_analogy.box(170, 40, 270, 100, "expected 15:40", "green", sub="every school day", size=18, subsize=14)
vs_analogy.box(470, 40, 276, 100, "15:55, no bus", "pink", sub="the absence is the alarm", size=18, subsize=14)
vs_analogy.note(450, 190, "watch for what should arrive, not only for errors", "pen", size=18)

vs_how = Doodle(760, 400, "Larder's vendor watch from September 2027. Absence alerts for every vendor that sends Larder something on a rhythm: billing webhooks (expected several an hour in business hours; none for 15 minutes is a ticket, none for 45 a page), the WMS B stock events, the settlement files by 05:00, the PSP's daily report. A poll every 15 minutes catches what webhooks miss. Every quarter, a 30-minute vendor review per critical vendor with its owner: incidents, how fast they answered, whether their status page was honest, contract and price changes, and how ready an exit would be. Scorecards for 8 vendors; the billing vendor got amber in Q3 and agreed to an outbound health check.",
                "Absence alerts for what should arrive, a 15-minute poll, and a quarterly scorecard per critical vendor.")
for i, (t, s) in enumerate([("billing webhooks", "none 15 min → ticket · 45 → page"), ("WMS B events", "none 5 min in hours"), ("settlement files", "by 05:00"), ("PSP report", "daily by 06:00")]):
    vs_how.box(14 + i * 186, 14, 172, 96, t, "y", sub=s, size=15, subsize=11)
vs_how.box(14, 130, 732, 56, "poll every 15 min: catches what webhooks miss", "blue", size=15)
vs_how.box(14, 206, 732, 110, None, "paper")
vs_how.head(380, 234, "quarterly scorecard per critical vendor (8)", size=16)
vs_how.text(380, 264, "incidents · response time · status page honesty", size=14)
vs_how.text(380, 290, "contract and price changes · exit readiness", size=14)
vs_how.note(380, 350, "Q3: billing vendor amber → agreed an outbound health check", "pen", size=16)

VENDOR_SILENCE = dict(
    slug="vendor-silence",
    kicker="a.k.a. “supplier management for silent failures”",
    tldr="Some vendor failures make <b>no noise</b>: the webhooks just stop, a file doesn't arrive, nothing errors. Alerting on errors never catches them. Watch for <b>absence</b>: what should arrive on a rhythm, and hasn't. Back webhooks up with a <b>poll</b>. And manage each critical vendor as an ongoing relationship: a <b>quarterly review with a scorecard</b> covering incidents, response, honesty, contract changes and how ready an exit would be.",
    chips=[("Family", "running the year"), ("Lives in", "absence alerts per vendor; ops/vendors/scorecards.md, quarterly"), ("Pairs with", "the vendor sheet (vol. 2), OLAs, Ana's vendor checklist")],
    itil=dict(groups=["general"], chain=["engage", "improve", "deliver"], practices=["supplier management", "monitoring and event management"],
              sre="(“absence of signal” alerting; dependencies' SLOs)", principles=["Think and work holistically"],
              older="ITIL v3: supplier management, supplier performance reviews"),
    problem_side="Larder, Tuesday 31 August 2027",
    problem="""  <p class="lead">At <b>08:10</b> the billing vendor stops sending payment webhooks. Nothing errors: Larder's systems simply receive nothing, so <b>nothing alerts</b>. In the portal Korenwolf's invoices start showing as <b>unpaid</b>. At <b>17:20</b> Ruben emails Mo: <i>“Why does Larder say we haven't paid?”</i> <span class="hl-pink">Nine hours of silence, found by the client</span>, two months before the renewal talks.</p>
  <ul>
    <li>Error alerts can't see a failure that makes no error.</li>
    <li>The vendor's status page said nothing all day.</li>
    <li>Nobody reviews vendors until something goes wrong.</li>
  </ul>""",
    problem_figs=[vs_problem],
    meanwhile=[("architect-4", "saas-integration", "Ana's vendor integration checklist of 6 September: poll every 15 minutes, silence alerts, stay below rate limits, production contract checks, status-page alerts.",
                "Eli's side: absence alerts for every vendor with a rhythm, and a quarterly scorecard per critical vendor.")],
    analogy_side="the school bus that doesn't come",
    analogy="""  <p>The school bus always arrives at <b>15:40</b>. When it's late, nobody phones. A parent notices because <b>it's 15:55 and the bus isn't there</b>: the alarm is the absence. A good parent also has the bus company's number, and a sense of <b>how often</b> the bus has been late this term, so they can complain with facts.</p>""",
    analogy_figs=[vs_analogy],
    map=[("The 15:40 bus", "Billing webhooks, several an hour in business hours"),
         ("15:55 and no bus", "No webhook for 15 minutes: a ticket"),
         ("Checking the timetable app", "A poll every 15 minutes"),
         ("The bus company's number", "The vendor sheet's emergency line"),
         ("How often it's been late this term", "The quarterly vendor scorecard")],
    how_side="watch for absence, poll as backup, review vendors quarterly",
    how="""  <p>After Ana's integration checklist (6 September), Eli adds the operations side:</p>
  <ul>
    <li><b>Absence alerts</b> for every vendor that sends something on a rhythm. Billing webhooks: none for <b>15 minutes</b> in business hours makes a ticket, none for <b>45</b> pages. WMS B stock events: none for 5 minutes in opening hours. Settlement files: by 05:00. The PSP's daily report: by 06:00.</li>
    <li>A <b>poll every 15 minutes</b> asks the vendor what changed, so a lost webhook is found even if the vendor thinks it sent it.</li>
    <li>A <b>quarterly vendor review</b>, 30 minutes per critical vendor with its owner, and a <b>scorecard</b>: incidents, how fast they answered, whether their status page was honest, contract and price changes, and how ready an exit would be.</li>
  </ul>
  <p>Eight vendors get scorecards. The billing vendor is <b>amber</b> in Q3, and at the review it agrees to an <b>outbound health check</b> that tells Larder when its own webhook queue backs up. Korenwolf is told what changed, in the four-part format, by Mo.</p>""",
    how_figs=[vs_how],
    steps=[("List what each vendor should send, and how often", "Webhooks, files, reports."),
           ("Alert on absence", "Nothing for N minutes in hours when something is expected."),
           ("Back push with a poll", "Ask what changed, every 15 minutes."),
           ("Keep a scorecard per critical vendor", "Incidents, response, honesty, contract, exit."),
           ("Review quarterly with the owner", "And bring the scorecard to renewals."),
           ("Tell affected clients what changed", "In their words.")],
    vocab=[("Silent failure", "A failure that produces no error, only missing results."),
           ("Absence alert", "An alert that fires when something expected doesn't arrive."),
           ("Heartbeat (vendor)", "A regular signal a vendor sends to show it's working."),
           ("Polling", "Asking a system for changes on a schedule, instead of waiting to be told."),
           ("Supplier scorecard", "A regular rating of a vendor on agreed criteria."),
           ("Exit readiness", "How easily you could move away from a vendor.")],
    code=dict(file="ops/vendors/scorecards.md", note="Q3 2027 · reviewed 4–8 October", plain=True, src="""
vendor          owner  incidents  answered in   status page   contract       exit ready   score
billing SaaS    Cho    1 (31 Aug, 9 h silence)  4 h   silent   renews Jun '28  medium      AMBER
                → agreed: outbound health check on their webhook queue (Nov)
WMS B           Eli    0          —             —             renewed '27    low          GREEN
PSP A           Cho    1 (slow, 22 min)  15 min honest        —              PSP B ready  GREEN
address lookup  Ben    0          —             none          monthly        high         GREEN
cloud           Eli    0          —             honest        —              low          GREEN
… 8 vendors

absence alerts   billing webhooks: none 15 min (business hours) → ticket · 45 → page
                 WMS B events: none 5 min (07–23) · settlement files by 05:00 · PSP report by 06:00
"""),
    tools="tools: the monitoring tool's “absent data” alerts, a small poller per vendor, and a scorecard table.",
    ladder=[("error alerts only", ["Silent failures found by clients.", "Vendors reviewed when angry."]),
            ("absence alerts and scorecards", ["Poll as backup.", "Quarterly reviews."]),
            ("vendors with SLOs", ["Each vendor's behaviour measured against an internal target.", "Scorecards automatic."]),
            ("built for vendor failure", ["Plan B automatic for each critical vendor.", "Exit always ready."])],
    ladder_now=1,
    baseline="Each line compares <b>error alerts and vendor reviews only after trouble</b> to <b>absence alerts, a poll and quarterly scorecards</b>.",
    ratings=[(2, 4, "Silent failures found in 15 minutes, not by the client."),
             (3, 3, "Neutral: the vendor is as reliable as it was."),
             (2, 4, "Detected in minutes."),
             (3, 3, "Neutral."),
             (2, 4, "Vendor behaviour visible every quarter."),
             (3, 3, "Neutral."),
             (2, 3, "Renewals argued with scorecards."),
             (3, 3, "Neutral."),
             (3, 3, "30 minutes per vendor a quarter.")],
    pitfalls=[("Alerting only on errors", "Silence looks like health.", "alert on absence."),
              ("Trusting push alone", "Lost webhooks are lost forever.", "poll as a backup."),
              ("Absence alerts at night", "Pages when nothing is expected.", "only in the hours something is expected."),
              ("Reviewing vendors only at renewal", "No facts, no leverage.", "quarterly scorecards.")],
    use=["A vendor failure was found by a customer.", "You depend on webhooks or files from vendors.", "A vendor contract renews in the next year.", "After setting OLAs that rely on vendors."],
    skip=["Vendors you call only on demand: error alerts catch their failures."],
    related=["<b>The Vendor Is Down at Peak</b> (vol. 2)", "<b>SaaS & Vendor Integration</b> (Ana, vol. 4)", "<b>What Do Teams Promise Each Other?</b> (this volume)", "<b>Event-Driven Integration</b> (Ana, vol. 4)"],
    quiz=[("Why didn't anything alert on 31 August?", "Nothing errored; the webhooks just stopped, and only errors were alerted on."),
          ("What is an absence alert?", "An alert that fires when something expected doesn't arrive in time."),
          ("Why poll as well as receive webhooks?", "A lost webhook is never retried; a poll finds what changed anyway."),
          ("What's on a vendor scorecard?", "Incidents, response time, status page honesty, contract and price changes, exit readiness."),
          ("What did the billing vendor agree to after scoring amber?", "An outbound health check on its webhook queue.")],
    quiz_sit=[("The settlement file hasn't arrived by 05:00 on a Sunday. Does anyone get paged?", "Not necessarily: if finance doesn't need it until Monday, a ticket is enough. The absence alert's urgency should match when the missing thing is needed.")],
    try_it="List every vendor that sends you something on a rhythm. For each, write how often it should arrive and what you'd do if it didn't. Add one absence alert for the one that matters most.",
    remember="The worst vendor failures <span class=\"hl\">make no noise</span>. Alert on what <span class=\"hl\">should have arrived</span>, poll as backup, and keep score quarterly.",
    sources=["AXELOS, <i>ITIL 4: Supplier management</i> practice guide (2020).",
             "Betsy Beyer et al., <i>Site Reliability Engineering</i> (2016): chapter 6, monitoring (black-box vs white-box).",
             "Michael T. Nygard, <i>Release It!</i> (2nd ed., 2018): integration points."],
)

# ------------------------------------------------------------------ 12 What Can the Stores Fix Themselves?
sl_problem = Doodle(760, 260, "Doodle of the store tickets in September 2027, across five stores: about 55 a week. A third of them are things a store lead could fix in two minutes with the right button or guide: restart a frozen handheld, reload a label printer, check whether the problem is only this store, swap a battery. They still wait for Sam's team or on-call, sometimes for an hour at the evening peak.",
                    "A third of store tickets could be fixed in two minutes by the store lead, with the right button or guide.")
sl_problem.box(14, 30, 230, 100, "≈ 55 a week", "paper", sub="5 stores", size=21, subsize=14)
sl_problem.box(264, 30, 482, 100, "≈ 1 in 3: two-minute fixes", "y", sub="restart · reload · “just us?” · battery", size=19, subsize=13)
sl_problem.note(380, 180, "…waiting for the desk, up to an hour at the peak", "red", size=18)

sl_analogy = Doodle(760, 220, "Doodle of a supermarket's self-checkout with a small help sign: 'item not recognised? press here and try again'. Most problems are solved by the customer in seconds. An assistant comes only for what the sign doesn't cover, and the sign is changed whenever the assistant sees the same question three times.",
                    "“Item not recognised? Press here.” The sign solves most problems; the assistant handles the rest, and updates the sign.")
sl_analogy.icon("screen", 60, 40, 1.4)
sl_analogy.box(170, 40, 270, 100, "the help sign", "green", sub="most problems, seconds", size=18, subsize=14)
sl_analogy.box(470, 40, 276, 100, "the assistant", "y", sub="the rest · updates the sign", size=18, subsize=14)
sl_analogy.note(450, 190, "move the fix to the person closest to the problem", "pen", size=18)

sl_how = Doodle(760, 380, "Larder's store self-service page, from 4 October 2027, on every store lead's phone. 'Is it just us?': the store's own status, other stores and Larder's status. Buttons, done through device management: restart a handheld, push the latest picker app, lock a lost device. 40-second video guides: reload the label printer, swap a handheld battery, check the Wi-Fi from the floor. Every action is logged and counts as a solved problem; if it doesn't help, one tap opens a ticket with the device and steps already filled in. Guides are added when the desk sees the same fix three times. December: 31 percent of store problems solved by the stores; tickets per store per week from 9.1 to 6.4.",
                "“Just us?”, three safe buttons, short videos, and one tap to a ticket with everything filled in.")
sl_how.box(14, 14, 236, 120, "just us?", "blue", sub="this store · others · Larder", size=20, subsize=12)
sl_how.box(262, 14, 236, 120, "safe buttons", "green", sub="restart · update · lock lost", size=20, subsize=12)
sl_how.box(510, 14, 236, 120, "40-second guides", "y", sub="printer · battery · Wi-Fi", size=18, subsize=12)
sl_how.box(14, 160, 732, 64, "didn't help? one tap → ticket with device + steps filled in", "paper", size=15)
sl_how.row([("Sep", "9.1 tickets / store / week", "pink"), ("Dec", "6.4 · 31 % solved in store", "green")], x=110, y=250, h=80, w=250, gap=40, size=17, subsize=13, arrows=True)
sl_how.note(380, 362, "a new guide whenever the desk sees the same fix three times", "pen", size=15)

SHIFT_LEFT = dict(
    slug="shift-left",
    kicker="a.k.a. “shift-left and self-service”",
    tldr="Many tickets are problems the reporter could fix themselves in two minutes, given <b>a safe button or a short guide</b>. Moving those fixes <b>closer to the person</b> (“shift-left”) is faster for them and frees the desk for the new and hard. Give the people at the edge a <b>“is it just us?”</b> check, a few <b>safe actions</b>, <b>very short guides</b>, and one tap to a ticket that's already filled in when it doesn't work.",
    chips=[("Family", "running the year"), ("Lives in", "the store self-service page on store leads' phones; ops/stores/guides/"), ("Pairs with", "known errors (vol. 2), service requests (vol. 1), the service desk")],
    itil=dict(groups=["service", "general"], chain=["engage", "deliver"], practices=["service desk", "service request management", "knowledge management"],
              sre="(reducing interrupts by self-service)", principles=["Optimise and automate", "Focus on value"],
              older="ITIL v3: self-help, the service desk's first-line fix rate"),
    problem_side="Larder, September 2027",
    problem="""  <p class="lead">With five stores, Larder gets about <b>55 store tickets a week</b>. Sam's team fixes many from the known-error list, but <b>about a third</b> are things a store lead could fix in two minutes with the right button or guide: restart a frozen handheld, reload a label printer, check whether a problem is <b>only this store</b>, swap a battery. <span class="hl-pink">They still wait for the desk or on-call, sometimes for an hour at the evening peak.</span></p>
  <ul>
    <li>Pickers stand idle while a two-minute fix waits in a queue.</li>
    <li>The desk spends its time on things it has solved a hundred times.</li>
    <li>Antwerp and Eindhoven are about to add more stores, and more tickets.</li>
  </ul>""",
    problem_figs=[sl_problem],
    analogy_side="the self-checkout's help sign",
    analogy="""  <p>A supermarket's self-checkout has a small sign: <b>“Item not recognised? Press here and try again.”</b> Most problems are solved by the customer in seconds. An <b>assistant</b> comes only for what the sign doesn't cover, and whenever the assistant answers the same question three times, <b>the sign is changed</b>.</p>""",
    analogy_figs=[sl_analogy],
    map=[("The help sign", "40-second guides on the store lead's phone"),
         ("Press here and try again", "Safe buttons: restart a handheld, push the app"),
         ("The assistant", "Sam's team and on-call"),
         ("Changing the sign", "A new guide when the desk sees the same fix three times"),
         ("Seconds, not minutes", "Two-minute fixes done in the store")],
    how_side="“just us?”, safe buttons, short guides, one tap to a ticket",
    how="""  <p>From <b>4 October</b> every store lead has a <b>self-service page</b> on their phone, linked from the store poster's QR code:</p>
  <ul>
    <li><b>Is it just us?</b> The store's own status (line, Wi-Fi, heartbeat), the other stores, and Larder's status page.</li>
    <li><b>Safe buttons</b>, through device management: restart a handheld, push the latest picker app, lock a lost device. Nothing that can break anything for anyone else.</li>
    <li><b>40-second video guides</b> in Dutch and French: reload the label printer, swap a handheld battery, check the Wi-Fi from the floor.</li>
    <li>If it doesn't help, <b>one tap opens a ticket</b> with the device, the store and the steps already tried filled in.</li>
  </ul>
  <p>Every action is logged and counts as a solved problem. A new guide is added whenever the desk sees <b>the same fix three times</b>. By <b>December</b>, <b>31 %</b> of store problems are solved in the store, and tickets per store per week drop from <b>9.1 to 6.4</b>, even with Antwerp and Eindhoven added.</p>""",
    how_figs=[sl_how],
    steps=[("Sort tickets by “could they have fixed it?”", "With the right button or guide."),
           ("Add an “is it just us?” check", "Most panic is about the wrong scope."),
           ("Offer only safe actions", "Nothing that can affect anyone else."),
           ("Make guides very short", "40 seconds, in their language, on a phone."),
           ("One tap to a prefilled ticket", "When self-service doesn't work."),
           ("Add a guide after three repeats", "And count self-solved problems.")],
    vocab=[("Shift-left", "Moving the fix closer to the person with the problem."),
           ("Self-service", "Users solving their own problems or requests with provided tools."),
           ("Safe action", "An action a user can take without risk to others."),
           ("Deflection", "A problem solved without a ticket."),
           ("Prefilled ticket", "A ticket opened with context already captured."),
           ("First-contact resolution", "Solved at the first attempt, wherever that is.")],
    code=dict(file="ops/stores/self-service.md", note="from 4 October 2027 · store leads' phones", plain=True, src="""
# Store self-service (store leads)

just us?    store line · Wi-Fi · heartbeat · other stores · status page
buttons     restart handheld <no.> · push latest picker app · lock lost device
            (via MDM, logged, affects only this store's devices)
guides      label printer: reload the roll (40 s, nl/fr)
            handheld battery swap (35 s) · Wi-Fi check from the floor (45 s)
didn't help → one tap: ticket with store, device, steps tried, screenshot
new guide   when the desk sees the same fix 3 times (owner: Sam's team)

Sep 2027: 9.1 tickets / store / week   Dec 2027: 6.4 · 31 % of problems solved in store
"""),
    tools="tools: the device management tool's self-service actions, a simple page per store, phone videos, and the helpdesk's ticket link with fields.",
    ladder=[("everything via the desk", ["Two-minute fixes wait an hour.", "Desk swamped by repeats."]),
            ("self-service for the common", ["“Just us?”, safe buttons, short guides.", "Prefilled tickets."]),
            ("guided diagnosis", ["The page suggests the fix from the symptom.", "Known errors linked."]),
            ("problems fixed before noticed", ["Devices heal themselves.", "Stores see only the result."])],
    ladder_now=1,
    baseline="Each line compares <b>every store problem going through the desk</b> to <b>a self-service page with “just us?”, safe buttons and short guides</b>.",
    ratings=[(2, 4, "Pickers back to work in minutes."),
             (3, 3, "Neutral."),
             (2, 4, "Two-minute fixes take two minutes."),
             (3, 3, "Neutral: only safe actions."),
             (2, 4, "Stores see their own status."),
             (2, 4, "31 % of problems never reach the desk."),
             (3, 3, "Neutral."),
             (2, 4, "Fewer evening calls to on-call."),
             (3, 3, "A page and a few videos.")],
    pitfalls=[("Unsafe buttons", "A store restarts something shared.", "only actions that affect this store."),
              ("Long guides", "Nobody reads a PDF during the peak.", "40-second videos."),
              ("Dead end", "Self-service fails and there's no way forward.", "one tap to a prefilled ticket."),
              ("Guides that go stale", "Steps for last year's printer.", "owned by the desk, updated on repeats.")],
    use=["Many tickets are simple, repeated fixes.", "People wait for help with things they could do.", "The desk is swamped by repeats.", "New sites are being added."],
    skip=["Problems that need access or judgement the reporter shouldn't have."],
    related=["<b>We Know the Bug, Now What?</b> (vol. 2)", "<b>Who Fixes What?</b> (vol. 2)", "<b>Can I Have a New Handheld?</b> (vol. 1)", "<b>Self-Service for Business Customers</b> (Grace, vol. 6)"],
    quiz=[("What does shift-left mean?", "Moving fixes closer to the person with the problem."),
          ("What's on the store self-service page?", "“Is it just us?”, safe buttons (restart, update, lock), 40-second guides, and one tap to a prefilled ticket."),
          ("What makes an action safe for self-service?", "It can only affect this store's own devices, not anything shared."),
          ("When is a new guide added?", "When the desk sees the same fix three times."),
          ("What changed by December?", "31 % of store problems solved in store; tickets per store per week 9.1 → 6.4.")],
    quiz_sit=[("A store lead asks for a button to restart the WMS B connection “because it fixes things”. Do you add it?", "No: it's shared by every store. Find why it needs restarting (a problem), and give the store “is it just us?” so they can see it's being handled.")],
    try_it="Take last month's tickets and mark those the reporter could have fixed in two minutes with a safe button or a short guide. Build the guide for the most common one, as a 40-second video.",
    remember="Put the fix <span class=\"hl\">next to the problem</span>: “just us?”, safe buttons, 40-second guides, and <span class=\"hl\">one tap to a ticket</span> when it isn't enough.",
    sources=["AXELOS, <i>ITIL 4: Service desk</i> and <i>Knowledge management</i> practice guides (2020).",
             "Consortium for Service Innovation, <i>KCS v6 Practices Guide</i> (2016): self-service.",
             "Betsy Beyer et al., <i>Site Reliability Engineering</i> (2016): chapter 29, dealing with interrupts."],
)

# ------------------------------------------------------------------ 13 Operating in a Second Country
sc_problem = Doodle(760, 260, "Doodle of Eli's first look at Antwerp in June 2027, when the store's keys arrive on 1 June. The store IT kit and city runbook assume the Netherlands: a Dutch internet provider with a six-week lead time, Dutch posters, the Dutch holiday calendar, iDEAL. In Belgium the line takes eight weeks to arrive, half the staff and customers speak French, the public holidays differ, Bancontact replaces iDEAL, and the store laptop's keyboard layout is AZERTY.",
                    "Every Dutch assumption in the kit, checked against Belgium: line, language, holidays, payments, even the keyboard.")
for i, (t, nl, be) in enumerate([("line", "6 weeks", "8 weeks"), ("language", "nl", "nl + fr"), ("holidays", "NL", "BE"), ("payments", "iDEAL", "Bancontact"), ("keyboard", "QWERTY", "AZERTY")]):
    sc_problem.box(14 + i * 148, 30, 136, 120, t, "y", sub=f"{nl} → {be}", size=17, subsize=12)
sc_problem.note(380, 200, "the kit was written for one country without anyone noticing", "red", size=17)

sc_analogy = Doodle(760, 220, "Doodle of a family moving abroad with their car. Same car, but: a different side of the road in some countries, different emergency number, different rules for winter tyres, a different plug for the charger. They make a list before they go, not at the first roundabout.",
                    "Same car, new country: emergency number, winter tyres, the charger plug. Make the list before the first roundabout.")
sc_analogy.icon("chassis", 50, 60, 1.2)
sc_analogy.row([("emergency no.", None, "y"), ("winter tyres", None, "y"), ("charger plug", None, "y")], x=170, y=50, h=70, w=180, gap=12, size=16)
sc_analogy.note(450, 170, "the list before the trip, not at the roundabout", "pen", size=18)

sc_how = Doodle(760, 400, "Eli's 'second country' sheet for Antwerp, written on Monday 5 July 2027 with Inès, Cho, Lena and Sam. Line ordered on 2 June from a Belgian provider (8 weeks), live 2 August, 4G backup on a Belgian SIM. Language: posters, guides, status page and desk replies in Dutch and French; the service desk gets two French-speaking agents' hours. Calendar: Belgian public holidays (21 July, 15 August, 1 and 11 November) added to the change calendar and on-call notes. Payments: Bancontact through the payment provider, Cho, live in July. Devices: AZERTY on the store laptop, French on handhelds by choice. Escalation: Inès joins the store leads' escalation list. Opened Monday 18 October; week one 2.4 tickets per 100 orders.",
                "One sheet of differences, written months before opening. Antwerp opened 18 October with 2.4 tickets per 100 orders.")
rows = [("line", "BE provider · ordered 2 Jun · live 2 Aug · BE SIM backup"), ("language", "nl + fr: posters, guides, status page, desk"),
        ("calendar", "BE holidays: 21 Jul · 15 Aug · 1 + 11 Nov"), ("payments", "Bancontact via PSP (Cho), July"),
        ("devices", "AZERTY laptop · handhelds in fr by choice"), ("people", "Inès on the escalation list")]
for i, (k, v) in enumerate(rows):
    y = 14 + i * 50
    sc_how.box(14, y, 150, 42, k, "blue", size=15)
    sc_how.box(174, y, 572, 42, v, "paper", size=13)
sc_how.note(380, 340, "Antwerp opened Mon 18 Oct · week 1: 2.4 tickets per 100 orders", "green", size=16)
sc_how.note(380, 376, "the sheet becomes part of the city runbook: “country differences”", "pen", size=15)

SECOND_COUNTRY = dict(
    slug="second-country",
    kicker="a.k.a. “operating across borders”",
    tldr="A new country quietly breaks assumptions built into every kit and runbook: <b>line lead times, languages, public holidays, payment methods, local vendors, laws, even keyboard layouts</b>. Before opening, write a <b>“second country” sheet</b> with the people who know the place, listing each difference and what changes. Put holidays in the change calendar, speak the users' language at the desk, and make the sheet part of the runbook for the next country.",
    chips=[("Family", "running the year"), ("Lives in", "ops/countries/be.md, linked from the city runbook"), ("Pairs with", "the city runbook (vol. 3), the store IT kit, the service desk")],
    itil=dict(groups=["service", "general"], chain=["plan", "design", "deliver"], practices=["service design", "service desk", "supplier management"],
              sre="(regional launches; launch checklists)", principles=["Think and work holistically", "Start where you are"],
              older="ITIL v3: service design, the service desk's language and hours"),
    problem_side="Larder, June 2027",
    problem="""  <p class="lead">Antwerp's keys arrive on <b>1 June</b>, and Eli looks at the store IT kit and the city runbook with Belgium in mind. Both <b>quietly assume the Netherlands</b>: a Dutch provider with a six-week lead time, Dutch posters, the Dutch holiday calendar, iDEAL. In Belgium the line takes <b>eight weeks</b>, half the staff and customers speak <b>French</b>, the <b>public holidays differ</b>, <b>Bancontact</b> replaces iDEAL, and the store laptop's keyboard is <b>AZERTY</b>. <span class="hl-pink">The kit was written for one country without anyone noticing.</span></p>
  <ul>
    <li>Hidden assumptions surface one at a time, after opening.</li>
    <li>French-speaking pickers can't use Dutch-only guides.</li>
    <li>A change could land on a Belgian holiday nobody marked.</li>
  </ul>""",
    problem_figs=[sc_problem],
    meanwhile=[("project-5", "stakeholders-abroad", "Sanne's “different country, different rules”: the permit, food-safety registration, VAT, Bancontact, staff documents in Dutch, courier contracts, alcohol ages.",
                "Eli's IT version of the same list: line lead time, two languages at the desk, Belgian holidays in the change calendar, Bancontact, AZERTY.")],
    analogy_side="driving the family car abroad",
    analogy="""  <p>A family moving abroad takes the same car, but a lot changes: the <b>emergency number</b>, the rules for <b>winter tyres</b>, the <b>plug for the charger</b>, in some countries the side of the road. They make <b>a list before they go</b>, with a friend who lives there, not at the first roundabout.</p>""",
    analogy_figs=[sc_analogy],
    map=[("Same car", "Same platform, kit and runbook"),
         ("A friend who lives there", "Inès, Lena with Maarten, Cho"),
         ("The emergency number", "Escalation: Inès on the list; the desk in French"),
         ("Winter tyre rules", "Belgian holidays in the change calendar"),
         ("The charger plug", "Bancontact; AZERTY; a Belgian SIM for backup")],
    how_side="one sheet of differences, written early with people who know",
    how="""  <p>On <b>Monday 5 July</b> Eli writes the <b>second-country sheet</b> with Inès (Antwerp's store manager), Cho, Lena and Sam:</p>
  <ul>
    <li><b>Line</b>: a Belgian provider, ordered <b>2 June</b> (8 weeks), live <b>2 August</b>; 4G backup on a Belgian SIM.</li>
    <li><b>Language</b>: posters, guides, the status page and desk replies in <b>Dutch and French</b>; Sam's team adds French-speaking agents' hours.</li>
    <li><b>Calendar</b>: Belgian public holidays (<b>21 July, 15 August, 1 and 11 November</b>, and the rest) go into the change calendar and the on-call notes.</li>
    <li><b>Payments</b>: Bancontact through the payment provider, Cho, live in July.</li>
    <li><b>Devices</b>: an AZERTY keyboard on the store laptop; handhelds in French for pickers who choose it.</li>
    <li><b>People</b>: Inès joins the store leads' escalation list.</li>
  </ul>
  <p>Antwerp opens on <b>Monday 18 October</b>, later than planned because of the permit, so the IT is ready with weeks to spare. Week one has <b>2.4 tickets per 100 orders</b>. The sheet becomes the <b>“country differences”</b> section of the city runbook, ready for the next country.</p>""",
    how_figs=[sc_how],
    steps=[("Re-read every kit and runbook for the new country", "Mark every assumption."),
           ("Write the sheet with people who know the place", "The local manager, legal, payments."),
           ("Check lead times locally", "Lines and vendors differ by country."),
           ("Serve users in their language", "Posters, guides, status page, desk."),
           ("Add local holidays to the change calendar", "And to on-call notes."),
           ("Fold the sheet into the runbook", "For the next country.")],
    vocab=[("Localisation", "Adapting a service to a country's language, rules and habits."),
           ("Country differences", "The list of what changes between countries."),
           ("Local vendor", "A supplier you need only in the new country (an ISP)."),
           ("Public holiday calendar", "Days that change store traffic and staffing."),
           ("AZERTY", "The keyboard layout used in Belgium and France."),
           ("Bancontact", "Belgium's most used debit card payment method.")],
    code=dict(file="ops/countries/be.md", note="Mon 5 July 2027 · Eli, Inès, Cho, Lena, Sam", plain=True, src="""
# Belgium · what changes for IT                              first store: Antwerp

line        Belgian ISP, 8 weeks (ordered 2 Jun → live 2 Aug) · 4G backup: BE SIM
language    nl + fr: posters, 40-s guides, status page, desk replies (Sam: fr hours)
calendar    BE public holidays in ops/changes/calendar.md + on-call notes
            (21 Jul · 15 Aug · 1 Nov · 11 Nov · Easter Monday · Whit Monday …)
payments    Bancontact via PSP (Cho) · live Jul 2027
devices     store laptop AZERTY · handhelds nl or fr by picker's choice
people      Inès (store manager) on the store leads' escalation list
legal       data stays in the EU region · staff docs in Dutch (Joost, Lena)
opened      Mon 18 Oct 2027 · week 1: 2.4 tickets / 100 orders (Utrecht 2.9)
"""),
    tools="tools: the kit and runbook, an afternoon with the local manager and legal, and translated guides.",
    ladder=[("assume it's the same", ["Differences found after opening.", "One-language guides."]),
            ("a country sheet before opening", ["Written with people who know.", "Holidays in the calendar."]),
            ("country as configuration", ["Language, holidays, payments set per country in config.", "Kits generated per country."]),
            ("multi-country by design", ["New countries change data, not process.", "Desk and docs multilingual by default."])],
    ladder_now=1,
    baseline="Each line compares <b>a Dutch kit used in Belgium</b> to <b>a second-country sheet written months before opening</b>.",
    ratings=[(2, 4, "French-speaking staff and customers served in French."),
             (3, 3, "Neutral."),
             (3, 3, "Neutral."),
             (2, 3, "No changes land on Belgian holidays by accident."),
             (2, 4, "Every difference on one page."),
             (3, 3, "Neutral."),
             (3, 3, "Neutral."),
             (3, 3, "Neutral."),
             (3, 3, "An afternoon, months ahead.")],
    pitfalls=[("Assuming it's the same", "Differences found one by one after opening.", "re-read every kit for the new country."),
              ("Writing it alone", "You don't know what you don't know.", "with the local manager, legal, payments."),
              ("One language", "Half the store can't use the guides.", "both languages, from day one."),
              ("Forgetting the calendar", "A change on a national holiday.", "holidays in the change calendar.")],
    use=["Opening in a new country or region.", "Serving users in a new language.", "Adding a local vendor.", "Before writing kits you'll reuse abroad."],
    skip=["A new city in the same country: the city runbook covers it."],
    related=["<b>Different Country, Different Rules</b> (Sanne, vol. 5)", "<b>Localisation for a New Country</b> (Grace, vol. 6)", "<b>A New City by Checklist</b> (vol. 3)", "<b>When Must We Not Change Anything?</b> (vol. 3)"],
    quiz=[("Which Dutch assumptions broke in Belgium?", "Line lead time, language, holidays, payment method (iDEAL vs Bancontact), keyboard layout."),
          ("Who wrote the sheet with Eli?", "Inès, Cho, Lena and Sam."),
          ("Why add Belgian holidays to the change calendar?", "Traffic and staffing change on them; a change mustn't land on one by accident."),
          ("How did the language difference change the desk?", "Replies, guides, posters and the status page in Dutch and French, with French-speaking agents' hours."),
          ("What happens to the sheet after Antwerp?", "It becomes the “country differences” section of the city runbook.")],
    quiz_sit=[("Larder considers a first city in Germany. What do you do first?", "Re-read the kit, city runbook and Belgian sheet for German assumptions, then write a German sheet with someone who knows the place: line lead times, language, holidays, payments, local vendors, law.")],
    try_it="Take one of your runbooks or checklists and read it as if you were opening in another country. List every assumption that would change. Who would you need in the room to complete the list?",
    remember="A kit written in one country <span class=\"hl\">assumes that country</span>. Write the differences down <span class=\"hl\">before opening</span>, with people who know the place.",
    sources=["AXELOS, <i>ITIL 4: Service design</i> and <i>Service desk</i> practice guides (2020).",
             "Betsy Beyer et al., <i>Site Reliability Engineering</i> (2016): chapter 27, launch checklists.",
             "Erin Meyer, <i>The Culture Map</i> (2014)."],
)

# ------------------------------------------------------------------ 14 Switching a System Off
dc_problem = Doodle(760, 260, "Doodle of July 2027. Ana's application portfolio review on 19 July marks four applications to eliminate (a survey tool, a second chat tool, an old cron server, a legacy reporting database, together about 2,300 euros a month) and StockPilot to switch off on 15 September when the warehouse move is done. Larder has never switched a system off on purpose. The last attempt, an old reporting job in 2026, was turned off on a Friday and turned back on on Monday because finance's month-end report broke.",
                    "Five systems to switch off. The last time Larder tried, finance's month-end broke and it was switched back on.")
for i, t in enumerate(["StockPilot", "survey tool", "2nd chat tool", "old cron", "legacy reporting DB"]):
    dc_problem.box(14 + i * 148, 30, 136, 90, t, "y", size=14)
dc_problem.note(380, 160, "≈ €84k a year (StockPilot) + ≈ €2.3k a month (the other four)", "pen", size=16)
dc_problem.note(380, 200, "2026: switched off Friday, back on Monday: finance's month-end broke", "red", size=16)

dc_analogy = Doodle(760, 220, "Doodle of moving out of a flat. You don't just stop paying the rent. You redirect the post, read the meters, take photos, cancel the internet, keep the contract papers, return the keys, and tell the people who still send letters there. Miss one and something arrives at an address you no longer have.",
                    "Moving out: redirect the post, read the meters, keep the papers, cancel, return the keys.")
dc_analogy.icon("door", 60, 40, 1.4)
dc_analogy.row([("redirect post", None, "y"), ("read meters", None, "y"), ("keep papers", None, "y"), ("return keys", None, "y")], x=150, y=50, h=70, w=140, gap=12, size=15)
dc_analogy.note(450, 170, "miss one and a letter goes to an empty flat", "pen", size=18)

dc_how = Doodle(760, 400, "Larder's decommissioning checklist, used for StockPilot in September 2027. Find users: 30 days of access logs, not just the people you know about; StockPilot's showed a finance spreadsheet pulling stock history every Monday. Announce: four weeks' notice with a date. Read-only: two weeks where nothing can change but everything can be read; anyone who needs something shouts now. Keep the data the law and finance need: three years of stock movements exported and archived, with Lena's retention date. Remove: API keys, network rules, monitoring, runbooks, catalogue, asset register entries. Cancel the contract. Delete. StockPilot switched off 15 September; bridge contract ended 30 September; the four smaller systems and three 2026 Dispatch leftovers gone by 30 September.",
                "Users from logs, notice, read-only, keep what's required, remove every trace, cancel, delete, and update the catalogue.")
steps = [("find users", "30 days of logs"), ("announce", "4 weeks' notice"), ("read-only", "2 weeks"), ("keep data", "export + retention date"),
         ("remove traces", "keys · rules · alerts · runbooks"), ("cancel + delete", "and update the catalogue")]
for i, (t, s) in enumerate(steps):
    r, c = divmod(i, 3)
    dc_how.box(14 + c * 248, 14 + r * 100, 236, 86, t, "green" if i < 3 else "y", sub=s, size=18, subsize=13)
dc_how.box(14, 222, 732, 64, "found by the logs: finance's spreadsheet pulling stock history every Monday", "pink", size=15)
dc_how.note(380, 322, "StockPilot off 15 Sep · contract ended 30 Sep · 4 apps + 3 Dispatch leftovers gone by 30 Sep", "green", size=14)
dc_how.note(380, 358, "≈ €84k a year + ≈ €2.3k a month saved", "pen", size=16)

DECOMMISSIONING = dict(
    slug="decommissioning",
    kicker="a.k.a. “retiring a service”",
    tldr="Switching a system off is a change, and often a risky one: someone you didn't know about is still using it. Retire systems <b>on purpose</b>. <b>Find users from the logs</b>, not from memory. <b>Announce</b> a date. Go <b>read-only</b> for a while so anyone still depending on it shouts. <b>Keep the data</b> the law and finance need. <b>Remove every trace</b> (keys, rules, alerts, runbooks). <b>Cancel</b> the contract, delete, and update the catalogue.",
    chips=[("Family", "running the year"), ("Lives in", "ops/decommission/checklist.md; the catalogue and asset register"), ("Pairs with", "the catalogue (vol. 1), the store cutover (vol. 3), Ana's application portfolio")],
    itil=dict(groups=["service", "general"], chain=["design", "plan"], practices=["service catalogue management", "IT asset management", "change enablement"],
              sre="(“turndown”; removing a service safely)", principles=["Keep it simple and practical", "Think and work holistically"],
              older="ITIL v3: service retirement (the retired services part of the portfolio)"),
    problem_side="Larder, July 2027",
    problem="""  <p class="lead">Ana's application portfolio review on <b>19 July</b> marks four applications to eliminate: a survey tool, a second chat tool, an old cron server and a legacy reporting database, together about <b>€2,300 a month</b>. <b>StockPilot</b> is to be switched off on <b>15 September</b>, once the warehouse move is done. Larder has never switched a system off on purpose. <span class="hl-pink">The last attempt, an old reporting job in 2026, was turned off on a Friday and back on on Monday</span>, because finance's month-end report broke.</p>
  <ul>
    <li>Nobody knows everyone who uses a system.</li>
    <li>Data that must be kept can disappear with the system.</li>
    <li>Credentials, rules and alerts for dead systems linger for years.</li>
  </ul>""",
    problem_figs=[dc_problem],
    meanwhile=[("architect-4", "application-portfolio", "Ana's application portfolio of 19 July: 23 applications, ≈ €61k a month; eliminate four (≈ €2.3k a month), migrate StockPilot and Mo's spreadsheet CRM.",
                "Eli's checklist for actually switching them off: users from the logs, read-only first, data kept, every trace removed.")],
    analogy_side="moving out of a flat",
    analogy="""  <p>Moving out of a flat isn't just stopping the rent. You <b>redirect the post</b>, <b>read the meters</b>, <b>keep the contract papers</b>, cancel the internet, return the keys, and tell the people who still send letters there. Miss one, and something important arrives at an address you no longer have.</p>""",
    analogy_figs=[dc_analogy],
    map=[("Who still sends you post", "Who still uses the system: from the logs"),
         ("Redirecting the post", "Pointing users and integrations elsewhere"),
         ("Keeping the contract papers", "Archiving data with a retention date"),
         ("Returning the keys", "Removing API keys, network rules, accounts"),
         ("Cancelling the internet", "Cancelling the vendor contract")],
    how_side="users from logs, notice, read-only, keep, remove, cancel, delete",
    how="""  <p>Eli writes a <b>decommissioning checklist</b> and uses it first on StockPilot:</p>
  <ol>
    <li><b>Find users from the logs</b>: 30 days of access logs, not just the users people know about. StockPilot's logs show a <b>finance spreadsheet pulling stock history every Monday</b>. Marco's team moves it to the data team's export in August.</li>
    <li><b>Announce</b> with four weeks' notice and a date.</li>
    <li><b>Read-only</b> for two weeks: nothing can change, everything can still be read. Anyone who needs something shouts now.</li>
    <li><b>Keep the data</b> the law and finance need: three years of stock movements exported and archived, with Lena's retention date on it.</li>
    <li><b>Remove every trace</b>: API keys, network rules, monitoring and alerts, runbooks, catalogue and asset-register entries.</li>
    <li><b>Cancel</b> the contract, then <b>delete</b>.</li>
  </ol>
  <p>StockPilot is switched off on <b>15 September</b>, and the bridge contract ends on <b>30 September</b> (about <b>€84k a year</b>). The four smaller systems, and three 2026 Dispatch leftovers that Ana's sweep found (a courier cron fallback, a Core database view and a nightly copy job), are gone by <b>30 September</b>. Nothing has to be switched back on.</p>""",
    how_figs=[dc_how],
    steps=[("Find users from logs", "30 days, every caller, not just the known."),
           ("Announce a date", "Four weeks' notice is common."),
           ("Go read-only first", "Dependents shout while you can still help."),
           ("Keep what must be kept", "Export, archive, retention date (legal)."),
           ("Remove every trace", "Keys, rules, alerts, runbooks, catalogue, assets."),
           ("Cancel, delete, and record it", "The catalogue says it's retired, and when.")],
    vocab=[("Decommissioning", "Retiring a system or service on purpose."),
           ("Hidden dependency", "A user or system relying on something nobody knew about."),
           ("Read-only period", "A time when a system can be read but not changed, before switching off."),
           ("Retention", "How long data must be kept, by law or policy."),
           ("Orphaned credential", "An API key or account for a system that no longer exists."),
           ("Retired service", "A service listed as gone, with its date, in the catalogue.")],
    code=dict(file="ops/decommission/stockpilot.md", note="switched off 15 September 2027", plain=True, src="""
# Decommission · StockPilot                                  owner: Eli

users (logs, 30 days)   Core sync (moved to WMS B) · finance spreadsheet (Mondays!)
                        → finance moved to data team export, 23 Aug
announce                16 Aug: "read-only 1 Sep, off 15 Sep"
read-only               1–15 Sep · 0 complaints
keep                    stock movements 2024–2027 → archive bucket, retention to 2034 (Lena)
remove                  API keys ×3 · network rules ×2 · 4 alerts · RB-09/10 retired
                        catalogue: "retired 15 Sep 2027" · assets: SAAS-04 closed
cancel                  bridge contract ends 30 Sep (Marco) · deleted 1 Oct
same checklist          survey tool · 2nd chat tool · old cron · legacy reporting DB
                        + 3 Dispatch leftovers (Ana's sweep) · all by 30 Sep
"""),
    tools="tools: access logs, a read-only switch (or permissions), an archive bucket with a retention date, and the catalogue.",
    ladder=[("switch off and hope", ["Users found by breaking them.", "Traces left behind."]),
            ("a decommissioning checklist", ["Logs, notice, read-only, keep, remove, cancel.", "Catalogue updated."]),
            ("retirement planned at launch", ["Every new service records its users and data from day one.", "Retirement is cheap."]),
            ("regular pruning", ["Unused services flagged automatically.", "Retired yearly as routine."])],
    ladder_now=1,
    baseline="Each line compares <b>switching off and finding out</b> to <b>a decommissioning checklist with users from logs and a read-only period</b>.",
    ratings=[(2, 4, "Finance's Monday report kept working."),
             (3, 3, "Neutral."),
             (3, 3, "Neutral."),
             (2, 4, "A switch-off that didn't need undoing."),
             (2, 4, "The catalogue says what's gone, and when."),
             (2, 3, "Fewer systems to patch and watch."),
             (1, 4, "≈ €84k a year + ≈ €2.3k a month."),
             (2, 3, "Fewer alerts from things nobody uses."),
             (3, 3, "A few weeks of calendar, little effort.")],
    pitfalls=[("Users from memory", "The spreadsheet nobody mentioned.", "read 30 days of logs."),
              ("Deleting data with the system", "Records the law requires are gone.", "export and archive with a retention date."),
              ("Leaving traces", "Keys and network rules for a dead system.", "remove every trace, then check."),
              ("No read-only period", "Dependents find out by breaking.", "read-only first.")],
    use=["A system is being replaced.", "A portfolio review marks systems to eliminate.", "A contract is ending.", "You find a system nobody can explain."],
    skip=["Truly unused test resources with no data: delete them (but check the logs)."],
    related=["<b>Application Portfolio (TIME)</b> (Ana, vol. 4)", "<b>What Do We Run, and Who Owns It?</b> (vol. 1)", "<b>Cutting Over a Store</b> (vol. 3)", "<b>Transition Architectures</b> (Ana, vol. 4)"],
    quiz=[("Why find users from logs, not memory?", "Hidden users exist; StockPilot's logs found a finance spreadsheet nobody had mentioned."),
          ("What's the read-only period for?", "Anyone still depending on the system finds out and shouts while it can still be read."),
          ("What data did Larder keep from StockPilot?", "Three years of stock movements, archived with Lena's retention date."),
          ("What traces must be removed?", "API keys, network rules, monitoring and alerts, runbooks, catalogue and asset entries."),
          ("What was saved?", "About €84k a year for StockPilot and about €2.3k a month for the four smaller systems.")],
    quiz_sit=[("During the read-only period, someone in marketing says the survey tool holds three years of customer feedback they still use. What do you do?", "Pause the switch-off date if needed, export what they need to where they can use it (with Lena on personal data and retention), then continue. That's exactly what the read-only period is for.")],
    try_it="Pick one system nobody seems to use. Read 30 days of its access logs. Who still calls it? Write the checklist for switching it off, including what data must be kept and for how long.",
    remember="Switching off is <span class=\"hl\">a change</span>. Find users <span class=\"hl\">from the logs</span>, go read-only first, keep what the law needs, and remove every trace.",
    sources=["AXELOS, <i>ITIL 4: Service catalogue management</i> and <i>IT asset management</i> practice guides (2020).",
             "Betsy Beyer et al., <i>The Site Reliability Workbook</i> (2018): chapter on turndowns and migrations.",
             "Gartner, “TIME” model for application portfolio rationalisation (background, via Ana's note)."],
)

# ------------------------------------------------------------------ 15 Running a Peak
pk_problem = Doodle(760, 260, "Doodle of Eli's memory of December 2026: the database resized in a hurry on the 16th, the failover on the 18th, 38 minutes, about 900 orders lost or late, Femke calling three times. For December 2027 the forecast is about 27,000 orders a day across seven stores and two countries. Capacity changes are done and the freeze starts on 13 December, but nobody has written down what 'ready for Christmas' means.",
                    "Last Christmas: a hurried resize and 38 minutes down. This one: 27,000 orders a day, and no definition of “ready”.")
pk_problem.box(14, 30, 350, 100, "Dec 2026", "pink", sub="resize 16th · failover 18th · 38 min", size=20, subsize=13)
pk_problem.box(396, 30, 350, 100, "Dec 2027", "y", sub="≈ 27,000 orders a day · 7 stores · 2 countries", size=20, subsize=12)
pk_problem.note(380, 180, "“are we ready?” · “I think so”", "red", size=19)

pk_analogy = Doodle(760, 220, "Doodle of a theatre's opening night. A week before: a full dress rehearsal, the understudies told which nights they're on standby, the fire exits checked, the box office briefed. On the night: a short call at the half hour, everyone in place, and nothing new added to the show.",
                    "A dress rehearsal, understudies on standby, a call at the half hour, and nothing new added on the night.")
pk_analogy.icon("curtain", 60, 40, 1.3)
pk_analogy.row([("dress rehearsal", "a week before", "blue"), ("understudies", "on standby", "y"), ("half-hour call", "every night", "green"), ("nothing new", "in the show", "pink")], x=160, y=40, h=96, w=140, gap=10, size=15, subsize=12)
pk_analogy.note(450, 190, "ready is a checklist, not a feeling", "pen", size=18)

pk_how = Doodle(760, 400, "Larder's Christmas 2027 readiness. Readiness review on Monday 29 November: twelve checks, each with an owner and a green, amber or red: capacity changes done and the 5-times load test passed; database failover tested on 7 December (1 minute 37); major-incident drill on 30 November; PSP switch to the backup provider tested; vendor contacts confirmed for the holidays; store spares and batteries; the change freeze from 13 December to 3 January; extra cover: from 17 to 24 December, Eli or Bram on standby every evening behind the normal primary and secondary; a 15-minute check-in at 09:00 every day from 13 to 24 December with Joost's operations lead, Sam and Mo. Result: on Friday 17 December at 18:12 PSP A slowed down for 22 minutes; the automatic switch moved payments to PSP B in 40 seconds; no failed orders. Busiest day Thursday 23 December, about 29,400 orders; no SEV1 or SEV2 all month.",
                "Twelve checks on 29 November, a freeze, extra cover, a daily 09:00 check-in. 17 Dec: PSP switched in 40 s, no failed orders.")
checks = ["capacity + 5× test", "failover 7 Dec: 1:37", "major-incident drill", "PSP switch tested", "vendors' holiday lines", "store spares + batteries"]
for i, t in enumerate(checks):
    r, c = divmod(i, 3)
    pk_how.box(14 + c * 248, 14 + r * 62, 236, 52, t, "green", size=14)
pk_how.box(14, 146, 360, 64, "freeze 13 Dec – 3 Jan", "pink", size=16)
pk_how.box(386, 146, 360, 64, "Eli / Bram standby 17–24 Dec", "y", size=15)
pk_how.box(14, 226, 732, 56, "09:00 daily check-in 13–24 Dec · 15 min · ops lead, Sam, Mo, on-call", "blue", size=14)
pk_how.box(14, 296, 732, 56, "Fri 17 Dec 18:12 · PSP A slow 22 min · switched to PSP B in 40 s · 0 failed orders", "green", size=14)
pk_how.note(380, 384, "busiest day Thu 23 Dec ≈ 29,400 orders · no SEV1 or SEV2 all December", "pen", size=15)

RUNNING_A_PEAK = dict(
    slug="running-a-peak",
    kicker="a.k.a. “peak readiness”",
    tldr="The busiest weeks of the year deserve their own preparation, written down: a <b>readiness review</b> weeks before (capacity, failover, drills, vendors, spares, each green, amber or red with an owner), a <b>freeze</b>, <b>extra on-call cover</b> at the riskiest hours, and a <b>short daily check-in</b> with the people running the business. On the day, nothing new goes in. Ready is <b>a checklist, not a feeling</b>.",
    chips=[("Family", "running the year"), ("Lives in", "ops/peaks/christmas-2027.md; the change calendar"), ("Pairs with", "capacity headroom, the change calendar (vol. 3), major incidents (vol. 2)")],
    itil=dict(groups=["service", "general"], chain=["plan", "deliver"], practices=["capacity and performance management", "service continuity management", "incident management"],
              sre="(launch and event readiness reviews; “production readiness”)", principles=["Think and work holistically", "Collaborate and promote visibility"],
              older="ITIL v3: capacity management (business capacity), IT service continuity"),
    pager=dict(when="Fri 17 Dec 2027 · Ben on call · Eli on standby", lines=[
        ("18:12", "<b>ALERT</b> PSP A latency p95 4.1 s (3 s timeout)"),
        ("18:12", "circuit breaker opens · payments routed to PSP B (automatic)"),
        ("18:12", "checkout_errors 0.2 % · orders_per_5min normal"),
        ("18:14", "Ben ack · SEV3 · PSP A status page: “degraded”"),
        ("18:34", "PSP A recovers · traffic returns gradually"),
        ("18:40", "0 failed orders · noted for the 09:00 check-in")]),
    problem_side="Larder, November 2027",
    problem="""  <p class="lead">Eli remembers December 2026 well: the database resized in a hurry on the 16th, the failover on the 18th, <b>38 minutes</b>, about <b>900 orders</b>, Femke calling three times. For December 2027 the forecast is about <b>27,000 orders a day</b> across seven stores and two countries. The capacity changes are done and the freeze starts on <b>13 December</b>. <span class="hl-pink">But when Femke asks “are we ready?”, the honest answer is “I think so”.</span></p>
  <ul>
    <li>Readiness lives in several people's heads.</li>
    <li>The riskiest hours have the same cover as any other week.</li>
    <li>Operations, support and IT watch the peak separately.</li>
  </ul>""",
    problem_figs=[pk_problem],
    meanwhile=[("architect-5", "failure-mode-analysis", "Ana's failure mode analysis of 6 December: top risk “PSP slow” (RPN 216) → 3 s timeout, circuit breaker, automatic switch to PSP B.",
                "Eli's peak night: on 17 December at 18:12 PSP A slowed for 22 minutes, and that switch moved payments in 40 seconds with no failed orders.")],
    analogy_side="the theatre's opening night",
    analogy="""  <p>A week before opening night a theatre holds <b>a full dress rehearsal</b>, tells the <b>understudies</b> which nights they're on standby, checks the fire exits and briefs the box office. Every night there's <b>a short call at the half hour</b>. And on opening night, <b>nothing new is added to the show</b>. Ready is something you can tick off, not a feeling.</p>""",
    analogy_figs=[pk_analogy],
    map=[("The dress rehearsal", "Load test at 5×, failover test, major-incident drill"),
         ("Understudies on standby", "Eli or Bram on standby every evening, 17–24 Dec"),
         ("Fire exits checked", "PSP switch tested; vendors' holiday lines confirmed"),
         ("The half-hour call", "09:00 daily check-in, 13–24 December"),
         ("Nothing new in the show", "The freeze, 13 December – 3 January")],
    how_side="a readiness review, a freeze, extra cover, a daily check-in",
    how="""  <p>On <b>Monday 29 November</b> Eli runs a <b>readiness review</b>: twelve checks, each with an owner and a green, amber or red. Among them:</p>
  <ul>
    <li>Capacity changes done, and the <b>5× load test</b> passed on 15 November.</li>
    <li><b>Database failover</b> tested on <b>7 December</b>, before the freeze: <b>1:37</b>.</li>
    <li>A <b>major-incident drill</b> held on <b>30 November</b>.</li>
    <li>The automatic switch to the backup payment provider tested, and every critical vendor's holiday contact confirmed.</li>
    <li>Store spares and spare batteries in every store.</li>
  </ul>
  <p>Then the run itself. The <b>freeze</b> runs from <b>13 December to 3 January</b>. From <b>17 to 24 December</b>, <b>Eli or Bram is on standby every evening</b> behind the usual primary and secondary. There's a <b>15-minute check-in at 09:00</b> every day from 13 to 24 December, with Joost's operations lead, Sam, Mo and on-call.</p>
  <p>On <b>Friday 17 December at 18:12</b>, PSP A slows down for 22 minutes. The circuit breaker from Ana's failure analysis moves payments to <b>PSP B in 40 seconds</b>, and <b>no orders fail</b>. The busiest day is Thursday <b>23 December</b>, with about <b>29,400 orders</b>. There's <b>no SEV1 or SEV2</b> all month.</p>""",
    how_figs=[pk_how],
    steps=[("Write what “ready” means", "A dozen checks, each with an owner."),
           ("Review it weeks before", "Green, amber, red, with time to fix amber."),
           ("Rehearse the worst case", "Load test, failover, a major-incident drill."),
           ("Freeze, and add cover at the riskiest hours", "Standby behind the usual rota."),
           ("Hold a short daily check-in", "IT, operations, support, client managers."),
           ("Review afterwards", "What to keep for next year's checklist.")],
    vocab=[("Peak", "A period of much higher demand than normal."),
           ("Readiness review", "A structured check that a service is prepared for an event."),
           ("Standby", "An extra person ready to join, beyond the normal rota."),
           ("Daily check-in", "A short, fixed meeting during the peak to share status."),
           ("Circuit breaker", "Stops calling a failing dependency and switches to a fallback."),
           ("Peak review", "A look back after the peak to improve the next one.")],
    code=dict(file="ops/peaks/christmas-2027.md", note="readiness review Mon 29 November 2027", plain=True, src="""
check                                   owner     status
capacity changes + 5× load test         Bram      ✓ green (15 Nov, p95 640 ms)
DB failover test before the freeze      Eli       ✓ green (7 Dec, 1:37)
major-incident drill                    Eli, Ana  ✓ green (30 Nov)
PSP A → B automatic switch tested       Cho       ✓ green
vendors' holiday contacts               owners    ✓ green (8 of 8)
store spares + batteries                leads     amber → green (6 Dec)
freeze 13 Dec – 3 Jan                   pipeline  ✓
standby 17–24 Dec evenings              Eli/Bram  ✓
09:00 check-in 13–24 Dec                Eli       ✓ (ops lead, Sam, Mo, on-call)
… 12 checks

result  17 Dec 18:12 PSP A slow 22 min → PSP B in 40 s · 0 failed orders
        busiest day Thu 23 Dec ≈ 29,400 orders · SEV1 0 · SEV2 0 · SEV3 6
"""),
    tools="tools: a readiness checklist, the load test, the failover test, a drill, a standby rota and a 15-minute daily slot.",
    ladder=[("“I think we're ready”", ["Readiness in heads.", "Normal cover at peak."]),
            ("a readiness review and a run plan", ["Checks with owners.", "Freeze, standby, daily check-in."]),
            ("rehearsed every year", ["Checklist improved after each peak.", "Drills routine."]),
            ("peaks are ordinary", ["Capacity and failover automatic.", "The peak needs no special cover."])],
    ladder_now=1,
    baseline="Each line compares <b>“I think we're ready”</b> to <b>a readiness review, a freeze, standby cover and a daily check-in</b>.",
    ratings=[(2, 4, "No failed orders when a provider slowed at the peak."),
             (2, 4, "No SEV1 or SEV2 in December."),
             (2, 4, "The PSP switch took 40 seconds."),
             (2, 4, "Nothing new during the freeze."),
             (2, 4, "One checklist answers “are we ready?”"),
             (3, 3, "Neutral."),
             (3, 3, "Standby costs a few evenings."),
             (2, 3, "Extra cover means no one carries the peak alone."),
             (3, 3, "A review and 15 minutes a day for two weeks.")],
    pitfalls=[("Ready as a feeling", "“I think so.”", "a written checklist with owners."),
              ("Testing during the freeze", "The test itself becomes a change at the peak.", "test before the freeze."),
              ("IT watching alone", "Operations and support see problems first.", "a shared daily check-in."),
              ("No review afterwards", "Next year starts from scratch.", "keep what worked in the checklist.")],
    use=["A known peak is coming: Christmas, King's Day, a campaign.", "Last peak went badly.", "Several teams need to watch the same weeks.", "Leaders ask “are we ready?”"],
    skip=["Normal weeks: the usual rota and alerts are enough."],
    related=["<b>Will Christmas Fit?</b> (this volume)", "<b>When Must We Not Change Anything?</b> (vol. 3)", "<b>When Is It a Major Incident?</b> (vol. 2)", "<b>Failure Mode Analysis</b> (Ana, vol. 5)"],
    quiz=[("What does Larder's readiness review contain?", "About twelve checks with owners and status: capacity and load test, failover test, drill, PSP switch, vendors' holiday lines, store spares, freeze, standby, check-in."),
          ("Why test failover on 7 December?", "Before the freeze starts on 13 December, so the test isn't a change at the peak."),
          ("What's the daily check-in?", "15 minutes at 09:00, 13–24 December, with operations, support, client managers and on-call."),
          ("What happened on 17 December 2027?", "PSP A slowed for 22 minutes; payments switched to PSP B in 40 seconds; no orders failed."),
          ("What extra cover was added?", "Eli or Bram on standby every evening from 17 to 24 December.")],
    quiz_sit=[("On 1 December the store spares check is amber: two stores have no spare batteries. What happens?", "It gets an owner and a date before the freeze (here: the store leads, by 6 December), and goes green at the next check-in. Amber two weeks ahead is exactly what the review is for.")],
    try_it="Pick your next peak. Write twelve checks for “ready”, each with an owner. Review them four weeks before. Which one is amber today?",
    remember="Ready is <span class=\"hl\">a checklist, not a feeling</span>: review it weeks before, freeze, add cover, and <span class=\"hl\">check in daily</span> with the people running the business.",
    sources=["Betsy Beyer et al., <i>Site Reliability Engineering</i> (2016): chapter 27, reliable product launches at scale.",
             "AXELOS, <i>ITIL 4: Capacity and performance management</i> and <i>Service continuity management</i> practice guides (2020).",
             "Michael T. Nygard, <i>Release It!</i> (2nd ed., 2018): circuit breakers and steady state."],
)

NOTES = [VENDOR_SILENCE, SHIFT_LEFT, SECOND_COUNTRY, DECOMMISSIONING, RUNNING_A_PEAK]
