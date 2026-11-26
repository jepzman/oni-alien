# Series 2 · Book 5 · The IT Operations Notebook · Vol. 6 · Leading.
# Narrator: Eli (he/him). Facts: docs/larder-casebook.md, "Book 5, Vol. 6".

# ------------------------------------------------------------------ 11 Continual Improvement That Continues
ir_problem = Doodle(760, 260, "Doodle of July 2028: Larder's improvement work lives in seven lists. Review actions, problems, known errors to retire, near-miss actions, risk actions, items from the IT pulse, the maturity check's focus areas, and 27 automation ideas. Each list has its own rhythm, or none. Some items appear on three lists; others on none. The reliability team can't say what it's improving this month, or why that and not something else.",
                    "Seven improvement lists, each with its own rhythm or none, and no answer to “what are we improving this month?”")
for i, t in enumerate(["review actions", "problems", "near misses", "risk actions", "pulse", "maturity", "automation"]):
    ir_problem.box(14 + i * 106, 30, 98, 90, t, "y", size=12)
ir_problem.note(380, 170, "duplicates on three lists · some items on none", "red", size=18)
ir_problem.note(380, 206, "“what are we improving this month?” · no answer", "pen", size=16)

ir_analogy = Doodle(760, 220, "Doodle of a family's single to-do board on the fridge, replacing notes in five places: a column for 'next', a column for 'doing' with room for only three cards, and 'done'. Every Sunday they spend ten minutes choosing what moves into 'doing'. Things get finished because only three are open.",
                    "One board instead of five lists: next, doing (three cards max), done. Ten minutes every Sunday.")
ir_analogy.row([("next", "many", "paper"), ("doing", "max 3", "y"), ("done", None, "green")], x=110, y=40, h=96, w=170, gap=40, size=20, subsize=14, arrows=True)
ir_analogy.note(380, 186, "things finish because only a few are open", "pen", size=18)

ir_how = Doodle(760, 400, "Larder's improvement register from July 2028: one list for everything that should get better, whatever the source: reviews, problems, near misses, risks, the pulse, the maturity check, automation ideas. Each item: source, owner, a one-line benefit, a size and a score. 20 percent of the reliability team's time goes to it, every week. At most five items in progress at once. A 30-minute monthly prioritisation with Ben, Sam and Joost's operations lead; items can be dropped on purpose with a reason. July: 64 items after merging duplicates. By October: 23 done, 11 dropped honestly, 5 in progress.",
                "One register, 20 % of the team's time, at most five in progress, a monthly 30-minute choice. 23 done by October.")
ir_how.box(14, 14, 732, 50, "sources: reviews · problems · near misses · risks · pulse · maturity · automation → ONE register", "blue", size=14)
ir_how.row([("next", "scored", "paper"), ("in progress", "max 5", "y"), ("done", None, "green"), ("dropped", "with a reason", "paper")], x=14, y=86, h=86, gap=36, size=17, subsize=13, arrows=True)
ir_how.box(14, 196, 360, 64, "20 % of team time, weekly", "green", size=15)
ir_how.box(386, 196, 360, 64, "monthly 30 min: Ben, Sam, Joost's lead", "y", size=15)
ir_how.row([("Jul", "64 items (merged)", "paper"), ("Oct", "23 done · 11 dropped · 5 doing", "green")], x=110, y=282, h=80, w=250, gap=40, size=17, subsize=13, arrows=True)

IMPROVEMENT_REGISTER = dict(
    slug="improvement-register",
    kicker="a.k.a. “the continual improvement register”",
    tldr="Improvement ideas come from everywhere: reviews, problems, near misses, risks, surveys, maturity checks. Kept in separate lists, they compete, duplicate and stall. Keep <b>one register</b> for all of them, with a source, owner, benefit and size for each. Give it a <b>fixed share of time</b>, limit <b>work in progress</b>, and hold a short <b>monthly choice</b> with the people it serves. Improvement continues when it has a rhythm, not when someone feels enthusiastic.",
    chips=[("Family", "leading"), ("Lives in", "one register in the tracker; 20 % of the team's time; monthly 30 minutes"), ("Pairs with", "action items (vol. 2), the maturity check, automation strategy")],
    itil=dict(groups=["general"], chain=["improve"], practices=["continual improvement"],
              sre="(reliability work planned alongside feature work)", principles=["Progress iteratively with feedback", "Keep it simple and practical"],
              older="ITIL v3: the CSI register, the seven-step improvement process"),
    problem_side="Larder, July 2028",
    problem="""  <p class="lead">By July, Larder's improvement work lives in <b>seven lists</b>: review actions, problems, near-miss actions, risk actions, items from the IT pulse, the maturity check's focus areas, and 27 automation ideas. Each list has its own rhythm, or none. Some items appear on three lists, and others on none. <span class="hl-pink">The reliability team can't say what it's improving this month, or why that and not something else.</span></p>
  <ul>
    <li>Improvement competes with itself.</li>
    <li>Everything is started; little is finished.</li>
    <li>When the team gets busy, improvement quietly stops.</li>
  </ul>""",
    problem_figs=[ir_problem],
    analogy_side="the family's one board",
    analogy="""  <p>A family replaces notes in five places with <b>one board on the fridge</b>: a column for “next”, a column for “doing” with room for <b>only three cards</b>, and “done”. Every Sunday they spend <b>ten minutes</b> choosing what moves into “doing”. Things finally get finished, because only three are open at a time.</p>""",
    analogy_figs=[ir_analogy],
    map=[("Notes in five places", "Seven improvement lists"),
         ("One board", "One improvement register"),
         ("Three cards in “doing”", "At most five items in progress"),
         ("Ten minutes every Sunday", "30 minutes monthly with Ben, Sam, Joost's lead"),
         ("Throwing a card away", "Dropping an item on purpose, with a reason")],
    how_side="one register, a share of time, a WIP limit, a monthly choice",
    how="""  <p>In <b>July</b> Bram merges the seven lists into <b>one register</b>. Each item has its <b>source</b> (review, problem, near miss, risk, pulse, maturity, automation), an owner, a one-line benefit, a size and a score. Duplicates are merged: <b>64 items</b>.</p>
  <ul>
    <li><b>A fixed share of time</b>: 20 % of the reliability team's week, every week, including busy weeks.</li>
    <li><b>A work-in-progress limit</b>: at most <b>five</b> items in progress at once.</li>
    <li><b>A monthly choice</b>: 30 minutes with Ben, Sam and Joost's operations lead, the people improvement is for. Items can be <b>dropped on purpose</b>, with a reason.</li>
  </ul>
  <p>By <b>October</b>, <b>23</b> items are done and <b>11</b> have been dropped honestly, with <b>5</b> in progress. The action-item rules from 2026 still hold inside it: an owner, a date, a done test. Improvement now has a rhythm that doesn't depend on anyone's enthusiasm, including Eli's.</p>""",
    how_figs=[ir_how],
    steps=[("Merge every improvement list into one", "Keep the source on each item."),
           ("Give each an owner, benefit, size, score", "One line each."),
           ("Reserve a fixed share of time", "Every week, busy or not."),
           ("Limit work in progress", "Finish before starting."),
           ("Choose monthly with the people it serves", "30 minutes."),
           ("Drop items on purpose", "With a reason, so the list stays believable.")],
    vocab=[("Continual improvement", "Ongoing, small improvements to services and practices."),
           ("Improvement register", "One list of all improvement ideas and their status."),
           ("WIP limit", "A cap on how many items are in progress at once."),
           ("Capacity allocation", "A fixed share of time reserved for improvement."),
           ("Source", "Where an improvement idea came from (review, risk, survey…)."),
           ("Throughput", "How many items get finished per month.")],
    code=dict(file="ops/improvement-register.md", note="from July 2028 · monthly with Ben, Sam, Joost's lead", plain=True, src="""
id    source       item                                       owner   size   score  status
I-07  maturity     write up the last 6 "ask Bram" systems     Bram    M      18     done (Sep)
I-12  pulse        replace HH-2024 handhelds (with Dee)       Dee     L      16     doing
I-15  risk R1      incident lead rotation for all 4           Eli     S      15     done (Aug)
I-21  automation   restore tests self-starting                Yusuf   M      14     done (Sep)
I-30  near miss    cert check for services outside the path   Lotte   S      12     done (Aug)
I-44  review       billing silence: vendor health check       Cho     S      9      dropped: vendor did it
… 64 items

rules   20 % of reliability time weekly · ≤ 5 in progress · monthly 30 min choice
Oct     23 done · 11 dropped (reasons on each) · 5 doing
"""),
    tools="tools: one board in the tracker, a fixed weekly share of time, and a monthly 30-minute meeting.",
    ladder=[("seven lists, no rhythm", ["Everything started, little finished.", "Stops when busy."]),
            ("one register, time, a WIP limit", ["Monthly choice with stakeholders.", "Honest drops."]),
            ("improvement measured", ["Benefit checked after each item.", "Throughput tracked."]),
            ("improvement everywhere", ["Every team runs its own register the same way.", "Shared monthly."])],
    ladder_now=1,
    baseline="Each line compares <b>seven improvement lists without a rhythm</b> to <b>one register with fixed time, a WIP limit and a monthly choice</b>.",
    ratings=[(2, 3, "Improvements chosen with the people they serve."),
             (2, 3, "Risks and problems actually get worked."),
             (3, 3, "Neutral."),
             (3, 3, "Neutral."),
             (2, 4, "Anyone can see what's improving this month."),
             (2, 3, "Automation ideas finished, not just started."),
             (3, 3, "Neutral."),
             (3, 3, "Neutral."),
             (3, 3, "30 minutes a month plus the reserved time.")],
    pitfalls=[("Many lists", "Duplicates and gaps.", "one register."),
              ("No reserved time", "Improvement stops when busy.", "a fixed share every week."),
              ("Starting everything", "Nothing finishes.", "a WIP limit."),
              ("Never dropping", "A list nobody believes.", "drop on purpose, with a reason.")],
    use=["Improvement ideas live in several places.", "Things start but don't finish.", "Improvement stops whenever the team is busy.", "After a maturity check or a year of reviews."],
    skip=["A tiny team that just talks about it weekly, and finishes things."],
    related=["<b>Why Do Action Items Never Close?</b> (vol. 2)", "<b>Where Are We Weak?</b> (this volume)", "<b>What to Automate Next</b> (this volume)", "<b>The Architecture Backlog</b> (Ana, vol. 6)"],
    quiz=[("What goes into the improvement register?", "Everything that should get better, from reviews, problems, near misses, risks, the pulse, the maturity check and automation ideas."),
          ("How much time does it get?", "20 % of the reliability team's time, every week."),
          ("What's the WIP limit?", "At most five items in progress."),
          ("Who chooses, and how often?", "The team with Ben, Sam and Joost's lead, monthly, in 30 minutes."),
          ("What happened by October?", "23 done, 11 dropped with reasons, 5 in progress.")],
    quiz_sit=[("A busy month: Christmas preparations start, and someone suggests pausing the 20 % until January. What do you say?", "Keep it, perhaps on peak-related items: improvement that stops whenever it's busy never continues. If something must give, lower the WIP limit, not the time.")],
    try_it="Find every list of improvement ideas your team keeps. Merge them into one with a source on each. Reserve a share of next week for it, choose three items, and drop one on purpose.",
    remember="Improvement continues when it has <span class=\"hl\">one list, a share of time and a rhythm</span>, not when someone feels enthusiastic.",
    sources=["AXELOS, <i>ITIL 4: Continual improvement</i> practice guide (2020).",
             "David J. Anderson, <i>Kanban</i> (2010): limiting work in progress.",
             "Mike Rother, <i>Toyota Kata</i> (2009)."],
)

