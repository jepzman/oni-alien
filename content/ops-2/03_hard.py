# Series 2 · Book 5 · The IT Operations Notebook · Vol. 2 · The hard ones.
# Narrator: Eli (he/him). Facts: docs/larder-casebook.md, "Book 5, Vol. 2".

# ------------------------------------------------------------------ 12 Was It a Change?
ch_problem = Doodle(760, 260, "Doodle of Thursday 29 October 2026, 18:10. A network rule tidy-up Eli had written in the afternoon is applied by the pipeline at 18:10 and cuts Dispatch off from the database. Bram, on call and three weeks into the job, checks Dispatch, then the database, then the containers. Nobody asks what changed. Eli is on a train. After 25 minutes Bram finds the rule in the pipeline's history. Couriers are assigned by hand for most of that time.",
                    "25 minutes checking everything except the one question: what changed?")
ch_problem.row([("Dispatch?", "looks fine", "paper"), ("database?", "looks fine", "paper"), ("containers?", "look fine", "paper")], x=14, y=30, h=84, w=220, gap=36, size=17, subsize=14, arrows=True)
ch_problem.box(110, 150, 540, 60, "18:10 network rule tidy-up · applied by the pipeline", "pink", stroke="red", size=16)
ch_problem.note(380, 240, "found at 18:35 · couriers assigned by hand", "red", size=18)

ch_analogy = Doodle(760, 220, "Doodle of a car that starts making a noise right after a garage visit. A good mechanic's first question isn't 'what could it be?' but 'what did we touch last?' Most new noises come from the last thing someone changed.",
                    "A new noise after the garage? The first question is “what did we touch last?”")
ch_analogy.icon("chassis", 60, 60, 1.3)
ch_analogy.box(190, 40, 260, 100, "“what could it be?”", "paper", sub="a hundred things", size=18, subsize=14)
ch_analogy.box(486, 40, 260, 100, "“what did we touch?”", "green", sub="usually the answer", size=18, subsize=14)
ch_analogy.note(450, 190, "most incidents follow a change", "pen", size=18)

ch_how = Doodle(760, 380, "Larder's change feed, live from 30 October 2026 (action A-19, planned since July). Every deploy, infrastructure change, network rule change, feature flag change and vendor change posts one line into the incident channel: time, what, who, and how to undo it. The first question in every incident, from the runbook template: what changed in the last two hours? On 29 October, with the feed, the rule would have been on screen at 18:11. In November, 4 of 9 incidents followed a change; in each, the change was found in under 2 minutes.",
                "Every change posts one line: time, what, who, how to undo. The first question in every incident: what changed?")
ch_how.box(14, 14, 732, 160, None, "paper")
for i, t in enumerate(["18:02 deploy  core v412          Ben     undo: deploy v411",
                       "18:10 network rule tidy-up      Eli     undo: revert PR 233",
                       "18:12 flag    low_stock_switch  auto    undo: flag off",
                       "18:20 vendor  PSP A maintenance  PSP     undo: backup route"]):
    ch_how.text(30, 50 + i * 34, t, anchor="start", size=15)
ch_how.box(14, 196, 732, 60, "first question in every incident: what changed in the last 2 hours?", "y", size=16)
ch_how.row([("Nov", "4 of 9 incidents followed a change", "pink"), ("found in", "< 2 min each time", "green")], x=110, y=280, h=76, w=250, gap=40, size=18, subsize=14)

