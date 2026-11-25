# Series 2 · Book 5 · The IT Operations Notebook · Vol. 2 · Learning.
# Narrator: Eli (he/him). Facts: docs/larder-casebook.md, "Book 5, Vol. 2".

# ------------------------------------------------------------------ 07 What Can We Learn from It?
pr_problem = Doodle(760, 250, "Doodle of the Monday after the 21 August StockPilot outage. In the corridor someone says 'Cho restarted the sync four times, that made it worse.' Cho hears it. The question everyone is asking is 'who did what wrong?' Nobody is asking why restarting four times looked like the right thing to do at 17:41, or what the runbook said.",
                    "The corridor version: “Cho restarted it four times.” Nobody asks why that made sense at 17:41.")
pr_problem.box(14, 30, 360, 100, "“who did it wrong?”", "pink", sub="the corridor, Monday", size=20, subsize=15)
pr_problem.box(386, 30, 360, 100, "“why did it make sense?”", "paper", sub="nobody asks", dash=True, size=19, subsize=15)
pr_problem.note(380, 176, "RB-09 said: “sync stuck? restart it”", "pen", size=18)
pr_problem.note(380, 214, "next time, people will hide what they did", "red", size=18)

pr_analogy = Doodle(760, 220, "Doodle of an aviation safety report: after a near miss, the pilots write what happened and why it made sense at the time, without fear of punishment. The investigators look for what in the cockpit, the checklist or the training led to it, and change that. Aviation got very safe this way.",
                    "Pilots report freely; investigators fix the cockpit, the checklist and the training.")
pr_analogy.icon("ship", 40, 50, 1.0)
pr_analogy.box(150, 40, 280, 100, "what happened", "y", sub="told freely, no blame", size=18, subsize=14)
pr_analogy.arrow(436, 90, 476, 90)
pr_analogy.box(480, 40, 266, 100, "what we change", "green", sub="checklist · training · cockpit", size=18, subsize=14)
pr_analogy.note(450, 190, "blame makes people hide; learning needs the truth", "pen", size=17)

pr_how = Doodle(760, 380, "Larder's post-incident review format, first used on Wednesday 26 August 2026 for the StockPilot outage. 45 minutes, led by someone who wasn't in the incident (Ana). Five parts: the timeline from the scribe's notes; at each decision point, what did the person know and why did their action make sense; what helped; what got in the way; and at most three actions with owners and dates. Findings for 21 August: the runbook said 'restart' without saying 'unless the vendor is down'; no vendor sheet; our alert beat their status page by 40 minutes. Actions: vendor sheet (Eli, 28 Aug), runbook RB-09 split (Cho, 28 Aug), the low-stock switch (Ben, 18 Sep).",
                "45 minutes, a neutral facilitator, five parts, at most three actions. Cho rewrote the runbook himself.")
for i, (t, f) in enumerate([("timeline", "paper"), ("why it made sense", "y"), ("what helped", "green"), ("what got in the way", "pink"), ("≤ 3 actions", "blue")]):
    pr_how.box(14 + i * 148, 14, 136, 84, t, f, size=15)
pr_how.box(14, 124, 732, 150, None, "paper")
pr_how.head(380, 150, "26 Aug · StockPilot outage · facilitator Ana", size=16)
pr_how.text(30, 184, "• RB-09 said “restart”, not “unless the vendor is down”", anchor="start", size=15)
pr_how.text(30, 212, "• no vendor sheet · our alert beat their status page by 40 min", anchor="start", size=15)
pr_how.text(30, 244, "→ vendor sheet (Eli) · split RB-09 (Cho) · low-stock switch (Ben)", anchor="start", size=15)
pr_how.note(380, 310, "the question is never “who?”, always “what made it make sense?”", "red", size=16)
pr_how.note(380, 350, "every SEV1 and SEV2 gets one, within a week", "pen", size=17)

