# Series 2 · Book 3 · The Project Manager's Notebook · Vol. 6 · Leading others (the PMO, servant leadership, ethics)
# Narrator: Sanne. Facts: docs/larder-casebook.md, "Book 3, Vol. 6"; numbers in the comment block of 01_fitting.py.
# Ghent: lease signed Thu 2 Mar 2028; pre-application meeting Tue 7 Feb; permit lodged Mon 13 Mar, granted Fri 12 May
#   (deliveries from 07:00 by design, CO₂ cooling; no objections). G1 fit-out planned Fri 2 Jun, forecast Thu 8 Jun on
#   22 May (amber); actual Wed 7 Jun. One red at readiness (Dutch help pages, Grace's team), fixed Sun 18 Jun.
#   Opened Mon 19 Jun 2028.
# Nadia: from a retail chain's store-opening team (predictive, like Sanne); starts Mon 7 Feb 2028; weekly 1:1 Tuesdays.
#   Sanne's mistake: Fri 25 Feb rewrote Nadia's first Ghent status at 22:00 and sent her own; Nadia's next two were thin.

LEAD = ["governance", "resources"]

# ------------------------------------------------------------------ 09 Who Helps the Project Managers Now?
pm_problem = Doodle(760, 260, "Doodle of February 2028. Vol. 1's launch desk was two hours a week of Sanne's time: templates, a lessons page, a quarterly sheet for Femke. Now there are two project managers, two Belgian and Dutch launches a year, a playbook, an eighteen-template kit and a programme. Nadia asks where things live and who keeps them up to date. The answer is still: ask Sanne.",
                    "The launch desk was two hours a week. Now: two PMs, a programme, a kit. The answer is still “ask Sanne”.", exact=True)
pm_problem.box(20, 24, 330, 140, None, "paper")
pm_problem.head(185, 60, "launch desk, Feb 2026", size=19)
pm_problem.text(185, 94, "2 hours a week", size=16)
pm_problem.text(185, 122, "templates, lessons, a sheet", size=16)
pm_problem.box(410, 24, 330, 140, None, "y")
pm_problem.head(575, 60, "Feb 2028", size=19)
pm_problem.text(575, 94, "2 PMs, a programme", size=16)
pm_problem.text(575, 122, "playbook + 18 templates", size=16)
pm_problem.note(380, 210, "a support function that is one person's memory", "red", size=18)
pm_problem.note(380, 242, "and Nadia's first question: “where does this live?”", "pen", size=16)

pm_analogy = Doodle(760, 250, "Doodle of a hospital's nursing station. It doesn't treat patients. It keeps the charts, the drug cupboard, the rota and the handover sheet in order, so every nurse can do the treating. If it starts telling doctors how to operate, it's a different thing, and usually a worse one.",
                    "A nursing station keeps charts, cupboard, rota and handover in order, so others can treat patients.", exact=True)
pm_analogy.row([("charts", "kept current", "blue"), ("cupboard", "stocked", "green"), ("rota", "who's where", "y"), ("handover", "every shift", "paper")], y=40, h=96, size=17, subsize=13)
pm_analogy.note(380, 196, "it supports the treating; it doesn't do it, or overrule it", "pen", size=17)

pm_how = Doodle(760, 470, "The launch office from 1 February 2028, a supportive project management office with one rule that's mandatory. It owns: the playbook and the eighteen-template kit; the people booking for the programme; Femke's quarterly portfolio sheet; the lessons page after every launch. It runs: a monthly peer review where Sanne and Nadia read each other's status and risk register. One rule is not optional: the five gates and go or no-go. It doesn't: write project plans, approve every document, or own any launch. Two measures: days from kick-off to an agreed plan, Rotterdam about thirty-five, Ghent fourteen; and how many kit templates were actually used, sixteen of eighteen on Ghent.",
                "Supportive by default, mandatory on one thing (gates). Measured by how fast PMs can plan, and what they use.", exact=True)
pm_how.box(14, 14, 360, 200, None, "green")
pm_how.head(194, 42, "owns", size=17)
for i, t in enumerate(["playbook + 18-template kit", "programme people booking", "Femke's portfolio sheet", "lessons after every launch"]):
    pm_how.text(194, 76 + i * 32, t, size=14)
pm_how.box(386, 14, 360, 200, None, "pink")
pm_how.head(566, 42, "doesn't", size=17)
for i, t in enumerate(["write project plans", "approve every document", "own any launch", "measure by forms filled"]):
    pm_how.text(566, 76 + i * 32, t, size=14)
pm_how.box(14, 228, 360, 100, "monthly peer review", "blue", sub="Sanne ↔ Nadia: status + risks", size=16, subsize=13)
pm_how.box(386, 228, 360, 100, "one mandatory rule", "y", sub="five gates and go / no-go", size=16, subsize=13)
pm_how.box(14, 344, 360, 112, None, "paper")
pm_how.head(194, 372, "kick-off → agreed plan", size=15)
pm_how.text(194, 404, "Rotterdam ≈ 35 days", size=14)
pm_how.text(194, 430, "Ghent 14 days", size=14)
pm_how.box(386, 344, 360, 112, None, "paper")
pm_how.head(566, 372, "kit templates used", size=15)
pm_how.text(566, 404, "Ghent: 16 of 18", size=14)
pm_how.text(566, 430, "the 2 unused: reviewed", size=14)

