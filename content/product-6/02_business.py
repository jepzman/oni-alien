# Series 2 · Book 2 · The Product Owner's Notebook · Vol. 6 · Business customers.
# Narrator: Grace. Running case study: Larder (facts in docs/larder-casebook.md).

# ------------------------------------------------------------------ 04 B2B vs B2C Products
bb_problem = Doodle(760, 280, "Doodle of July 2027. Larder for Business now has Korenwolf and three other office clients, ordering through the portal and the Business API. Grace keeps treating them like households with bigger baskets, and it keeps going wrong: invoices need cost centres, the buyer isn't the user, and a missing item is a contract breach, not a refund.",
                    "Offices treated like households with bigger baskets. It keeps going wrong.")
bb_problem.box(20, 40, 320, 90, "households", "y", sub="one person: buyer = user")
bb_problem.box(400, 40, 340, 90, "offices", "blue", sub="buyer ≠ user ≠ payer")
bb_problem.note(380, 200, "same app, different customers", "red", size=20)

bb_analogy = Doodle(760, 250, "Doodle of a bakery selling to walk-in customers and to a hotel. The walk-in customer chooses, pays and eats. The hotel's chef chooses, the purchasing department signs a contract, accounts pay monthly, and guests eat. Same bread, different business.",
                     "A bakery and a hotel: the chef chooses, purchasing signs, accounts pay, guests eat. Same bread, different business.")
bb_analogy.icon("store", 30, 60, 1.2)
bb_analogy.box(150, 50, 280, 100, "walk-in customer", "y", sub="chooses, pays, eats")
bb_analogy.box(460, 50, 280, 100, "the hotel", "blue", sub="chef · purchasing · accounts · guests")
bb_analogy.note(450, 210, "same bread, different business", "pen")

bb_how = Doodle(760, 400, "Grace's comparison, 5 July 2027. Households: one person decides, uses and pays; they leave quietly; a missing item means a refund. Offices: the office manager uses it, procurement like Ruben buys it, finance pays monthly, a sponsor like Hanna cares about complaints; a missing item breaks a service level; they leave at renewal, after warnings. What stays shared: the catalogue, stock, picking, substitutions, delivery. What differs: accounts and roles, contracts and service levels, invoices, ordering in advance. One ordering core, two front doors.",
                 "Different buyers, users, contracts and promises; one shared core. One ordering core, two front doors.")
bb_how.head(20, 30, "", anchor="start", size=15)
bb_how.head(250, 30, "households", anchor="start", size=15)
bb_how.head(520, 30, "offices", anchor="start", size=15)
for i, (k, a, b, f) in enumerate([("who decides", "one person", "manager · buyer · sponsor", "paper"), ("pays", "card, per order", "invoice, monthly", "paper"),
                                  ("missing item", "a refund", "an SLA breach", "pink"), ("leaving", "quietly", "at renewal", "y")]):
    y = 44 + i * 46
    bb_how.box(12, y, 736, 38, None, f, rx=4)
    bb_how.text(20, y + 25, k, "t-head", anchor="start", size=14)
    bb_how.text(250, y + 25, a, anchor="start", size=14)
    bb_how.text(520, y + 25, b, anchor="start", size=14)
bb_how.box(12, 236, 736, 50, "shared core: catalogue · stock · picking · swaps · delivery", "green", size=15)
bb_how.note(380, 326, "one ordering core, two front doors", "pen", size=17)

