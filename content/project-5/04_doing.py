# Series 2 · Book 3 · The Project Manager's Notebook · Vol. 5 · Doing something about it (the Risk domain, part 2)
# Narrator: Sanne. Facts: docs/larder-casebook.md, "Book 3, Vol. 5"; numbers in the comment block of 01_involved.py.
# R-07 responses (22 Feb 2027): before 60 % × €40k = €24k; after 30 % × €40k = €12k; responses cost €8k
#   (agent €6k from the Belgian set-up line, cooling supplier's early drawings €2k) → worth €12k − €8k = €4k.

RISK = ["risk"]

# ------------------------------------------------------------------ 13 What Do We Do About It?
rp_problem = Doodle(760, 260, "Doodle of Monday 22 February 2027. R-07, the permit, is red at sixteen. The register's response column says 'monitor'. Watching a risk is not a response. Sanne has two weeks before the steering group, and four ways to act on a threat to choose from.",
                    "R-07 is red at 16. Its response says “monitor”. Watching is not doing.", exact=True)
rp_problem.box(20, 24, 330, 140, None, "pink")
rp_problem.head(185, 60, "R-07 · 16 · red", size=19)
rp_problem.text(185, 94, "response: “monitor”", size=16)
rp_problem.text(185, 122, "owner: Sanne (since 10 Feb)", size=16)
rp_problem.box(410, 24, 330, 140, None, "y")
rp_problem.head(575, 60, "four ways to act", size=19)
rp_problem.text(575, 94, "avoid · transfer", size=16)
rp_problem.text(575, 122, "mitigate · accept", size=16)
rp_problem.note(380, 210, "“monitor” means “hope”, with a review date", "red", size=19)
rp_problem.note(380, 242, "and the opportunities had no response either", "pen", size=16)

rp_analogy = Doodle(760, 250, "Doodle of a homeowner and the risk of a storm. Avoid: don't build on the cliff edge. Transfer: buy insurance, someone else pays. Mitigate: fix the roof tiles and clear the gutters. Accept: keep some savings for whatever is left. Four different answers to the same storm.",
                    "One storm, four answers: don't build there, insure it, fix the roof, keep savings for the rest.", exact=True)
rp_analogy.row([("avoid", "not on the cliff", "pink"), ("transfer", "insurance", "blue"), ("mitigate", "fix the roof", "green"), ("accept", "savings for the rest", "y")], y=40, h=96, size=18, subsize=14)
rp_analogy.note(380, 196, "most real plans use more than one", "pen", size=19)

rp_how = Doodle(760, 470, "The response workshop for R-07, Monday 22 February 2027. Avoid: keep deliveries after seven and a smaller cooling plant, so no permit is needed; rejected by Joost because Koen delivers at five thirty and a smaller plant can't hold the range. Transfer: Hilde, a permit agent, six thousand euros, from 8 March; this transfers the paperwork, not the date. Mitigate: an informal meeting with the city on 11 March; the cooling supplier's drawings by 15 March; application lodged by 26 March. Accept the rest: contingency, and a trigger: not lodged by 26 March goes to the steering group. The sum: before, sixty percent of forty thousand, twenty-four thousand; after, thirty percent, twelve thousand; the responses cost eight thousand. Worth it, by four thousand.",
                "R-07: avoid rejected, transfer the paperwork, mitigate three ways, accept the rest with a trigger. €8k to cut €24k to €12k.", exact=True)
rp_how.box(14, 14, 360, 124, None, "paper", stroke="red")
rp_how.head(194, 42, "avoid ✗", size=18)
rp_how.text(194, 74, "deliveries after 07:00, smaller plant", size=14)
rp_how.text(194, 100, "rejected: Koen 05:30; range too small", size=14)
rp_how.box(386, 14, 360, 124, None, "blue")
rp_how.head(566, 42, "transfer", size=18)
rp_how.text(566, 74, "Hilde, permit agent, €6k, from 8 Mar", size=14)
rp_how.text(566, 100, "the paperwork moves; the date doesn't", size=14)
rp_how.box(14, 150, 360, 150, None, "green")
rp_how.head(194, 178, "mitigate", size=18)
rp_how.text(194, 210, "meet the city: Thu 11 Mar", size=14)
rp_how.text(194, 236, "cooling drawings: by Mon 15 Mar", size=14)
rp_how.text(194, 262, "lodge: by Fri 26 Mar", size=14)
rp_how.box(386, 150, 360, 150, None, "y")
rp_how.head(566, 178, "accept the rest", size=18)
rp_how.text(566, 210, "contingency for the residual", size=14)
rp_how.text(566, 236, "trigger: not lodged by 26 Mar", size=14)
rp_how.text(566, 262, "→ steering group", size=14)
rp_how.box(14, 316, 732, 140, None, "paper")
rp_how.head(380, 346, "is it worth it?", size=18)
rp_how.text(380, 380, "before: 60 % × €40k = €24k · after: 30 % × €40k = €12k", size=15)
rp_how.text(380, 410, "responses cost €8k (agent 6 + early drawings 2)", size=15)
rp_how.text(380, 440, "€24k − €12k − €8k = €4k better, and the tail gets shorter", size=15)

rp_deep1 = Doodle(760, 330, "Antwerp's responses on one page: threats on the left, opportunities on the right. Threats: avoid, R-07's delivery hours, considered and rejected; transfer, the permit agent and the builder's late penalty; mitigate, R-07's early meeting and drawings, R-02 the agency started in May; accept, R-10 the rival, passively; escalate, R-04 Bancontact certification to Cho's payments roadmap. Opportunities: exploit, O-01 Rotterdam's shelving drawings sent in January; enhance, O-02 asking the landlord for insulation; share, a joint launch offer with the bakery next door; accept, O-03 a bigger waitlist than planned.",
                  "Five answers to a threat, four to an opportunity, each with an Antwerp example.", exact=True)
rp_deep1.box(14, 14, 360, 300, None, "pink")
rp_deep1.head(194, 44, "threats", size=18)
for i, t in enumerate(["avoid: early hours (rejected)", "transfer: agent; late penalty", "mitigate: meet city, drawings", "accept: the rival (watch)", "escalate: Bancontact → Cho"]):
    rp_deep1.text(194, 88 + i * 46, t, size=15)
