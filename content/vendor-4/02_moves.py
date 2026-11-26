# Series 5 · On the Client's Floor · Vol. 4 · Delivery Under Fire · Other people's moves (notes 4–7).
from datetime import date


def on_site(d):
    return f"day {(d - date(2027, 7, 4)).days} on site"


# ------------------------------------------------------------------ 04 Whose Fault Is the Billing Failure?
vb_problem = Doodle(760, 240, "Doodle of integration testing on 16 May 2028. Halvorsen's test system rejects 3.1 per cent of the records in Wrenfield's file. At 11:20 an email from a Halvorsen engineer arrives, copied to Elaine: Wrenfield's extract is malformed. Hana's reply, half-written, is angry.",
                    "3.1 % rejected. 11:20: “Wrenfield's extract is malformed”, copied to Elaine.", exact=True)
vb_problem.box(24, 40, 220, 100, "our file", "blue", sub="spec v1.2", size=21, subsize=15)
vb_problem.arrow(248, 90, 510, 90, label="3.1 % rejected", lx=379, ly=78)
vb_problem.box(516, 40, 220, 100, "Halvorsen test", "y", sub="billing", size=20, subsize=15)
vb_problem.icon("envelope", 300, 150, 1.0)
vb_problem.note(470, 196, "“malformed” (cc: Elaine)", "red", size=19)

vb_how = Doodle(760, 330, "Joint triage under interface agreement IA-01. Within four hours, both firms look at the same evidence: a sample of rejected records, the file header, and Halvorsen's parser logs. The header says SPEC=1.2. Halvorsen's test system runs parser version 1.1, without address line 4. Halvorsen's production was updated; the test system wasn't. Fixed in nine days by Halvorsen. IA-01 gains a version check on test environments too. No blame in the summary.",
                "Same evidence, same table, four hours. The cause was a version, not a vendor.", exact=True)
for i, (h, sub, fill) in enumerate([("rejected sample", "200 records", "paper"), ("file header", "SPEC=1.2", "y"), ("parser logs", "running v1.1", "pink")]):
    vb_how.box(14 + i * 250, 20, 232, 90, h, fill, sub=sub, size=19, subsize=16)
vb_how.box(14, 140, 732, 70, "cause: Halvorsen's TEST system still on parser v1.1 (no address line 4)", "pink", size=17)
vb_how.box(14, 226, 360, 70, "fixed in 9 days", "green", sub="by Halvorsen", size=19, subsize=15)
vb_how.box(386, 226, 360, 70, "IA-01 updated", "blue", sub="version check on test envs too", size=19, subsize=15)
vb_how.note(380, 318, "summary: a cause and a fix. no names.", "pen", size=17)

