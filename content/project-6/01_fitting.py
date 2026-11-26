# Series 2 · Book 3 · The Project Manager's Notebook · Vol. 6 · Fitting it to the work (tailoring, programmes, benefits)
# Narrator: Sanne. Running case study: Larder (facts in docs/larder-casebook.md, "Book 3, Vol. 6").
#
# THE SETTING (checked by script: weekdays and counts)
#   Eindhoven: tailoring sheet Mon 27 Sep 2027 → opened Mon 22 Nov 2027 (8 weeks), from playbook v3 (Antwerp, Oct).
#     Rotterdam: 58 file pages, 3 standing meetings (Thu leads, Fri status, Mon decision log) + fortnightly steering.
#     Eindhoven: 20 pages, 1 standing meeting (Thu 09:30, 30 min) + a steering note every other Friday, no meeting.
#   Artefact review Mon 6 Dec 2027: the 73 file pages (Rotterdam 58 + Antwerp 15): used as is 21 · used shortened 14 ·
#     merged into another 12 · not used 26 → the launch kit: 18 templates.
#   Playbook v4 Mon 13 Dec 2027 (v1 Utrecht Apr 2027, v2 The Hague Jun, v3 Antwerp Oct, v4 after Eindhoven).
#   Rotterdam benefits review Mon 17 Jan 2028 (Sanne's mistake: the +12-week check of Aug 2026 never happened):
#     500 orders a day by end May 2026 → met (590 in week 4) · 90 % express on time by end of summer 2026 → missed:
#     86 % in Sep 2026, 90 % only in Nov 2026 · next city in ≤ 8 weeks → met: Utrecht 15 Feb → 12 Apr 2027 (8 weeks),
#     The Hague 8, Eindhoven 8 (Antwerp, abroad, excluded) · payback forecast ≈ Dec 2026 → Jan 2027.
#   Programme "Cities 2028" from Mon 10 Jan 2028 (sponsor Femke): Ghent (open Mon 19 Jun 2028) and Haarlem (planned
#     Mon 4 Sep, moved to Mon 11 Sep 2028 on 17 Jul, Ana's new database), plus two shared projects: launch office and
#     the courier contract renewal. Board plan Mon 20 Mar 2028: eight cities, 60,000 orders a day by end 2028.
#   Nadia, second project manager, starts Mon 7 Feb 2028 (one of Marco's four central hires for 2028).

FND = ["governance"]

# ------------------------------------------------------------------ 01 How Light Can We Go?
tl_problem = Doodle(760, 260, "Doodle of Monday 27 September 2027. Eindhoven must open in eight weeks, on 22 November, while Antwerp is still three weeks from opening. Rotterdam's project file had fifty-eight pages and four standing meetings. Sanne can't run both launches that way, and Eindhoven is the fourth Dutch city: most of what Rotterdam had to invent is now known.",
                    "Eindhoven in eight weeks, Antwerp still open. Rotterdam's way: 58 pages, four standing meetings.", exact=True)
tl_problem.box(20, 24, 330, 140, None, "paper")
tl_problem.head(185, 60, "Rotterdam, 2026", size=19)
tl_problem.text(185, 94, "58 pages in the file", size=16)
tl_problem.text(185, 122, "4 standing meetings", size=16)
tl_problem.box(410, 24, 330, 140, None, "y")
tl_problem.head(575, 60, "Eindhoven, 2027", size=19)
tl_problem.text(575, 94, "8 weeks, 4th Dutch city", size=16)
tl_problem.text(575, 122, "Antwerp at the same time", size=16)
tl_problem.note(380, 210, "the first project's process, copied, would sink the fourth", "red", size=18)
tl_problem.note(380, 242, "most of what Rotterdam invented is now known", "pen", size=16)

tl_analogy = Doodle(760, 250, "Doodle of a cook making a family recipe for the fourth time. The first time she weighed everything, read every line and set three timers. Now she weighs only the flour and the salt, the two things that ruin it if wrong, and keeps one timer for the oven. Same dish, a quarter of the effort, because she knows where it goes wrong.",
                    "The fourth time: weigh only the flour and the salt, keep one timer. You know where it goes wrong.", exact=True)
tl_analogy.row([("1st time", "weigh all, 3 timers", "paper"), ("4th time", "flour + salt, 1 timer", "green")], y=40, h=96, gap=60, size=18, subsize=14, arrows=True)
tl_analogy.note(380, 196, "keep the checks where it goes wrong; drop the rest", "pen", size=18)

tl_how = Doodle(760, 470, "Eindhoven's tailoring sheet, 27 September 2027, one page in four parts. Keep in full: the gates, the risk register with Larder owners, the store IT line from week one, the go or no-go. Shorten: the charter to half a page, the plan to the playbook's timeline with dates filled in, status to five lines. Drop: the communications plan, the separate quality review, earned value, the Monday decision log. Meetings: one standing meeting, Thursday 09:30 for thirty minutes, and a written steering note every other Friday instead of a meeting. Review the fit at week four. Result: twenty file pages instead of fifty-eight, and Eindhoven opened on 22 November.",
                "One page: keep, shorten, drop, meetings, and a date to check the fit. 58 pages became 20; four meetings became one.", exact=True)
tl_how.box(14, 14, 236, 236, None, "green")
tl_how.head(132, 42, "keep in full", size=17)
for i, t in enumerate(["gates G1–G5", "risk register", "(Larder owners)", "store IT, week 1", "go / no-go"]):
    tl_how.text(132, 78 + i * 30, t, size=14)
tl_how.box(262, 14, 236, 236, None, "y")
tl_how.head(380, 42, "shorten", size=17)
for i, t in enumerate(["charter: ½ page", "plan: the playbook", "timeline, dated", "status: 5 lines", "budget: 1 table"]):
    tl_how.text(380, 78 + i * 30, t, size=14)
tl_how.box(510, 14, 236, 236, None, "pink")
tl_how.head(628, 42, "drop", size=17)
for i, t in enumerate(["communications plan", "separate quality review", "earned value", "Monday decision log", "(Ana's log is enough)"]):
    tl_how.text(628, 78 + i * 30, t, size=14)
tl_how.box(14, 266, 484, 120, None, "blue")
tl_how.head(256, 294, "meetings", size=17)
tl_how.text(256, 326, "one: Thursday 09:30, 30 minutes", size=14)
tl_how.text(256, 352, "steering: a written note every other Friday", size=14)
tl_how.box(510, 266, 236, 120, None, "paper")
tl_how.head(628, 294, "check the fit", size=17)
tl_how.text(628, 326, "week 4: Mon 25 Oct", size=14)
tl_how.text(628, 352, "what's missing? unused?", size=14)
tl_how.row([("58 → 20 pages", "", "y"), ("4 → 1 meeting", "", "y"), ("opened 22 Nov", "8 weeks", "green")], y=402, h=56, size=16, subsize=12)

tl_deep1 = Doodle(760, 300, "Five dials Sanne set for Eindhoven, each from light to heavy, with a dot where Eindhoven sat and a ring where Rotterdam sat. Novelty: Eindhoven light, the fourth Dutch city; Rotterdam heavy. Size and money: both middle. Regulation: Eindhoven light, a standard Dutch store; Antwerp would be heavy. Team: Eindhoven light, a team that had done it three times. Cost of a slip: both middle. Process follows the dials.",
                  "Five dials, set before choosing any process. Eindhoven (dot) is lighter than Rotterdam (ring) on three of them.", exact=True)
dials = [("novelty", 1, 4), ("size, money", 2, 2), ("regulation", 1, 2), ("team experience", 1, 3), ("cost of a slip", 2, 3)]
for i, (name, e, r) in enumerate(dials):
    y = 30 + i * 52
    tl_deep1.text(16, y + 6, name, anchor="start", size=15)
    tl_deep1.line(f"M200 {y} H700", thin=True)
    for k in range(5):
        tl_deep1.line(f"M{200 + k * 125} {y - 8} V{y + 8}", thin=True)
    tl_deep1.raw(f'<circle class="d f-pink" cx="{200 + r * 125}" cy="{y}" r="11"/>')
    tl_deep1.raw(f'<circle class="d f-green" cx="{200 + e * 125}" cy="{y}" r="7"/>')
