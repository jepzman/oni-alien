# Series 5 · On the Client's Floor · Vol. 3 · Digging Up the Legacy · The data and its seams (notes 5–8).
from datetime import date


def on_site(d):
    return f"day {(d - date(2027, 7, 4)).days} on site"


# ------------------------------------------------------------------ 05 How Bad Is the Data, Really?
pd_problem = Doodle(760, 240, "Doodle of three numbers for one question: how many wave 1 customer records fail the address check? The bid's assumption A1-07: no more than 5 per cent. MetroVolt's sample in April: 7.8 per cent. The full profile of all 380,000 wave 1 accounts in November: 31 per cent.",
                    "5 % assumed. 7.8 % in the sample. 31 % in the full data.", exact=True)
for i, (h, sub, fill) in enumerate([("5 %", "A1-07 · the bid", "green"), ("7.8 %", "the sample · April", "y"), ("31 %", "all 380,000 · Nov", "pink")]):
    pd_problem.box(14 + i * 252, 30, 228, 120, h, fill, sub=sub, size=34, subsize=17)
pd_problem.note(380, 200, "the sample came from accounts opened after 2015", "red", size=20)

pd_how = Doodle(760, 340, "The full profile of wave 1's 380,000 accounts on four dimensions. Validity: 31 per cent fail the address check, 117,800 records, mostly old accounts and streets renamed since 2011. Uniqueness: 4.2 per cent are probable duplicates. Consistency: 2.9 per cent of meter numbers don't match Gareth's meter register. Completeness: 0.6 per cent of accounts lack a priority services flag that other records suggest they need. Each with a number by area and by account age.",
                "Four dimensions, every record, numbers by area and age. The sample was clean because it was young.", exact=True)
for i, (h, n, sub, fill) in enumerate([("validity", "31 %", "address check · 117,800", "pink"), ("uniqueness", "4.2 %", "probable duplicates", "y"),
                                       ("consistency", "2.9 %", "meter ≠ meter register", "y"), ("completeness", "0.6 %", "priority flag missing", "blue")]):
    pd_how.box(14 + i * 186, 20, 174, 140, h, fill, sub=sub, size=18, subsize=14)
    pd_how.text(101 + i * 186, 56, n, cls="t-head", size=26)
pd_how.box(14, 180, 732, 56, "accounts opened before 2005: 48 % fail · after 2015: 6 %", "paper", size=17)
pd_how.box(14, 250, 732, 50, "the sample was drawn from accounts opened after 2015", "pink", size=17)
pd_how.note(380, 326, "Pip, in March: “ask for a sample; nobody's looked since 2014”", "pen", size=17)

