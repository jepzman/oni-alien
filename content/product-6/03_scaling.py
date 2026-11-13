# Series 2 · Book 2 · The Product Owner's Notebook · Vol. 6 · Scaling the product.
# Narrator: Grace. Running case study: Larder (facts in docs/larder-casebook.md).

# ------------------------------------------------------------------ 08 Platform Thinking
pt_problem = Doodle(760, 280, "Doodle of July 2027. Substitution logic now lives in three places: the consumer app's approvals, the business standing orders, and Larder Plus's never-swap preferences. Each team changed it separately; a rule fixed in one place stayed broken in another, and the picker app received three slightly different kinds of swap instruction.",
                    "Swap rules in three places, changed separately. Pickers get three kinds of instruction.")
for i, (t, f) in enumerate([("consumer approvals", "y"), ("business orders", "blue"), ("Plus preferences", "green")]):
    pt_problem.box(20 + i * 250, 40, 220, 80, t, f, size=15)
pt_problem.note(380, 200, "one capability, three copies", "red", size=20)

pt_analogy = Doodle(760, 250, "Doodle of a town's water supply: every house once had its own well, each tested differently. A shared waterworks with a published standard, a team that runs it and a tap in every house means every house gets the same safe water, and nobody digs a well.",
                     "Every house its own well, or one waterworks with a standard, a team, and a tap in every house.")
pt_analogy.icon("bucket", 40, 60, 1.3)
pt_analogy.box(170, 50, 270, 90, "a well each", "pink", sub="tested differently")
pt_analogy.box(470, 50, 270, 90, "one waterworks", "green", sub="a standard, a team, taps")
pt_analogy.note(450, 205, "the same safe water for all", "pen")

pt_how = Doodle(760, 400, "Grace's substitution platform from 19 July 2027. One capability, owned by one team, Ben's, with a documented interface: offer a swap, record the answer, apply rules such as never-swap flags, allergens and price limits, tell the picker. Its customers are internal: the consumer app, the business portal, Plus, the picker app. Its own outcomes: swap answers within the window, wrong swaps packed per thousand orders. A rule now changes once, everywhere. Three copies retired by October.",
                 "One owned capability with an interface, its own customers and outcomes. A rule changes once, everywhere.")
pt_how.box(200, 14, 360, 90, "substitution platform", "green", sub="Ben's team · documented API", size=17)
for i, t in enumerate(["consumer app", "business portal", "Larder Plus", "picker app"]):
    x = 14 + i * 184
    pt_how.box(x, 150, 174, 60, t, "y", size=15)
    pt_how.arrow(x + 87, 146, 380, 108)
pt_how.box(14, 236, 732, 50, "outcomes: answered in window · wrong swaps per 1,000", "blue", size=15)
pt_how.note(380, 326, "a rule changes once, everywhere · 3 copies retired by Oct", "pen", size=15)

