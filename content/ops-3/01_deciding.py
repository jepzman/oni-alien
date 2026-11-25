# Series 2 · Book 5 · The IT Operations Notebook · Vol. 3 · Deciding about changes.
# Narrator: Eli (he/him). Facts: docs/larder-casebook.md, "Book 5, Vol. 3".

# ------------------------------------------------------------------ 01 Which Changes Need a Second Look?
ct_problem = Doodle(760, 260, "Doodle of Eli's count of Larder's changes in December 2026: 212. 160 deploys through the pipeline, 31 infrastructure and network changes, 21 feature flag changes. Every one was handled the same way: whoever made it decided how careful to be. Between October and December, 9 incidents followed a change; 7 of them were infrastructure or network changes, which are 15 percent of all changes.",
                    "212 changes in December, all treated alike. The risky 15 % caused most of the trouble.")
ct_problem.row([("160", "deploys", "blue"), ("31", "infrastructure + network", "pink"), ("21", "feature flags", "y")], x=14, y=30, h=96, w=232, gap=18, size=28, subsize=14)
ct_problem.note(380, 170, "Oct–Dec: 9 incidents after changes · 7 of them infra/network", "red", size=17)
ct_problem.note(380, 210, "“how careful?” decided by whoever made the change", "pen", size=17)

ct_analogy = Doodle(760, 230, "Doodle of a hospital's medicine rules. Paracetamol from the ward cupboard: a nurse gives it by a standing order, no doctor needed. A new antibiotic: a doctor prescribes it and a pharmacist checks it. In a cardiac arrest: the crash team acts at once and writes it up afterwards. Three paths, chosen by risk, not by who is asking.",
                    "Standing orders for the routine, a second check for the risky, a crash team for the emergency.")
ct_analogy.row([("paracetamol", "standing order", "green"), ("new antibiotic", "doctor + pharmacist", "y"), ("cardiac arrest", "act now, write later", "pink")], y=40, h=96, gap=20, size=18, subsize=14)
ct_analogy.note(380, 196, "the path is chosen by risk, not by who's asking", "pen", size=18)

ct_how = Doodle(760, 380, "Larder's three kinds of change from Monday 18 January 2027. Standard: one of 9 pre-approved recipes, such as a deploy through the pipeline with a canary, a feature flag outside a critical window, enrolling a device, a new user through the joiners checklist; they go straight ahead and are logged by the change feed. Normal: anything else; a risk score, a reviewer who knows the system, and a tested way back. Emergency: to restore service during an incident; the incident lead approves, two people do it, it is written up within a day. February: 87 percent standard, 12 percent normal, 1 percent emergency.",
                "Three paths. Most changes are standard and go fast; normal ones get a real second look.")
for i, (t, s, f) in enumerate([("standard", "9 recipes · go · logged", "green"), ("normal", "risk score · reviewer · undo", "y"), ("emergency", "lead approves · 2 people · write up", "pink")]):
    ct_how.box(14 + i * 248, 14, 236, 120, t, f, sub=s, size=22, subsize=13)
ct_how.row([("87 %", "standard (Feb)", "green"), ("12 %", "normal", "y"), ("1 %", "emergency", "pink")], x=14, y=170, h=90, w=236, gap=12, size=26, subsize=14)
ct_how.note(380, 300, "a recipe becomes standard after 10 clean runs", "pen", size=17)
ct_how.note(380, 340, "anything that isn't a recipe is normal, however small it feels", "red", size=16)

