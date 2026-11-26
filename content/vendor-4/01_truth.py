# Series 5 · On the Client's Floor · Vol. 4 · Delivery Under Fire · Telling the truth (notes 1–3).
# Narrator: Ines Duarte (she/her). Facts: docs/lodestar-casebook.md, "Vol. 4".
from datetime import date


def on_site(d):
    return f"day {(d - date(2027, 7, 4)).days} on site"


# ------------------------------------------------------------------ 01 Why Is Everything Green Except the Truth?
wm_problem = Doodle(760, 250, "Doodle of a watermelon: green on the outside, labelled Callum's dashboard, all four squads green. Cut open, red inside: 61 per cent of test cases blocked by environments, rehearsal 1 reconciled only 98.1 per cent of balances, and the burn-up shows the build 2.4 weeks behind.",
                    "Green on the outside: every squad on track. Red inside: blocked tests, a failed rehearsal, 2.4 weeks behind.", exact=True)
wm_problem.circle(170, 125, 100, "green")
wm_problem.circle(170, 125, 80, "pink")
wm_problem.note(170, 240, "the dashboard: all green", "pen", size=17)
for i, t in enumerate(["61 % of tests blocked", "rehearsal 1: 98.1 % reconciled", "burn-up: 2.4 weeks behind"]):
    wm_problem.box(330, 30 + i * 66, 416, 54, t, "pink", size=18)

wm_how = Doodle(760, 330, "The status report rebuilt from measures. Four measures replace four squad opinions: the burn-up against plan in story points; test cases passed out of planned; the last rehearsal's reconciliation percentage; and open severity-1 and -2 defects. Each has a threshold that sets its colour, agreed with Elaine. The overall colour is the worst of the four. On 14 April it is amber, with the numbers in the first line.",
                "Four measures with agreed thresholds. The overall colour is the worst of them.", exact=True)
for i, (h, v, t, fill) in enumerate([("burn-up vs plan", "−2.4 weeks", "amber > 1 wk", "y"), ("tests passed", "39 % of planned", "amber < 70 % · red < 30 %", "y"),
                                     ("rehearsal reconciled", "98.1 %", "red < 99.9 %", "pink"), ("sev 1–2 open", "7", "amber > 5", "y")]):
    wm_how.box(14 + i * 186, 20, 174, 150, h, fill, sub=t, size=17, subsize=13)
    wm_how.text(101 + i * 186, 60, v, cls="t-head", size=22)
wm_how.box(14, 186, 732, 64, "overall: the worst of the four, with the numbers in line one", "paper", size=18)
wm_how.note(380, 300, "squads still say how they feel, underneath the numbers", "pen", size=18)