PLATFORM = dict(
    slug="platform-thinking",
    kicker="a.k.a. “one waterworks”",
    tldr="When several products need the same capability, copies drift apart and every change happens three times. <b>Platform thinking</b> turns that capability into one <b>owned</b>, <b>documented</b> internal product with its own <b>customers</b> (the other teams) and its own <b>outcomes</b>. Do it when the capability is truly shared and stable enough; don't build a platform for something only one product needs.",
    chips=[("Family", "scaling the product"), ("Origin", "platform product management; Team Topologies' platform teams"), ("Lives in", "an owned team, a documented interface, and internal customers"), ("Pairs with", "golden paths (Ana), operations as a customer, bounded contexts (Ana)")],
    problem_side="Larder, 19 July 2027",
    problem="""  <p class="lead">Substitution logic now lives in <b>three places</b>: the consumer app's approvals, the business standing orders, and Larder Plus's never-swap preferences. Each team changed it separately; a rule fixed in one place stayed broken in another, and the picker app received <span class="hl-pink">three slightly different kinds of swap instruction</span>.</p>
  <ul>
    <li>Copies of a capability drift apart.</li>
    <li>Every rule change has to be made several times.</li>
    <li>Nobody owns the capability as a whole.</li>
  </ul>""",
    problem_figs=[pt_problem],
    analogy_side="one waterworks",
    analogy="""  <p>Every house in a town once had <b>its own well</b>, each tested differently. A shared <b>waterworks</b> with a published standard, a team that runs it and a <b>tap in every house</b> means every house gets the same safe water, and nobody digs a well again.</p>""",
    analogy_figs=[pt_analogy],
    map=[("A well per house", "Swap logic copied in three products"),
         ("The waterworks", "The substitution platform"),
         ("The published standard", "A documented interface"),
         ("The team that runs it", "Ben's team"),
         ("A tap in every house", "Consumer app, portal, Plus, picker app")],
    how_side="one owner, an interface, internal customers, outcomes",
    how="""  <p>Grace made substitutions a <b>platform</b>: one capability, owned by <b>Ben's team</b>, with a documented interface: offer a swap, record the answer, apply rules (never-swap flags, allergens, price limits), tell the picker. Its <b>customers</b> are internal: the consumer app, the business portal, Plus and the picker app. Its own <b>outcomes</b>: answers within the window, wrong swaps per 1,000 orders. A rule now changes <b>once, everywhere</b>; the three copies were retired by October.</p>""",
    how_figs=[pt_how],
    steps=[("Find the shared capability", "Used by several products, copied or about to be."),
           ("Check it's stable enough", "Its core rules shouldn't change weekly."),
           ("Give it an owner", "One team, with a product owner's eye."),
           ("Define the interface", "Documented, versioned, easy to use."),
           ("Treat other teams as customers", "Roadmap, support, feedback."),
           ("Give it outcomes", "And retire the copies.")],
    vocab=[("Platform", "A shared capability other products build on."),
           ("Internal customer", "Another team that uses your platform."),
           ("Interface", "How others use the platform (an API)."),
           ("Platform team", "The team that owns and runs it."),
           ("Self-service", "Teams use it without asking the platform team."),
           ("Duplication", "The same logic in several places.")],
    code=dict(file="product/platforms/substitutions.md", note="the platform charter, July 2027", plain=True, src="""
# Substitution platform · charter · 19 Jul 2027 · owner: Ben's team · PO: Grace

Does     offer a swap · record the customer's answer · apply rules (never-swap flags, allergens,
         price limit, business account settings) · send the instruction to the picker app
Doesn't  choose suggestions (Catalogue: similarity ranking) · refunds (Payments)
Interface  documented API + events (swap.offered, swap.answered, swap.applied), versioned
Customers  consumer app · business portal + standing orders · Larder Plus · picker app
Outcomes   answered within the window ≥ 85 % · wrong swaps packed ≤ 1 per 1,000 orders
Copies retired  consumer app rules (Aug) · business orders (Sep) · Plus preferences (Oct)
"""),
    tools="tools: a documented API and events, a platform team, an internal roadmap and support channel, usage metrics per internal customer.",
    gains=["<b>One change</b>, everywhere.",
           "<b>Consistent</b> for customers and pickers.",
           "<b>Clear ownership</b>.",
           "<b>Faster new products</b> on top.",
           "<b>Its own outcomes</b>."],
    losses=["<b>A team</b> dedicated to it.",
            "<b>Dependencies</b> for other teams.",
            "<b>Interface design</b> takes care.",
            "<b>Too early</b> and it fits nobody."],
    baseline="Each line compares <b>a capability copied into several products</b> to <b>one owned platform with an interface, internal customers and outcomes</b>.",
    ratings=[(2, 4, "Customers see the same swap rules everywhere."),
             (2, 4, "New products reuse it."),
             (2, 4, "Outcomes measured once, for all."),
             (2, 4, "One change to test, not three."),
             (1, 5, "Three copies gone."),
             (2, 4, "One place to understand swaps."),
             (2, 4, "Joost's pickers get one kind of instruction."),
             (2, 4, "Products build on it quickly."),
             (3, 3, "A team to run it.")],
    pitfalls=[("Platform too early", "Built for one user.", "wait until it's truly shared."),
              ("No owner", "Everyone's, so nobody's.", "one team."),
              ("Hard to use", "Teams copy it again.", "a simple, documented interface."),
              ("Copies kept", "Old logic lingers.", "retire them on a date.")],
    use=["Capabilities used by several products.",
         "When copies drift and bugs repeat.",
         "Before launching another product that needs it.",
         "Growing product organisations."],
    skip=["Capabilities only one product needs."],
    related=["<b>Golden paths</b> (Ana, book 1 vol. 6)", "<b>Operations as a customer</b> (Vol. 5)", "<b>Bounded contexts</b> (Ana, book 1 vol. 1)", "<b>Writing product principles</b> (this volume)"],
    quiz=[("When does a capability deserve a platform?", "When several products need it and its rules are stable enough."),
          ("Who are the platform's customers?", "Internal teams: consumer app, portal, Plus, picker app."),
          ("What outcomes does it have?", "Answers within the window; wrong swaps per 1,000 orders."),
          ("What changed?", "A rule changes once, everywhere; three copies retired.")],
    try_it="Find one piece of logic that exists in more than one of your products. List where it lives and how the copies differ, and sketch who would own it as a platform and what its interface would be.",
    remember="Build the <span class=\"hl\">waterworks</span>; stop digging <span class=\"hl\">wells</span>.",
    sources=["Matthew Skelton and Manuel Pais, <i>Team Topologies</i> (2019).",
             "Evan Bottcher, “What I Talk About When I Talk About Platforms” (martinfowler.com, 2018).",
             "Marty Cagan, <i>Empowered</i> (2020), platform teams.",
             "Geoffrey Parker et al., <i>Platform Revolution</i> (2016)."],
)