PMO_GROWN = dict(
    slug="pmo-grown-up",
    kicker="a.k.a. the PMO, grown up: a launch office that serves project managers",
    tldr="A <b>project management office</b> (PMO) is whatever helps projects run well across an organisation. It can be <b>supportive</b> (templates, lessons, coaching), <b>controlling</b> (required methods, reviews) or <b>directive</b> (it runs the projects). Grow it only as far as the work needs: start supportive, make mandatory only the few things that protect the organisation, and judge it by what it makes easier (days to an agreed plan, templates actually used), not by forms filled. If its knowledge lives in one person, it isn't an office yet.",
    chips=[("Family", "leading others"), ("Lives in", "the playbook, the kit, a booking sheet and a monthly review"), ("Pairs with", "the PMO (vol. 1), the playbook, programmes")],
    pmbok=dict(covers="the project management office: its kinds, what it owns, how far it should control, and how to measure it",
               domains=LEAD, processes=[], principles=["Build an empowered culture"], focus=["planning", "monitoring and controlling"],
               older="6th: section 2.4.4.3, PMO types (supportive, controlling, directive). 7th: the PMO in the system for value delivery."),
    problem_side="Larder, February 2028",
    problem="""  <p class="lead">Vol. 1's <b>launch desk</b> was two hours a week of Sanne's time: templates, a lessons page, a quarterly sheet of projects for Femke, agreed “until Utrecht”. Two years later there are <b>two project managers</b>, a programme, playbook v4, an <b>18-template kit</b>, a booking sheet for shared people and Femke's portfolio review. Nadia's first questions are all the same shape: where does this live, and who keeps it current? <span class="hl-pink">Every answer is “ask Sanne”.</span> A support function that is one person's memory stops the day that person is on holiday.</p>
  <ul>
    <li>The desk grew without anyone deciding what it was.</li>
    <li>Nothing said what was optional and what wasn't.</li>
    <li>Nobody measured whether it helped.</li>
  </ul>""",
    problem_figs=[pm_problem],
    analogy_side="the nursing station",
    analogy="""  <p>A hospital's <b>nursing station</b> doesn't treat patients. It keeps the <b>charts</b> current, the <b>drug cupboard</b> stocked, the <b>rota</b> clear and the <b>handover</b> sheet done every shift, so every nurse can get on with treating. A few rules there are absolute (how drugs are signed out). If the station starts telling surgeons how to operate, it has become something else, and usually something worse.</p>""",
    analogy_figs=[pm_analogy],
    map=[("The charts", "The playbook and the 18-template kit"),
         ("The rota", "The programme's booking of shared people"),
         ("The handover sheet", "The lessons page after every launch"),
         ("Signing out drugs", "The five gates and go / no-go: mandatory"),
         ("Telling surgeons how to operate", "Writing PMs' plans for them: not its job")],
    how_side="what it owns, what it doesn't, one rule, two measures",
    how="""  <p>From <b>Tuesday 1 February 2028</b> the desk becomes the <b>launch office</b>, written down on one page. It <b>owns</b> the playbook and kit (versioned, with change requests from any PM), the programme's people booking, Femke's quarterly portfolio sheet and the lessons page after every launch. It runs a <b>monthly peer review</b>: Sanne and Nadia read each other's status and risk register and ask the three review questions from Vol. 5. It is <b>supportive</b> by default, with <b>one mandatory rule</b>: the five gates and go / no-go, because Antwerp and Rotterdam both showed what they catch. It <b>doesn't</b> write project plans, approve every document, or own any launch. And it's measured by what it makes easier: <b>days from kick-off to an agreed plan</b> (Rotterdam about 35; Ghent <b>14</b>) and <b>templates actually used</b> (Ghent: 16 of 18; the two unused go to the next review). Nadia keeps the kit from April. The office's knowledge now lives in two people and a document.</p>""",
    how_figs=[pm_how],
    steps=[("Write down what the office owns", "And what it doesn't."),
           ("Start supportive", "Templates, lessons, coaching, booking."),
           ("Make only a few things mandatory", "The ones that protect the organisation."),
           ("Run a peer review", "Project managers reading each other's work."),
           ("Measure what it makes easier", "Days to a plan; templates used."),
           ("Spread its knowledge", "Two people at least, and the document.")],
    vocab=[("PMO", "Project management office: a function that supports or governs projects across an organisation."),
           ("Supportive PMO", "Provides templates, lessons and coaching; low control."),
           ("Controlling PMO", "Requires methods and reviews; medium control."),
           ("Directive PMO", "Manages the projects directly; high control."),
           ("Peer review", "Colleagues reviewing each other's work to improve it."),
           ("Bus factor", "How many people could leave before knowledge is lost; here, one.")],
    code=dict(file="programme/09-launch-office.md", note="Sanne, Tuesday 1 February 2028", plain=True, src="""
# LAUNCH OFFICE · what it is                                   from 1 Feb 2028 · Sanne, Nadia

KIND        supportive, with one mandatory rule
OWNS        playbook v4 + 18-template kit (versioned; any PM can request a change) ·
            programme people booking · Femke's quarterly portfolio sheet ·
            lessons page after every launch
RUNS        monthly peer review: Sanne and Nadia read each other's status and risks
            (done? due? nearest trigger?)
MANDATORY   the five gates and go / no-go, in every launch
DOESN'T     write project plans · approve every document · own any launch
MEASURES    days from kick-off to agreed plan: Rotterdam ≈ 35 · Ghent 14
            kit templates used: Ghent 16 of 18 (2 unused → next review)
BUS FACTOR  1 → 2: Nadia keeps the kit from April
"""),
    tools="tools: one page describing the office, the playbook and kit, a booking sheet, a monthly review, and two measures.",
    dial=[("Light", "one or two projects", ["A shared folder of templates.", "Lessons after each project.", "No office."]),
          ("Standard", "a launch programme", ["A supportive office with one mandatory rule.", "Peer reviews.", "Measured by days to a plan and templates used."]),
          ("Heavy", "large organisations", ["Controlling or enterprise PMO.", "Portfolio governance, standards, audits.", "Training and career paths for PMs."])],
    baseline="Each line compares <b>a launch desk that is one person's memory</b> to <b>a written, supportive office with one mandatory rule and two measures</b>.",
    ratings=[(3, 4, "Help aimed at what makes launches easier."),
             (3, 4, "Plans agreed in two weeks, not five."),
             (3, 4, "Gates are kept in every launch."),
             (2, 4, "Where things live is written down."),
             (3, 4, "Femke's portfolio sheet is kept up."),
             (3, 5, "PMs own their launches and the kit."),
             (3, 4, "Changes to the kit come from any PM."),
             (3, 4, "Peer review catches gaps."),
             (3, 4, "One page; a monthly hour.")],
    pitfalls=[("Office as police", "PMs work around it.", "supportive by default."),
              ("Everything mandatory", "Ceremony replaces judgment.", "a few rules that protect."),
              ("Measured by forms", "Paperwork grows.", "measure what it makes easier."),
              ("One person's memory", "Stops on their holiday.", "two people and a document.")],
    use=["When several projects or PMs share methods.", "When knowledge sits with one person.", "When a new PM joins.", "When the portfolio needs one view."],
    skip=["A single project with one PM."],
    related=["<b>Who Helps the Project Managers?</b> (vol. 1)", "<b>Can a Launch Be a Recipe?</b> (this volume)", "<b>One Project, or Many?</b> (this volume)", "<b>Guardrails Not Gates</b> (Ana, vol. 6)"],
    quiz=[("Name the three kinds of PMO.", "Supportive, controlling, directive."),
          ("What's the launch office's one mandatory rule?", "The five gates and go / no-go."),
          ("How is it measured?", "Days from kick-off to an agreed plan; kit templates actually used."),
          ("Femke asks the launch office to approve every purchase order. What do you say?", "That's control the projects and Marco's money rules already have; the office stays supportive, with only the gates mandatory."),
          ("Why did Nadia take over the kit in April?", "So the office's knowledge lives in two people and a document, not one memory.")],
    try_it="Write what your PMO (or the person who helps PMs) owns, doesn't do, and makes mandatory, on one page. Add one measure of what it makes easier.",
    remember="The station keeps the <span class=\"hl\">charts</span>; the nurses do the <span class=\"hl\">treating</span>.",
    sources=["Project Management Institute, <i>PMBOK Guide</i>, Eighth Edition (2025): the PMO.",
             "Project Management Institute, <i>PMBOK Guide</i>, Sixth Edition (2017): 2.4.4.3 Project management office.",
             "Brian Hobbs and Monique Aubry, <i>The Project Management Office (PMO): A Quest for Understanding</i> (2010)."],
)

