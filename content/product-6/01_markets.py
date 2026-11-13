# Series 2 · Book 2 · The Product Owner's Notebook · Vol. 6 · New markets.
# Narrator: Grace. Running case study: Larder (facts in docs/larder-casebook.md).

# ------------------------------------------------------------------ 01 Launching a New City
nc_problem = Doodle(760, 280, "Doodle of April 2027. Utrecht opens on 12 April, The Hague in June, Antwerp in the autumn. Rotterdam's launch a year ago took Grace's team six weeks of app work, a long checklist and a lot of memory. Nobody wrote down what was configuration, what was local, and what to watch in the first weeks.",
                    "Three openings this year. Rotterdam's launch lived in people's memory.")
for i, (t, s, f) in enumerate([("Utrecht", "12 Apr", "y"), ("The Hague", "June", "paper"), ("Antwerp", "autumn", "paper")]):
    nc_problem.box(20 + i * 250, 40, 220, 80, t, f, sub=s, size=17)
nc_problem.note(380, 200, "every launch from memory", "red", size=20)

nc_analogy = Doodle(760, 250, "Doodle of a restaurant chain opening a new branch: the recipe book and kitchen layout are the same everywhere; the local part is the menu's specials, the suppliers and the opening hours; and the first month has a checklist of what to watch every evening.",
                     "A new branch: same recipe book, local specials, and a first-month checklist every evening.")
nc_analogy.icon("store", 30, 60, 1.2)
for i, (t, s, f) in enumerate([("recipe book", "the same", "green"), ("specials", "local", "y"), ("first month", "watched nightly", "blue")]):
    nc_analogy.box(150 + i * 200, 50, 186, 90, t, f, sub=s, size=16)
nc_analogy.note(450, 205, "repeat the core, adapt the edge", "pen")

nc_how = Doodle(760, 400, "Grace's city playbook, written from Rotterdam's lessons for Utrecht, 5 April 2027. Configuration, the same everywhere: zones, slots, prices, opening hours, set in the admin tool, no code. Local: store layout in the picker app, first-week offers, local help pages, partners. Launch: staff orders a week before, waitlist push on the day, hypercare for two weeks. Watch daily: orders, on time, swap refunds, tickets per 100 orders, second orders within 14 days. Utrecht: app ready in 6 days of work instead of 6 weeks.",
                 "Configuration the same, local edges, a launch rhythm, and five numbers watched daily. 6 weeks of app work → 6 days.")
nc_how.box(14, 14, 360, 120, None, "green")
nc_how.head(194, 44, "configuration (same)", size=15)
nc_how.text(194, 76, "zones · slots · prices", size=14)
nc_how.text(194, 104, "hours · in the admin tool", size=14)
nc_how.box(386, 14, 360, 120, None, "y")
nc_how.head(566, 44, "local (different)", size=15)
nc_how.text(566, 76, "store layout · offers", size=14)
nc_how.text(566, 104, "help pages · partners", size=14)
nc_how.box(14, 152, 732, 50, "staff orders −7 days · waitlist push · 2 weeks hypercare", "blue", size=14)
nc_how.box(14, 220, 732, 50, "watch daily: orders · on time · swap refunds · tickets · 2nd orders", "paper", size=13)
nc_how.note(380, 312, "Utrecht app work: 6 weeks → 6 days", "green", size=17)