CHANGE_INCIDENTS = dict(
    slug="change-related-incidents",
    kicker="a.k.a. “what changed?”",
    tldr="Many incidents start with <b>a change</b>: a deploy, a config edit, a network rule, a feature flag, a vendor's maintenance. So the first question in every incident is <b>“what changed in the last two hours?”</b>, and to answer it in a minute you need every change in <b>one visible feed</b>, with time, what, who and <b>how to undo it</b>. Undoing the change often restores service faster than diagnosing the system.",
    chips=[("Family", "the hard ones"), ("Lives in", "a change feed in #incident; the first line of every runbook"), ("Pairs with", "change enablement (vol. 3), incident roles, the dependency map")],
    itil=dict(groups=["service"], chain=["deliver", "improve"], practices=["incident management", "change enablement"],
              sre="“roughly 70 % of outages are due to changes in a live system”", principles=["Collaborate and promote visibility"],
              older="ITIL v3: change management, the forward schedule of change"),
    pager=dict(when="Thu 29 Oct 2026 · Bram on call (week 4)", lines=[
        ("18:10", "pipeline applies network-rules PR 233 (tidy-up, Eli)"),
        ("18:12", "<b>PAGE</b> dispatch_delay 140 s · all cities"),
        ("18:14", "Bram ack · Dispatch logs: cannot reach database"),
        ("18:20", "database healthy · containers healthy · Eli on a train, no signal"),
        ("18:27", "stores: couriers assigned by hand"),
        ("18:35", "Bram finds PR 233 in the pipeline history · reverts it"),
        ("18:37", "Dispatch reconnects · backlog cleared by 18:50")]),
    problem_side="Larder, Thursday 29 October 2026",
    problem="""  <p class="lead">At 18:10 the pipeline applies a <b>network rule tidy-up</b> that Eli wrote and had approved that afternoon. It removes a rule Dispatch needs to reach the database. Bram, three weeks into the job and on call, checks Dispatch, then the database, then the containers, and all of them look healthy. Eli is on a train with no signal. <span class="hl-pink">Nobody asks what changed.</span> At 18:35 Bram finds the change in the pipeline's history and reverts it. Couriers are assigned by hand for most of those 25 minutes.</p>
  <ul>
    <li>Changes are scattered: pipeline history, chat, the cloud console.</li>
    <li>“What changed?” isn't the first question in any runbook.</li>
    <li>The change feed has been an open action since July (A-19).</li>
  </ul>""",
    problem_figs=[ch_problem],
    meanwhile=[("architect-3", "deployment-diagrams", "Ana's deployment diagram, drawn after the same incident: what runs where, which network, how Dispatch reaches Postgres, on one page for on-call.",
                "Eli's side of 29 October: the change feed and the first question in every runbook, “what changed in the last two hours?”")],
    analogy_side="the noise after the garage visit",
    analogy="""  <p>Your car starts making a new noise <b>the day after a garage visit</b>. A good mechanic doesn't start with “what could it be?”, because there are a hundred possibilities. The first question is <b>“what did we touch last?”</b>. Most new noises come from the last thing someone changed, and putting that back is usually faster than understanding the whole engine.</p>""",
    analogy_figs=[ch_analogy],
    map=[("The garage visit", "A deploy, a config edit, a network rule change"),
         ("“What could it be?”", "Checking Dispatch, the database, the containers"),
         ("“What did we touch last?”", "The change feed: the last two hours"),
         ("Putting the part back", "Reverting PR 233"),
         ("The garage's job sheet", "One line per change: time, what, who, how to undo")],
    how_side="one feed of every change, and “what changed?” first",
    how="""  <p>Bram finishes A-19 on <b>30 October</b>, the day after. From then on every change posts one line into <code>#incident</code>: deploys, infrastructure and network changes, feature flag changes (including automatic ones), and vendor maintenance notices. Each line has the <b>time, what, who, and how to undo it</b>.</p>
  <p>Every runbook and the incident template now start with the same question: <b>what changed in the last two hours?</b> If something did, and it's plausibly related, <b>undo it first</b> and diagnose afterwards, because a revert is usually faster and safer than a fix under pressure.</p>
  <p>The review of 29 October (facilitated by Ana) adds one more finding. The tidy-up was a <b>normal change applied at 18:10, the start of the evening peak</b>. That question, when changes may run, goes to volume 3. In November <b>4 of 9</b> incidents followed a change, and each time the change was found in <b>under 2 minutes</b>.</p>""",
    how_figs=[ch_how],
    steps=[("Collect every kind of change in one feed", "Deploys, infrastructure, network, flags, vendors."),
           ("One line each: time, what, who, undo", "The undo is the important part."),
           ("Put the feed where incidents happen", "The incident channel, not a separate tool."),
           ("Ask “what changed?” first", "In every runbook and the incident template."),
           ("Undo first, diagnose after", "If the change is plausibly related."),
           ("Look at when changes run", "A change at the peak is its own risk.")],
    vocab=[("Change", "Adding, modifying or removing anything that could affect a service."),
           ("Change feed", "A running list of every change, visible to on-call."),
           ("Revert (roll back)", "Undoing a change to the last known good state."),
           ("Change-related incident", "An incident caused or triggered by a change."),
           ("Mean time to innocence", "Time spent proving it wasn't your part; a sign of missing information."),
           ("Correlation", "Two things happening together; a good place to start, not yet proof.")],
    code=dict(file="ops/runbooks/_template.md", note="first section of every runbook · from 30 October 2026", plain=True, src="""
## 0 · What changed in the last 2 hours?           (look at #incident change feed)

  18:02  deploy   core v412               Ben   undo: deploy v411
  18:10  network  rules tidy-up (PR 233)   Eli   undo: revert PR 233     ← here
  …
  Is a change plausibly related?  → undo it first, then diagnose.
                                    say it in the channel before undoing.
  Nothing changed?               → go on to section 1.

feed sources: deploy pipeline · infrastructure pipeline · flag service
              · cloud audit log (console changes) · vendors.md maintenance mails
"""),
    tools="tools: webhooks from the pipelines, the flag service and the cloud's audit log into one channel. Most tools can post a message; the work is collecting them all.",
    ladder=[("changes scattered", ["History in five places.", "“What changed?” asked late, or never."]),
            ("one feed, first question", ["Every change posts time, what, who, undo.", "Runbooks start with it."]),
            ("changes linked to signals", ["Graphs show change markers.", "Alerts mention recent changes."]),
            ("automatic undo", ["A change that breaks a signal rolls itself back (vol. 3).", "People confirm."])],
    ladder_now=1,
    baseline="Each line compares <b>changes scattered across five places</b> to <b>one change feed and “what changed?” as the first question</b>.",
    ratings=[(2, 4, "Shorter incidents after changes."),
             (3, 3, "Neutral on its own."),
             (2, 4, "Found in under 2 minutes, then reverted."),
             (2, 3, "Every change carries its undo."),
             (1, 4, "All changes in one place."),
             (3, 3, "Neutral."),
             (3, 3, "A day of webhooks."),
             (2, 4, "A new on-call person can answer the key question alone."),
             (3, 4, "Automatic once set up.")],
    pitfalls=[("Only deploys in the feed", "Network, flags and console clicks are missed.", "every kind of change, including vendors'."),
              ("No undo written", "Reverting needs the author, who's on a train.", "each line says how to undo."),
              ("Diagnosing before undoing", "Twenty minutes understanding what a revert fixes in one.", "undo first if it's plausibly related."),
              ("Blaming the author", "Eli wrote the rule; Eli isn't the cause.", "ask why a peak-time change looked fine.")],
    use=["Incidents where nobody asked what changed.", "Changes come from several tools.", "New people join on-call.", "Before setting change rules (vol. 3)."],
    skip=["Never: even one deploy a week belongs in a feed."],
    related=["<b>Deployment Diagrams</b> (Ana, vol. 3)", "<b>Who Is in Charge?</b> (this volume)", "<b>Feature Flags</b> (cloud, vol. 6)", "<b>When Is It a Major Incident?</b> (this volume)"],
    quiz=[("What's the first question in every Larder incident now?", "What changed in the last two hours?"),
          ("What does each change-feed line contain?", "Time, what, who, and how to undo it."),
          ("Why undo before diagnosing?", "A revert is usually faster and safer than a fix under pressure; diagnose once customers are fine."),
          ("Why did Bram take 25 minutes on 29 October?", "Changes weren't visible in one place and no runbook asked “what changed?”, so he checked healthy systems one by one."),
          ("What other finding did the review make?", "A normal change ran at 18:10, at the start of the evening peak: when changes may run is a question for vol. 3.")],
    quiz_sit=[("Checkout errors jump at 19:05. The feed shows a flag turned on at 19:02 and a deploy at 17:30. What do you do?", "Turn the flag off first (it's the closest change and easy to undo), say so in the channel, and watch errors. If they don't drop within a few minutes, look at the deploy next.")],
    try_it="Write down every way a change can reach your production systems: pipelines, consoles, flags, vendors. How many of them would on-call see in one place, in one minute? Pick the most hidden one and make it post to a shared channel.",
    remember="The first question is <span class=\"hl\">what changed?</span>, and the fastest fix is often <span class=\"hl\">undo it</span>. Make every change visible, with its undo.",
    sources=["Betsy Beyer et al., <i>Site Reliability Engineering</i> (2016): introduction and chapter 8, release engineering.",
             "AXELOS, <i>ITIL 4: Change enablement</i> and <i>Incident management</i> practice guides (2020).",
             "Nicole Forsgren, Jez Humble and Gene Kim, <i>Accelerate</i> (2018): change failure rate."],
)

