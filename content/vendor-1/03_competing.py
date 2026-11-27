# Series 5 · On the Client's Floor · Vol. 1 · Winning the Work · Up against the others (notes 9–12).
from datetime import date

# ------------------------------------------------------------------ 09 What About the Vendor Already Here?
ti_problem = Doodle(760, 250, "Doodle of the landscape around MAVIS. Halvorsen billing has been there since 2016, with 34 custom integrations and the only people who understand the tariff engine. Every night at 02:10 MAVIS sends Halvorsen a file. Halvorsen is bidding for all of Lodestar too. Whoever wins Lodestar needs Halvorsen's interface.",
                    "Halvorsen is a rival for Lodestar and a dependency for whoever wins it.", exact=True)
ti_problem.box(24, 60, 200, 110, "MAVIS", "paper", sub="1997", size=24, subsize=17)
ti_problem.arrow(228, 115, 470, 115, label="02:10 file, every night", lx=349, ly=100)
ti_problem.box(474, 40, 262, 150, "Halvorsen", "y", sub="billing since 2016", size=24, subsize=17)
ti_problem.note(605, 172, "34 custom integrations", "pen", size=17)
ti_problem.note(380, 226, "rival in the bid, dependency in the build", "red", size=21)

ti_how = Doodle(760, 300, "What the incumbent needs and what the newcomer needs, drawn as two overlapping circles. Halvorsen needs its billing contract renewed in 2029, a clean interface, and not to be blamed. Wrenfield needs the interface specification by 30 July, support during testing, and a named contact. In the overlap: a written interface letter, dated 9 March 2027: Halvorsen will support whichever supplier wins, at its standard rates.",
                "Find the overlap between what they protect and what you need, and put it in a letter.", exact=True)
ti_how.circle(235, 150, 150, "y")
ti_how.circle(525, 150, 150, "blue")
ti_how.head(195, 60, "Halvorsen needs", size=18)
for i, t in enumerate(["the 2029 renewal", "not to be blamed", "its own rates"]):
    ti_how.text(195, 100 + i * 34, t, size=17)
ti_how.head(565, 60, "Wrenfield needs", size=18)
for i, t in enumerate(["spec by 30 July", "test support", "a named contact"]):
    ti_how.text(565, 100 + i * 34, t, size=17)
ti_how.box(300, 200, 160, 70, "the letter", "green", sub="9 Mar 2027", size=19, subsize=16)