PROFILING = dict(
    slug="profiling-the-data", date=date(2027, 11, 19), meta=on_site(date(2027, 11, 19)), where="FL 19", pass_kind="contractor",
    kicker="a.k.a. “data profiling” before migration",
    tldr="A sample tells you about the sample. Before you migrate, <b>profile all the data</b> you'll move, on four dimensions: <b>validity</b> (does it pass the rules?), <b>uniqueness</b> (duplicates), <b>consistency</b> (does it agree with other systems?) and <b>completeness</b>. Break every number down by <b>segment</b> (area, age, type), because averages hide where the problem lives. Then check how the sample was drawn.",
    chips=[("Family", "the data and its seams"), ("Lives in", "discovery/data-profile-wave1.xlsx"), ("Pairs with", "assumptions (vol. 1), the discovery report, the 02:10 job")],
    problem_side="The Grid, 19 November 2027",
    problem="""  <p class="lead">Assumption <b>A1-07</b> said no more than <b>5 %</b> of customer records would fail the address check. MetroVolt's sample in April showed <b>7.8 %</b>. On <b>19 November</b> Bilal's full profile of all <b>380,000</b> wave 1 accounts finishes running.</p>
  <ul>
    <li><b>31 %</b> fail the address check: <b>117,800</b> records.</li>
    <li>The 10,000-record sample was drawn from accounts opened <b>after 2015</b>. <span class="hl-pink">Young accounts, clean addresses.</span></li>
    <li>A1-07 prices £9,500 for each 1 % above 5 %. Twenty-six points above.</li>
  </ul>""",
    problem_figs=[pd_problem],
    sides=dict(client=("Customer Operations", "<p>The data is Customer Ops' data. Priya's teams have lived with bad addresses for years (two in ten complaint calls), but nobody had a number. 31 % feels like an accusation, and it arrives in a cost-cutting year.</p>", "We knew it was bad. We didn't know it was that bad."),
                vendor=("Bilal and Ines", "<p>For Wrenfield, 31 % is the biggest finding of discovery: it's the work, the risk and the money. It must be <b>beyond dispute</b> before anyone sees it, and it must explain why the sample said 7.8 %, without making MetroVolt look as if it cheated.</p>", "Every record, every number by segment, and how the sample was drawn.")),
    sides_after="Nobody chose the biased sample. Someone pulled the most convenient 10,000 records. That's what samples are, unless someone designs them.",
    analogy_side="the restaurant inspection",
    analogy="""  <p>A restaurant inspector who only looks at the clean front counter will give it five stars. A thorough one opens <b>every fridge</b>, checks each against the same rules, and notes <b>which fridge</b> the problems are in. “The back fridge, everything older than a week” is far more useful than “30 % of food is out of date”.</p>""",
    map=[("The clean front counter", "The sample of accounts opened after 2015"),
         ("Every fridge", "All 380,000 wave 1 accounts"),
         ("The same rules for each", "Four dimensions: validity, uniqueness, consistency, completeness"),
         ("Which fridge", "Breakdown by area and account age"),
         ("“Older than a week”", "Accounts opened before 2005: 48 % fail")],
    how_side="all the data, four dimensions, every number by segment",
    how="""  <p>Bilal profiles <b>every wave 1 account</b> against agreed rules, on four dimensions:</p>
  <ul>
    <li><b>Validity</b>: addresses checked against the national address file: <b>31 %</b> fail.</li>
    <li><b>Uniqueness</b>: probable duplicate customers (same name, date of birth and nearby address): <b>4.2 %</b>.</li>
    <li><b>Consistency</b>: meter numbers that don't match Gareth's meter register: <b>2.9 %</b>.</li>
    <li><b>Completeness</b>: accounts with signs of vulnerability but no Priority Services flag: <b>0.6 %</b>, small and the most important.</li>
  </ul>
  <p>Then every number is <b>broken down</b>. By account age: opened before 2005, <b>48 %</b> fail; after 2015, <b>6 %</b>. By area: streets renamed since 2011 fail almost entirely (ADDRFIX's old table). The breakdown explains the sample: it was drawn from recent accounts, so it couldn't see the problem.</p>
  <p>Bilal runs the profile twice, on two days, and Bert checks thirty failing records by hand. All thirty are really wrong. The number is beyond dispute.</p>""",
    how_figs=[pd_how],
    steps=[("Profile everything you'll move", "Not a sample, if you can run it."),
           ("Agree the rules first", "With the data owner, in writing."),
           ("Four dimensions", "Validity, uniqueness, consistency, completeness."),
           ("Break down every number", "By segment: age, area, type."),
           ("Check how any sample was drawn", "It explains the gap."),
           ("Verify by hand", "The expert checks a handful of failures.")],
    vocab=[("Data profiling", "Measuring a dataset's content and quality systematically."),
           ("Validity", "Whether values pass the rules (e.g. a real address)."),
           ("Uniqueness", "Whether each real thing appears once."),
           ("Consistency", "Whether data agrees across systems."),
           ("Completeness", "Whether required values are present."),
           ("Sampling bias", "A sample that differs systematically from the whole.")],
    code=dict(file="discovery/data-profile-wave1.md", note="Bilal · Fri 19 Nov 2027 (run twice, 18 and 19 Nov)", src="""
DATA PROFILE · WAVE 1 (Northern district) · 380,000 live accounts

dimension      rule                                     fail      %
validity       address matches national address file    117,800  31.0
uniqueness     same name + DOB + nearby address           15,960   4.2
consistency    meter number = meter register (Gareth)     11,020   2.9
completeness   vulnerability signs but no PSR flag         2,280   0.6

validity by account age   < 2005: 48 %  · 2005–15: 29 %  · > 2015: 6 %
validity by cause         renamed streets (ADDRFIX 2011 table) 38 % of failures
                          missing flat numbers 27 % · free-text addresses 22 % · other 13 %
sample (Apr 2027)         10,000 accounts, all opened after 2015 → 7.8 %
hand check                Bert, 30 failing records: 30 really wrong
A1-07                     limit 5 % · actual 31 % · 26 points over
"""),
    contract=dict(side="the assumption, now tested", doc="Lodestar SOW · Appendix C, A1-07", date="signed 30 June 2027", stamp="false",
                  clauses=[("A1-07", "No more than 5 % of wave 1 customer records fail the address check. If false: Change Request at £9,500 per 1 % above 5 %.", "31 %. 26 points. £247,000, by the contract's own formula."),
                           ("3.2", "If an Assumption proves materially incorrect, either Party may raise a Change Request under clause 7.", "this is why we fought for “either party may raise” instead of “absorb”.")],
                  plain="a priced assumption turns a disaster into arithmetic. The contract already says what 31 % costs; the argument is about what to do, not who pays."),
    health=dict(now="a",
                g=("the data owner is curious", ["Share the profile as it runs.", "Decide the rules together.", "Celebrate finding it early."]),
                a=("bad news in a cut year", ["Run it twice; hand-check it.", "Explain the sample without blame.", "Tell the data owner first."]),
                r=("they'll dispute the number", ["Rules agreed in writing beforehand.", "Every failing record listable.", "Their expert does the hand check."])),
    pressure=dict(level=4, title="31 %", cost="the biggest finding of discovery · a client who'll hate it",
                  items=["The number is a relief and a dread: you were right to worry, and now you have to say it.", "Bilal ran it twice and asked Bert to check thirty records by hand. That's what makes it safe to say out loud."]),
    baseline="Each line compares <b>trusting the 10,000-record sample</b> with <b>a full four-dimension profile, broken down by segment and hand-checked</b>.",
    ratings=[(3, 4, "Customer Ops gets a number it can't dispute and a cause it can act on."),
             (3, 3, "Hard news, but the team stops guessing."),
             (1, 5, "A1-07 prices the gap exactly."),
             (2, 4, "Cleansing becomes a defined piece of work."),
             (2, 5, "The migration design faces the real data."),
             (1, 5, "The biggest risk is measured in November."),
             (2, 5, "Rules agreed, run twice, hand-checked."),
             (3, 3, "Two weeks of profiling."),
             (3, 3, "Re-run before each wave.")],
    pitfalls=[("Trusting a sample", "It was drawn from the clean part.", "profile everything, or design the sample."),
              ("One average", "31 % hides where the problem lives.", "break down by segment."),
              ("Rules agreed afterwards", "The number gets argued away.", "agree rules first, in writing."),
              ("Blaming whoever drew the sample", "It was convenience, not deceit.", "explain it neutrally."),
              ("Validity only", "Duplicates and mismatches bite later.", "all four dimensions.")],
    grimoire=[(2, "doom-prophet", "The Doom Prophet", "would say “we tried that in 2014”. Pip's “nobody's looked since 2014” turned out to be a prophecy too.")],
    use=["Before any data migration.", "When an assumption depends on data quality.", "When a sample looks better than people's experience."],
    skip=["Tiny datasets you can inspect by eye."],
    related=["<b>Quality Checks</b> (patterns, Vol. 9)", "<b>What Are We Assuming?</b> (vol. 1)", "<b>What Do We Say When Discovery Changes Everything?</b> (this volume)", "<b>What Does the 02:10 Job Really Do?</b> (this volume)"],
    quiz=[("What are the four dimensions of the profile?", "Validity, uniqueness, consistency and completeness."),
          ("Why did the sample show 7.8 % instead of 31 %?", "It was drawn from accounts opened after 2015, which have cleaner addresses."),
          ("Why break numbers down by segment?", "Averages hide where the problem lives; old accounts fail far more."),
          ("What does A1-07 say 31 % costs?", "£9,500 for each 1 % above 5 %: 26 points, about £247,000."),
          ("Why did Bert hand-check thirty records?", "To make sure the rule wasn't wrong and the number is beyond dispute.")],
    quiz_sit=[("Priya's deputy says “the check is too strict; flats without numbers are fine”. What do you do?", "Agree the rule together and re-run: if flats without numbers are acceptable to Customer Ops, the failure rate changes and so does the price. The rules belong to the data owner.")],
    try_it="Pick a dataset you rely on. Choose one rule for each of the four dimensions, run them on all of it, and break the worst number down by one segment. Where does the problem live?",
    remember="A sample tells you about <span class=\"hl\">the sample</span>. Profile <span class=\"hl\">everything you'll move</span>, and break it down.",
    late=dict(when="Fri 19 November 2027 · 23:40 · hotel near The Grid",
              lines=["31 %. Bilal ran it twice. Bert checked thirty by hand. All thirty wrong.",
                     "Pip was right in March: nobody had looked. I should find him and thank him.",
                     "A1-07 says £247,000. The contract did its job. Now I have to do mine: tell them, in the right order."]),
    sources=["Jack Olson, <i>Data Quality: The Accuracy Dimension</i> (2003).",
             "DAMA International, <i>DAMA-DMBOK</i> (2nd ed., 2017): data quality dimensions.",
             "UK Government Data Quality Hub, <i>The Government Data Quality Framework</i> (2020)."],
)

