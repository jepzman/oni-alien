# Series 2 · Book 5 · The IT Operations Notebook · Vol. 6 · Shaping the team.
# Narrator: Eli (he/him). Facts: docs/larder-casebook.md, "Book 5, Vol. 6".

# ------------------------------------------------------------------ 01 Who Runs What?
wr_problem = Doodle(760, 260, "Doodle of Larder in April 2028: 30 engineers in five product teams, and on-call spread unevenly. Ben's ordering team carries the pager for checkout, the most critical service, with five people. Dee's team has four people on a one-in-four rota for the apps. Eli and Bram carry the platform, and are everyone's escalation. Femke and Ana agree a reliability team is needed by the autumn, but nobody has decided what it would run.",
                    "Five product teams, uneven pagers, and Eli and Bram as everyone's escalation. A reliability team, running what?")
for i, (t, s) in enumerate([("Ordering", "5 · checkout pager"), ("Apps", "4 · 1-in-4 rota"), ("Payments + data", "6"), ("Business", "5"), ("Platform", "Eli + Bram · everyone's escalation")]):
    wr_problem.box(14 + i * 148, 30, 136, 110, t, "pink" if i == 4 else "y", sub=s, size=15, subsize=11)
wr_problem.note(380, 190, "“a reliability team by the autumn” · running what?", "red", size=18)

wr_analogy = Doodle(760, 220, "Doodle of a hospital deciding who runs what. Each ward runs its own beds, day and night, because it knows its patients. But intensive care has its own specialist team, because those patients need round-the-clock experts. Some patients move into intensive care only after a check that they need it, and move back out when they're stable.",
                    "Wards run their own beds; intensive care has a specialist team; patients move in after a check, and back out.")
wr_analogy.box(14, 40, 340, 100, "wards", "green", sub="run their own beds", size=19, subsize=15)
wr_analogy.box(406, 40, 340, 100, "intensive care", "pink", sub="a specialist team, after a check", size=19, subsize=14)
wr_analogy.note(380, 190, "who runs what depends on what the patient needs", "pen", size=18)

wr_how = Doodle(760, 400, "Larder's model, agreed on Monday 10 April 2028 with Femke, Ana and the tech leads. Product teams build and run their own services by default: their on-call, their SLOs, with help and tools from the reliability team. The reliability team (Eli as lead, Bram, and two SREs to hire) runs on-call for tier 1 services, starting with Ordering on 1 October, then Dispatch in 2029, but only after a production readiness review; the product team stays second line, fixes its own bugs and follows the error budget policy. The reliability team also owns the platform, observability, the incident process and the continuity plans. Either side can hand a service back if readiness drops or the budget is spent twice in a quarter.",
                "Build it, run it by default; the reliability team runs tier 1 after a readiness review; either side can hand back.")
wr_how.box(14, 14, 360, 140, None, "green")
wr_how.head(194, 44, "product teams", size=18)
wr_how.text(194, 76, "build + run their services", size=15)
wr_how.text(194, 102, "own on-call, own SLOs", size=15)
wr_how.text(194, 128, "help + tools from reliability", size=14)
wr_how.box(386, 14, 360, 140, None, "pink")
wr_how.head(566, 44, "reliability team", size=18)
wr_how.text(566, 76, "tier 1 on-call after a review", size=15)
wr_how.text(566, 102, "Ordering 1 Oct · Dispatch 2029", size=14)
wr_how.text(566, 128, "platform · observability · process", size=14)
wr_how.box(14, 176, 732, 60, "product team stays second line · fixes its bugs · error budget policy applies", "y", size=15)
wr_how.box(14, 252, 732, 60, "hand back if readiness drops or the budget is spent twice in a quarter", "paper", size=15)
wr_how.note(380, 350, "agreed Mon 10 Apr 2028 · Femke, Ana, tech leads, Eli", "pen", size=16)
wr_how.note(380, 386, "Eli leads the team: Bram + two SREs to hire", "pen", size=15)