B2B = dict(
    slug="b2b-vs-b2c",
    kicker="a.k.a. “the bakery and the hotel”",
    tldr="Business customers (B2B) and consumers (B2C) can use the same product and still be different customers. In B2B the <b>buyer, user, payer and sponsor</b> are different people; there are <b>contracts and service levels</b>; payment is by <b>invoice</b>; and customers leave at <b>renewal</b>, not quietly. Map who's who, keep a <b>shared core</b> for what's truly the same, and give each a <b>front door</b> that fits how they buy.",
    chips=[("Family", "business customers"), ("Origin", "B2B product management practice"), ("Lives in", "the product strategy and the roles model"), ("Pairs with", "proto-personas, service levels as features, canonical data model (Ana)")],
    problem_side="Larder, 5 July 2027",
    problem="""  <p class="lead">Larder for Business now has <b>Korenwolf and three other office clients</b>, ordering through the portal and the Business API. Grace keeps treating them like <b>households with bigger baskets</b>, and it keeps going wrong: invoices need cost centres, the <b>buyer isn't the user</b>, and a missing item is a <span class="hl-pink">contract breach, not a refund</span>.</p>
  <ul>
    <li>B2B has several people per customer, each wanting something different.</li>
    <li>Contracts turn quality into promises with penalties.</li>
    <li>Business customers leave at renewal, after warnings you can miss.</li>
  </ul>""",
    problem_figs=[bb_problem],
    meanwhile=[("architect-4", "canonical-data-model", "the same day, Ana decides against one canonical order model: a business order and a household order differ.",
                "The same day, Grace maps how offices and households differ as customers: one core, two front doors.")],
    analogy_side="the bakery and the hotel",
    analogy="""  <p>A bakery sells to <b>walk-in customers</b> and to a <b>hotel</b>. The walk-in customer chooses, pays and eats. At the hotel, the <b>chef</b> chooses, <b>purchasing</b> signs a contract, <b>accounts</b> pay monthly, and <b>guests</b> eat. Same bread, same ovens, a different business, and a different conversation when something goes wrong.</p>""",
    analogy_figs=[bb_analogy],
    map=[("The chef", "The office manager"),
         ("Purchasing", "Ruben, procurement"),
         ("Accounts, monthly", "Invoices per cost centre"),
         ("The hotel manager", "Hanna, the sponsor"),
         ("Same ovens", "Shared catalogue, stock, picking, delivery")],
    how_side="who's who, shared core, two front doors",
    how="""  <p>Grace compared the two. <b>Households</b>: one person decides, uses and pays; a missing item means a refund; they leave quietly. <b>Offices</b>: the office manager uses it, procurement buys it, finance pays monthly, a sponsor cares about complaints; a missing item breaks a <b>service level</b>; they leave at <b>renewal</b>. Shared: catalogue, stock, picking, substitutions, delivery. Different: accounts and roles, contracts, invoices, ordering ahead. Her rule: <b>one ordering core, two front doors</b>.</p>""",
    how_figs=[bb_how],
    steps=[("Map the roles", "Buyer, user, payer, sponsor, approver."),
           ("Write what each wants", "One line per role."),
           ("Name the promises", "Contracts and service levels."),
           ("Separate core from front door", "What's truly shared, what isn't."),
           ("Measure each side", "Retention for households; renewal health for offices."),
           ("Watch the renewal calendar", "Business churn has a date.")],
    vocab=[("B2B", "Business to business."),
           ("B2C", "Business to consumer."),
           ("Buyer", "Who signs and negotiates."),
           ("User", "Who uses the product day to day."),
           ("Sponsor", "The senior person who owns the outcome."),
           ("Renewal", "The moment a business customer decides to continue.")],
    code=dict(file="product/strategy/b2b-b2c.md", note="the comparison, July 2027", plain=True, src="""
# Households and offices · one ordering core, two front doors · Grace, 5 Jul 2027

|                 | Households (B2C)          | Offices (B2B)                                   |
|-----------------|---------------------------|-------------------------------------------------|
| Decides         | one person                | office manager (user) · Ruben (buyer) · Hanna (sponsor) |
| Pays            | card, per order           | invoice, monthly, per cost centre               |
| Orders          | today, for tonight        | weekly standing orders, a week ahead            |
| Missing item    | refund ticket             | service level breach (98 % by 09:00)            |
| Leaves          | quietly                   | at renewal, after warnings                      |
| Measure         | perfect orders, retention | SLA %, office managers' changes, renewal health |
Shared core: catalogue · stock · picking · substitutions · delivery
Front doors: app + web shop · business portal + Business API (ADR 0019)
"""),
    tools="tools: a roles map per business client, the strategy page, separate measures for each customer type.",
    gains=["<b>Fewer wrong assumptions</b> about offices.",
           "<b>The right people</b> served in each account.",
           "<b>A shared core</b>, not two products.",
           "<b>Renewal risks</b> seen early.",
           "<b>Clear measures</b> per customer type."],
    losses=["<b>Two front doors</b> to build and keep.",
            "<b>More roles</b> and permissions.",
            "<b>Contracts</b> limit flexibility.",
            "<b>Tension</b> over what's shared."],
    baseline="Each line compares <b>treating offices like households with bigger baskets</b> to <b>mapping roles and promises, with a shared core and two front doors</b>.",
    ratings=[(2, 5, "Office managers, buyers and sponsors each served."),
             (2, 4, "Renewals protected."),
             (2, 4, "Roles mapped from real accounts."),
             (3, 4, "Problems seen per role."),
             (2, 4, "Only the front doors differ."),
             (2, 5, "Mo, Grace and Ana share the picture."),
             (2, 4, "Hanna and Ruben get what they care about."),
             (3, 3, "Neutral."),
             (3, 3, "Two front doors to maintain.")],
    pitfalls=[("Bigger baskets", "Offices as large households.", "map the roles."),
              ("Two products", "Separate stock and picking.", "one shared core."),
              ("One measure", "Perfect orders for offices too.", "SLA and renewal health."),
              ("Forgetting the buyer", "Users love it; procurement doesn't renew.", "serve every role.")],
    use=["Products sold to both businesses and consumers.",
         "Adding a business line to a consumer product.",
         "Before designing business features.",
         "When business customers keep being surprised."],
    skip=["Purely consumer or purely business products."],
    related=["<b>Proto-personas</b> (Vol. 1)", "<b>Service levels as features</b> (this volume)", "<b>Working with account managers</b> (Vol. 5)", "<b>Canonical data model</b> (Ana, book 1 vol. 4)"],
    quiz=[("Who are the roles in a business customer?", "User, buyer, payer, sponsor (and sometimes approver)."),
          ("What does a missing item mean for an office?", "A service-level breach, not just a refund."),
          ("What's shared at Larder?", "Catalogue, stock, picking, substitutions and delivery."),
          ("What's Grace's rule?", "One ordering core, two front doors.")],
    try_it="Pick your biggest business customer. Write who the user, buyer, payer and sponsor are, and one thing each wants. Check which of those your product serves today.",
    remember="Same <span class=\"hl\">bread</span>, different business: know the chef, purchasing and the <span class=\"hl\">hotel manager</span>.",
    sources=["Blair Reeves and Benjamin Gaines, <i>Building Products for the Enterprise</i> (2018).",
             "Geoffrey Moore, <i>Crossing the Chasm</i>, 3rd ed. (2014).",
             "Brent Adamson et al., <i>The Challenger Customer</i> (2015), buying groups.",
             "Marty Cagan, <i>Inspired</i>, 2nd ed. (2017)."],
)