# ------------------------------------------------------------------ 06 How Do We Get Data Out of a Mainframe?
mf_problem = Doodle(760, 240, "Doodle of the question Lodestar needs answered during the day: which customer records changed in MAVIS since the last sync? MAVIS can only produce a nightly extract. Three options are drawn: reading the database log, using update timestamps, or comparing nightly snapshots. Between MAVIS and the new platform: copybooks, EBCDIC text and packed decimal numbers.",
                    "“What changed since 09:00?” MAVIS can only answer at 02:10.", exact=True)
mf_problem.box(24, 50, 180, 110, "MAVIS", "paper", sub="DB2 · COBOL", size=22, subsize=16)
mf_problem.box(556, 50, 180, 110, "Lodestar", "blue", sub="new platform", size=22, subsize=16)
for i, t in enumerate(["database log?", "timestamps?", "snapshots?"]):
    mf_problem.box(250, 30 + i * 52, 260, 42, t, "y", size=17)
mf_problem.note(380, 216, "copybooks · EBCDIC · packed decimals in between", "pen", size=18)

mf_how = Doodle(760, 330, "Three change-capture options, tested in October. Database log capture: tested on nine core tables, about 40 seconds' delay, needs a licence of 85,000 pounds a year and MetroVolt's mainframe team. Timestamps: 18 per cent of tables have no reliable update time. Nightly snapshot compare: works for every table, 24 hours' delay. Proposal: log capture for the nine core tables, snapshots for the rest. Underneath, the translation layer: 84 copybooks, EBCDIC to Unicode, packed decimals to numbers, each with a test.",
                "Test each option on real tables; mix them by what each table needs.", exact=True)
for i, (h, sub, fill) in enumerate([("log capture", "40 s · £85k/yr licence", "green"), ("timestamps", "18 % of tables: none", "pink"), ("snapshots", "24 h · all tables", "y")]):
    mf_how.box(14 + i * 250, 20, 232, 100, h, fill, sub=sub, size=20, subsize=15)
mf_how.box(14, 140, 732, 60, "proposal: log capture for 9 core tables · snapshots for the rest", "blue", size=18)
mf_how.box(14, 220, 732, 70, "translation layer", "paper", sub="84 copybooks · EBCDIC → Unicode · packed decimals → numbers · a test each", size=19, subsize=15)
mf_how.note(380, 316, "(Hollis will overrule part of this in January: see note 14)", "pen", size=17)