WHO_RUNS_WHAT = dict(
    slug="who-runs-what",
    kicker="a.k.a. “operating models: you build it, you run it, or SRE?”",
    tldr="There are two classic answers to “who runs a service?”: <b>the team that builds it</b> (they know it best, and feel its pain) or <b>a specialist reliability team</b> (deep operational skill, round-the-clock cover). Most organisations need both: product teams run their own services by default, and a reliability team runs the most critical ones, <b>but only after a readiness review</b>, with the product team as second line and a <b>way to hand back</b>. Write the terms down.",
    chips=[("Family", "shaping the team"), ("Lives in", "ops/operating-model.md, agreed with Femke, Ana and the tech leads"), ("Pairs with", "production readiness, handing over the pager, error budgets (vol. 4)")],
    itil=dict(groups=["general"], chain=["plan", "design"], practices=["strategy management", "workforce and talent management", "service design"],
              sre="“SRE engagement models”; shared responsibility with product teams", principles=["Think and work holistically", "Collaborate and promote visibility"],
              older="ITIL v3: functions (technical, application and IT operations management)"),
    problem_side="Larder, April 2028",
    problem="""  <p class="lead">Larder now has <b>30 engineers in five product teams</b>, and on-call is uneven. Ben's ordering team carries the pager for checkout, the most critical service, with <b>five people</b>. Dee's team has <b>four</b> on a one-in-four rota for the apps. Eli and Bram carry the platform, and are <b>everyone's escalation</b>. Femke and Ana agree that Larder needs a <b>reliability team</b> by the autumn. <span class="hl-pink">Nobody has decided what it would actually run.</span></p>
  <ul>
    <li>A reliability team that runs everything becomes the new bottleneck.</li>
    <li>One that runs nothing is just another name for Eli and Bram.</li>
    <li>Product teams worry about losing ownership, or being left alone with it.</li>
  </ul>""",
    problem_figs=[wr_problem],
    analogy_side="wards and intensive care",
    analogy="""  <p>In a hospital, each <b>ward runs its own beds</b>, day and night, because it knows its patients. But <b>intensive care</b> has a specialist team, because those patients need round-the-clock experts. Patients move into intensive care only <b>after a check</b> that they need it, and back out when they're stable. Both sides know the terms.</p>""",
    analogy_figs=[wr_analogy],
    map=[("Wards running their own beds", "Product teams running their own services"),
         ("Intensive care", "The reliability team running tier 1"),
         ("The check before moving in", "A production readiness review"),
         ("Moving back out when stable", "Handing a service back"),
         ("The ward stays involved", "The product team as second line")],
    how_side="build it, run it by default; tier 1 to the reliability team, on terms",
    how="""  <p>On <b>Monday 10 April</b>, Eli proposes a model to Femke, Ana and the tech leads, and they agree it:</p>
  <ul>
    <li><b>By default</b>, product teams <b>build and run</b> their own services: their own on-call and SLOs, with tools, training and help from the reliability team.</li>
    <li>The <b>reliability team</b> (Eli as lead, Bram, and two SREs to hire) runs on-call for <b>tier 1 services</b>: Ordering from <b>1 October</b>, then Dispatch in 2029. That happens only after a <b>production readiness review</b>.</li>
    <li>The product team stays <b>second line</b>, fixes its own bugs, and the <b>error budget policy</b> still applies to it.</li>
    <li>The reliability team also owns the <b>platform, observability, the incident process and the continuity plans</b>.</li>
    <li>Either side can <b>hand a service back</b> if readiness drops or the error budget is spent twice in a quarter.</li>
  </ul>
  <p>Ben's first question is whether his team will still be woken up. The answer: only as second line, and less often. Dee asks whether her team can join later, and the answer is yes, through the same review.</p>""",
    how_figs=[wr_how],
    steps=[("List services by tier and current owner", "Who carries which pager today?"),
           ("Default to build it, run it", "Ownership stays with builders."),
           ("Give a specialist team the most critical", "After a readiness review."),
           ("Keep the product team as second line", "They fix their bugs; budgets still apply."),
           ("Write a way to hand back", "Conditions both sides agree."),
           ("Agree it with leadership and teams", "On one page.")],
    vocab=[("You build it, you run it", "The team that builds a service operates it, including on-call."),
           ("Reliability team (SRE team)", "A team specialised in running and improving critical services."),
           ("Engagement model", "The terms under which a reliability team takes on, helps with, or hands back a service."),
           ("Second line", "The team called by the first responder for deeper knowledge."),
           ("Hand-back", "Returning operational responsibility to the product team."),
           ("Platform team", "A team providing shared tools and infrastructure to others.")],
    code=dict(file="ops/operating-model.md", note="agreed Mon 10 April 2028", plain=True, src="""
# Who runs what at Larder

default        product teams build AND run their services (on-call, SLOs)
               reliability team helps: tools, training, reviews, incident process
reliability    runs on-call for tier 1 after a production readiness review
team           Ordering: 1 Oct 2028 · Dispatch: 2029 · payments: to decide
               owns: platform · observability · incident process · continuity plans
               people: Eli (lead) · Bram · 2 SREs (hire Jul, Aug)
terms          product team = second line · fixes its bugs · error budget policy applies
hand-back      readiness drops (review fails) OR budget spent twice in a quarter
               → 4 weeks' notice, joint plan
"""),
    tools="tools: the catalogue with tiers, a one-page operating model, and a meeting with leadership and every tech lead.",
    ladder=[("whoever is nearest", ["Pagers by accident.", "One or two heroes."]),
            ("a written model", ["Build it, run it by default.", "Tier 1 to reliability, on terms."]),
            ("engagement as a product", ["Clear menu: consult, help, run.", "Readiness reviews routine."]),
            ("teams choose", ["Product teams pick their level of help.", "Hand-backs rare and calm."])],
    ladder_now=1,
    baseline="Each line compares <b>pagers by accident and two heroes</b> to <b>a written model: build it, run it by default, tier 1 to a reliability team on terms</b>.",
    ratings=[(2, 3, "Tier 1 run by specialists."),
             (2, 3, "Readiness reviews before anyone takes a pager."),
             (3, 3, "Neutral."),
             (3, 3, "Neutral."),
             (2, 4, "Everyone knows who runs what, and why."),
             (3, 3, "Neutral."),
             (3, 3, "A team of four, funded."),
             (1, 4, "No more two-person escalation for everything."),
             (3, 3, "One page and one meeting.")],
    pitfalls=[("A reliability team for everything", "A new bottleneck; product teams stop caring.", "tier 1 only, after review."),
              ("No hand-back", "The reliability team is stuck with neglected services.", "write the conditions."),
              ("Product teams cut out", "They stop learning from production.", "second line, budgets apply."),
              ("Deciding without the teams", "Resistance from day one.", "agree it with every tech lead.")],
    use=["On-call is uneven or held by heroes.", "You're forming a reliability or platform team.", "Product teams ask who should run their service.", "Critical services need round-the-clock expertise."],
    skip=["Small organisations where one team runs everything well."],
    related=["<b>Is This Service Ready for Production?</b> (this volume)", "<b>Who Gets Woken Up?</b> (vol. 1)", "<b>When Do We Stop Shipping Features?</b> (vol. 4)", "<b>Handover to Operations</b> (Ana, vol. 6)"],
    quiz=[("What's Larder's default?", "Product teams build and run their own services."),
          ("What does the reliability team run?", "Tier 1 services' on-call (Ordering from 1 October), after a readiness review, plus platform, observability, incident process and continuity."),
          ("What stays with the product team?", "Second line, fixing its bugs, and the error budget policy."),
          ("When can a service be handed back?", "If readiness drops or the budget is spent twice in a quarter, with 4 weeks' notice."),
          ("Why not have the reliability team run everything?", "It becomes a bottleneck, and product teams stop learning from production.")],
    quiz_sit=[("Grace's new recipes feature team asks the reliability team to run its service from day one. What do you say?", "It's not tier 1, so by default the team runs it, with the reliability team's help (SLOs, alerts, runbooks). If it ever becomes tier 1, it can go through a readiness review.")],
    try_it="List your services by tier and who carries their pager today. Which are run by accident? Write a one-page model: who runs what by default, who runs the critical few, on what terms, and how to hand back.",
    remember="<span class=\"hl\">Build it, run it</span> by default; the critical few go to specialists <span class=\"hl\">after a check</span>, with the builders still close.",
    sources=["Betsy Beyer et al., <i>The Site Reliability Workbook</i> (2018): chapter 18, SRE engagement model.",
             "Matthew Skelton and Manuel Pais, <i>Team Topologies</i> (2019).",
             "AXELOS, <i>ITIL 4: Workforce and talent management</i> and <i>Strategy management</i> practice guides (2020)."],
)