# ------------------------------------------------------------------ 13 Telling a Business Client
cr_problem = Doodle(760, 260, "Doodle of Tuesday 14 July 2026, during the Korenwolf pilot. The weekly pantry restock for Korenwolf's Amsterdam office should arrive between 07:00 and 09:00. It arrives at 09:35. Hanna asks Mo what happened. Mo forwards Eli's internal note: 'MDM update at 06:00 bricked 9 handhelds at Zuid, KE pending, PRB-005.' Hanna replies: 'I don't know what any of this means. Will it happen again?'",
                    "The client asked “will it happen again?” and got an internal note full of abbreviations.")
cr_problem.icon("truck", 40, 40, 1.4)
cr_problem.box(130, 30, 250, 90, "promised 07:00–09:00", "green", size=17)
cr_problem.box(400, 30, 346, 90, "arrived 09:35", "pink", sub="Korenwolf HQ, Tue 14 Jul", size=19, subsize=14)
cr_problem.box(14, 150, 732, 64, "“MDM update bricked 9 HHs at Zuid, KE pending, PRB-005”", "paper", size=16)
cr_problem.note(380, 244, "Hanna: “I don't know what this means. Will it happen again?”", "red", size=17)

cr_analogy = Doodle(760, 220, "Doodle of a letter from an airline after a cancelled flight: what you experienced, why in one honest sentence, what we did about it for you, and what we're changing so it doesn't happen again. No internal codes, no blame on 'technical issues' alone.",
                    "A good airline letter: what you went through, why in one honest line, what we did, what changes.")
cr_analogy.icon("envelope", 60, 60, 1.3)
for i, (t, f) in enumerate([("what you felt", "y"), ("why, honestly", "paper"), ("what we did", "blue"), ("what changes", "green")]):
    cr_analogy.box(160 + i * 148, 50, 136, 84, t, f, size=15)
cr_analogy.note(450, 186, "in their words, about their day", "pen", size=18)

cr_how = Doodle(760, 380, "The client incident report Eli and Mo send Hanna on Thursday 16 July 2026, one page. What you experienced: the restock arrived at 09:35 instead of by 09:00, 35 minutes late. Why: an automatic app update on our store devices at 06:00 failed on 9 of 31 handhelds, so picking started late. What we did on the day: the van driver called ahead at 08:40 (could have been earlier). What changes, with dates: app updates on store devices moved to 23:30, outside store hours, from 20 July; your order is now picked first at 06:00; if a delivery will be late, Mo calls you before 08:00. Mo adds the one-line apology and sends it. Hanna replies: 'Thank you, that's clear.'",
                "One page, four parts, their words, dated changes. Mo sends it; Eli writes the middle.")
for i, (t, s, f) in enumerate([("what you felt", "35 min late (09:35)", "y"), ("why", "a device update failed on 9 of 31", "paper"),
                               ("what we did", "the driver called at 08:40", "blue"), ("what changes", "updates at 23:30 from 20 Jul · picked first · call before 08:00", "green")]):
    cr_how.box(14, 14 + i * 74, 732, 62, f"{t}: {s}", f, size=16)
cr_how.note(380, 334, "Hanna: “Thank you, that's clear.”", "green", size=18)
cr_how.note(380, 366, "from the pilot to the three-office contract: same format, every time", "pen", size=15)

