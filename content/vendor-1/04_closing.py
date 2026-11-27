# Series 5 · On the Client's Floor · Vol. 1 · Winning the Work · Closing the deal (notes 13–15).
from datetime import date

# ------------------------------------------------------------------ 13 Who Will Vouch for Us?
rf_problem = Doodle(760, 240, "Doodle of two reference calls on 23 April 2027 and a site visit on 28 April. Elaine has a list of questions; the first one is: tell me about a time Wrenfield gave you bad news. Vivian's instinct is to pick the happiest client and script them.",
                    "Elaine's first question to every referee: “Tell me about a time they gave you bad news.”", exact=True)
rf_problem.icon("phone", 40, 40, 2.2)
rf_problem.box(160, 40, 340, 110, "Elaine's question 1", "y", sub="“a time they gave you bad news?”", size=20, subsize=16)
rf_problem.box(540, 40, 200, 110, "Vivian's plan", "pink", sub="happiest client, scripted", size=18, subsize=15)
rf_problem.note(380, 210, "a scripted referee can't answer question 1", "red", size=21)

rf_how = Doodle(760, 300, "Choosing references by the client's fears. MetroVolt's three fears, from the orals: legacy data, honesty about delays, and working with another supplier. Pennine Housing Group answers the first two: a tenancy system moved in 2025, six weeks late, told in week three. Ashby Building Society answers the third: a mainframe integration in 2024 alongside the core banking vendor. Each referee is briefed on the fears, not scripted on the answers.",
                "Pick referees for the client's fears, brief them on those fears, and let them tell the truth.", exact=True)
fears = ["legacy data", "honest about delays", "another supplier"]
for i, f in enumerate(fears):
    rf_how.box(14, 20 + i * 76, 220, 60, f, "pink", size=18)
rf_how.box(400, 20, 346, 136, "Pennine Housing", "green", sub="2025 · 6 weeks late, told in week 3", size=20, subsize=15)
rf_how.box(400, 172, 346, 80, "Ashby Building Society", "green", sub="2024 · mainframe + core vendor", size=18, subsize=15)
rf_how.arrow(238, 50, 396, 70)
rf_how.arrow(238, 126, 396, 110)
rf_how.arrow(238, 202, 396, 210)
rf_how.note(380, 286, "brief them on the fears · never script the answers", "red", size=19)