INCUMBENT = dict(
    slug="the-incumbent", date=date(2027, 3, 2), meta="bid day 28 of 50", where="CAFÉ",
    kicker="a.k.a. “working with (and against) the incumbent supplier”",
    tldr="The incumbent knows the client's systems, people and history better than you ever will in six weeks, and you'll probably <b>need them</b> whoever wins. Don't treat them as the enemy. Find out <b>what they protect</b> (a renewal, a reputation, their rates) and <b>what you need from them</b> (an interface, test support, a contact), meet them early and in the open, and put the overlap <b>in writing</b>. You can compete for one contract and cooperate on the next one.",
    chips=[("Family", "up against the others"), ("Lives in", "bid/lodestar/halvorsen-letter.pdf"), ("Pairs with", "dependencies, the multi-vendor RACI")],
    problem_side="a café opposite The Grid, 2 March 2027",
    problem="""  <p class="lead">Halvorsen Systems has run MetroVolt's billing since <b>2016</b>. It has <b>34 custom integrations</b>, the only people who understand MetroVolt's tariff engine, and a file from MAVIS every night at <b>02:10</b>. Halvorsen is also bidding for <b>all of Lodestar</b>.</p>
  <ul>
    <li>Wrenfield's design keeps Halvorsen billing. So <b>dependency D-03</b>, the billing interface spec, belongs to a rival.</li>
    <li>Vivian's view: “They'll stall us. Let's not mention them.” <span class="hl-pink">Hollis will score the integration section; he'll notice.</span></li>
    <li>On <b>Tuesday 2 March</b> Ines emails Sven Aldous, Halvorsen's account director, and asks him for coffee. He brings biscuits.</li>
  </ul>""",
    problem_figs=[ti_problem],
    sides=dict(client=("Hollis watches", "<p>MetroVolt has two big suppliers that will have to share a file at 02:10 for years. Hollis wants to see that <b>the new one won't start a war with the old one</b>. A bid that pretends Halvorsen doesn't exist is a bid that will blame Halvorsen later.</p>", "Whoever wins, they'll have to work with Sven."),
                vendor=("Ines meets Sven", "<p>For Wrenfield, Halvorsen is a <b>rival</b> (it wants Lodestar too) and a <b>dependency</b> (Wrenfield's plan needs its interface). Ines needs Sven's cooperation in writing before she can price D-03, without giving away Wrenfield's design.</p>", "Compete for this one. Cooperate on the next ten years.")),
    sides_after="Incumbents are rarely villains. They're protecting a business they built honestly, often over years nobody else remembers.",
    analogy_side="the new builder and the old electrician",
    analogy="""  <p>A new builder is hired for an extension, and the house's electrician has done the wiring for twelve years. The electrician also quoted for the extension and lost. The builder still needs him: he knows where every cable runs. The smart builder buys him a coffee, asks what he needs, and agrees <b>in writing</b> who connects what, at what rate.</p>""",
    map=[("The old electrician", "Halvorsen Systems (billing since 2016)"),
         ("He knows where every cable runs", "34 integrations, the tariff engine, the 02:10 file"),
         ("He quoted for the extension too", "Halvorsen bids for all of Lodestar"),
         ("Who connects what, at what rate", "The interface letter of 9 March 2027"),
         ("The next twelve years", "Billing renewal in 2029, and every wave after this one")],
    how_side="what they protect, what you need, and a letter",
    how="""  <p>Before the coffee, Ines writes two lists. <b>What Halvorsen protects</b>: its billing contract (up for renewal in 2029), its reputation if the new system breaks billing, and its rates for interface work. <b>What Wrenfield needs</b>: the interface specification by 30 July 2027, support in integration testing, a named technical contact.</p>
  <p>At the café she says plainly: “You're bidding, we're bidding, one of us will lose. Whoever wins needs the billing interface working. If we win, we'll need your help, and we'll pay your standard rates for it. If you win, nothing changes for you.” She shares nothing about Wrenfield's design.</p>
  <p>Sven asks for one thing: that the winner won't blame Halvorsen for MAVIS's data. Ines agrees that interface defects will be triaged jointly, by evidence. Halvorsen's <b>letter of 9 March</b> says it will support whichever supplier wins, at standard rates, with a named contact. The bid quotes it in the integration section. Hollis scores that section 4 out of 5.</p>""",
    how_figs=[ti_how],
    steps=[("Map what the incumbent owns", "Systems, integrations, knowledge, contracts and renewal dates."),
           ("Write what they protect", "Renewal, reputation, rates. Usually reasonable."),
           ("Write what you need", "Specific: documents, dates, people, support."),
           ("Meet early, openly, and say it's a contest", "Don't pretend; don't fish for their bid."),
           ("Offer something real", "Paid work at their rates, fair blame rules."),
           ("Get the overlap in writing", "A short letter you can quote in the bid.")],
    vocab=[("Incumbent", "The supplier already serving the client in this or a related area."),
           ("Co-opetition", "Competing and cooperating with the same firm at the same time."),
           ("Interface agreement", "A written deal on how two systems, and two suppliers, connect."),
           ("Lock-in", "Being hard to replace because of knowledge, data or integrations only you hold."),
           ("Letter of support", "A short written commitment from a third party, quoted in a bid."),
           ("Joint triage", "Investigating a cross-supplier defect together, by evidence, before assigning blame.")],
    code=dict(file="bid/lodestar/incumbent-halvorsen.md", note="before and after coffee · Tue 2 Mar 2027", src="""
INCUMBENT · Halvorsen Systems (billing, since 2016)      contact: Sven Aldous

they hold        34 custom integrations · tariff engine · the 02:10 file intake
they protect     billing renewal (2029) · reputation if billing breaks · rates
we need          D-03 interface spec by 30 Jul 27 · integration test support
                 · a named technical contact · 2 days/week during testing
we offer         paid work at their standard rates · joint, evidence-based triage
                 of interface defects · advance notice of every file change
we don't share   our design, our price, our team

outcome          letter, 9 Mar 2027: "Halvorsen will support the successful
                 supplier with integration to billing at its standard rates, with
                 a named technical contact." → quoted in bid section 3.6
"""),
    contract=dict(side="what the letter makes possible later", doc="Lodestar SOW · Appendix C (draft)", date="from the bid", stamp="third party",
                  clauses=[("D-03", "The billing supplier provides the interface specification for customer and meter data by 30 July 2027 and technical support during integration testing, as set out in its letter of 9 March 2027.", "a dependency on a third party is only real if someone promised it in writing."),
                           ("3.6", "Where a Dependency is to be provided by a third-party supplier of MetroVolt, MetroVolt shall use reasonable endeavours to procure its provision.", "MetroVolt manages Halvorsen. we don't.")],
                  plain="you have no contract with the incumbent; the client does. So the dependency should say what the incumbent promised, and the client should be responsible for getting it delivered."),
    health=dict(now="a",
                g=("the incumbent is friendly", ["A short meeting and a letter.", "Plan joint work from day one.", "Keep them informed of changes."]),
                a=("they're also bidding", ["Meet openly; say it's a contest.", "Offer paid work and fair blame rules.", "Share nothing about your bid."]),
                r=("they refuse to talk", ["Ask the client to require their support.", "Price the risk of a slow interface.", "Never badmouth them in the bid."])),
    pressure=dict(level=2, title="the coffee", cost="an awkward hour · one nervous account director",
                  items=["Meeting a rival feels like betrayal to your own sales team. Explain that the bid needs D-03 to be real.", "Sven isn't an enemy. Sven is the person you'll be on the phone with at 02:30 in September 2028."]),
    baseline="Each line compares <b>ignoring the incumbent in the bid</b> with <b>meeting them openly and quoting a letter of support</b>.",
    ratings=[(2, 4, "Hollis sees a bidder who'll work with Halvorsen."),
             (3, 4, "D-03 has a name and a date."),
             (2, 4, "Interface work priced at known rates."),
             (2, 4, "Who does what at the billing boundary is clearer."),
             (3, 4, "The design can rely on a real interface."),
             (2, 4, "The biggest third-party dependency is tested early."),
             (2, 4, "The letter is quotable and dated."),
             (4, 3, "A week to arrange and get the letter."),
             (4, 4, "A letter.")],
    pitfalls=[("Pretending they don't exist", "The bid ignores the system everyone knows you'll depend on.", "name them, and show the plan."),
              ("Fishing for their bid", "Using the coffee to learn their price.", "say it's a contest and keep to the interface."),
              ("Badmouthing them", "The client chose them, and still pays them.", "talk about the interface, not their faults."),
              ("A verbal promise", "“Sure, we'll help” evaporates after you win.", "a dated letter."),
              ("Making them your dependency, not the client's", "You have no contract with them.", "the client procures their support.")],
    grimoire=[(6, "incumbent-dragon", "The Incumbent Dragon", "is Halvorsen in 2029, from MetroVolt's side: comfortable, not evil."), (6, "frenemy-pact", "The Frenemy Pact", "is what Ines and Sven just made.")],
    use=["An incumbent holds a system you must integrate with.", "The incumbent is bidding against you.", "The client will have to live with both of you."],
    skip=["There's no incumbent, or no shared boundary."],
    related=["<b>How Do We Compete with a Big Consultancy?</b> (next note)", "<b>Who Does What When Three Firms Share a Project?</b> (vol. 2)", "<b>What Are We Assuming?</b> (this volume)", "<b>The Vendor Went Quiet</b> (Eli, vol. 4)"],
    quiz=[("Why is the incumbent both a rival and a dependency?", "It bids for the same work, and the winner needs its systems and interfaces."),
          ("What did Halvorsen protect?", "Its 2029 billing renewal, its reputation if billing broke, and its rates."),
          ("What did Ines offer Sven?", "Paid work at standard rates and joint, evidence-based triage of interface defects."),
          ("Why should the dependency be MetroVolt's to procure?", "Wrenfield has no contract with Halvorsen; only MetroVolt can make Halvorsen deliver."),
          ("What should you never do at a meeting with a rival bidder?", "Fish for their price or share your own design or price.")],
    quiz_sit=[("After the coffee, Vivian suggests asking Sven what Halvorsen is bidding. What do you say?", "No. It risks the procurement and the trust you just built. The meeting was about the interface, and that's all it should be.")],
    try_it="Pick a supplier or team you depend on but don't control. Write what they protect and what you need. Where do the two overlap? What would you ask them to put in writing?",
    remember="The incumbent knows where the cables run. Compete for <span class=\"hl\">this contract</span>, cooperate on <span class=\"hl\">the next ten years</span>, and get it <span class=\"hl\">in writing</span>.",
    late=dict(when="Tue 2 March 2027 · 22:15 · Leeds",
              lines=["Coffee with Sven. He brought biscuits. He's been at MetroVolt longer than anyone on the panel.",
                     "He asked for one thing: don't blame Halvorsen for MAVIS's data. Fair. I'd ask the same.",
                     "Vivian asked if I found out their price. No, Vivian."]),
    sources=["Adam Brandenburger and Barry Nalebuff, <i>Co-opetition</i> (1996).",
             "UK Cabinet Office, <i>The Sourcing Playbook</i> (2020): multi-supplier service integration.",
             "Gregor Hohpe and Bobby Woolf, <i>Enterprise Integration Patterns</i> (2003)."],
)

# ------------------------------------------------------------------ 10 How Do We Compete with a Big Consultancy?
bc_problem = Doodle(760, 240, "Doodle of two bidders side by side. Vexmoor: about 40,000 people, a famous brand, three years at MetroVolt, Orion's hub, and day rates on slide 4 that look cheaper. Wrenfield: 80 people in Leeds, no history with MetroVolt, and the people who will actually do the work.",
                    "40,000 people and three years at MetroVolt, against 80 people in Leeds.", exact=True)