MAINFRAME = dict(
    slug="mainframe-integration", date=date(2027, 10, 21), meta=on_site(date(2027, 10, 21)), where="FL 19", pass_kind="contractor",
    kicker="a.k.a. “change data capture from a mainframe”",
    tldr="Getting data out of an old mainframe has two problems: <b>knowing what changed</b> and <b>translating what you get</b>. Test the change-capture options on <b>real tables</b>: reading the <b>database log</b>, trusting <b>update timestamps</b>, or comparing <b>nightly snapshots</b>; each table may need a different one. Then build a translation layer for <b>copybooks</b>, <b>EBCDIC</b> text and <b>packed decimals</b>, with a test for every field type.",
    chips=[("Family", "the data and its seams"), ("Lives in", "discovery/change-capture-spike.md"), ("Pairs with", "the strangler plan, being overruled")],
    problem_side="The Grid, 21 October 2027",
    problem="""  <p class="lead">During the waves, some MetroVolt processes will still update MAVIS while Lodestar serves migrated customers. Lodestar needs to know <b>what changed in MAVIS</b> during the day. MAVIS can only produce a <b>nightly extract</b>.</p>
  <ul>
    <li>Hana's favourite idea since the bid: read the database's change log (her “option 1 of 3, subject to discovery”).</li>
    <li>Bilal's: use “last updated” timestamps. Simple, if they exist.</li>
    <li>And everything MAVIS gives out comes in <b>COBOL copybook layouts</b>, <b>EBCDIC</b> text and <b>packed decimal</b> numbers. <span class="hl-pink">One wrong field definition corrupts money.</span></li>
  </ul>""",
    problem_figs=[mf_problem],
    sides=dict(client=("MetroVolt's mainframe team", "<p>The mainframe team is four people who keep MAVIS running at night. Any option that touches the database log needs their time, a new licence and a change to a system they've kept stable for decades. Their first answer to new tools is no.</p>", "Don't break the thing that never breaks."),
                vendor=("Hana", "<p>Hana needs change capture that's fast enough for the waves, cheap enough for the budget, and acceptable to the people who run the mainframe. Her favourite design may be right, but only a test on real tables will show it.</p>", "Test all three. Let the tables choose.")),
    sides_after="The best integration with an old system is often a mix: the fancy option where it matters, the boring one everywhere else.",
    analogy_side="news from a village with no phone",
    analogy="""  <p>You need to know what happens in a village with no phone. You could put someone at the <b>post office reading every letter</b> as it's posted (fast, but they need permission), ask each house to <b>write the date on their door</b> when something changes (if they remember), or <b>photograph the whole street every night</b> and compare (slow, but it never misses anything). And everything is written in the local dialect, which you'll need to translate.</p>""",
    map=[("Reading every letter at the post office", "Database log capture"),
         ("A date on every door", "Update timestamps"),
         ("Photographing the street nightly", "Snapshot compare"),
         ("Permission from the postmaster", "The mainframe team and a licence"),
         ("The local dialect", "Copybooks, EBCDIC and packed decimals")],
    how_side="test the options on real tables, then mix",
    how="""  <p>Hana runs a <b>two-week spike</b> with the mainframe team's blessing, read-only, in the test region.</p>
  <ul>
    <li><b>Log capture</b> on the nine core customer tables: changes arrive in about <b>40 seconds</b>. It needs a commercial tool (about <b>£85k a year</b>) and the mainframe team to configure it.</li>
    <li><b>Timestamps</b>: <b>18 %</b> of the tables have no reliable “last updated” column; some programs update rows without touching it.</li>
    <li><b>Snapshot compare</b>: works for every table, with a <b>24-hour</b> delay and a large nightly comparison.</li>
  </ul>
  <p>The proposal: <b>log capture for the nine core tables</b>, where minutes matter; <b>snapshots for everything else</b>. In parallel, Lottie and Bert build the <b>translation layer</b>: 84 copybooks turned into field definitions, EBCDIC to Unicode, packed decimals to numbers, each field type with a test against the golden master. A pound sign in EBCDIC is a different byte; the test catches it on day two.</p>""",
    how_figs=[mf_how],
    steps=[("List what needs to be fresh, and how fresh", "Per table, not per system."),
           ("Spike every option on real tables", "Read-only, with the owners' blessing."),
           ("Measure delay, cost and effort", "Including the client's people and licences."),
           ("Mix options by table", "Fancy where it matters, boring elsewhere."),
           ("Build the translation layer early", "Copybooks, encodings, number formats."),
           ("A test for every field type", "Money fields first.")],
    vocab=[("Change data capture (CDC)", "Detecting and delivering changes made to a database."),
           ("Log-based capture", "Reading changes from the database's own transaction log."),
           ("Snapshot compare", "Comparing two full copies to find what changed."),
           ("Copybook", "A COBOL definition of a record's layout."),
           ("EBCDIC", "The character encoding used on IBM mainframes."),
           ("Packed decimal (COMP-3)", "A compact way of storing numbers, two digits per byte.")],
    code=dict(file="discovery/change-capture-spike.md", note="Hana · Thu 21 Oct 2027", src="""
CHANGE CAPTURE · SPIKE RESULTS (MAVIS test region, 4–15 Oct)

option          tables tested   delay     cost / effort                    verdict
log capture     9 core          ≈ 40 s    licence ≈ £85k/yr · mainframe    core tables
                                          team 6 days to configure
timestamps      412             —         18 % of tables: no reliable      no
                                          "last updated"
snapshot diff   412             24 h      nightly compare, 2 h window      the rest
proposal        log capture: CUSTOMER, ACCOUNT, ADDRESS, METER_LINK, CONTACT,
                PSR, TARIFF_ASSIGN, BALANCE, AGREEMENT · snapshots: 403 others
translation     84 copybooks → field definitions · EBCDIC → Unicode (£ = x'5B'!)
                COMP-3 → decimal · 1 test per field type, checked vs golden master
"""),
    contract=dict(side="what the design schedule left open", doc="Lodestar SOW · Schedule 2, §3.3", date="v1.0 · Sep 2027", stamp="subject to discovery",
                  clauses=[("3.3", "Change detection between MAVIS and the new platform: mechanism to be confirmed in discovery (options: log capture, timestamps, snapshot compare).", "we left it open in the bid on purpose. good thing."),
                           ("Sch. 5", "Third-party licences required by the Solution are excluded from the Charges unless listed in Schedule 5.", "£85k a year isn't in Schedule 5. it's in the change request.")],
                  plain="leaving the mechanism “subject to discovery” let the spike decide without a fight. A licence the design now needs isn't in the price, so it goes to the client openly as part of the discovery findings."),
    health=dict(now="g",
                g=("the mainframe team is curious", ["Spike together.", "Share results the same day.", "Let them choose with you."]),
                a=("the mainframe team is wary", ["Read-only, in test, with their blessing.", "Measure their effort honestly.", "Offer the boring option too."]),
                r=("“no new tools on the mainframe”", ["Snapshots everywhere, with the delay priced.", "Show what the delay costs the waves.", "Escalate only with numbers."])),
    pressure=dict(level=3, title="a favourite idea on trial", cost="a two-week spike · one engineer's pride",
                  items=["Hana's idea won for nine tables and lost for 403. Say both halves out loud; she earned both.", "A wrong byte in a money field is the stuff of headlines. The tests are worth the boredom."]),
    baseline="Each line compares <b>picking the favourite mechanism for everything</b> with <b>testing all three on real tables and mixing them</b>.",
    ratings=[(3, 4, "The mainframe team sees its concerns tested, not dismissed."),
             (3, 4, "Hana's idea is used where it's best."),
             (3, 3, "A licence appears; priced openly."),
             (3, 4, "Each table's mechanism is listed."),
             (3, 5, "The design fits the real tables."),
             (2, 4, "Encoding errors caught on day two."),
             (3, 4, "Spike results on file."),
             (3, 3, "Two weeks."),
             (3, 2, "Two mechanisms to run instead of one.")],
    pitfalls=[("One mechanism for every table", "Overkill for most, too slow for some.", "decide per table."),
              ("Trusting timestamps", "Some programs don't update them.", "test them on real tables."),
              ("Ignoring the mainframe team", "Their no stops everything.", "spike with their blessing."),
              ("Translating by hand", "One wrong copybook field corrupts money.", "generated definitions and a test per type."),
              ("Hiding the licence cost", "It appears at go-live.", "price it in the findings.")],
    use=["Integrating with a mainframe or any system without change events.", "When freshness needs differ by table.", "Before committing to a CDC tool."],
    skip=["The old system already publishes reliable change events."],
    related=["<b>Change Data Capture</b> (patterns, Vol. 9)", "<b>How Do We Strangle a Customer System?</b> (this volume)", "<b>What If the Client Overrules Our Design?</b> (this volume)", "<b>How Do I Design on Two Pages of Facts?</b> (vol. 1)"],
    quiz=[("What were the three change-capture options?", "Database log capture, update timestamps, and nightly snapshot compare."),
          ("Why weren't timestamps enough?", "18 % of tables had no reliable “last updated” column."),
          ("What was proposed?", "Log capture for nine core tables, snapshots for the other 403."),
          ("What is a copybook?", "A COBOL definition of a record's layout."),
          ("Why a test per field type?", "Encodings and packed decimals are easy to get wrong, and money fields can't be.")],
    quiz_sit=[("The mainframe team says they can't spare six days to configure log capture until March. What do you do?", "Price the impact (snapshots only until March, with a 24-hour delay during the pilot), show it to Elaine and Hollis, and let them decide whether to free the time or accept the delay.")],
    try_it="Pick a system you need data from. For three of its tables, write how fresh you need the data and how you'd detect changes. Would one mechanism really fit all three?",
    remember="Test change capture <span class=\"hl\">on real tables</span>. Fancy where it matters, boring <span class=\"hl\">everywhere else</span>.",
    late=dict(when="Thu 21 October 2027 · 22:05 · hotel near The Grid",
              lines=["Log capture: 40 seconds on nine tables. Hana's idea works. For nine tables.",
                     "The pound sign is a different byte in EBCDIC. Lottie's test caught it. Imagine finding that on 380,000 bills.",
                     "£85k a year for the licence. That's going in the findings, not in our margin."]),
    sources=["Martin Kleppmann, <i>Designing Data-Intensive Applications</i> (2017): change data capture.",
             "IBM, <i>Enterprise COBOL for z/OS Programming Guide</i>: data representation and COMP-3.",
             "Debezium documentation: log-based change data capture concepts."],
)