# ------------------------------------------------------------------ 02 Hiring the First SREs
hs_problem = Doodle(760, 260, "Doodle of Eli's first draft of the job advert, April 2028: twenty-two technologies listed, '24/7 availability', 'rockstar', and an interview of three whiteboard rounds about algorithms. Ana reads it and asks: would you have got this job in 2025? Would Bram? Nothing in it tests what the job really is: staying calm in an incident, reading an unfamiliar system, automating handwork, and explaining things to stores.",
                    "Twenty-two technologies, “24/7”, three whiteboard rounds. Nothing about calm, curiosity or explaining things.")
hs_problem.box(14, 30, 230, 100, "22 technologies", "pink", size=19)
hs_problem.box(264, 30, 230, 100, "“24/7, rockstar”", "pink", size=19)
hs_problem.box(514, 30, 232, 100, "3 × whiteboard", "pink", sub="algorithms", size=19, subsize=14)
hs_problem.note(380, 180, "Ana: “would you have got this job?”", "red", size=19)

hs_analogy = Doodle(760, 220, "Doodle of hiring a chef. A restaurant can ask a cook to list every dish they know, or it can ask them to cook a service: two hours in the real kitchen, a busy moment, a missing ingredient, a dish sent back. The second shows calm, skill and taste; the first shows memory.",
                    "Don't ask the cook to list dishes. Ask them to cook a short service, with a dish sent back.")