# ------------------------------------------------------------------ 09 Accessibility as Product Quality
ac_problem = Doodle(760, 280, "Doodle of August 2027. A customer who uses a screen reader writes to Sam: the swap screen reads the countdown every second, and the three-minute window runs out before she can answer. An audit finds 41 issues. The European Accessibility Act has applied to online shops since June 2025; Larder has been out of line for two years without noticing.",
                    "A screen-reader user can't answer a swap before the timer ends. An audit finds 41 issues.")
ac_problem.box(20, 40, 320, 90, "the swap timer", "pink", sub="read aloud every second", stroke="red")
ac_problem.box(400, 40, 340, 90, "audit", "y", sub="41 issues")
ac_problem.note(380, 200, "built for some, not for everyone", "red", size=20)

ac_analogy = Doodle(760, 250, "Doodle of a building with a ramp, wide doors and a lift designed in from the start: easier for wheelchairs, but also for parents with pushchairs, delivery workers and anyone with a sprained ankle. Adding them later costs far more.",
                     "A ramp and wide doors designed in: better for wheelchairs, pushchairs, deliveries and sprained ankles.")
ac_analogy.icon("door", 40, 60, 1.3)
for i, (t, f) in enumerate([("wheelchairs", "y"), ("pushchairs", "blue"), ("deliveries", "green")]):
    ac_analogy.box(170 + i * 190, 60, 176, 70, t, f, size=16)
ac_analogy.note(450, 200, "designed in, not bolted on", "pen")

ac_how = Doodle(760, 400, "Grace's accessibility work from 16 August 2027. Fix the worst first: the swap timer announces only at one minute and at the end, and customers can ask for more time, which meets the timing rule. Then the other 40 issues by priority, with Noor. Test with five customers with disabilities, paid. Make it part of quality: accessibility checks in the definition of done, automated checks in CI, a screen-reader test before each release. By November: all 41 fixed; the extend option is used by 6 percent of all customers, not only screen-reader users.",
                 "Worst first, real users, then part of done. All 41 fixed; 6 % of everyone uses “more time”.")
for i, (t, s, f) in enumerate([("timer", "announce less · “more time”", "pink"), ("40 more", "by priority, with Noor", "y"), ("5 users", "with disabilities, paid", "blue")]):
    ac_how.box(14 + i * 248, 14, 236, 100, t, f, sub=s, size=17, subsize=13)
ac_how.box(14, 136, 732, 56, "definition of done · CI checks · screen-reader test per release", "green", size=14)
ac_how.box(14, 212, 360, 70, "41 issues", "green", sub="all fixed by November", size=16)
ac_how.box(386, 212, 360, 70, "“more time”", "green", sub="used by 6 % of everyone", size=16)
ac_how.note(380, 322, "accessibility as quality, not a project", "pen", size=16)

