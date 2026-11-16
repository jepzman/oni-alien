# Series 2 · Book 3 · The Project Manager's Notebook · Vol. 2 · Starting, and one plan.
# Narrator: Sanne. Running case study: Larder (facts in docs/larder-casebook.md, "Book 3, Vol. 2").
# Spine: PMBOK Guide, Eighth Edition, Governance domain. Names are PMI's; every explanation is in our own words.

GOV = ["governance"]

# ------------------------------------------------------------------ 01 Should This Project Exist?
ch_problem = Doodle(760, 250, "Doodle of 19 February 2026. The Rotterdam launch has been running since the autumn. Sanne asks five people what it is for and gets five answers: a store, a date, proof for investors, more orders, a test of the platform. Nobody can point to a page where it was agreed.",
                    "A project four months old, and five different answers to “what is it for?”")
ch_problem.row([("“a store”", "Joost", "paper"), ("“a date”", "Femke", "paper"), ("“proof”", "Marco", "paper"), ("“orders”", "Priya", "paper"), ("“a test”", "Ana", "paper")], y=30, h=80, gap=10, size=17, subsize=14)
ch_problem.note(380, 160, "all true · none written down · none signed", "red", size=20)
ch_problem.note(380, 200, "running since the autumn without a charter", "pen", size=18)

ch_analogy = Doodle(760, 240, "Doodle of a ship's papers. Before a ship leaves port the owner signs one page: where it is going, what it carries, who the captain is, and how much the voyage may cost. The captain keeps it in the cabin. It isn't the route plan. It is the permission to sail.",
                    "The owner signs one page before the ship leaves: where to, with what, under which captain. The route comes later.")
ch_analogy.icon("ship", 30, 60, 1.5)
ch_analogy.row([("where + why", None, "y"), ("the captain", None, "blue"), ("the limits", None, "pink"), ("signed", "by the owner", "green")], x=190, y=60, h=70, w=132, gap=8, size=14, subsize=12)
ch_analogy.note(470, 186, "permission to sail, not the route", "pen", size=20)

ch_how = Doodle(760, 400, "The Rotterdam charter on one page, signed on 19 February 2026. Six boxes. Why: second city, proof that a city opens in weeks. Benefits: 500 orders a day by end of May, 90 percent on time by the end of summer, next city in 8 weeks or less. In and out: the store, the city in the platform, staff; not new app features. Limits: opening 27 April, 380 thousand euros, at most four hires. People: sponsor Joost, project manager Sanne, steering group. Done when: hypercare exit and handover to the store manager. Signed by Joost and Femke.",
                "One page, six boxes, two signatures. Everything later hangs from it.")
boxes = [("why", "second city · proof of speed", "y"), ("benefits", "500/day · 90 % · ≤ 8 weeks", "green"), ("in / out", "store · city · staff", "blue"),
         ("limits", "27 April · €380k · 4 hires", "pink"), ("people", "sponsor Joost · PM Sanne", "y"), ("done when", "hypercare exit + handover", "green")]
for i, (t, s, f) in enumerate(boxes):
    r, c = divmod(i, 3)
    ch_how.box(14 + c * 248, 14 + r * 130, 236, 112, t, f, sub=s, size=20, subsize=13)
ch_how.box(160, 290, 440, 70, "signed: Joost · Femke", "paper", sub="19 February 2026", size=20, subsize=14)

ch_deep1 = Doodle(760, 250, "Three documents that are often confused. The business case says whether the investment is worth it: benefits against costs and risks; the sponsor owns it. The charter says the project may start and names its goal, limits and manager; the sponsor signs it. The plan says how the project will be done; the project manager owns it. An arrow runs from business case to charter to plan.",
                  "Business case: is it worth it? Charter: you may start. Plan: here is how.")
ch_deep1.row([("business case", "is it worth it?", "y"), ("charter", "you may start", "green"), ("plan", "here is how", "blue")], y=40, h=100, gap=40, size=20, subsize=16, arrows=True)
ch_deep1.note(132, 180, "owner: sponsor", size=16)
ch_deep1.note(380, 180, "signed by: sponsor", size=16)
ch_deep1.note(628, 180, "owner: project manager", size=16)
ch_deep1.note(380, 226, "one feeds the next; none replaces another", "pen", size=18)

CHARTER = dict(
    slug="project-charter",
    kicker="a.k.a. “the project charter”",
    tldr="A <b>project charter</b> is a short document, signed by the sponsor, that says the project <b>exists</b>: why, for what benefit, what is in and out, within which limits, who is the sponsor and who is the project manager, and what “done” means. It is permission to start and to spend, not a plan. A project without one runs on <b>assumptions that differ from person to person</b>. If yours has none, write it now.",
    chips=[("Family", "starting"), ("Lives in", "page 1 of the project file"), ("Pairs with", "the value chain, the role card, the business case")],
    pmbok=dict(covers="starting a project: the charter, the business case behind it, authority for the project manager", domains=GOV,
               processes=["Initiate Project or Phase"], principles=["Focus on value", "Be an accountable leader"], focus=["initiating"],
               older="6th: “Develop Project Charter” (4.1). 7th: the charter as an artefact; initiation under the Stakeholder and Planning domains."),
    problem_side="Larder, 19 February 2026",
    problem="""  <p class="lead">Rotterdam has been “a project” since the Series B closed in September. On her way to a first plan, Sanne asks five people what it is for. Joost: a store. Femke: a date for the investors. Marco: proof that a city doesn't cost five months. Priya: more orders. Ana: a test of “a city is configuration”. <span class="hl-pink">All true, none written down, none signed.</span> She has six weeks of notes (a value chain, a role card, a scan) and no single page that authorises any of it.</p>
  <ul>
    <li>No agreed goal means every argument starts from zero.</li>
    <li>Sanne spends €380k on the strength of a hallway conversation.</li>
    <li>Nobody has said what “finished” is.</li>
  </ul>""",
    problem_figs=[ch_problem],
    analogy_side="the ship's papers",
    analogy="""  <p>Before a ship leaves port, the owner signs <b>one page</b>: where it is going and why, what it carries, who the captain is, what the voyage may cost. The captain keeps it in the cabin. It is not the route: the captain works that out. It is the <b>permission to sail</b>, and the thing both of them point to when a storm forces a choice.</p>""",
    analogy_figs=[ch_analogy],
    map=[("The owner", "Joost, the sponsor (with Femke)"),
         ("The captain named on the page", "Sanne, with her authority and her limits"),
         ("Where to, and why", "The reason and the three benefits"),
         ("What the voyage may cost", "27 April, €380k, four hires"),
         ("Not the route", "Not the plan: that comes next")],
    how_side="one page, six boxes, two signatures",
    how="""  <p>Sanne already has most of the content. She folds the <b>value chain</b>, the <b>role card</b> and the limits from her <b>scan</b> into one page with six boxes: <b>why</b>, <b>benefits</b>, <b>in and out</b>, <b>limits</b>, <b>people</b>, <b>done when</b>. The new parts are “out” (no new app features for Rotterdam) and “done when” (hypercare exit and handover to the store manager). Joost reads it in ten minutes, changes one word, and signs. Femke signs too. It becomes page 1 of the project file.</p>""",
    how_figs=[ch_how],
    steps=[("Write why, in two lines", "Linked to the strategy."),
           ("State the benefits with numbers and dates", "From the value chain."),
           ("Say what is in, and what is out", "“Out” prevents most arguments."),
           ("List the limits", "Date, money, people, rules."),
           ("Name the sponsor, the project manager and their authority", "Including what goes up."),
           ("Define “done”, and get it signed", "By the person who pays.")],
    vocab=[("Project charter", "The document that formally authorises a project and gives the project manager authority."),
           ("Business case", "The reasoning that the investment is worth making."),
           ("Sponsor", "The person who provides resources and answers for the project in the business."),
           ("Scope (high level)", "What the project will and won't deliver, in a few lines."),
           ("Success criteria", "How everyone will know the project worked."),
           ("Authorise", "Give formal permission to start and to spend.")],
    code=dict(file="rotterdam/01-charter.md", note="signed by Joost and Femke, 19 February 2026", plain=True, src="""
# ROTTERDAM LAUNCH · PROJECT CHARTER                                    v1 · 19 Feb 2026

WHY        Larder promised investors six cities by end 2027. Rotterdam is the second,
           and the proof that a city opens in weeks, not months (Zuid took five).
BENEFITS   500 orders a day by end May                       owner: Joost
           90 % express on time by the end of the summer     owner: Joost
           a launch playbook: next city in ≤ 8 weeks         owner: Femke
IN         store fitted, stocked and staffed · Rotterdam set up in the platform and apps
           · ~40 pickers and couriers trained · launch marketing · two weeks of hypercare
OUT        new app features for Rotterdam · Larder for Business · any change to Amsterdam
LIMITS     opening 27 April 2026 (lease) · budget €380k (reserve €6k) · max 4 new hires
PEOPLE     sponsor Joost · project manager Sanne · steering: Femke, Marco, Priya, Joost
AUTHORITY  Sanne runs the plan and spends within budget. To Joost: date at risk > 3 days,
           a change > €5,000, any change to what customers get at launch.
DONE WHEN  hypercare exit criteria met · store handed to the Rotterdam store manager ·
           closing report accepted by the steering group

Signed     Joost (sponsor)     Femke (CEO)
"""),
    tools="tools: one page, the value chain and role card you already have, and ten minutes with the sponsor.",
    deep_dive=dict(
        side="what belongs in a charter, and what to do when you arrive late",
        intro="A charter looks too simple to need a longer chapter. The trouble is in three places: it gets confused with the business case and the plan, it gets written too long, and on most real projects it gets written late or not at all. This chapter takes those in turn.",
        parts=[
            ("Business case, charter, plan", """  <p>Three documents, three questions, three owners.</p>
  <ul>
    <li>The <b>business case</b> asks <i>is this worth doing?</i> It compares benefits with costs and risks. The <b>sponsor</b> owns it, and it stays alive: if the answer becomes “no”, the project should stop.</li>
    <li>The <b>charter</b> says <i>you may start</i>. It takes the business case's conclusion, adds the goal, the limits and the named project manager, and is <b>signed by the sponsor</b>.</li>
    <li>The <b>plan</b> says <i>here is how</i>. The <b>project manager</b> owns it, the team makes it, and it changes often.</li>
  </ul>
  <p>At Larder the business case was never written as a document: it is the Series B condition and the lease. Sanne puts those two facts in the “why” box, so the charter doesn't pretend to an analysis that wasn't done.</p>""", [ch_deep1]),
            ("The test of each line: would we argue about it in April?", """  <p>A charter should fit on <b>one page</b>. To decide what goes in, Sanne uses one test: <i>is this something people might disagree about when the pressure is on?</i></p>
  <ul>
    <li><b>Out of scope</b> passes the test easily. In March someone will ask for “just one” Rotterdam feature. The line “OUT: new app features for Rotterdam” ends that conversation in a sentence.</li>
    <li><b>Done when</b> passes too. Without it, the project manager is still answering store questions in August.</li>
    <li><b>Authority</b> passes: the three triggers.</li>
    <li>A list of tasks, a schedule, the names of every team member: these <b>fail</b>. They belong in the plan, and they change.</li>
  </ul>""", []),
            ("Arriving late: the retro-charter", """  <p>Textbooks put the charter before the first day of work. Sanne arrived in week 16 of something already moving, which is how most project managers meet their projects. A late charter is still worth writing, with three adjustments.</p>
  <ol class="steps">
    <li><b>Write what is true now.</b><p>Not what should have been agreed in September. If the budget is already €380k with €6k of reserve, say so.</p></li>
    <li><b>Expect one real disagreement.</b><p>Writing it down will surface one. Here it was “done when”: Joost assumed Sanne would stay on Rotterdam through the summer; Femke needed her on Utrecht. Better found in February than in May.</p></li>
    <li><b>Get it signed anyway.</b><p>The signature is the point. It turns “everyone knows” into “we agreed”.</p></li>
  </ol>
  <p>The same page is used again at the <b>start of each phase</b>, in a smaller form: before stocking begins, someone must say “yes, go” (the gates, two notes on).</p>""", []),
        ]),
    dial=[("Light", "a two-week internal job", ["Three lines in a message: why, done when, who decides.", "A thumbs-up from the sponsor.", "No document."]),
          ("Standard", "Rotterdam", ["One page, six boxes.", "Signed by the sponsor.", "Page 1 of the project file."]),
          ("Heavy", "a large or contracted project", ["A full business case first.", "A multi-page charter with assumptions and risks.", "Approval by a board; funding released in stages."])],
    baseline="Each line compares <b>a project running on five people's assumptions</b> to <b>a one-page charter signed by the sponsor</b>.",
    ratings=[(2, 5, "Why and benefits are agreed in writing."),
             (2, 4, "Limits are stated, so forecasts have something to hold on to."),
             (2, 4, "“Out” and “done when” prevent two classic surprises."),
             (2, 4, "One page anyone can read."),
             (2, 5, "The sponsor has signed."),
             (3, 3, "Neutral."),
             (3, 3, "Neutral: it is short on purpose."),
             (3, 3, "Neutral."),
             (4, 4, "One page, ten minutes to sign.")],
    pitfalls=[("No charter", "“Everyone knows why.”", "write it, even late."),
              ("A ten-page charter", "It becomes a plan and goes stale.", "one page; the test is “would we argue about it?”."),
              ("Written by the project manager, signed by nobody", "No authority behind it.", "the sponsor signs."),
              ("No “out”, no “done when”", "Scope creeps and the project never ends.", "write both.")],
    use=["Before any project starts.", "When you inherit a project without one.", "At the start of each phase, in small.", "When people disagree about the goal."],
    skip=["Never. For tiny work it is three lines."],
    related=["<b>What Is It All For?</b> (vol. 1)", "<b>What Is My Job Here?</b> (vol. 1)", "<b>Business case one-pager</b> (Grace, vol. 2)", "<b>Who Decides What?</b> (next note)"],
    quiz=[("Who signs the charter?", "The sponsor."),
          ("Charter or plan: “the builder hands over on 3 April”?", "Plan. It is a detail of how, and it may change."),
          ("Why write “out of scope”?", "So that a later request can be answered by pointing at an agreed line."),
          ("In March Priya asks for a Rotterdam-only loyalty feature “since we're launching anyway”. What does Sanne do?", "Point to OUT in the charter. If Priya still wants it, it is a change for the sponsor to decide, not a favour."),
          ("Sanne joined in week 16. Is it too late for a charter?", "No. Write what is true now and get it signed; expect it to surface one disagreement.")],
    try_it="Write your project's charter in six boxes: why, benefits, in / out, limits, people, done when. Which box can't you fill? Take that question to your sponsor this week.",
    remember="One page, signed by the <span class=\"hl\">owner</span>: permission to <span class=\"hl\">sail</span>, not the route.",
    sources=["Project Management Institute, <i>PMBOK Guide</i>, Eighth Edition (2025): Governance domain, initiating.",
             "Project Management Institute, <i>PMBOK Guide</i>, Sixth Edition (2017): 4.1 Develop Project Charter.",
             "Project Management Institute, <i>Business Analysis for Practitioners</i> (2015): business cases."],
)