REFERENCES = dict(
    slug="references", date=date(2027, 4, 23), meta="after the orals", where="LEEDS",
    kicker="a.k.a. “client references and site visits”",
    tldr="References win on <b>specifics</b>, and the most convincing ones include <b>something that went wrong</b> and how you handled it. Choose referees by the <b>client's fears</b>, not by who loves you most. <b>Brief</b> them on what the client is worried about; <b>never script</b> their answers. For a site visit, show the people who'd step in if a key person fell ill, and how you actually work on an ordinary Tuesday.",
    chips=[("Family", "closing the deal"), ("Lives in", "bid/lodestar/references.md"), ("Pairs with", "the orals, big consultancy")],
    problem_side="reference calls on 23 April, site visit on 28 April 2027",
    problem="""  <p class="lead">Two days after the orals, Desmond asks for <b>two references</b> and a <b>site visit</b>. Elaine sends her list of questions in advance. The first: <i>“Tell me about a time Wrenfield gave you bad news.”</i></p>
  <ul>
    <li>Vivian wants Wrenfield's happiest client, a small charity website, and a short script.</li>
    <li>MetroVolt's fears, heard at the orals: <b>legacy data</b>, <b>honesty about delays</b>, <b>working alongside another supplier</b>. <span class="hl-pink">The charity website answers none of them.</span></li>
    <li>Halvorsen is out of the contest after the orals. It's Wrenfield and Vexmoor.</li>
  </ul>""",
    problem_figs=[rf_problem],
    sides=dict(client=("Elaine calls", "<p>Elaine doesn't want to hear that Wrenfield is lovely. She wants to know <b>what it's like when things go wrong</b>: who calls, how early, and whether the story changes. Every reference she took for Orion was glowing.</p>", "Tell me about the bad day."),
                vendor=("Ines chooses", "<p>The most useful reference is <b>Pennine Housing Group</b>: a tenancy system for 140,000 tenancies, moved in 2025, <b>six weeks late</b>. Wrenfield told them in week three and re-planned in the open. It's not the happiest story. It's the one that answers question 1.</p>", "Our best reference is our worst month, handled well.")),
    sides_after="A reference with a problem in it is more believable than one without, because every real project has one.",
    analogy_side="the tradesperson's past customers",
    analogy="""  <p>Before hiring a builder, you ask to speak to past customers. The one who says “perfect, no problems” tells you little. The one who says <b>“they found rot under the floor, told us that afternoon, showed us photos and the price, and still finished a week late”</b> tells you exactly what you need: what happens on the bad day.</p>""",
    map=[("“Perfect, no problems”", "The charity website, scripted"),
         ("“They found rot and told us that afternoon”", "Pennine: six weeks late, told in week three"),
         ("Asking about a job like yours", "Choosing referees by MetroVolt's fears"),
         ("Visiting the builder's yard", "The site visit to Wrenfield in Leeds"),
         ("Who'd cover if the foreman was ill", "The bench behind Hana and Ines")],
    how_side="choose by their fears, brief, don't script",
    how="""  <p>Ines lists MetroVolt's three fears and picks one referee for each. <b>Pennine Housing Group</b> (Joanne Pryce, IT director): a legacy tenancy system, data cleaned in waves, six weeks late and <b>told in week three</b>. <b>Ashby Building Society</b> (Tom Hendry, head of change): a 2024 integration with a mainframe, working daily alongside the core banking vendor.</p>
  <p>Ines calls each referee before MetroVolt does. She tells them <b>what MetroVolt is worried about</b> and asks them to <b>be honest</b>, including about what went wrong. She doesn't send a script. Joanne tells Elaine: <i>“They rang me on a Tuesday in week three, said we'd be six weeks late and why, and the date they gave me then was the date we went live.”</i></p>
  <p>At the <b>site visit on 28 April</b>, Elaine and Hollis meet the two engineers who'd cover for Hana, see Wrenfield's weekly status template and a real (anonymised) RAID log, and watch a stand-up. Hollis asks to see a test report. He gets the real one, including two failing tests.</p>""",
    how_figs=[rf_how],
    steps=[("List the client's fears", "From the tender, the questions and the orals."),
           ("Pick a referee for each fear", "Similar problem, recent, reachable."),
           ("Call them first", "Thank them, tell them the client's worries."),
           ("Ask them to be honest", "Including what went wrong. Never script answers."),
           ("Show an ordinary day at the site visit", "Real templates, real logs, the people behind the key people."),
           ("Thank them afterwards", "Whatever the result.")],
    vocab=[("Reference", "A past client who agrees to describe working with you."),
           ("Site visit", "The client visits your office to see how you work."),
           ("Due diligence", "The client's checks before contract: references, finances, security."),
           ("Bench", "The people in your firm who could step in on the account."),
           ("Scripted reference", "A referee given answers to recite; usually obvious and useless."),
           ("Proof point", "A specific, checkable fact supporting a claim.")],
    code=dict(file="bid/lodestar/references.md", note="Ines · Thu 22 Apr 2027", src="""
REFERENCES · LODESTAR

MetroVolt's fears (orals)      referee                          why
legacy data                    Pennine Housing Group            tenancy system, 140,000
honest about delays              Joanne Pryce, IT director      tenancies, 2025; 6 weeks late,
                                                                told in week 3
another supplier               Ashby Building Society           mainframe integration, 2024,
                                 Tom Hendry, head of change     alongside the core vendor

briefing (by phone, not email): what MetroVolt worries about · please be honest,
including what went wrong · no script
site visit, Wed 28 Apr: the 2 engineers behind Hana · weekly status template ·
a real RAID log (anonymised) · a stand-up · the real test report (2 failing tests)
"""),
    contract=dict(side="what due diligence can ask for", doc="Lodestar ITT · §8 due diligence", date="3 Feb 2027", stamp="checked",
                  clauses=[("8.1", "MetroVolt may contact references, visit the bidder's premises and request evidence of financial standing before award.", "they'll also read our accounts. £9m turnover, no debt. good."),
                           ("8.3", "Information provided during due diligence that is materially inaccurate may lead to exclusion.", "the real test report, then. with the two failures.")],
                  plain="references and visits are part of the evaluation, and misleading the client during them can exclude you. Honest is also the safe option."),
    health=dict(now="a",
                g=("they already trust you", ["One reference may do.", "Offer the visit anyway.", "Still pick by their fears."]),
                a=("they've been burned before", ["A referee for each fear.", "Honest stories, including a bad one.", "Show the bench."]),
                r=("they're looking for a reason to say no", ["Specifics only; no adjectives.", "Expect calls you didn't arrange.", "Don't over-manage the referees."])),
    pressure=dict(level=2, title="waiting", cost="phone calls to old clients · a tidy office",
                  items=["Asking an old client for a favour feels awkward. They usually say yes, and they like being asked about how it went.", "Don't tidy the RAID log for the visit. A clean one looks fake."]),
    baseline="Each line compares <b>the happiest client, scripted</b> with <b>referees chosen for the client's fears, briefed but not scripted</b>.",
    ratings=[(2, 5, "Elaine hears about the bad day, from someone else."),
             (3, 3, "Neutral."),
             (3, 3, "Neutral."),
             (3, 3, "Neutral."),
             (3, 4, "The real test report, failures included."),
             (3, 3, "Neutral."),
             (2, 3, "Nothing misleading in due diligence."),
             (4, 3, "Two calls and a day's visit."),
             (4, 4, "Nothing to keep up.")],
    pitfalls=[("The happiest client", "A glowing reference on a different kind of work.", "choose by the client's fears."),
              ("Scripting", "Referees recite; the client notices.", "brief on the worries, never the answers."),
              ("Surprising the referee", "They get a call they weren't expecting.", "call them first."),
              ("A staged site visit", "A tidy office and a perfect log.", "show an ordinary Tuesday."),
              ("Forgetting to thank them", "You'll need them again.", "thank them whatever happens.")],
    use=["References and site visits are requested.", "The client's fears are known.", "You have a past project with a problem handled well."],
    skip=["Never skip it when asked. If you have no relevant reference, say so and offer something else (a pilot, a paid discovery)."],
    related=["<b>How Do We Win the Room?</b> (previous note)", "<b>What Do We Give Away in the Final Offer?</b> (next note)", "<b>How Do We Compete with a Big Consultancy?</b> (this volume)"],
    quiz=[("Why is a reference with a problem in it more convincing?", "Every real project has one; hearing how it was handled is the evidence the client needs."),
          ("How should you choose referees?", "One for each of the client's fears, on similar work."),
          ("What's the difference between briefing and scripting a referee?", "Briefing tells them the client's worries; scripting gives them answers to recite."),
          ("What should a site visit show?", "An ordinary day: real templates, real logs, and the people behind the key people."),
          ("Why show the real test report with two failures?", "A perfect one looks staged, and misleading the client in due diligence can exclude you.")],
    quiz_sit=[("Your best reference left their company last month. What do you do?", "Tell the client, offer their successor or another client on similar work, and, if they're willing, the former contact as a personal reference. Don't hide the change.")],
    try_it="List your client's three biggest fears. For each, find a past project that answers it, including what went wrong. Who would you call, and what would you tell them before the client does?",
    remember="The best reference is <span class=\"hl\">your worst month, handled well</span>, told by someone else, <span class=\"hl\">unscripted</span>.",
    late=dict(when="Fri 23 April 2027 · 21:20 · Leeds",
              lines=["Joanne told Elaine about week three. I could hear Elaine writing.",
                     "Vivian still thinks the charity would have been nicer. Nicer isn't what Elaine is buying.",
                     "Note: don't tidy the RAID log before Wednesday. Hollis will know."]),
    sources=["David Maister, Charles Green and Robert Galford, <i>The Trusted Advisor</i> (2000).",
             "APMP, <i>Body of Knowledge</i>: proof points and references.",
             "Crown Commercial Service, guidance on supplier due diligence."],
)

