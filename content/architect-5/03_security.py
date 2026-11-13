# Series 2 · The Solution Architect's Notebook · Vol. 5 · Security & compliance.
# Running case study: Larder (facts in docs/larder-casebook.md).

# ------------------------------------------------------------------ 09 Security Architecture Review
sr_problem = Doodle(760, 280, "Doodle of October 2027. The Business API, the business portal and the single sign-on with clients were each built and reviewed by their own team, feature by feature. Three more office clients are about to start. Nobody has looked at the whole design from an attacker's side, across the trust boundaries between Larder and its clients.",
                    "Each piece reviewed by its own team; nobody has looked at the whole design from an attacker's side.")
for i, (t, f) in enumerate([("Business API", "blue"), ("business portal", "y"), ("client SSO", "green")]):
    sr_problem.box(20 + i * 250, 40, 220, 80, t, f, sub="reviewed alone", size=16)
sr_problem.box(200, 150, 360, 56, "3 new office clients next month", "paper", size=15)
sr_problem.note(380, 252, "nobody walked the boundaries", "red", size=19)

sr_analogy = Doodle(760, 250, "Doodle of a building's security survey: the surveyor walks every door between public and private spaces, the street door, the loading bay, the door from reception to the offices, and asks at each who can pass, how they prove it, and what they could reach.",
                     "A security survey walks every door between public and private, and asks who can pass and what they could reach.")
sr_analogy.icon("door", 30, 60, 1.3)
for i, (t, f) in enumerate([("street door", "paper"), ("loading bay", "pink"), ("office door", "y")]):
    sr_analogy.box(140 + i * 205, 60, 190, 70, t, f, size=15)
sr_analogy.note(450, 205, "who can pass, and what could they reach?", "pen")

sr_how = Doodle(760, 400, "Larder's security architecture review, 11 October 2027: two half-days, Ana with Cho, Ben, Eli and an external reviewer. The diagram's trust boundaries: internet to Business API, client identity provider to Larder, portal to Larder Core, billing webhooks into Larder. At each, a STRIDE pass and a checklist. Eleven findings, three high: business API keys never expire and some were shared by email; an office manager could see another office's orders by changing the number in the address; billing webhooks were not signature-checked. The three highs fixed within two weeks, the rest dated in the backlog.",
                 "Walk each trust boundary with STRIDE and a checklist. Eleven findings, three high, fixed in two weeks.")
for i, (t, sub, f) in enumerate([("internet", "→ Business API", "pink"), ("client IdP", "→ Larder", "y"), ("portal", "→ Core", "blue"), ("billing", "→ webhooks", "paper")]):
    sr_how.box(14 + i * 184, 14, 174, 70, t, f, sub=sub, size=15, subsize=14)
sr_how.box(14, 100, 732, 46, "at each: STRIDE + checklist (authn, authz, data, secrets, logs)", "green", size=14)
for i, (t, s) in enumerate([("API keys never expire", "→ 90-day keys, rotation"), ("other office's orders by ID", "→ check ownership"), ("unsigned webhooks", "→ verify signatures")]):
    y = 166 + i * 54
    sr_how.box(14, y, 732, 46, None, "pink", rx=4, stroke="red")
    sr_how.text(30, y + 30, t, "t-head", anchor="start", size=15)
    sr_how.text(730, y + 30, s, anchor="end", size=14)
sr_how.note(380, 350, "11 findings · 3 high fixed in two weeks", "pen", size=16)
sr_how.note(380, 380, "now a standard step for designs that cross a boundary", "green", size=15)

