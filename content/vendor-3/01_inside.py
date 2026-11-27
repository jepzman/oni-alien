# Series 5 · On the Client's Floor · Vol. 3 · Digging Up the Legacy · Inside MAVIS (notes 1–4).
# Narrator: Ines Duarte (she/her). Facts: docs/lodestar-casebook.md, "Vol. 3".
from datetime import date


def on_site(d):
    return f"day {(d - date(2027, 7, 4)).days} on site"


# ------------------------------------------------------------------ 01 What Is Actually in There?
sa_problem = Doodle(760, 250, "Doodle of what MetroVolt's documents say about MAVIS next to what the running system shows. The documents: a 2006 architecture diagram with 9 boxes, a wiki last edited in 2014. The system: 4.1 million lines of COBOL, 1,214 programs, 386 batch jobs, 412 database tables. Nobody can say which of them still matter.",
                    "The 2006 diagram has nine boxes. The mainframe has 1,214 programs.", exact=True)
sa_problem.box(24, 30, 300, 180, None, "paper", rx=4)
sa_problem.head(174, 60, "the documents", size=20)
for i, t in enumerate(["2006 diagram: 9 boxes", "wiki, last edit 2014", "“see Bert”"]):
    sa_problem.text(174, 100 + i * 34, t, size=17)
sa_problem.box(436, 30, 300, 180, None, "y", rx=4)
sa_problem.head(586, 60, "the running system", size=20)
for i, t in enumerate(["4.1m lines of COBOL", "1,214 programs", "386 batch jobs", "412 tables"]):
    sa_problem.text(586, 96 + i * 28, t, size=17)
sa_problem.arrow(330, 120, 430, 120, label="≠", lx=380, ly=108)
sa_problem.note(380, 238, "which of it still matters?", "red", size=21)

sa_analogy = Doodle(760, 210, "Doodle of an archaeologist's dig: a site divided into a grid of squares, each square labelled with what was found and how deep. The archaeologist trusts the layers in the ground more than the old maps of the town.",
                    "Archaeologists trust the layers in the ground more than the old map of the town.", exact=True)
for r in range(3):
    for c in range(6):
        sa_analogy.box(30 + c * 80, 20 + r * 56, 76, 52, None, ["y", "paper", "blue"][(r + c) % 3], rx=2)
sa_analogy.box(540, 40, 200, 130, "the dig", "green", sub="what's really there", size=20, subsize=16)

sa_how = Doodle(760, 340, "Ines's heat map of MAVIS. Evidence from the running system: twelve months of job scheduler logs, the mainframe's program execution records, the call graph from the source code, and the database's table access statistics. Programs coloured by use: 37 per cent never ran in the last twelve months, 41 per cent ran rarely, 22 per cent run every night. Sixty-one programs touch customer addresses. The map shows where Lodestar has to look first.",
                "Map it by what runs, not by what's written. 37 % hasn't run for a year.", exact=True)
for i, (t, sub) in enumerate([("scheduler logs", "12 months"), ("execution records", "per program"), ("call graph", "from source"), ("table access", "DB2 stats")]):
    sa_how.box(14 + i * 186, 14, 174, 70, t, "paper", sub=sub, size=17, subsize=15)
sa_how.box(14, 110, 270, 60, "37 % never ran", "paper", sub="12 months", size=18, subsize=15)
sa_how.box(296, 110, 220, 60, "41 % rarely", "y", size=18)
sa_how.box(528, 110, 218, 60, "22 % every night", "pink", size=18)
sa_how.box(14, 196, 732, 70, "61 programs touch customer addresses", "blue", sub="→ discovery starts there", size=19, subsize=16)
sa_how.note(380, 310, "evidence from the system, checked with Bert", "pen", size=19)