# ------------------------------------------------------------------ 10 Who Serves Whom?
sl_problem = Doodle(760, 260, "Doodle of Friday 25 February 2028 and Sanne's mistake for this collection. Nadia's first Ghent status arrives at six in the evening. It is honest but long and puts the wrong thing first. At ten that night Sanne rewrites it and sends her own version to Femke. Nadia's next two statuses are thin: Sanne will fix it anyway.",
                    "Sanne rewrites Nadia's first status at 22:00 and sends her own. Nadia's next two are thin.", exact=True)
sl_problem.row([("Nadia's status", "18:00, honest, long", "y"), ("Sanne rewrites", "22:00, sends hers", "pink"), ("next two", "thin: “she'll fix it”", "pink")], y=24, h=96, gap=34, size=17, subsize=13, arrows=True)
sl_problem.note(380, 170, "helping by doing the work takes the work away", "red", size=18)
sl_problem.note(380, 206, "Nadia learned that her version doesn't count", "pen", size=17)

sl_analogy = Doodle(760, 250, "Doodle of a parent teaching a teenager to cook. The parent who grabs the pan when the onions start to catch gets a better dinner tonight, and a teenager who never cooks. The parent who asks what's happening to the onions, and turns the heat down only if asked, gets a worse dinner tonight, and a cook by summer.",
                    "Grab the pan: a better dinner tonight. Ask about the onions: a cook by summer.", exact=True)