WATERMELON = dict(
    slug="watermelon-report", date=date(2028, 4, 14), meta=on_site(date(2028, 4, 14)), where="FL 19", pass_kind="contractor",
    kicker="a.k.a. “the watermelon report”: green outside, red inside",
    tldr="A status report built from team opinions turns green on the outside and red inside: each team is “on track” for its own sprint while the programme slips. Build the colour from <b>measures with agreed thresholds</b>: progress against plan, tests passed, rehearsal results, open serious defects. Make the <b>overall colour the worst of them</b>, put the numbers in the first line, and keep the teams' opinions underneath, where they belong.",
    chips=[("Family", "telling the truth"), ("Lives in", "delivery/lodestar/status/ (measures sheet)"), ("Pairs with", "the first status report (vol. 2), re-planning")],
    problem_side="The Grid, April 2028",
    problem="""  <p class="lead">Callum's weekly dashboard on <b>Friday 14 April</b>: four squads, four greens. Each squad lead has said honestly that their sprint is on track.</p>
  <ul>
    <li>Oskar's own notes say <b>61 %</b> of planned test cases are blocked by test environments.</li>
    <li><b>Rehearsal 1</b>, on Saturday 8 April, reconciled <b>98.1 %</b> of balances. The criterion is 100 %.</li>
    <li>The burn-up chart Hana keeps privately shows the build <b>2.4 weeks behind</b> the baseline.</li>
    <li><span class="hl-pink">Every square on the dashboard is true. The picture is false.</span></li>
  </ul>""",
    problem_figs=[wm_problem],
    sides=dict(client=("Elaine", "<p>Elaine has been here before. Orion's reports were green for 22 months. When she sees four greens in April, two months before a pilot, she doesn't feel reassured; she feels the old dread. She'll trust a colour only if she can see what it's made of.</p>", "Green again. What's it made of?"),
                vendor=("Callum and Ines", "<p>Callum isn't hiding anything: he reports what the squads tell him. But squads see their sprint, not the programme. Ines needs a status built from <b>measures that can't be green unless the programme is</b>, before Vexmoor's assurance team finds the red inside.</p>", "Opinions are honest. Measures are true.")),
    sides_after="Watermelons are rarely lies. They're what you get when you add up local truths without measuring the whole.",
    analogy_side="the car dashboard",
    analogy="""  <p>A car doesn't ask the engine, the brakes and the tyres how they feel. It <b>measures</b>: oil pressure, brake fluid, tyre pressure, each with a threshold. If any one crosses it, a warning lights up, whatever the others say. Nobody would trust a car that showed green because three of four parts felt fine.</p>""",
    map=[("Asking each part how it feels", "Each squad reporting its own sprint"),
         ("Oil pressure, tyre pressure", "Burn-up, tests passed, reconciliation, serious defects"),
         ("A threshold for each", "Agreed with Elaine, written down"),
         ("Any warning lights the dashboard", "Overall colour = the worst measure"),
         ("The mechanic's notes", "The squads' comments, underneath")],
    how_side="measures, thresholds, the worst one wins",
    how="""  <p>Ines and Callum rebuild the status around <b>four measures</b>, each with a threshold agreed with Elaine:</p>
  <ul>
    <li><b>Burn-up against plan</b> (story points delivered vs baseline v2.0): amber if more than one week behind, red if more than three. Now: <b>−2.4 weeks</b>, amber.</li>
    <li><b>Tests passed</b> out of those planned to date: amber below 70 %, red below 30 %. Now: <b>39 %</b>, amber (most are blocked by environments, not failing).</li>
    <li><b>Last rehearsal reconciled</b>: red below 99.9 %. Now: <b>98.1 %</b>, red.</li>
    <li><b>Open severity 1–2 defects</b>: amber above 5. Now: <b>7</b>, amber.</li>
  </ul>
  <p>The <b>overall colour is the worst of the four</b>: red for reconciliation. The first line: <i>“RED: rehearsal 1 reconciled 98.1 % of balances (target 100 %); cause found (rounding rule R7 in the back-feed); rehearsal 2 in July.”</i> The squads' own words stay, underneath the numbers. Elaine reads it and says: “Finally a red I believe.”</p>""",
    how_figs=[wm_how],
    steps=[("Choose three to five programme measures", "Progress, quality, readiness."),
           ("Agree thresholds with the client", "Written, before the numbers arrive."),
           ("Overall colour = worst measure", "No averaging."),
           ("Numbers in line one", "And the cause, if known."),
           ("Keep the teams' words underneath", "Context, not colour."),
           ("Show the trend", "This week and the last four.")],
    vocab=[("Watermelon report", "A status that's green outside and red inside."),
           ("Burn-up chart", "Work completed over time against the total planned."),
           ("Threshold", "The value at which a measure changes colour."),
           ("Leading indicator", "A measure that warns before the outcome (e.g. blocked tests)."),
           ("Lagging indicator", "A measure of results already happened (e.g. a failed rehearsal)."),
           ("Roll-up", "Combining team reports into a programme view; dangerous if it's an average.")],
    code=dict(file="delivery/lodestar/status/2028-04-14.md", note="weekly status #38 · Fri 14 Apr 2028", src="""
LODESTAR · WEEKLY STATUS #38 · Fri 14 Apr 2028                              RED
Rehearsal 1 reconciled 98.1 % of balances (target 100 %); cause found: rounding
rule R7 missing in the back-feed; fix in sprint 19; rehearsal 2 on 15 Jul.

measure                     now          threshold            colour   4 wks ago
burn-up vs baseline v2.0    −2.4 weeks   amber > 1 · red > 3  AMBER    −0.8
tests passed / planned      39 %         amber < 70 % (*)     AMBER    61 %
last rehearsal reconciled   98.1 %       red < 99.9 %         RED      —
open sev 1–2 defects        7            amber > 5            AMBER    3
(*) 61 % of planned tests blocked by environments (see I-14), not failing
squads: data "on track" · platform "on track" · billing "on track" · testing "blocked"
"""),
    contract=dict(side="what the colours mean, by contract", doc="Lodestar SOW · Schedule 7, Annex B (as amended)", date="v1.2 · 14 Apr 2028", stamp="measured",
                  clauses=[("B.2", "<ins>The overall status is the most severe of the measures in Annex B.3; measures and thresholds are agreed with MetroVolt's Programme Director.</ins>", "no averaging. ever."),
                           ("5.2", "Status colours … describe progress against the next Milestone, irrespective of cause.", "from vol. 2. still the rule. the cause goes in line one.")],
                  plain="defining the overall colour as the worst measure, in the contract's reporting schedule, makes a watermelon impossible by construction."),
    health=dict(now="a",
                g=("trust is high", ["Measures and opinions, side by side.", "Red is a conversation, not a crisis.", "Trends over time."]),
                a=("the client has lived through green-then-red", ["Measures with agreed thresholds.", "Worst measure wins.", "Numbers in line one."]),
                r=("an assurer hunting for red", ["Find the red first, yourself.", "Cause and fix with the red.", "Never argue a colour down."])),
    pressure=dict(level=4, title="the first red", cost="one awkward conversation with Callum · a red the managing director will see",
                  items=["Callum's report wasn't dishonest. Say so, before you change it.", "The first red after months of green feels like failure. It's the first report anyone will fully believe."]),
    baseline="Each line compares <b>four squad greens</b> with <b>four measures, agreed thresholds and the worst one setting the colour</b>.",
    ratings=[(2, 5, "“Finally a red I believe.”"),
             (3, 3, "Hard to see red; easier than a surprise later."),
             (3, 3, "Neutral."),
             (3, 3, "Neutral."),
             (3, 4, "The R7 back-feed bug is visible and fixed."),
             (2, 5, "Leading indicators show trouble early."),
             (2, 5, "Definitions in the contract."),
             (4, 3, "Measures take an hour a week to update."),
             (3, 3, "A sheet to maintain.")],
    pitfalls=[("Rolling up opinions", "Every sprint green, the programme red.", "measures, not moods."),
              ("Averaging colours", "One red hides behind three greens.", "the worst measure wins."),
              ("Thresholds set after the numbers", "They bend to fit.", "agree them in advance."),
              ("No cause with the red", "Panic instead of action.", "cause and fix in line one."),
              ("Arguing colours down", "The client stops believing them.", "argue the plan, not the colour.")],
    grimoire=[(2, "toxic-positivity-siren", "The Toxic Positivity Siren", "is the watermelon's patron saint: “no problems, only opportunities”, as the water rises.")],
    use=["Any programme with several teams.", "When reports have been green for a long time.", "Before an outside assurer looks."],
    skip=["A single small team where everyone sees the same board."],
    related=["<b>What Goes in the First Status Report?</b> (vol. 2)", "<b>Is Anyone Reading the RAID Log?</b> (next note)", "<b>How Do We Re-plan Without Lying?</b> (this volume)", "<b>Where Are We, Really?</b> (Sanne, vol. 2)"],
    quiz=[("Why can a report be green outside and red inside without anyone lying?", "Each team reports its own sprint honestly; nobody measures the whole programme."),
          ("What four measures did Lodestar use?", "Burn-up vs plan, tests passed, last rehearsal reconciliation, open severity 1–2 defects."),
          ("How is the overall colour set?", "It's the worst of the measures."),
          ("What goes in line one?", "The colour, the numbers and the cause if known."),
          ("Why agree thresholds in advance?", "So they can't be bent to fit the numbers.")],
    quiz_sit=[("Graham asks whether the report could be amber “since the cause is found”. What do you say?", "No: the colour describes progress against the milestone, irrespective of cause. The cause and fix are in line one; that's what will reassure Elaine.")],
    try_it="Take your project's status. Pick three measures that would show trouble early, with thresholds. Make the overall colour the worst of them. What colour are you?",
    remember="Opinions are honest; <span class=\"hl\">measures are true</span>. The overall colour is <span class=\"hl\">the worst one</span>.",
    late=dict(when="Fri 14 April 2028 · 21:20 · hotel near The Grid",
              lines=["Four greens and a red inside. Nobody lied. Everybody was looking at their own sprint.",
                     "Elaine: “Finally a red I believe.” Callum looked as if he'd been forgiven for something.",
                     "R7, again. The rounding rule we kept for wave 1, forgotten in the back-feed. Fixed in sprint 19."]),
    sources=["Project Management Institute, <i>PMBOK Guide</i>: performance measurement.",
             "Troy Magennis, <i>Forecasting Using Data</i> (2011).",
             "UK Infrastructure and Projects Authority, delivery confidence assessments."],
)

