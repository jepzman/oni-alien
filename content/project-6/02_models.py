# Series 2 · Book 3 · The Project Manager's Notebook · Vol. 6 · Models, methods, artefacts
# Narrator: Sanne. Facts: docs/larder-casebook.md, "Book 3, Vol. 6"; numbers in the comment block of 01_fitting.py.
# AI trial 1 Feb → 10 Mar 2028 (Larder's approved assistant, Lena's rules): status draft 90 → 30 min; Ghent risks
#   suggested 23, kept 9, new to the team 2, wrong 1 ("no permit needed"); plan check found 3 date mismatches.
#   Sanne's mistake Fri 11 Feb: an unchecked draft said "Ghent lease signed" (it was agreed in principle; signed 2 Mar).
# Sustainability (Mon 6 Mar 2028, Korenwolf's questionnaire, answered Mon 13 Mar): Ghent cooling on CO₂ (natural
#   refrigerant) +€7k, ≈ €1.8k a year less energy with heat recovery; shelving reused from Zuid's refit (saves ≈ €5k);
#   e-bike batteries returned to the lease supplier; unsold food to a food bank from week 1 (since Rotterdam).

MMA = ["governance"]

# ------------------------------------------------------------------ 05 Which Tools, When?
tb_problem = Doodle(760, 260, "Doodle of Monday 14 February 2028, Nadia's second week. She has read the playbook and Sanne's notebooks: critical path, earned value, Monte Carlo, RACI, MoSCoW, Scrum, Kanban, Tuckman, wideband Delphi, engagement matrices. Her question: which of all these do I use on Ghent? Sanne realises she has never written down how she chooses.",
                    "Nadia: “Which of all these do I use on Ghent?” Sanne has never written down how she chooses.", exact=True)
for i, t in enumerate(["critical path", "earned value", "Monte Carlo", "RACI", "MoSCoW", "Scrum", "Kanban", "Tuckman", "Delphi", "engagement matrix"]):
    r, c = divmod(i, 5)
    tb_problem.box(14 + c * 148, 20 + r * 62, 138, 50, t, "paper" if (i % 2) else "y", size=14, rx=6)
tb_problem.note(380, 176, "a shelf of tools, no rule for picking one", "red", size=19)
tb_problem.note(380, 214, "Nadia's question is the right one", "pen", size=17)

tb_analogy = Doodle(760, 250, "Doodle of a mechanic's workshop. Nobody uses every tool on every car. The mechanic starts from the symptom: a noise from the front wheel, so the jack, the torque wrench and a stethoscope. The wall of tools is sorted by job, not alphabetically.",
                    "A mechanic starts from the symptom, then picks the tool. The wall is sorted by job.", exact=True)
tb_analogy.row([("symptom", "a noise, front left", "pink"), ("question", "bearing or brake?", "y"), ("tool", "jack, stethoscope", "green")], y=40, h=96, gap=40, size=18, subsize=14, arrows=True)
tb_analogy.note(380, 196, "start from the question, not the toolbox", "pen", size=19)

tb_how = Doodle(760, 470, "Sanne's toolbox page, February 2028, sorted by the question being asked. What decides the date: the network diagram and critical path; how sure, three-point estimates; a date as odds, Monte Carlo. Is the money buying progress: earned value, on fixed-price or long work. What's in and out: the scope statement, MoSCoW, the work breakdown. Who does what: RACI. Who's affected: the register, power and interest. What could happen: the risk register, expected monetary value. Which way to run it: predictive, adaptive or hybrid; Scrum for a team building in sprints, Kanban for a flow of requests. How is the team: Tuckman's stages. How much to lead: situational leadership. Will people take up the change: a change model. Each line names the note.",
                "Sorted by question, not by name. Each tool points to the note that shows it on a real launch.", exact=True)
rows_tb = [("what decides the date?", "network + critical path · three-point · Monte Carlo"),
           ("is the money buying progress?", "earned value (long or fixed-price work)"),
           ("what's in, what's out?", "scope statement · MoSCoW · work breakdown"),
           ("who does what? who's affected?", "RACI · stakeholder register · power / interest"),
           ("what could happen?", "risk register · EMV · responses"),
           ("which way to run the work?", "predictive · adaptive (Scrum, Kanban) · hybrid"),
           ("how is the team doing?", "Tuckman's stages · levelling"),
           ("how much do I lead this person?", "situational leadership"),
           ("will people take up the change?", "a change model (aware → able → kept)")]
for i, (q, t) in enumerate(rows_tb):
    y = 12 + i * 50
    tb_how.box(8, y, 290, 42, q, "y" if i % 2 else "blue", size=14, rx=6)
    tb_how.text(312, y + 27, t, anchor="start", size=14)