sl_analogy.box(14, 40, 350, 110, "grab the pan", "pink", sub="better tonight, no cook", size=18, subsize=14)
sl_analogy.box(396, 40, 350, 110, "ask, then step back", "green", sub="a cook by summer", size=18, subsize=14)
sl_analogy.note(380, 200, "serve the person's growth, not tonight's dinner", "pen", size=18)

sl_how = Doodle(760, 470, "How Sanne leads Nadia from March 2028. Situational leadership: Nadia is experienced at store openings and new to Larder and Belgium, so Sanne coaches on Larder things and delegates construction things. Weekly one-to-one, Tuesdays, thirty minutes, Nadia's agenda. Questions instead of rewrites: what's the one thing Femke must know? why amber? what will you do by Friday? Remove blocks: an introduction to Maarten, Lena's time booked, Hilde for the permit. Credit in public: Nadia named for the permit granted on 12 May. Result: Ghent opened on 19 June, Nadia's launch; Sanne wrote no status for it after 25 February.",
                "Coach on what's new to her, delegate what she knows; ask, unblock, credit. Ghent opened on 19 June: Nadia's launch.", exact=True)
sl_how.box(14, 14, 732, 110, None, "blue")
sl_how.head(380, 42, "situational: coach what's new, delegate what she knows", size=16)
sl_how.text(380, 74, "new: Larder's ways, Belgium, the steering group → coach", size=14)
sl_how.text(380, 100, "known: builders, fit-outs, store openings → delegate", size=14)
sl_how.row([("1:1 Tuesdays", "30 min, her agenda", "y"), ("questions", "not rewrites", "green"), ("unblock", "Maarten, Lena, Hilde", "paper"), ("credit", "permit, 12 May", "pink")], y=140, h=96, size=16, subsize=12)
sl_how.box(14, 256, 732, 120, None, "paper")
sl_how.head(380, 284, "the three status questions", size=16)
sl_how.text(380, 316, "what's the one thing Femke must know? · why that colour?", size=14)
sl_how.text(380, 342, "what will you do by Friday, and what do you need from me?", size=14)
sl_how.box(14, 392, 732, 64, "Ghent opened Mon 19 June: Nadia's launch", "green", sub="Sanne wrote none of its statuses after 25 February", size=17, subsize=13)