# ------------------------------------------------------------------ 12 Leading Change in How Teams Work
lc_problem = Doodle(760, 260, "Doodle of June 2028. The reliability team wants every product team to set SLOs, error budgets and readiness checks for its own services, since 'build it, run it' is the model. Eli sends a well-written page to all five teams. Dee's team answers: 'more process, less building'. Two teams don't answer. Ben's team, which already has them for Ordering, is fine. A page from the reliability team isn't changing anyone's habits.",
                    "A good page sent to five teams: one already doing it, one saying “more process”, two silent.")
lc_problem.row([("Ordering", "already ✓", "green"), ("Apps (Dee)", "“more process”", "pink"), ("Payments", "silent", "paper"), ("Business", "silent", "paper"), ("Data", "“later”", "y")], y=30, h=96, gap=12, size=15, subsize=12)
lc_problem.note(380, 176, "a page doesn't change habits", "red", size=19)

lc_analogy = Doodle(760, 220, "Doodle of a town introducing a new recycling scheme. A leaflet through every door changes little. What works: one street tries it first with help, the bins are easier than before, neighbours see the clean street and the lower bill, and the next streets ask to join. People adopt what makes their own life easier.",
                    "A leaflet changes little. One street first, with help, easier bins, a visible win, and the next streets ask.")
lc_analogy.row([("one street", "tries it, helped", "y"), ("easier bins", "less effort", "blue"), ("visible win", "clean, cheaper", "green"), ("others ask", None, "green")], y=40, h=96, gap=14, size=16, subsize=12)
lc_analogy.note(380, 186, "people adopt what makes their own life easier", "pen", size=18)

lc_how = Doodle(760, 400, "How SLOs spread to Larder's product teams, July to October 2028. A pilot with one willing team: Cho's payments team, in July, with Lotte sitting with them for two days to write SLOs, set burn alerts and delete five noisy alerts; their night pages fell from 4 to 1 a month. Made easy: the golden path now creates the SLO file, alerts and readiness checklist, and the reliability team offers a two-hour session per team. A visible win: Cho shows the pager numbers at the engineering all-hands on Thursday 31 August. Patience with the resistant: Dee's team asks to join in September, after their own rota merge; the data team in October. By October: four of five teams have SLOs for their services. Nobody was ordered to.",
                "A willing pilot, help in person, an easier path, a visible win, patience. Four of five teams by October; nobody ordered.")
lc_how.row([("pilot", "Cho's team, July · Lotte 2 days", "y"), ("easier", "golden path + 2-h session", "blue"), ("visible win", "all-hands, 31 Aug", "green"), ("patience", "Dee: Sep · data: Oct", "green")], y=14, h=110, gap=14, size=17, subsize=11)
lc_how.box(14, 150, 732, 64, "payments: night pages 4 → 1 a month · 5 noisy alerts deleted", "paper", size=15)
lc_how.row([("June", "1 of 5 teams", "pink"), ("October", "4 of 5 teams", "green")], x=110, y=240, h=80, w=250, gap=40, size=19, subsize=15, arrows=True)
lc_how.note(380, 360, "nobody was ordered to", "red", size=18)