TOOLBOX = dict(
    slug="models-and-methods",
    kicker="a.k.a. models, methods and artifacts: choosing the right tool for the question",
    tldr="The PMBOK Guide lists dozens of <b>models</b> (ways of thinking: situational leadership, Tuckman's team stages, change models), <b>methods</b> (ways of doing: critical path, earned value, Monte Carlo, Scrum, Kanban, RACI) and <b>artefacts</b> (the documents they produce). None is required. Choose by the <b>question</b> you need answered on this project, the way a mechanic starts from the symptom: what decides the date? is the money buying progress? who's affected? A toolbox page sorted by question is worth more than knowing every tool by name.",
    chips=[("Family", "models, methods, artefacts"), ("Lives in", "one page sorted by question, in the playbook"), ("Pairs with", "tailoring, the playbook, every earlier note")],
    pmbok=dict(covers="the models, methods and artefacts the guide describes, and how to choose among them for a given project",
               domains=MMA, processes=[], principles=["Adopt a holistic view", "Build an empowered culture"], focus=["planning"],
               older="6th: “tools and techniques” in every process (the ITTOs). 7th: a section on models, methods and artifacts. 8th: the same, linked to the processes."),
    problem_side="Larder, Monday 14 February 2028",
    problem="""  <p class="lead"><b>Nadia</b> joined on 7 February as Larder's second project manager. In her second week she has read the playbook and Sanne's notebooks: critical path, earned value, Monte Carlo, RACI, MoSCoW, Scrum, Kanban, Tuckman, wideband Delphi, engagement matrices. <span class="hl-pink">“Which of all these do I use on Ghent?”</span> Sanne realises she has never written down how she chooses. She just knows, from six launches, and knowing isn't something Nadia can read.</p>
  <ul>
    <li>The tools are known by name, not by the question they answer.</li>
    <li>Using everything is as wrong as using nothing.</li>
    <li>The choice lives in one person's experience.</li>
  </ul>""",
    problem_figs=[tb_problem],
    analogy_side="the mechanic's wall",
    analogy="""  <p>A mechanic doesn't use every tool on every car. She starts from the <b>symptom</b> (a noise from the front left wheel), turns it into a <b>question</b> (bearing or brake?) and then picks the <b>tool</b>: the jack, a stethoscope, the torque wrench. Her wall is sorted <b>by job</b>, not alphabetically, so an apprentice can find the right one.</p>""",
    analogy_figs=[tb_analogy],
    map=[("The symptom", "“Ghent's date feels tight”"),
         ("The question", "What decides the date?"),
         ("The tool", "The network and critical path; Monte Carlo for odds"),
         ("A wall sorted by job", "The toolbox page, sorted by question"),
         ("The apprentice", "Nadia, in her second week")],
    how_side="a page sorted by question, and three kinds of tool",
    how="""  <p>Sanne writes the <b>toolbox page</b> with Nadia that afternoon, sorted by <b>question</b>. <b>What decides the date?</b> The network and critical path; three-point estimates for how sure; Monte Carlo when two chains meet or a yes-or-no risk sits on the path (Antwerp's permit). <b>Is the money buying progress?</b> Earned value, on long or fixed-price work; not on an eight-week Dutch launch. <b>What's in and out?</b> The scope statement, MoSCoW, the work breakdown. <b>Who does what, who's affected?</b> RACI, the register, power and interest. <b>What could happen?</b> The register, EMV, responses. <b>Which way to run the work?</b> Predictive for the fit-out; adaptive (Scrum for a team building in sprints, Kanban for a flow of requests) for the apps; hybrid for a launch. And three <b>models</b> for people: <b>Tuckman's stages</b> (a new team storms; plan for it), <b>situational leadership</b> (direct a beginner, delegate to an expert; she uses it on Nadia), and a <b>change model</b> (people must know, be able, and keep doing it: Ghent's pickers on the new handhelds). For Ghent, Nadia picks nine of the tools. Each line on the page points to the note that shows the tool on a real launch.</p>""",
    how_figs=[tb_how],
    steps=[("Write the questions this project must answer", "Date, money, scope, people, risk."),
           ("Pick the lightest tool that answers each", "Not every tool you know."),
           ("Sort your toolbox by question", "So others can use it."),
           ("Use models for people, methods for work", "Know which you're reaching for."),
           ("Name what you're not using, and why", "On the tailoring sheet."),
           ("Point each tool to a worked example", "A tool without an example is a word.")],
    vocab=[("Model", "A way of thinking about a situation: Tuckman's stages, situational leadership."),
           ("Method", "A way of doing something: critical path, earned value, Scrum."),
           ("Artefact", "A document or other product of the work: a register, a plan, a burn-up."),
           ("Situational leadership", "Leading differently by how able and willing a person is: direct, coach, support, delegate."),
           ("Tuckman's stages", "Forming, storming, norming, performing (and adjourning)."),
           ("Change model", "Steps people go through to take up a change: aware, willing, able, sustained.")],
    code=dict(file="programme/05-toolbox.md", note="Sanne and Nadia, Monday 14 February 2028", plain=True, src="""
# TOOLBOX · sorted by the question you need answered            14 Feb 2028

QUESTION                          TOOL                                  SEE (book 3)
What decides the date?            network diagram, critical path         vol. 3 · 08-09
How sure is that date?            three-point estimates; Monte Carlo     vol. 3 · 06; vol. 5 · 12
Is the money buying progress?     earned value (long / fixed price)      vol. 4 · 06
What's in, what's out?            scope statement, MoSCoW, WBS            vol. 3 · 03-04
Who does what?                    RACI                                    vol. 4 · 09
Who's affected, how much?         register, power / interest              vol. 5 · 01-02
What could happen?                risk register, EMV, responses           vol. 5 · 09-13
Which way to run the work?        predictive / adaptive / hybrid          vol. 1 · 11
How is the team?                  Tuckman's stages, levelling             vol. 4 · 12, 14
How much do I lead this person?   situational leadership                  this volume · 10
Will people take up the change?   change model: aware → able → kept       Ghent handhelds

GHENT (Nadia)   9 tools chosen · not using: earned value (fixed price, 12 weeks),
                Monte Carlo unless the permit range widens
"""),
    tools="tools: the questions, one page sorted by them, and the earlier notes as worked examples.",
    dial=[("Light", "small work", ["Three questions, three tools.", "No page.", "Ask a colleague."]),
          ("Standard", "a city launch", ["A toolbox page sorted by question.", "Chosen tools on the tailoring sheet.", "Each pointing to an example."]),
          ("Heavy", "an organisation's method", ["A method library with guidance.", "Training per tool.", "Tool choice reviewed at gates."])],
    baseline="Each line compares <b>a shelf of tools known by name</b> to <b>a toolbox page sorted by question, with worked examples</b>.",
    ratings=[(3, 4, "Tools serve the project's real questions."),
             (3, 4, "The right estimating tool for each date."),
             (3, 4, "Risk tools used where risk lives."),
             (3, 4, "Anyone can see why a tool was chosen."),
             (3, 3, "Neutral."),
             (3, 4, "Nadia chooses for Ghent herself."),
             (3, 4, "The page changes as questions change."),
             (3, 3, "Neutral."),
             (3, 4, "Fewer tools, used well.")],
    pitfalls=[("Every tool, every time", "Overhead, no extra insight.", "one tool per question."),
              ("The favourite tool", "Every problem looks like a nail.", "start from the question."),
              ("Models as rules", "People aren't stages.", "use models to think, not to label."),
              ("Tools without examples", "Words, not skills.", "point each to a worked case.")],
    use=["When planning a project's method.", "When a new project manager starts.", "When a question has no tool.", "When a tool is used out of habit."],
    skip=["Never; even a small job has questions."],
    related=["<b>How Light Can We Go?</b> (this volume)", "<b>Plan It All, or Learn As We Go?</b> (vol. 1)", "<b>Why Is the Team Arguing?</b> (vol. 4)", "<b>Who Serves Whom?</b> (this volume)"],
    quiz=[("Model or method: earned value?", "A method. Tuckman's stages is a model."),
          ("When does Sanne reach for Monte Carlo?", "When chains meet or a yes-or-no risk sits on the path, and the date matters."),
          ("Why not earned value on Ghent?", "A fixed-price builder and a short launch: the gates and status answer the money question."),
          ("Ghent's new pickers resist the handhelds. Which tool?", "A change model: are they aware why, able to use them, and is it kept up? Then train, not order."),
          ("A colleague uses Scrum for the fit-out. What do you ask?", "What question it answers there; a builder's sequence needs a network and dates, Scrum suits a team building in sprints.")],
    try_it="Write the five questions your project must answer. Next to each, the one tool you'd use, and where you've seen it used well.",
    remember="Start from the <span class=\"hl\">noise</span>, then pick the <span class=\"hl\">tool</span>.",
    sources=["Project Management Institute, <i>PMBOK Guide</i>, Eighth Edition (2025): models, methods and artifacts.",
             "Paul Hersey and Kenneth Blanchard, <i>Management of Organizational Behavior</i> (1969 onwards): situational leadership.",
             "Bruce Tuckman, “Developmental Sequence in Small Groups” (1965).",
             "Jeffrey Hiatt, <i>ADKAR</i> (2006): a change model."],
)

# ------------------------------------------------------------------ 06 Which Documents Earn Their Keep?
ar_problem = Doodle(760, 260, "Doodle of Monday 6 December 2027. The project file has seventy-three pages: fifty-eight from Rotterdam, fifteen from Antwerp. Eindhoven used twenty. Grace asks which pages the playbook should point to. Nobody knows which were read after they were written.",
                    "73 pages in the file; Eindhoven used 20. Which ones were read after they were written?", exact=True)
