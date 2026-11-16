# The PMBOK map: the PMBOK Guide, Eighth Edition (PMI, 2025) on one page, in our own words.
# Each item links to the note that covers it. Add to this file as each volume of book 3 is written.
# Names of principles, domains and focus areas are PMI's; every description here is ours.

LEAD = ("The <b>PMBOK Guide</b> is the Project Management Institute's description of how projects are run. It is long, careful and "
        "hard to read from front to back. This page is the way in: the whole of the <b>eighth edition</b> on one sheet, each part in "
        "plain words, and a link to the note in <b>Sanne's notebook</b> that explains it with a real project. Use it to find a topic, "
        "or to see how far you've got.")

SHAPE = """  <p>The eighth edition has four layers. Start at the top and each layer answers the next question:</p>
  <ul class="drivers">
    <li><b>6 principles</b>: <i>how should I think?</i> They hold on every project, whatever the method.</li>
    <li><b>7 performance domains</b>: <i>what must I look after?</i> Seven areas of a project that all need attention, all the way through.</li>
    <li><b>5 focus areas</b>: <i>what kind of attention, right now?</i> Starting, planning, doing, checking, finishing.</li>
    <li><b>40 processes</b>: <i>what do I actually do?</i> Each one sits in one domain and one focus area. None is compulsory: you choose
    and size them for your project, which the guide calls <b>tailoring</b>.</li>
  </ul>"""

# (name, in plain words, (journal key, slug) or None)
PRINCIPLES = [
    ("Adopt a holistic view", "A project is one connected system inside a bigger one. Look at the whole before you fix a part.", ("project-1", "holistic-view")),
    ("Focus on value", "The point is the benefit the project exists for, not the list of tasks or the documents.", ("project-1", "focus-on-value")),
    ("Embed quality into processes and deliverables", "Build quality into how the work is done. Don't inspect for it at the end.", ("project-1", "embed-quality")),
    ("Be an accountable leader", "Own the outcome, tell the truth about status, and look after the people.", ("project-1", "accountable-leader")),
    ("Integrate sustainability within all project areas", "Weigh the long-term effect on people, planet and money in each decision.", ("project-1", "sustainability")),
    ("Build an empowered culture", "Give the people doing the work the room, the facts and the trust to decide.", ("project-1", "empowered-culture")),
]

# (css key, name, the question it answers, number of processes, where in this book)
DOMAINS = [
    ("governance", "Governance", "Who decides, how do we start, steer, change and close?", 9, '<a href="../project-2/index.html">Vol. 2</a>'),
    ("scope", "Scope", "What will we deliver, and what not?", 6, '<a href="../project-3/index.html">Vol. 3</a>'),
    ("schedule", "Schedule", "By when?", 3, '<a href="../project-3/index.html">Vol. 3</a>'),
    ("finance", "Finance", "For how much, and is the money there when we need it?", 4, '<a href="../project-4/index.html">Vol. 4</a>'),
    ("stakeholders", "Stakeholders", "Who is affected, and what do they need from us?", 7, "Vol. 5"),
    ("resources", "Resources", "Which people and things do we need, and how do we lead the team?", 5, '<a href="../project-4/index.html">Vol. 4</a>'),
    ("risk", "Risk", "What could go wrong, or better than planned, and what do we do about it?", 6, "Vol. 5"),
]
DOMAINS_NOTE = ('  <p>The domains are explained together in <a href="../project-1/notes/performance-domains.html">What Must I Keep an Eye On?</a>. '
                'Each one then gets its own volume, where every one of its processes is covered and listed here by name.</p>')

