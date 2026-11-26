# Series 2 · Book 3 · The Project Manager's Notebook · Vol. 2 · Running and steering.
# Narrator: Sanne. Running case study: Larder (facts in docs/larder-casebook.md, "Book 3, Vol. 2").
# Spine: PMBOK Guide, Eighth Edition, Governance domain. Names are PMI's; every explanation is in our own words.

GOV = ["governance"]

# ------------------------------------------------------------------ 07 Is the Work Actually Happening?
dw_problem = Doodle(760, 250, "Doodle of 5 March 2026. The plan is approved and everyone is busy. Sanne asks a simple question in the corridor: what did we finish this week? Three leads describe what they are working on. Nobody names anything finished. The count of must-haves done has moved from 33 to 34 in a week.",
                    "Everyone is busy. In a week the count of finished must-haves moved from 33 to 34.")
dw_problem.row([("“working on zones”", "Eli", "paper"), ("“nearly there”", "Ben", "paper"), ("“waiting for Eli”", "Dee", "pink")], y=30, h=80, size=17, subsize=14)
dw_problem.box(230, 140, 300, 60, "must-haves done: 33 → 34", "y", size=18)
dw_problem.note(380, 232, "busy is not the same as done", "red", size=19)

dw_analogy = Doodle(760, 240, "Doodle of a restaurant kitchen during service. The head chef stands at the pass. Every dish stops there before it leaves. The chef doesn't cook: the chef sees what is ready, what is late, who is waiting for whom, and calls out what is needed next.",
                    "The head chef at the pass doesn't cook. The chef sees what's ready, what's late and who is waiting.")
dw_analogy.icon("kitchen", 30, 70, 1.4)
dw_analogy.row([("what's ready?", None, "green"), ("what's late?", None, "y"), ("who is waiting?", None, "pink")], x=170, y=70, h=70, w=180, gap=12, size=16)
dw_analogy.note(450, 190, "everything passes one place, on a rhythm", "pen", size=19)

dw_how = Doodle(760, 400, "Rotterdam's weekly rhythm from March 2026. Monday: the decision log with Ana. Thursday at half past nine: thirty minutes with the seven leads, three questions each. What did you finish. What do you need from someone here in the next two weeks. What is blocking you. Friday: the one-page status. In between: a board of the 71 must-haves in four columns, not started, in progress, blocked and done, and Sanne clearing blockers. The count on 5 March: 34 done, 6 blocked.",
                "A weekly rhythm, three questions, and a board where “done” is the only column that counts.")
dw_how.row([("Mon", "decision log, with Ana", "paper"), ("Thu 09:30", "the leads · 30 min", "y"), ("Fri", "one-page status", "paper")], y=14, h=76, size=19, subsize=14)
dw_how.box(14, 110, 732, 100, None, "y")
dw_how.head(380, 138, "Thursday's three questions", size=19)
dw_how.text(380, 168, "what did you finish?  ·  what do you need from someone here?", size=16)
dw_how.text(380, 194, "what is blocking you?", size=16)
dw_how.row([("not started", "18", "paper"), ("in progress", "13", "blue"), ("blocked", "6", "pink"), ("done", "34", "green")], y=236, h=96, size=18, subsize=26)
dw_how.note(380, 370, "71 must-haves · Sanne's job between meetings: empty the blocked column", "pen", size=17)

DIRECTING = dict(
    slug="directing-the-work",
    kicker="a.k.a. “managing project execution”",
    tldr="Once the plan is agreed, the project manager's daily job is to <b>keep the work moving</b>: a steady rhythm, a clear view of what is <b>finished</b> (not what is busy), and fast removal of whatever blocks the people doing it. You don't do the work or tell experts how. You make sure everyone knows what is next, who is waiting for whom, and that <b>nothing sits blocked for a week</b> because nobody knew.",
    chips=[("Family", "running and steering"), ("Lives in", "one weekly meeting, one board, your calendar between them"), ("Pairs with", "the issue log, sprint goals, the decision log")],
    pmbok=dict(covers="leading and co-ordinating the work in the plan; producing the deliverables; removing blockers", domains=GOV + ["resources"],
               processes=["Manage Project Execution"], principles=["Build an empowered culture", "Focus on value"], focus=["executing"],
               older="6th: “Direct and Manage Project Work” (4.3). 7th: the Project Work domain."),
    problem_side="Larder, 5 March 2026",
    problem="""  <p class="lead">A week after the plan went to the steering group, everyone is busy. Sanne asks three leads in the corridor what they finished this week. Eli: “working on the zones.” Ben: “nearly there.” Dee: “waiting for Eli.” <span class="hl-pink">In seven days the count of finished must-haves has gone from 33 to 34.</span> Dee has been waiting four days. Eli didn't know.</p>
  <ul>
    <li>Effort is visible; finished work isn't.</li>
    <li>People wait for each other without saying so.</li>
    <li>A plan on a page doesn't move work by itself.</li>
  </ul>""",
    problem_figs=[dw_problem],
    meanwhile=[("architect-2", "decision-log", "from 16 March Ana and Sanne review the decision log together every Monday: 6 open decisions had no owner.",
                "Sanne's week starts with Ana's decision log on Mondays, before the leads meet on Thursdays.")],
    analogy_side="the pass in a restaurant kitchen",
    analogy="""  <p>During service the <b>head chef</b> stands at the <b>pass</b>, where every plate stops before it leaves. The chef isn't cooking. The chef sees what is ready, what is late, and which station is waiting for another, and calls it out: “two minutes on the fish, hold the sauce.” Without the pass, each cook is busy and the tables wait.</p>""",
    analogy_figs=[dw_analogy],
    map=[("The pass", "Thursday 09:30 and the must-have board"),
         ("A plate that leaves", "A must-have that is done, by its “done means”"),
         ("“Hold the sauce”", "“Dee needs the zones from Eli by Tuesday”"),
         ("The chef doesn't cook", "Sanne doesn't configure zones"),
         ("Service rhythm", "Monday, Thursday, Friday")],
    how_side="a rhythm, three questions, a board that counts “done”",
    how="""  <p>Sanne sets a <b>weekly rhythm</b>. <b>Monday</b>: open decisions, with Ana. <b>Thursday 09:30</b>, thirty minutes, the seven leads, three questions each: <b>what did you finish? what do you need from someone here in the next two weeks? what is blocking you?</b> <b>Friday</b>: the status page. In between hangs a <b>board</b> of the 71 must-haves in four columns. Her own job between meetings is the <b>blocked</b> column: six cards on 5 March. Four are cleared by Tuesday with one conversation each. The next week the count moves from 34 to 41.</p>""",
    how_figs=[dw_how],
    steps=[("Set a rhythm and keep it", "Same day, same time, short."),
           ("Ask what was finished", "Against “done means”, not effort."),
           ("Ask what each person needs from another", "Out loud, with a date."),
           ("Ask what is blocked", "And write it where all can see."),
           ("Clear blockers between meetings", "That is your work."),
           ("Leave the how to the people doing it", "Step in only at the joins.")],
    vocab=[("Execution", "Carrying out the work in the plan."),
           ("Deliverable", "A finished, checkable piece of the result."),
           ("Blocker", "Something that stops a piece of work from moving."),
           ("Cadence", "The regular rhythm of meetings and reports."),
           ("Work in progress", "Started, not finished. More is not better."),
           ("Stand-up", "A short, regular meeting to co-ordinate.")],
    code=dict(file="rotterdam/07-weekly-rhythm.md", note="from 5 March 2026", plain=True, src="""
# ROTTERDAM · HOW THE WEEK RUNS

MON  10:30  decision log with Ana (15 min): what is open, who decides, by when
THU  09:30  the leads (30 min, standing): three questions each
              1 what did you finish?          (against "done means")
              2 what do you need from someone here in the next two weeks?
              3 what is blocking you?
FRI  12:00  status page to the steering group (every 2nd Friday: the meeting)

THE BOARD · 71 must-haves      not started   in progress   blocked   done
  Thu 26 Feb                        25            11           2       33
  Thu  5 Mar                        18            13           6       34
  Thu 12 Mar                        13            14           3       41

BLOCKED ON 5 MAR → CLEARED BY
  Dee waits for delivery zones (Eli)           Eli, Tue 10 Mar
  supplier slots need the opening hours        Joost confirmed 08:00–22:00, 6 Mar
  training plan needs handheld delivery date   order confirmed for 16 Mar
  adverts need the final zone map              draft map agreed as good enough, 9 Mar
"""),
    tools="tools: a wall or a shared board, a 30-minute slot, and a notebook for who needs what from whom.",
    dial=[("Light", "one small team", ["A daily or weekly check-in.", "A simple board.", "Blockers said out loud."]),
          ("Standard", "Rotterdam: seven leads", ["Monday, Thursday, Friday rhythm.", "A must-have board with a blocked column.", "The project manager clears blockers."]),
          ("Heavy", "many teams and vendors", ["Work authorisation and formal progress reporting.", "Integrated schedules updated weekly.", "Dedicated co-ordinators per workstream."])],
    baseline="Each line compares <b>an approved plan and a busy team</b> to <b>a weekly rhythm, three questions and a board that counts finished work</b>.",
    ratings=[(3, 4, "Must-haves, not activity, are counted."),
             (2, 4, "A steady rate of “done” can be forecast."),
             (2, 4, "Blockers surface within a week."),
             (2, 5, "Anyone can read the board."),
             (3, 4, "The count moves, and Joost sees it."),
             (3, 4, "Leads ask each other directly."),
             (3, 4, "Re-ordering happens weekly."),
             (3, 4, "“Done” is checked against “done means”."),
             (4, 3, "Thirty minutes a week, and Sanne's time between.")],
    pitfalls=[("Status theatre", "Each lead reports to the project manager; nobody talks to each other.", "ask what they need from someone in the room."),
              ("Counting effort", "“80 % done” for three weeks.", "done or not done."),
              ("Doing the work yourself", "The project manager configures zones.", "clear the blocker; leave the how."),
              ("A meeting that grows", "Problem-solving for all in front of all.", "30 minutes; solve in pairs afterwards.")],
    use=["From the day the plan is agreed.", "When people are busy but little finishes.", "When teams wait for each other.", "On any project with more than one team."],
    skip=["A single team with its own working rhythm: join it, don't add another."],
    related=["<b>What's in the Way Right Now?</b> (next note)", "<b>Sprint goals</b> (Grace, vol. 3)", "<b>Decision log</b> (Ana, vol. 2)", "<b>Let the Team Decide</b> (vol. 1)"],
    quiz=[("What are Thursday's three questions?", "What did you finish? What do you need from someone here? What is blocking you?"),
          ("Whose job is the blocked column?", "The project manager's, between meetings."),
          ("Why count “done” and not “in progress”?", "Effort doesn't open a store; finished must-haves do."),
          ("Ben says the app work is “90 % done” for the third Thursday running. What does Sanne ask?", "Which must-haves are done by their “done means”, and what stands between the rest and done. Then whether something is blocking."),
          ("Two leads start solving a problem in the Thursday meeting. What does Sanne do?", "Ask them to take it together straight after, and note who will report back. The meeting stays at thirty minutes.")],
    try_it="This week, ask each person on your project three things: what did you finish, what do you need from someone else, what is blocking you? Write the blockers on one list. Clear two before Friday.",
    remember="Stand at the <span class=\"hl\">pass</span>. Count the plates that <span class=\"hl\">leave</span>.",
    sources=["Project Management Institute, <i>PMBOK Guide</i>, Eighth Edition (2025): Governance domain, managing execution.",
             "Project Management Institute, <i>PMBOK Guide</i>, Sixth Edition (2017): 4.3 Direct and Manage Project Work.",
             "David J. Anderson, <i>Kanban</i> (2010): visualising work and limiting work in progress."],
)