rp_deep1.box(386, 14, 360, 300, None, "green")
rp_deep1.head(566, 44, "opportunities", size=18)
for i, t in enumerate(["exploit: shelving drawings", "enhance: ask for insulation", "share: offer with the bakery", "accept: a bigger waitlist"]):
    rp_deep1.text(566, 88 + i * 46, t, size=15)

RESPONSES = dict(
    slug="risk-responses",
    kicker="a.k.a. planning risk responses: avoid, transfer, mitigate, accept, escalate",
    tldr="For each important risk, choose what to <b>do</b>, not just what to watch. For a <b>threat</b>: <b>avoid</b> it (change the plan so it can't happen), <b>transfer</b> it (to someone better placed, by contract or insurance), <b>mitigate</b> it (make it less likely or less bad), or <b>accept</b> it (with money set aside and a trigger, or knowingly). For an <b>opportunity</b>: <b>exploit</b>, <b>enhance</b>, <b>share</b> or <b>accept</b>. If it's not the project's to handle, <b>escalate</b> it to whoever owns it. Check that a response is worth what it costs, and what risk it leaves behind.",
    chips=[("Family", "doing something about it"), ("Lives in", "the register's response, owner, trigger and cost columns"), ("Pairs with", "the risk register, expected monetary value, implementing responses")],
    pmbok=dict(covers="choosing responses to threats and opportunities, checking they're worth their cost, and naming residual and secondary risks, fallbacks and triggers",
               domains=RISK, processes=["Plan Risk Responses"], principles=["Be an accountable leader", "Focus on value"], focus=["planning"],
               older="6th: “Plan Risk Responses” (11.5), strategies for threats and opportunities, escalation added in the 6th edition. 7th: the Uncertainty domain."),
    problem_side="Antwerp, 22 February 2027",
    problem="""  <p class="lead">R-07, the permit, is now <b>red at 16</b>, owned by Sanne since 10 February. The register's response column still says <b>“monitor”</b>. So do six others. <span class="hl-pink">Watching a risk is not a response; it's hope, with a review date.</span> The steering group meets on 5 March and Femke will ask what's being done. The four opportunities have no responses at all.</p>
  <ul>
    <li>“Monitor” stood in for a decision.</li>
    <li>Nobody had compared what a response costs with what it saves.</li>
    <li>Opportunities were listed and left alone.</li>
  </ul>""",
    problem_figs=[rp_problem],
    analogy_side="the storm",
    analogy="""  <p>A homeowner facing storms has four answers. <b>Avoid</b>: don't build on the cliff edge. <b>Transfer</b>: buy insurance, so someone else pays for the damage. <b>Mitigate</b>: fix the loose tiles and clear the gutters, so the damage is smaller. <b>Accept</b>: keep some savings for whatever's left. Sensible homeowners use three of the four. Insurance alone doesn't keep the rain out of the bedroom.</p>""",
    analogy_figs=[rp_analogy],
    map=[("Not building on the cliff", "Avoid: no deliveries before 07:00, a smaller plant (rejected)"),
         ("Insurance", "Transfer: Hilde, the permit agent; the builder's late penalty"),
         ("Fixing the tiles", "Mitigate: meet the city early, drawings by 15 March, lodge by 26 March"),
         ("Savings for the rest", "Accept: contingency and a trigger"),
         ("Insurance doesn't keep the rain out", "An agent transfers the paperwork, not the date")],
    how_side="four options per threat, a sum, a trigger, and the opportunities",
    how="""  <p>On <b>Monday 22 February</b> Sanne runs a response workshop with Joost, Lena, Maarten and Pieter. For R-07 they weigh all four. <b>Avoid</b>: deliveries only after 07:00 and a smaller cooling plant, so no permit is needed; Joost rejects it, since Koen delivers at 05:30 and a smaller plant can't hold the range. <b>Transfer</b>: hire <b>Hilde</b>, a permit agent Maarten recommends, for <b>€6k</b> from the Belgian set-up line, from 8 March. Maarten warns: “She takes the paperwork. The date stays yours.” <b>Mitigate</b>: an informal meeting with the city on <b>Thursday 11 March</b>; the cooling supplier's drawings by <b>Monday 15 March</b> (€2k to bring them forward); the application lodged by <b>Friday 26 March</b>. <b>Accept</b> the rest: the contingency covers it, with a <b>trigger</b>: not lodged by 26 March goes to the steering group. The sum: before, 60 % × €40k = <b>€24k</b>; after, 30 % × €40k = <b>€12k</b>; the responses cost <b>€8k</b>; they're worth it, and they shorten the late tail. Then the rest of the register: <b>R-04</b>, Bancontact certification, is <b>escalated</b> to Cho's payments roadmap, where it belongs; Tomás sends Rotterdam's shelving drawings to Pieter (<b>exploit</b> O-01); Femke will ask the landlord about insulation (<b>enhance</b> O-02).</p>""",
    how_figs=[rp_how],
    steps=[("Consider all the options", "Avoid, transfer, mitigate, accept; escalate if it's not yours."),
           ("Price each response", "What it costs, what it saves."),
           ("Choose, often more than one", "Name the residual risk."),
           ("Set a trigger for the rest", "The sign that it's happening, and who acts."),
           ("Look for secondary risks", "What the response itself could cause."),
           ("Do the same for opportunities", "Exploit, enhance, share, accept.")],
    vocab=[("Avoid", "Change the plan so the threat can't happen or can't affect the project."),
           ("Transfer", "Move the threat's consequences, and its handling, to a third party."),
           ("Mitigate", "Reduce the probability or the impact."),
           ("Accept", "Take the risk: actively (a reserve, a fallback) or passively."),
           ("Escalate", "Hand a risk to the person who owns it, outside the project."),
           ("Exploit / enhance / share", "Make an opportunity certain / more likely / shared with a partner who can help."),
           ("Residual risk", "What remains after the response."),
           ("Secondary risk", "A new risk caused by a response."),
           ("Trigger", "A sign that a risk is about to happen, or a date by which a response must have worked.")],
    code=dict(file="antwerp/13-risk-responses.md", note="response workshop, Monday 22 February 2027", plain=True, src="""
# ANTWERP · RISK RESPONSES                                        22 Feb 2027

R-07 PERMIT NOT GRANTED BY EARLY JULY                      before: 4 x 4 = 16 · 60 % x €40k = €24k
  AVOID      no deliveries before 07:00 + a smaller plant     REJECTED (Joost: Koen 05:30; range)
  TRANSFER   Hilde, permit agent, €6k, from Mon 8 Mar         paperwork moves, the date doesn't
  MITIGATE   informal meeting with the city   Thu 11 Mar      owner Sanne
             cooling supplier's drawings      Mon 15 Mar      owner "cooling supplier"  (!)
             application lodged               Fri 26 Mar      owner Hilde
  ACCEPT     residual 3 x 4 = 12 · 30 % x €40k = €12k → contingency
  TRIGGER    not lodged by Fri 26 Mar → steering group
  WORTH IT?  €24k - €12k = €12k less exposure for €8k (agent 6, drawings 2) → yes
  SECONDARY  agent's availability in summer → Hilde names a stand-in

R-03 builder late    TRANSFER late penalty €1,000/day (max 10) · MITIGATE weekend priced
R-02 hiring          MITIGATE Belgian agency from May        R-10 rival   ACCEPT (watch)
R-04 Bancontact      ESCALATE to Cho's payments roadmap (not the project's to fix)
O-01 shelving        EXPLOIT Tomás sends Rotterdam's drawings to Pieter
O-02 insulation      ENHANCE Femke asks at the works approval
O-04 bakery offer    SHARE   a joint launch offer with the bakery next door
"""),
    tools="tools: the register, the four options and escalate, a price for each response, and a trigger with a date.",
    deep_dive=dict(
        side="threat responses, opportunity responses, is it worth it, and what a response leaves behind",
        intro="Choosing a response is a small business decision: what will we spend to change the odds or the damage? This chapter goes through the five threat responses and the four opportunity responses with Antwerp's examples, shows the sum that tells you whether a response is worth it, and covers the risks a response leaves behind or creates.",
        parts=[
            ("Five answers to a threat", """  <ul>
    <li><b>Avoid</b>: change the plan so the threat can't happen: a different design, a different site, a smaller scope. Often the strongest and most expensive. Antwerp's (no early deliveries, a smaller plant) was rejected in February, and partly adopted in July.</li>
    <li><b>Transfer</b>: hand the consequences to someone better placed: a fixed-price contract, a late penalty, insurance, an agent. It moves money or work; it rarely moves the date. Hilde took the permit paperwork; the opening date stayed Larder's.</li>
    <li><b>Mitigate</b>: act now to make the threat less likely (meet the city early) or less bad (drawings ready, so a re-application is quick).</li>
    <li><b>Accept</b>: <b>actively</b>, with a reserve and a fallback plan ready; or <b>passively</b>, deciding to deal with it if it comes. The rival opening first was accepted passively.</li>
    <li><b>Escalate</b>: the threat belongs to someone outside the project. Bancontact certification was Cho's roadmap's; the project told Cho and stopped pretending to own it.</li>
  </ul>""", [rp_deep1]),
            ("Four answers to an opportunity", """  <ul>
    <li><b>Exploit</b>: make it certain. Tomás sent Rotterdam's shelving drawings in January; about €6k saved.</li>
    <li><b>Enhance</b>: make it more likely. Femke asked the landlord to pay for roof insulation, with the energy numbers. (The answer was no; it cost a letter.)</li>
    <li><b>Share</b>: bring in a partner who can help it happen and share the benefit. The bakery next door ran a joint opening offer: a free loaf with a first order, a Larder voucher with a coffee.</li>
    <li><b>Accept</b>: take it if it comes. The waitlist grew faster than planned; nothing to do but staff for it.</li>
  </ul>""", []),
            ("Is a response worth it?", """  <p>Compare the expected cost of the risk <b>before</b> and <b>after</b> the response, and the <b>cost</b> of the response. For R-07: before, 60 % × €40k = €24k; after, 30 % × €40k = €12k; the responses cost €8k. €12k less exposure for €8k: worth it.</p>
  <p>Two cautions. A response can be worth it even when the sum is close, if it shortens a tail the sponsor fears (here, the simulation's late runs). And a response that costs more than it saves can still be right when the effect is one the sponsor won't accept at any odds; that's what appetite is for.</p>""", []),
            ("What a response leaves behind", """  <ul>
    <li><b>Residual risk</b>: what's left. R-07 went from 16 to 12, still red. The residual is accepted with a reserve and a trigger.</li>
    <li><b>Secondary risk</b>: what the response creates. An agent who goes on holiday in July; Hilde named a stand-in.</li>
    <li><b>Fallback plan</b>: what you'll do if the response fails: here, open with dry goods only (rejected in July, but worth having thought about).</li>
    <li><b>Triggers</b>: a date or a sign that says it's time to act: “not lodged by 26 March.” A trigger needs someone watching it. The next note is about what happened when nobody was.</li>
  </ul>""", []),
        ]),
    dial=[("Light", "small work", ["One action per top risk.", "An owner and a date.", "No sums."]),
          ("Standard", "Antwerp", ["All four options weighed for the red risks.", "Cost vs saving; residual and secondary risks.", "Triggers; opportunities too; escalate what isn't yours."]),
          ("Heavy", "large programmes", ["Response plans per risk with budgets.", "Contracts and insurance designed around risk.", "Fallback plans rehearsed."])],
    baseline="Each line compares <b>“monitor” in the response column</b> to <b>chosen responses with costs, residual risk, triggers and opportunities</b>.",
    ratings=[(3, 4, "Money goes to responses that change the outcome."),
             (2, 4, "The permit's late tail got shorter."),
             (2, 5, "Red risks have real responses."),
             (2, 4, "Each response, cost and trigger on one page."),
             (3, 4, "Femke saw what was being done, and why."),
             (3, 4, "Pieter, Hilde and Tomás own pieces."),
             (3, 4, "Fallbacks and triggers are ready."),
             (3, 3, "Neutral."),
             (3, 3, "A workshop, then minutes per risk.")],
    pitfalls=[("“Monitor” as a response", "Hope with a review date.", "choose a real response."),
              ("Transfer and forget", "The date doesn't move with the paperwork.", "keep owning the outcome."),
              ("No sum", "Responses that cost more than they save.", "compare before, after and cost."),
              ("No trigger", "The residual surprises you.", "a date or a sign, and a watcher.")],
    use=["For every red and amber risk.", "When a risk crosses a threshold.", "When opportunities appear.", "When a risk belongs to someone else."],
    skip=["Green risks you accept knowingly: say so in one word."],
    related=["<b>What Is It Worth?</b> (this volume)", "<b>Did We Do What We Said?</b> (next note)", "<b>Make It, Buy It, or Hire It?</b> (vol. 2)", "<b>When Do I Take It Upstairs?</b> (vol. 2)"],
    quiz=[("Name the threat responses.", "Avoid, transfer, mitigate, accept, and escalate."),
          ("Name the opportunity responses.", "Exploit, enhance, share, accept."),
          ("What did Hilde transfer, and what didn't she?", "The paperwork; not the date, which stayed Larder's."),
          ("A risk's response costs €10k and cuts its EMV from €12k to €6k. Do it?", "Not on the sum (€6k saved for €10k), unless it shortens a tail the sponsor won't accept; say which."),
          ("Your payments lead says Bancontact certification is “the project's risk”. Is it?", "No: it's on the payments roadmap; escalate it to its owner and track it as a dependency.")],
    try_it="Find every “monitor” in your risk register's response column. For each, write one real response, its cost, and a trigger with a date.",
    remember="Don't build on the <span class=\"hl\">cliff</span>, insure the <span class=\"hl\">house</span>, fix the <span class=\"hl\">roof</span>, keep some savings.",
    sources=["Project Management Institute, <i>PMBOK Guide</i>, Eighth Edition (2025): Risk domain, planning risk responses.",
             "Project Management Institute, <i>PMBOK Guide</i>, Sixth Edition (2017): 11.5 Plan Risk Responses.",
             "David Hillson, <i>Managing Risk in Projects</i> (2009)."],
)