tl_deep1.text(200, 292, "light", size=14)
tl_deep1.text(700, 292, "heavy", size=14)
tl_deep1.note(450, 292, "● Eindhoven   ◯ Rotterdam", "pen", size=14)

TAILOR_WHOLE = dict(
    slug="tailoring-a-whole-project",
    kicker="a.k.a. “tailoring a whole project”: choosing and sizing the whole method for one project",
    tldr="Vol. 1 tailored one process at a time. <b>Tailoring a whole project</b> means setting the method for all of it, on one page, before it starts: what to <b>keep in full</b> (the parts where this project can go wrong), what to <b>shorten</b>, what to <b>drop</b>, which meetings to hold, and a date to <b>check the fit</b>. Set it from a few dials (novelty, size, regulation, the team's experience, the cost of a slip), not from the last project's habits. The fourth time you do something, most of the first time's process is waste; the checks where it went wrong are not.",
    chips=[("Family", "fitting it to the work"), ("Lives in", "one page at the front of the project file"), ("Pairs with", "tailoring (vol. 1), the playbook, the risk register")],
    pmbok=dict(covers="tailoring the whole approach to one project: choosing which processes, artefacts and meetings to use and how far, and reviewing the fit",
               domains=FND, processes=[], principles=["Focus on value", "Build an empowered culture"], focus=["initiating", "planning"],
               older="6th: “tailoring considerations” in each knowledge area. 7th: a tailoring chapter with a four-step process. 8th: tailoring built into every domain."),
    problem_side="Larder, Monday 27 September 2027",
    problem="""  <p class="lead">Eindhoven must open on <b>Monday 22 November</b>, eight weeks away. Antwerp, the launch that slipped, is still three weeks from its own opening, and Sanne runs both. Rotterdam's project file had <b>58 pages</b> and the launch had <b>four standing meetings</b>. <span class="hl-pink">Copy that, and Sanne spends Eindhoven's eight weeks writing documents.</span> But Eindhoven is the fourth Dutch city. Most of what Rotterdam had to invent (the workstreams, the gates, the money rules, the people sums) now exists in the playbook.</p>
  <ul>
    <li>The first project's process is the default, because it's there.</li>
    <li>Dropping things feels like cutting corners.</li>
    <li>Nobody has said which checks still matter.</li>
  </ul>""",
    problem_figs=[tl_problem],
    meanwhile=[("architect-6", "just-enough-design", "Ana's just-enough up-front design: decide early only what is hard to change later, and leave the rest.",
                "Sanne's tailoring sheet does the same for process: keep the checks where a launch goes wrong, drop the paperwork that was there to learn.")],
    analogy_side="the fourth time a recipe is cooked",
    analogy="""  <p>The first time a cook makes a family recipe she <b>weighs everything</b>, reads every line, sets three timers. By the fourth time she weighs only the <b>flour and the salt</b>, the two things that ruin the dish if they're wrong, and keeps <b>one timer</b>, for the oven. Same dish, a quarter of the effort. She didn't get careless. She learned where it goes wrong.</p>""",
    analogy_figs=[tl_analogy],
    map=[("Weighing everything the first time", "Rotterdam's 58 pages and four meetings"),
         ("The flour and the salt", "Gates, the risk register, store IT from week one, go / no-go"),
         ("One timer for the oven", "One meeting, Thursday 09:30"),
         ("Reading every line", "A communications plan, earned value, a separate quality review"),
         ("Knowing where it goes wrong", "The lessons of Rotterdam and Antwerp")],
    how_side="one page: keep, shorten, drop, meetings, check the fit",
    how="""  <p>Sanne writes Eindhoven's <b>tailoring sheet</b> on one page. <b>Keep in full</b>: the five gates, the risk register with a Larder owner on every row (Antwerp's lesson), the store IT line from week one (Rotterdam's), the go / no-go. <b>Shorten</b>: the charter to half a page, the plan to the playbook's timeline with Eindhoven's dates filled in, status to five lines, the budget to one table. <b>Drop</b>: the communications plan (one language, people who know each other), the separate quality review, earned value, the Monday decision log (Ana's log is enough). <b>Meetings</b>: one standing meeting, Thursday 09:30 for thirty minutes; the steering group gets a written note every other Friday instead of a meeting. <b>Check the fit</b> at week four, Monday 25 October: Joost asks to put one thing back, a ten-minute call on the Friday before go / no-go, and nothing else is missed. The file ends at <b>20 pages</b>; Eindhoven opens on <b>22 November</b>, eight weeks from the sheet.</p>""",
    how_figs=[tl_how],
    steps=[("Set the dials first", "Novelty, size, regulation, team experience, cost of a slip."),
           ("Keep in full what has gone wrong before", "The checks that caught real problems."),
           ("Shorten what still helps", "Half a page is still a charter."),
           ("Drop what was there to learn", "Say why, in one line each."),
           ("Choose the fewest meetings that work", "Written notes where talk adds nothing."),
           ("Check the fit on a date", "Put back only what was missed.")],
    vocab=[("Tailoring", "Choosing and sizing the processes, artefacts and meetings for one project."),
           ("Tailoring sheet", "One page that says what is kept, shortened and dropped, and why."),
           ("Method", "The set of ways of working a project uses."),
           ("Overhead", "Effort spent on running the project rather than doing it."),
           ("Fit review", "A planned check of whether the tailoring is working."),
           ("Dial", "A property of the project (novelty, regulation…) that pushes process lighter or heavier.")],
    code=dict(file="programme/01-tailoring-sheet.md", note="Sanne, Eindhoven, Monday 27 September 2027", plain=True, src="""
# EINDHOVEN · HOW WE'LL RUN IT (tailoring sheet)                    27 Sep 2027

DIALS      novelty low (4th Dutch city) · size/money medium (€360k) · regulation low ·
           team experience high (3 launches) · cost of a slip medium (≈ €17k a week)
KEEP       gates G1–G5 · risk register, every owner at Larder · store IT from week 1 ·
           go / no-go with the steering group
SHORTEN    charter → ½ page · plan → playbook v3 timeline, dated · status → 5 lines ·
           budget → 1 table (5 lines + contingency)
DROP       communications plan (one language, known people) · separate quality review
           (the gates check quality) · earned value (fixed-price builder, 8 weeks) ·
           Monday decision log (Ana's log covers it)
MEETINGS   Thu 09:30, 30 min, leads · steering: written note every other Friday
CHECK FIT  Mon 25 Oct (week 4) → put back: a 10-minute call on the Friday before go/no-go
RESULT     20 file pages (Rotterdam 58) · opened Mon 22 Nov 2027, 8 weeks from this sheet
"""),
    tools="tools: the playbook, five dials, a one-page sheet, and a date four weeks out to check it.",
    deep_dive=dict(
        side="the dials, what can't be dropped, tailoring down and up, and checking the fit",
        intro="Vol. 1 introduced tailoring as four steps applied to processes one at a time. After six launches Sanne tailors a whole project in an afternoon. This chapter shows the dials she sets first, the few things that never get tailored away, why tailoring sometimes means adding process, and how to check the fit without arguing about it.",
        parts=[
            ("Set the dials before choosing anything", """  <p>Process should follow the project, so describe the project first. Sanne uses five dials, each from light to heavy:</p>
  <ul>
    <li><b>Novelty</b>: done this before, here? Eindhoven light; Antwerp heavy.</li>
    <li><b>Size and money</b>: how much is at stake?</li>
    <li><b>Regulation</b>: permits, inspections, contracts with teeth? Antwerp's permit made it heavy.</li>
    <li><b>Team experience</b>: has this team done it together?</li>
    <li><b>Cost of a slip</b>: what a week late costs (≈ €17k for a city, since playbook v3).</li>
  </ul>
  <p>Each dial pushes a different part: novelty and regulation push risk and stakeholder work, size pushes money control, team experience pushes planning detail, cost of a slip pushes schedule control.</p>""", [tl_deep1]),
            ("What never gets tailored away", """  <p>Some things are cheap and catch disasters, so they stay however light the project: <b>a sponsor who decides</b>; <b>a written “done means”</b>; <b>a risk list with owners inside the organisation</b>; <b>a go / no-go</b> before anything irreversible; <b>a status the sponsor can trust</b>. Everything else is a choice. Eindhoven's twenty pages included all five.</p>""", []),
            ("Tailoring can mean adding", """  <p>Tailoring isn't a diet. Antwerp, tailored honestly, needed <b>more</b> than Rotterdam: a stakeholder register of thirty-one, a communications plan in three languages, a simulation. The mistake there was tailoring by habit (Rotterdam's light touch on permits), not tailoring too much. Turn every dial, and let some of them say “heavier”.</p>""", []),
            ("Checking the fit without an argument", """  <p>Set the review date when you write the sheet, and ask two questions only: <b>what did we miss</b> because we dropped it, and <b>what did we keep that nobody used</b>? Put back only what was actually missed. At Eindhoven's week-four check Joost missed one thing, a short call before go / no-go, and nobody missed the communications plan. Record both answers in the playbook, so the next sheet starts from evidence.</p>""", []),
        ]),
    dial=[("Light", "a small internal change", ["Three lines: keep, drop, meet.", "No dials.", "Check at the end."]),
          ("Standard", "Eindhoven", ["One page from five dials.", "Keep, shorten, drop, meetings.", "Fit checked at week four."]),
          ("Heavy", "regulated or first-of-a-kind", ["A tailoring record with reasons.", "Approved by governance.", "Reviewed at every gate."])],
    baseline="Each line compares <b>Rotterdam's full method, copied</b> to <b>one tailoring page set from five dials, with a fit check</b>.",
    ratings=[(3, 5, "Effort goes to the launch, not the file."),
             (3, 4, "The checks that matter are kept in full."),
             (3, 4, "Where launches go wrong is still covered."),
             (3, 4, "One page says how the project runs."),
             (3, 4, "Steering notes are read; meetings were skipped."),
             (3, 4, "The team spends its time on the work."),
             (3, 4, "The fit check puts things back."),
             (3, 3, "Neutral."),
             (2, 5, "20 pages and one meeting.")],
    pitfalls=[("Copying the first project", "Its learning costs, again.", "set the dials for this one."),
              ("Cutting the cheap safety checks", "Small saving, big risk.", "keep the five that never go."),
              ("Tailoring only down", "Some projects need more.", "let dials say heavier."),
              ("No fit check", "Gaps found at go / no-go.", "set the date when you write the sheet.")],
    use=["At the start of every project.", "When a project is a repeat of earlier ones.", "When a project is new in a way the last wasn't.", "At each gate, briefly."],
    skip=["Never; on tiny work it's three lines."],
    related=["<b>How Much Process Do We Need?</b> (vol. 1)", "<b>Can a Launch Be a Recipe?</b> (next note)", "<b>Just-Enough Up-Front Design</b> (Ana, vol. 6)", "<b>Different Country, Different Rules</b> (vol. 5)"],
    quiz=[("Name Sanne's five dials.", "Novelty, size and money, regulation, team experience, cost of a slip."),
          ("What did Eindhoven keep in full?", "Gates, the risk register with Larder owners, store IT from week one, go / no-go."),
          ("What did the week-four check put back?", "A ten-minute call on the Friday before go / no-go."),
          ("Ghent is a second Belgian city. Which dials move compared with Eindhoven?", "Regulation and novelty go up (Belgian permit, a new city abroad); keep the stakeholder and permit work Antwerp needed."),
          ("A lead says dropping earned value is unprofessional. Answer them.", "It's dropped on purpose for a fixed-price, eight-week job; the gates and status cover the risk; the sheet says why.")],
    try_it="Write your project's tailoring sheet on one page: dials, keep, shorten, drop, meetings, and a fit-check date. Ask one colleague what they'd put back.",
    remember="The fourth time, weigh the <span class=\"hl\">flour and the salt</span>. Keep one <span class=\"hl\">timer</span>.",
    sources=["Project Management Institute, <i>PMBOK Guide</i>, Eighth Edition (2025): tailoring.",
             "Project Management Institute, <i>PMBOK Guide</i>, Seventh Edition (2021): section 3, Tailoring.",
             "Alistair Cockburn, “Methodology per project” (2000)."],
)