PIR = dict(
    slug="post-incident-review",
    kicker="a.k.a. “blameless postmortem”",
    tldr="A <b>post-incident review</b> turns an incident into lessons. Build the <b>timeline</b>, and at each decision ask <b>what the person knew and why their action made sense at the time</b>, not who got it wrong. People act on the information, tools and instructions they have, so that's what you change. Keep it <b>short</b> (45 minutes), led by <b>someone who wasn't in it</b>, and end with <b>at most three actions</b> with owners and dates.",
    chips=[("Family", "learning"), ("Lives in", "ops/reviews/YYYY-MM-DD-name.md, within a week of every SEV1 and SEV2"), ("Pairs with", "incident roles (the scribe), problem management, action items")],
    itil=dict(groups=["service", "general"], chain=["improve"], practices=["incident management", "continual improvement"],
              sre="“blameless postmortem culture”", principles=["Progress iteratively with feedback", "Collaborate and promote visibility"],
              older="ITIL v3: major incident review"),
    problem_side="Larder, Monday 24 August 2026",
    problem="""  <p class="lead">On the Monday after the StockPilot outage someone says in the corridor: <b>“Cho restarted the sync four times, that made it worse.”</b> Cho hears it. The question going round is who did what wrong. <span class="hl-pink">Nobody is asking why restarting four times looked like the right thing to do at 17:41.</span> The answer is that it's exactly what runbook RB-09 said.</p>
  <ul>
    <li>Blame teaches people to hide what they did.</li>
    <li>The real causes (the runbook, the missing vendor sheet) stay where they are.</li>
    <li>The next person on call follows the same runbook into the same wall.</li>
  </ul>""",
    problem_figs=[pr_problem],
    analogy_side="aviation's safety reports",
    analogy="""  <p>After a near miss, airline pilots write down <b>what happened and why it made sense at the time</b>, and in most systems they can do it without fear of punishment. Investigators then look for what in <b>the cockpit, the checklist or the training</b> led there, and change that. Flying got very safe this way. If pilots were blamed, the reports would stop, and so would the learning.</p>""",
    analogy_figs=[pr_analogy],
    map=[("The near-miss report", "The post-incident review"),
         ("Why it made sense at the time", "What the on-call person knew at each decision"),
         ("The checklist", "The runbook (RB-09)"),
         ("The cockpit", "Alerts, dashboards, the vendor sheet"),
         ("Changing the checklist", "Actions: split RB-09, write vendors.md, build the switch")],
    how_side="timeline, why it made sense, three actions, no names as causes",
    how="""  <p>The first review is on <b>Wednesday 26 August</b>: 45 minutes, facilitated by <b>Ana</b>, who wasn't in the incident. It has five parts:</p>
  <ol>
    <li><b>Timeline</b>, from the pager log and the scribe's notes.</li>
    <li>At each decision: <b>what did the person know, and why did the action make sense?</b> Cho explains: the sync was stale, RB-09 said to restart it, and the restart seemed to work for a minute each time.</li>
    <li><b>What helped</b>: our own alert, 40 minutes before StockPilot's status page.</li>
    <li><b>What got in the way</b>: RB-09 didn't say “unless the vendor is down”, there was no vendor sheet, and nobody knew StockPilot's hours.</li>
    <li><b>At most three actions</b>, each with an owner and a date: the vendor sheet (Eli, 28 Aug), splitting RB-09 into “stuck” and “vendor down” (<b>Cho</b>, 28 Aug), and the low-stock switch (Ben, 18 Sep).</li>
  </ol>
  <p>The review is shared with everyone in engineering, and with Sam and Joost. Its language rule is strict: <b>no person is ever a cause</b>. “Cho restarted four times” becomes “RB-09 led on-call to restart a sync whose vendor was down”. From now on every SEV1 and SEV2 gets a review within a week.</p>""",
    how_figs=[pr_how],
    steps=[("Book it within a week", "While memory is fresh, after people have slept."),
           ("Facilitate with someone not involved", "They ask; they don't judge."),
           ("Build the timeline from records", "Pager log, scribe notes, chat."),
           ("Ask “why did it make sense?” at each decision", "What did they know? What did the tools say?"),
           ("List what helped, too", "Keep what worked."),
           ("End with at most three actions", "Owners and dates; share the write-up widely.")],
    vocab=[("Post-incident review (postmortem)", "A structured look back at an incident to learn from it."),
           ("Blameless", "Assuming people acted reasonably on what they knew; looking for causes in the system."),
           ("Timeline", "What happened when, in order, from records."),
           ("Decision point", "A moment where someone chose what to do next."),
           ("Contributing factor", "Something that made the incident possible or worse; there are usually several."),
           ("Facilitator", "The person running the review, ideally not involved in the incident.")],
    code=dict(file="ops/reviews/2026-08-21-stockpilot-outage.md", note="review held Wed 26 August 2026 · facilitator Ana", plain=True, src="""
# StockPilot outage · Fri 21 Aug 2026 · SEV2 · 2 h 10 min · ≈ 140 orders affected

Timeline      17:30 our alert · 17:41 restart (RB-09) ×4 · 17:52 vendor auto-reply
              18:10 vendor status "investigating" · 19:40 vendor recovers
Why it made   Sync stale → RB-09 says "restart". Each restart looked fine for
sense         ~1 min. Nothing said "check the vendor first".
Helped        Our alert was 40 min ahead of the vendor's status page.
Got in the    RB-09 had one path. No vendor sheet; support hours unknown.
way           No way to stop customers ordering stale stock.
Actions (≤3)  1 ops/vendors.md ........................ Eli  · 28 Aug ✓
              2 split RB-09: "stuck" vs "vendor down" .. Cho  · 28 Aug ✓
              3 low-stock switch when stale > 15 min .. Ben  · 18 Sep
Not a cause   any person. Shared with: engineering, Sam, Joost.
"""),
    tools="tools: a template, the pager log, the scribe's notes, a 45-minute slot and a facilitator from outside the incident.",
    ladder=[("blame in the corridor", ["Who did it?", "People hide what they did."]),
            ("blameless reviews for SEV1–2", ["Within a week, facilitated.", "At most three actions."]),
            ("reviews searchable and linked", ["Patterns across reviews looked for (next note).", "Template in the incident tool."]),
            ("learning from success too", ["Reviews of near misses and good saves.", "Lessons shared across teams."])],
    ladder_now=1,
    baseline="Each line compares <b>“who did it?” in the corridor</b> to <b>a blameless, facilitated review with three owned actions</b>.",
    ratings=[(3, 3, "Neutral on its own."),
             (2, 4, "Causes in runbooks and tools get fixed."),
             (2, 3, "The next on-call has a better runbook."),
             (3, 3, "Neutral."),
             (2, 4, "Everyone reads what happened and why."),
             (3, 3, "Neutral."),
             (3, 3, "Neutral."),
             (1, 4, "People can say what they did without fear."),
             (3, 3, "45 minutes plus an hour of writing.")],
    pitfalls=[("A person as root cause", "“Human error” ends the search too early.", "ask what made the action make sense."),
              ("Twelve actions", "None of them get done.", "at most three, owned and dated."),
              ("Facilitated by the boss", "People defend instead of describe.", "someone not involved, not senior."),
              ("Shared with nobody", "Only the room learns.", "publish it to everyone affected.")],
    use=["Every SEV1 and SEV2.", "A SEV3 that keeps happening.", "When the corridor has already found someone to blame.", "Near misses worth learning from (this volume)."],
    skip=["SEV4: a line in the ticket is enough."],
    related=["<b>Who Is in Charge?</b> (this volume)", "<b>Why Did It Really Happen?</b> (next note)", "<b>Why Do Action Items Never Close?</b> (this volume)", "<b>Incident Response & Postmortems</b> (cloud, vol. 6)"],
    quiz=[("What does “blameless” mean?", "Assuming people acted reasonably on what they knew, and looking for causes in tools, runbooks and information."),
          ("Why should the facilitator be someone who wasn't involved?", "They can ask neutral questions; people involved, or seniors, tend to steer and defend."),
          ("What question is asked at each decision point?", "What did the person know, and why did their action make sense at the time?"),
          ("Why at most three actions?", "More rarely get done; three owned, dated actions do."),
          ("What was the cause in the 21 August review, if not Cho?", "RB-09 had only a restart path, no vendor sheet existed, and nothing stopped customers ordering stale stock.")],
    quiz_sit=[("In a review, someone says “the real problem is that Dee didn't check the logs.” What does the facilitator ask?", "What did Dee know at that point, and what made checking the logs not the obvious step? Was it the runbook, the alert, the dashboard? The fix goes there.")],
    try_it="Take your last incident and write its timeline. At each decision write what the person knew and why their action made sense. What do you find in the tools, runbooks and information, rather than in the people?",
    remember="Ask <span class=\"hl\">why it made sense</span>, not who got it wrong. Blame makes people hide the truth; <span class=\"hl\">the system</span> is what you can fix.",
    sources=["John Allspaw, “Blameless PostMortems and a Just Culture” (Etsy, 2012).",
             "Sidney Dekker, <i>The Field Guide to Understanding 'Human Error'</i> (3rd ed., 2014).",
             "Betsy Beyer et al., <i>Site Reliability Engineering</i> (2016): chapter 15, postmortem culture."],
)

# ------------------------------------------------------------------ 08 Why Did It Really Happen?
pm_problem = Doodle(760, 260, "Doodle of the stock sync since spring 2026: restarted about three times a week, in Eli's toil log since June, and involved in 13 of 41 incidents and tickets between June and early September. Each one closed with 'restarted, works again'. Every incident was closed; the problem never was.",
                    "Thirteen incidents closed with “restarted, works again”. The problem behind them never opened.")
for i in range(13):
    pm_problem.box(14 + i * 56, 40, 48, 60, "↻", "y", size=18)
pm_problem.note(380, 140, "13 of 41 incidents · Jun → Sep · “restarted, works again”", "pen", size=17)
pm_problem.box(110, 170, 540, 60, "incidents: closed · problem: never opened", "pink", stroke="red", size=17)

pm_analogy = Doodle(760, 220, "Doodle of a leaking roof. Every time it rains, someone puts a bucket under the drip and mops the floor: incident handled. A problem fix is going up on the roof on a dry day, finding the cracked tile and replacing it.",
                    "The bucket handles today's rain. Going up on a dry day to find the cracked tile fixes the roof.")
pm_analogy.icon("bucket", 70, 70, 1.3)
pm_analogy.box(160, 40, 260, 100, "bucket + mop", "y", sub="every rain · the incident", size=18, subsize=14)
pm_analogy.box(450, 40, 296, 100, "the cracked tile", "green", sub="a dry day · the problem", size=18, subsize=14)
pm_analogy.note(450, 190, "incidents restore service; problems remove causes", "pen", size=18)

pm_how = Doodle(760, 380, "Problem PRB-003, the stock sync, opened by Eli on 7 September 2026. Pattern: failures cluster between 17:00 and 19:00 and right after the sync has been down a few minutes. Causal analysis: StockPilot allows 600 requests a minute; when a call failed, Core retried at once, with every store and every batch retrying together; the retries pushed past the limit, StockPilot answered with 'too many requests', and Core retried again: a retry storm. Fix, shipped 14 September: retries with backoff and jitter, and changes fetched in one batch per store. Restarts in October: zero. Known error KE-03 kept the workaround until then.",
                "From 13 incidents to one cause: a retry storm against a rate limit. Restarts in October: zero.")
