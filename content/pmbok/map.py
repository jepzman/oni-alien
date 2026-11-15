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
    ("governance", "Governance", "Who decides, how do we start, steer, change and close?", 9, "Vol. 2"),
    ("scope", "Scope", "What will we deliver, and what not?", 6, "Vol. 3"),
    ("schedule", "Schedule", "By when?", 3, "Vol. 3"),
    ("finance", "Finance", "For how much, and is the money there when we need it?", 4, "Vol. 4"),
    ("stakeholders", "Stakeholders", "Who is affected, and what do they need from us?", 7, "Vol. 5"),
    ("resources", "Resources", "Which people and things do we need, and how do we lead the team?", 5, "Vol. 4"),
    ("risk", "Risk", "What could go wrong, or better than planned, and what do we do about it?", 6, "Vol. 5"),
]
DOMAINS_NOTE = ('  <p>The domains are explained together in <a href="../project-1/notes/performance-domains.html">What Must I Keep an Eye On?</a>. '
                'Each one then gets its own volume, where every one of its processes is covered and listed here by name.</p>')

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