# ------------------------------------------------------------------ 02 Can a Launch Be a Recipe?
pb_problem = Doodle(760, 260, "Doodle of December 2027. Six cities are open. Each launch taught something, and the lessons sit in four places: Grace's playbook for the app, Sanne's lessons pages, the project file, and people's heads. Ghent and Haarlem are next in 2028, and a new project manager will run them. Which version of 'how we launch a city' will she use?",
                    "Six launches, lessons in four places. A new PM will run 2028. Which “how we launch” will she use?", exact=True)
pb_problem.row([("Grace's playbook", "the apps", "y"), ("lessons pages", "41 lines a launch", "paper"), ("project file", "73 pages", "paper"), ("people's heads", "Sanne, Joost, Yara", "pink")], y=24, h=96, size=16, subsize=13)
pb_problem.note(380, 170, "a recipe only exists if someone else can cook from it", "red", size=18)
pb_problem.note(380, 206, "the new project manager starts in February", "pen", size=16)

pb_analogy = Doodle(760, 250, "Doodle of a restaurant chain's recipe card. The card fixes what makes the dish the dish: the sauce, the weights, the cooking time. It leaves room for what each kitchen must decide: the local supplier of tomatoes, the plate. Each time a kitchen finds a better way, the head chef changes the card and dates it.",
                    "A chain's recipe card: fixed where it matters, local where it must be, dated each time it changes.", exact=True)
pb_analogy.box(14, 40, 350, 110, "fixed on the card", "green", sub="sauce, weights, timing", size=18, subsize=14)
pb_analogy.box(396, 40, 350, 110, "each kitchen decides", "y", sub="local tomatoes, the plate", size=18, subsize=14)
pb_analogy.note(380, 200, "v4 · changed after the last kitchen found a better way", "pen", size=17)

pb_how = Doodle(760, 470, "The city launch playbook, version by version. Version 1, Utrecht, April 2027: the eight workstreams, five milestones, the people sums, the money rules; a city in eight weeks. Version 2, The Hague, June 2027: a city is configuration, not code; launch on the new warehouse system. Version 3, Antwerp, October 2027: regulators are stakeholders; score risks with locals; every response has a Larder owner; the price of a week late. Version 4, Eindhoven, December 2027: the tailoring sheet; the launch kit of eighteen templates; the benefits check at plus four and plus twelve weeks with a named owner. Each version: what is fixed, what is local, and what changed.",
                "v1 → v4: each launch changed the recipe. v4 adds the tailoring sheet, the 18-template kit and owned benefit checks.", exact=True)
vers = [("v1 Utrecht", "Apr 2027", ["8 workstreams, 5 milestones", "people + money sums", "a city in 8 weeks"], "paper"),
        ("v2 The Hague", "Jun 2027", ["a city = configuration", "launch on WMS B", "five daily numbers"], "blue"),
        ("v3 Antwerp", "Oct 2027", ["regulators = stakeholders", "risks scored by locals", "Larder owner per response"], "y"),
        ("v4 Eindhoven", "Dec 2027", ["tailoring sheet", "launch kit: 18 templates", "benefit checks, owned"], "green")]
for i, (h, d, items, f) in enumerate(vers):
    x = 14 + i * 186
    pb_how.box(x, 20, 174, 250, None, f)
    pb_how.head(x + 87, 50, h, size=16)
    pb_how.text(x + 87, 74, d, size=13)
    for k, t in enumerate(items):
        pb_how.text(x + 87, 120 + k * 44, t, size=12)
    if i:
        pb_how.arrow(x - 10, 145, x - 2, 145)
