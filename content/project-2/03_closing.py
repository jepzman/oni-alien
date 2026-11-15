# Series 2 · Book 3 · The Project Manager's Notebook · Vol. 2 · Closing.
# Narrator: Sanne. Running case study: Larder (facts in docs/larder-casebook.md, "Book 3, Vol. 2").
# Spine: PMBOK Guide, Eighth Edition, Governance domain. Names are PMI's; every explanation is in our own words.

GOV = ["governance"]

# ------------------------------------------------------------------ 13 What Did We Learn?
ll_problem = Doodle(760, 250, "Doodle of what happened after Zuid opened in November 2024. A meeting was held, a long document of lessons was written, and it was saved in a folder. Nobody opened it again. Fifteen months later Rotterdam's team asked Tomás what went wrong at Zuid, and he told them from memory.",
                    "Zuid's lessons: written once, filed, never opened. Rotterdam learned them from Tomás's memory.")
ll_problem.row([("a meeting", "Nov 2024", "paper"), ("a long document", "38 lessons", "paper"), ("a folder", "opened: never", "pink")], y=40, h=90, gap=40, size=19, subsize=15, arrows=True)
ll_problem.note(380, 186, "written is not the same as learned", "red", size=20)
ll_problem.note(380, 222, "a lesson counts when the next project does something differently", "pen", size=16)

ll_analogy = Doodle(760, 240, "Doodle of a family recipe book. Next to the cake recipe someone has written in pencil: use less sugar, oven runs hot, takes ten minutes longer. The note is on the recipe itself, so the next baker sees it at the moment it matters. Nobody keeps a separate notebook called mistakes we made with cakes.",
                    "Notes in the margin of the recipe: the next baker sees them at the moment they matter.")
ll_analogy.icon("recipe", 50, 40, 1.8)
ll_analogy.note(330, 70, "“less sugar”", "pen", size=22, anchor="start")
ll_analogy.note(330, 112, "“oven runs hot”", "pen", size=22, anchor="start")
ll_analogy.note(330, 154, "“10 minutes longer”", "pen", size=22, anchor="start")
ll_analogy.note(380, 216, "the lesson lives on the recipe, not in a drawer", "red", size=18)

ll_how = Doodle(760, 400, "How Rotterdam's lessons were handled. During the project: one line a week, forty-one lines by May. On 18 May: a ninety-minute session sorts them into three piles. Twelve become changes to the launch playbook, each with an owner. Nine become changes to templates and checklists. Twenty are noted and dropped. The top three: add store IT as an eighth workstream; order long-lead items in week one; the product owner signs the launch scope. Then the test: at Utrecht's kick-off, the playbook is the agenda.",
                "One line a week, sorted once, and turned into changes to the things the next project will use.")
ll_how.row([("1 line a week", "41 lines by May", "y"), ("sort · 18 May", "90 minutes, the leads", "blue"), ("change something", "playbook · templates", "green")], y=14, h=84, gap=40, size=18, subsize=14, arrows=True)
ll_how.row([("12", "→ the launch playbook", "green"), ("9", "→ templates, checklists", "green"), ("20", "noted, dropped", "paper")], y=124, h=90, size=28, subsize=14)
ll_how.box(14, 238, 732, 110, None, "y")
ll_how.head(380, 264, "top three", size=18)
ll_how.text(380, 292, "store IT is an eighth workstream  ·  order long-lead items in week 1", size=15)
ll_how.text(380, 318, "the product owner signs the launch scope", size=15)
ll_how.note(380, 380, "the test: Utrecht's kick-off uses the playbook as its agenda", "pen", size=17)