pm_how.box(14, 14, 230, 110, "pattern", "y", sub="17:00–19:00 · after a blip", size=19, subsize=14)
pm_how.arrow(250, 69, 290, 69)
pm_how.box(296, 14, 220, 110, "cause", "pink", sub="retry storm vs 600/min limit", size=19, subsize=13)
pm_how.arrow(522, 69, 562, 69)
pm_how.box(568, 14, 178, 110, "fix 14 Sep", "green", sub="backoff + jitter · batch", size=18, subsize=13)
pm_how.box(14, 150, 732, 110, None, "paper")
pm_how.text(380, 182, "call fails → every store retries at once → 429 too many requests", size=15)
pm_how.text(380, 212, "→ retries again → over the limit → fails again …", size=15)
pm_how.text(380, 242, "until someone restarts it (and the burst starts over)", size=15)
pm_how.row([("Jun–Sep", "≈ 3 restarts a week", "pink"), ("October", "0 restarts", "green")], x=110, y=284, h=72, w=250, gap=40, size=18, subsize=14, arrows=True)

PROBLEM_MGMT = dict(
    slug="problem-management",
    kicker="a.k.a. “problem management”",
    tldr="An <b>incident</b> is fixed when the service works again; a <b>problem</b> is the <b>cause</b> behind one or more incidents, and it's fixed only when that cause is gone. Look for patterns across incidents (the same service, the same hour, the same workaround), open a problem, analyse the cause properly, keep a <b>workaround</b> until the fix lands, then <b>check the incidents stop</b>. It's how you stop restarting the same thing three times a week.",
    chips=[("Family", "learning"), ("Lives in", "ops/problems/PRB-nnn.md, reviewed monthly"), ("Pairs with", "post-incident reviews, known errors, toil")],
    itil=dict(groups=["service"], chain=["improve", "deliver"], practices=["problem management"],
              sre="“fix the cause, not the symptom”; eliminating toil at its source", principles=["Think and work holistically", "Progress iteratively with feedback"],
              older="ITIL v3: problem management (reactive and proactive)"),
    problem_side="Larder, early September 2026",
    problem="""  <p class="lead">Since spring the stock sync has been restarted about <b>three times a week</b>. It's been in Eli's toil log since June. Between June and early September it shows up in <b>13 of 41</b> incidents and tickets, and every one was closed as “restarted, works again”. <span class="hl-pink">Every incident was closed; nobody ever opened the problem.</span> The 21 August review asked “why does it get stuck at all?” and nobody could answer.</p>
  <ul>
    <li>Each restart is quick, so the pattern hides.</li>
    <li>Incident work rewards getting things running again, not getting to the cause.</li>
    <li>With every new store the sync does more work and gets stuck more often.</li>
  </ul>""",
    problem_figs=[pm_problem],
    analogy_side="the leaking roof",
    analogy="""  <p>Every time it rains, the drip comes back, and someone puts <b>a bucket under it and mops the floor</b>: today's rain is handled. Fixing the roof is a different job. You go up <b>on a dry day</b>, find the <b>cracked tile</b>, and replace it. Until then you keep the bucket handy, and after it you check that the next rain stays outside.</p>""",
    analogy_figs=[pm_analogy],
    map=[("The bucket and the mop", "Restarting the sync (incident handling)"),
         ("Each rainy day", "Each of the 13 incidents"),
         ("Going up on a dry day", "Opening PRB-003 and analysing it calmly"),
         ("The cracked tile", "A retry storm against StockPilot's rate limit"),
         ("Checking the next rain", "Restarts in October: zero")],
    how_side="find the pattern, find the cause, keep the workaround, check it's gone",
    how="""  <p>Eli opens <b>PRB-003</b> on <b>7 September</b> and works on it with Ben.</p>
  <ul>
    <li><b>Pattern:</b> the failures cluster between <b>17:00 and 19:00</b>, and right after the sync has been down for a few minutes.</li>
    <li><b>Causal analysis:</b> StockPilot allows <b>600 requests a minute</b>. When a call failed, Larder Core retried <b>at once</b>, with every store's batches retrying together. The burst went over the limit, StockPilot answered “429 too many requests”, and Core retried again: a <b>retry storm</b>. A restart only cleared the queue until the next blip.</li>
    <li><b>Workaround</b> until the fix, written as known error <b>KE-03</b> (next note): restart, but only after checking the vendor is up (RB-09).</li>
    <li><b>Fix</b>, shipped on <b>14 September</b>: retries with <b>exponential backoff and jitter</b>, and changes fetched in one batch per store.</li>
    <li><b>Check:</b> no restarts at all in October. PRB-003 is closed on 2 November, and the toil log loses its sync column.</li>
  </ul>
  <p>Eli now looks through the month's incidents for patterns on the first Monday of each month. Two more problems are opened that way before Christmas.</p>""",
    how_figs=[pm_how],
    steps=[("Look for patterns monthly", "Same service, same hour, same workaround."),
           ("Open a problem with an owner", "Separate from any one incident."),
           ("Analyse the cause properly", "Timelines, logs, “why” more than once, test the theory."),
           ("Write the workaround as a known error", "So incidents are handled well meanwhile."),
           ("Fix the cause and check it", "Did the incidents stop?"),
           ("Close it with evidence", "Numbers before and after.")],
    vocab=[("Problem", "The cause, or possible cause, of one or more incidents."),
           ("Incident vs problem", "Incidents restore service; problems remove causes."),
           ("Workaround", "A way to reduce the effect of a problem until it's fixed."),
           ("Causal analysis", "Working out why something happened, usually several causes, not one."),
           ("Retry storm", "Many clients retrying at once, making a struggling service worse."),
           ("Proactive problem management", "Finding problems from patterns before they cause a big incident.")],
    code=dict(file="ops/problems/PRB-003-stock-sync.md", note="opened 7 Sep · fixed 14 Sep · closed 2 Nov 2026", plain=True, src="""
# PRB-003 · stock sync gets stuck · owner Eli (with Ben)

Evidence      13 of 41 incidents/tickets Jun–Sep · ≈ 3 restarts a week
Pattern       17:00–19:00 · after a short StockPilot blip · more stores = worse
Cause         failed call → immediate retry, all stores at once → over the
              600/min limit → 429 → retry again (retry storm). Restart only
              clears the queue until the next blip.
Workaround    KE-03: check vendor status, then restart (RB-09 "stuck" path)
Fix           exponential backoff + jitter (max 5 min) · one batch per store
              shipped Mon 14 Sep (Ben)
Check         restarts: Sep 1–13: 6 · Sep 14–30: 0 · October: 0
Closed        2 Nov 2026 · toil log: "sync" column removed
"""),
    tools="tools: the incident list, a monthly hour to look for patterns, and the logs. The analysis matters more than any tool.",
    ladder=[("incidents only", ["Restart, close, repeat.", "Patterns invisible."]),
            ("problems opened from reviews and patterns", ["Owner, workaround, fix, check.", "Monthly pattern hunt."]),
            ("problems tracked with data", ["Incidents linked to problems.", "Cost of each problem in incidents and toil."]),
            ("problems prevented", ["Patterns flagged automatically.", "Fixes prioritised by cost."])],
    ladder_now=1,
    baseline="Each line compares <b>closing every incident with a restart</b> to <b>opening a problem, finding the cause, and checking the incidents stop</b>.",
    ratings=[(2, 4, "No more stale stock on Friday evenings."),
             (2, 4, "The sync stops failing."),
             (3, 3, "Neutral."),
             (3, 3, "Neutral."),
             (2, 3, "Patterns across incidents are looked for monthly."),
             (2, 4, "Three restarts a week → none."),
             (3, 4, "Fewer refunds from stale stock."),
             (2, 4, "One less reason to be paged."),
             (3, 3, "A week of focused work.")],
    pitfalls=[("Closing the problem with the incident", "The workaround becomes the fix.", "a problem stays open until the cause is gone."),
              ("Stopping at the first “why”", "“The sync crashed” isn't a cause.", "ask again, and test the theory."),
              ("Automating the workaround", "A script restarts it hourly; the cause stays.", "fix the cause, keep the workaround only meanwhile."),
              ("No check afterwards", "It's “fixed”, and still happens.", "compare incidents before and after.")],
    use=["The same workaround keeps closing incidents.", "A review can't answer “why does this keep happening?”", "Toil comes from a fault, not from the job.", "Monthly, as a pattern hunt."],
    skip=["A true one-off with a clear, already-fixed cause."],
    related=["<b>What Can We Learn from It?</b> (this volume)", "<b>We Know the Bug, Now What?</b> (next note)", "<b>Why Am I Always Busy?</b> (vol. 1)", "<b>Retry with Backoff</b> (distributed, vol. 1)"],
    quiz=[("What's the difference between an incident and a problem?", "An incident is fixed when service works again; a problem is the cause behind incidents, fixed when the cause is gone."),
          ("What was PRB-003's cause?", "A retry storm: Core retried failed calls at once, from all stores, pushing past StockPilot's 600/min limit."),
          ("What's a workaround for, if the problem is still open?", "To handle incidents well while the fix is built; it's written as a known error."),
          ("How did Eli know it was fixed?", "Restarts went from about three a week to zero in October."),
          ("What is proactive problem management?", "Looking for patterns across incidents before a big one forces you to.")],
    quiz_sit=[("A colleague suggests a cron job that restarts the stock sync every hour “so it never gets stuck”. What do you say?", "That's automating the workaround and hiding the cause. Open (or reopen) the problem, find why it gets stuck, and fix that.")],
    try_it="List last quarter's incidents and group them by service and by how they were fixed. Which fix appears three times or more? Open a problem for it, with an owner, a workaround and a date to look at the cause.",
    remember="The bucket handles <span class=\"hl\">today's rain</span>. Open the problem, find <span class=\"hl\">the cracked tile</span>, and check the next rain stays out.",
    sources=["AXELOS, <i>ITIL 4: Problem management</i> practice guide (2020).",
             "Marc Brooker, “Timeouts, retries, and backoff with jitter” (Amazon Builders' Library, 2019).",
             "Sidney Dekker, <i>The Field Guide to Understanding 'Human Error'</i> (3rd ed., 2014): on root causes."],
)