CITY = dict(
    slug="launching-new-city",
    kicker="a.k.a. “the new branch”",
    tldr="Launching a new city (or store, or region) gets cheaper and safer when it's a <b>playbook</b>, not a project. Separate what's <b>configuration</b> (the same everywhere, set without code) from what's <b>local</b> (store layout, offers, partners, help pages), give the launch a fixed <b>rhythm</b> (staff orders, waitlist, hypercare), and agree the <b>few numbers</b> to watch daily in the first weeks. Update the playbook after every launch.",
    chips=[("Family", "new markets"), ("Origin", "franchise and roll-out practice; Larder's ADR 0003 (a city is configuration)"), ("Lives in", "a city playbook, updated after every launch"), ("Pairs with", "launch checklist, hypercare, capability map (Ana)")],
    problem_side="Larder, 5 April 2027",
    problem="""  <p class="lead"><b>Utrecht</b> opens on 12 April, <b>The Hague</b> in June, <b>Antwerp</b> in the autumn. Rotterdam's launch a year ago took Grace's team <b>six weeks of app work</b>, a long checklist and a lot of memory. <span class="hl-pink">Nobody wrote down</span> what was configuration, what was local, and what to watch in the first weeks.</p>
  <ul>
    <li>Launches from memory repeat old mistakes.</li>
    <li>Product work per city doesn't scale to six cities.</li>
    <li>The first weeks decide whether customers come back.</li>
  </ul>""",
    problem_figs=[nc_problem],
    meanwhile=[("architect-4", "capability-map", "a month earlier, Ana's capability map marked “city setup” red for 2027.",
                "A month later, Grace's city playbook turned Utrecht's app work from six weeks into six days.")],
    analogy_side="the new branch",
    analogy="""  <p>A restaurant chain opening a new branch uses the same <b>recipe book</b> and kitchen layout everywhere. What's <b>local</b> is the specials board, the suppliers and the opening hours. And for the <b>first month</b>, the manager checks a few things every evening: covers, waiting times, complaints, who comes back.</p>""",
    analogy_figs=[nc_analogy],
    map=[("The recipe book", "Configuration: zones, slots, prices, hours"),
         ("Specials and suppliers", "Store layout, first-week offers, partners"),
         ("The opening night", "Staff orders, waitlist push, hypercare"),
         ("Checks every evening", "Five numbers watched daily"),
         ("Who comes back", "Second orders within 14 days")],
    how_side="configuration, local edges, rhythm, five numbers",
    how="""  <p>Grace wrote a <b>city playbook</b> from Rotterdam's lessons. <b>Configuration</b> is the same everywhere and set in the admin tool: zones, slots, prices, hours (ADR 0003). <b>Local</b>: store layout in the picker app, first-week offers, help pages, partners. A fixed <b>rhythm</b>: staff orders a week before, the waitlist push on the day, two weeks of hypercare. <b>Five numbers</b> watched daily: orders, on time, swap refunds, tickets per 100 orders, second orders within 14 days. Utrecht's app work: <b>six days instead of six weeks</b>.</p>""",
    how_figs=[nc_how],
    steps=[("List last launch's work", "Every task, from the checklist and memory."),
           ("Sort: configuration or local", "Push everything you can into configuration."),
           ("Fix the rhythm", "Staff orders, waitlist, opening, hypercare."),
           ("Choose the first-week numbers", "Five, watched daily."),
           ("Run it, then update it", "A short review after every launch."),
           ("Give it an owner", "Someone keeps the playbook current.")],
    vocab=[("Playbook", "A repeatable, written way to do something."),
           ("Configuration", "Settings changed without code."),
           ("Localisation", "Adapting to a place: language, rules, habits."),
           ("Hypercare", "Extra support right after a launch."),
           ("Activation", "A new customer's first good experience."),
           ("Second-order rate", "Share of new customers who order again.")],
    code=dict(file="product/cities/playbook.md", note="the city playbook, v1 for Utrecht, April 2027", plain=True, src="""
# City playbook · v1 (Utrecht) · owner: Grace with Sanne and Joost

CONFIGURATION (admin tool, no code)   zones · slots · prices + VAT · opening hours · payment methods
LOCAL                                 store layout (picker app) · first-week offers · help pages ·
                                      local partners · press
RHYTHM   −7 days  staff orders (all departments)       day 0   waitlist push, Grace + Ben in store
         +14 days hypercare daily 09:00 (exit: tickets < 3 per 100 for 2 days, no P1 for 5)
WATCH DAILY (first 4 weeks)   orders · on time · swap refunds · tickets per 100 · 2nd order ≤ 14 days
Utrecht (12 Apr): app work 6 days (Rotterdam: 6 weeks) · week 1 tickets 2.9 per 100 · 2nd orders 46 %
Updated after: The Hague (v2, Jun) · Antwerp (v3, Oct: + language, rules, currency checks)
"""),
    tools="tools: the admin tool for configuration, a playbook page, the launch checklist, a first-weeks dashboard.",
    gains=["<b>Launches in days</b> of product work.",
           "<b>Lessons kept</b> between launches.",
           "<b>Calm openings</b>: a known rhythm.",
           "<b>Early warnings</b> from five numbers.",
           "<b>Others can run it</b>, not just Grace."],
    losses=["<b>Upfront work</b> to configure everything.",
            "<b>Local surprises</b> still happen.",
            "<b>Playbooks go stale</b> without updates.",
            "<b>Not every market</b> fits the same mould."],
    baseline="Each line compares <b>launching each city as a project from memory</b> to <b>a playbook of configuration, local edges, a rhythm and five daily numbers</b>.",
    ratings=[(2, 4, "Customers in a new city get a polished app on day one."),
             (2, 5, "Cities open faster and cheaper."),
             (2, 4, "Five numbers, from day one."),
             (2, 4, "Problems seen in the first week."),
             (2, 4, "Product work spent on what's really local."),
             (2, 4, "Sanne, Joost and the team share one playbook."),
             (2, 4, "Femke trusts the city dates."),
             (2, 5, "Six days of app work."),
             (2, 4, "One page, updated after each launch.")],
    pitfalls=[("Everything local", "Each city coded by hand.", "push it into configuration."),
              ("No first-week numbers", "Problems found in month two.", "five numbers, daily."),
              ("Never updated", "v1 forever.", "a review after every launch."),
              ("Copy-paste abroad", "A country treated as a city.", "add language, rules and money checks.")],
    use=["Opening cities, stores, regions.",
         "Rolling out a product to new customer groups.",
         "Any launch you'll do more than twice.",
         "After a launch that went badly."],
    skip=["A one-off launch you'll never repeat."],
    related=["<b>Launch checklist</b> (Vol. 3)", "<b>Hypercare</b> (Vol. 3)", "<b>Localisation for a new country</b> (this volume)", "<b>Capability map</b> (Ana, book 1 vol. 4)"],
    quiz=[("What are the playbook's four parts?", "Configuration, local edges, a launch rhythm, and daily numbers."),
          ("What's configuration at Larder?", "Zones, slots, prices, hours and payment methods, set without code."),
          ("Which five numbers are watched?", "Orders, on time, swap refunds, tickets per 100, second orders within 14 days."),
          ("What changed for Utrecht?", "App work fell from six weeks to six days.")],
    try_it="List everything your last launch needed. Mark each item configuration or local, and write the five numbers you'd watch daily for the first month next time.",
    remember="Same <span class=\"hl\">recipe book</span>, local <span class=\"hl\">specials</span>, and a checklist every evening.",
    sources=["Melissa Perri, <i>Escaping the Build Trap</i> (2018).",
             "Reed Hastings and Erin Meyer, <i>No Rules Rules</i> (2020), on context over control.",
             "Sean Ellis and Morgan Brown, <i>Hacking Growth</i> (2017), activation.",
             "Atul Gawande, <i>The Checklist Manifesto</i> (2009)."],
)