# ------------------------------------------------------------------ 05 Account Needs vs Product Vision
av_problem = Doodle(760, 280, "Doodle of September 2027, three months before Korenwolf's renewal. Ruben asks for stock reserved only for Korenwolf and a dedicated picker every Monday morning. Mo says the renewal depends on it. Grace's product vision is one shared store serving everyone well. Saying yes builds a Korenwolf store inside Larder; saying no risks the biggest account.",
                    "Before renewal: “reserve stock for us, and a dedicated picker.” Yes builds a store inside a store; no risks the account.")
av_problem.box(20, 40, 320, 90, "Ruben", "pink", sub="reserved stock · own picker")
av_problem.box(400, 40, 340, 90, "the vision", "green", sub="one shared store, for all")
av_problem.note(380, 200, "the account or the vision?", "red", size=20)

av_analogy = Doodle(760, 250, "Doodle of a theatre's biggest subscriber asking for their own private row every night. The theatre can't give away a row, but it can offer every subscriber priority booking a week early. The subscriber's real need, a good seat without stress, is met for everyone.",
                     "The biggest subscriber wants a private row. Priority booking for all subscribers meets the real need.")
av_analogy.icon("ticket", 40, 60, 1.3)
av_analogy.box(170, 50, 270, 90, "a private row", "pink", sub="for one")
av_analogy.box(470, 50, 270, 90, "priority booking", "green", sub="for every subscriber")
av_analogy.note(450, 205, "meet the need, keep the theatre", "pen")

av_how = Doodle(760, 400, "Grace and Mo's answer, 13 September 2027. The need behind Ruben's ask: Monday mornings with nothing missing, because missing items there reach the board. The vision test: does it serve all business accounts, or only Korenwolf? The answer: reserve stock for every business account's standing orders the evening before, at a cut-off, and pick standing orders first from 06:00. Korenwolf's Monday completeness rose from 96.8 to 99.1 percent; the other three offices improved too. Renewal signed in December.",
                 "Find the need, test it against the vision, solve it for every account. Monday completeness 96.8 → 99.1 %.")
for i, (t, s, f) in enumerate([("need", "Mondays complete", "y"), ("vision test", "all accounts?", "blue"), ("answer", "reserve for all", "green")]):
    av_how.box(14 + i * 248, 14, 236, 100, t, f, sub=s, size=17, subsize=13)
av_how.box(14, 136, 732, 56, "stock reserved the evening before · standing orders picked first", "paper", size=14)
av_how.box(14, 212, 360, 70, "Korenwolf Mondays", "green", sub="96.8 % → 99.1 %", size=16)
av_how.box(386, 212, 360, 70, "other 3 offices", "green", sub="improved too", size=16)
av_how.note(380, 322, "renewal signed in December", "pen", size=17)

