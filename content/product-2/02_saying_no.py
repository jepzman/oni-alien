# Series 2 · Book 2 · The Product Owner's Notebook · Vol. 2 · Saying no.
# Narrator: Grace. Running case study: Larder (facts in docs/larder-casebook.md).

# ------------------------------------------------------------------ 05 Saying No Without Burning Bridges
sn_problem = Doodle(760, 280, "Doodle of a timeline. November 2025: Grace parks Femke's recipe idea quietly, without telling her clearly. 24 February 2026: at a board meeting an investor asks again where the recipe ideas are. Femke turns to Grace. A quiet no came back as a public surprise.",
                    "A quiet “not now” in November came back as a public question in February.")
sn_problem.line("M40 120 H720")
sn_problem.box(40, 40, 230, 60, "Nov: parked", "paper", sub="quietly, no message", dash=True)
sn_problem.box(300, 140, 230, 60, "24 Feb: board", "y", sub="“where are the recipes?”")
sn_problem.box(540, 40, 200, 60, "Femke", "pink", sub="“Grace?”", stroke="red")
sn_problem.arrow(270, 70, 300, 150, dash=True)
sn_problem.arrow(530, 150, 560, 100, color="red")
sn_problem.note(380, 254, "a no nobody heard isn't a no", "red")

sn_analogy = Doodle(760, 260, "Doodle of a good waiter. Not tonight: the fish is off. Here's why: it didn't come in fresh. May I suggest: the lamb is excellent. Back on Friday: ask me then. The guest leaves happy without the fish.",
                    "A good waiter says no to the fish, and the guest still leaves happy.")
sn_analogy.icon("menu", 30, 60, 1.6)
for i, (t, s, f) in enumerate([("not tonight", "the fish is off", "pink"), ("here's why", "not fresh today", "paper"), ("may I suggest", "the lamb", "green"), ("on Friday", "ask me again", "y")]):
    x = 130 + i * 156
    sn_analogy.box(x, 70, 146, 84, t, f, sub=s, size=16, subsize=14)
sn_analogy.note(440, 222, "no · reason · instead · a date", "pen")

sn_how = Doodle(760, 330, "Grace's five-part no to Femke about recipe ideas, 25 February 2026. One: thank and restate the idea. Two: the outcome and the evidence: no outcome on the tree, 62 percent of customers indifferent, a RICE score of 1,500. Three: what we're doing instead: the no-swaps flag is live, approvals reach Amsterdam in mid-April. Four: a small yes: marketing tries three recipe links in the weekly newsletter for four weeks. Five: when we'll look again: Q3 planning in July.",
                "Five parts: restate, reason with evidence, what instead, a small yes, a date. The no is clear; the door stays open.")
for i, (t, s, f) in enumerate([("1 · restate", "“recipes from the basket”", "paper"), ("2 · the reason", "62 % indifferent · RICE 1,500", "y"), ("3 · instead", "flag live · approvals Apr", "blue")]):
    x = 14 + i * 248
    sn_how.box(x, 20, 236, 90, t, f, sub=s, size=17, subsize=14)
    if i < 2:
        sn_how.arrow(x + 238, 65, x + 248, 65)
for i, (t, s, f) in enumerate([("4 · a small yes", "3 links in the newsletter, 4 wks", "green"), ("5 · look again", "Q3 planning, July", "y")]):
    x = 136 + i * 248
    sn_how.box(x, 150, 236, 90, t, f, sub=s, size=17, subsize=14)
sn_how.arrow(374, 195, 382, 195)
sn_how.note(380, 280, "sent in writing, the day after the board", "pen", size=18)
sn_how.note(380, 310, "result, late March: 2.1 % clicked, 0.3 % added to basket → parked", "green", size=16)