# ------------------------------------------------------------------ 09 We Know the Bug, Now What?
ke_problem = Doodle(760, 250, "Doodle of September 2026: Sam's team now handles store tickets first, but the fixes they could use are in engineers' heads and old chats. The picker app freezing after an Android update, the label printer that prints blank labels, the courier app's login loop: each is known, and each comes back to engineers every time.",
                    "Known bugs with known workarounds, but only in engineers' heads.")
for i, (t, s) in enumerate([("app freezes", "after Android update"), ("blank labels", "label printer"), ("login loop", "courier app")]):
    ke_problem.box(14 + i * 248, 30, 236, 96, t, "y", sub=s, size=19, subsize=14)
ke_problem.note(380, 170, "the workaround is known · the first line doesn't know it", "red", size=18)
ke_problem.note(380, 210, "so it comes back to an engineer, every time", "pen", size=17)

ke_analogy = Doodle(760, 220, "Doodle of a car manufacturer's service bulletin: 'Model X, warning light comes on in cold weather: harmless, reset like this; permanent fix in the next software update.' Every garage gets it, so mechanics don't each spend an hour rediscovering it.",
                    "A service bulletin: the known fault, the workaround, and when the real fix comes.")
ke_analogy.icon("newspaper", 60, 40, 1.4)
ke_analogy.box(160, 30, 586, 130, None, "paper")
for i, t in enumerate(["fault: warning light in cold weather", "workaround: harmless, reset with steps 1–3", "fix: software update, March"]):
    ke_analogy.text(180, 66 + i * 34, t, anchor="start", size=17)
ke_analogy.note(450, 196, "every garage gets it; nobody rediscovers it", "pen", size=17)

ke_how = Doodle(760, 360, "Larder's known-error list from September 2026: one line per known error with a number, the symptom in store words, how to recognise it, the workaround as numbered steps, who can apply it, the problem it belongs to and the fix date if any. By October, 11 known errors. KE-03 stock sync stuck (until 14 September), KE-04 picker app freezes after Android update: restart the handheld from the device tool; KE-07 label printer prints blank: power-cycle, reload the roll. Sam's team fixes 38 percent of store tickets from it in October.",
                "Symptom in store words, how to recognise it, the workaround, who can apply it, the fix if any.")
ke_how.box(14, 14, 732, 40, "KE no. · symptom · recognise it by · workaround · who · problem · fix", "paper", size=14)
for i, (k, s, w, f) in enumerate([("KE-03", "stock looks wrong", "check vendor · restart (RB-09)", "y"),
                                   ("KE-04", "app freezes after update", "restart from device tool", "green"),
                                   ("KE-07", "labels print blank", "power-cycle · reload roll", "green")]):
    y = 66 + i * 70
    ke_how.box(14, y, 110, 58, k, f, size=16)
    ke_how.box(134, y, 260, 58, s, "paper", size=14)
    ke_how.box(404, y, 342, 58, w, "paper", size=14)
ke_how.note(380, 300, "11 known errors by October · 38 % of store tickets fixed from them", "green", size=16)
ke_how.note(380, 336, "a known error is retired when its fix lands", "pen", size=16)