# ------------------------------------------------------------------ 14 Did We Do What We Said?
ir_problem = Doodle(760, 260, "Doodle of Friday 2 April 2027 and Sanne's mistake for this collection. At the risk review she reads R-07's actions. The meeting with the city on 11 March: done. Hilde started on 8 March: done. The cooling supplier's drawings by 15 March: not done. The owner column says cooling supplier. The supplier was waiting for Larder's final layout. The trigger, not lodged by 26 March, passed a week ago. Hilde thought Sanne was watching it; Sanne thought Hilde was.",
                    "Drawings due 15 March, owner “cooling supplier”. The trigger passed on 26 March. Each thought the other was watching.", exact=True)
ir_problem.row([("Hilde starts", "8 Mar ✓", "green"), ("city meeting", "11 Mar ✓", "green"), ("drawings", "15 Mar ✗", "pink"), ("lodged", "26 Mar ✗", "pink")], y=24, h=84, size=17, subsize=14)
ir_problem.note(380, 150, "owner of the drawings: “cooling supplier”", "red", size=19)
ir_problem.note(380, 186, "the supplier was waiting for Larder's layout", "pen", size=16)
ir_problem.note(380, 222, "Hilde thought Sanne watched the trigger; Sanne thought Hilde did", "pen", size=16)