REVIEW = dict(
    slug="security-architecture-review",
    kicker="a.k.a. “the security survey”",
    tldr="A <b>security architecture review</b> looks at a whole design from an attacker's side before it's widely used. Draw the system with its <b>trust boundaries</b> (where data or control passes between parties with different trust), and at each one ask the <b>STRIDE</b> questions and go through a short <b>checklist</b>: who can pass, how they prove it, what they can reach, what's logged, how secrets are kept. Rank the findings, fix the high ones on a date, and make the review a standard step for designs that cross a boundary.",
    chips=[("Family", "security &amp; compliance"), ("Origin", "Microsoft's STRIDE (1999), threat modelling and secure design reviews"), ("Lives in", "a review page per design, findings in the backlog with dates"), ("Pairs with", "threat modelling, identity federation, data classification")],
    problem_side="Larder, 11 October 2027",
    problem="""  <p class="lead">The <b>Business API</b>, the <b>business portal</b> and <b>single sign-on with clients</b> were each built and reviewed by their own team, feature by feature. Three more office clients start next month. <span class="hl-pink">Nobody has looked at the whole design from an attacker's side</span>, across the boundaries between Larder, its clients and its vendors.</p>
  <ul>
    <li>Feature reviews miss problems between features.</li>
    <li>Trust boundaries multiply as partners connect.</li>
    <li>Fixes after many clients depend on a design cost far more.</li>
  </ul>""",
    problem_figs=[sr_problem],
    analogy_side="the security survey",
    analogy="""  <p>A security surveyor walks a building's <b>doors between public and private</b>: the <b>street door</b>, the <b>loading bay</b>, the <b>office door</b> behind reception. At each, they ask who can pass, how they prove it, what they could reach once through, and whether anyone would notice. Locks on individual cupboards come later.</p>""",
    analogy_figs=[sr_analogy],
    map=[("Doors between public and private", "Trust boundaries in the design"),
         ("The street door", "Internet → Business API"),
         ("The loading bay", "Billing's webhooks into Larder"),
         ("Who can pass, how they prove it", "Authentication and authorisation at each boundary"),
         ("Would anyone notice?", "Logging and alerting")],
    how_side="each boundary, STRIDE and a checklist",
    how="""  <p>Ana ran two half-days with Cho, Ben, Eli and an <b>external reviewer</b>. They marked four <b>trust boundaries</b> on the container diagram and did a <b>STRIDE</b> pass and a checklist at each. <b>Eleven findings</b>, three high: business <b>API keys never expired</b> (some had been shared by email); an office manager could see <b>another office's orders</b> by changing the number in the address; <b>billing webhooks weren't signature-checked</b>. The highs were fixed within two weeks; the rest went into the backlog with dates.</p>""",
    how_figs=[sr_how],
    steps=[("Draw the design with boundaries", "Every place data or control crosses between parties."),
           ("Ask STRIDE at each boundary", "Spoofing, tampering, repudiation, disclosure, denial, elevation."),
           ("Run a short checklist", "Authentication, authorisation, data, secrets, logging, dependencies."),
           ("Bring an outside eye", "Someone who didn't build it."),
           ("Rank and date the findings", "High: fixed before more users; others in the backlog."),
           ("Make it a standard step", "For every design that crosses a trust boundary.")],
    vocab=[("Trust boundary", "Where data or control passes between parties with different trust."),
           ("STRIDE", "Spoofing, Tampering, Repudiation, Information disclosure, Denial of service, Elevation of privilege."),
           ("IDOR", "Insecure direct object reference: reaching others' data by changing an ID."),
           ("Attack surface", "Every way in that an attacker could try."),
           ("Webhook signature", "A code proving a webhook came from the real sender."),
           ("Finding", "A weakness found in the review, with a severity.")],
    code=dict(file="docs/security/reviews/2027-10-business.md", note="review summary, 11 October 2027", plain=True, src="""
# Security architecture review · business ordering · 11 Oct 2027
Scope: Business API (/business/v1), business portal + BFF, client SSO (ADR 0021), billing webhooks
People: Ana, Cho, Ben, Eli + external reviewer · 2 × half a day · STRIDE per boundary + checklist

| # | Boundary                | Finding                                       | Sev  | Fix (owner, date)                  |
|---|-------------------------|-----------------------------------------------|------|------------------------------------|
| 1 | internet → Business API | API keys never expire; some shared by email    | High | 90-day keys, rotation, portal-only (Ben, 22 Oct) |
| 2 | portal → Core           | other office's orders visible by changing ID   | High | ownership check per request (Ben, 18 Oct) |
| 3 | billing → webhooks      | signatures not verified                        | High | verify + reject unsigned (Cho, 20 Oct) |
| 4 | client IdP → Larder     | no alert on new federation trust               | Med  | alert + review (Eli, 30 Nov)       |
| … | 7 more (5 medium, 2 low) in the backlog with dates                                  |
"""),
    tools="tools: the C4 container diagram with boundaries marked, STRIDE (OWASP Threat Dragon or a whiteboard), the OWASP ASVS as a checklist, the backlog for findings.",
    gains=["<b>Whole-design problems</b> found, not just feature bugs.",
           "<b>Before more clients</b> depend on it.",
           "<b>Ranked, dated findings</b>.",
           "<b>An outside eye</b> sees what builders can't.",
           "<b>A repeatable step</b> for future designs."],
    losses=["<b>Two half-days</b> of senior people.",
            "<b>External reviewers</b> cost money.",
            "<b>Findings can be uncomfortable</b>.",
            "<b>Doesn't replace</b> testing and code review."],
    baseline="Each line compares <b>feature-by-feature security checks</b> to <b>reviewing the whole design at its trust boundaries with STRIDE, a checklist and an outside eye</b>.",
    ratings=[(2, 4, "Boundaries marked on one diagram."),
             (2, 4, "Mo and the clients told what was fixed."),
             (3, 4, "Findings ranked; highs fixed first."),
             (1, 5, "Three high-severity holes closed before new clients."),
             (3, 4, "Repeated for each new boundary."),
             (2, 5, "Findings, owners and dates recorded."),
             (2, 4, "Cheaper than a breach, by far."),
             (3, 3, "Two half-days per design."),
             (3, 4, "Teams fix their own findings.")],
    pitfalls=[("Only the builders", "No outside eye.", "bring someone who didn't build it."),
              ("Feature checklists only", "Gaps between features missed.", "walk the boundaries."),
              ("Findings without dates", "“We'll fix it later.”", "owner and date for every finding."),
              ("Once, ever", "Reviewed at launch, never again.", "review each new boundary.")],
    use=["Before opening a system to partners or clients.",
         "Designs that add a trust boundary.",
         "After major architecture changes.",
         "Before a client's security audit."],
    skip=["Small changes inside one trusted boundary (code review is enough)."],
    related=["<b>Data classification &amp; residency</b> (this volume)", "<b>Identity federation &amp; SSO</b> (vol. 4)", "<b>Threat modelling</b> (patterns, Vol. 5)", "<b>Validate at the boundary</b> (patterns, Vol. 5)"],
    quiz=[("What is a trust boundary?", "Where data or control passes between parties with different trust."),
          ("What does STRIDE stand for?", "Spoofing, tampering, repudiation, information disclosure, denial of service, elevation of privilege."),
          ("What were Larder's three high findings?", "Non-expiring API keys, other offices' orders reachable by ID, unsigned webhooks."),
          ("Why bring an outside reviewer?", "The builders' assumptions are exactly what they can't see.")],
    try_it="Draw your system's container diagram and mark every trust boundary. At each one, ask the six STRIDE questions and write down the weakest answer. Fix or date the worst one this month.",
    remember="Walk every <span class=\"hl\">door</span> between public and private before the <span class=\"hl\">tenants</span> move in.",
    sources=["Adam Shostack, <i>Threat Modeling: Designing for Security</i> (2014).",
             "OWASP Application Security Verification Standard (ASVS) 4.0.",
             "OWASP Top 10 (2021), A01 Broken Access Control.",
             "Loren Kohnfelder and Praerit Garg, “The threats to our products” (Microsoft, 1999), STRIDE."],
)