CLIENT_REPORTS = dict(
    slug="client-incident-reports",
    kicker="a.k.a. “the customer-facing incident report”",
    tldr="When an incident hits a <b>business client</b>, they need a short report they can pass to their own managers: <b>what they experienced, why (one honest sentence, no codes), what you did on the day, and what changes, with dates</b>. Write it for their reader, not your engineers. Let the <b>account owner</b> send it, and keep the same format every time so trust builds with each report.",
    chips=[("Family", "the hard ones"), ("Lives in", "ops/client-reports/, sent by Mo within two working days"), ("Pairs with", "incident communication, post-incident reviews, SLAs (vol. 4)")],
    itil=dict(groups=["general", "service"], chain=["engage", "improve"], practices=["relationship management", "service level management", "incident management"],
              sre="(the external postmortem)", principles=["Focus on value", "Collaborate and promote visibility"],
              older="ITIL v3: business relationship management, service reporting"),
    problem_side="Larder, Tuesday 14 July 2026",
    problem="""  <p class="lead">During the Korenwolf pilot, the weekly pantry restock for the Amsterdam office is due between 07:00 and 09:00. On Tuesday <b>14 July</b> it arrives at <b>09:35</b>. Hanna asks Mo what happened. Mo forwards Eli's internal note: <i>“MDM update at 06:00 bricked 9 HHs at Zuid, KE pending, PRB-005.”</i> <span class="hl-pink">Hanna replies: “I don't know what any of this means. Will it happen again?”</span> And she has to explain it to her own board.</p>
  <ul>
    <li>Internal notes are written for engineers.</li>
    <li>A business client needs something they can forward.</li>
    <li>The pilot ends in July; the contract decision comes in September.</li>
  </ul>""",
    problem_figs=[cr_problem],
    analogy_side="the airline's letter after a cancelled flight",
    analogy="""  <p>A good airline letter after a cancelled flight has four parts: <b>what you went through</b> (“your flight on Tuesday was cancelled and you arrived six hours late”), <b>why, in one honest sentence</b>, <b>what we did</b> for you, and <b>what we're changing</b>. It has no internal codes and doesn't hide behind “technical issues”. You might still be annoyed, but you know they understood your day.</p>""",
    analogy_figs=[cr_analogy],
    map=[("Your flight was cancelled", "Your restock arrived at 09:35, not by 09:00"),
         ("Why, in one honest sentence", "A device update at 06:00 failed on 9 of 31 handhelds"),
         ("What we did for you", "The driver called ahead at 08:40"),
         ("What we're changing", "App updates moved to 23:30 from 20 July; your order picked first"),
         ("Signed by someone you know", "Sent by Mo, the account manager")],
    how_side="four parts, their words, dated changes, sent by the account owner",
    how="""  <p>Eli and Mo write the report together on <b>16 July</b>: Eli writes the middle, Mo the beginning and end. It's one page in four parts:</p>
  <ol>
    <li><b>What you experienced</b>: “Your restock arrived at 09:35 instead of by 09:00: 35 minutes late.”</li>
    <li><b>Why</b>: “An automatic app update on our store devices at 06:00 failed on 9 of 31 handhelds, so picking started late.” No codes, and no blaming the vendor.</li>
    <li><b>What we did on the day</b>: “Our driver called your reception at 08:40. We should have called you earlier.”</li>
    <li><b>What changes, with dates</b>: app updates on store devices move to <b>23:30</b>, outside store hours, from 20 July; your order is <b>picked first at 06:00</b>; and if a delivery will be late, <b>Mo calls you before 08:00</b>.</li>
  </ol>
  <p>Mo adds a one-line apology and sends it. Hanna replies: <b>“Thank you, that's clear.”</b> The template goes into <code>ops/client-reports/</code>. Every incident that affects a business client gets one within <b>two working days</b>, sent by the account manager. In September Ruben asks for it in the contract.</p>""",
    how_figs=[cr_how],
    steps=[("Start with what they experienced", "Their time, their staff, their day."),
           ("Explain why in one honest sentence", "No codes, no vague “technical issues”."),
           ("Say what you did on the day", "Including what you should have done better."),
           ("List changes with dates", "Things they can check."),
           ("Let the account owner send it", "The relationship is theirs."),
           ("Use the same format every time", "Trust builds with consistency.")],
    vocab=[("Client incident report", "A short, external account of an incident for a business customer."),
           ("Account manager", "The person who owns the relationship with a client (Mo)."),
           ("External postmortem", "SRE's name for a review written for customers."),
           ("Commitment", "A dated promise in the report the client can hold you to."),
           ("Service credit", "Money back when a service level is missed (vol. 4)."),
           ("Plain language", "Words the client's own manager would understand.")],
    code=dict(file="ops/client-reports/2026-07-14-korenwolf.md", note="sent by Mo · Thu 16 July 2026", plain=True, src="""
To: Hanna (Korenwolf, Head of Workplace)        From: Mo (Larder for Business)
Subject: Your restock on Tuesday 14 July: what happened and what we're changing

What you experienced   Your pantry restock arrived at 09:35 instead of by
                       09:00: 35 minutes late.
Why                    An automatic app update on our store devices at
                       06:00 failed on 9 of 31 handhelds at our Zuid store, so
                       picking started late.
What we did            Our driver called your reception at 08:40. We should
                       have called you earlier.
What changes           · From Mon 20 July, app updates on our store devices
                         run at 23:30, outside store hours.
                       · From next Tuesday your order is picked first, at 06:00.
                       · If a delivery will be late, I call you before 08:00.
We're sorry for the disruption to your team's morning.               Mo
"""),
    tools="tools: a one-page template, the review notes, and a conversation with the account manager.",
    ladder=[("internal notes forwarded", ["Codes and abbreviations.", "“Will it happen again?”"]),
            ("a four-part report in their words", ["Sent by the account owner.", "Dated changes."]),
            ("reports tied to service levels", ["Each report states the SLA effect and any credit (vol. 4).", "Monthly summary for the client."]),
            ("clients see it live", ["Status page and report link per incident.", "Commitments tracked to done."])],
    ladder_now=1,
    baseline="Each line compares <b>forwarding an internal note</b> to <b>a four-part report in the client's words, sent by the account manager</b>.",
    ratings=[(2, 4, "The client's mornings are protected by dated changes."),
             (3, 3, "Neutral on its own."),
             (3, 3, "Neutral."),
             (2, 3, "The update window moved out of store hours."),
             (2, 4, "The client knows what happened and what changes."),
             (3, 3, "Neutral."),
             (3, 4, "Keeps the contract on track."),
             (3, 3, "Neutral."),
             (3, 3, "An hour per report.")],
    pitfalls=[("Forwarding the internal note", "Codes, blame and abbreviations.", "write for their manager."),
              ("Hiding behind “technical issues”", "Reads as evasive.", "one honest sentence of why."),
              ("Promises without dates", "“We'll improve” can't be checked.", "dated, checkable changes."),
              ("Engineering sends it", "The relationship is skipped.", "the account manager sends it.")],
    use=["An incident affects a business client.", "A client asks “will it happen again?”", "During a pilot or before a renewal.", "When the contract asks for reports."],
    skip=["Incidents that didn't touch the client: say nothing unless asked (and then be honest)."],
    related=["<b>Who Needs to Know?</b> (this volume)", "<b>Working with Account Managers</b> (Grace, vol. 5)", "<b>Service Levels as Features</b> (Grace, vol. 6)", "<b>What Can We Learn from It?</b> (this volume)"],
    quiz=[("What are the four parts?", "What you experienced, why, what we did on the day, what changes (with dates)."),
          ("Who sends it, and why?", "The account manager (Mo): the relationship is theirs, and the client knows them."),
          ("Why one honest sentence of why?", "It shows you understood the cause without burying the client in detail or codes."),
          ("Why dated changes?", "The client can check them; “we'll improve” can't be checked."),
          ("How fast does Larder send one?", "Within two working days.")],
    quiz_sit=[("A delivery to Korenwolf's Utrecht office is late because the van broke down, not because of IT. Does this format still apply?", "Yes: the format is about the client's experience, not the cause. Mo sends it with Joost's operations team writing the middle instead of Eli.")],
    try_it="Take your last incident that touched a customer and write the four-part report as if to their manager: what they experienced, why in one sentence, what you did, what changes with dates. Would they understand it without asking a follow-up question?",
    remember="Write for <span class=\"hl\">their manager</span>, not your engineers: what they felt, why, what you did, and <span class=\"hl\">what changes, with dates</span>.",
    sources=["Betsy Beyer et al., <i>The Site Reliability Workbook</i> (2018): appendix on postmortems (and external versions).",
             "AXELOS, <i>ITIL 4: Relationship management</i> and <i>Service level management</i> practice guides (2020).",
             "Atlassian, <i>Incident Management Handbook</i> (2020): communicating with customers."],
)

# ------------------------------------------------------------------ 14 When Is It a Major Incident?
mi_problem = Doodle(760, 260, "Doodle of Friday 18 December 2026, 18:05, the Christmas peak, two days after the database primary was resized in a hurry. The managed database fails over to its replica in about 90 seconds, but Larder Core's three virtual machines keep their connections pointed at the old primary, and checkout fails. Dee, on call, declares SEV1. Femke phones Eli three times in ten minutes; Sam's team has 300 chats; store leads ask in four places; the incident lead spends half the time answering questions instead of leading.",
                    "SEV1 at the Christmas peak, and the SEV1 process drowned in calls, chats and questions.")
mi_problem.box(14, 30, 230, 100, "checkout down", "pink", sub="18:05 · Christmas peak", size=19, subsize=14)
mi_problem.box(264, 30, 230, 100, "Femke × 3 calls", "y", sub="in ten minutes", size=19, subsize=14)
mi_problem.box(514, 30, 232, 100, "300 chats", "y", sub="Sam's team", size=19, subsize=14)
mi_problem.box(110, 160, 540, 60, "the lead answers questions instead of leading", "paper", size=17)
mi_problem.note(380, 246, "38 minutes · ≈ 900 orders lost or late", "red", size=18)