# ------------------------------------------------------------------ 02 Who Decides What?
gs_problem = Doodle(760, 250, "Doodle of late February 2026. One question, should the store open on Sundays from day one, has been to four meetings in two weeks. Joost thought Priya decided. Priya thought Joost did. Sanne has it on her list as open. Meanwhile the rota and the adverts wait.",
                    "One question, four meetings, two weeks. Everyone thought someone else decided.")
gs_problem.row([("meeting 1", "“ask Priya”", "paper"), ("meeting 2", "“ask Joost”", "paper"), ("meeting 3", "“let's park it”", "paper"), ("meeting 4", "“who decides?”", "pink")], y=30, h=80, gap=34, size=16, subsize=14, arrows=True)
gs_problem.note(380, 160, "Sunday opening from day one?", "pen", size=20)
gs_problem.note(380, 200, "the rota and the adverts are waiting", "red", size=18)

gs_analogy = Doodle(760, 240, "Doodle of a football match. The players decide every pass. The coach decides the line-up and the substitutions. The club board decides the budget and the transfers. The referee applies rules nobody on the pitch can change. Nobody phones the board about a throw-in.",
                    "Players decide the pass, the coach the line-up, the board the budget. Nobody phones the board about a throw-in.")
gs_analogy.row([("players", "every pass", "green"), ("coach", "line-up, tactics", "y"), ("board", "budget, transfers", "pink"), ("referee", "the rules", "paper")], y=50, h=90, size=18, subsize=14)
gs_analogy.note(380, 200, "each decision at the level that has the facts and the right", "pen", size=18)

gs_how = Doodle(760, 460, "Rotterdam's governance on one page, agreed at the steering group of 27 February 2026. Four levels. The teams decide how the work is done. Sanne decides how the plan fits together, within the charter. The sponsor, Joost, decides when a trigger is hit: three days, five thousand euros, launch scope. The steering group, Femke, Marco, Priya and Joost, meets every second Friday for thirty minutes and decides the launch date, the budget and go or no-go. To the side: two people with a veto in their own area, Marco on spending and Lena on contracts and personal data.",
                "Four levels, what each decides, and how fast. Two vetoes at the side.")
levels = [("steering group", "date · budget · go / no-go", "every 2nd Friday, 30 min", "pink"), ("sponsor · Joost", "the three triggers", "within 2 working days", "y"),
          ("Sanne", "how the plan fits together", "same day", "blue"), ("the teams", "how the work is done", "on the spot", "green")]