SAYING_NO = dict(
    slug="saying-no",
    kicker="a.k.a. “the fish is off tonight”",
    tldr="A product owner says no far more often than yes. A good no is <b>clear</b> (no “maybe later” that means never), <b>explained</b> with the outcome and the evidence, offers <b>what you're doing instead</b>, often includes a <b>small yes</b> (a cheap test, a manual workaround), and sets <b>when you'll look again</b>. Say it <b>in writing</b>, to the person, before they hear it from someone else. A quiet “parked” comes back louder.",
    chips=[("Family", "saying no"), ("Origin", "product practice; Steve Jobs, “focus is about saying no” (WWDC, 1997); Marty Cagan on stakeholder management"), ("Lives in", "a short message, linked from the parked list"), ("Pairs with", "opportunity solution tree, Kano model, request triage")],
    problem_side="Larder, 24 February 2026",
    problem="""  <p class="lead">In November Grace parked Femke's <b>recipe ideas</b> on her opportunity tree. She mentioned it in a stand-up; she never told Femke clearly. At the February board meeting, an investor asks where the recipe ideas are. Femke, surprised, turns to Grace in front of the board. The no was right; <span class="hl-pink">the way it was said wasn't</span>, and it cost Femke a moment of looking uninformed.</p>
  <ul>
    <li>Quiet parking feels kinder; it just postpones the conversation, often to a worse moment.</li>
    <li>“Maybe later” without a date sounds like yes to the asker.</li>
    <li>A no without reasons feels like a judgement on the person, not the idea.</li>
  </ul>""",
    problem_figs=[sn_problem],
    analogy_side="the good waiter",
    analogy="""  <p>A good waiter doesn't pretend the fish is coming. <b>“Not tonight”</b>, clearly. <b>“It didn't come in fresh”</b>, a reason. <b>“May I suggest the lamb?”</b>, something instead. <b>“It's back on Friday”</b>, a date. The guest doesn't get the fish and still leaves happy, and comes back on Friday.</p>""",
    analogy_figs=[sn_analogy],
    map=[("“Not tonight”", "A clear no: recipe ideas aren't on the Q2 plan"),
         ("“It didn't come in fresh”", "The reason: no outcome served, 62 % indifferent"),
         ("“May I suggest the lamb”", "What we're doing instead: the flag, approvals"),
         ("A taste from the kitchen", "A small yes: newsletter recipe links for four weeks"),
         ("“Back on Friday”", "When we'll look again: Q3 planning, July")],
    how_side="clear, explained, and with a door left open",
    how="""  <p>Grace wrote to Femke the next morning, in five short paragraphs, and offered to brief the investor herself. The <b>small yes</b> mattered: marketing put three recipe links in the weekly newsletter for four weeks. By late March the numbers were in: 2.1 % clicked, 0.3 % added an item. Femke shared them with the investor herself. Recipes stayed parked, and nobody was surprised.</p>""",
    how_figs=[sn_how],
    steps=[("Say it soon, to the person", "Before a meeting, in writing, not via the grapevine."),
           ("Restate the idea fairly", "Show you understood it, in the asker's terms."),
           ("Give the reason with evidence", "The outcome it doesn't serve, the data, the score."),
           ("Say what you're doing instead", "The work that won, and what it'll achieve."),
           ("Offer a small yes", "A cheap test, a workaround, an owner elsewhere, or a link to their goal."),
           ("Set a date", "When and how you'll look again; put it in the parked list.")],
    vocab=[("Parked", "Not now, with a reason and a review date."),
           ("Declined", "Not planned, with a reason; ask again if things change."),
           ("Small yes", "A cheap way to serve part of the request."),
           ("Review date", "When a parked idea gets looked at again."),
           ("Disagree and commit", "Accepting a decision you argued against."),
           ("Stakeholder", "Anyone who can affect, or is affected by, the product.")],
    code=dict(file="product/messages/2026-02-25-recipes.md", note="Grace's message to Femke, 25 February 2026", plain=True, src="""
To: Femke    Subject: Recipe ideas: where they stand, and a small test

Hi Femke, sorry you were put on the spot yesterday. I should have told you
clearly in November. Here's where it stands.

The idea   Suggest recipes from what's in the basket, to grow basket size.
Why not now  Our Q2 outcome is refund tickets 6 % → 2 %. Recipes don't serve it,
           and in our Kano survey 62 % of customers were indifferent to them
           (212 answers). RICE: 1,500, against 15,200 for approvals.
Instead    The "no swaps" flag went live on 23 Feb; approvals reach Amsterdam
           in mid-April. Both target the refunds that cost us ~€45k a month.
Small yes  Marketing can add 3 recipe links to the weekly newsletter for 4 weeks.
           If more than 5 % click and 1 % add an item, recipes come back in Q3.
Next look  Q3 planning, first week of July. I'm happy to brief the investor.

Grace
"""),
    tools="tools: a short written message, and a public “parked” list with reasons and review dates (a page in the product wiki, or a column on the board).",
    gains=["<b>No surprises</b> for senior stakeholders.",
           "<b>Focus protected</b> without damaging relationships.",
           "<b>Ideas get a fair test</b> through the small yes.",
           "<b>Fewer repeat requests</b>: the reason and date are on record.",
           "<b>Trust grows</b>: people learn your no is reasoned."],
    losses=["<b>Uncomfortable</b>: writing a no to the CEO is hard.",
            "<b>Small yeses cost something</b>: marketing's time.",
            "<b>Not every no lands well</b>, even done right.",
            "<b>Takes time</b>: 30 minutes per message."],
    baseline="Each line compares <b>parking ideas quietly or saying “maybe later”</b> to <b>a clear written no with the reason, what instead, a small yes and a review date</b>.",
    ratings=[(3, 4, "The team keeps working on what customers need."),
             (3, 4, "Focus stays on the outcome that matters."),
             (2, 4, "The no is backed by data, and the small yes adds more."),
             (2, 4, "The small yes tests the idea in weeks, cheaply."),
             (2, 5, "One outcome, one plan, defended clearly."),
             (2, 4, "Everyone knows what's parked and why."),
             (2, 5, "Stakeholders hear it first, with reasons."),
             (3, 3, "Doesn't change delivery flow."),
             (3, 3, "Half an hour per message.")],
    pitfalls=[("The quiet park", "Nobody tells the asker; it comes back at the board.", "say it to the person, in writing, soon."),
              ("“Maybe later”", "No date, so the asker hears yes.", "a clear no now, and a dated review."),
              ("No reason", "“It's not a priority.”", "the outcome and the evidence, in one or two sentences."),
              ("All or nothing", "Either the full feature or nothing.", "look for a small yes that tests the idea cheaply.")],
    use=["Ideas from senior stakeholders that don't fit the outcome.",
         "Requests that have been parked quietly too long.",
         "Before a meeting where the idea may come up.",
         "Any no that will be repeated to others."],
    skip=["Tiny requests: a one-line answer in triage is enough.",
          "When you're actually unsure: say so and test it."],
    related=["<b>Handling the HiPPO</b> (this volume)", "<b>Feature request triage</b> (this volume)", "<b>Kano model</b> (this volume)", "<b>Outcomes over outputs</b> (Vol. 1)"],
    quiz=[("Name the five parts of a good no.", "Restate the idea, the reason with evidence, what instead, a small yes, a date to look again."),
          ("Why is quiet parking risky?", "The asker doesn't know; it comes back at a worse moment, often in public."),
          ("What's a small yes?", "A cheap way to serve or test part of the request, like newsletter links for four weeks."),
          ("Why put it in writing?", "It's clear, can be forwarded, and the reason and date are on record.")],
    try_it="Find one idea you've parked without telling the asker clearly. Write them five short paragraphs: restate, reason, instead, a small yes, a review date. Send it before your next meeting with them.",
    remember="“The fish is <span class=\"hl\">off</span> tonight. May I suggest the lamb? Back on <span class=\"hl\">Friday</span>.”",
    sources=["Marty Cagan, <i>Inspired</i>, 2nd ed. (2017), on stakeholder management.",
             "Melissa Perri, <i>Escaping the Build Trap</i> (2018).",
             "William Ury, <i>The Power of a Positive No</i> (2007).",
             "Steve Jobs, Apple Worldwide Developers Conference (1997): “focus is about saying no”."],
)