ACCOUNTVISION = dict(
    slug="account-needs-vs-vision",
    kicker="a.k.a. “the private row”",
    tldr="A big account's request can pull a product away from its vision, one exception at a time. Before saying yes or no, find the <b>need behind the request</b>, then apply a <b>vision test</b>: would this serve <b>all</b> customers like them, or only this one? Usually there's an answer that meets the need for everyone. When there isn't, say no clearly, with the reason, and offer what you can. Exceptions for one become the product's shape.",
    chips=[("Family", "business customers"), ("Origin", "B2B product strategy; “build for the segment, not the customer”"), ("Lives in", "the request review and the product principles"), ("Pairs with", "working with account managers, negotiating scope, product principles")],
    problem_side="Larder, 13 September 2027",
    problem="""  <p class="lead">Three months before Korenwolf's renewal, Ruben asks for <b>stock reserved only for Korenwolf</b> and a <b>dedicated picker</b> every Monday morning. Mo says the renewal depends on it. Grace's vision is <b>one shared store</b> serving everyone well. <span class="hl-pink">Yes builds a Korenwolf store inside Larder; no risks the biggest account.</span></p>
  <ul>
    <li>Big accounts' requests feel non-negotiable.</li>
    <li>Each exception makes the next one easier to ask for.</li>
    <li>Saying no without an alternative damages the account.</li>
  </ul>""",
    problem_figs=[av_problem],
    analogy_side="the private row",
    analogy="""  <p>A theatre's biggest subscriber asks for their <b>own private row</b> every night. The theatre can't give away a row, but it can offer every subscriber <b>priority booking</b> a week early. The subscriber's real need, a good seat without stress, is met, and the theatre stays a theatre.</p>""",
    analogy_figs=[av_analogy],
    map=[("The private row", "Reserved stock and a picker just for Korenwolf"),
         ("A good seat without stress", "Monday mornings with nothing missing"),
         ("Priority booking for all subscribers", "Stock reserved for every standing order"),
         ("The theatre stays a theatre", "One shared store"),
         ("The subscriber renews", "Renewal signed in December")],
    how_side="the need, the vision test, a solution for all",
    how="""  <p>Grace and Mo asked about the <b>need</b>: Monday mornings with nothing missing, because missing items there reach Korenwolf's board. The <b>vision test</b>: would this serve every business account? The answer did: <b>stock reserved the evening before</b> for every business account's standing orders, and standing orders <b>picked first</b> from 06:00. Korenwolf's Monday completeness rose from <b>96.8 % to 99.1 %</b>; the other three offices improved too. The <b>renewal was signed in December</b>.</p>""",
    how_figs=[av_how],
    steps=[("Ask for the need", "What goes wrong without it, for whom?"),
           ("Apply the vision test", "Would it serve every customer like them?"),
           ("Design for the segment", "A setting or feature for all."),
           ("Say no clearly when it fails", "With the reason and an alternative."),
           ("Involve the account manager", "They carry the answer."),
           ("Measure for all accounts", "Not only the one who asked.")],
    vocab=[("Product vision", "Where the product is going and for whom."),
           ("Segment", "A group of similar customers."),
           ("Custom work", "Building for one customer."),
           ("Vision test", "Does this serve the segment, or one account?"),
           ("Stock reservation", "Holding stock for known orders."),
           ("Renewal", "The client's decision to continue.")],
    code=dict(file="product/business/2027-09-reservations.md", note="the decision, 13 September 2027", plain=True, src="""
# Korenwolf's Monday request · Grace + Mo · 13 Sep 2027

Request      stock reserved only for Korenwolf · a dedicated picker on Mondays
Need         Monday mornings complete (missing items reach Korenwolf's board); 96.8 % in Aug
Vision test  "one shared store, for everyone" → for all business accounts? yes, if generalised
Decision     for every business account: stock reserved at 20:00 the evening before for
             standing orders; standing orders picked first from 06:00
Declined     a dedicated Korenwolf picker (Joost: shared crew, same result)
Result Oct   Korenwolf Mondays 99.1 % · other 3 offices 97.9 → 99.0 % · renewal signed Dec 2027
"""),
    tools="tools: the request review with the account manager, the product principles, settings for all business accounts, per-account dashboards.",
    gains=["<b>The account kept</b>.",
           "<b>The vision kept</b>.",
           "<b>Every client benefits</b>.",
           "<b>No custom forks</b>.",
           "<b>A precedent</b> for future asks."],
    losses=["<b>Takes longer</b> than a quick yes.",
            "<b>Not every ask</b> generalises.",
            "<b>Account managers</b> carry hard answers.",
            "<b>Reserved stock</b> can't go to households."],
    baseline="Each line compares <b>saying yes or no to a big account's request as asked</b> to <b>finding the need and solving it for every account like them</b>.",
    ratings=[(2, 5, "Every office's Mondays improved."),
             (1, 5, "The renewal signed."),
             (2, 4, "Monday completeness measured before and after."),
             (3, 4, "A month to see the effect."),
             (1, 5, "One shared store kept."),
             (2, 4, "Mo, Joost and Grace agreed the answer."),
             (2, 5, "Ruben got his need met, with reasons."),
             (3, 4, "Standing orders flow first."),
             (3, 3, "Neutral.")],
    pitfalls=[("Yes as asked", "A Korenwolf picker.", "find the need; solve for all."),
              ("No without help", "“Not in our vision.”", "an alternative that meets the need."),
              ("Vision as an excuse", "Ignoring real needs.", "test honestly."),
              ("Measuring one client", "Others forgotten.", "measure for all accounts.")],
    use=["Big accounts' special requests.",
         "Before renewals.",
         "When custom work starts to pile up.",
         "Setting precedents for a segment."],
    skip=["Truly unique, paid custom work agreed as a separate service (rare, and priced)."],
    related=["<b>Working with account managers</b> (Vol. 5)", "<b>Negotiating scope</b> (Vol. 5)", "<b>Writing product principles</b> (this volume)", "<b>B2B vs B2C products</b> (this volume)"],
    quiz=[("What's the vision test?", "Would this serve every customer like them, or only this one?"),
          ("What was the need behind Ruben's request?", "Monday mornings with nothing missing."),
          ("What did Larder build?", "Stock reserved the evening before for every business account's standing orders, picked first."),
          ("What happened to Korenwolf's Mondays?", "96.8 % → 99.1 % complete; renewal signed in December.")],
    try_it="Take a special request from your biggest customer. Write the need behind it, ask whether a version would help every similar customer, and sketch that version.",
    remember="Not a <span class=\"hl\">private row</span>: <span class=\"hl\">priority booking</span> for every subscriber.",
    sources=["Marty Cagan, <i>Inspired</i>, 2nd ed. (2017), on specials vs products.",
             "Blair Reeves and Benjamin Gaines, <i>Building Products for the Enterprise</i> (2018).",
             "Roman Pichler, <i>Strategize</i>, 2nd ed. (2022), product vision.",
             "Des Traynor, <i>Intercom on Product Management</i> (2016)."],
)