bc_problem.box(24, 20, 330, 170, None, "pink", rx=6)
bc_problem.head(189, 52, "Vexmoor", size=24)
for i, t in enumerate(["≈ 40,000 people", "3 years at MetroVolt", "built Orion's hub", "cheaper on slide 4"]):
    bc_problem.text(189, 86 + i * 26, t, size=17)
bc_problem.box(406, 20, 330, 170, None, "blue", rx=6)
bc_problem.head(571, 52, "Wrenfield", size=24)
for i, t in enumerate(["80 people", "never met MetroVolt", "a legacy move in 2025", "the people at the orals"]):
    bc_problem.text(571, 86 + i * 26, t, size=17)
bc_problem.note(380, 226, "don't fight on their ground", "red", size=21)

bc_how = Doodle(760, 300, "A competitor map for Vexmoor. Their strengths: brand, scale, relationships with the board, knowledge of Orion. Their weaknesses: Orion's failure, senior people sell while junior people deliver, offshore delivery. Wrenfield's answer to each: named senior team who will do the work, an honest plan with ranges, specific legacy experience, and never a word against Orion.",
                "Answer their strengths with specifics, and let the panel notice the weaknesses on its own.", exact=True)
bc_how.box(14, 14, 360, 40, "their strengths", "pink", size=19)
bc_how.box(386, 14, 360, 40, "our answer", "green", size=19)
rows = [("brand and scale", "named people, CVs, faces"), ("board relationships", "an honest plan Hollis can check"),
        ("they know Orion", "we'll learn MAVIS in discovery"), ("cheaper day rates", "fewer, more senior days")]
for i, (a, b) in enumerate(rows):
    y = 64 + i * 48
    bc_how.box(14, y, 360, 40, a, "paper", size=17)
    bc_how.box(386, y, 360, 40, b, "paper", size=17)
bc_how.note(380, 280, "never a word against Orion: the panel built it", "red", size=19)