mi_analogy = Doodle(760, 220, "Doodle of a city's emergency services. A house fire is handled by one fire crew with its usual routine. A major incident, like a chemical spill near a school, switches on a different, practised plan: a commander at a separate post, a liaison for the mayor, a press officer, a log of every decision. The routine doesn't scale; the major plan exists because of that.",
                    "A house fire uses the routine. A chemical spill switches on a different, practised plan.")
mi_analogy.box(14, 40, 340, 100, "house fire", "y", sub="the crew's routine", size=19, subsize=15)
mi_analogy.box(406, 40, 340, 100, "chemical spill", "pink", sub="the major plan: commander · liaison · log", size=19, subsize=13)
mi_analogy.note(380, 190, "the routine doesn't scale to the rare, huge one", "pen", size=18)

mi_how = Doodle(760, 400, "Larder's major incident procedure, written 21 to 23 December 2026. Declared when: a SEV1 during a critical window (Friday 17:00 to 20:00, Korenwolf's 07:00 to 09:00, campaign days), or any SEV1 lasting more than 30 minutes, or more than one city down. What's added to a SEV1: a senior incident lead (Eli or Ana) who does only leading; a leadership liaison who keeps Femke informed every 15 minutes so she doesn't call the lead; customer messages in the app and on the status page; a decision log; the fix team protected from all questions. Afterwards: a review within three working days with Femke present, and options for leadership to decide. The 18 December review led to Ana's options page and Femke's choice of option B on 12 January.",
                "A practised plan on top of SEV1: a senior lead, a liaison for Femke, customer messages, a decision log, a protected fix team.")
mi_how.box(14, 14, 732, 70, "when: SEV1 in a critical window · or > 30 min · or > 1 city", "pink", size=16)
for i, (t, s, f) in enumerate([("senior lead", "Eli or Ana, leads only", "y"), ("liaison", "Femke every 15 min", "y"),
                               ("customers", "app banner + status page", "green"), ("decision log", "every choice, timed", "paper"), ("fix team", "no questions", "blue")]):
    mi_how.box(14 + i * 148, 106, 136, 100, t, f, sub=s, size=16, subsize=12)
mi_how.box(14, 230, 732, 70, "review in 3 working days, Femke present, options for leadership", "paper", size=16)
mi_how.row([("22 Dec", "review", "paper"), ("12 Jan", "Ana's options page", "paper"), ("ADR 0017", "option B: failover < 2 min", "green")], x=14, y=320, h=66, gap=40, size=16, subsize=13, arrows=True)