LESSONS = dict(
    slug="lessons-learned",
    kicker="a.k.a. “managing project knowledge” (lessons learned)",
    tldr="Projects learn expensive things and then forget them. <b>Managing knowledge</b> means two things: <b>using</b> what the organisation already knows when you start, and <b>capturing</b> what you learn in a form the next project will actually meet. Collect lessons <b>as you go</b> (one line a week), sort them once, and turn the good ones into <b>changes to templates, checklists and playbooks</b>. A lesson filed in a report has been written down. It hasn't been learned.",
    chips=[("Family", "closing"), ("Lives in", "one line a week; then the playbook and templates"), ("Pairs with", "the launch desk, quality assurance, post-launch review")],
    pmbok=dict(covers="using existing knowledge and capturing new knowledge; lessons learned", domains=GOV,
               processes=["Manage Project Knowledge"], principles=["Embed quality into processes and deliverables", "Build an empowered culture"], focus=["executing", "closing"],
               older="6th: “Manage Project Knowledge” (4.4, new in the 6th), the lessons learned register. 7th: knowledge management under the Project Work domain."),
    problem_side="Larder, 18 May 2026",
    problem="""  <p class="lead">After Zuid opened in November 2024 there was a meeting, and a document with <b>38 lessons</b>. It was saved in a folder. <span class="hl-pink">Nobody opened it again.</span> In January Sanne learned what went wrong at Zuid by asking Tomás, who told her from memory. Now Rotterdam is open, Utrecht starts in the spring, and Sanne has 41 lines of her own. If she writes a report and files it, Utrecht will ask her from memory too, and she may not be at Larder.</p>
  <ul>
    <li>Lessons gathered only at the end are half forgotten.</li>
    <li>A long list in a folder is read by nobody.</li>
    <li>Knowledge that lives in one head leaves with it.</li>
  </ul>""",
    problem_figs=[ll_problem],
    analogy_side="notes in the margin of the recipe",
    analogy="""  <p>In a family recipe book someone has written next to the cake: <b>“less sugar, oven runs hot, ten minutes longer.”</b> The note is on the recipe, so the next baker sees it at the moment it matters. Nobody keeps a separate notebook called “mistakes we made with cakes”, because nobody would read it before baking.</p>""",
    analogy_figs=[ll_analogy],
    map=[("The recipe", "The launch playbook, the gate checklists, the templates"),
         ("The pencil note", "A lesson, written as a change to one of them"),
         ("Written while baking", "One line a week, during the project"),
         ("A drawer of old notebooks", "Zuid's 38 lessons in a folder"),
         ("The next baker", "Whoever leads Utrecht")],
    how_side="collect weekly, sort once, change the recipe",
    how="""  <p>Since February the Thursday meeting has ended with one question: <b>“anything we'd do differently next time?”</b> One line, the week it happens: 41 lines by May. On <b>18 May</b>, a week after hypercare, the leads spend ninety minutes sorting them. <b>Twelve</b> become changes to the <b>launch playbook</b>, each written as an instruction, with an owner. <b>Nine</b> become changes to templates and gate checklists. <b>Twenty</b> are noted and dropped: true, but nobody would act on them. Sanne also records what <b>worked</b>, so nobody “improves” it away. The real test comes at Utrecht's kick-off, where the playbook is the agenda.</p>""",
    how_figs=[ll_how],
    steps=[("Start by reading what exists", "And asking who did it last time."),
           ("Collect one line a week", "While the reason is fresh."),
           ("Sort once, with the people who did the work", "Soon after the end."),
           ("Rewrite each keeper as a change to something", "A checklist line, a template, a playbook step."),
           ("Give each change an owner and do it", "Before the team scatters."),
           ("Use it at the next kick-off", "That is the only proof.")],
    vocab=[("Lesson learned", "Knowledge gained from doing the work, good or bad, that should change future work."),
           ("Lessons register", "The running list of lessons during a project."),
           ("Explicit knowledge", "What can be written down: steps, numbers, templates."),
           ("Tacit knowledge", "What people know but find hard to write: judgment, feel. Shared by working together."),
           ("Retrospective", "A regular look back by the team at how the work is going."),
           ("Playbook", "A reusable description of how to do a recurring kind of project.")],
    code=dict(file="rotterdam/13-lessons.md", note="sorted by the leads, 18 May 2026 · 41 lines → 21 changes", plain=True, src="""
# ROTTERDAM · LESSONS → CHANGES

INTO THE LAUNCH PLAYBOOK (12; top six shown)                            OWNER
 1 Store IT and internet is an eighth workstream; line ordered in week 1  Eli
 2 Order every item with a lead time over 4 weeks in week 1               Joost
 3 The product owner signs the launch scope; the PM never restates it     Sanne
 4 First picker group starts one week before stocking, trains at a        Tomás
   running store
 5 Fixed-price fit-out with late-day and retention clauses                Joost
 6 Saturday slot capacity is set from the waitlist size, two weeks before Grace

INTO TEMPLATES AND CHECKLISTS (9; three shown)
   every automated check alerts on failure and on "nothing checked"      Eli
   Gate 1 criteria include "internet line live or workaround tested"      Sanne
   the plan on a page has a WEAK POINT line                               Sanne

WHAT WORKED (keep)   the team planning its own work · the three triggers · RTM-0 weekly
                     order · go with conditions · one page for everything

NOTED AND DROPPED    20 lines (true, but nobody would act on them)
FIRST USE            Utrecht kick-off: the playbook is the agenda
"""),
    tools="tools: one question every Thursday, a 90-minute sort, and edit rights on the playbook.",
    dial=[("Light", "a small team", ["A retrospective every few weeks.", "One change at a time.", "Nothing written beyond the change."]),
          ("Standard", "Rotterdam", ["One line a week.", "A 90-minute sort at the end.", "Changes to the playbook and templates, with owners."]),
          ("Heavy", "many projects, a PMO", ["A lessons database with categories.", "Formal post-project reviews.", "A PMO that feeds lessons into standards and training."])],
    baseline="Each line compares <b>a lessons report written at the end and filed</b> to <b>one line a week, sorted once, turned into changes to what the next project uses</b>.",
    ratings=[(3, 4, "The eight-week benefit depends on it."),
             (2, 4, "The next plan starts from what happened."),
             (2, 4, "Known traps are in the checklists."),
             (3, 4, "What changed, and why, is visible."),
             (3, 4, "Femke sees the playbook grow."),
             (3, 4, "The people who did the work sort the lessons."),
             (3, 3, "Neutral."),
             (2, 4, "Mistakes are designed out, not remembered."),
             (4, 3, "A minute a week and one session.")],
    pitfalls=[("Only at the end", "Half is forgotten, the rest is polite.", "one line a week."),
              ("A report in a folder", "Zuid's 38 lessons.", "change the playbook, the template, the checklist."),
              ("Only what went wrong", "Good practice gets “improved” away.", "record what worked."),
              ("Blame", "People stop offering lessons.", "ask what to change, not who was at fault.")],
    use=["From the first week, a line at a time.", "At every phase gate and at the end.", "At every kick-off: read the last project's lessons.", "When the same mistake appears twice."],
    skip=["A true one-off that nobody will ever repeat (rare)."],
    related=["<b>Who Helps the Project Managers?</b> (vol. 1)", "<b>Is Our Way of Working Working?</b> (this volume)", "<b>Post-launch review</b> (Grace, vol. 4)", "<b>The city launch playbook</b> (vol. 6)"],
    quiz=[("What are the two halves of managing knowledge?", "Using what is already known, and capturing what is learned."),
          ("Why one line a week?", "At the end, half is forgotten and the reasons are gone."),
          ("What makes a lesson “learned”?", "Something the next project uses has changed because of it."),
          ("A lead writes: “communication could have been better.” What does Sanne do with it?", "Ask what, exactly, they would change. If nobody can name a change, it goes on the dropped pile."),
          ("How will Sanne know the lessons worked?", "Utrecht's kick-off uses the playbook, and Utrecht doesn't repeat Rotterdam's mistakes.")],
    try_it="At your next team meeting ask one question: “anything we'd do differently next time?” Write one line. Then pick one lesson you already have and turn it into a change to a checklist or template today.",
    remember="Write the lesson on the <span class=\"hl\">recipe</span>, not in a <span class=\"hl\">drawer</span>.",
    sources=["Project Management Institute, <i>PMBOK Guide</i>, Eighth Edition (2025): Governance domain, managing project knowledge.",
             "Project Management Institute, <i>PMBOK Guide</i>, Sixth Edition (2017): 4.4 Manage Project Knowledge.",
             "Nick Milton, <i>The Lessons Learned Handbook</i> (2010).",
             "Norman Kerth, <i>Project Retrospectives</i> (2001)."],
)