# ------------------------------------------------------------------ 08 What's in the Way Right Now?
il_problem = Doodle(760, 250, "Doodle of the end of March 2026. At the review of the way of working on 20 March, Eli asks an innocent question: who is ordering the store's internet line? Silence. It was on nobody's plan: it sat between the fit-out and the platform. The provider needs six weeks. The store opens in five and a half.",
                    "“Who is ordering the store's internet line?” Silence. Six weeks' lead time, five and a half weeks left.")
il_problem.box(20, 40, 220, 90, "fit-out", "y", sub="“not building work”", size=19, subsize=14)
il_problem.box(520, 40, 220, 90, "platform", "blue", sub="“not software”", size=19, subsize=14)
il_problem.box(280, 40, 200, 90, "internet line", "pink", sub="nobody's", size=18, subsize=15, dash=True)
il_problem.note(380, 180, "lead time 6 weeks · opening in 5½", "red", size=20)
il_problem.note(380, 216, "this is no longer a risk. It has happened.", "pen", size=18)

il_analogy = Doodle(760, 240, "Doodle of a ship's defect book. When something on board breaks, it goes in the book the same day: what, who found it, who fixes it, by when. The captain reads the book every morning. A fault that isn't in the book doesn't get fixed; a fault that stays in the book for a week gets the captain's attention.",
                    "A ship's defect book: what broke, who fixes it, by when. Read every morning.")
il_analogy.icon("ledger", 40, 50, 1.6)
il_analogy.row([("what", None, "paper"), ("owner", None, "y"), ("by when", None, "y"), ("closed", None, "green")], x=190, y=70, h=60, w=128, gap=8, size=16)
il_analogy.note(460, 180, "written the same day, read every day", "pen", size=19)

il_how = Doodle(760, 400, "The Rotterdam issue log, with issue I-07, the internet line. Raised 20 March by Eli. Impact: no fixed line at opening. Owner: Eli. Actions: line ordered 30 March, live about 13 May; workaround, a 4G router with a second SIM as backup, 600 euros; the picker app already works 30 minutes offline. Tested in the rehearsal week. Status at opening: workaround in use. Closed on 13 May when the line went live. Beside it, the difference between a risk, which might happen, and an issue, which has happened.",
                "A risk might happen. An issue has. Every issue gets an owner, a date, and a workaround if it can't be fixed in time.")
il_how.box(14, 14, 350, 80, "risk", "y", sub="might happen → plan for it", size=20, subsize=15)
il_how.box(396, 14, 350, 80, "issue", "pink", sub="has happened → fix it now", size=20, subsize=15)
il_how.arrow(366, 54, 394, 54)
il_how.box(14, 118, 732, 220, None, "paper")
il_how.head(380, 146, "I-07 · store internet line · raised 20 March · owner Eli", size=18)
for i, t in enumerate(["impact: no fixed line on 27 April", "fix: line ordered 30 March → live ≈ 13 May",
                       "workaround: 4G router + backup SIM (€600) · picker app works offline", "tested in rehearsal week · closed 13 May"]):
    il_how.text(380, 182 + i * 34, t, size=16)
il_how.note(380, 372, "23 issues raised by the end · 21 closed · 2 handed over", "pen", size=17)

ISSUES = dict(
    slug="issue-log",
    kicker="a.k.a. “the issue log”",
    tldr="An <b>issue</b> is a problem that <b>has already happened</b> and is in the way now. (A risk is something that <i>might</i> happen.) Issues go in one <b>log</b> the day they are found: what it is, what it affects, <b>one owner</b>, a <b>date</b>, and its status. If the real fix can't arrive in time, the log also holds the <b>workaround</b>. The log is read every week, and an issue that isn't moving is escalated.",
    chips=[("Family", "running and steering"), ("Lives in", "one shared list, read every Thursday"), ("Pairs with", "the risk register, directing the work, escalation")],
    pmbok=dict(covers="issues: recording, owning, resolving and escalating problems during execution", domains=GOV + ["risk"],
               processes=["Manage Project Execution"], principles=["Be an accountable leader", "Adopt a holistic view"], focus=["executing", "monitoring"],
               older="6th: the “issue log”, an output of Direct and Manage Project Work (4.3). 7th: the issue log as an artefact."),
    problem_side="Larder, 20–30 March 2026",
    problem="""  <p class="lead">At the review of the way of working on <b>20 March</b>, Eli asks: “who is ordering the store's internet line?” Silence. The builder: not building work. Eli: not software. It was on <b>nobody's plan</b>; Sanne's own map of the whole launch had no line for store IT. The provider quotes <b>six weeks</b>. The store opens in five and a half. <span class="hl-pink">This isn't a risk any more. It has happened.</span></p>
  <ul>
    <li>The problem sat between two workstreams.</li>
    <li>For ten days it lived in chat, with no owner.</li>
    <li>The line was ordered only on 30 March.</li>
  </ul>""",
    problem_figs=[il_problem],
    analogy_side="the ship's defect book",
    analogy="""  <p>On a ship, anything that breaks goes in the <b>defect book</b> the same day: what, where, who found it, who will fix it, by when. The captain reads it every morning. A fault that isn't in the book doesn't get fixed. A fault that has been in the book for a week gets the captain's personal attention. And if a part can't arrive before the next port, the book says how the ship will manage without it.</p>""",
    analogy_figs=[il_analogy],
    map=[("The defect book", "The issue log"),
         ("Written the same day", "I-07 should have been logged on 20 March, not discussed for ten days"),
         ("Who fixes it, by when", "Owner Eli; line ordered 30 March"),
         ("Managing until the next port", "The workaround: a 4G router; the offline picker app"),
         ("The captain reads it every morning", "Read every Thursday; stuck issues go to Joost")],
    how_side="log it the day it's found: owner, date, workaround",
    how="""  <p>Sanne starts the <b>issue log</b> that afternoon, ten days later than she should have, and enters the line as <b>I-07</b> with Eli as owner. The <b>fix</b>: the line is ordered on 30 March and will be live around 13 May, two weeks after opening. The <b>workaround</b>: a 4G router with a backup SIM (€600, within Sanne's authority), leaning on something Ana's team built months ago: the picker app works thirty minutes offline. It is tested in rehearsal week. The store opens on the router; I-07 is closed on 13 May. Then Sanne adds an eighth workstream line to her whole-launch map: <b>store IT</b>.</p>""",
    how_figs=[il_how],
    steps=[("Log it the day it's found", "One line; don't wait to understand it fully."),
           ("Say what it affects", "Which must-have, which milestone."),
           ("Give it one owner and a date", "A name, not a team."),
           ("If the fix is late, agree a workaround", "And test it."),
           ("Read the log every week", "Out loud, with the leads."),
           ("Close it, and ask why it happened", "The answer may be a lesson.")],
    vocab=[("Issue", "A current problem that is affecting the project."),
           ("Risk", "An uncertain event that might affect the project."),
           ("Issue log", "The list of issues with owner, date and status."),
           ("Workaround", "A temporary way to manage while the real fix is on its way."),
           ("Root cause", "The underlying reason the issue happened."),
           ("Ageing", "How long an issue has been open.")],
    code=dict(file="rotterdam/08-issue-log.md", note="extract · started 20 March 2026", plain=True, src="""
# ROTTERDAM · ISSUE LOG (extract)

ID    RAISED  ISSUE                           AFFECTS         OWNER   DUE     STATUS
I-05  12 Mar  nightly price script failed     quality check   Eli     13 Mar  closed 13 Mar
              silently for four nights                                         (alert added)
I-07  20 Mar  no internet line ordered for    opening 27 Apr  Eli     13 May  closed 13 May
              the store (lead time 6 weeks)
              FIX         line ordered 30 Mar, live 13 May
              WORKAROUND  4G router + backup SIM, €600; picker app works 30 min offline
                          tested in rehearsal week (20–24 Apr): OK
              WHY         store IT was on no workstream → added to the launch map
I-09  23 Mar  builder forecasts handover      G1, 3 Apr       Sanne   23 Mar  closed 23 Mar
              8 Apr (5 days late)                                              (escalated)
I-14   3 Apr  two blocking snags at handover  chilled stock   builder  7 Apr  closed 7 Apr
I-19  24 Apr  Saturday slot capacity too low  go / no-go      Grace   26 Apr  closed 26 Apr
I-20  24 Apr  Dutch help pages not finished   go / no-go      Grace   26 Apr  closed 26 Apr

TOTAL at closing: 23 raised · 21 closed · 2 handed over to the store manager
"""),
    tools="tools: one shared list with five columns, read aloud once a week.",
    dial=[("Light", "a small team", ["A “blocked” column on the board.", "An owner on each card.", "Cleared within days."]),
          ("Standard", "Rotterdam", ["One log: issue, affects, owner, due, status.", "Read every Thursday.", "Workarounds written down and tested."]),
          ("Heavy", "large programmes", ["Severity levels and response times.", "Root-cause analysis for serious issues.", "Trend reporting to the board."])],
    baseline="Each line compares <b>problems discussed in chat until someone picks them up</b> to <b>one issue log with owners, dates and workarounds, read weekly</b>.",
    ratings=[(3, 4, "Issues are judged by what they block."),
             (2, 4, "Open issues and their dates feed the forecast."),
             (2, 4, "Problems can't sit unowned for ten days."),
             (2, 5, "Everything in the way is on one list."),
             (3, 4, "Joost sees problems with a plan attached."),
             (3, 4, "Anyone can raise an issue."),
             (3, 4, "Workarounds keep the date alive."),
             (3, 4, "Asking “why” improves the process."),
             (4, 3, "A list to keep and ten minutes a week.")],
    pitfalls=[("Issues live in chat", "Ten days pass.", "log it the day it's found."),
              ("Owned by “the team”", "Nobody.", "one name."),
              ("Waiting for the real fix", "And missing the date.", "agree and test a workaround."),
              ("Mixing risks and issues", "Might-happens hide the have-happeneds.", "two lists; a risk that happens moves across.")],
    use=["From the first week of execution.", "The moment something is found that blocks a must-have.", "When a problem has been in chat for a day.", "At every weekly meeting."],
    skip=["Tiny problems fixed within the hour."],
    related=["<b>Is the Work Actually Happening?</b> (previous note)", "<b>When Do I Take It Upstairs?</b> (this volume)", "<b>Risks vs issues</b> (vol. 5)", "<b>See the Whole</b> (vol. 1)"],
    quiz=[("Risk or issue: “the cold room might arrive late”?", "A risk. It hasn't happened."),
          ("Risk or issue: “no internet line was ordered”?", "An issue. It has happened."),
          ("What does every issue need?", "What it affects, one owner, a date, a status, and a workaround if the fix is late."),
          ("On 22 April the 4G router drops out for ten minutes in rehearsal. What does Sanne do?", "Log it as a new issue the same day, owner Eli, due before go / no-go: find out why and whether the backup SIM took over."),
          ("Why add “store IT” to the launch map after closing I-07?", "The issue's cause was a gap between workstreams. Fixing the cause stops it happening in Utrecht.")],
    try_it="Look through this week's project chat. Find one problem that was discussed but has no owner or date. Put it on a list with both. That list is your issue log.",
    remember="A <span class=\"hl\">risk</span> might happen. An <span class=\"hl\">issue</span> has. Log it the same day.",
    sources=["Project Management Institute, <i>PMBOK Guide</i>, Eighth Edition (2025): Governance domain, managing execution.",
             "Project Management Institute, <i>PMBOK Guide</i>, Sixth Edition (2017): the issue log (4.3).",
             "AXELOS, <i>Managing Successful Projects with PRINCE2</i> (2017): issue and change control."],
)