# ------------------------------------------------------------------ 02 Localisation for a New Country
lo_problem = Doodle(760, 280, "Doodle of August 2027. The French version of the app shipped in May, translated. In July, forty Antwerp households tested it, and the problems weren't the words: Belgian Dutch product names that sound odd to Flemish customers, prices that didn't show Belgian VAT correctly, a curt French swap message, and 212 products whose names and VAT differed between systems.",
                    "French shipped in May. Antwerp testers found the problems weren't the words.")
for i, (t, f) in enumerate([("Flemish names", "y"), ("Belgian VAT", "pink"), ("curt French", "y"), ("212 products", "pink")]):
    lo_problem.box(14 + i * 184, 40, 174, 70, t, f, size=15)
lo_problem.note(380, 190, "translated, not localised", "red", size=20)

lo_analogy = Doodle(760, 250, "Doodle of a cookbook adapted for another country: not just translated, but with local measures, ingredients you can actually buy there, the oven temperatures people use, and recipes tested in a local kitchen.",
                     "A cookbook adapted for another country: local measures, ingredients you can buy, tested in a local kitchen.")
lo_analogy.icon("recipe", 40, 60, 1.3)
for i, (t, f) in enumerate([("measures", "y"), ("ingredients", "green"), ("local kitchen", "blue")]):
    lo_analogy.box(170 + i * 190, 60, 176, 70, t, f, size=16)