BIG_CONSULTANCY = dict(
    slug="big-consultancy", date=date(2027, 3, 16), meta="bid day 42 of 50", where="LEEDS",
    kicker="a.k.a. “competitive positioning” and “ghosting”, done honestly",
    tldr="You won't beat a big consultancy on <b>size, brand or relationships</b>, so don't try. Write down their real strengths and your <b>specific answer</b> to each: named senior people who will do the work, specific experience, a plan the client can check. Describe the <b>risks of approaches</b>, not the failures of firms. Never attack their past work: the panel was part of it.",
    chips=[("Family", "up against the others"), ("Lives in", "bid/lodestar/competitors.md (never sent)"), ("Pairs with", "the orals, references")],
    problem_side="Wrenfield, 16 March 2027",
    problem="""  <p class="lead">From the clarification log, Wrenfield knows <b>Vexmoor Consulting</b> is bidding, plans to reuse Orion's data hub, and may deliver partly offshore. Vexmoor has about <b>40,000 people</b>, has worked at MetroVolt for three years, and its partner, Oliver Thane, knows the board.</p>
  <ul>
    <li>Vivian's draft of the “why us” section begins: <i>“Unlike previous suppliers, who failed to deliver…”</i></li>
    <li>Elaine ran Orion. Hollis approved its architecture. Priya sponsored its last year. <span class="hl-pink">The sentence insults three of the six people scoring the bid.</span></li>
    <li>Graham asks the real question: “Why would anyone pick 80 people over 40,000?”</li>
  </ul>""",
    problem_figs=[bc_problem],
    sides=dict(client=("Priya weighs it", "<p>Choosing a famous firm is <b>safe for the chooser</b>: if it fails, nobody blames the person who picked the big name. Choosing a small one is a personal risk. Priya needs reasons she can repeat to the board that sound like evidence, not like a gamble.</p>", "If I pick the small firm and it fails, it's my name."),
                vendor=("Ines and Callum", "<p>Wrenfield can't match Vexmoor's brand. It can match the work: <b>senior people who do it themselves</b>, a smaller and more honest plan, and recent experience moving a legacy customer system. It has to say that without ever saying “Orion failed”.</p>", "Make choosing us feel like the careful option.")),
    sides_after="The panel already knows what went wrong with Orion. It doesn't need the bidder to tell it; it needs a bidder who seems to have learned.",
    analogy_side="the local restaurant next to the chain",
    analogy="""  <p>A small restaurant opens across from a famous chain. It doesn't put up a sign saying “the chain's food is bad”: half its customers ate there last week. It puts the <b>chef's name on the menu</b>, says where the fish came from this morning, and lets people taste. The chain's size isn't the weakness. Its sameness is.</p>""",
    map=[("The famous chain", "Vexmoor: brand, scale, relationships"),
         ("“Their food is bad” sign", "Attacking Orion in the bid"),
         ("The chef's name on the menu", "Named people, who'll present and deliver"),
         ("Where the fish came from", "Specific experience: a legacy customer system moved in 2025"),
         ("Letting people taste", "Showing work on MetroVolt's own data at the orals")],
    how_side="their strengths, your specific answers, and no attacks",
    how="""  <p>Callum and Ines write a competitor sheet that <b>never leaves Wrenfield</b>. Vexmoor's strengths: brand, scale, board relationships, knowledge of Orion. Weaknesses the panel will see without help: Orion's history, a model where partners sell and juniors deliver, offshore delivery.</p>
  <p>Each strength gets a <b>specific answer</b> in the bid. Brand → <b>named people</b> with CVs, who present at the orals and are named as key personnel in the contract. Relationships → <b>an honest plan</b> with P50 and P80 that Hollis can check line by line. Orion knowledge → a <b>paid discovery</b> that learns MAVIS properly. Cheaper rates → <b>fewer, more senior days</b>.</p>
  <p>Where a risk applies to Vexmoor's likely approach, the bid describes the <b>approach</b>, not the firm: <i>“Reusing partly built components is often the fastest route, provided their data model is checked against current data first. Our discovery includes that check for any component MetroVolt wishes to keep.”</i> That's fair, useful to MetroVolt, and true of anyone. Vivian's sentence is deleted.</p>""",
    how_figs=[bc_how],
    steps=[("Write their strengths honestly", "If you can't name them, you'll lose to them."),
           ("Answer each with something specific", "A name, a number, a document, a date."),
           ("Choose ground you can win on", "Seniority, focus, honesty, a specific experience."),
           ("Describe risks of approaches, not firms", "True of anyone; useful to the client."),
           ("Make choosing you feel careful", "Evidence the sponsor can repeat to the board."),
           ("Keep the sheet in-house", "It's for your thinking, not for the client.")],
    vocab=[("Win theme", "The main reason to choose you, repeated through the bid."),
           ("Discriminator", "Something you offer that rivals can't easily claim."),
           ("Ghosting", "Raising the risks of a rival's likely approach without naming them; fair only if true of anyone."),
           ("Pyramid staffing", "A few senior people sell, many junior people deliver."),
           ("Key personnel", "People named in the contract who can't be swapped without consent."),
           ("Safe choice bias", "Preferring the famous option because failure is easier to defend.")],
    code=dict(file="bid/lodestar/competitors.md", note="in-house only · Tue 16 Mar 2027", src="""
COMPETITOR SHEET · VEXMOOR CONSULTING          (never sent, never quoted)

their strengths              our specific answer                     where in the bid
brand, ≈ 40,000 people       named team, CVs, same people at orals   §5 team · key personnel
board relationships          a plan with P50/P80 Hollis can check     §4 delivery
know Orion's hub             paid discovery checks any component      §3.4 · §6 commercial
cheaper day rates            fewer, senior days; rate card            §6

weaknesses the panel sees on its own: Orion's history · partners sell,
juniors deliver · offshore (from their clarification question)
→ we say nothing about any of them

banned words in our bid: "unlike previous suppliers" · "Orion" · "failed"
"transformational" · "world-class"
"""),
    contract=dict(side="how “named people” becomes a promise", doc="Lodestar SOW · §6 key personnel (draft)", date="from the bid", stamp="named",
                  clauses=[("6.1", "The Supplier shall provide the Key Personnel named in Schedule 6 (including the Lead Architect and the Technical Lead) for the duration of Wave 1.", "Ines and Hana. by name."),
                           ("6.3", "The Supplier shall not remove or replace Key Personnel without MetroVolt's prior written consent, not to be unreasonably withheld.", "our discriminator is now our obligation. good.")],
                  plain="if your advantage is the people, offer to name them in the contract. It turns a sales claim into a promise the client can enforce, which is exactly why it's believed."),
    health=dict(now="a",
                g=("they've worked with you before", ["Your track record there is the answer.", "Still no attacks.", "Remind them what was different."]),
                a=("you're the unknown", ["Specific answers to each rival strength.", "Named people in the contract.", "Make the careful choice look like you."]),
                r=("the panel is loyal to the big firm", ["Ask whether you're making up the numbers.", "Compete on a smaller, safer first step.", "Lose gracefully; they'll remember."])),
    pressure=dict(level=3, title="David and Goliath", cost="one deleted paragraph · one bruised account director",
                  items=["The temptation is to point at Orion. Every person who could choose you worked on it.", "Small-firm fear is real: you're asking someone to take a personal risk. Give them evidence to hold."]),
    baseline="Each line compares <b>a “why us” that attacks the last supplier</b> with <b>specific answers to the rival's strengths, and no attacks</b>.",
    ratings=[(2, 4, "Nobody on the panel is insulted."),
             (3, 3, "Neutral."),
             (3, 3, "Neutral now; key personnel limit later flexibility."),
             (3, 3, "Neutral."),
             (3, 4, "A paid check of reused parts, offered to anyone."),
             (2, 3, "The rival's approach risks are described, fairly."),
             (2, 4, "Claims are specific and checkable."),
             (4, 4, "A page of thinking."),
             (4, 4, "Nothing to keep up.")],
    pitfalls=[("Attacking the last supplier", "The panel worked on it.", "talk about approaches and what you'll do."),
              ("Competing on size", "You'll never be bigger.", "compete on seniority, focus and specifics."),
              ("Generic claims", "“Agile, experienced, passionate” is in every bid.", "a name, a number or a date for each claim."),
              ("Unfair ghosting", "Hinting at faults that aren't true.", "only risks that are true of any firm."),
              ("Forgetting the chooser's risk", "The sponsor needs a defensible choice.", "give them evidence they can repeat.")],
    grimoire=[(6, "bake-off-arena", "The Bake-Off Arena", "shows the same fight from MetroVolt's later side: Pip, Corvid and Vexmoor, in 2028.")],
    use=["A bigger, better-known rival is bidding.", "The rival has history with the client.", "Your team wants to point at a past failure."],
    skip=["You're the big firm: then read it backwards."],
    related=["<b>What About the Vendor Already Here?</b> (previous note)", "<b>How Do We Win the Room?</b> (this volume)", "<b>Who Will Vouch for Us?</b> (this volume)", "<b>Stakeholder Map</b> (Ana, vol. 1)"],
    quiz=[("Why not attack Orion in the bid?", "The people scoring the bid ran, approved and sponsored it."),
          ("What is a discriminator?", "Something you offer that rivals can't easily claim, e.g. named senior people."),
          ("When is ghosting fair?", "When it describes the risk of an approach, true of anyone, rather than accusing a firm."),
          ("Why offer to name key people in the contract?", "It turns a sales claim into an enforceable promise, which makes it credible."),
          ("What is safe choice bias?", "Choosers prefer the famous option because a failure is easier to defend.")],
    quiz_sit=[("At the orals, a panel member asks “Why should we trust a small firm after what happened last time?” How do you answer without mentioning Orion?", "Point to the specifics: the named team in the room will do the work and is named in the contract; the plan has ranges they can check; discovery is paid and separate; and a reference can describe a similar move in 2025.")],
    try_it="Write down a rival's three real strengths. For each, write one specific answer you could prove: a name, a number, a document. Then delete any sentence in your pitch that mentions them.",
    remember="Don't fight a famous name on size. Put <span class=\"hl\">the chef's name on the menu</span>, and never say a word against <span class=\"hl\">the kitchen next door</span>.",
    late=dict(when="Tue 16 March 2027 · 22:05 · Leeds",
              lines=["Deleted “unlike previous suppliers”. Vivian says it was the best line in the bid. It would have been the last line they read.",
                     "Graham asked why anyone would pick 80 over 40,000. Because they'll meet all 6 of the 80 who'll do the work.",
                     "Put Hana and me in the key personnel clause. Now we can't leave. That's the point."]),
    sources=["APMP, <i>Body of Knowledge</i>: competitive analysis, discriminators and ghosting.",
             "David Maister, Charles Green and Robert Galford, <i>The Trusted Advisor</i> (2000).",
             "Tom Sant, <i>Persuasive Business Proposals</i> (2012)."],
)

# ------------------------------------------------------------------ 11 What If Sales Already Promised?
sp_problem = Doodle(760, 240, "Doodle of a promise travelling. On 19 January at a dinner, Vivian tells Priya twelve months, all customers. Priya repeats it to Lord Varnish. Lord Varnish puts it in an executive update: Lodestar, all customers off MAVIS in twelve months. By March it's a line in a board paper.",
                    "One sentence at dinner, three retellings, one board paper.", exact=True)
steps_ = [("dinner, 19 Jan", "Vivian → Priya", "y"), ("Priya → Varnish", "a corridor", "paper"), ("exec update", "“all customers, 12 mo”", "pink"), ("board paper", "March", "pink")]
for i, (h, sub, fill) in enumerate(steps_):
    sp_problem.box(14 + i * 188, 40, 168, 100, h, fill, sub=sub, size=18, subsize=15)
    if i:
        sp_problem.arrow(14 + i * 188 - 18, 90, 14 + i * 188 - 2, 90)