# ------------------------------------------------------------------ 07 What Does the Billing System Really Need?
bi_problem = Doodle(760, 240, "Doodle of Halvorsen's interface specification version 1.1, delivered on 30 July as dependency D-03 promised: 41 fields on 12 pages. Hana's tests against Halvorsen's test system find six behaviours the specification doesn't mention, including field 17: if the town name isn't in capitals, the record is silently dropped.",
                    "41 fields on 12 pages, and six behaviours the pages don't mention.", exact=True)
bi_problem.box(24, 30, 240, 170, "spec v1.1", "y", sub="41 fields · 12 pages", size=22, subsize=16)
for i, t in enumerate(["field 17: capitals or dropped", "dates: day first only", "£ amounts: no sign", "+3 more"]):
    bi_problem.box(300, 24 + i * 46, 436, 38, t, "pink", size=16)
bi_problem.note(380, 224, "silently dropped is the worst kind of failure", "red", size=19)

bi_how = Doodle(760, 320, "The billing boundary. On Lodestar's side, a billing adapter, a translation layer that turns Lodestar's customer model into Halvorsen's file, so Halvorsen's quirks stay at the edge. Between the adapter and Halvorsen, contract tests agreed with Sven's team: 58 tests, run on every build against Halvorsen's test system. The spec becomes version 1.2, adding address line 4 and documenting all six behaviours, signed on 2 November.",
                "Keep their model at the edge, and turn the spec into tests both sides run.", exact=True)
bi_how.box(14, 60, 200, 110, "Lodestar", "blue", sub="customer model", size=21, subsize=15)
bi_how.box(240, 60, 200, 110, "billing adapter", "green", sub="their quirks live here", size=19, subsize=14)
bi_how.box(546, 60, 200, 110, "Halvorsen", "y", sub="billing", size=21, subsize=15)
bi_how.arrow(218, 115, 236, 115)
bi_how.arrow(444, 115, 542, 115)
bi_how.note(493, 196, "58 contract tests", "pen", size=17)
bi_how.box(14, 210, 732, 70, "spec v1.2 · 2 Nov 2027", "paper", sub="+ address line 4 · all 6 behaviours written down · version on every file", size=19, subsize=15)