# ------------------------------------------------------------------ 06 Handling the HiPPO
hp_problem = Doodle(760, 280, "Doodle of Femke, back from a meeting with Korenwolf in March 2026, asking for a big Larder for Business banner at the top of the app's home screen so everyone sees it. The team says nothing. Dee starts building it that afternoon.",
                    "The most senior person says “put it at the top”. Nobody asks what it might cost.")
hp_problem.icon("crown", 50, 30, 1.0)
hp_problem.box(20, 100, 200, 70, "Femke", "y", sub="CEO")
hp_problem.arrow(226, 135, 330, 135, label="“at the top!”", lx=278, ly=121)
hp_problem.icon("phone", 340, 70, 2.0)
hp_problem.box(368, 90, 50, 22, None, "pink", rx=3)
for i, t in enumerate(["Ben: …", "Dee: starts building", "Grace: …"]):
    hp_problem.box(500, 30 + i * 70, 240, 54, t, "paper", size=16)
hp_problem.note(380, 262, "nobody asks: what does it cost the shop?", "red")

hp_analogy = Doodle(760, 260, "Doodle of an airline cockpit. The captain has decided to land. The first officer sees the fuel reading and speaks up with a standard phrase: I'm concerned, here's what I see, I suggest we check. The instruments, not rank, decide.",
                    "In a cockpit, the first officer speaks up with the instruments; rank doesn't land the plane.")
hp_analogy.box(20, 40, 210, 80, "captain", "y", sub="“we land now”")
hp_analogy.box(20, 150, 210, 80, "first officer", "blue", sub="reads the gauges")
for i, t in enumerate(["“I'm concerned…”", "“…the fuel reads 900 kg”", "“…I suggest we check”"]):
    hp_analogy.box(300, 30 + i * 66, 300, 50, t, "paper", size=16)
hp_analogy.icon("stopwatch", 650, 90, 1.2)
hp_analogy.note(380, 248, "concern · data · a proposal", "green")

hp_how = Doodle(760, 320, "Grace's test of Femke's banner, 10 to 17 March 2026. Hypothesis: a home-screen banner brings office leads without hurting orders. 10 percent of app users saw the banner. Group A without banner: 9.5 percent of sessions became an order. Group B with banner: 9.1 percent, and 3 office leads. Across all users that would be about 4 percent fewer orders. Decision with Femke: the banner moves to the account menu and the newsletter; leads go to Mo.",
                "Turn the opinion into a hypothesis, test it with a guardrail, and let Femke read the result herself.")
hp_how.icon("phone", 70, 20, 2.0)
hp_how.box(20, 150, 200, 76, "A · no banner", "paper", sub="9.5 % order", size=17)
hp_how.icon("phone", 330, 20, 2.0)
hp_how.box(358, 40, 50, 22, None, "pink", rx=3)
hp_how.box(280, 150, 200, 76, "B · banner, 10 %", "y", sub="9.1 % · 3 leads", size=17)
hp_how.box(530, 40, 216, 186, None, "green", rx=10)
hp_how.head(638, 76, "decided together", size=16)
for i, t in enumerate(["account menu", "+ newsletter", "+ leads → Mo"]):
    hp_how.text(638, 116 + i * 30, t, size=16)
hp_how.note(250, 268, "−0.4 pp ≈ 4 % fewer orders if shown to all", "red", size=18)
hp_how.note(380, 304, "hypothesis · guardrail · one week · read together", "pen", size=18)