# ------------------------------------------------------------------ 09 Is Our Way of Working Working?
qa_problem = Doodle(760, 250, "Doodle of 12 March 2026. The nightly script that checks every product has a price was Rotterdam's proudest quality measure. Eli discovers it has been failing for four nights. No list was produced, so nobody saw a problem. The check existed. It wasn't working. Nobody was checking the check.",
                    "The nightly check had failed silently for four nights. Nobody was checking the check.")
qa_problem.row([("night 1", "failed", "pink"), ("night 2", "failed", "pink"), ("night 3", "failed", "pink"), ("night 4", "failed", "pink")], y=30, h=70, size=17, subsize=15)
qa_problem.note(380, 140, "no list produced → “no problems”", "red", size=20)
qa_problem.note(380, 180, "the check existed. It wasn't working.", "pen", size=18)
qa_problem.note(380, 220, "who checks the check?", "pen", size=18)

qa_analogy = Doodle(760, 240, "Doodle of a restaurant. The chef tastes each dish before it goes out: that is checking the result. Once a month an inspector checks the kitchen itself: are the fridges cold, are hands washed, are the knives sharp, is the tasting actually happening. The inspector never tastes a dish.",
                    "The chef tastes the dish. The inspector checks the kitchen. Different jobs, both needed.")
qa_analogy.box(20, 40, 330, 100, "the chef tastes the dish", "y", sub="is this result right?", size=18, subsize=15)
qa_analogy.box(410, 40, 330, 100, "the inspector checks the kitchen", "blue", sub="will this way of working give good results?", size=16, subsize=13)
qa_analogy.note(185, 180, "quality control", "red", size=20)
qa_analogy.note(575, 180, "quality assurance", "red", size=20)

qa_how = Doodle(760, 400, "The quality assurance review of 20 March 2026: five checks in the way of working, each asked three questions. Does it exist, is it being done, does it catch things. Nightly price script: exists, was failing silently, now alerts Eli. Shelf scan: exists, not started yet. Twenty practice orders: exists, done by twelve of fifteen pickers. Weekly end-to-end order: exists, done, caught two faults. Thursday's done-means check: exists, done. Three improvements agreed, each with an owner.",
                "For each check in the process: does it exist, is it being done, does it catch things?")
qa_how.row([("exists?", None, "paper"), ("being done?", None, "paper"), ("catches things?", None, "paper")], x=250, y=14, h=44, w=158, gap=8, size=14)
rowsQ = [("nightly price script", ["yes", "NO: 4 nights", "now alerts Eli"], ["green", "pink", "y"]),
         ("label scan at the shelf", ["yes", "from 6 April", "to check"], ["green", "paper", "paper"]),
         ("20 practice orders", ["yes", "12 of 15 pickers", "3 to finish"], ["green", "y", "y"]),
         ("weekly order in RTM-0", ["yes", "yes", "2 faults found"], ["green", "green", "green"]),
         ("“done means” on Thursdays", ["yes", "yes", "yes"], ["green", "green", "green"])]
for i, (name, cells, fills) in enumerate(rowsQ):
    y = 72 + i * 58
    qa_how.text(14, y + 30, name, anchor="start", size=15)
    for k, (c, f) in enumerate(zip(cells, fills)):
        qa_how.box(250 + k * 166, y, 158, 46, c, f, size=13, rx=5)
qa_how.note(380, 384, "three improvements, each with an owner and a date", "pen", size=16)

QA = dict(
    slug="quality-assurance",
    kicker="a.k.a. “quality assurance” (and how it differs from quality control)",
    tldr="<b>Quality control</b> checks the <b>result</b>: is this shelf right, does this order work? <b>Quality assurance</b> checks the <b>way of working</b>: do our checks exist, are they being done, do they catch things? Control finds faults. Assurance finds out <b>why faults get through</b>, and improves the process. A project needs both; assurance is the one that gets forgotten, because when it is missing everything looks fine.",
    chips=[("Family", "running and steering"), ("Lives in", "a short review every few weeks; improvements in the plan"), ("Pairs with", "build quality in, tailoring, lessons learned")],
    pmbok=dict(covers="quality assurance: checking and improving the way the project works; audits and process improvement", domains=GOV,
               processes=["Manage Quality Assurance"], principles=["Embed quality into processes and deliverables"], focus=["executing"],
               older="6th: “Manage Quality” (8.2), with “Control Quality” (8.3) for the results. 7th: quality under the Delivery domain."),
    problem_side="Larder, 12–20 March 2026",
    problem="""  <p class="lead">The <b>nightly script</b> that lists products without a price was Rotterdam's proudest quality measure: the lesson of Zuid, automated. On <b>12 March</b> Eli finds it has been <b>failing for four nights</b>. A failed run produces no list, and no list looks exactly like “no problems”. <span class="hl-pink">The check existed. It wasn't working. Nobody was checking the check.</span> When it runs again it lists 212 products.</p>
  <ul>
    <li>A check that fails quietly gives false comfort.</li>
    <li>Everyone looked at results; nobody looked at the process.</li>
    <li>The same could be true of every other check.</li>
  </ul>""",
    problem_figs=[qa_problem],
    analogy_side="the chef and the inspector",
    analogy="""  <p>In a restaurant the <b>chef tastes each dish</b> before it leaves the kitchen. That catches a salty sauce. Once a month an <b>inspector checks the kitchen</b>: are the fridges cold, is the tasting really happening, are the thermometers accurate? The inspector never tastes a dish, and still prevents more bad dinners than the tasting does.</p>""",
    analogy_figs=[qa_analogy],
    map=[("Tasting the dish", "Quality control: the nightly list, the shelf scan, the test order"),
         ("Inspecting the kitchen", "Quality assurance: the review of 20 March"),
         ("Is the thermometer accurate?", "Does the script alert when it fails?"),
         ("Is tasting really happening?", "Have all pickers done their 20 practice orders?"),
         ("The inspector's short report", "Three improvements with owners")],
    how_side="three questions about every check in the process",
    how="""  <p>On <b>20 March</b> (the date set in February to review the way of working) Sanne, Eli, Tomás and Ben go through the five checks built into Rotterdam and ask three questions of each: <b>does it exist? is it being done? does it catch things?</b> The script: existed, wasn't running; it now sends Eli an alert if it fails or finds nothing to check. The practice orders: 12 of 15 pickers have done them; three haven't. The weekly test order: running, and it has caught two real faults. Three improvements go into the plan with owners. The review takes forty minutes, and it is where the missing internet line comes up.</p>""",
    how_figs=[qa_how],
    steps=[("List the checks your process relies on", "From “done means” and the plan."),
           ("Ask: does each exist?", "Written down, with an owner."),
           ("Ask: is it actually being done?", "Look at evidence, not intentions."),
           ("Ask: does it catch things?", "A check that never finds anything deserves a look."),
           ("Agree a few improvements", "Owner and date each."),
           ("Repeat every few weeks", "And after any fault that got through.")],
    vocab=[("Quality assurance", "Making sure the processes used will produce good results."),
           ("Quality control", "Checking the results themselves against what was required."),
           ("Audit", "A structured check that a process is being followed and is working."),
           ("Process improvement", "Changing how work is done so faults are less likely."),
           ("Silent failure", "A check that fails without telling anyone."),
           ("Escaped defect", "A fault that got past the checks.")],
    code=dict(file="rotterdam/09-quality-review.md", note="Sanne, Eli, Tomás, Ben · 20 March 2026 · 40 minutes", plain=True, src="""
# ROTTERDAM · IS OUR WAY OF WORKING WORKING?  (review 1 · 20 March 2026)

CHECK                        EXISTS  BEING DONE?                 CATCHES THINGS?
Nightly price/VAT/zone script  yes   NO: failed silently 8–11    yes: 212 products when
                                     Mar (see I-05)              it ran again
Label scan at the shelf        yes   starts with stocking, 6 Apr to be checked at G2
20 practice orders per picker  yes   12 of 15 done               yes: 2 pickers re-trained
Weekly end-to-end order, RTM-0 yes   yes, every Wednesday        yes: 2 faults (VAT on
                                                                 deposits; a missing zone)
"Done means" on Thursdays      yes   yes                         yes: 3 items reopened

IMPROVEMENTS                                             OWNER    BY
1 script alerts on failure AND on "nothing checked"      Eli      23 Mar
2 no picker on shift before 20 practice orders           Tomás    30 Mar
3 store IT added to the launch map and the gates         Sanne    23 Mar

ALSO FOUND   no internet line ordered → issue I-07
NEXT REVIEW  17 April, with Gate 2
"""),
    tools="tools: the list of checks, three questions, forty minutes, and evidence in the room.",
    dial=[("Light", "a small team", ["A retrospective question: “did any check let something through?”", "One improvement at a time.", "Every few weeks."]),
          ("Standard", "Rotterdam", ["A 40-minute review of each built-in check.", "Three questions each.", "Improvements with owners."]),
          ("Heavy", "regulated or safety-critical work", ["A quality management plan and standards.", "Independent audits.", "Measured defect rates and corrective-action tracking."])],
    baseline="Each line compares <b>trusting that built-in checks are working</b> to <b>a short, regular review of whether each check exists, is done and catches things</b>.",
    ratings=[(3, 4, "A store that works on day one."),
             (3, 4, "Fewer late discoveries."),
             (2, 4, "Silent failures are found."),
             (2, 4, "The state of each check is known."),
             (3, 4, "Joost sees evidence, not reassurance."),
             (3, 4, "The team improves its own process."),
             (3, 4, "The way of working is adjusted on purpose."),
             (3, 5, "That is the point."),
             (4, 3, "Forty minutes every few weeks.")],
    pitfalls=[("Only checking results", "The process decays unnoticed.", "review the checks themselves."),
              ("Checks that fail quietly", "No news looks like good news.", "alert on failure and on “nothing checked”."),
              ("Assurance as blame", "People hide gaps.", "ask about the process, not the person."),
              ("A long list of improvements", "None happen.", "three, with owners.")],
    use=["A few weeks into execution.", "After any fault that got through.", "At each phase gate.", "When all checks have been green for suspiciously long."],
    skip=["Throwaway work with nothing built in to check."],
    related=["<b>Build Quality In</b> (vol. 1)", "<b>How Much Process Do We Need?</b> (vol. 1)", "<b>Fitness functions</b> (Ana, vol. 1)", "<b>What Did We Learn?</b> (this volume)"],
    quiz=[("Assurance or control: scanning a label at the shelf?", "Control: it checks a result."),
          ("Assurance or control: checking that every picker did the practice orders?", "Assurance: it checks that the process is being followed."),
          ("What are the three questions?", "Does it exist? Is it being done? Does it catch things?"),
          ("The weekly test order has passed six times in a row. Good news?", "Probably, but ask whether it still tests what matters. A check that never finds anything deserves a look."),
          ("Why did the failed script look like “no problems”?", "It produced no list. It now alerts when it fails or when it has nothing to check.")],
    try_it="Pick one check your project relies on. Find evidence, today, that it ran this week and what it found. If you can't, you've found your first quality assurance result.",
    remember="The <span class=\"hl\">chef</span> tastes the dish. Someone must also check the <span class=\"hl\">kitchen</span>.",
    sources=["Project Management Institute, <i>PMBOK Guide</i>, Eighth Edition (2025): Governance domain, managing quality assurance.",
             "Project Management Institute, <i>PMBOK Guide</i>, Sixth Edition (2017): 8.2 Manage Quality, 8.3 Control Quality.",
             "W. Edwards Deming, <i>Out of the Crisis</i> (1986).",
             "Joseph Juran, <i>Juran's Quality Handbook</i> (7th ed., 2016)."],
)