ARCHAEOLOGY = dict(
    slug="software-archaeology", date=date(2027, 10, 4), meta=on_site(date(2027, 10, 4)), where="FL 19", pass_kind="contractor",
    kicker="a.k.a. “software archaeology” or legacy discovery",
    tldr="A legacy system's documents describe what someone intended, years ago. To learn what it <b>does</b>, dig in the running system: <b>scheduler logs</b>, <b>execution records</b>, the <b>call graph</b> and <b>table access</b>. Colour every program by how often it runs, find the parts that touch your problem, and only then ask the expert to explain them. Most old systems are smaller in use than on disk.",
    chips=[("Family", "inside MAVIS"), ("Lives in", "discovery/mavis-heat-map.xlsx"), ("Pairs with", "the person who knows, reading legacy code")],
    problem_side="The Grid, October 2027",
    problem="""  <p class="lead">With read access to MAVIS since 16 August, discovery can start properly. MetroVolt's documents are a <b>2006 architecture diagram</b> with nine boxes and a wiki last edited in 2014. The system itself: <b>4.1 million lines of COBOL</b>, <b>1,214 programs</b>, <b>386 batch jobs</b> and <b>412 database tables</b>.</p>
  <ul>
    <li>Hana wants to start reading code at program one. At her speed that's about <b>nine years</b>.</li>
    <li>Bert knows more than the documents, but he's one person, three days a week, retiring in 2029.</li>
    <li>Discovery ends on <b>10 December</b>. <span class="hl-pink">Ten weeks to understand thirty years.</span></li>
  </ul>""",
    problem_figs=[sa_problem],
    sides=dict(client=("Hollis", "<p>MetroVolt's own architects stopped mapping MAVIS years ago. Hollis knows the diagram is wrong and is a little embarrassed about it. He wants Wrenfield to find out what's there without making MetroVolt look as if it lost control of its own system.</p>", "Tell me what's in there, kindly."),
                vendor=("Ines and Hana", "<p>Wrenfield needs to know which parts of MAVIS Lodestar must replace, which it can ignore, and where the surprises are, in ten weeks. Reading everything is impossible; trusting the diagram is dangerous.</p>", "Let the running system tell us what matters.")),
    sides_after="Every old system has more code than anyone uses. The job is to find the part that's alive.",
    analogy_side="the archaeological dig",
    analogy="""  <p>An archaeologist arriving at an old town doesn't trust the town's old maps; they were drawn for other reasons. She <b>marks out a grid</b> and digs, recording what's found in each square and how deep. The layers in the ground say what people actually did there. The maps are useful afterwards, to explain what she found.</p>""",
    analogy_figs=[sa_analogy],
    map=[("The old town map", "The 2006 diagram and the wiki"),
         ("The grid of squares", "Programs, jobs and tables, listed from the system"),
         ("Layers in the ground", "Scheduler logs and execution records"),
         ("What's found in each square", "Run frequency, callers, tables touched"),
         ("Asking the oldest resident", "Checking the map with Bert")],
    how_side="evidence from the running system, coloured by use",
    how="""  <p>Hana and Lottie collect four kinds of <b>evidence from the running system</b>, with help from MetroVolt's mainframe team: <b>twelve months of scheduler logs</b> (which jobs ran, when, how long), <b>execution records</b> per program, a <b>call graph</b> built from the source (which program calls which), and <b>table access statistics</b> from the database.</p>
  <p>Every program is coloured by use. <b>37 %</b> never ran in twelve months. <b>41 %</b> ran rarely (month-end, year-end, a regulatory report). <b>22 %</b> run every night. Then they filter by the problem: <b>61 programs</b> read or write customer addresses. That's where discovery starts.</p>
  <p>Only then do they take the map to Bert, who corrects it in an afternoon: two “dead” programs run once a year for the regulator, and one “nightly” job is a copy nobody switched off in 2016.</p>""",
    how_figs=[sa_how],
    steps=[("List everything from the system", "Programs, jobs, tables, files: from catalogues, not documents."),
           ("Gather twelve months of runtime evidence", "Scheduler logs, execution records, table access."),
           ("Build the call graph", "Which program calls which; which job runs which."),
           ("Colour by use", "Never, rarely, nightly."),
           ("Filter by your problem", "What touches customers, addresses, billing."),
           ("Check the map with the expert", "Afterwards, with the evidence in front of you.")],
    vocab=[("Software archaeology", "Learning how an old system works from its artefacts and behaviour."),
           ("Call graph", "A map of which programs call which."),
           ("Dead code", "Code that never runs; safe to leave behind, carefully."),
           ("Heat map", "Parts of a system coloured by how much they're used."),
           ("Batch job", "A program or chain of programs run on a schedule, often at night."),
           ("Runtime evidence", "Logs and statistics from the live system.")],
    code=dict(file="discovery/mavis-heat-map.md", note="summary · Mon 4 Oct 2027", src="""
MAVIS · HEAT MAP (12 months of runtime evidence)

inventory        4.1m lines COBOL · 1,214 programs · 386 batch jobs · 412 tables
                 84 copybooks · 1 scheduler · 1 nightly window (22:00–05:30)
use (programs)   never 449 (37 %) · rarely 498 (41 %) · nightly 267 (22 %)
address-related  61 programs · 23 tables · 9 nightly jobs (incl. the 02:10 job)
Bert's fixes     2 "dead" programs run once a year for the regulator (keep)
                 1 "nightly" job is a copy left running since 2016 (ignore)
next             read the 61, starting with the 9 nightly jobs
"""),
    contract=dict(side="what discovery is contracted to produce", doc="Lodestar SOW · Schedule 3 (discovery deliverables)", date="signed 30 June 2027", stamp="discovery",
                  clauses=[("D1", "An inventory of MAVIS components relevant to Wave 1, with evidence of use.", "“with evidence of use”. Hollis wrote that. good instinct."),
                           ("D4", "A discovery report setting out findings, their effect on the Assumptions, and options.", "this map is the first page of D4.")],
                  plain="discovery is a deliverable with defined outputs. Writing “with evidence of use” into it means the inventory must come from the running system, not from old documents."),
    health=dict(now="a",
                g=("the client knows its system", ["Their map plus your evidence.", "Quick check with the experts.", "Start from the problem area."]),
                a=("documents are old, the expert is busy", ["Runtime evidence first.", "Colour by use.", "Expert checks the map."]),
                r=("the client denies the system is a mess", ["Show the evidence, not opinions.", "No adjectives about their code.", "Let the numbers speak."])),
    pressure=dict(level=3, title="thirty years in ten weeks", cost="a huge codebase · a hard deadline",
                  items=["The size is frightening. Most of it doesn't run. Say that to the team on day one.", "Never call the client's system “a mess”. It ran their business for thirty years."]),
    baseline="Each line compares <b>reading the code from the top, or trusting the 2006 diagram</b> with <b>a heat map from runtime evidence, checked with Bert</b>.",
    ratings=[(3, 4, "Hollis sees facts, not judgements."),
             (2, 4, "Ten weeks is enough once 37 % is set aside."),
             (3, 4, "Discovery effort goes where Lodestar needs it."),
             (2, 4, "What Lodestar replaces is now a list."),
             (2, 5, "The design rests on what runs."),
             (2, 4, "Surprises surface early (the 2016 copy)."),
             (3, 4, "Evidence attached to deliverable D1."),
             (3, 3, "Two weeks of collection."),
             (4, 3, "The map needs updating each wave.")],
    pitfalls=[("Reading from the top", "Years of reading for code that never runs.", "colour by use first."),
              ("Trusting the old diagram", "It shows intent, not reality.", "evidence from the running system."),
              ("Ignoring “rare” programs", "The yearly regulatory report breaks.", "ask the expert about every rare one."),
              ("Insulting the system", "The people who built it are in the room.", "numbers, not adjectives."),
              ("Mapping everything", "Discovery runs out of time.", "filter by your problem.")],
    use=["Any legacy replacement or integration.", "Documents are old or missing.", "Time is short and the codebase large."],
    skip=["The system is small and well documented, and the documents match the logs."],
    related=["<b>Who Knows How It Really Works?</b> (next note)", "<b>How Do We Read Code Nobody Owns?</b> (this volume)", "<b>Strangler Fig</b> (patterns, Vol. 1)", "<b>How Do I Design on Two Pages of Facts?</b> (vol. 1)"],
    quiz=[("Where does software archaeology get its evidence?", "From the running system: scheduler logs, execution records, the call graph and table access."),
          ("What share of MAVIS programs never ran in twelve months?", "37 %."),
          ("Why filter by the problem?", "To spend limited time on the 61 programs that touch customer addresses."),
          ("Why check the map with Bert afterwards?", "Runtime evidence misses things like yearly regulatory runs; the expert corrects it quickly with the evidence in front of him."),
          ("Why avoid calling the system a mess?", "It ran the business for thirty years, and its builders are your colleagues now.")],
    quiz_sit=[("Hollis asks for the full inventory of all 1,214 programs explained. What do you offer?", "The full list with evidence of use, and explanations for the parts Lodestar touches. Explaining dead code costs time and changes no decision.")],
    try_it="Pick an old system you depend on. Find one source of runtime evidence (logs, schedules, usage stats). Colour its parts by use. What share hasn't run in a year?",
    remember="Documents show <span class=\"hl\">what someone meant</span>. Logs show <span class=\"hl\">what really runs</span>. Dig first, then ask.",
    late=dict(when="Mon 4 October 2027 · 21:50 · hotel near The Grid",
              lines=["1,214 programs. 449 haven't run in a year. That's the best news since August.",
                     "Bert corrected our map in an afternoon and seemed pleased someone had looked.",
                     "Sixty-one programs touch addresses. Nine of them run at night. One of them runs at 02:10."]),
    sources=["Michael Feathers, <i>Working Effectively with Legacy Code</i> (2004).",
             "Serge Demeyer, Stéphane Ducasse and Oscar Nierstrasz, <i>Object-Oriented Reengineering Patterns</i> (2002).",
             "Adam Tornhill, <i>Your Code as a Crime Scene</i> (2nd ed., 2024)."],
)