LEADING_CHANGE = dict(
    slug="leading-change",
    kicker="a.k.a. “organisational change management”",
    tldr="New ways of working spread when they <b>make people's own lives easier</b>, not when a page says they should. Start with <b>one willing team</b>, help them <b>in person</b>, make the new way <b>easier than the old</b> (templates, tools), show a <b>visible win</b> in their numbers, and be <b>patient</b> with the rest. Resistance is often a fair question (“what does this cost us?”) waiting for a good answer.",
    chips=[("Family", "leading"), ("Lives in", "a pilot, the golden path templates, the all-hands slot"), ("Pairs with", "who runs what, SLOs (vol. 4), Ana's influencing without authority")],
    itil=dict(groups=["general"], chain=["engage", "improve"], practices=["organisational change management", "relationship management"],
              sre="(SRE adoption by teams; engagement models)", principles=["Collaborate and promote visibility", "Start where you are"],
              older="ITIL v3: organisational change (in service transition)"),
    problem_side="Larder, June 2028",
    problem="""  <p class="lead">With “build it, run it” as the model, the reliability team wants every product team to set <b>SLOs, error budgets and readiness checks</b> for its own services. Eli sends a well-written page to all five teams. <b>Dee's team</b> answers “more process, less building”. <b>Two teams</b> don't answer at all. Ben's team already does it for Ordering. <span class="hl-pink">A page from the reliability team isn't changing anyone's habits.</span></p>
  <ul>
    <li>People hear “more work” before they hear “less pain”.</li>
    <li>A central team asking others to change sounds like a demand.</li>
    <li>Silence isn't agreement.</li>
  </ul>""",
    problem_figs=[lc_problem],
    meanwhile=[("architect-6", "influencing-without-authority", "Ana's influencing without authority: change what teams do by making it their idea, their win and the easy path.",
                "Eli does the same for SLOs: a willing pilot, help in person, the golden path, a win shown at the all-hands, and patience.")],
    analogy_side="the town's new recycling",
    analogy="""  <p>A town introducing a new recycling scheme finds that <b>a leaflet through every door</b> changes little. What works: <b>one street tries it first</b>, with help; the new bins are <b>easier than before</b>; neighbours see the clean street and the lower bill; and the <b>next streets ask to join</b>. People adopt what makes their own life easier.</p>""",
    analogy_figs=[lc_analogy],
    map=[("A leaflet through every door", "A page sent to five teams"),
         ("One street first, with help", "Cho's team, with Lotte for two days"),
         ("Easier bins", "The golden path creates SLOs and alerts"),
         ("The clean street", "Payments' night pages 4 → 1"),
         ("Next streets ask to join", "Dee's team in September, data in October")],
    how_side="a willing pilot, help in person, an easier path, a visible win, patience",
    how="""  <p>Eli changes approach in <b>July</b>:</p>
  <ul>
    <li><b>A willing pilot</b>: Cho's payments team, the most curious. <b>Lotte sits with them for two days</b>: they write SLOs together, set burn-rate alerts, and delete five noisy alerts. Their night pages fall from <b>4 to 1 a month</b>.</li>
    <li><b>Make it easier than before</b>: the golden path now creates the SLO file, burn alerts and readiness checklist for any service, and the reliability team offers a <b>two-hour session</b> per team. Doing it is now less work than not doing it.</li>
    <li><b>A visible win, told by the team</b>: <b>Cho</b>, not Eli, shows the pager numbers at the engineering all-hands on <b>Thursday 31 August</b>.</li>
    <li><b>Patience, and listening</b>: Dee's “more process” was a fair worry about time. Her team's rota merge (this volume) answered it, and in <b>September</b> they ask to join. The data team follows in October.</li>
  </ul>
  <p>By <b>October</b>, <b>four of five teams</b> have SLOs for their own services. Nobody was ordered to.</p>""",
    how_figs=[lc_how],
    steps=[("Find a willing team", "Curious, not forced."),
           ("Help in person", "Sit with them; do it together."),
           ("Make the new way easier than the old", "Templates, tools, the golden path."),
           ("Let them show their win", "Their numbers, their voice."),
           ("Listen to resistance", "It's often a fair question about cost."),
           ("Be patient", "Next teams ask when they see it working.")],
    vocab=[("Organisational change", "Changing how people and teams work, not just systems."),
           ("Pilot", "A first, small use of a change with a willing group."),
           ("Adoption", "People choosing to use a new way of working."),
           ("Resistance", "Pushback, often carrying a real concern."),
           ("Early adopters", "The first people or teams willing to try something."),
           ("Path of least resistance", "Making the desired way the easiest one.")],
    code=dict(file="ops/adoption/slos-2028.md", note="July – October 2028", plain=True, src="""
team          when       how                                   result
Ordering      2027       (already, tier 1)                     —
Payments      Jul 2028   pilot · Lotte 2 days · 5 alerts gone  night pages 4 → 1 / month
                         Cho presents at all-hands, 31 Aug
Apps (Dee)    Sep 2028   asked to join after the rota merge    SLOs for 3 services
Data          Oct 2028   2-hour session                        SLOs for 2 pipelines
Business      —          not yet (busy with Haarlem)           offered again in Dec

made easier   golden path creates SLO file + burn alerts + readiness checklist
never         a mandate · a deadline · a dashboard of who hasn't done it
"""),
    tools="tools: one willing team, a few days of in-person help, templates in the golden path, and an all-hands slot.",
    ladder=[("a page to everyone", ["Compliance or silence.", "“More process.”"]),
            ("pilot, help, easy path, visible win", ["Teams ask to join.", "Resistance listened to."]),
            ("a community of practice", ["Teams teach each other.", "Reliability team as coach."]),
            ("it's just how we work", ["New teams start with it.", "Nobody remembers the change."])],
    ladder_now=1,
    baseline="Each line compares <b>sending a page to five teams</b> to <b>a willing pilot, help in person, an easier path, a visible win and patience</b>.",
    ratings=[(2, 3, "More services measured by what users feel."),
             (2, 3, "Teams own their reliability."),
             (3, 3, "Neutral."),
             (3, 3, "Neutral."),
             (2, 4, "Four of five teams with SLOs."),
             (3, 3, "Neutral."),
             (3, 3, "Neutral."),
             (2, 4, "Payments' nights 4 → 1."),
             (3, 3, "Weeks of help, not a mandate.")],
    pitfalls=[("Change by memo", "Compliance or silence.", "a pilot, in person."),
              ("Starting with the most resistant", "A fight you'll lose.", "the most willing first."),
              ("More work than before", "Nobody adopts it.", "make it easier than the old way."),
              ("Dismissing resistance", "You miss the real problem.", "listen: it's often about cost or time.")],
    use=["You want other teams to change how they work.", "A memo or page had no effect.", "A central team is seen as imposing process.", "A good practice works for one team and should spread."],
    skip=["Changes required by law with a deadline: still help, but say it plainly."],
    related=["<b>Influencing Without Authority</b> (Ana, vol. 6)", "<b>How Good Is Good Enough?</b> (vol. 4)", "<b>Who Runs What?</b> (this volume)", "<b>Let the Team Decide</b> (Sanne, vol. 1)"],
    quiz=[("Why didn't the page work?", "It asked for more work from a central team; it didn't make anyone's life easier."),
          ("Who was the pilot, and what changed for them?", "Cho's payments team; night pages fell from 4 to 1 a month."),
          ("How was the new way made easier?", "The golden path creates SLO files, alerts and checklists; two-hour sessions per team."),
          ("Why did Cho, not Eli, present at the all-hands?", "A team's own win in its own voice persuades better than the central team's."),
          ("What did Dee's “more process” really mean?", "A fair worry about time, answered by the rota merge.")],
    quiz_sit=[("The business team still hasn't set SLOs in December. Femke suggests making it mandatory. What do you suggest?", "Ask the team why (Haarlem took their autumn), offer the two-hour session at a better time, and show them payments' and apps' numbers. Mandate only if there's a real risk; usually patience costs less.")],
    try_it="Think of a practice you want other teams to adopt. Who's most willing? What would make it easier than their current way? What win would they see in their own numbers, and who should tell it?",
    remember="People adopt what <span class=\"hl\">makes their own life easier</span>. One willing team, help in person, an easier path, and <span class=\"hl\">their win in their voice</span>.",
    sources=["John P. Kotter, <i>Leading Change</i> (1996).",
             "Chip and Dan Heath, <i>Switch</i> (2010).",
             "AXELOS, <i>ITIL 4: Organisational change management</i> practice guide (2020)."],
)