# ------------------------------------------------------------------ 10 Where Are We, Really?
sr_problem = Doodle(760, 250, "Doodle of 27 March 2026. Sanne's status page has seven lines and seven colours. Marco asks: why is schedule amber and not red, and would you have called it amber last week too? She realises the colours are her mood. There is no rule behind any of them.",
                    "“Why amber and not red?” The colours were a mood. There was no rule behind them.")
sr_problem.icon("traffic", 50, 30, 1.5)
sr_problem.box(180, 30, 250, 60, "schedule: amber", "y", size=18)
sr_problem.box(180, 110, 250, 60, "finance: green", "green", size=18)
sr_problem.text(600, 60, "why amber?", size=18)
sr_problem.text(600, 92, "compared with what?", size=18)
sr_problem.text(600, 124, "getting better or worse?", size=18)
sr_problem.note(380, 216, "a colour without a rule is an opinion", "red", size=20)

sr_analogy = Doodle(760, 240, "Doodle of a car navigation screen. It shows where you are on the planned route, how far is left, and the expected arrival time, updated as you drive. If traffic builds up it says so at once and offers another route. It never says “making good progress”.",
                    "A sat-nav shows where you are, what's left, and when you'll arrive. It never says “making good progress”.")
sr_analogy.icon("map", 40, 60, 1.6)
sr_analogy.row([("where we are", "against the route", "blue"), ("what's left", "distance", "y"), ("arrival time", "updated as we drive", "green")], x=180, y=60, h=84, w=178, gap=10, size=16, subsize=13)
sr_analogy.note(460, 196, "position · remaining · forecast", "pen", size=20)

sr_how = Doodle(760, 400, "Rotterdam's status of 27 March 2026, one month before opening. A chart of must-haves done against the plan line: 49 done, the plan said 52. Milestones: fit-out forecast 8 April against a baseline of 3 April, escalated on the 23rd and recovered. Money: 355.5 thousand euros committed of 380. Overall amber, by the written rules. A forecast: 71 must-haves by 24 April if the rate of four a week rises to six. And two decisions asked of the steering group.",
                "Position against the baseline, a forecast, a colour that follows rules, and what is needed from the reader.")
sr_how.box(14, 14, 420, 230, None, "paper")
sr_how.line("M50 220 h360 M50 220 v-190", thin=True)
sr_how.line("M50 152 L410 40", dash=True, thin=True)
sr_how.line("M50 152 L130 136 L210 118 L290 100 L310 96", color="green")
sr_how.note(370, 36, "plan", size=14)
sr_how.note(326, 120, "49 done", "green", size=16)
sr_how.note(330, 82, "plan: 52", size=14)
sr_how.note(230, 240, "must-haves done, by week (of 71)", size=14)
sr_how.box(452, 14, 294, 68, "AMBER", "y", sub="by the rules", size=24, subsize=14)
sr_how.box(452, 94, 294, 68, "forecast", "blue", sub="71 by 24 Apr needs 6 a week", size=18, subsize=13)
sr_how.box(452, 174, 294, 70, "money", "green", sub="€355.5k of €380k committed", size=18, subsize=13)
sr_how.box(14, 264, 732, 100, None, "pink")
sr_how.head(380, 292, "needed from the steering group", size=18)
sr_how.text(380, 322, "1 confirm approvals move to June (31 Mar session)  ·  2 nothing new for launch after 3 April", size=14)

sr_deep1 = Doodle(760, 304, "The written rules for Rotterdam's status colours. Schedule: green if every milestone is forecast on its baseline date; amber if one is forecast up to three days late with a recovery plan; red if any is more than three days late or there is no plan. Scope: green if must-haves done are within three of the plan line; amber if four to eight behind; red if more. Finance: green if the forecast is within budget and the reserve is untouched; amber if the reserve is in use; red if the forecast is over budget.",
                  "Colours with rules: anyone holding the same numbers would pick the same colour.")
rules = [("schedule", "all on baseline", "≤ 3 days late + plan", "> 3 days late"),
         ("scope", "≤ 3 behind plan", "4–8 behind", "> 8 behind"),
         ("finance", "reserve untouched", "reserve in use", "over budget")]
for k, (t, f) in enumerate([("green", "green"), ("amber", "y"), ("red", "pink")]):
    sr_deep1.box(150 + k * 202, 14, 194, 40, t, f, size=17, rx=5)
for i, (d, g, a, r) in enumerate(rules):
    y = 70 + i * 66
    sr_deep1.text(14, y + 34, d, anchor="start", size=17)
    for k, c in enumerate([g, a, r]):
        sr_deep1.box(150 + k * 202, y, 194, 54, c, "paper", size=13, rx=5)
sr_deep1.note(380, 290, "overall = the worst of the lines", "pen", size=17)

sr_deep2 = Doodle(760, 240, "A simple forecast. 49 must-haves done on 27 March, 22 to go, four weeks to go or no-go. The last three weeks averaged four a week. At that rate 16 more will be done, 65 of 71: six short. To finish, the rate must rise to five and a half a week, or scope must shrink. The forecast is a sum, shown with its assumption.",
                  "Remaining ÷ rate = weeks needed. 22 left at 4 a week is 5½ weeks. There are 4.")
sr_deep2.row([("22 left", "71 − 49", "y"), ("4 a week", "average of last 3 weeks", "blue"), ("5½ weeks needed", "there are 4", "pink")], y=40, h=96, gap=40, size=20, subsize=14, arrows=True)
sr_deep2.note(380, 184, "at this rate: 65 of 71 by go / no-go", "red", size=19)
sr_deep2.note(380, 220, "to finish: 5½ a week, or fewer must-haves", "pen", size=18)