HIPPO = dict(
    slug="hippo",
    kicker="a.k.a. “the first officer reads the gauges”",
    tldr="The <b>HiPPO</b> is the Highest Paid Person's Opinion: in many rooms it wins by default. Don't fight the person; <b>change the question</b> from “who's right?” to “how would we know?”. Restate the idea as a <b>hypothesis</b>, add a <b>guardrail</b> metric (what mustn't get worse), run the <b>smallest test</b> that answers it, and <b>read the result together</b>. Senior people usually like evidence; what they dislike is being blocked.",
    chips=[("Family", "saying no"), ("Origin", "“HiPPO” coined by Avinash Kaushik (2007); experimentation practice at Microsoft (Ronny Kohavi)"), ("Lives in", "a hypothesis card and a one-week test"), ("Pairs with", "testable hypotheses, saying no, A/B tests")],
    problem_side="Larder, 10 March 2026",
    problem="""  <p class="lead">Femke comes back from a follow-up meeting with Korenwolf full of energy: Larder for Business should be <b>a big banner at the top of the app's home screen</b>, “so everyone sees it”. Nobody in the room objects. Dee starts building it that afternoon. Grace isn't against business customers, but the home screen is where <b>consumer orders start</b>, and <span class="hl-pink">nobody has asked what the banner costs</span> the shop.</p>
  <ul>
    <li>Rank decides, because disagreeing with the CEO feels risky.</li>
    <li>The idea's cost (here, attention on the home screen) is invisible.</li>
    <li>A flat refusal would make it a battle; quietly building it makes it a gamble.</li>
  </ul>""",
    problem_figs=[hp_problem],
    analogy_side="the cockpit",
    analogy="""  <p>Airlines learned this the hard way. In the cockpit, the <b>first officer</b> is trained to speak up to the captain with a standard pattern: <b>“I'm concerned”</b>, <b>what the instruments say</b>, and <b>a proposal</b>. It isn't insubordination; it's the job. The instruments decide, and good captains want to hear it.</p>""",
    analogy_figs=[hp_analogy],
    map=[("The captain's call", "Femke's banner, at the top"),
         ("The instruments", "Conversion and leads, measured"),
         ("“I'm concerned, the fuel reads…”", "Grace naming the risk to orders, with the number"),
         ("“I suggest we check”", "A one-week test with 10 % of users"),
         ("Landing safely together", "Femke and Grace reading the result and deciding")],
    how_side="from opinion to hypothesis",
    how="""  <p>Grace went to Femke the same day: <i>“I love that we want offices to see it. I'm worried the home screen costs us consumer orders. Can we show it to 10 % for a week and look together?”</i> Femke agreed at once. The result: orders down <b>0.4 points</b> in the banner group, about 4 % if shown to everyone, for <b>3 leads</b>. Femke made the call herself: account menu, newsletter, and leads straight to Mo.</p>""",
    how_figs=[hp_how],
    steps=[("Agree with the goal", "Start with what's right about it: “offices should know about this”."),
           ("Name your concern", "One sentence, the specific risk: “the home screen is where orders start”."),
           ("Write the hypothesis", "“A home-screen banner brings office leads without reducing orders.”"),
           ("Add a guardrail", "The metric that mustn't get worse (order conversion), with a threshold."),
           ("Run the smallest test", "10 % of users for a week; or a fake door; or five interviews."),
           ("Read it together", "Show the senior person the result first and let them decide.")],
    vocab=[("HiPPO", "Highest Paid Person's Opinion."),
           ("Hypothesis", "A testable statement: we believe X will cause Y."),
           ("Guardrail metric", "A number that must not get worse during a test."),
           ("Holdout", "Users who don't see the change, for comparison."),
           ("Conversion", "Share of sessions that end in an order."),
           ("Speaking up", "Raising a concern to a senior person, with data and a proposal.")],
    code=dict(file="product/tests/2026-03-business-banner.md", note="test card, 10–17 March 2026", plain=True, src="""
# Test: Larder for Business banner on the home screen

Idea (Femke)   A large banner at the top of the app's home screen.
Hypothesis     The banner brings office leads without reducing consumer orders.
Guardrail      Order conversion (sessions → order) must not drop more than 0.2 pp.
Success        ≥ 10 qualified office leads in one week.
Design         10 % of app users see the banner, 90 % don't · 10–17 Mar · Dee

Result         A (no banner)   9.5 % of sessions → order
               B (banner)      9.1 % of sessions → order   (−0.4 pp: guardrail broken)
               Leads           3 (two under 40 staff)
               If shown to all: ≈ 4 % fewer orders ≈ 1,100 orders a week.

Decision       With Femke, 18 Mar: the banner moves to the account menu and the
               monthly newsletter; leads go straight to Mo. Banner code removed.
"""),
    tools="tools: a feature flag with percentage rollout (Unleash, LaunchDarkly, Statsig) and your analytics tool; for a smaller test, a fake door or five customer interviews.",
    gains=["<b>No battle</b>: the question becomes “how would we know?”.",
           "<b>Costs become visible</b>: here, 4 % of orders.",
           "<b>Senior people keep authority</b> and decide on evidence.",
           "<b>Team members speak up</b> when there's a safe pattern.",
           "<b>Good HiPPO ideas get through faster</b>, with proof."],
    losses=["<b>Not every idea can be tested</b> in a week.",
            "<b>Takes courage</b> to raise the concern.",
            "<b>A test costs something</b>: a week of 10 % of users.",
            "<b>Some HiPPOs don't want data</b>: then it's an escalation."],
    baseline="Each line compares <b>building whatever the most senior person asks</b> to <b>restating it as a hypothesis with a guardrail, testing it small and reading the result together</b>.",
    ratings=[(3, 4, "The home screen keeps serving the people who order."),
             (2, 5, "4 % of orders saved, measured."),
             (1, 5, "Data, not rank, decides."),
             (2, 4, "One week to an answer."),
             (2, 4, "The team builds what the evidence supports."),
             (2, 4, "Everyone sees why the banner moved."),
             (2, 5, "Femke decides herself, on the result."),
             (3, 3, "A short test; little effect on flow."),
             (3, 3, "A test card and a week of data.")],
    pitfalls=[("Fighting the person", "“That's a bad idea.”", "agree with the goal, question the method."),
              ("Building it quietly", "Dee ships the banner; nobody measures.", "every senior idea gets a hypothesis and a guardrail."),
              ("No guardrail", "Leads go up; nobody checks orders.", "name the metric that mustn't get worse."),
              ("Reading results alone", "Grace presents “Femke was wrong”.", "read it together, let them make the call.")],
    use=["A senior stakeholder's idea with a hidden cost.",
         "When the room goes quiet after the boss speaks.",
         "Ideas that touch high-traffic screens or flows.",
         "Any opinion that can be tested in a week."],
    skip=["Strategic calls that are the leader's to make (which city next).",
          "Legal or safety requirements: not up for testing."],
    related=["<b>Saying no without burning bridges</b> (this volume)", "<b>Testable hypotheses</b> (Vol. 1)", "<b>Fake door test</b> (Vol. 1)", "<b>Decision rights (RACI/DACI)</b> (Ana, book 1 vol. 2)"],
    quiz=[("What does HiPPO stand for?", "Highest Paid Person's Opinion."),
          ("How do you change the question?", "From “who's right?” to “how would we know?”: a hypothesis and a test."),
          ("What's a guardrail metric?", "A number that mustn't get worse during the test, like order conversion."),
          ("Why read the result together?", "So the senior person decides on the evidence and keeps their authority.")],
    try_it="Think of the last idea that went ahead because a senior person liked it. Write it as a hypothesis, add one guardrail metric with a threshold, and design a one-week test. Next time a similar idea comes up, bring the card to the conversation.",
    remember="Agree with the <span class=\"hl\">goal</span>. Test the <span class=\"hl\">method</span>. Read the gauges together.",
    sources=["Avinash Kaushik, <i>Web Analytics: An Hour a Day</i> (2007), on the HiPPO.",
             "Ronny Kohavi, Diane Tang, Ya Xu, <i>Trustworthy Online Controlled Experiments</i> (2020).",
             "FAA / ICAO, Crew Resource Management training, on speaking up.",
             "Amy Edmondson, <i>The Fearless Organization</i> (2018)."],
)