BILLING_INTERFACE = dict(
    slug="billing-interface", date=date(2027, 11, 2), meta=on_site(date(2027, 11, 2)), where="FL 19", pass_kind="contractor",
    kicker="a.k.a. “integrating with another vendor's system”",
    tldr="Another vendor's interface specification describes what they <b>think</b> their system does. Test it against the <b>real system</b> early, write down every surprise, and turn the specification into <b>contract tests</b> both firms run. Keep their model at the edge with a <b>translation layer</b> (an adapter), so their quirks don't leak into your design. And put a <b>version on every file</b>.",
    chips=[("Family", "the data and its seams"), ("Lives in", "integration/billing-adapter/ · contract tests"), ("Pairs with", "the incumbent (vol. 1), the RACI (vol. 2)")],
    problem_side="The Grid, 2 November 2027",
    problem="""  <p class="lead">Halvorsen delivered its interface specification on <b>30 July</b>, on time: dependency <b>D-03</b> met. Version 1.1: <b>41 fields</b> on twelve pages. In October Hana tests real files against Halvorsen's test system.</p>
  <ul>
    <li>She finds <b>six behaviours</b> the spec doesn't mention.</li>
    <li>The worst: if field 17 (town) isn't in capitals, Halvorsen <b>silently drops the record</b>. No error, no bill.</li>
    <li>Lodestar's addresses, cleaned to the national format, need a fourth address line. <span class="hl-pink">Version 1.1 has three.</span></li>
  </ul>""",
    problem_figs=[bi_problem],
    sides=dict(client=("Sven and Halvorsen", "<p>Halvorsen's spec was written from what the system was designed to do in 2016. The quirks are known to Halvorsen's engineers and to nobody else. Sven doesn't want his system to look broken in front of MetroVolt, and doesn't want blame for MAVIS's data either.</p>", "It's always worked with MAVIS's files."),
                vendor=("Hana and Ines", "<p>Wrenfield must feed billing correctly for 380,000 customers, through a system it doesn't control. Silent drops would mean customers without bills, discovered months later. It needs the real behaviour written down and tested, and a fourth address line.</p>", "Let's turn the spec into tests we both run.")),
    sides_after="An interface spec is a promise about behaviour. A test suite is a promise you can check every day.",
    analogy_side="the plug adapter",
    analogy="""  <p>Travelling abroad, you don't rewire your hairdryer for each country. You carry a <b>plug adapter</b> that turns their socket into yours, and you test it before you trust it with your laptop. If their sockets have a quirk (one only works when the switch is on), you write it on the adapter.</p>""",
    map=[("Their socket", "Halvorsen's file format"),
         ("Your hairdryer", "Lodestar's customer model"),
         ("The plug adapter", "The billing adapter"),
         ("Testing before trusting it", "58 contract tests on every build"),
         ("A note on the adapter", "Spec v1.2: the six behaviours written down")],
    how_side="test the real thing, adapter at the edge, tests both sides run",
    how="""  <p><b>Test the real system.</b> Hana sends 2,000 realistic records through Halvorsen's test system and compares what was billed with what was sent. Six surprises: town names must be in capitals or the record is dropped; dates only day-first; amounts never signed; three more about tariff codes.</p>
  <p><b>Keep their model at the edge.</b> Lodestar keeps its own customer model. A <b>billing adapter</b> translates it into Halvorsen's file: capitals, date order, signs, codes. If Halvorsen changes, only the adapter changes.</p>
  <p><b>Turn the spec into tests.</b> With Sven's engineer, Hana writes <b>58 contract tests</b>: given this record, Halvorsen produces this bill line, or this error. Both firms run them, Wrenfield on every build. Silent drops become a test failure.</p>
  <p><b>Version everything.</b> On <b>2 November</b> Sven signs <b>spec v1.2</b>: address line 4 added, all six behaviours written down, and a version number in every file header. Sven's comment: “We should have written these down in 2016.” It goes into IA-01. (Remember the version header; it matters in May.)</p>""",
    how_figs=[bi_how],
    steps=[("Test the real system early", "Realistic records through their test environment."),
           ("Write down every surprise", "With examples."),
           ("Put an adapter at the edge", "Their model stops there."),
           ("Write contract tests together", "Given input, expected output or error."),
           ("Both sides run them", "On every build."),
           ("Version the spec and every file", "So mismatches show immediately.")],
    vocab=[("Interface specification", "A description of the format and behaviour of a connection between systems."),
           ("Contract test", "A test that checks one system meets what another relies on."),
           ("Adapter (translation layer)", "Code that converts between two models at the boundary."),
           ("Anti-corruption layer", "An adapter that keeps another system's model out of yours."),
           ("Silent failure", "A failure that produces no error."),
           ("Versioning", "Labelling each format so both sides know which they're using.")],
    code=dict(file="integration/billing-adapter/CONTRACT.md", note="spec v1.2 signed Tue 2 Nov 2027", src="""
BILLING INTERFACE · Halvorsen spec v1.2 (supersedes v1.1, 30 Jul 2027)

header    every file starts: HVN|SPEC=1.2|SENDER=…|COUNT=…|TOTAL=…
fields    42 (v1.1: 41; added: ADDRESS_LINE_4)
behaviours now written down (were in nobody's spec)
  B1  TOWN not upper-case → record silently dropped   → adapter upper-cases; test CT-17
  B2  dates day-first only (DDMMYYYY)                   → adapter formats; CT-22
  B3  amounts unsigned; credits via TYPE=CR            → adapter maps; CT-31
  B4–B6 tariff codes: 3 legacy aliases                  → adapter maps; CT-40..42
contract tests  58 · Wrenfield runs on every build · Halvorsen runs on each release
signed          Sven Aldous (Halvorsen) · Hana Sato (Wrenfield) · Hollis Wade (MetroVolt)
"""),
    contract=dict(side="the dependency, met and improved", doc="Lodestar SOW · Appendix C, D-03 · IA-01 §5", date="2 Nov 2027", stamp="v1.2",
                  clauses=[("D-03", "The billing supplier provides the interface specification by 30 July 2027.", "met. on time. and incomplete, through nobody's bad faith."),
                           ("IA-01, 5", "<ins>Each file carries a header stating the specification version. A receiving system that does not support the stated version shall reject the file with an error.</ins>", "a rejected file at 02:15 beats 11,000 missing bills in March.")],
                  plain="a dependency can be delivered on time and still be incomplete. Testing early and writing the real behaviour into the interface agreement turns that into a shared improvement instead of a blame war."),
    health=dict(now="g",
                g=("the other vendor cooperates", ["Write the tests together.", "Credit their engineers.", "Version everything."]),
                a=("they're defensive about quirks", ["Show examples, not criticism.", "“Let's write down what we both already know.”", "Make it a joint document."]),
                r=("they won't engage", ["Test and document anyway.", "Send findings via the client.", "Adapter absorbs everything."])),
    pressure=dict(level=2, title="someone else's quirks", cost="six surprises · one signature",
                  items=["Finding quirks in a rival's system tempts you to gloat. Don't: you'll need Sven at 02:30 one night.", "Silent drops are scary because you'd never know. The tests make them loud."]),
    baseline="Each line compares <b>trusting spec v1.1</b> with <b>real tests, an adapter at the edge, 58 contract tests and spec v1.2</b>.",
    ratings=[(3, 4, "Hollis sees two vendors fixing a seam together."),
             (3, 4, "Hana's team stops guessing at Halvorsen's rules."),
             (3, 3, "Neutral."),
             (3, 4, "The boundary is written and tested."),
             (3, 5, "Their model stays at the edge."),
             (2, 5, "Silent drops become test failures."),
             (2, 5, "Signed by both vendors and MetroVolt."),
             (3, 3, "Two weeks of testing."),
             (3, 3, "Tests to keep running.")],
    pitfalls=[("Trusting the document", "Real behaviour differs.", "test the real system early."),
              ("Their model in your core", "Every quirk spreads.", "an adapter at the edge."),
              ("Tests only on your side", "Their next release breaks you.", "both sides run them."),
              ("No version on files", "Mismatches are invisible.", "a version in every header."),
              ("Gloating about quirks", "You lose the partner you need.", "make it a joint improvement.")],
    use=["Feeding or reading another vendor's system.", "A spec written long ago.", "Any boundary where silent failure is possible."],
    skip=["Never skip the tests; the adapter can be thin if the formats already match."],
    related=["<b>Anti-Corruption Layer</b> (patterns, Vol. 7)", "<b>Contract Testing</b> (patterns, Vol. 4)", "<b>What About the Vendor Already Here?</b> (vol. 1)", "<b>Who Does What When Three Firms Share a Project?</b> (vol. 2)"],
    quiz=[("What was wrong with D-03, if it was delivered on time?", "Nothing in bad faith, but the spec missed six real behaviours, including silent drops."),
          ("What does the billing adapter do?", "Translates Lodestar's model into Halvorsen's format, keeping their quirks at the edge."),
          ("What is a contract test?", "Given an input, the other system produces an agreed output or error."),
          ("Why a version in every file header?", "So a system expecting another version rejects the file loudly."),
          ("What did v1.2 add?", "Address line 4 and the six behaviours written down.")],
    quiz_sit=[("A Halvorsen release changes how credits are handled, and contract test CT-31 fails on Wrenfield's build. What do you do?", "Tell Sven's team and Hollis the same day with the failing test; under IA-01 format changes need 30 days' notice. Agree whether to adapt or roll back, and update the spec version.")],
    try_it="Take an interface you depend on. Send ten realistic records and compare what happens with what the spec says. Write one contract test for the most dangerous difference.",
    remember="A spec says what they <span class=\"hl\">think</span> it does. Tests say what it <span class=\"hl\">does</span>. Keep their model at the edge.",
    late=dict(when="Tue 2 November 2027 · 21:30 · hotel near The Grid",
              lines=["Field 17: lower-case town names vanish. No error. No bill. Since 2016, nobody noticed because MAVIS shouts in capitals.",
                     "Sven signed v1.2 and said they should have written it down years ago. Biscuits again.",
                     "Version in every file header. If anyone ever runs the old parser, it'll fail loudly. I hope."]),
    sources=["Eric Evans, <i>Domain-Driven Design</i> (2003): anti-corruption layer.",
             "Martin Fowler, “ContractTest” (martinfowler.com, 2011).",
             "Pact documentation: consumer-driven contract testing."],
)