lo_analogy.note(450, 200, "translated is not the same as local", "pen")

lo_how = Doodle(760, 400, "Grace's localisation checklist for Belgium, 2 August 2027. Language: French and Flemish Dutch, written by native writers, tone checked with testers. Money and tax: Belgian VAT on prices and invoices, Bancontact first. Rules: age limits per city. Products: names and VAT from one master, the catalogue, owned by Grace's team, with French and Dutch names. Habits: bigger weekend slot orders, different substitution expectations. Testing: forty Antwerp households before launch, a second round in September. Antwerp opened on 18 October with tickets at 2.4 per 100 in week one.",
                 "Language, money, rules, products, habits, and testing with local customers. Antwerp week one: 2.4 tickets per 100.")
for i, (t, s, f) in enumerate([("language", "FR + Flemish, native", "y"), ("money", "BE VAT · Bancontact", "green"), ("rules", "age by city", "pink"),
                               ("products", "one master, FR/NL names", "blue"), ("habits", "weekend slots", "paper"), ("testing", "40 households, twice", "green")]):
    r, c = divmod(i, 3)
    lo_how.box(14 + c * 248, 14 + r * 104, 236, 92, t, f, sub=s, size=17, subsize=13)
lo_how.note(380, 256, "212 product mismatches fixed in the catalogue", "pen", size=16)
lo_how.note(380, 290, "Antwerp opened 18 Oct · week 1: 2.4 tickets per 100", "green", size=16)