ir_analogy = Doodle(760, 250, "Doodle of a relay race. The plan said four runners, the baton passed at each mark. The race is lost not by a slow runner but at the third handover, where two runners each thought the other had the baton. A plan of who runs which leg isn't the race. The race is the handovers.",
                    "A relay is lost at the handover, where each runner thought the other had the baton.", exact=True)
for i in range(4):
    ir_analogy.box(14 + i * 186, 50, 170, 70, f"leg {i + 1}", "green" if i < 2 else "y", size=17)
ir_analogy.icon("baton", 372, 130, 0.8, color="red")
ir_analogy.note(380, 210, "the plan names the runners; the race is the handovers", "pen", size=18)

ir_how = Doodle(760, 450, "How Sanne made responses happen from 2 April 2027. Every response action becomes a task in the plan, with an owner inside Larder, a date and a definition of done. The drawings get a Larder owner: Tomás's layout lead sends the 640 square metre layout on 6 April; drawings arrive 9 April; Hilde lodges on Monday 19 April, three and a half weeks after 26 March. Every trigger appears in the Friday status with a named watcher. The risk review asks three questions of every red risk: what was done since last time, what's due, which trigger is closest. The cost: the public inquiry runs from 24 May to 22 June instead of early May; the simulation's P50 moves from 13 to 20 September.",
                "Actions as tasks, owners inside Larder, triggers in the status with a watcher. Lodged 19 April: 3½ weeks late.", exact=True)
ir_how.box(14, 14, 732, 120, None, "blue")
ir_how.head(380, 42, "three rules from 2 April", size=18)
ir_how.text(380, 74, "1 every response action is a task in the plan: owner, date, done", size=15)
ir_how.text(380, 100, "2 every owner works at Larder (a supplier is a source, not an owner)", size=15)
ir_how.text(380, 124, "3 every trigger is in the Friday status, with a named watcher", size=15)
ir_how.row([("layout sent", "Tue 6 Apr", "y"), ("drawings in", "Fri 9 Apr", "y"), ("lodged", "Mon 19 Apr", "pink"), ("complete", "Mon 10 May", "y"), ("inquiry", "24 May–22 Jun", "paper")], y=160, h=84, size=15, subsize=12, gap=10)
ir_how.box(14, 270, 360, 160, None, "paper")
ir_how.head(194, 298, "the review asks", size=17)
for i, t in enumerate(["what was done?", "what's due next?", "which trigger is closest?"]):
    ir_how.text(194, 334 + i * 30, t, size=15)