# ------------------------------------------------------------------ 14 What Do We Give Away in the Final Offer?
bf_problem = Doodle(760, 240, "Doodle of the best and final offer request on 27 April 2027: please consider a ten per cent reduction, due Friday 30 April. Graham's first idea is to take the 480,000 pounds out of the contingency. Ines draws the estimate curve: without the contingency, the fixed price stops being a P80 price and becomes a coin toss.",
                    "“Please consider a 10 % reduction.” Graham's first idea: take it out of the contingency.", exact=True)
bf_problem.icon("envelope", 30, 40, 1.6)
bf_problem.box(140, 30, 290, 90, "“consider 10 %”", "y", sub="due Fri 30 April", size=21, subsize=16)
bf_problem.box(470, 30, 270, 90, "−£480k from contingency?", "pink", size=18)
bf_problem.note(380, 170, "then the fixed price is a coin toss, not a P80", "red", size=21)

bf_how = Doodle(760, 340, "The trade table. Things Wrenfield can give, each with what MetroVolt gets in return: train-the-trainer instead of training 40 super-users saves 120,000 pounds and MetroVolt's trainers learn the system; a 60-day warranty instead of 90 saves 60,000 pounds; Things Wrenfield won't give: the contingency, the day rates, the discovery. Total reduction 180,000 pounds, 3.75 per cent: 4.62 million.",
                "Trade, don't cut. Every pound off buys back scope, risk or time, and the contingency goes last.", exact=True)
bf_how.box(14, 14, 470, 40, "we give, and you get", "green", size=19)
bf_how.box(500, 14, 246, 40, "we don't give", "pink", size=19)
for i, (a, b) in enumerate([("train-the-trainer", "−£120k · your trainers own it"), ("warranty 90 → 60 days", "−£60k · faster handover")]):
    bf_how.box(14, 64 + i * 70, 470, 60, a, "paper", sub=b, size=18, subsize=15)
for i, t in enumerate(["contingency (P80)", "day rates", "discovery £380k"]):
    bf_how.box(500, 64 + i * 46, 246, 38, t, "paper", size=17)
bf_how.box(14, 220, 732, 70, "£4.8m → £4.62m", "y", sub="−£180k, −3.75 % · contingency untouched", size=24, subsize=16)
bf_how.note(380, 322, "and say why the rest isn't moving", "pen", size=19)