# ------------------------------------------------------------------ 02 Who Knows How It Really Works?
pk_problem = Doodle(760, 240, "Doodle of Bert Ogundipe, 31 years on MAVIS, at his desk with a queue of people waiting: Hana, Bilal, Oskar, Lottie, two MetroVolt analysts and someone from Halvorsen. Each has one quick question. Bert has three days a week and retires in March 2029. On his desk, a mug that says I wrote that in 1998.",
                    "One Bert, seven quick questions a day, eighteen months to retirement.", exact=True)
pk_problem.circle(110, 120, 50, "y")
pk_problem.text(110, 126, "Bert", size=22)
pk_problem.note(110, 210, "31 years · retires Mar 2029", "pen", size=17)
for i, n in enumerate(["Hana", "Bilal", "Oskar", "Lottie", "Asif", "Rosa", "Sven's eng."]):
    pk_problem.box(220 + i * 76, 100, 70, 40, n, "paper", size=13, rx=20)
pk_problem.note(480, 70, "“one quick question”", "red", size=19)

pk_how = Doodle(760, 320, "How Lodestar captures Bert's knowledge. One door: questions go through Lottie, who batches them. Two hours a day of Bert's time, protected, no more. Pairing: Lottie sits with Bert for every session and writes the answer in Bert's book, one page per answer, reviewed by Bert. Recorded walkthroughs of the nine nightly jobs. And succession: Bert chooses what he wants to teach and to whom, including two MetroVolt engineers.",
                "One door, two protected hours, every answer written once, and Bert choosing his successors.", exact=True)
for i, (h, sub, fill) in enumerate([("one door", "questions via Lottie", "y"), ("2 hours a day", "protected", "blue"), ("written once", "Bert's book", "green"), ("recorded", "9 nightly jobs", "paper")]):
    pk_how.box(14 + i * 186, 20, 174, 100, h, fill, sub=sub, size=19, subsize=15)
pk_how.box(14, 150, 732, 80, "succession, chosen by Bert", "pink", sub="what he teaches, to whom: Lottie, and two MetroVolt engineers", size=19, subsize=15)
pk_how.note(380, 280, "by 10 December: 64 pages in Bert's book", "pen", size=19)