# ------------------------------------------------------------------ 10 Data Classification & Residency
dc_problem = Doodle(760, 280, "Doodle of 25 October 2027, a week after Antwerp opened. Lena asks a simple question: where are Belgian customers' data? Ana's first answer is the database in Frankfurt. The real answer turns out to be fourteen places, including an analytics tool storing events in the United States, a spreadsheet export on a shared drive, and a test environment with a copy of real customers.",
                    "“Where are Belgian customers' data?” First answer: Frankfurt. Real answer: fourteen places.")
dc_problem.box(20, 40, 260, 90, "Lena's question", "y", sub="“where is it?”")
dc_problem.box(320, 40, 420, 90, "14 places", "pink", sub="analytics in the US · a shared drive · test copy", stroke="red", subsize=14)
dc_problem.note(380, 200, "the copies nobody listed", "red", size=20)

dc_analogy = Doodle(760, 250, "Doodle of a doctor's practice: appointment times on the noticeboard, staff rotas in the office, patient notes in a locked cabinet, prescriptions pads in the safe. The label on each decides where it may be kept, who may see it and when it's shredded.",
                     "A doctor's practice: noticeboard, office, locked cabinet, safe. The label decides where it lives and who sees it.")
dc_analogy.icon("cabinet", 30, 60, 1.2)
for i, (t, f) in enumerate([("noticeboard", "green"), ("office", "paper"), ("cabinet", "y"), ("safe", "pink")]):
    dc_analogy.box(140 + i * 152, 60, 140, 70, t, f, size=15)