BAFO = dict(
    slug="best-and-final-offer", date=date(2027, 4, 29), meta="BAFO due tomorrow", where="LEEDS",
    kicker="a.k.a. “BAFO”, the last price negotiation",
    tldr="When the client asks for a lower final price, <b>trade, don't cut</b>. Every pound off should buy something back: <b>less scope</b>, <b>less risk carried</b> or <b>more time</b>. Make a list of what you can give and what the client gets in return, and a list of what you won't give and why. <b>The contingency goes last</b>: without it, your fixed price is a bet. Explain the offer in one paragraph the client can repeat.",
    chips=[("Family", "closing the deal"), ("Lives in", "bid/lodestar/bafo.md"), ("Pairs with", "pricing models, estimating in fog")],
    problem_side="Wrenfield, 29 April 2027",
    problem="""  <p class="lead">On <b>Tuesday 27 April</b> Desmond writes to the two remaining bidders, Wrenfield and Vexmoor: <i>“Please submit your best and final offer by Friday 30 April. MetroVolt invites you to consider a 10 % reduction.”</i> Ten per cent of £4.8m is <b>£480k</b>.</p>
  <ul>
    <li>Graham's first idea: take £480k out of the contingency. “We'll be careful.”</li>
    <li>The contingency is exactly the gap between the P50 and P80 estimates. <span class="hl-pink">Without it, the fixed price is a coin toss.</span></li>
    <li>A rumour reaches Vivian that Vexmoor will cut <b>12 %</b>. Nobody can check it.</li>
  </ul>""",
    problem_figs=[bf_problem],
    sides=dict(client=("Desmond and Nkem", "<p>Asking for 10 % is <b>procurement's job</b>, not an insult. Every pound saved is a pound they can show the Horizon board. They also know a bidder who cuts 10 % with no explanation either padded the first price or is about to suffer.</p>", "Show us it was a real price, and what you'd move."),
                vendor=("Ines and Graham", "<p>Wrenfield wants to win, and Graham wants to show willing. Ines wants the fixed price to stay <b>fixed for a world Wrenfield can survive</b>. The answer is a trade table: things that genuinely cost less if MetroVolt accepts something different.</p>", "We can move the scope. We can't move the odds.")),
    sides_after="A clean cut with no trade tells the client your first price had fat in it. A trade tells them your price was real.",
    analogy_side="the car salesman and the extras",
    analogy="""  <p>A good car dealer asked for 10 % off doesn't cut the price of the engine. He says: <b>“Without the extended warranty, it's £600 less; with steel wheels instead of alloys, £400 less. The engine price is the engine price.”</b> You get a cheaper car and you know exactly what you gave up. If he just knocked 10 % off, you'd wonder what was wrong with it.</p>""",
    map=[("The engine price", "The contingency and the day rates"),
         ("Without the extended warranty", "Warranty 90 → 60 days: −£60k"),
         ("Steel wheels instead of alloys", "Train-the-trainer instead of 40 super-users: −£120k"),
         ("“What's wrong with it?”", "What a 10 % cut with no trade signals"),
         ("A cheaper car you understand", "£4.62m, with each change explained")],
    how_side="a trade table, and the contingency goes last",
    how="""  <p>Callum and Ines list everything that could change the price. Each item gets three columns: <b>what we give</b>, <b>what MetroVolt gets</b>, <b>what it costs them</b>.</p>
  <ul>
    <li><b>Train-the-trainer</b> instead of training 40 super-users directly: <b>−£120k</b>. MetroVolt's own trainers learn the system, which helps waves 2–4. (X-04 changes.)</li>
    <li><b>Warranty 90 → 60 days</b>: <b>−£60k</b>. Faster handover to MetroVolt support.</li>
    <li>Not offered, with reasons in the letter: <b>the contingency</b> (it's what makes the price fixed), <b>day rates</b> (they price every future change), <b>discovery</b> (already capped).</li>
  </ul>
  <p>Total: <b>−£180k (3.75 %)</b>, to <b>£4.62m</b>. Graham worries it isn't 10 %. Ines shows him the curve: at £4.32m the P80 margin would be about 10 %, below Wrenfield's 15 % floor. Graham agrees. The letter's last paragraph: <i>“We have not reduced our contingency. That is what allows us to offer a fixed price we are confident we can honour.”</i></p>""",
    how_figs=[bf_how],
    steps=[("Don't answer the percentage", "Answer with a list of trades."),
           ("List everything that drives the price", "Scope, risk, time, service levels, payment terms."),
           ("For each trade, say what they get", "A trade the client values is worth more than a cut."),
           ("List what won't move, and why", "Contingency, rates, capped work."),
           ("Check the margin at P80 after the trade", "Against your floor, not your hopes."),
           ("Explain it in one paragraph", "The panel will repeat it to the board.")],
    vocab=[("BAFO", "Best and final offer: the last price, after negotiation."),
           ("Trade", "Giving something in return for a lower price."),
           ("Contingency", "Money in the price for the risks you carry."),
           ("Margin floor", "The lowest margin your firm will accept."),
           ("Train-the-trainer", "Teaching the client's trainers, who then train users."),
           ("Winner's curse", "Winning by pricing below what the work will really cost.")],
    code=dict(file="bid/lodestar/bafo.md", note="sent Fri 30 Apr 2027, 11:20", src="""
BEST AND FINAL OFFER · LODESTAR phase 1

                                          was        now        change
discovery (T&M, capped)                   £380,000   £380,000   —
wave 1 fixed price                        £4.80m     £4.62m     −£180,000 (−3.75 %)

we give                          you get                              saving
train-the-trainer (not 40 users) your trainers own it for waves 2–4    £120,000
warranty 90 → 60 days            faster handover to MetroVolt support  £60,000

not reduced, and why
contingency   it is what makes the price fixed (we price at P80)
day rates     they price every future change, in your favour too
discovery     already capped

check: P80 margin after trade ≈ 16 % (floor 15 %) · at −10 % it would be ≈ 10 %
"""),
    contract=dict(side="what the BAFO letter turns into", doc="MetroVolt BAFO request · 27 Apr 2027", date="reply due 30 Apr", stamp="final",
                  clauses=[("2", "Best and final offers are final. MetroVolt will not invite further price negotiation.", "one shot. no “we'll sort it later”."),
                           ("4", "Changes to scope in a BAFO must be stated explicitly and will be reflected in the contract.", "so X-04 changes from “beyond 40 super-users” to “train-the-trainer”. write it.")],
                  plain="a BAFO is final, and any scope you trade away is written into the contract. List every change explicitly, or you'll deliver the old scope at the new price."),
    health=dict(now="a",
                g=("long relationship", ["A small gesture may be enough.", "Trade on things they value.", "Still protect the contingency."]),
                a=("competitive final round", ["Trade table, not a cut.", "Explain what won't move.", "Check the margin at P80."]),
                r=("a price war", ["Know your floor and keep it.", "Losing on price is better than the winner's curse.", "Leave the door open politely."])),
    pressure=dict(level=4, title="the last price", cost="a rumour about Vexmoor · a nervous managing director · 72 hours",
                  items=["Rumours about a rival's price are almost never checkable. Price your own work, not their gossip.", "Graham needs a way to say yes to 3.75 %. The curve gives it to him; the margin floor is his own rule."]),
    baseline="Each line compares <b>cutting 10 % out of the contingency</b> with <b>trading £180k of scope and keeping the contingency</b>.",
    ratings=[(3, 4, "A reasoned offer reads as a real price."),
             (2, 4, "The team isn't committed to a coin-toss price."),
             (1, 4, "P80 margin stays above the floor."),
             (3, 4, "The traded scope is written down explicitly."),
             (3, 4, "Training for waves 2–4 improves."),
             (1, 4, "The contingency still covers the bad half of the curve."),
             (3, 4, "The letter explains what didn't move."),
             (4, 3, "Two days of work."),
             (4, 4, "One letter.")],
    pitfalls=[("Cutting the contingency", "The fixed price stops being fixed for you.", "the contingency goes last, if ever."),
              ("A cut with no trade", "The client wonders what was padded.", "every pound buys something back."),
              ("Pricing against a rumour", "You race a number nobody can check.", "price your own work."),
              ("Trading scope silently", "You deliver the old scope at the new price.", "state every change explicitly."),
              ("Below your floor to win", "The winner's curse.", "check the margin at P80 against the floor.")],
    use=["Any final price negotiation.", "A client asks for a percentage off.", "A rival is rumoured to be cheaper."],
    skip=["The price really did have room in it: then say so, and cut honestly."],
    related=["<b>Fixed Price, or Time and Materials?</b> (this volume)", "<b>How Long Will It Really Take?</b> (this volume)", "<b>Who Remembers What We Promised?</b> (next note)", "<b>Make It, Buy It, or Hire It?</b> (Sanne, vol. 2)"],
    quiz=[("What does “trade, don't cut” mean?", "Every reduction buys back scope, risk or time, instead of simply lowering the price."),
          ("Why does the contingency go last?", "It covers the gap between the P50 and P80 estimates; without it the fixed price is a coin toss."),
          ("What did Wrenfield trade?", "Train-the-trainer instead of 40 super-users (−£120k) and a 60-day warranty instead of 90 (−£60k)."),
          ("Why explain what didn't move?", "It shows the first price was real and gives the panel a reason to repeat."),
          ("What is the winner's curse?", "Winning by pricing below what the work will really cost.")],
    quiz_sit=[("Desmond phones (through the proper channel) and says “Vexmoor is at £4.2m.” What do you do?", "Thank him, and don't move below your floor. Restate what your price buys and offer another trade if one exists. If £4.2m is real, it may be the winner's curse for them.")],
    try_it="Take a price you've quoted. List three things you could change that would genuinely cost you less, and what the client would get in return for each. Which part of the price must never move, and how would you explain why in one sentence?",
    remember="Trade, don't cut. Every pound off <span class=\"hl\">buys something back</span>, and <span class=\"hl\">the contingency goes last</span>.",
    late=dict(when="Thu 29 April 2027 · 23:45 · Leeds",
              lines=["£4.62m. 3.75 %, not 10. Graham signed it at 22:10, after looking at the curve for a long time.",
                     "If Vexmoor really cut 12 %, they'll win, and then they'll have to live with it.",
                     "I'd rather lose at £4.62m than win at £4.32m. I said that out loud. Graham didn't disagree."]),
    sources=["Roger Fisher and William Ury, <i>Getting to Yes</i> (1981).",
             "Chris Voss, <i>Never Split the Difference</i> (2016).",
             "Richard Thaler, <i>The Winner's Curse</i> (1992)."],
)