pb_how.box(14, 290, 360, 166, None, "green")
pb_how.head(194, 318, "fixed in every city", size=17)
for i, t in enumerate(["gates G1–G5, go / no-go", "store IT in week 1", "risk owners at Larder", "benefit checks +4, +12 wks"]):
    pb_how.text(194, 350 + i * 26, t, size=14)
pb_how.box(386, 290, 360, 166, None, "y")
pb_how.head(566, 318, "decided locally", size=17)
for i, t in enumerate(["the site and the builder", "local rules and permits", "zones, opening hours", "who's on the team"]):
    pb_how.text(566, 350 + i * 26, t, size=14)

pb_deep1 = Doodle(760, 280, "How a lesson becomes a playbook line, in four steps, with the Antwerp permit as the example. A lesson from the closing report: the permit risk was scored by people who knew Rotterdam. A pattern: did it happen in more than one launch? Rotterdam's internet line was the same kind: a local rule nobody in the room knew. A playbook change: risks are scored with someone who has done it in that country. A check: Ghent's register, January 2028, scored by Maarten and Hilde. Lessons that fail any step stay on the lessons page.",
                  "Lesson → pattern → playbook line → checked on the next launch. The rest stays on the lessons page.", exact=True)
pb_deep1.row([("lesson", "permit scored by Rotterdam people", "paper"), ("pattern", "internet line: same kind", "y"), ("playbook line", "score risks with locals", "green"), ("checked", "Ghent register, Jan 2028", "blue")], y=24, h=110, gap=34, size=16, subsize=11, arrows=True)
pb_deep1.note(380, 186, "41 lessons from Rotterdam → 12 playbook changes; Antwerp 33 → 4", "pen", size=16)
pb_deep1.note(380, 226, "a playbook that only grows is a manual nobody reads", "red", size=16)

PLAYBOOK = dict(
    slug="city-launch-playbook",
    kicker="a.k.a. “the city launch playbook”: turning repeated projects into a method",
    tldr="When a kind of project repeats, write down how it's done in a <b>playbook</b>: what is <b>fixed</b> in every instance (the parts that make it work, and the checks where it went wrong), what is <b>decided locally</b>, the templates, and the timeline. <b>Version</b> it: after each project, turn lessons that held in more than one place into changes, and <b>remove</b> what nobody used. A playbook is only real when someone who didn't write it can run a launch from it.",
    chips=[("Family", "fitting it to the work"), ("Lives in", "one versioned document plus a kit of templates"), ("Pairs with", "lessons learned, tailoring a whole project, the PMO")],
    pmbok=dict(covers="capturing a repeatable way of delivering a kind of project (models, methods and artefacts chosen and proven), and improving it after each project",
               domains=FND, processes=["Manage Project Knowledge"], principles=["Focus on value", "Embed quality into processes and deliverables"], focus=["closing", "planning"],
               older="6th: organisational process assets and Manage Project Knowledge (4.4). 7th: models, methods and artifacts; tailoring."),
    problem_side="Larder, December 2027",
    problem="""  <p class="lead">Six cities are open. Each launch taught something, and the lessons are in <b>four places</b>: Grace's playbook (the apps), Sanne's lessons pages, the project file, and people's heads, mostly Sanne's, Joost's and Yara's. Ghent and Haarlem open in 2028, and a <b>second project manager</b> will run them, starting in February. <span class="hl-pink">Asked “how do we launch a city?”, three people would give three answers, all partly right.</span></p>
  <ul>
    <li>Lessons were captured, but in different places.</li>
    <li>Nothing says which parts are fixed and which are local.</li>
    <li>Old advice was never removed, so the documents only grew.</li>
  </ul>""",
    problem_figs=[pb_problem],
    meanwhile=[("product-6", "launching-new-city", "Grace's city playbook for the product side: configuration vs local, a launch rhythm, five daily numbers; v1 Utrecht, v2 The Hague, v3 after Antwerp.",
                "Sanne and Grace merge their two playbooks into one in December: v4 has a product chapter and a project chapter, one timeline, one owner each.")],
    analogy_side="the chain's recipe card",
    analogy="""  <p>A restaurant chain's recipe card <b>fixes</b> what makes the dish the dish: the sauce, the weights, the cooking time. It leaves room for what each kitchen must <b>decide</b>: the local supplier of tomatoes, the plate. When a kitchen finds a better way, the head chef <b>changes the card and dates it</b>, and takes off the line nobody follows any more. A card that only grows becomes a book nobody reads during service.</p>""",
    analogy_figs=[pb_analogy],
    map=[("The sauce and the weights", "Gates, store IT in week one, risk owners at Larder, benefit checks"),
         ("The local tomatoes", "The site, local rules, zones, the team"),
         ("A dated card", "Playbook v1 → v4"),
         ("A kitchen's better way", "A lesson that held in more than one launch"),
         ("A line taken off", "Rules from Rotterdam nobody used again")],
    how_side="one versioned playbook: fixed, local, kit, changes",
    how="""  <p>On <b>Monday 13 December 2027</b> Sanne and Grace merge their two documents into <b>playbook v4</b>: one timeline, a product chapter and a project chapter, each with one owner. Each version has changed the recipe. <b>v1</b> (Utrecht, April 2027) fixed the eight workstreams, the five milestones and the people and money sums: a city in eight weeks. <b>v2</b> (The Hague, June) made a city configuration, not code. <b>v3</b> (Antwerp, October) added Antwerp's four lines. <b>v4</b> (after Eindhoven) adds the <b>tailoring sheet</b>, the <b>launch kit</b> of 18 templates from the artefact review, and <b>benefit checks</b> at +4 and +12 weeks with a named owner (see “Did we get what we paid for?”). Two sections are fixed in every city and decided locally, and every page says which. v4 is also 11 pages <b>shorter</b> than v3 with Grace's added: lines nobody had used in two launches were taken out. The test comes in February: Nadia, the new project manager, plans Ghent from it in her second week, and her questions become v4.1.</p>""",
    how_figs=[pb_how],
    steps=[("Gather the lessons from every launch", "And the lessons pages, and people's heads."),
           ("Keep what held in more than one place", "One-off lessons stay on the lessons page."),
           ("Mark each part fixed or local", "On the page itself."),
           ("Attach the kit", "The templates that were actually used."),
           ("Take out what nobody used", "Date every version."),
           ("Test it on someone who didn't write it", "Their questions are the next version.")],
    vocab=[("Playbook", "A written, versioned way of delivering a kind of project."),
           ("Organisational process assets", "Templates, lessons and methods an organisation keeps and reuses."),
           ("Knowledge management", "Making what people learned available to those who need it next."),
           ("Explicit knowledge", "Knowledge that can be written down."),
           ("Tacit knowledge", "Know-how that lives in people; shared by working together."),
           ("Template kit", "The small set of templates a playbook says to use.")],
    code=dict(file="programme/02-playbook-v4.md", note="Sanne and Grace, Monday 13 December 2027 (contents page)", plain=True, src="""
# CITY LAUNCH PLAYBOOK · v4                                 13 Dec 2027 · owners: Sanne, Grace

HISTORY   v1 Utrecht (Apr 2027) · v2 The Hague (Jun) · v3 Antwerp (Oct) · v4 Eindhoven (Dec)
          v4 is 11 pages shorter than v3 + Grace's: lines unused in 2 launches removed
1 TAILORING SHEET            five dials · keep / shorten / drop · fit check at week 4
2 TIMELINE                   8 weeks (NL) · plan for 12+ abroad, permits first
3 FIXED IN EVERY CITY        gates G1–G5 · go / no-go · store IT in week 1 · every risk
                             and response owned at Larder · benefit checks +4 and +12 weeks
4 DECIDED LOCALLY            site, builder · local rules and permits (with a local expert) ·
                             zones and hours · the team
5 PRODUCT CHAPTER (Grace)    configuration vs local · five daily numbers · languages
6 PROJECT CHAPTER (Sanne)    money rules · people from demand · price of a week late (≈ €17k)
7 LAUNCH KIT                 18 templates (see the artefact review of 6 Dec)
CHANGES   send to Sanne · reviewed after every launch · v4.1 after Nadia plans Ghent (Feb)
"""),
    tools="tools: every launch's lessons, one versioned document, the template kit, and a reader who didn't write it.",
    deep_dive=dict(
        side="what goes in, how lessons become lines, fixed vs local, and keeping it short",
        intro="Most playbooks fail in one of two ways: nobody writes them, or nobody can read them. Larder's went through four versions in nine months. This chapter shows what a playbook needs, how a lesson earns a line, how to decide fixed and local, and the habit that kept v4 shorter than v3.",
        parts=[
            ("What a playbook needs", """  <ul>
    <li>A <b>timeline</b> with milestones and gates, in weeks from the start.</li>
    <li>What's <b>fixed</b> in every instance, and why (each fixed line points to the launch that taught it).</li>
    <li>What's <b>decided locally</b>, and who decides.</li>
    <li>A <b>tailoring sheet</b> to fill in first.</li>
    <li>A <b>kit</b>: the templates, already shortened.</li>
    <li>A <b>version history</b> and an owner.</li>
  </ul>
  <p>What it doesn't need: everything that was ever written about launches. That's what the lessons pages are for.</p>""", []),
            ("How a lesson earns a line", """  <p>A lesson goes into the playbook only after four steps: it's written in a closing report; it's a <b>pattern</b> (it happened, or nearly happened, in more than one launch); it becomes a <b>specific line</b>; and it's <b>checked</b> on the next launch. Rotterdam's 41 lessons gave 12 changes; Antwerp's 33 gave only 4, because most were already covered or one-off.</p>""", [pb_deep1]),
            ("Fixed or local?", """  <p>Make a part <b>fixed</b> when getting it wrong was expensive and the right answer is the same everywhere: gates, store IT in week one, owned risks. Make it <b>local</b> when the right answer depends on the place: the builder, the permit route, the zones. When in doubt, fix the <b>question</b> and leave the answer local: “list every permit with a local expert” is fixed; which permits is local.</p>""", []),
            ("Keeping it short", """  <p>Every review asks one more question than “what should we add?”: <b>what didn't anyone use?</b> A line unused in two launches comes out, into the history. v4 lost eleven pages that way. The test of length is simple: Nadia read v4 in an afternoon and planned Ghent in her second week. A playbook that takes a week to read gets skimmed, and then it's back in people's heads.</p>""", []),
        ]),
    dial=[("Light", "a task repeated twice", ["A checklist.", "Updated when it fails.", "One owner."]),
          ("Standard", "city launches", ["A versioned playbook: fixed, local, kit.", "Changed after every launch.", "Tested on a new reader."]),
          ("Heavy", "franchises, regulated roll-outs", ["A controlled method with change approval.", "Training and certification on it.", "Audits of use."])],
    baseline="Each line compares <b>lessons in four places and people's heads</b> to <b>one versioned playbook with fixed and local parts, a kit, and changes after every launch</b>.",
    ratings=[(3, 5, "Each launch starts from the last one's learning."),
             (3, 5, "Dutch launches in eight weeks, three times."),
             (2, 4, "Old failures are fixed lines."),
             (2, 4, "One place says how a launch runs."),
             (3, 4, "The board sees a repeatable method."),
             (3, 4, "Nadia plans from it in week two."),
             (3, 4, "Local parts are marked as local."),
             (3, 4, "Quality checks are in the recipe."),
             (3, 4, "Shorter with each version.")],
    pitfalls=[("Never written", "It leaves with the people.", "write it after the second launch."),
              ("Only grows", "Nobody reads it.", "remove what nobody used."),
              ("All fixed", "Local sense is overruled.", "mark fixed and local."),
              ("Tested by its author", "Gaps stay invisible.", "test it on a new reader.")],
    use=["When a kind of project repeats.", "Before a new person runs one.", "After every instance.", "When lessons are in many places."],
    skip=["One-off projects: keep the lessons page instead."],
    related=["<b>What Did We Learn?</b> (vol. 2)", "<b>How Light Can We Go?</b> (previous note)", "<b>Launching a New City</b> (Grace, vol. 6)", "<b>Golden Paths</b> (Ana, vol. 6)"],
    quiz=[("What does every version of the playbook say about each part?", "Whether it's fixed in every city or decided locally."),
          ("Name two things v4 added.", "The tailoring sheet; the 18-template launch kit; benefit checks with a named owner."),
          ("Why was v4 shorter than v3?", "Lines unused in two launches were taken out."),
          ("A lesson from Haarlem says “Fridays are bad for deliveries.” Into the playbook?", "Not yet: check whether it's a pattern elsewhere; until then it stays on the lessons page."),
          ("How was v4 tested?", "Nadia, who didn't write it, planned Ghent from it; her questions became v4.1.")],
    try_it="If your team repeats a kind of project, write its playbook's contents page: timeline, fixed, local, kit. Mark one line you'd remove because nobody used it.",
    remember="Fix the <span class=\"hl\">sauce</span>. Let the kitchen choose the <span class=\"hl\">tomatoes</span>. Date the card.",
    sources=["Project Management Institute, <i>PMBOK Guide</i>, Eighth Edition (2025): models, methods and artifacts; knowledge management.",
             "Project Management Institute, <i>PMBOK Guide</i>, Sixth Edition (2017): 4.4 Manage Project Knowledge.",
             "Atul Gawande, <i>The Checklist Manifesto</i> (2009)."],
)