# ------------------------------------------------------------------ 08 How Do We Strangle a Customer System?
sp_problem = Doodle(760, 240, "Doodle of MAVIS as a large old tree and Lodestar as a young fig vine growing around it, district by district. Questions on labels: which system owns each account during the waves? What about the seven MAVIS processes that still need data? How do we go back if a wave fails?",
                    "Lodestar grows around MAVIS district by district. Who owns which customer in between?", exact=True)
sp_problem.box(280, 40, 200, 170, "MAVIS", "paper", sub="2.3m accounts", size=24, subsize=16)
sp_problem.line("M300 210 C 250 160 330 120 290 60 M460 210 C 520 150 430 110 470 50", color="green")
for i, t in enumerate(["who owns each account?", "7 MAVIS processes?", "a way back?"]):
    sp_problem.box(14 if i < 2 else 520, 40 + (i % 2) * 90, 226, 60, t, "pink", size=16)

sp_how = Doodle(760, 360, "The strangler plan. Every account has one system of record flag: MAVIS or Lodestar. Customer Ops' tools ask a router which system answers for each account. Migrated accounts become read-only in MAVIS, with a nightly back-feed for the seven MAVIS processes that still need their data, such as collections letters and regulatory reports. Each wave can be rolled back for fourteen days. Every night, reconciliation compares counts and balances between the two.",
                "One owner per account, a router, a back-feed, a way back, and a nightly reconciliation.", exact=True)
sp_how.box(14, 20, 200, 90, "router", "y", sub="who answers for this account?", size=19, subsize=13)
sp_how.box(280, 20, 200, 90, "MAVIS", "paper", sub="SoR = MAVIS", size=19, subsize=14)
sp_how.box(546, 20, 200, 90, "Lodestar", "blue", sub="SoR = Lodestar", size=19, subsize=14)
sp_how.arrow(218, 40, 276, 40)
sp_how.arrow(218, 95, 542, 100, curve=(380, 175))
sp_how.arrow(542, 65, 484, 65)
sp_how.note(640, 150, "back-feed, nightly", "pen", size=16)
for i, (h, sub, fill) in enumerate([("read-only", "migrated in MAVIS", "paper"), ("back-feed", "7 MAVIS processes", "green"), ("roll back", "14 days per wave", "pink"), ("reconcile", "counts + balances, nightly", "y")]):
    sp_how.box(14 + i * 186, 190, 174, 80, h, fill, sub=sub, size=18, subsize=13)
sp_how.note(380, 320, "district by district: pilot (20,000) → wave 1 (380,000) → waves 2–4", "pen", size=18)