hs_analogy.icon("kitchen", 60, 50, 1.2)
hs_analogy.box(170, 40, 270, 100, "list every dish", "pink", sub="tests memory", size=18, subsize=14)
hs_analogy.box(470, 40, 276, 100, "cook a short service", "green", sub="tests calm, skill, taste", size=18, subsize=14)
hs_analogy.note(450, 190, "the sample should look like the job", "pen", size=18)

hs_how = Doodle(760, 400, "Larder's SRE hiring, May and June 2028. A role card on one page: what the job is (run tier 1 with others, automate toil, lead incidents, teach), what matters (calm, curiosity, writing code to remove handwork, explaining clearly), on-call one week in four with pay and rest, and what doesn't matter (any particular tool). 61 applicants, 12 screening calls, 5 work samples: a real past incident's timeline to talk through, and a broken staging service to investigate for 90 minutes with Bram, thinking aloud. Panel: Eli, Bram, Ana; scoring sheet written before the first interview. Hired: Lotte (she/her), from a logistics company's platform team, starting Monday 3 July; and Yusuf (he/him), from a bank's operations team, starting Tuesday 1 August.",
                "A one-page role card, a work sample that looks like the job, a scoring sheet first. Hired: Lotte and Yusuf.")
hs_how.box(14, 14, 236, 120, "role card", "blue", sub="the job · what matters · on-call · not tools", size=18, subsize=11)
hs_how.box(262, 14, 236, 120, "work sample", "green", sub="a real incident · a broken service · 90 min", size=18, subsize=11)
hs_how.box(510, 14, 236, 120, "scoring sheet", "y", sub="written before interview 1", size=18, subsize=12)
hs_how.row([("61", "applicants", "paper"), ("12", "screening calls", "paper"), ("5", "work samples", "paper"), ("2", "hired", "green")], x=14, y=160, h=80, gap=36, size=22, subsize=12, arrows=True)
hs_how.row([("Lotte (she/her)", "logistics platform · Mon 3 Jul", "green"), ("Yusuf (he/him)", "bank operations · Tue 1 Aug", "green")], x=14, y=270, h=90, w=356, gap=20, size=18, subsize=13)