dc_analogy.note(450, 200, "the label sets the rules", "pen")

dc_how = Doodle(760, 400, "Larder's data classes from 25 October 2027, with rules per class. Public: product names and prices, anywhere. Internal: stock levels, rotas, EU or vetted vendors. Confidential: customers' names, addresses and orders: EU only, encrypted, access by role, deleted after the retention period, masked in test. Restricted: payment tokens, age-check results, staff badge data: EU only, a few named systems, every access logged. Actions: analytics moved to its EU instance by 30 November; test data masked; exports to shared drives blocked. Every table and topic tagged with its class in the data catalogue.",
                 "Four classes, rules per class. The class goes on every table and topic; the rules follow.")
for i, (c, e, r, f) in enumerate([("public", "prices, products", "anywhere", "green"), ("internal", "stock, rotas", "EU or vetted vendors", "paper"),
                                  ("confidential", "names, addresses, orders", "EU · encrypted · masked in test", "y"), ("restricted", "payment tokens, age checks", "EU · named systems · access logged", "pink")]):
    y = 14 + i * 58
    dc_how.box(14, y, 732, 50, None, f, rx=6)
    dc_how.text(30, y + 32, c, "t-head", anchor="start", size=16)
    dc_how.text(200, y + 32, e, anchor="start", size=14)
    dc_how.text(730, y + 32, r, anchor="end", size=13)
dc_how.box(14, 256, 732, 50, "analytics → EU instance · test data masked · no exports to drives", "blue", size=14)
dc_how.note(380, 346, "every table and topic tagged in the data catalogue", "pen", size=16)

