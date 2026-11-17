# Series 2 · Book 3 · The Project Manager's Notebook · Vol. 6 · Growing (the project manager, the next one, the handover)
# Narrator: Sanne. Facts: docs/larder-casebook.md, "Book 3, Vol. 6"; numbers in the comment block of 01_fitting.py.
# Two-year review Wed 12 Jan 2028 with Joost (her manager); feedback from 6 people; PMP exam passed Fri 21 Apr 2028.
# Hiring: role card Mon 8 Nov 2027; 34 applicants → 9 screening calls → 4 work samples (6–10 Dec) → offer Fri 17 Dec;
#   Nadia starts Mon 7 Feb 2028 (one of Marco's four central hires for 2028). Panel: Sanne, Joost, Yara.
# Handover of Haarlem to Nadia: plan Mon 26 Jun 2028; Nadia leads from Mon 3 Jul; Haarlem moved 4 → 11 Sep on Mon 17 Jul
#   (Nadia and Ana); Sanne's mistake: week of 24 Jul agreed a charger-position change on the builder's call (Wed 26 Jul);
#   fixed Fri 28 Jul. Haarlem opened Mon 11 Sep 2028. Eight cities by the board of Thu 28 Sep.
# Closing note Mon 25 Sep 2028: about 51,000 orders a day in September, on course for 60,000 by December.

GROW = ["resources"]

# ------------------------------------------------------------------ 12 How Do I Get Better at This?
gr_problem = Doodle(760, 260, "Doodle of Wednesday 12 January 2028, Sanne's two-year review with Joost. Two years ago she arrived from warehouse fit-outs with a ninety-six-task plan the team threw away. Since then: six city launches, one that slipped, a playbook. Joost asks two questions: what are you better at, and what next? Sanne has a long list of what happened and a short list of what she learned.",
                    "Two years, six launches. Joost: “What are you better at, and what next?” A long list of events, a short one of learning.", exact=True)
gr_problem.box(20, 24, 330, 140, None, "paper")
gr_problem.head(185, 60, "Jan 2026", size=19)
gr_problem.text(185, 94, "a 96-task plan, thrown away", size=16)
gr_problem.text(185, 122, "predictive only", size=16)
gr_problem.box(410, 24, 330, 140, None, "green")
gr_problem.head(575, 60, "Jan 2028", size=19)
gr_problem.text(575, 94, "6 launches, 1 slipped", size=16)
gr_problem.text(575, 122, "a playbook, a programme", size=16)
gr_problem.note(380, 210, "experience is what happened; growth is what you can now do", "red", size=17)
gr_problem.note(380, 242, "and what next: a programme, a colleague, a certificate?", "pen", size=16)

gr_analogy = Doodle(760, 250, "Doodle of a cyclist training for a long ride. Riding a lot isn't enough. She keeps a log, asks a coach to watch her climb, works on the weak thing (hills), and enters one event a year that tests her against a standard. The log turns rides into progress.",
                    "Riding a lot isn't training. A log, a coach, the weak thing, and a test against a standard.", exact=True)
gr_analogy.row([("a log", "every ride", "y"), ("a coach", "watches the climb", "blue"), ("the weak thing", "hills", "pink"), ("a test", "one event a year", "green")], y=40, h=96, size=17, subsize=13)
gr_analogy.note(380, 196, "the log turns rides into progress", "pen", size=19)

gr_how = Doodle(760, 470, "Sanne's growth plan from the review of 12 January 2028. What's better, from feedback from six people: tailoring, honest status, the team owning its estimates. What to work on: regulators and outside stakeholders, Antwerp's lesson; letting go, coaching instead of doing; programme thinking. Three ways to grow: the programme Cities 2028, a stretch; coaching Nadia, which teaches letting go; the PMP certification, taken on 21 April 2028, for the shared vocabulary and the structured review of what she had learned by doing. And one habit since January 2026: this notebook, one page per question.",
                "Better at · to work on · three ways to grow · one habit. The notebook is the log that turned launches into learning.", exact=True)
gr_how.box(14, 14, 360, 160, None, "green")
gr_how.head(194, 42, "better at (6 people said)", size=16)
for i, t in enumerate(["tailoring to the work", "status that tells the truth", "teams owning estimates"]):
    gr_how.text(194, 78 + i * 30, t, size=14)
gr_how.box(386, 14, 360, 160, None, "pink")
gr_how.head(566, 42, "to work on", size=16)
for i, t in enumerate(["outside stakeholders, regulators", "letting go: coach, not do", "programme thinking"]):
    gr_how.text(566, 78 + i * 30, t, size=14)
gr_how.row([("a stretch", "programme Cities 2028", "y"), ("a person", "coaching Nadia", "blue"), ("a standard", "PMP, 21 Apr 2028", "paper")], y=190, h=96, size=16, subsize=13)
gr_how.box(14, 304, 732, 150, None, "y")
gr_how.head(380, 334, "one habit since 12 January 2026", size=16)
gr_how.text(380, 366, "this notebook: one page per question, written the week it happened", size=14)
gr_how.text(380, 392, "the situation, what I did, what I'd do next time", size=14)
gr_how.text(380, 418, "90 pages in two years; the playbook was built from them", size=14)

gr_deep1 = Doodle(760, 280, "Three kinds of skill a project manager needs, after PMI's talent triangle, with Sanne's examples. Ways of working: predictive, adaptive and hybrid methods, estimating, risk, earned value. Power skills: leading without authority, communicating, coaching, negotiating, honesty under pressure. Business acumen: knowing what a launch is worth, payback, the price of a week late, the investors' view. Most of her growth after the first year was in the second and third.",
                  "Ways of working, power skills, business acumen. After year one, most of the growth was in the last two.", exact=True)
gr_deep1.row([("ways of working", "methods, estimating, risk", "blue"), ("power skills", "influence, coaching, honesty", "pink"), ("business acumen", "value, payback, a week's price", "green")], y=30, h=120, size=17, subsize=13)
gr_deep1.note(380, 200, "year one: mostly ways of working · year two: mostly the other two", "pen", size=16)
gr_deep1.note(380, 240, "a certificate tests the first well, the others barely", "red", size=16)