sp_problem.note(380, 200, "nobody who'll do the work was at the dinner", "red", size=21)

sp_how = Doodle(760, 300, "Re-anchoring the promise. On the left, what was said: all customers, twelve months. On the right, what the bid says, in the executive summary, in bold: in twelve months, 380,000 customers off MAVIS; first 20,000 in nine months; all 2.3 million in about thirty months, in waves, each faster than the last. Underneath: the re-anchor goes in writing, early, near the old number, and gives the client something real by the old date.",
                "Keep the date, shrink the promise, and say the whole truth next to it.", exact=True)
sp_how.box(14, 20, 300, 140, "what was said", "pink", sub="“all customers, 12 months”", size=20, subsize=17)
sp_how.arrow(320, 90, 380, 90)
sp_how.box(386, 20, 360, 140, None, "green", rx=10)
sp_how.head(566, 50, "what the bid says", size=20)
for i, t in enumerate(["12 months: 380,000 customers", "9 months: the first 20,000", "≈ 30 months: all 2.3 million"]):
    sp_how.text(566, 86 + i * 26, t, size=17)
sp_how.row([("in writing", None, "paper"), ("early", None, "paper"), ("near the old number", None, "paper"), ("something real by then", None, "paper")], x=14, y=200, h=60, w=172, gap=14, size=16)