SERVANT = dict(
    slug="servant-leadership",
    kicker="a.k.a. servant leadership in practice: coaching another project manager",
    tldr="<b>Servant leadership</b> means leading by serving the people doing the work: removing what blocks them, growing their ability, and giving them the credit. With a less experienced colleague, the hardest part is <b>not doing their work for them</b>. Match how much you lead to what they already know (<b>situational leadership</b>: direct, coach, support, delegate), ask <b>questions</b> instead of rewriting, <b>unblock</b> what they can't, and <b>step back</b> where they're able. Rescuing gets a better result today and a weaker colleague tomorrow.",
    chips=[("Family", "leading others"), ("Lives in", "a weekly 1:1, three questions, and a list of blocks to remove"), ("Pairs with", "leading without authority, the toolbox, hiring")],
    pmbok=dict(covers="servant leadership and coaching: developing another person's capability, matching leadership style to their readiness, removing obstacles",
               domains=["resources"], processes=["Lead the Team"], principles=["Build an empowered culture", "Be an accountable leader"], focus=["executing"],
               older="6th: interpersonal skills, leadership (3.4.4 and 9.4). 7th: the Team domain, servant leadership. 8th: Resources domain, leading the team."),
    problem_side="Larder, Friday 25 February 2028",
    problem="""  <p class="lead">This is <b>Sanne's mistake</b> for this collection. Nadia's first Ghent status reaches her at 18:00. It's honest and complete, but long, and it puts the wrong thing first: the builder's schedule before the lease that isn't signed yet. At 22:00 Sanne rewrites it and sends <b>her own version</b> to Femke, with a kind note to Nadia. <span class="hl-pink">Nadia's next two statuses are thin. Why write it well, if Sanne will fix it anyway?</span> The rewrite got Femke a better page that night, and took the page away from Nadia.</p>
  <ul>
    <li>Helping by doing the work took the work away.</li>
    <li>Nadia learned her version didn't count.</li>
    <li>Sanne was coaching by habit, not by what Nadia needed.</li>
  </ul>""",
    problem_figs=[sl_problem],
    meanwhile=[("architect-6", "growing-architects", "Ana grows Cho and Dee into architects from May 2028: pairing first, then leading ADRs with Ana as reviewer, then alone.",
                "Sanne does the same with Nadia, a little earlier and with one stumble: she rewrote a status before she learned to ask about it instead.")],
    analogy_side="teaching a teenager to cook",
    analogy="""  <p>A parent teaching a teenager to cook watches the onions start to catch. <b>Grabbing the pan</b> saves tonight's dinner and produces a teenager who never cooks. <b>Asking</b> “what's happening to the onions?”, and turning the heat down only if asked, gets a slightly worse dinner tonight and a cook by the summer. The second parent isn't less helpful. They're helping the cook, not the dinner.</p>""",
    analogy_figs=[sl_analogy],
    map=[("Grabbing the pan", "Rewriting Nadia's status at 22:00"),
         ("Tonight's dinner", "A better page for Femke on 25 February"),
         ("“What's happening to the onions?”", "“What's the one thing Femke must know?”"),
         ("Turning the heat down if asked", "Unblocking: Maarten, Lena, Hilde"),
         ("A cook by summer", "Ghent opened on 19 June, Nadia's launch")],
    how_side="match the style, ask, unblock, credit, step back",
    how="""  <p>Sanne apologises on the Monday and changes how she leads. <b>Situational leadership</b>: Nadia ran store openings for a retail chain for six years, so on builders and fit-outs Sanne <b>delegates</b>; on Larder's ways, Belgium and the steering group she <b>coaches</b>. A <b>weekly 1:1</b>, Tuesdays, thirty minutes, on Nadia's agenda. For statuses, <b>three questions</b> instead of a red pen: what's the one thing Femke must know? why that colour? what will you do by Friday, and what do you need from me? <b>Unblocking</b> what Nadia can't do herself yet: an introduction to Maarten, Lena's time booked for the Belgian contracts, Hilde for the permit. <b>Credit</b> in public: when Ghent's permit is granted on <b>12 May</b> (no objections; deliveries from 07:00 by design), Sanne names Nadia in the steering note. Ghent opens on <b>Monday 19 June</b>. Sanne wrote none of its statuses after 25 February.</p>""",
    how_figs=[sl_how],
    steps=[("Ask what they already know", "And lead accordingly."),
           ("Delegate what they can do", "Coach what's new."),
           ("Ask questions instead of rewriting", "Three good ones."),
           ("Remove the blocks they can't", "Introductions, access, time."),
           ("Give credit in public", "By name."),
           ("Notice when you rescue", "And give the work back.")],
    vocab=[("Servant leadership", "Leading by serving the team's needs: removing obstacles, growing people."),
           ("Situational leadership", "Changing style with a person's readiness: directing, coaching, supporting, delegating."),
           ("Coaching", "Helping someone find their own answer, mostly through questions."),
           ("Rescuing", "Doing someone's work for them when they could learn to do it."),
           ("1:1", "A regular private meeting between a leader and one person."),
           ("Delegation", "Handing over a piece of work together with the authority to decide it.")],
    code=dict(file="programme/10-nadia-coaching.md", note="Sanne, from Monday 28 February 2028", plain=True, src="""
# LEADING NADIA · how I'll help (and how I won't)                  from 28 Feb 2028

MISTAKE   Fri 25 Feb: rewrote her first Ghent status at 22:00, sent mine → her next two thin
STYLE     delegate: builders, fit-out, store opening (6 years at a retail chain)
          coach: Larder's ways, Belgian rules, steering group, Femke
1:1       Tuesdays 09:00, 30 min, her agenda
STATUS    I don't rewrite. I ask: (1) the one thing Femke must know? (2) why that colour?
          (3) what will you do by Friday, what do you need from me?
UNBLOCK   Maarten (intro 1 Mar) · Lena's time for contracts (booked) · Hilde for the
          permit (from 7 Mar)
CREDIT    12 May: Ghent permit granted, no objections → Nadia named in the steering note
RESULT    Ghent opened Mon 19 Jun 2028 · statuses by Nadia from 3 Mar onwards
"""),
    tools="tools: a weekly 1:1, three questions, a list of blocks to remove, and the discipline not to grab the pan.",
    dial=[("Light", "a colleague asks for help once", ["Ask what they think first.", "Help on the block.", "Hand it back."]),
          ("Standard", "a new project manager", ["Situational style per area.", "Weekly 1:1, three questions, unblocking.", "Credit in public; no rewrites."]),
          ("Heavy", "a development programme", ["Formal mentoring and coaching.", "Development plans and stretch assignments.", "Feedback from several people."])],
    baseline="Each line compares <b>rewriting her status</b> to <b>situational coaching, questions, unblocking and public credit</b>.",
    ratings=[(3, 4, "Ghent was run by someone who'll run more."),
             (3, 4, "Nadia's statuses became reliable."),
             (3, 3, "Neutral."),
             (3, 4, "Status written by the person who knows."),
             (3, 4, "Femke trusts Nadia's statuses."),
             (2, 5, "Nadia owns Ghent."),
             (3, 4, "Style changes area by area."),
             (3, 3, "Neutral."),
             (3, 3, "Thirty minutes a week.")],
    pitfalls=[("Rescuing", "Better today, weaker tomorrow.", "ask, then give it back."),
              ("One style for everything", "Micromanaging experts, abandoning beginners.", "match the style to the area."),
              ("Credit kept", "People stop trying.", "name them in public."),
              ("Blocks left in place", "Coaching without help.", "remove what they can't.")],
    use=["When someone new takes on work you know.", "When you catch yourself redoing others' work.", "When handing over.", "Every week, in a 1:1."],
    skip=["A real emergency: act, then debrief and hand back."],
    related=["<b>How Do I Lead People Who Don't Report to Me?</b> (vol. 4)", "<b>Which Tools, When?</b> (this volume)", "<b>Growing Other Architects</b> (Ana, vol. 6)", "<b>Who Do We Hire?</b> (this volume)"],
    quiz=[("What was Sanne's mistake?", "Rewriting Nadia's status and sending her own; Nadia's next two were thin."),
          ("Where did Sanne delegate and where did she coach?", "Delegate: builders and fit-out; coach: Larder's ways, Belgium, the steering group."),
          ("Name the three status questions.", "The one thing Femke must know; why that colour; what by Friday and what do you need."),
          ("Nadia's risk register misses a Belgian risk you know well. What do you do?", "Ask a question that leads her to it (“what did Antwerp's register get wrong?”), not add it yourself."),
          ("When is it right to take over?", "In a real emergency: act, then debrief and give the work back.")],
    try_it="Think of the last time you redid someone's work. Next time, write three questions instead and ask them. Note what they produce.",
    remember="Don't grab the <span class=\"hl\">pan</span>. Ask about the <span class=\"hl\">onions</span>.",
    sources=["Project Management Institute, <i>PMBOK Guide</i>, Eighth Edition (2025): Resources domain, leading the team.",
             "Robert K. Greenleaf, <i>The Servant as Leader</i> (1970).",
             "Paul Hersey and Kenneth Blanchard, situational leadership (1969 onwards).",
             "John Whitmore, <i>Coaching for Performance</i> (1992)."],
)