CHANGE_TYPES = dict(
    slug="change-types",
    kicker="a.k.a. “change enablement”",
    tldr="Not every change deserves the same care. Sort them into three kinds. <b>Standard</b> changes are low-risk, repeated recipes that are <b>pre-approved</b> and just go. <b>Normal</b> changes get a risk score, a <b>reviewer who knows the system</b> and a tested way back. <b>Emergency</b> changes restore service during an incident, with fewer checks but never none. Most changes become fast and boring, and the risky few get real attention.",
    chips=[("Family", "deciding about changes"), ("Lives in", "ops/changes/recipes.md and the pipeline"), ("Pairs with", "the change feed (vol. 2), risk scoring, the change calendar")],
    itil=dict(groups=["service"], chain=["design", "build", "deliver"], practices=["change enablement"],
              sre="“progressive rollouts”; ~70 % of outages follow a change", principles=["Optimise and automate", "Keep it simple and practical"],
              older="ITIL v3: change management (standard, normal, emergency changes)"),
    problem_side="Larder, January 2027",
    problem="""  <p class="lead">After the Christmas failover Eli counts December's changes: <b>212</b>. That's 160 deploys through the pipeline, 31 infrastructure and network changes, and 21 feature-flag changes. Each one was handled however its author thought best. From October to December, <b>9 incidents</b> followed a change, and <span class="hl-pink">7 of them were infrastructure or network changes, which are only 15 % of all changes</span>. One was the 29 October network rule.</p>
  <ul>
    <li>Risky changes get the same casual treatment as routine deploys.</li>
    <li>Routine changes sometimes get stuck waiting for someone to look.</li>
    <li>Nobody can say which changes need a second pair of eyes.</li>
  </ul>""",
    problem_figs=[ct_problem],
    analogy_side="the hospital's medicine rules",
    analogy="""  <p>On a hospital ward, a nurse gives <b>paracetamol by a standing order</b>, with no doctor needed. A <b>new antibiotic</b> needs a doctor's prescription and a pharmacist's check. In a <b>cardiac arrest</b> the crash team acts at once and writes it up afterwards. The path is chosen by <b>risk</b>, not by who's asking or how busy the ward is.</p>""",
    analogy_figs=[ct_analogy],
    map=[("Paracetamol by standing order", "A standard change: a pre-approved recipe"),
         ("Doctor + pharmacist", "A normal change: risk score + a reviewer who knows the system"),
         ("The crash team", "An emergency change during an incident"),
         ("Writing it up afterwards", "The emergency change recorded within a day"),
         ("The standing-order list", "ops/changes/recipes.md: 9 recipes")],
    how_side="three paths, and most changes on the fast one",
    how="""  <p>From <b>Monday 18 January</b> every change takes one of three paths:</p>
  <ul>
    <li><b>Standard</b>: one of <b>9 recipes</b>, written and pre-approved. Examples: a deploy through the pipeline with a canary, a feature flag outside a critical window, enrolling a device, a new user through the joiners checklist, adding a DNS record. These go straight ahead, and the change feed logs them. A new recipe becomes standard after <b>10 clean runs</b>.</li>
    <li><b>Normal</b>: anything that isn't a recipe, however small it feels. It needs a <b>risk score</b> (this volume), a <b>reviewer who knows that system</b>, and a <b>tested way back</b>.</li>
    <li><b>Emergency</b>: a change to restore service during an incident. The incident lead approves, <b>two people</b> do it, and it's written up within a day (this volume).</li>
  </ul>
  <p>In February the split is <b>87 % standard, 12 % normal, 1 % emergency</b>. Network and database changes are never recipes. If PR 233 came today, it would be a normal change.</p>""",
    how_figs=[ct_how],
    steps=[("Count your changes by kind", "Deploys, infrastructure, network, flags, vendors."),
           ("Find the incidents that followed changes", "Which kinds are risky in practice?"),
           ("Write recipes for the safe, repeated ones", "Pre-approved: they just go."),
           ("Everything else is normal", "Risk score, a knowing reviewer, a tested way back."),
           ("Define the emergency path", "Fewer checks, never zero, written up after."),
           ("Promote recipes after clean runs", "And demote one that causes an incident.")],
    vocab=[("Change", "Adding, modifying or removing anything that could affect a service."),
           ("Standard change", "Low-risk, repeated, pre-approved; follows a recipe."),
           ("Normal change", "Needs assessment and authorisation before it's made."),
           ("Emergency change", "Must be made as soon as possible, usually to restore service."),
           ("Change authority", "Whoever may approve a kind of change: at Larder, a knowing reviewer."),
           ("Recipe", "The written steps for a standard change.")],
    code=dict(file="ops/changes/recipes.md", note="the 9 standard changes · from Mon 18 January 2027", plain=True, src="""
# Standard changes (pre-approved · logged by the change feed)

R1  deploy an app through the pipeline (canary 5 % → 100 %)   not in a critical window
R2  turn a feature flag on/off (except ADR 0017 flags)        not in a critical window
R3  enrol / wipe a device in MDM                              any time
R4  joiner / mover / leaver (ops/jml.md)                      any time
R5  add a DNS record (never change or delete one)             not in a critical window
R6  scale Dispatch copies 2–6                                 any time
R7  rotate a certificate via auto-renew                       any time
R8  add a store to monitoring and on-call                     any time
R9  publish a known-error entry                               any time

Never standard: network rules · database settings · failover config · anything first-time
New recipe → standard after 10 clean runs · a recipe that causes an incident → normal again
"""),
    tools="tools: a recipes file, the pipeline (which already enforces most of R1), and the change feed for the log.",
    ladder=[("everyone decides alone", ["No kinds of change.", "Risky and routine treated the same."]),
            ("three paths, written recipes", ["Most changes standard.", "Normal ones reviewed by someone who knows."]),
            ("the pipeline knows the path", ["Recipes enforced in the pipeline.", "Normal changes can't merge without score and reviewer."]),
            ("most change is standard", ["Risky changes split into safe recipes.", "Normal changes rare."])],
    ladder_now=1,
    baseline="Each line compares <b>212 changes handled however their author liked</b> to <b>three paths with 9 pre-approved recipes</b>.",
    ratings=[(3, 3, "Neutral on its own."),
             (2, 3, "The risky 15 % get a real second look."),
             (3, 3, "Neutral."),
             (2, 4, "Network and database changes always reviewed."),
             (2, 4, "Every change has a known path."),
             (3, 4, "Routine changes stop waiting."),
             (3, 3, "Neutral."),
             (2, 3, "Fewer surprises after other people's changes."),
             (3, 4, "Most changes need no meeting at all.")],
    pitfalls=[("Treating all changes the same", "Either everything waits, or nothing is checked.", "three paths by risk."),
              ("“It's small, so it's standard”", "Small network changes stop cities.", "only written recipes are standard."),
              ("Recipes that never change", "A recipe that caused an incident stays pre-approved.", "demote it to normal."),
              ("No emergency path", "People skip the process entirely under pressure.", "a light path, written in advance.")],
    use=["Incidents follow changes.", "Some changes wait for days, others aren't checked at all.", "After an outage, when people want to “approve everything”.", "Before adding a change board."],
    skip=["A tiny team deploying one app: a pipeline with tests and a canary may be all you need."],
    related=["<b>Was It a Change?</b> (vol. 2)", "<b>Do We Need a Change Board?</b> (next note)", "<b>How Risky Is This Change?</b> (this volume)", "<b>Canary Releases</b> (cloud, vol. 6)"],
    quiz=[("What makes a change standard?", "It's low-risk and repeated, follows a written recipe, and is pre-approved."),
          ("What does a normal change need at Larder?", "A risk score, a reviewer who knows that system, and a tested way back."),
          ("When is a change an emergency change?", "When it must be made at once, usually to restore service during an incident."),
          ("Why are network changes never standard?", "They caused most change-related incidents, including 29 October."),
          ("How does a recipe become standard?", "After 10 clean runs; and it's demoted again if it causes an incident.")],
    quiz_sit=[("Dee wants to change a database setting “just slightly” on a Tuesday afternoon. It isn't a recipe. Which path?", "Normal: a risk score, a reviewer who knows the database (Eli or Bram), and a tested way back, however small it feels.")],
    try_it="Count last month's changes by kind and mark which ones were followed by an incident. Write three recipes for your safest, most repeated changes. Which kind of change must never be standard?",
    remember="Make the <span class=\"hl\">routine fast and boring</span>, and give the <span class=\"hl\">risky few</span> a real second look. The path depends on risk, not on how small it feels.",
    sources=["AXELOS, <i>ITIL 4: Change enablement</i> practice guide (2020).",
             "Nicole Forsgren, Jez Humble and Gene Kim, <i>Accelerate</i> (2018): change approval.",
             "Betsy Beyer et al., <i>Site Reliability Engineering</i> (2016): chapter 8, release engineering."],
)

# ------------------------------------------------------------------ 02 Do We Need a Change Board?
cb_problem = Doodle(760, 260, "Doodle of a change advisory board trial at Larder, three Thursdays from 14 January to 4 February 2027, proposed by Marco after the Christmas outage. Six people, one hour each week, 41 changes reviewed. The median wait for a non-deploy change went from 1 day to 6. Most reviewers couldn't judge database or network changes and approved them anyway. Changes piled up for the next Thursday, so the 4 February batch was large, and one of its changes failed in production regardless.",
                    "Six people, an hour a week, 41 changes. Waits went from 1 day to 6, and a change still failed.")
cb_problem.box(14, 30, 230, 100, "6 people × 1 h", "y", sub="Thursdays, 3 weeks", size=19, subsize=14)
cb_problem.box(264, 30, 230, 100, "1 day → 6 days", "pink", sub="median wait", size=20, subsize=14)
cb_problem.box(514, 30, 232, 100, "1 failed anyway", "pink", sub="4 Feb batch", size=19, subsize=14)
cb_problem.note(380, 176, "“I can't judge a network rule. Approved.”", "red", size=18)
cb_problem.note(380, 214, "changes pile up → bigger batches → riskier Thursdays", "pen", size=17)

cb_analogy = Doodle(760, 220, "Doodle of a newspaper. Once, every article went to the editor-in-chief for approval, and the paper came out late and was no better. Now each article is checked by an editor who knows the subject, the editor-in-chief sees only the few that could get the paper sued, and corrections are quick.",
                    "Every article to the editor-in-chief: late, and no better. A subject editor for each, the chief for the risky few.")
cb_analogy.icon("newspaper", 60, 40, 1.5)
cb_analogy.box(170, 40, 270, 100, "everything to the chief", "pink", sub="late, no better", size=17, subsize=14)
cb_analogy.box(470, 40, 276, 100, "a subject editor each", "green", sub="the chief: risky few only", size=17, subsize=13)
cb_analogy.note(450, 190, "review by someone who knows, close to the work", "pen", size=18)

cb_how = Doodle(760, 360, "What replaced the board on Monday 8 February 2027. Normal changes: reviewed in the pull request by one person who knows that system (a list per system: network, database, Dispatch, payments, devices), with the risk score and the way back in the description; median wait under one day. High-risk changes, risk score 12 or more, about two a month: a 20-minute review with Eli, the system owner and whoever is affected, which can happen in writing. Marco gets a monthly line: number of changes, change failure rate, and the high-risk ones.",
                "A knowing reviewer for normal changes; a short board only for the high-risk few; a monthly line for Marco.")
cb_how.box(14, 14, 360, 120, "normal change", "y", sub="one reviewer who knows the system · in the PR", size=20, subsize=13)
cb_how.box(386, 14, 360, 120, "high-risk (score ≥ 12)", "pink", sub="20 min · Eli + owner + affected · ≈ 2 a month", size=18, subsize=12)
for i, t in enumerate(["network: Eli, Bram", "database: Eli, Bram", "Dispatch: Ben", "payments: Cho", "devices: Dee"]):
    cb_how.box(14 + i * 148, 160, 136, 60, t, "paper", size=13)