GROWING = dict(
    slug="growing-as-a-project-manager",
    kicker="a.k.a. growing as a project manager, and what certification is for",
    tldr="Experience is what happened to you; growth is what you can now do that you couldn't. Turn the first into the second on purpose: keep a <b>log</b> (one page per hard question, written that week), ask for <b>feedback</b> from several people, pick one or two <b>weak things</b> to work on, take a <b>stretch</b> that exercises them, teach someone, and measure yourself against a <b>standard</b> now and then. A certification such as the PMP is good for a shared vocabulary and a structured review of what you learned by doing; it tests methods well and judgment barely.",
    chips=[("Family", "growing"), ("Lives in", "a log, a yearly review, a growth plan of one page"), ("Pairs with", "servant leadership, hiring, the closing note")],
    pmbok=dict(covers="developing as a project professional: skills across ways of working, power skills and business acumen; feedback; certification and continuing learning",
               domains=GROW, processes=[], principles=["Be an accountable leader", "Build an empowered culture"], focus=["closing"],
               older="6th: the project manager's competences and the PMI talent triangle (3.4). 7th: leadership and the team. 8th: the project manager's role and development."),
    problem_side="Larder, Wednesday 12 January 2028",
    problem="""  <p class="lead">Sanne's <b>two-year review</b> with Joost. She arrived on 12 January 2026 from warehouse fit-outs, with a 96-task plan the team threw away on 4 February. Since then: Rotterdam, Utrecht, The Hague, Antwerp (five weeks late), Eindhoven, a playbook, and now a programme. Joost asks two questions: <span class="hl-pink">“What are you better at? And what next?”</span> Sanne has a long list of what happened, and finds the list of what she can now do is much shorter, and harder to write.</p>
  <ul>
    <li>Experience piled up faster than reflection.</li>
    <li>Strengths and gaps were impressions, not evidence.</li>
    <li>“What next” was a job title, not a skill.</li>
  </ul>""",
    problem_figs=[gr_problem],
    meanwhile=[("product-6", "growing-as-po", "Grace's two-year review (8 November 2027): what she's better at, from evidence, and a plan for the next year.",
                "Sanne's review two months later uses the same shape, and a log she has kept since her first week: this notebook.")],
    analogy_side="the cyclist's training",
    analogy="""  <p>A cyclist who wants to ride further doesn't just ride more. She keeps a <b>log</b> of every ride, asks a <b>coach</b> to watch her on a climb, works on her <b>weak thing</b> (hills), and enters <b>one event a year</b> that measures her against a standard. Riding is the experience. The log, the coach and the hills turn it into progress.</p>""",
    analogy_figs=[gr_analogy],
    map=[("The log of every ride", "This notebook: one page per question"),
         ("A coach watching the climb", "Feedback from six people"),
         ("The weak thing: hills", "Regulators and outside stakeholders; letting go"),
         ("A long ride as a stretch", "The Cities 2028 programme"),
         ("One event against a standard", "The PMP exam, 21 April 2028")],
    how_side="evidence, two weak things, three ways to grow, one habit",
    how="""  <p>Before the review Sanne asks <b>six people</b> (Joost, Femke, Grace, Ana, Eli, Yara) two questions each: what do I do well, and what should I do differently? <b>Better at</b>, in their words: fitting process to the work, a status they believe, and teams that own their estimates. <b>To work on</b>: people <b>outside</b> Larder (Antwerp's permit office was her blind spot), <b>letting go</b> (Eli: “you still fix things you should hand back”), and thinking in <b>programmes</b>, not launches. Three ways to grow follow. A <b>stretch</b>: the Cities 2028 programme. A <b>person</b>: coaching Nadia, which turns “letting go” into a weekly practice (and a mistake, in February). A <b>standard</b>: the <b>PMP</b> exam, taken on <b>21 April 2028</b> and passed. She's clear what it's for: a shared vocabulary with partners and the next hires, and a structured pass through the guide to find what she'd learned by doing and what she'd never met. It doesn't prove judgment; Antwerp did that, the hard way. And one <b>habit</b> she's kept since her first week: this notebook. One page per hard question, written the week it happened. Ninety pages in two years, and the playbook was built from them.</p>""",
    how_figs=[gr_how],
    steps=[("Keep a log", "One page per hard question, that week."),
           ("Ask several people for feedback", "Two questions each."),
           ("Pick one or two weak things", "From the evidence."),
           ("Take a stretch that exercises them", "And someone to teach."),
           ("Test yourself against a standard", "Know what it does and doesn't prove."),
           ("Review once a year", "Better at, to work on, next.")],
    vocab=[("Talent triangle", "PMI's three skill areas: ways of working, power skills, business acumen."),
           ("Power skills", "Leading, communicating, coaching, negotiating: once called soft skills."),
           ("Stretch assignment", "Work slightly beyond what you can already do, chosen to grow."),
           ("PMP", "Project Management Professional, PMI's best-known certification."),
           ("Continuing education", "Learning kept up after certification (PMI asks for 60 hours every three years)."),
           ("Reflective practice", "Writing down what happened and what you'd do differently, regularly.")],
    code=dict(file="programme/12-growth-plan.md", note="Sanne, two-year review with Joost, Wednesday 12 January 2028", plain=True, src="""
# SANNE · TWO YEARS ON, AND NEXT                                  12 Jan 2028 · with Joost

FEEDBACK FROM   Joost · Femke · Grace · Ana · Eli · Yara (two questions each)
BETTER AT       tailoring to the work · status people believe · teams owning estimates
TO WORK ON      people outside Larder (regulators: Antwerp) · letting go ("you still fix
                things you should hand back", Eli) · thinking in programmes
GROW BY         stretch: programme manager, Cities 2028 (from 10 Jan)
                a person: coach Nadia (from 7 Feb)
                a standard: PMP exam (passed Fri 21 Apr 2028), for shared vocabulary
                and a structured look at what I learned by doing; not proof of judgment
HABIT           this notebook since 12 Jan 2026: one page per question, written that week
                · ~90 pages · the playbook was built from them
NEXT REVIEW     Jan 2029
"""),
    tools="tools: a notebook, six people's honest answers, a stretch, someone to coach, and one exam.",
    deep_dive=dict(
        side="three kinds of skill, learning from projects, certifications, and mentoring both ways",
        intro="Most project managers learn by doing, which is slow and expensive for the projects they learn on. This chapter covers what there is to get better at, how to learn faster from your own projects, what certifications are actually good for, and why the person you coach teaches you as much as you teach them.",
        parts=[
            ("Three kinds of skill", """  <p>PMI groups a project manager's skills into a <b>talent triangle</b>. <b>Ways of working</b>: the methods in this book, from critical path to Monte Carlo. <b>Power skills</b>: leading without authority, communicating across languages, coaching, telling the truth under pressure. <b>Business acumen</b>: knowing what the work is worth, what a week late costs, how investors see it.</p>
  <p>Sanne's first year was mostly the first kind: she had to learn adaptive methods and Larder's money. Her second year was mostly the other two: the permit office, Femke's investor update, Nadia. That's the usual shape.</p>""", [gr_deep1]),
            ("Learning from your own projects", """  <ul>
    <li><b>Write it down the same week</b>: the situation, what you did, what you'd do next time. Memory edits.</li>
    <li><b>Look for your own patterns</b>: Sanne's three biggest mistakes (the internet line, the permit, the drawings) were all the same kind: something outside the room that nobody in the room knew.</li>
    <li><b>Ask the people who were there</b>: feedback from six people is evidence; one opinion is weather.</li>
    <li><b>Turn a lesson into a habit</b>, not a resolution: “read three low rows aloud at every review.”</li>
  </ul>""", []),
            ("What certifications are for", """  <p>A certification such as the <b>PMP</b> (PMI), <b>PRINCE2</b> (a UK method), or an agile one gives three things: a <b>shared vocabulary</b> with other professionals, a <b>structured review</b> of a whole body of knowledge (Sanne found two areas she'd never met: procurement contract types beyond fixed price, and formal quality audits), and a <b>signal</b> to employers and partners. It doesn't show judgment, influence or courage. Take one when the vocabulary and the review are worth the study; don't mistake it for the experience.</p>""", []),
            ("Mentoring, both ways", """  <p>Coaching Nadia was on the plan to teach Nadia. It taught Sanne more: the 25 February status showed her “letting go” in one evening, and Nadia's questions in her second week (“which tools do I use?”) produced the toolbox page. Find someone to coach early. And keep someone who coaches you: for Sanne from 2028, Ana, who grows architects the same way.</p>""", []),
        ]),
    dial=[("Light", "a busy year", ["A page a month in a log.", "Ask two people for feedback.", "One thing to work on."]),
          ("Standard", "Sanne", ["A log every week.", "Feedback from six people; a yearly review.", "A stretch, a person to coach, a standard."]),
          ("Heavy", "a career path", ["Formal development plans.", "Certifications and continuing education.", "Mentors and assessments."])],
    baseline="Each line compares <b>experience left to accumulate</b> to <b>a log, evidence-based feedback, chosen weak things, a stretch, a person to coach and a standard</b>.",
    ratings=[(3, 4, "Learning aimed at what the work needs."),
             (3, 4, "Better plans from known patterns."),
             (3, 4, "Her blind spot (outside the room) named."),
             (3, 4, "Strengths and gaps in writing."),
             (3, 4, "Joost and Femke see the growth."),
             (3, 4, "Coaching Nadia builds the team."),
             (3, 4, "Stretch work changes how she works."),
             (3, 3, "Neutral."),
             (3, 3, "A page a week, a review a year.")],
    pitfalls=[("Experience as growth", "Ten years, one year ten times.", "log, reflect, change a habit."),
              ("Feedback from one person", "Weather, not evidence.", "ask several."),
              ("Certificate as proof", "Judgment untested.", "know what it's for."),
              ("No one to coach", "A slower way to learn.", "teach someone early.")],
    use=["Every week (the log).", "Once a year (the review).", "Before choosing a next role.", "When considering a certification."],
    skip=["Never."],
    related=["<b>Who Serves Whom?</b> (this volume)", "<b>Growing as a Product Owner</b> (Grace, vol. 6)", "<b>Growing Other Architects</b> (Ana, vol. 6)", "<b>What Is My Job Here?</b> (vol. 1)"],
    quiz=[("Experience or growth: six launches?", "Experience. Growth is what she can now do: tailor, report honestly, coach."),
          ("What were Sanne's two weak things?", "People outside Larder (regulators); letting go."),
          ("What is the PMP for, in Sanne's view?", "A shared vocabulary and a structured review; not proof of judgment."),
          ("A colleague wants a certificate “to become a better PM”. What would you add?", "A log, feedback from several people, and a stretch; the certificate helps the vocabulary, the rest builds judgment."),
          ("What pattern did Sanne find in her three biggest mistakes?", "Each was something outside the room nobody in the room knew.")],
    try_it="Ask three people two questions: what do I do well, and what should I do differently? Write the answers on one page with one thing you'll practise this quarter.",
    remember="Riding isn't training. Keep the <span class=\"hl\">log</span>, find the <span class=\"hl\">hills</span>.",
    sources=["Project Management Institute, <i>PMBOK Guide</i>, Eighth Edition (2025): the project manager.",
             "Project Management Institute, the PMI Talent Triangle (2022 update: ways of working, power skills, business acumen).",
             "Donald Schön, <i>The Reflective Practitioner</i> (1983)."],
)