ACCESS = dict(
    slug="accessibility",
    kicker="a.k.a. “the ramp at the front door”",
    tldr="<b>Accessibility</b> means people with disabilities can use the product as well as anyone. Treat it as <b>product quality</b>, not a one-off project: fix the worst barriers first, <b>test with real disabled users</b>, and build it into the <b>definition of done</b>, automated checks and release tests. The law (in the EU, the European Accessibility Act and WCAG-based standards) is the minimum; the gains usually help everyone.",
    chips=[("Family", "scaling the product"), ("Origin", "WCAG (W3C); European Accessibility Act (applies from June 2025)"), ("Lives in", "the definition of done, CI checks and release tests"), ("Pairs with", "definitions of ready and done, prototype testing with users, compliance by design (Ana)")],
    problem_side="Larder, 16 August 2027",
    problem="""  <p class="lead">A customer who uses a <b>screen reader</b> writes to Sam: the swap screen reads the countdown aloud <b>every second</b>, and the three-minute window runs out before she can answer. An audit finds <b>41 issues</b>. The European Accessibility Act has applied to online shops since <b>June 2025</b>; <span class="hl-pink">Larder has been out of line for two years without noticing</span>.</p>
  <ul>
    <li>Teams don't notice barriers they don't experience.</li>
    <li>Time limits and visual-only cues exclude people.</li>
    <li>Fixing late costs more than building in.</li>
  </ul>""",
    problem_figs=[ac_problem],
    analogy_side="the ramp at the front door",
    analogy="""  <p>A building with a <b>ramp</b>, <b>wide doors</b> and a <b>lift</b> designed in from the start is easier for wheelchair users, and also for parents with pushchairs, delivery workers and anyone with a sprained ankle. Adding them later costs far more, and looks it.</p>""",
    analogy_figs=[ac_analogy],
    map=[("The ramp", "A swap timer that can be extended"),
         ("Wide doors", "Clear labels and focus order"),
         ("Pushchairs and deliveries", "6 % of all customers using “more time”"),
         ("Designed in", "Accessibility in the definition of done"),
         ("Building regulations", "The European Accessibility Act")],
    how_side="worst first, real users, part of done",
    how="""  <p>Grace fixed the worst first: the swap timer now announces only at one minute and at the end, and customers can ask for <b>more time</b> (WCAG's timing rule). Noor and the team worked through the other <b>40 issues</b> by priority and <b>tested with five customers with disabilities</b>, paid for their time. Accessibility joined the <b>definition of done</b>, with automated checks in CI and a screen-reader test before each release. By November all 41 were fixed; “more time” is used by <b>6 % of all customers</b>.</p>""",
    how_figs=[ac_how],
    steps=[("Audit against WCAG", "With an expert and automated tools."),
           ("Fix the worst barriers first", "Ones that block a task completely."),
           ("Test with disabled users", "Paid, regularly, on real tasks."),
           ("Add it to the definition of done", "Every story, every release."),
           ("Automate what you can", "Checks in CI; manual tests for the rest."),
           ("Publish an accessibility statement", "And a way to report problems.")],
    vocab=[("Accessibility", "Usable by people with disabilities."),
           ("WCAG", "Web Content Accessibility Guidelines (W3C)."),
           ("Screen reader", "Software that reads the screen aloud."),
           ("European Accessibility Act", "EU law requiring accessible products and services, including e-commerce."),
           ("Timing adjustable", "Users can extend or turn off time limits (WCAG 2.2.1)."),
           ("Curb-cut effect", "Accessibility changes that help everyone.")],
    code=dict(file="product/quality/accessibility.md", note="the accessibility plan, August 2027", plain=True, src="""
# Accessibility · owner: Grace with Noor · target WCAG 2.1 AA (EN 301 549) · from 16 Aug 2027

Audit (Aug)   41 issues: 9 blocking, 18 serious, 14 minor
Worst first   swap timer: announced at 1:00 and 0:00 only; "more time" adds 3 minutes (WCAG 2.2.1)
              swap buttons labelled ("Accept oat milk, 40 cents more")
Testing       5 customers with disabilities (screen reader, low vision, motor, cognitive), paid
Done means    automated checks pass in CI · keyboard and screen-reader test on changed screens
Release       screen-reader run-through of order, swap, checkout before each release
Statement     published in the app and web shop, with a contact for problems (Sam's team)
Nov 2027      41 of 41 fixed · "more time" used by 6 % of all customers
"""),
    tools="tools: WCAG and EN 301 549, automated checkers (axe, Lighthouse), screen readers (VoiceOver, TalkBack, NVDA), testing with disabled users.",
    gains=["<b>Everyone can order</b>.",
           "<b>Better for all</b>: 6 % use “more time”.",
           "<b>Legal</b>, at last.",
           "<b>Quality built in</b>, not bolted on.",
           "<b>Real users</b> find real problems."],
    losses=["<b>Audit and fixes</b> take sprints.",
            "<b>Testing with users</b> costs time and money.",
            "<b>Design constraints</b> on new features.",
            "<b>Ongoing checks</b> per release."],
    baseline="Each line compares <b>ignoring accessibility until a complaint</b> to <b>fixing barriers, testing with disabled users and making it part of done</b>.",
    ratings=[(1, 5, "Customers with disabilities can answer swaps."),
             (2, 4, "Legal risk removed; more customers served."),
             (2, 5, "An audit and five real users."),
             (2, 4, "Release checks catch new barriers."),
             (3, 4, "Worst barriers first."),
             (2, 4, "The team learned what barriers look like."),
             (2, 4, "Lena relieved; Sam's complaint answered."),
             (3, 4, "Checks inside the normal flow."),
             (3, 3, "Checks on every release.")],
    pitfalls=[("A one-off project", "Fixed once, broken again.", "part of the definition of done."),
              ("Automated checks only", "Tools miss most barriers.", "test with real users."),
              ("Compliance only", "The minimum, grudgingly.", "quality for everyone."),
              ("Fixing the easy first", "Blockers wait.", "worst barriers first.")],
    use=["Every customer-facing product.",
         "Before new markets (rules differ).",
         "Designing time limits, colours, gestures.",
         "When complaints mention barriers."],
    skip=["Never."],
    related=["<b>Definitions of ready &amp; done</b> (Vol. 3)", "<b>Prototype testing with users</b> (Vol. 1)", "<b>Compliance by design</b> (Ana, book 1 vol. 5)", "<b>A/B tests</b> (Vol. 4)"],
    quiz=[("What was the worst barrier?", "The swap countdown read aloud every second, with no way to get more time."),
          ("How was it fixed?", "Fewer announcements and a “more time” option."),
          ("How is accessibility kept?", "In the definition of done, CI checks and release tests."),
          ("Who used “more time”?", "6 % of all customers, not only screen-reader users.")],
    try_it="Turn on your phone's screen reader and complete your product's most important task with your eyes closed. Write down every place you got stuck, and fix the worst one this sprint.",
    remember="Build the <span class=\"hl\">ramp</span> into the front door; everyone uses it.",
    sources=["W3C, Web Content Accessibility Guidelines (WCAG) 2.1 and 2.2.",
             "Directive (EU) 2019/882, the European Accessibility Act (applies from 28 June 2025).",
             "Sarah Horton and Whitney Quesenbery, <i>A Web for Everyone</i> (2014).",
             "Kat Holmes, <i>Mismatch</i> (2018)."],
)