STRANGLER = dict(
    slug="strangler-plan", date=date(2027, 11, 30), meta=on_site(date(2027, 11, 30)), where="FL 19", pass_kind="contractor",
    kicker="a.k.a. “the strangler fig”, applied to customers, not URLs",
    tldr="Strangling a customer system means two systems run side by side for years. Make it safe with five things: <b>one system of record per account</b>, a <b>router</b> that knows which system answers, a <b>back-feed</b> for old processes that still need data, a <b>way back</b> for each wave, and a <b>nightly reconciliation</b> of counts and balances. Move customers in groups that make sense to the business, not to the database.",
    chips=[("Family", "the data and its seams"), ("Lives in", "Schedule 2 v1.1, §4 (migration architecture)"), ("Pairs with", "mainframe integration, migration in waves")],
    problem_side="The Grid, 30 November 2027",
    problem="""  <p class="lead">The bid promised to replace MAVIS <b>in waves, district by district</b>. Discovery now has enough facts to design how two customer systems live side by side, possibly until 2030.</p>
  <ul>
    <li>Customer Ops' call-centre tools must know, for any customer, <b>which system to ask</b>.</li>
    <li><b>Seven MAVIS processes</b> (collections letters, regulatory returns, the meter feed, and four more) still need migrated customers' data.</li>
    <li>Hollis's question at the design authority: <span class="hl-pink">“And if wave 1 goes wrong on the Sunday, how do we go back?”</span></li>
  </ul>""",
    problem_figs=[sp_problem],
    sides=dict(client=("Hollis and Customer Ops", "<p>For MetroVolt, two systems at once means two places to look, two chances of disagreement and a call-centre agent asking “which screen?”. Hollis wants it impossible for an account to live in both. Customer Ops wants nothing to change on their screens.</p>", "One customer, one truth, and a way back."),
                vendor=("Ines and Hana", "<p>Wrenfield must design the in-between years so they're boring: clear ownership, a router, old processes still fed, and every wave reversible. A strangler that can't be reversed is just a slow big bang.</p>", "Make the coexistence dull, measurable and undoable.")),
    sides_after="The strangler fig is easy to draw and hard to run. The hard part isn't the new system; it's the years in between.",
    analogy_side="moving a library across town",
    analogy="""  <p>A library moving to a new building moves <b>one section at a time</b>. The catalogue says which building each book is in. The old building still answers questions about moved books for a while, so readers aren't lost. Each move can be reversed if the new shelves fail. And every night, someone counts the books in both buildings to make sure none fell off the van.</p>""",
    map=[("One section at a time", "District by district"),
         ("The catalogue says which building", "The system-of-record flag and the router"),
         ("The old building still answers", "The back-feed to seven MAVIS processes"),
         ("A reversible move", "Fourteen-day rollback per wave"),
         ("Counting books nightly", "Reconciliation of counts and balances")],
    how_side="one owner, a router, a back-feed, a way back, a reconciliation",
    how="""  <p><b>One system of record per account.</b> Each account has a flag: MAVIS or Lodestar. Never both. When a wave moves, the flag flips for those accounts and MAVIS makes them <b>read-only</b>.</p>
  <p><b>A router.</b> Customer Ops' tools ask one service, “who answers for account 4417…?”, and are sent to MAVIS or Lodestar. Agents see the same screens; the router hides the seam.</p>
  <p><b>A back-feed.</b> The seven MAVIS processes that still need migrated customers get a <b>nightly feed</b> from Lodestar in MAVIS's own format, including COPYMTR's meter file. Each process gets an owner and a retirement date (most retire with wave 4).</p>
  <p><b>A way back.</b> For <b>14 days</b> after each wave, MAVIS keeps the migrated accounts up to date through the back-feed, so flags can be flipped back if the wave fails. After 14 days, the decision is final.</p>
  <p><b>Nightly reconciliation.</b> Every night: account counts, balances and open debts compared between the two systems, per district. Any difference stops the next wave.</p>""",
    how_figs=[sp_how],
    steps=[("Choose business-shaped groups", "Districts customers and staff understand."),
           ("One owner per record", "A flag, never two masters."),
           ("A router in front", "Users don't need to know which system answers."),
           ("Feed the old processes", "A back-feed with owners and retirement dates."),
           ("Keep a way back", "A rollback window per group."),
           ("Reconcile nightly", "Differences stop the next move.")],
    vocab=[("Strangler fig", "Replacing an old system gradually while both run."),
           ("System of record", "The system whose data is authoritative for a record."),
           ("Router (façade)", "A layer that sends each request to the right system."),
           ("Back-feed", "Sending data from the new system back to the old one's processes."),
           ("Rollback window", "How long a migration can still be reversed."),
           ("Reconciliation", "Comparing totals between systems to prove nothing was lost.")],
    code=dict(file="design/schedule-2-v1.1-section-4.md", note="for the design authority · Tue 30 Nov 2027", src="""
MIGRATION ARCHITECTURE · Schedule 2 v1.1 §4 (draft)

ownership    SOR flag per account: MAVIS | LODESTAR (never both)
             flip at wave cutover; MAVIS read-only for SOR=LODESTAR
router       "account-owner" service; Customer Ops tools call it first
back-feed    nightly, Lodestar → MAVIS format, for 7 MAVIS processes:
             collections letters · regulatory returns · COPYMTR (meters) ·
             debt reporting · PSR return · year-end statements · complaints MI
             each with an owner (MetroVolt) and a retirement wave
rollback     14 days per wave: MAVIS kept current via back-feed; flags flippable
reconcile    nightly per district: account count · balances · open debt
             any difference → next wave blocked (go / no-go criterion)
groups       pilot: Ashgrove (20,000, incl. 340 staff households) → wave 1:
             Northern district (380,000) → waves 2–4 (phase 2)
"""),
    contract=dict(side="how the design schedule grows", doc="Lodestar SOW · Schedule 2, §4 and §3.3", date="v1.1 draft · 30 Nov 2027", stamp="for DA",
                  clauses=[("§4.1", "<ins>Each customer account has exactly one system of record at any time.</ins>", "Hollis's sentence. it's now a requirement we can test."),
                           ("3.3 (SOW)", "Elements of Schedule 2 identified as subject to discovery may be refined by agreement following the discovery phase without a Change Request, provided the Charges are unaffected.", "the router is a refinement. the back-feed for 7 processes isn't free: it's in the change request.")],
                  plain="refining the design within discovery is allowed without a change request only if the price doesn't move. Be honest about which parts are refinements and which are new work."),
    health=dict(now="a",
                g=("the client trusts the plan", ["Agree groups with the business.", "Reconcile from day one.", "Celebrate each flag flip."]),
                a=("they fear two systems", ["One owner per account, written as a requirement.", "Router so users see no change.", "A way back, with a date."]),
                r=("they want a big bang instead", ["Show how a big bang fails.", "Offer a small pilot to prove it.", "Price both honestly."])),
    pressure=dict(level=3, title="the years in between", cost="seven old processes · a rollback promise",
                  items=["A rollback promise feels like admitting you might fail. It's what lets everyone say yes.", "The back-feed is unglamorous work nobody will thank you for. It's what stops letters going to the wrong address."]),
    baseline="Each line compares <b>“strangle it in waves” as a slogan</b> with <b>one owner per account, a router, a back-feed, a rollback window and nightly reconciliation</b>.",
    ratings=[(3, 4, "Hollis's “one truth” is a written requirement."),
             (3, 3, "More moving parts to build."),
             (3, 3, "The back-feed is priced in the change request."),
             (3, 4, "Seven processes listed with owners."),
             (3, 5, "No account with two masters."),
             (2, 5, "Each wave reversible for 14 days."),
             (3, 4, "Schedule 2 v1.1, at the design authority."),
             (3, 3, "Three weeks of design."),
             (3, 2, "Two systems to run for years.")],
    pitfalls=[("Two masters for one record", "Updates collide.", "one system of record per account."),
              ("Users choosing the system", "Agents look in the wrong place.", "a router hides the seam."),
              ("Forgetting old processes", "Letters stop, reports break.", "a back-feed with owners."),
              ("No way back", "A strangler becomes a slow big bang.", "a rollback window per wave."),
              ("No reconciliation", "Missing customers found months later.", "nightly counts and balances.")],
    use=["Replacing a system of record gradually.", "Coexistence will last months or years.", "Groups of records can move separately."],
    skip=["The old system is small enough to switch over in one tested weekend."],
    related=["<b>Strangler Fig</b> (patterns, Vol. 1)", "<b>How Do We Move 380,000 Customers?</b> (this volume)", "<b>How Do We Get Data Out of a Mainframe?</b> (this volume)", "<b>Transition Architectures</b> (Ana, vol. 4)"],
    quiz=[("What does “one system of record per account” prevent?", "Two systems updating the same account and disagreeing."),
          ("What does the router do?", "Sends each request to whichever system owns the account, so users don't have to know."),
          ("What is the back-feed for?", "Seven MAVIS processes that still need migrated customers' data."),
          ("How long can a wave be rolled back?", "Fourteen days."),
          ("What stops the next wave?", "Any difference in the nightly reconciliation of counts and balances.")],
    quiz_sit=[("A Customer Ops manager asks for agents to see both MAVIS and Lodestar data side by side “just in case”. What do you say?", "Offer read-only history from MAVIS through the router for migrated customers, but keep one system of record: two editable views of the same customer is how updates get lost.")],
    try_it="Pick something you'd replace gradually. Write the five parts: the groups you'd move, the ownership flag, the router, what the old system still needs fed, and how you'd go back.",
    remember="A strangler is safe only with <span class=\"hl\">one owner per record</span>, a router, a back-feed, <span class=\"hl\">a way back</span>, and a nightly count.",
    late=dict(when="Tue 30 November 2027 · 22:45 · hotel near The Grid",
              lines=["Hollis asked how we'd go back. Fourteen days, I said. He wrote it into §4 himself.",
                     "Seven MAVIS processes still need feeding. Nobody will ever thank us for the back-feed. Good.",
                     "Discovery ends in ten days. Then I have to tell them about 31 %."]),
    sources=["Martin Fowler, “StranglerFigApplication” (martinfowler.com, 2004).",
             "Sam Newman, <i>Monolith to Microservices</i> (2019): coexistence patterns.",
             "Sam Newman, <i>Building Microservices</i> (2nd ed., 2021): migrating data and splitting the monolith."],
)

NOTES = [PROFILING, MAINFRAME, BILLING_INTERFACE, STRANGLER]