# ------------------------------------------------------------------ 13 Who Do We Hire?
hi_problem = Doodle(760, 260, "Doodle of November 2027. Marco has approved one of four central hires for 2028: a second project manager. The last time Larder hired one, Sanne, it was two conversations and a gut feeling. Thirty-four people apply. Every one of them can talk about stakeholders and risk registers. Which of them can run a launch?",
                    "34 applicants who can all talk about risk registers. Which one can run a launch?", exact=True)
hi_problem.box(20, 24, 330, 140, None, "paper")
hi_problem.head(185, 60, "last time (Sanne)", size=19)
hi_problem.text(185, 94, "two conversations", size=16)
hi_problem.text(185, 122, "a gut feeling", size=16)
hi_problem.box(410, 24, 330, 140, None, "y")
hi_problem.head(575, 60, "this time", size=19)
hi_problem.text(575, 94, "34 applicants", size=16)
hi_problem.text(575, 122, "all fluent in the words", size=16)
hi_problem.note(380, 210, "interviews test talking about the work", "red", size=18)
hi_problem.note(380, 242, "the job is doing it", "pen", size=17)

hi_analogy = Doodle(760, 250, "Doodle of a restaurant hiring a cook. They don't just ask about recipes. They ask the candidate to cook one dish in their kitchen, on a busy evening, and watch how they taste, ask, and handle the order that goes wrong.",
                    "A restaurant asks a cook to cook: one dish, their kitchen, a real evening.", exact=True)
hi_analogy.box(14, 40, 350, 110, "talk about recipes", "paper", sub="everyone can", size=18, subsize=14)
hi_analogy.box(396, 40, 350, 110, "cook one dish", "green", sub="their kitchen, their evening", size=18, subsize=14)
hi_analogy.arrow(366, 95, 392, 95)
hi_analogy.note(380, 200, "watch how they taste, ask, and recover", "pen", size=18)

hi_how = Doodle(760, 470, "The hiring process, November 2027 to February 2028. Role card, 8 November: what the job is, the three things that matter most: honest status, working with people outside, tailoring. Thirty-four applicants, nine screening calls, four work samples in the week of 6 December. The work sample: Antwerp's status and issue log of 15 July 2027, names removed; forty-five minutes to write Friday's status and the first three actions, then twenty minutes talking it through with Sanne, Joost and Yara, who score it on a sheet written before the first candidate. Nadia's stood out: amber, the issue in the first line, and her first action was to ask who at Larder owned the permit response. Offer 17 December; start 7 February 2028.",
                "Role card → 34 → 9 → 4 work samples → Nadia. The sample was Antwerp's real issue; she asked who owned the response.", exact=True)
hi_how.row([("role card", "8 Nov", "paper"), ("34 applied", "", "y"), ("9 screened", "calls", "y"), ("4 work samples", "6–10 Dec", "blue"), ("Nadia", "offer 17 Dec", "green")], y=14, h=80, gap=10, size=15, subsize=12)
hi_how.box(14, 110, 732, 170, None, "blue")
hi_how.head(380, 138, "the work sample (65 minutes)", size=16)
hi_how.text(380, 170, "Antwerp's status + issue log of 15 July 2027, names removed", size=14)
hi_how.text(380, 196, "45 min: write Friday's status and your first three actions", size=14)
hi_how.text(380, 222, "20 min: talk it through with Sanne, Joost and Yara", size=14)
hi_how.text(380, 250, "scored on a sheet written before the first candidate", size=13)
hi_how.box(14, 296, 360, 160, None, "paper")
hi_how.head(194, 324, "scored on", size=16)
for i, t in enumerate(["the truth in line one", "first actions: right ones?", "outside stakeholders", "asks good questions"]):
    hi_how.text(194, 356 + i * 25, t, size=14)