# ------------------------------------------------------------------ 10 Product-Led Growth
pl_problem = Doodle(760, 280, "Doodle of September 2027. Larder grows mostly through paid ads and city launch campaigns. New customers' first order is often their last: only 41 percent order again within 30 days. Plus has 5,400 members, but most found it through a banner. Marketing spend per new customer keeps rising.",
                    "Growth bought with ads; only 41 % of new customers order again within 30 days.")
pl_problem.box(20, 40, 320, 90, "paid ads", "pink", sub="cost per customer rising")
pl_problem.box(400, 40, 340, 90, "2nd order ≤ 30 days", "y", sub="41 %")
pl_problem.note(380, 200, "pouring water into a leaky bucket", "red", size=19)

pl_analogy = Doodle(760, 250, "Doodle of a neighbourhood café that grows without advertising: the first visit is so good people come back, a loyalty card makes the tenth coffee free, and regulars bring friends. The café itself does the selling.",
                     "A café that grows without ads: a great first visit, a loyalty card, regulars who bring friends.")
pl_analogy.icon("cup", 40, 60, 1.3)
for i, (t, f) in enumerate([("first visit", "y"), ("loyalty card", "blue"), ("bring a friend", "green")]):
    pl_analogy.box(170 + i * 190, 60, 176, 70, t, f, size=16)
pl_analogy.note(450, 200, "the product does the selling", "pen")

pl_how = Doodle(760, 400, "Grace's product-led growth work from 6 September 2027. First order: a welcome screen explaining swaps and the delivery promise, a guaranteed slot, and a follow-up asking how it went; second orders within 30 days rose from 41 to 49 percent. Plus: offered after the second good order, first month free, instead of a banner; trial-to-paid 62 percent. Sharing: give 10 euros, get 10 euros, shared from the order-delivered screen; 12 percent of new customers by December. Paid acquisition cost per new customer fell 18 percent.",
                 "A great first order, Plus at the right moment, sharing that works. 2nd orders 41 → 49 %; paid cost per customer −18 %.")
for i, (t, s, f) in enumerate([("first order", "explain swaps · guaranteed slot", "y"), ("Plus offer", "after the 2nd good order", "blue"), ("sharing", "€10 / €10 from delivery", "green")]):
    pl_how.box(14 + i * 248, 14, 236, 100, t, f, sub=s, size=17, subsize=13)
for i, (t, s) in enumerate([("2nd order ≤ 30 d", "41 % → 49 %"), ("Plus trial → paid", "62 %"), ("via sharing", "12 % of new")]):
    pl_how.box(14 + i * 248, 136, 236, 80, t, "green", sub=s, size=16)
pl_how.box(14, 236, 732, 50, "paid cost per new customer −18 %", "paper", size=16)
pl_how.note(380, 326, "the product does more of the selling", "pen", size=16)