VENDOR_BLAME = dict(
    slug="vendor-blame", date=date(2028, 5, 16), meta=on_site(date(2028, 5, 16)), where="FL 19", pass_kind="contractor",
    kicker="a.k.a. multi-vendor defect triage",
    tldr="When another vendor blames you, don't answer the email; <b>go to the evidence together</b>. Use the interface agreement's <b>joint triage</b>: the same samples, the same logs, both teams at one table, within hours. Find the <b>cause before the culprit</b>, fix it, improve the agreement so it can't happen again, and write a summary with <b>no names in it</b>. You'll need this vendor again tomorrow.",
    chips=[("Family", "other people's moves"), ("Lives in", "integration/triage/2028-05-16.md · IA-01 v1.2"), ("Pairs with", "the RACI (vol. 2), the billing interface (vol. 3)")],
    problem_side="The Grid, 16 May 2028",
    problem="""  <p class="lead">Integration testing with Halvorsen starts on <b>Tuesday 16 May</b>. Halvorsen's test system <b>rejects 3.1 %</b> of the records in Wrenfield's first full file.</p>
  <ul>
    <li>At 11:20, a Halvorsen engineer emails Hana: <i>“Wrenfield's extract is malformed. Please fix.”</i> Copied to <b>Elaine</b> and Sven.</li>
    <li>Hana's reply, half-written, begins: “Our file follows v1.2 exactly, unlike…”</li>
    <li>The pilot is <b>20 days</b> away. <span class="hl-pink">Billing cycles on Halvorsen are one of its acceptance criteria.</span></li>
  </ul>""",
    problem_figs=[vb_problem],
    sides=dict(client=("Elaine", "<p>Elaine sees two suppliers arguing by email, copied to her, three weeks before the pilot. She doesn't care whose fault it is. She cares whether customers will get bills in June, and whether her suppliers can sort it out without her.</p>", "I'm copied. That means it's about to be my problem."),
                vendor=("Hana and Ines", "<p>Hana is sure the file is right. She may well be. But proving it by email will start exactly the war IA-01 was written to prevent, and make Wrenfield look as defensive as Halvorsen. Ines needs the cause, fast, and a relationship that survives finding it.</p>", "Don't win the email. Find the cause.")),
    sides_after="In a blame war, both vendors usually have part of the cause. In this one, neither vendor did anything wrong on purpose.",
    analogy_side="two mechanics and a car that won't start",
    analogy="""  <p>The garage that fitted the new battery says the old alternator is faulty. The alternator specialist says the battery's wrong. The car owner doesn't need their letters. A good pair of mechanics <b>open the bonnet together</b>, put a meter on it, and find the loose connector neither of them fitted. Then they tell the owner what it was, not whose it was.</p>""",
    map=[("Letters between garages", "Emails between Halvorsen and Wrenfield"),
         ("Opening the bonnet together", "Joint triage under IA-01"),
         ("A meter on it", "Samples, the file header, parser logs"),
         ("The loose connector", "Halvorsen's test system on parser v1.1"),
         ("What it was, not whose", "A blameless summary")],
    how_side="the same evidence, at one table, within four hours",
    how="""  <p>Ines asks Hana not to send her reply. Instead, under <b>IA-01</b> (signed in August 2027), she calls a <b>joint triage</b>: “a rejected file is MetroVolt IT on-call's to start, joint, by evidence, within four hours”. MetroVolt IT's lead chairs it at 14:00. Sven joins by phone.</p>
  <p>The evidence: a sample of <b>200 rejected records</b>, the <b>file header</b>, and Halvorsen's <b>parser logs</b>. The header says <code>SPEC=1.2</code>. The logs show the test system running <b>parser version 1.1</b>, which doesn't know address line 4. Halvorsen updated production in December; the <b>test system was never updated</b>. Every rejected record has an address line 4.</p>
  <p>Nobody's careless; a test environment was forgotten. Halvorsen updates its test system in <b>nine days</b>. <b>IA-01 v1.2</b> adds a rule: every environment, test included, must reject a file whose spec version it doesn't support, loudly. The triage summary goes to Elaine at 17:00: cause, fix, date, the agreement change. No names. Sven calls Ines that evening to say thank you for the tone.</p>""",
    how_figs=[vb_how],
    steps=[("Don't answer the blame email", "Not even to correct it."),
           ("Call the triage the agreement defines", "Within hours, with the right chair."),
           ("Same evidence on one table", "Samples, headers, logs, versions."),
           ("Find the cause before the culprit", "Usually a gap, not a person."),
           ("Fix it and improve the agreement", "So it can't recur."),
           ("Summarise without names", "Cause, fix, date, change.")],
    vocab=[("Joint triage", "Investigating a cross-supplier problem together, by evidence."),
           ("Blameless summary", "A write-up of cause and fix that doesn't name individuals."),
           ("Environment drift", "Test and production systems running different versions."),
           ("Interface agreement", "The written rules for a connection between systems and suppliers."),
           ("Root cause", "The underlying reason, not the first visible symptom."),
           ("Defect ownership", "Who fixes a defect, decided after the cause is known.")],
    code=dict(file="integration/triage/2028-05-16.md", note="joint triage under IA-01 · Tue 16 May 2028", src="""
JOINT TRIAGE · rejected records, Halvorsen test system · 16 May 2028
chair: MetroVolt IT on-call lead · present: Halvorsen (Sven by phone), Wrenfield

symptom     3.1 % of records rejected (11,872 of 382,940 in the test file)
evidence    200 rejected records · file header "HVN|SPEC=1.2|…" · parser logs
finding     test system runs parser v1.1 (production on v1.2 since Dec 2027)
            every rejected record has ADDRESS_LINE_4 (added in v1.2)
cause       test environment not updated with production; no version check
fix         Halvorsen updates test parser → done 25 May (9 days)
prevention  IA-01 v1.2 §5: every environment rejects unsupported spec versions
            with an error; version listed in the weekly environment report
summary to Elaine 17:00: cause · fix · date · agreement change (no names)
"""),
    contract=dict(side="the agreement that did the work", doc="Interface agreement IA-01 · v1.2", date="26 May 2028", stamp="evidence first",
                  clauses=[("IA-01, 4", "Defects at the interface are assigned to a party only after joint triage on the evidence listed in section 3.", "Sven's sentence from 2027. it saved us from our own reply."),
                           ("IA-01, 5", "<ins>Every environment, including test environments, shall reject a file whose stated specification version it does not support.</ins>", "the lesson, written into the agreement.")],
                  plain="a good interface agreement turns blame emails into a triage with rules. Use it the first time, even when you're sure you're right, and improve it with whatever the triage teaches."),
    health=dict(now="g",
                g=("vendors cooperate", ["Triage quickly, informally.", "Share the fix credit.", "Update the agreement."]),
                a=("an accusing email, copied to the client", ["Don't reply in kind.", "Triage under the agreement.", "Blameless summary to the client."]),
                r=("a real blame war", ["Evidence packs, dated.", "Client chairs the triage.", "Escalate the process, not the people."])),
    pressure=dict(level=4, title="being blamed", cost="an accusing email · 20 days to the pilot",
                  items=["Being blamed in front of the client makes everyone want to fire back. A calm triage at 14:00 is the strongest reply.", "Hana was right about the file. Let the evidence say so; she doesn't have to."]),
    baseline="Each line compares <b>a reply-all defending the file</b> with <b>joint triage on the same evidence, a fix, an improved agreement and no names</b>.",
    ratings=[(3, 5, "Elaine sees suppliers fix it without her."),
             (3, 4, "Hana is vindicated without a fight."),
             (3, 3, "Neutral."),
             (3, 4, "The cause and fix are written."),
             (3, 4, "The design was right; the environment wasn't."),
             (2, 5, "Version checks now catch drift everywhere."),
             (3, 5, "Triage record and IA-01 v1.2."),
             (3, 4, "Cause found in four hours."),
             (3, 3, "Another check to run.")],
    pitfalls=[("Winning the email", "You start a war.", "don't reply; triage."),
              ("Arguing without evidence", "Opinions against opinions.", "samples, headers, logs."),
              ("Naming people", "The other vendor's engineer is humiliated.", "cause, not culprit."),
              ("Fixing but not preventing", "It happens again in wave 2.", "improve the agreement."),
              ("Leaving the client out", "They hear about it anyway.", "a summary the same day.")],
    grimoire=[(2, "credit-vampire", "The Credit Vampire", "has a cousin, the Blame Vampire, who feeds on other teams' mistakes. Starve it with evidence.")],
    use=["Another vendor blames you.", "A defect crosses a supplier boundary.", "The client is copied on an accusation."],
    skip=["The defect is clearly inside your own system: just fix it and say so."],
    related=["<b>Who Does What When Three Firms Share a Project?</b> (vol. 2)", "<b>What Does the Billing System Really Need?</b> (vol. 3)", "<b>What Happens When Steering Turns on Us?</b> (this volume)", "<b>The Vendor Went Quiet</b> (Eli, vol. 4)"],
    quiz=[("What should you do with an accusing email?", "Not reply in kind; call the joint triage the interface agreement defines."),
          ("What evidence did the triage use?", "200 rejected records, the file header and Halvorsen's parser logs."),
          ("What was the cause?", "Halvorsen's test system still ran parser v1.1, without address line 4."),
          ("What changed in IA-01?", "Every environment must reject unsupported spec versions with an error."),
          ("Why a summary without names?", "The cause was a gap, not a person; naming people damages the relationship you'll need tomorrow.")],
    quiz_sit=[("The triage shows the cause is partly Wrenfield's: 0.4 % of records had a date in the wrong format. What do you do?", "Say so first, in the summary, with the fix and date. Owning your part quickly is what makes the other vendor own theirs.")],
    try_it="Remember the last time another team blamed yours. Write down what evidence would have settled it, and who should have been at the table. Draft the blameless summary.",
    remember="Don't win the email. <span class=\"hl\">Find the cause together</span>, fix it, and write it up <span class=\"hl\">without names</span>.",
    late=dict(when="Tue 16 May 2028 · 21:30 · hotel near The Grid",
              lines=["Hana's reply would have been right, and it would have been a disaster. She deleted it herself.",
                     "Parser v1.1 on Halvorsen's test system. The version header did its job: we found it in an hour.",
                     "Sven called to thank us for the tone. I said the tone was his, in the café, in 2027."]),
    sources=["John Allspaw, “Blameless PostMortems and a Just Culture” (Etsy, 2012).",
             "Kevin Holland, <i>An Introduction to Service Integration and Management (SIAM)</i> (2015).",
             "Sidney Dekker, <i>The Field Guide to Understanding 'Human Error'</i> (3rd ed., 2014)."],
)