cb_how.box(110, 244, 540, 64, "Marco, monthly: changes · failure rate · high-risk list", "green", size=16)
cb_how.note(380, 336, "median wait: 6 days → under 1 day", "pen", size=17)

CHANGE_BOARD = dict(
    slug="change-board",
    kicker="a.k.a. “change authority”, “the CAB question”",
    tldr="A weekly <b>change advisory board</b> feels safe, but research and experience agree it slows change without making it safer: reviewers far from the work can't judge it, and changes pile into bigger, riskier batches. Better: <b>peer review by someone who knows that system</b>, in the pull request, for normal changes, and a short board only for the <b>rare high-risk</b> change. Give leaders <b>numbers</b>, not meetings.",
    chips=[("Family", "deciding about changes"), ("Lives in", "the pull request template, ops/changes/reviewers.md"), ("Pairs with", "change types, risk scoring, DORA numbers")],
    itil=dict(groups=["service"], chain=["design", "build"], practices=["change enablement"],
              sre="(peer review and automated checks over external approval)", principles=["Optimise and automate", "Collaborate and promote visibility"],
              older="ITIL v3: the change advisory board (CAB)"),
    problem_side="Larder, 14 January – 4 February 2027",
    problem="""  <p class="lead">After the Christmas outage Marco proposes a <b>change board</b>: every non-deploy change approved at a weekly meeting. Eli agrees to a three-week trial. <b>Six people, one hour each Thursday, 41 changes.</b> The median wait for a non-deploy change goes from <b>1 day to 6</b>. Most reviewers can't judge database or network changes, and approve them anyway. <span class="hl-pink">Changes pile up for Thursday, so the 4 February batch is large, and one of its changes fails in production regardless.</span></p>
  <ul>
    <li>Approval by people who can't judge the change is a ritual, not a check.</li>
    <li>Waiting a week makes batches bigger, and bigger batches are riskier.</li>
    <li>The people who can judge (Eli, Bram, Ben) spend an hour a week approving others' recipes.</li>
  </ul>""",
    problem_figs=[cb_problem],
    analogy_side="the newspaper's editors",
    analogy="""  <p>A newspaper once sent <b>every article to the editor-in-chief</b>. The paper came out late, and it was no better: the chief couldn't check a football report and a court report equally well. Now each article is checked by <b>an editor who knows the subject</b>, the chief sees only the few that could get the paper sued, and corrections go out quickly.</p>""",
    analogy_figs=[cb_analogy],
    map=[("Every article to the chief", "Every change to a weekly board"),
         ("Late, and no better", "1 day → 6 days, and a change failed anyway"),
         ("A subject editor", "A reviewer who knows that system, in the pull request"),
         ("The few that could get you sued", "High-risk changes: risk score 12 or more"),
         ("The chief's circulation figures", "Marco's monthly line: changes, failure rate, high-risk list")],
    how_side="knowing reviewers for normal changes, a short board for the risky few",
    how="""  <p>On <b>Monday 8 February</b> the board is replaced, with Marco's agreement, by three things:</p>
  <ul>
    <li><b>Normal changes</b> are reviewed in the pull request by <b>one person who knows that system</b>, from a short list per system (network and database: Eli, Bram; Dispatch: Ben; payments: Cho; devices: Dee). The risk score and the way back go in the description.</li>
    <li><b>High-risk changes</b> (score 12 or more, about <b>two a month</b>) get a <b>20-minute review</b> with Eli, the system's owner and whoever is affected. It can be done in writing.</li>
    <li><b>Marco gets numbers, not meetings</b>: each month, the number of changes, the <b>change failure rate</b> and the list of high-risk changes with their outcome.</li>
  </ul>
  <p>The median wait for a normal change drops <b>below one day</b>. In February–June the change failure rate falls from 6 % to 3 % (this volume). Eli tells Marco that the board's best effect was making everyone write down how to undo their change, and that habit stays.</p>""",
    how_figs=[cb_how],
    steps=[("Ask what the board actually catches", "Count approvals, waits and failures."),
           ("Name reviewers per system", "People who can really judge the change."),
           ("Review in the pull request", "Risk score and way back in the description."),
           ("Keep a short board for high risk", "A score threshold, 20 minutes, can be in writing."),
           ("Give leaders numbers", "Changes, failure rate, high-risk list monthly."),
           ("Keep what the board taught", "Written undo plans.")],
    vocab=[("Change advisory board (CAB)", "A group that reviews and advises on changes before they are made."),
           ("Change authority", "The person or group allowed to approve a kind of change."),
           ("Peer review", "Review by a colleague who knows the system, close to the work."),
           ("Batch size", "How many changes go out together; bigger batches fail bigger."),
           ("Lead time for changes", "Time from a change being ready to it being live."),
           ("Approval theatre", "Approval by people who can't judge what they approve.")],
    code=dict(file=".github/pull_request_template.md", note="normal changes · from Mon 8 February 2027", plain=True, src="""
## Change (normal)                                   reviewer: one from ops/changes/reviewers.md

What changes      ________________________________________________
Risk score        blast __ + undo __ + tested __ + timing __ + new __ = __ / 15
                  ≥ 12 → high-risk review (Eli + owner + affected, 20 min)
Way back          how, how long, tested where? ___________________
Window            not Fri 17–20 · not weekdays 07–09 · not a campaign day
Watching          who watches which signal for 30 min after? _____

Reviewers   network, database: Eli, Bram · Dispatch: Ben · payments: Cho
            devices, apps: Dee · stores: Eli + the store lead
"""),
    tools="tools: the pull request template, a reviewers file per system, and a monthly report from the pipeline.",
    ladder=[("everything to a board", ["Weekly batches.", "Approval by people who can't judge."]),
            ("knowing reviewers, a board for the few", ["Review in the pull request.", "Leaders get numbers."]),
            ("checks automated", ["Tests, policy checks and risk score in the pipeline.", "Reviewers see only what machines can't judge."]),
            ("approval by evidence", ["Canary and signals decide.", "High-risk changes rare by design."])],
    ladder_now=1,
    baseline="Each line compares <b>a weekly board for every non-deploy change</b> to <b>knowing reviewers in the pull request and a short board for high risk</b>.",
    ratings=[(3, 3, "Neutral on its own."),
             (2, 3, "Review by people who can judge."),
             (3, 3, "Neutral."),
             (2, 4, "Smaller batches; failure rate 6 % → 3 %."),
             (3, 4, "Leaders see numbers, not minutes."),
             (2, 3, "Six hours a week of meetings removed."),
             (2, 4, "Fewer people in fewer meetings."),
             (3, 3, "Neutral."),
             (1, 4, "Under a day instead of six.")],
    pitfalls=[("Approval as reassurance", "The board feels safe and checks nothing.", "count what it catches."),
              ("Reviewers who can't judge", "Approved because the author seems confident.", "named reviewers per system."),
              ("Weekly batches", "Changes wait and pile up.", "review when ready, in the pull request."),
              ("No board at all for the truly risky", "A major database change gets one tired reviewer.", "a short high-risk review.")],
    use=["Someone proposes approving every change after an outage.", "Changes wait days for a meeting.", "Reviewers approve what they can't judge.", "Auditors ask how changes are authorised (show the log)."],
    skip=["Regulations that require a named board: keep it, but feed it pre-reviewed, scored changes."],
    related=["<b>Which Changes Need a Second Look?</b> (this volume)", "<b>Which Changes Fail?</b> (this volume)", "<b>Guardrails Not Gates</b> (Ana, vol. 6)", "<b>Lightweight Architecture Review</b> (Ana, vol. 6)"],
    quiz=[("What did the three-week board trial show?", "Waits went from 1 day to 6, reviewers approved what they couldn't judge, batches grew, and a change still failed."),
          ("Who reviews a normal change now?", "One person who knows that system, in the pull request."),
          ("When does a change still get a board review?", "When its risk score is 12 or more: about two a month, 20 minutes, can be in writing."),
          ("What does Marco get instead of meetings?", "A monthly line: number of changes, change failure rate, and the high-risk list with outcomes."),
          ("Why do bigger batches matter?", "More changes at once fail bigger and are harder to undo or diagnose.")],
    quiz_sit=[("After an outage, the CEO says “from now on, I want to approve every change”. What do you offer instead?", "A monthly page: number of changes, change failure rate, high-risk changes and their outcome, plus the promise that high-risk ones get a short review with the right people. Explain that approval by someone who can't judge slows change without making it safer.")],
    try_it="For a month, note every change approval in your team: who approved it, could they really judge it, and how long did the change wait? Which approvals would a knowing peer have done better and faster?",
    remember="Approval is only a check if the approver <span class=\"hl\">can judge the change</span>. Review close to the work, and keep a board for the <span class=\"hl\">risky few</span>.",
    sources=["Nicole Forsgren, Jez Humble and Gene Kim, <i>Accelerate</i> (2018): chapter 7, external change approval.",
             "AXELOS, <i>ITIL 4: Change enablement</i> practice guide (2020): change authorities.",
             "DORA, <i>Accelerate State of DevOps</i> reports (2019 onwards): streamlining change approval."],
)