ar_problem.box(20, 24, 330, 140, None, "paper")
ar_problem.head(185, 60, "the project file", size=19)
ar_problem.text(185, 94, "Rotterdam 58 + Antwerp 15", size=16)
ar_problem.text(185, 122, "= 73 pages", size=16)
ar_problem.box(410, 24, 330, 140, None, "y")
ar_problem.head(575, 60, "Eindhoven", size=19)
ar_problem.text(575, 94, "used 20", size=16)
ar_problem.text(575, 122, "which, and why?", size=16)
ar_problem.note(380, 210, "a document's value is in being used, not in being written", "red", size=17)
ar_problem.note(380, 242, "nobody had asked of any page: who read this?", "pen", size=16)

ar_analogy = Doodle(760, 250, "Doodle of clearing a kitchen drawer. Everything out on the table. Used this month goes back. Used this year goes in the cupboard. Two things that do the same job: keep one. Not used in a year: out. The drawer closes again.",
                    "Clear the drawer: used this month, back; two that do one job, keep one; unused for a year, out.", exact=True)
ar_analogy.row([("used often", "back in", "green"), ("used sometimes", "cupboard", "y"), ("same job twice", "keep one", "blue"), ("never used", "out", "pink")], y=40, h=96, size=17, subsize=13)
ar_analogy.note(380, 196, "the drawer closes again", "pen", size=19)

ar_how = Doodle(760, 470, "The artefact review of 6 December 2027. Each of the seventy-three pages sorted by one question: was it used after it was written, and by whom? Used as is: twenty-one, among them the risk register, the issue log, the money rules, the gate criteria. Used shortened: fourteen, among them the charter and the status report. Merged into another page: twelve, for example the three schedule views into one milestone chart. Not used: twenty-six, among them earned value, the communications plan of Rotterdam's tailoring, the RACI's long version. Result: the launch kit, eighteen templates, each one page or less.",
                "73 pages, one question each: used after it was written? → 21 as is, 14 shortened, 12 merged, 26 not used → an 18-template kit.", exact=True)
bars = [("as is", 21, "green"), ("shortened", 14, "y"), ("merged", 12, "blue"), ("not used", 26, "pink")]
for i, (lab, n, f) in enumerate(bars):
    y = 20 + i * 62
    ar_how.text(16, y + 32, lab, anchor="start", size=16)
    ar_how.box(140, y, n * 18, 46, str(n), f, size=16, rx=4)
ar_how.box(14, 280, 732, 176, None, "paper")
ar_how.head(380, 308, "the launch kit: 18 templates", size=17)
kit = ["tailoring sheet · charter (½ page) · stakeholder register", "local rules map · money rules · budget + reserves",
       "people from demand · RACI · must-have list (WBS)", "milestone chart · risk register · issue log · change log",
       "Friday status (5 lines) · gate criteria · go / no-go", "handover checklist · closing report with benefit checks"]
for i, t in enumerate(kit):
    ar_how.text(380, 338 + i * 20, t, size=13)