# ------------------------------------------------------------------ 05 What Do We Do When Our Rival Advises the Client?
ra_problem = Doodle(760, 240, "Doodle of Vexmoor's role growing: in June 2027, Horizon assurance, attending steering, no vote. In May 2028, Oliver Thane proposes a Lodestar acceleration review, at Rupert's request: Vexmoor to review Wrenfield's migration tooling, with access to the source code and interviews with Wrenfield's engineers. Bea's email asks for the code repository by Friday.",
                    "June 2027: assurance, no vote. May 2028: “send us your source code by Friday”.", exact=True)
ra_problem.box(24, 50, 220, 90, "June 2027", "paper", sub="assurance · no vote", size=19, subsize=15)
ra_problem.arrow(248, 95, 300, 95)
ra_problem.box(304, 30, 432, 130, "May 2028", "pink", sub="“acceleration review”: code access + interviews", size=21, subsize=15)
ra_problem.note(380, 210, "the firm that lost the bid, asking for the winner's code", "red", size=19)

ra_how = Doodle(760, 330, "How Wrenfield responded. Ask the sponsor to define the review in writing: purpose, scope, access, dates. Give everything the contract entitles MetroVolt to: documents, test results, rehearsal reconciliation reports, the decision log. Protect what it doesn't: source code under clause 12 intellectual property, offered instead as a supervised walkthrough. Interviews with Elaine present. An evidence pack ready in three days. No comment on Vexmoor, ever.",
                "Sponsor defines the scope; give what the contract gives; protect what it protects; let evidence answer.", exact=True)
for i, (h, sub, fill) in enumerate([("scope in writing", "from Priya", "y"), ("give", "docs · tests · logs", "green"), ("protect", "code: walkthrough only", "pink"), ("interviews", "Elaine present", "blue")]):
    ra_how.box(14 + i * 186, 20, 174, 100, h, fill, sub=sub, size=18, subsize=14)
ra_how.box(14, 150, 732, 70, "evidence pack in 3 days", "paper", sub="baseline v2.0 · status measures · rehearsal reports · RAID · decision log · change register", size=18, subsize=14)
ra_how.note(380, 270, "no comment about Vexmoor, in any room, in any email", "red", size=18)