# ------------------------------------------------------------------ 02 Is Anyone Reading the RAID Log?
rl_problem = Doodle(760, 240, "Doodle of the RAID log on 3 April 2028: a spreadsheet of 214 rows of risks, assumptions, issues and dependencies. 61 have no owner. 88 haven't been updated since January. The top risk on the sheet is still the 2027 laptop delay. Nobody has opened it for three weeks.",
                    "214 rows. 61 without an owner. Last opened three weeks ago.", exact=True)
rl_problem.box(24, 20, 360, 190, None, "paper", rx=4)
for i in range(9):
    rl_problem.line(f"M34 {62 + i * 16} h340", thin=True)
rl_problem.head(204, 36, "RAID.xlsx · 214 rows", size=17)
for i, (h, sub) in enumerate([("61", "no owner"), ("88", "not updated since Jan"), ("#1 risk", "2027 laptops")]):
    rl_problem.box(420, 20 + i * 66, 326, 56, h, "pink", sub=sub, size=19, subsize=14)

rl_how = Doodle(760, 320, "The RAID log rebuilt. The top twelve items only, on one page, each with an owner, a next step and a date. Everything else in a backlog, reviewed monthly. A fifteen-minute review every Monday at 09:45, standing, with Elaine. A rule: an item without an owner or a date isn't on the page. Closed items get a line saying what closed them.",
                "Twelve items, each with an owner, a next step and a date, read aloud for fifteen minutes on Mondays.", exact=True)