# Processes, per domain, once its volume is written: (process, focus area, in plain words, [(journal key, slug), …]).
P2 = "project-2"
P3 = "project-3"
P4 = "project-4"
PROCESSES = [
    ("governance", [
        ("Initiate Project or Phase", "initiating", "Agree that the project, or its next phase, should start: why, for what benefit, who is behind it.",
         [(P2, "project-charter"), (P2, "governance-structure"), (P2, "phase-gates")]),
        ("Integrate and Align Project Plans", "planning", "Make one plan in which scope, dates, money, people and risks agree with each other; approve it as the baseline.",
         [(P2, "project-management-plan"), (P2, "baselines")]),
        ("Plan Sourcing Strategy", "planning", "Decide what to make and what to buy, from whom, and under which kind of contract.",
         [(P2, "sourcing-strategy")]),
        ("Manage Project Execution", "executing", "Lead and co-ordinate the work in the plan; clear what blocks it.",
         [(P2, "directing-the-work"), (P2, "issue-log")]),
        ("Manage Quality Assurance", "executing", "Check that the way of working will produce good results, and improve it.",
         [(P2, "quality-assurance")]),
        ("Manage Project Knowledge", "executing", "Use what the organisation already knows, and capture what this project learns.",
         [(P2, "lessons-learned")]),
        ("Monitor and Control Project Performance", "monitoring and controlling", "Measure against the baseline, forecast the end, report honestly, and act.",
         [(P2, "status-reports"), (P2, "escalation")]),
        ("Assess and Implement Changes", "monitoring and controlling", "Size every requested change, have the right person decide it, and build approved changes into the plan.",
         [(P2, "change-control")]),
        ("Close Project or Phase", "closing", "Finish properly: results accepted and handed over, contracts and money settled, the team released.",
         [(P2, "handover"), (P2, "closing-a-project")]),
    ]),
    ("scope", [
        ("Plan Scope Management", "planning", "Decide how scope will be found, written down, broken down, accepted and changed on this project.",
         [(P3, "scope-schedule-approach")]),
        ("Elicit and Analyze Requirements", "planning", "Draw out what the people affected need, sort it, and trace each need to something delivered and checked.",
         [(P3, "requirements")]),
        ("Define Scope", "planning", "Write what the project will deliver, how each deliverable will be accepted, and what is left out.",
         [(P3, "scope-statement")]),
        ("Develop Scope Structure", "planning", "Break the whole result down into smaller deliverables and work packages: the work breakdown structure.",
         [(P3, "work-breakdown-structure")]),
        ("Validate Scope", "monitoring and controlling", "Have the people who asked for each deliverable formally accept it.",
         [(P3, "validate-scope")]),
        ("Monitor and Control Scope", "monitoring and controlling", "Watch what is being delivered against the baseline, and stop unapproved additions.",
         [(P3, "scope-creep")]),
    ]),
    ("schedule", [
        ("Plan Schedule Management", "planning", "Decide how the schedule will be built, in what detail, in which units, and how it will be tracked.",
         [(P3, "scope-schedule-approach")]),
        ("Develop Schedule", "planning", "Estimate the work, link it in order, find the critical path, and fit it to calendars and constraints.",
         [(P3, "estimating-methods"), (P3, "three-point-estimates"), (P3, "estimating-with-the-team"), (P3, "network-diagram"),
          (P3, "critical-path"), (P3, "float-and-buffers"), (P3, "gantt-and-milestones"), (P3, "crashing-and-fast-tracking")]),
        ("Monitor and Control Schedule", "monitoring and controlling", "Measure progress against the schedule baseline, forecast the dates, and act on slips.",
         [(P3, "schedule-tracking")]),
    ]),
    ("finance", [
        ("Plan Financial Management", "planning", "Decide what the budget covers, who may spend what, and how money is counted, reported and controlled.",
         [(P4, "financial-management")]),
        ("Estimate Costs", "planning", "Put a money figure on each piece of work, from quotes, rates and past jobs, with how sure each one is.",
         [(P4, "cost-estimates")]),
        ("Develop Budget", "planning", "Add the estimates up, add reserves, spread the budget over time and check the cash is there when it's needed.",
         [(P4, "budget-and-reserves"), (P4, "cash-flow")]),
        ("Monitor and Control Finances", "monitoring and controlling", "Compare committed, spent and earned with the plan; forecast the final cost; check the value it brings.",
         [(P4, "committed-and-spent"), (P4, "earned-value"), (P4, "cost-forecasting"), (P4, "payback")]),
    ]),
    ("resources", [
        ("Plan Resource Management", "planning", "Decide who does what, how people and equipment will be found, trained, looked after and released.",
         [(P4, "raci")]),
        ("Estimate Resources", "planning", "Work out how many people, with which skills, and which equipment and materials the work needs.",
         [(P4, "estimating-resources")]),
        ("Acquire Resources", "executing", "Get the people and things: hire, borrow, lease or buy, with the agreement of whoever owns them.",
         [(P4, "acquiring-resources")]),
        ("Lead the Team", "executing", "Lead and develop the people doing the work, including those who don't report to you, and work through conflict.",
         [(P4, "leading-without-authority"), (P4, "team-conflict")]),
        ("Monitor and Control Resourcing", "monitoring and controlling", "Check that people and things are available as planned; level overloads; act on shortfalls.",
         [(P4, "resource-levelling"), (P4, "monitoring-resources")]),
    ]),
]
PROCESSES_NOTE = ('  <p class="aside">process names as listed in public summaries of the eighth edition; check the exact wording against your '
                  'own copy of the guide. The plain-words column is mine.</p>')