hi_how.box(386, 296, 360, 160, None, "green")
hi_how.head(566, 324, "Nadia's sample", size=16)
for i, t in enumerate(["amber; the issue first", "action 1: who at Larder", "owns the permit response?", "starts Mon 7 Feb 2028"]):
    hi_how.text(566, 356 + i * 25, t, size=14)

HIRING = dict(
    slug="hiring-a-project-manager",
    kicker="a.k.a. acquiring a project manager: the role card and the work-sample interview",
    tldr="To hire a project manager, decide first what the job <b>is</b> here (a role card with the three things that matter most), then watch candidates <b>do</b> it: a <b>work sample</b> built from a real situation (a status and an issue log, names removed), done in a set time, talked through with a small panel including someone who isn't a project manager. Write the <b>scoring sheet before</b> the first candidate, and give everyone the same task. Interviews test talking about the work; a work sample tests the work.",
    chips=[("Family", "growing"), ("Lives in", "a role card, a work sample, a scoring sheet"), ("Pairs with", "where do they come from (vol. 4), servant leadership, handing over")],
    pmbok=dict(covers="acquiring project management capability: defining the role, selecting fairly on evidence, and onboarding",
               domains=GROW, processes=["Acquire Resources"], principles=["Build an empowered culture"], focus=["executing"],
               older="6th: Acquire Resources (9.3), selection criteria. 7th: the Team domain."),
    problem_side="Larder, November 2027",
    problem="""  <p class="lead">Marco has approved one of his <b>four central hires for 2028</b> for a second project manager, to run launches while Sanne runs the programme. The last time Larder hired one, Sanne herself, it was two conversations and a good feeling. <b>Thirty-four</b> people apply. Every one of them can talk fluently about stakeholders, risk registers and agile. <span class="hl-pink">Which of them can run a launch, and tell Femke the truth on a bad Friday?</span></p>
  <ul>
    <li>Conversations reward people who talk well about the work.</li>
    <li>Nobody had said what the job needs most at Larder.</li>
    <li>Each interviewer would judge on something different.</li>
  </ul>""",
    problem_figs=[hi_problem],
    meanwhile=[("product-6", "hiring-a-po", "Grace hires Jonas as the business product owner (from 22 November 2027) with a work sample of ten anonymised, Korenwolf-style requests to sort in two hours.",
                "Sanne hires Nadia the same month, the same way: a real Antwerp status and issue log, names removed, and a scoring sheet written first.")],
    analogy_side="the cook's trial",
    analogy="""  <p>A restaurant hiring a cook doesn't only ask about recipes. It asks the candidate to <b>cook one dish</b> in its kitchen, on a real evening, and watches: do they taste as they go, ask where things are, handle the order that comes back? Everyone can talk about a risotto. Cooking one under pressure is the job.</p>""",
    analogy_figs=[hi_analogy],
    map=[("Talking about recipes", "A conversation about stakeholders and risk"),
         ("Cooking one dish", "Writing Friday's status from Antwerp's real issue log"),
         ("Their kitchen", "Larder's own documents, names removed"),
         ("The order that comes back", "The permit issue of 15 July 2027"),
         ("Tasting as they go", "Asking who owns the response")],
    how_side="role card, work sample, a scoring sheet first, a mixed panel",
    how="""  <p>On <b>Monday 8 November 2027</b> Sanne writes a <b>role card</b>: run a city launch from the playbook, with three things that matter most: <b>honest status</b>, working with <b>people outside Larder</b> (Antwerp's lesson), and <b>tailoring</b>. Thirty-four applicants; <b>nine</b> screening calls of twenty minutes; <b>four</b> work samples in the week of <b>6 December</b>. The sample: Antwerp's status and issue log of <b>15 July 2027</b> (the day the permit became an issue), names removed; 45 minutes to write Friday's status and the first three actions; 20 minutes talking it through with Sanne, Joost and <b>Yara</b>, the Rotterdam store manager, who isn't a project manager and sees things they don't. All three score on a sheet written <b>before</b> the first candidate. <b>Nadia</b>, six years in a retail chain's store-opening team, writes amber with the issue in line one, and her first action is a question: <b>“who at Larder owns the permit response?”</b> Offer on <b>Friday 17 December</b>; she starts on <b>Monday 7 February 2028</b> with a first week planned: the playbook, a day at Eindhoven, an afternoon with Maarten.</p>""",
    how_figs=[hi_how],
    steps=[("Write the role card", "The three things that matter most here."),
           ("Write the scoring sheet before interviewing", "Same for everyone."),
           ("Build a work sample from a real case", "Names removed."),
           ("Time it, then talk it through", "What did they see first? What would they ask?"),
           ("Include a panellist from outside the role", "They see different things."),
           ("Plan the first week before they arrive", "Onboarding is part of hiring.")],
    vocab=[("Role card", "A short description of what the job is for and what matters most."),
           ("Work sample", "A realistic task from the job, done during selection."),
           ("Structured interview", "The same questions and scoring for every candidate."),
           ("Scoring sheet", "Criteria and scales agreed before interviewing."),
           ("Onboarding", "Bringing a new person into their role: people, tools, first work."),
           ("Hiring cap", "A limit on new hires; Marco's: four central hires a year.")],
    code=dict(file="programme/13-pm-hiring.md", note="Sanne, Joost and Yara, November 2027 → February 2028", plain=True, src="""
# HIRING · PROJECT MANAGER, CITY LAUNCHES                 role card 8 Nov 2027 · start 7 Feb 2028

ROLE        run a city launch from the playbook, under the Cities 2028 programme
MATTERS     1 honest status · 2 people outside Larder · 3 tailoring to the work
FUNNEL      34 applied → 9 screening calls (20 min) → 4 work samples (6-10 Dec) → 1 offer
SAMPLE      Antwerp status + issue log of 15 Jul 2027 (names removed) · 45 min: write
            Friday's status + first 3 actions · 20 min talk-through
PANEL       Sanne · Joost · Yara (store manager, not a PM)
SCORING     written 1 Dec, before the first candidate: truth in line one (1-4) ·
            right first actions (1-4) · outside stakeholders (1-4) · questions (1-4)
CHOSEN      Nadia (6 years opening stores for a retail chain): amber, issue first;
            action 1 "who at Larder owns the permit response?" · offer Fri 17 Dec
WEEK ONE    playbook v4 · a day at Eindhoven · an afternoon with Maarten · 1:1 Tuesdays
CAP         one of Marco's four central hires for 2028
"""),
    tools="tools: a role card, a real case with names removed, a stopwatch, a scoring sheet written first, and Yara.",
    dial=[("Light", "a contractor for a few weeks", ["Look at past work.", "One conversation on a real problem.", "References."]),
          ("Standard", "a permanent PM", ["Role card, screening, a work sample.", "Scoring sheet first, mixed panel.", "First week planned."]),
          ("Heavy", "senior or many hires", ["Assessment centres.", "Several work samples.", "Structured references and probation reviews."])],
    baseline="Each line compares <b>two conversations and a feeling</b> to <b>a role card, a real work sample, a scoring sheet written first, and a mixed panel</b>.",
    ratings=[(3, 4, "Hired for what the job needs here."),
             (3, 4, "The work sample predicts the work."),
             (3, 4, "A weak hire is less likely."),
             (3, 4, "Criteria written before candidates."),
             (3, 4, "Joost and Yara trust the choice."),
             (3, 4, "Nadia owns a launch from week two."),
             (3, 3, "Neutral."),
             (3, 3, "Neutral."),
             (3, 2, "Four 65-minute samples and a panel.")],
    pitfalls=[("Conversation only", "Rewards talkers.", "a work sample."),
              ("Criteria after meeting them", "Bias decides.", "scoring sheet first."),
              ("Only PMs on the panel", "One kind of view.", "add someone the PM will serve."),
              ("No first week", "A slow, lonely start.", "plan onboarding before day one.")],
    use=["Hiring a PM or any role with a doable core task.", "When many candidates sound alike.", "When fairness matters (always).", "Before writing a job ad."],
    skip=["Never skip the role card; a sample may be shorter for short contracts."],
    related=["<b>Where Do They Come From?</b> (vol. 4)", "<b>Hiring a Product Owner</b> (Grace, vol. 6)", "<b>Who Serves Whom?</b> (this volume)", "<b>Can Someone Else Run This?</b> (next note)"],
    quiz=[("What were the three things that matter most?", "Honest status, people outside Larder, tailoring."),
          ("What was the work sample?", "Antwerp's status and issue log of 15 July 2027, names removed: write the status and first three actions."),
          ("Why was Yara on the panel?", "She isn't a PM; she sees how a candidate would work with a store."),
          ("A strong talker scores 2 on the sample. Joost wants to hire anyway. What do you say?", "The sheet was agreed first; the sample is the job; discuss the gap against the criteria, not the impression."),
          ("What did Nadia's first action show?", "She looked for the owner of the response, the lesson Antwerp learned late.")],
    try_it="For the next hire you help with, write the role card's three things and the scoring sheet before you see any CV. Turn one real past situation into a 45-minute task.",
    remember="Don't ask about the <span class=\"hl\">risotto</span>. Ask them to <span class=\"hl\">cook</span> one.",
    sources=["Project Management Institute, <i>PMBOK Guide</i>, Eighth Edition (2025): Resources domain, acquiring resources.",
             "Frank L. Schmidt and John E. Hunter, “The Validity and Utility of Selection Methods in Personnel Psychology” (1998).",
             "Laszlo Bock, <i>Work Rules!</i> (2015): structured interviews and work samples."],
)