MAJOR_INCIDENTS = dict(
    slug="major-incidents",
    kicker="a.k.a. “major incident management”",
    tldr="A <b>major incident</b> is the rare one that hurts the whole business: a SEV1 at the worst time, or one that drags on. The normal incident process doesn't scale to it, because leaders, support and stores all need the lead at once. Define <b>when it's major</b> in advance, and add a <b>practised plan on top of SEV1</b>: a senior lead who only leads, a <b>liaison</b> for leadership, <b>customer messages</b>, a <b>decision log</b>, a fix team protected from questions, and a review with leadership afterwards.",
    chips=[("Family", "the hard ones"), ("Lives in", "ops/incidents/major.md, practised twice a year"), ("Pairs with", "severity levels, incident roles, communication, game days (vol. 5)")],
    itil=dict(groups=["service"], chain=["deliver", "engage", "improve"], practices=["incident management (major incidents)", "service continuity management"],
              sre="“major incident”: incident command at full size", principles=["Think and work holistically", "Collaborate and promote visibility"],
              older="ITIL v3: the major incident procedure"),
    pager=dict(when="Fri 18 Dec 2026 · Dee on call · Christmas peak", lines=[
        ("18:05", "managed Postgres fails over to the replica (≈ 90 s)"),
        ("18:06", "<b>PAGE</b> checkout_errors 64 % · orders_per_5min −80 %"),
        ("18:09", "Dee declares SEV1 · Eli joins as lead"),
        ("18:12", "Femke calls Eli ×3 in 10 min · 300 chats at support · 4 store groups asking"),
        ("18:20", "cause: Core's connection pools still point at the old primary"),
        ("18:22", "Core restarted VM by VM, until 18:43 (no runbook for this yet)"),
        ("18:43", "checkout back · ≈ 900 orders lost or late")]),
    problem_side="Larder, Friday 18 December 2026",
    problem="""  <p class="lead">At 18:05 on the Friday before Christmas, two days after the database primary was resized in a hurry, the managed database <b>fails over</b> to its replica in about 90 seconds. Larder Core's three VMs <b>keep their connections pointed at the old primary</b>, and checkout fails. Dee declares SEV1 at 18:09 and Eli takes the lead. Then the SEV1 process drowns. <span class="hl-pink">Femke phones Eli three times in ten minutes, Sam's team has 300 chats, and store leads ask in four different groups.</span> Eli spends half the incident answering questions. Checkout is back at 18:43: <b>38 minutes</b>, and about <b>900 orders</b> lost or late.</p>
  <ul>
    <li>The SEV1 roles work for 20 minutes on a Tuesday, not for the whole company at Christmas.</li>
    <li>Leadership wants information, and the only source is the lead.</li>
    <li>Customers see failing payments and no message.</li>
  </ul>""",
    problem_figs=[mi_problem],
    meanwhile=[("architect-3", "explaining-trade-offs", "Ana's options page for Femke, 12 January 2027: 99.99 % everywhere (a second region) or protect the minutes that matter; Femke chooses B, ADR 0017.",
                "Eli's major incident review of 22 December asked for exactly that decision: where should Larder spend to make the next Christmas failover take two minutes, not 38?")],
    analogy_side="the house fire and the chemical spill",
    analogy="""  <p>A <b>house fire</b> is handled by one fire crew following its routine. A <b>chemical spill near a school</b> switches on a <b>different, practised plan</b>: a commander at a separate post, a liaison who keeps the mayor informed so the mayor doesn't phone the commander, a press officer, and a log of every decision. The routine doesn't scale to the rare, huge event, and that's exactly why the major plan exists and is rehearsed.</p>""",
    analogy_figs=[mi_analogy],
    map=[("House fire, the crew's routine", "A normal SEV1"),
         ("Chemical spill near a school", "SEV1 at the Christmas peak"),
         ("Commander at a separate post", "A senior lead who only leads"),
         ("Liaison for the mayor", "A leadership liaison who updates Femke every 15 minutes"),
         ("The decision log", "Every choice, with its time and reason")],
    how_side="a practised plan on top of SEV1, and leadership in the review",
    how="""  <p>Eli writes the major incident procedure between <b>21 and 23 December</b>. It is a SEV1, plus:</p>
  <ul>
    <li><b>When it's major</b> (any one is enough): a SEV1 in a <b>critical window</b> (Friday 17:00–20:00, Korenwolf's 07:00–09:00, campaign days); any SEV1 lasting <b>more than 30 minutes</b>; or <b>more than one city</b> down.</li>
    <li><b>A senior lead</b> (Eli or Ana) who does nothing but lead.</li>
    <li><b>A leadership liaison</b> who updates Femke every 15 minutes, so she doesn't need to call the lead. Femke agreed to this in the review.</li>
    <li><b>Customer messages</b>: an in-app banner and the status page, from templates.</li>
    <li><b>A decision log</b>: every choice, with its time and reason.</li>
    <li><b>A protected fix team</b>: nobody asks them anything except the lead.</li>
  </ul>
  <p>The review is held on <b>22 December</b>, with Femke there. It doesn't end with actions alone. It ends with <b>options for leadership</b>: how fast must failover be at the moments that matter, and what is that worth? Ana turns that into her options page, and on <b>12 January</b> Femke chooses option B (ADR 0017): failover in under 2 minutes, tested monthly, and no changes in critical windows. The procedure is practised for the first time in a game day in January (vol. 3).</p>""",
    how_figs=[mi_how],
    steps=[("Define “major” before it happens", "Critical windows, duration, breadth."),
           ("Name a senior lead pool", "Two or three people who only lead."),
           ("Add a leadership liaison", "Leaders get updates without calling the lead."),
           ("Template customer messages", "In-app and status page, ready to send."),
           ("Keep a decision log", "Choices, times, reasons."),
           ("Review with leadership, and practise", "Options to decide, and a drill twice a year.")],
    vocab=[("Major incident", "An incident with very high impact on the business, handled by a separate procedure."),
           ("Critical window", "A time when outages hurt most."),
           ("Leadership liaison", "The person keeping executives informed, so the lead can lead."),
           ("Decision log", "A timed record of decisions during the incident."),
           ("Failover", "Switching to a standby when the main component fails."),
           ("Game day", "A planned exercise that rehearses an incident (vol. 5).")],
    code=dict(file="ops/incidents/major.md", note="written 21–23 December 2026 · first drill January 2027", plain=True, src="""
# Major incident = SEV1 + this

major when   SEV1 in a critical window (Fri 17–20 · Korenwolf 07–09 · campaign days)
             or SEV1 > 30 min · or > 1 city down
lead         senior: Eli or Ana · leads only · announces "this is a major incident"
liaison      Femke + leaders, every 15 min, direct message (Femke won't call the lead)
customers    in-app banner + status page from templates (comms role)
stores       one message to all store leads every 15 min
decision log time · decision · why · by whom  (scribe)
fix team     answers only to the lead
afterwards   review ≤ 3 working days, Femke present · options for leadership
             · drill twice a year (game day)

18 Dec 2026: 38 min · ≈ 900 orders · review 22 Dec → options → ADR 0017 (12 Jan)
"""),
    tools="tools: the SEV1 setup, message templates, a liaison channel for leaders, a decision log in the incident doc, and a calendar slot for drills.",
    ladder=[("SEV1 stretched until it breaks", ["Lead swamped by calls.", "Customers see no message."]),
            ("a written major-incident plan", ["Liaison, customer messages, decision log.", "Review with leadership."]),
            ("practised", ["Drills twice a year.", "Templates and roles pre-set in the tools."]),
            ("designed out where it counts", ["Failover tested monthly (ADR 0017).", "Major incidents rare and short."])],
    ladder_now=1,
    baseline="Each line compares <b>stretching the SEV1 process at Christmas</b> to <b>a defined, practised major-incident plan on top of it</b>.",
    ratings=[(2, 4, "Customers get a message; leaders get updates."),
             (3, 3, "Neutral on its own; ADR 0017 does the rest."),
             (2, 3, "The lead and fix team can focus."),
             (3, 4, "No changes in critical windows follows from it."),
             (2, 4, "One decision log, one liaison, one story."),
             (3, 3, "Neutral."),
             (2, 4, "Leaders decide spend with options in front of them."),
             (2, 3, "The lead isn't alone with everyone's questions."),
             (3, 3, "A page, and two drills a year.")],
    pitfalls=[("No definition", "People argue whether it's “major” at 18:10.", "write the triggers in advance."),
              ("Leaders call the lead", "The lead can't lead.", "a liaison, agreed with leaders beforehand."),
              ("A plan never practised", "Nobody remembers it at Christmas.", "drill twice a year."),
              ("A review with only engineers", "Actions, but no decisions about money or risk.", "leadership present, with options.")],
    use=["A SEV1 at the worst moment.", "Leaders and customers swamp the incident lead.", "Before peaks (Christmas, King's Day).", "When a business client's mornings are on the line."],
    skip=["Normal SEV1s and SEV2s: the usual roles are enough."],
    related=["<b>How Bad Is It?</b> (this volume)", "<b>Who Needs to Know?</b> (this volume)", "<b>Explaining Trade-offs to Non-Engineers</b> (Ana, vol. 3)", "<b>DR Tiers</b> (Ana, vol. 5)"],
    quiz=[("When is an incident major at Larder?", "A SEV1 in a critical window, or lasting over 30 minutes, or with more than one city down."),
          ("What does the leadership liaison do?", "Updates Femke and leaders every 15 minutes, so they don't need to call the lead."),
          ("What caused the 38 minutes on 18 December?", "The database failed over in about 90 seconds, but Core's VMs kept connections to the old primary until each was restarted by hand."),
          ("How does a major incident review differ?", "Leadership is present, and it ends with options for them to decide, not only engineering actions."),
          ("What came out of it?", "Ana's options page and Femke's choice of option B (ADR 0017): failover under 2 minutes, tested monthly, no changes in critical windows.")],
    quiz_sit=[("At 07:40 on a Tuesday the van routes for Korenwolf won't load and drivers are waiting. It's a SEV1 for business deliveries only. Is it major?", "Yes: it's a SEV1 in a critical window (Korenwolf's 07:00–09:00). Senior lead, a liaison for Femke and Mo, a message to Korenwolf's office managers, and a decision log.")],
    try_it="Write down your critical windows: the hours when an outage would hurt most. Then write who would lead, who would keep your leaders informed, and what customers would see, if your main service went down in one of them. Plan a one-hour drill.",
    remember="The rare, huge incident needs a <span class=\"hl\">different, practised plan</span>: a lead who only leads, a <span class=\"hl\">liaison for leaders</span>, and a message for customers.",
    sources=["AXELOS, <i>ITIL 4: Incident management</i> practice guide (2020): major incidents.",
             "Betsy Beyer et al., <i>Site Reliability Engineering</i> (2016): chapter 14, managing incidents.",
             "UK Cabinet Office, <i>Emergency Response and Recovery</i> guidance: command structures (background on incident command)."],
)