# ------------------------------------------------------------------ 14 Who Looks After It Now?
ho_problem = Doodle(760, 250, "Doodle of the second week of May 2026. The store has been open two weeks. Yara, the Rotterdam store manager, still phones Sanne six times a day: where is the warranty for the cold room, who do I call about the internet, is the second door still coming? The project is nearly over. The store's questions still all come to the project manager.",
                    "Two weeks after opening, the store manager still phones the project manager six times a day.")
ho_problem.circle(150, 110, 50, "blue", label="Yara", sub="store")
ho_problem.circle(610, 110, 50, "y", label="Sanne", sub="project")
for i, y in enumerate([70, 90, 110, 130, 150]):
    ho_problem.arrow(202, y, 558, y, color="red")
ho_problem.note(380, 50, "“where's the warranty?”", "pen", size=16)
ho_problem.note(380, 196, "“is the second door still coming?”", "pen", size=16)
ho_problem.note(380, 232, "the project can't end while this is true", "red", size=19)

ho_analogy = Doodle(760, 240, "Doodle of buying a house. On the day of the sale the old owner walks the new owner round: this is the fuse box, the boiler was serviced in March, here are the manuals and the spare keys, the gutter at the back leaks a little and here is the roofer's number. Then the keys change hands. Without that walk, the new owner phones for a year.",
                    "Selling a house: a walk-round, the manuals, the keys, the roofer's number. Then you stop being the owner.")