# ------------------------------------------------------------------ 14 Can Someone Else Run This?
ho_problem = Doodle(760, 260, "Doodle of the week of 24 July 2028 and Sanne's mistake for this collection. Haarlem was handed to Nadia on 3 July. On Wednesday the builder's site manager phones Sanne, as he's used to, about moving the e-bike chargers. Sanne agrees on the call. Nadia finds out on Friday from the builder. The handover had a plan, and Sanne still answered the phone.",
                    "Haarlem is Nadia's from 3 July. On 26 July the builder phones Sanne, and Sanne decides on the call.", exact=True)
ho_problem.row([("3 Jul", "Nadia leads", "green"), ("Wed 26 Jul", "builder calls Sanne", "y"), ("Sanne agrees", "chargers moved", "pink"), ("Fri 28 Jul", "Nadia hears it", "pink")], y=24, h=96, size=16, subsize=13)
ho_problem.note(380, 170, "two voices to one supplier", "red", size=19)
ho_problem.note(380, 206, "handing over is also stopping", "pen", size=17)

ho_analogy = Doodle(760, 250, "Doodle of a relay baton changing hands in the passing zone. The incoming runner runs alongside, the outgoing runner hands it over cleanly, and then lets go and stops running. If the old runner keeps a hand on the baton, both slow down.",
                    "A clean baton change: run alongside, hand over, then let go and stop running.", exact=True)
ho_analogy.row([("run alongside", "shadow", "blue"), ("hand over", "lead, with support", "y"), ("let go", "and stop running", "green")], y=40, h=96, gap=34, size=18, subsize=14, arrows=True)
ho_analogy.note(380, 196, "a hand left on the baton slows both runners", "pen", size=18)

ho_how = Doodle(760, 470, "The handover of Haarlem from Sanne to Nadia, summer 2028. Plan, 26 June: what moves, the decision rights, the open risks and issues, the introductions. Shadow: Nadia joins every Haarlem meeting in the last two weeks of June. Lead from 3 July, with Sanne as back-up. Nadia leads the decision of 17 July to move the opening from 4 to 11 September with Ana, so Haarlem opens on the new ordering database. The slip: Sanne decides on a builder's call on 26 July. The fix, 28 July: a letter to every Haarlem supplier, Nadia decides; Sanne's phone says ask Nadia; the charger change reviewed by Nadia, kept. Step out: from 7 August Sanne attends only the programme board. Haarlem opened on Monday 11 September.",
                "Plan → shadow → lead → (slip, fixed in writing) → step out. Nadia moved the date herself; Haarlem opened 11 September.", exact=True)
ho_how.row([("plan", "26 Jun", "paper"), ("shadow", "last 2 weeks Jun", "blue"), ("lead", "from 3 Jul", "y"), ("step out", "from 7 Aug", "green")], y=14, h=80, gap=34, size=16, subsize=12, arrows=True)
ho_how.box(14, 110, 360, 190, None, "paper")
ho_how.head(194, 138, "handed over", size=16)
for i, t in enumerate(["decision rights (in writing)", "open risks and issues", "budget and contingency", "introductions: builder, Hilde", "the steering note"]):
    ho_how.text(194, 170 + i * 25, t, size=14)
ho_how.box(386, 110, 360, 190, None, "green")
ho_how.head(566, 138, "Nadia decided", size=16)
for i, t in enumerate(["17 Jul: 4 → 11 Sep, with Ana", "(the new ordering database)", "the charger change, kept", "go / no-go, 8 Sep"]):
    ho_how.text(566, 170 + i * 25, t, size=14)
ho_how.box(14, 316, 732, 80, "the slip, 26 Jul → fixed 28 Jul", "pink", sub="a letter to every supplier: Nadia decides · Sanne's phone: “ask Nadia”", size=16, subsize=13)
ho_how.box(14, 410, 732, 48, "Haarlem opened Mon 11 September 2028: eight cities", "green", size=16)