STATUS = dict(
    slug="status-reports",
    kicker="a.k.a. “monitoring and controlling project performance”",
    tldr="A status report answers four questions: <b>where are we</b> against the baseline, <b>where will we end up</b> if nothing changes (the forecast), <b>what are we doing about it</b>, and <b>what do we need from you</b>. Colours follow <b>written rules</b>, so two people with the same numbers pick the same colour. A report that collects numbers and changes nothing is monitoring without controlling: <b>every variance ends in a decision</b>, even if the decision is “accept it”.",
    chips=[("Family", "running and steering"), ("Lives in", "one page every Friday; the steering group every second Friday"), ("Pairs with", "baselines, own the outcome, escalation")],
    pmbok=dict(covers="measuring performance against the baseline, forecasting, reporting, and deciding on corrective action", domains=GOV + ["schedule", "finance", "scope"],
               processes=["Monitor and Control Project Performance"], principles=["Be an accountable leader", "Focus on value"], focus=["monitoring"],
               older="6th: “Monitor and Control Project Work” (4.5); work performance data → information → reports. 7th: the Measurement domain."),
    problem_side="Larder, 27 March 2026",
    problem="""  <p class="lead">One month to opening. Sanne's Friday page has seven lines and seven colours, and people have come to trust it. Then Marco asks: <b>“why is schedule amber and not red? Would you have called it amber last week?”</b> She starts to answer and stops. <span class="hl-pink">The colours are her judgment on the day. There is no rule behind any of them</span>, no line showing whether things are improving, and no statement of where the project will end up.</p>
  <ul>
    <li>A colour without a rule can't be checked or compared.</li>
    <li>The page shows today, not the direction.</li>
    <li>It says how things are, not what will happen or what to do.</li>
  </ul>""",
    problem_figs=[sr_problem],
    analogy_side="the sat-nav",
    analogy="""  <p>A <b>sat-nav</b> shows three things: <b>where you are</b> on the planned route, <b>how far is left</b>, and <b>when you'll arrive</b>, recalculated as you drive. When traffic builds it tells you at once and offers another route. It never says “making good progress”, and it never waits until you've missed the ferry to mention the jam.</p>""",
    analogy_figs=[sr_analogy],
    map=[("The planned route", "Baseline v1"),
         ("The dot on the map", "49 must-haves done; fit-out forecast; €355.5k committed"),
         ("Arrival time", "The forecast: 65 of 71 by go / no-go at the current rate"),
         ("“Traffic ahead: new route?”", "Corrective action, or a decision for the steering group"),
         ("“Making good progress”", "A green that is really a mood")],
    how_side="position, forecast, action, ask — and colours with rules",
    how="""  <p>For the steering group of <b>27 March</b> Sanne rebuilds the page. <b>Position</b>: a small chart of must-haves done against the plan line (49; the plan said 52), the milestones against baseline, money committed (€355.5k of €380k). <b>Forecast</b>: at the recent rate of four a week, 65 of 71 by go / no-go. <b>Action</b>: Ben and Eli pair on the six blocked items; nothing new enters the launch list after 3 April. <b>Ask</b>: two decisions. And each colour now follows a <b>written rule</b> (under “going deeper”). By those rules the overall status is amber. Marco reads the rules twice and says: “so next week I can check you.”</p>""",
    how_figs=[sr_how],
    steps=[("Measure against the baseline", "Done, dates, money."),
           ("Show the trend", "This week against the last few."),
           ("Forecast the end", "At the current rate, where do we land?"),
           ("Apply the colour rules", "Don't choose the colour; derive it."),
           ("Say what you are doing", "For each variance."),
           ("Say what you need, from whom, by when", "Or say plainly that you need nothing.")],
    vocab=[("Monitoring", "Collecting and comparing: where are we against the plan?"),
           ("Controlling", "Deciding and acting on what monitoring shows."),
           ("Variance", "The gap between baseline and actual."),
           ("Forecast", "Where the project will end up if the current trend continues."),
           ("Trend", "The direction over several periods."),
           ("RAG status", "Red, amber, green: a summary colour, useful only with rules."),
           ("Corrective action", "A step taken to bring performance back to the plan.")],
    code=dict(file="rotterdam/10-status-2026-03-27.md", note="to the steering group · Friday 27 March 2026 · 4½ weeks to opening", plain=True, src="""
# ROTTERDAM · STATUS · 27 March 2026 · measured against baseline v1

OVERALL  AMBER (worst line: scope)           last time: AMBER · trend: steady

             BASELINE         NOW                  FORECAST            COLOUR (rule)
SCOPE        52 of 71 by now  49 done · 6 blocked  65 by 24 Apr at     AMBER (3–8 behind
                                                   4 a week            → amber at 4+)
SCHEDULE     G1 3 Apr         builder said 8 Apr   3 Apr (weekend      GREEN (on baseline
                              on 23 Mar            work, C-02)         after C-02)
FINANCE      €380k            €355.5k committed    €379k               AMBER (reserve in
                              reserve €1k                              use)
GOVERNANCE   ok · STAKEHOLDERS ok (neighbours told 2 Mar) · RESOURCES ok (15 pickers
start Mon) · RISK amber (I-07 internet line: workaround agreed)

DOING        Ben + Eli pair on the 6 blocked must-haves until Thu 2 Apr
             nothing new on the launch list after 3 Apr
NEEDED       1 steering: confirm at the session on 31 Mar that approvals in Rotterdam
               move from launch to June (frees ~1 week of Ben's team)
             2 Joost: Sunday rota decision by 3 Apr
TURNS RED IF fewer than 55 must-haves done on 10 Apr, or G1 slips past 7 Apr
"""),
    tools="tools: the baseline, the board's weekly counts, a ruler for the trend line, and written colour rules.",
    deep_dive=dict(
        side="colour rules, forecasting, and the watermelon",
        intro="Most status reports fail in the same three ways: the colour is an opinion, there is no forecast, and nothing happens as a result. This chapter gives a working fix for each, using Rotterdam's real numbers, and ends with how to spot a report that is green on the outside and red inside.",
        parts=[
            ("Write the colour rules down", """  <p>A colour is a summary. It is only useful if <b>two people with the same numbers would choose the same one</b>. So write the rule for each line once, agree it with the steering group, and from then on <b>derive</b> the colour.</p>
  <p>Good rules have three properties. They use <b>numbers from the baseline</b> (days, must-haves, euros). They are <b>tied to authority</b>: Rotterdam's red line for schedule is “more than three days late”, the same three days that send a decision to the sponsor. And they say what <b>amber</b> means, which is usually “off the baseline, with a recovery plan we believe”.</p>
  <p>The overall colour is the <b>worst line</b>, not an average. One red domain can sink a project that is green in the other six.</p>""", [sr_deep1]),
            ("Forecast: where will we land?", """  <p>Position tells you about the past. The steering group cares about the end. The simplest honest forecast needs two numbers: <b>how much is left</b> and <b>how fast you are really going</b>.</p>
  <p>On 27 March: 71 − 49 = <b>22 left</b>. The last three weeks finished 7, 4 and 4, and the pace has settled at about <b>4 a week</b>. 22 ÷ 4 = <b>5½ weeks</b>. There are 4 before go / no-go. So at this rate Rotterdam reaches <b>65 of 71</b>, six short.</p>
  <p>That sum does three useful things. It turns “a bit behind” into a number. It shows the size of the fix: the rate must reach 5½ a week, or six must-haves must leave the list. And it can be <b>checked next week</b>: did the rate rise? (It did: moving approvals to June freed Ben's team, and the next three weeks finished 6, 5 and 9.)</p>
  <p>Always state the assumption (“at the average of the last three weeks”). Vol. 4 does the same sum for money, where it is called earned value.</p>""", [sr_deep2]),
            ("Monitoring without controlling", """  <p>A report that measures and then stops is only half the process. For every line that is off the baseline, one of four things must be written:</p>
  <ul>
    <li><b>Correct it</b>: an action that brings it back (pairing on the blocked items).</li>
    <li><b>Prevent it</b>: an action so it doesn't get worse (nothing new after 3 April).</li>
    <li><b>Change the baseline</b>: through change control, because the promise itself should move (approvals to June).</li>
    <li><b>Accept it</b>: say so, with the reason and who agreed.</li>
  </ul>
  <p>If none of the four is written, nobody is controlling anything.</p>""", []),
            ("Spotting a watermelon", """  <p>A <b>watermelon</b> report is green outside and red inside. Five signs, from the reader's side:</p>
  <ul>
    <li>Colours with <b>no numbers</b> next to them.</li>
    <li><b>No trend</b>: you can't tell if this week is better or worse.</li>
    <li>Progress as a <b>percentage of effort</b> (“80 % done”), not finished things.</li>
    <li>Green for weeks, then <b>red with no amber</b> in between.</li>
    <li><b>No “needed from you”</b>, ever. Real projects need decisions.</li>
  </ul>
  <p>And one from the writer's side: if you would be <b>uncomfortable seeing the reader check it</b>, it isn't finished.</p>""", []),
        ]),
    dial=[("Light", "a small team", ["Say it weekly: done, left, will we make it, what I need.", "No colours.", "Five minutes."]),
          ("Standard", "Rotterdam", ["One page against the baseline.", "A trend chart and a simple forecast.", "Colour rules, actions and asks."]),
          ("Heavy", "large or contracted work", ["Earned value and schedule analysis.", "Formal variance thresholds and reports.", "Independent assurance of the numbers."])],
    baseline="Each line compares <b>a weekly page of colours chosen by judgment</b> to <b>position against the baseline, a forecast, rule-based colours, actions and asks</b>.",
    ratings=[(3, 4, "The forecast is about the benefit's must-haves."),
             (2, 5, "A forecast, checked every week."),
             (2, 4, "“Turns red if” fires before it's too late."),
             (3, 5, "Anyone can check the colour."),
             (3, 5, "Marco can check Sanne."),
             (3, 3, "Neutral."),
             (3, 4, "Each variance gets one of four answers."),
             (3, 3, "Neutral."),
             (4, 3, "An hour a week to prepare.")],
    pitfalls=[("Colours by mood", "Can't be checked.", "written rules."),
              ("No forecast", "“Slightly behind” for weeks.", "left ÷ rate, with the assumption."),
              ("Monitoring only", "Numbers, no decisions.", "correct, prevent, change or accept."),
              ("Averaging", "Six greens hide one red.", "overall = the worst line.")],
    use=["Every week once there is a baseline.", "Before every steering group.", "When someone asks “are we on track?”", "When a status has been the same colour for a month."],
    skip=["Never the questions. The page can shrink to four sentences."],
    related=["<b>What Exactly Did We Promise?</b> (this volume)", "<b>Own the Outcome</b> (vol. 1)", "<b>Product update that gets read</b> (Grace, vol. 5)", "<b>Earned value</b> (vol. 4)"],
    quiz=[("What four questions does a status answer?", "Where are we, where will we end up, what are we doing, what do we need."),
          ("Monitoring or controlling: deciding to pair Ben and Eli?", "Controlling."),
          ("22 must-haves left, 4 finished a week. How long?", "5½ weeks."),
          ("Six lines are green and one is red. What is the overall colour?", "Red: the worst line."),
          ("On 10 April, 60 must-haves are done and 11 remain, with two weeks to go / no-go. The last three weeks finished 4, 6 and 5. What does Sanne report?", "A rate of about 5 a week: 11 need just over two weeks, and there are two. Forecast: 69 or 70 by 24 April. Amber by the scope rule, with the two at-risk must-haves named and the assumption stated. (On 24 April it was 69.)")],
    try_it="Take your last status report. For each colour, write the rule that would make someone else choose the same colour from the same numbers. Then add one sum: what's left ÷ your real rate. Does the answer fit in the time you have?",
    remember="Where we are, where we'll <span class=\"hl\">land</span>, what we're doing, what we <span class=\"hl\">need</span>.",
    sources=["Project Management Institute, <i>PMBOK Guide</i>, Eighth Edition (2025): Governance domain, monitoring and controlling performance.",
             "Project Management Institute, <i>PMBOK Guide</i>, Sixth Edition (2017): 4.5 Monitor and Control Project Work.",
             "Edward Tufte, <i>The Visual Display of Quantitative Information</i> (2nd ed., 2001).",
             "Mike Cohn, <i>Agile Estimating and Planning</i> (2005): burn-up charts and velocity."],
)