# ------------------------------------------------------------------ 15 Who Remembers What We Promised?
bd_problem = Doodle(760, 260, "Doodle of Thursday 6 May 2027. At 09:00 MetroVolt's all-hands announces Project Horizon: a fifteen per cent cost cut. At 11:40 Wrenfield gets an email: preferred bidder for Lodestar, subject to Horizon governance. Champagne in Leeds at 12:00. Ines counts the promises Wrenfield has made: in the bid, in 63 clarifications, at the orals, at the reference calls, in the final offer. Forty-seven.",
                    "09:00 Horizon. 11:40 preferred bidder, “subject to Horizon governance”. 47 promises, made by people who'll now step back.", exact=True)
bd_problem.box(14, 30, 220, 90, "09:00 · Horizon", "pink", sub="15 % cost cut", size=19, subsize=16)
bd_problem.box(260, 30, 240, 90, "11:40 · preferred", "green", sub="“subject to Horizon”", size=19, subsize=16)
bd_problem.box(526, 30, 220, 90, "12:00 · champagne", "y", sub="Leeds", size=19, subsize=16)
for i, t in enumerate(["bid", "clarifications", "orals", "references", "BAFO"]):
    bd_problem.box(14 + i * 148, 150, 136, 50, t, "paper", size=17)
bd_problem.note(380, 236, "47 promises · who remembers them in month 6?", "red", size=20)