RIVAL_ADVISER = dict(
    slug="rival-adviser", date=date(2028, 5, 24), meta=on_site(date(2028, 5, 24)), where="FL 27", pass_kind="contractor",
    kicker="a.k.a. “independent assurance” by a competitor",
    tldr="When a rival becomes your client's adviser, don't fight them and don't fear them. Ask the <b>sponsor</b> to define the reviewer's <b>scope in writing</b>. Give everything the contract entitles the client to, quickly and completely; protect what the contract protects (your <b>intellectual property</b>, your people's time) and offer a fair alternative. Keep an <b>evidence pack</b> ready, and never say a word about the rival. Let the evidence answer.",
    chips=[("Family", "other people's moves"), ("Lives in", "assurance/evidence-pack/ (refreshed monthly)"), ("Pairs with", "the stalled signature (vol. 2), the steering ambush")],
    problem_side="The Grid, May 2028",
    problem="""  <p class="lead">Since June 2027 <b>Vexmoor</b> has attended Lodestar's steering as “Horizon assurance”, with no vote. On <b>24 May 2028</b>, Oliver Thane tells Priya that Rupert wants a <b>“Lodestar acceleration review”</b>.</p>
  <ul>
    <li>Bea emails Ines the same afternoon: Vexmoor needs <b>access to Wrenfield's source code repository</b> by Friday, and one-to-one interviews with Hana, Bilal and Oskar.</li>
    <li>Vexmoor built Orion's hub, lost Lodestar to Wrenfield, and will bid for phase 2 in 2029.</li>
    <li>Graham's reaction from Leeds: “Absolutely not. Tell them where to go.” <span class="hl-pink">Rupert chairs the board that approves phase 2.</span></li>
  </ul>""",
    problem_figs=[ra_problem],
    sides=dict(client=("Priya", "<p>Priya didn't ask for the review; Rupert did. She trusts Wrenfield more than she did a year ago, and she can't refuse Horizon. She needs Wrenfield to cooperate visibly, and she needs the review to stay a review.</p>", "Help me give Rupert his review without losing my programme."),
                vendor=("Ines", "<p>Wrenfield has nothing to hide in its delivery, and a lot to protect in its code and its people's attention three weeks before the pilot. Refusing looks guilty; complying fully hands a future rival its tooling. The answer has to be fair to MetroVolt and to Wrenfield.</p>", "Transparent about the work. Careful about the code.")),
    sides_after="A rival adviser is uncomfortable, and normal. Big clients use consultants who also bid. The contract, not your feelings, decides what they see.",
    analogy_side="the second opinion",
    analogy="""  <p>A patient's family asks another hospital for a <b>second opinion</b>. A good surgeon doesn't take offence and doesn't refuse. She sends the <b>scans, notes and test results</b> promptly, offers to talk the other doctor through them, and doesn't hand over her private research notes. If the second opinion agrees, good. If it disagrees, the evidence is on the table.</p>""",
    map=[("The second opinion", "Vexmoor's acceleration review"),
         ("Scans, notes and results", "Documents, test results, rehearsal reports, decision log"),
         ("Talking the other doctor through them", "A supervised code walkthrough"),
         ("Private research notes", "Source code, protected under clause 12"),
         ("The family decides", "Priya and Rupert decide what the review means")],
    how_side="scope from the sponsor, give, protect, evidence",
    how="""  <p><b>Scope in writing, from the sponsor.</b> Ines doesn't reply to Bea. She asks Priya and Elaine for a one-page terms of reference: purpose, questions, access, dates, and who receives the findings. Priya writes it in two days. Purpose: “confidence in the wave 1 date”.</p>
  <p><b>Give what the contract gives.</b> MetroVolt is entitled to programme documents, test results and records. Wrenfield sends a complete <b>evidence pack</b> in three days: baseline v2.0, the status measures, both rehearsal reconciliation reports, the RAID page, the decision and change logs.</p>
  <p><b>Protect what it protects.</b> Wrenfield's migration tooling is its own pre-existing <b>intellectual property</b> (clause 12). Instead of repository access, Hana offers a <b>supervised two-hour walkthrough</b> of how it works and how it's tested. Interviews happen with <b>Elaine present</b>, capped at an hour each.</p>
  <p><b>Let evidence answer.</b> Ines tells the team one rule: nobody says anything about Vexmoor, in any room or email. The review's report, in June, says the date is “achievable with risk”, which is what Wrenfield's own status already said.</p>""",
    how_figs=[ra_how],
    steps=[("Don't answer the reviewer directly", "Go to the sponsor first."),
           ("Get terms of reference in writing", "Purpose, questions, access, dates."),
           ("Give what the contract gives, fast", "Complete and well organised."),
           ("Protect what it protects, fairly", "Offer an alternative (a walkthrough)."),
           ("Protect your people's time", "Capped interviews, the client present."),
           ("Never comment on the rival", "Let your evidence do it.")],
    vocab=[("Independent assurance", "A review by a third party to give the sponsor confidence."),
           ("Terms of reference", "A written description of a review's purpose, scope and access."),
           ("Intellectual property (IP)", "Rights in what you create, such as code and tools."),
           ("Background IP", "IP a supplier owned before the contract and uses in it."),
           ("Evidence pack", "Organised documents and records ready to show a reviewer."),
           ("Conflict of interest", "When an adviser may benefit from the advice they give.")],
    code=dict(file="assurance/evidence-pack/README.md", note="sent Fri 26 May 2028", src="""
EVIDENCE PACK · Lodestar acceleration review (terms of reference: Priya, 26 May)

purpose     "confidence in the wave 1 date" · findings to Priya and Rupert
contents    01 baseline v2.0 (DL-031) · 02 weekly status measures, 8 weeks
            03 rehearsal 1 reconciliation (98.1 %) + R7 fix evidence
            04 RAID top 12 + backlog · 05 decision log DL-001..DL-044
            06 change register · 07 test summary · 08 IA-01 + triage records
code        background IP (SOW §12): supervised walkthrough, 2 h, Hana, Thu 1 Jun
interviews  Hana, Bilal, Oskar · 1 h each · Elaine present
house rule  no comment about Vexmoor by anyone at Wrenfield, anywhere
outcome     review report (21 Jun): "wave 1 date achievable, with risk" (= our status)
"""),
    contract=dict(side="what MetroVolt can see, and what it can't", doc="Lodestar SOW · §12 (intellectual property) and §13 (records)", date="signed 30 June 2027", stamp="background IP",
                  clauses=[("12.2", "The Supplier's Background IP, including its migration tooling, remains the Supplier's. MetroVolt receives a licence to use it for the Services. Disclosure of Background IP source code to third parties requires the Supplier's consent.", "Vexmoor is a third party. a walkthrough is consent, on our terms."),
                           ("13.1", "The Supplier shall keep and, on request, provide MetroVolt and its auditors with records of the Services, including plans, test results and reports.", "everything in the pack. promptly. completely.")],
                  plain="the contract usually separates what the client may inspect (records, results) from what the supplier keeps (its own tools and code). Being generous with the first makes protecting the second look fair rather than defensive."),
    health=dict(now="a",
                g=("the sponsor trusts you", ["Cooperate warmly.", "Pack sent in days.", "The review confirms your status."]),
                a=("a rival adviser, a nervous sponsor", ["Terms of reference from the sponsor.", "Give fully; protect fairly.", "Silence about the rival."]),
                r=("the review is a disguised bid", ["Everything in writing.", "Escalate scope creep in the review to the sponsor.", "Evidence over argument."])),
    pressure=dict(level=4, title="the rival inside", cost="a week of preparation · three weeks before the pilot",
                  items=["Graham's anger is natural. Saying “absolutely not” would make Wrenfield the problem in Rupert's eyes.", "The house rule about Vexmoor protects the team from saying something they'll regret in a lift."]),
    baseline="Each line compares <b>refusing, or handing over everything</b> with <b>sponsor-defined scope, a full evidence pack and a supervised walkthrough</b>.",
    ratings=[(3, 4, "Priya can give Rupert his review."),
             (3, 3, "Interviews capped; the team keeps working."),
             (3, 3, "Neutral."),
             (3, 4, "The review's scope is written."),
             (3, 3, "Neutral."),
             (2, 4, "The review confirms what status already said."),
             (2, 5, "Everything sent is listed and dated."),
             (3, 3, "A week of preparation."),
             (3, 3, "Keep the pack current.")],
    pitfalls=[("Refusing", "You look as if you're hiding.", "give what the contract gives."),
              ("Handing over everything", "Your tooling goes to a future rival.", "protect background IP; offer a walkthrough."),
              ("Answering the reviewer directly", "Scope grows by email.", "terms of reference from the sponsor."),
              ("Commenting on the rival", "It becomes the story.", "silence; evidence."),
              ("Unprepared evidence", "Days lost assembling it.", "keep an evidence pack current.")],
    grimoire=[(5, "suits-from-beyond", "The Suits from Beyond", "is the same visit from MetroVolt's side: how to talk to the consultants without talking yourself out of a job.")],
    use=["A third party reviews your work for the client.", "The reviewer is, or may be, a competitor.", "Requests exceed what the contract gives."],
    skip=["An agreed audit under the contract with an independent auditor: just comply."],
    related=["<b>What If the Signature Stalls?</b> (vol. 2)", "<b>What Happens When Steering Turns on Us?</b> (next note)", "<b>How Do We Compete with a Big Consultancy?</b> (vol. 1)", "<b>What Are We Measured Against?</b> (vol. 2)"],
    quiz=[("Why go to the sponsor before answering the reviewer?", "So the review's scope is defined by the client in writing, not grown by email."),
          ("What did MetroVolt get under clause 13?", "Plans, test results, reports and records: the evidence pack."),
          ("Why not give repository access?", "The tooling is Wrenfield's background IP; disclosure to third parties needs consent."),
          ("What was offered instead?", "A supervised two-hour walkthrough with Hana."),
          ("What was the house rule?", "Nobody at Wrenfield comments on Vexmoor, anywhere.")],
    quiz_sit=[("In an interview, Bea asks Bilal whether Wrenfield “is really on track”. Elaine is present. What should Bilal say?", "What the status measures say, with the numbers, and that he's happy to show the data. No opinions about the plan beyond his area, and nothing about Vexmoor.")],
    try_it="Imagine a rival reviewing your work tomorrow. What would you give them under your contract, and what would you protect? Assemble the evidence pack you'd send.",
    remember="Give <span class=\"hl\">what the contract gives</span>, fast and fully. Protect what it protects, fairly. And never say a word about <span class=\"hl\">the rival</span>.",
    late=dict(when="Wed 24 May 2028 · 22:40 · hotel near The Grid",
              lines=["Bea wants our source code by Friday. Graham wants me to tell them where to go. Priya wants a review that stays a review.",
                     "Asked Priya for terms of reference. She wrote them in two days, better than I would have.",
                     "House rule: not a word about Vexmoor. Hana says that's the hardest rule we've ever had."]),
    sources=["UK Infrastructure and Projects Authority, guidance on independent assurance reviews.",
             "UK Government, <i>Model Services Contract</i>: intellectual property and records.",
             "David Maister, <i>True Professionalism</i> (1997)."],
)