PERSON_WHO_KNOWS = dict(
    slug="the-person-who-knows", date=date(2027, 10, 14), meta=on_site(date(2027, 10, 14)), where="FL 19", pass_kind="contractor",
    kicker="a.k.a. “key-person dependency” and knowledge capture",
    tldr="Every legacy system has a person who knows how it really works, and every project tries to drink from them at once. Protect them: <b>one door</b> for questions, <b>limited, protected hours</b>, a <b>pair</b> who writes every answer <b>once</b>, recordings of the critical parts, and a <b>succession plan they choose themselves</b>. Treat their knowledge as the client's asset and their goodwill as yours to earn.",
    chips=[("Family", "inside MAVIS"), ("Lives in", "discovery/berts-book/ (one page per answer)"), ("Pairs with", "software archaeology, one team")],
    problem_side="The Grid, October 2027",
    problem="""  <p class="lead"><b>Bert Ogundipe</b> has worked on MAVIS for <b>31 years</b>. He wrote a fifth of it. Since September he's assigned to Lodestar three days a week (dependency D-09), and he retires in <b>March 2029</b>.</p>
  <ul>
    <li>In the second week of October, Lottie counts Bert's interruptions: <b>23 “quick questions”</b> on Tuesday, from seven people, including two from Halvorsen.</li>
    <li>Half are the same question asked by different people.</li>
    <li>On Wednesday Bert works from home. <span class="hl-pink">On Thursday he tells Elaine he's “thinking about going early”.</span></li>
  </ul>""",
    problem_figs=[pk_problem],
    sides=dict(client=("Bert", "<p>Bert has been the only person who knows for twenty years. It used to make him important; now it makes him tired. He's proud of MAVIS and worried that his last two years will be spent being drained by a supplier that's replacing his life's work.</p>", "Everybody wants my head. Nobody wants me."),
                vendor=("Ines", "<p>Without Bert, discovery takes twice as long and gets things wrong. If he leaves early, Lodestar loses its best source of truth, and Wrenfield gets blamed for driving him out. His knowledge needs capturing; his goodwill needs earning.</p>", "We need Bert for eighteen months, and he needs to want to stay.")),
    sides_after="Key-person risk is usually treated as a risk about knowledge. It's mostly a risk about a person.",
    analogy_side="the village's last thatcher",
    analogy="""  <p>A village has one thatcher left, seventy years old. Everyone needs a roof fixed. If they all knock on his door at once, he'll stop working. A sensible village gives him <b>one apprentice</b>, a <b>fixed number of jobs a week</b>, writes down what he teaches, and asks him <b>whom he wants to teach</b>. The craft survives because he wanted it to.</p>""",
    map=[("The last thatcher", "Bert"),
         ("Everyone knocking at once", "23 quick questions a day"),
         ("One apprentice", "Lottie, at every session"),
         ("A fixed number of jobs a week", "Two protected hours a day"),
         ("Whom he wants to teach", "Succession chosen by Bert")],
    how_side="one door, protected hours, written once, his succession",
    how="""  <p>Ines and Elaine sit down with Bert on <b>14 October</b>, and mostly listen. Then they agree five changes, all of which Bert shapes:</p>
  <ul>
    <li><b>One door.</b> All questions for Bert go to Lottie, who batches them, removes duplicates and checks Bert's book first.</li>
    <li><b>Two protected hours a day</b>, 10:00 to 12:00. Outside them, nobody interrupts Bert about MAVIS, including Ines.</li>
    <li><b>Written once.</b> Lottie writes every answer as one page in <b>Bert's book</b>, which Bert reviews and corrects. By 10 December it has <b>64 pages</b>.</li>
    <li><b>Recorded.</b> Bert walks through the nine nightly jobs on video, in his own words.</li>
    <li><b>Succession, chosen by Bert.</b> He picks what he wants to teach and to whom: Lottie, and two MetroVolt engineers he trusts, so the knowledge stays at MetroVolt.</li>
  </ul>
  <p>Bert stops talking about going early. In November he asks to be credited by name in the discovery report. He is, on the first page.</p>""",
    steps=[("Count the interruptions", "Who asks what, how often."),
           ("Listen to the expert first", "Ask what would make the next eighteen months good for them."),
           ("One door for questions", "Batched, de-duplicated, checked against what's written."),
           ("Protected hours", "Fewer, longer sessions."),
           ("Write every answer once", "Reviewed by the expert, in a shared place."),
           ("Let them choose their successors", "Knowledge stays with the client.")],
    vocab=[("Key-person dependency", "Relying on one person's knowledge to deliver or run something."),
           ("Knowledge capture", "Turning what's in someone's head into something others can use."),
           ("Succession plan", "Who will take over someone's role or knowledge, and how."),
           ("Tacit knowledge", "Know-how people use without being able to easily write it down."),
           ("Pairing", "Two people working together so one learns from the other."),
           ("Bus factor", "How many people would have to leave before nobody knows how something works.")],
    code=dict(file="discovery/berts-book/index.md", note="as at Fri 10 Dec 2027", src="""
BERT'S BOOK · MAVIS, in Bert's words                       64 pages · reviewed by Bert

rules        questions via Lottie · Bert's hours 10:00–12:00 · check the book first
             every answer one page · Bert reviews within a week
sections     nightly jobs (9, with video) ................ pages  1–19
             address handling (the 61 programs) .......... pages 20–37
             billing preparation and the 02:10 file ...... pages 38–49
             year-end and regulatory runs ................ pages 50–58
             "why it's like that" (history) .............. pages 59–64
successors   Lottie Marsh (Wrenfield) · Marta (MetroVolt) · Asif (MetroVolt)
questions    Oct week 2: 23 / day, 7 people · Dec: 6 / day, all via Lottie
"""),
    contract=dict(side="the dependency, and what it doesn't say", doc="Lodestar SOW · Appendix C, D-09", date="signed 30 June 2027", stamp="a person, not a resource",
                  clauses=[("D-09", "MetroVolt provides a named MAVIS expert for three days per week from the Start Date.", "the contract counts his days. it can't make him want to come in."),
                           ("11.2", "The Supplier shall transfer knowledge to MetroVolt staff throughout the Services.", "Bert's successors at MetroVolt are §11.2 too.")],
                  plain="a dependency on a named person is fragile: the contract can count their days, not their goodwill. Treat it as a relationship and plan for the day they leave."),
    health=dict(now="a",
                g=("the expert is keen to share", ["Still one door and protected hours.", "Write everything once.", "Plan succession early."]),
                a=("the expert is overloaded", ["Listen first; let them shape the rules.", "Protect their time visibly.", "Credit them by name."]),
                r=("the expert resists", ["Ask what they fear (often: being discarded).", "Involve them in choosing successors.", "Rely more on runtime evidence."])),
    pressure=dict(level=4, title="one person", cost="an expert thinking of leaving · seven teams' questions",
                  items=["If the expert leaves early, the project slows and you get the blame. Their wellbeing is your risk register.", "Protecting someone's time means saying no to your own team, including yourself."]),
    baseline="Each line compares <b>everyone asking Bert whenever they like</b> with <b>one door, protected hours, a written book and a succession he chose</b>.",
    ratings=[(3, 4, "Elaine sees Wrenfield protecting MetroVolt's expert."),
             (2, 4, "Fewer interruptions, clearer answers."),
             (3, 3, "Neutral."),
             (3, 3, "Neutral."),
             (3, 4, "Answers are checked by Bert, in writing."),
             (1, 4, "Key-person risk shrinks: 64 pages and three successors."),
             (2, 3, "The book is a shared record."),
             (3, 3, "Questions wait for the protected hours."),
             (3, 3, "A book to keep up.")],
    pitfalls=[("Draining the expert", "They leave early.", "one door and protected hours."),
              ("Asking the same thing twice", "Duplicates waste their time.", "check the book first."),
              ("Capturing knowledge but not credit", "They feel used.", "credit them by name."),
              ("Choosing their successors for them", "Quiet resistance.", "let them choose."),
              ("Keeping the knowledge at the vendor", "The client is dependent on you instead.", "successors at the client too.")],
    grimoire=[(2, "martyr-banshee", "The Martyr Banshee", "is what an overloaded expert can become when nobody protects their time.")],
    use=["Any system with one or two people who really know it.", "The expert is overloaded or near retirement.", "Several teams need the same person."],
    skip=["Knowledge is already spread and written down."],
    related=["<b>What Is Actually in There?</b> (previous note)", "<b>How Do Two Companies Work as One Team?</b> (vol. 2)", "<b>Where Is That Written Down?</b> (Eli, vol. 1)", "<b>How Do We Read Code Nobody Owns?</b> (next note)"],
    quiz=[("What is the “one door”?", "All questions for the expert go through one person, who batches and de-duplicates them."),
          ("Why protected hours?", "Fewer, longer sessions instead of constant interruptions, so the expert can work and stay."),
          ("What is Bert's book?", "One page per answer, written by Lottie and reviewed by Bert."),
          ("Why let Bert choose his successors?", "Knowledge transfers when the expert wants it to, and stays at MetroVolt."),
          ("Why is key-person risk mostly about a person?", "The contract counts days; whether they stay depends on how they're treated.")],
    quiz_sit=[("Halvorsen's engineer keeps phoning Bert directly. What do you do?", "Ask Sven, kindly, to route questions through Lottie under the team's rules, and offer the relevant pages of Bert's book. Tell Bert you've done it.")],
    try_it="Name the person on your project whose absence would hurt most. Count how often they're interrupted. Design one door, protected hours and a place where every answer is written once. Ask them who they'd like to teach.",
    remember="Protect <span class=\"hl\">the person who knows</span>: one door, protected hours, every answer <span class=\"hl\">written once</span>, successors they choose.",
    late=dict(when="Thu 14 October 2027 · 22:00 · hotel near The Grid",
              lines=["Bert said he was thinking about going early. Elaine went pale. So did I.",
                     "We mostly listened. He set the rules himself. Two hours a day, through Lottie, and his name on the report.",
                     "Note: I asked him four quick questions last week. I'm part of the problem."]),
    sources=["Michael Feathers, <i>Working Effectively with Legacy Code</i> (2004).",
             "Ikujiro Nonaka and Hirotaka Takeuchi, <i>The Knowledge-Creating Company</i> (1995): tacit knowledge.",
             "Dorothy Leonard and Walter Swap, <i>Deep Smarts</i> (2005)."],
)