HIRING_SRES = dict(
    slug="hiring-sres",
    kicker="a.k.a. “workforce and talent management: hiring”",
    tldr="Hire operations engineers for <b>what the job really is</b>: staying calm in an incident, reading unfamiliar systems, writing code that removes handwork, and explaining clearly. A long list of tools filters out good people and tests nothing. Write a <b>one-page role card</b>, use a <b>work sample that looks like the job</b> (a real incident to talk through, a broken service to investigate), and write the <b>scoring sheet before the first interview</b>.",
    chips=[("Family", "shaping the team"), ("Lives in", "ops/hiring/sre-role-card.md, the work sample, the scoring sheet"), ("Pairs with", "growing operations engineers, humane on-call, Sanne's hiring note")],
    itil=dict(groups=["general"], chain=["plan", "build"], practices=["workforce and talent management"],
              sre="(hiring SREs: systems thinking, coding, calm under pressure)", principles=["Focus on value", "Keep it simple and practical"],
              older="ITIL v3: (not covered as a practice)"),
    problem_side="Larder, April 2028",
    problem="""  <p class="lead">Eli's first draft of the job advert lists <b>twenty-two technologies</b>, asks for <b>“24/7 availability”</b>, uses the word “rockstar”, and plans <b>three whiteboard rounds about algorithms</b>. Ana reads it and asks: <b>would you have got this job in 2025? Would Bram?</b> <span class="hl-pink">Nothing in it tests what the job really is</span>: staying calm in an incident, reading an unfamiliar system, automating handwork, and explaining things to a store lead at 07:00.</p>
  <ul>
    <li>Tool lists filter out people who learn fast.</li>
    <li>“24/7” scares off exactly the people who'd make on-call sustainable.</li>
    <li>Whiteboard puzzles measure interview skill, not incident skill.</li>
  </ul>""",
    problem_figs=[hs_problem],
    meanwhile=[("project-6", "hiring-a-project-manager", "Sanne's hiring of Nadia (Nov–Dec 2027): a role card, 34 applicants, work samples from Antwerp's real status and issue log, a scoring sheet written first.",
                "Eli copies the shape for SREs: a real past incident's timeline and a broken staging service as the work sample.")],
    analogy_side="hiring a chef",
    analogy="""  <p>A restaurant can ask a cook to <b>list every dish they know</b>, or it can ask them to <b>cook a short service</b>: two hours in the real kitchen, a busy moment, a missing ingredient, a dish sent back. The second shows calm, skill and taste. The first only shows memory.</p>""",
    analogy_figs=[hs_analogy],
    map=[("Listing every dish", "A list of 22 technologies"),
         ("Cooking a short service", "Investigating a broken staging service for 90 minutes"),
         ("A dish sent back", "Talking through a real past incident"),
         ("Calm, skill, taste", "Calm, curiosity, automation, clear explanation"),
         ("The head chef's scoring card", "The scoring sheet, written first")],
    how_side="a role card, a realistic work sample, a scoring sheet first",
    how="""  <p>Eli rewrites the process in <b>May</b>, borrowing the shape of Sanne's hiring:</p>
  <ul>
    <li><b>A one-page role card</b>: the job (run tier 1 with others, automate toil, lead incidents, teach the product teams), <b>what matters</b> (calm, curiosity, writing code to remove handwork, explaining clearly), on-call <b>one week in four, paid, with rest</b>, and <b>what doesn't matter</b>: any particular tool.</li>
    <li><b>A work sample that looks like the job</b>: talk through the timeline of a <b>real past incident</b> (the 29 October 2026 network rule, names removed), then investigate a <b>broken staging service</b> for 90 minutes with Bram, thinking aloud.</li>
    <li><b>A scoring sheet written before the first interview</b>, with Eli, Bram and Ana as the panel.</li>
  </ul>
  <p><b>61 applicants, 12 screening calls, 5 work samples.</b> Two are hired. <b>Lotte</b> (she/her), from a logistics company's platform team, found the broken service's cause in 40 minutes and explained it as if to a store lead. She starts on <b>Monday 3 July</b>. <b>Yusuf</b> (he/him), from a bank's operations team, asked the best questions about the incident timeline, and starts on <b>Tuesday 1 August</b>.</p>""",
    how_figs=[hs_how],
    steps=[("Write what the job really is", "Day to day, and at 3 a.m."),
           ("Name what matters, and what doesn't", "Qualities over tools."),
           ("Be honest about on-call", "Frequency, pay, rest."),
           ("Design a work sample like the job", "A real incident; a broken service."),
           ("Write the scoring sheet first", "Before meeting anyone."),
           ("Panel of people they'll work with", "Including someone outside the team.")],
    vocab=[("Role card", "A one-page description of a job, its purpose and what matters."),
           ("Work sample", "A task from the real job, done as part of the interview."),
           ("Scoring sheet", "Criteria and scales, agreed before interviews, to judge fairly."),
           ("Structured interview", "The same questions and criteria for every candidate."),
           ("Culture add", "Hiring people who bring something the team lacks, not more of the same."),
           ("Onboarding", "Helping a new person become effective (next notes).")],
    code=dict(file="ops/hiring/sre-role-card.md", note="May 2028", plain=True, src="""
# Site reliability engineer · Larder                       reliability team · Amsterdam

the job        run Larder's most critical services with three colleagues
               automate the handwork you find · lead incidents calmly
               teach product teams (SLOs, alerts, runbooks)
what matters   calm under pressure · curiosity about unfamiliar systems
               writing code that removes toil · explaining clearly to non-engineers
on-call        one week in four · €300/week · paged after midnight → start at noon
not required   any particular tool or cloud · a degree
work sample    1 talk through a real past incident's timeline (45 min)
               2 a broken staging service: find out what's wrong, thinking aloud (90 min)
scoring        written 9 May · panel: Eli, Bram, Ana
result         61 applicants → 12 calls → 5 samples → Lotte (3 Jul) · Yusuf (1 Aug)
"""),
    tools="tools: a role card, a staging service you can break on purpose, an anonymised incident timeline, a scoring sheet.",
    ladder=[("tool lists and puzzles", ["Hiring for memory.", "On-call hidden."]),
            ("role card, work sample, scoring sheet", ["Realistic and fair.", "Honest about on-call."]),
            ("hiring as a team habit", ["Interviewers trained.", "Samples refreshed from real incidents."]),
            ("hiring that diversifies the team", ["Track where hires come from.", "Grow people internally too."])],
    ladder_now=1,
    baseline="Each line compares <b>a tool list and whiteboard puzzles</b> to <b>a role card, a realistic work sample and a scoring sheet written first</b>.",
    ratings=[(3, 3, "Neutral."),
             (3, 3, "Neutral."),
             (3, 3, "Neutral."),
             (3, 3, "Neutral."),
             (3, 3, "Neutral."),
             (3, 3, "Neutral."),
             (3, 3, "Two hires in two months."),
             (1, 4, "Two more people who can run tier 1."),
             (3, 3, "About 30 hours of panel time.")],
    pitfalls=[("Tool lists", "Good learners filtered out.", "qualities over tools."),
              ("Hiding on-call", "New hires leave after their first rota.", "be honest: frequency, pay, rest."),
              ("Puzzles instead of the job", "You hire interview experts.", "a work sample like the job."),
              ("Scoring after the interview", "Gut feeling wins.", "the sheet comes first.")],
    use=["You're hiring for operations or SRE.", "Job adverts list tools, not the job.", "Interviews don't predict who does well.", "A new team is forming."],
    skip=["Short contracts for a narrow, well-defined task."],
    related=["<b>Who Do We Hire?</b> (Sanne, vol. 6)", "<b>Hiring a Product Owner</b> (Grace, vol. 6)", "<b>Growing Operations Engineers</b> (this volume)", "<b>On-Call People Can Live With</b> (next note)"],
    quiz=[("What was wrong with the first advert?", "22 technologies, “24/7”, “rockstar” and whiteboard puzzles: nothing about what the job really is."),
          ("What's in the SRE role card?", "The job, what matters (calm, curiosity, automation, explaining), honest on-call terms, and what isn't required."),
          ("What was the work sample?", "Talking through a real past incident's timeline, and investigating a broken staging service for 90 minutes with Bram."),
          ("When was the scoring sheet written?", "Before the first interview (9 May)."),
          ("Who was hired, and when do they start?", "Lotte (she/her) on 3 July and Yusuf (he/him) on 1 August.")],
    quiz_sit=[("A candidate knows every tool on your stack but blames others when talking through the incident timeline. Another knows half the tools but asks what made each decision make sense. Who scores higher?", "The second, on the criteria that matter: curiosity and blameless thinking. Tools can be learned in weeks; how someone thinks about incidents is much harder to teach.")],
    try_it="Write a one-page role card for an operations role: what the job is, what matters, the honest on-call terms, and what isn't required. Then design a 90-minute work sample from a real incident of yours.",
    remember="Hire for <span class=\"hl\">calm, curiosity and clear explanation</span>, and test it with <span class=\"hl\">a sample that looks like the job</span>.",
    sources=["Laszlo Bock, <i>Work Rules!</i> (2015): structured interviews and work samples.",
             "Betsy Beyer et al., <i>Site Reliability Engineering</i> (2016): chapter 1, hiring SREs.",
             "AXELOS, <i>ITIL 4: Workforce and talent management</i> practice guide (2020)."],
)