# ------------------------------------------------------------------ 03 When Must We Not Change Anything?
cc_problem = Doodle(760, 250, "Doodle of two Larder changes made at the worst moment. The network rule tidy-up of 29 October 2026, applied at 18:10, the start of the evening peak. And the database primary resized in a hurry on 16 December 2026, two days before the Christmas peak. On 12 January 2027 ADR 0017 says: no changes in the critical windows. But nothing stops anyone, and nobody has written down when the windows are.",
                    "A network change at the evening peak, a database resize two days before Christmas, and no calendar that says “not now”.")
cc_problem.box(14, 30, 350, 100, "29 Oct · 18:10", "pink", sub="network rule at the evening peak", size=20, subsize=14)
cc_problem.box(396, 30, 350, 100, "16 Dec", "pink", sub="database resized in a hurry", size=20, subsize=14)
cc_problem.note(380, 180, "ADR 0017: “no changes in critical windows”, but which ones, and who stops it?", "red", size=16)

cc_analogy = Doodle(760, 220, "Doodle of a city's roadworks calendar. No digging on the ring road in rush hour, none on the shopping street in December, none near the stadium on match days. The calendar is public, the permit system enforces it, and a burst water main can still be fixed at any time, with a phone call to the city.",
                    "No roadworks in rush hour or on match days, enforced by the permit system, with an emergency exception.")
cc_analogy.icon("traffic", 60, 30, 1.3)
cc_analogy.row([("rush hour", "no digging", "pink"), ("December, shops", "no digging", "pink"), ("burst main", "any time, call first", "green")], x=150, y=40, h=96, gap=16, size=17, subsize=14)
cc_analogy.note(450, 190, "written, public, enforced, with an emergency door", "pen", size=18)

cc_how = Doodle(760, 380, "Larder's change calendar from 1 February 2027. Critical windows every week: weekdays 07:00 to 09:00 (business deliveries), Friday 17:00 to 20:00 (the peak). Freezes: campaign days, King's Day 26 to 28 April 2027, and Christmas 13 December to 3 January. Store cutovers and city openings are on the same calendar, shared with Sanne's launches. The pipeline refuses deploys and normal changes in a window unless the change is marked emergency with the incident lead's name. February to June: no changes in windows except 2 emergencies; average lead time unchanged.",
                "Windows and freezes on one calendar, enforced by the pipeline, with an emergency door that needs a name.")
days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
for i, d in enumerate(days):
    x = 14 + i * 148
    cc_how.box(x, 14, 136, 40, d, "paper", size=15)
    cc_how.box(x, 60, 136, 46, "07–09", "pink", size=15)
    cc_how.box(x, 112, 136, 70, "open", "green", size=15)
    if d == "Fri":
        cc_how.box(x, 188, 136, 46, "17–20", "pink", size=15)
cc_how.box(14, 256, 732, 56, "freezes: King's Day 26–28 Apr · Christmas 13 Dec – 3 Jan · campaign days", "y", size=15)
cc_how.note(380, 340, "pipeline: blocked in windows unless “emergency” + the lead's name", "red", size=16)
cc_how.note(380, 370, "Feb–Jun: 0 changes in windows, except 2 emergencies", "pen", size=15)