ir_how.box(386, 270, 360, 160, None, "pink")
ir_how.head(566, 298, "what it cost", size=17)
for i, t in enumerate(["lodged 3½ weeks late", "inquiry from 24 May", "P50 13 → 20 Sep"]):
    ir_how.text(566, 334 + i * 30, t, size=15)

IMPLEMENT = dict(
    slug="implementing-responses",
    kicker="a.k.a. implementing risk responses: owners, actions, triggers",
    tldr="A response on the register is a plan. It only becomes real when someone <b>does</b> it: every response action as a <b>task in the plan</b>, with an <b>owner inside the organisation</b>, a <b>date</b> and a clear “done”; every <b>trigger</b> in the regular status, with a <b>named watcher</b>. A supplier or agent can do the work, but someone of yours must own that it happens. Check implementation at every risk review: what was done, what's due, which trigger is closest.",
    chips=[("Family", "doing something about it"), ("Lives in", "the plan (as tasks) and the Friday status (as triggers)"), ("Pairs with", "risk responses, the issue log, directing the work")],
    pmbok=dict(covers="carrying out the agreed risk responses: assigning actions to owners, tracking them as work, and watching triggers",
               domains=RISK + ["governance"], processes=["Implement Risk Responses"], principles=["Be an accountable leader"], focus=["executing"],
               older="6th: “Implement Risk Responses” (11.6, new in that edition). 7th: the Uncertainty and Delivery domains."),
    problem_side="Antwerp, Friday 2 April 2027",
    problem="""  <p class="lead">This is <b>Sanne's mistake</b> for this collection. At the risk review she reads R-07's actions aloud. Hilde started on 8 March: <b>done</b>. The meeting with the city on 11 March: <b>done</b>. The cooling supplier's drawings by 15 March: <b>not done</b>. The owner column says <b>“cooling supplier”</b>. The supplier had been waiting since mid-March for Larder's final 640 m² layout, and nobody at Larder knew it was waiting. <span class="hl-pink">The trigger, “not lodged by 26 March”, passed a week ago.</span> Hilde thought Sanne was watching it. Sanne thought Hilde was.</p>
  <ul>
    <li>The action's owner was outside Larder, again.</li>
    <li>Response actions lived on the register, not in the plan.</li>
    <li>A trigger with no watcher is a date nobody looks at.</li>
  </ul>""",
    problem_figs=[ir_problem],
    analogy_side="the relay race",
    analogy="""  <p>A relay team plans four runners and three handovers. The race is rarely lost by a slow runner. It's lost at a <b>handover</b>, where two runners each think the other has the baton. The team sheet named every runner. Nobody had practised the third handover.</p>""",
    analogy_figs=[ir_analogy],
    map=[("The team sheet", "The response plan of 22 February"),
         ("The runners", "Sanne, Hilde, the cooling supplier, Tomás's layout lead"),
         ("The dropped baton", "The drawings, waiting for a layout nobody knew was needed"),
         ("Each thought the other had it", "The trigger of 26 March, watched by nobody"),
         ("Practising the handovers", "Actions as tasks, owners inside Larder, triggers with watchers")],
    how_side="actions as tasks, owners inside the organisation, triggers with watchers",
    how="""  <p>Sanne fixes the drawings first. They get a <b>Larder owner</b>: Tomás's layout lead sends the 640 m² layout on <b>Tuesday 6 April</b>, the drawings arrive on <b>Friday 9 April</b>, and Hilde lodges the application on <b>Monday 19 April</b>, three and a half weeks after the trigger date. Then three rules for every response, from that day: <b>every action is a task in the plan</b>, with an owner, a date and a definition of done; <b>every owner works at Larder</b> (a supplier or agent is where the work comes from, not who owns it); <b>every trigger is in the Friday status</b>, with a named watcher. The risk review now asks three questions of each red risk: what was done since last time, what's due, which trigger is closest. Sanne tells the steering group on 7 May what the three and a half weeks cost: the public inquiry now runs from <b>24 May to 22 June</b> instead of early May, and the simulation's P50 has moved from 13 to <b>20 September</b>.</p>""",
    how_figs=[ir_how],
    steps=[("Turn each response action into a task", "In the plan, not only the register."),
           ("Give it an owner inside the organisation", "Suppliers do; your people own."),
           ("Write what “done” means", "And the date."),
           ("Put triggers in the status", "With a named watcher."),
           ("Review implementation, not just scores", "Done, due, nearest trigger."),
           ("Say what a late action cost", "In days, in odds, at the next steering group.")],
    vocab=[("Implement risk responses", "Carrying out the agreed responses as planned work."),
           ("Risk action", "One task that carries out part of a response."),
           ("Action owner", "The person inside the organisation who makes sure the action happens."),
           ("Trigger", "A date or sign that says a risk is starting, or a response is late."),
           ("Watcher", "The person who checks a trigger and acts when it's hit."),
           ("Handover", "The point where work passes from one person or organisation to another.")],
    code=dict(file="antwerp/14-response-actions.md", note="Sanne, risk review of Friday 2 April 2027 and after", plain=True, src="""
# ANTWERP · R-07 RESPONSE ACTIONS                         review Fri 2 Apr 2027

ACTION                         OWNER (WAS → NOW)              DUE      DONE
Hilde starts (agent)           Sanne                          8 Mar    8 Mar  ✓
Informal meeting with the city Sanne                          11 Mar   11 Mar ✓
640 m² layout to the supplier  - → Tomás's layout lead        (none)   6 Apr  (was missing)
Cooling drawings               "cooling supplier" → Sanne     15 Mar   9 Apr  ✗ 3½ weeks
Application lodged             Hilde (Sanne watches)          26 Mar   19 Apr ✗
TRIGGER "not lodged by 26 Mar" watcher: nobody → Sanne, in the Friday status

RULES FROM 2 APR  every action a task in the plan (owner, date, done) · every owner
                  at Larder · every trigger in the Friday status with a watcher
REVIEW ASKS       done since last time? · due next? · nearest trigger?
COST (to steering group, 7 May)  inquiry 24 May–22 Jun (was early May) · P50 13 → 20 Sep
"""),
    tools="tools: the plan, an owner column that only takes your own people's names, the Friday status, and three questions.",
    dial=[("Light", "small work", ["Each risk action on the to-do list.", "Named, dated.", "Checked weekly."]),
          ("Standard", "Antwerp", ["Actions as tasks with Larder owners.", "Triggers in the status with watchers.", "Reviews ask done, due, nearest trigger."]),
          ("Heavy", "large programmes", ["Risk actions in the schedule with earned value.", "Action owners report at each review.", "Audit of response implementation."])],
    baseline="Each line compares <b>responses written on the register with a supplier as owner</b> to <b>actions as planned tasks, owners inside Larder and triggers with watchers</b>.",
    ratings=[(3, 4, "Responses actually happen."),
             (2, 3, "Late actions show up in days and odds."),
             (2, 4, "Dropped handovers found at the next review."),
             (2, 4, "Triggers are in the status everyone reads."),
             (3, 3, "Femke heard the cost plainly; trust held."),
             (3, 4, "Owners own the actions."),
             (3, 3, "Neutral."),
             (3, 3, "Neutral."),
             (3, 3, "Minutes per review.")],
    pitfalls=[("Supplier as owner", "Nobody of yours watches.", "an owner inside the organisation."),
              ("Actions only on the register", "Not in anyone's week.", "make them tasks in the plan."),
              ("Triggers without watchers", "Dates nobody looks at.", "name a watcher, show it in the status."),
              ("Reviews that re-score only", "Scores move; nothing gets done.", "ask what was done.")],
    use=["As soon as responses are agreed.", "At every risk review.", "When work passes to a supplier or agent.", "When a trigger date approaches."],
    skip=["Never; it's what makes the register worth having."],
    related=["<b>What Do We Do About It?</b> (previous note)", "<b>What's in the Way Right Now?</b> (vol. 2)", "<b>Is the Work Actually Happening?</b> (vol. 2)", "<b>Dependencies across Teams</b> (Grace, vol. 5)"],
    quiz=[("What were Sanne's three rules from 2 April?", "Actions as tasks in the plan; owners at Larder; triggers in the Friday status with a watcher."),
          ("Why were the drawings late?", "The supplier was waiting for Larder's layout; the owner was outside Larder; nobody at Larder knew."),
          ("What did the delay cost?", "Lodged 3½ weeks late; inquiry 24 May–22 Jun; P50 from 13 to 20 September."),
          ("An agent says “leave it with me”. What do you still do?", "Name a Larder owner, put the agent's steps in the plan with dates, and put the trigger in the status."),
          ("At a review, a red risk's score hasn't changed for six weeks. What's the first question?", "What was done since last time? A steady score may mean nothing has been done.")],
    try_it="For each response in your register, find the task in your plan that carries it out. If there isn't one, create it with an owner from your own organisation and a date.",
    remember="The plan names the <span class=\"hl\">runners</span>. The race is the <span class=\"hl\">handovers</span>.",
    sources=["Project Management Institute, <i>PMBOK Guide</i>, Eighth Edition (2025): Risk domain, implementing risk responses.",
             "Project Management Institute, <i>PMBOK Guide</i>, Sixth Edition (2017): 11.6 Implement Risk Responses.",
             "Tom DeMarco and Timothy Lister, <i>Waltzing with Bears</i> (2003)."],
)