# ------------------------------------------------------------------ 03 How Do We Read Code Nobody Owns?
rc_problem = Doodle(760, 240, "Doodle of program CUSTBL07, 1999, 6,400 lines of COBOL that prepares customer bills. Three people explain what it does: Bert remembers one thing, the 2006 document says another, and Hana's reading of the code suggests a third. Nobody can prove which.",
                    "Three explanations of one program, and no way to tell which is right.", exact=True)
rc_problem.box(270, 20, 220, 90, "CUSTBL07", "y", sub="1999 · 6,400 lines", size=21, subsize=15)
for i, (who, t) in enumerate([("Bert", "“rounds down”"), ("the 2006 doc", "“rounds normally”"), ("Hana", "“rounds… half down?”")]):
    rc_problem.box(14 + i * 252, 150, 228, 64, who, "paper", sub=t, size=18, subsize=15)
    rc_problem.arrow(128 + i * 252, 148, 380, 112)

rc_how = Doodle(760, 320, "Characterisation tests. Take 10,000 real accounts, run them through CUSTBL07 in MAVIS's test region, and record every output. That record is the golden master: the program's real behaviour, right or wrong. Run the new platform on the same inputs and compare field by field. Each difference is either a bug in the new code or a hidden rule in the old. Three hidden rules found, including rule 7: pro-rata standing charges rounded half down, since 1999.",
                "Record what the old code really does, then make the new code match or explain every difference.", exact=True)
rc_how.box(14, 20, 170, 80, "10,000 real", "y", sub="accounts", size=19, subsize=15)
rc_how.arrow(188, 60, 230, 60)
rc_how.box(234, 20, 170, 80, "CUSTBL07", "paper", sub="MAVIS test", size=19, subsize=15)
rc_how.arrow(408, 60, 450, 60)
rc_how.box(454, 20, 292, 80, "golden master", "green", sub="every output, recorded", size=19, subsize=15)
rc_how.box(234, 140, 170, 80, "new platform", "blue", sub="same inputs", size=19, subsize=15)
rc_how.arrow(408, 180, 450, 180)
rc_how.box(454, 140, 292, 80, "compare", "pink", sub="field by field", size=19, subsize=15)
rc_how.box(14, 250, 732, 50, "3 hidden rules · rule 7: pro-rata charges round half down (1999)", "y", size=17)