# ------------------------------------------------------------------ 06 What Happens When Steering Turns on Us?
sa_problem = Doodle(760, 250, "Doodle of the steering committee on 28 June 2028. Without warning, Oliver Thane shows a slide: Lodestar nine weeks behind; recommend a Vexmoor-led recovery. Lord Varnish, attending for once, says: I always said this would happen. Priya looks at Ines. The pilot went live on 5 June but its acceptance was rejected on 23 June because 0.8 per cent of records were in the exception queue, not 0.5.",
                    "Slide 1: “9 weeks behind. Recommend Vexmoor-led recovery.” Nobody had seen it before.", exact=True)
sa_problem.box(150, 20, 460, 120, "9 WEEKS BEHIND", "pink", sub="“recommend a Vexmoor-led recovery”", size=26, subsize=17)
sa_problem.box(14, 170, 220, 60, "Lord Varnish", "paper", sub="“I always said…”", size=17, subsize=14)
sa_problem.box(270, 170, 220, 60, "Priya", "paper", sub="looks at Ines", size=17, subsize=14)
sa_problem.box(526, 170, 220, 60, "pilot", "y", sub="0.8 % vs 0.5 %", size=17, subsize=14)

sa_how = Doodle(760, 330, "Ines's response in the room, and after. In the room: thank Oliver; don't argue the number; ask for the data behind it; promise a written answer in 48 hours; ask Priya to defer any decision until then. After: compare the claim with the evidence. The nine weeks came from comparing progress with baseline version 1, before the change request. Against baseline v2.0 the slip is two weeks, the pilot acceptance. Answer in writing on Friday. And from then on, pre-wire every steering: papers shared with Oliver two days before.",
                "In the room: thanks, a question, 48 hours. After: evidence in writing. From then on: no surprises in either direction.", exact=True)
for i, (h, sub, fill) in enumerate([("thank", "don't argue", "paper"), ("ask", "“the data behind 9?”", "y"), ("48 hours", "written answer", "blue"), ("defer", "no decision today", "green")]):
    sa_how.box(14 + i * 186, 20, 174, 90, h, fill, sub=sub, size=19, subsize=14)
sa_how.box(14, 140, 732, 70, "the 9 weeks were measured against baseline v1.0 (pre CR-007)", "pink", sub="against v2.0: 2 weeks (pilot acceptance)", size=17, subsize=15)
sa_how.box(14, 230, 732, 60, "from now on: every steering paper shared with Oliver two days before", "paper", size=17)
sa_how.note(380, 316, "and Oliver shares his with us. Priya made it a rule.", "pen", size=17)