SALES_PROMISED = dict(
    slug="sales-already-promised", date=date(2027, 3, 22), meta="bid day 48 of 50", where="LEEDS",
    kicker="a.k.a. “re-anchoring an overpromise”",
    tldr="When someone has already promised a date you can't hit, you can't un-say it, but you can <b>re-anchor</b> it: give the client <b>something real by the promised date</b>, say the <b>whole truth next to it</b>, and do it <b>in writing, early</b>, near where the old number lives. Do it with the person who promised, not around them. The later the correction, the more it looks like failure instead of honesty.",
    chips=[("Family", "up against the others"), ("Lives in", "bid executive summary, first paragraph"), ("Pairs with", "estimating in fog, the orals")],
    problem_side="Wrenfield, 22 March 2027",
    problem="""  <p class="lead">Two days before the deadline, Vivian admits the whole story. At a dinner on <b>19 January</b>, before the tender came out, she told Priya Nair: <i>“Wrenfield could get all your customers off MAVIS in twelve months.”</i> Priya repeated it to Lord Varnish. Lord Varnish put it in an executive update.</p>
  <ul>
    <li>Phase 1 is <b>380,000</b> accounts. “All customers” is <b>2.3 million</b>. Ines's estimate for everything is about <b>30 months</b>.</li>
    <li>The tender's rules (clause 6.7) forbid contact with MetroVolt staff. <span class="hl-pink">Vivian can't call Priya to correct it.</span></li>
    <li>If the bid simply says “12 months” for wave 1, MetroVolt will hear “12 months for everything”, and remember Wrenfield said it.</li>
  </ul>""",
    problem_figs=[sp_problem],
    sides=dict(client=("Priya, holding the number", "<p>Priya didn't invent “twelve months”; a supplier told her. She's repeated it upwards. If the bids now say thirty, she looks naive in front of Lord Varnish. She'll favour a bidder who <b>lets her keep face</b> and tells her the truth.</p>", "I need a twelve-month story I can still tell."),
                vendor=("Ines, Vivian and Graham", "<p>Vivian's promise is Wrenfield's promise now. Ines won't repeat it. Graham won't let the bid contradict Vivian so bluntly that Priya feels lied to. They need a sentence that <b>keeps the date</b>, <b>shrinks the promise</b> and <b>states the whole truth</b>.</p>", "Something true by month twelve, and the rest said out loud.")),
    sides_after="Re-anchoring isn't saying “we were wrong”. It's giving the client something real by the date they heard, and the true shape of the rest.",
    analogy_side="the decorator who said “done by Christmas”",
    analogy="""  <p>A decorator says “the whole house, done by Christmas”, then measures it and realises that's impossible. She doesn't wait until 20 December. In November she says: <b>“By Christmas you'll have the living room and the kitchen finished, so you can host. The bedrooms follow in January, one a week.”</b> The family still gets Christmas.</p>""",
    map=[("“The whole house by Christmas”", "“All customers in twelve months”"),
         ("Living room and kitchen by Christmas", "380,000 customers in twelve months, the first 20,000 in nine"),
         ("Bedrooms in January, one a week", "Waves 2–4, about 30 months in all, each faster"),
         ("Saying it in November", "Saying it in the bid, before signature"),
         ("So you can host", "So Priya has a true twelve-month story")],
    how_side="keep the date, shrink the promise, say it in writing",
    how="""  <p>The three of them agree a rule: <b>Vivian's date stays; the scope attached to it changes; the whole truth sits right next to it.</b> The first paragraph of the executive summary, in bold:</p>
  <p><i>“In twelve months, 380,000 MetroVolt customers will be off MAVIS, and the first 20,000 within nine. Moving all 2.3 million will take about thirty months, in waves, each faster than the last because each one teaches the next.”</i></p>
  <p>It's in <b>writing</b>, so it's what MetroVolt quotes from now on. It's <b>early</b>: in the bid, not after signature. It's <b>near the old number</b>: the phrase “twelve months” is there, so Priya's story survives. And it gives something <b>real by the old date</b>. Vivian reads it and says, quietly, “that's what I should have said in January.” At the orals she'll say it herself.</p>""",
    how_figs=[sp_how],
    steps=[("Find out exactly what was promised", "Words, date, to whom, and who it was repeated to."),
           ("Do it with the person who promised", "Not around them. They have to own the correction too."),
           ("Keep the date, change what's attached", "Something real and valuable by the promised date."),
           ("Put the whole truth next to it", "The full timeline, in the same sentence or the next."),
           ("Write it where the old number lives", "Executive summary, first paragraph."),
           ("Say it out loud at the first chance", "The orals, by the person who made the promise.")],
    vocab=[("Overpromise", "A commitment made without the people who'd deliver it."),
           ("Re-anchoring", "Replacing a remembered number with a true one, close to the old one."),
           ("Anchoring", "People judge later numbers against the first one they heard."),
           ("Scope re-framing", "Keeping a date by changing what's delivered by it."),
           ("Executive summary", "The page every evaluator reads; often the only one the sponsor reads."),
           ("Sales handover", "Passing what sales said and promised to the people who'll deliver it.")],
    code=dict(file="bid/lodestar/re-anchor.md", note="Vivian, Graham, Ines · Mon 22 Mar 2027", src="""
RE-ANCHOR · "all customers in twelve months"

said        19 Jan, dinner, Vivian → Priya: "all your customers off MAVIS in 12 months"
repeated    Priya → Lord Varnish → exec update (Feb): "Lodestar: all customers, 12 mo"
true        wave 1 (380,000) P50 11 / P80 14 · all 2.3m ≈ 30 months in waves

the sentence (exec summary, para 1, bold)
  "In twelve months, 380,000 MetroVolt customers will be off MAVIS, and the first
   20,000 within nine. Moving all 2.3 million will take about thirty months, in
   waves, each faster than the last because each one teaches the next."

rules       keep the date · shrink what's attached · whole truth next to it
            in writing · before signature · Vivian says it at the orals
never       "twelve months" on its own, anywhere
"""),
    contract=dict(side="what the bid's own words commit to", doc="Lodestar bid · executive summary and §4.2", date="24 Mar 2027", stamp="in writing",
                  clauses=[("ES.1", "In twelve months, 380,000 MetroVolt customers will be off MAVIS, and the first 20,000 within nine. Moving all 2.3 million will take about thirty months, in waves.", "the only place “twelve months” appears without a scope next to it: nowhere."),
                           ("ITT 5.4", "The tender response, including its executive summary, will be incorporated into the contract.", "so the re-anchor is contractual. good.")],
                  plain="the bid becomes part of the contract, so the re-anchored sentence is now what Wrenfield promised, not the dinner. Make sure the old number never appears on its own anywhere in the document."),
    health=dict(now="a",
                g=("trust is high", ["Correct it in a conversation, then in writing.", "The client will thank you.", "Do it the same week."]),
                a=("before signature, no contact allowed", ["Re-anchor in the bid itself.", "Keep the date, shrink what's attached.", "Let the promiser say it at the orals."]),
                r=("after signature, already in the plan", ["A formal re-baseline with evidence.", "Expect it to cost trust.", "Next time, catch it in the bid."])),
    pressure=dict(level=4, title="someone else's promise", cost="a hard conversation with a senior colleague · two days to the deadline",
                  items=["Vivian didn't lie; she was hopeful at dinner. Treat it as a fixable mistake, not a crime, and she'll help fix it.", "If you correct it around her, you'll win the bid and lose the account director."]),
    baseline="Each line compares <b>letting “twelve months” stand, or contradicting it bluntly</b>, with <b>re-anchoring it in the bid, with the person who promised</b>.",
    ratings=[(2, 4, "Priya gets a true story she can still tell."),
             (1, 4, "Nobody will be held to thirty months' work in twelve."),
             (1, 4, "The fixed price covers the scope actually promised."),
             (1, 5, "“380,000 in twelve months” can't be misheard."),
             (2, 4, "The plan isn't bent to fit a dinner."),
             (1, 4, "The biggest expectation risk is dealt with before signing."),
             (1, 4, "The bid, not the dinner, is what was promised."),
             (4, 4, "One meeting and one paragraph."),
             (4, 4, "Nothing to keep up, if it's early.")],
    pitfalls=[("Hoping it was forgotten", "It wasn't. It's in a board paper.", "find out exactly where the number went."),
              ("Correcting it around the promiser", "Wins the bid, loses the colleague.", "do it with them; let them say it."),
              ("Contradicting it bluntly", "The sponsor looks naive in front of her boss.", "keep the date, change what's attached."),
              ("Waiting until after signature", "Then it looks like failure.", "re-anchor in the bid."),
              ("The old number on its own, anywhere", "One stray “12 months” undoes the paragraph.", "search the document for it.")],
    grimoire=[(6, "overpromise-golem", "The Overpromise Golem", "is what happens when nobody re-anchors: Felix's “real-time AI”, MetroVolt, 2028.")],
    use=["Sales, a manager or a colleague has promised something undeliverable.", "A number has been repeated upwards.", "Before signature, while the words can still change."],
    skip=["The promise is achievable: then don't argue with it, deliver it."],
    related=["<b>How Long Will It Really Take?</b> (this volume)", "<b>How Do We Win the Room?</b> (next note)", "<b>Who Remembers What We Promised?</b> (this volume)", "<b>How Do We Keep Them With Us?</b> (Sanne, vol. 5)"],
    quiz=[("What does re-anchoring mean?", "Replacing a remembered number with a true one, kept close to the old one."),
          ("Why keep the date instead of correcting it?", "The client has repeated it; giving something real by that date lets them keep their story."),
          ("Why couldn't Vivian just call Priya?", "The tender rules forbid contact with MetroVolt staff outside the clarification process."),
          ("Why involve the person who made the promise?", "They have to own the correction, or you lose them as an ally."),
          ("Why search the whole bid for the old number?", "One stray “twelve months” on its own would undo the re-anchor.")],
    quiz_sit=[("At the orals, Lord Varnish says “I was told twelve months for everything.” Who answers, and what do they say?", "Vivian, briefly and warmly: that's what she hoped in January; once the team looked properly, the honest version is 380,000 customers in twelve months, the first 20,000 in nine, and all of them in about thirty months, in waves. Then Ines shows the plan.")],
    try_it="Think of a date or number someone promised on your behalf. Write a single sentence that keeps the date, changes what's attached to it, and puts the whole truth next to it. Who would need to say it, and where?",
    remember="You can't un-say a promise. You can <span class=\"hl\">keep the date</span>, <span class=\"hl\">shrink what's attached</span>, and say the rest out loud, <span class=\"hl\">early</span>.",
    late=dict(when="Mon 22 March 2027 · 21:30 · Leeds",
              lines=["“All your customers in twelve months.” At dinner. In January. To the sponsor.",
                     "Vivian cried a little, then wrote the new sentence better than I did. She'll say it at the orals.",
                     "Searched the bid for “12 months”. Found it four times. Now it's zero times on its own."]),
    sources=["Daniel Kahneman, <i>Thinking, Fast and Slow</i> (2011): anchoring.",
             "Jeff Thull, <i>Mastering the Complex Sale</i> (2010): from sales promise to delivery.",
             "Kim Scott, <i>Radical Candor</i> (2017): correcting a colleague kindly."],
)

# ------------------------------------------------------------------ 12 How Do We Win the Room?
or_problem = Doodle(760, 260, "Doodle of room 27B on 21 April 2027. A long table with the panel of six: Elaine in the chair, Priya, Hollis, Nkem, Kofi, and Desmond who doesn't score. Opposite, four people from Wrenfield: Ines, Hana, Bilal, Callum. Vivian sits at the end. A clock shows ninety minutes. A door marked minute 52 shows Lord Varnish arriving.",
                    "Room 27B: six on the panel, four presenting, ninety minutes, and one visitor at minute 52.", exact=True)
or_problem.box(140, 100, 480, 60, "", "paper", rx=6)
for i, n in enumerate(["Elaine", "Priya", "Hollis", "Nkem", "Kofi", "Desmond"]):
    or_problem.circle(170 + i * 84, 74, 22, "y" if n != "Desmond" else "paper")
    or_problem.text(170 + i * 84, 40, n, size=15)
for i, n in enumerate(["Ines", "Hana", "Bilal", "Callum"]):
    or_problem.circle(230 + i * 100, 188, 22, "blue")
    or_problem.text(230 + i * 100, 232, n, size=15)