# ------------------------------------------------------------------ 13 AI in Operations: Where It Helps, Where It Lies
ai_problem = Doodle(760, 260, "Doodle of Tuesday 25 July 2028, 17:20. During a SEV3 about database connections, Yusuf, three weeks in, asks the AI assistant for help. It answers confidently: restart the database primary to clear the connections. In Larder's setup that would trigger a failover in the 17:00 to 20:00 window. Yusuf checks the runbook first, which says the opposite. Earlier that month the same assistant had drafted three review write-ups that saved hours.",
                    "The same assistant: hours saved on write-ups, and a confident suggestion that would have caused a failover at the peak.")
ai_problem.box(14, 30, 350, 100, "review drafts", "green", sub="3 h → 1 h each", size=20, subsize=15)
ai_problem.box(396, 30, 350, 100, "“restart the primary”", "pink", sub="17:20 · would trigger a failover", size=19, subsize=14)
ai_problem.note(380, 180, "Yusuf checked the runbook first: it said the opposite", "red", size=17)

ai_analogy = Doodle(760, 220, "Doodle of a new, very fast intern who has read everything. Wonderful for first drafts, summaries and 'where would I find…?'. But the intern has never been in this building, sometimes guesses with total confidence, and is never allowed to touch the boiler controls. Every draft is checked by someone who knows.",
                    "A very fast intern who has read everything: great drafts, sometimes confidently wrong, never at the boiler.")
ai_analogy.icon("book", 60, 50, 1.3)
ai_analogy.box(170, 40, 270, 100, "drafts · summaries", "green", sub="fast, helpful", size=18, subsize=14)
ai_analogy.box(470, 40, 276, 100, "the boiler controls", "pink", sub="never", size=18, subsize=14)
ai_analogy.note(450, 190, "checked by someone who knows the building", "pen", size=18)

ai_how = Doodle(760, 400, "Larder's rules for AI in operations, from August 2028, built on Lena's rules from Sanne's trial (an approved tool; every fact checked; the sender owns it; say when AI drafted it). Good uses: draft an incident timeline from the chat (about 90 percent right); draft a review write-up (3 hours to 1); summarise a long log; explain an unfamiliar configuration; suggest a runbook from incident notes. Never: run or approve anything in production; decide during an incident; paste customer personal data or secrets into prompts. Suggestions about production are checked against the runbook and tested before they become a runbook step. AI-drafted documents say so at the top.",
                "Good for drafts, summaries and explanations. Never acts on production, never decides, never sees customer data.")
ai_how.box(14, 14, 360, 160, None, "green")
ai_how.head(194, 42, "good uses", size=18)
for i, t in enumerate(["timeline drafts (≈ 90 % right)", "review drafts: 3 h → 1 h", "summarise logs · explain config", "suggest runbooks (then test)"]):
    ai_how.text(194, 72 + i * 26, t, size=13)
ai_how.box(386, 14, 360, 160, None, "pink")
ai_how.head(566, 42, "never", size=18)
for i, t in enumerate(["run or approve in production", "decide during an incident", "customer personal data in prompts", "secrets in prompts"]):
    ai_how.text(566, 72 + i * 26, t, size=13)
ai_how.box(14, 196, 732, 64, "Lena's rules: approved tool · every fact checked · sender owns it · say AI drafted it", "blue", size=14)
ai_how.box(14, 276, 732, 60, "a suggestion about production → checked against the runbook → tested → then a step", "y", size=14)
ai_how.note(380, 370, "25 July: the runbook beat the confident answer", "pen", size=16)