READING_CODE = dict(
    slug="reading-legacy-code", date=date(2027, 10, 27), meta=on_site(date(2027, 10, 27)), where="FL 19", pass_kind="contractor",
    kicker="a.k.a. “characterisation tests” and the golden master",
    tldr="When nobody can say for sure what old code does, stop arguing and <b>measure it</b>. Run real inputs through it and record every output: a <b>characterisation test</b>, or <b>golden master</b>. It describes what the code <b>does</b>, right or wrong. Run the new system on the same inputs, compare field by field, and treat every difference as either a bug or a <b>hidden business rule</b> someone must decide about.",
    chips=[("Family", "inside MAVIS"), ("Lives in", "tests/golden-master/custbl07/"), ("Pairs with", "the person who knows, the 02:10 job")],
    problem_side="The Grid, 27 October 2027",
    problem="""  <p class="lead"><b>CUSTBL07</b>, written in 1999, is 6,400 lines of COBOL that prepare customer bills before they go to Halvorsen. Lodestar must reproduce what it does for every migrated customer.</p>
  <ul>
    <li>Bert remembers it “rounds down”. The 2006 document says it “rounds normally”. Hana's reading suggests it rounds <b>half down</b>, sometimes.</li>
    <li>A rounding difference of a penny on 380,000 bills is <b>£3,800 a month</b>, and a regulator question.</li>
    <li><span class="hl-pink">Nobody can prove which explanation is right</span>, and nobody owns the code anymore.</li>
  </ul>""",
    problem_figs=[rc_problem],
    sides=dict(client=("Nkem and Customer Ops", "<p>MetroVolt cares about one thing: <b>bills must not change</b> when customers move to Lodestar, unless MetroVolt decides they should. A different penny on 380,000 bills means complaints, a regulator letter and a headline.</p>", "Same bill, or a decision. Never an accident."),
                vendor=("Hana and Oskar", "<p>Wrenfield has to rebuild behaviour nobody can describe reliably. Reading the code is slow and error-prone; asking people gives three answers. They need a way to <b>prove</b> what the old code does.</p>", "Let the code tell us, with real data.")),
    sides_after="Old code is the most accurate specification the client has. It's just written in a language nobody reads anymore.",
    analogy_side="the recipe nobody wrote down",
    analogy="""  <p>A bakery's founder made the best bread in town and never wrote the recipe down. Her daughter doesn't argue about what's in it. She bakes the founder's last batch alongside her own, <b>tastes and weighs both</b>, and changes her recipe until nobody can tell them apart, noting every surprise (“she always added salt twice”).</p>""",
    map=[("The founder's bread", "CUSTBL07's outputs"),
         ("Baking side by side", "Running the same 10,000 accounts through both"),
         ("Tasting and weighing", "Field-by-field comparison"),
         ("“Salt twice”", "Rule 7: pro-rata charges round half down"),
         ("Nobody can tell them apart", "Zero unexplained differences")],
    how_side="record real behaviour, compare, explain every difference",
    how="""  <p>Oskar and Hana pick <b>10,000 real accounts</b> covering every tariff and odd case Bert can name. They run them through CUSTBL07 in MAVIS's test region and <b>record every output field</b>. That record is the <b>golden master</b>: what the program actually does today, right or wrong.</p>
  <p>Then the new billing-preparation code runs on the same inputs, and a comparison tool checks <b>every field of every account</b>. The first run shows 2,914 differences. Each one is either a bug in the new code (most of them) or a <b>hidden rule</b> in the old. Three hidden rules emerge. <b>Rule 7</b>: since 1999, pro-rata standing charges for accounts with a meter exchange in the month are rounded <b>half down</b>.</p>
  <p>Hidden rules aren't Wrenfield's to decide. Each one goes to Nkem and Customer Ops with the evidence: keep it (customers' bills unchanged) or fix it (a deliberate change, communicated). They keep rule 7 for wave 1. The golden master becomes a permanent regression test.</p>""",
    how_figs=[rc_how],
    steps=[("Choose real inputs that cover the cases", "Ask the expert for the odd ones."),
           ("Record every output of the old code", "The golden master: behaviour, not intent."),
           ("Run the new code on the same inputs", "Same data, same period."),
           ("Compare field by field", "Automate it."),
           ("Classify every difference", "New bug, or hidden rule."),
           ("Let the client decide hidden rules", "Keep or change, deliberately, in writing.")],
    vocab=[("Characterisation test", "A test that records what code currently does, so changes can be detected."),
           ("Golden master", "A recorded set of outputs used as the reference."),
           ("Hidden business rule", "Behaviour the business relies on that nobody documented."),
           ("Regression test", "A test that checks nothing that worked has broken."),
           ("Parallel run", "Running old and new side by side on the same inputs."),
           ("Rounding half down", "Rounding exact halves down instead of up.")],
    code=dict(file="tests/golden-master/custbl07/README.md", note="Oskar and Hana · Wed 27 Oct 2027", src="""
GOLDEN MASTER · CUSTBL07 (billing preparation, 1999)

inputs        10,000 live accounts, all 14 tariffs, 312 odd cases from Bert's list
recorded      48 output fields × 10,000 accounts (MAVIS test region, Sep 2027 data)
run 1         2,914 differences → 2,871 new-code bugs · 43 → 3 hidden rules
hidden rules  R5  standing charge for vacant properties: 0 after 90 days
              R7  pro-rata standing charge on meter exchange: round HALF DOWN
              R11 Welsh-language flag copies to all accounts at one address
decisions     R5 keep · R7 keep for wave 1 (Nkem, DL-021) · R11 fix (Customer Ops)
now           runs on every build; 0 unexplained differences required to merge
"""),
    contract=dict(side="what the contract says about bills", doc="Lodestar SOW · Schedule 2, §5.3", date="v1.0 · Sep 2027", stamp="same bills",
                  clauses=[("5.3", "Migrated customers' bills shall be calculated identically to MAVIS, except where MetroVolt instructs a change.", "“identically”. the golden master is how we prove it."),
                           ("Sch. 4, M3", "Balances reconcile 100 % (MAVIS ↔ new platform).", "rounding is reconciliation. a penny is a failed criterion.")],
                  plain="if the contract says bills must be identical, you need proof, not explanations. A golden master is that proof, and it turns hidden rules into decisions the client owns."),
    health=dict(now="g",
                g=("trust is high", ["Share the golden master with the client's testers.", "Decide hidden rules together.", "Celebrate each one found."]),
                a=("they fear bill changes", ["Show differences, not adjectives.", "Every hidden rule to the client with evidence.", "Keep unless they choose otherwise."]),
                r=("disputes about what the old system did", ["The golden master is evidence.", "Recorded, dated inputs.", "Decisions in the log."])),
    pressure=dict(level=3, title="a penny on every bill", cost="2,914 differences on the first run",
                  items=["The first comparison always looks terrible. Most differences are your own bugs, which is good news: you found them.", "Hidden rules feel like traps. They're the client's business, written in COBOL."]),
    baseline="Each line compares <b>reading the code and asking people</b> with <b>a golden master of 10,000 real accounts, compared field by field</b>.",
    ratings=[(3, 5, "Customer Ops decides hidden rules with evidence."),
             (2, 4, "No more arguing about what it “really” does."),
             (3, 4, "Bugs found in October, not after go-live."),
             (3, 4, "Three hidden rules made explicit."),
             (3, 5, "Proof of identical bills."),
             (2, 5, "A penny difference can't reach a customer."),
             (2, 4, "Decisions logged (DL-021)."),
             (3, 3, "A week to build the harness."),
             (3, 3, "Runs on every build.")],
    pitfalls=[("Trusting explanations", "Three people, three answers.", "measure the code's behaviour."),
              ("Too few cases", "Odd tariffs aren't covered.", "ask the expert for every odd case."),
              ("Fixing hidden rules yourself", "Bills change without a decision.", "the client decides each one."),
              ("Comparing totals only", "Errors cancel out.", "field by field, account by account."),
              ("A one-off check", "Later changes break it again.", "keep it as a regression test.")],
    use=["Rebuilding behaviour from code nobody can explain.", "Outputs customers or regulators see.", "Before refactoring or replacing old code."],
    skip=["The behaviour is fully specified and already covered by tests."],
    related=["<b>Characterization Tests</b> (patterns, Vol. 4)", "<b>Who Knows How It Really Works?</b> (previous note)", "<b>What Does the 02:10 Job Really Do?</b> (next note)", "<b>How Will We Know It's Done?</b> (vol. 2)"],
    quiz=[("What is a characterisation test?", "A test that records what code currently does, right or wrong, as a reference."),
          ("What is a golden master?", "The recorded outputs of the old code for a set of real inputs."),
          ("What two things can a difference mean?", "A bug in the new code, or a hidden rule in the old."),
          ("Who decides what to do with a hidden rule?", "The client (here Nkem and Customer Ops), with evidence."),
          ("What is rule 7?", "Pro-rata standing charges on a meter exchange are rounded half down, since 1999.")],
    quiz_sit=[("A MetroVolt manager says rule 7 is “obviously a bug, just fix it”. What do you do?", "Agree it may be, and take it to Nkem as a decision: fixing it changes some customers' bills, which needs a deliberate choice and communication. Record the decision either way.")],
    try_it="Pick a piece of old code whose behaviour people argue about. Run twenty real inputs through it and record the outputs. Did anything surprise you?",
    remember="Don't argue about what old code does. <span class=\"hl\">Record it</span>, then make every difference <span class=\"hl\">a bug or a decision</span>.",
    late=dict(when="Wed 27 October 2027 · 22:30 · hotel near The Grid",
              lines=["2,914 differences on the first run. Hana went quiet. By evening, 2,871 were ours. Fixed.",
                     "Rule 7: half down, since 1999. Bert laughed: “I told you it rounded down.” He was nearly right.",
                     "Nkem decided to keep it. Same bills, on purpose."]),
    sources=["Michael Feathers, <i>Working Effectively with Legacy Code</i> (2004): characterisation tests.",
             "Emily Bache, “Approval Testing” (talks and samples, 2012–).",
             "Gerard Meszaros, <i>xUnit Test Patterns</i> (2007)."],
)

# ------------------------------------------------------------------ 04 What Does the 02:10 Job Really Do?
bj_problem = Doodle(760, 240, "Doodle of the 02:10 job as everyone describes it: one arrow from MAVIS to Halvorsen, labelled customer file. And as the scheduler shows it: fourteen steps, two of them never mentioned by anyone: step 9, ADDRFIX, which has rewritten Northern district postcodes since 2003, and step 12, which copies the file to Gareth's meter system.",
                    "Everyone describes one arrow. The scheduler shows fourteen steps.", exact=True)
bj_problem.box(24, 20, 140, 60, "MAVIS", "paper", size=19)
bj_problem.arrow(168, 50, 590, 50, label="“the customer file”", lx=380, ly=38)
bj_problem.box(596, 20, 140, 60, "Halvorsen", "paper", size=19)
for i in range(14):
    fill = "pink" if i in (8, 11) else "y"
    bj_problem.box(24 + i * 51, 130, 45, 50, str(i + 1), fill, size=17, rx=4)
