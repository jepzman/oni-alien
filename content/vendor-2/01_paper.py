# Series 5 · On the Client's Floor · Vol. 2 · Signing and Starting · The paper (notes 1–5).
# Narrator: Ines Duarte (she/her). Facts: docs/lodestar-casebook.md, "Vol. 2".
from datetime import date

# ------------------------------------------------------------------ 01 What Does the Contract Actually Say?
sw_problem = Doodle(760, 250, "Doodle of the Lodestar statement of work, draft v0.3, on 9 June 2027: 64 pages, eleven sections and six schedules. Hana has never read a contract. Lottie asks what a schedule is. Ines circles five clauses in red: scope, assumptions, acceptance, change control and key personnel.",
                    "64 pages. Five clauses decide almost every future argument.", exact=True)
sw_problem.box(24, 24, 230, 200, None, "paper", rx=4)
sw_problem.head(139, 56, "SOW v0.3", size=22)
sw_problem.text(139, 90, "64 pages", size=17)
sw_problem.text(139, 116, "11 sections", size=17)
sw_problem.text(139, 142, "6 schedules", size=17)
for i, (no, t) in enumerate([("§2", "scope"), ("§3", "assumptions"), ("§5", "acceptance"), ("§6", "key people"), ("§7", "change")]):
    sw_problem.box(300 + (i % 3) * 150, 30 + (i // 3) * 90, 136, 74, no, "pink", sub=t, size=22, subsize=16)
sw_problem.note(500, 236, "read these five with the people who'll live with them", "red", size=18)

sw_analogy = Doodle(760, 220, "Doodle of a tenancy agreement. Most of it is standard. Five clauses matter when something goes wrong: what's included, who fixes what, how the deposit comes back, how to change the agreement, and who the landlord's contact is.",
                    "A tenancy agreement is mostly standard. Five clauses decide every dispute.", exact=True)
sw_analogy.icon("door", 40, 40, 2)
sw_analogy.row([("what's included", None, "y"), ("who fixes what", None, "y"), ("the deposit", None, "y"), ("changes", None, "y"), ("contacts", None, "y")], x=150, y=60, h=80, w=112, gap=10, size=16)
sw_analogy.note(450, 190, "the rest: read once, file", "pen", size=19)

sw_how = Doodle(760, 340, "The SOW reading session on 9 June. Each of the five clauses gets a test question. Scope: could two people list the same work from it? Assumptions: is the consequence of a false one written down? Acceptance: could we pass it, and does silence count? Change: is it quick for small things? Key personnel: what happens if someone is ill? Three redlines come out of it, including a catch-all scope clause, services include all work reasonably necessary to achieve the objectives, replaced with a reference to schedule 2.",
                "Five clauses, five test questions, three redlines.", exact=True)
tests = [("§2 scope", "could two people list the same work?"), ("§3 assumptions", "is the consequence written?"),
         ("§5 acceptance", "could we pass it? does silence count?"), ("§7 change", "quick for small things?"), ("§6 key people", "what if someone is ill?")]
for i, (c, q) in enumerate(tests):
    y = 14 + i * 50
    sw_how.box(14, y, 180, 42, c, "y", size=17, rx=4)
    sw_how.box(204, y, 400, 42, q, "paper", size=16, rx=4)
sw_how.box(620, 14, 126, 242, "3 redlines", "pink", size=19)
sw_how.note(380, 300, "“all work reasonably necessary” → “the Services in Schedule 2”", "red", size=19)

SOW = dict(
    slug="statement-of-work", date=date(2027, 6, 9), meta="preferred bidder, week 5", where="FL 19",
    kicker="a.k.a. “the SOW”, read clause by clause",
    tldr="The statement of work is what you'll argue about for the next two years. Read it <b>with the people who'll deliver it</b>, not just with lawyers. Most of it is standard; <b>five clauses</b> decide almost every dispute: <b>scope</b>, <b>assumptions</b>, <b>acceptance</b>, <b>change control</b> and <b>key personnel</b>. Give each one a test question, and redline anything that fails, especially catch-all phrases like “all work reasonably necessary”.",
    chips=[("Family", "the paper"), ("Lives in", "contract/lodestar/SOW-v0.3-redline.pdf"), ("Pairs with", "assumptions, acceptance criteria, change control")],
    problem_side="The Grid, floor 19, 9 June 2027",
    problem="""  <p class="lead">From <b>10 May</b>, Desmond, Anjali Rao (MetroVolt's legal counsel), Callum and Ines meet twice a week to turn the bid into a contract. Draft <b>v0.3</b> arrives on <b>Wednesday 9 June</b>: 64 pages, 11 sections, 6 schedules.</p>
  <ul>
    <li>Callum has read contracts. Hana, Bilal and Oskar, who'll live inside this one, never have.</li>
    <li>Clause <b>2.4</b> says: <i>“The Services include all work reasonably necessary to achieve the Objectives.”</i> <span class="hl-pink">The Objectives include “a single view of every MetroVolt customer”.</span></li>
    <li>The promises register flagged <b>P-23</b>: Ines's own words at the orals, “you won't see change requests for data”. It contradicts assumption A1-07.</li>
  </ul>""",
    problem_figs=[sw_problem],
    sides=dict(client=("Anjali drafts", "<p>MetroVolt's legal team writes for <b>the worst day</b>: if the supplier fails, the contract must make it possible to recover the money, the data and the time. A catch-all scope clause is how lawyers protect a client from gaps they can't foresee.</p>", "If it's not in here, we can't make them do it."),
                vendor=("Ines, Hana and Callum read", "<p>For Wrenfield, every vague phrase is <b>unpriced work</b>. “All work reasonably necessary” to achieve a single view of 2.3 million customers is phase 2, 3 and 4, at a phase 1 price. Ines also needs to un-say P-23 before it becomes a clause.</p>", "If it's in here vaguely, we'll do it for free.")),
    sides_after="Both sides want the same thing, a contract that works on the worst day. They disagree about whose worst day.",
    analogy_side="the tenancy agreement",
    analogy="""  <p>A tenancy agreement is twenty pages of standard text, and <b>five clauses</b> decide every argument: what's included, who fixes what, how the deposit comes back, how the agreement changes, and whom you call. Sensible tenants read those five properly and <b>ask the landlord to change any that are vague</b>, before signing, while everyone is still friendly.</p>""",
    analogy_figs=[sw_analogy],
    map=[("What's included", "§2 scope and Schedule 2 (solution)"),
         ("Who fixes what", "§3 assumptions and dependencies"),
         ("How the deposit comes back", "§5 acceptance, §9 payment"),
         ("How the agreement changes", "§7 change control"),
         ("Whom you call", "§6 key personnel, §8 governance")],
    how_side="five clauses, five test questions, and redlines",
    how="""  <p>Ines books a two-hour reading session for the delivery team, with Callum explaining the legal words. They read the five clauses aloud, each with a <b>test question</b>:</p>
  <ul>
    <li><b>§2 scope</b>: could two people list the same work from this? Clause 2.4 fails. Redline: <i>“The Services are those described in Schedule 2.”</i></li>
    <li><b>§3 assumptions</b>: is the consequence of a false assumption written? Yes, once “absorb” is struck. P-23 is fixed here: A1-07 stays, with its price, and Ines tells Elaine directly that her orals answer was wrong.</li>
    <li><b>§5 acceptance</b>: could we pass it, and what does silence mean? Draft says “to MetroVolt's satisfaction”. Redline (next note).</li>
    <li><b>§7 change control</b>: is it quick for small changes? No: every change needs steering approval. Redline: a small change pool.</li>
    <li><b>§6 key personnel</b>: what happens if someone is ill? Not covered. Added: replacement within 20 working days, with MetroVolt's approval.</li>
  </ul>
  <p>The rest (liability, insurance, data protection, exit) is read once, checked by Wrenfield's lawyer and filed.</p>""",
    how_figs=[sw_how],
    steps=[("Read it with the delivery team", "Two hours, the five clauses aloud."),
           ("Give each clause a test question", "Could two people read it the same way?"),
           ("Hunt for catch-alls", "“Reasonably necessary”, “including but not limited to”, “to our satisfaction”."),
           ("Check the bid made it in", "Assumptions, exclusions, the commercial model, the promises register."),
           ("Fix promises you regret, openly", "In the contract and in person, before signing."),
           ("Let the lawyers do the rest", "Liability, insurance, data protection, exit.")],
    vocab=[("Statement of work (SOW)", "The part of a contract that says what will be done, how and for how much."),
           ("Schedule", "An attachment to the contract with detail: solution, plan, rates, people."),
           ("Redline", "A marked-up draft showing proposed deletions and additions."),
           ("Catch-all clause", "Wording that sweeps unnamed work into scope."),
           ("Order of precedence", "Which document wins when two disagree."),
           ("Entire agreement", "A clause saying only what's in the contract counts.")],
    code=dict(file="contract/lodestar/sow-reading.md", note="delivery team reading · Wed 9 Jun 2027", src="""
SOW v0.3 · the five clauses

clause  test question                           result    action
§2.4    could two people list the same work?    FAIL      redline: "the Services are
        "all work reasonably necessary to                  those described in Schedule 2"
        achieve the Objectives"
§3.2    is a false assumption's consequence     FAIL→OK   strike "absorb"; CR under §7
        written?                                           (+ P-23 corrected with Elaine)
§5.2    could we pass it? does silence count?   FAIL      redline: criteria + 10 days +
        "to MetroVolt's satisfaction"                      deemed acceptance
§7      quick for small changes?                FAIL      add a change pool for < £25k
§6      what if a key person is ill?            MISSING   replacement in 20 working days,
                                                           with MetroVolt's approval
order of precedence: SOW > schedules > tender response > tender   (checked)
"""),
    contract=dict(side="the scope clause, before and after", doc="Lodestar SOW · draft v0.3 · redlined", date="9 June 2027", stamp="redlined",
                  clauses=[("2.4", "<del>The Services include all work reasonably necessary to achieve the Objectives.</del> <ins>The Services are those described in Schedule 2 (Solution) and Schedule 3 (Deliverables). The Objectives describe the purpose of the programme and do not of themselves create obligations.</ins>", "Anjali accepted the second sentence on the third call."),
                           ("1.3", "In case of conflict, the order of precedence is: this SOW, its Schedules, the Tender Response, the Tender.", "so the SOW wins over the bid. read it as if the bid didn't exist.")],
                  plain="a catch-all scope clause turns your client's ambitions into your obligations. Replace it with a reference to the schedules that describe the work, and say that objectives are purpose, not promises."),
    health=dict(now="a",
                g=("trust is high", ["Fewer redlines; a working session with legal.", "Still read the five clauses as a team.", "Keep a list of what you agreed and why."]),
                a=("burned before, careful lawyers", ["Five clauses, test questions.", "Redline catch-alls with a clear alternative.", "Fix regretted promises in person."]),
                r=("take it or leave it", ["Price the vague clauses explicitly.", "Escalate the few that could sink you.", "Walk away if one of them can't move."])),
    pressure=dict(level=3, title="the redlines", cost="three legal calls · one admission at the orals",
                  items=["Admitting P-23 was wrong is uncomfortable. It's far cheaper now than in December.", "Engineers find contracts boring until they're in a dispute. Two hours now saves weeks later."]),
    baseline="Each line compares <b>leaving the contract to lawyers</b> with <b>reading the five clauses with the delivery team and redlining catch-alls</b>.",
    ratings=[(3, 4, "Elaine hears about P-23 from Ines first."),
             (2, 4, "The team knows what it signed up to."),
             (1, 4, "Phase 2 work isn't hidden in phase 1's scope."),
             (1, 5, "Scope means Schedule 2, nothing else."),
             (3, 4, "The design isn't stretched to cover “all customers”."),
             (2, 4, "Missing clauses (illness) found before signing."),
             (2, 4, "Redlines and reasons on file."),
             (4, 3, "Two hours plus three legal calls."),
             (4, 4, "Read once, then the five are referred to often.")],
    pitfalls=[("Lawyers only", "The people who'll live with it never read it.", "a reading session for the delivery team."),
              ("Missing catch-alls", "“All work reasonably necessary” slips through.", "hunt for the usual phrases."),
              ("Trusting the bid", "The SOW wins over the bid if they disagree.", "check the bid's protections made it in."),
              ("Hiding a regretted promise", "It becomes a clause.", "correct it openly, in writing and in person."),
              ("Redlines without alternatives", "“Delete” starts a fight.", "propose wording that protects both sides.")],
    use=["Any contract you'll deliver under.", "Before signing, while everyone is friendly.", "When the bid had promises you regret."],
    skip=["A standard order on your own terms you've used for years: a quick check is enough."],
    related=["<b>How Will We Know It's Done?</b> (next note)", "<b>What Are We Assuming?</b> (vol. 1)", "<b>Who Remembers What We Promised?</b> (vol. 1)", "<b>Make It, Buy It, or Hire It?</b> (Sanne, vol. 2)"],
    quiz=[("Which five clauses decide most disputes?", "Scope, assumptions, acceptance, change control and key personnel."),
          ("What's wrong with “all work reasonably necessary to achieve the Objectives”?", "It turns the client's ambitions into unpriced obligations."),
          ("What does the order of precedence clause tell you?", "Which document wins when two disagree; here the SOW beats the bid."),
          ("How was P-23 fixed?", "A1-07 stayed in the contract with its price, and Ines told Elaine directly that her orals answer was wrong."),
          ("Why read the contract with the delivery team?", "They'll live with it and spot what the work really needs.")],
    quiz_sit=[("Anjali refuses to change 2.4: “we need protection against gaps.” What do you offer?", "Keep the protection but make it bounded: gaps found within discovery are added by agreement without a change request if under a set amount; anything else goes through change control. Objectives stay as purpose.")],
    try_it="Take a contract or agreement you work under. Find the five clauses (scope, assumptions, acceptance, change, people). Give each a test question. Which one fails, and what would you redline?",
    remember="Most of a contract is standard. <span class=\"hl\">Five clauses</span> decide every argument. Read them <span class=\"hl\">with the people who'll live with them</span>.",
    late=dict(when="Wed 9 June 2027 · 22:00 · hotel near The Grid",
              lines=["Hana read §2.4 out loud and said “that's all of it, then”. Yes. That's why we're here.",
                     "Told Elaine my orals answer about data change requests was wrong. She said “I know. I wondered if you'd tell me.”",
                     "Anjali struck “absorb” on the third call. I think she was testing us too."]),
    sources=["UK Government, <i>Model Services Contract</i> and guidance notes.",
             "Ken Adams, <i>A Manual of Style for Contract Drafting</i> (5th ed., 2023).",
             "World Commerce &amp; Contracting, <i>Most Negotiated Terms</i> reports."],
)

# ------------------------------------------------------------------ 02 How Will We Know It's Done?
ac_problem = Doodle(760, 230, "Doodle of the acceptance clause as first drafted: milestones are accepted when completed to MetroVolt's reasonable satisfaction. A cartoon shows the M3 pilot payment, 1.2 million pounds, waiting behind a door labelled satisfaction, with no handle.",
                    "“To MetroVolt's reasonable satisfaction.” £1.2m behind a door with no handle.", exact=True)
ac_problem.box(24, 30, 360, 110, "§5.2 (draft)", "y", sub="“to MetroVolt's reasonable satisfaction”", size=20, subsize=16)
ac_problem.icon("door", 430, 30, 2.2)
ac_problem.box(600, 50, 146, 80, "M3 · £1.2m", "pink", sub="pilot payment", size=20, subsize=15)
ac_problem.note(380, 200, "no criteria, no deadline, no answer = no payment", "red", size=20)

ac_how = Doodle(760, 330, "The acceptance process agreed for every milestone. Wrenfield submits test evidence against written criteria. MetroVolt has ten working days to accept, or to reject with reasons tied to a criterion. If it says nothing, the milestone is deemed accepted. Rejected items are fixed and re-submitted, once, then escalated. Example criteria for M3, the pilot: 20,000 accounts migrated; reconciliation of balances 100 per cent; no more than half a per cent of records in the exception queue; two successful Halvorsen billing cycles.",
                "Criteria, evidence, ten days, reasons, and silence means yes.", exact=True)
flow = [("evidence", "against criteria", "y"), ("10 days", "MetroVolt reviews", "paper"), ("accept", "or reject + reason", "blue"), ("fix, resubmit", "once, then escalate", "paper")]
for i, (h, sub, fill) in enumerate(flow):
    ac_how.box(14 + i * 186, 20, 170, 80, h, fill, sub=sub, size=18, subsize=15)
    if i:
        ac_how.arrow(14 + i * 186 - 14, 60, 14 + i * 186 - 2, 60)
ac_how.note(380, 130, "silence after 10 days = deemed accepted", "red", size=19)
ac_how.box(14, 150, 732, 40, "M3 pilot · acceptance criteria", "green", size=18)
for i, t in enumerate(["20,000 accounts migrated", "balances reconcile 100 %", "≤ 0.5 % in exception queue", "2 billing cycles on Halvorsen"]):
    ac_how.box(14 + i * 186, 198, 174, 60, t, "paper", size=15, rx=4)
ac_how.note(380, 300, "each one testable by someone who wasn't in the room", "pen", size=19)

ACCEPTANCE = dict(
    slug="acceptance-criteria", date=date(2027, 6, 16), meta="preferred bidder, week 6", where="FL 19",
    kicker="a.k.a. “acceptance criteria and deemed acceptance”",
    tldr="Every milestone payment waits behind an acceptance clause, so write it as <b>a test both sides can run</b>: named <b>criteria</b> for each milestone, the <b>evidence</b> you'll provide, a <b>deadline</b> for the client to decide, rejections only <b>with reasons tied to a criterion</b>, and <b>deemed acceptance</b> if they say nothing. “To our satisfaction” is a door without a handle.",
    chips=[("Family", "the paper"), ("Lives in", "SOW §5 and Schedule 4 (milestones)"), ("Pairs with", "the statement of work, the baseline")],
    problem_side="The Grid, floor 19, 16 June 2027",
    problem="""  <p class="lead">Draft clause <b>5.2</b> says a milestone is accepted <i>“when completed to MetroVolt's reasonable satisfaction”</i>. There are no criteria, no deadline, and nothing about what happens if MetroVolt says nothing.</p>
  <ul>
    <li>Milestone M3, the pilot, is worth <b>£1.2m</b>: a quarter of the fixed price, and Wrenfield's cash flow for the spring.</li>
    <li>Oskar remembers a project where acceptance took <b>five months</b> because the client's tester was on leave. <span class="hl-pink">Nobody refused; nobody accepted.</span></li>
    <li>Elaine has the opposite memory: Orion's supplier claimed a milestone was “done” because a document existed.</li>
  </ul>""",
    problem_figs=[ac_problem],
    sides=dict(client=("Elaine and Anjali", "<p>After Orion, MetroVolt wants to accept <b>working results, not documents</b>, and to be able to say no. “Reasonable satisfaction” feels like protection: MetroVolt decides. Nobody on the client side has thought about what silence means.</p>", "We won't pay for another document."),
                vendor=("Oskar and Callum", "<p>Wrenfield wants acceptance to be <b>a test, not an opinion</b>: criteria agreed now, evidence it can produce, a decision by a date. And it wants protection from the slow no: a reviewer on holiday shouldn't stop a payroll.</p>", "Tell us the test now, and we'll pass it.")),
    sides_after="Both fears are reasonable: paying for nothing, and doing the work and never being paid. Written criteria and a deadline cure both.",
    analogy_side="the MOT test",
    analogy="""  <p>A car's MOT isn't “to the inspector's satisfaction”. It's a <b>list of checks</b> (brakes, lights, emissions), each pass or fail, with a written reason for any failure. You can fix the failed item and come back for a re-test. Nobody can fail your car for being the wrong colour, and the garage can't keep it for five months.</p>""",
    map=[("The list of checks", "Acceptance criteria per milestone"),
         ("Pass or fail, each item", "Evidence against each criterion"),
         ("A written reason for a failure", "Rejection tied to a named criterion"),
         ("Fix it and come back", "Fix and resubmit, once, then escalate"),
         ("They can't keep your car for months", "Ten working days, then deemed acceptance")],
    how_side="criteria, evidence, a deadline, reasons, and silence means yes",
    how="""  <p>Oskar and Elaine's test manager write <b>criteria for each milestone</b>, each testable by someone who wasn't in the room. For M3, the pilot: 20,000 accounts migrated; account balances reconcile <b>100 %</b> between MAVIS and the new platform; no more than <b>0.5 %</b> of records left in the exception queue; <b>two successful billing cycles</b> on Halvorsen.</p>
  <p>The process becomes clause 5: Wrenfield submits <b>evidence</b> against the criteria; MetroVolt has <b>10 working days</b> to accept or reject; a rejection must <b>name the criterion</b> that failed; Wrenfield fixes and resubmits once, then it goes to steering. If MetroVolt says nothing in 10 days, the milestone is <b>deemed accepted</b>. Anjali agrees, on one condition: deemed acceptance doesn't apply over Christmas. Fair.</p>
  <p>Elaine gets what she wanted from Orion's lesson: <b>no milestone is a document</b>. Even M2 (design approved) needs the design authority's signed minutes, not just a PDF.</p>""",
    how_figs=[ac_how],
    steps=[("Write criteria per milestone", "Testable by someone who wasn't there."),
           ("Agree the evidence", "Reports, reconciliations, signed minutes, test results."),
           ("Set a deadline to decide", "Ten working days is common."),
           ("Rejections name a criterion", "No criterion, no rejection."),
           ("Add deemed acceptance", "Silence after the deadline is a yes; agree exceptions."),
           ("Limit the loops", "Fix and resubmit once, then escalate.")],
    vocab=[("Acceptance criteria", "The conditions a deliverable must meet to be accepted."),
           ("Acceptance test", "Checking the deliverable against the criteria."),
           ("Deemed acceptance", "Acceptance by default if the client doesn't decide in time."),
           ("Milestone", "A defined, checkable result that triggers payment."),
           ("Exception queue", "Records the migration couldn't move automatically, waiting for a person."),
           ("Reconciliation", "Checking that totals match between the old system and the new one.")],
    code=dict(file="contract/lodestar/schedule-4-acceptance.md", note="agreed Wed 16 Jun 2027", src="""
SCHEDULE 4 · MILESTONES AND ACCEPTANCE (extract)

M2  design approved          signed design authority minutes · Schedule 2 v1.0
M3  pilot live (20,000)      20,000 accounts migrated
                             balances reconcile 100 % (MAVIS ↔ new platform)
                             ≤ 0.5 % of records in the exception queue
                             2 successful billing cycles on Halvorsen
M4  wave 1 live (380,000)    same four criteria at 380,000 · cutover report
M5  hypercare ended          8 weeks · no open severity-1 or -2 incidents
M6  warranty ended           60 days · warranty defects closed

process (§5): evidence → 10 working days → accept / reject naming a criterion
→ fix + resubmit once → steering · silence after 10 days = deemed accepted
(not 20 Dec – 3 Jan)
"""),
    contract=dict(side="the acceptance clause, before and after", doc="Lodestar SOW · draft v0.4 · redlined", date="16 June 2027", stamp="agreed",
                  clauses=[("5.2", "<del>A Milestone is accepted when completed to MetroVolt's reasonable satisfaction.</del> <ins>A Milestone is accepted when the Supplier demonstrates that the Acceptance Criteria in Schedule 4 are met.</ins>", ""),
                           ("5.4", "<ins>MetroVolt shall accept, or reject with reasons referring to the Acceptance Criteria, within 10 Working Days of receiving the evidence. If MetroVolt does neither, the Milestone is deemed accepted, except between 20 December and 3 January.</ins>", "Anjali's Christmas exception. fair.")],
                  plain="acceptance should be a test, not an opinion. Name the criteria, set a deadline, require reasons for a rejection and decide what silence means, so neither side can wait the other out."),
    health=dict(now="a",
                g=("trust is high", ["Simple criteria and a friendly test.", "Still a deadline.", "Deemed acceptance rarely needed."]),
                a=("burned by “document milestones”", ["Working results only.", "Criteria testable by outsiders.", "Deemed acceptance with sensible exceptions."]),
                r=("acceptance used as leverage", ["Evidence submitted formally, dated.", "Rejections without a criterion are invalid: say so.", "Escalate after one loop."])),
    pressure=dict(level=2, title="the payment door", cost="two drafting sessions · one Christmas exception",
                  items=["Criteria feel like extra work in June. They're the difference between a payment in March and a payment in August.", "Write them with the client's tester; their name on them is their buy-in."]),
    baseline="Each line compares <b>“to MetroVolt's reasonable satisfaction”</b> with <b>criteria, evidence, ten days, reasons and deemed acceptance</b>.",
    ratings=[(3, 4, "Elaine pays only for working results."),
             (2, 4, "The team knows exactly what “done” means."),
             (1, 4, "Payments can't be stalled by silence."),
             (2, 5, "Each milestone has four testable criteria."),
             (3, 4, "The pilot is tested on reconciliation, not on slides."),
             (2, 4, "Billing cycles are in the criteria, so the Halvorsen risk is tested early."),
             (2, 4, "Rejections must name a criterion."),
             (4, 3, "Two sessions."),
             (4, 3, "Evidence packs per milestone.")],
    pitfalls=[("“To our satisfaction”", "Acceptance is an opinion.", "criteria in a schedule."),
              ("Document milestones", "Paid for a PDF; nothing works.", "working results only."),
              ("No deadline", "Acceptance waits for a holiday to end.", "ten working days, then deemed accepted."),
              ("Reasonless rejections", "“Not quite right.”", "rejections must name a criterion."),
              ("Endless loops", "Fix, reject, fix, reject.", "one resubmission, then escalate.")],
    use=["Any milestone payment.", "Fixed-price work.", "A client burned by paying for documents."],
    skip=["Pure time and materials with no milestones; still agree a “definition of done” for deliveries."],
    related=["<b>What Does the Contract Actually Say?</b> (previous note)", "<b>Fixed Price, or Time and Materials?</b> (vol. 1)", "<b>What Are We Measured Against?</b> (this volume)", "<b>Definition of Ready and Done</b> (Grace, vol. 3)"],
    quiz=[("Why is “to MetroVolt's reasonable satisfaction” a problem?", "It's an opinion with no criteria or deadline; payment can stall indefinitely."),
          ("What is deemed acceptance?", "A milestone counts as accepted if the client neither accepts nor rejects by the deadline."),
          ("Name two of the M3 acceptance criteria.", "20,000 accounts migrated; balances reconcile 100 %; ≤ 0.5 % in the exception queue; two billing cycles on Halvorsen."),
          ("Why must a rejection name a criterion?", "So rejections are about the agreed test, not new wishes."),
          ("Why did Elaine insist no milestone is a document?", "Orion's supplier was paid for documents while nothing went live.")],
    quiz_sit=[("Day 9 of the review: MetroVolt's tester says she “needs more time to look properly”. What do you do?", "Offer to walk her through the evidence that day, and agree in writing a short extension with a new date, rather than relying on deemed acceptance and souring the relationship.")],
    try_it="Pick a deliverable you owe someone. Write four acceptance criteria a stranger could test, the evidence you'd give, and how long they have to decide. What happens if they don't?",
    remember="Acceptance is <span class=\"hl\">a test, not an opinion</span>: criteria, evidence, a deadline, and <span class=\"hl\">silence means yes</span>.",
    late=dict(when="Wed 16 June 2027 · 21:40 · hotel near The Grid",
              lines=["Four criteria for the pilot. Two billing cycles on Halvorsen is the one that scares me.",
                     "Oskar told the five-month story. Anjali laughed, then added deemed acceptance herself.",
                     "Christmas exception. She's right: nobody should be deemed anything on Boxing Day."]),
    sources=["UK Government, <i>Model Services Contract</i>: testing and acceptance.",
             "Lisa Crispin and Janet Gregory, <i>Agile Testing</i> (2009): acceptance tests.",
             "ISTQB, <i>Foundation Level Syllabus</i>: acceptance testing."],
)

# ------------------------------------------------------------------ 03 How Do We Change the Deal Without a War?
cc_problem = Doodle(760, 230, "Doodle of the first change. On 3 August MetroVolt's accessibility team asks for its accessibility checker to run in Wrenfield's build pipeline. Worth about eight thousand pounds. Under the draft contract, it would need the monthly steering committee, a 14-page form and six weeks.",
                    "An £8k change, a 14-page form, and six weeks to the next steering committee.", exact=True)
cc_problem.box(24, 40, 260, 110, "the ask", "y", sub="accessibility checker · ≈ £8k", size=20, subsize=16)
cc_problem.arrow(290, 95, 340, 95)
cc_problem.box(346, 40, 180, 110, "14-page form", "paper", size=19)
cc_problem.arrow(530, 95, 580, 95)
cc_problem.box(586, 40, 160, 110, "steering", "pink", sub="in 6 weeks", size=19, subsize=16)
cc_problem.note(380, 200, "so people stop asking, and start assuming", "red", size=20)

cc_how = Doodle(760, 330, "Lodestar's change process. Anyone raises a change request on one page. Wrenfield gives an impact assessment within ten working days: cost, time, risk. Changes under 25,000 pounds come out of a 150,000-pound change pool approved by Elaine within a week. Bigger ones go to steering. Every change goes in the change register. CR-001, 12 August: the accessibility checker, 8,000 pounds, approved in four days.",
                "Small changes fast, big ones at steering, all of them written down.", exact=True)
cc_how.box(14, 20, 170, 80, "CR, 1 page", "y", sub="anyone raises", size=19, subsize=15)
cc_how.arrow(188, 60, 216, 60)
cc_how.box(220, 20, 190, 80, "impact", "paper", sub="cost · time · risk · 10 days", size=19, subsize=14)
cc_how.arrow(414, 60, 470, 20, label="< £25k", lx=430, ly=16)
cc_how.arrow(414, 60, 470, 110, label="≥ £25k", lx=420, ly=118)
cc_how.box(474, 0, 272, 60, "Elaine · change pool", "green", sub="£150k · within a week", size=17, subsize=14)
cc_how.box(474, 84, 272, 60, "steering", "blue", sub="monthly", size=18, subsize=14)
cc_how.box(14, 170, 732, 50, "change register: every CR, cost, days, decision", "paper", size=18)
cc_how.box(14, 236, 732, 60, "CR-001 · 12 Aug · accessibility checker", "green", sub="£8,000 · approved in 4 days from the pool", size=18, subsize=15)

CHANGE_CONTROL = dict(
    slug="change-control", date=date(2027, 8, 12), meta="day 39 on site", where="FL 19", pass_kind="contractor",
    kicker="a.k.a. “change control”, the clause everyone uses",
    tldr="Every project changes. The question is whether changes are <b>raised early and priced calmly</b>, or <b>argued over late</b>. Make change control <b>fast for small things</b> (a pre-approved change pool), <b>fair for big ones</b> (an impact assessment, then steering), and <b>always written down</b> (a change register). A process too slow for an £8k change teaches everyone to stop asking and start assuming.",
    chips=[("Family", "the paper"), ("Lives in", "SOW §7 · delivery/lodestar/change-register.md"), ("Pairs with", "assumptions, the baseline, governance")],
    problem_side="The Grid, floor 19, August 2027",
    problem="""  <p class="lead">On <b>Tuesday 3 August</b>, MetroVolt's accessibility team asks for its accessibility checker to run in Wrenfield's build pipeline. It's a good idea and a small job, about <b>£8k</b>. It isn't in Schedule 2.</p>
  <ul>
    <li>The first draft of clause 7 sent <b>every</b> change, however small, to the monthly steering committee, with a 14-page form.</li>
    <li>The next steering meeting is <b>six weeks</b> away. <span class="hl-pink">Hana's instinct is to “just do it”.</span> So is MetroVolt's.</li>
    <li>Ines has seen where “just do it” goes: forty small favours, nothing written down, and an argument in month ten about why the project is late.</li>
  </ul>""",
    problem_figs=[cc_problem],
    sides=dict(client=("Elaine", "<p>For MetroVolt, a change request can feel like the vendor <b>sending a bill for a favour</b>. After Orion, “change request” is a dirty word. Elaine wants small sensible things done without a fight, and big things brought to her early.</p>", "Please don't send me an invoice every time we ask a question."),
                vendor=("Ines and Callum", "<p>For Wrenfield, every unrecorded favour is <b>fixed-price time given away</b>, and invisible when the plan slips. But a heavy process makes Wrenfield look petty. It needs changes to be cheap to raise, quick to decide and always written down.</p>", "Small and fast, but never invisible.")),
    sides_after="Change control isn't about saying no. It's about making every yes visible, so nobody is surprised by the total.",
    analogy_side="the builder's variation sheet",
    analogy="""  <p>A good builder keeps a <b>variation sheet</b> taped to the kitchen wall. “Extra socket, £80” gets a line and a signature on the spot. “Move the staircase” gets a proper quote and a conversation. At the end, nobody is shocked by the bill, because every change was <b>written down when it happened</b>.</p>""",
    map=[("The variation sheet on the wall", "The change register"),
         ("Extra socket, signed on the spot", "A change from the pool, approved by Elaine"),
         ("Move the staircase: a proper quote", "A change of £25k or more, to steering"),
         ("The quote", "The impact assessment: cost, time, risk"),
         ("No shock at the end", "The register's running total at every steering")],
    how_side="a pool for small changes, steering for big ones, a register for all",
    how="""  <p>Back in June, Ines and Anjali rewrote clause 7 around three ideas. <b>Anyone can raise a change</b> on one page. Wrenfield returns an <b>impact assessment within 10 working days</b>: cost (from the rate card), time, risk, and what else it affects. Then the route depends on size: under <b>£25k</b>, Elaine can approve it from a <b>£150k change pool</b>, within a week; £25k and over goes to <b>steering</b>.</p>
  <p>Every change, including the free ones, goes in the <b>change register</b> with its cost and days. Zero-cost changes are still recorded: they consume time, and they show goodwill.</p>
  <p><b>CR-001</b> is the accessibility checker: raised 4 August, assessed 6 August (£8,000, 2 days of Hana, no impact on dates), approved by Elaine on <b>12 August</b>, done the next week. Hana grumbles about the form. The form is one page.</p>""",
    how_figs=[cc_how],
    steps=[("One page to raise a change", "What, why, who asked."),
           ("An impact assessment in 10 days", "Cost from the rate card, time, risk, knock-on effects."),
           ("A pool for small changes", "A named approver and a budget."),
           ("Steering for big ones", "With the assessment, not a debate."),
           ("A register for everything", "Including free changes: they're goodwill, made visible."),
           ("Show the running total", "At every steering, so nobody is surprised.")],
    vocab=[("Change request (CR)", "A formal request to change scope, price, dates or approach."),
           ("Impact assessment", "What a change would cost, take and risk."),
           ("Change pool", "A pre-approved budget for small changes."),
           ("Change register", "The list of all changes and their status."),
           ("Scope creep", "Unrecorded growth of the work."),
           ("Early warning notice", "Telling the other side as soon as you see something that may change cost or time.")],
    code=dict(file="delivery/lodestar/change-register.md", note="as at Thu 12 Aug 2027", src="""
CHANGE REGISTER · LODESTAR                      pool: £150,000 · used £8,000

CR      raised   what                                 cost     days  route   status
CR-001  04 Aug   accessibility checker in pipeline    £8,000   +0    pool    approved 12 Aug
CR-002  09 Aug   discovery end 26 Nov → 10 Dec        £0       +11   steer.  pending (RN-01)
                 (relief for late access)
CN-001  10 Aug   rename "Golden Customer Record" →    £0       +0    note    done
                 "customer record" in all docs
running total    £8,000 · +11 working days (if CR-002 approved)
"""),
    contract=dict(side="the change clause, as signed", doc="Lodestar SOW · §7 change control", date="signed 30 June 2027", stamp="signed",
                  clauses=[("7.2", "Either Party may raise a Change Request. The Supplier shall provide an impact assessment within 10 Working Days, priced using the Rates in Schedule 5.", ""),
                           ("7.4", "Changes with a value below £25,000 may be approved by MetroVolt's Programme Director, up to a total of £150,000 (the Change Pool). Other Changes require approval by the Steering Committee.", "the pool. the best clause we negotiated."),
                           ("7.6", "No Change is binding unless recorded in the Change Register and approved under this clause.", "so “just do it” doesn't count. for either side.")],
                  plain="a good change clause is quick for small things and fair for big ones, and says that only recorded changes count. That protects the client from surprise bills and the vendor from invisible favours."),
    health=dict(now="g",
                g=("trust is high", ["Use the pool generously.", "Record free changes too.", "Show the total monthly."]),
                a=("change requests feel like bills", ["Explain the register, not the price.", "Offer free small changes, recorded.", "Bring big ones early."]),
                r=("changes are a fight", ["Assessments by the book, on time.", "Quote §7.6 calmly.", "Escalate the total, not each item."])),
    pressure=dict(level=2, title="the first change", cost="one grumble · one page",
                  items=["Engineers hate forms. Keep the form to one page and fill it in for them when you can.", "The first change sets the habit. Make it quick and friendly, and everyone will use the process."]),
    baseline="Each line compares <b>every change to steering, or “just do it”</b> with <b>a change pool, an assessment in 10 days and a register for everything</b>.",
    ratings=[(2, 4, "Small asks are answered in days, without a bill fight."),
             (2, 4, "No invisible favours in a fixed price."),
             (1, 4, "Every change is priced or recorded as goodwill."),
             (2, 4, "The register shows what's in, now."),
             (3, 4, "Changes are assessed before they're built."),
             (2, 4, "Knock-on effects are assessed."),
             (1, 5, "§7.6: only recorded changes count."),
             (3, 4, "CR-001 approved in four days."),
             (3, 3, "A register to keep.")],
    pitfalls=[("Everything to steering", "Small changes wait six weeks, so people stop asking.", "a change pool with a named approver."),
              ("“Just do it”", "Invisible favours; a surprise in month ten.", "record everything, even free changes."),
              ("Heavy forms", "Nobody fills them in.", "one page."),
              ("Late assessments", "The client feels stalled.", "ten working days, kept."),
              ("Surprise totals", "Each CR fine, the sum shocking.", "show the running total at every steering.")],
    grimoire=[(6, "scope-creep-swarm", "The Scope-Creep Swarm", "is what “while you're at it, could you just…” becomes without a register.")],
    use=["Any contract with a defined scope.", "Fixed price, especially.", "From the first change, to set the habit."],
    skip=["Pure time and materials, where the client directs the work daily: still keep a light register."],
    related=["<b>What Are We Assuming?</b> (vol. 1)", "<b>What Does the Contract Actually Say?</b> (this volume)", "<b>What Are We Measured Against?</b> (this volume)", "<b>Can We Change That?</b> (Sanne, vol. 2)"],
    quiz=[("What is the change pool for?", "A pre-approved budget so small changes can be decided quickly by a named person."),
          ("Why record free changes?", "They use time, show goodwill, and explain the plan later."),
          ("What does clause 7.6 say, and why does it help both sides?", "Only recorded, approved changes count; no surprise bills, no invisible favours."),
          ("What's in an impact assessment?", "Cost, time, risk and knock-on effects."),
          ("Why make the first change quick and friendly?", "It sets the habit; people will use a process that works.")],
    quiz_sit=[("A MetroVolt manager asks Lottie directly to “quickly add a field”. Lottie does it. What now?", "Record it (as a change note, at no cost if small), thank the manager, and remind both of them gently that requests go through the register, so the work shows up in the plan.")],
    try_it="List the last five things you were asked to do that weren't in the original plan. Were they written down? What did they cost in time? Design a one-page change form you'd actually use.",
    remember="Change control isn't saying no. It's making <span class=\"hl\">every yes visible</span>: fast for small things, fair for big ones, <span class=\"hl\">always written down</span>.",
    late=dict(when="Thu 12 August 2027 · 20:50 · hotel near The Grid",
              lines=["CR-001 approved in four days. £8,000. Elaine signed it standing up.",
                     "Hana says the form is bureaucracy. It's one page. I filled in half of it for her.",
                     "Started the register with a free change too. I want the first steering to see goodwill as well as invoices."]),
    sources=["Project Management Institute, <i>PMBOK Guide</i>: change control.",
             "UK Government, <i>Model Services Contract</i>: change control procedure.",
             "NEC4 Engineering and Construction Contract: early warnings and compensation events."],
)

# ------------------------------------------------------------------ 04 What If the Signature Stalls?
cs_problem = Doodle(760, 240, "Doodle of the decision path changing. Before Horizon: procurement, then Priya, then sign. After 18 May: procurement, then the Horizon Investment Board, advised by Vexmoor, then sign. Vexmoor, which lost the bid, now reviews the winner's business case.",
                    "Before Horizon: three steps. After 18 May: a new board, advised by the firm that lost.", exact=True)
cs_problem.row([("procurement", None, "paper"), ("Priya", None, "y"), ("sign", None, "green")], x=14, y=30, h=60, w=150, gap=40, size=18, arrows=True)
cs_problem.note(600, 66, "before 6 May", "pen", size=19)
cs_problem.row([("procurement", None, "paper"), ("Horizon board", None, "pink"), ("sign?", None, "paper")], x=14, y=130, h=60, w=150, gap=40, size=18, arrows=True)
cs_problem.box(560, 126, 186, 68, "Vexmoor", "pink", sub="reviews the case", size=18, subsize=15)
cs_problem.arrow(556, 160, 506, 160)
cs_problem.note(380, 226, "the losing bidder now advises the decision", "red", size=20)

cs_how = Doodle(760, 300, "What Wrenfield did during the six-week stall. Find the new path: the Horizon Investment Board meets on 22 June, papers due 11 June. Give the new people what they need: a one-page case in Horizon's language, cost out. MAVIS mainframe costs 1.9 million pounds a year; Lodestar's waves retire it. Keep the team together: a letter of intent. Don't lobby around the process; answer Vexmoor's questions fully and on time.",
                "Find the new path, speak its language, keep the team, and don't go around it.", exact=True)
items = [("find the path", "Horizon board, 22 June", "y"), ("speak its language", "cost out: £1.9m/yr", "blue"), ("keep the team", "letter of intent", "green"), ("don't go around", "answer Vexmoor fully", "paper")]
for i, (h, sub, fill) in enumerate(items):
    cs_how.box(14 + (i % 2) * 372, 20 + (i // 2) * 120, 360, 100, h, fill, sub=sub, size=20, subsize=16)
cs_how.note(380, 280, "approved 22 June, with a condition: Vexmoor gives “assurance” at steering", "red", size=17)

CONTRACT_STALLS = dict(
    slug="contract-stalls", date=date(2027, 5, 18), meta="preferred bidder, day 12", where="LEEDS",
    kicker="a.k.a. “award limbo” during a client reorganisation",
    tldr="When a reorganisation freezes your contract, don't wait and don't lobby around it. <b>Find the new decision path</b> (who decides now, when, on what papers), <b>speak its language</b> (a reorg about cost wants a cost case), <b>keep your team together</b> with a written interim arrangement, and <b>answer every question fully</b>, even from a rival advising the client. The people deciding are new and nervous; make yes easy.",
    chips=[("Family", "the paper"), ("Lives in", "contract/lodestar/horizon-case.pdf"), ("Pairs with", "working at risk, mapping the client")],
    problem_side="Wrenfield and MetroVolt, 18 May 2027",
    problem="""  <p class="lead">Twelve days after Wrenfield is named preferred bidder, Desmond calls: <b>Project Horizon</b> now requires every contract over £1m to be re-approved by a new <b>Horizon Investment Board</b>, chaired by Rupert Thorne. <b>Vexmoor Consulting</b>, Rupert's advisers, will review each business case first.</p>
  <ul>
    <li>Vexmoor lost Lodestar three weeks ago. <span class="hl-pink">Now it reviews the winner's business case.</span></li>
    <li>The board meets on <b>22 June</b>. Papers are due on <b>11 June</b>. Lodestar can't sign before then.</li>
    <li>Wrenfield has six people waiting to start on 1 June. Graham asks whether to release them to other work.</li>
    <li>Vivian wants to call Priya and “get this sorted”.</li>
  </ul>""",
    problem_figs=[cs_problem],
    sides=dict(client=("Priya and Elaine", "<p>Priya still wants Lodestar, but she's now defending her own department against a 15 % cut. A new board and new advisers are questioning every programme. She needs <b>arguments Horizon will accept</b>, and no supplier making her look like she can't control her own procurement.</p>", "Help me make the case, and please don't go around me."),
                vendor=("Ines and Graham", "<p>Wrenfield needs to know <b>who decides now</b> and what they need, and it needs to keep its team from being reassigned. It must not look desperate, and it must not complain about Vexmoor, whatever it thinks.</p>", "The deal isn't dead. It's in a different room.")),
    sides_after="A reorg doesn't change whether the project is a good idea. It changes who has to be convinced, and in what words.",
    analogy_side="the house sale when the buyer's bank merges",
    analogy="""  <p>You're selling a house, and the buyer's bank merges with another. The new bank wants its own valuation, by its own surveyor. You don't phone the bank's chairman. You find out <b>what the surveyor needs</b>, have the papers ready, keep your removal van booked on a flexible date, and answer every question politely, even if the surveyor once tried to buy the house himself.</p>""",
    map=[("The bank merges", "Project Horizon (6 May)"),
         ("The new bank's surveyor", "Vexmoor's review of the business case"),
         ("What the surveyor needs", "A cost case in Horizon's language"),
         ("The removal van on a flexible date", "The team, held by a letter of intent"),
         ("Not phoning the chairman", "Not lobbying Rupert around Priya")],
    how_side="the new path, its language, the team, and no shortcuts",
    how="""  <p><b>Find the new path.</b> Ines asks Desmond three questions in writing: who decides, when, and what the paper must contain. Answer: the Horizon Investment Board, 22 June, a four-page template with a section titled “cost reduction”.</p>
  <p><b>Speak its language.</b> Horizon is about cost. Lodestar's original case was about customers. Ines and Nkem rewrite it around one number: <b>MAVIS's mainframe and support cost about £1.9m a year</b>, and each wave of Lodestar shrinks it. Priya submits it as her paper, not Wrenfield's.</p>
  <p><b>Keep the team.</b> Graham asks MetroVolt for a letter of intent (next note) so the six can start preparation at limited risk instead of scattering to other work.</p>
  <p><b>Don't go around.</b> Vivian doesn't call Priya. When Vexmoor's analyst, Bea, sends 23 questions about Wrenfield's plan, Ines answers all 23 within three days, factually, with sources. On <b>22 June</b> the board approves Lodestar with a condition: <b>Vexmoor provides “independent assurance” at the steering committee</b>. The contract is signed on <b>30 June</b>.</p>""",
    how_figs=[cs_how],
    steps=[("Ask who decides now", "In writing: who, when, on what papers."),
           ("Learn the new language", "A cost reorg wants cost; a risk reorg wants risk."),
           ("Help your sponsor make the case", "Their paper, your numbers."),
           ("Hold the team with something written", "A letter of intent, not a promise on the phone."),
           ("Answer every question fully and fast", "Including from a rival advising the client."),
           ("Don't lobby around the process", "It embarrasses your sponsor and rarely works.")],
    vocab=[("Award limbo", "The gap between being chosen and signing, when anything can happen."),
           ("Investment board", "A group approving spending above a threshold."),
           ("Business case", "The argument for spending money: costs, benefits, risks."),
           ("Independent assurance", "A third party reviewing a programme for the sponsor."),
           ("Letter of intent", "A written, limited commitment before the full contract."),
           ("Re-approval", "Getting an already-made decision approved again under new rules.")],
    code=dict(file="contract/lodestar/horizon-case-summary.md", note="submitted by Priya · Fri 11 Jun 2027", src="""
LODESTAR · Horizon Investment Board, 22 June 2027 (summary, page 1 of 4)

cost reduction
  MAVIS mainframe, licences and support        ≈ £1.9m / year
  wave 1 (380,000 accounts) retires            ≈ 16 % of batch load
  all waves (≈ 30 months)                      mainframe decommissioned
  key-person risk: 2 COBOL specialists, 1 retiring in 2029
spend
  phase 1  £380k discovery + £4.62m fixed (wave 1), milestone-paid
risk
  waves, a pilot gate in month 9, paid discovery, named key personnel

questions from Horizon assurance (Vexmoor): 23 · answered in 3 days: 23
decision 22 June: APPROVED, condition: Horizon assurance attends steering
"""),
    contract=dict(side="what the preferred-bidder letter allowed", doc="MetroVolt award letter · 6 May 2027", date="11:40", stamp="subject to",
                  clauses=[("1", "MetroVolt intends to award the Lodestar contract to Wrenfield Digital Ltd, subject to contract, to the standstill period, and to approval under Horizon governance.", "the third “subject to” was the one that bit."),
                           ("5", "MetroVolt reserves the right not to proceed with the award, without liability for bidders' costs.", "which is why we need a letter of intent before we spend.")],
                  plain="until a contract is signed, the client can stop without paying you anything. During a stall, anything you spend without a written interim agreement is your own money."),
    health=dict(now="a",
                g=("the sponsor is strong", ["Support their paper; stay quiet otherwise.", "Short stall, small risk.", "Keep the team informed."]),
                a=("a reorg, a nervous sponsor, a rival as adviser", ["New path, new language.", "Letter of intent for the team.", "Answer the rival's questions fully."]),
                r=("the project may be cancelled", ["Prepare to release the team.", "Leave gracefully; offer a smaller start.", "Keep the relationship for next time."])),
    pressure=dict(level=4, title="limbo", cost="six weeks · six people waiting · one rival reading your plan",
                  items=["Not knowing is worse than bad news. Give the team a date when you'll know more, and keep it.", "Answering a rival's 23 questions politely is galling. It's also exactly what the board will be told about you."]),
    baseline="Each line compares <b>waiting, or lobbying around the process</b>, with <b>the new path, a cost case, a letter of intent and full answers</b>.",
    ratings=[(3, 4, "Priya isn't embarrassed; her paper is strong."),
             (2, 3, "The team waits, but with a date and some work."),
             (2, 3, "Some spend at risk, capped."),
             (3, 3, "Neutral."),
             (3, 3, "Neutral."),
             (2, 4, "The new decision path is known."),
             (2, 4, "23 answers on file, fast and factual."),
             (3, 3, "Six weeks, mostly outside your control."),
             (4, 3, "Extra papers for a new board.")],
    pitfalls=[("Lobbying around the sponsor", "A call to the new boss behind your sponsor's back.", "help the sponsor make the case."),
              ("Speaking the old language", "A customer case to a cost board.", "rewrite for what the new board measures."),
              ("Letting the team scatter", "Your named people are reassigned.", "a letter of intent and a date."),
              ("Complaining about the rival adviser", "It sounds like sour grapes.", "answer fully; let the facts speak."),
              ("Spending unprotected", "If it's cancelled, it's your money.", "only within a written cap.")],
    grimoire=[(5, "suits-from-beyond", "The Suits from Beyond", "is Vexmoor arriving for Horizon, seen from inside MetroVolt."), (5, "reorg-ritual", "The Reorg Ritual", "is the boxes moving on 1 September.")],
    use=["A client reorganises between award and signature.", "A new approval step appears.", "A rival gains influence over the decision."],
    skip=["The delay is purely administrative and dated: just wait, politely."],
    related=["<b>Should We Start Before It's Signed?</b> (next note)", "<b>Who Really Decides Here?</b> (this volume)", "<b>Who Decides What, and Where?</b> (this volume)", "<b>Business Drivers</b> (Ana, vol. 1)"],
    quiz=[("What three questions did Ines ask when the contract stalled?", "Who decides now, when, and what the paper must contain."),
          ("Why rewrite the business case around cost?", "Horizon was a cost-cutting programme; the board measured cost reduction."),
          ("Why answer Vexmoor's questions fully?", "The board would hear how Wrenfield behaved; complaining would look like sour grapes."),
          ("Why not call Priya to “sort it”?", "It would embarrass her and look like lobbying around the process."),
          ("What condition came with approval?", "Vexmoor provides “independent assurance” at the Lodestar steering committee.")],
    quiz_sit=[("Bea's questions include one that hints Wrenfield's plan is copied from Orion. How do you answer?", "Factually: describe the plan's differences (waves, pilot gate, paid discovery) with references to the bid, without commenting on Orion or on the question's tone.")],
    try_it="Think of a decision you're waiting on that has moved to new people. Write down who decides now, when, and what they measure. How would you rewrite your case in their language?",
    remember="A reorg moves the decision to <span class=\"hl\">a different room</span>. Find the room, <span class=\"hl\">speak its language</span>, and don't go around it.",
    late=dict(when="Tue 18 May 2027 · 22:30 · Leeds",
              lines=["Vexmoor reviews our business case. The firm we beat, marking our homework.",
                     "Vivian wanted to call Priya. I asked her to wait one day. She waited.",
                     "MAVIS costs £1.9m a year to keep alive. That's the sentence. Everything else is detail."]),
    sources=["UK HM Treasury, <i>The Green Book</i> (2022): business cases.",
             "John Kotter, <i>Leading Change</i> (1996).",
             "Crown Commercial Service, guidance on contract award and standstill."],
)

# ------------------------------------------------------------------ 05 Should We Start Before It's Signed?
wr_problem = Doodle(760, 230, "Doodle of six Wrenfield people with nothing to do and a calendar from 1 June to 30 June. Graham asks: do we start without a contract? Each week of waiting costs about 35,000 pounds in idle time. Each week of working costs the same, and if the contract is never signed, nobody pays it.",
                    "Each week costs £35k either way: idle, or working without a contract.", exact=True)
for i in range(6):
    wr_problem.circle(60 + i * 60, 70, 22, "blue")
wr_problem.note(210, 130, "six people, ready", "pen", size=19)
wr_problem.icon("calendar", 430, 30, 1.6)
wr_problem.box(540, 30, 200, 100, "≈ £35k / week", "y", sub="idle or at risk", size=20, subsize=16)
wr_problem.note(380, 200, "start without a contract?", "red", size=21)

wr_how = Doodle(760, 300, "The letter of intent of 21 May 2027, drawn as a fence around a small field. Inside the fence: mobilisation planning, environment and access requests, security vetting, discovery preparation. The fence has a cap, 250,000 pounds, and an end date, signature or 30 June. Outside the fence: any build work, any data access, any promise. Wrenfield spent 212,000 pounds inside it, reported weekly to Desmond.",
                "A fence with a cap and an end date. Work inside it; nothing outside it.", exact=True)
wr_how.box(14, 14, 520, 230, None, "green", rx=16, dash=True)
wr_how.head(274, 46, "letter of intent · 21 May", size=20)
for i, t in enumerate(["mobilisation plan", "access requests", "security vetting", "discovery prep"]):
    wr_how.box(34 + (i % 2) * 250, 66 + (i // 2) * 74, 230, 60, t, "paper", size=17)
wr_how.box(550, 14, 196, 108, "cap £250k", "y", sub="end: signature or 30 Jun", size=19, subsize=14)
wr_how.box(550, 136, 196, 108, "outside", "pink", sub="build · data · promises", size=19, subsize=15)
wr_how.note(274, 280, "spent £212k, reported every Friday", "pen", size=19)

WORKING_AT_RISK = dict(
    slug="working-at-risk", date=date(2027, 5, 21), meta="preferred bidder, day 15", where="LEEDS",
    kicker="a.k.a. “letters of intent” and “working at risk”",
    tldr="Starting before the contract is signed can save weeks, and can also mean <b>lending your client money</b> they never repay. Only do it with a <b>written letter of intent</b> that sets <b>a scope</b>, <b>a cap</b>, <b>an end date</b> and says the client pays your costs if it doesn't proceed. Work inside that fence and nowhere else, report the spend weekly, and stop when the money or the date runs out.",
    chips=[("Family", "the paper"), ("Lives in", "contract/lodestar/letter-of-intent.pdf"), ("Pairs with", "the stalled signature, day one")],
    problem_side="Wrenfield, 21 May 2027",
    problem="""  <p class="lead">With the contract stuck until at least 22 June, Wrenfield's six named people are waiting. Each idle week costs Wrenfield about <b>£35k</b> in salaries. Hana has had two other offers inside Wrenfield. Graham wants to start <b>on 1 June anyway</b>, “as a gesture”.</p>
  <ul>
    <li>If Wrenfield starts without anything in writing and Horizon cancels Lodestar, <span class="hl-pink">MetroVolt owes nothing</span>. Clause 5 of the award letter says so.</li>
    <li>If Wrenfield waits, security vetting and laptop requests (dependency D-05) won't even begin until July.</li>
    <li>Elaine would like Wrenfield to start too. She can't promise money she doesn't control.</li>
  </ul>""",
    problem_figs=[wr_problem],
    sides=dict(client=("Elaine and Desmond", "<p>MetroVolt wants the programme to start the day the contract is signed, not six weeks after. But Desmond can't commit spend before Horizon approves. A <b>small, capped letter</b> is something procurement can sign; an open promise isn't.</p>", "We can cover a small, defined piece. Not a programme."),
                vendor=("Graham and Ines", "<p>Wrenfield needs to keep the team together and get the slow things moving (vetting, access, laptops), without lending MetroVolt money. The answer is a letter that pays for <b>preparation</b>, not delivery, up to a cap.</p>", "Prepare at their risk. Build only at ours, and only after signing.")),
    sides_after="A letter of intent is a small contract about the waiting. It lets both sides move without pretending the big contract exists.",
    analogy_side="the deposit on the wedding venue",
    analogy="""  <p>A couple wants a wedding venue, but their budget won't be approved until next month. The venue offers to <b>hold the date and start planning</b> for a <b>small, refundable-to-them deposit</b>, written down: tastings and planning only, no catering ordered, no flowers bought. If the wedding is off, the venue keeps the deposit for the planning it did. Nobody orders the cake.</p>""",
    map=[("Holding the date and planning", "Mobilisation, access requests, vetting, discovery prep"),
         ("A small written deposit", "The letter of intent, capped at £250k"),
         ("No catering ordered", "No build work, no data access"),
         ("Kept if the wedding's off", "MetroVolt pays costs up to the cap if it doesn't proceed"),
         ("Nobody orders the cake", "Nobody promises anything outside the letter")],
    how_side="a fence: scope, cap, end date, costs covered",
    how="""  <p>Graham asks Desmond for a <b>letter of intent</b>, and Ines drafts what it should cover. Signed on <b>Friday 21 May</b>, it sets:</p>
  <ul>
    <li><b>Scope</b>: mobilisation planning, environment and access requests, security vetting, discovery preparation (reading documents MetroVolt shares, planning interviews).</li>
    <li><b>Cap</b>: £250k, at the contract's day rates.</li>
    <li><b>End</b>: on signature (when the work counts towards discovery) or <b>30 June</b>, whichever comes first.</li>
    <li><b>If MetroVolt doesn't proceed</b>: it pays Wrenfield's costs up to the cap.</li>
  </ul>
  <p>Outside the fence: <b>no build work, no access to customer data, no promises</b> to anyone at MetroVolt. Callum reports the spend to Desmond <b>every Friday</b>. By 30 June it's <b>£212k</b>, and the security vetting is done, which is why the team can at least get into the building on 5 July.</p>""",
    how_figs=[wr_how],
    steps=[("Ask for it in writing", "A phone call isn't a letter of intent."),
           ("Define the scope narrowly", "Preparation, not delivery."),
           ("Set a cap and an end date", "Whichever comes first."),
           ("Say who pays if it stops", "Costs up to the cap, at agreed rates."),
           ("Report the spend weekly", "To the person who signed it."),
           ("Stop at the fence", "No work outside the scope, however tempting.")],
    vocab=[("Letter of intent (LOI)", "A short, limited agreement before the main contract."),
           ("Working at risk", "Spending before you're sure you'll be paid."),
           ("Mobilisation", "Getting people, access and tools ready to start."),
           ("Cap", "The maximum the client will pay under the letter."),
           ("Long-stop date", "The date the letter ends if the contract isn't signed."),
           ("Security vetting", "Background checks needed before access to client systems.")],
    code=dict(file="contract/lodestar/loi-burn.md", note="weekly to Desmond · Fri 25 Jun 2027", src="""
LETTER OF INTENT · LODESTAR (signed 21 May 2027)    cap £250,000 · ends 30 Jun

week of    work (inside the scope only)                        spend    to date
24 May     mobilisation plan · access + laptop requests         £31,000  £31,000
31 May     security vetting forms (6) · discovery reading       £44,000  £75,000
07 Jun     interview plan · environment requests                £46,000  £121,000
14 Jun     Horizon questions (23) · discovery prep              £48,000  £169,000
21 Jun     discovery prep · kick-off draft                      £43,000  £212,000

not done (outside the fence): build work · customer data · promises
vetting: 6 of 6 cleared on 28 Jun
"""),
    contract=dict(side="the letter of intent", doc="MetroVolt letter of intent · Lodestar", date="21 May 2027", stamp="capped",
                  clauses=[("2", "MetroVolt authorises the Supplier to carry out the Preparatory Work described in the Annex, up to a maximum of £250,000 at the Rates in the tender response.", "the Annex is the fence. read it to the team."),
                           ("4", "If the Contract is not signed by 30 June 2027, MetroVolt shall pay the Supplier's reasonable costs of the Preparatory Work up to the maximum.", "this is the clause that makes it a letter, not a hope."),
                           ("5", "Preparatory Work carried out after signature of the Contract counts towards the Discovery Services.", "")],
                  plain="a letter of intent is only worth something if it says what happens if the big contract never comes. Without clause 4, it's a polite way of working for free."),
    health=dict(now="a",
                g=("you trust the client", ["A short letter is still worth it.", "Keep the scope small.", "Report the spend anyway."]),
                a=("they want you to start; they can't sign yet", ["A capped letter for preparation.", "No build, no data, no promises.", "Weekly spend reports."]),
                r=("“just start, we'll sort the paper later”", ["No letter, no work.", "Offer a free half-day, not a team.", "Keep the people on other work."])),
    pressure=dict(level=3, title="the waiting", cost="£212k at risk · one tempted managing director",
                  items=["Graham's “gesture” was generous and dangerous. A letter turns it into something MetroVolt can honour.", "The team wants to start building. Preparation feels like waiting; tell them it's what makes July possible."]),
    baseline="Each line compares <b>starting on goodwill with nothing in writing</b> with <b>a capped letter of intent for preparation only</b>.",
    ratings=[(3, 4, "Desmond can sign something small and defined."),
             (2, 4, "The team stays together with real work."),
             (1, 4, "Costs covered up to the cap if it's cancelled."),
             (2, 4, "Preparation only: the fence is written."),
             (3, 3, "Neutral."),
             (1, 4, "Vetting and access started early."),
             (2, 4, "Weekly spend on file."),
             (3, 4, "Vetting done before day one."),
             (4, 3, "A weekly report.")],
    pitfalls=[("Starting on a promise", "Cancelled, and nobody pays.", "a letter that says who pays."),
              ("No cap", "A letter becomes an open cheque.", "a cap and an end date."),
              ("Scope creep inside the letter", "Preparation turns into building.", "a narrow annex, read to the team."),
              ("Touching data early", "Data protection without a contract.", "no customer data before signature."),
              ("Forgetting to report", "The client is surprised by the bill.", "weekly spend to the signer.")],
    use=["Signature is delayed but likely.", "Slow preparation (vetting, access) would delay the start.", "The team would scatter otherwise."],
    skip=["The client won't put anything in writing: then don't start; offer a free half-day at most."],
    related=["<b>What If the Signature Stalls?</b> (previous note)", "<b>What Do We Do on Day One?</b> (this volume)", "<b>Why Can't We Log In?</b> (this volume)", "<b>Fixed Price, or Time and Materials?</b> (vol. 1)"],
    quiz=[("What makes a letter of intent worth having?", "A clause saying the client pays your costs, up to a cap, if the contract isn't signed."),
          ("What four things should it set?", "Scope, cap, end date, and who pays if it stops."),
          ("Why preparation only, not build work?", "Build work commits both sides to a design before the contract, and is the most expensive to lose."),
          ("Why no customer data before signature?", "Data protection terms are in the contract; without them, access is a risk to both sides."),
          ("What did the letter achieve for day one?", "Security vetting was done, so the team could get into the building on 5 July.")],
    quiz_sit=[("On 28 June Elaine asks the team to “just start migrating a test batch” to save time. What do you say?", "Not yet: data and build work are outside the letter, and the contract is two days away. Offer to have everything ready to start the day it's signed.")],
    try_it="Think of work you've been asked to start before an agreement is final. Write a one-paragraph letter of intent: scope, cap, end date and who pays if it stops. Would the other side sign it?",
    remember="Prepare at <span class=\"hl\">their risk, inside a fence</span>. Build only <span class=\"hl\">after signing</span>.",
    late=dict(when="Fri 21 May 2027 · 21:15 · Leeds",
              lines=["Letter of intent signed. £250k cap, 30 June, preparation only.",
                     "Graham wanted to start on goodwill. Goodwill doesn't pay six salaries if Horizon says no.",
                     "Read the annex to the team. Lottie asked if she could “just look at the data”. Not yet. Not for six weeks."]),
    sources=["UK Government, guidance on letters of intent in public contracts.",
             "Practical Law, notes on letters of intent and comfort letters.",
             "NEC4, notes on early contractor involvement."],
)

NOTES = [SOW, ACCEPTANCE, CHANGE_CONTROL, CONTRACT_STALLS, WORKING_AT_RISK]