AI_IN_OPS = dict(
    slug="ai-in-ops",
    kicker="a.k.a. “AI assistants in operations, with care”",
    tldr="AI assistants are useful in operations for <b>drafts, summaries and explanations</b>: incident timelines, review write-ups, long logs, unfamiliar configuration. They're also <b>confidently wrong</b> sometimes, and they don't know your system. So: an approved tool; <b>every fact checked</b>; the person who sends it owns it; say when AI drafted it. <b>Never let it act on production or decide during an incident</b>, and never paste customer data or secrets into it.",
    chips=[("Family", "leading"), ("Lives in", "ops/ai.md, built on Lena's rules"), ("Pairs with", "post-incident reviews (vol. 2), runbooks (vol. 1), Sanne's AI in project work")],
    itil=dict(groups=["general"], chain=["improve", "deliver"], practices=["knowledge management", "information security management", "continual improvement"],
              sre="(automation with humans in the loop; never trust an unverified action)", principles=["Optimise and automate", "Think and work holistically"],
              older="(not in ITIL v3)"),
    problem_side="Larder, July 2028",
    problem="""  <p class="lead">Eli tries an approved AI assistant for operations work in June and July, under Lena's rules from Sanne's trial. Some uses are excellent: three review write-ups drafted in an hour each instead of three. Then, on <b>Tuesday 25 July at 17:20</b>, during a SEV3 about database connections, Yusuf, three weeks into the job, asks it for help. It answers confidently: <b>restart the database primary</b> to clear the connections. <span class="hl-pink">In Larder's setup that would trigger a failover inside the 17:00–20:00 window.</span> Yusuf checks the runbook first, and the runbook says the opposite.</p>
  <ul>
    <li>Fluent answers sound like knowledge of your system.</li>
    <li>New people are the most likely to trust them under pressure.</li>
    <li>Without rules, it's a matter of luck who checks.</li>
  </ul>""",
    problem_figs=[ai_problem],
    meanwhile=[("project-6", "ai-in-project-work", "Sanne's AI trial (1 Feb – 10 Mar 2028) and Lena's rules: an approved tool, every fact checked, the sender owns it, say when AI drafted it; her mistake: an unchecked draft said “Ghent lease signed”.",
                "Eli applies the same rules to operations and adds his own: never act on production, never decide in an incident, no customer data in prompts.")],
    analogy_side="the very fast intern",
    analogy="""  <p>Picture a new intern who is very fast and <b>has read everything</b>. Wonderful for first drafts, summaries and “where would I find…?”. But the intern has <b>never been in this building</b>, sometimes guesses with total confidence, and is <b>never allowed to touch the boiler controls</b>. Every draft is checked by someone who knows the building.</p>""",
    analogy_figs=[ai_analogy],
    map=[("First drafts and summaries", "Timeline drafts, review drafts, log summaries"),
         ("Never been in the building", "Doesn't know Larder's failover setup"),
         ("Confident guesses", "“Restart the primary”"),
         ("The boiler controls", "Production: never acted on by the assistant"),
         ("Checked by someone who knows", "Every fact checked against the runbook")],
    how_side="useful for drafts; never for production; every fact checked",
    how="""  <p>From <b>August</b> Larder's operations rules sit on top of Lena's four rules (an approved tool, every fact checked, the sender owns it, say when AI drafted it):</p>
  <ul>
    <li><b>Good uses</b>: drafting an incident timeline from the chat (about <b>90 %</b> right, and the scribe corrects the rest); drafting a review write-up (<b>3 hours → 1</b>); summarising a long log; explaining an unfamiliar configuration file; suggesting a runbook from incident notes.</li>
    <li><b>Never</b>: run or approve anything in production; <b>decide during an incident</b> (the incident lead decides); paste <b>customer personal data or secrets</b> into a prompt.</li>
    <li><b>Suggestions about production</b> are checked against the runbook and tested on staging or in a game day before they become a runbook step.</li>
    <li><b>AI-drafted documents</b> say so at the top, so readers know to check.</li>
  </ul>
  <p>Yusuf's 25 July check becomes a story in the onboarding pack: the runbook beat the confident answer, and checking first was exactly right.</p>""",
    how_figs=[ai_how],
    steps=[("Use an approved tool only", "With the data rules your legal team set."),
           ("Use it for drafts and summaries", "Where a mistake is cheap and checked."),
           ("Check every fact", "Against runbooks, logs and people who know."),
           ("Never let it act on production", "Or decide in an incident."),
           ("Keep customer data and secrets out", "Of every prompt."),
           ("Label AI drafts", "So readers know to check.")],
    vocab=[("AI assistant", "A language-model tool that drafts, summarises and answers questions."),
           ("Hallucination", "A fluent, confident answer that is wrong."),
           ("Human in the loop", "A person checks and decides before anything happens."),
           ("Approved tool", "A tool legal and security have agreed for company data."),
           ("Grounding", "Checking AI output against real sources (runbooks, logs)."),
           ("Automation bias", "Trusting a machine's answer more than you should.")],
    code=dict(file="ops/ai.md", note="from August 2028 · on top of Lena's rules", plain=True, src="""
# AI in operations

Lena's rules   approved tool only · every fact checked · the sender owns it
               · say when AI drafted it
good for       timeline drafts from #incident (≈ 90 % right; scribe corrects)
               review drafts (3 h → 1 h) · log summaries · explaining config
               runbook suggestions → checked + tested before merging
never          run, approve or change anything in production
               decide during an incident (the lead decides)
               customer personal data or secrets in prompts
label          "AI-drafted, checked by <name>" at the top

25 Jul 2028 17:20  assistant: "restart the primary" · runbook: never in a window
                   (would fail over) · Yusuf checked first ✓ → onboarding story
"""),
    tools="tools: an approved assistant, the runbooks as the source of truth, Lena's rules, and a label template.",
    ladder=[("anyone, anything", ["Confident answers trusted.", "Data pasted in."]),
            ("rules: drafts yes, production never", ["Every fact checked.", "Labelled."]),
            ("grounded assistants", ["The assistant reads Larder's own runbooks and catalogue.", "Answers cite sources."]),
            ("assistants as team members", ["Trusted for drafting and search.", "Humans decide and act."])],
    ladder_now=1,
    baseline="Each line compares <b>using AI assistants without rules</b> to <b>drafts and summaries with every fact checked, and never on production</b>.",
    ratings=[(3, 3, "Neutral."),
             (2, 3, "Dangerous suggestions stopped by the rules."),
             (3, 3, "Neutral."),
             (2, 3, "No AI action on production."),
             (2, 3, "AI-drafted documents labelled."),
             (2, 4, "Review write-ups 3 h → 1 h."),
             (3, 3, "Neutral."),
             (2, 3, "Less writing after nights on call."),
             (3, 3, "A page of rules.")],
    pitfalls=[("Trusting fluency", "Confident isn't correct.", "check every fact against your sources."),
              ("Letting it act", "A wrong command in production.", "never on production."),
              ("Pasting customer data", "A privacy breach.", "approved tool, no personal data."),
              ("Unlabelled drafts", "Readers assume a person checked everything.", "label AI drafts.")],
    use=["Write-ups and summaries take hours.", "People already use AI informally.", "Onboarding new engineers to unfamiliar systems.", "Searching large logs."],
    skip=["Any decision or action on production during an incident."],
    related=["<b>Can AI Help?</b> (Sanne, vol. 6)", "<b>What Can We Learn from It?</b> (vol. 2)", "<b>What Do I Do at 3 a.m.?</b> (vol. 1)", "<b>When the Incident Is a Security Incident</b> (vol. 5)"],
    quiz=[("What are Lena's four rules?", "Approved tool, every fact checked, the sender owns it, say when AI drafted it."),
          ("What may the assistant never do?", "Act on or approve anything in production, decide during an incident, or receive customer data or secrets."),
          ("What happened on 25 July?", "The assistant suggested restarting the primary, which would cause a failover in the peak window; Yusuf checked the runbook first."),
          ("What's it good for?", "Timeline and review drafts, log summaries, explaining config, suggesting runbooks (then tested)."),
          ("What is automation bias?", "Trusting a machine's answer more than you should, especially under pressure.")],
    quiz_sit=[("A colleague wants to give the assistant access to run read-only queries on production to speed up investigations. What do you ask?", "Which data it could read (customer data?), whether the tool is approved for that, and who checks its conclusions. Read-only still exposes data; start with logs that have personal data masked, with Lena's agreement.")],
    try_it="List three operations tasks where a draft would save time and a mistake is cheap to catch. Write your “never” list. Try one draft task this week and note every fact you had to correct.",
    remember="Use AI for <span class=\"hl\">drafts, never decisions</span>. Check every fact, keep customer data out, and <span class=\"hl\">never let it touch production</span>.",
    sources=["NIST, <i>AI Risk Management Framework</i> (AI RMF 1.0, 2023).",
             "Ethan Mollick, <i>Co-Intelligence</i> (2024).",
             "AXELOS, <i>ITIL 4: Knowledge management</i> practice guide (2020)."],
)

# ------------------------------------------------------------------ 14 Growing Operations Engineers
go_problem = Doodle(760, 260, "Doodle of a conversation in August 2028. Bram, two years at Larder, asks Eli what his next step is. There is no career path for operations: the engineering ladder describes product engineers, shipping features. Lotte and Yusuf will ask the same. Eli realises the only person who has grown into his job is himself, by accident, at 160 percent.",
                    "“What's my next step?” No career path for operations, and the only person who grew into the job did it by accident.")
go_problem.box(14, 30, 300, 100, "Bram, 2 years", "y", sub="“what's next for me?”", size=20, subsize=14)
go_problem.box(346, 30, 400, 100, "engineering ladder", "paper", sub="written for feature builders", size=19, subsize=14)
go_problem.note(380, 180, "Eli grew into his job by accident, at 160 %", "red", size=18)

go_analogy = Doodle(760, 220, "Doodle of a hospital training junior doctors: clear grades, each with what you can do alone; real responsibility step by step, with a senior close by; and the seniors' job includes teaching. The best seniors measure themselves by how well the juniors handle a night on their own.",
                    "Clear grades, real responsibility step by step, seniors who teach, and a night handled alone as the measure.")
go_analogy.row([("grades", "what you do alone", "y"), ("real responsibility", "step by step", "blue"), ("seniors teach", "it's the job", "green")], y=40, h=96, gap=20, size=17, subsize=13)
go_analogy.note(380, 190, "measured by the juniors' night alone", "pen", size=18)

go_how = Doodle(760, 400, "Larder's operations career path from September 2028, written with Bram, Lotte and Yusuf and agreed with the engineering managers. Three levels: SRE, senior SRE, staff SRE. Each described by scope (a service, several services, the whole platform), incidents (handles, leads, leads major ones and teaches), automation (scripts, whole jobs, strategies) and teaching (learns, mentors, grows others). Growth by real responsibility: Bram led Ordering's readiness review; Lotte led the first incident without Eli; Yusuf owns the game days from October; incident lead rotates among all four. 1:1s every two weeks with a growth goal each. Bram promoted to senior SRE on 1 October 2028. Eli's own title becomes reliability lead, and his measure is how little he's needed at night.",
                "Three levels by scope, incidents, automation and teaching. Growth by real responsibility. Bram senior from 1 October.")