# ------------------------------------------------------------------ 03 One Project, or Many?
pg_problem = Doodle(760, 260, "Doodle of January 2028. Five things on Sanne's desk at once: Ghent, Haarlem, a launch office, the courier contract renewal, and Ana's station lockers pilot asking for store space. Each has its own plan and its own status. They share people, money and the same date: eight cities by the end of 2028. Run separately, they will collide.",
                    "Five pieces of work, five plans, one goal: eight cities by the end of 2028. Run apart, they collide.", exact=True)
pg_problem.row([("Ghent", "Jun", "y"), ("Haarlem", "Sep", "y"), ("launch office", "Feb", "paper"), ("couriers", "renewal", "paper"), ("lockers", "Ana's pilot", "paper")], y=24, h=84, size=16, subsize=13, gap=10)
pg_problem.note(380, 156, "shared people: Joost's ops lead, Eli, Lena", "pen", size=17)
pg_problem.note(380, 194, "shared goal: eight cities, 60,000 orders a day", "pen", size=17)
pg_problem.note(380, 232, "nobody looks at them together", "red", size=18)

pg_analogy = Doodle(760, 250, "Doodle of a wedding weekend. One wedding is a project. The whole weekend, with the rehearsal dinner, the ceremony, the party and the Sunday brunch, run by one planner so the guests get one good weekend, is a programme. The family's budget for the whole year, choosing between the wedding, a new car and the roof, is a portfolio.",
                    "One wedding is a project; the whole weekend is a programme; the family's year of spending is a portfolio.", exact=True)
pg_analogy.box(14, 130, 230, 90, "project", "y", sub="the ceremony", size=18, subsize=13)
pg_analogy.box(264, 80, 230, 140, "programme", "blue", sub="the whole weekend", size=18, subsize=13)
pg_analogy.box(514, 30, 232, 190, "portfolio", "green", sub="the year's spending", size=18, subsize=13)

pg_how = Doodle(760, 470, "Larder in three layers, January 2028. Portfolio: Femke's quarterly sheet of everything Larder invests in, choosing what to fund: cities, the new ordering database, Larder Plus, the lockers. Programme: Cities 2028, Sanne as programme manager, sponsor Femke, run for one benefit: eight cities and sixty thousand orders a day by end 2028. Inside it, four projects: Ghent, opening 19 June; Haarlem, 4 September; the launch office; the courier contract renewal. The lockers pilot stays outside the programme, as Ana's project, with one dependency. A programme board every four weeks; one roadmap; one risk list for what crosses projects.",
                "Portfolio chooses what to fund; the programme makes four projects deliver one benefit; projects deliver.", exact=True)