PLG = dict(
    slug="product-led-growth",
    kicker="a.k.a. “the café that needs no ads”",
    tldr="<b>Product-led growth</b> means the product itself does much of the work of winning and keeping customers: a <b>first experience</b> good enough to come back for, <b>offers at the right moment</b> (a trial after a good experience, not a banner), and <b>sharing</b> that's natural. Measure activation and retention, not just sign-ups. Paid growth into a product that doesn't keep people is water into a leaky bucket.",
    chips=[("Family", "scaling the product"), ("Origin", "OpenView's “product-led growth” (2016); growth practice"), ("Lives in", "the onboarding, offers and sharing flows, and the activation metrics"), ("Pairs with", "funnels, cohorts &amp; retention curves, pricing experiments")],
    problem_side="Larder, 6 September 2027",
    problem="""  <p class="lead">Larder grows mostly through <b>paid ads</b> and city launch campaigns. A new customer's first order is often their last: only <b>41 %</b> order again within 30 days. Plus has 5,400 members, but most found it through a <b>banner</b>. Marketing spend per new customer keeps rising. <span class="hl-pink">Water into a leaky bucket.</span></p>
  <ul>
    <li>Paid growth stops when the budget does.</li>
    <li>A bad first experience loses the customer for good.</li>
    <li>Offers at the wrong moment are ignored.</li>
  </ul>""",
    problem_figs=[pl_problem],
    analogy_side="the café that needs no ads",
    analogy="""  <p>A neighbourhood café grows without advertising: the <b>first visit</b> is so good people come back, a <b>loyalty card</b> makes the tenth coffee free, and regulars <b>bring friends</b>. The café itself does the selling.</p>""",
    analogy_figs=[pl_analogy],
    map=[("The first visit", "The first order: swaps explained, a guaranteed slot"),
         ("The loyalty card", "Plus, offered after the second good order"),
         ("Regulars bringing friends", "Give €10, get €10 from the delivered screen"),
         ("Advertising", "Paid ads and launch campaigns"),
         ("Coming back", "Second order within 30 days")],
    how_side="first order, the right moment, sharing",
    how="""  <p>Grace worked on three moments. <b>First order</b>: a welcome screen explaining swaps and the delivery promise, a guaranteed slot, and a follow-up asking how it went: second orders within 30 days rose from <b>41 % to 49 %</b>. <b>Plus</b>: offered after the second good order, first month free, instead of a banner: trial-to-paid <b>62 %</b>. <b>Sharing</b>: give €10, get €10, from the order-delivered screen: <b>12 %</b> of new customers by December. Paid cost per new customer fell <b>18 %</b>.</p>""",
    how_figs=[pl_how],
    steps=[("Measure activation", "The first good experience and the second order."),
           ("Fix the first experience", "Explain what's different; remove first-time risks."),
           ("Offer at the right moment", "After a good experience, not on day one."),
           ("Make sharing natural", "At a happy moment, with a reason to share."),
           ("Watch retention cohorts", "Not just sign-ups."),
           ("Then spend on acquisition", "Into a bucket that holds water.")],
    vocab=[("Product-led growth", "Growth driven mainly by the product experience."),
           ("Activation", "A new customer's first real value."),
           ("Retention", "Customers who keep using the product."),
           ("Referral", "Customers bringing other customers."),
           ("Trial", "Using a paid offer free for a period."),
           ("Acquisition cost", "What it costs to win a new customer.")],
    code=dict(file="product/growth/2027-q4.md", note="growth moments, September–December 2027", plain=True, src="""
# Product-led growth · Q3–Q4 2027 · owner: Grace with Noor and Femke's marketing lead

FIRST ORDER     welcome screen (how swaps work, the delivery promise) · guaranteed slot ·
                "how did it go?" message the next day
                2nd order ≤ 30 days: 41 % → 49 % (A/B, 6 weeks)
PLUS            offered after the 2nd order with no ticket, first month free (banner removed)
                trial → paid 62 % (banner sign-ups: 44 %)
SHARING         give €10, get €10 · shown on the order-delivered screen
                12 % of new customers by December
RESULT          paid acquisition cost per new customer −18 % (Q4 vs Q2)
"""),
    tools="tools: funnels and cohorts, the experiment platform, in-app messages, a referral system, retention dashboards.",
    gains=["<b>Customers stay</b>.",
           "<b>Cheaper growth</b>.",
           "<b>Offers that convert</b>.",
           "<b>Customers bring customers</b>.",
           "<b>Marketing and product</b> share goals."],
    losses=["<b>Slower</b> than switching on ads.",
            "<b>Referral fraud</b> to watch.",
            "<b>More product work</b> on onboarding.",
            "<b>Not every product</b> spreads by sharing."],
    baseline="Each line compares <b>growth bought with ads and banners</b> to <b>a strong first order, offers at the right moment and natural sharing</b>.",
    ratings=[(2, 5, "New customers get a good first order."),
             (1, 5, "Acquisition cost −18 %."),
             (2, 4, "Tested with A/B and cohorts."),
             (2, 4, "Six-week tests per moment."),
             (2, 4, "Three moments, not twenty tactics."),
             (2, 4, "Marketing and product share the numbers."),
             (2, 4, "Femke sees growth that doesn't depend on spend."),
             (2, 4, "Small changes, shipped in steps."),
             (3, 3, "Neutral.")],
    pitfalls=[("Sign-ups only", "Downloads celebrated.", "activation and retention."),
              ("Offers on day one", "Plus before the first order.", "after a good experience."),
              ("Forced sharing", "Spam your contacts.", "a happy moment, a real reason."),
              ("Ads into leaks", "Spending more as retention falls.", "fix the first experience first.")],
    use=["Consumer products with repeat use.",
         "When acquisition costs rise.",
         "Subscriptions and memberships.",
         "When first-time customers don't return."],
    skip=["Products sold through long sales cycles only (business deals)."],
    related=["<b>Funnels</b> (Vol. 4)", "<b>Cohorts &amp; retention curves</b> (Vol. 4)", "<b>Pricing experiments</b> (this volume)", "<b>Vanity vs actionable metrics</b> (Vol. 4)"],
    quiz=[("What are the three moments Grace worked on?", "The first order, the Plus offer, and sharing."),
          ("When is Plus offered now?", "After the second order with no ticket, with a free first month."),
          ("What happened to second orders?", "41 % → 49 % within 30 days."),
          ("Why fix the first experience before spending?", "Paid growth into poor retention is a leaky bucket.")],
    try_it="Find your product's activation moment (the first real value). Measure how many new customers reach it and come back, and change one thing about the first experience to raise it.",
    remember="Be the <span class=\"hl\">café</span> people come back to and bring their <span class=\"hl\">friends</span>.",
    sources=["Wes Bush, <i>Product-Led Growth</i> (2019).",
             "Sean Ellis and Morgan Brown, <i>Hacking Growth</i> (2017).",
             "Andrew Chen, <i>The Cold Start Problem</i> (2021).",
             "Nir Eyal, <i>Hooked</i> (2014)."],
)