ho_analogy.row([("walk-round", "how it all works", "blue"), ("the papers", "manuals, warranties", "y"), ("what's still open", "and who to call", "pink"), ("the keys", "signed over", "green")], y=50, h=90, size=17, subsize=13)
ho_analogy.note(380, 200, "after the keys, the questions go to the new owner", "pen", size=19)

ho_how = Doodle(760, 400, "Rotterdam's handover in the week of 11 May 2026. Gate 5: the hypercare exit criteria are met. Then four things pass from Sanne to Yara and Joost. The store as built: drawings, warranties, supplier contacts. How it runs: the daily numbers, the nightly checks, who to call. What is still open: two issues, the deferred second cold-room door, the snag retention. And the benefits: 500 orders a day and 90 percent on time, owned by Joost. A two-week period where Sanne answers within a day, then stops. Signed by Yara on 15 May.",
                "Four things handed over, a short period of help, a signature, and then the phone stops ringing.")
ho_how.box(14, 14, 732, 64, "Gate 5 · 11 May · hypercare exit criteria met", "green", size=18)
ho_how.row([("as built", "drawings · warranties", "y"), ("how it runs", "numbers · contacts", "blue"), ("still open", "2 issues · the door", "pink"), ("the benefits", "owner: Joost", "green")], y=104, h=100, size=18, subsize=12)
ho_how.arrow(380, 206, 380, 238)
ho_how.box(160, 240, 440, 70, "to Yara and Joost", "paper", sub="walked through on site, 12 May", size=19, subsize=14)
ho_how.box(14, 330, 350, 56, "Sanne helps until 29 May", "paper", size=17, dash=True)
ho_how.box(396, 330, 350, 56, "signed: Yara · 15 May", "green", size=17)