# ------------------------------------------------------------------ 06 Service Levels as Features
sl_problem = Doodle(760, 280, "Doodle of October 2027. Korenwolf's contract promises 98 percent complete deliveries by 09:00. Each month Mo builds the report by hand from three exports, it arrives on the tenth, and credits for missed mornings are negotiated by email. Office managers have no idea whether today's delivery is on track until it's late.",
                    "The 98 % promise lives in a hand-made report on the tenth and credits argued by email.")
sl_problem.box(20, 40, 320, 90, "Mo's report", "pink", sub="3 exports · on the 10th")
sl_problem.box(400, 40, 340, 90, "credits", "y", sub="argued by email")
sl_problem.note(380, 200, "a promise nobody can see", "red", size=20)

sl_analogy = Doodle(760, 250, "Doodle of a rail company that promises trains on time: the departure board shows each train's status live, the monthly punctuality figures are published, and delay compensation is paid automatically to season-ticket holders.",
                     "A railway's promise you can see: live departure board, published punctuality, automatic compensation.")
sl_analogy.icon("clock", 40, 60, 1.3)
for i, (t, f) in enumerate([("live board", "blue"), ("monthly figures", "y"), ("auto refund", "green")]):
    sl_analogy.box(170 + i * 190, 60, 176, 70, t, f, size=16)
sl_analogy.note(450, 200, "the promise is visible", "pen")

sl_how = Doodle(760, 400, "Larder's service levels as features from 4 October 2027, in the business portal. Live: each office's delivery status this morning, picked, loaded, on the way, delivered, with the time. Monthly: the service-level report generated automatically on the first working day, per office, using the contract's definition. Credits: when a morning misses, the credit appears on the next invoice automatically. Mo's monthly report work went from two days to zero; complaints to Hanna about missing deliveries fell to none in Q4.",
                 "Live status, an automatic monthly report, automatic credits. Mo's two days a month → none.")
for i, (t, s, f) in enumerate([("live status", "picked · loaded · on the way", "blue"), ("monthly report", "auto, 1st working day", "y"), ("credits", "automatic, next invoice", "green")]):
    sl_how.box(14 + i * 248, 14, 236, 100, t, f, sub=s, size=17, subsize=13)
sl_how.box(14, 136, 732, 56, "measured with the contract's definition, per office", "paper", size=15)
sl_how.box(14, 212, 360, 70, "Mo's report", "green", sub="2 days a month → 0", size=16)
sl_how.box(386, 212, 360, 70, "complaints to Hanna", "green", sub="none in Q4", size=16)
sl_how.note(380, 322, "the promise became part of the product", "pen", size=16)