pg_how.box(14, 14, 732, 100, None, "green")
pg_how.head(380, 42, "portfolio: Femke's quarterly sheet", size=17)
pg_how.text(380, 72, "cities · ordering database · Larder Plus · lockers · business portal", size=14)
pg_how.text(380, 96, "decides what gets funded, and in what order", size=13)
pg_how.box(14, 130, 732, 250, None, "blue")
pg_how.head(380, 158, "programme: Cities 2028 (Sanne; sponsor Femke)", size=17)
pg_how.text(380, 184, "benefit: eight cities, 60,000 orders a day by end 2028", size=14)
pg_how.row([("Ghent", "open 19 Jun", "y"), ("Haarlem", "open 4 Sep", "y"), ("launch office", "from Feb", "paper"), ("courier renewal", "by May", "paper")], x=30, y=204, h=80, w=165, gap=12, size=16, subsize=13)
pg_how.text(380, 316, "one roadmap · one risk list for what crosses projects", size=14)
pg_how.text(380, 342, "a programme board every four weeks · shared people booked here", size=14)
pg_how.box(14, 396, 360, 62, "lockers pilot", "paper", sub="Ana's project: one dependency", size=16, subsize=12, dash=True)
pg_how.box(386, 396, 360, 62, "projects deliver", "y", sub="each with its own plan", size=16, subsize=12)

PROGRAMME = dict(
    slug="programmes-and-portfolios",
    kicker="a.k.a. projects, programmes and portfolios",
    tldr="A <b>project</b> delivers a result. A <b>programme</b> runs related projects together for a <b>benefit</b> none of them gives alone: one roadmap, one place where shared people and shared risks are managed, one board. A <b>portfolio</b> is everything the organisation invests in, managed to choose <b>what</b> gets funded and in what order. When several projects share people, money and a goal, run them as a programme; when they only share a budget, a portfolio view is enough.",
    chips=[("Family", "fitting it to the work"), ("Lives in", "a programme roadmap, a shared risk list, a board every four weeks"), ("Pairs with", "the value delivery system, the PMO, governance")],
    pmbok=dict(covers="how projects relate to programmes and portfolios, when to group projects into a programme, and how each layer is governed",
               domains=FND, processes=[], principles=["Adopt a holistic view", "Focus on value"], focus=["initiating", "monitoring and controlling"],
               older="6th: section 1.2.3.1, projects, programmes and portfolios. 7th: the system for value delivery. PMI's separate standards for programme and portfolio management."),
    problem_side="Larder, January 2028",
    problem="""  <p class="lead">Five pieces of work land on Sanne's desk in the same week: <b>Ghent</b> (Belgium again, June), <b>Haarlem</b> (September), a <b>launch office</b> to set up, the <b>courier contract renewal</b>, and Ana's <b>station lockers pilot</b> asking for space in the stores. Each has its own plan and its own status. <span class="hl-pink">They share Joost's operations lead, Eli and Lena, the same budget year, and the same promise: eight cities by the end of 2028.</span> Run separately, they'll book the same people for the same weeks, and nobody will be watching the promise.</p>
  <ul>
    <li>Five plans, no view of all of them.</li>
    <li>Shared people are booked twice.</li>
    <li>The benefit (eight cities, 60,000 orders a day) belongs to none of them.</li>
  </ul>""",
    problem_figs=[pg_problem],
    analogy_side="the wedding weekend",
    analogy="""  <p>One <b>wedding ceremony</b> is a project. The <b>whole weekend</b>, rehearsal dinner, ceremony, party, Sunday brunch, run by one planner so the guests get one good weekend, is a programme: the pieces share guests, caterers and a goal. The family's <b>spending for the whole year</b>, choosing between the wedding, a new car and the roof, is a portfolio. Different questions, different people asking them.</p>""",
    analogy_figs=[pg_analogy],
    map=[("The ceremony", "Ghent's launch: a project"),
         ("The whole weekend", "Cities 2028: Ghent, Haarlem, launch office, courier renewal"),
         ("Shared guests and caterers", "Joost's ops lead, Eli, Lena"),
         ("One good weekend", "Eight cities, 60,000 orders a day"),
         ("The family's year", "Femke's portfolio sheet")],
    how_side="three layers, one benefit, one board",
    how="""  <p>On <b>Monday 10 January 2028</b> Femke makes <b>Cities 2028</b> a programme, with Sanne as programme manager. Its <b>benefit</b> is the board's: eight cities and 60,000 orders a day by the end of 2028 (confirmed in the board plan of 20 March). Four projects sit inside it: Ghent, Haarlem, the launch office and the courier renewal. The lockers pilot stays <b>outside</b>, as Ana's project with one recorded dependency (store space), because it serves a different benefit. The programme adds three things the projects can't give themselves: one <b>roadmap</b> with every project's milestones; one <b>risk list</b> for what crosses projects (shared people, Belgian permits, the builder used in both cities); and a <b>programme board</b> every four weeks that books shared people and moves money between projects within the programme's total. Above it, Femke's quarterly sheet becomes a real <b>portfolio</b> review: cities against the ordering database, Larder Plus and the business portal, ranked for funding.</p>""",
    how_figs=[pg_how],
    steps=[("Ask what benefit the projects share", "If none, they're a portfolio, not a programme."),
           ("Group the ones that serve it", "Leave the rest outside, with dependencies."),
           ("One roadmap", "Every project's milestones together."),
           ("One list of cross-project risks", "And one booking of shared people."),
           ("A programme board on a rhythm", "It can move money and people within the total."),
           ("Report the benefit, not only the projects", "Cities open, orders a day.")],
    vocab=[("Project", "Temporary work to deliver a result."),
           ("Programme", "Related projects managed together for benefits none gives alone."),
           ("Portfolio", "All the organisation's investments, managed to choose and balance them."),
           ("Programme roadmap", "One timeline of all the programme's projects and benefits."),
           ("Dependency", "Something one piece of work needs from another."),
           ("Benefit", "The measurable improvement the work exists for.")],
    code=dict(file="programme/03-cities-2028.md", note="Sanne, with Femke, Monday 10 January 2028", plain=True, src="""
# PROGRAMME · CITIES 2028                       manager: Sanne · sponsor: Femke · from 10 Jan 2028

BENEFIT     eight cities and 60,000 orders a day by end 2028 (board plan, 20 Mar)
PROJECTS    Ghent (open Mon 19 Jun) · Haarlem (open Mon 4 Sep) · launch office (from 1 Feb) ·
            courier contract renewal (by May)
OUTSIDE     station lockers pilot (Ana): dependency = store space at Utrecht Centraal
ROADMAP     one page, every milestone, updated by each PM on Fridays
SHARED      people booked here: Joost's ops lead · Eli · Lena · Maarten (Ghent permit)
CROSS RISKS Belgian permit (Ghent) · one builder for both cities · two openings, one ops lead
BOARD       every 4 weeks: Femke, Marco, Joost, Priya, Ana · can move money and people
            between projects within the programme total
PORTFOLIO   Femke's quarterly sheet: cities · ordering database · Larder Plus · business
            portal · lockers, ranked for funding
"""),
    tools="tools: one roadmap, one cross-project risk list, a booking sheet for shared people, and a board.",
    dial=[("Light", "two related projects", ["One shared timeline.", "A weekly call between the PMs.", "No board."]),
          ("Standard", "Cities 2028", ["A programme with a benefit, a roadmap and cross-project risks.", "A board every four weeks.", "A portfolio sheet above it."]),
          ("Heavy", "large transformations", ["Programme management office.", "Benefits register and tranches.", "Portfolio governance with stage funding."])],
    baseline="Each line compares <b>five separately run pieces of work</b> to <b>a programme with one benefit, one roadmap and one board, under a portfolio view</b>.",
    ratings=[(3, 5, "Work is steered by the benefit: eight cities."),
             (2, 4, "Shared people are booked once."),
             (2, 4, "Cross-project risks have one list."),
             (2, 4, "One roadmap for everything."),
             (3, 4, "The board sees the promise, not five plans."),
             (3, 4, "Project managers keep their projects."),
             (3, 4, "Money moves between projects within the total."),
             (3, 3, "Neutral."),
             (3, 3, "A board every four weeks.")],
    pitfalls=[("Programme of unrelated work", "A board with nothing to decide.", "group only what shares a benefit."),
              ("Programme as a big project", "Detail chokes it.", "manage the links; let projects run."),
              ("No benefit owner", "Projects finish; the promise doesn't.", "report the benefit."),
              ("Portfolio by habit", "Last year's priorities.", "rank investments each quarter.")],
    use=["Several projects sharing people, money and a goal.", "When projects collide on people or dates.", "When the benefit needs more than one project.", "Quarterly, for the portfolio."],
    skip=["A single project; a portfolio of unrelated small work."],
    related=["<b>What Is It All For?</b> (vol. 1)", "<b>Who Helps the Project Managers Now?</b> (this volume)", "<b>Application Portfolio (TIME)</b> (Ana, vol. 4)", "<b>Did We Get What We Paid For?</b> (next note)"],
    quiz=[("Project, programme or portfolio: Ghent's launch?", "A project, inside the Cities 2028 programme."),
          ("Why is the lockers pilot outside the programme?", "It serves a different benefit; it's Ana's project, with one dependency."),
          ("What can the programme board do that a project can't?", "Move money and people between projects within the total; manage cross-project risks."),
          ("Two project managers both book Eli for the week of 12 June. Who decides?", "The programme: shared people are booked at programme level; the board settles it."),
          ("Femke asks whether the business portal should join the programme. What do you ask?", "Does it serve the programme's benefit (eight cities, 60,000 a day)? If not, it's a separate investment in the portfolio.")],
    try_it="List the projects that share people with yours. Do they serve one benefit? If yes, draw one roadmap of all of them and one list of the risks between them.",
    remember="One ceremony, one <span class=\"hl\">weekend</span>, one family <span class=\"hl\">year</span>.",
    sources=["Project Management Institute, <i>PMBOK Guide</i>, Eighth Edition (2025): the value delivery system; projects, programmes and portfolios.",
             "Project Management Institute, <i>The Standard for Program Management</i> (4th ed., 2017).",
             "Project Management Institute, <i>The Standard for Portfolio Management</i> (4th ed., 2017)."],
)