# ------------------------------------------------------------------ 15 What About the Near Misses?
nm_problem = Doodle(760, 250, "Doodle of three things that almost happened in late 2026 and were never written down: on 3 December the log disk on the database reached 91 percent and Bram cleared it at 14:00; on 10 December a deploy was rolled back by its canary before customers noticed; on 21 December Eli spotted that the courier app's new API certificate, set up by Dee's team in November outside the automatic renewal, would expire in three days. Each one was handled quietly and forgotten.",
                    "Three things that almost broke in December, handled quietly, and forgotten.")
for i, (d, t) in enumerate([("3 Dec", "DB log disk 91 %"), ("10 Dec", "canary rolled back"), ("21 Dec", "cert expires in 3 days")]):
    nm_problem.box(14 + i * 248, 30, 236, 100, d, "y", sub=t, size=19, subsize=14)
nm_problem.note(380, 176, "fixed quietly · told to nobody · lesson lost", "red", size=18)

nm_analogy = Doodle(760, 220, "Doodle of a factory's near-miss board by the canteen. A worker who almost slipped on a wet floor writes it on a card: 'wet floor by press 4, nearly fell'. The safety officer reads the cards weekly and fixes the leaking pipe before somebody breaks an arm. For every serious accident there are many near misses; each one is a free lesson.",
                    "A card on the near-miss board: “wet floor by press 4, nearly fell”. The pipe gets fixed before anyone breaks an arm.")
nm_analogy.icon("board", 60, 40, 1.6)
nm_analogy.box(180, 40, 280, 100, "near-miss cards", "y", sub="written by anyone", size=18, subsize=14)
nm_analogy.arrow(466, 90, 506, 90)
nm_analogy.box(510, 40, 236, 100, "fix the pipe", "green", sub="before the accident", size=18, subsize=14)
nm_analogy.note(450, 190, "for every accident, many near misses: free lessons", "pen", size=17)

nm_how = Doodle(760, 360, "Larder's near-miss log from 1 December 2026: anyone can add a line in two minutes in a channel. What almost happened, how it was caught, what would have happened, and is there a pattern. Nine entries in December. Reviewed monthly with the incidents. Two became actions: the courier API certificate went onto automatic renewal, and every new certificate now registers in the expiry check; the log disk got an alert at 80 percent as a ticket. The canary entry was a good save worth keeping: it showed the canary works.",
                "Two minutes per line, anyone can add one, reviewed with the incidents. Nine in December; two became actions.")
nm_how.box(14, 14, 732, 40, "what almost happened · how it was caught · what it would have done · pattern?", "paper", size=14)
for i, (t, a, f) in enumerate([("cert expiring in 3 days", "→ auto-renew + expiry check for new certs", "green"),
                               ("DB log disk 91 %", "→ ticket alert at 80 %", "green"),
                               ("canary rolled back a deploy", "→ keep: the canary works", "blue")]):
    nm_how.box(14, 70 + i * 66, 300, 54, t, "y", size=15)
    nm_how.box(326, 70 + i * 66, 420, 54, a, f, size=14)
nm_how.note(380, 296, "9 entries in December · 2 actions · 1 good save", "pen", size=17)
nm_how.note(380, 332, "nobody is ever asked “why didn't you prevent it?”", "red", size=16)