AMBUSH = dict(
    slug="steering-ambush", date=date(2028, 6, 28), meta=on_site(date(2028, 6, 28)), where="FL 27", pass_kind="contractor",
    kicker="a.k.a. the surprise slide at steering",
    tldr="When someone ambushes you at a steering committee, <b>don't fight the slide in the room</b>. Thank them, <b>ask for the data</b> behind the claim, promise a <b>written answer in 48 hours</b>, and ask the chair to <b>defer any decision</b> until then. Then answer with evidence, calmly, in writing. And change the rules so it can't happen again: <b>every paper shared before</b> every meeting, in both directions.",
    chips=[("Family", "other people's moves"), ("Lives in", "governance/steering/2028-06-28-response.md"), ("Pairs with", "the rival adviser, the watermelon report, delivering bad news (vol. 3)")],
    problem_side="The Grid, room 27A, 28 June 2028",
    problem="""  <p class="lead">The pilot, <b>Ashgrove</b>, went live on <b>Monday 5 June</b>: 20,000 accounts, two billing cycles fine, balances reconciled. But <b>0.8 %</b> of records were left in the exception queue; the criterion is <b>0.5 %</b>. On <b>23 June</b> MetroVolt rejected the milestone, correctly, naming the criterion.</p>
  <ul>
    <li>At steering on <b>Wednesday 28 June</b>, Oliver Thane asks to “share a perspective”. His slide: <b>“Lodestar: 9 weeks behind. Recommend Vexmoor-led recovery.”</b></li>
    <li>Nobody at Wrenfield, and not Priya either, has seen it before.</li>
    <li>Lord Varnish, attending for the first time since the kick-off: <span class="hl-pink">“I always said this would happen.”</span></li>
  </ul>""",
    problem_figs=[sa_problem],
    sides=dict(client=("Priya", "<p>Priya is ambushed too: a slide about her programme, unseen, in front of Lord Varnish and Rupert's delegate. If Wrenfield argues in the room, she's chairing a fight between suppliers. If Wrenfield says nothing, the slide becomes the truth by default.</p>", "Don't make me referee this today."),
                vendor=("Ines", "<p>Ines's instinct is to show the baseline on her laptop and prove the slide wrong on the spot. She might even succeed, and look exactly as defensive as Oliver hopes. The slide's power is surprise; time and evidence take it away.</p>", "Don't win the room. Win Friday.")),
    sides_after="Ambushes work by making you defend yourself badly in public. Refusing to be rushed is most of the defence.",
    analogy_side="the cross-examination",
    analogy="""  <p>A witness under hostile cross-examination who's shown an unexpected document doesn't guess at it. A good one says: <b>“I'd need to see where that figure comes from before I can comment.”</b> The judge allows time. Later, with the source in hand, the witness explains calmly that the figure compared this year with the wrong year.</p>""",
    map=[("An unexpected document", "Oliver's slide"),
         ("“I'd need to see where that comes from”", "“Could we see the data behind nine weeks?”"),
         ("The judge allows time", "Priya defers the decision 48 hours"),
         ("Compared with the wrong year", "Measured against baseline v1.0, not v2.0"),
         ("Explaining calmly later", "A written answer on Friday")],
    how_side="in the room: thank, ask, 48 hours; after: evidence; then: new rules",
    how="""  <p><b>In the room</b>, Ines says four sentences: <i>“Thank you, Oliver. We take any view of the date seriously. Could we see the data behind the nine weeks? We'll answer in writing by Friday, and I'd ask that no decision is taken until then.”</i> Priya agrees immediately; it gets her out of refereeing. Lord Varnish says nothing more.</p>
  <p><b>After</b>, Bea sends the spreadsheet that afternoon (to her credit, promptly). The nine weeks compare today's progress with <b>baseline v1.0</b>, from before CR-007. Against <b>baseline v2.0</b>, agreed in February, the slip is <b>two weeks</b>: the pilot's acceptance, rejected on 23 June for 0.8 % exceptions, being fixed for resubmission.</p>
  <p><b>Friday, in writing</b>: two pages to Priya, copied to the steering: the two baselines side by side, the pilot criterion and its fix, the wave 1 date unchanged with nine days of buffer left. No adjectives about Vexmoor. Priya forwards it to Rupert without comment.</p>
  <p><b>New rules</b>, proposed by Ines and made by Priya: every steering paper, from anyone, is shared <b>two days before</b>. Ines meets Oliver before every steering from then on. He shares his papers too.</p>""",
    how_figs=[sa_how],
    steps=[("Stay calm and thank them", "The room is watching you, not the slide."),
           ("Ask for the data", "One question, no counter-argument."),
           ("Promise a written answer with a date", "48 hours is usually enough."),
           ("Ask the chair to defer decisions", "It helps the chair too."),
           ("Answer with evidence, in writing", "Side by side, no adjectives."),
           ("Change the rules", "Papers shared before every meeting, both ways.")],
    vocab=[("Ambush", "Surprising someone with criticism in a meeting they can't prepare for."),
           ("Pre-wiring", "Sharing positions and papers before a meeting."),
           ("Deferral", "Postponing a decision until information is available."),
           ("Baseline confusion", "Comparing progress with an out-of-date plan."),
           ("Right of reply", "A chance to answer a claim before decisions are made."),
           ("No-surprises rule", "Agreeing nobody brings unseen papers to a meeting.")],
    code=dict(file="governance/steering/2028-06-28-response.md", note="sent Fri 30 Jun 2028, 11:00", src="""
RESPONSE TO "LODESTAR: 9 WEEKS BEHIND" (steering, 28 Jun 2028)

claim       9 weeks behind (Horizon assurance slide 1)
source      Bea's sheet (received 28 Jun, 16:20): progress vs baseline v1.0
            (pilot 6 Mar, wave 1 24 Jun 2028)
baseline    v2.0 (DL-031, 11 Feb 2028): pilot 5 Jun, wave 1 Sat 23 Sep 2028
against v2.0
  pilot     live 5 Jun ✓ · M3 rejected 23 Jun: exceptions 0.8 % (criterion 0.5 %)
            cause: duplicate-merge rule too cautious · fix: sprint 23 ·
            resubmit 30 Jun → accept expected 3 Jul      slip: 2 weeks (M3 only)
  wave 1    23 Sep unchanged · buffer remaining: 9 working days
request     no change to governance; papers shared 2 days before each steering
"""),
    contract=dict(side="the governance rule that stops ambushes", doc="Lodestar SOW · Schedule 7, §2.7 (as amended)", date="v1.3 · 5 Jul 2028", stamp="no surprises",
                  clauses=[("2.7", "<ins>Papers for the Steering Committee, from any attendee, shall be circulated to all members at least two Working Days before the meeting. Papers not circulated may be noted but not decided upon.</ins>", "Priya's rule, after 28 June."),
                           ("2.6", "A representative of Horizon Assurance may attend the Steering Committee and receive its papers, without a vote.", "receive papers. now also share them.")],
                  plain="a governance rule that undecided papers can be noted but not decided on removes the power of a surprise slide, for everyone, including you."),
    health=dict(now="a",
                g=("the sponsor trusts you", ["A quiet word after the meeting may be enough.", "Answer in writing anyway.", "Propose the paper rule."]),
                a=("a rival with the sponsor's boss's ear", ["Thank, ask, 48 hours.", "Evidence side by side.", "Pre-wire every steering after."]),
                r=("a campaign to replace you", ["Everything in writing.", "Formal right of reply.", "Escalate the process, never the people."])),
    pressure=dict(level=5, title="ambushed in public", cost="a slide · a senior “I always said” · 48 hours",
                  items=["The urge to prove the slide wrong in the room is overwhelming. Fight it; you'll win more slowly and much more completely.", "Lord Varnish's comment hurts most. It isn't about you; it's about Orion. Let it go."]),
    baseline="Each line compares <b>arguing the slide in the room</b> with <b>thanks, a question, 48 hours, a written answer and a new paper rule</b>.",
    ratings=[(3, 5, "Priya forwarded the answer to Rupert without comment."),
             (2, 3, "Two days of hard work, no public fight."),
             (3, 3, "Neutral."),
             (3, 4, "The two baselines are clearly separated."),
             (3, 3, "Neutral."),
             (2, 4, "A false 9 weeks didn't trigger a recovery takeover."),
             (2, 5, "Written answer and a new governance rule."),
             (3, 3, "Two days."),
             (3, 3, "Pre-wiring every steering.")],
    pitfalls=[("Fighting in the room", "You look defensive; the slide wins.", "thank, ask, 48 hours."),
              ("Silence", "The slide becomes true.", "ask for the data and a deferral."),
              ("Attacking the ambusher", "You become the story.", "evidence only, no adjectives."),
              ("A verbal answer", "Forgotten by Monday.", "two pages, in writing."),
              ("Not changing the rules", "It happens again.", "papers shared before, both ways.")],
    grimoire=[(1, "meeting-before-the-meeting", "The Meeting Before the Meeting", "is the cure: from 28 June, Ines meets Oliver before every steering."), (3, "seagull-overlord", "The Seagull Overlord", "is Lord Varnish's appearance: flies in, squawks, flies out.")],
    use=["Someone surprises you with a damaging claim in a meeting.", "A rival has influence over the client.", "Governance lets unseen papers be decided on."],
    skip=["The claim is right and you knew it: then say so in the room, and bring the plan."],
    related=["<b>What Do We Do When Our Rival Advises the Client?</b> (previous note)", "<b>How Do We Tell Them It's Worse Than They Think?</b> (vol. 3)", "<b>How Do We Re-plan Without Lying?</b> (this volume)", "<b>Who Decides What, and Where?</b> (vol. 2)"],
    quiz=[("What four things did Ines say in the room?", "Thanks, a question about the data, a written answer by Friday, and a request to defer decisions."),
          ("Where did the “nine weeks” come from?", "Comparing progress with baseline v1.0, from before CR-007."),
          ("What was the real slip against baseline v2.0?", "Two weeks: the pilot's acceptance, rejected for 0.8 % exceptions."),
          ("What rule did Priya add?", "Steering papers from anyone circulate two working days before; others can be noted but not decided."),
          ("Why not prove the slide wrong in the room?", "You'd look defensive and turn the meeting into a fight the chair has to referee.")],
    quiz_sit=[("At the next steering, Oliver brings a new unseen slide. What do you say?", "Calmly point to Schedule 7 §2.7: the slide can be noted, and Wrenfield will respond in writing; no decision today. Then meet Oliver beforehand next time, as agreed.")],
    try_it="Write the four sentences you'd say if a surprise slide attacked your project tomorrow. Then write the governance rule that would stop it happening again.",
    remember="Don't win the room; <span class=\"hl\">win Friday</span>. Thank, ask for the data, answer <span class=\"hl\">in writing</span>, and change the rules.",
    late=dict(when="Wed 28 June 2028 · 23:10 · hotel near The Grid",
              lines=["Nine weeks, on a slide I'd never seen, in front of Lord Varnish. I said four sentences. My hands were shaking under the table.",
                     "Bea sent the sheet by 16:20. Baseline v1.0. It's an honest mistake, or it isn't. Doesn't matter: the answer's the same.",
                     "Friday's two pages are written. Two weeks, not nine. Now I'm going to sleep, or at least lie down."]),
    sources=["Douglas Stone, Bruce Patton and Sheila Heen, <i>Difficult Conversations</i> (1999).",
             "Patrick Lencioni, <i>Death by Meeting</i> (2004).",
             "UK Office of Government Commerce, <i>Managing Successful Programmes</i>: programme boards."],
)