# ------------------------------------------------------------------ 15 Is the List Still True?
rm_problem = Doodle(760, 260, "Doodle of Thursday 15 July 2027. The city's case officer phones Hilde: fourteen objections in the inquiry, about lorries before seven and condenser noise. Larder must change the hours or bring a noise study, and there will be no decision before September. R-07 is no longer something that might happen. It has happened.",
                    "15 July: fourteen objections, no decision before September. R-07 has stopped being a risk.", exact=True)
rm_problem.box(20, 24, 330, 140, None, "y")
rm_problem.head(185, 60, "risk register", size=19)
rm_problem.text(185, 94, "R-07 · 12 · might happen", size=16)
rm_problem.text(185, 122, "contingency, a trigger", size=16)
rm_problem.box(410, 24, 330, 140, None, "pink")
rm_problem.head(575, 60, "15 July", size=19)
rm_problem.text(575, 94, "14 objections", size=16)
rm_problem.text(575, 122, "no decision before Sep", size=16)
rm_problem.arrow(352, 94, 406, 94, color="red")
rm_problem.note(380, 210, "a risk that has happened is an issue", "red", size=19)
rm_problem.note(380, 242, "and an issue needs a decision this week, not a score", "pen", size=16)

rm_analogy = Doodle(760, 250, "Doodle of a weather forecast and a burst pipe. The forecast says forty percent chance of frost tonight: that's a risk, so you lag the pipes and leave the heating on low. In the morning water is coming through the ceiling: that's an issue, so you turn off the water and call the plumber. Same pipe, different list.",
                    "“40 % chance of frost” is a risk: lag the pipes. Water through the ceiling is an issue: turn off the water.", exact=True)
rm_analogy.box(14, 40, 350, 100, "risk: frost tonight?", "blue", sub="lag the pipes, heat on low", size=17, subsize=14)
rm_analogy.box(396, 40, 350, 100, "issue: water coming in", "pink", sub="stop the water, call the plumber", size=17, subsize=14)
rm_analogy.arrow(366, 90, 392, 90)
rm_analogy.note(380, 190, "same pipe, different list, different speed", "pen", size=19)

rm_how = Doodle(760, 470, "From risk to issue to lesson, July to October 2027. Thursday 15 July: the case officer's call; R-07 closed as a risk and opened as issue I-12, owner Sanne. Friday 23 July, an extra steering group with three options. A: wait and hope for an August decision; rejected. B: amend the application now, deliveries from seven only and an acoustic screen on the condenser, and open on Monday 18 October; chosen by Femke. C: open with dry goods only; rejected by Lena for food safety. Cost: twenty-seven thousand euros in the project, from the last fourteen thousand of contingency and thirteen of the management reserve; outside it, rent and lost orders. Monday 6 September: permit granted. Monday 18 October: open. October: four lines into playbook v3.",
                "Risk → issue (15 Jul) → decision (23 Jul) → permit (6 Sep) → open (18 Oct) → four lines in playbook v3.", exact=True)