DATACLASS = dict(
    slug="data-classification",
    kicker="a.k.a. “the noticeboard, the cabinet and the safe”",
    tldr="<b>Data classification</b> gives every kind of data a <b>label</b> by sensitivity (for example public, internal, confidential, restricted), and each label carries <b>rules</b>: where it may be stored (<b>residency</b>), how it's protected, who can see it, how long it's kept, whether it may be used in testing. Then you find <b>every copy</b> (databases, exports, analytics, test environments) and make the rules true. The label does the arguing, so each new design doesn't have to.",
    chips=[("Family", "security &amp; compliance"), ("Origin", "information security practice (ISO 27001); GDPR"), ("Lives in", "a classes page, tags in the data catalogue, checks in CI"), ("Pairs with", "data ownership &amp; master data, compliance by design, security architecture review")],
    problem_side="Larder, 25 October 2027",
    problem="""  <p class="lead">A week after <b>Antwerp</b> opened, Lena asks: <b>where are Belgian customers' data?</b> Ana's first answer is the database in Frankfurt. The real answer is <b>fourteen places</b>, including the product <b>analytics tool</b> storing events in the United States, a <b>spreadsheet export</b> on a shared drive, and a <b>test environment</b> holding a copy of real customers. <span class="hl-pink">Nobody had listed the copies.</span></p>
  <ul>
    <li>Data spreads into tools, exports and test copies.</li>
    <li>Without labels, every design argues protection from scratch.</li>
    <li>Residency rules apply to every copy, not just the main database.</li>
  </ul>""",
    problem_figs=[dc_problem],
    analogy_side="the doctor's practice",
    analogy="""  <p>A doctor's practice keeps <b>appointment times</b> on the noticeboard, <b>staff rotas</b> in the office, <b>patient notes</b> in a locked cabinet and <b>prescription pads</b> in the safe. Nobody debates each sheet of paper: its <b>label</b> decides where it may be kept, who may see it and when it's shredded.</p>""",
    analogy_figs=[dc_analogy],
    map=[("The noticeboard", "Public: products and prices"),
         ("The office", "Internal: stock levels, rotas"),
         ("The locked cabinet", "Confidential: customers' names, addresses, orders"),
         ("The safe", "Restricted: payment tokens, age-check results"),
         ("Shredding dates", "Retention per class")],
    how_side="four labels, rules per label, every copy found",
    how="""  <p>Ana and Lena agreed <b>four classes</b> with rules: <b>public</b> anywhere; <b>internal</b> in the EU or vetted vendors; <b>confidential</b> (customer names, addresses, orders) EU only, encrypted, access by role, <b>masked in test</b>, deleted after retention; <b>restricted</b> (payment tokens, age-check results, staff badges) EU only, named systems, <b>every access logged</b>. The inventory found 14 stores of customer data: analytics moved to its <b>EU instance</b> by 30 November, test data masked, exports to shared drives blocked. Every table and topic now carries its class.</p>""",
    how_figs=[dc_how],
    steps=[("Agree three to five classes", "With legal; plain names and examples."),
           ("Write rules per class", "Location, encryption, access, retention, test use."),
           ("Find every copy", "Databases, topics, tools, exports, backups, test environments."),
           ("Tag data with its class", "In the catalogue, on tables, topics and fields."),
           ("Fix the gaps", "Move, mask, delete or block, with dates."),
           ("Check new designs", "The class decides; a CI check for new tables.")],
    vocab=[("Data classification", "Labelling data by how sensitive it is."),
           ("Data residency", "Where (which country or region) data is stored."),
           ("Personal data", "Information about an identifiable person (GDPR)."),
           ("Data masking", "Replacing real values with realistic fakes for testing."),
           ("Retention period", "How long data is kept before deletion."),
           ("Data catalogue", "A list of datasets with owners, classes and locations.")],
    code=dict(file="docs/security/data-classes.md", note="the data classes page, October 2027", plain=True, src="""
# Data classes                                   agreed 25 Oct 2027 · Ana, Lena · owner per dataset in the catalogue

| Class        | Examples                                   | Where          | Protection                    | Test use | Retention    |
|--------------|--------------------------------------------|----------------|-------------------------------|----------|--------------|
| Public       | products, prices, store hours              | anywhere       | integrity only                | yes      | —            |
| Internal     | stock levels, rotas, routes                | EU / vetted    | access by role                | yes      | per dataset  |
| Confidential | customers' names, addresses, orders, office managers | EU only | encrypted, access by role | masked  | 2 yrs after last order |
| Restricted   | payment tokens, age-check results, badge data | EU only, named systems | encrypted, every access logged | never | minimum by law |

Inventory 25 Oct: 14 stores of customer data. Gaps → product analytics (US) → EU instance (30 Nov);
staging copy of customers → masked (15 Nov); CSV exports on shared drive → blocked + deleted (1 Nov).
CI: new tables and topics must declare a class (fitness function FF-09).
"""),
    tools="tools: a data catalogue (DataHub, OpenMetadata, or a simple sheet), cloud tags, masking tools for test data, DLP rules on shared drives, a CI check for class tags.",
    gains=["<b>Lena's question answered</b>, for every copy.",
           "<b>Rules decided once</b>, applied everywhere.",
           "<b>Residency</b> handled before regulators ask.",
           "<b>Safer test data</b>.",
           "<b>Faster designs</b>: the class decides."],
    losses=["<b>The inventory takes weeks</b>.",
            "<b>Tags drift</b> without checks.",
            "<b>Some tools</b> must be replaced or reconfigured.",
            "<b>Masked test data</b> is harder to build."],
    baseline="Each line compares <b>protecting data case by case, with unknown copies</b> to <b>four classes with rules, every copy found and tagged, and checks for new data</b>.",
    ratings=[(2, 5, "Four labels anyone can apply."),
             (2, 5, "Lena, Grace and Ana use the same classes."),
             (2, 4, "New designs inherit the rules."),
             (1, 5, "US analytics and real test data fixed."),
             (3, 4, "Classes stay; systems change."),
             (2, 5, "Every table and topic tagged."),
             (3, 3, "Neutral."),
             (3, 3, "An inventory, then upkeep."),
             (3, 4, "Teams tag their own data.")],
    pitfalls=[("Too many classes", "Nine levels nobody remembers.", "three to five, with examples."),
              ("Main database only", "Copies in tools and tests ignored.", "inventory every copy."),
              ("Labels without rules", "“Confidential” changes nothing.", "rules per class."),
              ("One-off exercise", "New tables untagged.", "a CI check for new data.")],
    use=["Entering a new country or market.",
         "Before a privacy audit or a client's questionnaire.",
         "Adding analytics, AI or reporting tools.",
         "When test environments use production data."],
    skip=["Never entirely; even a small product holds personal data."],
    related=["<b>Compliance by design</b> (this volume)", "<b>Data ownership &amp; master data</b> (vol. 4)", "<b>Envelope encryption</b> (patterns, Vol. 5)", "<b>Least privilege</b> (patterns, Vol. 5)"],
    quiz=[("What does a data class carry?", "Rules: where data may live, protection, access, retention and test use."),
          ("What did Larder's inventory find?", "Fourteen stores of customer data, including US analytics and a real test copy."),
          ("What is data residency?", "Which country or region the data is stored in."),
          ("How do new tables get a class?", "A CI check requires every new table and topic to declare one.")],
    try_it="Pick one kind of personal data in your product (say, addresses). Find every place it's stored, including tools, exports, backups and test environments. Give it a class, write its rules, and list the copies that break them.",
    remember="<span class=\"hl\">Label</span> the paper; the label decides the <span class=\"hl\">cabinet</span>.",
    sources=["ISO/IEC 27001:2022, Annex A 5.12 Classification of information.",
             "Regulation (EU) 2016/679 (GDPR), Articles 5, 25 and 44–49.",
             "European Data Protection Board, Recommendations 01/2020 on transfers.",
             "NIST SP 800-60, <i>Guide for Mapping Types of Information to Security Categories</i>."],
)