ARTEFACTS = dict(
    slug="artefact-review",
    kicker="a.k.a. artifacts: which project documents earn their keep",
    tldr="Every project produces <b>artefacts</b>: plans, registers, logs, reports. Their value is in being <b>used</b>, not written. After a project (or a few), review each one with one question: <b>was it used after it was written, and by whom?</b> Keep what was used, shorten what was used in part, merge what did the same job twice, and drop what nobody read. What's left becomes a small <b>template kit</b>. The register you read every week is worth ten plans nobody opened.",
    chips=[("Family", "models, methods, artefacts"), ("Lives in", "a one-off review, then a kit in the playbook"), ("Pairs with", "the project file, the playbook, tailoring")],
    pmbok=dict(covers="the artefacts projects produce (strategy, logs and registers, plans, hierarchy charts, baselines, visual data, reports, agreements) and choosing which earn their keep",
               domains=MMA, processes=["Manage Project Knowledge"], principles=["Focus on value"], focus=["closing"],
               older="6th: outputs of every process, the project documents list. 7th: artifacts (with models and methods). 8th: the same, with the processes."),
    problem_side="Larder, Monday 6 December 2027",
    problem="""  <p class="lead">The project file has <b>73 pages</b>: 58 from Rotterdam, 15 from Antwerp. Eindhoven, tailored, used 20. Grace, merging the playbooks, asks which pages the playbook should point to. <span class="hl-pink">Nobody knows which pages were read after they were written.</span> Some were opened every Friday for three months; some were written, filed and never seen again. Both kinds look the same in the file.</p>
  <ul>
    <li>Documents were judged by being complete, not by being used.</li>
    <li>Some did the same job twice (three schedule views).</li>
    <li>A new project manager can't tell which to copy.</li>
  </ul>""",
    problem_figs=[ar_problem],
    analogy_side="clearing the kitchen drawer",
    analogy="""  <p>Clearing a kitchen drawer, you take <b>everything out</b>. Used this month: back in. Used this year: the cupboard. <b>Two things that do the same job</b> (three bottle openers): keep the best one. Not used in a year: out. The drawer closes again, and you can find the scissors.</p>""",
    analogy_figs=[ar_analogy],
    map=[("Everything on the table", "All 73 pages of the project file"),
         ("Used this month", "The risk register, the issue log, the Friday status"),
         ("Three bottle openers", "Three schedule views → one milestone chart"),
         ("Not used in a year", "Earned value, the long RACI"),
         ("A drawer that closes", "The launch kit: 18 templates")],
    how_side="one question per page, four piles, one kit",
    how="""  <p>Sanne and Grace go through all 73 pages on <b>Monday 6 December</b>, asking of each: <b>was it used after it was written, and by whom?</b> The evidence: who opened it, what it was quoted in, whether Eindhoven copied it. <b>Used as is: 21</b>, among them the risk register, the issue log, the money rules, the gate criteria and the change log, all opened weekly and quoted in decisions. <b>Used shortened: 14</b>: the charter (to half a page), the status (to five lines), the plan (to the playbook's timeline). <b>Merged: 12</b>, such as the three schedule views into one milestone chart, or the lessons page into the closing report. <b>Not used: 26</b>, among them the earned-value sheets (the right tool once, in Rotterdam, but not again), the long RACI and the extras list after the baseline. The result is the <b>launch kit</b>: <b>18 templates</b>, each a page or less, in playbook v4. Nothing is deleted. The full file stays as the worked example, and the 26 unused pages are still there for the project that needs them.</p>""",
    how_figs=[ar_how],
    steps=[("Put every artefact on the table", "The whole file."),
           ("Ask of each: used after it was written?", "By whom, how often, for what decision?"),
           ("Sort into four piles", "As is, shortened, merged, not used."),
           ("Build a small kit from the first three", "One page each where possible."),
           ("Keep the rest as examples", "Not as defaults."),
           ("Repeat after the next few projects", "Usage changes.")],
    vocab=[("Artefact", "A document, template or other product of project work."),
           ("Log", "A running record: issues, changes, decisions."),
           ("Register", "A list of items with their attributes: risks, stakeholders."),
           ("Baseline", "An approved version used for comparison."),
           ("Template", "A blank artefact to start from."),
           ("Template kit", "The small set of templates a method says to use.")],
    code=dict(file="programme/06-artefact-review.md", note="Sanne and Grace, Monday 6 December 2027", plain=True, src="""
# ARTEFACT REVIEW · the project file, 73 pages                       6 Dec 2027

QUESTION   used after it was written? by whom? for which decision?
AS IS      21   risk register · issue log · money rules · gate criteria · change log ·
                go / no-go · handover checklist · people from demand · ...
SHORTENED  14   charter → ½ page · status → 5 lines · plan → playbook timeline · ...
MERGED     12   3 schedule views → 1 milestone chart · lessons → closing report · ...
NOT USED   26   earned-value sheets · long RACI · extras list after baseline · ...
TOTAL      73

LAUNCH KIT (playbook v4)  18 templates, one page or less each:
  tailoring sheet · charter · stakeholder register · local rules map · money rules ·
  budget + reserves · people from demand · RACI (short) · must-have list (WBS) ·
  milestone chart · risk register · issue log · change log · Friday status ·
  gate criteria · go / no-go · handover checklist · closing report + benefit checks
KEPT      the full file stays online as the worked example (nothing deleted)
"""),
    tools="tools: the whole file, one question, four piles, and a kit.",
    dial=[("Light", "small work", ["After the job, ask what you'd write again.", "Keep that.", "Bin the rest."]),
          ("Standard", "a repeated kind of project", ["Review every artefact for use.", "A small template kit.", "Repeat every few projects."]),
          ("Heavy", "regulated work", ["Required artefacts kept by rule.", "A records policy.", "Kit reviewed by the PMO."])],
    baseline="Each line compares <b>a 73-page file where everything looks equally important</b> to <b>a review by use and an 18-template kit</b>.",
    ratings=[(3, 5, "Documents that are used, not filed."),
             (3, 3, "Neutral."),
             (3, 4, "The registers that caught problems are kept."),
             (3, 4, "The kit says which documents matter."),
             (3, 3, "Neutral."),
             (3, 4, "Teams fill in short templates."),
             (3, 4, "Unused pages stay available as examples."),
             (3, 3, "Neutral."),
             (2, 5, "18 templates instead of 73 pages.")],
    pitfalls=[("Judged by completeness", "Long, unread documents.", "judge by use."),
              ("Deleting the examples", "The next unusual project needs them.", "keep them as examples."),
              ("Duplicates kept", "Two versions of the truth.", "merge what does one job."),
              ("One review forever", "Usage changes.", "repeat every few projects.")],
    use=["After a few projects of the same kind.", "Before building a playbook or kit.", "When a new PM asks what to copy.", "When documents multiply."],
    skip=["A one-off project: the lessons page is enough."],
    related=["<b>Can a Launch Be a Recipe?</b> (this volume)", "<b>What Did We Learn?</b> (vol. 2)", "<b>How Light Can We Go?</b> (this volume)", "<b>Docs as Code</b> (Ana, vol. 3)"],
    quiz=[("What was the one question?", "Was it used after it was written, and by whom?"),
          ("Name the four piles and their counts.", "As is 21, shortened 14, merged 12, not used 26."),
          ("Why weren't the 26 deleted?", "They stay as worked examples for a project that needs them; they're just not defaults."),
          ("Nadia wants earned value for Ghent “because Rotterdam had it.” What do you say?", "Ask what question it answers there; for a short fixed-price launch the gates and status do; it's in the file if she needs it."),
          ("Which three pages were merged into one?", "The three schedule views, into one milestone chart.")],
    try_it="List your project's documents. Next to each, write who opened it in the last month. Merge or drop the ones with no name.",
    remember="Everything on the table. Keep what was <span class=\"hl\">used</span>. Close the <span class=\"hl\">drawer</span>.",
    sources=["Project Management Institute, <i>PMBOK Guide</i>, Eighth Edition (2025): models, methods and artifacts.",
             "Project Management Institute, <i>PMBOK Guide</i>, Seventh Edition (2021): section 4.6, artifacts.",
             "Agile Manifesto (2001): “working software over comprehensive documentation”."],
)

# ------------------------------------------------------------------ 07 Can AI Help?
ai_problem = Doodle(760, 260, "Doodle of Friday 11 February 2028 and Sanne's mistake for this collection. In the second week of an AI trial, Sanne lets the assistant draft the programme's Friday status from her Thursday notes and sends it to Joost after a quick skim. One line says Ghent's lease is signed. It was agreed in principle; it is signed on 2 March. Joost congratulates Femke before Sanne notices.",
                    "An AI-drafted status, skimmed and sent: “Ghent lease signed.” It was agreed in principle.", exact=True)
ai_problem.box(20, 24, 330, 140, None, "blue")
ai_problem.head(185, 60, "the draft said", size=19)
ai_problem.text(185, 94, "“Ghent lease signed”", size=16)
ai_problem.text(185, 122, "sent after a skim", size=16)
ai_problem.box(410, 24, 330, 140, None, "pink")
ai_problem.head(575, 60, "the notes said", size=19)
ai_problem.text(575, 94, "“lease agreed in principle”", size=16)
ai_problem.text(575, 122, "signed on 2 March", size=16)
ai_problem.note(380, 210, "fluent and wrong reads exactly like fluent and right", "red", size=18)
ai_problem.note(380, 242, "the sender owns every line, whoever drafted it", "pen", size=16)

ai_analogy = Doodle(760, 250, "Doodle of a new, very fast assistant in an office. They draft letters in seconds, summarise long reports and spot mismatched dates. They have never been to the site, don't know the client, sometimes fill a gap with something that sounds right, and must not see the files marked confidential. A good manager uses them a lot, and reads everything before it leaves the building.",
                    "A fast new assistant: drafts, summaries, checks. Hasn't been to the site. Read everything before it leaves.", exact=True)
ai_analogy.box(14, 30, 350, 120, None, "green")
ai_analogy.head(189, 60, "fast at", size=18)
ai_analogy.text(189, 92, "drafts · summaries · checks", size=15)
ai_analogy.text(189, 120, "translations to correct", size=15)
ai_analogy.box(396, 30, 350, 120, None, "pink")
ai_analogy.head(571, 60, "doesn't know", size=18)
ai_analogy.text(571, 92, "the site, the people", size=15)
ai_analogy.text(571, 120, "fills gaps that sound right", size=15)
ai_analogy.note(380, 200, "use them a lot; read everything before it leaves", "pen", size=18)

ai_how = Doodle(760, 470, "Results of the six-week AI trial, 1 February to 10 March 2028, on Larder's approved assistant under Lena's rules. Drafting the Friday status from notes and the issue log: ninety minutes down to thirty, every line checked against its source. Summarising meetings in English and Dutch: used weekly. Suggesting risks for Ghent from the lessons pages: twenty-three suggested, nine kept, two new to the team, one wrong: it said Ghent needed no environmental permit because Antwerp's had been granted. Checking the plan: three dates that disagreed between the roadmap and Ghent's plan. Translations: drafts for the Flemish writer to correct. Rules: approved tool only; no personal data; a person checks every fact against its source; the sender owns it; decisions and conversations stay human.",
                "Six weeks: status drafts 90 → 30 minutes; 23 risks suggested, 9 kept, 1 dangerously wrong; 3 date clashes found.", exact=True)