KNOWN_ERRORS = dict(
    slug="known-errors",
    kicker="a.k.a. “the known error database”",
    tldr="A <b>known error</b> is a problem whose cause, or at least whose <b>workaround</b>, is known but not yet fixed. Write each one down where the <b>first line</b> will find it: the symptom in users' words, how to recognise it, the workaround as steps, who can apply it, and the fix date if there is one. It stops engineers being interrupted for things already solved, and it's the list that tiered support runs on.",
    chips=[("Family", "learning"), ("Lives in", "ops/known-errors.md, searchable from the helpdesk"), ("Pairs with", "problem management, tiers and swarming, the service desk")],
    itil=dict(groups=["service", "general"], chain=["deliver", "improve"], practices=["problem management", "knowledge management"],
              sre="(runbooks for the desk)", principles=["Collaborate and promote visibility", "Keep it simple and practical"],
              older="ITIL v3: the known error database (KEDB)"),
    problem_side="Larder, September 2026",
    problem="""  <p class="lead">From 1 September Sam's team handles store tickets first, but the fixes they could use are in engineers' heads and old chat threads. The picker app <b>freezing after an Android update</b>, the label printer <b>printing blank labels</b>, the courier app's <b>login loop</b>: each one is known and has a workaround. <span class="hl-pink">Each still comes back to an engineer every time</span>, and the Rotterdam printer took four hops and two days.</p>
  <ul>
    <li>The first line can only forward what they can't look up.</li>
    <li>Engineers solve the same thing again from memory.</li>
    <li>Workarounds differ depending on who you ask.</li>
  </ul>""",
    problem_figs=[ke_problem],
    analogy_side="the car service bulletin",
    analogy="""  <p>When a car model has a known fault, the manufacturer sends every garage <b>a service bulletin</b>: “warning light in cold weather; harmless; reset it with steps 1–3; permanent fix in the March software update”. A mechanic who meets it <b>doesn't spend an hour rediscovering it</b>, and the customer gets the same answer at every garage.</p>""",
    analogy_figs=[ke_analogy],
    map=[("The service bulletin", "A known-error entry"),
         ("The fault and how to recognise it", "Symptom in store words, how to tell it's this one"),
         ("Reset with steps 1–3", "The workaround as numbered steps"),
         ("Every garage gets it", "Sam's team searches it from the helpdesk"),
         ("Fix in the March update", "The problem it belongs to, and its fix date")],
    how_side="one line per known error, in store words, retired when fixed",
    how="""  <p>Eli and Sam start <code>ops/known-errors.md</code> in September, and the helpdesk can search it. Each entry has a <b>number</b>, the <b>symptom in store words</b> (“labels print blank”, not “printer driver fault”), <b>how to recognise it</b> (to avoid applying the wrong fix), the <b>workaround</b> as numbered steps, <b>who can apply it</b> (store lead, first line, on-call), the <b>problem</b> it belongs to, and the <b>fix date</b> if there is one.</p>
  <p>By October there are <b>11 known errors</b>. KE-03 (stock sync stuck) is retired when PRB-003's fix lands. KE-04 (picker app freezes after an Android system update: restart from the device tool) stays until Dee's team defers system updates to 23:30. KE-07 (blank labels: power-cycle and reload the roll) stays for good, because it's the printer's own quirk. Each new fix from a swarm becomes a new entry before the ticket is closed. In October Sam's team fixes <b>38 %</b> of store tickets straight from the list.</p>""",
    how_figs=[ke_how],
    steps=[("Collect fixes people apply from memory", "Old chats, repeat tickets, engineers."),
           ("Write the symptom as users say it", "That's what the first line searches for."),
           ("Say how to recognise it", "So the wrong workaround isn't applied."),
           ("Write the workaround as steps", "With who is allowed to apply it."),
           ("Link it to its problem and fix date", "So it can be retired."),
           ("Retire it when the fix lands", "A stale workaround is a new bug.")],
    vocab=[("Known error", "A problem with a documented cause or workaround, not yet fixed."),
           ("Known error database (KEDB)", "The list of known errors, searchable by the people who need it."),
           ("Workaround", "Steps that reduce or remove the effect until the fix."),
           ("Symptom", "What the user sees and says."),
           ("Retire", "Remove an entry once its fix has landed and been checked."),
           ("First-line fix rate", "The share of tickets fixed by the first line alone.")],
    code=dict(file="ops/known-errors.md", note="11 entries by October 2026", plain=True, src="""
KE-03  "stock looks wrong in the app"          problem PRB-003 · RETIRED 14 Sep (fix shipped)
       recognise: stock_sync stale alert, several stores at once
       workaround: check StockPilot status → if up, RB-09 "stuck" path   who: on-call

KE-04  "picker app frozen after the morning"   problem PRB-005 · fix: defer system updates
       recognise: frozen on the logo after an Android system update
       workaround: restart the handheld from the device tool             who: first line

KE-07  "labels print blank"                    no problem: printer quirk · permanent entry
       recognise: paper moves, nothing printed, after a roll change
       workaround: 1 power off 10 s · 2 reload the roll, shiny side down
                   3 print a test label                                  who: store lead
"""),
    tools="tools: one markdown file the helpdesk can search, or the helpdesk's own knowledge base. Store words, not engineer words.",
    ladder=[("in engineers' heads", ["Same fix rediscovered.", "First line forwards everything."]),
            ("a searchable list in store words", ["Workarounds as steps.", "Linked to problems; retired when fixed."]),
            ("suggested automatically", ["The helpdesk suggests entries from ticket text.", "Usage counted per entry."]),
            ("fixed at the source", ["Entries with high usage get prioritised fixes.", "The list shrinks over time."])],
    ladder_now=1,
    baseline="Each line compares <b>workarounds in engineers' heads</b> to <b>a searchable known-error list in store words</b>.",
    ratings=[(2, 4, "Stores get the known fix at once."),
             (3, 3, "Neutral: the faults are still there."),
             (2, 4, "Minutes, not hops."),
             (3, 3, "Neutral."),
             (2, 4, "Everyone applies the same workaround."),
             (2, 4, "Engineers stop rediscovering fixes."),
             (3, 3, "Neutral."),
             (2, 4, "On-call interrupted less."),
             (3, 3, "Minutes per entry.")],
    pitfalls=[("Engineer words", "“Driver fault in CUPS queue” nobody searches for.", "write the symptom as the store says it."),
              ("No way to recognise it", "A workaround applied to the wrong problem.", "say how to tell it's this one."),
              ("Never retired", "Old workarounds applied after the fix, breaking things.", "link to the problem; retire on fix."),
              ("A list instead of a fix", "Known errors pile up for years.", "high-use entries push their problems up the queue.")],
    use=["The first line forwards things engineers fix in a minute.", "The same workaround is explained again and again.", "Problems are open with no fix date yet.", "Before giving stores self-service (vol. 4)."],
    skip=["A fault that's fixed today: no entry needed."],
    related=["<b>Why Did It Really Happen?</b> (this volume)", "<b>Who Fixes What?</b> (this volume)", "<b>Where Is That Written Down?</b> (vol. 1)"],
    quiz=[("What is a known error?", "A problem with a documented cause or workaround that isn't fixed yet."),
          ("Why write the symptom in store words?", "That's what the first line and the stores search for."),
          ("Why include “how to recognise it”?", "So the workaround isn't applied to a different problem with a similar symptom."),
          ("When is an entry retired?", "When its problem's fix has landed and been checked."),
          ("Why is KE-07 permanent?", "It's a quirk of the printer, not a fault Larder can fix.")],
    quiz_sit=[("Dee's team ships the fix for KE-04 on Tuesday. On Thursday Sam's team still restarts frozen handhelds from the list. What went wrong, and what's the fix?", "KE-04 wasn't retired when its fix shipped. Retire it now, check whether the freezes really stopped (if not, reopen PRB-005), and make retiring entries part of closing a problem.")],
    try_it="Write down five fixes you apply from memory. For each, write the symptom as the user would say it, how to recognise it, the workaround as steps and who can apply it. Give the list to whoever answers first.",
    remember="A fix in <span class=\"hl\">one engineer's head</span> gets rediscovered every week. Write it as the user says it, and <span class=\"hl\">retire it</span> when the real fix lands.",
    sources=["AXELOS, <i>ITIL 4: Problem management</i> and <i>Knowledge management</i> practice guides (2020).",
             "Consortium for Service Innovation, <i>KCS v6 Practices Guide</i> (2016).",
             "Thomas A. Limoncelli et al., <i>The Practice of System and Network Administration</i> (3rd ed., 2016): documentation for the helpdesk."],
)

# ------------------------------------------------------------------ 10 Why Do Action Items Never Close?
ai_problem = Doodle(760, 250, "Doodle of Eli's count on 5 October 2026: nine reviews since June have produced 37 action items. Eleven are done. Twelve have no owner, nine have no date, and four of them are 'improve monitoring' with nothing more specific. The oldest open item is from June.",
                    "37 actions from nine reviews. 11 done. Some with no owner, no date, or no meaning.")
ai_problem.box(14, 30, 170, 100, "37", "paper", sub="actions since June", size=30, subsize=14)
ai_problem.box(196, 30, 170, 100, "11", "green", sub="done", size=30, subsize=14)
ai_problem.box(378, 30, 170, 100, "12", "pink", sub="no owner", size=30, subsize=14)
ai_problem.box(560, 30, 186, 100, "9", "pink", sub="no date", size=30, subsize=14)
ai_problem.box(110, 160, 540, 60, "4 × “improve monitoring” · oldest open: June", "y", size=17)