HANDOVER_P = dict(
    slug="handing-over-a-programme",
    kicker="a.k.a. handing over: letting someone else run it",
    tldr="Handing over work you've led means moving <b>decision rights</b>, not just documents: write down what moves, introduce the new lead to everyone who calls, let them <b>shadow</b>, then <b>lead with you as back-up</b>, then <b>step out</b> on a date. The hardest part is the last one: when someone phones you out of habit, <b>send them on</b> instead of deciding. Tell every outside party in writing who decides now. A handover is finished when the new lead makes a big decision without you.",
    chips=[("Family", "growing"), ("Lives in", "a handover plan, a letter to suppliers, and a date to step out"), ("Pairs with", "who looks after it now (vol. 2), servant leadership, hiring")],
    pmbok=dict(covers="transferring leadership of a project or programme: decision rights, knowledge, relationships, and the outgoing lead stepping back",
               domains=["governance", "resources"], processes=["Close Project or Phase", "Lead the Team"], principles=["Build an empowered culture"], focus=["closing", "executing"],
               older="6th: transitions in Close Project or Phase (4.7) and team development. 7th: the Team and Delivery domains."),
    problem_side="Larder, week of 24 July 2028",
    problem="""  <p class="lead">This is <b>Sanne's mistake</b> for this collection. Haarlem was handed to Nadia on <b>3 July</b>, with a plan. On <b>Wednesday 26 July</b> the builder's site manager phones Sanne, as he has for two launches, about moving the e-bike chargers to the other wall. It's a small, sensible change; Sanne agrees on the call. <span class="hl-pink">Nadia hears about it on Friday, from the builder.</span> Now one supplier has two people who decide, and Nadia has learned that her authority holds until someone rings Sanne.</p>
  <ul>
    <li>Suppliers call whoever they're used to.</li>
    <li>Sanne answered out of habit, and helpfully.</li>
    <li>The handover moved the documents, not the phone calls.</li>
  </ul>""",
    problem_figs=[ho_problem],
    meanwhile=[("product-6", "handing-over", "Grace hands part of her area to Jonas: shadow 3–14 January, lead 17 January–25 February, Grace steps out on 28 February 2028.",
                "Sanne uses the same shape for Haarlem, and learns that stepping out includes the phone."),
               ("architect-6", "handover-to-operations", "Ana hands Ordering to the reliability team with game days and a pager date (1 October 2028).",
                "Sanne's handover to Nadia has its own pager date: 7 August, when she stops attending anything but the programme board.")],
    analogy_side="the baton",
    analogy="""  <p>In a relay the baton changes hands in a <b>passing zone</b>. The incoming runner is already running alongside; the outgoing runner hands it over cleanly, and then <b>lets go and stops running</b>. If the old runner keeps a hand on the baton for a few more steps, out of care, both slow down and the team may be disqualified.</p>""",
    analogy_figs=[ho_analogy],
    map=[("Running alongside", "Nadia shadows Haarlem in the last two weeks of June"),
         ("The clean pass", "Decision rights in writing, 3 July"),
         ("A hand left on the baton", "Sanne deciding on the builder's call, 26 July"),
         ("Letting go", "A letter to every supplier; “ask Nadia”"),
         ("Stopping running", "From 7 August, only the programme board")],
    how_side="plan, shadow, lead, step out, and redirect the phone",
    how="""  <p>The plan, written on <b>26 June</b>: what moves (decision rights, open risks and issues, budget and contingency, the steering note), introductions (the builder, Hilde, Haarlem's landlord), and dates. Nadia <b>shadows</b> every Haarlem meeting in the last two weeks of June and <b>leads</b> from 3 July with Sanne as back-up. The handover's real test comes early: on <b>17 July</b> Nadia and Ana decide to move Haarlem from <b>4 to 11 September</b> so it opens on the new ordering database, and Nadia takes it to Femke herself. Then the slip. On <b>Friday 28 July</b> Sanne fixes the cause, not just the charger: a <b>letter to every Haarlem supplier</b> saying Nadia decides; Sanne's phone and email reply “ask Nadia”; the charger change goes back to Nadia, who keeps it. From <b>7 August</b> Sanne <b>steps out</b> to the programme board only. Haarlem opens on <b>Monday 11 September</b>: Larder's eighth city, in time for the board of 28 September.</p>""",
    how_figs=[ho_how],
    steps=[("Write what moves", "Decision rights first."),
           ("Introduce them to everyone who calls", "In person where you can."),
           ("Shadow, then lead with back-up", "With dates."),
           ("Tell outside parties in writing", "Who decides now."),
           ("Send calls on; don't decide", "Even small things."),
           ("Step out on a date", "Done when they decide something big without you.")],
    vocab=[("Handover", "Moving responsibility for work from one person to another."),
           ("Decision rights", "Which decisions a role may take alone."),
           ("Shadowing", "The new lead joins the work before taking it over."),
           ("Back-up", "The outgoing lead, available but not deciding."),
           ("Step-out date", "When the outgoing lead stops taking part."),
           ("Two voices", "A supplier or team hearing decisions from two people.")],
    code=dict(file="programme/14-haarlem-handover.md", note="Sanne and Nadia, 26 June → 7 August 2028", plain=True, src="""
# HAARLEM · HANDOVER TO NADIA                                      plan 26 Jun 2028

MOVES       decision rights (all Haarlem decisions within the playbook and budget) ·
            open risks (6) and issues (2) · budget and contingency · steering note
INTRODUCED  builder's site manager · Hilde (permit) · landlord · Haarlem store manager
DATES       shadow 19-30 Jun · lead from Mon 3 Jul (Sanne back-up) · step out Mon 7 Aug
TEST        17 Jul: Nadia + Ana move opening 4 → 11 Sep (new ordering database);
            Nadia takes it to Femke herself
SLIP        Wed 26 Jul: Sanne agreed the charger move on the builder's call
FIX         Fri 28 Jul: letter to every Haarlem supplier, "Nadia decides" · Sanne's phone
            and email: "ask Nadia" · charger change reviewed by Nadia: kept
RESULT      Haarlem opened Mon 11 Sep 2028 · eight cities by the board of Thu 28 Sep
"""),
    tools="tools: a handover plan, introductions, a letter to suppliers, an auto-reply, and a step-out date.",
    dial=[("Light", "a small piece of work", ["A one-page note.", "Introductions.", "Stop answering for it."]),
          ("Standard", "a city launch", ["Plan, shadow, lead, step out, with dates.", "Decision rights in writing.", "Suppliers told; calls redirected."]),
          ("Heavy", "a programme or a regulated service", ["Formal transition plan and acceptance.", "Knowledge transfer sessions.", "A hypercare period with metrics."])],
    baseline="Each line compares <b>a handover of documents, with the old lead still answering calls</b> to <b>decision rights moved in writing, suppliers told, calls redirected, a step-out date</b>.",
    ratings=[(3, 4, "The launch kept moving through the change."),
             (3, 4, "Decisions come from one place."),
             (3, 4, "Open risks moved with their owner."),
             (2, 4, "Everyone knows who decides."),
             (3, 4, "Femke heard the date change from Nadia."),
             (2, 5, "Nadia owns Haarlem."),
             (3, 4, "Nadia moved the date herself."),
             (3, 3, "Neutral."),
             (3, 3, "A plan, a letter, a date.")],
    pitfalls=[("Documents, not decisions", "Nothing really moves.", "move decision rights first."),
              ("Answering out of habit", "Two voices.", "send calls on."),
              ("No step-out date", "The old lead lingers.", "set it in the plan."),
              ("Outside parties not told", "They call who they know.", "write to them.")],
    use=["When someone takes over work you lead.", "When you move to a bigger role.", "Before leave or leaving.", "Whenever a supplier calls the wrong person."],
    skip=["Never; on small work it's one note and a phone call."],
    related=["<b>Who Looks After It Now?</b> (vol. 2)", "<b>Handing Over a Product Area</b> (Grace, vol. 6)", "<b>Handover to Operations</b> (Ana, vol. 6)", "<b>Who Serves Whom?</b> (this volume)"],
    quiz=[("What moves first in a handover?", "Decision rights."),
          ("What was Sanne's slip, and how was the cause fixed?", "She decided on a builder's call; a letter to every supplier and an “ask Nadia” reply."),
          ("What showed the handover had worked?", "Nadia moved Haarlem's date (4 → 11 Sep) with Ana and took it to Femke herself."),
          ("A week after stepping out, Femke asks you about Haarlem. What do you do?", "Point her to Nadia, and tell Nadia she asked."),
          ("When is a handover finished?", "When the new lead makes a big decision without you.")],
    try_it="List the people who still call you about work you've handed over. Write to each of them, today, saying who decides now.",
    remember="Hand over the <span class=\"hl\">baton</span>. Then <span class=\"hl\">stop running</span>.",
    sources=["Project Management Institute, <i>PMBOK Guide</i>, Eighth Edition (2025): Governance, closing a phase; Resources, leading the team.",
             "Michael Watkins, <i>The First 90 Days</i> (2003).",
             "Project Management Institute, <i>PMBOK Guide</i>, Sixth Edition (2017): 4.7 Close Project or Phase."],
)