uses = [("draft the Friday status", "90 → 30 min, checked line by line", "green"),
        ("summarise meetings (en, nl)", "weekly; owner reads before sending", "green"),
        ("suggest risks for Ghent", "23 → 9 kept, 2 new, 1 wrong (permit)", "y"),
        ("check the plan for clashes", "3 dates disagreed: roadmap vs Ghent", "green"),
        ("first drafts of translations", "for the Flemish writer to correct", "y")]
for i, (u, r, f) in enumerate(uses):
    y = 14 + i * 56
    ai_how.box(8, y, 744, 48, None, f, rx=6)
    ai_how.text(22, y + 30, u, anchor="start", size=15)
    ai_how.text(740, y + 30, r, anchor="end", size=14)
ai_how.box(8, 300, 744, 158, None, "blue")
ai_how.head(380, 328, "Lena's rules and Sanne's", size=17)
for i, t in enumerate(["only Larder's approved assistant · no personal data, no contract terms in other tools",
                       "every fact checked against its source before it leaves",
                       "the sender owns every line · decisions and conversations stay with people",
                       "say when a text was drafted with AI"]):
    ai_how.text(380, 360 + i * 25, t, size=13)

ai_deep1 = Doodle(760, 300, "Where AI helps in project work and where it doesn't, as two columns. Helps: first drafts of status and minutes; summaries of long documents; consistency checks across plans; suggesting risks from past lessons; translation drafts; formulas and small scripts. Doesn't: judgment about people; knowing what happened on site this morning; decisions with consequences; trust and relationships; facts it can't see; anything confidential outside approved tools. In the middle: always checked by a person who knows.",
                  "Drafts, summaries, checks: yes. Judgment, relationships, decisions, unseen facts: no. A person checks in between.", exact=True)
ai_deep1.box(14, 14, 330, 270, None, "green")
ai_deep1.head(179, 42, "helps", size=18)
for i, t in enumerate(["first drafts: status, minutes", "summaries of long documents", "consistency checks", "risks from past lessons", "translation drafts", "formulas, small scripts"]):
    ai_deep1.text(179, 78 + i * 34, t, size=14)
ai_deep1.box(416, 14, 330, 270, None, "pink")
ai_deep1.head(581, 42, "doesn't", size=18)
for i, t in enumerate(["judgment about people", "what happened today", "decisions and their ownership", "trust, relationships", "facts it can't see", "confidential, off-tool"]):
    ai_deep1.text(581, 78 + i * 34, t, size=14)
ai_deep1.box(350, 120, 60, 60, "✓", "y", size=22)
ai_deep1.note(380, 200, "a person", "pen", size=12)