# ------------------------------------------------------------------ 07 Opportunity Cost
oc_problem = Doodle(760, 280, "Doodle of Mo, who joined in March 2026, asking Grace's team to build office ordering in the app for the Korenwolf pilot: just four weeks for Ben's team. It looks free because the team is already there. Hidden underneath: approvals in Amsterdam slip from mid-April to mid-May, and the Rotterdam musts are at risk.",
                    "“Just four weeks” looks free. The price is what those four weeks would otherwise have done.")
oc_problem.box(20, 30, 300, 80, "Mo", "y", sub="“just 4 weeks for Ben's team”")
oc_problem.arrow(326, 70, 420, 70)
oc_problem.box(426, 30, 314, 80, "office ordering", "blue", sub="for the Korenwolf pilot")
oc_problem.box(110, 160, 540, 76, None, "pink", stroke="red", dash=True)
oc_problem.text(380, 192, "approvals in Amsterdam: mid-April → mid-May", size=16)
oc_problem.text(380, 220, "Rotterdam musts: no slack left", size=16)
oc_problem.note(380, 266, "the hidden price", "red")

oc_analogy = Doodle(760, 250, "Doodle of a Saturday calendar. A friend asks for help moving house on Saturday. Saying yes looks free, but Saturday is also the kids' football final. Every yes is a no to the next best thing.",
                    "Helping a friend move on Saturday costs the kids' football final. The cost of a yes is the next best thing.")
oc_analogy.icon("calendar", 40, 50, 1.6)
oc_analogy.note(85, 170, "Saturday", "pen")
oc_analogy.box(220, 40, 240, 70, "help a friend move", "y", sub="“it's only a day”", size=16)
oc_analogy.box(500, 40, 240, 70, "the football final", "green", sub="the next best thing", size=16)
oc_analogy.arrow(340, 116, 340, 160)
oc_analogy.box(220, 164, 520, 50, "the real cost of yes = missing the final", "pink", size=16)

oc_how = Doodle(760, 320, "Grace's comparison, 25 March 2026. Saying yes to Mo: four weeks of office ordering, then approvals, which reach Amsterdam in mid-May. The next best use: approvals reach Amsterdam on 13 April. The difference is four weeks of avoidable refunds, about 30,000 euros, plus the Rotterdam musts losing their slack. A cheaper yes for Mo: run the pilot by hand, about three hours a week of support, decided with Ana on 13 April.",
                "Compare the yes with the next best use of the same weeks. Then look for a cheaper yes.")
oc_how.head(20, 50, "yes to Mo", anchor="start", size=16)
oc_how.box(160, 26, 240, 40, "office ordering · 4 wks", "blue", size=14, rx=4)
oc_how.box(406, 26, 240, 40, "approvals → mid-May", "y", size=14, rx=4)
oc_how.head(20, 120, "next best", anchor="start", size=16)
oc_how.box(160, 96, 240, 40, "approvals → 13 Apr", "green", size=14, rx=4)
oc_how.line("M400 86 V146", dash=True, color="red")
oc_how.line("M646 86 V146", dash=True, color="red")
oc_how.arrow(400, 156, 646, 156, color="red", both=True)
oc_how.note(523, 184, "4 weeks ≈ €30k of refunds", "red", size=17)
oc_how.box(110, 214, 540, 64, "a cheaper yes: the pilot by hand", "green", sub="≈ 3 h a week of support · with Ana, 13 Apr", size=16)
oc_how.note(380, 306, "price every yes in what it pushes out", "pen", size=17)