bj_problem.note(250, 214, "9: ADDRFIX (2003)", "red", size=18)
bj_problem.note(560, 214, "12: copy to meters", "red", size=18)

bj_how = Doodle(760, 330, "Tracing a batch job. For each of the fourteen steps, record its program, inputs, outputs and who uses the outputs. Two findings. Step 9, ADDRFIX, since 2003, rewrites postcodes in the Northern district using a lookup table last updated in 2011, and is one cause of failing addresses. Step 12 sends a copy of the file to Gareth's meter system, an undocumented consumer that Lodestar must keep feeding.",
                "For each step: inputs, outputs, and who uses the outputs. That's how you find the side effects.", exact=True)
bj_how.box(14, 14, 160, 40, "step", "paper", size=17, rx=4)
for c, h in enumerate(["reads", "writes", "used by"]):
    bj_how.box(184 + c * 188, 14, 180, 40, h, "paper", size=17, rx=4)
rows = [("8 · EXTRACT", "customer tables", "file A", "step 9"), ("9 · ADDRFIX", "file A + table 2011", "file A (changed!)", "Halvorsen"),
        ("12 · COPYMTR", "file A", "meter drop", "Gareth's meters"), ("14 · SEND", "file A", "Halvorsen inbox", "billing")]
for r, cells in enumerate(rows):
    y = 62 + r * 46
    fill = "pink" if r in (1, 2) else "y"
    bj_how.box(14, y, 160, 40, cells[0], fill, size=15, rx=4)
    for c, t in enumerate(cells[1:]):
        bj_how.box(184 + c * 188, y, 180, 40, t, "paper", size=14, rx=4)
bj_how.note(380, 280, "ADDRFIX's 2011 table: one cause of the bad addresses", "red", size=18)
bj_how.note(380, 312, "COPYMTR: a consumer nobody listed. Lodestar must feed it too.", "pen", size=18)