AI = dict(
    slug="ai-in-project-work",
    kicker="a.k.a. AI in project work: drafts, summaries, checks, and who owns the result",
    tldr="AI assistants are good at <b>first drafts</b> (status, minutes, risk lists), <b>summaries</b>, <b>consistency checks</b> across plans and <b>translation drafts</b>, and they save real time. They don't know what happened on site this morning, they can fill a gap with something that <b>sounds right and isn't</b>, and they must not see confidential data outside an approved tool. Use them a lot, under three rules: an <b>approved tool</b> only; a person <b>checks every fact against its source</b>; the <b>sender owns every line</b>. Decisions, judgment about people and relationships stay human.",
    chips=[("Family", "models, methods, artefacts"), ("Lives in", "the approved assistant, Lena's rules, and a habit of checking"), ("Pairs with", "status reports, the risk register, the toolbox")],
    pmbok=dict(covers="using artificial intelligence in project work: where it helps, its limits, confidentiality, accountability and checking",
               domains=MMA, processes=[], principles=["Be an accountable leader", "Embed quality into processes and deliverables"], focus=["executing", "monitoring and controlling"],
               older="Not in the 6th or 7th editions. The 8th adds AI in project management as a newer topic."),
    problem_side="Larder, Friday 11 February 2028",
    problem="""  <p class="lead">This is <b>Sanne's mistake</b> for this collection. In the second week of a six-week trial of Larder's <b>approved AI assistant</b>, she lets it draft the programme's Friday status from her Thursday notes and the issue log. It reads well. She skims it and sends it to Joost. One line says <b>“Ghent lease signed.”</b> Her notes said <b>“agreed in principle”</b>; it's signed on 2 March. <span class="hl-pink">Joost congratulates Femke in the leadership channel before Sanne notices.</span> Corrected within the hour, no harm done, except to the thing a status report is for: being believed.</p>
  <ul>
    <li>A fluent draft read as a checked one.</li>
    <li>“Agreed in principle” became “signed”: the gap was filled with what usually comes next.</li>
    <li>The sender was Sanne, whoever drafted it.</li>
  </ul>""",
    problem_figs=[ai_problem],
    analogy_side="the fast new assistant",
    analogy="""  <p>Imagine a new assistant who drafts a letter in seconds, summarises a fifty-page report over coffee and spots that two documents disagree on a date. They've <b>never been to the site</b>, don't know the client, sometimes <b>fill a gap with something that sounds right</b>, and mustn't see the files marked confidential. A good manager uses them a lot, and <b>reads everything before it leaves the building</b>.</p>""",
    analogy_figs=[ai_analogy],
    map=[("Drafts in seconds", "Friday status: 90 minutes → 30"),
         ("Spots disagreeing dates", "3 clashes between the roadmap and Ghent's plan"),
         ("Never been to the site", "“Ghent needs no permit, Antwerp's was granted”"),
         ("Fills a gap that sounds right", "“agreed in principle” → “signed”"),
         ("Reads everything before it leaves", "Every fact checked; the sender owns it")],
    how_side="six weeks, five uses, four rules",
    how="""  <p>The trial runs from <b>1 February to 10 March 2028</b>, on Larder's approved assistant (company contract, data not used for training), under <b>Lena's rules</b>: no personal data, no contract terms in any other tool. Five uses earn their place. <b>Drafting the Friday status</b> from notes and the issue log: <b>90 minutes → 30</b>, with every line checked against its source after 11 February. <b>Summarising meetings</b> in English and Dutch. <b>Suggesting risks</b> for Ghent from the Rotterdam and Antwerp lessons pages: <b>23</b> suggested, <b>9</b> kept, <b>2</b> that nobody on the team had thought of, and <b>1 dangerously wrong</b>: Ghent needs no environmental permit because Antwerp's was granted. (It does; a permit is per site. Sanne, after Antwerp, caught it at once; Nadia, in her first week, might not have.) <b>Checking the plan</b>: three dates that disagreed between the roadmap and Ghent's plan. <b>Translation drafts</b> for the Flemish writer to correct. The trial ends with four rules in the playbook: approved tool only; every fact checked against its source; the <b>sender owns every line</b>; say when a text was drafted with AI. Decisions, judgment about people and conversations stay with people.</p>""",
    how_figs=[ai_how],
    steps=[("Use the organisation's approved tool", "With legal's rules on data."),
           ("Give it the sources, not the conclusion", "Notes, logs, the plan."),
           ("Use it to draft, summarise and check", "Not to decide."),
           ("Check every fact against its source", "Especially the ones that read well."),
           ("Own what you send", "Whoever drafted it."),
           ("Say when AI drafted it", "So readers know what was checked.")],
    vocab=[("AI assistant", "A tool that generates text, summaries or analysis from instructions and documents."),
           ("Hallucination", "A confident output that isn't true or isn't supported by the sources."),
           ("Approved tool", "An AI service the organisation has contracted and cleared for its data."),
           ("Human in the loop", "A person reviews and decides before output is used."),
           ("Confidential data", "Information that must not leave approved systems: personal data, contract terms."),
           ("Accountability", "The person who sends or decides answers for the result.")],
    code=dict(file="programme/07-ai-trial.md", note="Sanne, with Lena, trial 1 February → 10 March 2028", plain=True, src="""
# AI IN PROJECT WORK · six-week trial                       1 Feb - 10 Mar 2028

TOOL       Larder's approved assistant (company contract; data not used for training)
LENA'S     no personal data · no contract terms in any other tool · Belgian and Dutch
RULES      privacy rules apply to prompts as to any document
USE                              RESULT                                   KEEP?
Friday status draft              90 → 30 min; every line checked          yes
Meeting summaries (en, nl)       weekly; owner reads before sending       yes
Risk suggestions (Ghent)         23 suggested · 9 kept · 2 new · 1 WRONG  yes, with care
                                 ("no permit needed, Antwerp's granted")
Plan consistency check           3 date clashes roadmap vs Ghent plan     yes
Translation drafts               for the Flemish writer to correct        yes
MISTAKE    Fri 11 Feb: unchecked draft said "Ghent lease signed" (agreed in principle;
           signed 2 Mar) → corrected within the hour
RULES      approved tool only · every fact checked against its source · the sender owns
           every line · say when AI drafted it · decisions and people stay human
"""),
    tools="tools: an approved assistant, the sources, Lena's rules, and the habit of checking the lines that read best.",
    deep_dive=dict(
        side="where it helps, where it doesn't, confidentiality, and checking habits",
        intro="AI arrived in project work faster than any method in this book. The eighth edition of the guide treats it as a newer topic, not a process. This chapter is Sanne's practical view after six weeks: the jobs it does well, the jobs it shouldn't do, the confidentiality rules, and the checking habits that make the time it saves real.",
        parts=[
            ("Where it helps", """  <ul>
    <li><b>First drafts</b> from your own sources: the Friday status from notes and logs; minutes from a transcript; a charter from the playbook's template.</li>
    <li><b>Summaries</b> of long material: a 40-page permit decision, a supplier's contract (inside the approved tool).</li>
    <li><b>Consistency checks</b>: dates across the roadmap and project plans; totals across the budget and the money table.</li>
    <li><b>Prompts for thinking</b>: risks from past lessons, questions for a pre-mortem. Treat them as suggestions from a well-read stranger.</li>
    <li><b>Translation drafts</b> and small formulas or scripts, checked by someone who knows.</li>
  </ul>""", [ai_deep1]),
            ("Where it doesn't", """  <p>It doesn't know <b>what happened today</b> unless you tell it; it can't judge <b>people</b> (whether Nadia is ready to run Haarlem); it shouldn't make <b>decisions</b>, because someone must own them; it can't build <b>trust</b> with a neighbour, a regulator or a team. And it can be <b>confidently wrong</b>, in a way that's hardest to see exactly where you know least: the permit suggestion would have looked plausible to anyone who hadn't lived through Antwerp.</p>""", []),
            ("Confidentiality", """  <p>Prompts are documents. Anything pasted into a tool is sent to that tool's provider. Larder's rules, from Lena: use only the <b>approved</b> assistant; no <b>personal data</b> (names in an issue log are personal data); no <b>contract terms</b> outside it; the same Dutch and Belgian privacy rules apply as to any other system. When in doubt, describe the problem without the data.</p>""", []),
            ("Checking habits that make it work", """  <ul>
    <li><b>Give it the sources</b>, and ask it to say which source each line comes from.</li>
    <li><b>Check the lines that read best</b>: the smooth sentences are where a gap was filled.</li>
    <li><b>Check every number and date</b> against the source, every time.</li>
    <li><b>Own it</b>: if you send it, it's yours. The status is Sanne's, not the assistant's.</li>
    <li><b>Label it</b>: “drafted with AI, checked by Sanne” tells readers what happened.</li>
  </ul>
  <p>With those habits the 60 minutes saved on a status were real. Without them, they were borrowed from the next correction.</p>""", []),
        ]),
    dial=[("Light", "personal use", ["Approved tool, no personal data.", "Drafts and summaries.", "Check before sending."]),
          ("Standard", "a programme", ["A trial with measured results.", "Written rules with legal.", "Every fact checked; sender owns it; labelled."]),
          ("Heavy", "regulated or sensitive work", ["AI policy and approved use cases.", "Logs of AI-assisted outputs.", "Independent review of high-stakes uses."])],
    baseline="Each line compares <b>no AI, or AI drafts sent after a skim</b> to <b>an approved assistant used for drafts, summaries and checks, with every fact checked and owned</b>.",
    ratings=[(3, 4, "Time moves from typing to thinking."),
             (3, 4, "Plan clashes caught by a check."),
             (3, 4, "More risks suggested; one wrong caught."),
             (3, 4, "Status is faster, and labelled."),
             (3, 3, "Trust held after one correction, with rules."),
             (3, 3, "Neutral."),
             (3, 4, "Drafts in minutes when plans change."),
             (3, 3, "Only as good as the checking."),
             (3, 5, "Status: 90 minutes → 30.")],
    pitfalls=[("Skim and send", "Fluent and wrong goes out.", "check every fact against its source."),
              ("Unapproved tools", "Confidential data leaves.", "the approved assistant only."),
              ("AI as decider", "Nobody owns the decision.", "people decide."),
              ("Trusting it where you know least", "Errors look plausible there.", "check hardest where you're newest.")],
    use=["Drafts from your own sources.", "Summaries and translations.", "Consistency checks.", "Prompts for risk and pre-mortem thinking."],
    skip=["Judgments about people; anything confidential outside approved tools; decisions."],
    related=["<b>Where Are We, Really?</b> (vol. 2)", "<b>What Could Happen?</b> (vol. 5)", "<b>Which Tools, When?</b> (this volume)", "<b>Working with Legal &amp; Privacy</b> (Grace, vol. 5)"],
    quiz=[("Name three jobs AI did well in the trial.", "Status drafts, meeting summaries, plan consistency checks (also risk suggestions, translation drafts)."),
          ("What was the dangerous suggestion?", "That Ghent needed no permit because Antwerp's was granted; a permit is per site."),
          ("What are the four rules?", "Approved tool only; every fact checked against its source; the sender owns every line; say when AI drafted it."),
          ("Nadia wants to paste the issue log, with names, into a free AI tool at home. What do you say?", "No: names are personal data and the tool isn't approved; use Larder's assistant, or describe it without the data."),
          ("Joost asks if the AI can decide Haarlem's go / no-go from the checklist. Answer him.", "It can summarise the checklist; the decision and its ownership stay with the steering group.")],
    try_it="Give an approved AI assistant your notes for this week's status and ask it to cite the source of each line. Check every line. Count the ones you had to change, and time the whole thing.",
    remember="A fast new assistant: use it <span class=\"hl\">a lot</span>, read <span class=\"hl\">everything</span> before it leaves.",
    sources=["Project Management Institute, <i>PMBOK Guide</i>, Eighth Edition (2025): AI in project management (newer topics).",
             "Project Management Institute, <i>AI Essentials for Project Professionals</i> (2024).",
             "European Union, Artificial Intelligence Act (2024), and the GDPR (2016): obligations when AI handles personal data."],
)