# ------------------------------------------------------------------ 11 Can We Change That?
cc_problem = Doodle(760, 250, "Doodle of the end of March 2026. In one week Sanne is asked for five things. Priya would like an in-store launch event. Joost wants a second cold-room door. Tomás wants the opening hours looked at again. Ben wants approvals moved out of the Rotterdam launch. Marco wants to know why the reserve keeps shrinking. Each request is reasonable. Said yes to in the corridor, together they would sink the date.",
                    "Five reasonable requests in one week. Agreed in the corridor, they would sink the date.")
for i, (t, w) in enumerate([("launch event", "Priya"), ("cold-room door", "Joost"), ("opening hours", "Tomás"), ("approvals later", "Ben")]):
    cc_problem.box(14 + i * 186, 30, 172, 76, t, "paper", sub=w, size=14, subsize=14)
cc_problem.box(230, 130, 300, 56, "baseline v1", "y", size=19)
for x in (100, 286, 472, 658):
    cc_problem.arrow(x, 106, 380 + (x - 380) * 0.3, 128, color="red")
cc_problem.note(380, 226, "“it's only a small change”", "red", size=20)

cc_analogy = Doodle(760, 240, "Doodle of a building site. The client walks through and says: could that wall move half a metre? The builder doesn't pick up a hammer. The builder writes a variation: what it changes, what it costs, how many days it adds. The client signs or doesn't. Only then does the wall move, and the drawings are updated.",
                    "On a building site a moved wall starts with a signed variation: what, how much, how many days.")
cc_analogy.row([("ask", "“move that wall?”", "paper"), ("size it", "cost · days", "y"), ("decide", "the client signs", "pink"), ("do it", "update drawings", "green")], y=50, h=90, gap=34, size=18, subsize=12, arrows=True)
cc_analogy.note(380, 200, "no hammer before the signature", "pen", size=20)

cc_how = Doodle(760, 400, "Rotterdam's change log on 31 March 2026. Change 1: fridges with doors, plus 14 thousand euros, approved by Marco on 2 February. Change 2: weekend work by the builder, plus 5 thousand euros, approved by Joost on 23 March. Change 3: substitution approvals move from the Rotterdam launch to June, approved by the steering group on 31 March. Change 4: a 4G router, 600 euros, approved by Sanne. Change 5: an in-store launch event, rejected. Change 6: a second cold-room door, deferred to after opening. Each row shows who decided, by the thresholds, and that the baseline is now version 2.",
                "One log. Every change sized, decided at the right level, and built into the plan, or refused with a reason.")
rowsC = [("C-01 fridges with doors", "+€14k", "Marco", "approved", "green"), ("C-02 builder weekend work", "+€5k", "Joost", "approved", "green"),
         ("C-03 approvals → June", "scope", "steering", "approved", "green"), ("C-04 4G router", "+€0.6k", "Sanne", "approved", "green"),
         ("C-05 in-store launch event", "+€8k", "Joost", "rejected", "pink"), ("C-06 2nd cold-room door", "+€6k · 4 days", "Joost", "after opening", "y")]
for i, (t, imp, who, res, f) in enumerate(rowsC):
    y = 14 + i * 54
    cc_how.box(14, y, 290, 44, t, "paper", size=14, rx=5)
    cc_how.box(312, y, 150, 44, imp, "paper", size=13, rx=5)
    cc_how.box(470, y, 110, 44, who, "blue", size=14, rx=5)
    cc_how.box(588, y, 158, 44, res, f, size=14, rx=5)
cc_how.note(380, 362, "after C-03: baseline v2 · 31 March", "pen", size=18)
cc_how.note(380, 390, "change · impact · who decides · result", size=14)

cc_deep1 = Doodle(760, 250, "The path of one change request in five steps: raise it in writing, size its impact on all seven domains, route it to the right decider by the thresholds, decide to approve, reject or defer, and implement by updating the plan, the baseline and the people affected. An arrow from decide loops back to raise, labelled: or come back with a smaller version.",
                  "Five steps: raise, size, route, decide, implement. The plan changes only at step five.")
cc_deep1.row([("1 raise", "in writing", "paper"), ("2 size", "all 7 domains", "y"), ("3 route", "by threshold", "blue"), ("4 decide", "yes · no · later", "pink"), ("5 do it", "plan + people", "green")], y=40, h=90, gap=34, size=16, subsize=12, arrows=True)
cc_deep1.arrow(570, 132, 80, 132, curve=(325, 200), label="or come back smaller", lx=325, ly=196)

cc_deep2 = Doodle(760, 300, "The impact of change C-03, moving substitution approvals in Rotterdam from launch to June, checked against the seven domains. Scope: one should removed from the launch. Schedule: about a week of Ben's team freed; forecast for the must-haves improves. Finance: no cost. Stakeholders: Joost and the store team must be told again; customers in Rotterdam get approvals six weeks later. Resources: Ben's team available for blocked items. Risk: fewer new things on opening day. Governance: scope change, so the steering group decides.",
                  "One change, seven questions. C-03 costs nothing in money and one hard conversation.")
imp = [("scope", "one Should leaves the launch"), ("schedule", "≈ 1 week of Ben's team freed"), ("finance", "no cost"), ("stakeholders", "store team told again; customers wait 6 weeks"),
       ("resources", "Ben's team on the blocked must-haves"), ("risk", "less that is new on opening day"), ("governance", "launch scope → steering group decides")]
for i, (d, t) in enumerate(imp):
    y = 12 + i * 40
    cc_deep2.box(14, y, 170, 32, d, "blue", size=15, rx=5)
    cc_deep2.text(200, y + 22, t, anchor="start", size=15)