HANDOVER = dict(
    slug="handover",
    kicker="a.k.a. “transition to operations” (part of closing)",
    tldr="A project's result is worth something only once <b>someone else is running it</b>. The <b>handover</b> gives the people who will operate it everything they need: the thing itself, how it works, what is <b>still open</b>, and who now owns each benefit. Plan it from the start, do it face to face, set a short period of help with an <b>end date</b>, and get a signature. Until then the project isn't finished. It has only stopped.",
    chips=[("Family", "closing"), ("Lives in", "a handover pack and a walk-round"), ("Pairs with", "hypercare, phase gates, the benefits map")],
    pmbok=dict(covers="transferring the result to operations: acceptance, documentation, open items, benefit owners", domains=GOV + ["stakeholders"],
               processes=["Close Project or Phase"], principles=["Focus on value", "Integrate sustainability within all project areas"], focus=["closing"],
               older="6th: “final product, service or result transition”, an output of Close Project or Phase (4.7). 7th: transition under the Delivery domain."),
    problem_side="Larder, 11–15 May 2026",
    problem="""  <p class="lead">Rotterdam has been open for two weeks. <b>Yara</b>, the store manager, phones Sanne six times a day. Where is the cold-room warranty? Who do I call when the router drops? Is that second door still coming? Yara isn't doing anything wrong. <span class="hl-pink">Everything about how the store came to be is in Sanne's head and Sanne's binder</span>, and Sanne is due on her other projects and then Utrecht.</p>
  <ul>
    <li>The people who run the result weren't given what they need.</li>
    <li>Open items have no owner after the project.</li>
    <li>There is no moment when the project stops being responsible.</li>
  </ul>""",
    problem_figs=[ho_problem],
    meanwhile=[("product-3", "hypercare", "Grace's hypercare ran daily at 09:00 from 27 April to 11 May; its exit criteria (tickets under 3 per 100, no P1 for five days) were met.",
                "Sanne's Gate 5 uses Grace's hypercare exit criteria as the signal that the store can be handed over.")],
    analogy_side="selling a house",
    analogy="""  <p>On the day a house is sold, a decent seller <b>walks the buyer round</b>: here is the fuse box, the boiler was serviced in March, these are the manuals and the spare keys. The gutter at the back <b>still leaks a little</b>; here is the roofer's number. Then the keys change hands. Skip the walk and the buyer phones for a year. Skip the leak and they phone a lawyer.</p>""",
    analogy_figs=[ho_analogy],
    map=[("The buyer", "Yara, the store manager, and Joost"),
         ("The walk-round", "Tuesday 12 May, on site, two hours"),
         ("Manuals and keys", "Drawings, warranties, supplier contacts, logins"),
         ("The leaking gutter", "Two open issues, the deferred door, the snag retention"),
         ("The keys change hands", "Yara signs on 15 May; Sanne's help ends 29 May")],
    how_side="four things, a walk-round, an end date, a signature",
    how="""  <p><b>Gate 5</b> on 11 May: the hypercare exit criteria are met. That week Sanne builds a <b>handover pack</b> of four parts. <b>As built</b>: drawings, warranties, supplier and landlord contacts. <b>How it runs</b>: the five daily numbers, the nightly checks, who to call for what. <b>Still open</b>: two issues, the deferred second cold-room door (now Joost's to decide), and the builder's 5 % retention, released when the last snag was fixed on 15 May. <b>The benefits</b>: both store benefits, with Joost as owner and the dates to check them. She walks Yara through it <b>on site</b>, and they agree an end: Sanne answers within a day until <b>29 May</b>, then questions go to Joost. Yara signs. The phone calls fall to one a week.</p>""",
    how_figs=[ho_how],
    steps=[("Name the receiver at the start", "And involve them before the end."),
           ("Agree what “ready to hand over” means", "Exit criteria, as a gate."),
           ("Pack four things", "As built, how it runs, still open, the benefits."),
           ("Walk through it in person", "On site, with time for questions."),
           ("Set a short support period with an end date", "Then questions go to the new owner."),
           ("Get it signed", "Acceptance is a decision.")],
    vocab=[("Handover (transition)", "Passing the project's result to those who will operate it."),
           ("Acceptance", "The receiver's formal agreement that the result meets what was agreed."),
           ("As-built documentation", "Records of what was actually delivered."),
           ("Warranty period", "The time during which the supplier must fix defects."),
           ("Hypercare", "A short period of extra support straight after go-live."),
           ("Operational readiness", "The receiving team's ability to run the result.")],
    code=dict(file="rotterdam/14-handover.md", note="walked through 12 May · signed by Yara 15 May 2026", plain=True, src="""
# ROTTERDAM · HANDOVER TO THE STORE          from: Sanne   to: Yara (store), Joost (ops)

GATE 5 · 11 May   tickets < 3 per 100 orders for two days: yes · no P1 for five days: yes

1 AS BUILT        drawings and permits · cold room, fridges, shelving: warranties (2 yrs)
                  builder, cold-room supplier, landlord, internet provider: contacts
                  5 % retention released 15 May (last snag fixed)
2 HOW IT RUNS     five daily numbers (orders, on time, complete, tickets per 100, waste)
                  nightly price / VAT / zone check → Eli's alert, copy to Yara
                  who to call: store IT Eli · app Ben · suppliers Tomás · contracts Lena
3 STILL OPEN      I-21 two street numbers missing from zone RTM-2      Eli      22 May
                  I-23 Saturday slots full by Thursday                 Grace    June
                  C-06 second cold-room door (deferred)                Joost decides
                  substitution approvals in Rotterdam (C-03)           Grace    8 June
4 BENEFITS        500 orders a day by end May · 90 % on time by end of summer
                  owner: Joost · checked 25 May, 20 July and at the start of Utrecht

SUPPORT           Sanne answers within one working day until 29 May. After that: Joost.
ACCEPTED          Yara, 15 May 2026
"""),
    tools="tools: a four-part pack, two hours on site, and an end date in both diaries.",
    dial=[("Light", "a small internal change", ["Show the new owner how it works.", "A short note of what's open.", "“It's yours from Monday.”"]),
          ("Standard", "Rotterdam", ["A four-part handover pack.", "A walk-round on site.", "Two weeks of support with an end date; a signature."]),
          ("Heavy", "large systems, contracts", ["Operational readiness reviews.", "Formal acceptance tests and certificates.", "Service-level agreements and a warranty process."])],
    baseline="Each line compares <b>a project that fades out while the store keeps phoning</b> to <b>a planned handover: four parts, a walk-round, an end date and a signature</b>.",
    ratings=[(2, 5, "Benefits have an owner who stays."),
             (3, 3, "Neutral."),
             (2, 4, "Open items can't be lost."),
             (2, 5, "Everything the store needs is in one pack."),
             (3, 4, "Joost and Yara know what they've taken on."),
             (3, 4, "The store team runs its own store."),
             (3, 3, "Neutral."),
             (3, 4, "Warranties and checks carry on."),
             (4, 3, "A pack and a walk-round.")],
    pitfalls=[("Throwing it over the wall", "A link to a folder.", "walk through it, in person."),
              ("Hiding what's open", "It comes back as a complaint.", "list every open item with an owner."),
              ("Support with no end", "The project manager becomes the helpdesk.", "an end date, agreed."),
              ("Receiver meets it at the end", "They weren't ready.", "name them at the start; Yara joined on 2 March.")],
    use=["Every project that leaves something running.", "At the end of each phase that hands to another team.", "When the receiver keeps phoning.", "When a supplier hands over to you (Gate 1 was one)."],
    skip=["The result is used once and thrown away."],
    related=["<b>Hypercare after launch</b> (Grace, vol. 3)", "<b>May We Take the Next Step?</b> (this volume)", "<b>What Is It All For?</b> (vol. 1)", "<b>Handing over a product area</b> (Grace, vol. 6)"],
    quiz=[("What four things are handed over?", "As built, how it runs, what's still open, and the benefits with their owner."),
          ("Why set an end date for support?", "So questions move to the new owner and the project manager can be released."),
          ("Who owns the deferred cold-room door now?", "Joost. It was handed over as an open item."),
          ("On 3 June Yara phones Sanne about a broken fridge shelf. What does Sanne do?", "Help her find the warranty contact in the pack, and remind her kindly that since 29 May these go to Joost."),
          ("When should the receiver first be involved?", "From the start. Yara joined on 2 March and took part in Gates 1 and 2.")],
    try_it="Name the person who will run your project's result. Write the four headings (as built, how it runs, still open, benefits) and one line under each. What would they phone you about in month two? Put that in the pack.",
    remember="Walk them round, show them the <span class=\"hl\">leak</span>, hand over the <span class=\"hl\">keys</span>.",
    sources=["Project Management Institute, <i>PMBOK Guide</i>, Eighth Edition (2025): Governance domain, closing a project or phase.",
             "Project Management Institute, <i>PMBOK Guide</i>, Sixth Edition (2017): 4.7 Close Project or Phase.",
             "AXELOS, <i>ITIL 4: Service Transition practices</i> (2019)."],
)