ai_analogy = Doodle(760, 220, "Doodle of a household's fridge list after a burst pipe. Version one: 'be more careful with pipes', 'look into insurance', 'fix things'. Nothing happens. Version two: 'Sam: lag the loft pipe, Saturday', 'Kim: call the insurer about cover, Monday'. Both get done.",
                    "“Be more careful with pipes” never happens. “Sam: lag the loft pipe, Saturday” does.")
ai_analogy.box(14, 30, 350, 130, None, "pink")
for i, t in enumerate(["be more careful", "look into insurance", "fix things"]):
    ai_analogy.text(189, 66 + i * 32, t, size=17)
ai_analogy.box(396, 30, 350, 130, None, "green")
for i, t in enumerate(["Sam · lag loft pipe · Sat", "Kim · call insurer · Mon"]):
    ai_analogy.text(571, 76 + i * 36, t, size=17)
ai_analogy.note(380, 196, "an owner, a date and something you can see is done", "pen", size=17)

ai_how = Doodle(760, 360, "Eli's rules for review actions from 6 October 2026. Each review has at most three actions. Each action has one owner, a date, a size (an hour, a day, a week) and a done test you can check. A 15-minute review every Tuesday goes through every open action: done, on track, late with a new date, or dropped on purpose with a reason. The cleanup on 6 October: 26 open, 9 dropped honestly, 17 kept with owners and dates. By 30 November: 15 of the 17 done.",
                "Three per review, owner + date + size + done test, a 15-minute Tuesday look, and honest dropping.")
for i, (t, f) in enumerate([("one owner", "y"), ("a date", "y"), ("a size", "y"), ("a done test", "y")]):
    ai_how.box(14 + i * 186, 14, 172, 72, t, f, size=17)
ai_how.box(14, 110, 732, 70, "Tuesdays, 15 min: done · on track · late (new date) · dropped (reason)", "blue", size=16)
ai_how.row([("6 Oct", "26 open → 9 dropped · 17 kept", "paper"), ("30 Nov", "15 of 17 done", "green")], x=110, y=206, h=84, w=250, gap=40, size=19, subsize=14, arrows=True)
ai_how.note(380, 330, "dropping an action on purpose is allowed; forgetting it isn't", "pen", size=16)

ACTION_ITEMS = dict(
    slug="action-items",
    kicker="a.k.a. “follow-through”",
    tldr="A review is only as good as the <b>actions that get done</b>. Keep them <b>few</b> (three per review), each with <b>one owner, a date, a size and a test for done</b>. Look at all open actions in a <b>short weekly slot</b>, and allow actions to be <b>dropped on purpose</b>, with a reason, rather than quietly forgotten. Vague actions (“improve monitoring”) are wishes; rewrite them or drop them.",
    chips=[("Family", "learning"), ("Lives in", "ops/actions.md (or the tracker), Tuesdays 15 minutes"), ("Pairs with", "post-incident reviews, problem management, continual improvement")],
    itil=dict(groups=["general"], chain=["improve"], practices=["continual improvement"],
              sre="“postmortem action items”, tracked to completion", principles=["Progress iteratively with feedback", "Keep it simple and practical"],
              older="ITIL v3: the CSI register"),
    problem_side="Larder, 5 October 2026",
    problem="""  <p class="lead">Bram, Larder's second platform engineer, starts on <b>5 October</b>. On his first day he asks what's open from past incidents. Eli counts: nine reviews since June have produced <b>37 actions</b>, and <b>11</b> are done. Twelve have <b>no owner</b>, nine have <b>no date</b>, and four just say <b>“improve monitoring”</b>. <span class="hl-pink">The oldest open action is from June, and nobody remembers why it mattered.</span></p>
  <ul>
    <li>Each review felt productive; the follow-through wasn't.</li>
    <li>Vague actions can't be started, so they never finish.</li>
    <li>The next incident finds the same gaps.</li>
  </ul>""",
    problem_figs=[ai_problem],
    analogy_side="the fridge list after a burst pipe",
    analogy="""  <p>After a burst pipe, a household writes a list on the fridge: <b>“be more careful with pipes”, “look into insurance”, “fix things”</b>. Nothing happens. Version two says <b>“Sam: lag the loft pipe, Saturday”</b> and <b>“Kim: call the insurer about cover, Monday”</b>. Both get done, because each has a name, a day, and something you can check.</p>""",
    analogy_figs=[ai_analogy],
    map=[("“Be more careful with pipes”", "“Improve monitoring”"),
         ("“Sam: lag the loft pipe, Saturday”", "“Ben: low-stock switch when stale &gt; 15 min, 18 Sep”"),
         ("Something you can check", "A done test: “switch on in production, tested”"),
         ("Looking at the fridge every week", "Tuesday's 15-minute action review"),
         ("Crossing one off on purpose", "Dropping an action with a reason")],
    how_side="few, owned, dated, sized, testable, and looked at weekly",
    how="""  <p>On <b>6 October</b> Eli sets four rules:</p>
  <ul>
    <li><b>At most three actions per review</b> (as in the review format).</li>
    <li>Each action has <b>one owner</b>, <b>a date</b>, <b>a size</b> (an hour, a day or a week) and <b>a done test</b> you can check: “alert fires in a test”, not “monitoring improved”.</li>
    <li><b>Tuesdays, 15 minutes</b>, Eli and Bram go through every open action: done, on track, late with a new date, or <b>dropped on purpose</b> with a reason written down.</li>
    <li>An action that misses its date twice comes to tech leads, either to get time or to be dropped.</li>
  </ul>
  <p>The first cleanup is the same day. Of 26 open actions, <b>9 are dropped honestly</b>: overtaken by events, or not worth it. <b>17</b> are rewritten with owners, dates and done tests. By <b>30 November</b>, <b>15 of the 17</b> are done.</p>""",
    how_figs=[ai_how],
    steps=[("Cap actions per review", "Three, the ones that matter most."),
           ("Give each one owner and a date", "A person, not a team."),
           ("Size it", "An hour, a day, a week: if bigger, it's a project."),
           ("Write a done test", "Something anyone can check."),
           ("Review all open actions weekly", "15 minutes: done, on track, late, dropped."),
           ("Drop on purpose, with a reason", "Better than a list nobody believes.")],
    vocab=[("Action item", "A change agreed in a review to prevent or reduce a repeat."),
           ("Owner", "One person who makes sure it's done (not necessarily alone)."),
           ("Done test", "A check that shows the action is finished."),
           ("Dropping", "Deciding on purpose not to do an action, with a reason."),
           ("Follow-through rate", "Actions done ÷ actions agreed."),
           ("Improvement register", "The list of open improvements and their status.")],
    code=dict(file="ops/actions.md", note="after the cleanup of Tue 6 October 2026", plain=True, src="""
id    from review       action                               owner   size  date    done test               status
A-12  2026-08-21 SP     low-stock switch, stale > 15 min     Ben     week  18 Sep  switch tested in prod   ✓ done
A-19  2026-07-03 sync   change feed in #incident             Bram  day   30 Oct  every deploy posts      on track
A-21  2026-08-02 esc.   phone-call step in escalation        Eli     hour  7 Aug   test call received      ✓ done
A-23  2026-09-10 KE     KE-04: defer Android updates→23:30   Dee     day   20 Oct  no freezes for 2 weeks  late → 3 Nov
A-07  2026-06-12 iDEAL  "improve monitoring"                 —       —     —       —                       dropped: replaced
                                                                                                          by A-19 + payment
                                                                                                          step alert (done)
open 17 · done since 6 Oct: 4 · dropped 9 (reasons above each)
"""),
    tools="tools: one table (or the team's tracker), a recurring 15-minute slot, and permission to drop things.",
    ladder=[("actions written, then forgotten", ["No owners, no dates.", "Same gaps next incident."]),
            ("owned, dated, reviewed weekly", ["Three per review, done tests.", "Honest dropping."]),
            ("tracked with the work", ["Actions in the team's normal tracker.", "Follow-through rate reported monthly."]),
            ("prioritised by value", ["Actions ranked with other work.", "Costs and incidents prevented counted."])],
    ladder_now=1,
    baseline="Each line compares <b>37 actions with no owners or dates</b> to <b>three per review, owned, dated, tested and reviewed weekly</b>.",
    ratings=[(3, 3, "Neutral on its own."),
             (2, 4, "Fixes from reviews actually land."),
             (3, 3, "Neutral."),
             (2, 3, "Change-related actions (the feed) get done."),
             (2, 4, "Everyone can see what's open and why."),
             (3, 3, "Neutral."),
             (3, 4, "Time goes to the actions that matter; the rest are dropped."),
             (3, 3, "Neutral."),
             (3, 4, "15 minutes a week.")],
    pitfalls=[("Vague actions", "“Improve monitoring” can't be started.", "rewrite with a done test, or drop it."),
              ("Team as owner", "Everyone owns it, so nobody does.", "one person."),
              ("Too many per review", "Everything is important, so nothing is.", "three at most."),
              ("Never dropping", "The list grows until nobody trusts it.", "drop on purpose, with a reason.")],
    use=["Reviews happen but the same gaps return.", "Nobody can say what's open from past incidents.", "Action lists are long and old.", "A new person asks “what's still open?”"],
    skip=["Never, if you hold reviews."],
    related=["<b>What Can We Learn from It?</b> (this volume)", "<b>Did We Do What We Said?</b> (Sanne, vol. 5)", "<b>Why Did It Really Happen?</b> (this volume)"],
    quiz=[("What does every action need?", "One owner, a date, a size and a done test."),
          ("Why cap actions at three per review?", "Few actions get done; long lists get ignored."),
          ("What happens in the Tuesday slot?", "Every open action is marked done, on track, late with a new date, or dropped with a reason."),
          ("Why allow dropping?", "A list with honest drops is believed; a list of forgotten items isn't."),
          ("What happened to “improve monitoring”?", "Dropped, and replaced by specific actions with done tests.")],
    quiz_sit=[("An action has missed its date twice and the owner says “I just haven't had time”. What happens?", "It goes to tech leads: either it gets time in someone's plan, or it's dropped on purpose with a reason. It doesn't get a third quiet new date.")],
    try_it="Collect every open action from your last five reviews or retrospectives. For each: owner, date, size, done test. Drop anything that can't get all four, and write why. How many are left?",
    remember="A review is as good as its <span class=\"hl\">finished actions</span>. Three per review, one owner each, a date, and <span class=\"hl\">drop on purpose</span> rather than forget.",
    sources=["Betsy Beyer et al., <i>The Site Reliability Workbook</i> (2018): chapter 10, postmortem culture.",
             "AXELOS, <i>ITIL 4: Continual improvement</i> practice guide (2020): the improvement register.",
             "John Allspaw, “Blameless PostMortems and a Just Culture” (Etsy, 2012)."],
)