rm_how.row([("15 Jul", "R-07 → issue I-12", "pink"), ("23 Jul", "option B chosen", "y"), ("6 Sep", "permit granted", "green"), ("18 Oct", "open", "green")], y=14, h=78, size=17, subsize=13, gap=34, arrows=True)
rm_how.box(14, 110, 732, 140, None, "paper")
rm_how.head(380, 138, "the steering group of Friday 23 July", size=17)
rm_how.text(30, 170, "A wait for an August decision: odds poor — rejected", anchor="start", size=15)
rm_how.text(30, 198, "B amend now: deliveries from 07:00, acoustic screen → open Mon 18 Oct — CHOSEN", anchor="start", size=15)
rm_how.text(30, 226, "C open with dry goods only: food safety, customers — rejected (Lena)", anchor="start", size=15)
rm_how.box(14, 266, 360, 190, None, "pink")
rm_how.head(194, 294, "what it cost", size=17)
for i, t in enumerate(["project: €27k", "contingency 14 → 0", "mgmt reserve 15 → 2", "outside: ≈ €10k rent", "+ ≈ €75k of orders"]):
    rm_how.text(194, 326 + i * 26, t, size=14)
rm_how.box(386, 266, 360, 190, None, "green")
rm_how.head(566, 294, "playbook v3 (Oct)", size=17)
for i, t in enumerate(["regulators are stakeholders", "score risks with locals", "every response: our owner", "price a week late: ≈ €17k"]):
    rm_how.text(566, 330 + i * 30, t, size=14)