CHANGE_CALENDAR = dict(
    slug="change-calendar",
    kicker="a.k.a. “change windows and freezes”",
    tldr="Some hours are worse than others for change: the evening peak, the morning delivery run, the week before Christmas. A <b>change calendar</b> writes them down as <b>critical windows</b> (weekly) and <b>freezes</b> (seasonal), shares them with whoever plans launches, and <b>enforces them in the pipeline</b>, so “not now” doesn't depend on memory. Keep one clear <b>emergency door</b>, with a name on it.",
    chips=[("Family", "deciding about changes"), ("Lives in", "ops/changes/calendar.md, the pipeline's window check, Sanne's launch calendar"), ("Pairs with", "change types, release vs deploy, running a peak (vol. 4)")],
    itil=dict(groups=["service"], chain=["plan", "deliver"], practices=["change enablement", "availability management"],
              sre="“change freezes” around peaks, used sparingly", principles=["Focus on value", "Optimise and automate"],
              older="ITIL v3: the forward schedule of change, change windows"),
    problem_side="Larder, January 2027",
    problem="""  <p class="lead">Two of Larder's changes were made at the worst moment: the network rule tidy-up of <b>29 October</b>, applied at 18:10 as the evening peak started, and the database primary <b>resized in a hurry on 16 December</b>, two days before the Christmas peak. On <b>12 January</b> ADR 0017 says “no changes in the critical windows”. <span class="hl-pink">But nobody has written down when the windows are, and nothing stops anyone.</span> King's Day is in April, and the WMS B cutovers start the same month.</p>
  <ul>
    <li>A rule in a decision record isn't a rule in the pipeline.</li>
    <li>Launch dates and change plans live in different calendars.</li>
    <li>Without an emergency door, people will just bypass the rule.</li>
  </ul>""",
    problem_figs=[cc_problem],
    analogy_side="the city's roadworks calendar",
    analogy="""  <p>A city keeps a <b>roadworks calendar</b>: no digging on the ring road in rush hour, none on the shopping street in December, none near the stadium on match days. It's public, and the <b>permit system enforces it</b>: you can't get a permit for those times. A burst water main can still be fixed <b>at any time</b>, but the crew phones the city first.</p>""",
    analogy_figs=[cc_analogy],
    map=[("Rush hour on the ring road", "Friday 17:00–20:00; weekdays 07:00–09:00"),
         ("The shopping street in December", "The Christmas freeze, 13 Dec – 3 Jan"),
         ("Match days", "King's Day, campaign days"),
         ("The permit system", "The pipeline's window check"),
         ("The burst main, with a phone call", "An emergency change with the incident lead's name")],
    how_side="one calendar, enforced by the pipeline, with an emergency door",
    how="""  <p>From <b>1 February 2027</b> Larder has one change calendar:</p>
  <ul>
    <li><b>Weekly critical windows</b>: weekdays <b>07:00–09:00</b> (business deliveries, Korenwolf's mornings) and Friday <b>17:00–20:00</b> (the peak).</li>
    <li><b>Freezes</b>: campaign days, <b>King's Day 26–28 April</b>, and <b>Christmas 13 December – 3 January</b>. During a freeze only standard changes that don't touch customers run.</li>
    <li><b>Store cutovers and city openings</b> go on the same calendar, shared with Sanne's launch calendar, so a WMS B cutover never lands on an opening week.</li>
  </ul>
  <p>The <b>pipeline</b> checks the clock. A deploy or normal change in a window is refused, unless it's marked <b>emergency</b> with the incident lead's name, which also posts to the change feed. From February to June there are <b>no changes in windows except 2 emergencies</b>, and average lead time doesn't change: people simply plan around the windows.</p>""",
    how_figs=[cc_how],
    steps=[("Write down your critical windows", "When does an outage hurt most?"),
           ("Add seasonal freezes", "Peaks and campaign days, kept short."),
           ("Share it with launch planning", "One calendar for changes and openings."),
           ("Enforce it in the pipeline", "Refused in windows, not just discouraged."),
           ("Keep an emergency door with a name", "The incident lead's, posted to the feed."),
           ("Review the windows yearly", "Businesses change; so do their peaks.")],
    vocab=[("Critical window", "A recurring time when changes are not made."),
           ("Change freeze", "A longer period (a peak, a holiday) with only the safest changes."),
           ("Change calendar", "The shared schedule of windows, freezes and planned big changes."),
           ("Emergency exception", "A change allowed inside a window, with a named approver."),
           ("Maintenance window", "An agreed time when planned disruption is acceptable."),
           ("Freeze debt", "Changes that pile up during a freeze and go out together after it: plan for it.")],
    code=dict(file="ops/changes/calendar.md", note="from 1 February 2027 · enforced by the pipeline", plain=True, src="""
# Change calendar

weekly windows (no deploys, no normal changes)
  Mon–Fri 07:00–09:00   business deliveries (Korenwolf and others)
  Fri     17:00–20:00   evening peak
freezes (standard changes that don't touch customers only)
  King's Day   Mon 26 – Wed 28 Apr 2027
  Christmas    Mon 13 Dec 2027 – Mon 3 Jan 2028
  campaigns    as marketing adds them (≥ 4 weeks' notice)
big changes (shared with Sanne's launch calendar)
  WMS B cutovers Zuid 19 Apr · Noord 24 May · Rotterdam 21 Jun · Utrecht 26 Jul
  openings      Utrecht 12 Apr · The Hague 14 Jun (on WMS B)
emergency     label "emergency" + incident lead's name → allowed, posted to the feed
after a freeze: no more than 5 normal changes on the first day back
"""),
    tools="tools: a calendar file in the repo, a time check in the pipeline, and a shared launch calendar.",
    ladder=[("“don't change things at busy times”", ["In people's heads.", "Peak-time changes happen."]),
            ("a written, enforced calendar", ["Windows and freezes in the pipeline.", "Emergency door with a name."]),
            ("all change paths checked", ["Flags, consoles and vendors' maintenance too.", "Freeze debt planned."]),
            ("windows matter less", ["Safe change (canaries, instant undo) makes most windows unnecessary.", "Only true peaks stay frozen."])],
    ladder_now=1,
    baseline="Each line compares <b>a rule in a decision record</b> to <b>a shared calendar of windows and freezes enforced by the pipeline</b>.",
    ratings=[(2, 4, "No changes during Friday peaks or business mornings."),
             (3, 3, "Neutral."),
             (3, 3, "Neutral."),
             (2, 4, "Risky moments are protected by the pipeline."),
             (2, 4, "Everyone sees the windows and the cutovers."),
             (3, 3, "Neutral."),
             (3, 3, "Neutral."),
             (2, 3, "Fewer evening incidents for on-call."),
             (3, 4, "Planned once, enforced automatically.")],
    pitfalls=[("A rule nobody enforces", "“No changes on Friday evening” until someone forgets.", "the pipeline checks the clock."),
              ("Long freezes", "Changes pile up and go out together afterwards.", "keep freezes short; limit the first day back."),
              ("Forgetting other change paths", "The console, flags and vendors ignore the pipeline.", "bring them into the feed and the rule."),
              ("No emergency door", "People bypass the whole system under pressure.", "a named, logged exception.")],
    use=["Changes have caused incidents at peak times.", "A peak or campaign is coming.", "Launches and big changes clash.", "Business clients have fixed delivery windows."],
    skip=["Services nobody uses at particular times: windows add nothing."],
    related=["<b>Was It a Change?</b> (vol. 2)", "<b>Release or Deploy?</b> (next note)", "<b>Running a Peak</b> (vol. 4)", "<b>Explaining Trade-offs to Non-Engineers</b> (Ana, vol. 3)"],
    quiz=[("What are Larder's weekly critical windows?", "Weekdays 07:00–09:00 and Friday 17:00–20:00."),
          ("What may run during a freeze?", "Only standard changes that don't touch customers."),
          ("How is the calendar enforced?", "The pipeline refuses deploys and normal changes in windows, unless marked emergency with the lead's name."),
          ("Why share it with Sanne's launch calendar?", "So cutovers and openings never land on the same week."),
          ("What is freeze debt?", "Changes that pile up during a freeze and go out together afterwards; limit the first day back.")],
    quiz_sit=[("At 17:30 on a Friday, Ben has a fix for a typo on the checkout page. It's not causing errors. What happens?", "It waits until 20:00 (or Monday): it's not an emergency, and the window exists for exactly this kind of harmless-looking change.")],
    try_it="Mark your services' busiest and most sensitive hours on a week grid. How many changes last month landed in them? Write the windows down and find one way to make the pipeline say “not now”.",
    remember="Write down <span class=\"hl\">when not to change</span>, make the <span class=\"hl\">pipeline enforce it</span>, and keep one door for emergencies, with a name on it.",
    sources=["AXELOS, <i>ITIL 4: Change enablement</i> practice guide (2020): change schedules.",
             "Betsy Beyer et al., <i>The Site Reliability Workbook</i> (2018): chapter 16, canarying releases (and freezes).",
             "Gene Kim et al., <i>The DevOps Handbook</i> (2016): low-risk releases."],
)

# ------------------------------------------------------------------ 04 Release or Deploy?
rd_problem = Doodle(760, 260, "Doodle of the plan for Larder Plus, the 7.99 euro delivery subscription, in March 2027. The first plan: build it on a branch, merge everything the night before launch, deploy on launch morning and switch it on for everyone at once. One big deploy, one big release, at the same moment, and if anything goes wrong, the only way back is to undo the whole deploy.",
                    "The first Plus plan: one big deploy and one big release, at the same moment.")
rd_problem.box(14, 40, 230, 100, "8 weeks on a branch", "paper", size=17)
rd_problem.arrow(250, 90, 290, 90)
rd_problem.box(296, 40, 220, 100, "deploy + switch on", "pink", sub="launch morning, everyone", size=17, subsize=13)
rd_problem.arrow(522, 90, 562, 90)
rd_problem.box(568, 40, 178, 100, "problem?", "pink", sub="undo the whole deploy", size=17, subsize=13)
rd_problem.note(380, 200, "the risk of the code and the risk of the launch, stacked", "red", size=17)

rd_analogy = Doodle(760, 220, "Doodle of a theatre. The set is built and placed on stage days before opening night, behind the closed curtain, and rehearsed with a small invited audience. On opening night only the curtain goes up. If a prop breaks, they fix the prop; they don't rebuild the stage.",
                    "The set goes on stage days before, behind the curtain. Opening night only raises the curtain.")