for i, (t, s, speed, f) in enumerate(levels):
    y = 14 + i * 90
    w = 300 + i * 60
    gs_how.box(270 - w // 2 + 20, y, w, 74, t, f, sub=s, size=18, subsize=14)
    gs_how.note(660, y + 42, speed, "pen", size=15)
gs_how.box(120, 380, 520, 64, "vetoes", "paper", sub="Marco: spending · Lena: contracts, personal data", size=17, subsize=14, dash=True)

GOVERNANCE = dict(
    slug="governance-structure",
    kicker="a.k.a. “project governance”: the sponsor, the steering group and decision levels",
    tldr="<b>Governance</b> is the answer to three questions: <b>who decides what</b>, <b>how fast</b>, and <b>how do they find out</b> a decision is needed. A small project needs a sponsor, a steering group that meets on a rhythm, and a few written limits that send decisions up. Agree it <b>before the first hard decision</b>: in the middle of one, every rule looks like a move in the argument.",
    chips=[("Family", "starting"), ("Lives in", "one page, next to the charter"), ("Pairs with", "decision rights, the role card, escalation")],
    pmbok=dict(covers="the governance framework: sponsor, steering group, decision authority, how the project is overseen", domains=GOV,
               processes=["Initiate Project or Phase"], principles=["Be an accountable leader", "Build an empowered culture"], focus=["initiating", "monitoring"],
               older="6th: “project governance” in 2.4 and the sponsor's role. 7th: governance under the system for value delivery."),
    problem_side="Larder, 27 February 2026",
    problem="""  <p class="lead">Should the Rotterdam store open on <b>Sundays from day one</b>? The question has been to four meetings in two weeks. Joost thought Priya decided, because it changes the slots customers see. Priya thought Joost did, because it's his rota. Sanne has it on her list as “open”. <span class="hl-pink">Nobody is avoiding it. Nobody knows whose it is.</span> The rota and the adverts are waiting.</p>
  <ul>
    <li>Decisions without an owner go round in circles.</li>
    <li>The steering group meets, but nobody knows what it's for.</li>
    <li>Sanne's three triggers exist, but only between her and Joost.</li>
  </ul>""",
    problem_figs=[gs_problem],
    analogy_side="a football club",
    analogy="""  <p>At a football club the <b>players</b> decide every pass. The <b>coach</b> decides the line-up and the substitutions. The <b>board</b> decides the budget and the transfers. The <b>referee</b> applies rules nobody on the pitch can change. It works because everyone knows it in advance. Nobody phones the board about a throw-in, and no player buys a striker.</p>""",
    analogy_figs=[gs_analogy],
    map=[("Players", "The seven workstream teams"),
         ("Coach", "Sanne"),
         ("Board", "The steering group: Femke, Marco, Priya, Joost"),
         ("The club's owner", "Joost as sponsor"),
         ("The referee", "Marco on spending; Lena on contracts and personal data")],
    how_side="four levels, a rhythm, and what goes up",
    how="""  <p>At the steering group of <b>27 February</b> Sanne brings one page. <b>Four levels</b>: the teams (how the work is done), Sanne (how the plan fits together), the sponsor (the three triggers), the steering group (the launch date, the budget, go / no-go). For each: <b>what it decides</b> and <b>how fast</b>. Two vetoes that already exist at Larder are written in: Marco on spending, Lena on contracts and personal data. The steering group gets a rhythm (every second Friday, 30 minutes) and a rule: papers the day before, decisions in the room. Sunday opening is decided in four minutes: Joost's call, Priya consulted, not at launch.</p>""",
    how_figs=[gs_how],
    steps=[("List the kinds of decision the project will need", "Ten is plenty."),
           ("Put each at the lowest level that has the facts and the right", "Most stay with the teams."),
           ("Write the limits that send a decision up", "Days, money, scope."),
           ("Give the steering group a purpose and a rhythm", "What it decides; when it meets."),
           ("Write in the vetoes that already exist", "Finance, legal, safety."),
           ("Agree it before you need it", "And put it next to the charter.")],
    vocab=[("Governance", "The framework of who decides, who oversees and how."),
           ("Steering group", "The sponsor and senior people who decide what is above the project manager."),
           ("Decision authority", "The right to make a certain kind of decision."),
           ("Threshold", "A limit that, when crossed, sends a decision up a level."),
           ("Terms of reference", "A short statement of what a group is for and how it works."),
           ("Veto", "The right to stop a decision in one's own area.")],
    code=dict(file="rotterdam/02-governance.md", note="agreed at the steering group, 27 February 2026", plain=True, src="""
# ROTTERDAM · WHO DECIDES WHAT

LEVEL            DECIDES                                         HOW FAST
The teams        how the work is done, sized and ordered         on the spot
Sanne            how the plan fits together; spend in budget;    same day
                 changes under €5,000 that move no milestone
Sponsor (Joost)  date at risk > 3 days · change > €5,000 ·       2 working days
                 anything that changes what customers get
Steering group   launch date · total budget · go / no-go ·       every 2nd Friday,
(Femke, Marco,   closing the project                             30 min; papers the
 Priya, Joost)                                                   day before
VETOES           Marco: spending outside budget · Lena: contracts, personal data

FRIDAYS          27 Feb · 13 Mar (baseline) · 27 Mar · 10 Apr · 24 Apr (go / no-go) ·
                 8 May · 22 May (closing)
FIRST USE        Sunday opening from day one → Joost decides, Priya consulted: not at launch
"""),
    tools="tools: one page, a recurring 30-minute meeting, and the habit of asking “whose decision is this?” first.",
    dial=[("Light", "one team and its manager", ["“You decide, unless it costs more than X.”", "A weekly chat with the sponsor.", "Nothing written beyond that."]),
          ("Standard", "Rotterdam", ["Four levels on one page.", "A fortnightly steering group.", "Thresholds and vetoes written down."]),
          ("Heavy", "many teams, vendors, public money", ["A project board with formal terms of reference.", "Stage approvals and audit.", "Delegated financial authority in writing."])],
    baseline="Each line compares <b>decisions wandering between meetings</b> to <b>four written levels, a rhythm and thresholds</b>.",
    ratings=[(3, 4, "Big decisions are made by those who own the benefit."),
             (2, 4, "Decisions stop costing weeks."),
             (2, 4, "Stuck decisions are visible."),
             (2, 4, "Everyone can see whose a decision is."),
             (2, 4, "The steering group knows what it's for."),
             (3, 4, "Most decisions stay with the teams."),
             (2, 4, "A change has a known route."),
             (3, 3, "Neutral."),
             (4, 3, "One meeting every two weeks.")],
    pitfalls=[("Everything goes to the steering group", "It becomes a bottleneck.", "thresholds; most decisions stay low."),
              ("A steering group that only listens", "Status in, nothing out.", "papers before, decisions in the room."),
              ("Rules invented mid-argument", "They look like tactics.", "agree them before the first hard decision."),
              ("Forgotten vetoes", "Finance or legal stops it late.", "write them in from the start.")],
    use=["At the start, with the charter.", "When a decision has been to three meetings.", "When a steering group has no clear purpose.", "When new parties join."],
    skip=["A sponsor and a team who already decide well together: keep it spoken."],
    related=["<b>Decision rights</b> (Ana, vol. 2)", "<b>Should This Project Exist?</b> (previous note)", "<b>When Do I Take It Upstairs?</b> (this volume)", "<b>Let the Team Decide</b> (vol. 1)"],
    quiz=[("What three questions does governance answer?", "Who decides what, how fast, and how they find out a decision is needed."),
          ("What does Rotterdam's steering group decide?", "The launch date, the total budget, go / no-go and closing."),
          ("Who can veto a contract?", "Lena."),
          ("Ben wants to swap the order of two app tasks inside a sprint. Who decides?", "Ben's team. It moves no milestone and costs nothing."),
          ("A decision has been discussed in three meetings. What is Sanne's first question in the fourth?", "“Whose decision is this?” Then that person decides, or a date is set for them to.")],
    try_it="Write down the last decision on your project that took too long. Whose was it? Now list five kinds of decision your project needs and put a name and a speed next to each.",
    remember="Nobody phones the <span class=\"hl\">board</span> about a <span class=\"hl\">throw-in</span>.",
    sources=["Project Management Institute, <i>PMBOK Guide</i>, Eighth Edition (2025): Governance domain.",
             "Project Management Institute, <i>Governance of Portfolios, Programs, and Projects: A Practice Guide</i> (2016).",
             "AXELOS, <i>Managing Successful Projects with PRINCE2</i> (2017): the project board."],
)

# ------------------------------------------------------------------ 03 May We Take the Next Step?
pg_problem = Doodle(760, 250, "Doodle of the story of Zuid again. In November 2024 stocking began in a store where the cold room wasn't finished. Pickers worked around builders. Two weeks later the shelves had to be emptied so the floor could be sealed. Nobody had asked whether the store was ready for the next step.",
                    "Zuid, 2024: stocking started in an unfinished store. Two weeks later the shelves were emptied again.")
pg_problem.row([("fit-out", "not finished", "pink"), ("stocking", "started anyway", "y"), ("shelves emptied", "to seal the floor", "pink")], y=40, h=90, gap=40, size=18, subsize=15, arrows=True)
pg_problem.note(380, 190, "nobody asked “are we ready for the next step?”", "red", size=19)

pg_analogy = Doodle(760, 240, "Doodle of a canal lock. A boat may only move to the next level when the gate behind is closed and the water is level. The lock keeper checks, then opens the gate. Rushing the gate floods the lock. The check takes minutes; the flood takes days.",
                    "A canal lock: the next gate opens only when the water is level. The check takes minutes.")
pg_analogy.row([("level 1", None, "blue"), ("gate", "is it level?", "y"), ("level 2", None, "blue"), ("gate", "is it level?", "y"), ("level 3", None, "blue")], y=50, h=90, gap=10, size=17, subsize=14)
pg_analogy.note(380, 196, "the keeper checks, then opens", "pen", size=20)

pg_how = Doodle(760, 400, "Rotterdam's five gates. Gate 1, 3 April: fit-out complete, may stocking start. Gate 2, 17 April: stock on shelves, may the rehearsal start. Gate 3, 20 April: app ready. Gate 4, 24 April: go or no-go for opening, decided by the steering group. Gate 5, 11 May: hypercare exit, may the project hand over. Below: what happened at Gate 1 on 3 April. Six criteria, five met. Fourteen snags, two of them blocking: a cold-room door seal and a missing fire extinguisher sign. The decision: go, with conditions, both fixed by 7 April.",
                "Five gates, each with criteria written in advance and three possible answers: go, go with conditions, no-go.")
pg_how.row([("G1 · 3 Apr", "fit-out done", "y"), ("G2 · 17 Apr", "stock in", "y"), ("G3 · 20 Apr", "app ready", "y"), ("G4 · 24 Apr", "go / no-go", "pink"), ("G5 · 11 May", "hypercare exit", "y")], y=14, h=76, gap=10, size=15, subsize=13)
pg_how.box(14, 116, 732, 150, None, "paper")
pg_how.head(380, 144, "Gate 1 · 3 April · may stocking start?", size=19)
pg_how.text(380, 178, "6 criteria · 5 met · 14 snags, 2 blocking", size=16)
pg_how.text(380, 206, "cold-room door seal · fire-extinguisher sign", size=16)
pg_how.note(380, 244, "decision: GO WITH CONDITIONS → both fixed by 7 April", "green", size=18)
pg_how.row([("go", None, "green"), ("go with conditions", "named, dated, owned", "y"), ("no-go", "and what happens next", "pink")], y=296, h=76, size=18, subsize=13)

GATES = dict(
    slug="phase-gates",
    kicker="a.k.a. “phase gates” and “go / no-go”",
    tldr="A <b>phase gate</b> is a planned point where someone with authority asks: <b>is the last step truly finished, and are we ready for the next?</b> The criteria are written <b>before</b> the gate, so the answer is a check, not a negotiation. There are three answers: <b>go</b>, <b>go with conditions</b> (named, dated, owned) or <b>no-go</b>. A gate closes one phase and starts the next, so it is initiating and closing in one meeting.",
    chips=[("Family", "starting"), ("Lives in", "the plan (the dates) and a one-page checklist per gate"), ("Pairs with", "the launch checklist, milestones, one-way doors")],
    pmbok=dict(covers="starting and ending phases: phase gates, entry and exit criteria, go / no-go decisions", domains=GOV,
               processes=["Initiate Project or Phase", "Close Project or Phase"], principles=["Embed quality into processes and deliverables"], focus=["initiating", "closing"],
               older="6th: “phase gate” in 1.2.4.3; Close Project or Phase (4.7). 7th: phase gate reviews under the Development Approach and Life Cycle domain."),
    problem_side="Larder, 2 March → 3 April 2026",
    problem="""  <p class="lead">Tomás tells Sanne the other half of the Zuid story. In November 2024 <b>stocking began in a store where the cold room wasn't finished</b>. Pickers worked around builders for two weeks; then every shelf was emptied so the floor could be sealed. Nobody decided that. It simply started, because the date said so. <span class="hl-pink">Rotterdam has five dates where the same thing could happen.</span></p>
  <ul>
    <li>A milestone date says when; it doesn't say “ready”.</li>
    <li>Under pressure, “nearly done” is treated as done.</li>
    <li>Problems are carried forward and get more expensive.</li>
  </ul>""",
    problem_figs=[pg_problem],
    meanwhile=[("product-3", "launch-checklist", "Grace's launch checklist (from 30 March) is the product side of Gate 4: eight areas with owners, two reds on 24 April.",
                "Sanne's Gate 4 on 24 April is where Grace's checklist is decided on: go, with two conditions.")],
    analogy_side="the canal lock",
    analogy="""  <p>In a <b>canal lock</b> a boat moves up one level at a time. The next gate opens only when the gate behind is shut and the water is level. The <b>lock keeper checks</b>, then opens. Nobody argues with the keeper, because the rule was there before the boat arrived. Rushing the gate floods the lock: minutes saved, days lost.</p>""",
    analogy_figs=[pg_analogy],
    map=[("Each water level", "A phase: fit-out, stocking, rehearsal, opening, hypercare"),
         ("The gate", "A phase gate on a milestone date"),
         ("“Is the water level?”", "Exit criteria, written on 2 March"),
         ("The lock keeper", "Sanne for gates 1–3 and 5; the steering group for gate 4"),
         ("Opening with a small leak, watched", "Go with conditions")],
    how_side="criteria first, then three possible answers",
    how="""  <p>On <b>2 March</b> Sanne turns the five shared milestones into <b>five gates</b> and, with each workstream lead, writes four to eight <b>criteria</b> per gate. Each gate gets a decider. Then the first test, <b>Gate 1 on 3 April</b>: may stocking start? Sanne, Joost, Tomás and the builder walk the store with the list. Five of six criteria are met. There are <b>14 snags</b>; two block stocking (a cold-room door seal, a missing fire-safety sign). Decision: <b>go with conditions</b>. Dry goods are stocked from Monday; chilled waits until both are fixed, by 7 April. The builder's handover is signed with the snag list attached.</p>""",
    how_figs=[pg_how],
    steps=[("Pick the points where a mistake would be expensive to carry forward", "Usually the shared milestones."),
           ("Write the criteria now, with the people who do the work", "Checkable, four to eight."),
           ("Name who decides at each gate", "The level that owns the risk."),
           ("At the gate, check the list on the spot", "Evidence, not opinions."),
           ("Choose: go, go with conditions, no-go", "Conditions get an owner and a date."),
           ("Record it, and start the next phase on purpose", "A line in the file.")],
    vocab=[("Phase", "A stretch of the project that ends with something agreed."),
           ("Phase gate", "A review at the end of a phase to decide whether to continue."),
           ("Exit criteria", "What must be true to leave a phase."),
           ("Entry criteria", "What must be true to start the next one."),
           ("Go / no-go", "A gate before something hard to undo, such as an opening."),
           ("Snag list", "Small defects found at handover, each with an owner and a date.")],
    code=dict(file="rotterdam/03-gates.md", note="criteria written 2 March · Gate 1 held 3 April 2026", plain=True, src="""
# ROTTERDAM · GATES

GATE  DATE     QUESTION                       DECIDES          RESULT
G1    3 Apr    fit-out done: start stocking?  Sanne + Joost    GO WITH CONDITIONS
G2    17 Apr   stock in: start rehearsal?     Sanne + Tomás
G3    20 Apr   app ready for Rotterdam?       Sanne + Grace
G4    24 Apr   open on 27 April?              steering group
G5    11 May   hypercare over: hand over?     Sanne + Joost

GATE 1 · 3 APRIL · criteria                                          met?
  1 builder's work complete against the drawings                     yes (14 snags)
  2 cold room holds 2–4 °C for 48 hours                              yes
  3 electrical and fire inspection passed                            yes
  4 shelving, fridges and charging points installed                  yes
  5 nothing open that stops safe stocking                            NO: 2 snags
  6 handover signed, warranty papers received                        yes

CONDITIONS   cold-room door seal (builder, 7 Apr) · fire-safety sign (builder, 6 Apr)
MEANWHILE    dry goods stocked from 6 Apr; chilled from 8 Apr
"""),
    tools="tools: a checklist per gate, written weeks ahead, and a walk-round with the people who can fix things.",
    dial=[("Light", "a small change", ["One question before release: “what must be true?”", "The owner says go.", "A line in chat."]),
          ("Standard", "Rotterdam", ["Five gates on the milestones.", "Four to eight written criteria each.", "Go, go with conditions, or no-go, recorded."]),
          ("Heavy", "large investments, safety, regulators", ["Formal stage gates with a board.", "Independent review of evidence.", "Funding released gate by gate."])],
    baseline="Each line compares <b>moving on because the date arrived</b> to <b>gates with criteria written in advance and three possible answers</b>.",
    ratings=[(3, 4, "Each gate asks if the project is still worth continuing."),
             (2, 4, "Unfinished work isn't carried into the next phase."),
             (2, 5, "Expensive mistakes are stopped at the gate."),
             (2, 4, "Everyone knows what “ready” means."),
             (2, 4, "The steering group decides on evidence."),
             (3, 4, "Leads wrote their own criteria."),
             (3, 3, "Neutral: a no-go costs days."),
             (2, 5, "Each phase is properly finished."),
             (4, 3, "A checklist and an hour per gate.")],
    pitfalls=[("Criteria written at the gate", "They bend to fit the day.", "write them weeks before."),
              ("Only “go” is possible", "A gate that can't say no is a ceremony.", "three answers, and a plan for no-go."),
              ("Conditions without owners", "“We'll sort it.”", "a name and a date for each."),
              ("A gate on everything", "Progress stops.", "only where carrying a mistake forward is expensive.")],
    use=["Before anything hard to undo.", "Where one team hands over to another.", "At the shared milestones of a hybrid.", "Before releasing more money."],
    skip=["Small, reversible steps: let them flow."],
    related=["<b>Launch checklist</b> (Grace, vol. 3)", "<b>One-way and two-way doors</b> (Ana, vol. 2)", "<b>What Do I Do When?</b> (vol. 1)", "<b>Are We Done?</b> (this volume)"],
    quiz=[("When are gate criteria written?", "Before the gate, with the people who do the work."),
          ("What are the three possible answers?", "Go, go with conditions, no-go."),
          ("Which two focus areas meet at a gate?", "Closing (the phase that ends) and initiating (the phase that starts)."),
          ("At Gate 2 the stock is on the shelves but 180 products fail the nightly price check. Go?", "Not a plain go. Either go with a condition (fixed and re-checked before G4, owner Eli) or no-go for the rehearsal, depending on whether the rehearsal can run without them."),
          ("Why not a gate after every task?", "Gates cost time. Use them where a mistake carried forward is expensive.")],
    try_it="Find the next point in your project where “nearly done” could slip through. Write five criteria for it today, and the name of the person who will say go, go with conditions, or no-go.",
    remember="The gate opens when the <span class=\"hl\">water is level</span>, not when the <span class=\"hl\">clock</span> says so.",
    sources=["Project Management Institute, <i>PMBOK Guide</i>, Eighth Edition (2025): Governance domain, initiating and closing a phase.",
             "Robert G. Cooper, <i>Winning at New Products</i> (5th ed., 2017): the Stage-Gate model.",
             "AXELOS, <i>Managing Successful Projects with PRINCE2</i> (2017): managing a stage boundary."],
)

# ------------------------------------------------------------------ 04 What's the Plan?
mp_problem = Doodle(760, 250, "Doodle of 20 February 2026. After the planning session each workstream has its own plan. The fit-out plan ends on 3 April. The stocking plan needs ten working days. The hiring plan has pickers starting on 13 April. Each is sensible alone. Put side by side, the pickers arrive a week after the stock they are supposed to put on the shelves.",
                    "Seven sensible plans. Side by side, the pickers arrive a week after the stock.")
mp_problem.row([("fit-out", "done 3 Apr", "y"), ("stocking", "6–17 Apr", "blue"), ("hiring", "pickers start 13 Apr", "pink")], y=40, h=90, size=19, subsize=15)
mp_problem.note(380, 180, "who puts the stock on the shelves from 6 April?", "red", size=20)
mp_problem.note(380, 216, "seven plans are not one plan", "pen", size=18)

mp_analogy = Doodle(760, 240, "Doodle of an orchestra. Each musician has their own part. The conductor has the full score: every part on one page, bar by bar, so that the violins and the drums arrive at the same place at the same time. The score is not more music. It is the same music, lined up.",
                    "Every musician has a part. The conductor has the score: the same music, lined up.")
mp_analogy.row([("violin part", None, "paper"), ("brass part", None, "paper"), ("drum part", None, "paper")], y=30, h=56, size=17)
mp_analogy.box(160, 116, 440, 70, "the full score", "y", sub="every part, bar by bar, lined up", size=20, subsize=15)
mp_analogy.arrow(132, 86, 260, 114)
mp_analogy.arrow(380, 86, 380, 114)
mp_analogy.arrow(628, 86, 500, 114)

mp_how = Doodle(760, 400, "The Rotterdam plan on a page, 20 February 2026. In the middle, the five milestones. Around it, six short parts that must agree with each other: scope, the 71 must-haves; schedule, the milestone chart; money, 380 thousand euros by workstream; people, who and when; risks, the top fifteen; and how we run it, the tailoring table. Lines between them show the checks: does the money cover the scope, do the people arrive when the schedule needs them, do the risks have time and money set aside.",
                "One page in the middle, six parts around it, and the checks that make them agree.")
mp_how.box(250, 150, 260, 90, "the plan on a page", "y", sub="5 milestones · 71 must-haves", size=18, subsize=14)
parts = [(20, 20, "scope", "71 must-haves"), (270, 20, "schedule", "milestone chart"), (520, 20, "money", "€380k by workstream"),
         (20, 300, "people", "who, and from when"), (270, 300, "risks", "top 15 · owners"), (520, 300, "how we run it", "tailoring table")]
for x, y, t, sub in parts:
    mp_how.box(x, y, 220, 76, t, "blue", sub=sub, size=18, subsize=14)
for x1, y1 in [(130, 96), (380, 96), (630, 96)]:
    mp_how.line(f"M{x1} {y1} L{380 + (x1 - 380) * 0.35:.0f} 150", thin=True)
for x1, y1 in [(130, 300), (380, 300), (630, 300)]:
    mp_how.line(f"M{x1} {y1} L{380 + (x1 - 380) * 0.35:.0f} 240", thin=True)
mp_how.note(125, 200, "do they agree?", "red", size=18)
mp_how.note(640, 200, "do they agree?", "red", size=18)

mp_deep1 = Doodle(760, 300, "Six cross-checks that make a plan one plan. Scope against schedule: is there time for every must-have. Scope against money: is every must-have paid for. Schedule against people: are people there when the work starts. Schedule against sourcing: do long orders arrive in time. Risk against money and time: is there a reserve for the top risks. Everything against the charter: does it still fit the limits. For Rotterdam three checks failed on 20 February.",
                  "Six cross-checks. On 20 February Rotterdam failed three of them.")
checks = [("scope × schedule", "time for every must-have?", "ok"), ("scope × money", "every must-have paid for?", "ok"), ("schedule × people", "people there when work starts?", "NO"),
          ("schedule × sourcing", "long orders arrive in time?", "NO"), ("risk × reserve", "time and money set aside?", "NO"), ("all × charter", "inside the limits?", "ok")]
for i, (a, b, r) in enumerate(checks):
    row_, col = divmod(i, 2)
    x, y = 14 + col * 372, 20 + row_ * 88
    mp_deep1.box(x, y, 280, 70, a, "blue", sub=b, size=17, subsize=13)
    mp_deep1.box(x + 290, y, 70, 70, r, "pink" if r == "NO" else "green", size=18)

PLAN = dict(
    slug="project-management-plan",
    kicker="a.k.a. “the project management plan”",
    tldr="The <b>project management plan</b> is the one plan everyone works from. Its job is <b>integration</b>: making the parts (what, when, how much, who, what could go wrong, how we run it) <b>agree with each other</b>. Seven good workstream plans are not a project plan until someone has laid them side by side and fixed the places where they clash. Keep it as short as the project allows; a plan nobody reads integrates nothing.",
    chips=[("Family", "one plan"), ("Lives in", "page 4 of the project file, plus the parts it points to"), ("Pairs with", "the whole-project map, baselines, tailoring")],
    pmbok=dict(covers="making one integrated plan from the parts; the project management plan and its components", domains=GOV,
               processes=["Integrate and Align Project Plans"], principles=["Adopt a holistic view"], focus=["planning"],
               older="6th: “Develop Project Management Plan” (4.2), with subsidiary plans and baselines. 7th: the Planning domain."),
    problem_side="Larder, 20 February 2026",
    problem="""  <p class="lead">The plan Sanne promised for <b>20 February</b> exists, in seven pieces: each lead planned their own workstream on 4 February and has refined it since. Each is sensible. Then she lays them side by side on the meeting-room table. The fit-out ends on 3 April. Stocking runs 6–17 April. <span class="hl-pink">The first pickers start on 13 April: a week after the stock they are meant to put on the shelves.</span> And nobody's plan has a line for training on the handhelds.</p>
  <ul>
    <li>Each plan is right; together they don't fit.</li>
    <li>The clashes sit between workstreams, where nobody looks.</li>
    <li>There is no single thing to point at and call “the plan”.</li>
  </ul>""",
    problem_figs=[mp_problem],
    analogy_side="the conductor's score",
    analogy="""  <p>In an orchestra every musician has their <b>part</b>. The conductor has the <b>full score</b>: all the parts on one page, bar by bar. It isn't more music. It is the same music <b>lined up</b>, so the conductor can see that the brass come in two bars before the drums, and fix it in rehearsal, not in the concert.</p>""",
    analogy_figs=[mp_analogy],
    map=[("The parts", "Seven workstream plans, owned by the leads"),
         ("The full score", "The plan on a page, owned by Sanne"),
         ("Bar numbers", "The five shared milestones"),
         ("Brass two bars early", "Pickers hired a week after stocking starts"),
         ("Rehearsal", "The side-by-side session on 20 February")],
    how_side="lay the parts side by side, fix the clashes, write one page",
    how="""  <p>Sanne and the leads spend an hour on <b>cross-checks</b> (listed under “going deeper”). Three fail. Joost moves the first picker group to <b>30 March</b>, so they train at Noord and are on site from 6 April. Handheld training gets an owner (Tomás). And the plan has no time or money set aside for its top risks: the reserve is €6k. Sanne says so in writing; it is the plan's weakest point. Then she writes <b>one page</b>: the goal, five milestones, the seven workstreams with their leads and next date, the money by workstream, the top risks, and pointers to the six parts. Joost gets it on the 20th, as promised; it goes to the steering group on the 27th.</p>""",
    how_figs=[mp_how],
    steps=[("Let each workstream plan its own work", "They have the facts."),
           ("Lay the plans side by side", "On a wall or a table."),
           ("Run the cross-checks", "Where does one plan need what another doesn't give?"),
           ("Fix each clash with the two leads involved", "Not by yourself."),
           ("Write the one page", "And point to the parts."),
           ("Say plainly what is still weak", "A plan is a claim; be honest about it.")],
    vocab=[("Project management plan", "The document that says how the project will be carried out, monitored and closed."),
           ("Integration", "Making the parts of a project work as one."),
           ("Subsidiary plan", "A part of the plan for one area: scope, schedule, cost, risk and so on."),
           ("Milestone chart", "The plan as a few key dates."),
           ("Assumption", "Something the plan treats as true without proof."),
           ("Reserve", "Time or money set aside for what can go wrong.")],
    code=dict(file="rotterdam/04-plan-on-a-page.md", note="to Joost 20 February · to the steering group 27 February 2026", plain=True, src="""
# ROTTERDAM · THE PLAN ON A PAGE                                        v1 · 20 Feb 2026

GOAL        open the Rotterdam store on 27 April, safely, with all 71 must-haves done
MILESTONES  3 Apr fit-out done · 17 Apr stock in · 20 Apr app ready · 24 Apr go / no-go ·
            27 Apr opening · (11 May hypercare exit)

WORKSTREAM         LEAD        NEXT DATE                           BUDGET
Store fit-out      Joost       builder on site 2 Mar               €226k
Equipment + IT     Joost       cold room delivered 27 Mar           €48k
People             Joost       first 15 pickers start 30 Mar        €60k
Stock + suppliers  Tomás       supplier slots booked by 13 Mar        -
Platform set-up    Eli, Ana    zones and prices loaded 20 Mar         -
Apps               Ben, Dee    Rotterdam visible in test 13 Mar       -
Payments + legal   Cho, Lena   food-safety registration 6 Mar         -
Launch marketing   Priya       waitlist opens 16 Mar                €40k
Reserve                                                              €6k
                                                            TOTAL  €380k
TOP RISKS   cold-room delivery · hiring on time · StockPilot rate limit (full list: risks)
WEAK POINT  reserve is €6k and there is no spare week. One bad surprise uses both.
PARTS       scope (71 must-haves) · milestone chart · budget · people · risks · how we run it
"""),
    tools="tools: a wall, the seven workstream plans, six cross-checks and one page.",
    deep_dive=dict(
        side="integration: the cross-checks that turn seven plans into one",
        intro="“Integrate the plans” is the least concrete instruction in project management. This chapter makes it concrete: six cross-checks you can run in an hour, what Rotterdam's three failures looked like, and how to keep the plan integrated after the first day.",
        parts=[
            ("Six cross-checks", """  <p>Integration means asking of every pair of parts: <i>does one need something the other doesn't give?</i> Six pairs catch most problems.</p>
  <ul>
    <li><b>Scope × schedule.</b> Is there time for every must-have before its milestone?</li>
    <li><b>Scope × money.</b> Is every must-have paid for? Is anything paid for that isn't a must-have?</li>
    <li><b>Schedule × people.</b> Are the people there, and trained, on the day their work starts?</li>
    <li><b>Schedule × sourcing.</b> Do long-lead orders arrive before they are needed?</li>
    <li><b>Risk × reserve.</b> Is there time and money set aside for the top risks?</li>
    <li><b>Everything × the charter.</b> Does the whole still fit the limits and serve the benefit?</li>
  </ul>""", [mp_deep1]),
            ("Rotterdam's three failures", """  <ol class="steps">
    <li><b>Schedule × people.</b><p>Pickers started a week after stocking. Fixed by moving the first group of 15 to 30 March. Cost: one extra week of wages, about €9k, found inside the people budget by starting the second group a week later.</p></li>
    <li><b>Schedule × sourcing.</b><p>The handhelds were to be ordered “in March” with a three-week delivery; training needs them on 30 March. Order moved to 23 February.</p></li>
    <li><b>Risk × reserve.</b><p>Not fixed, only made visible. The reserve is €6k and the schedule has no spare week. Sanne writes it on the page as the weak point and tells the steering group what she would need: either €15k more or a decision, now, on which must-haves would go first.</p></li>
  </ol>
  <p>Notice what the checks did <b>not</b> find: there was no line for store IT and internet, so nothing clashed with it. Cross-checks compare the plans you have. They can't see a plan that is missing (the issue log, later in this volume).</p>""", []),
            ("Keeping it integrated", """  <p>A plan is integrated on the day it is written and starts drifting the day after. Three habits keep it together.</p>
  <ul>
    <li><b>One owner for the page.</b> Leads change their own plans; only Sanne changes the page, and she changes it when a milestone, the money or a must-have moves.</li>
    <li><b>The weekly meeting is an integration meeting.</b> Thursdays at 09:30 each lead says what they need from another lead in the next two weeks. That sentence is a cross-check, spoken.</li>
    <li><b>Changes go through one door.</b> A change is checked against all the parts before it is approved (change control, later in this volume).</li>
  </ul>
  <p>A larger project would keep each part as its own document (the older editions call them <b>subsidiary plans</b>: scope, schedule, cost, quality, resources, communications, risk, procurement, stakeholder). The logic is the same; only the weight differs.</p>""", []),
        ]),
    dial=[("Light", "one team", ["A list of what, by when, by whom.", "One conversation to check it hangs together.", "Kept on a board."]),
          ("Standard", "Rotterdam", ["A plan on a page, pointing to six short parts.", "Cross-checks with the leads.", "Updated when a milestone, money or scope moves."]),
          ("Heavy", "large, contracted work", ["A full plan with subsidiary plans.", "Formal review and approval.", "Version control and change control on every part."])],
    baseline="Each line compares <b>seven separate workstream plans</b> to <b>one integrated plan on a page, cross-checked with the leads</b>.",
    ratings=[(3, 4, "The page starts with the goal."),
             (2, 4, "Clashes are found on a table, not on site."),
             (2, 4, "The weak point is written down."),
             (2, 5, "One thing to point at."),
             (2, 4, "The steering group sees the whole."),
             (4, 4, "Leads still own their plans."),
             (3, 3, "Neutral: one more thing to keep current."),
             (3, 4, "Hand-offs between workstreams are planned."),
             (3, 3, "An hour to check, a page to keep.")],
    pitfalls=[("Stapling", "Seven plans in one folder called “the plan”.", "cross-check, then write one page."),
              ("The project manager rewrites the parts", "Leads stop owning them.", "fix clashes with the leads."),
              ("A plan with no weak point", "Nobody believes it.", "say what is fragile."),
              ("Written once", "It drifts.", "one owner; update on real change.")],
    use=["After the workstreams have planned.", "Before asking for a baseline.", "When hand-offs keep failing.", "When someone asks “where's the plan?”"],
    skip=["A single small team: the board is the plan."],
    related=["<b>See the Whole</b> (vol. 1)", "<b>Let the Team Decide</b> (vol. 1)", "<b>What Exactly Did We Promise?</b> (this volume)", "<b>Roadmap vs release plan</b> (Grace, vol. 2)"],
    quiz=[("What is the plan's main job?", "Integration: making the parts agree with each other."),
          ("Name three cross-checks.", "Scope × schedule, schedule × people, risk × reserve (also scope × money, schedule × sourcing, all × charter)."),
          ("Who fixes a clash between two workstreams?", "The two leads, with the project manager."),
          ("Ben moves a demo by two days inside his sprint. Does the plan on a page change?", "No. It changes only when a milestone, the money or a must-have moves."),
          ("The reserve is €6k and there is no spare week. Should the plan hide that?", "No. Sanne writes it as the weak point and tells the steering group what would fix it.")],
    try_it="Put your project's plans side by side (even as sticky notes). Run two cross-checks: are the people there when the work starts, and do long orders arrive in time? Write down the first clash you find and who must talk to whom.",
    remember="Seven <span class=\"hl\">parts</span> are not a <span class=\"hl\">score</span> until someone lines them up.",
    sources=["Project Management Institute, <i>PMBOK Guide</i>, Eighth Edition (2025): Governance domain, integrating and aligning plans.",
             "Project Management Institute, <i>PMBOK Guide</i>, Sixth Edition (2017): 4.2 Develop Project Management Plan.",
             "Harold Kerzner, <i>Project Management: A Systems Approach</i> (13th ed., 2022)."],
)

# ------------------------------------------------------------------ 05 Make It, Buy It, or Hire It?
ss_problem = Doodle(760, 250, "Doodle of 24 February 2026. The builder's offer has two prices. A fixed price of 148 thousand euros with handover on 3 April. Or by the hour, estimated at 131 thousand euros, with no promised date. Marco likes the lower number. Sanne notices who carries the risk in each.",
                    "Two prices for the same fit-out. The cheaper one leaves the risk with Larder.")
ss_problem.box(20, 30, 330, 110, "fixed price · €148k", "y", sub="handover 3 April, in the contract", size=19, subsize=14)
ss_problem.box(410, 30, 330, 110, "by the hour · ≈ €131k", "paper", sub="no promised date", size=19, subsize=14)
ss_problem.note(185, 176, "risk: the builder's", "green", size=18)
ss_problem.note(575, 176, "risk: Larder's", "red", size=18)
ss_problem.note(380, 222, "€17k buys a date", "pen", size=20)

ss_analogy = Doodle(760, 240, "Doodle of getting to the airport. Drive yourself: cheap, your risk, your time. A taxi on the meter: flexible, you pay for the traffic jam. A fixed-fare transfer: you pay more, and the jam is the driver's problem. The choice depends on how much the flight matters.",
                    "Drive, take a metered taxi, or book a fixed fare: who pays for the traffic jam?")
ss_analogy.row([("drive yourself", "your time, your risk", "green"), ("taxi on the meter", "you pay for the jam", "y"), ("fixed fare", "the jam is theirs", "blue")], y=40, h=96, size=18, subsize=14)
ss_analogy.note(132, 186, "make", "red", size=20)
ss_analogy.note(380, 186, "time + materials", "red", size=20)
ss_analogy.note(628, 186, "fixed price", "red", size=20)

ss_how = Doodle(760, 400, "Rotterdam's sourcing table, 24 February 2026. Store fit-out: buy, fixed price of 148 thousand euros, a thousand euros a day off for late handover up to ten days, five percent held back until snags are fixed. Cold room and fridges: buy, supply and install, 64 thousand euros, ordered 13 February. Shelving, handhelds, chargers and IT: buy from catalogue, 48 thousand euros. E-bikes: lease, paid by operations. Picker training: make, by Tomás's team at Noord. City set-up in the platform: make, by Larder's engineers.",
                "For each thing: make, buy or lease, and a contract that puts the risk with whoever can control it.")
rowsS = [("store fit-out", "buy · fixed price €148k", "late: −€1k a day · 5 % held back", "y"),
         ("cold room + fridges", "buy · installed €78k", "ordered 13 Feb · 8 weeks", "y"),
         ("equipment + store IT", "buy · catalogue €48k", "3-week delivery", "y"),
         ("e-bikes", "lease", "paid by operations", "blue"),
         ("picker training", "make", "Tomás's team at Noord", "green"),
         ("city set-up, apps", "make", "Larder's engineers", "green")]
for i, (a, b, c, f) in enumerate(rowsS):
    y = 12 + i * 60
    ss_how.box(14, y, 210, 48, a, "paper", size=15, rx=5)
    ss_how.box(234, y, 250, 48, b, f, size=13, rx=5)
    ss_how.text(498, y + 30, c, anchor="start", size=14)
ss_how.note(380, 388, "yellow = buy · blue = lease · green = make", "pen", size=15)

SOURCING = dict(
    slug="sourcing-strategy",
    kicker="a.k.a. “sourcing strategy”: make or buy, and contract types",
    tldr="For every big piece of a project, decide: <b>make</b> it with your own people, <b>buy</b> it, or <b>lease</b> it. If you buy, the <b>contract type</b> decides who carries the risk. <b>Fixed price</b>: the supplier does, and charges for it. <b>Time and materials</b>: you do. <b>Cost plus</b>: you do, with the supplier's fee on top. Put each risk with the party who can control it, and decide early: suppliers have lead times too.",
    chips=[("Family", "one plan"), ("Lives in", "a sourcing table in the plan; the contracts themselves with legal"), ("Pairs with", "build vs buy, long-lead items, the risk register")],
    pmbok=dict(covers="make-or-buy decisions, choosing suppliers, contract types and who carries which risk", domains=GOV + ["finance"],
               processes=["Plan Sourcing Strategy"], principles=["Focus on value", "Integrate sustainability within all project areas"], focus=["planning"],
               older="6th: “project procurement management” (plan, conduct, control procurements). 7th: procurement under the Project Work domain."),
    problem_side="Larder, 24 February 2026",
    problem="""  <p class="lead">The builder's offer has two prices. <b>Fixed price: €148k</b>, handover on 3 April written into the contract. <b>By the hour: about €131k</b>, no promised date. Marco, looking at a reserve of €6k, likes the second number. Sanne looks at who pays if the electrician is late. <span class="hl-pink">With the cheaper offer, Larder does: in money and in days it doesn't have.</span></p>
  <ul>
    <li>The lowest price isn't the lowest cost.</li>
    <li>Nobody has decided what Larder does itself and what it buys.</li>
    <li>Contracts are being signed one by one, with no overall view.</li>
  </ul>""",
    problem_figs=[ss_problem],
    analogy_side="getting to the airport",
    analogy="""  <p>You can <b>drive yourself</b>: cheap, and every problem is yours. You can take a <b>taxi on the meter</b>: flexible, but you pay for the traffic jam. Or you can book a <b>fixed-fare transfer</b>: more money, and the jam is the driver's problem. Which is right depends on what missing the flight would cost you.</p>""",
    analogy_figs=[ss_analogy],
    map=[("Driving yourself", "Make: training by Tomás's team; the city set-up by Larder's engineers"),
         ("A taxi on the meter", "Time and materials: the builder's cheaper offer"),
         ("A fixed fare", "Fixed price: €148k with a handover date"),
         ("Missing the flight", "Missing 27 April, with rent running"),
         ("Booking early", "The cold room ordered on 13 February")],
    how_side="one table: make, buy or lease, and which contract",
    how="""  <p>Sanne makes one <b>sourcing table</b> with Joost, Marco and Lena. For each item: make, buy or lease, the reason, and the kind of contract. The <b>fit-out</b> is bought at a <b>fixed price</b>: the scope is clear (drawings exist) and the date matters more than €17k. Lena adds two clauses: <b>€1,000 off per late day</b>, up to ten days, and <b>5 % held back</b> until the snags are fixed. The <b>cold room</b> is supply-and-install from one supplier, so one party owns “it works”. <b>E-bikes</b> are leased by operations. <b>Training</b> and the <b>city set-up</b> are made in-house: that is knowledge Larder needs for four more cities.</p>""",
    how_figs=[ss_how],
    steps=[("List the big pieces of the project", "Anything over a few thousand euros or a few weeks."),
           ("For each: make, buy or lease?", "Keep what you'll need again; buy what others do better."),
           ("If buying: how clear is the scope?", "Clear → fixed price. Unclear → time and materials, with a cap."),
           ("Put each risk with whoever can control it", "And expect to pay for that."),
           ("Check lead times against the plan", "Order dates, not just delivery dates."),
           ("Have legal and finance read it once, as a whole", "Not contract by contract.")],
    vocab=[("Make-or-buy", "The decision to do something yourself or pay someone else."),
           ("Fixed price", "One agreed price for an agreed result; the seller carries the cost risk."),
           ("Time and materials", "Paying for hours and materials used; the buyer carries the risk."),
           ("Cost plus", "Paying the seller's costs plus a fee; used when scope is very uncertain."),
           ("Retention", "Part of the price held back until defects are fixed."),
           ("Lead time", "The time between ordering and receiving.")],
    code=dict(file="rotterdam/05-sourcing.md", note="Sanne with Joost, Marco and Lena · 24 February 2026", plain=True, src="""
# ROTTERDAM · WHAT WE MAKE, BUY AND LEASE

ITEM                     HOW     CONTRACT                          WHY
Store fit-out            buy     fixed price €148k                 scope clear (drawings);
                                 handover 3 Apr; −€1,000 per late  the date is worth more
                                 day (max 10); 5 % retention       than the €17k saved
Cold room + fridges      buy     supply and install €78k           one party owns "it works"
                                 ordered 13 Feb, 8 weeks
Shelving, handhelds,     buy     catalogue prices €48k             standard goods
chargers, store IT               ordered 23 Feb, 3 weeks
E-bikes (40)             lease   monthly, by operations            not a project cost;
                                                                   maintenance included
Picker + courier         make    Tomás's team at Noord             we need this skill for
training                                                           four more cities
City set-up, apps        make    Larder's engineers                "a city is configuration"
Launch adverts           buy     time and materials, cap €12k      content will change
"""),
    tools="tools: a one-page table, the builder's two offers side by side, and an hour with finance and legal.",
    dial=[("Light", "a small purchase or two", ["Ask: who pays if it's late?", "One line of reasoning.", "Standard terms."]),
          ("Standard", "Rotterdam: two main suppliers", ["A sourcing table.", "Contract type chosen per item.", "Late-delivery and retention clauses."]),
          ("Heavy", "large or public procurement", ["A procurement plan and tender process.", "Evaluation criteria and scoring.", "Contract managers and formal claims handling."])],
    baseline="Each line compares <b>signing contracts one by one on price</b> to <b>one sourcing table: make, buy or lease, and a contract type chosen by who should carry the risk</b>.",
    ratings=[(3, 4, "In-house where the skill is needed again."),
             (2, 4, "The handover date is in a contract."),
             (2, 4, "Risk sits with whoever controls it."),
             (3, 4, "One table shows every commitment."),
             (3, 4, "Marco and Lena saw the whole once."),
             (3, 3, "Neutral."),
             (3, 2, "A fixed price makes later changes dearer."),
             (3, 4, "Retention keeps the builder interested in snags."),
             (4, 3, "A table and a legal read.")],
    pitfalls=[("Cheapest offer wins", "The risk comes back with interest.", "ask who pays if it's late."),
              ("Fixed price for unclear scope", "Every change is an extra.", "fix the scope first, or cap time and materials."),
              ("Buying what you need to learn", "The knowledge leaves with the supplier.", "make what you'll repeat."),
              ("Ordering by delivery date", "Forgetting the lead time.", "plan the order date.")],
    use=["Any project that spends money outside.", "Before the first contract is signed.", "When a supplier offers two pricing models.", "When lead times are long."],
    skip=["Everything is done by your own team with what it already has."],
    related=["<b>Build vs buy</b> (Ana, vol. 2)", "<b>Exit plans</b> (Ana, vol. 2)", "<b>Think Past the Finish</b> (vol. 1)", "<b>When Do I Take It Upstairs?</b> (this volume)"],
    quiz=[("Who carries the cost risk in a fixed-price contract?", "The seller."),
          ("When does time and materials fit?", "When the scope is unclear or will change. Add a cap."),
          ("Why make the training in-house?", "Larder needs that skill for four more cities."),
          ("In March Joost wants to add a second cold-room door. The builder quotes €6k as an extra. Why is that expensive, and whose decision is it?", "Fixed-price contracts price changes high. It is over €5,000, so the sponsor decides, through change control."),
          ("What does the 5 % retention do?", "It is paid only when the snags are fixed, so the builder comes back.")],
    try_it="List the three biggest things your project buys. For each, write who pays, in money and in days, if it arrives late. Is that the party who can control the delay?",
    remember="The cheapest price leaves the <span class=\"hl\">traffic jam</span> with you.",
    sources=["Project Management Institute, <i>PMBOK Guide</i>, Eighth Edition (2025): Governance domain, sourcing strategy.",
             "Project Management Institute, <i>PMBOK Guide</i>, Sixth Edition (2017): chapter 12, project procurement management.",
             "Roger Fisher and William Ury, <i>Getting to Yes</i> (1981)."],
)

# ------------------------------------------------------------------ 06 What Exactly Did We Promise?
bl_problem = Doodle(760, 250, "Doodle of 9 March 2026, Sanne's own mistake. In February she read Grace's roadmap and wrote in her plan that substitution approvals would be in Rotterdam at launch. She told Joost. Joost told the store team. On 9 March Grace's release plan shows approvals coming to Rotterdam later. Three people now hold three versions of what was promised.",
                    "Sanne's mistake: she promised Joost a feature that Grace had never promised her.")
bl_problem.row([("Sanne's plan", "“approvals at launch”", "pink"), ("Joost", "told the store team", "paper"), ("Grace's release plan", "“approvals: later”", "blue")], y=40, h=90, gap=40, size=17, subsize=14, arrows=True)
bl_problem.note(380, 186, "three versions of the promise", "red", size=20)
bl_problem.note(380, 222, "nobody had signed any of them", "pen", size=18)

bl_analogy = Doodle(760, 240, "Doodle of a child's height marked on a door frame. The pencil mark with a date is the baseline. Next year you measure against the mark, not against memory. If you paint the door frame, you make a new mark on purpose and write the date.",
                    "A pencil mark on the door frame: you measure against the mark, not against memory.")
bl_analogy.line("M120 20 v190 M100 20 h40")
for y, t in [(170, "March: 112 cm"), (120, "now: 118 cm")]:
    bl_analogy.line(f"M110 {y} h40", color="red")
    bl_analogy.note(250, y + 6, t, "pen", size=18)
bl_analogy.box(430, 60, 300, 100, "the mark, with a date", "y", sub="moved only on purpose", size=19, subsize=15)

bl_how = Doodle(760, 400, "Rotterdam's baseline, approved by the steering group on 13 March 2026, version 1. Scope baseline: 71 must-haves, with six app must-haves agreed on 3 March; substitution approvals in Rotterdam is a should, not promised for launch. Schedule baseline: the five milestones, 3, 17, 20, 24 and 27 April. Cost baseline: 380 thousand euros, of which 273 thousand committed. Each signed by its owner: Grace and Joost for scope, the leads for the schedule, Marco for cost. Below: after 13 March the baseline changes only through change control.",
                "Three baselines, each signed by the person who owns that promise, approved together on 13 March.")
bl_how.row([("scope", "71 must-haves · 6 in the app", "blue"), ("schedule", "3 · 17 · 20 · 24 · 27 April", "y"), ("cost", "€380k · €335k committed", "green")], y=14, h=100, size=22, subsize=14)
bl_how.note(132, 142, "signed: Grace, Joost", "pen", size=16)
bl_how.note(380, 142, "signed: the leads", "pen", size=16)
bl_how.note(628, 142, "signed: Marco", "pen", size=16)
bl_how.box(120, 176, 520, 70, "BASELINE v1 · approved 13 March", "paper", sub="by the steering group", size=20, subsize=14)
bl_how.box(14, 280, 350, 90, "not promised for launch", "pink", sub="approvals in Rotterdam: a Should", size=17, subsize=14)
bl_how.box(396, 280, 350, 90, "after 13 March", "paper", sub="changes only through change control", size=17, subsize=14, dash=True)

BASELINES = dict(
    slug="baselines",
    kicker="a.k.a. “baselines”: scope, schedule and cost",
    tldr="A <b>baseline</b> is the approved version of the plan: <b>what</b> we will deliver, <b>by when</b>, <b>for how much</b>. It is the promise, frozen and dated. Progress is measured against it, and it changes only through an approved change. Without a baseline, “on track” means “close to whatever the plan says this week”. Each part should be <b>signed by the person who owns that promise</b>, not assumed by the project manager.",
    chips=[("Family", "one plan"), ("Lives in", "the plan, marked “baseline v1” with a date"), ("Pairs with", "change control, status reports, MoSCoW")],
    pmbok=dict(covers="scope, schedule and cost baselines; approving the plan as the reference for measurement", domains=GOV + ["scope", "schedule", "finance"],
               processes=["Integrate and Align Project Plans"], principles=["Be an accountable leader"], focus=["planning", "monitoring"],
               older="6th: the scope, schedule and cost baselines, together the “performance measurement baseline”. 7th: baselines under the Planning and Measurement domains."),
    problem_side="Larder, 9–13 March 2026",
    problem="""  <p class="lead">This one is <b>Sanne's own mistake</b>. In February she read Grace's roadmap, saw “substitution approvals” in the Now column, and wrote in her plan that Rotterdam would have them at launch. She told Joost. Joost told the store team. On <b>9 March</b> Grace's release plan shows approvals reaching Rotterdam <i>after</i> Amsterdam. <span class="hl-pink">Three people hold three versions of the promise, and Sanne wrote the wrong one.</span> Grace is polite about it. Joost less so.</p>
  <ul>
    <li>The plan contained a promise its owner never made.</li>
    <li>Nothing marked which version of the plan was “agreed”.</li>
    <li>Without that, nobody can say what changed, or when.</li>
  </ul>""",
    problem_figs=[bl_problem],
    meanwhile=[("product-2", "moscow", "on 3 March Grace's MoSCoW session cuts the Rotterdam app scope from 14 Musts to 6. Approvals in Rotterdam is a Should.",
                "ten days later those 6 Musts become the app part of Sanne's scope baseline, signed by Grace.")],
    analogy_side="the pencil mark on the door frame",
    analogy="""  <p>Parents mark a child's height on the <b>door frame</b>, with a date. Next year they measure against the <b>mark</b>, not against what anyone remembers. If the door frame is repainted, they make a new mark <b>on purpose</b> and date it. Nobody quietly moves the old one to make the child look taller.</p>""",
    analogy_figs=[bl_analogy],
    map=[("The mark and its date", "Baseline v1, 13 March 2026"),
         ("Measuring against the mark", "Status: must-haves done, milestones, spend, all against v1"),
         ("Memory", "“I thought we said approvals at launch”"),
         ("A new mark, on purpose", "Baseline v2, after an approved change"),
         ("Quietly moving the mark", "Editing the plan and calling it on track")],
    how_side="each owner signs their part; the steering group approves the whole",
    how="""  <p>Sanne corrects the misread the same day, in person, to Joost and the store team, and says it was hers. Then she fixes the cause. Each part of the plan goes to <b>the person who owns that promise</b>. <b>Scope</b>: Grace signs the six app Musts from her session on 3 March (approvals in Rotterdam is a Should, not promised); Joost signs the store and staffing must-haves. <b>Schedule</b>: each lead confirms their milestone. <b>Cost</b>: Marco confirms €380k, of which €335k is already committed. On <b>13 March</b> the steering group approves the three together as <b>baseline v1</b>. From now on the plan can still change, but the baseline moves only through change control.</p>""",
    how_figs=[bl_how],
    steps=[("Finish integrating the plan", "A baseline of a clashing plan is worthless."),
           ("Have each owner sign their part", "Scope, schedule, cost."),
           ("Write what is not promised", "The Shoulds and Coulds."),
           ("Get the whole approved, with a date and a version", "By the level that owns the limits."),
           ("Measure against it", "Not against the latest edit."),
           ("Change it only through an approved change", "And number the new version.")],
    vocab=[("Baseline", "The approved version of a plan, used to measure progress and manage change."),
           ("Scope baseline", "The agreed description of what will be delivered."),
           ("Schedule baseline", "The agreed dates."),
           ("Cost baseline", "The agreed budget over time."),
           ("Variance", "The difference between the baseline and what is happening."),
           ("Re-baseline", "Approving a new baseline after a significant, agreed change.")],
    code=dict(file="rotterdam/06-baseline-v1.md", note="approved by the steering group, 13 March 2026", plain=True, src="""
# ROTTERDAM · BASELINE v1 · 13 March 2026

SCOPE      71 must-haves (list: scope)                                   signed
           app (6 Musts, 3 Mar): zones + slots · prices + VAT ·          Grace
             opening hours · iDEAL + cards · order tracking · store in app
           store, stock, staff, legal, marketing must-haves (65)         Joost
           NOT PROMISED FOR LAUNCH: substitution approvals in Rotterdam (a Should;
             release R3, planned 27 Apr if Amsterdam's rollout goes well)

SCHEDULE   3 Apr fit-out done · 17 Apr stock in · 20 Apr app ready ·     the leads
           24 Apr go / no-go · 27 Apr opening · 11 May hypercare exit

COST       €380k total · committed to date €335k                         Marco
           (builder €148k · cold room €78k · equipment €48k · recruiting and
           marketing contracts €61k)
           reserve €6k

RULE       measured against v1 from today. v1 changes only by an approved change
           (log: changes). Corrected on 9 Mar: "approvals at launch" was never promised.
"""),
    tools="tools: the plan on a page, three signatures, a version number and a date.",
    dial=[("Light", "a small team", ["“This is what we agreed on Monday.”", "A dated message.", "Re-agreed when it changes."]),
          ("Standard", "Rotterdam", ["Scope, schedule and cost on one page.", "Each signed by its owner.", "Approved, versioned, dated."]),
          ("Heavy", "contracts, public money", ["Formal baselines under configuration control.", "Time-phased budget for earned value.", "Re-baselining only by the board."])],
    baseline="Each line compares <b>a plan that is edited as things change</b> to <b>a dated baseline, signed by the owners of each promise</b>.",
    ratings=[(3, 4, "What is promised is tied to what the benefit needs."),
             (2, 5, "There is a fixed thing to forecast against."),
             (2, 4, "A wrong promise is caught at signing."),
             (2, 5, "“On track” has a meaning."),
             (2, 4, "Joost knows exactly what he'll get."),
             (3, 4, "Owners sign their own promises."),
             (3, 2, "Changing the promise now takes a decision."),
             (3, 3, "Neutral."),
             (4, 3, "Signatures and a version to keep.")],
    pitfalls=[("The project manager writes other people's promises", "As Sanne did.", "each owner signs their part."),
              ("A baseline that moves every week", "Nothing to measure against.", "change it only by approved change."),
              ("Baselining too early", "Before the plan hangs together.", "integrate first."),
              ("Only what is in", "The Shoulds are assumed.", "write what is not promised.")],
    use=["Once the plan is integrated.", "Before the first real status report.", "When people remember different promises.", "After a major approved change (re-baseline)."],
    skip=["Purely exploratory work: agree a goal and a time box, not a baseline."],
    related=["<b>MoSCoW and its traps</b> (Grace, vol. 2)", "<b>Roadmap vs release plan</b> (Grace, vol. 2)", "<b>Can We Change That?</b> (this volume)", "<b>Where Are We, Really?</b> (this volume)"],
    quiz=[("What are the three baselines?", "Scope, schedule and cost."),
          ("Who signed the app scope?", "Grace: it's her promise."),
          ("What was Sanne's mistake?", "She put a promise in her plan (approvals at launch) that its owner had never made, and passed it on."),
          ("On 20 March Eli re-orders two of his tasks. Does the baseline change?", "No. The plan's detail changes; the baseline (must-haves, milestones, budget) doesn't."),
          ("Joost says “just update the baseline to the new date, it's cleaner”. What does Sanne answer?", "The baseline moves only through an approved change, so everyone can see that it moved, when and why. Otherwise late becomes invisible.")],
    try_it="Write down what your project has promised: what, by when, for how much. Next to each line, write the name of the person who made that promise. Any line with your own name where it should be someone else's? Go and get it signed.",
    remember="Measure against the <span class=\"hl\">mark</span>, not against <span class=\"hl\">memory</span>.",
    sources=["Project Management Institute, <i>PMBOK Guide</i>, Eighth Edition (2025): Governance domain, aligning plans and baselines.",
             "Project Management Institute, <i>PMBOK Guide</i>, Sixth Edition (2017): scope, schedule and cost baselines.",
             "Project Management Institute, <i>Practice Standard for Project Configuration Management</i> (2007)."],
)

NOTES = [CHARTER, GOVERNANCE, GATES, PLAN, SOURCING, BASELINES]