# ------------------------------------------------------------------ 07 When Do We Go Over Their Heads?
es_problem = Doodle(760, 240, "Doodle of the performance test environment, a condition of the design authority. Promised by MetroVolt IT for 15 May 2028. On 10 July it still isn't ready. Hollis's team keeps saying next week. The performance test must happen by the end of July, or wave 1 can't go.",
                    "Promised 15 May. On 10 July: “next week”. Again.", exact=True)
es_problem.icon("calendar", 40, 40, 1.6)
for i, t in enumerate(["15 May: promised", "29 May: next week", "12 Jun: next week", "26 Jun: next week", "10 Jul: next week"]):
    es_problem.box(160 + (i % 3) * 196, 30 + (i // 3) * 70, 184, 54, t, "pink" if i else "y", size=16)
es_problem.note(380, 216, "performance test must pass by end of July", "red", size=19)

es_how = Doodle(760, 330, "Lodestar's escalation ladder, agreed in the governance schedule. Rung one: the working group, five days. Rung two: Elaine and Callum, five days. Rung three: Priya, with Graham as Wrenfield's executive, a call between the two. Before each rung: tell the person you're escalating past, and bring a proposal, not a complaint. Here: tell Hollis first; proposal: use the pilot's production-grade servers on two weekends. Fixed in nine days. Then come back down.",
                "Climb a ladder agreed in advance, tell the person first, bring a proposal, and climb back down.", exact=True)
for i, (h, sub, fill) in enumerate([("working group", "5 days", "paper"), ("Elaine + Callum", "5 days", "y"), ("Priya + Graham", "exec call", "pink")]):
    es_how.box(14 + i * 250, 180 - i * 70, 232, 70, h, fill, sub=sub, size=19, subsize=15)
es_how.box(14, 270, 360, 50, "tell Hollis first", "green", size=17)
es_how.box(386, 270, 360, 50, "proposal: pilot servers, 2 weekends", "blue", size=16)

ESCALATION = dict(
    slug="escalation", date=date(2028, 7, 10), meta=on_site(date(2028, 7, 10)), where="FL 19", pass_kind="contractor",
    kicker="a.k.a. escalation without burning the relationship",
    tldr="Escalating is legitimate; how you do it decides whether you have a relationship afterwards. Use a <b>ladder agreed in advance</b>, with time limits at each rung. <b>Tell the person first</b> that you're going to escalate, and why. Bring a <b>proposal</b>, not a complaint. Escalate the <b>problem</b>, never the person. And once it's solved, <b>climb back down</b> and work with them as before.",
    chips=[("Family", "other people's moves"), ("Lives in", "Schedule 7, §4 (escalation ladder)"), ("Pairs with", "governance (vol. 2), test environments")],
    problem_side="The Grid, July 2028",
    problem="""  <p class="lead">One of the design authority's four conditions was a <b>performance test by July</b>. It needs a production-sized test environment from MetroVolt IT, promised for <b>15 May</b>.</p>
  <ul>
    <li>On 29 May, 12 June and 26 June, Hollis's team says “next week”. On <b>10 July</b>, the same.</li>
    <li>Without the test, the go / no-go criteria for wave 1 can't be met. The go / no-go is <b>6 September</b>.</li>
    <li>Hollis's team is short of people since Horizon. <span class="hl-pink">Escalating over Hollis feels like betraying the man who overruled Hana gracefully and then asked her to teach his team.</span></li>
  </ul>""",
    problem_figs=[es_problem],
    sides=dict(client=("Hollis", "<p>Hollis's infrastructure team lost three people in Horizon. He has four programmes asking for environments and no authority to buy more. Saying “next week” is easier than saying “I can't”. He'd rather not be escalated over, and he'd rather the problem were solved.</p>", "I'm drowning. Please don't make it look like it's my fault."),
                vendor=("Ines", "<p>Ines needs the environment by the end of July. She's waited eight weeks, kindly. The contract has an escalation ladder for exactly this. The question is how to use it without losing Hollis, who she'll need every week until 2030.</p>", "Escalate the environment, not Hollis.")),
    sides_after="Most escalations are really requests for resources someone below doesn't have the authority to give. Escalating them helps the person you escalate past, if you do it right.",
    analogy_side="the referee and the captain",
    analogy="""  <p>A team captain who disagrees with a decision doesn't shout at the referee or run to the league. She <b>tells the referee</b> she'll raise it, follows the <b>agreed procedure</b> with a clear request, and the next week shakes the referee's hand before kick-off. The procedure exists so that disagreements don't become feuds.</p>""",
    map=[("Telling the referee first", "Telling Hollis before going to Priya"),
         ("The agreed procedure", "The escalation ladder in Schedule 7"),
         ("A clear request", "A proposal: pilot servers on two weekends"),
         ("The league", "Priya and Graham's executive call"),
         ("Shaking hands next week", "Climbing back down; Monday's working group as usual")],
    how_side="a ladder, tell them first, a proposal, then back down",
    how="""  <p>The <b>escalation ladder</b> is in Schedule 7: <b>working group</b> (five days), then <b>Elaine and Callum</b> (five days), then <b>Priya</b>, with Graham as Wrenfield's executive counterpart. The issue had sat on rung one for eight weeks because nobody wanted to climb.</p>
  <p><b>Tell the person first.</b> On 10 July Ines goes to Hollis's desk: “I'm going to take the performance environment to Elaine this week, not because of you, but because it needs a decision your team can't make alone. Here's what I'll propose. Is there anything you'd change?” Hollis, relieved, suggests the proposal himself.</p>
  <p><b>Bring a proposal.</b> To Elaine: use the <b>pilot's production-grade servers</b> on two weekends (they're idle then), with MetroVolt IT's on-call cover, paid from the change pool. Elaine takes it to Priya the same day; Priya agrees in one email. The test runs on <b>22 and 29 July</b> and passes with 18 % headroom.</p>
  <p><b>Climb back down.</b> On Monday, the working group runs as usual. Ines thanks Hollis's team publicly in the status report. Hollis says the escalation got him two extra contractors for the autumn.</p>""",
    how_figs=[es_how],
    steps=[("Agree the ladder in advance", "Rungs, time limits, names."),
           ("Don't wait too long on a rung", "The time limit is the trigger."),
           ("Tell the person first", "Why, and what you'll propose."),
           ("Escalate the problem, not the person", "Resources, decisions, conflicts."),
           ("Bring a proposal", "Something the senior person can say yes to."),
           ("Climb back down", "Same meetings, same respect, credit given.")],
    vocab=[("Escalation", "Taking an issue to someone with more authority."),
           ("Escalation ladder", "Agreed levels and time limits for escalating."),
           ("Executive sponsor pairing", "Senior people from client and supplier who resolve what others can't."),
           ("Proposal", "A specific solution the decider can approve."),
           ("De-escalation", "Returning to normal working once the issue is solved."),
           ("Resource conflict", "Several demands on the same scarce people or kit.")],
    code=dict(file="governance/escalations/E-006.md", note="raised Mon 10 Jul 2028 · closed Mon 31 Jul", src="""
ESCALATION E-006 · performance test environment (DA condition 3)

promised      15 May 2028 (MetroVolt IT) · status 10 Jul: "next week" (5th time)
impact        perf test by end of July → go / no-go criterion C9 (6 Sep)
rung 1        working group: 29 May → 10 Jul (8 weeks; time limit was 5 days)
told first    Hollis, 10 Jul 09:30: "needs a decision your team can't make alone"
proposal      pilot's production-grade servers, weekends 22 + 29 Jul,
              MetroVolt IT on-call cover, £6,400 from the change pool
rung 2        Elaine, 10 Jul 14:00 → Priya, 10 Jul 16:00 → approved by email 17:12
outcome       perf test passed 29 Jul (18 % headroom at 1.5× peak)
de-escalation thanks to MetroVolt IT in status #53 · Hollis: 2 contractors for autumn
"""),
    contract=dict(side="the ladder in the contract", doc="Lodestar SOW · Schedule 7, §4 (escalation)", date="v1.1 · Aug 2027", stamp="rung 2",
                  clauses=[("4.1", "Issues not resolved by a working group within 5 Working Days are referred to the Programme Director and the Supplier's Engagement Manager, and then within a further 5 Working Days to the Sponsor and the Supplier's Executive.", "we waited eight weeks on a five-day rung. that was our mistake, not Hollis's."),
                           ("4.3", "Escalation is a normal part of governance and does not imply fault.", "we put this sentence in. it helps every time.")],
                  plain="a contractual escalation ladder, with the sentence that escalation implies no fault, lets you climb without it feeling like an accusation. Use the time limits; waiting too long is unkind to everyone."),
    health=dict(now="g",
                g=("trust is high", ["Escalate early and lightly.", "Tell them first, always.", "Senior pair solves it in a call."]),
                a=("an overloaded counterpart", ["Escalate the resource gap.", "Let them shape the proposal.", "Thank them publicly after."]),
                r=("escalation as warfare", ["Ladder, in writing, by the clock.", "Never personal.", "Document each rung."])),
    pressure=dict(level=3, title="going over a friend's head", cost="eight weeks of patience · one uncomfortable conversation",
                  items=["Waiting too long felt kind. It wasn't: it left Hollis without the help he needed and put wave 1 at risk.", "Telling Hollis first took two minutes and saved the relationship."]),
    baseline="Each line compares <b>waiting politely, or going straight to the top</b> with <b>the agreed ladder, telling the person first, a proposal and climbing back down</b>.",
    ratings=[(3, 4, "Priya sees a problem solved, not a fight."),
             (3, 4, "The team gets its environment."),
             (3, 3, "£6,400 from the pool."),
             (3, 3, "Neutral."),
             (3, 4, "Performance tested properly before wave 1."),
             (2, 5, "Go / no-go criterion C9 can be met."),
             (3, 4, "E-006 recorded with each rung."),
             (2, 4, "Solved in a day once escalated."),
             (4, 4, "Light.")],
    pitfalls=[("Waiting too long", "A five-day rung becomes eight weeks.", "use the time limits."),
              ("Going straight to the top", "The person below is humiliated.", "climb rung by rung."),
              ("Not telling them first", "They hear it from their boss.", "two minutes at their desk."),
              ("Escalating a complaint", "The senior person has nothing to approve.", "bring a proposal."),
              ("Staying escalated", "Every issue goes up from now on.", "climb back down.")],
    grimoire=[(3, "skip-level-seance", "The Skip-Level Séance", "is the inside version: when and how to go over your own manager's head, and the price.")],
    use=["An issue has sat past its time limit.", "It needs a decision or resources the person can't give.", "Delay threatens a milestone."],
    skip=["The person can still solve it within the time limit: help them instead."],
    related=["<b>Who Decides What, and Where?</b> (vol. 2)", "<b>Why Do the Test Environments Never Work?</b> (this volume)", "<b>What Happens When Steering Turns on Us?</b> (previous note)", "<b>Who Decides What?</b> (Sanne, vol. 2)"],
    quiz=[("What are the rungs of Lodestar's ladder?", "Working group (5 days), Elaine and Callum (5 days), Priya with Graham."),
          ("What should you do before climbing a rung?", "Tell the person you're escalating past, and why."),
          ("What made the escalation quick?", "A proposal Priya could say yes to: the pilot's servers on two weekends."),
          ("Why does clause 4.3 help?", "It says escalation doesn't imply fault, so it's not an accusation."),
          ("What was Wrenfield's own mistake?", "Waiting eight weeks on a five-day rung.")],
    quiz_sit=[("Graham wants to phone Rupert directly about the environment. What do you advise?", "No: the ladder goes to Priya with Graham as her counterpart. Going to Rupert skips Priya and Elaine, and turns a resource problem into a political one.")],
    try_it="Find an issue on your project that has waited too long. Who is it stuck with? Write two sentences you'd say to them before escalating, and a proposal the next person up could approve.",
    remember="Escalate <span class=\"hl\">the problem, not the person</span>. Tell them first, bring a proposal, and <span class=\"hl\">climb back down</span>.",
    late=dict(when="Mon 10 July 2028 · 21:00 · hotel near The Grid",
              lines=["Eight weeks of “next week”. My fault for being polite for seven of them.",
                     "Told Hollis first. He looked relieved and wrote half the proposal himself.",
                     "Priya approved it at 17:12. The test runs in two weekends. Thank-you note to Hollis's team in Friday's status."]),
    sources=["Roger Fisher and William Ury, <i>Getting to Yes</i> (1981).",
             "UK Government, <i>Model Services Contract</i>: dispute resolution procedure.",
             "Kim Scott, <i>Radical Candor</i> (2017)."],
)

NOTES = [VENDOR_BLAME, RIVAL_ADVISER, AMBUSH, ESCALATION]