BATCH_JOB = dict(
    slug="the-0210-job", date=date(2027, 11, 9), meta=on_site(date(2027, 11, 9)), where="FL 19", pass_kind="contractor",
    kicker="a.k.a. “tracing a batch job” and its side effects",
    tldr="Old batch jobs do more than anyone remembers. Trace them <b>step by step</b> from the scheduler, not from descriptions: each step's <b>program, inputs, outputs</b> and, above all, <b>who uses the outputs</b>. That's where you find the <b>side effects</b> the business quietly depends on and the <b>undocumented consumers</b> you'll have to keep feeding. Then decide, with the client, which to keep.",
    chips=[("Family", "inside MAVIS"), ("Lives in", "discovery/0210-job-trace.md"), ("Pairs with", "the billing interface, profiling the data, the RACI (vol. 2)")],
    problem_side="The Grid, 9 November 2027",
    problem="""  <p class="lead">Everyone describes the <b>02:10 job</b> the same way: “MAVIS sends the customer file to Halvorsen.” One arrow. The interface agreement IA-01 is written around it. Rework of the job is <b>excluded</b> from Wrenfield's scope (exclusion X-02).</p>
  <ul>
    <li>The scheduler shows <b>fourteen steps</b>.</li>
    <li>Step 9, <b>ADDRFIX</b>, added in 2003, rewrites postcodes for the Northern district, which is exactly wave 1's district.</li>
    <li>Step 12, <b>COPYMTR</b>, sends a copy of the file to Gareth's meter system. <span class="hl-pink">It's on nobody's list, including IA-01.</span></li>
  </ul>""",
    problem_figs=[bj_problem],
    sides=dict(client=("Hollis and Gareth", "<p>For Hollis, the 02:10 job is plumbing that works. Finding two undocumented steps is uncomfortable. For Gareth's team, COPYMTR is how their meter system learns about new customers; if Lodestar stops it, meters stop matching accounts, and it'll be Wrenfield's fault.</p>", "It's always worked. Don't break it."),
                vendor=("Ines and Bilal", "<p>X-02 excludes reworking the job, but wave 1 customers will come from Lodestar, so <b>steps 9 and 12 have to be replaced</b> for them. That's work nobody priced, and ADDRFIX may explain why addresses fail.</p>", "The exclusion assumed one arrow. There are fourteen.")),
    sides_after="Side effects are features nobody asked for and everybody uses.",
    analogy_side="the old house's mystery switch",
    analogy="""  <p>An old house has a switch by the back door that nobody uses, so the new owners plan to remove it. An electrician traces the wire first: it runs the <b>pump that keeps the cellar dry</b>, installed by a previous owner in 2003. Remove it, and the cellar floods in March. Nobody would have known until then.</p>""",
    map=[("The switch by the back door", "Step 12, COPYMTR"),
         ("The cellar pump", "Gareth's meter system, fed every night"),
         ("Tracing the wire", "Following each step's outputs to their users"),
         ("The previous owner's 2003 fix", "Step 9, ADDRFIX"),
         ("Flooding in March", "Meters not matching accounts after wave 1")],
    how_side="each step: reads, writes, and who uses it",
    how="""  <p>Bilal and Lottie trace the job from the scheduler's definition, one step at a time, with Bert's book open. For each step they write four things: the <b>program</b>, what it <b>reads</b>, what it <b>writes</b>, and <b>who uses what it writes</b>. The last column is the one that matters.</p>
  <p><b>Step 9, ADDRFIX</b> (2003) rewrites Northern district postcodes using a lookup table <b>last updated in 2011</b>. Since then, new streets and changed postcodes have been “corrected” into wrong ones. It's one of the causes of failing addresses.</p>
  <p><b>Step 12, COPYMTR</b> writes a copy of the customer file to a folder Gareth's meter system reads at 03:00. Nobody listed it because nobody at Customer Ops knew it existed, and Network Assets assumed it was part of “the file”.</p>
  <p>Both go to Elaine the same week, as facts, with a note on X-02: the exclusion priced reworking the job for MAVIS; Lodestar must now replace steps 9 and 12 for migrated customers. Kofi is added to IA-01 for COPYMTR. The cost goes into the discovery report.</p>""",
    how_figs=[bj_how],
    steps=[("Start from the scheduler's definition", "Not from anyone's description."),
           ("For each step: program, reads, writes", "From the code and the job control."),
           ("Then: who uses each output?", "Follow files and tables to their readers."),
           ("Mark side effects and hidden consumers", "Anything that changes data or feeds someone unlisted."),
           ("Check with the expert", "Bert's book, then Bert."),
           ("Tell the client as facts, with scope impact", "Before the discovery report.")],
    vocab=[("Batch job", "A sequence of steps run on a schedule."),
           ("Job control", "The definitions that tell the scheduler what to run and in what order."),
           ("Side effect", "A change a step makes beyond its stated purpose."),
           ("Hidden consumer", "A system or team using an output nobody listed."),
           ("Lineage", "Where data comes from and where it goes."),
           ("Exclusion", "Work explicitly outside the contract's scope.")],
    code=dict(file="discovery/0210-job-trace.md", note="Bilal and Lottie · Tue 9 Nov 2027", src="""
THE 02:10 JOB · traced from the scheduler (14 steps)

step  program    reads                   writes              used by
 1    SORTCUST   customer tables         work file           step 2
 …
 8    EXTRACT    customer tables         file A              step 9
 9    ADDRFIX    file A + PC_FIX (2011)  file A (postcodes   Halvorsen   ← SIDE EFFECT
                                          rewritten, North)
12    COPYMTR    file A                  /drop/meters/       Gareth's    ← HIDDEN
                                                             meter system   CONSUMER
14    SEND       file A                  Halvorsen inbox     billing
findings   ADDRFIX corrects postcodes with a 2011 table → one cause of bad addresses
           COPYMTR feeds meters nightly; not in IA-01; Kofi added
scope      X-02 excluded reworking the job for MAVIS; Lodestar must replace
           steps 9 and 12 for migrated customers → discovery report, finding 2
"""),
    contract=dict(side="what the exclusion covered, and what it didn't", doc="Lodestar SOW · Appendix C, X-02", date="signed 30 June 2027", stamp="assumption tested",
                  clauses=[("X-02", "Rework of the 02:10 MAVIS → Halvorsen batch job is excluded.", "we priced one arrow out. wave 1 needs steps 9 and 12 replaced for migrated customers."),
                           ("3.2", "If an Assumption proves materially incorrect, either Party may raise a Change Request under clause 7.", "the job's description was an assumption too. we wrote it down. good.")],
                  plain="an exclusion is based on a description of the thing excluded. If the description was wrong, the exclusion may not protect you, so tell the client early and let the change process handle it."),
    health=dict(now="a",
                g=("trust is high", ["Share the trace as soon as it's done.", "Agree scope impact together.", "Thank the expert publicly."]),
                a=("the job “has always worked”", ["Facts, not criticism of the 2003 fix.", "Show who depends on each output.", "Scope impact with the contract clause."]),
                r=("blame between departments", ["Trace and evidence only.", "Bring both departments together.", "Don't take sides on who should have known."])),
    pressure=dict(level=3, title="the side effects", cost="two surprises · an exclusion that leaks",
                  items=["Finding unpriced work feels like failure. It's what discovery is for, and you found it in November, not in September 2028.", "Gareth may react badly to “your system depends on a hidden step”. Tell Kofi first, kindly."]),
    baseline="Each line compares <b>trusting the one-arrow description</b> with <b>a step-by-step trace of reads, writes and users</b>.",
    ratings=[(3, 4, "Facts about MetroVolt's own job, shared early."),
             (3, 3, "Neutral."),
             (1, 4, "Unpriced work found before the build."),
             (2, 5, "Steps 9 and 12 are now on the scope list."),
             (3, 5, "The design feeds the hidden consumer."),
             (2, 5, "Meters won't silently stop matching accounts."),
             (2, 4, "Trace and finding on file before the report."),
             (3, 3, "A week of tracing."),
             (4, 4, "A document per job.")],
    pitfalls=[("Trusting the description", "One arrow hides fourteen steps.", "trace from the scheduler."),
              ("Ignoring who reads the outputs", "Hidden consumers break after go-live.", "follow every output to its readers."),
              ("Blaming the 2003 fix", "It solved a real problem then.", "describe it neutrally."),
              ("Hiding the scope impact", "It turns up in the change request as a surprise.", "tell the client the same week."),
              ("Forgetting the interface agreement", "The hidden consumer has no owner.", "add them to the RACI.")],
    grimoire=[(1, "turf-wars", "The Turf Wars of the Two Towers", "explains why Customer Ops never knew Network Assets was reading their file.")],
    use=["Any batch job you'll replace or feed.", "Any interface described as “one file”.", "Before relying on an exclusion."],
    skip=["The job is fully documented, recent and has tests."],
    related=["<b>What Is Actually in There?</b> (this volume)", "<b>Who Does What When Three Firms Share a Project?</b> (vol. 2)", "<b>How Bad Is the Data, Really?</b> (next note)", "<b>Batch &amp; File Transfer</b> (Ana, vol. 4)"],
    quiz=[("Which column of the trace matters most?", "Who uses each step's output."),
          ("What does ADDRFIX do?", "Since 2003 it rewrites Northern district postcodes using a lookup table last updated in 2011."),
          ("What is COPYMTR?", "A hidden step that copies the customer file to Gareth's meter system."),
          ("Why might X-02 not protect Wrenfield?", "It was based on a description of the job that turned out to be wrong; wave 1 still needs steps 9 and 12 replaced."),
          ("What was added to IA-01?", "Kofi and COPYMTR, so the hidden consumer has an owner.")],
    quiz_sit=[("Hollis says: “COPYMTR is Network Assets' problem, not Lodestar's.” What do you say?", "Agree the meter system is theirs, but if Lodestar's customers stop appearing in the file, their meters stop matching accounts. Propose Lodestar feeds the same drop for migrated customers, and add the step to IA-01.")],
    try_it="Pick a scheduled job you depend on. List its steps from the scheduler, and for each step, who reads what it writes. Is there a consumer nobody mentioned?",
    remember="Batch jobs do more than anyone remembers. Follow every output <span class=\"hl\">to whoever reads it</span>.",
    late=dict(when="Tue 9 November 2027 · 23:15 · hotel near The Grid",
              lines=["Fourteen steps. Two nobody mentioned. One of them has been fixing postcodes wrong since 2011.",
                     "Kofi didn't know COPYMTR existed either. His system has depended on it for nine years.",
                     "X-02 doesn't cover this. I'm going to have to write a change request. I promised myself it would be an honest one."]),
    sources=["Michael Feathers, <i>Working Effectively with Legacy Code</i> (2004).",
             "Martin Kleppmann, <i>Designing Data-Intensive Applications</i> (2017): batch processing and derived data.",
             "Gregor Hohpe and Bobby Woolf, <i>Enterprise Integration Patterns</i> (2003): file transfer."],
)

NOTES = [ARCHAEOLOGY, PERSON_WHO_KNOWS, READING_CODE, BATCH_JOB]