for i, (t, s, f) in enumerate([("SRE", "a service · handles incidents · scripts · learns", "paper"), ("senior SRE", "several services · leads incidents · whole jobs · mentors", "y"), ("staff SRE", "the platform · leads major · strategy · grows others", "green")]):
    go_how.box(14 + i * 248, 14, 236, 110, t, f, sub=s, size=19, subsize=11)
for i, (n, r) in enumerate([("Bram", "led Ordering's readiness review"), ("Lotte", "led the first incident without Eli"), ("Yusuf", "owns game days from October")]):
    go_how.box(14, 146 + i * 48, 160, 40, n, "blue", size=15)
    go_how.box(184, 146 + i * 48, 562, 40, r, "paper", size=14)
go_how.box(14, 296, 732, 50, "incident lead rotates among all four · 1:1s every 2 weeks · Bram senior SRE 1 Oct", "green", size=14)
go_how.note(380, 376, "Eli's measure: how little he's needed at night", "red", size=16)

GROWING = dict(
    slug="growing-ops-engineers",
    kicker="a.k.a. “workforce and talent management: growth”",
    tldr="Operations engineers grow when there's a <b>path</b> that describes their work (scope, incidents, automation, teaching), and when they're given <b>real responsibility, step by step</b>: leading a review, leading an incident, owning game days. Seniors' job includes <b>teaching</b>. Write the path with the people on it, have regular 1:1s with a growth goal each, and measure the lead by <b>how well the team does without them</b>.",
    chips=[("Family", "leading"), ("Lives in", "ops/career-path.md; 1:1s every two weeks"), ("Pairs with", "hiring SREs, humane on-call, Ana's growing architects")],
    itil=dict(groups=["general"], chain=["improve", "plan"], practices=["workforce and talent management"],
              sre="(SRE career ladders; mentoring; rotating incident command)", principles=["Collaborate and promote visibility", "Progress iteratively with feedback"],
              older="ITIL v3: (not covered as a practice)"),
    problem_side="Larder, August 2028",
    problem="""  <p class="lead">In August Bram, two years at Larder, asks Eli: <b>“What's my next step?”</b> There's no career path for operations, because the engineering ladder was written for product engineers shipping features. Lotte and Yusuf will ask the same soon. <span class="hl-pink">Eli realises the only person who has grown into the operations job at Larder is himself, by accident, at 160 %.</span></p>
  <ul>
    <li>Without a path, good people leave to grow somewhere else.</li>
    <li>Operations work (incidents, automation, teaching) is invisible on a feature ladder.</li>
    <li>Responsibility stays with the lead, so nobody else grows into it.</li>
  </ul>""",
    problem_figs=[go_problem],
    meanwhile=[("architect-6", "growing-architects", "Ana grows Cho and Dee into architects from May 2028: Cho led ADR 0029 alone in September; an architecture path on the career ladder from October.",
                "Eli does the same for operations: a path written with the team, and Bram, Lotte and Yusuf each given a piece of what used to be Eli's.")],
    analogy_side="training junior doctors",
    analogy="""  <p>A hospital trains junior doctors with <b>clear grades</b>, each describing what you can do alone, and <b>real responsibility, step by step</b>, with a senior close by. Teaching is <b>part of the senior's job</b>, not a favour. The best seniors measure themselves by how well the juniors handle <b>a night on their own</b>.</p>""",
    analogy_figs=[go_analogy],
    map=[("Grades of doctor", "SRE, senior SRE, staff SRE"),
         ("What you can do alone", "Scope, incidents, automation, teaching per level"),
         ("Responsibility step by step", "Lead a review, lead an incident, own game days"),
         ("Seniors teach", "Mentoring is part of the senior level"),
         ("A night handled alone", "9 October, without Eli")],
    how_side="a path by scope, incidents, automation and teaching; real responsibility",
    how="""  <p>In <b>September</b> Eli writes an operations career path <b>with Bram, Lotte and Yusuf</b>, and agrees it with the engineering managers. It has three levels (SRE, senior SRE, staff SRE), each described in four areas:</p>
  <ul>
    <li><b>Scope</b>: a service → several services → the platform.</li>
    <li><b>Incidents</b>: handles → leads → leads major incidents and teaches.</li>
    <li><b>Automation</b>: scripts → whole jobs → strategy.</li>
    <li><b>Teaching</b>: learns → mentors → grows others.</li>
  </ul>
  <p>Growth comes from <b>real responsibility</b>, not courses alone. <b>Bram</b> led Ordering's readiness review. <b>Lotte</b> led the first incident without Eli. <b>Yusuf</b> owns the game days from October. The incident lead rotates among all four. There are 1:1s every two weeks, each with one growth goal. <b>Bram is promoted to senior SRE on 1 October</b>. Eli's title becomes <b>reliability lead</b>, and he measures himself by how little he's needed at night.</p>""",
    how_figs=[go_how],
    steps=[("Write the path with the people on it", "Levels by what the work really is."),
           ("Describe scope, incidents, automation, teaching", "Not tools."),
           ("Hand over real responsibility", "Reviews, incidents, game days."),
           ("Rotate leadership roles", "Incident lead, review facilitator."),
           ("Hold regular 1:1s with a goal", "Every two weeks."),
           ("Measure the lead by the team", "How well it does without them.")],
    vocab=[("Career path (ladder)", "Levels describing growing scope and responsibility."),
           ("Senior SRE", "Leads incidents and whole automations; mentors others."),
           ("Staff SRE", "Shapes the platform and strategy; grows others."),
           ("Stretch assignment", "Responsibility a little beyond someone's current level."),
           ("Rotation", "Sharing a role (like incident lead) among the team."),
           ("1:1", "A regular conversation between a lead and a team member.")],
    code=dict(file="ops/career-path.md", note="written with Bram, Lotte, Yusuf · September 2028", plain=True, src="""
               SRE                    senior SRE                  staff SRE
scope          a service              several services            the platform
incidents      handles, follows lead  leads (SEV1–2)              leads major · teaches leads
automation     scripts                whole jobs, end to end      automation strategy
teaching       learns, asks           mentors one or two          grows others · hiring

growth by responsibility
  Bram    led Ordering's readiness review (Aug) → senior SRE, 1 Oct 2028
  Lotte   led the first incident without Eli (9 Oct)
  Yusuf   owns game days from Oct · facilitates reviews
  all     incident lead rotation · 1:1 every 2 weeks, one growth goal each
Eli       reliability lead · measure: how little he's needed at night
"""),
    tools="tools: a one-page path, a rotation, a 1:1 calendar, and the courage to hand over the interesting work.",
    ladder=[("grow by accident", ["No path.", "The lead keeps the interesting work."]),
            ("a written path and real responsibility", ["Rotation, 1:1s, promotions.", "Written with the team."]),
            ("growth across teams", ["Product engineers rotate into reliability.", "SREs into product teams."]),
            ("a pipeline of leads", ["The next reliability lead is already growing.", "The lead can leave without a gap."])],
    ladder_now=1,
    baseline="Each line compares <b>growing by accident</b> to <b>a written operations path and real responsibility, step by step</b>.",
    ratings=[(3, 3, "Neutral."),
             (3, 3, "Neutral."),
             (2, 3, "More people who can lead an incident."),
             (3, 3, "Neutral."),
             (2, 3, "Everyone knows what the next level looks like."),
             (3, 3, "Neutral."),
             (3, 3, "Neutral."),
             (1, 4, "Four people who can lead; the lead isn't needed at night."),
             (3, 3, "A path, a rotation, 1:1s.")],
    pitfalls=[("Borrowing the feature ladder", "Operations work invisible.", "describe scope, incidents, automation, teaching."),
              ("Keeping the interesting work", "Nobody else grows.", "hand it over, with support."),
              ("Courses instead of responsibility", "Knowledge without confidence.", "real work, step by step."),
              ("Writing the path alone", "It describes the lead's view.", "write it with the team.")],
    use=["Someone asks “what's next for me?”", "Only one person can lead incidents.", "A new team has formed.", "You want to be able to leave without a gap."],
    skip=["Never, if you want people to stay and grow."],
    related=["<b>Growing Other Architects</b> (Ana, vol. 6)", "<b>Hiring the First SREs</b> (this volume)", "<b>Did the Handover Work?</b> (this volume)", "<b>How Do I Get Better at This?</b> (Sanne, vol. 6)"],
    quiz=[("What four areas describe each level?", "Scope, incidents, automation, teaching."),
          ("How do people grow at Larder's reliability team?", "By real responsibility: leading reviews, incidents, game days, plus a rotation and 1:1s."),
          ("Who did what?", "Bram led the readiness review, Lotte the first incident without Eli, Yusuf owns game days."),
          ("When was Bram promoted?", "1 October 2028, to senior SRE."),
          ("How does Eli measure himself now?", "By how little he's needed at night.")],
    quiz_sit=[("A SEV1 starts at 18:00. Eli is free and could lead, but it's Lotte's turn on the rotation. What happens?", "Lotte leads; Eli offers to be on hand as an adviser, through her. Taking it back at the first big moment would undo the growth the rotation is for.")],
    try_it="Write down three things only you do in your team. For each, who could do it next, with your support? Hand one over this month, and agree a growth goal with that person.",
    remember="Grow people with <span class=\"hl\">real responsibility</span>, step by step, and measure yourself by <span class=\"hl\">how little you're needed</span>.",
    sources=["Camille Fournier, <i>The Manager's Path</i> (2017).",
             "Will Larson, <i>Staff Engineer</i> (2021).",
             "AXELOS, <i>ITIL 4: Workforce and talent management</i> practice guide (2020)."],
)