or_problem.icon("clock", 20, 90, 1.2)
or_problem.note(56, 182, "90 min", "pen", size=19)
or_problem.icon("door", 660, 80, 1.3)
or_problem.note(700, 180, "min 52:", "red", size=17)
or_problem.note(700, 202, "Varnish", "red", size=17)

or_analogy = Doodle(760, 220, "Doodle of a restaurant's kitchen trial for a new head chef. The candidate doesn't present slides about cooking; she cooks a dish from the restaurant's own fridge, in front of the owners, and explains each choice. The owners taste it.",
                    "A chef's trial: cook from their fridge, in front of them.", exact=True)
or_analogy.icon("fridge", 60, 40, 2)
or_analogy.arrow(200, 110, 280, 110)
or_analogy.icon("kitchen", 300, 50, 1.6)
or_analogy.arrow(420, 110, 500, 110)
or_analogy.box(510, 50, 230, 120, "they taste it", "green", sub="not a slide about taste", size=20, subsize=16)

or_how = Doodle(760, 340, "The ninety minutes, planned. Ten minutes: who we are, with Vivian re-stating the promise. Twenty minutes: their data, Bilal's profile of the 10,000-record sample showing 7.8 per cent failing the address check, and what it means for price. Fifteen minutes: the hardest question, answered before it's asked: why won't this be another failed programme? Then forty-five minutes of questions, with each question routed to the person who'll do that work. Three rehearsals beforehand, the last with Graham playing Hollis.",
                "Show them their own data, answer the hardest question first, and let the doers answer.", exact=True)
segs = [("10′ · who", "re-anchor", "paper", 120), ("20′ · their data", "7.8 % fail", "y", 170), ("15′ · the hard one", "why not again?", "pink", 170), ("45′ · questions", "the doer answers", "blue", 248)]
x = 14
for h, sub, fill, w in segs:
    or_how.box(x, 30, w, 100, h, fill, sub=sub, size=17, subsize=15)
    x += w + 8
or_how.box(14, 170, 360, 120, "the sample", "y", sub="10,000 records · arrived 1 April", size=20, subsize=16)
or_how.text(194, 274, "7.8 % fail the address check", size=17)
or_how.box(390, 170, 356, 120, "rehearsals × 3", "paper", sub="last one: Graham plays Hollis", size=20, subsize=16)
or_how.note(380, 326, "no slide anyone in the room couldn't defend alone", "red", size=19)