OPP_COST = dict(
    slug="opportunity-cost",
    kicker="a.k.a. “Saturday is also the football final”",
    tldr="A team's weeks are fixed; every yes spends some of them. The real cost of a yes isn't its effort, it's the <b>next best thing those weeks would have done</b>: its <b>opportunity cost</b>. Before agreeing to a request, name that next best thing and <b>price the delay</b> it would suffer. Often the honest answer isn't yes or no but a <b>cheaper yes</b>: a manual version, a smaller slice, a later date.",
    chips=[("Family", "saying no"), ("Origin", "economics: Friedrich von Wieser (1914); in product, Marty Cagan, Teresa Torres and others"), ("Lives in", "a one-paragraph comparison in the reply to a request"), ("Pairs with", "cost of delay, saying no, options analysis")],
    problem_side="Larder, 25 March 2026",
    problem="""  <p class="lead">Mo joined in March to look after Larder for Business. The Korenwolf pilot starts on <b>4 May</b>, and Mo asks Grace for <b>office ordering in the app</b>: “just four weeks for Ben's team”. Four weeks feels small, and the team is right there. But Ben's team is building approvals for Amsterdam (13 April) and the Rotterdam musts (done by 20 April). <span class="hl-pink">The four weeks aren't free</span>; they'd come out of something.</p>
  <ul>
    <li>Requests are judged by their own effort, not by what they push out.</li>
    <li>The work pushed out has no advocate in the room.</li>
    <li>Saying no outright to a colleague's first big request damages a new relationship.</li>
  </ul>""",
    problem_figs=[oc_problem],
    meanwhile=[("architect-2", "options-analysis", "Grace's opportunity-cost sum is why “do it by hand” got a fair hearing in this matrix.", "Grace brought the price of “just four weeks” to this meeting: about €30k of delayed approvals.")],
    analogy_side="the Saturday",
    analogy="""  <p>A friend asks you to help them move on Saturday. “It's only a day.” But Saturday is also the <b>kids' football final</b>. The day of lifting boxes isn't the cost; <b>missing the final</b> is. Seeing that, you might find a <b>cheaper yes</b>: help on Sunday morning, or lend them your van.</p>""",
    analogy_figs=[oc_analogy],
    map=[("Helping a friend move", "Building office ordering for the pilot"),
         ("The football final", "Approvals in Amsterdam on 13 April"),
         ("Missing the final", "≈ €30k of avoidable refunds, Rotterdam without slack"),
         ("Lending the van instead", "A cheaper yes: the pilot by hand"),
         ("“It's only a day”", "“Just four weeks”")],
    how_side="name the next best thing, price it",
    how="""  <p>Grace didn't say no to Mo. She showed him the comparison: four weeks of office ordering would push approvals to mid-May, about <b>€30,000</b> of refunds, and leave Rotterdam with no slack. Then she offered a cheaper yes: run the twelve-week pilot by hand. Mo and Grace took both options to Ana's options analysis on 13 April, where “by hand” won.</p>""",
    how_figs=[oc_how],
    steps=[("Ask what the weeks would replace", "Look at the plan: which item moves if this one comes in?"),
           ("Price the delay", "Use its cost of delay: €/week × weeks of delay."),
           ("Add the non-money costs", "Slack lost on a fixed date, a promise broken, a team switched mid-flow."),
           ("Compare openly", "Put the request and the next best use side by side for the asker."),
           ("Look for a cheaper yes", "By hand, smaller, later, or someone else's team."),
           ("Decide with the asker", "Or with whoever owns both, if it's not your call.")],
    vocab=[("Opportunity cost", "The value of the best alternative you give up."),
           ("Next best use", "What the same time would otherwise have done."),
           ("Capacity", "The team's available weeks; fixed in the short term."),
           ("Cheaper yes", "A smaller or manual way to meet the request."),
           ("Sunk cost", "Time already spent; irrelevant to the next decision."),
           ("Trade-off", "Giving up some of one thing to get more of another.")],
    code=dict(file="product/messages/2026-03-25-office-ordering.md", note="Grace's reply to Mo, 25 March 2026", plain=True, src="""
To: Mo   Subject: Office ordering for the Korenwolf pilot: the real price

Your ask    Office ordering in the app, ready for the pilot on 4 May (~4 weeks, Ben's team).

If we say yes, these move:
  Approvals in Amsterdam   13 Apr → mid-May    ≈ €30k of avoidable refunds
  Rotterdam musts          lose their slack     launch on 27 Apr at risk

A cheaper yes
  Run the 12-week pilot by hand: support enters one standing order a week
  (~3 h/week), you send the invoice from a sheet. No code, no risk to checkout.
  If Korenwolf signs for more offices, we build business ordering properly.

Next step   Ana is running an options analysis on 13 Apr; let's bring both.
"""),
    tools="tools: the roadmap and cost-of-delay sheet you already have; a short written comparison. For bigger asks, Ana's options analysis (book 1, vol. 2).",
    gains=["<b>Hidden costs become visible</b>, in euros.",
           "<b>The pushed-out work gets an advocate</b>.",
           "<b>Cheaper yeses</b> instead of flat refusals.",
           "<b>Better relationships</b>: the asker sees the trade-off.",
           "<b>Plans stay intact</b> on fixed dates."],
    losses=["<b>Estimates are rough</b>; the comparison can be disputed.",
            "<b>Takes time</b> to write, for every big ask.",
            "<b>The asker may still escalate</b>.",
            "<b>Cheaper yeses cost someone</b> (support's hours)."],
    baseline="Each line compares <b>judging a request by its own effort</b> to <b>pricing what it pushes out, and offering a cheaper yes</b>.",
    ratings=[(3, 4, "Customers keep the fix that was already coming."),
             (2, 5, "≈ €30k of delay avoided, with a working pilot."),
             (2, 4, "Delay priced from the cost-of-delay sheet."),
             (3, 3, "Neutral on learning speed."),
             (2, 5, "The plan stays on its two big outcomes."),
             (2, 4, "Mo sees what the four weeks would replace."),
             (2, 4, "A new colleague gets a yes, just a cheaper one."),
             (2, 4, "No mid-flow switch for Ben's team."),
             (3, 3, "A short written comparison per big ask.")],
    pitfalls=[("Effort only", "“It's only four weeks.”", "ask what those four weeks would otherwise do."),
              ("No price", "“Approvals would slip.” So what?", "put a euro figure on the slip."),
              ("Flat no", "Mo hears no in his first month.", "offer a cheaper yes."),
              ("Deciding alone", "Grace overrules Mo on a business question.", "bring both options to whoever owns the trade-off.")],
    use=["Any request that needs real team time.",
         "Requests from new or senior colleagues.",
         "When a plan has a fixed date nearby.",
         "When “we're here anyway” is the argument."],
    skip=["Tiny requests: triage handles them.",
          "When the team has genuine spare capacity (rare)."],
    related=["<b>Cost of delay</b> (this volume)", "<b>Saying no without burning bridges</b> (this volume)", "<b>Feature request triage</b> (this volume)", "<b>Options analysis</b> (Ana, book 1 vol. 2)"],
    quiz=[("What is opportunity cost?", "The value of the next best thing the same time or money would have done."),
          ("How did Grace price Mo's request?", "Four weeks of delayed approvals at about €30k, plus Rotterdam losing its slack."),
          ("What's a cheaper yes?", "A smaller, manual or later way to meet the request, like running the pilot by hand."),
          ("Why compare openly with the asker?", "They see the trade-off themselves and can help decide.")],
    try_it="Take the next request that needs more than a week of your team's time. Write down what it would push out, put a euro figure on that delay, and propose one cheaper yes. Send it to the asker as three short paragraphs.",
    remember="The price of a yes is the <span class=\"hl\">football final</span> you'll miss. Look for the <span class=\"hl\">cheaper yes</span>.",
    sources=["Friedrich von Wieser, <i>Social Economics</i> (1914), on opportunity cost.",
             "Donald Reinertsen, <i>The Principles of Product Development Flow</i> (2009).",
             "Marty Cagan, <i>Empowered</i> (2020).",
             "Shreyas Doshi, on the LNO framework and opportunity cost (2020–22)."],
)