# ------------------------------------------------------------------ 03 On-Call People Can Live With
hc_problem = Doodle(760, 260, "Doodle of Larder's on-call load measured for the first time in May 2028, across all rotas. Dee's apps team: four people, one week in four, 9 night pages a month, two people saying they'd leave rather than do another year. Ordering: five people, 6 night pages a month. The platform rota of Eli and Bram: one week in two. Across Larder, 31 night pages a month.",
                    "Measured for the first time: 31 night pages a month, a one-in-four rota with 9 of them, and people ready to leave.")
hc_problem.row([("Apps", "4 people · 9 nights/month", "pink"), ("Ordering", "5 people · 6 nights", "y"), ("Platform", "Eli + Bram · 1 in 2", "pink")], y=30, h=100, gap=20, size=19, subsize=13)
hc_problem.note(380, 180, "31 night pages a month across Larder", "red", size=19)
hc_problem.note(380, 216, "two people: “I'd leave rather than another year”", "pen", size=16)

hc_analogy = Doodle(760, 220, "Doodle of a fire station's rota. Enough firefighters that each does a sensible number of night shifts. When call-outs at night keep coming from the same faulty alarm in one building, the station fixes the alarm with the building's owner instead of asking firefighters to be tougher.",
                    "Enough people for sensible nights, and when one faulty alarm keeps calling, fix the alarm, not the people.")
hc_analogy.icon("bell", 60, 50, 1.3)
hc_analogy.box(170, 40, 270, 100, "enough people", "green", sub="sensible night shifts", size=18, subsize=14)
hc_analogy.box(470, 40, 276, 100, "fix the faulty alarm", "y", sub="not tougher firefighters", size=18, subsize=14)
hc_analogy.note(450, 190, "the load is a design problem", "pen", size=18)

hc_how = Doodle(760, 400, "Larder's on-call rules from June 2028, for every rota. Measured monthly per rota: pages per shift, night pages, hours worked out of hours. Limits: at least six people per rota, or rotas merge; on average no more than two night pages per week-long shift; above that, the noisiest alerts go to the monthly pager review and get fixed before new features. Pay: 300 euros a week as primary (Marco agreed, up from 200); time back for any night work; paged after midnight, start at noon. Dee's apps rota merges with the business team's into one of eight people. The platform rota becomes the reliability team's four-person rota when Yusuf joins. September: night pages across Larder 12 a month, down from 31; nobody planning to leave over on-call.",
                "Measure load per rota; at least six people; cap night pages; fix the noisiest alerts first; pay and rest fairly.")