# ------------------------------------------------------------------ 15 Are We Done?
cl_problem = Doodle(760, 250, "Doodle of 20 May 2026. The store opened on time, three weeks ago. The team has drifted to other work. But the project is not over: the builder's last invoice is unpaid, two purchase orders are open, the budget code is still live, nobody has told the steering group it's finished, and nobody has said thank you.",
                    "The store has been open three weeks. The project never ended. It just went quiet.")
cl_problem.box(250, 20, 260, 70, "store open ✓", "green", size=20)
for i, t in enumerate(["invoice unpaid", "2 orders open", "code still live", "no report", "no thank-you"]):
    cl_problem.box(14 + i * 148, 120, 138, 56, t, "paper", size=12, dash=True)
cl_problem.note(380, 220, "finished and closed are different things", "red", size=20)

cl_analogy = Doodle(760, 240, "Doodle of the end of a camping trip. Arriving at the lake isn't the end. Before leaving, the campers put out the fire, pack the tents, pay the site owner, take the rubbish, and look back once to check nothing is left. Only then do they drive home. A fire left smouldering is still their fire.",
                    "The trip isn't over at the lake. It's over when the fire is out, the site is paid and nothing is left behind.")
cl_analogy.row([("fire out", None, "pink"), ("tents packed", None, "y"), ("site paid", None, "green"), ("rubbish out", None, "blue"), ("look back", None, "paper")], y=60, h=70, gap=10, size=15)
cl_analogy.note(380, 186, "then, and only then, drive home", "pen", size=20)

cl_how = Doodle(760, 400, "Rotterdam's closing, presented to the steering group on 22 May 2026. Against the charter: opened 27 April, on the baseline date. All 71 must-haves done. Cost 379,600 euros against 380,000. Benefits: 590 orders a day in week four, the 500 target met early; 84 percent on time, target 90 percent by the end of summer, still open, owner Joost; playbook version one written. Closing checklist: results accepted, contracts closed, money settled, file archived, lessons turned into changes, team thanked and released. The steering group accepts the report: the project is closed.",
                "Against the charter: what was promised, what happened, what is still owed, and a decision to close.")
cl_how.row([("date", "27 Apr · on baseline", "green"), ("scope", "71 of 71 must-haves", "green"), ("cost", "€379.6k of €380k", "green")], y=14, h=84, size=20, subsize=14)
cl_how.row([("500 orders/day", "590 in week 4 ✓", "green"), ("90 % on time", "84 % · open → Joost", "y"), ("playbook", "v1 written ✓", "green")], y=118, h=84, size=18, subsize=14)
cl_how.note(380, 226, "benefits: two met, one still to come, with an owner", "pen", size=17)
for i, t in enumerate(["accepted", "contracts closed", "money settled", "file archived", "lessons → changes", "team released"]):
    r, c = divmod(i, 3)
    cl_how.box(14 + c * 248, 250 + r * 56, 236, 46, "✓ " + t, "paper", size=15, rx=5)