rd_analogy.icon("curtain", 60, 50, 1.3)
rd_analogy.row([("set on stage", "days before · curtain shut", "blue"), ("invited audience", "a small preview", "y"), ("opening night", "curtain up", "green")], x=170, y=40, h=96, w=170, gap=36, size=16, subsize=13, arrows=True)
rd_analogy.note(450, 190, "deploy = set on stage · release = curtain up", "pen", size=18)

rd_how = Doodle(760, 380, "How Larder Plus actually shipped. From 10 May 2027, 46 small deploys of Plus code went to production behind a flag that was off: nobody could see it. 24 May: released to Larder staff. Tuesday 1 June: released to 5 percent of customers in Amsterdam. A renewal bug showed up on day two; the flag was turned off for 2 hours while it was fixed, with no deploy undone. Tuesday 8 June, 10:00, outside any window: released to everyone. The release was a flag change, a standard change; the risk of the code had already been taken, in small steps.",
                "46 dark deploys, then a release in steps by flag. A bug meant 2 hours with the flag off, not a rollback.")
rd_how.row([("10 May →", "46 dark deploys", "blue"), ("24 May", "staff", "y"), ("1 Jun", "5 % Amsterdam", "y"), ("8 Jun 10:00", "everyone", "green")], x=14, y=14, h=96, gap=36, size=17, subsize=13, arrows=True)
rd_how.box(110, 146, 540, 70, "2 Jun: renewal bug → flag off 2 h → fixed → flag on", "pink", size=16)
rd_how.row([("deploy", "code in production · engineers decide · often", "blue"), ("release", "people can use it · product decides · when ready", "green")], x=14, y=246, h=96, w=356, gap=20, size=19, subsize=13)

RELEASE_DEPLOY = dict(
    slug="release-vs-deploy",
    kicker="a.k.a. “release management and deployment management”",
    tldr="<b>Deploying</b> puts new code into production; <b>releasing</b> lets people use it. Done together, the risk of the code and the risk of the launch arrive at once, and the only way back is undoing the deploy. Done apart, code goes out <b>dark</b> in small, frequent deploys, and the release is a <b>flag turned on in steps</b>: staff first, then a few customers, then everyone. A problem is fixed by turning the flag off, not by rolling back.",
    chips=[("Family", "deciding about changes"), ("Lives in", "the flag service, the release plan for each launch"), ("Pairs with", "feature flags, the change calendar, rollback plans")],
    itil=dict(groups=["service", "technical"], chain=["build", "design", "deliver"], practices=["release management", "deployment management"],
              sre="“progressive rollouts”; decoupling deploy from release", principles=["Progress iteratively with feedback"],
              older="ITIL v3: release and deployment management (one process)"),
    problem_side="Larder, March 2027",
    problem="""  <p class="lead">Femke decides on <b>1 March</b> that <b>Larder Plus</b>, a €7.99 monthly delivery subscription, launches in June. The first plan from the team building it: eight weeks on a branch, merge the night before, <b>deploy on launch morning and switch it on for everyone at once</b>. <span class="hl-pink">The risk of new code and the risk of a launch, stacked on the same morning.</span> If anything breaks, the only way back is undoing the whole deploy, along with everything else that went out with it.</p>
  <ul>
    <li>Big merges hide conflicts until the last minute.</li>
    <li>A launch-morning deploy is a large normal change at a sensitive time.</li>
    <li>Product and engineering both feel the pressure of one moment.</li>
  </ul>""",
    problem_figs=[rd_problem],
    analogy_side="the set behind the curtain",
    analogy="""  <p>A theatre doesn't build the set on opening night. The set goes <b>on stage days before, behind the closed curtain</b>, and it's tried out with <b>a small invited audience</b>. On opening night the only thing that happens is <b>the curtain goes up</b>. If a prop breaks during the preview, they fix the prop; they don't rebuild the stage.</p>""",
    analogy_figs=[rd_analogy],
    map=[("The set placed on stage", "Deploying Plus code to production, flag off"),
         ("The closed curtain", "The flag: off for customers"),
         ("The invited audience", "Staff, then 5 % of Amsterdam customers"),
         ("Curtain up on opening night", "Release: flag on for everyone, 8 June 10:00"),
         ("Fixing the prop, not the stage", "Flag off for 2 hours, fix, flag on")],
    how_side="dark deploys, then a release in steps by flag",
    how="""  <p>Eli and Ben rewrite the plan:</p>
  <ul>
    <li>From <b>10 May</b>, Plus code goes out in <b>46 small deploys</b>, each a standard change through the pipeline, behind a flag that is <b>off</b>. Nobody outside the team can see it.</li>
    <li><b>24 May</b>: released to Larder staff.</li>
    <li><b>Tuesday 1 June</b>: released to <b>5 % of Amsterdam customers</b>. On day two a renewal bug charges two test customers twice. The flag goes <b>off for 2 hours</b> while the bug is fixed and deployed, the charges are refunded, and the flag goes back on. Nothing is rolled back.</li>
    <li><b>Tuesday 8 June, 10:00</b>, outside every window: released to everyone.</li>
  </ul>
  <p>The release itself is <b>a flag change</b>, which is a standard change. The risk of the code was taken earlier, in small steps. From now on, Eli's rule for any launch is two plans: a <b>deploy plan</b> (engineering, small, frequent) and a <b>release plan</b> (product, in steps, with a flag as the way back).</p>""",
    how_figs=[rd_how],
    steps=[("Deploy small and often, behind a flag", "Code in production, nobody sees it."),
           ("Write a release plan separately", "Who sees it when: staff, a few, everyone."),
           ("Choose release times by the calendar", "Never in a window, never on a Friday evening."),
           ("Make the flag the way back", "Off in seconds, no deploy undone."),
           ("Watch signals at each step", "Errors, support tickets, the business number."),
           ("Remove the flag after the release", "Old flags are debt.")],
    vocab=[("Deploy", "Putting a new version of code into an environment, such as production."),
           ("Release", "Making a change available to users."),
           ("Dark launch", "Code deployed to production but not visible to users."),
           ("Feature flag", "A switch that turns a feature on or off without a deploy."),
           ("Progressive release", "Releasing to a growing share of users, step by step."),
           ("Flag debt", "Old flags left in the code after the release is finished.")],
    code=dict(file="ops/releases/larder-plus.md", note="release plan · owner Grace · deploy plan · owner Ben", plain=True, src="""
# Larder Plus · deploy plan and release plan, kept apart

deploy plan (engineering)     from 10 May · small deploys, flag plus_enabled = off
                              46 deploys by 7 Jun · each a standard change (R1)
release plan (product)        flag plus_enabled, by audience
  Mon 24 May   staff                          watch: sign-ups, errors
  Tue 1 Jun    5 % Amsterdam customers        watch: payments, renewals, tickets
  Wed 2 Jun    renewal charged twice (2 test customers) → flag OFF 11:40–13:40,
               fix deployed, refunds done, flag ON
  Tue 8 Jun    10:00 everyone                 (not in a window; Eli + Grace watching)
  by 6 Jul     remove the flag (flag debt)
way back       flag off (seconds) · no rollback of deploys needed
"""),
    tools="tools: a feature flag service (or a simple config table), the pipeline, and a release plan per launch.",
    ladder=[("deploy = release", ["Big deploys on launch day.", "Rollback is the only way back."]),
            ("dark deploys, flagged releases", ["Release plan in steps.", "Flag off as the way back."]),
            ("automated progressive release", ["The flag service raises the share as signals stay good.", "Stops by itself on bad signals."]),
            ("release as a product decision", ["Engineers deploy all day.", "Product releases when ready, no engineering event."])],
    ladder_now=1,
    baseline="Each line compares <b>deploy and release together on launch morning</b> to <b>dark deploys and a flagged release in steps</b>.",
    ratings=[(2, 4, "A bug reached 5 %, for 2 hours, not everyone."),
             (3, 3, "Neutral."),
             (2, 4, "Flag off in seconds."),
             (2, 4, "Small deploys and a release that is a flag change."),
             (3, 3, "Neutral."),
             (3, 3, "Neutral."),
             (3, 3, "Neutral."),
             (2, 3, "No big-bang launch mornings."),
             (3, 3, "A release plan and a flag per launch.")],
    pitfalls=[("Big-bang launch morning", "Deploy and release together, at a busy time.", "deploy dark first, release in steps."),
              ("Flags that never go", "Hundreds of old switches nobody understands.", "remove the flag after the release."),
              ("Flags as the only test", "Dark code still runs in production and can break it.", "dark doesn't mean untested."),
              ("Data changes behind a flag", "A flag can't undo data that's been written.", "plan data changes separately (next notes).")],
    use=["A launch has a date and a marketing push.", "Deploys are big and rare.", "Rollback is your only way back.", "Product and engineering argue about launch-day risk."],
    skip=["Tiny internal changes nobody needs to be told about."],
    related=["<b>Feature Flags</b> (cloud, vol. 6)", "<b>Dark Launches & Rollouts</b> (Grace, vol. 3)", "<b>How Do We Undo It?</b> (this volume)", "<b>When Must We Not Change Anything?</b> (this volume)"],
    quiz=[("What's the difference between deploying and releasing?", "Deploying puts code into production; releasing lets people use it."),
          ("What is a dark launch?", "Code deployed to production behind a switch that is off, so users don't see it."),
          ("How was the Plus renewal bug handled?", "The flag was turned off for 2 hours while the fix was deployed; nothing was rolled back."),
          ("Who owns the release plan, and who owns the deploy plan?", "Product (Grace) owns release; engineering (Ben) owns deploys."),
          ("Why remove flags after a release?", "Old flags pile up as debt: confusing, untested paths in the code.")],
    quiz_sit=[("Marketing wants Plus “live” at 18:00 on a Friday to match an email. What do you suggest?", "Release it at 10:00 on a weekday, before the email, to a growing share, then send the email when it's on for everyone. Or send the email later. A release in the Friday window is exactly what the calendar exists to prevent.")],
    try_it="Take your next feature with a launch date. Write two plans: the deploy plan (small, dark, frequent) and the release plan (who sees it when, which signals, what's the flag). How much risk moves off launch day?",
    remember="<span class=\"hl\">Deploy</span> the set behind the curtain, <span class=\"hl\">release</span> by raising it in steps. The flag is the fastest way back.",
    sources=["AXELOS, <i>ITIL 4: Release management</i> and <i>Deployment management</i> practice guides (2020).",
             "Pete Hodgson, “Feature Toggles (aka Feature Flags)” (martinfowler.com, 2017).",
             "Jez Humble and David Farley, <i>Continuous Delivery</i> (2010)."],
)