CHANGE = dict(
    slug="change-control",
    kicker="a.k.a. “assessing and implementing changes” (integrated change control)",
    tldr="Change is normal. <b>Uncontrolled</b> change is what sinks projects. Change control is a short path every change to the baseline takes: <b>write it down</b>, <b>size its effect</b> on everything (not just the part it touches), have <b>the right person decide</b>, and only then <b>build it into the plan</b> and tell everyone affected. It isn't there to say no. It makes sure every yes is given with the cost in view, and that there is <b>one current version of the promise</b>.",
    chips=[("Family", "running and steering"), ("Lives in", "one change log; the baseline's version number"), ("Pairs with", "baselines, trade-off sliders, saying no")],
    pmbok=dict(covers="assessing change requests against the whole project, deciding at the right level, implementing approved changes", domains=GOV + ["scope"],
               processes=["Assess and Implement Changes"], principles=["Adopt a holistic view", "Focus on value"], focus=["monitoring"],
               older="6th: “Perform Integrated Change Control” (4.6), the change control board, the change log. 7th: change under the Project Work and Delivery domains."),
    problem_side="Larder, 23–31 March 2026",
    problem="""  <p class="lead">In the last week of March five requests reach Sanne. Priya: an <b>in-store launch event</b>. Joost: a <b>second cold-room door</b>. Tomás: the <b>opening hours</b>, again. Ben: move <b>substitution approvals</b> out of the Rotterdam launch. And Marco, who has noticed the reserve go from €20k to €1k: <b>“who agreed to all this?”</b> <span class="hl-pink">Each request is reasonable. Each asker says it's small.</span> And two changes are already in the plan with nothing to show who approved them.</p>
  <ul>
    <li>Changes agreed in corridors leave no trace.</li>
    <li>Each is sized by the person asking, for their part only.</li>
    <li>Nobody can say which version of the promise is current.</li>
  </ul>""",
    problem_figs=[cc_problem],
    meanwhile=[("architect-2", "trade-off-sliders", "on 31 March the Rotterdam sliders put the launch date first and feature scope fourth: approvals go to Amsterdam first, Rotterdam in June.",
                "that session is where Sanne's change C-03 is decided; the sliders are the steering group's reasoning, the change log is the record.")],
    analogy_side="the variation on a building site",
    analogy="""  <p>A client walks through a half-built house: “could that wall move half a metre?” A good builder doesn't pick up a hammer. They write a <b>variation</b>: what moves, what else it affects (the wiring, the window), what it costs, how many days. The client <b>signs</b>, or doesn't. Only then does the wall move, and the <b>drawings are updated</b>, so the electrician isn't working from the old ones.</p>""",
    analogy_figs=[cc_analogy],
    map=[("“Could that wall move?”", "“Could we add a launch event?”"),
         ("The variation", "A change request: one paragraph"),
         ("Wiring and window", "The effect on the other six domains"),
         ("The client signs", "Sanne, Joost or the steering group, by the thresholds"),
         ("Updating the drawings", "Baseline v2, and telling the store team")],
    how_side="one log, one path, the thresholds you already have",
    how="""  <p>Sanne starts a <b>change log</b> and first enters the two changes already made (the fridges, the builder's weekend work), with who approved them. Marco has his answer. Then each new request takes the same short path: a paragraph, the <b>impact on all seven domains</b>, and the decider set by the thresholds from February. The 4G router (€600): hers. The cold-room door (€6k, four days): Joost, who <b>defers</b> it to after opening. The launch event (€8k, three workstreams): Joost <b>rejects</b> it, with a reason. And <b>approvals in Rotterdam</b>: a change to what customers get, so it goes to the steering group, which decides on <b>31 March</b>: Amsterdam first, Rotterdam in June. The baseline becomes <b>v2</b>, and this time Joost hears it once, in writing, from the right source.</p>""",
    how_figs=[cc_how],
    steps=[("Write the request down", "One paragraph: what and why."),
           ("Size it against everything", "Scope, dates, money, people, risk, stakeholders."),
           ("Send it to the right decider", "By the thresholds."),
           ("Decide: approve, reject or defer", "With the reason."),
           ("Build approved changes into the plan and baseline", "New version, dated."),
           ("Tell everyone affected", "Including those who asked for something else.")],
    vocab=[("Change request", "A formal proposal to change the baseline: scope, schedule, cost or how the project is run."),
           ("Impact assessment", "Working out what a change would do to every part of the project."),
           ("Change log", "The record of every request and its outcome."),
           ("Change control board", "The group that decides larger changes; here, the steering group."),
           ("Scope creep", "Scope growing through small unapproved additions."),
           ("Re-baseline", "Issuing a new approved baseline after a change.")],
    code=dict(file="rotterdam/11-change-log.md", note="as of 1 April 2026 · baseline v2", plain=True, src="""
# ROTTERDAM · CHANGE LOG

ID    DATE    CHANGE                         IMPACT                  DECIDED BY   RESULT
C-01   2 Feb  fridges with doors             +€14k; reserve 20 → 6   Marco        approved
C-02  23 Mar  builder works 28–29 March     +€5k; reserve 6 → 1     Joost        approved
              to hold G1 on 3 Apr            G1 back on 3 Apr
C-03  31 Mar  substitution approvals in      scope: one Should out   steering     approved
              Rotterdam: launch → June       frees ~1 week (Ben)     group        → baseline v2
                                             customers wait 6 weeks
C-04   1 Apr  4G router + backup SIM         +€0.6k; reserve 1 → 0.4 Sanne        approved
              (workaround for I-07)
C-05  26 Mar  in-store launch event          +€8k; touches people,   Joost        REJECTED: no link
                                             marketing, stock                     to the benefit;
                                                                                  no reserve
C-06  27 Mar  second cold-room door          +€6k; +4 days on G1     Joost        DEFERRED to
                                                                                  after opening

BASELINE v2 (31 Mar)  scope: approvals in Rotterdam planned for June (was: a Should for 27 Apr)
                      schedule: unchanged · cost: €380k, reserve €0.4k
TOLD                  store team (Joost, in writing, 1 Apr) · support (Sam) · marketing (Priya)
"""),
    tools="tools: one log, a seven-line impact check, the thresholds from the governance page.",
    deep_dive=dict(
        side="the path of a change, the impact check, and saying no well",
        intro="Change control has a reputation as bureaucracy, earned by processes that are slow and built to refuse. This chapter shows the light version that works: the five steps, the seven-question impact check on a real change, the three possible answers, and what to do about changes that have already happened.",
        parts=[
            ("Five steps, and where they usually break", """  <p>Every change goes through the same five steps. Most trouble comes from skipping the second or the fifth.</p>
  <ol class="steps">
    <li><b>Raise.</b><p>In writing, one paragraph. Anyone may raise one. Writing it down is what stops the corridor yes.</p></li>
    <li><b>Size.</b><p>The effect on the whole project, not only on the asker's part. This is the step corridor decisions skip.</p></li>
    <li><b>Route.</b><p>The thresholds decide who decides. Small changes stay with the project manager and take minutes.</p></li>
    <li><b>Decide.</b><p>Approve, reject or defer. Each with a reason, written in the log.</p></li>
    <li><b>Implement.</b><p>Update the plan and the baseline; tell everyone affected. A change approved but not communicated is how the electrician ends up with old drawings.</p></li>
  </ol>""", [cc_deep1]),
            ("The seven-question impact check", """  <p>To size a change, walk it through the <b>seven domains</b> (the weekly scan from Vol. 1, used on one change). For <b>C-03</b>, moving approvals in Rotterdam from launch to June:</p>
  <p>In money it is free. Its real cost is in <b>stakeholders</b>: the store team was once told (wrongly, by Sanne) that approvals would be there at launch, then told it was a Should, and now must be told June. That conversation is the price, and it is written into the change so it actually happens.</p>
  <p>Its benefit shows in <b>schedule</b> and <b>risk</b>: a week of Ben's team for the blocked must-haves, and one less new thing on opening day. With the date ranked first on the sliders, the steering group took four minutes.</p>""", [cc_deep2]),
            ("Three answers, not two", """  <ul>
    <li><b>Approve.</b> Build it in; issue a new baseline if scope, a milestone or the budget moved.</li>
    <li><b>Reject.</b> With the reason, in the log. C-05, the launch event: €8k with €1k of reserve, three workstreams touched, and no arrow to any benefit on the benefits map. Priya didn't enjoy the answer, but she could see it wasn't personal: the same test had parked the tote bags in January.</li>
    <li><b>Defer.</b> A real third option, with a date. C-06, the second cold-room door: a good idea that costs four days on a milestone with none to spare. “After opening” is logged and handed over at closing, so it isn't lost.</li>
  </ul>
  <p>A rejected or deferred requester can always <b>come back with a smaller version</b>. That is the process working.</p>""", []),
            ("Changes that already happened", """  <p>Two of Rotterdam's changes were made before there was a log. That is common, and the fix is simple: <b>log them afterwards</b>, with who approved them and when. The log isn't a court. Its job is to make the current promise traceable: the reserve went from €20k to €0.4k through four named decisions, each by the person entitled to make it.</p>
  <p>What may not be done afterwards is the <b>decision</b> itself. If a change turns out to have been made by someone without the authority, it goes to the right person now, as an open question, even if the work is done.</p>
  <p>On adaptive work the same idea is lighter still: re-ordering a backlog inside a sprint isn't a change request. Moving a <b>shared milestone</b> or the <b>launch scope</b> is. The boundary is the baseline.</p>""", []),
        ]),
    dial=[("Light", "one team, adaptive work", ["The product owner re-orders the backlog.", "Only changes to the goal or the date are discussed.", "A note in the log."]),
          ("Standard", "Rotterdam", ["One change log.", "A seven-line impact check.", "Thresholds decide who decides; baseline versions."]),
          ("Heavy", "contracts, regulated work", ["Formal change requests and a change control board.", "Contract variations with price and time.", "Configuration management of every document."])],
    baseline="Each line compares <b>changes agreed in corridors</b> to <b>one log, an impact check on the whole, a decider by threshold and a versioned baseline</b>.",
    ratings=[(3, 5, "Every change is tested against the benefit."),
             (2, 4, "The baseline moves only on purpose."),
             (2, 4, "Knock-on effects are found before the yes."),
             (2, 5, "One current version of the promise."),
             (2, 5, "Marco can see who agreed to what."),
             (3, 3, "Neutral: teams keep changes inside their own work."),
             (3, 4, "Good changes get a fast, clear yes."),
             (3, 4, "Late additions are stopped before they cause faults."),
             (4, 3, "A paragraph and a check per change.")],
    pitfalls=[("The corridor yes", "No trace, no sizing.", "write it down first."),
              ("Sized by the asker", "“It's small.”", "walk it through all seven domains."),
              ("A process built to refuse", "People go round it.", "small changes decided in minutes at a low level."),
              ("Approved, not communicated", "Half the team works to the old plan.", "telling people is step five.")],
    use=["From the day there is a baseline.", "Whenever someone says “it's only a small change”.", "When the reserve shrinks and nobody knows why.", "When two people hold different versions of the plan."],
    skip=["Changes inside a team's own work that touch no milestone, money or promise."],
    related=["<b>What Exactly Did We Promise?</b> (this volume)", "<b>Trade-off sliders</b> (Ana, vol. 2)", "<b>Saying no without burning bridges</b> (Grace, vol. 2)", "<b>Negotiating scope</b> (Grace, vol. 5)"],
    quiz=[("Name the five steps.", "Raise, size, route, decide, implement."),
          ("What are the three possible decisions?", "Approve, reject, defer."),
          ("Who decided C-03, and why that level?", "The steering group: it changed what customers get at launch."),
          ("Dee re-orders two tasks in her sprint. Change request?", "No. It touches no milestone, money or promise."),
          ("On 14 April Joost phones the builder directly and orders the second cold-room door. What does Sanne do?", "Log it as a change made, size the impact now (it threatens stocking and Gate 2), and bring it to Joost as an open decision the same day: he has the authority, but he needs the cost in front of him.")],
    try_it="List every change made to your project's scope, dates or budget in the last month. For each, write who approved it. Any blanks? Then write the thresholds: what can you approve alone, and what goes up?",
    remember="No <span class=\"hl\">hammer</span> before the <span class=\"hl\">signature</span>. Then update the drawings.",
    sources=["Project Management Institute, <i>PMBOK Guide</i>, Eighth Edition (2025): Governance domain, assessing and implementing changes.",
             "Project Management Institute, <i>PMBOK Guide</i>, Sixth Edition (2017): 4.6 Perform Integrated Change Control.",
             "Project Management Institute, <i>Practice Standard for Project Configuration Management</i> (2007)."],
)

# ------------------------------------------------------------------ 12 When Do I Take It Upstairs?
es_problem = Doodle(760, 250, "Doodle of Monday 23 March 2026. The builder phones: the electrical inspection has been re-booked, and handover will be 8 April, not 3 April. Five days late. Sanne's first instinct is to fix it herself and tell Joost on Friday, with a solution. Five days is over the three-day line. Each day she waits is a day the weekend crews can't be booked.",
                    "Five days late, on a three-day threshold. The instinct: fix it first, tell the sponsor on Friday.")
es_problem.box(20, 40, 320, 100, "builder: “8 April”", "pink", sub="baseline: 3 April · 5 days late", size=20, subsize=15)
es_problem.box(420, 40, 320, 100, "Sanne's instinct", "paper", sub="“I'll sort it, then tell Joost”", size=20, subsize=15)
es_problem.note(380, 186, "threshold: date at risk by more than 3 days", "red", size=19)
es_problem.note(380, 222, "every day of waiting removes an option", "pen", size=18)

es_analogy = Doodle(760, 240, "Doodle of a nurse on a night ward. A patient's temperature passes a set number. The nurse doesn't wait for morning or try a few more things first. The nurse phones the doctor now, and says four things: who the patient is, what has changed, what the nurse thinks is going on, and what the nurse recommends.",
                    "A nurse phones the doctor when the number is passed: what's happening, what I think, what I recommend.")
es_analogy.row([("situation", "what has changed", "paper"), ("impact", "what it means", "y"), ("options", "two or three", "blue"), ("recommendation", "what I'd do", "green")], y=50, h=90, size=16, subsize=13)
es_analogy.note(380, 200, "now, not at the morning round", "pen", size=20)