cl_how.note(380, 384, "steering group, 22 May: closed", "green", size=18)

CLOSING = dict(
    slug="closing-a-project",
    kicker="a.k.a. “closing a project or phase”",
    tldr="A project is <b>finished</b> when the work is done. It is <b>closed</b> when someone with authority has agreed that it is: results accepted and handed over, contracts and money settled, the file archived, lessons turned into changes, benefits passed to their owners, and the team thanked and released. Closing is short and easy to skip, and skipping it leaves <b>open invoices, orphaned promises and a team that never heard “well done”</b>. The same checklist, smaller, closes every phase.",
    chips=[("Family", "closing"), ("Lives in", "a closing report on one page and a checklist"), ("Pairs with", "the charter, handover, lessons learned")],
    pmbok=dict(covers="closing a project or phase: acceptance, contract and financial closure, final report, releasing the team", domains=GOV + ["finance", "resources"],
               processes=["Close Project or Phase"], principles=["Be an accountable leader", "Focus on value"], focus=["closing"],
               older="6th: “Close Project or Phase” (4.7); “Close Procurements” was folded into it. 7th: closing under the Delivery and Project Work domains."),
    problem_side="Larder, 20–22 May 2026",
    problem="""  <p class="lead">The store opened on time, three weeks ago. Everyone has moved on: Ben to approvals for Rotterdam, Eli to Dispatch, Joost to the summer. But Marco's team still has the <b>Rotterdam budget code open</b>, with two purchase orders on it and the builder's final invoice unpaid. Nobody has told the steering group it's over. <span class="hl-pink">And nobody has said thank you to forty people who opened a city in fifteen weeks.</span></p>
  <ul>
    <li>Open orders and codes keep collecting costs.</li>
    <li>Without a final report, nobody compares result with promise.</li>
    <li>A project that fades out teaches the team that finishing doesn't matter.</li>
  </ul>""",
    problem_figs=[cl_problem],
    analogy_side="leaving the campsite",
    analogy="""  <p>A camping trip doesn't end when you reach the lake. Before driving home you <b>put out the fire</b>, pack the tents, <b>pay the site owner</b>, take the rubbish, and <b>look back once</b> to check nothing is left. It takes half an hour, and it's the difference between a good trip and a phone call from the site owner in a week. A fire left smouldering is still your fire.</p>""",
    analogy_figs=[cl_analogy],
    map=[("Reaching the lake", "Opening on 27 April"),
         ("Putting out the fire", "Closing issues, or handing them over by name"),
         ("Paying the site owner", "Final invoices, purchase orders, the budget code"),
         ("One look back", "The closing report against the charter"),
         ("Driving home", "The steering group says “closed”; the team is released")],
    how_side="compare with the charter, tick the checklist, get the decision",
    how="""  <p>Sanne takes <b>the charter</b> out again and writes the closing report against it, line by line, on one page. <b>Promised</b>: open 27 April, €380k, 71 must-haves. <b>Happened</b>: opened 27 April, €379.6k, 71 of 71. <b>Benefits</b>: orders reached 590 a day in week four (target 500 by end of May: met); on time is 84 % against 90 % by the end of the summer (open; owner Joost); playbook v1 is written. Then the <b>checklist</b>: results accepted (Yara, 15 May), contracts closed, the budget code closed with Marco, the project file archived, lessons turned into 21 changes. On <b>22 May</b> the steering group accepts the report. Femke says the word: <b>closed</b>. That evening Joost buys dinner for everyone, and Sanne reads out one thing each lead did that made the difference.</p>""",
    how_figs=[cl_how],
    steps=[("Confirm the result is accepted and handed over", "With a signature."),
           ("Settle contracts and money", "Invoices, orders, the budget code."),
           ("Write the closing report against the charter", "Promised, happened, why different."),
           ("Hand each benefit and open item to an owner", "By name, with dates."),
           ("Archive the file; make sure lessons became changes", "Where the next project will find them."),
           ("Get the decision to close, then thank and release the team", "Out loud.")],
    vocab=[("Project closure", "The formal end of a project, agreed by the sponsor or steering group."),
           ("Final report", "A summary of what was promised, what was delivered, and what remains."),
           ("Contract closure", "Confirming all obligations under a contract are met and paid."),
           ("Financial closure", "Closing budget codes and settling all costs."),
           ("Release", "Formally freeing people and resources for other work."),
           ("Benefits review", "A later check, by the benefit owner, of whether the benefits arrived.")],
    code=dict(file="rotterdam/15-closing-report.md", note="accepted by the steering group, 22 May 2026 · project closed", plain=True, src="""
# ROTTERDAM LAUNCH · CLOSING REPORT                                         22 May 2026

              PROMISED (charter, baseline v2)     HAPPENED
DATE          opening 27 April                     opened 27 April
SCOPE         71 must-haves                        71 of 71 (2 fixed 24–26 Apr, after go /
                                                   no-go with conditions)
COST          €380k                                €379.6k (reserve €20k used: fridges €14k,
                                                   weekend work €5k, router €0.6k)
BENEFITS      500 orders a day by end May          590 a day in week 4 (18–24 May)   MET
              90 % express on time by end summer   84 % in May                        OPEN
              next city in ≤ 8 weeks               playbook v1 written; test: Utrecht OPEN
                                                   → owners Joost, Joost, Femke

CHANGES       6 raised: 4 approved, 1 rejected, 1 deferred     ISSUES  23 raised, 21 closed
WHAT WENT WRONG   no internet line at opening (I-07) · a promise restated wrongly (9 Mar) ·
                  builder 5 days late, recovered for €5k
CHECKLIST     [x] accepted: Yara, 15 May      [x] contracts closed, retention released
              [x] budget code closed (Marco)  [x] file archived · 21 lessons → changes
              [x] open items handed over      [x] team thanked and released

DECISION      steering group: CLOSED.  Sanne → the courier hiring drive, then Utrecht.
"""),
    tools="tools: the charter, a one-page report, a six-line checklist and a dinner.",
    dial=[("Light", "a small job", ["“Done, accepted, nothing open.”", "A thank-you.", "A line in the log."]),
          ("Standard", "Rotterdam", ["A one-page report against the charter.", "A six-line checklist.", "A decision by the steering group."]),
          ("Heavy", "large or contracted work", ["Formal acceptance certificates.", "Contract and financial audits.", "A post-implementation review months later."])],
    baseline="Each line compares <b>a project that goes quiet after go-live</b> to <b>a closing report against the charter, a checklist and a decision to close</b>.",
    ratings=[(2, 5, "Benefits are compared with the promise and given owners."),
             (3, 4, "Real cost and time feed the next estimate."),
             (2, 4, "No open invoices or orphaned promises."),
             (2, 5, "Promised against happened, on one page."),
             (3, 5, "The steering group sees the loop closed."),
             (3, 4, "The team hears “done”, and “thank you”."),
             (3, 3, "Neutral."),
             (3, 4, "Loose ends are tied."),
             (4, 3, "A page, a checklist, a meeting.")],
    pitfalls=[("Fading out", "Nobody says it's over.", "a decision to close."),
              ("Closing only the work", "Money and contracts stay open.", "settle them; close the code."),
              ("A report that only celebrates", "Nothing learned.", "include what went wrong."),
              ("No thank-you", "People remember.", "say it, specifically.")],
    use=["At the end of every project.", "At the end of every phase, in small.", "When a project is stopped early (close it properly too).", "When an old project “still has budget”."],
    skip=["Never. A cancelled project needs closing even more."],
    related=["<b>Should This Project Exist?</b> (this volume)", "<b>Who Looks After It Now?</b> (previous note)", "<b>What Did We Learn?</b> (this volume)", "<b>Post-launch review</b> (Grace, vol. 4)"],
    quiz=[("Finished or closed: “the store is open”?", "Finished. Closed needs acceptance, settlement and a decision."),
          ("What is the closing report compared against?", "The charter and the baseline."),
          ("One benefit is still open at closing. Is that a problem?", "No, if it has an owner and dates to check it. Benefits often arrive after the project."),
          ("Femke cancels a project halfway. Does it need closing?", "Yes: accept what exists, settle contracts and money, record why, release the team."),
          ("The on-time figure is 84 %, below the 90 % target. Should the report leave it out?", "No. It reports it as open, with the owner (Joost) and the check dates.")],
    try_it="Think of a project of yours that ended in the last year. Run the six-line checklist on it now: accepted, contracts, money, file, lessons, team. Which line is still open?",
    remember="Put out the <span class=\"hl\">fire</span>, pay the site, look back once. Then say <span class=\"hl\">thank you</span>.",
    sources=["Project Management Institute, <i>PMBOK Guide</i>, Eighth Edition (2025): Governance domain, closing a project or phase.",
             "Project Management Institute, <i>PMBOK Guide</i>, Sixth Edition (2017): 4.7 Close Project or Phase.",
             "Atul Gawande, <i>The Checklist Manifesto</i> (2009)."],
)

NOTES = [LESSONS, HANDOVER, CLOSING]