# ------------------------------------------------------------------ 08 What Does It Leave Behind?
su_problem = Doodle(760, 260, "Doodle of Monday 6 March 2028. Korenwolf's supplier questionnaire arrives. Ana answers for the platform: about nine tonnes of carbon a year in the cloud. The other questions are about the stores: refrigerants, energy, waste, materials. Ghent's cooling plant is being specified that week, with a synthetic refrigerant that warms the climate about fourteen hundred times as much as carbon dioxide if it leaks.",
                    "Korenwolf asks about refrigerants, energy, waste. Ghent's cooling is being specified this week.", exact=True)
su_problem.box(20, 24, 330, 140, None, "paper")
su_problem.head(185, 60, "the questionnaire", size=19)
su_problem.text(185, 94, "Ana: cloud ≈ 9 t CO₂e a year", size=16)
su_problem.text(185, 122, "stores: no answer yet", size=16)
su_problem.box(410, 24, 330, 140, None, "pink")
su_problem.head(575, 60, "Ghent's cooling spec", size=19)
su_problem.text(575, 94, "synthetic refrigerant", size=16)
su_problem.text(575, 122, "≈ 1,400 × CO₂ if it leaks", size=16)
su_problem.note(380, 210, "the cheapest moment to change it is this week", "red", size=18)
su_problem.note(380, 242, "a launch leaves a store running for ten years", "pen", size=16)

su_analogy = Doodle(760, 250, "Doodle of a family building a house. The cheapest time to choose the heating, the insulation and the windows is on the drawing, not after they've moved in. The builder finishes in a year; they live with the choices for thirty.",
                    "Choose the heating on the drawing, not after you move in. The build takes a year; you live there for thirty.", exact=True)
su_analogy.row([("on the drawing", "cheap to change", "green"), ("during the build", "costly", "y"), ("after moving in", "very costly", "pink")], y=40, h=96, size=18, subsize=14)
su_analogy.note(380, 196, "decide what it leaves behind while you still can", "pen", size=18)

su_how = Doodle(760, 470, "Ghent's launch sustainability choices, 6 to 13 March 2028, with numbers. Cooling: a carbon-dioxide system, a natural refrigerant, instead of a synthetic one: seven thousand euros more, with heat recovery warming the store, about eighteen hundred euros a year less energy, paid back in about four years; approved by Femke. Shelving: reused from Zuid's refit, about five thousand euros saved. E-bike batteries: returned to the lease supplier for recycling, in the contract. Food: unsold food to a Ghent food bank from week one, as in every city since Rotterdam. People: neighbours met before the permit was lodged. The questionnaire answered on 13 March with platform and store numbers.",
                "Decided on the drawing: CO₂ cooling (+€7k, ≈ €1.8k a year back), reused shelving (−€5k), batteries back, food to a food bank.", exact=True)
sus = [("cooling", "CO₂ (natural) not synthetic", "+€7k · ≈ €1.8k/yr back · ≈ 4 yrs", "green"),
       ("shelving", "reused from Zuid's refit", "≈ €5k saved", "green"),
       ("e-bike batteries", "back to the lease supplier", "in the contract", "y"),
       ("food", "unsold → Ghent food bank", "from week 1", "y"),
       ("neighbours", "met before the permit", "Antwerp's lesson", "blue")]
for i, (a, b, c, f) in enumerate(sus):
    y = 14 + i * 64
    su_how.box(8, y, 744, 56, None, f, rx=6)
    su_how.head(22, y + 34, a, anchor="start", size=15)
    su_how.text(196, y + 34, b, anchor="start", size=14)
    su_how.text(740, y + 34, c, anchor="end", size=14)
su_how.box(8, 346, 744, 112, None, "paper")
su_how.head(380, 374, "Korenwolf's questionnaire, answered 13 March", size=16)
su_how.text(380, 404, "platform ≈ 9 t CO₂e a year (Ana) · stores: refrigerant, energy, waste", size=14)
su_how.text(380, 430, "playbook v4.2: a sustainability line on every launch's tailoring sheet", size=14)