SERVICELEVELS = dict(
    slug="service-levels-as-features",
    kicker="a.k.a. “the departure board”",
    tldr="A service level in a contract is a promise, and promises customers can't see breed doubt. Make service levels <b>features</b>: show status <b>live</b>, generate the <b>report automatically</b> using the contract's exact definition, and pay <b>credits automatically</b> when you miss. The promise becomes part of the product, the account manager stops building spreadsheets, and trust grows even on bad days.",
    chips=[("Family", "business customers"), ("Origin", "SaaS status pages and SLA reporting; service design"), ("Lives in", "the business portal, the invoice and the monthly report"), ("Pairs with", "availability maths (Ana), B2B vs B2C, dashboards that get used")],
    problem_side="Larder, 4 October 2027",
    problem="""  <p class="lead">Korenwolf's contract promises <b>98 % complete deliveries by 09:00</b>. Each month Mo builds the report <b>by hand</b> from three exports; it arrives on the tenth; <b>credits</b> for missed mornings are argued by email. Office managers have no idea whether today's delivery is on track until it's late. <span class="hl-pink">A promise nobody can see.</span></p>
  <ul>
    <li>Hand-made reports are late and disputed.</li>
    <li>Customers learn about misses after the fact.</li>
    <li>Arguing over credits damages the relationship.</li>
  </ul>""",
    problem_figs=[sl_problem],
    analogy_side="the departure board",
    analogy="""  <p>A railway that promises trains on time shows each train's status on a <b>live departure board</b>, publishes <b>monthly punctuality</b>, and pays <b>delay compensation automatically</b> to season-ticket holders. Passengers still dislike delays, but they trust the railway to be honest about them.</p>""",
    analogy_figs=[sl_analogy],
    map=[("The live departure board", "Each office's delivery status this morning"),
         ("Monthly punctuality", "The automatic service-level report"),
         ("Automatic compensation", "Credits on the next invoice"),
         ("The timetable promise", "98 % complete by 09:00"),
         ("Season-ticket holders", "Business accounts")],
    how_side="live status, automatic report, automatic credits",
    how="""  <p>Grace's team built the promise into the <b>business portal</b>: <b>live status</b> for each office's morning delivery (picked, loaded, on the way, delivered); a <b>monthly report</b> generated on the first working day, per office, using the <b>contract's definition</b>; and <b>credits</b> added to the next invoice automatically when a morning misses. Mo's report work went from <b>two days a month to none</b>; complaints to Hanna about missing deliveries: <b>none in Q4</b>.</p>""",
    how_figs=[sl_how],
    steps=[("Write the promise precisely", "The contract's definition, as a calculation."),
           ("Show it live", "Today's status, where customers look."),
           ("Report automatically", "Same definition, on a fixed day."),
           ("Pay credits automatically", "No arguing."),
           ("Alert yourselves first", "Before the customer sees a miss."),
           ("Review with the client", "Trends, not disputes.")],
    vocab=[("Service level", "A measurable promise about quality of service."),
           ("SLA", "Service level agreement, in a contract."),
           ("Service credit", "Compensation for missing a service level."),
           ("Status page", "Live service status shown to customers."),
           ("Definition", "Exactly how a promise is measured."),
           ("Self-service report", "A report customers get without asking.")],
    code=dict(file="product/business/service-levels.md", note="the service-level features, October 2027", plain=True, src="""
# Service levels in the business portal · live from 4 Oct 2027 · owner: Grace

Promise     98 % of office mornings complete (every ordered item, or an agreed swap) by 09:00
Definition  per office, per delivery morning, as in the contract (§4.2); not per crate
Live        portal → "This morning": picked 06:40 · loaded 07:05 · on the way · delivered 08:31
Report      generated 1st working day, per office + total; same numbers Mo and Ruben see
Credits     missed morning → 10 % of that delivery credited on the next invoice, automatically
Alerts      Mo and the store manager alerted at 08:15 if a delivery is at risk
Q4 2027     Korenwolf 99.0 % · Mo's report work 2 days/month → 0 · complaints to Hanna: 0
"""),
    tools="tools: the portal, delivery events from Dispatch, the billing service for credits, a scheduled report job.",
    gains=["<b>Trust</b>: the promise is visible.",
           "<b>No hand-made reports</b>.",
           "<b>No credit disputes</b>.",
           "<b>Early alerts</b> to fix mornings.",
           "<b>A selling point</b> for new clients."],
    losses=["<b>Misses are visible</b> too.",
            "<b>Automatic credits</b> cost money.",
            "<b>Definitions</b> must be exact.",
            "<b>Building it</b> takes a few sprints."],
    baseline="Each line compares <b>a hand-made monthly report and credits by email</b> to <b>live status, an automatic report and automatic credits in the product</b>.",
    ratings=[(2, 5, "Office managers see their delivery live."),
             (2, 4, "Renewal helped; a selling point."),
             (2, 5, "One definition, computed the same way."),
             (2, 4, "Alerts at 08:15, before the miss."),
             (3, 3, "Neutral."),
             (2, 5, "Mo, Ruben and Grace see the same numbers."),
             (1, 5, "Hanna's complaints stopped."),
             (3, 4, "Live status every morning."),
             (2, 5, "Mo's two days a month saved.")],
    pitfalls=[("Vague promises", "“High completeness.”", "an exact definition."),
              ("Hiding misses", "Only the monthly average.", "live status, honestly."),
              ("Manual credits", "Argued case by case.", "automatic, by rule."),
              ("Different numbers", "Report vs portal disagree.", "one calculation.")],
    use=["Contracts with service levels.",
         "Business clients that ask for reports.",
         "When account managers build reports by hand.",
         "Selling to procurement teams."],
    skip=["Consumer products without contractual promises (use a status page)."],
    related=["<b>Availability maths</b> (Ana, book 1 vol. 5)", "<b>B2B vs B2C products</b> (this volume)", "<b>Dashboards that get used</b> (Vol. 4)", "<b>Self-service for business customers</b> (this volume)"],
    quiz=[("What three features make a service level visible?", "Live status, an automatic report, automatic credits."),
          ("Why use the contract's exact definition?", "So the portal, report and invoice all agree."),
          ("What happened to Mo's report work?", "Two days a month to none."),
          ("What do automatic credits avoid?", "Arguing over each missed morning.")],
    try_it="Take one promise you make to customers. Write its exact definition as a calculation, and sketch where a customer could see today's status and this month's number without asking.",
    remember="Put the promise on the <span class=\"hl\">departure board</span>, and pay the <span class=\"hl\">refund</span> automatically.",
    sources=["Alex Hidalgo, <i>Implementing Service Level Objectives</i> (2020).",
             "Atlassian, “What is an SLA?” and status page practice.",
             "Lou Downe, <i>Good Services</i> (2020).",
             "Betsy Beyer et al., <i>Site Reliability Engineering</i> (2016), SLOs and SLAs."],
)