THE_ORALS = dict(
    slug="the-orals", date=date(2027, 4, 21), meta="orals day", where="FL 27",
    kicker="a.k.a. “the presentation, the bid defence, the beauty parade”",
    tldr="The orals are where the panel decides whether it <b>believes</b> the bid. Bring <b>the people who'll do the work</b>, not the people who sell it. Show your thinking on <b>the client's own data</b>, not on generic slides. Answer <b>the hardest question before it's asked</b>. Route every question to the person who'd do that work, and rehearse with someone playing the toughest panel member. Ninety minutes, planned to the minute.",
    chips=[("Family", "up against the others"), ("Lives in", "bid/lodestar/orals/ (deck, run sheet, Q bank)"), ("Pairs with", "assumptions, big consultancy, references")],
    problem_side="The Grid, room 27B, 21 April 2027",
    problem="""  <p class="lead">On <b>7 April</b> three bidders are shortlisted: Wrenfield, Vexmoor and Halvorsen. Orals are on <b>Wednesday 21 April</b>, 90 minutes each, in room 27B on floor 27. The panel: <b>Elaine</b> (chair), <b>Priya</b>, <b>Hollis</b>, <b>Nkem</b> from finance, <b>Kofi Asante</b> from metering, and Desmond, who runs the process but doesn't score.</p>
  <ul>
    <li>MetroVolt sent each shortlisted bidder a <b>10,000-record sample</b> on 1 April, as promised in clarification Q-05.</li>
    <li>Bilal's profile of it: <b>7.8 %</b> of records fail the address check. The bid assumed <b>5 %</b> (A1-07).</li>
    <li>Vivian's first plan: she presents for 40 minutes, “the techies” take questions. <span class="hl-pink">The panel has already met forty presenters who never came back after signing.</span></li>
  </ul>""",
    problem_figs=[or_problem],
    sides=dict(client=("the panel of six", "<p>Each panel member has a different fear. <b>Elaine</b>: another Orion. <b>Hollis</b>: an architecture that's pretty and wrong. <b>Nkem</b>: a price that grows. <b>Kofi</b>: metering forgotten again. <b>Priya</b>: choosing the small firm and being blamed. They'll score on what they <b>see</b> the team do in the room.</p>", "Are these the people who'll actually be here at 2 a.m.?"),
                vendor=("four from Wrenfield", "<p>Wrenfield has 90 minutes to be believed. Its best evidence is the people (Ines, Hana, Bilal, Callum, named in the bid) and the sample: <b>the only bidder that will show MetroVolt its own data</b>, including the bad news that 7.8 % isn't 5 %.</p>", "Let them watch us think about their problem.")),
    sides_after="An oral presentation is a short job interview for a team. The panel is imagining working with you.",
    analogy_side="the chef's trial",
    analogy="""  <p>A restaurant hiring a head chef doesn't watch slides about cooking. It asks for a <b>trial</b>: cook a dish from <b>our</b> fridge, in <b>our</b> kitchen, while we watch. The owners learn more from how she handles a missing ingredient than from her CV. A good candidate tells them about the missing ingredient before they notice.</p>""",
    analogy_figs=[or_analogy],
    map=[("Cooking from their fridge", "Profiling MetroVolt's own 10,000-record sample"),
         ("A missing ingredient", "7.8 % failing, not 5 %"),
         ("Mentioning it before they notice", "Showing the gap, and what it costs, unprompted"),
         ("The chef, not the agent", "Ines, Hana, Bilal and Callum presenting"),
         ("The owners taste it", "The panel asks questions of the people who'll do the work")],
    how_side="their data, the hard question first, and the doers answer",
    how="""  <p><b>The run sheet.</b> Ten minutes on who: Vivian opens for two of them and says the re-anchored sentence herself; then each presenter says what they'll personally do on Lodestar. Twenty minutes on <b>their data</b>: Bilal shows the sample profile live, including the 7.8 %, and what A1-07 means at that rate (about <b>£26k</b> on wave 1 for the extra 2.8 %, paid only if it holds). Fifteen minutes on <b>the hardest question</b>, asked by Ines before anyone else can: <i>“Why won't this be another programme that never goes live?”</i> Answer: waves, a pilot gate in month 9, paid discovery, and the people in this room named in the contract. Then 45 minutes of questions.</p>
  <p><b>Routing.</b> Every question goes to the person who'd do the work: architecture to Hana, data to Bilal, plan and money to Callum, everything else to Ines. Nobody answers outside their area; “Hana will take that” is the most convincing sentence in the room.</p>
  <p><b>Rehearsal.</b> Three run-throughs, timed. In the last one, Graham plays Hollis and is unpleasant. At minute 52 on the day, <b>Lord Varnish</b> walks in and asks about “synergy with Orion's hub”. Ines answers in one sentence (“where the hub's data model fits MetroVolt's data, discovery will tell us, and we'll reuse it”) and hands back to Elaine. Hollis writes something down. It turns out to be a 4.</p>""",
    how_figs=[or_how],
    steps=[("Bring the doers", "The named team presents; sales opens and closes."),
           ("Use their data", "One real piece of the client's world, worked through live."),
           ("Ask the hardest question yourself", "In the first half, with your answer."),
           ("Route every question", "To the person who'd do that work; nobody else answers."),
           ("Rehearse three times", "Timed; once with someone playing the toughest panellist."),
           ("Plan for the visitor", "A one-sentence answer for the senior person who drops in.")],
    vocab=[("Orals", "A presentation and Q&amp;A with the evaluation panel, usually scored."),
           ("Run sheet", "The minute-by-minute plan for the presentation."),
           ("Question bank", "Likely questions, each with an owner and a short answer."),
           ("Murder board", "A hostile rehearsal panel that asks the worst questions."),
           ("Moderation", "Panel members agreeing a score together after scoring alone."),
           ("Clarification at orals", "Anything said can be written into the contract; say only what you'd sign.")],
    code=dict(file="bid/lodestar/orals/run-sheet.md", note="final rehearsal · Mon 19 Apr 2027", src="""
ORALS · Wed 21 Apr 2027, 14:00–15:30, room 27B, The Grid

min   who      what
0     Vivian   thanks · the re-anchored sentence, in her own words      (2)
2     all      "on Lodestar I will…" — one sentence each                (8)
10    Bilal    their sample, live: 10,000 records, 7.8 % fail address    (12)
22    Ines     what that means: A1-07, ≈ £26k on wave 1, if it holds  (8)
30    Ines     the hard one, asked by us: "why won't this be another      (15)
               programme that never goes live?" waves · pilot gate m9 ·
               paid discovery · the people here named in the contract
45    Elaine   questions (45), routed: architecture → Hana · data → Bilal
               plan, money → Callum · everything else → Ines
90    end      no slide anyone here couldn't defend alone

if Lord Varnish appears: one sentence, then hand back to the chair
"""),
    contract=dict(side="what's said in the room counts", doc="Lodestar ITT · §7 presentations", date="3 Feb 2027", stamp="on the record",
                  clauses=[("7.2", "The presenting team must include the Key Personnel proposed in the tender response.", "so no “A team for the orals, B team for the work”."),
                           ("7.4", "Statements made at the presentation may be recorded and incorporated into the contract as clarifications of the tender response.", "Bilal's 7.8 % is now on the record. good: it was true.")],
                  plain="anything you say at the orals can end up in the contract. That's why the people who'll do the work should answer: they won't promise what they can't deliver."),
    health=dict(now="a",
                g=("they know you already", ["Shorter presentation, more conversation.", "Show what's new since last time.", "Still the doers answer."]),
                a=("they've never met you", ["Their data, live.", "The hard question first.", "Named people, routed answers."]),
                r=("the panel has a favourite", ["Make it hard to score you low: evidence, not charm.", "Answer the favourite's strengths specifically.", "Leave them a document worth keeping."])),
    pressure=dict(level=5, title="ninety minutes", cost="three rehearsals · two nights of bad sleep · one surprise visitor",
                  items=["Everyone is nervous. Give each person one part they own completely; nerves shrink when the job is small and clear.", "After the last rehearsal, stop changing slides. Sleep is worth more than slide 14."]),
    baseline="Each line compares <b>sales presenting slides, engineers taking questions</b> with <b>the doers presenting the client's own data and answering their own areas</b>.",
    ratings=[(2, 5, "The panel watches the real team work on its real data."),
             (2, 3, "Nerves, but shared; nobody is outside their area."),
             (3, 4, "The 7.8 % is priced in front of finance."),
             (3, 4, "Questions get exact answers from owners."),
             (3, 5, "Hana defends the design herself."),
             (2, 4, "Bad news shown before it was found."),
             (2, 4, "What was said is true and recorded."),
             (3, 2, "Three rehearsals, a week of preparation."),
             (4, 4, "A run sheet and a question bank.")],
    pitfalls=[("The sales team presents", "The panel never meets the people who'd do the work.", "the named team presents."),
              ("Generic slides", "The same deck as for every client.", "one real piece of their world, live."),
              ("Hiding bad news", "The 7.8 % comes out in due diligence, later and worse.", "show it, priced, before they find it."),
              ("Everyone answers everything", "Contradictions in front of the panel.", "route every question to one owner."),
              ("Arguing with the senior visitor", "Winning the point, losing the room.", "one sentence, then back to the chair.")],
    grimoire=[(6, "bake-off-arena", "The Bake-Off Arena", "is the same day from the panel's side of the table, a year later, with Pip presenting.")],
    use=["Any shortlisted bid with a presentation.", "Pitches, design reviews and steering committees, too.", "When the panel has been burned before."],
    skip=["Written-only evaluations: put the same thinking in the document."],
    related=["<b>What If Sales Already Promised?</b> (previous note)", "<b>How Do We Compete with a Big Consultancy?</b> (this volume)", "<b>Who Will Vouch for Us?</b> (next note)", "<b>Presenting to Executives</b> (Ana, vol. 3)"],
    quiz=[("Who should present at the orals?", "The named people who'll do the work; sales opens and closes."),
          ("Why profile the client's own sample?", "It shows the team thinking about their real problem, and it surfaces bad news honestly."),
          ("Why ask the hardest question yourself?", "You choose the timing and the answer, and it shows you're not hiding from it."),
          ("What is routing?", "Sending each question to the one person who'd do that work."),
          ("Why be careful what you say at the orals?", "Statements can be recorded and incorporated into the contract.")],
    quiz_sit=[("Hollis asks Callum a detailed question about the change-detection design. Callum starts to answer. What do you do?", "Gently route it: “Hana designed that part; Hana?” The panel trusts an answer from the owner, and Callum avoids promising something he can't defend.")],
    try_it="Plan your next important presentation as a run sheet: who speaks, for how long, about what. Add one real piece of the audience's own world, and the hardest question they could ask, answered by you in the first half.",
    remember="Bring <span class=\"hl\">the doers</span>, use <span class=\"hl\">their data</span>, and ask <span class=\"hl\">the hard question</span> before they do.",
    late=dict(when="Wed 21 April 2027 · 23:50 · the train home",
              lines=["Bilal showed them 7.8 % of their own records failing, on their own screen, and Nkem nodded. Nobody nods at bad news unless they believe it.",
                     "Lord Varnish at minute 52. One sentence. Hollis wrote something down.",
                     "Vivian said the twelve-month sentence herself, better than in the bid. I think she meant it."]),
    sources=["APMP, <i>Body of Knowledge</i>: orals and presentations.",
             "Nancy Duarte, <i>Resonate</i> (2010).",
             "Chip Heath and Dan Heath, <i>Made to Stick</i> (2007)."],
)

NOTES = [INCUMBENT, BIG_CONSULTANCY, SALES_PROMISED, THE_ORALS]