MONITOR_R = dict(
    slug="risk-monitoring",
    kicker="a.k.a. “risks vs issues”: monitoring risks, closing them, and handing them to the issue log",
    tldr="<b>Monitor risks</b> on a rhythm: at each review ask what's <b>new</b>, what has <b>changed</b>, which responses are <b>done</b>, which <b>triggers</b> are close, and which risks can be <b>closed</b>. A <b>risk</b> might happen; an <b>issue</b> has happened. When a risk happens, close it on the register and open it on the <b>issue log</b>, with an owner and a decision date this week; the reserve and the fallback plan you prepared are now for spending. At the end, turn what the list taught you into lessons the next project will trip over.",
    chips=[("Family", "doing something about it"), ("Lives in", "the fortnightly risk review, the issue log, the lessons"), ("Pairs with", "the risk register, the issue log, escalation, lessons learned")],
    pmbok=dict(covers="reviewing risks on a rhythm, tracking triggers and responses, closing risks, turning risks that happen into issues, and recording what was learned",
               domains=RISK + ["governance"], processes=["Monitor Risks"], principles=["Be an accountable leader", "Adopt a holistic view"], focus=["monitoring and controlling", "closing"],
               older="6th: “Monitor Risks” (11.7), risk reviews and audits, reserve analysis. 7th: the Uncertainty and Measurement domains."),
    problem_side="Antwerp, Thursday 15 July 2027",
    problem="""  <p class="lead">The public inquiry closed on 22 June with <b>fourteen objections</b>: lorries before seven, condenser noise. On <b>Thursday 15 July</b> the city's case officer phones Hilde. Larder must either change the delivery hours or bring an independent noise study, and either way <span class="hl-pink">there will be no decision before September</span>. The planning date is 13 September; the cold room needs the permit before it can be installed. R-07 sits on the register at 12, with a contingency and a trigger. It is no longer something that might happen. It has happened.</p>
  <ul>
    <li>A risk that happens needs a decision, not a score.</li>
    <li>The reserve and the fallbacks are now for spending.</li>
    <li>The rest of the register still needs watching.</li>
  </ul>""",
    problem_figs=[rm_problem],
    meanwhile=[("product-6", "launching-new-city", "Grace's city playbook: v1 Utrecht (April), v2 The Hague (June), v3 after Antwerp (October), each version changed by the last launch.",
                "Sanne's four lines from Antwerp go into playbook v3: regulators as stakeholders, risks scored with locals, a Larder owner for every response, and the price of a week late.")],
    analogy_side="frost and the burst pipe",
    analogy="""  <p>The forecast says <b>40 % chance of frost</b> tonight. That's a risk: you lag the pipes and leave the heating on low. In the morning there's <b>water coming through the ceiling</b>. That's an issue: you turn off the water and call the plumber, now. It's the same pipe on a different list, and the second list moves much faster.</p>""",
    analogy_figs=[rm_analogy],
    map=[("The forecast", "The risk register: R-07, might happen"),
         ("Lagging the pipes", "The responses: agent, early meeting, drawings"),
         ("Water through the ceiling", "15 July: no decision before September"),
         ("Turning off the water", "Issue I-12, a decision on 23 July"),
         ("Next winter's checklist", "Four lines in playbook v3")],
    how_side="close the risk, open the issue, decide, spend, learn",
    how="""  <p>That afternoon Sanne <b>closes R-07 as a risk</b> and opens <b>issue I-12</b>, owner Sanne, decision needed by the end of next week. It's over every threshold, so Femke calls an extra steering group for <b>Friday 23 July</b> with three options. <b>A</b>: wait for an August decision; the odds are poor. <b>B</b>: amend the application now, with deliveries <b>from 07:00 only</b> (Koen agrees a 07:00 drop) and an <b>acoustic screen</b> on the condenser, and plan the opening for <b>Monday 18 October</b>. <b>C</b>: open in September with dry goods only; Lena rejects it on food safety, and customers would get half a store. Femke chooses <b>B</b>: half of the avoid option rejected in February, five months later and five weeks too late. The cost inside the project is <b>€27k</b> (staff starts held €11k, marketing re-booked €9k, the installer re-booked €4k, the screen €3k), from the last €14k of contingency and €13k of Femke's management reserve. Outside it, about €10k of rent and, by Marco's sum, about €75k of orders. In the last week of July Sanne and Inès knock on every door in the street with the new hours. The permit is granted on <b>Monday 6 September</b>, the cold room is in and tested by the 17th, the food-safety visit is on the 29th, and Antwerp opens on <b>Monday 18 October</b>: 2.4 tickets per 100 orders in week one, better than Utrecht's 2.9. Forecast final cost <b>€457k</b> of €465k. In October Sanne writes four lines into <b>playbook v3</b>.</p>""",
    how_figs=[rm_how],
    steps=[("Review on a rhythm", "New, changed, done, near triggers, closable."),
           ("Read the low rows too", "Who scored them, and would they still?"),
           ("When a risk happens, move it", "Close it as a risk, open it as an issue."),
           ("Decide fast, with options", "Over a threshold: to the sponsor, this week."),
           ("Spend the reserve you prepared", "And report what's left."),
           ("Turn the list into lessons", "Into the playbook, not a folder.")],
    vocab=[("Risk", "Something that might happen."),
           ("Issue", "Something that has happened and needs action."),
           ("Risk review", "A regular meeting to update risks, responses and triggers."),
           ("Reserve analysis", "Comparing the reserve left with the risk left."),
           ("Closing a risk", "Taking it off the active list because it has passed or happened."),
           ("Risk audit", "A check that the risk process itself is working.")],
    code=dict(file="antwerp/15-risk-to-issue.md", note="Sanne, 15 July → October 2027", plain=True, src="""
# ANTWERP · R-07 → I-12, AND WHAT WE LEARNED

15 Jul  R-07 CLOSED as a risk (happened) · I-12 OPENED: no permit decision before Sep,
        14 objections (lorries before 07:00, condenser noise) · owner Sanne · decide by 23 Jul
23 Jul  STEERING GROUP (extra)
        A wait for an August decision ............................. rejected (odds)
        B amend: deliveries from 07:00, acoustic screen, open 18 Oct  CHOSEN (Femke)
        C open with dry goods only ................................ rejected (Lena)
        COST in project €27k = staff starts 11 + marketing 9 + installer 4 + screen 3
             contingency 14 → 0 (earlier: hiring 4, translation rework 2)
             management reserve 15 → 2
             outside: rent ≈ €10k (operations) · ≈ €75k contribution (5 weeks × €15k)
26-30 Jul door to door with the new hours (Sanne, Inès)
6 Sep   permit granted · 17 Sep cold room tested · 29 Sep food-safety visit
18 Oct  OPEN · week 1: 2.4 tickets per 100 · forecast final cost €457k of €465k

RISK vs ISSUE   might happen → register, response, reserve · has happened → issue log,
                owner, decision this week

PLAYBOOK v3 (Oct 2027)
 1 regulators are stakeholders: "manage closely" until the permit is granted
 2 score risks with people who have done it in that country
 3 every response action has an owner at Larder and a trigger with a watcher
 4 price a week late in every appetite statement: ≈ €15k contribution + ≈ €2k rent
"""),
    tools="tools: the register, a fortnightly hour, the issue log, a steering group that can meet at a week's notice, and the playbook.",
    dial=[("Light", "small work", ["Look at the risk list each week.", "Move what happened to the to-do list.", "One lesson at the end."]),
          ("Standard", "Antwerp", ["Fortnightly review: new, changed, done, triggers, closed.", "Risks that happen become issues.", "Reserve left reported; lessons into the playbook."]),
          ("Heavy", "large programmes", ["Risk audits.", "Reserve analysis against quantified exposure.", "Risk reports to portfolio boards."])],
    baseline="Each line compares <b>a register that keeps scoring a risk that has happened</b> to <b>a review that closes it, opens an issue, decides within a week and writes the lesson down</b>.",
    ratings=[(3, 4, "The launch was saved for October, not lost."),
             (2, 3, "The new date held: 18 October."),
             (2, 4, "Reserves and fallbacks were ready to spend."),
             (2, 5, "Risk, issue and cost are all on the page."),
             (2, 4, "Femke decided with options in eight days."),
             (3, 4, "Inès joined the door-to-door."),
             (3, 4, "Option B was ready because avoid had been studied."),
             (3, 4, "The next launch inherits four lines."),
             (3, 3, "An hour a fortnight.")],
    pitfalls=[("Scoring an issue", "It happened; act.", "move it to the issue log."),
              ("Waiting for the next review", "A week lost.", "a happened risk is decided this week."),
              ("Reserve spent quietly", "Nobody sees what's left.", "report reserve left with risk left."),
              ("Lessons in a folder", "The next city repeats it.", "write them into the playbook.")],
    use=["Fortnightly through the project.", "When a trigger is hit.", "When a risk happens.", "At closing: the lessons."],
    skip=["Never; on small work it's a glance at the list each week."],
    related=["<b>What's in the Way Right Now?</b> (vol. 2)", "<b>When Do I Take It Upstairs?</b> (vol. 2)", "<b>What Did We Learn?</b> (vol. 2)", "<b>Launching a New City</b> (Grace, vol. 6)"],
    quiz=[("What's the difference between a risk and an issue?", "A risk might happen; an issue has happened and needs action."),
          ("What happened to R-07 on 15 July?", "Closed as a risk, opened as issue I-12, decision by 23 July."),
          ("Which option did Femke choose, and why was it ready?", "B: deliveries from 07:00 and a screen; it had been studied as the avoid option in February."),
          ("A risk's trigger is hit on a Tuesday; the next review is in nine days. What do you do?", "Act now: treat it as an issue, tell the owner and, if over a threshold, the sponsor, with options."),
          ("What did Antwerp cost, inside and outside the project?", "€27k inside (contingency and management reserve); about €10k rent and €75k of orders outside.")],
    try_it="At your next review, ask of every risk: has it happened? If yes, move it to the issue log with an owner and a decision date this week. Then write one lesson your next project should start with.",
    remember="Frost is a <span class=\"hl\">risk</span>. Water through the ceiling is an <span class=\"hl\">issue</span>.",
    sources=["Project Management Institute, <i>PMBOK Guide</i>, Eighth Edition (2025): Risk domain, monitoring risks.",
             "Project Management Institute, <i>PMBOK Guide</i>, Sixth Edition (2017): 11.7 Monitor Risks.",
             "Project Management Institute, <i>Practice Standard for Project Risk Management</i> (2009): risk reviews and audits."],
)

NOTES = [RESPONSES, IMPLEMENT, MONITOR_R]