# ------------------------------------------------------------------ 08 Feature Request Triage
rt_problem = Doodle(760, 280, "Doodle of requests arriving at Grace from everywhere in January and February 2026: Slack messages, corridor chats, emails and stand-ups. Forty-seven requests, none written down in one place. Sam asks three times about the auto-refund button. Nobody gets a clear answer.",
                    "Forty-seven requests through five doors. Sam asks three times; nobody hears back.")
for i, t in enumerate(["Slack DMs", "corridor", "email", "stand-up", "lunch"]):
    rt_problem.box(20, 20 + i * 46, 160, 38, t, "paper", size=15, rx=6)
    rt_problem.arrow(186, 39 + i * 46, 380, 130, dash=True)
rt_problem.box(386, 90, 180, 80, "Grace's head", "y")
rt_problem.box(600, 40, 140, 70, "Sam", "pink", sub="asked 3×", stroke="red")
rt_problem.note(380, 264, "47 requests · no list · no answers", "red")

rt_analogy = Doodle(760, 260, "Doodle of an emergency room triage nurse. Everyone who walks in is seen within minutes and sorted: now, soon, later, or a GP instead. Not everyone is treated at once, but everyone knows where they stand.",
                    "At A&E everyone is seen quickly and sorted. Not everyone is treated now, but everyone knows where they stand.")
rt_analogy.icon("badge", 40, 60, 1.5)
rt_analogy.box(20, 170, 130, 50, "triage", "y", size=17)
for i, (t, f) in enumerate([("now", "pink"), ("soon", "y"), ("later", "blue"), ("see your GP", "paper")]):
    rt_analogy.arrow(156, 195, 220, 40 + i * 52, dash=True)
    rt_analogy.box(226, 20 + i * 52, 200, 42, t, f, size=16, rx=6)
rt_analogy.note(600, 120, "everyone knows", "green", size=20)
rt_analogy.note(600, 150, "where they stand", "green", size=20)

rt_how = Doodle(760, 330, "Grace's triage from 2 March 2026. One front door: a short request form posted to one channel. Every Monday, a 30-minute triage with Ben and Dee. Four outcomes, with the counts for the 47 backlog requests: joins an existing opportunity, 9; a quick fix under a day, 6; parked with a review date, 21; declined with a reason, 11. Every requester hears back within a week, and the list is public.",
                "One front door, thirty minutes on Mondays, four possible answers, and everyone hears back within a week.")
rt_how.box(20, 120, 150, 70, "one form", "y", sub="one channel")
rt_how.arrow(176, 155, 230, 155)
rt_how.box(236, 110, 160, 90, "Monday", "blue", sub="30 min, Ben + Dee")
for i, (t, n, f) in enumerate([("joins an opportunity", "9", "green"), ("quick fix (< 1 day)", "6", "green"), ("parked, review date", "21", "y"), ("declined, with reason", "11", "paper")]):
    y = 20 + i * 66
    rt_how.arrow(402, 155, 458, y + 26, dash=True)
    rt_how.box(462, y, 230, 52, t, f, size=15, rx=6)
    rt_how.text(722, y + 34, n, "t-head", size=22)
rt_how.note(380, 310, "every requester hears back within a week · list is public", "green", size=18)