# ------------------------------------------------------------------ 15 What Was It All For?
cl_problem = Doodle(760, 260, "Doodle of Monday 25 September 2028, three days before the board. Eight cities are open. Sanne rereads her first notebook pages from January 2026: a lease date, a spreadsheet with thirty-one rows without an owner, and the six principles she'd copied out on her second day without knowing what they'd look like in practice.",
                    "Eight cities open. Sanne rereads January 2026: a lease date, 31 rows without an owner, six principles copied out.", exact=True)
cl_problem.box(20, 24, 330, 140, None, "paper")
cl_problem.head(185, 60, "12 Jan 2026", size=19)
cl_problem.text(185, 94, "one city, 15 weeks to go", size=16)
cl_problem.text(185, 122, "31 rows without an owner", size=16)
cl_problem.box(410, 24, 330, 140, None, "green")
cl_problem.head(575, 60, "25 Sep 2028", size=19)
cl_problem.text(575, 94, "eight cities open", size=16)
cl_problem.text(575, 122, "≈ 51,000 orders a day", size=16)
cl_problem.note(380, 210, "six principles: what did they turn out to mean?", "pen", size=18)
cl_problem.note(380, 242, "the last page of the notebook", "pen", size=16)

cl_analogy = Doodle(760, 250, "Doodle of a hiker at the top of a long route, looking back down at the path. From the top you can see which turns mattered: the stream where they almost turned back, the ridge they skipped in the wind. On the way up, each looked like any other bend.",
                    "From the top you can see which turns mattered. On the way up each was just a bend.", exact=True)
cl_analogy.line("M40 220 C 140 200, 160 120, 260 140 S 420 80, 500 100 S 640 40, 720 30", dash=True)
cl_analogy.raw('<circle class="d f-pink" cx="260" cy="140" r="9"/>')
cl_analogy.raw('<circle class="d f-pink" cx="500" cy="100" r="9"/>')
cl_analogy.raw('<circle class="d f-green" cx="720" cy="30" r="11"/>')
cl_analogy.note(260, 176, "the stream", "pen", size=15)
cl_analogy.note(500, 136, "the ridge", "pen", size=15)
cl_analogy.note(660, 22, "the top", "pen", size=15)

cl_how = Doodle(760, 470, "The six principles of the guide, each with the moment in Sanne's notebook where it stopped being a sentence. Adopt a holistic view: Antwerp's permit, outside the plan and outside the room. Focus on value: the benefits check that found Rotterdam's on-time target two months late. Embed quality: the store IT line in week one, after Rotterdam's internet line. Be an accountable leader: amber before the investors, 25 May 2028. Integrate sustainability: Ghent's cooling plant changed on paper. Build an empowered culture: the team throwing away her ninety-six-task plan on 4 February 2026, and Nadia moving Haarlem's date herself.",
                "Six principles, six moments. Each stopped being a sentence on a particular day.", exact=True)
pr = [("holistic view", "Antwerp's permit: outside the room", "blue"),
      ("focus on value", "benefits check: on-time, 2 months late", "y"),
      ("embed quality", "store IT in week 1, every city", "green"),
      ("accountable leader", "amber before investors, 25 May 2028", "pink"),
      ("sustainability", "Ghent's cooling changed on paper", "green"),
      ("empowered culture", "4 Feb 2026 plan binned · Nadia's date", "y")]
for i, (p_, t, f) in enumerate(pr):
    y = 14 + i * 74
    cl_how.box(8, y, 250, 64, p_, f, size=16, rx=6)
    cl_how.text(274, y + 39, t, anchor="start", size=15)