# ------------------------------------------------------------------ 15 Making It Yours
mi_problem = Doodle(760, 260, "Doodle of Monday 30 October 2028, two and a half years after Eli's first page. In March 2026: one person on call all year, 410 pages a month, 9 useful, nothing written down, the domain on an expired card, and Eli at 160 percent. In October 2028: a reliability team of four, product teams running their own services, 12 night pages across Larder, every major incident reviewed, restores in 22 minutes, and the first incident handled without him.",
                    "March 2026: one person, 410 pages, 160 %. October 2028: a team, 12 night pages, an incident handled without him.")
mi_problem.box(14, 30, 350, 140, None, "pink")
mi_problem.head(189, 58, "March 2026", size=18)
for i, t in enumerate(["on call: Eli, 52 weeks", "410 pages · 9 useful", "nothing written down · 160 %"]):
    mi_problem.text(189, 92 + i * 26, t, size=14)
mi_problem.box(396, 30, 350, 140, None, "green")
mi_problem.head(571, 58, "October 2028", size=18)
for i, t in enumerate(["a team of four + product rotas", "12 night pages across Larder", "9 Oct: handled without Eli"]):
    mi_problem.text(571, 92 + i * 26, t, size=14)
mi_problem.note(380, 216, "the job was never to be the one who keeps it running", "red", size=17)

mi_analogy = Doodle(760, 220, "Doodle of a gardener who started with one overgrown plot. She didn't plant everything at once: first she cleared one bed, then put in paths, then a water butt, then planted, season by season. Now there's a garden others tend with her, and her notebook says what she'd do first if she started again.",
                    "One overgrown plot, one bed at a time, season by season, until others tend it with you.")
mi_analogy.row([("clear one bed", None, "y"), ("paths", None, "paper"), ("water", None, "blue"), ("plant", None, "green"), ("others tend it", None, "green")], y=50, h=80, gap=12, size=15, arrows=True)
mi_analogy.note(380, 180, "start where you are; one bed at a time", "pen", size=18)

mi_how = Doodle(760, 400, "Eli's order, if he started again: one rung at a time. One: know what you run and who owns it (catalogue, dependencies, assets). Two: share the pager safely (rota, alerts worth waking for, runbooks, a service desk). Three: handle incidents together and learn without blame (severity, roles, reviews, problems). Four: change safely (kinds of change, windows, a way back). Five: promise and measure what users feel (SLIs, SLOs, budgets, an SLA you can keep). Six: practise the worst (restores, fallback, game days, security). Seven: build the team that doesn't need you (who runs what, hiring, on-call, handover, growth). Numbers, 2026 to 2028: useful pages 2 to about 80 percent; change failures 6 to 3 percent; restore 3 h 40 to 22 minutes; toil 41 to 19 percent; Eli's own night pages in October 2028: none.",
                "Seven steps, in this order, one rung at a time. And the numbers that moved.")
steps = ["1 know what you run", "2 share the pager safely", "3 incidents together", "4 change safely", "5 promise + measure", "6 practise the worst", "7 a team that doesn't need you"]
for i, t in enumerate(steps):
    r, c = divmod(i, 4)
    mi_how.box(14 + c * 186, 14 + r * 70, 172, 58, t, "green" if i == 6 else "y", size=13)
for i, (t, v) in enumerate([("useful pages", "2 % → ≈ 80 %"), ("change failures", "6 % → 3 %"), ("full restore", "3 h 40 → 22 min"), ("toil", "41 % → 19 %"), ("Eli's night pages, Oct 2028", "0")]):
    mi_how.box(14, 166 + i * 44, 420, 38, t, "paper", size=14)
    mi_how.box(444, 166 + i * 44, 302, 38, v, "green", size=15)