bd_how = Doodle(760, 320, "The promises register: every promise Wrenfield made during the bid, from five sources, each with a source, an owner and a due date. Examples: first 20,000 customers in month 9; Hana and Ines named for wave 1; weekly status every Friday; joint triage with Halvorsen; the sample profile shared with MetroVolt; train-the-trainer. The bid team hands the register to the delivery team in one session on 7 May; Vivian steps back to account management.",
                "Every promise from every source, in one list, with an owner. The bid team leaves; the list stays.", exact=True)
bd_how.box(14, 14, 732, 40, "promises register · 47 lines", "y", size=20)
rows = [("P-01", "first 20,000 live in month 9", "Callum"), ("P-07", "Hana + Ines named, wave 1", "Graham"),
        ("P-12", "status every Friday", "Callum"), ("P-19", "joint triage with Halvorsen", "Ines"),
        ("P-31", "sample profile shared", "Bilal"), ("P-44", "train-the-trainer", "Callum")]
for i, (pid, t, who) in enumerate(rows):
    y = 62 + i * 36
    bd_how.box(14, y, 80, 30, pid, "paper", size=15, rx=3)
    bd_how.box(100, y, 500, 30, t, "paper", size=16, rx=3)
    bd_how.box(606, y, 140, 30, who, "blue", size=15, rx=3)
bd_how.note(380, 300, "bid team → delivery team, one session, Fri 7 May", "pen", size=19)