# ------------------------------------------------------------------ 11 Which Incident Numbers Mean Anything?
im_problem = Doodle(760, 260, "Doodle of the first incident report Femke asked for, in early November 2026: 'mean time to recovery 48 minutes'. It looks bad, but one four-hour SEV3 in a back-office tool pulls the average up; most incidents took about 20 minutes. Meanwhile a 25-minute SEV1 that stopped Dispatch is just one number among many. The average says nothing about what customers felt.",
                    "“MTTR 48 minutes.” One four-hour back-office SEV3 drags it up; a 25-minute SEV1 disappears into it.")
for i, (m, f) in enumerate([(18, "green"), (22, "green"), (25, "pink"), (19, "green"), (240, "y"), (21, "green")]):
    h = min(160, m * 0.6 + 20)
    im_problem.box(40 + i * 110, 200 - h, 80, h, f"{m}", f, size=17)
im_problem.note(380, 230, "mean 48 min · median 21 min · the SEV1 (25) hidden in the middle", "red", size=16)

im_analogy = Doodle(760, 220, "Doodle of a hospital comparing its average waiting time. It looks fine, because hundreds of quick visits hide the three patients who waited six hours with chest pain. The meaningful numbers are by severity: how long did the red patients wait?",
                    "An average wait hides the three chest-pain patients who waited six hours.")
im_analogy.box(14, 40, 340, 100, "average wait: 42 min", "y", sub="looks fine", size=19, subsize=15)
im_analogy.box(406, 40, 340, 100, "red patients: 3 × 6 h", "pink", sub="the real story", size=19, subsize=15)
im_analogy.note(380, 190, "count by severity, and count what people felt", "pen", size=18)

im_how = Doodle(760, 380, "Larder's monthly incident page from November 2026, one page for Femke. Counts by severity: SEV1, SEV2, SEV3. Customer harm: orders affected and customer-minutes. Response: time to acknowledge (median, and the worst), from 14 minutes in June to 4 in November. Recovery: the median per severity and the longest, each with its name, not one overall average. Learning: reviews held, actions done, problems closed. Trend over six months, with a line of what changed.",
                "Count by severity, measure harm in orders, show medians and the worst case, and the learning loop.")
for i, (t, s, f) in enumerate([("count by SEV", "1 · 2 · 3", "paper"), ("customer harm", "orders · minutes", "pink"), ("acknowledge", "14 → 4 min (median)", "green"), ("recovery", "median + longest, by SEV", "y"), ("learning", "reviews · actions · problems", "blue")]):
    r, c = divmod(i, 3)
    im_how.box(14 + c * 248, 14 + r * 120, 236, 100, t, f, sub=s, size=18, subsize=13)
im_how.box(510, 134, 236, 100, "trend", "paper", sub="6 months + what changed", size=18, subsize=13)
im_how.note(380, 280, "no single average across everything", "red", size=18)
im_how.note(380, 320, "harm first, speed second, learning third", "pen", size=17)