MAKING_IT_YOURS = dict(
    slug="making-it-yours",
    kicker="a.k.a. “start where you are”",
    tldr="This notebook is ninety practices, and nobody needs all of them at once. Start <b>where you are</b>: find the rung you're on for the few practices that hurt most, and climb <b>one rung at a time</b>. Eli's order, if he started again: know what you run, share the pager safely, handle incidents together, change safely, promise what users feel, practise the worst, and build the team that doesn't need you. The goal was never to be the one who keeps it running.",
    chips=[("Family", "leading"), ("Lives in", "your own first page"), ("Pairs with", "every note in the notebook; Sanne's “What Was It All For?”")],
    itil=dict(groups=["general"], chain=["plan", "improve", "engage", "design", "build", "deliver"], practices=["the service value system", "the guiding principles", "continual improvement"],
              sre="“hope is not a strategy”; reliability is a team sport", principles=["Start where you are", "Progress iteratively with feedback", "Keep it simple and practical"],
              older="ITIL v3: the service lifecycle"),
    problem_side="Larder, Monday 30 October 2028",
    problem="""  <p class="lead">Two and a half years after his first page, Eli reads his notebook from the start. In <b>March 2026</b>: one person on call all year, <b>410 pages a month</b> with 9 that mattered, nothing written down, the domain renewing on an expired card, and Eli at <b>160 %</b>. In <b>October 2028</b>: a reliability team of four, product teams running their own services, <b>12 night pages</b> a month across Larder, every major incident reviewed within a week, restores in <b>22 minutes</b>, and the first incident on the most critical service <b>handled without him</b>. <span class="hl-pink">The job was never to be the one who keeps it running.</span></p>
  <ul>
    <li>Ninety practices is too many to start with.</li>
    <li>Every organisation starts on a different rung.</li>
    <li>The order matters more than the completeness.</li>
  </ul>""",
    problem_figs=[mi_problem],
    meanwhile=[("project-6", "what-was-it-all-for", "Sanne's closing note, 25 September 2028: the six principles revisited, eight cities, and one line for her first day: “the plan is the team's, the truth is yours…”.",
                "Eli's closing note a month later: the seven steps he'd take again, and the numbers that moved since 30 March 2026.")],
    analogy_side="the gardener's overgrown plot",
    analogy="""  <p>A gardener who took on <b>one overgrown plot</b> didn't plant everything at once. First she <b>cleared one bed</b>, then laid paths, then put in a water butt, then planted, <b>season by season</b>. Now there's a garden others tend with her, and her notebook says what she'd do first if she started again: <b>the path to the shed</b>, so everyone else could find the tools.</p>""",
    analogy_figs=[mi_analogy],
    map=[("One overgrown plot", "Larder's operations in March 2026"),
         ("Clearing one bed", "A catalogue and an on-call rota"),
         ("Paths and water", "Alerts, runbooks, a service desk, incident roles"),
         ("Season by season", "One rung at a time, two and a half years"),
         ("Others tend it with her", "A reliability team and product teams running their own services")],
    how_side="seven steps, in order, one rung at a time",
    how="""  <p>Eli writes the order he'd follow if he started again, one rung at a time:</p>
  <ol>
    <li><b>Know what you run</b>: catalogue, dependencies, assets, owners (vol. 1).</li>
    <li><b>Share the pager safely</b>: a rota, alerts worth waking for, runbooks, one front door for problems (vol. 1).</li>
    <li><b>Handle incidents together and learn without blame</b>: severity, roles, communication, reviews, problems (vol. 2).</li>
    <li><b>Change safely</b>: kinds of change, windows, risk, a way back, keeping current (vol. 3).</li>
    <li><b>Promise and measure what users feel</b>: SLIs, SLOs, error budgets, an SLA you can keep (vol. 4).</li>
    <li><b>Practise the worst</b>: restores, paper fallback, game days, security, vendors (vol. 5).</li>
    <li><b>Build the team that doesn't need you</b>: who runs what, hiring, humane on-call, handover, growth (vol. 6).</li>
  </ol>
  <p>The numbers that moved: useful pages from <b>2 % to about 80 %</b>; change failures from <b>6 % to 3 %</b>; a full restore from <b>3 h 40 to 22 minutes</b>; toil from <b>41 % to 19 %</b>; and Eli's own night pages in October 2028: <b>none</b>. Most of them came from small rungs, climbed one at a time, by more and more people.</p>""",
    how_figs=[mi_how],
    steps=[("Pick the three practices that hurt most", "Not all ninety."),
           ("Find your rung on each", "Honestly, with evidence."),
           ("Climb one rung", "The next one, not the top."),
           ("Write it down as you go", "Your own notebook."),
           ("Bring others onto the rota and the work", "Early."),
           ("Look back every six months", "What moved, what's next.")],
    vocab=[("Start where you are", "Build on what exists; don't start from scratch."),
           ("Rung", "One step on a practice's ladder, from by hand to automatic."),
           ("Iterative improvement", "Small steps, each checked, rather than a big redesign."),
           ("Heroics", "Reliability that depends on individuals' extra effort."),
           ("Sustainable operations", "Reliability that lasts without heroics."),
           ("Your notebook", "Your own record of what you did and why.")],
    code=dict(file="ops/00-what-we-are-for.md", note="Eli · Mon 30 October 2028 (first written Mon 30 March 2026)", plain=True, src="""
# What IT operations at Larder is for                         (revised, 30 Oct 2028)

Customers buy      express · slots · office restock · Plus · eight cities, two countries
We keep running    tier 1: ordering, payments, Dispatch · tier 2–4: per the catalogue
Who                reliability team (Eli, Bram, Lotte, Yusuf) + every product team
A bad hour costs   ≈ €45k of orders at a Friday peak (2026: ≈ €15k)

                   Mar 2026            Oct 2028
on call            Eli, 52 weeks       4-person reliability rota + product rotas (≥ 6)
pages              410 / month, 2 %    ≈ 80 % useful · 12 night pages across Larder
incidents          nobody leads        roles, reviews ≤ 1 week, problems closed
changes            "be careful"        3 paths · windows · ways back · 3 % failures
full restore       never tried         22 min (drilled quarterly)
toil               41 % (Eli)          19 % (team)
Eli at 3 a.m.      always              not needed (9 Oct: 18 min, without him)
"""),
    tools="tools: this notebook's ladders, one honest look at where you are, and a page of your own.",
    ladder=[("heroics", ["One person holds it up.", "Nothing written."]),
            ("the first rungs, written", ["Catalogue, rota, alerts, runbooks.", "Incidents together."]),
            ("most practices on their way", ["Change, promises, continuity.", "A team forming."]),
            ("it runs without heroics", ["A team that doesn't need any one person.", "Improvement continues."])],
    ladder_now=3,
    baseline="Each line compares <b>Larder's operations on 30 March 2026</b> to <b>Larder's operations on 30 October 2028</b>.",
    ratings=[(2, 4, "Customers feel fewer and shorter problems."),
             (2, 4, "Change failures halved; problems closed."),
             (1, 4, "Restores 3 h 40 → 22 min; incidents in minutes."),
             (2, 4, "Three paths, windows, ways back."),
             (1, 4, "Everything on a page, with an owner."),
             (1, 4, "41 % → 19 % toil."),
             (2, 4, "Bills, tools and vendors managed."),
             (1, 4, "Four people, humane rotas, nobody indispensable."),
             (2, 3, "Many practices, each light.")],
    pitfalls=[("Trying to do everything at once", "Nothing finishes; people burn out.", "three practices, one rung each."),
              ("Copying someone else's top rung", "Automation before anything is written down.", "start where you are."),
              ("Doing it alone", "A new kind of hero.", "bring others in early."),
              ("Not writing it down", "The next person starts from scratch.", "keep your own notebook.")],
    use=["You've inherited “everything technical”.", "You're the person who keeps it running.", "You've read this notebook and wonder where to start.", "Every six months, to look back."],
    skip=["Never."],
    related=["<b>What Is IT Operations For?</b> (vol. 1)", "<b>What Was It All For?</b> (Sanne, vol. 6)", "<b>Where Are We Weak?</b> (this volume)", "<b>Handing Over a Product Area</b> (Grace, vol. 6)"],
    quiz=[("What's Eli's first step if he started again?", "Know what you run and who owns it."),
          ("What's the last step?", "Build the team that doesn't need you."),
          ("Why one rung at a time?", "Small steps finish and stick; doing everything at once finishes nothing."),
          ("Which numbers moved most?", "Useful pages 2 % → ≈ 80 %, restore 3 h 40 → 22 min, toil 41 % → 19 %, Eli's night pages to none."),
          ("What was the job, in the end?", "Not to be the one who keeps it running, but to build something that keeps running without one person.")],
    quiz_sit=[("A friend has just become the only operations person at a 40-person company. They ask where to start. What do you say?", "Write down what you run and who owns it this week; then get at least three more people onto a rota with alerts worth waking for and a runbook for each. Everything else can wait for the next rung.")],
    try_it="Write your own first page: what your customers buy, what you keep running, and what a bad hour costs. Then pick the three practices from this notebook that hurt most today, find your rung on each, and climb one.",
    remember="Start <span class=\"hl\">where you are</span>, one rung at a time, and remember the goal: <span class=\"hl\">a service that keeps running without heroes</span>, including you.",
    sources=["AXELOS, <i>ITIL 4 Foundation</i> (2019): the guiding principles.",
             "Betsy Beyer et al., <i>Site Reliability Engineering</i> (2016), and <i>The Site Reliability Workbook</i> (2018).",
             "Gene Kim et al., <i>The Phoenix Project</i> (2013)."],
)

NOTES = [IMPROVEMENT_REGISTER, LEADING_CHANGE, AI_IN_OPS, GROWING, MAKING_IT_YOURS]