# ------------------------------------------------------------------ 11 Compliance by Design
cd_problem = Doodle(760, 280, "Doodle of November 2027. Antwerp brings new rules: Belgian e-invoicing for business customers, beer and wine for 16-year-olds but spirits only from 18, and more deletion requests in French. Today compliance is a yearly scramble: Sam's team deletes customers by hand in nine systems, and Lena collects evidence for auditors from screenshots.",
                    "New Belgian rules, and compliance today is a yearly scramble: deletions by hand in nine systems, evidence from screenshots.")
cd_problem.box(20, 40, 220, 90, "e-invoicing", "paper", sub="Belgian B2B")
cd_problem.box(270, 40, 220, 90, "age 16 / 18", "paper", sub="beer vs spirits")
cd_problem.box(520, 40, 220, 90, "deletions", "pink", sub="by hand, 9 systems")
cd_problem.note(380, 200, "evidence from screenshots, once a year", "red", size=19)

cd_analogy = Doodle(760, 250, "Doodle of a modern lift: the building code isn't checked by an inspector once a year looking for problems. The lift itself won't move with the doors open or overloaded, and it logs every service and fault, so the inspector reads the log.",
                     "A lift won't move with its doors open, and logs every fault. The inspector reads the log.")
cd_analogy.icon("switch", 30, 60, 1.3)
cd_analogy.box(150, 50, 280, 100, "built-in rules", "green", sub="won't move with doors open")
cd_analogy.box(460, 50, 280, 100, "the log", "blue", sub="the inspector reads it")
cd_analogy.note(450, 210, "the rule is in the machine", "pen")

cd_how = Doodle(760, 400, "Larder's compliance features from 8 November 2027. Each rule becomes a platform feature with automatic evidence. Age checks: the courier app asks for an ID check at the door for age-restricted items, using the city's rule (16 or 18), and stores only checked yes or no. Deletion: one customer erasure event that all nine systems act on, with a report of who confirmed. Retention: per data class, as configuration, with a nightly job. E-invoicing: business invoices in Belgium sent through the billing service in the required structured format. Evidence: a compliance page generated weekly for Lena.",
                 "Each rule becomes a platform feature that also produces its own evidence.")
for i, (rule, feat, f) in enumerate([("age 16 / 18 by city", "courier app ID check, stores yes/no", "y"), ("right to erasure", "one erasure event → 9 systems confirm", "blue"),
                                     ("retention", "per class, config + nightly job", "green"), ("Belgian e-invoices", "billing service, structured format", "paper")]):
    y = 14 + i * 62
    cd_how.box(14, y, 260, 52, rule, "pink", size=14, rx=6)
    cd_how.arrow(278, y + 26, 320, y + 26)
    cd_how.box(324, y, 422, 52, feat, f, size=14, rx=6)