NEAR_MISSES = dict(
    slug="near-misses",
    kicker="a.k.a. “learning from what didn't happen”",
    tldr="A <b>near miss</b> is an incident that almost happened: caught by luck, by a person, or by a safety net. It carries the same lesson as the incident would have, <b>at no cost</b>. Make it <b>easy to log</b> (two minutes, anyone), review near misses with the incidents, and turn the patterns into actions. Log the <b>good saves</b> too: they show which safety nets work.",
    chips=[("Family", "the hard ones"), ("Lives in", "#near-miss channel, reviewed monthly with the incidents"), ("Pairs with", "post-incident reviews, problem management, incident metrics")],
    itil=dict(groups=["general", "service"], chain=["improve"], practices=["continual improvement", "problem management (proactive)", "risk management"],
              sre="“learning from success”; Safety-II", principles=["Progress iteratively with feedback", "Collaborate and promote visibility"],
              older="ITIL v3: proactive problem management"),
    problem_side="Larder, December 2026",
    problem="""  <p class="lead">Three things almost go wrong in December. On the <b>3rd</b> the database's log disk reaches <b>91 %</b>, and Bram clears it at 14:00. On the <b>10th</b> a deploy is <b>rolled back by its canary</b> before customers notice. On the <b>21st</b> Eli spots that the courier app's new API certificate, set up by Dee's team in November <b>outside the automatic renewal</b>, will expire in <b>three days</b>. <span class="hl-pink">Each one is handled quietly and told to nobody.</span> The certificate would have stopped every courier on Christmas Eve.</p>
  <ul>
    <li>Near misses look like non-events, so they're forgotten.</li>
    <li>The same gap (a certificate outside the renewal) can be anywhere else too.</li>
    <li>Good saves, like the canary, are never credited, so nobody knows the safety net works.</li>
  </ul>""",
    problem_figs=[nm_problem],
    analogy_side="the factory's near-miss board",
    analogy="""  <p>A factory keeps a <b>near-miss board by the canteen</b>. A worker who almost slipped writes a card: “wet floor by press 4, nearly fell”. The safety officer reads the cards weekly and <b>fixes the leaking pipe</b> before somebody breaks an arm. Safety people say that for every serious accident there are many near misses. Each one is <b>a free lesson</b>, if someone writes it down.</p>""",
    analogy_figs=[nm_analogy],
    map=[("A card on the board", "A line in #near-miss"),
         ("“Wet floor by press 4”", "“Courier API cert expires 24 Dec, not on auto-renew”"),
         ("The safety officer's weekly read", "The monthly review with the incidents"),
         ("Fixing the leaking pipe", "Automatic renewal and an expiry check for every new cert"),
         ("A cushioned floor that worked", "The canary that rolled back a bad deploy")],
    how_side="two minutes to log, reviewed with incidents, patterns become actions",
    how="""  <p>Eli opens <code>#near-miss</code> on <b>1 December</b>. Anyone can add a line in two minutes: <b>what almost happened</b>, <b>how it was caught</b>, <b>what it would have done</b>, and whether it looks like a <b>pattern</b>. Nobody is ever asked “why didn't you prevent it?”. The question is what caught it, and what would catch it next time.</p>
  <p>December has <b>nine entries</b>. At the monthly review with the incidents, two become actions. The courier certificate goes onto <b>automatic renewal</b>, and <b>every new certificate must register in the expiry check</b>: that's the pattern, a new service set up outside the normal path. The log disk gets an <b>80 % ticket alert</b>. The canary entry is kept as a <b>good save</b>, because it's evidence that the canary works and is worth keeping. Near misses also go on Femke's monthly page, as a line: “9 near misses, 2 actions”.</p>""",
    how_figs=[nm_how],
    steps=[("Open an easy place to log", "A channel, two minutes, anyone."),
           ("Ask four things only", "What, how caught, what it would have done, pattern?"),
           ("Never blame the person who logs it", "Or the log stays empty."),
           ("Review with the incidents monthly", "Same people, same patterns."),
           ("Turn patterns into actions", "With the same rules as review actions."),
           ("Log the good saves too", "They show which safety nets work.")],
    vocab=[("Near miss", "An event that could have caused harm but didn't."),
           ("Good save", "A near miss caught by a safety net (a canary, an alert, a person)."),
           ("Safety net", "Something that catches a mistake before it reaches customers."),
           ("Safety-II", "Learning from what goes right, not only from failures."),
           ("Latent condition", "A hidden weakness waiting for the right moment (a cert outside renewal)."),
           ("Leading indicator", "A sign of risk before an incident (near misses, rising disk use).")],
    code=dict(file="#near-miss", note="December 2026 · 9 entries (3 shown)", plain=True, src="""
03 Dec  DB log disk at 91 % (14:00)        caught: Bram, on a routine look
        would have: database stops writing → checkout down
        pattern? no alert below 95 %       → action: ticket alert at 80 % (Bram)

10 Dec  deploy core v431 rolled back        caught: canary, errors 3 % on 5 % of traffic
        would have: checkout errors for everyone for ~10 min
        pattern? good save                 → keep the canary; credit Ben's setup

21 Dec  courier API cert expires 24 Dec     caught: Eli, reading the cert list by hand
        would have: every courier app fails on Christmas Eve
        pattern? new service set up outside the normal path
                                           → auto-renew now · every new cert registers
                                             in the expiry check (Dee + Eli, 8 Jan)
"""),
    tools="tools: one chat channel, four questions, and a monthly review slot shared with the incidents.",
    ladder=[("handled quietly, forgotten", ["Nobody hears about them.", "Same gap waits elsewhere."]),
            ("logged and reviewed", ["Two minutes, anyone, no blame.", "Patterns become actions."]),
            ("near misses from signals", ["Alerts that fire and clear, rollbacks and retries are logged automatically.", "Trends shown."]),
            ("risk-driven", ["Near misses feed the risk register (vol. 5).", "Safety nets reviewed for gaps."])],
    ladder_now=1,
    baseline="Each line compares <b>near misses handled quietly</b> to <b>a two-minute log, reviewed with incidents, with patterns turned into actions</b>.",
    ratings=[(3, 4, "A Christmas Eve outage that never happened."),
             (2, 4, "Gaps found before they cause incidents."),
             (3, 3, "Neutral."),
             (3, 3, "Neutral."),
             (2, 4, "What almost happened is seen by everyone."),
             (3, 3, "Neutral."),
             (3, 4, "Lessons at no cost."),
             (3, 4, "Fewer night pages from things that were nearly caught."),
             (4, 4, "Two minutes per line.")],
    pitfalls=[("Blaming the logger", "“Why was the disk at 91 % at all?”", "ask what caught it and what would catch it next time."),
              ("A form, not a line", "Nobody logs anything.", "four questions in a chat line."),
              ("Logged, never reviewed", "A graveyard of near misses.", "review with the incidents monthly."),
              ("Only failures", "Safety nets that work are never credited.", "log good saves too.")],
    use=["Things almost went wrong and nobody heard.", "Before a peak, when the same gap could hit.", "Incidents are rare, so there's little to learn from.", "You want leading indicators, not only lagging ones."],
    skip=["Truly trivial slips with no possible customer harm."],
    related=["<b>What Can We Learn from It?</b> (this volume)", "<b>Why Did It Really Happen?</b> (this volume)", "<b>Canary Releases</b> (cloud, vol. 6)", "<b>Which Incident Numbers Mean Anything?</b> (this volume)"],
    quiz=[("What is a near miss?", "An event that could have caused harm but didn't: caught by luck, a person or a safety net."),
          ("What are the four questions?", "What almost happened, how it was caught, what it would have done, and is there a pattern?"),
          ("Why log good saves?", "They show which safety nets work, and that they're worth keeping."),
          ("What pattern did the certificate near miss show?", "New services set up outside the normal path miss the safety nets; every new cert must register in the expiry check."),
          ("Why must logging never lead to blame?", "People stop logging, and the free lessons disappear.")],
    quiz_sit=[("A colleague says “I nearly ran the migration on production instead of staging, but I noticed in time. Not worth writing down.” What do you say?", "It is worth it: two minutes in #near-miss. What caught it (they noticed), what would have happened, and is there a pattern (are the two environments too easy to confuse?). That's a cheap fix before someone doesn't notice.")],
    try_it="Ask your team: “What almost went wrong last month?” Write down each answer with the four questions. Which one shows a gap that could be anywhere else too?",
    remember="A near miss is a <span class=\"hl\">free lesson</span>. Make it two minutes to log, never blame the logger, and <span class=\"hl\">fix the pipe</span> before someone falls.",
    sources=["Erik Hollnagel, <i>Safety-I and Safety-II</i> (2014).",
             "Herbert W. Heinrich, <i>Industrial Accident Prevention</i> (1931): the accident triangle (as background, not as a law).",
             "AXELOS, <i>ITIL 4: Problem management</i> and <i>Risk management</i> practice guides (2020)."],
)

NOTES = [CHANGE_INCIDENTS, CLIENT_REPORTS, MAJOR_INCIDENTS, NEAR_MISSES]