BID_TO_DELIVERY = dict(
    slug="bid-to-delivery", date=date(2027, 5, 7), meta="preferred bidder, day 2", where="LEEDS",
    kicker="a.k.a. “the bid-to-delivery handover” and the promises register",
    tldr="A bid makes dozens of promises, in the document, in clarifications, at the orals, in reference calls and in the final offer, and the people who made them often step back once it's won. Before the champagne is finished, build a <b>promises register</b>: every promise, <b>its source, an owner and a date</b>. Hand it over in one session, with the assumptions and the named people, so nobody discovers the deal in month six.",
    chips=[("Family", "closing the deal"), ("Lives in", "delivery/lodestar/promises-register.md"), ("Pairs with", "assumptions, the statement of work, the baseline")],
    problem_side="MetroVolt and Wrenfield, 6–7 May 2027",
    problem="""  <p class="lead">On <b>Thursday 6 May</b> at 09:00, MetroVolt's all-hands announces <b>Project Horizon</b>: a 15 % cost cut, about 600 roles, led by Rupert Thorne, with <b>Vexmoor Consulting</b> as his advisers. At 11:40 Wrenfield gets Desmond's email: <b>preferred bidder for Lodestar</b>, “subject to Horizon governance”.</p>
  <ul>
    <li>Champagne in Leeds at noon. Graham makes a speech. Vivian is thanked twice.</li>
    <li>Ines counts what Wrenfield has promised: in the bid, in 63 clarifications, at the orals, on the reference calls, in the final offer. <b>47 promises</b>.</li>
    <li>Vivian moves back to account management on Monday. <span class="hl-pink">Half the promises were made in rooms the delivery team never sat in.</span></li>
    <li>And “subject to Horizon governance” means nobody knows yet what happens next.</li>
  </ul>""",
    problem_figs=[bd_problem],
    sides=dict(client=("Elaine, holding the bid", "<p>For MetroVolt, the bid <b>is</b> the promise: every sentence, every answer at the orals. Elaine will hold Wrenfield to what Bilal said about the sample and what Vivian said about twelve months. She doesn't care who in Wrenfield said it.</p>", "You said it. I wrote it down."),
                vendor=("Ines and Callum", "<p>Wrenfield's bid team (Vivian, a bid writer, Graham) made promises the delivery team has to keep. Some were never written in the bid at all: a sentence at the orals, a reassurance to a referee. Callum wants them all in one list <b>before</b> people forget what they said.</p>", "If it's not on the list, we'll find out about it at a steering committee.")),
    sides_after="Clients remember promises by what was said. Vendors remember them by who said it. The register makes both the same list.",
    analogy_side="the house sale's fixtures list",
    analogy="""  <p>When you buy a house, the sellers made promises at every viewing: “the boiler was serviced last year”, “we'll leave the curtains”. A good solicitor makes them write all of it on <b>the fixtures and fittings form</b>, signed, so on moving day nobody argues about the curtains. The estate agent who said it all has moved on to the next sale.</p>""",
    map=[("Promises at viewings", "Promises at the orals and on reference calls"),
         ("The estate agent moves on", "Vivian goes back to account management"),
         ("The fixtures and fittings form", "The promises register"),
         ("Arguing about curtains on moving day", "Discovering a promise at a steering committee"),
         ("Signed by both", "Walked through at the kick-off with MetroVolt")],
    how_side="every promise, its source, an owner and a date",
    how="""  <p>On <b>Friday 7 May</b> Callum books three hours with everyone who touched the bid. They go source by source: the <b>bid document</b> (31 promises), <b>clarification answers</b> (4), the <b>orals</b> (7, from Bilal's notes and the panel's questions), the <b>reference calls and site visit</b> (3) and the <b>BAFO</b> (2). Each promise gets a line: ID, the exact words, the source, an <b>owner</b> in the delivery team and a <b>due date</b>.</p>
  <p>Some are big (P-01, first 20,000 live in month 9). Some are small and dangerous because they're easy to forget (P-12, a status report every Friday; P-31, sharing the sample profile with MetroVolt's data team). Two are promises Wrenfield should never have made, and are flagged for the contract talks (an orals answer that implied “no change requests for data” and a reference-call comment that Hana would be on site “every day”).</p>
  <p>Vivian walks the team through what she said at dinner, at the orals and to Priya's assistant. Then she steps back, with one standing job: <b>tell Callum within a day if she ever promises anything again</b>. The register goes into the delivery folder next to the assumptions. It'll be walked through with MetroVolt at the kick-off.</p>""",
    how_figs=[bd_how],
    steps=[("Book the handover before the celebration ends", "Within a week, while memories are fresh."),
           ("Go source by source", "Bid, clarifications, orals, references, final offer, any emails."),
           ("Write each promise in the exact words", "With its source."),
           ("Give each an owner and a date", "In the delivery team, not the bid team."),
           ("Flag the dangerous ones", "Take them into the contract talks to fix in writing."),
           ("Keep a line open to sales", "New promises reach the register within a day.")],
    vocab=[("Promises register", "Every commitment made while selling, with source, owner and date."),
           ("Bid-to-delivery handover", "Passing the deal, its promises and its risks to the delivery team."),
           ("Preferred bidder", "The bidder chosen to negotiate the contract; not yet a contract."),
           ("Key personnel", "Named people the contract says must deliver."),
           ("Commitment creep", "Small promises made after the bid by people outside delivery."),
           ("Standstill period", "A pause after an award decision when losing bidders may challenge it.")],
    code=dict(file="delivery/lodestar/promises-register.md", note="handover session · Fri 7 May 2027", src="""
PROMISES REGISTER · LODESTAR                       47 lines · owner: Callum

id    promise (exact words)                         source     owner    due
P-01  "first 20,000 customers live within 9 months" bid ES.1   Callum   month 9
P-02  "380,000 customers within 12 months"          bid ES.1   Callum   month 12
P-07  Ines Duarte and Hana Sato for all of wave 1   bid §5     Graham   always
P-12  "a status report every Friday"                orals Q14  Callum   weekly
P-19  joint, evidence-based triage with Halvorsen   bid §3.6   Ines     from M2
P-31  "we'll share the sample profile with your     orals      Bilal    by 31 May
       data team"
P-44  train-the-trainer for waves 2–4               BAFO       Callum   M4
…
FLAGGED for contract talks
P-23  orals: "you won't see change requests for     orals Q31  Ines     fix in SOW
       data" (contradicts A1-07)
P-38  reference call: Hana "on site every day"      ref. call  Callum   clarify: 3 days
"""),
    contract=dict(side="what “preferred bidder” means, and doesn't", doc="MetroVolt award letter · 6 May 2027", date="11:40", stamp="not yet a contract",
                  clauses=[("1", "MetroVolt intends to award the Lodestar contract to Wrenfield Digital Ltd, subject to contract, to the standstill period, and to approval under Horizon governance.", "three “subject to”s. no contract yet."),
                           ("3", "The contract will incorporate the tender, the tender response, clarifications and the best and final offer.", "so all 47 are in. including P-23.")],
                  plain="preferred bidder means you've won the right to negotiate, not the contract. Everything you said while bidding will be incorporated, so the promises register is really a list of contract terms, and the dangerous ones must be fixed before signing."),
    health=dict(now="a",
                g=("smooth award", ["Handover within a week.", "Walk the register with the client at kick-off.", "Close the flagged ones in the contract."]),
                a=("won, but “subject to” something", ["Handover now anyway: memories fade.", "Fix dangerous promises in the contract talks.", "Keep sales close but quiet."]),
                r=("won, and the client remembers different promises", ["Compare registers line by line.", "Agree one list in writing.", "Fix the gaps before you sign, not after."])),
    pressure=dict(level=3, title="winning", cost="a hangover · 47 promises · one “subject to Horizon”",
                  items=["Winning is when the stress moves from the bid team to the delivery team. Acknowledge it, out loud.", "Vivian walking through her own promises takes courage. Thank her for it in front of the team."]),
    baseline="Each line compares <b>handing over the bid document only</b> with <b>a promises register from every source, with owners and dates</b>.",
    ratings=[(3, 4, "The delivery team knows what MetroVolt heard."),
             (2, 4, "No surprises from promises made in other rooms."),
             (2, 4, "Two dangerous promises caught before the contract."),
             (2, 5, "47 promises in one list."),
             (3, 4, "P-23 contradicts A1-07: fixed before signing."),
             (2, 4, "Every promise has an owner and a date."),
             (2, 4, "Source and exact words recorded."),
             (4, 3, "A three-hour session."),
             (4, 3, "The register needs keeping up.")],
    pitfalls=[("Handing over the document only", "Promises from the orals and calls are lost.", "go source by source."),
              ("Paraphrasing", "“About nine months” becomes “nine months” becomes “by March”.", "exact words, with the source."),
              ("Owners in the bid team", "They've moved on.", "owners in the delivery team."),
              ("Ignoring dangerous promises", "They're incorporated into the contract.", "flag them and fix them before signing."),
              ("Sales keeps promising", "New commitments after the handover.", "a standing rule: tell the owner within a day.")],
    grimoire=[(5, "reading-the-omens", "Reading the Omens", "is Horizon from inside MetroVolt: the freeze, the consultants, the all-hands at 09:00.")],
    use=["Any won bid.", "Sales and delivery are different people.", "Promises were made outside the document."],
    skip=["The same three people sold it and will deliver it, and wrote everything down: a short check is still worth it."],
    related=["<b>What Are We Assuming?</b> (this volume)", "<b>What If Sales Already Promised?</b> (this volume)", "<b>What Does the Contract Actually Say?</b> (vol. 2)", "<b>What Exactly Did We Promise?</b> (Sanne, vol. 2)"],
    quiz=[("What is a promises register?", "Every commitment made while selling, with exact words, source, owner and due date."),
          ("Why go source by source?", "Promises were made in the bid, clarifications, orals, reference calls and the final offer, not only the document."),
          ("Why write the exact words?", "Paraphrases drift; the client will quote the exact words."),
          ("What does “preferred bidder” mean?", "You've been chosen to negotiate the contract; it isn't signed yet."),
          ("Why fix dangerous promises before signing?", "Everything said during the bid is incorporated into the contract.")],
    quiz_sit=[("Three weeks after the handover, Vivian mentions she told Priya's assistant the pilot “might be ready by Christmas”. What do you do?", "Add it to the register with the exact words and source, flag it, and agree with Vivian how to correct it with Priya directly, before it reaches a steering committee.")],
    try_it="Think of a deal, a project or a job you've just won. List every promise made while winning it, from every conversation, in the exact words. Who owns each one now?",
    remember="The bid team leaves. <span class=\"hl\">The promises stay</span>. Write them all down, <span class=\"hl\">in the exact words</span>, before the champagne is finished.",
    late=dict(when="Fri 7 May 2027 · 22:10 · Leeds",
              lines=["We won. Subject to contract, standstill and something called Horizon governance.",
                     "Forty-seven promises. Two of them we should never have made. One of them was mine, at the orals, about change requests. Fixing it next week.",
                     "Vivian walked us through every dinner. That took more courage than the orals did."]),
    sources=["APMP, <i>Body of Knowledge</i>: the bid-to-delivery handover.",
             "Crown Commercial Service, guidance on award, standstill and contract finalisation.",
             "Atul Gawande, <i>The Checklist Manifesto</i> (2009)."],
)

NOTES = [REFERENCES, BAFO, BID_TO_DELIVERY]