hc_how.box(14, 14, 236, 110, "measure", "blue", sub="pages · nights · hours, per rota", size=19, subsize=12)
hc_how.box(262, 14, 236, 110, "limits", "y", sub="≥ 6 people · ≤ 2 nights / shift", size=19, subsize=12)
hc_how.box(510, 14, 236, 110, "pay + rest", "green", sub="€300 / week · time back", size=19, subsize=13)
hc_how.box(14, 150, 732, 64, "over the limit → noisiest alerts fixed before new features (monthly pager review)", "pink", size=14)
hc_how.box(14, 230, 732, 64, "apps + business rotas merged (8 people) · platform → reliability rota (4, from Aug)", "paper", size=14)
hc_how.row([("May", "31 night pages", "pink"), ("Sep", "12 night pages", "green")], x=110, y=312, h=70, w=250, gap=40, size=18, subsize=15, arrows=True)

HUMANE_ON_CALL = dict(
    slug="humane-on-call",
    kicker="a.k.a. “sustainable on-call”",
    tldr="On-call is sustainable when it's <b>measured</b> (pages, night pages and hours, per rota), <b>limited</b> (enough people on each rota, a cap on night pages), and <b>fairly paid and rested</b>. When a rota goes over its limit, the fix is to <b>change the system</b> (the noisiest alerts get fixed before new features), not to ask people to be tougher. People leave over on-call long before they say so.",
    chips=[("Family", "shaping the team"), ("Lives in", "ops/on-call.md (all rotas); a monthly pager review"), ("Pairs with", "the on-call rota (vol. 1), alert hygiene (vol. 1), error budgets (vol. 4)")],
    itil=dict(groups=["general", "service"], chain=["improve", "deliver"], practices=["workforce and talent management", "incident management", "monitoring and event management"],
              sre="“balanced on-call”: at most ~2 incidents per shift; at most 25 % of time on call", principles=["Focus on value", "Optimise and automate"],
              older="ITIL v3: (not covered)"),
    problem_side="Larder, May 2028",
    problem="""  <p class="lead">In May, Eli measures on-call load across every rota for the first time. <b>Dee's apps team</b>: four people, one week in four, <b>9 night pages a month</b>, and two people quietly saying they'd leave rather than do another year. <b>Ordering</b>: five people, 6 night pages a month. The <b>platform</b> rota of Eli and Bram: one week in two. <span class="hl-pink">Across Larder: 31 night pages a month</span>, and nobody had counted them.</p>
  <ul>
    <li>Small rotas mean frequent weeks and frequent nights.</li>
    <li>Noisy alerts become a tax on sleep.</li>
    <li>The cost shows up as resignations, not tickets.</li>
  </ul>""",
    problem_figs=[hc_problem],
    analogy_side="the fire station's nights",
    analogy="""  <p>A fire station keeps <b>enough firefighters</b> that each does a sensible number of night shifts. When night call-outs keep coming from <b>the same faulty alarm</b> in one building, the station gets the building's owner to <b>fix the alarm</b>. It doesn't ask its firefighters to be tougher.</p>""",
    analogy_figs=[hc_analogy],
    map=[("Enough firefighters", "At least six people per rota"),
         ("A sensible number of nights", "No more than two night pages per week-long shift on average"),
         ("The faulty alarm", "The noisiest alerts on a rota"),
         ("Fixing it with the owner", "Noisy alerts fixed before new features"),
         ("Pay and time off", "€300 a week, time back after nights")],
    how_side="measure, limit, pay and rest, and fix the system when it's over",
    how="""  <p>From <b>June</b>, the same rules apply to every rota at Larder:</p>
  <ul>
    <li><b>Measure monthly</b>, per rota: pages per shift, night pages, hours worked out of hours.</li>
    <li><b>Limits</b>: at least <b>six people</b> per rota, or rotas merge; on average <b>no more than two night pages</b> per week-long shift.</li>
    <li><b>Over the limit</b>: the noisiest alerts go to a monthly <b>pager review</b> and are fixed <b>before new features</b>, much like the error budget policy.</li>
    <li><b>Pay and rest</b>: <b>€300 a week</b> as primary (Marco agrees, up from €200), time back for any night work, and the old rule: paged after midnight, start at noon.</li>
  </ul>
  <p>Dee's apps rota <b>merges</b> with the business team's into one rota of <b>eight</b>. The platform rota becomes the reliability team's four-person rota when Yusuf joins in August. The pager review fixes eleven noisy alerts in two months. By <b>September</b>, night pages across Larder are down to <b>12 a month</b> from 31, and the two people who'd planned to leave are still there.</p>""",
    how_figs=[hc_how],
    steps=[("Measure load per rota", "Pages, nights, hours, monthly."),
           ("Set limits", "People per rota; night pages per shift."),
           ("Merge small rotas", "Six or more people each."),
           ("Fix noisy alerts first when over the limit", "Before new features."),
           ("Pay and rest fairly", "Money for the week, time back for nights."),
           ("Ask people directly", "Load numbers miss how it feels.")],
    vocab=[("On-call load", "How much on-call costs people: pages, nights, hours."),
           ("Night page", "A page between 23:00 and 07:00."),
           ("Pager review", "A monthly look at what paged, and what to fix."),
           ("Rota size", "How many people share a rota; it sets how often each is on call."),
           ("Compensation", "Pay and time back for being on call."),
           ("Burnout", "Exhaustion from sustained stress; often the hidden cost of on-call.")],
    code=dict(file="ops/on-call.md#load", note="rules from June 2028 · all rotas", plain=True, src="""
rota            people  pages/shift  night pages/month   May → Sep
apps + business 8       3.1 → 1.4    9 → 3               merged 12 Jun
ordering        5 → 6   2.4 → 1.2    6 → 2               (+ Jonas's team engineer)
platform →      2 → 4   4.0 → 1.6    11 → 4              Lotte (Jul) · Yusuf (Aug)
  reliability
… all rotas                          31 → 12

limits    ≥ 6 people per rota · ≤ 2 night pages per shift (average, monthly)
over      → monthly pager review: noisiest alerts fixed before features
pay       €300/week primary (Marco, 6 Jun) · time back for night work
          paged after 00:00 → start at 12:00
"""),
    tools="tools: the paging tool's reports, a monthly pager review, the alert rules, and a conversation with each rota.",
    ladder=[("load unknown", ["Small rotas, noisy nights.", "People leave silently."]),
            ("measured, limited, paid", ["Six-plus per rota.", "Noisy alerts fixed first."]),
            ("load drives priorities", ["On-call cost in every service review.", "New services must meet the limits."]),
            ("quiet nights by design", ["Night pages rare.", "Rotas easy to staff."])],
    ladder_now=1,
    baseline="Each line compares <b>unmeasured on-call on small rotas</b> to <b>measured load, limits, fair pay and fixing the system first</b>.",
    ratings=[(3, 3, "Neutral."),
             (2, 3, "Noisy alerts fixed, often real problems."),
             (3, 3, "Neutral."),
             (3, 3, "Neutral."),
             (2, 4, "Every rota's load is known."),
             (2, 3, "Eleven noisy alerts fixed."),
             (2, 3, "Pay up; resignations avoided."),
             (1, 4, "31 → 12 night pages a month."),
             (3, 3, "A monthly review.")],
    pitfalls=[("Asking people to be tougher", "They leave instead.", "fix the system."),
              ("Tiny rotas", "One week in four, or two.", "six or more; merge if needed."),
              ("Pay without fixes", "Paid to be woken up for nothing.", "fix noisy alerts first."),
              ("Only numbers", "Load can be fine and still feel awful.", "ask people directly.")],
    use=["On-call load is unmeasured.", "Rotas are small.", "People hint they'll leave.", "Before giving any team a new pager."],
    skip=["Teams with no out-of-hours duties."],
    related=["<b>Who Gets Woken Up?</b> (vol. 1)", "<b>Which Alerts Deserve a Human?</b> (vol. 1)", "<b>When Do We Stop Shipping Features?</b> (vol. 4)", "<b>Hiring the First SREs</b> (this volume)"],
    quiz=[("What's measured, per rota?", "Pages per shift, night pages, hours worked out of hours."),
          ("What are Larder's limits?", "At least six people per rota; on average no more than two night pages per shift."),
          ("What happens over the limit?", "The noisiest alerts are fixed before new features, via the monthly pager review."),
          ("How did pay change?", "€300 a week as primary, up from €200, plus time back for night work."),
          ("What was the result?", "Night pages across Larder fell from 31 to 12 a month.")],
    quiz_sit=[("A rota is over its night-page limit, but the team has a feature deadline in two weeks. What happens?", "The rule says the noisiest alerts are fixed first; the team lead can ask Femke for an exception, in writing, like the error budget policy. Usually two or three alert fixes take a day and save the next month's nights.")],
    try_it="Count last month's pages for one rota: how many at night, per person? How many people share the rota? Find the single alert that woke people most, and fix it or demote it this week.",
    remember="On-call load is a <span class=\"hl\">design problem</span>. Measure it, limit it, pay for it, and <span class=\"hl\">fix the alarm, not the people</span>.",
    sources=["Betsy Beyer et al., <i>Site Reliability Engineering</i> (2016): chapter 11, being on-call.",
             "Betsy Beyer et al., <i>The Site Reliability Workbook</i> (2018): chapter 8, on-call.",
             "Christina Maslach and Michael Leiter, <i>The Burnout Challenge</i> (2022)."],
)

NOTES = [WHO_RUNS_WHAT, HIRING_SRES, HUMANE_ON_CALL]