LOCAL = dict(
    slug="localisation",
    kicker="a.k.a. “the cookbook for another country”",
    tldr="<b>Localisation</b> is more than translation. A new country brings <b>language</b> (with the right tone and dialect), <b>money and tax</b>, <b>rules</b>, <b>product data</b>, and <b>habits</b>. Work through each, get product data right at its <b>source</b>, and above all <b>test with local customers</b> before launch, more than once. The problems customers notice are rarely the words.",
    chips=[("Family", "new markets"), ("Origin", "internationalisation (i18n) and localisation (l10n) practice"), ("Lives in", "a country checklist and the city playbook"), ("Pairs with", "launching a new city, data ownership &amp; master data (Ana), compliance by design")],
    problem_side="Larder, 2 August 2027",
    problem="""  <p class="lead">The <b>French</b> version of the app shipped in May, translated. In July, <b>forty Antwerp households</b> tested it, and the problems weren't the words: product names in Netherlands Dutch that sound odd to <b>Flemish</b> customers, prices not showing <b>Belgian VAT</b> correctly, a <b>curt</b> French swap message, and <b>212 products</b> whose names and VAT differed between systems. <span class="hl-pink">Translated, not localised.</span></p>
  <ul>
    <li>Translation fixes words, not prices, rules or tone.</li>
    <li>Product data errors multiply across systems.</li>
    <li>Only local customers notice what feels foreign.</li>
  </ul>""",
    problem_figs=[lo_problem],
    meanwhile=[("architect-4", "data-ownership", "the same week, Ana's ADR 0024 makes the catalogue the single master for product names and VAT.",
                "The same week, Grace's Antwerp testers found the 212 product mismatches that ADR 0024 fixes.")],
    analogy_side="the cookbook for another country",
    analogy="""  <p>A good cookbook adapted for another country isn't just translated. It uses <b>local measures</b>, <b>ingredients you can actually buy</b> there, the oven temperatures people use, and every recipe is <b>tested in a local kitchen</b>. Otherwise the words are right and the cake is wrong.</p>""",
    analogy_figs=[lo_analogy],
    map=[("Local measures", "Belgian VAT, euro formats, Bancontact"),
         ("Ingredients you can buy", "Products with French and Flemish names, one master"),
         ("Tone of the recipe", "The swap message in polite French"),
         ("A local kitchen", "Forty Antwerp households, twice"),
         ("The words right, the cake wrong", "Translated, not localised")],
    how_side="language, money, rules, products, habits, testing",
    how="""  <p>Grace made a <b>country checklist</b>. <b>Language</b>: French and Flemish Dutch by native writers, tone checked with testers. <b>Money and tax</b>: Belgian VAT on prices and invoices, Bancontact first. <b>Rules</b>: age limits by city. <b>Products</b>: names and VAT from <b>one master</b>, the catalogue her team owns, with French and Dutch names (the 212 mismatches fixed there). <b>Habits</b>: bigger weekend slot orders. <b>Testing</b>: forty households in July, again in September. Antwerp opened on <b>18 October</b>: <b>2.4 tickets per 100</b> orders in week one.</p>""",
    how_figs=[lo_how],
    steps=[("Language, with native writers", "Dialect and tone, not just words."),
           ("Money and tax", "Prices, VAT, invoices, payment methods."),
           ("Rules", "Age limits, consumer law, data rules."),
           ("Product data at the source", "One master, every language."),
           ("Habits", "How people shop, when, and what they expect."),
           ("Test with local customers", "Before launch, twice.")],
    vocab=[("Internationalisation (i18n)", "Building so a product can be adapted."),
           ("Localisation (l10n)", "Adapting it to a specific place."),
           ("Locale", "Language plus region, e.g. nl-BE, fr-BE."),
           ("Master data", "The single source for shared data like products."),
           ("Tone of voice", "How the product sounds, beyond the words."),
           ("Beta test", "Real customers trying it before launch.")],
    code=dict(file="product/countries/belgium.md", note="the Belgium checklist, August 2027", plain=True, src="""
# Country checklist: Belgium (Antwerp, opening 18 Oct 2027) · owner: Grace

Language  fr-BE, nl-BE by native writers · tone reviewed with testers (swap message rewritten)
Money     prices incl. Belgian VAT (6 % / 21 %) · invoices in Belgian format · Bancontact first
Rules     age checks per city setting (BE: 16 beer/wine, 18 spirits) · consumer law: help pages (Lena)
Products  names + VAT category from the catalogue (master, ADR 0024) · 212 mismatches fixed by 30 Aug
Habits    more weekend slot orders · substitutions: "same brand or nothing" more common (flag default?)
Testing   40 Antwerp households, 12–23 Jul (round 1) · 9–20 Sep (round 2: 6 issues, all fixed)
Week 1    2.4 tickets per 100 orders (Rotterdam week 1: 7.1)
"""),
    tools="tools: native writers, a translation management system, locale settings, the catalogue as product master, a local beta group.",
    gains=["<b>A product that feels local</b>.",
           "<b>Correct prices and tax</b>.",
           "<b>Clean product data</b> everywhere.",
           "<b>Fewer tickets</b> at launch.",
           "<b>A checklist</b> for the next country."],
    losses=["<b>Native writers and testers</b> cost money.",
            "<b>Two rounds of testing</b> take time.",
            "<b>More languages</b> to maintain.",
            "<b>Some habits</b> need product changes."],
    baseline="Each line compares <b>translating the app</b> to <b>localising language, money, rules, product data and habits, tested with local customers</b>.",
    ratings=[(1, 5, "Antwerp customers got a product that felt local."),
             (2, 4, "2.4 tickets per 100 in week one, not 7."),
             (2, 4, "Problems found by testers, not complaints."),
             (2, 4, "Two test rounds before launch."),
             (3, 3, "Neutral."),
             (2, 4, "One checklist for the whole team."),
             (2, 4, "Femke's first country opened smoothly."),
             (3, 4, "Fixes made before launch."),
             (3, 3, "Writers and testers to organise.")],
    pitfalls=[("Translation only", "Machine-translated strings.", "native writers, tone checked."),
              ("Fixing data downstream", "Names corrected in the app.", "fix it at the master."),
              ("One country, one language", "French only in Belgium.", "check every language spoken."),
              ("No local testing", "Launch is the test.", "local customers, twice.")],
    use=["Entering a new country or language.",
         "Serving a region with different rules or habits.",
         "When translated products underperform.",
         "Before marketing abroad."],
    skip=["Markets with the same language, money and rules (a city playbook is enough)."],
    related=["<b>Launching a new city</b> (this volume)", "<b>Data ownership &amp; master data</b> (Ana, book 1 vol. 4)", "<b>Compliance by design</b> (Ana, book 1 vol. 5)", "<b>Prototype testing with users</b> (Vol. 1)"],
    quiz=[("What does localisation cover beyond language?", "Money and tax, rules, product data, habits."),
          ("Where were the 212 product mismatches fixed?", "In the catalogue, the single master (ADR 0024)."),
          ("How was it tested?", "Forty Antwerp households, in two rounds."),
          ("How did Antwerp's first week compare?", "2.4 tickets per 100 orders, against Rotterdam's 7.1.")],
    try_it="Pick a market you serve or plan to. Go through language, money, rules, product data and habits, writing one risk for each, and recruit five local customers to try the product this month.",
    remember="Adapt the <span class=\"hl\">cookbook</span>; test it in a <span class=\"hl\">local kitchen</span>.",
    sources=["W3C, “Localization vs. Internationalization” (w3.org/International).",
             "John Yunker, <i>The Art of the Global Gateway</i> (2017).",
             "Erin Meyer, <i>The Culture Map</i> (2014).",
             "Belgian FPS Finance, VAT rates (6 % food, 21 % standard)."],
)