# ------------------------------------------------------------------ 07 Self-Service for Business Customers
ss_problem = Doodle(760, 280, "Doodle of June 2027. Office managers change their standing orders by emailing Mo before 08:00 the day before, as agreed for January. With four office clients, Mo spends about twelve hours a week re-typing changes, mistakes reach invoices, and nobody can change anything after Mo goes home.",
                    "Every change emailed to Mo and re-typed: twelve hours a week, mistakes on invoices.")
ss_problem.box(20, 40, 320, 90, "office managers", "paper", sub="email Mo before 08:00")
ss_problem.box(400, 40, 340, 90, "Mo", "pink", sub="12 hours a week re-typing", stroke="red")
ss_problem.note(380, 200, "the account manager as a keyboard", "red", size=19)

ss_analogy = Doodle(760, 250, "Doodle of a bank that once required a phone call to the branch for every transfer. Online banking let customers do it themselves, any time; the branch staff spent their time on advice instead of typing.",
                     "Phoning the branch for every transfer, versus online banking: staff advise instead of typing.")
ss_analogy.icon("phone", 40, 60, 1.3)
ss_analogy.box(170, 50, 270, 90, "phone the branch", "pink", sub="every transfer")
ss_analogy.box(470, 50, 270, 90, "online banking", "green", sub="any time, yourself")
ss_analogy.note(450, 205, "staff free for advice", "pen")

ss_how = Doodle(760, 400, "The business portal's self-service, live from May 2027 and reviewed on 7 June. Office managers can skip a week, change quantities, add a one-off item and see the next delivery, until 16:00 the day before. Approvals above an office's budget limit go to the approver automatically. Mo keeps the relationship: renewals, reviews, new offices. Four weeks in: 80 percent of changes made in the portal; Mo's re-typing from twelve hours a week to two; invoice corrections from nine a month to one.",
                 "Skip, change, add, see, until 16:00. 80 % of changes in the portal; Mo's re-typing 12 h → 2 h a week.")
for i, (t, f) in enumerate([("skip", "y"), ("change", "y"), ("add items", "y"), ("see next", "blue")]):
    ss_how.box(14 + i * 184, 14, 174, 70, t, f, size=14)
ss_how.box(14, 104, 732, 50, "until 16:00 the day before · approvals above budget routed", "paper", size=14)
for i, (t, s) in enumerate([("in the portal", "80 % of changes"), ("Mo's re-typing", "12 h → 2 h a week"), ("invoice fixes", "9 → 1 a month")]):
    ss_how.box(14 + i * 248, 176, 236, 80, t, "green", sub=s, size=16)
ss_how.note(380, 296, "Mo keeps the relationship, not the keyboard", "pen", size=16)