# ------------------------------------------------------------------ 11 What Would You Do?
et_problem = Doodle(760, 260, "Doodle of Monday 22 May 2028. Ghent's fit-out gate, due Friday 2 June, is forecast for Thursday 8 June: the builder is six days behind. The opening on 19 June still holds, with less room to stock. Femke has an investor update on Thursday 25 May and asks Sanne to show Ghent green: it'll be fine by June, and investors only read colours.",
                    "Ghent is amber: the fit-out six days behind. Femke: “Show it green for Thursday. It'll be fine by June.”", exact=True)
et_problem.box(20, 24, 330, 140, None, "y")
et_problem.head(185, 60, "Ghent, 22 May", size=19)
et_problem.text(185, 94, "G1: 2 Jun → 8 Jun", size=16)
et_problem.text(185, 122, "opening 19 Jun holds", size=16)
et_problem.box(410, 24, 330, 140, None, "pink")
et_problem.head(575, 60, "Femke asks", size=19)
et_problem.text(575, 94, "“show it green”", size=16)
et_problem.text(575, 122, "investors, Thu 25 May", size=16)
et_problem.note(380, 210, "a small lie, for a good reason, to a powerful audience", "red", size=18)
et_problem.note(380, 242, "and Nadia is watching what Sanne does", "pen", size=16)

et_analogy = Doodle(760, 250, "Doodle of a car mechanic asked by a friend selling his car to write 'no faults' on the inspection sheet, because the small leak 'is nothing'. The mechanic writes 'small oil leak, cheap to fix', and offers to fix it before the sale. The friend is annoyed for a day. The buyer trusts the sheet, and the mechanic.",
                    "Asked to write “no faults”, the mechanic writes “small leak, cheap to fix”, and offers to fix it.", exact=True)
et_analogy.box(14, 40, 350, 110, "“no faults”", "pink", sub="what the friend wants", size=18, subsize=14)
et_analogy.box(396, 40, 350, 110, "“small leak, cheap fix”", "green", sub="true, and helpful", size=18, subsize=14)
et_analogy.note(380, 200, "the sheet is only worth something if it's always true", "pen", size=18)

et_how = Doodle(760, 470, "Sanne's answer, Monday 22 May 2028, as three options and the one she offers. Green: untrue; breaks the colour rules; if June goes wrong, every later status is doubted. Red: untrue the other way; the opening holds. Amber with the facts and the recovery: the fit-out six days late, the opening on 19 June holds, stocking compressed from twelve to eight days with a second shift, decision point Friday 2 June. Four values behind it: responsibility, respect, fairness, honesty. Femke presents amber on 25 May; the investors ask one question; the fit-out gate passes on Wednesday 7 June; Ghent opens on 19 June.",
                "Not green, not red: amber, with the facts, the recovery and the decision date. Femke presented it; Ghent opened on time.", exact=True)