rl_how.box(14, 14, 460, 250, None, "y", rx=6)
rl_how.head(244, 44, "the top 12 · one page", size=20)
for i, t in enumerate(["R-01 back-feed R7 · Hana · fix S19 · 28 Apr", "I-14 test envs · Hollis · booking · 21 Apr", "D-21 MetroBus alerts · MV IT · May", "R-04 exception staff · Customer Ops · May", "…"]):
    rl_how.text(30, 82 + i * 34, t, anchor="start", size=15)
rl_how.box(490, 14, 256, 110, "Monday 09:45", "green", sub="15 min · standing · Elaine", size=19, subsize=14)
rl_how.box(490, 140, 256, 124, "backlog", "paper", sub="202 items · monthly", size=19, subsize=14)
rl_how.note(380, 300, "no owner or no date = not on the page", "red", size=18)

RAID = dict(
    slug="raid-log", date=date(2028, 4, 3), meta=on_site(date(2028, 4, 3)), where="FL 19", pass_kind="contractor",
    kicker="a.k.a. “RAID log”: risks, assumptions, issues, dependencies",
    tldr="A RAID log people don't read is a filing cabinet. Keep a <b>short page</b> of the items that matter now (a dozen), each with an <b>owner</b>, a <b>next step</b> and a <b>date</b>; move the rest to a backlog you review monthly. Read the page aloud for <b>fifteen minutes every week</b>, with the client. An item without an owner or a date isn't managed; it's decoration.",
    chips=[("Family", "telling the truth"), ("Lives in", "delivery/lodestar/raid-top12.md"), ("Pairs with", "the watermelon report, re-planning")],
    problem_side="The Grid, 3 April 2028",
    problem="""  <p class="lead">Lodestar's RAID log has grown since the bid: <b>214 rows</b> of risks, assumptions, issues and dependencies, maintained by Callum, read by nobody.</p>
  <ul>
    <li><b>61</b> rows have no owner. <b>88</b> haven't been updated since January.</li>
    <li>Row 1, the top risk by its score, is still <b>the 2027 laptop delay</b>.</li>
    <li>The real top risk (the rounding rule missing from the back-feed, found in rehearsal 1) <span class="hl-pink">is row 197</span>.</li>
  </ul>""",
    problem_figs=[rl_problem],
    sides=dict(client=("Elaine", "<p>Elaine is copied on the RAID log every week and has stopped opening it. She wants to know <b>what could hurt the pilot</b> and who's doing what about it, in a minute, not in a spreadsheet.</p>", "Tell me the five things that worry you, and who's on them."),
                vendor=("Callum", "<p>Callum keeps the log because the contract asks for one, and because deleting a row feels like hiding a risk. So it grows, and the important rows sink. He's protecting himself, and the log protects nobody.</p>", "If I delete it and it happens, it's my fault.")),
    sides_after="A long risk log feels safe for the person who writes it. A short one is safe for the project.",
    analogy_side="the pilot's checklist and the manual",
    analogy="""  <p>A plane has a <b>manual</b> of thousands of pages and a <b>checklist</b> of a dozen lines, read aloud before take-off. Nobody reads the manual every flight. Everyone reads the checklist, every flight, and each line has someone who answers “checked”.</p>""",
    map=[("The manual", "The backlog: 202 items, reviewed monthly"),
         ("The checklist", "The top 12, on one page"),
         ("Read aloud before take-off", "Fifteen minutes, Monday 09:45"),
         ("Someone answers “checked”", "An owner for each line"),
         ("A new checklist for a new phase", "Re-picking the top 12 as the project moves")],
    how_side="a short page, owners and dates, read weekly",
    how="""  <p>On <b>3 April</b> Ines and Callum go through all 214 rows in two hours. <b>Twelve</b> go on the page: the ones that could stop the pilot or wave 1 in the next three months. Each gets an <b>owner</b> (a person, not a team), a <b>next step</b> and a <b>date</b>. The rest go to a <b>backlog</b>, reviewed on the first Monday of each month. Forty-one rows are <b>closed</b>, each with a line saying what closed it (the laptops arrived in July 2027).</p>
  <p>The page is read aloud every <b>Monday at 09:45</b>, fifteen minutes, standing, with Elaine. For each item, the owner says one sentence: done, next, still on date or not. New items come in only with an owner and a date.</p>
  <p>Callum's fear is answered by the backlog: nothing is deleted, only sorted. In the first month the page changes eleven times. The rounding-rule risk (row 197) is item 1 on the page, and fixed by 28 April.</p>""",
    how_figs=[rl_how],
    steps=[("Sort the whole log once", "Page, backlog or closed."),
           ("Keep the page short", "A dozen items that matter in the next three months."),
           ("Owner, next step, date", "For every item on the page."),
           ("Read it aloud weekly", "Fifteen minutes, with the client."),
           ("Review the backlog monthly", "Promote what's getting closer."),
           ("Close with a reason", "What closed it, in one line.")],
    vocab=[("RAID log", "A list of risks, assumptions, issues and dependencies."),
           ("Risk", "Something that might happen and would hurt."),
           ("Issue", "Something that is happening now."),
           ("Risk owner", "The one person responsible for watching and acting on a risk."),
           ("Next step", "The very next action, specific enough to check."),
           ("Risk backlog", "Items being watched but not actively managed this week.")],
    code=dict(file="delivery/lodestar/raid-top12.md", note="Monday review · 3 Apr 2028", src="""
RAID · TOP 12 (read aloud Mondays 09:45, 15 min, with Elaine)     backlog: 161 · closed: 41

id     item                                         owner         next step          date
R-01   back-feed misses rounding rule R7            Hana          fix in sprint 19   28 Apr
I-14   test environments blocked 61 % of tests      Hollis        booking calendar   21 Apr
D-21   MetroBus delay alerts (DA condition 2)       MetroVolt IT  alert rules live   15 May
R-04   exception-queue staff not yet trained        Customer Ops  training plan      2 May
R-07   Halvorsen test env on spec v1.1?             Sven          confirm version    10 Apr
I-16   performance test environment (DA cond. 3)    Hollis        date confirmed     12 Apr
…      (6 more)
rule: no owner or no date = not on the page
"""),
    contract=dict(side="what the contract asks for", doc="Lodestar SOW · Schedule 7, §5.3", date="v1.1 · Aug 2027", stamp="read weekly",
                  clauses=[("5.3", "The Supplier shall maintain a register of risks, assumptions, issues and dependencies and review it with MetroVolt's Programme Director at least monthly.", "monthly is the minimum. weekly is how it gets read."),
                           ("6.1", "Each Party shall notify the other promptly of any matter which could increase the Charges, delay a Milestone or impair performance.", "a risk at row 197 isn't “notified”.")],
                  plain="contracts ask for a risk register and a review. Meeting the clause with 214 rows nobody reads doesn't meet its purpose, or the early-warning clause next to it."),
    health=dict(now="g",
                g=("trust is high", ["The page is a conversation starter.", "Short and frequent.", "Client owners on the page too."]),
                a=("the client has stopped reading", ["Twelve items, read aloud.", "Owners and dates.", "Close old items with reasons."]),
                r=("the log is evidence in a dispute", ["Keep the full backlog intact.", "Date every change.", "Still read the page weekly."])),
    pressure=dict(level=2, title="the long list", cost="two hours of sorting · one worried engagement manager",
                  items=["Callum's fear of deleting risks is reasonable. The backlog keeps everything; only attention moves.", "Fifteen minutes standing is a ritual people keep. An hour sitting is one they skip."]),
    baseline="Each line compares <b>a 214-row log nobody reads</b> with <b>a top-12 page with owners and dates, read aloud weekly</b>.",
    ratings=[(2, 4, "Elaine knows the five things that matter."),
             (3, 4, "Less time maintaining, more acting."),
             (3, 3, "Neutral."),
             (3, 3, "Neutral."),
             (3, 3, "Neutral."),
             (1, 5, "The real top risk is item 1, fixed in weeks."),
             (2, 4, "Owners and dates on record; closures explained."),
             (4, 4, "Fifteen minutes a week."),
             (2, 4, "One page instead of 214 rows.")],
    pitfalls=[("Everything on one list", "The important sinks.", "a page and a backlog."),
              ("Teams as owners", "Nobody acts.", "one person per item."),
              ("No dates", "Items sit forever.", "a next step with a date."),
              ("Emailed, not read", "Nobody opens it.", "read aloud, weekly."),
              ("Deleting to tidy", "History lost.", "close with a reason, keep the backlog.")],
    use=["Any project with a risk register.", "When nobody reads the log.", "Before a key milestone."],
    skip=["Never skip it; on a tiny project the page may have three items."],
    related=["<b>Why Is Everything Green Except the Truth?</b> (previous note)", "<b>What Could Happen?</b> (Sanne, vol. 5)", "<b>Risk Register</b> (Ana, vol. 6)", "<b>What Are We Assuming?</b> (vol. 1)"],
    quiz=[("What goes on the RAID page?", "The dozen items that could hurt in the next three months, each with an owner, next step and date."),
          ("What happens to the rest?", "They go to a backlog reviewed monthly; nothing is deleted."),
          ("Why read it aloud?", "Owners commit in front of the client; nobody reads an emailed spreadsheet."),
          ("What's the rule for new items?", "No owner or no date means it isn't on the page."),
          ("What was the real top risk in April?", "The rounding rule R7 missing from the back-feed (row 197 of the old log).")],
    quiz_sit=[("Hollis is the owner of three items and never has an update on Mondays. What do you do?", "Talk to him privately: ask whether he's the right owner or needs a named person in his team, and agree one sentence he can give each week. Don't shame him in the review.")],
    try_it="Open your project's risk list. Pick the twelve items that matter in the next three months. Give each one person, a next step and a date. Read the page aloud to your team on Monday.",
    remember="A risk log is <span class=\"hl\">read, not kept</span>. Twelve items, an owner and a date each, <span class=\"hl\">fifteen minutes a week</span>.",
    late=dict(when="Mon 3 April 2028 · 20:30 · hotel near The Grid",
              lines=["214 rows. The real top risk was row 197. The laptops from 2027 were still row 1.",
                     "Callum didn't want to delete anything. Nothing was deleted. Forty-one things were closed, with reasons.",
                     "Fifteen minutes, standing. Elaine came. She asked two questions. That's more than the spreadsheet got all year."]),
    sources=["Project Management Institute, <i>PMBOK Guide</i>: risk and issue management.",
             "Tom DeMarco and Timothy Lister, <i>Waltzing with Bears</i> (2003).",
             "Atul Gawande, <i>The Checklist Manifesto</i> (2009)."],
)