SUSTAIN = dict(
    slug="sustainability-in-practice",
    kicker="a.k.a. integrating sustainability: what a project leaves behind",
    tldr="A project ends; what it builds runs for years. <b>Sustainability</b> in project work means weighing a choice's long effects (on the climate, on resources, on the people around it, on running costs) <b>while the choice is still cheap to change</b>: on the drawing, in the specification, in the contract. Put a line for it on the tailoring sheet, price the options over the life of the result, not just the build, and let the sponsor decide with both numbers.",
    chips=[("Family", "models, methods, artefacts"), ("Lives in", "a line on the tailoring sheet and in each specification"), ("Pairs with", "think past the finish (vol. 1), payback, sourcing")],
    pmbok=dict(covers="weighing environmental, social and economic effects across the life of what a project delivers, and building them into decisions",
               domains=MMA + ["finance"], processes=[], principles=["Integrate sustainability within all project areas"], focus=["planning"],
               older="6th: not covered as such. 7th: stewardship (a principle). 8th: “integrate sustainability” is one of the six principles."),
    problem_side="Larder, Monday 6 March 2028",
    problem="""  <p class="lead">Korenwolf's annual <b>supplier questionnaire</b> arrives. Ana answers for the platform: about <b>9 tonnes</b> of CO₂-equivalent a year in the cloud, 0.6 g an order. The other questions are about the <b>stores</b>: refrigerants, energy, waste, materials. That same week, Ghent's cooling plant is being specified with a <b>synthetic refrigerant</b> that, if it leaks, warms the climate about <b>1,400 times</b> as much as the same weight of CO₂. <span class="hl-pink">The cheapest moment to change that choice is this week; after the plant is ordered it's ten years.</span></p>
  <ul>
    <li>Launches were judged on the build, not on what they leave running.</li>
    <li>Nobody had priced options over the store's life.</li>
    <li>A customer asked a question the project had no answer to.</li>
  </ul>""",
    problem_figs=[su_problem],
    meanwhile=[("architect-5", "green-software", "Ana's green software: about 9 t CO₂e a year for the platform, 0.9 → 0.6 g an order, answered for Korenwolf's supplier questionnaire.",
                "Sanne answers the store half of the same questionnaire, and changes Ghent's cooling plant while it's still on paper.")],
    analogy_side="choosing on the drawing",
    analogy="""  <p>A family building a house can choose the <b>heating, insulation and windows</b> on the drawing for the price of an eraser. During the build each change costs money; after they've moved in, it costs a lot. The builder finishes in a year. The family lives with the choices for thirty.</p>""",
    analogy_figs=[su_analogy],
    map=[("On the drawing", "Ghent's cooling specification, March 2028"),
         ("The heating choice", "CO₂ (natural refrigerant) vs synthetic"),
         ("Living there thirty years", "A store running for ten years"),
         ("Heating bills", "≈ €1.8k a year less energy with heat recovery"),
         ("The builder's year", "The launch project: twelve weeks")],
    how_side="decide on the drawing; price over the life; the sponsor decides",
    how="""  <p>Between <b>6 and 13 March</b> Sanne and Nadia go through Ghent's choices while they're still on paper. <b>Cooling</b>: a <b>CO₂ system</b> (a natural refrigerant) instead of the synthetic one costs <b>€7k more</b>; with heat recovery warming the store it saves about <b>€1.8k a year</b> in energy, so it pays back in about four years and removes the leak risk. Femke approves it from the programme's money. <b>Shelving</b>: reused from Zuid's refit, about <b>€5k</b> saved (Antwerp's opportunity O-01, again). <b>E-bike batteries</b>: returned to the lease supplier for recycling, written into the contract. <b>Food</b>: unsold food to a Ghent food bank from week one, as in every city since Rotterdam. <b>Neighbours</b>: met before the permit is lodged, Antwerp's lesson. On <b>13 March</b> Korenwolf gets an answer with platform and store numbers. Playbook v4.2 adds one line to every tailoring sheet: <b>what does this launch leave running, and what does it cost over ten years?</b></p>""",
    how_figs=[su_how],
    steps=[("Find the choices that last", "Plant, materials, contracts."),
           ("Make them while still on paper", "The cheapest moment."),
           ("Price options over the life", "Build cost and running cost."),
           ("Include people as well as carbon", "Neighbours, jobs, food waste."),
           ("Let the sponsor decide with both numbers", "And record why."),
           ("Answer the questions customers ask", "From the project's records.")],
    vocab=[("Sustainability", "Meeting today's needs without harming the ability to meet tomorrow's: environment, society, money."),
           ("Life-cycle cost", "Build cost plus running, maintenance and disposal over the life of a result."),
           ("CO₂-equivalent (CO₂e)", "Greenhouse effect expressed as the weight of CO₂ that would do the same."),
           ("Global warming potential", "How much a gas warms the climate compared with CO₂."),
           ("Natural refrigerant", "A cooling gas such as CO₂ or ammonia with little or no warming effect."),
           ("Supplier questionnaire", "A customer's questions about a supplier's environmental and social practices.")],
    code=dict(file="programme/08-ghent-sustainability.md", note="Sanne and Nadia, 6–13 March 2028", plain=True, src="""
# GHENT · WHAT THIS LAUNCH LEAVES RUNNING                            6-13 Mar 2028

CHOICE            OPTION CHOSEN                  BUILD     RUNNING (10 YEARS)        DECIDED
Cooling           CO2 system, heat recovery      +€7k      ≈ -€1.8k/yr; no synthetic  Femke
                  (not synthetic, ≈ 1,400 x CO2)            refrigerant to leak
Shelving          reused from Zuid's refit       ≈ -€5k    -                          Nadia
E-bike batteries  back to the lease supplier     €0        recycled                   Joost
Unsold food       Ghent food bank, from week 1   €0        daily                      store mgr
Neighbours        met before the permit lodge    €0        (Antwerp's lesson)         Nadia

KORENWOLF QUESTIONNAIRE (answered 13 Mar)  platform ≈ 9 t CO2e/yr, 0.6 g an order (Ana) ·
  stores: refrigerants, energy per order, food waste, materials reused (Sanne)
PLAYBOOK v4.2  tailoring sheet line: "what does this launch leave running, and what does
               it cost over ten years?"
"""),
    tools="tools: the specification before it's ordered, a ten-year cost line, the sponsor, and the customer's questions.",
    dial=[("Light", "small work", ["Ask what it leaves behind.", "Pick the better option if it costs little.", "Note why."]),
          ("Standard", "a city launch", ["A line on the tailoring sheet.", "Options priced over ten years.", "The sponsor decides with both numbers."]),
          ("Heavy", "large construction", ["Life-cycle assessments.", "Certifications and reporting.", "Sustainability targets in contracts."])],
    baseline="Each line compares <b>launches judged on the build alone</b> to <b>lasting choices made on paper and priced over the store's life</b>.",
    ratings=[(3, 4, "The store costs less to run for ten years."),
             (3, 3, "Neutral."),
             (3, 4, "No synthetic refrigerant to leak."),
             (2, 4, "Customer questions answered from records."),
             (3, 4, "Korenwolf got real numbers."),
             (3, 3, "Neutral."),
             (3, 4, "Choices made while cheap to change."),
             (3, 4, "Better plant designed in."),
             (3, 3, "A line on a sheet, an hour of pricing.")],
    pitfalls=[("Too late", "Changes cost ten times more.", "decide on the drawing."),
              ("Build cost only", "Cheap now, dear for years.", "price over the life."),
              ("Carbon only", "People forgotten.", "include neighbours, waste, jobs."),
              ("Claims without numbers", "Customers stop believing.", "answer from records.")],
    use=["When specifying anything that lasts.", "When signing long contracts.", "When customers ask.", "On every tailoring sheet."],
    skip=["Never; on small work it's one question."],
    related=["<b>Think Past the Finish</b> (vol. 1)", "<b>Was It Worth It?</b> (vol. 4)", "<b>Green Software</b> (Ana, vol. 5)", "<b>Make It, Buy It, or Hire It?</b> (vol. 2)"],
    quiz=[("Why decide in March?", "The cooling plant was still on paper; after ordering, the choice lasts ten years."),
          ("What did the CO₂ system cost and save?", "+€7k; about €1.8k a year less energy; payback about four years."),
          ("What's the v4.2 tailoring line?", "What does this launch leave running, and what does it cost over ten years?"),
          ("A builder offers a cheaper floor that lasts five years instead of fifteen. What do you price?", "Both over fifteen years, including the replacement and disruption; let the sponsor decide with both numbers."),
          ("Is sustainability only about carbon?", "No: people (neighbours, jobs), resources, waste and running costs too.")],
    try_it="Find one choice in your project that will outlast it. Price two options over its life, not just to build. Who decides?",
    remember="Choose the heating on the <span class=\"hl\">drawing</span>. You live with it for <span class=\"hl\">thirty years</span>.",
    sources=["Project Management Institute, <i>PMBOK Guide</i>, Eighth Edition (2025): principle, integrate sustainability.",
             "Project Management Institute, <i>PMBOK Guide</i>, Seventh Edition (2021): stewardship.",
             "Gilbert Silvius and Ron Schipper, “Sustainability in project management competencies” (2014)."],
)

NOTES = [TOOLBOX, ARTEFACTS, AI, SUSTAIN]