FOCUS = [
    ("Initiating", "Agree that the project (or the next phase) should exist, why, and who is behind it."),
    ("Planning", "Work out what, by when, for how much, with whom, and what could stop us."),
    ("Executing", "Do the work and lead the people doing it."),
    ("Monitoring and controlling", "Compare what is happening with the plan, and decide what to change."),
    ("Closing", "Hand over, settle up, and keep what was learned."),
]

FOUNDATIONS = [
    ("Project, product or operations", ("project-1", "project-product-operations")),
    ("The system for value delivery: portfolios, programmes, projects, operations", ("project-1", "value-delivery-system")),
    ("The project manager and the sponsor", ("project-1", "project-manager-role")),
    ("The project environment", ("project-1", "project-environment")),
    ("Life cycles and development approaches: predictive, adaptive, hybrid", ("project-1", "life-cycles")),
    ("The five focus areas", ("project-1", "focus-areas")),
    ("The seven performance domains", ("project-1", "performance-domains")),
    ("Tailoring", ("project-1", "tailoring")),
    ("The project management office (PMO)", ("project-1", "pmo")),
]

EDITIONS = """  <p>Most courses and many colleagues still speak sixth or seventh edition. The ideas are the same; the shelves they sit on moved.
  Every note carries an <b>“in older editions”</b> line, and this table shows the big moves.</p>"""

CROSSWALK = [
    ("Built around", "processes", "principles", "principles, domains and processes together"),
    ("Principles", "none stated", "12", "6"),
    ("Main grouping", "10 knowledge areas", "8 performance domains", "7 performance domains"),
    ("Timing", "5 process groups", "not used", "5 focus areas"),
    ("Processes", "49, each with inputs, tools and outputs", "none (moved online)", "40, all optional"),
    ("Tailoring", "a short section", "its own chapter", "built into every domain"),
    ("Agile and hybrid", "a separate practice guide", "woven in", "woven in"),
]

shape = Doodle(760, 330, "Doodle of the shape of the PMBOK Guide, eighth edition, as four layers of a binder. Top layer: six principles, how to think. Second: seven performance domains, what to look after: governance, scope, schedule, finance, stakeholders, resources, risk. Third: five focus areas, what kind of attention now: initiating, planning, executing, monitoring and controlling, closing. Bottom: forty processes, what to do, all optional. Tailoring runs down the side: choose and size for your project.",
               "Four layers: how to think, what to look after, what kind of attention, what to do. Tailoring runs through all of it.")
shape.box(20, 14, 600, 62, "6 principles", "y", sub="how should I think?", size=20, subsize=15)
shape.box(20, 90, 600, 62, "7 performance domains", "blue", sub="what must I look after?", size=20, subsize=15)
shape.box(20, 166, 600, 62, "5 focus areas", "green", sub="what kind of attention, right now?", size=20, subsize=15)
shape.box(20, 242, 600, 62, "40 processes", "paper", sub="what do I actually do? (all optional)", size=20, subsize=15)
shape.box(640, 14, 100, 290, None, "pink", dash=True)
shape.text(690, 150, "tailoring", "t-head", size=20)
shape.note(690, 176, "choose", size=15)
shape.note(690, 194, "and size", size=15)