# ------------------------------------------------------------------ 03 Where Did This Extra Work Come From?
sd_problem = Doodle(760, 240, "Doodle of small requests arriving through side doors over six weeks: Teams messages, corridor chats, a sticky note on Hana's screen, an email to Lottie. Twenty-three asks, each small: an extra field, a report, a filter. Together, forty-one days of work. None of them in the change register.",
                    "23 small asks in six weeks, through side doors. Together: 41 days.", exact=True)
for i, t in enumerate(["Teams", "corridor", "sticky note", "email", "stand-up", "lunch"]):
    sd_problem.box(14 + (i % 3) * 130, 20 + (i // 3) * 70, 120, 56, t, "y", size=16)
sd_problem.arrow(410, 90, 480, 90)
sd_problem.box(484, 30, 262, 120, "41 days", "pink", sub="23 asks · 0 in the register", size=26, subsize=15)
sd_problem.note(380, 210, "each one reasonable; together, the slip", "red", size=20)

sd_how = Doodle(760, 330, "Catching side-door scope. One: count it, by asking every squad member on Friday what they did that wasn't on the board. Two: log each as a change note with its days. Three: triage weekly with Elaine: into the change pool, into wave 2, or no. Of the 23: 9 into the pool, 58,000 pounds; 11 to wave 2; 3 declined. Four: make the front door easy, a two-line request form in the Teams channel.",
                "Count it, log it, triage it weekly, and make the front door easier than the side door.", exact=True)
for i, (h, sub, fill) in enumerate([("count", "Fridays: off-board?", "y"), ("log", "a change note each", "blue"), ("triage weekly", "pool · wave 2 · no", "green"), ("front door", "2-line form", "paper")]):
    sd_how.box(14 + i * 186, 20, 174, 100, h, fill, sub=sub, size=19, subsize=13)
for i, (h, n, fill) in enumerate([("change pool", "9 · £58k", "green"), ("wave 2", "11", "y"), ("declined", "3", "pink")]):
    sd_how.box(14 + i * 250, 160, 232, 80, h, fill, sub=n, size=19, subsize=17)
sd_how.note(380, 290, "the board is the plan; work off the board is a change", "pen", size=18)

SIDE_DOOR = dict(
    slug="side-door-scope", date=date(2028, 4, 20), meta=on_site(date(2028, 4, 20)), where="FL 19", pass_kind="contractor",
    kicker="a.k.a. “scope creep through the side door”",
    tldr="On a blended team, most scope creep doesn't come through the change process; it comes through <b>side doors</b>: chat messages, corridor favours, “while you're in there”. Each request is small and reasonable; together they're the slip. <b>Count</b> the work that wasn't on the board, <b>log</b> each as a change, <b>triage</b> weekly with the client (change pool, later, or no), and make the <b>front door easier</b> than the side door.",
    chips=[("Family", "telling the truth"), ("Lives in", "delivery/lodestar/change-register.md (change notes)"), ("Pairs with", "change control (vol. 2), one team (vol. 2)")],
    problem_side="The Grid, April 2028",
    problem="""  <p class="lead">The burn-up says the build is <b>2.4 weeks behind</b>. The squads say they're working hard. Both are true. On <b>Thursday 20 April</b>, Ines asks every squad member one question: <i>“What did you do in the last six weeks that wasn't on the board?”</i></p>
  <ul>
    <li><b>23 small requests</b>: an extra field for Kofi's metering team, three reports for Gareth's analysts, a filter for Customer Ops, a screen tweak asked for at lunch.</li>
    <li>Each took a day or two. Together: <b>41 days</b>, about the size of the slip.</li>
    <li><span class="hl-pink">None of them are in the change register.</span> All of them came from friendly MetroVolt colleagues in the mixed squads.</li>
  </ul>""",
    problem_figs=[sd_problem],
    sides=dict(client=("MetroVolt colleagues", "<p>For MetroVolt people in the squads, asking Lottie for a field is just teamwork: that's what “one team” meant in August. Filling in a change request for a one-day job feels bureaucratic and rude. None of them think of it as scope.</p>", "We're one team. It's a tiny thing."),
                vendor=("Ines and the squads", "<p>For Wrenfield, every favour is fixed-price time spent on things outside Schedule 2, and invisible in the plan. Saying no to colleagues feels terrible; saying yes 23 times has cost two and a half weeks.</p>", "Every yes is fine. Every invisible yes isn't.")),
    sides_after="Side-door scope is the price of a good blended team. The answer isn't fewer friends; it's a door that's easier to use than the side one.",
    analogy_side="the shop assistant's favours",
    analogy="""  <p>A shop assistant who gives regulars a free extra slice, a small discount, a delivery on the way home, is lovely. At the end of the month, the till is short and nobody knows why. A sensible shop doesn't ban kindness; it gives the assistant a <b>notebook for favours</b>, and decides each week which ones become a loyalty scheme.</p>""",
    map=[("Free extra slices", "Extra fields, reports, filters"),
         ("The till short at month end", "The 2.4-week slip"),
         ("A notebook for favours", "Change notes for every off-board job"),
         ("Deciding weekly", "Triage with Elaine: pool, wave 2, or no"),
         ("A loyalty scheme", "The change pool, used properly")],
    how_side="count, log, triage weekly, and make the front door easy",
    how="""  <p><b>Count it.</b> Every Friday, each squad member answers one question: what did you do this week that wasn't on the board? Lottie collects the answers in five minutes.</p>
  <p><b>Log it.</b> Each item becomes a <b>change note</b> with its days, the person who asked and why. The 23 from the last six weeks are logged retroactively.</p>
  <p><b>Triage weekly with Elaine.</b> Fifteen minutes after the RAID review. Each note goes one of three ways: into the <b>change pool</b> (it's worth doing now), to <b>wave 2</b>, or <b>no</b>. Of the 23: <b>9</b> into the pool (£58k, at the rate card), <b>11</b> to wave 2, <b>3</b> declined. The slip is explained, and partly paid for.</p>
  <p><b>Make the front door easy.</b> A pinned two-line form in the #lodestar channel: what you need, and why. Lottie answers within a day with “on the board”, “to Elaine for triage” or “wave 2”. MetroVolt colleagues use it because it's faster than catching Hana in the corridor.</p>""",
    how_figs=[sd_how],
    steps=[("Ask what wasn't on the board", "Every Friday, every person."),
           ("Log every item with its days", "Who asked, why."),
           ("Triage with the client weekly", "Now (pool), later, or no."),
           ("Use the change pool for “now”", "It's what it's for."),
           ("Make the front door faster", "A two-line form, answered in a day."),
           ("Never blame the askers", "They were being good teammates.")],
    vocab=[("Scope creep", "Unplanned growth of work."),
           ("Side-door request", "A request that bypasses the agreed change process."),
           ("Change note", "A lightweight record of a small change and its cost."),
           ("Triage", "Sorting requests quickly into categories for action."),
           ("Change pool", "Pre-approved money for small changes."),
           ("Front door", "The official, easy way to ask for work.")],
    code=dict(file="delivery/lodestar/side-door-2028-04.md", note="triage with Elaine · Thu 20 Apr 2028", src="""
SIDE-DOOR WORK · 6 weeks to 14 Apr 2028 · 23 requests · 41 days

asked by            requests  days   triage
metering (Kofi)     6         11     4 → pool (£16k) · 2 → wave 2
Network Assets      5         9      1 → pool · 2 → wave 2 · 2 → no
Customer Ops        8         14     4 → pool · 4 → wave 2
others              4         7      0 → pool · 3 → wave 2 · 1 → no
total               23        41     9 → pool (£58,000) · 11 → wave 2 · 3 → no

front door: #lodestar pinned form "what do you need? why?" → Lottie replies within 1 day
Friday question: "what did you do this week that wasn't on the board?"
change pool: £150,000 · used £74,000 (CR-001 £8k · CN-010..018 £58k · other £8k)
"""),
    contract=dict(side="the clause that makes side doors visible", doc="Lodestar SOW · §7.6 and §8.5", date="signed 30 June 2027", stamp="only recorded changes count",
                  clauses=[("7.6", "No Change is binding unless recorded in the Change Register and approved under this clause.", "so the 23 favours weren't changes. they were gifts. now they're changes."),
                           ("8.5", "Instructions to the Supplier are valid only if given by MetroVolt's Programme Director or the Steering Committee.", "Kofi asked. Elaine decides. the form routes it.")],
                  plain="the contract already says only recorded changes count and only named people can instruct. Side-door work is outside both, which is why it must be counted and routed, not just done."),
    health=dict(now="g",
                g=("blended team, high trust", ["Count and route, kindly.", "Most go in the pool.", "Celebrate the front door."]),
                a=("the slip is unexplained", ["Count six weeks back.", "Triage with the client.", "Show the 41 days."]),
                r=("favours used as leverage", ["Log every request with the asker.", "Quote §8.5 gently.", "Decline what's outside scope."])),
    pressure=dict(level=3, title="saying no to friends", cost="41 days found · 3 polite noes",
                  items=["Saying no to Kofi feels like betraying the one-team agreement. The front door says “yes, through here” instead.", "Never make the squad members feel they were caught doing something wrong. They were being kind."]),
    baseline="Each line compares <b>saying yes in corridors</b> with <b>counting, logging and triaging side-door work weekly, with an easy front door</b>.",
    ratings=[(3, 4, "MetroVolt colleagues still get help, through a door that works."),
             (2, 4, "Squads stop absorbing invisible work."),
             (1, 4, "£58k of work paid from the pool."),
             (2, 5, "Everything done is on the board or the register."),
             (3, 3, "Neutral."),
             (2, 4, "Slip explained, then controlled."),
             (2, 4, "Every change noted, with the asker."),
             (4, 3, "Five minutes on Friday, fifteen on Thursday."),
             (3, 3, "A form and a log to run.")],
    pitfalls=[("Banning favours", "The one-team spirit dies.", "route them, don't ban them."),
              ("Not counting", "The slip is a mystery.", "ask what wasn't on the board."),
              ("Logging but not triaging", "The list grows, nothing decided.", "weekly, with the client."),
              ("A slow front door", "People go back to the corridor.", "answer in a day."),
              ("Blaming the askers", "Trust collapses.", "they were good teammates.")],
    grimoire=[(6, "scope-creep-swarm", "The Scope-Creep Swarm", "is the same plague at GridSight in 2028: “while you're at it, could you just…”.")],
    use=["Blended or co-located teams.", "Fixed-price work.", "When the plan slips and nobody knows why."],
    skip=["Pure time and materials where the client directs daily: still count it."],
    related=["<b>How Do We Change the Deal Without a War?</b> (vol. 2)", "<b>How Do Two Companies Work as One Team?</b> (vol. 2)", "<b>Is Anyone Reading the RAID Log?</b> (previous note)", "<b>Can We Change That?</b> (Sanne, vol. 2)"],
    quiz=[("Where does most scope creep come from on a blended team?", "Side doors: chats, corridors and favours, not the change process."),
          ("What's the Friday question?", "What did you do this week that wasn't on the board?"),
          ("What are the three triage outcomes?", "Into the change pool now, to wave 2, or no."),
          ("How many of the 23 went where?", "9 into the pool (£58k), 11 to wave 2, 3 declined."),
          ("Why make the front door easy?", "People use the fastest route; if the form is faster than the corridor, they'll use the form.")],
    quiz_sit=[("Gareth's analyst asks Lottie for a report “by Friday, it's for Rupert”. What does Lottie do?", "Thank her, put it through the front-door form, and tell Ines so it can go to Elaine's triage that day; if it's urgent and small, it can come from the change pool quickly.")],
    try_it="Ask everyone on your team: what did you do last week that wasn't on the plan? Add up the days. Where did the requests come from? Design a two-line front door.",
    remember="Side-door work isn't wrong; <span class=\"hl\">invisible</span> work is. Count it, triage it, and make <span class=\"hl\">the front door easier</span>.",
    late=dict(when="Thu 20 April 2028 · 21:00 · hotel near The Grid",
              lines=["Twenty-three favours. Forty-one days. The slip, almost to the day.",
                     "Nobody did anything wrong. Lottie was helping Kofi. Kofi was being a good teammate. That's the problem.",
                     "Elaine put nine in the pool without blinking. The front-door form had four requests by 17:00."]),
    sources=["Karl Wiegers, <i>Software Requirements</i> (3rd ed., 2013): managing scope change.",
             "Project Management Institute, <i>PMBOK Guide</i>: scope control.",
             "Dominica DeGrandis, <i>Making Work Visible</i> (2017)."],
)

NOTES = [WATERMELON, RAID, SIDE_DOOR]