# ------------------------------------------------------------------ 03 Pricing Experiments
pe_problem = Doodle(760, 280, "Doodle of June 2027. Larder Plus, free delivery for a monthly fee, launches this month. Femke picked 7.99 euros because a competitor charges that. Marco worries it's too cheap to pay for itself; Priya worries it's too expensive to sell. Nobody has asked customers, and the price will be hard to change once people subscribe.",
                    "Plus at €7.99 because a competitor charges that. Too cheap? Too dear? Nobody asked customers.")
pe_problem.box(20, 40, 220, 90, "Femke", "y", sub="€7.99, like them")
pe_problem.box(270, 40, 220, 90, "Marco", "blue", sub="“too cheap”")
pe_problem.box(520, 40, 220, 90, "Priya", "pink", sub="“too dear”")
pe_problem.note(380, 200, "a price by copying, hard to change later", "red", size=18)

pe_analogy = Doodle(760, 250, "Doodle of a market trader finding the right price for strawberries: asking regulars what they'd think too cheap or too dear, then trying two prices on two mornings and counting punnets and takings, not compliments.",
                     "A market trader asks regulars, then tries two prices on two mornings and counts takings, not compliments.")
pe_analogy.icon("coins", 40, 60, 1.3)
pe_analogy.box(170, 50, 270, 90, "ask", "y", sub="too cheap? too dear?")
pe_analogy.box(470, 50, 270, 90, "try", "green", sub="count takings")
pe_analogy.note(450, 205, "what people do, not what they say", "pen")

pe_how = Doodle(760, 400, "Grace's pricing work for Larder Plus, 14 June 2027. First a price sensitivity survey with 1,100 customers: an acceptable range from about 5 to 9 euros. Then, with Lena's agreement, a four-week test on new sign-ups only: 6.99 against 7.99, with the first month free in both, and a rule that nobody ends up paying more than the winning price. Result: sign-up 3.4 percent at 6.99 and 3.1 at 7.99; revenue per visitor higher at 7.99; members' order frequency the same. Decision: 7.99 with the first month free. By 1 September: 5,400 members, ordering 34 percent more often.",
                 "Ask first, then a careful test on new sign-ups. €7.99 kept, now on evidence. 5,400 members by September.")
pe_how.box(14, 14, 732, 50, "survey: 1,100 customers · acceptable ≈ €5–€9", "paper", size=15)
pe_how.box(14, 84, 360, 120, None, "y")
pe_how.head(194, 116, "€6.99", size=18)
pe_how.text(194, 150, "sign-up 3.4 %", size=15)
pe_how.text(194, 180, "revenue / visitor lower", size=14)
pe_how.box(386, 84, 360, 120, None, "green")
pe_how.head(566, 116, "€7.99", size=18)
pe_how.text(566, 150, "sign-up 3.1 %", size=15)
pe_how.text(566, 180, "revenue / visitor higher", size=14)
pe_how.box(14, 224, 732, 50, "new sign-ups only · first month free · nobody pays above the winner", "blue", size=14)
pe_how.note(380, 314, "€7.99 + first month free · 5,400 members by 1 Sep", "green", size=16)
pe_how.note(380, 348, "members order 34 % more often", "pen", size=16)