INCIDENT_METRICS = dict(
    slug="incident-metrics",
    kicker="a.k.a. “MTTA, MTTR and their traps”",
    tldr="Incident numbers should answer three questions: <b>how much did customers suffer, how fast did we respond, and are we learning?</b> Count incidents <b>by severity</b>, measure harm in <b>orders or customer-minutes</b>, and use <b>medians and the worst case</b> per severity rather than one average (MTTR) across everything, because one long, minor incident makes the average lie. Show the trend, and say what changed.",
    chips=[("Family", "learning"), ("Lives in", "one page a month for Femke and tech leads"), ("Pairs with", "severity levels, action items, SLOs (vol. 4)")],
    itil=dict(groups=["general"], chain=["improve", "engage"], practices=["measurement and reporting", "incident management"],
              sre="“MTTR is a misleading average”; measure user impact", principles=["Focus on value", "Keep it simple and practical"],
              older="ITIL v3: incident KPIs, service reporting"),
    problem_side="Larder, early November 2026",
    problem="""  <p class="lead">After the 29 October incident, Femke asks for “the incident numbers”. Eli's first draft says <b>“mean time to recovery: 48 minutes”</b>. It looks bad, and it's misleading. One <b>four-hour SEV3</b> in a back-office report pulls the average up, while most incidents took around 20 minutes. <span class="hl-pink">And the 25-minute SEV1 that stopped Dispatch is just one number among many.</span> Nothing in the draft says what customers felt, or whether anything is getting better.</p>
  <ul>
    <li>Averages hide both the worst incidents and the typical ones.</li>
    <li>Counting all incidents together mixes a printer with a city.</li>
    <li>Speed is measured; harm and learning aren't.</li>
  </ul>""",
    problem_figs=[im_problem],
    analogy_side="the hospital's average wait",
    analogy="""  <p>A hospital proudly reports an <b>average waiting time of 42 minutes</b>. It looks fine, because hundreds of quick visits for small things hide the <b>three chest-pain patients who waited six hours</b>. The meaningful question is <b>by severity</b>: how long did the red patients wait? And what changed this month so they'll wait less next month?</p>""",
    analogy_figs=[im_analogy],
    map=[("Average wait", "Mean time to recovery (MTTR) across everything"),
         ("Hundreds of quick visits", "Many short SEV3s and one long back-office one"),
         ("The chest-pain patients", "SEV1s: Dispatch on 29 October"),
         ("Waiting time for red patients", "Median and longest recovery per severity"),
         ("What changed this month", "Reviews held, actions done, problems closed")],
    how_side="harm, response, recovery by severity, and learning, on one page",
    how="""  <p>From <b>November</b> Eli sends Femke one page a month, with five parts:</p>
  <ul>
    <li><b>Count by severity</b>: SEV1, SEV2, SEV3, with six months of trend.</li>
    <li><b>Customer harm</b>: orders affected (failed, late or with wrong stock) and customer-minutes. This is the number Femke reads first.</li>
    <li><b>Time to acknowledge</b>: the median, and the worst case with its name. From <b>14 minutes in June to 4 in November</b>, after escalation and test pages.</li>
    <li><b>Recovery by severity</b>: the median and the longest, each with its name. There is <b>no overall average</b>.</li>
    <li><b>Learning</b>: reviews held, actions done, problems closed.</li>
  </ul>
  <p>Each part has one sentence on <b>what changed and why</b>. Eli keeps MTTR in a footnote, to explain why it isn't on the page: averages of skewed numbers mostly measure luck. Femke says the harm line is the first incident number she has understood.</p>""",
    how_figs=[im_how],
    steps=[("Count by severity, never all together", "A printer isn't a city."),
           ("Measure harm in customers' units", "Orders affected, customer-minutes."),
           ("Use medians and the worst case", "Name the worst; don't average it away."),
           ("Track time to acknowledge", "It's the part on-call controls most."),
           ("Show the learning loop", "Reviews, actions, problems closed."),
           ("Write what changed", "One sentence per number.")],
    vocab=[("MTTA", "Mean time to acknowledge: from alert to someone saying “I've got it”."),
           ("MTTR", "Mean time to recovery (or repair): from start to service restored."),
           ("Median", "The middle value; not pulled around by one extreme incident."),
           ("Customer-minutes", "Customers affected × minutes affected: a rough measure of harm."),
           ("Skewed distribution", "Most values small, a few very large: averages mislead here."),
           ("Leading indicator", "A number that moves before the outcome does (actions done, time to acknowledge).")],
    code=dict(file="ops/reports/incidents-2026-11.md", note="for Femke and tech leads · one page", plain=True, src="""
# Incidents · November 2026                            (trend: Jun → Nov)

count          SEV1 0 · SEV2 2 · SEV3 7      (Jun–Nov SEV1: 1, 0, 0, 0, 1, 0)
customer harm  ≈ 85 orders affected (Oct: ≈ 420, Dispatch 29 Oct)
acknowledge    median 4 min · worst 11 min (SEV3, Sun 08:10)   Jun: median 14
recovery       SEV2 median 24 min · longest 41 min (PSP, 13 Nov)
               SEV3 median 19 min · longest 3 h 50 (back-office report, not urgent)
learning       reviews 2/2 within a week · actions 15 of 17 done · PRB-003 closed

what changed   change feed in #incident (A-19) → "what changed?" answered in 1 min
note           no MTTR here: one 4-hour SEV3 made it 48 min; most took ≈ 20.
"""),
    tools="tools: the incident list with severity, start, acknowledge and resolve times, and an estimate of orders affected per incident.",
    ladder=[("one average, or nothing", ["MTTR across everything.", "Harm unknown."]),
            ("a monthly page by severity", ["Harm in orders; medians and the worst.", "Learning shown."]),
            ("collected automatically", ["Times from the paging tool.", "Orders affected from the order data."]),
            ("tied to SLOs", ["Harm measured against error budgets (vol. 4).", "Trends drive priorities."])],
    ladder_now=1,
    baseline="Each line compares <b>one MTTR across all incidents</b> to <b>a monthly page by severity with harm, medians, worst cases and learning</b>.",
    ratings=[(2, 4, "Harm to customers is the headline."),
             (3, 3, "Neutral on its own."),
             (2, 3, "Acknowledge times are watched and fall."),
             (3, 3, "Neutral."),
             (1, 4, "Femke understands what happened and what's improving."),
             (3, 3, "Neutral."),
             (2, 3, "Effort goes where harm is."),
             (3, 3, "Neutral."),
             (3, 3, "An hour a month.")],
    pitfalls=[("One average for everything", "One long minor incident dominates.", "by severity, medians and the worst."),
              ("Counting incidents as the goal", "People stop declaring them.", "count harm; more declared SEV3s can be good."),
              ("Speed without harm", "Fast recovery from incidents that hurt thousands.", "orders affected first."),
              ("Numbers without a story", "Leaders guess at the cause of a trend.", "one sentence on what changed.")],
    use=["Leaders ask for “the incident numbers”.", "MTTR is the only number you have.", "You want to show whether reviews are working.", "Before agreeing service levels (vol. 4)."],
    skip=["Very few incidents: describe each one instead of counting."],
    related=["<b>How Bad Is It?</b> (this volume)", "<b>Why Do Action Items Never Close?</b> (this volume)", "<b>Vanity vs Actionable Metrics</b> (Grace, vol. 4)", "<b>Availability Maths</b> (Ana, vol. 5)"],
    quiz=[("Why can MTTR mislead?", "Incident durations are skewed; one long minor incident pulls the average far from what typically happens."),
          ("What does Larder measure harm in?", "Orders affected and customer-minutes."),
          ("What replaces the overall average?", "Median and longest recovery, per severity, with names."),
          ("Why track time to acknowledge?", "It's the part of the response on-call controls most, and it moved from 14 to 4 minutes."),
          ("Why is counting incidents a dangerous goal?", "People stop declaring them; more honestly declared SEV3s can be a good sign.")],
    quiz_sit=[("Femke asks why there were more SEV3s this month than last. What might be a good answer, and what do you check?", "It may be good news: the new desk and tiers record things that used to be fixed quietly. Check harm (orders affected) and the SEV1–2 trend: if those fell, more declared SEV3s mean better visibility, not worse service.")],
    try_it="Take last quarter's incidents. Compute the average recovery time, then the median and the longest per severity. How different is the story? Estimate orders or users affected for the top three.",
    remember="Averages hide the <span class=\"hl\">worst night</span> and the <span class=\"hl\">typical one</span>. Count by severity, measure harm in customers, and show what changed.",
    sources=["Štěpán Davidovič, <i>Incident Metrics in SRE</i> (Google / O'Reilly, 2021).",
             "Betsy Beyer et al., <i>The Site Reliability Workbook</i> (2018): chapter 2, implementing SLOs.",
             "AXELOS, <i>ITIL 4: Measurement and reporting</i> practice guide (2020)."],
)

NOTES = [PIR, PROBLEM_MGMT, KNOWN_ERRORS, ACTION_ITEMS, INCIDENT_METRICS]