et_how.row([("green", "untrue · breaks the rules", "pink"), ("red", "untrue the other way", "pink"), ("amber + facts", "true · with a recovery", "green")], y=14, h=96, size=17, subsize=13)
et_how.box(14, 126, 732, 150, None, "y")
et_how.head(380, 154, "what Sanne gives Femke for Thursday", size=16)
et_how.text(380, 186, "Ghent amber: fit-out 6 days late (G1 2 Jun → 8 Jun)", size=14)
et_how.text(380, 212, "opening 19 June holds: stocking 12 → 8 days, a second shift", size=14)
et_how.text(380, 238, "decision point Fri 2 June; next update to you that day", size=14)
et_how.text(380, 262, "one sentence for investors, written with you", size=13)
et_how.row([("responsibility", "", "blue"), ("respect", "", "blue"), ("fairness", "", "blue"), ("honesty", "", "blue")], y=292, h=56, size=15)
et_how.box(14, 368, 732, 88, "25 May: amber, one question · 7 Jun: G1 passed · 19 Jun: open", "green", size=15)

ETHICS = dict(
    slug="ethics",
    kicker="a.k.a. ethics and professional conduct: telling the truth under pressure",
    tldr="A project manager's reports are only useful if they're <b>always</b> true, so pressure to shade them is an ethical question, not a presentational one. PMI's code names four values: <b>responsibility</b>, <b>respect</b>, <b>fairness</b> and <b>honesty</b>. In practice: don't report what you know is false, in either direction; follow your own written rules (the colour rules exist for this moment); offer the person under pressure a <b>true version that helps them</b>: the facts, the recovery and a decision date. Say no to the request and yes to the person.",
    chips=[("Family", "leading others"), ("Lives in", "the colour rules, and what you do when they're inconvenient"), ("Pairs with", "status reports, delivering bad news, escalation")],
    pmbok=dict(covers="professional and ethical conduct: honesty in reporting, responsibility, respect and fairness, and handling pressure to misreport",
               domains=["governance"], processes=[], principles=["Be an accountable leader"], focus=["monitoring and controlling"],
               older="6th and 7th: the PMI Code of Ethics and Professional Conduct (responsibility, respect, fairness, honesty), referenced by both."),
    problem_side="Larder, Monday 22 May 2028",
    problem="""  <p class="lead">Ghent's fit-out gate, due <b>Friday 2 June</b>, is forecast for <b>Thursday 8 June</b>: the builder is six days behind after a late steel delivery. The opening on <b>19 June</b> still holds, with less time to stock. By the colour rules written in Rotterdam, that's <b>amber</b>. Femke has an investor update on <b>Thursday 25 May</b>. <span class="hl-pink">“Show Ghent green. It'll be fine by June, and investors only read colours.”</span> She isn't asking for anything dramatic: one colour, for one week, for a good reason. Nadia, who runs Ghent, is in the room.</p>
  <ul>
    <li>A small untruth, to a powerful audience, for a likely-true outcome.</li>
    <li>The colour rules were written for exactly this.</li>
    <li>A new colleague is learning what's normal here.</li>
  </ul>""",
    problem_figs=[et_problem],
    meanwhile=[("product-5", "bad-news", "Grace's delivering bad news: early, with facts, options and a recommendation, to the person who needs it.",
                "Sanne gives Femke the same: amber with the facts, the recovery and a decision date, written so she can present it.")],
    analogy_side="the inspection sheet",
    analogy="""  <p>A friend selling his car asks his mechanic to write <b>“no faults”</b> on the inspection sheet: the small oil leak “is nothing”. The mechanic writes <b>“small oil leak, cheap to fix”</b> and offers to fix it before the sale. The friend is annoyed for a day. The buyer trusts the sheet, and every sheet that mechanic signs afterwards is worth something.</p>""",
    analogy_figs=[et_analogy],
    map=[("“No faults”", "Ghent green"),
         ("The small leak", "The fit-out six days late"),
         ("“Cheap to fix”", "The opening holds: stocking compressed, a second shift"),
         ("Offering to fix it", "A true sentence for investors, written with Femke"),
         ("Every later sheet", "Every later status the board reads")],
    how_side="no to the request, yes to the person: a true version that helps",
    how="""  <p>Sanne says no, and in the same breath offers something. <b>Green</b> would be untrue and would break the colour rules; if June went wrong, every later status would be doubted, including Nadia's. <b>Red</b> would be untrue the other way: the opening holds. She offers <b>amber with the facts and the recovery</b>: the fit-out six days late; the opening on 19 June holds; stocking compressed from twelve days to eight with a second shift; a decision point on <b>Friday 2 June</b>, when Femke gets the next update. And one sentence for the investors, written with her: “Ghent is on track to open on 19 June; the fit-out is six days behind and we've planned the recovery.” Behind it are PMI's four values: <b>responsibility</b> (own the report), <b>respect</b> (for Femke's pressure, and her audience), <b>fairness</b> (investors decide on true information), <b>honesty</b>. Femke presents amber on 25 May. The investors ask one question. The gate passes on <b>Wednesday 7 June</b>; Ghent opens on <b>19 June</b>. Later Nadia asks Sanne what she'd have done if Femke had insisted. “Told her I couldn't send it, and that she could. Then written down that I'd said so.”</p>""",
    how_figs=[et_how],
    steps=[("Recognise the question as ethical", "Not presentational."),
           ("Check your own written rules", "They exist for this moment."),
           ("Say no to the untruth, both ways", "Not green, not red."),
           ("Offer a true version that helps", "Facts, recovery, decision date."),
           ("Write it with them", "One sentence they can present."),
           ("If overruled, don't send it yourself", "And record that you said so.")],
    vocab=[("Code of ethics", "A profession's statement of the conduct it expects; PMI's has four values."),
           ("Responsibility", "Owning your decisions and their consequences, including reports."),
           ("Respect", "Treating others, their views and their pressures with consideration."),
           ("Fairness", "Deciding impartially; letting others decide on true information."),
           ("Honesty", "Understanding the truth and acting truthfully, in what you say and imply."),
           ("Watermelon status", "Green outside, red inside: reports that hide trouble.")],
    code=dict(file="programme/11-ghent-status-25-may.md", note="Sanne and Nadia for Femke, Monday 22 May 2028", plain=True, src="""
# GHENT · STATUS FOR THE INVESTOR UPDATE                   for Femke, Thu 25 May 2028

COLOUR    AMBER (rules: a gate late but the opening holds → amber; opening > 3 days late → red)
FACTS     G1 fit-out: planned Fri 2 Jun → forecast Thu 8 Jun (steel delivered 6 days late)
          opening Mon 19 Jun: HOLDS
RECOVERY  stocking compressed 12 → 8 days · second picker shift 9-16 Jun (+€2.1k, from
          contingency) · builder on Saturday 3 Jun at their cost (late penalty clause)
DECIDE    Fri 2 Jun: if G1 forecast later than 9 Jun → steering group, options ready
FOR INVESTORS (agreed with Femke)  "Ghent is on track to open on 19 June; the fit-out is
          six days behind and we've planned the recovery."
NOT SENT  green (untrue; breaks the colour rules) · red (untrue; opening holds)
AFTER     25 May amber presented, one question · Wed 7 Jun G1 passed · Mon 19 Jun open
"""),
    tools="tools: the colour rules, the facts, a recovery, a decision date, and one sentence written together.",
    dial=[("Light", "a small internal report", ["Report it true.", "Say what you're doing about it.", "Done."]),
          ("Standard", "a programme with a board", ["Written colour rules followed.", "A true version that helps the person under pressure.", "Record if overruled."]),
          ("Heavy", "regulated or public reporting", ["Independent assurance of reports.", "Whistle-blowing routes.", "Ethics training and audits."])],
    baseline="Each line compares <b>a green for one week, to please</b> to <b>amber with the facts, the recovery and a decision date, written with the sponsor</b>.",
    ratings=[(3, 4, "Decisions rest on true information."),
             (3, 4, "Forecasts stay believable."),
             (3, 4, "The recovery was planned in time."),
             (1, 5, "The board sees the real colour."),
             (2, 5, "Investors and Femke can trust the next status."),
             (3, 4, "Nadia saw what's normal here."),
             (3, 3, "Neutral."),
             (3, 3, "Neutral."),
             (3, 3, "One awkward conversation.")],
    pitfalls=[("Shading “just this once”", "Every later report is doubted.", "always true, both ways."),
              ("Saying no and nothing else", "The person is left with their pressure.", "offer a true version that helps."),
              ("Moralising", "Pressure becomes a fight.", "respect their position; give facts."),
              ("Silent compliance", "You own the untruth.", "don't send it; record that you said so.")],
    use=["Whenever a report is asked to say less than the truth.", "Before audiences with power.", "When a colleague watches what's normal.", "When rules feel inconvenient."],
    skip=["Never."],
    related=["<b>Where Are We, Really?</b> (vol. 2)", "<b>Delivering Bad News</b> (Grace, vol. 5)", "<b>Own the Outcome</b> (vol. 1)", "<b>When Do I Take It Upstairs?</b> (vol. 2)"],
    quiz=[("Name PMI's four values.", "Responsibility, respect, fairness, honesty."),
          ("Why not red, to be safe?", "Untrue the other way: the opening held; overstating is also misreporting."),
          ("What did Sanne give Femke instead of green?", "Amber with facts, the recovery, a decision date, and one sentence for investors."),
          ("Femke insists on green. What then?", "Sanne doesn't send it herself; Femke can present her own view; Sanne records that she said so."),
          ("A supplier offers you a weekend away “for being a great client” mid-tender. What's at stake?", "Fairness and honesty: decline, tell your manager, keep the tender clean.")],
    try_it="Find your project's colour rules. If none are written, write them before you need them. Then think of the last time you shaded a report, and write the true version that would have helped.",
    remember="Write “small leak, <span class=\"hl\">cheap to fix</span>”, then offer to <span class=\"hl\">fix it</span>.",
    sources=["Project Management Institute, <i>Code of Ethics and Professional Conduct</i> (2006).",
             "Project Management Institute, <i>PMBOK Guide</i>, Eighth Edition (2025): principle, be an accountable leader.",
             "Tom DeMarco and Timothy Lister, <i>Peopleware</i> (3rd ed., 2013)."],
)

NOTES = [PMO_GROWN, SERVANT, ETHICS]