# ------------------------------------------------------------------ 04 Did We Get What We Paid For?
br_problem = Doodle(760, 260, "Doodle of Monday 17 January 2028 and Sanne's mistake for this collection. Rotterdam's value chain of January 2026 promised three benefit checks: at four weeks, at twelve weeks and at the start of Utrecht. Only the first happened, in the closing report. The twelve-week check, August 2026, never did. Twenty months later, nobody can say whether Rotterdam's on-time benefit was met.",
                    "Three checks promised in January 2026. One happened. The +12-week check never did.", exact=True)
br_problem.row([("+4 weeks", "May 2026 ✓", "green"), ("+12 weeks", "Aug 2026 ✗", "pink"), ("start of Utrecht", "Feb 2027 ✗", "pink")], y=24, h=96, size=18, subsize=14)
br_problem.note(380, 170, "the project closed; the benefits had no meeting", "red", size=18)
br_problem.note(380, 206, "“90 % on time by the end of the summer”: met or not?", "pen", size=17)

br_analogy = Doodle(760, 250, "Doodle of a family who fitted a heat pump to cut their energy bill by a third. The installer finished on time and on budget. The question they bought it for is answered only a year later, when the bills arrive. Families who never compare the bills never find out the settings were wrong.",
                    "The installer finished on budget. The bills a year later say whether it worked.", exact=True)
br_analogy.box(14, 40, 350, 110, "installed: on budget", "green", sub="the project", size=17, subsize=14)
br_analogy.box(396, 40, 350, 110, "bills: a third lower?", "y", sub="the benefit, a year later", size=17, subsize=14)
br_analogy.arrow(366, 95, 392, 95)
br_analogy.note(380, 200, "the reason you paid is checked after the project ends", "pen", size=17)

br_how = Doodle(760, 470, "Rotterdam's benefits checked on 17 January 2028. Benefit one: 500 orders a day by the end of May 2026, owner Joost: met, 590 in week four. Benefit two: 90 percent express on time by the end of the summer 2026, owner Joost: missed, 86 percent in September, 90 percent only in November after the second courier wave and a zone fix. Benefit three: a playbook so the next city opens in eight weeks or less, owner Femke: met, Utrecht, The Hague and Eindhoven each in eight weeks. Money: payback forecast about December 2026, actual January 2027. Below, the new rule in playbook v4: benefit checks at plus four and plus twelve weeks, owned by the benefit owner, on the steering group's calendar before the project closes.",
                "Two of three met; one met two months late and nobody noticed. From v4: benefit checks are booked before closing.", exact=True)
bens = [("500 orders a day by end May 2026", "Joost", "met: 590 in week 4", "green"),
        ("90 % express on time by end of summer", "Joost", "86 % Sep → 90 % Nov 2026", "pink"),
        ("next city in ≤ 8 weeks (a playbook)", "Femke", "met: Utrecht, The Hague, Eindhoven", "green"),
        ("payback (Marco)", "Marco", "forecast ≈ Dec 2026 → Jan 2027", "y")]
for i, (b, o, r, f) in enumerate(bens):
    y = 14 + i * 76
    br_how.box(8, y, 744, 66, None, f, rx=6)
    br_how.text(22, y + 28, b, anchor="start", size=15)
    br_how.text(22, y + 52, "owner: " + o, anchor="start", size=13)
    br_how.text(740, y + 40, r, anchor="end", size=14)
br_how.box(8, 330, 744, 128, None, "blue")
br_how.head(380, 358, "playbook v4: benefits after closing", size=17)
br_how.text(380, 390, "checks at +4 and +12 weeks, by the benefit owner", size=14)
br_how.text(380, 414, "booked on the steering calendar before the project closes", size=14)
br_how.text(380, 438, "a missed target goes to the portfolio review, with a reason", size=14)