PRICING = dict(
    slug="pricing-experiments",
    kicker="a.k.a. “the strawberry stall”",
    tldr="Prices are among the most powerful and least tested product decisions. Start with <b>research</b> (what range do customers find acceptable?), then <b>test carefully</b>: on new customers, for a fixed period, with legal agreement and a fair treatment of anyone who paid more. Measure <b>behaviour</b> (sign-ups, revenue per visitor, retention, frequency), not stated intent, and choose the price on the whole picture.",
    chips=[("Family", "new markets"), ("Origin", "Van Westendorp price sensitivity (1976); pricing research and A/B testing"), ("Lives in", "a pricing test card agreed with legal and finance"), ("Pairs with", "A/B tests, sample size, business case one-pager")],
    problem_side="Larder, 14 June 2027",
    problem="""  <p class="lead"><b>Larder Plus</b>, free delivery for a monthly fee, launches this month. Femke picked <b>€7.99</b> because a competitor charges that. Marco worries it's <b>too cheap</b> to pay for itself; Priya worries it's <b>too dear</b> to sell. <span class="hl-pink">Nobody has asked customers</span>, and a subscription price is hard to change once people have signed up.</p>
  <ul>
    <li>Copied prices fit someone else's costs and customers.</li>
    <li>Opinions about price are loud and untested.</li>
    <li>Subscription prices stick.</li>
  </ul>""",
    problem_figs=[pe_problem],
    analogy_side="the strawberry stall",
    analogy="""  <p>A market trader setting the price of strawberries <b>asks regulars</b> what would feel too cheap or too dear. Then she <b>tries two prices on two mornings</b> and counts punnets sold and takings, not compliments. The answer is in the till.</p>""",
    analogy_figs=[pe_analogy],
    map=[("Asking regulars", "A price sensitivity survey, 1,100 customers"),
         ("Two prices on two mornings", "€6.99 vs €7.99 for new sign-ups, four weeks"),
         ("Counting takings", "Revenue per visitor and order frequency"),
         ("Compliments", "What people say they'd pay"),
         ("A fair stall", "First month free; nobody pays above the winner")],
    how_side="ask, test fairly, measure behaviour",
    how="""  <p>Grace ran a <b>price sensitivity survey</b> with 1,100 customers: acceptable range about <b>€5–€9</b>. Then, agreed with <b>Lena</b> and Marco, a <b>four-week test on new sign-ups only</b>: €6.99 vs €7.99, first month free in both, a rule that <b>nobody ends up paying more than the winner</b>. Sign-up: <b>3.4 %</b> vs <b>3.1 %</b>; revenue per visitor higher at €7.99; order frequency the same. Decision: <b>€7.99 with the first month free</b>. By 1 September: <b>5,400 members</b>, ordering <b>34 %</b> more often than similar customers.</p>""",
    how_figs=[pe_how],
    steps=[("Research the range", "Survey: too cheap, cheap, expensive, too expensive."),
           ("Agree the test with legal and finance", "Who sees which price, and how it's made fair."),
           ("Test on new customers", "Never change existing customers' prices in a test."),
           ("Run a fixed period", "Long enough for real decisions."),
           ("Measure behaviour", "Sign-ups, revenue per visitor, retention, frequency."),
           ("Decide on the whole picture", "And treat test customers fairly afterwards.")],
    vocab=[("Price sensitivity", "How demand changes with price."),
           ("Van Westendorp", "A survey method asking four price questions."),
           ("Revenue per visitor", "Total revenue divided by visitors: combines price and conversion."),
           ("Willingness to pay", "The most a customer would pay."),
           ("Price anchoring", "Judging a price against a reference."),
           ("Grandfathering", "Keeping existing customers on an old price.")],
    code=dict(file="product/plus/pricing-test.md", note="the pricing test card, June 2027", plain=True, src="""
# Larder Plus pricing test · 14 Jun – 12 Jul 2027 · owner: Grace · agreed: Lena, Marco, Femke

Research    Van Westendorp survey, 1,100 customers: acceptable range ≈ €5.00 – €9.00
Test        new sign-ups only, randomised: A €6.99 / B €7.99 · first month free in both
Fairness    if A wins, B members pay A's price from month 2; if B wins, A keeps €6.99 for 12 months
Measure     sign-up rate · revenue per visitor (12 months, est.) · orders per member per month
Guardrail   delivery cost per Plus order ≤ €4.20
Result      sign-up A 3.4 % · B 3.1 % · revenue per visitor B +6 % · frequency equal
Decision    €7.99, first month free (A's 610 members keep €6.99 for 12 months)
1 Sep       5,400 members · +34 % order frequency vs similar non-members
"""),
    tools="tools: a price sensitivity survey, the experiment platform with randomisation, revenue and retention reports, legal review.",
    gains=["<b>Prices on evidence</b>, not copying.",
           "<b>Marco and Priya</b> answered with data.",
           "<b>Fairness</b> built into the test.",
           "<b>Revenue per visitor</b> as the decider.",
           "<b>A price</b> that stuck."],
    losses=["<b>Legal and reputational care</b> needed.",
            "<b>Weeks of testing</b> before deciding.",
            "<b>Survey answers</b> are only a start.",
            "<b>Long-term effects</b> take months to see."],
    baseline="Each line compares <b>copying a competitor's price</b> to <b>researching the range and testing prices fairly on new customers, measuring behaviour</b>.",
    ratings=[(3, 4, "A price customers accepted, with a free first month."),
             (1, 5, "Revenue per visitor decided it."),
             (1, 5, "Survey, then a real test."),
             (2, 4, "Four weeks to an answer."),
             (2, 4, "One question: €6.99 or €7.99."),
             (2, 4, "Femke, Marco and Priya saw the same numbers."),
             (2, 5, "Lena agreed the fairness rules up front."),
             (3, 3, "Neutral."),
             (3, 3, "A survey and a test card.")],
    pitfalls=[("Copying a competitor", "Their price, your costs.", "research your customers."),
              ("Testing on existing customers", "Different prices for the same member.", "new sign-ups only."),
              ("Measuring sign-ups only", "Cheapest always wins.", "revenue per visitor and retention."),
              ("Unfair afterwards", "Test members overpay.", "a fairness rule agreed in advance.")],
    use=["New products, subscriptions and plans.",
         "Price changes.",
         "Delivery fees and thresholds.",
         "When leaders disagree about price."],
    skip=["Prices fixed by contract or regulation."],
    related=["<b>A/B tests</b> (Vol. 4)", "<b>Sample size &amp; test duration</b> (Vol. 4)", "<b>Disagree and commit</b> (Vol. 5)", "<b>Business case one-pager</b> (Vol. 2)"],
    quiz=[("Why test on new sign-ups only?", "Existing customers shouldn't see their price change in a test."),
          ("What decided the price?", "Revenue per visitor, not sign-up rate alone."),
          ("What was the fairness rule?", "Test members never end up paying more than the winning price (A keeps €6.99 for a year)."),
          ("What happened by September?", "5,400 members, ordering 34 % more often.")],
    try_it="Pick a price in your product. Ask twenty customers the four price questions, and sketch a test on new customers only: the two prices, the measure (revenue per visitor), the fairness rule, and who must agree.",
    remember="Ask the <span class=\"hl\">regulars</span>, then count the <span class=\"hl\">takings</span>.",
    sources=["Peter van Westendorp, “NSS Price Sensitivity Meter” (ESOMAR, 1976).",
             "Madhavan Ramanujam and Georg Tacke, <i>Monetizing Innovation</i> (2016).",
             "Ron Kohavi, Diane Tang and Ya Xu, <i>Trustworthy Online Controlled Experiments</i> (2020).",
             "Robbie Kellman Baxter, <i>The Membership Economy</i> (2015)."],
)

NOTES = [CITY, LOCAL, PRICING]