# ------------------------------------------------------------------ 05 How Risky Is This Change?
cs_problem = Doodle(760, 250, "Doodle of the normal changes waiting for review in late January 2027: a database setting, a network rule, a new Dispatch version, a label printer driver, the picker app's weekly release. Reviewers ask the same question each time, 'how careful should we be?', and answer it by gut feeling. The network rule tidy-up of 29 October felt like a three-minute job.",
                    "Every normal change asked “how careful should we be?”, and gut feeling answered.")
for i, t in enumerate(["DB setting", "network rule", "Dispatch v", "printer driver", "picker app"]):
    cs_problem.box(14 + i * 148, 40, 136, 80, t, "y", size=15)
cs_problem.note(380, 170, "“how careful?” → gut feeling", "red", size=19)
cs_problem.note(380, 210, "29 Oct's tidy-up “felt like a three-minute job”", "pen", size=17)

cs_analogy = Doodle(760, 220, "Doodle of a mountain hut's avalanche checklist for walkers: how steep is the slope, how much new snow, is it warm today, how many in the group, have you done this route before. Each answer adds a point. A low score: go. A middle score: go with care and turn back early. A high score: don't go today, or go with a guide.",
                    "Five questions, a few points each: go, go with care, or not today.")
cs_analogy.icon("map", 60, 50, 1.3)
cs_analogy.row([("low", "go", "green"), ("middle", "go with care", "y"), ("high", "not today / with a guide", "pink")], x=170, y=40, h=96, w=180, gap=18, size=19, subsize=13)
cs_analogy.note(450, 190, "the same five questions, every time", "pen", size=18)

cs_how = Doodle(760, 400, "Larder's change risk score from 1 February 2027. Five questions, each scored 1 to 3. Blast radius: one store, one city, or everything. Way back: a flag or instant undo, a redeploy, or hard or impossible. Tested: in a production-like place, in staging only, or not at all. Timing: quiet hours, normal hours, or near a window or freeze. New: done many times, done once or twice, or first time. Total 5 to 15. Low, 5 to 7: standard path if it's a recipe, otherwise one reviewer. Medium, 8 to 11: knowing reviewer and a tested way back. High, 12 to 15: high-risk review, a planned time and someone watching. Examples: picker app weekly release 8, Postgres major upgrade 14, and the 29 October tidy-up re-scored at 13.",
                "Five questions, 1–3 each. 5–7 low · 8–11 medium · 12–15 high. 29 October's tidy-up would have scored 13.")
qs = [("blast radius", "store · city · all"), ("way back", "flag · redeploy · hard"), ("tested", "prod-like · staging · no"), ("timing", "quiet · normal · near window"), ("new?", "often · once · first")]
for i, (q, s) in enumerate(qs):
    cs_how.box(14 + i * 148, 14, 136, 90, q, "paper", sub=s, size=16, subsize=11)
cs_how.row([("5–7 low", "recipe or one reviewer", "green"), ("8–11 medium", "knowing reviewer + tested undo", "y"), ("12–15 high", "high-risk review + time + watcher", "pink")], x=14, y=130, h=96, w=236, gap=12, size=18, subsize=12)
for i, (t, sc, f) in enumerate([("picker app weekly release", "8", "y"), ("Postgres 13 → 16", "14", "pink"), ("29 Oct tidy-up, re-scored", "13", "pink")]):
    cs_how.box(14, 252 + i * 46, 600, 40, t, "paper", size=15)
    cs_how.box(626, 252 + i * 46, 120, 40, sc, f, size=17)