BENEFITS = dict(
    slug="benefits-realisation",
    kicker="a.k.a. “benefits realisation”: did the project deliver what it was for?",
    tldr="A project delivers <b>outputs</b>; it exists for <b>benefits</b>, which often arrive after it closes. <b>Benefits realisation</b> is checking, on dates agreed at the start, whether each benefit was reached, by its <b>owner</b> (usually not the project manager), and acting when it wasn't. Book the checks <b>before</b> the project closes, or there will be no meeting to hold them in. Compare with the forecast, explain the gap, and feed it into the next decision and the playbook.",
    chips=[("Family", "fitting it to the work"), ("Lives in", "a benefits table with owners and check dates, carried past closing"), ("Pairs with", "the value chain (vol. 1), the closing report, the portfolio")],
    pmbok=dict(covers="defining, measuring and sustaining the benefits a project exists for, before and after it closes, with named owners",
               domains=FND + ["finance"], processes=[], principles=["Focus on value"], focus=["closing", "monitoring and controlling"],
               older="6th: the benefits management plan (a business document). 7th: value delivery and outcomes. PMI's <i>Benefits Realization Management</i> practice guide."),
    problem_side="Larder, Monday 17 January 2028",
    problem="""  <p class="lead">This is <b>Sanne's mistake</b> for this collection. Rotterdam's value chain of 16 January 2026 named three benefits and three checks: at <b>+4 weeks</b>, <b>+12 weeks</b> and the <b>start of Utrecht</b>. The first happened, inside the closing report of 22 May. <span class="hl-pink">The +12-week check, due in August 2026, never did.</span> The project had closed; the steering group had stopped meeting; nobody had booked it. Preparing the 2028 programme, Femke asks a simple question: “Did Rotterdam do what we paid for?” Twenty months on, nobody can answer for the on-time benefit without digging.</p>
  <ul>
    <li>Benefit checks had no meeting once the project closed.</li>
    <li>The owners were named, but never reminded.</li>
    <li>A missed benefit could have changed the next launch.</li>
  </ul>""",
    problem_figs=[br_problem],
    analogy_side="the heat pump",
    analogy="""  <p>A family fits a heat pump to cut its energy bill by a third. The installer finishes <b>on time and on budget</b>. Whether the family got what it paid for is only known <b>a year later</b>, when the bills come in. Families who never compare the bills never find out that the settings were wrong, and recommend the installer to their neighbours anyway.</p>""",
    analogy_figs=[br_analogy],
    map=[("Installed on budget", "Rotterdam: opened on time, €379.6k of €380k"),
         ("The bills a year later", "The +12-week check, August 2026"),
         ("Comparing the bills", "The benefits review of 17 January 2028"),
         ("The wrong settings", "On-time delivery at 86 % in September"),
         ("Recommending the installer", "Copying the launch without checking it worked")],
    how_side="each benefit, its owner, the result, the reason, the rule",
    how="""  <p>Sanne and the owners do the check on <b>17 January 2028</b>, from the data. <b>500 orders a day by the end of May 2026</b> (Joost): <b>met</b>, 590 in week four. <b>90 % express on time by the end of the summer</b> (Joost): <b>missed</b>. It was 86 % in September and reached 90 % only in <b>November 2026</b>, after the second courier wave and a fix to zone RTM-2's street numbers (the issue handed over at closing, I-21). A +12-week check in August would have pulled both forward by two months. <b>The next city in eight weeks or less</b> (Femke): <b>met</b>: Utrecht (15 February → 12 April 2027), The Hague and Eindhoven each took eight weeks; Antwerp, abroad, didn't count. Marco adds the money: payback forecast about December 2026, actual <b>January 2027</b>. The rule goes into playbook v4 the same week: benefit checks at <b>+4 and +12 weeks</b>, run by the benefit owner, <b>booked on the steering calendar before the project closes</b>; a missed target goes to the portfolio review with its reason. Antwerp's +12-week check (10 January 2028) and Eindhoven's (14 February) go on the calendar that week; Ghent's are booked before it opens.</p>""",
    how_figs=[br_how],
    steps=[("Name each benefit with a measure and a date", "At the start."),
           ("Give each an owner", "Usually the person who runs the result."),
           ("Book the checks before closing", "On a calendar that outlives the project."),
           ("Check from data", "Against the target and the forecast."),
           ("Explain every gap", "And what would have closed it sooner."),
           ("Feed it forward", "Into the playbook and the portfolio.")],
    vocab=[("Output", "What the project produces: a store, an app setting."),
           ("Outcome", "The change the output causes: customers ordering."),
           ("Benefit", "The measurable gain the organisation wanted: 500 orders a day."),
           ("Benefit owner", "The person accountable for reaching a benefit after the project."),
           ("Benefits realisation", "Checking and sustaining benefits until they're reached."),
           ("Dis-benefit", "A negative effect the project causes, also to be tracked.")],
    code=dict(file="programme/04-rotterdam-benefits.md", note="Sanne, Joost, Femke, Marco, Monday 17 January 2028", plain=True, src="""
# ROTTERDAM · BENEFITS CHECK (20 months after opening)                17 Jan 2028

BENEFIT (value chain, 16 Jan 2026)        OWNER  TARGET            RESULT
500 orders a day                          Joost  by end May 2026   MET · 590 in week 4
90 % express on time                      Joost  by end summer 26  MISSED · 86 % Sep 2026,
                                                                     90 % Nov 2026 (courier wave 2,
                                                                     RTM-2 street numbers, I-21)
next city in <= 8 weeks (playbook)        Femke  Utrecht           MET · Utrecht 15 Feb-12 Apr 2027,
                                                                     The Hague 8, Eindhoven 8 weeks
PAYBACK (Marco)                                  ≈ Dec 2026        Jan 2027

CHECKS PROMISED   +4 wks (done, closing report) · +12 wks Aug 2026 (NOT HELD) · start of
                  Utrecht (NOT HELD)
COST OF THE MISS  on-time reached ~2 months later than a check in August would have allowed
RULE (playbook v4) checks at +4 and +12 weeks by the benefit owner, booked on the steering
                   calendar BEFORE closing · misses go to the portfolio review
BOOKED            Antwerp +12 wks 10 Jan 2028 · Eindhoven +12 wks 14 Feb · Ghent before opening
"""),
    tools="tools: the value chain from the start, the owners, the data, and a calendar that outlives the project.",
    dial=[("Light", "small work", ["Say what it's for.", "Look once afterwards.", "Tell the sponsor."]),
          ("Standard", "a city launch", ["Benefits with owners, measures and dates.", "Checks at +4 and +12 weeks, booked before closing.", "Gaps explained, fed into the playbook."]),
          ("Heavy", "large investments", ["A benefits register and realisation plan.", "Independent post-implementation review.", "Benefits tracked in the portfolio for years."])],
    baseline="Each line compares <b>one check inside the closing report</b> to <b>owned checks at +4 and +12 weeks, booked before closing, with gaps fed forward</b>.",
    ratings=[(2, 5, "The reason for the project is checked."),
             (3, 4, "Benefit forecasts get tested."),
             (2, 4, "A missed benefit is found in weeks, not years."),
             (2, 5, "Results against targets are on one page."),
             (3, 4, "The board sees what launches return."),
             (3, 4, "Owners own their benefits."),
             (3, 4, "Misses change the next launch."),
             (3, 3, "Neutral."),
             (3, 3, "Two short meetings after closing.")],
    pitfalls=[("Benefits in the charter only", "Forgotten at closing.", "carry them past closing."),
              ("No meeting after the project", "Checks never happen.", "book them before closing."),
              ("PM as benefit owner", "The PM has moved on.", "the person who runs the result owns it."),
              ("A miss without a reason", "Nothing is learned.", "explain it, feed it forward.")],
    use=["At the start: name benefits, owners, check dates.", "Before closing: book the checks.", "After closing: run them.", "Before funding the next one."],
    skip=["Work with no benefit beyond its output (then question the work)."],
    related=["<b>What Is It All For?</b> (vol. 1)", "<b>Are We Done?</b> (vol. 2)", "<b>Was It Worth It?</b> (vol. 4)", "<b>One Project, or Many?</b> (previous note)"],
    quiz=[("Output or benefit: the store is open?", "An output. 500 orders a day is a benefit."),
          ("Which Rotterdam benefit was missed, and when was it reached?", "90 % on time: 86 % in September, 90 % in November 2026."),
          ("What's the v4 rule?", "Checks at +4 and +12 weeks by the benefit owner, booked before closing; misses to the portfolio review."),
          ("Ghent's closing report is next week. What do you check is on the calendar?", "The +4 and +12-week benefit checks, with owners, beyond the project's end."),
          ("Joost says “the store's open, the project worked.” What do you ask?", "Did it reach its benefits, by when, and what does the data say?")],
    try_it="Find your last finished project's benefits. Who owns each? When was each checked? Book the missing check for this month.",
    remember="On budget is the <span class=\"hl\">installer</span>. Lower bills are the <span class=\"hl\">reason</span>.",
    sources=["Project Management Institute, <i>PMBOK Guide</i>, Eighth Edition (2025): value delivery; benefits.",
             "Project Management Institute, <i>Benefits Realization Management: A Practice Guide</i> (2019).",
             "Gerald Bradley, <i>Benefit Realisation Management</i> (2nd ed., 2010)."],
)

NOTES = [TAILOR_WHOLE, PLAYBOOK, PROGRAMME, BENEFITS]