# ------------------------------------------------------------------ 11 Writing Product Principles
pp_problem = Doodle(760, 280, "Doodle of October 2027. Grace's area now has three product teams, a designer, and soon a second product owner. Decisions she used to make in a conversation are now made in rooms she isn't in, and come out different: a swap that defaults without asking, a Plus banner on the checkout page, a business feature only Korenwolf can use.",
                    "Decisions made in rooms Grace isn't in come out differently from how she'd make them.")
for i, (t, f) in enumerate([("swap without asking", "pink"), ("banner at checkout", "pink"), ("Korenwolf-only", "pink")]):
    pp_problem.box(20 + i * 250, 40, 220, 80, t, f, size=15)
pp_problem.note(380, 200, "the team can't read Grace's mind", "red", size=20)

pp_analogy = Doodle(760, 250, "Doodle of a newspaper's style book: a few rules with examples, like name sources, short sentences, correct mistakes on page two. Every journalist writes like the paper without asking the editor.",
                     "A newspaper's style book: a few rules with examples, so every journalist writes like the paper.")
pp_analogy.icon("newspaper", 40, 60, 1.3)
for i, (t, f) in enumerate([("name sources", "y"), ("short sentences", "blue"), ("correct mistakes", "green")]):
    pp_analogy.box(170 + i * 190, 60, 176, 70, t, f, size=15)
pp_analogy.note(450, 200, "write like the paper, without asking", "pen")

pp_how = Doodle(760, 420, "Grace's product principles, written with the teams on 11 October 2027. Six, each with what it means you give up. Ask, don't assume: customers decide swaps, even if it's slower. Honest over clever: no dark patterns, even if it costs conversion. Every order complete or explained. One product for homes and offices: no single-client features. Fast for pickers is fast for customers. Less, but better: we remove what doesn't earn its place. Used in refinement and reviews; the checkout banner was removed citing principle two.",
                 "Six principles, each with what you give up. Used in refinement; the checkout banner removed citing #2.")
for i, (t, g) in enumerate([("ask, don't assume", "even if slower"), ("honest over clever", "even if it costs conversion"), ("complete or explained", "every order"),
                            ("one product, homes + offices", "no single-client features"), ("fast for pickers", "is fast for customers"), ("less, but better", "we remove features")]):
    r, c = divmod(i, 2)
    pp_how.box(14 + c * 372, 14 + r * 86, 360, 76, t, "y" if i % 2 == 0 else "blue", sub=g, size=15, subsize=13)
pp_how.note(380, 300, "each with what you give up", "pen", size=16)
pp_how.note(380, 336, "checkout banner removed, citing #2", "green", size=16)