CLOSING = dict(
    slug="what-was-it-all-for",
    kicker="a.k.a. the six principles revisited: the book's closing note",
    tldr="The guide's six principles read like sentences anyone would agree with: see the whole, focus on value, build quality in, be accountable, think long-term, let the team decide. They only mean something when you can name the <b>day</b> each one changed a decision. At the end of a project, or a book, go back to the principles and write that day next to each. The ones without a day are the ones you haven't learned yet.",
    chips=[("Family", "growing"), ("Lives in", "the last page of the notebook"), ("Pairs with", "the six principles (vol. 1), every note since")],
    pmbok=dict(covers="the six principles of the guide, revisited through two years of practice",
               domains=["governance"], processes=[], principles=["Adopt a holistic view", "Focus on value", "Embed quality into processes and deliverables", "Be an accountable leader", "Integrate sustainability within all project areas", "Build an empowered culture"], focus=["closing"],
               older="7th: twelve principles. 8th: six, said more briefly."),
    problem_side="Larder, Monday 25 September 2028",
    problem="""  <p class="lead">Three days before the board of 28 September, <b>eight cities are open</b>: Amsterdam, Rotterdam, Utrecht, The Hague, Antwerp, Eindhoven, Ghent and Haarlem, with about <b>51,000 orders a day</b> in September, on course for the board's 60,000 by December. Sanne rereads the first pages of this notebook, from <b>January 2026</b>: a lease date fifteen weeks away, Joost's spreadsheet with <b>31 rows without an owner</b>, and the six principles she copied out on her second day. <span class="hl-pink">She agreed with all six then. She couldn't have said what any of them would cost or change.</span></p>
  <ul>
    <li>Principles are easy to agree with and hard to use.</li>
    <li>Each one only became real on a particular day.</li>
    <li>That day is worth writing down.</li>
  </ul>""",
    problem_figs=[cl_problem],
    analogy_side="looking back down the path",
    analogy="""  <p>At the top of a long hike you can look back down the path and see <b>which turns mattered</b>: the stream where you nearly turned back, the ridge you skipped because of the wind. On the way up, each one looked like any other bend. The view from the top doesn't change the route. It tells you which bends to watch for next time.</p>""",
    analogy_figs=[cl_analogy],
    map=[("The stream", "Antwerp's permit, July 2027"),
         ("The ridge skipped in wind", "Green before investors, refused"),
         ("Any other bend", "Every principle, the day it was copied out"),
         ("The view from the top", "This page"),
         ("Bends to watch next time", "The playbook and Nadia's launches")],
    how_side="each principle, and the day it changed a decision",
    how="""  <p><b>Adopt a holistic view</b>: Antwerp's permit, the thing outside the plan and outside the room, which set the date for a whole city. <b>Focus on value</b>: the benefits check of January 2028, which found Rotterdam's on-time target met two months late, and that nobody had looked. <b>Embed quality</b>: store IT in week one of every launch since Rotterdam's 4G router, a check that costs an hour and has never been needed since. <b>Be an accountable leader</b>: Ghent amber before the investors on 25 May 2028, and a sponsor who presented it. <b>Integrate sustainability</b>: Ghent's cooling plant changed while it was still a drawing. <b>Build an empowered culture</b>: the first and the last: on <b>4 February 2026</b> the team threw away Sanne's 96-task plan and planned its own work, and on <b>17 July 2028</b> Nadia moved Haarlem's date without asking her. Two years, eight cities, ninety-odd pages. If Sanne could leave one line on the first page for the person she was on 12 January 2026, it would be: <b>the plan is the team's, the truth is yours, and the thing that sets your date is usually outside the room.</b></p>""",
    how_figs=[cl_how],
    steps=[("Reread the principles", "At the end of something."),
           ("Write the day each one changed a decision", "One line each."),
           ("Notice the ones without a day", "Those are next."),
           ("Write one line for your earlier self", "What you'd want to know."),
           ("Put it where the next person starts", "The playbook's first page."),
           ("Start the next notebook", "One page per question.")],
    vocab=[("Principle", "A general rule that guides decisions in every situation."),
           ("Holistic view", "Seeing the project as one system inside a bigger one."),
           ("Value", "The benefit the project exists for."),
           ("Accountability", "Owning the outcome and the truth about it."),
           ("Stewardship", "Looking after what you're trusted with, for the long term."),
           ("Empowerment", "Giving people the room, facts and trust to decide.")],
    code=dict(file="programme/15-six-principles.md", note="Sanne, Monday 25 September 2028", plain=True, src="""
# THE SIX PRINCIPLES, TWO YEARS ON                               25 Sep 2028 · eight cities

PRINCIPLE                       THE DAY IT CHANGED A DECISION
Adopt a holistic view           Antwerp: the permit outside the plan, outside the room
                                (scored 3 in Nov 2026 · an issue on 15 Jul 2027)
Focus on value                  17 Jan 2028: Rotterdam's on-time benefit met two months
                                late, and nobody had looked
Embed quality                   store IT in week 1 of every launch, since Rotterdam's
                                4G router (2026)
Be an accountable leader        25 May 2028: Ghent amber before the investors
Integrate sustainability        Mar 2028: Ghent's cooling changed while still a drawing
Build an empowered culture      4 Feb 2026: my 96-task plan thrown away by the team ·
                                17 Jul 2028: Nadia moved Haarlem's date herself

ONE LINE FOR 12 JANUARY 2026
  The plan is the team's, the truth is yours, and the thing that sets your date is
  usually outside the room.
NEXT   a new notebook (programme 2029) · this page goes on the playbook's first page
"""),
    tools="tools: the first pages of the notebook, the six principles, and one line for your earlier self.",
    dial=[("Light", "end of a small project", ["Reread the principles.", "One line on the one you used most.", "Done."]),
          ("Standard", "end of a programme or year", ["Each principle with its day.", "The ones without a day named.", "A line for the next person."]),
          ("Heavy", "end of a career stage", ["A written reflection.", "Shared with those you coach.", "Into the organisation's method."])],
    baseline="Each line compares <b>six principles agreed with on day two</b> to <b>six principles each tied to the day it changed a decision</b>.",
    ratings=[(3, 5, "The book ends where Vol. 1 began: value."),
             (3, 4, "Lessons that make dates hold."),
             (3, 4, "The outside-the-room risk named."),
             (3, 4, "Each principle has evidence."),
             (3, 4, "Femke and the board can read it."),
             (3, 5, "Nadia starts with it."),
             (3, 4, "Principles hold as methods change."),
             (3, 4, "Quality habits named."),
             (3, 4, "One page.")],
    pitfalls=[("Agreeing, not using", "Principles as wallpaper.", "find the day each changed a decision."),
              ("Only successes", "The lessons are in the slips.", "include Antwerp."),
              ("Kept private", "The next person starts from zero.", "put it on the playbook's first page."),
              ("Stopping the notebook", "The next two years go unrecorded.", "start the next one.")],
    use=["At the end of a project, programme or year.", "Before handing over.", "When coaching someone new.", "When principles feel like slogans."],
    skip=["Never."],
    related=["<b>See the Whole</b> (vol. 1)", "<b>Focus on Value</b> (vol. 1)", "<b>Let the Team Decide</b> (vol. 1)", "<b>How Do I Get Better at This?</b> (this volume)"],
    quiz=[("Name the six principles.", "Holistic view, focus on value, embed quality, accountable leader, integrate sustainability, empowered culture."),
          ("Which day did “empowered culture” first change a decision?", "4 February 2026: the team threw away Sanne's 96-task plan."),
          ("Which principle did Antwerp teach?", "Adopt a holistic view: the permit, outside the plan and the room."),
          ("A principle has no day next to it. What does that tell you?", "It's one you haven't learned in practice yet; watch for it next."),
          ("What's Sanne's one line for January 2026?", "The plan is the team's, the truth is yours, and the thing that sets your date is usually outside the room.")],
    try_it="Write the six principles down. Next to each, the day it changed one of your decisions. Leave the empty ones empty, and look at them again in a year.",
    remember="The plan is the <span class=\"hl\">team's</span>, the truth is <span class=\"hl\">yours</span>, and the date is set <span class=\"hl\">outside the room</span>.",
    sources=["Project Management Institute, <i>PMBOK Guide</i>, Eighth Edition (2025): the six principles.",
             "Project Management Institute, <i>The Standard for Project Management</i> (2021): principles.",
             "Sanne's notebook, vols. 1–6 (2026–2028)."],
)

NOTES = [GROWING, HIRING, HANDOVER_P, CLOSING]