TRIAGE = dict(
    slug="request-triage",
    kicker="a.k.a. “the triage nurse”",
    tldr="Requests reach a product owner through a dozen doors: chat, corridors, email, meetings. Give them <b>one front door</b> (a short form or a single channel), look at everything new in a <b>short weekly triage</b>, and give each request one of <b>four answers</b>: it <b>joins an existing opportunity</b>, it's a <b>quick fix</b> done this week, it's <b>parked with a review date</b>, or it's <b>declined with a reason</b>. Everyone hears back <b>within a week</b>, and the list is <b>public</b>.",
    chips=[("Family", "saying no"), ("Origin", "service-desk and support triage practice; product intake processes"), ("Lives in", "a form, a channel and a public list"), ("Pairs with", "saying no, opportunity solution tree, opportunity cost")],
    problem_side="Larder, 2 March 2026",
    problem="""  <p class="lead">Since January, requests have reached Grace through Slack messages, corridor chats, emails, stand-ups and lunch: <b>47 of them</b> by the end of February, from Sam, Joost, Tomás, Priya, Femke and the team. Grace answered each one in her head. Nobody else could see them. <b>Sam</b> asked about his auto-refund button <span class="hl-pink">three times</span>; <b>Tomás</b> waited six weeks for a one-line font-size change on the picker screen.</p>
  <ul>
    <li>Requests through many doors get lost or answered inconsistently.</li>
    <li>Askers don't know where they stand, so they ask again, louder.</li>
    <li>Tiny fixes wait as long as big features.</li>
  </ul>""",
    problem_figs=[rt_problem],
    analogy_side="the triage nurse",
    analogy="""  <p>In an emergency room, everyone who walks in is <b>seen within minutes</b> by a triage nurse and sorted: <b>now</b>, <b>soon</b>, <b>later</b>, or <b>see your GP</b> instead. Not everyone is treated at once, and some are sent elsewhere. But <b>nobody sits in the waiting room wondering</b> if anyone knows they're there.</p>""",
    analogy_figs=[rt_analogy],
    map=[("The front desk", "One form, one channel"),
         ("The triage nurse", "Grace with Ben and Dee, 30 minutes on Mondays"),
         ("Now", "A quick fix, under a day, this week"),
         ("Soon / later", "Joins an opportunity, or parked with a review date"),
         ("“See your GP”", "Declined, with a reason, or sent to another team")],
    how_side="one door, one weekly look, four answers",
    how="""  <p>The first triage cleared the 47-request backlog in 90 minutes: <b>9</b> joined existing opportunities, <b>6</b> were quick fixes (Tomás's font size shipped that week), <b>21</b> were parked with review dates and <b>11</b> declined with a reason. After that, Mondays took 30 minutes. Sam's button? Parked, with a link to the approvals work that makes most of his refunds unnecessary, and he could see that on the list.</p>""",
    how_figs=[rt_how],
    steps=[("Open one front door", "A five-field form (who, what, why, how often, how urgent) posting to one channel."),
           ("Redirect the other doors", "Kindly: “can you drop that in the form? I'll answer by Monday.”"),
           ("Triage weekly, briefly", "30 minutes with a tech lead and a designer; every new request gets one of four answers."),
           ("Four answers only", "Joins an opportunity · quick fix (< 1 day) · parked with a review date · declined with a reason."),
           ("Answer within a week", "Reply to the asker with the answer and a link."),
           ("Keep the list public", "Anyone can see every request, its answer and its date.")],
    vocab=[("Front door", "The one place requests come in."),
           ("Triage", "Sorting requests quickly into a few outcomes."),
           ("Quick fix", "Something under a day, done this week."),
           ("Parked", "Not now, with a reason and a review date."),
           ("Declined", "Won't do, with a reason."),
           ("Service level", "The promise: an answer within a week.")],
    code=dict(file="product/requests/README.md", note="request form and triage rules, from 2 March 2026", plain=True, src="""
# Requests for ordering & the customer apps          triage: Mondays 10:00, 30 min

The form (posts to #ordering-requests)
  Who's asking · What's the problem (not the solution) · Who has it, how often ·
  What happens today instead · Any deadline?

Four answers, within a week
  JOINS     an existing opportunity on the tree → linked, the asker is told which
  QUICK FIX under a day of work → done this week
  PARKED    not now, with a reason and a review date
  DECLINED  not planned, with a reason (or sent to the right team)

First triage, 2 Mar: 47 requests → 9 joined · 6 quick fixes · 21 parked · 11 declined
  R-14 Picker screen font size (Tomás)        QUICK FIX   shipped 4 Mar
  R-22 Auto-refund button (Sam)               PARKED      approvals should remove most
                                                          swap refunds; review 1 Jun
  R-31 Recipe ideas (Femke)                   PARKED      see message 25 Feb; review Jul
  R-40 Dark mode in the app                   DECLINED    no outcome now; ask again in Q4
"""),
    tools="tools: a form (Google Forms, Typeform, Jira Service Management, Linear's request intake, Productboard's portal) posting to one channel, and a public list or board.",
    gains=["<b>Nothing lost</b>: every request is written down.",
           "<b>Everyone hears back</b> within a week.",
           "<b>Quick fixes ship quickly</b> instead of waiting.",
           "<b>Fewer repeat asks</b>: the answer is public.",
           "<b>Patterns show up</b>: many requests point to one opportunity."],
    losses=["<b>A weekly habit</b> to keep up.",
            "<b>Redirecting people to a form</b> feels bureaucratic at first.",
            "<b>Public declines</b> can sting.",
            "<b>Quick fixes can crowd out</b> planned work if not capped."],
    baseline="Each line compares <b>requests through many doors, answered from memory</b> to <b>one front door, a weekly 30-minute triage, four possible answers within a week, on a public list</b>.",
    ratings=[(3, 4, "Small pains (Tomás's font) get fixed in days."),
             (3, 3, "Mostly protects focus; little direct impact."),
             (2, 4, "Requests counted: patterns become evidence."),
             (2, 4, "Problems surface weekly, not when they escalate."),
             (2, 4, "Most requests are parked or declined, visibly."),
             (2, 4, "Anyone can see what was asked and decided."),
             (2, 5, "Everyone gets an answer within a week."),
             (2, 4, "Quick fixes flow; big asks join the tree."),
             (3, 3, "30 minutes a week, plus replies.")],
    pitfalls=[("Many doors stay open", "Requests still arrive in DMs and get answered there.", "kindly redirect every one to the form."),
              ("Triage becomes planning", "Monday's 30 minutes turns into two hours of debate.", "four answers only; debate belongs elsewhere."),
              ("Silent parking", "“Parked” with no reason or date.", "every park gets a reason and a review date."),
              ("Quick fixes unbounded", "Twenty one-day fixes a week.", "cap quick fixes, e.g. two days of team time a week.")],
    use=["When requests reach you through many channels.",
         "When people ask the same thing repeatedly.",
         "Teams serving many internal stakeholders.",
         "After a busy period, to clear a backlog of asks."],
    skip=["Very small teams with one or two stakeholders.",
          "Incidents and bugs: they have their own process."],
    related=["<b>Saying no without burning bridges</b> (this volume)", "<b>Opportunity cost</b> (this volume)", "<b>Opportunity solution tree</b> (Vol. 1)", "<b>Decision log</b> (Ana, book 1 vol. 2)"],
    quiz=[("What are the four triage answers?", "Joins an existing opportunity, quick fix, parked with a review date, declined with a reason."),
          ("How fast should askers hear back?", "Within a week."),
          ("Why keep the list public?", "Askers see where they stand without asking again, and patterns become visible."),
          ("What should the form ask for?", "The problem, who has it and how often, not just the solution.")],
    try_it="Collect every request you've received in the last month from chat, email and memory onto one list. Give each one of the four answers in a 45-minute session with a tech lead, and send every asker a one-line reply this week. Then set up the form.",
    remember="One <span class=\"hl\">front door</span>. Thirty minutes on Mondays. Everyone knows <span class=\"hl\">where they stand</span>.",
    sources=["Marty Cagan, <i>Inspired</i>, 2nd ed. (2017), on stakeholder requests.",
             "ITIL 4, “Service request management” practice.",
             "Teresa Torres, <i>Continuous Discovery Habits</i> (2021), on mapping requests to opportunities.",
             "Intercom, <i>Intercom on Product Management</i> (2016), on feature requests."],
)

NOTES = [SAYING_NO, HIPPO, OPP_COST, TRIAGE]