cd_how.box(14, 270, 732, 50, "evidence: a compliance page generated weekly for Lena", "green", size=15)
cd_how.note(380, 358, "deletions: 3 days by hand → 4 hours, automatically", "pen", size=16)

COMPLIANCE = dict(
    slug="compliance-by-design",
    kicker="a.k.a. “the lift that won't move”",
    tldr="<b>Compliance by design</b> turns legal and regulatory rules into <b>platform features</b> (checks, events, configuration, jobs) instead of manual procedures and yearly audits. Each rule gets an owner, a feature that enforces it, and <b>automatic evidence</b> that it works. New markets then mean new configuration, not new scrambles. It's privacy by design (GDPR Article 25) applied to every rule.",
    chips=[("Family", "security &amp; compliance"), ("Origin", "privacy by design (Ann Cavoukian, 1990s; GDPR Art. 25); compliance as code"), ("Lives in", "the platform's features and a rules register with Lena"), ("Pairs with", "data classification, a city is configuration (ADR 0003), audit logging")],
    problem_side="Larder, 8 November 2027",
    problem="""  <p class="lead">Antwerp brings new rules: <b>structured e-invoices</b> for Belgian business customers, <b>beer and wine from 16 but spirits from 18</b> (the Netherlands: 18 for all), and more deletion requests. Today compliance is a <b>yearly scramble</b>: Sam's team deletes customers <b>by hand in nine systems</b> (about three days a month), and Lena collects audit evidence from <span class="hl-pink">screenshots</span>.</p>
  <ul>
    <li>Manual procedures fail quietly as volume grows.</li>
    <li>Each new country multiplies the procedures.</li>
    <li>Evidence collected once a year proves little.</li>
  </ul>""",
    problem_figs=[cd_problem],
    analogy_side="the lift that won't move",
    analogy="""  <p>A modern <b>lift</b> isn't kept safe by an inspector hunting for problems once a year. The lift itself <b>won't move with the doors open</b> or overloaded, and it <b>logs</b> every service and fault. The rule is built into the machine; the inspector reads the log.</p>""",
    analogy_figs=[cd_analogy],
    map=[("The building code", "GDPR, Belgian VAT, age rules"),
         ("Won't move with the doors open", "The courier app won't complete delivery without an age check"),
         ("The lift's log", "The weekly compliance page"),
         ("The inspector", "Lena and the auditors"),
         ("A new building, same lift", "A new city: new configuration, same features")],
    how_side="each rule a feature, with its own evidence",
    how="""  <p>Ana and Lena listed the rules and made each a <b>feature</b>. <b>Age checks</b>: the courier app asks for an ID check at the door for age-restricted items, using the city's rule (16 or 18), and stores only <b>“checked: yes/no”</b>. <b>Erasure</b>: one <b>customer.erasure.requested</b> event all nine systems act on, with a confirmation report. <b>Retention</b>: per data class, as configuration, with a nightly job. <b>E-invoices</b>: Belgian business invoices sent by the billing service in the required format. A <b>compliance page</b> is generated weekly for Lena. Deletions went from three days by hand to <b>four hours, automatically</b>.</p>""",
    how_figs=[cd_how],
    steps=[("List the rules", "With legal: law, contracts, standards; per country."),
           ("Give each an owner", "Who answers for it."),
           ("Turn each into a feature", "A check, an event, a setting or a job."),
           ("Make it configuration per market", "Age 16 or 18 is a city setting."),
           ("Produce evidence automatically", "Logs and reports, not screenshots."),
           ("Review with legal quarterly", "New rules, changed rules, failures.")],
    vocab=[("Compliance by design", "Building rules into the system instead of procedures around it."),
           ("Privacy by design", "Data protection built in from the start (GDPR Art. 25)."),
           ("Right to erasure", "A person's right to have their data deleted (GDPR Art. 17)."),
           ("Retention policy", "How long each kind of data is kept."),
           ("E-invoicing", "Invoices in a structured, machine-readable format."),
           ("Evidence", "Records that show a control works.")],
    code=dict(file="docs/compliance/rules-register.md", note="the rules register, November 2027", plain=True, src="""
# Rules register                                       owners: Lena (legal), Ana (platform) · reviewed quarterly

| Rule                            | Where   | Feature                                        | Evidence                   | Owner |
|---------------------------------|---------|------------------------------------------------|----------------------------|-------|
| Age: beer/wine 16, spirits 18   | BE      | courier app ID check; city setting; stores y/n | weekly: checks per delivery | Eli   |
| Age: all alcohol 18             | NL      | same feature, city setting 18                  | same                       | Eli   |
| Right to erasure (GDPR 17)      | all     | customer.erasure.requested → 9 systems confirm | report per request         | Ben   |
| Retention per data class        | all     | config + nightly deletion job                  | job log, counts per class  | Eli   |
| Structured e-invoices (B2B)     | BE      | billing service, structured format             | delivery receipts          | Cho   |
| Data stays in the EU            | all     | data classes + region checks in CI             | weekly scan                | Ana   |

Erasure before: ≈ 3 days/month by hand in 9 systems. After (from 6 Dec): ≈ 4 hours, automatic.
"""),
    tools="tools: the event backbone for erasure, configuration per city (ADR 0003), scheduled jobs, audit logs, a generated compliance page; a rules register with legal.",
    gains=["<b>Rules enforced</b> every time, not remembered.",
           "<b>New markets</b> become configuration.",
           "<b>Evidence for free</b>: Lena reads a page.",
           "<b>Days of manual work</b> saved monthly.",
           "<b>Less personal data stored</b> (yes/no, not IDs)."],
    losses=["<b>Engineering effort</b> up front.",
            "<b>Rules change</b>; features must follow.",
            "<b>Legal and engineering</b> must work closely.",
            "<b>Bugs in a control</b> fail at scale."],
    baseline="Each line compares <b>manual procedures and yearly evidence gathering</b> to <b>rules as platform features, configured per market, with automatic evidence</b>.",
    ratings=[(2, 4, "One register: rule, feature, evidence, owner."),
             (2, 5, "Lena and the engineers share one list."),
             (2, 4, "Antwerp's rules are settings."),
             (1, 5, "Rules enforced in software, every delivery."),
             (2, 5, "Eindhoven and the next country: configuration."),
             (2, 5, "Weekly evidence, not screenshots."),
             (2, 4, "Three days a month of deletions saved."),
             (3, 3, "Upfront work, then little upkeep."),
             (3, 4, "Teams own their rule's feature.")],
    pitfalls=[("Procedures first", "A wiki page instead of a check.", "make the system enforce it."),
              ("Storing too much", "Scanning and keeping ID cards.", "store the fact (yes/no), not the document."),
              ("Hard-coded rules", "Age 18 in the code.", "per market configuration."),
              ("No evidence", "It works, nobody can show it.", "generate evidence automatically.")],
    use=["Entering a new country or regulated market.",
         "When manual compliance work grows with volume.",
         "Before audits and client questionnaires.",
         "Designing features that touch personal data or regulated goods."],
    skip=["One-off obligations that won't recur (a manual step may be fine)."],
    related=["<b>Data classification &amp; residency</b> (this volume)", "<b>Constraints vs assumptions</b> (vol. 1)", "<b>Audit logging</b> (patterns, Vol. 5)", "<b>Working with legal &amp; privacy</b> (Grace, book 2 vol. 5)"],
    quiz=[("What does compliance by design mean?", "Turning rules into platform features with automatic evidence."),
          ("How does Larder handle different age rules?", "A city setting (16 or 18) used by the courier app's ID check."),
          ("What does the age check store?", "Only “checked: yes/no”, not the ID document."),
          ("What did automatic erasure change?", "Three days a month by hand became four hours, automatically.")],
    try_it="List three rules your system must follow and how each is enforced today. For the most manual one, sketch the feature that would enforce it and the evidence it would produce automatically.",
    remember="Build the rule into the <span class=\"hl\">lift</span>; let the inspector read the <span class=\"hl\">log</span>.",
    sources=["Regulation (EU) 2016/679 (GDPR), Article 25 (data protection by design) and Article 17.",
             "Ann Cavoukian, “Privacy by Design: The 7 Foundational Principles” (2009).",
             "Belgian Federal Public Service Finance, structured e-invoicing obligation for B2B (from 2026).",
             "Belgian law on alcohol sales to minors (Law of 10 December 2009)."],
)

NOTES = [REVIEW, DATACLASS, COMPLIANCE]