es_how = Doodle(760, 400, "Sanne's escalation to Joost on 23 March 2026, on one screen, sent within two hours of the builder's call. Situation: handover forecast 8 April, five days late, because the electrical inspection was re-booked. Impact: stocking shrinks from ten working days to seven; Gate 2 at risk. Three options. A: accept, squeeze stocking, no cost, high risk. B: weekend work on the weekend of 28–29 March, five thousand euros, handover back on 3 April. C: partial handover, cold room first, no cost, medium risk. Recommendation: B. Decision needed by Tuesday noon. Joost decides B at four o'clock the same day.",
                "Situation, impact, options, recommendation, deadline. On one screen, the same day.")
es_how.box(14, 14, 360, 96, "situation", "paper", sub="handover 8 Apr, not 3 Apr (5 days)", size=18, subsize=14)
es_how.box(386, 14, 360, 96, "impact", "y", sub="stocking: 10 days → 7 · Gate 2 at risk", size=18, subsize=14)
opts = [("A accept", "squeeze stocking · €0", "high risk", "paper"), ("B weekend work", "28–29 Mar · €5k", "back on 3 Apr", "green"), ("C partial handover", "cold room first · €0", "medium risk", "paper")]
for i, (t, s, r, f) in enumerate(opts):
    es_how.box(14 + i * 248, 130, 236, 100, t, f, sub=s, size=17, subsize=13)
    es_how.note(132 + i * 248, 252, r, "pen", size=15)
es_how.box(14, 280, 480, 80, "recommendation: B", "green", sub="reserve covers it: €6k → €1k", size=19, subsize=14)
es_how.box(506, 280, 240, 80, "decide by", "pink", sub="Tuesday 12:00", size=18, subsize=15)
es_how.note(380, 388, "Joost: B, at 16:00 the same day", "green", size=17)

ESCALATION = dict(
    slug="escalation",
    kicker="a.k.a. “escalation”",
    tldr="To <b>escalate</b> is to pass a decision up because it is <b>above your authority</b>, or because you can't resolve it at your level. It is part of the job, not a failure: the thresholds exist so the right person decides. Do it <b>early</b>, while options are still open, and do it <b>well</b>: the situation, what it means, two or three options, <b>your recommendation</b>, and when you need an answer.",
    chips=[("Family", "running and steering"), ("Lives in", "the governance page (when); one message (how)"), ("Pairs with", "who decides what, status reports, delivering bad news")],
    pmbok=dict(covers="escalating decisions and issues beyond the project manager's authority; corrective action with the sponsor", domains=GOV,
               processes=["Monitor and Control Project Performance"], principles=["Be an accountable leader"], focus=["monitoring"],
               older="6th: escalation paths in the project management plan; a risk response strategy (“escalate”) since the 6th. 7th: escalation under governance."),
    problem_side="Larder, 23 March 2026",
    problem="""  <p class="lead">Monday morning the builder phones. The electrical inspection has been re-booked; handover will be <b>8 April, not 3 April</b>. Five days. Sanne's first instinct is to fix it herself and bring Joost a solved problem on Friday. <span class="hl-pink">Five days is past the three-day line she herself agreed.</span> And the one fix that works, weekend crews, has to be booked by Tuesday.</p>
  <ul>
    <li>Escalating feels like admitting failure.</li>
    <li>Waiting for a solution burns the days that options need.</li>
    <li>The decision involves €5k that isn't hers to spend.</li>
  </ul>""",
    problem_figs=[es_problem],
    analogy_side="the night nurse",
    analogy="""  <p>On a hospital ward at night, a patient's temperature passes a set number. The <b>nurse phones the doctor now</b>, not at the morning round, and not after trying three more things. And the nurse doesn't just say “come quickly”. The call has a shape: <b>what is happening, what I think it means, what I'd recommend</b>. The doctor decides in a minute, because the thinking has been done.</p>""",
    analogy_figs=[es_analogy],
    map=[("The set number", "The thresholds: 3 days, €5,000, launch scope"),
         ("Phoning now", "Two hours after the builder's call"),
         ("“What I think it means”", "Stocking squeezed from ten days to seven; Gate 2 at risk"),
         ("“What I'd recommend”", "Option B: weekend work, €5k"),
         ("The doctor decides in a minute", "Joost decides at 16:00")],
    how_side="early, on one screen: situation, impact, options, recommendation, deadline",
    how="""  <p>Sanne takes ninety minutes to do three things: confirm the builder's date in writing, ask Tomás what seven stocking days would mean, and get a price for weekend work. Then one message to Joost: <b>situation</b> (8 April, five days late, the cause), <b>impact</b> (stocking shrinks from ten working days to seven; Gate 2 at risk), <b>three options</b> with cost and risk, her <b>recommendation</b> (B: work on the weekend of 28–29 March, €5k, handover back on 3 April; the reserve covers it and falls to €1k) and a <b>deadline</b> (Tuesday noon, to book the crews). Joost phones Marco and decides B at 16:00. It goes in the issue log as I-09 and the change log as C-02. The fit-out is handed over on 3 April.</p>""",
    how_figs=[es_how],
    steps=[("Know your thresholds before you need them", "Days, money, scope."),
           ("When one is crossed, escalate the same day", "Not after you've tried to fix it."),
           ("Check the facts quickly", "An hour or two, not a week."),
           ("Bring options, not just the problem", "Two or three, with cost and risk."),
           ("Recommend one", "It's your project; say what you'd do."),
           ("Say when you need the answer, then record the decision", "In the issue and change logs.")],
    vocab=[("Escalation", "Raising a decision or problem to someone with more authority."),
           ("Threshold", "A limit that, when crossed, requires escalation."),
           ("Tolerance", "How far from the plan the project manager may go before escalating."),
           ("Options paper", "A short comparison of choices with a recommendation."),
           ("Decision deadline", "The latest moment a decision still helps."),
           ("Management by exception", "Leaders are involved only when limits are crossed.")],
    code=dict(file="rotterdam/12-escalation-2026-03-23.md", note="message to Joost, Monday 23 March 2026, 11:40", plain=True, src="""
# ROTTERDAM · DECISION NEEDED BY TUESDAY 12:00 · fit-out 5 days late

SITUATION  The builder now forecasts handover on 8 April, not 3 April. Cause: the
           electrical inspection was re-booked (inspector's side). Confirmed in writing.
IMPACT     Stocking shrinks from 10 working days to 7. Tomás: possible only without
           chilled goods in week 1. Gate 2 (17 Apr) and rehearsal week at risk.
           Late-delivery clause: €1,000 a day is small comfort; we need the days.

OPTIONS                              COST    HANDOVER   RISK
A  accept; squeeze stocking          €0      8 Apr      high: no slack before G2
B  builder works 28–29 March        €5,000  3 Apr      low: crews available if booked
                                                        by Tuesday
C  partial handover: cold room and   €0      3 / 8 Apr  medium: pickers and builders
   dry area first                                       share the store for 3 days

RECOMMEND  B. The reserve covers it (€6k → €1k). It is the only option that keeps
           all ten stocking days. After this, the reserve can't absorb another surprise.
NEED       your decision, and Marco's OK on the spend, by Tuesday 12:00.

Joost, 16:00: B. Marco agrees. → issue I-09 closed · change C-02 approved
"""),
    tools="tools: your thresholds, a phone, ninety minutes of fact-checking and one screen of text.",
    dial=[("Light", "a small team", ["Walk over and say it.", "“Here's what I'd do.”", "A note afterwards."]),
          ("Standard", "Rotterdam", ["Written thresholds.", "A one-screen message: situation, impact, options, recommendation, deadline.", "Recorded in the logs."]),
          ("Heavy", "many levels, contracts", ["Defined tolerances per stage.", "Exception reports to a project board.", "Contractual notice periods and claims."])],
    baseline="Each line compares <b>trying to fix it alone and reporting on Friday</b> to <b>escalating the same day with options and a recommendation</b>.",
    ratings=[(3, 4, "The decision weighs the date against the money openly."),
             (2, 4, "The milestone is recovered."),
             (2, 5, "Options are still open when the decision is made."),
             (3, 5, "The sponsor knows within hours."),
             (3, 5, "Joost trusts that he'll hear early."),
             (3, 3, "Neutral."),
             (3, 4, "A fast decision keeps the plan moving."),
             (3, 3, "Neutral."),
             (4, 4, "One message.")],
    pitfalls=[("Escalating late", "With no options left.", "the same day the threshold is crossed."),
              ("Escalating only the problem", "“The builder is late, what shall I do?”", "options and a recommendation."),
              ("Escalating everything", "The sponsor stops reading.", "only what crosses a threshold."),
              ("No deadline", "The decision arrives after the crews are gone.", "say when you need it.")],
    use=["A threshold is crossed.", "A decision isn't yours to make.", "Two leads can't agree and it affects a milestone.", "An issue hasn't moved in a week."],
    skip=["It is inside your authority: decide, and report it in the status."],
    related=["<b>Who Decides What?</b> (this volume)", "<b>Where Are We, Really?</b> (this volume)", "<b>Delivering bad news</b> (Grace, vol. 5)", "<b>Options analysis</b> (Ana, vol. 2)"],
    quiz=[("When do you escalate?", "When a threshold is crossed or the decision isn't yours, the same day."),
          ("What five things does a good escalation contain?", "Situation, impact, options, recommendation, deadline."),
          ("Is escalating a failure?", "No. It's how the right person gets to decide in time."),
          ("The builder is two days late, with a plan to catch up. Escalate?", "No: inside the three-day tolerance. Report it in the status and watch it."),
          ("Joost doesn't answer by Tuesday 11:00. What does Sanne do?", "Phone him. If he can't be reached, go to the next level on the governance page (Femke) with the same message; the crews must be booked by noon.")],
    try_it="Write down your three thresholds: how many days, how much money and what kind of scope change can you decide alone? If you can't, ask your sponsor today. Then draft, for the most likely problem on your project, the message you'd send.",
    remember="Phone when the <span class=\"hl\">number</span> is passed, with what you'd <span class=\"hl\">recommend</span>.",
    sources=["Project Management Institute, <i>PMBOK Guide</i>, Eighth Edition (2025): Governance domain.",
             "AXELOS, <i>Managing Successful Projects with PRINCE2</i> (2017): tolerances and management by exception.",
             "Institute for Healthcare Improvement: the SBAR communication tool (situation, background, assessment, recommendation).",
             "Barbara Minto, <i>The Pyramid Principle</i> (1987)."],
)

NOTES = [DIRECTING, ISSUES, QA, STATUS, CHANGE, ESCALATION]