PRINCIPLES = dict(
    slug="product-principles",
    kicker="a.k.a. “the newspaper's style book”",
    tldr="<b>Product principles</b> are a handful of beliefs about how your product treats customers and makes trade-offs, each written so it <b>costs something</b> (“even if…”). They let a growing team decide the way you would <b>without you in the room</b>, and they make disagreements faster to settle. Write them from real decisions, with the team, and use them out loud in refinement and reviews.",
    chips=[("Family", "scaling the product"), ("Origin", "product practice (e.g. Julie Zhuo, Marty Cagan); design principles"), ("Lives in", "one page, quoted in refinement, reviews and PRDs"), ("Pairs with", "strategy on a page, architecture principles (Ana), one-page PRD")],
    problem_side="Larder, 11 October 2027",
    problem="""  <p class="lead">Grace's area now has <b>three product teams</b>, a designer, and soon a second product owner. Decisions she used to make in a conversation are now made in rooms she isn't in, and come out different: a <b>swap that defaults without asking</b>, a <b>Plus banner on the checkout page</b>, a <b>business feature only Korenwolf can use</b>. <span class="hl-pink">The team can't read Grace's mind.</span></p>
  <ul>
    <li>Growing teams can't all ask the product owner.</li>
    <li>Strategy says where; principles say how.</li>
    <li>Unwritten values drift.</li>
  </ul>""",
    problem_figs=[pp_problem],
    analogy_side="the newspaper's style book",
    analogy="""  <p>A good newspaper has a <b>style book</b>: a few rules with examples (name your sources, short sentences, correct mistakes prominently). Every journalist writes <b>like the paper</b> without asking the editor, and when two disagree, the style book settles it.</p>""",
    analogy_figs=[pp_analogy],
    map=[("The style book", "Six product principles on one page"),
         ("Name your sources", "Ask, don't assume"),
         ("Correct mistakes prominently", "Every order complete or explained"),
         ("Every journalist", "Three teams, a designer, a new product owner"),
         ("Settling a disagreement", "The checkout banner removed, citing #2")],
    how_side="a few beliefs, each with its cost",
    how="""  <p>Grace wrote <b>six principles</b> with the teams, from real decisions, each with what it costs: <b>ask, don't assume</b> (even if slower); <b>honest over clever</b> (no dark patterns, even if conversion drops); <b>every order complete or explained</b>; <b>one product for homes and offices</b> (no single-client features); <b>fast for pickers is fast for customers</b>; <b>less, but better</b> (we remove features). They're quoted in refinement and reviews; the checkout banner was removed <b>citing principle two</b>.</p>""",
    how_figs=[pp_how],
    steps=[("Collect hard decisions", "Where you chose one good thing over another."),
           ("Write the belief behind each", "One line."),
           ("Add the cost", "“Even if…”: what you give up."),
           ("Write them with the team", "So they're shared, not handed down."),
           ("Keep five to eight", "Memorable, on one page."),
           ("Use them out loud", "In refinement, reviews, PRDs.")],
    vocab=[("Product principle", "A belief that guides product trade-offs."),
           ("Dark pattern", "A design that tricks users against their interest."),
           ("Trade-off", "Choosing one good thing over another."),
           ("Decision autonomy", "Teams deciding without escalating."),
           ("Strategy", "Where the product is going; principles say how it behaves."),
           ("Taste", "Shared judgment about what's good.")],
    code=dict(file="product/principles.md", note="the product principles, October 2027", plain=True, src="""
# Ordering & apps · product principles · written with the teams, 11 Oct 2027

1  Ask, don't assume.            Customers decide swaps, even if it's slower.
2  Honest over clever.           No dark patterns, even if it costs conversion.
3  Every order complete or explained.  If we can't deliver it, we say so before the door.
4  One product for homes and offices.   No single-client features; settings for all.
5  Fast for pickers is fast for customers.  Picker time counts in every design.
6  Less, but better.             We remove what doesn't earn its place (slot waitlist, 2026).

Used   refinement: "which principle does this touch?" · reviews: cite by number
First use   Plus banner on checkout removed (#2), 13 Oct
"""),
    tools="tools: one page, the team's real decision history, refinement and review templates that ask which principle applies.",
    gains=["<b>Decisions without Grace</b> in the room.",
           "<b>Faster disagreements</b>.",
           "<b>Consistent product</b> across teams.",
           "<b>New people learn</b> the product's values.",
           "<b>Trade-offs explicit</b>."],
    losses=["<b>Principles can be ignored</b> if not used.",
            "<b>Vague ones</b> are useless.",
            "<b>Some conversion</b> given up on purpose.",
            "<b>Need revisiting</b> as the product grows."],
    baseline="Each line compares <b>values living in the product owner's head</b> to <b>six written principles with their costs, used in refinement and reviews</b>.",
    ratings=[(2, 5, "Customers treated the same way by every team."),
             (3, 4, "Some conversion traded for trust."),
             (3, 3, "Neutral."),
             (3, 4, "Faster decisions in refinement."),
             (2, 4, "Principle 6 keeps the product small."),
             (1, 5, "Three teams decide like one."),
             (2, 4, "Leaders see consistent choices."),
             (3, 4, "Fewer escalations."),
             (2, 4, "One page.")],
    pitfalls=[("Platitudes", "“Customer first.”", "a cost: “even if…”."),
              ("Too many", "Fifteen principles.", "five to eight."),
              ("Handed down", "Written alone.", "written with the team."),
              ("On a wall only", "Never quoted.", "use them in every review.")],
    use=["Growing product teams.",
         "Before handing over part of the product.",
         "When teams make inconsistent choices.",
         "Onboarding new product people."],
    skip=["A single small team that decides together daily."],
    related=["<b>Strategy on a page</b> (Vol. 2)", "<b>Architecture principles</b> (Ana, book 1 vol. 6)", "<b>Handing over a product area</b> (this volume)", "<b>Killing a feature</b> (Vol. 4)"],
    quiz=[("What makes a principle useful?", "It costs something: “even if…”."),
          ("How many did Grace write?", "Six, with the teams."),
          ("What was removed citing principle two?", "The Plus banner on the checkout page."),
          ("How are they used?", "Quoted in refinement and reviews.")],
    try_it="List three hard product decisions your team made this year. Write the belief behind each with its cost (“even if…”), and ask your team whether they'd have decided the same.",
    remember="Write the <span class=\"hl\">style book</span>; let every team write like the <span class=\"hl\">paper</span>.",
    sources=["Julie Zhuo, <i>The Making of a Manager</i> (2019), on shared values.",
             "Marty Cagan, <i>Inspired</i>, 2nd ed. (2017), product principles.",
             "Harry Brignull, <i>Deceptive Patterns</i> (2023).",
             "Dieter Rams, “Ten principles for good design” (1970s), “less, but better”."],
)

NOTES = [PLATFORM, ACCESS, PLG, PRINCIPLES]