SELFSERVICE = dict(
    slug="business-self-service",
    kicker="a.k.a. “online banking for the pantry”",
    tldr="When business customers must ask a person for every change, that person becomes a keyboard and a bottleneck. <b>Self-service</b> lets customers do routine things themselves (change, skip, add, see), any time, inside sensible <b>rules</b> (cut-off times, approvals). The account manager keeps the <b>relationship</b>: reviews, renewals, growth. Start with the changes people request most.",
    chips=[("Family", "business customers"), ("Origin", "B2B self-service portals; customer success practice"), ("Lives in", "the business portal (ADR 0022's portal BFF)"), ("Pairs with", "working with account managers, B2B vs B2C, backend for frontend (Ana)")],
    problem_side="Larder, 7 June 2027",
    problem="""  <p class="lead">Office managers change their standing orders by <b>emailing Mo</b> before 08:00 the day before, as agreed for January. With four office clients, Mo spends about <b>twelve hours a week re-typing</b> changes, mistakes reach invoices, and <span class="hl-pink">nobody can change anything after Mo goes home</span>.</p>
  <ul>
    <li>Routine changes don't need a person.</li>
    <li>Re-typing creates errors.</li>
    <li>The account manager's time goes on admin, not the relationship.</li>
  </ul>""",
    problem_figs=[ss_problem],
    meanwhile=[("architect-4", "backend-for-frontend", "the same day, Ana's portal backend cuts the order screen from seven calls and 2.8 seconds to one call and 0.6.",
                "The same day, Grace reviews the portal's first month: 80 % of office changes now made there.")],
    analogy_side="online banking",
    analogy="""  <p>Banks once required a <b>phone call to the branch</b> for every transfer. <b>Online banking</b> let customers do it themselves, any time, within limits. Branch staff stopped typing transfers and started giving advice.</p>""",
    analogy_figs=[ss_analogy],
    map=[("Phoning the branch", "Emailing Mo before 08:00"),
         ("Online banking", "The business portal"),
         ("Transfer limits", "Cut-off at 16:00; approvals above budget"),
         ("Advice from the branch", "Mo's reviews, renewals and new offices"),
         ("Any time", "Changes after Mo goes home")],
    how_side="routine changes, with rules; people for the relationship",
    how="""  <p>The <b>business portal</b> went live in May with the most-requested changes from Mo's inbox: <b>skip a week</b>, <b>change quantities</b>, <b>add one-off items</b>, <b>see the next delivery</b>, until <b>16:00</b> the day before. Orders above an office's budget go to its <b>approver</b> automatically. Mo keeps the <b>relationship</b>. Four weeks in: <b>80 %</b> of changes in the portal; Mo's re-typing from <b>twelve hours a week to two</b>; invoice corrections from <b>nine a month to one</b>.</p>""",
    how_figs=[ss_how],
    steps=[("Read the inbox", "The requests people make most."),
           ("Build those first", "Skip, change, add, see."),
           ("Set rules", "Cut-off times, approvals, budgets."),
           ("Move people to it gently", "Show office managers; keep email for a month."),
           ("Free the account manager", "For reviews, renewals, growth."),
           ("Measure the shift", "Share of changes self-served, errors, time saved.")],
    vocab=[("Self-service", "Customers doing routine tasks themselves."),
           ("Portal", "A website for customers' accounts."),
           ("Cut-off time", "The last moment a change is accepted."),
           ("Approval flow", "Routing orders above a limit to an approver."),
           ("Customer success", "Helping clients get value and renew."),
           ("Deflection", "Requests handled without a person.")],
    code=dict(file="product/business/portal-month-1.md", note="the portal's first month, 7 June 2027", plain=True, src="""
# Business portal · first month review · 7 Jun 2027 · Grace, Mo, Noor

Built (from Mo's inbox, Jan–Apr: 412 change emails)
  skip a week (31 %) · change quantities (38 %) · add a one-off item (22 %) · see next delivery
Rules      changes until 16:00 the day before · orders above an office's budget → its approver
Adoption   office managers trained in a 20-min call each; email still accepted until 30 Jun
Results    changes in the portal 80 % (week 4) · Mo's re-typing 12 h → 2 h a week ·
           invoice corrections 9 → 1 a month · changes after 18:00: 27 % (impossible before)
Next       edit standing orders for next month · invite colleagues (Sep)
"""),
    tools="tools: the business portal and its backend, the account manager's inbox as research, approval rules, usage analytics.",
    gains=["<b>Changes any time</b>, not office hours.",
           "<b>Fewer errors</b> from re-typing.",
           "<b>The account manager freed</b> for the relationship.",
           "<b>Scales</b> to more clients.",
           "<b>Office managers in control</b>."],
    losses=["<b>A portal to build and support</b>.",
            "<b>Some clients prefer</b> a person.",
            "<b>Rules</b> must be clear.",
            "<b>Training</b> needed at first."],
    baseline="Each line compares <b>every change emailed to the account manager</b> to <b>routine changes self-served in a portal, with the account manager on the relationship</b>.",
    ratings=[(2, 5, "Office managers change orders any time."),
             (2, 4, "Ready for many more office clients."),
             (2, 4, "Built from 412 real requests."),
             (2, 4, "First-month numbers in four weeks."),
             (2, 4, "The four most-requested changes first."),
             (3, 4, "Mo, Noor and Grace designed it together."),
             (2, 4, "Fewer invoice errors to explain."),
             (2, 4, "Changes flow straight into orders."),
             (2, 5, "Mo's ten hours a week back.")],
    pitfalls=[("Building everything", "A portal of every possible setting.", "the most-requested changes."),
              ("No rules", "Changes at 05:00.", "cut-off times and approvals."),
              ("Forcing it overnight", "Email stopped on day one.", "a gentle move, with training."),
              ("Account manager replaced", "Nobody owns the relationship.", "free them for it.")],
    use=["Business clients making routine changes through people.",
         "When account managers are buried in admin.",
         "Before growing the number of clients.",
         "When errors come from re-typing."],
    skip=["Rare, complex changes that need judgment (keep a person)."],
    related=["<b>Working with account managers</b> (Vol. 5)", "<b>B2B vs B2C products</b> (this volume)", "<b>Backend for frontend</b> (Ana, book 1 vol. 4)", "<b>Service levels as features</b> (this volume)"],
    quiz=[("Which changes were built first?", "The most-requested: skip, change quantities, add one-off items, see the next delivery."),
          ("What rules apply?", "Changes until 16:00 the day before; orders above budget go to the approver."),
          ("What happened to Mo's week?", "Re-typing fell from twelve hours to two."),
          ("What does the account manager do now?", "The relationship: reviews, renewals, new offices.")],
    try_it="Read the last month of requests your account managers handled. Count the top four kinds, and sketch a self-service screen for the most common one, with its rules.",
    remember="<span class=\"hl\">Online banking</span> for the routine; the branch for <span class=\"hl\">advice</span>.",
    sources=["Lincoln Murphy, customer success writing (Sixteen Ventures, 2010s).",
             "Nick Mehta, Dan Steinman and Lincoln Murphy, <i>Customer Success</i> (2016).",
             "Blair Reeves and Benjamin Gaines, <i>Building Products for the Enterprise</i> (2018).",
             "Matthew Dixon et al., <i>The Effortless Experience</i> (2013)."],
)

NOTES = [B2B, ACCOUNTVISION, SERVICELEVELS, SELFSERVICE]