CHANGE_RISK = dict(
    slug="change-risk",
    kicker="a.k.a. “change risk assessment”",
    tldr="A <b>risk score</b> replaces gut feeling with the same few questions every time: <b>how much breaks if it goes wrong, how fast can we undo it, where was it tested, when will it happen, and have we done it before?</b> Score each 1–3 and add them up. The total decides how much review, testing, timing and watching the change gets. It takes a minute, and it catches the change that “feels like a three-minute job”.",
    chips=[("Family", "deciding about changes"), ("Lives in", "the pull request template (normal changes)"), ("Pairs with", "change types, change board, rollback plans")],
    itil=dict(groups=["service", "general"], chain=["design", "build"], practices=["change enablement", "risk management"],
              sre="(blast radius and reversibility drive rollout care)", principles=["Keep it simple and practical"],
              older="ITIL v3: change impact and risk assessment"),
    problem_side="Larder, late January 2027",
    problem="""  <p class="lead">With normal changes now reviewed, the queue in late January holds a database setting, a network rule, a new Dispatch version, a label printer driver and the picker app's weekly release. Each reviewer asks the same question, <b>“how careful should we be?”</b>, and answers it by feel. <span class="hl-pink">The 29 October network tidy-up had felt like a three-minute job too.</span></p>
  <ul>
    <li>Gut feeling depends on who's reviewing, and how tired they are.</li>
    <li>Two similar changes get very different care.</li>
    <li>Nobody can explain afterwards why a change was treated lightly.</li>
  </ul>""",
    problem_figs=[cs_problem],
    analogy_side="the mountain hut's avalanche checklist",
    analogy="""  <p>Mountain huts give walkers a short <b>avalanche checklist</b>: how steep is the slope, how much new snow, is it warm today, how big is the group, have you done this route before. Each answer adds points. <b>Low</b>: go. <b>Middle</b>: go with care, and turn back early. <b>High</b>: not today, or only with a guide. Experienced walkers use it too, because experience is exactly what makes a dangerous slope look easy.</p>""",
    analogy_figs=[cs_analogy],
    map=[("How steep", "Blast radius: one store, a city, everything"),
         ("Can you turn back?", "Way back: flag, redeploy, hard"),
         ("New snow, warm day", "Tested where; near a window or freeze"),
         ("Done this route before?", "Done many times, once, or never"),
         ("Go · with care · not today", "Low · medium · high, each with its own path")],
    how_side="five questions, 1–3 each, and the total decides the path",
    how="""  <p>From <b>1 February</b> every normal change carries a score in its pull request. There are <b>five questions, each scored 1–3</b>:</p>
  <ul>
    <li><b>Blast radius</b>: one store (1), one city (2), everything (3).</li>
    <li><b>Way back</b>: a flag or instant undo (1), a redeploy (2), hard or impossible (3).</li>
    <li><b>Tested</b>: somewhere honestly like production (1), staging only (2), not at all (3).</li>
    <li><b>Timing</b>: quiet hours (1), normal hours (2), near a window or freeze (3).</li>
    <li><b>New?</b>: done many times (1), once or twice (2), first time (3).</li>
  </ul>
  <p>A total of <b>5–7 is low</b> (a recipe, or one reviewer). <b>8–11 is medium</b> (a knowing reviewer and a tested way back). <b>12–15 is high</b> (a high-risk review, a planned time, someone watching for 30 minutes after). The picker app's weekly release scores <b>8</b>, and the Postgres major upgrade (this volume) <b>14</b>. Re-scored, <b>29 October's tidy-up gets 13</b>: everything, a redeploy, untested, 18:10, first time. The score doesn't make changes safe. It makes people look at them the same way.</p>""",
    how_figs=[cs_how],
    steps=[("Pick five questions", "Blast radius, way back, tested, timing, new."),
           ("Score 1–3 each, honestly", "In the pull request, by the author."),
           ("The reviewer checks the score", "Disagreeing is part of the review."),
           ("Let the total choose the path", "Low, medium, high: different care."),
           ("Lower the score by design", "A flag or a smaller step often moves a change down."),
           ("Compare scores with failures", "Adjust the questions after a few months.")],
    vocab=[("Risk score", "A quick, consistent estimate of how dangerous a change is."),
           ("Blast radius", "How much breaks if the change goes wrong."),
           ("Reversibility", "How fast and how completely a change can be undone."),
           ("Change impact", "What a change affects: services, people, data."),
           ("Watcher", "A named person who watches signals for 30 minutes after a risky change."),
           ("Risk reduction by design", "Changing how a change is made (smaller, flagged) to lower its score.")],
    code=dict(file="ops/changes/risk-score.md", note="from 1 February 2027", plain=True, src="""
question       1                         2                  3
blast radius   one store / one device    one city           everything
way back       flag / instant undo       redeploy           hard or impossible
tested         prod-like (incl. data)    staging only       not at all
timing         quiet hours               normal hours       near a window/freeze
new?           done many times           once or twice      first time

5–7  low     recipe → go · otherwise one reviewer
8–11 medium  knowing reviewer + tested way back
12+  high    high-risk review (20 min) + planned time + watcher for 30 min

examples   picker app weekly 2+1+2+1+2 = 8 · Postgres 13→16 3+3+2+3+3 = 14
           29 Oct tidy-up (re-scored) 3+2+3+3+2 = 13 → would have been high
tip        a canary or a flag usually lowers "blast" and "way back" by one each
"""),
    tools="tools: five lines in the pull request template. A spreadsheet later, to compare scores with what actually failed.",
    ladder=[("gut feeling", ["Care depends on the reviewer.", "No record of why."]),
            ("a score in every normal change", ["Five questions, three paths.", "Reviewer checks the score."]),
            ("score partly automatic", ["Pipeline fills blast radius and tested.", "Timing from the calendar."]),
            ("scores calibrated", ["Compared with real failures each quarter.", "Questions adjusted."])],
    ladder_now=1,
    baseline="Each line compares <b>gut feeling about each change</b> to <b>a five-question score that picks the path</b>.",
    ratings=[(3, 3, "Neutral on its own."),
             (2, 3, "Risky changes get consistent care."),
             (3, 3, "Neutral."),
             (2, 4, "The “three-minute job” gets looked at properly."),
             (2, 4, "Why a change got the care it did is written down."),
             (3, 3, "Neutral."),
             (3, 3, "Neutral."),
             (3, 3, "Neutral."),
             (3, 4, "A minute per change.")],
    pitfalls=[("Scoring to get through", "Everything scores 7.", "the reviewer checks the score; scores are compared with failures."),
              ("Too many questions", "A form nobody fills in.", "five, 1–3 each."),
              ("Score as permission", "“It's low, so it's safe.”", "the score sets care, not certainty."),
              ("Never adjusting", "Questions that don't predict failures.", "compare with real failures every quarter.")],
    use=["Reviewers judge risk by feel.", "Similar changes get different treatment.", "You need to explain to auditors how risky changes are handled.", "After a “small” change caused an incident."],
    skip=["Standard changes: the recipe already is the risk decision."],
    related=["<b>Which Changes Need a Second Look?</b> (this volume)", "<b>Do We Need a Change Board?</b> (this volume)", "<b>How Do We Undo It?</b> (next note)", "<b>Failure Mode Analysis</b> (Ana, vol. 5)"],
    quiz=[("What are the five questions?", "Blast radius, way back, tested where, timing, and how new it is."),
          ("What happens at 12 or more?", "A high-risk review, a planned time, and a watcher for 30 minutes after."),
          ("What would the 29 October tidy-up have scored?", "13: everything, a redeploy, untested, near the peak, first time. High risk."),
          ("How can a change lower its own score?", "By design: a canary or a flag lowers blast radius and way back."),
          ("Does a low score mean the change is safe?", "No: it sets how much care it gets, not whether it will fail.")],
    quiz_sit=[("A change scores 11, but the author says “it's basically the same as last week's”. The reviewer disagrees with “new?”. What happens?", "They talk it through in the review; if last week's was different in a way that matters, “new?” goes up and the change becomes high risk (12). The disagreement is the point of the score.")],
    try_it="Score your last five changes with the five questions. Did the ones that went wrong score higher? Which question would have changed how you handled them?",
    remember="Ask the <span class=\"hl\">same five questions</span> every time: how much breaks, how fast back, tested where, when, done before? The total picks the care.",
    sources=["AXELOS, <i>ITIL 4: Change enablement</i> and <i>Risk management</i> practice guides (2020).",
             "Betsy Beyer et al., <i>The Site Reliability Workbook</i> (2018): chapter 16, canarying releases.",
             "Daniel Kahneman, <i>Thinking, Fast and Slow</i> (2011): on checklists over intuition."],
)

NOTES = [CHANGE_TYPES, CHANGE_BOARD, CHANGE_CALENDAR, RELEASE_DEPLOY, CHANGE_RISK]
