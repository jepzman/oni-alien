# Series 2 · Book 5 · The IT Operations Notebook · Vol. 5 · Recovering.
# Narrator: Eli (he/him). Facts: docs/larder-casebook.md, "Book 5, Vol. 5".

# ------------------------------------------------------------------ 01 What Matters Most If Everything Fails?
bi_problem = Doodle(760, 260, "Doodle of Monday 10 January 2028. Larder's first full restore of the production database, onto a fresh server, takes 3 hours 40 minutes. Afterwards Eli asks the obvious question: is that acceptable? Nobody can say. There is no agreed answer to how long each service may be down, or how much data it may lose, if everything fails.",
                    "The first full restore took 3 h 40. Is that acceptable? Nobody had agreed what “acceptable” is.")
bi_problem.box(14, 30, 300, 100, "full restore", "pink", sub="3 h 40 · Mon 10 Jan", size=20, subsize=14)
bi_problem.box(346, 30, 400, 100, "“is that OK?”", "paper", sub="how long down? how much lost? per service?", size=20, subsize=13)
bi_problem.note(380, 180, "no agreed recovery time or data-loss limit for anything", "red", size=17)

bi_analogy = Doodle(760, 220, "Doodle of a family deciding what to grab in a fire: the people first, then the pets, then the passports and the laptop with the photos, then nothing else. They agree it calmly at the kitchen table, and keep the passports in one drawer so the plan works in two minutes.",
                    "People, pets, passports, photos: agreed at the kitchen table, so the plan takes two minutes.")
bi_analogy.row([("people", "first", "pink"), ("pets", "second", "y"), ("passports", "third", "y"), ("photos", "fourth", "green")], y=40, h=96, gap=14, size=18, subsize=14)
bi_analogy.note(380, 186, "decide the order calmly, before the smoke", "pen", size=18)

bi_how = Doodle(760, 400, "Larder's business impact analysis, 17 to 21 January 2028, with Femke, Joost, Marco and Mo. For each service: what an hour down costs (in orders, Korenwolf credits, staff idle), and how much data it may lose. Result, matching Ana's DR tiers: tier 1, recover within 15 minutes, lose at most 1 minute of data: ordering and checkout, payments, Dispatch. Tier 2, within 1 hour, at most 15 minutes: business portal and API, store sync, the picker app's back end. Tier 3, within 1 day, at most 24 hours: billing integration, helpdesk, reporting. Tier 4, rebuild when convenient: internal tools. An hour of tier 1 down at a Friday peak: about 45,000 euros of orders.",
                "Four tiers set by what an hour down costs. Tier 1 (15 min, 1 min of data): ordering, payments, Dispatch.")
tiers = [("tier 1", "≤ 15 min · ≤ 1 min data", "ordering · payments · Dispatch", "pink"),
         ("tier 2", "≤ 1 h · ≤ 15 min data", "business portal + API · store sync · picker back end", "y"),
         ("tier 3", "≤ 1 day · ≤ 24 h data", "billing integration · helpdesk · reporting", "blue"),
         ("tier 4", "rebuild", "internal tools", "paper")]
for i, (t, r, s, f) in enumerate(tiers):
    y = 14 + i * 76
    bi_how.box(14, y, 110, 64, t, f, size=17)
    bi_how.box(134, y, 230, 64, r, "paper", size=13)
    bi_how.box(374, y, 372, 64, s, f, size=13)
bi_how.note(380, 348, "an hour of tier 1 down at a Friday peak ≈ €45,000 of orders", "red", size=16)
bi_how.note(380, 382, "3 h 40 for the ordering database: far outside tier 1", "pen", size=15)

BUSINESS_IMPACT = dict(
    slug="business-impact",
    kicker="a.k.a. “business impact analysis”",
    tldr="Before you can say whether a recovery is fast enough, decide <b>how long each service may be down (RTO)</b> and <b>how much data it may lose (RPO)</b>. Base both on <b>what an hour of loss costs the business</b>: orders, client credits, idle staff, trust. Set them with the business, group services into a few <b>tiers</b>, and then test whether you can actually meet them.",
    chips=[("Family", "recovering"), ("Lives in", "ops/continuity/bia.md; the tier on every catalogue line"), ("Pairs with", "restore tests, Ana's DR tiers, the catalogue (vol. 1)")],
    itil=dict(groups=["service"], chain=["plan", "design"], practices=["service continuity management"],
              sre="(recovery objectives drive design and testing)", principles=["Focus on value", "Think and work holistically"],
              older="ITIL v3: IT service continuity management, business impact analysis (BIA)"),
    problem_side="Larder, Monday 10 January 2028",
    problem="""  <p class="lead">On <b>10 January</b> Larder runs its first ever full restore of the production database, onto a fresh server. It takes <b>3 hours 40 minutes</b>. Eli asks the obvious question afterwards: <b>is that acceptable?</b> <span class="hl-pink">Nobody can say.</span> There's no agreed answer, for any service, to how long it may be down or how much data it may lose if everything fails.</p>
  <ul>
    <li>Without targets, “we have backups” sounds like enough.</li>
    <li>Every service gets the same effort, or none.</li>
    <li>Spending on recovery (a second region?) can't be judged.</li>
  </ul>""",
    problem_figs=[bi_problem],
    meanwhile=[("architect-5", "dr-tiers", "Ana's DR tiers after the same restore: tiers 1–4 (RTO 15 min / 1 h / 1 day / rebuild), backups copied to Paris.",
                "Eli's business impact analysis behind those tiers: which service sits where, and what an hour of each costs.")],
    analogy_side="what to grab in a fire",
    analogy="""  <p>A family agrees, calmly, at the kitchen table, what to grab in a fire: <b>people first, then the pets, then the passports and the laptop with the photos</b>, then nothing else. They keep the passports in one drawer so the plan works in two minutes. Deciding <b>during</b> the fire would be too late.</p>""",
    analogy_figs=[bi_analogy],
    map=[("People first", "Tier 1: ordering, payments, Dispatch"),
         ("Passports and photos", "Tier 2–3: business ordering, store sync, billing"),
         ("Nothing else", "Tier 4: rebuild internal tools later"),
         ("Agreed at the kitchen table", "Agreed with Femke, Joost, Marco and Mo"),
         ("Passports in one drawer", "Backups and runbooks ready for each tier")],
    how_side="cost per hour, tiers, and targets the business owns",
    how="""  <p>From <b>17 to 21 January</b> Eli meets Femke, Joost, Marco and Mo, one service at a time, with one question: <b>what does an hour without it cost?</b> That's counted in lost orders, Korenwolf credits, staff standing idle, and trust. Then <b>how much data could we lose</b> before someone has to re-enter it or a customer notices.</p>
  <ul>
    <li><b>Tier 1</b> (back within <b>15 minutes</b>, at most <b>1 minute</b> of data lost): ordering and checkout, payments, Dispatch. An hour down at a Friday peak is about <b>€45,000</b> of orders.</li>
    <li><b>Tier 2</b> (1 hour, 15 minutes of data): business portal and API, store sync, the picker app's back end.</li>
    <li><b>Tier 3</b> (1 day, 24 hours of data): billing integration, helpdesk, reporting.</li>
    <li><b>Tier 4</b>: internal tools, rebuilt when convenient.</li>
  </ul>
  <p>The tiers match Ana's DR tiers, and the tier goes onto every catalogue line. By that measure, the ordering database's 3 h 40 is <b>far outside tier 1</b>, which is the next note. Restoring from scratch is the worst case; a replica failover (under 2 minutes) covers most failures.</p>""",
    how_figs=[bi_how],
    steps=[("List services from the catalogue", "One at a time."),
           ("Ask what an hour down costs", "Orders, credits, idle staff, trust."),
           ("Ask how much data may be lost", "Minutes? Hours? A day?"),
           ("Group into a few tiers", "Three or four, not one per service."),
           ("Agree with the business", "They own the targets."),
           ("Test against them", "Restores, failovers, drills.")],
    vocab=[("RTO (recovery time objective)", "How long a service may be down before the loss is unacceptable."),
           ("RPO (recovery point objective)", "How much data, in time, may be lost."),
           ("Business impact analysis", "Working out what each service's loss costs, to set RTO and RPO."),
           ("Tier", "A group of services with the same recovery targets."),
           ("Continuity", "Keeping the business running through a serious disruption."),
           ("Worst case", "Restoring from backup onto new infrastructure, not just failing over.")],
    code=dict(file="ops/continuity/bia.md", note="17–21 January 2028 · with Femke, Joost, Marco, Mo", plain=True, src="""
service                 cost of 1 h down (Fri peak)       RTO     RPO      tier
ordering + checkout     ≈ €45k orders · trust             15 min  1 min    1
payments                orders fail at the last step      15 min  1 min    1
Dispatch                couriers by hand · late orders    15 min  1 min    1
business portal + API   Korenwolf credits · Mo's calls    1 h     15 min   2
store sync              stale stock → swaps, refunds      1 h     15 min   2
picker app back end     offline mode ≈ 2 h, then paper    1 h     15 min   2
billing integration     invoices late, not lost           1 day   24 h     3
helpdesk / reporting    slower support / no reports       1 day   24 h     3
internal tools          inconvenience                     rebuild —        4
10 Jan 2028 full restore of the ordering DB: 3 h 40 → far outside tier 1
"""),
    tools="tools: the catalogue, last year's incident costs, Marco's numbers, and a week of short meetings.",
    ladder=[("“we have backups”", ["No targets.", "Same effort everywhere."]),
            ("tiers with agreed RTO / RPO", ["Owned by the business.", "On the catalogue."]),
            ("targets tested", ["Restores and failovers measured against them.", "Gaps planned."]),
            ("designed to the tier", ["Each new service chooses its tier at design time.", "Recovery built in."])],
    ladder_now=1,
    baseline="Each line compares <b>“we have backups”</b> to <b>four tiers with recovery targets agreed with the business</b>.",
    ratings=[(2, 4, "Recovery effort goes to what customers need first."),
             (3, 3, "Neutral on its own."),
             (2, 3, "Targets show where recovery is too slow."),
             (3, 3, "Neutral."),
             (2, 4, "Every service's tier is on the catalogue."),
             (3, 3, "Neutral."),
             (2, 4, "Spending matched to the cost of downtime."),
             (3, 3, "Neutral."),
             (3, 3, "A week of short meetings.")],
    pitfalls=[("Engineers set the targets", "Nobody pays for them.", "agree them with the business."),
              ("Everything tier 1", "No priorities.", "cost per hour decides."),
              ("Only RTO, no RPO", "Fast back, with a day of data gone.", "both."),
              ("Targets never tested", "A number on paper.", "restore and fail over against them.")],
    use=["A restore took long and nobody knew if that was OK.", "Deciding on recovery spend (a second region).", "Clients or auditors ask about recovery.", "Before writing continuity plans."],
    skip=["Truly disposable services: tier 4 says it."],
    related=["<b>DR Tiers</b> (Ana, vol. 5)", "<b>Can We Actually Restore?</b> (next note)", "<b>What Do We Run, and Who Owns It?</b> (vol. 1)", "<b>When to Go Multi-Region</b> (Ana, vol. 5)"],
    quiz=[("What are RTO and RPO?", "How long a service may be down, and how much data (in time) it may lose."),
          ("How were Larder's tiers set?", "By what an hour down costs, agreed with Femke, Joost, Marco and Mo."),
          ("Which services are tier 1?", "Ordering and checkout, payments, Dispatch: 15 minutes, 1 minute of data."),
          ("Why was 3 h 40 a problem?", "It's far outside tier 1's 15 minutes for the ordering database's worst case."),
          ("What covers most failures without a restore?", "Replica failover, under 2 minutes.")],
    quiz_sit=[("Grace's team launches a new “recipes” feature. Which tier is it?", "Ask what an hour without it costs. If customers can still order without it, probably tier 3 or 4; it goes on the catalogue with that tier, and its backups match.")],
    try_it="Take your five most important services. For each, write what an hour down costs and how much data you could lose. Group them into tiers. When did you last test the worst case for tier 1?",
    remember="Decide <span class=\"hl\">what to grab first</span> before the fire: recovery time and data loss per service, set by <span class=\"hl\">what an hour costs</span>.",
    sources=["AXELOS, <i>ITIL 4: Service continuity management</i> practice guide (2020).",
             "ISO 22301:2019, Business continuity management systems (overview).",
             "Betsy Beyer et al., <i>Site Reliability Engineering</i> (2016): chapter 26, data integrity."],
)

# ------------------------------------------------------------------ 02 Can We Actually Restore?
rs_problem = Doodle(760, 260, "Doodle of the 3 hours 40 minutes of 10 January 2028, broken down. Copying the backup to a new server: 1 hour 10. Restoring and replaying logs: 1 hour 50. Checking by hand that the data looked right: 40 minutes. Backups had run every night since 2024 and been 'green' every morning. Nobody had restored one end to end.",
                    "Backups green every morning since 2024. The first end-to-end restore: 3 h 40, mostly copying and checking by hand.")
parts = [("copy backup", "1 h 10", 194), ("restore + replay", "1 h 50", 304), ("check by hand", "40 min", 112)]
x = 14
for t, d, w in parts:
    rs_problem.box(x, 40, w - 6, 90, t, "pink", sub=d, size=16, subsize=15)
    x += w + 8
rs_problem.note(380, 180, "“backup succeeded” every night ≠ “we can restore”", "red", size=18)

rs_analogy = Doodle(760, 220, "Doodle of a spare tyre in a car boot. It's been there for years. One day you need it and find it flat, the jack missing, and the wheel nuts too tight to undo. The spare only counts if you've checked it, and practised changing a wheel once on a dry afternoon.",
                    "A spare tyre you've never checked is flat when you need it. Practise once on a dry afternoon.")
rs_analogy.icon("chassis", 60, 60, 1.3)
rs_analogy.box(190, 40, 260, 100, "spare in the boot", "paper", sub="years, never checked", size=18, subsize=14)
rs_analogy.box(480, 40, 266, 100, "practised once", "green", sub="a dry afternoon", size=18, subsize=14)
rs_analogy.note(450, 190, "a backup counts once it's been restored", "pen", size=18)

rs_how = Doodle(760, 400, "Larder's restore practice from February 2028. Restores use storage snapshots plus write-ahead logs instead of copying full dumps, so nothing large has to move. Backups are copied to the Paris region daily. Checks are scripted: row counts per table, yesterday's orders, the latest payment, the latest stock change. Every month a random backup of a tier 1 or 2 database is restored to a scratch server and checked automatically; the time is recorded. Every quarter, a full drill onto fresh infrastructure, timed with a stopwatch. Times: 10 January 3 h 40; February monthly test 48 minutes; 18 April drill 22 minutes.",
                "Snapshots and logs instead of copies; scripted checks; a random restore every month; a timed drill every quarter.")
rs_how.box(14, 14, 236, 110, "snapshots + logs", "blue", sub="nothing big to copy", size=17, subsize=13)
rs_how.box(262, 14, 236, 110, "scripted checks", "green", sub="counts · last order · last payment", size=17, subsize=12)
rs_how.box(510, 14, 236, 110, "Paris copy", "y", sub="daily, another region", size=17, subsize=13)
rs_how.box(14, 150, 732, 60, "monthly: a random tier 1–2 backup restored and checked · quarterly: a full timed drill", "paper", size=14)
rs_how.row([("10 Jan", "3 h 40", "pink"), ("Feb monthly", "48 min", "y"), ("18 Apr drill", "22 min", "green")], x=14, y=236, h=90, gap=40, size=19, subsize=20, arrows=True)
rs_how.note(380, 364, "the time of every restore is written down", "pen", size=16)

RESTORE_TESTS = dict(
    slug="restore-tests",
    kicker="a.k.a. “backups are only as good as the restore”",
    tldr="A green “backup succeeded” every night proves only that something was written somewhere. A backup is real once it has been <b>restored, checked and timed</b>. Make restoring <b>fast by design</b> (snapshots and logs rather than huge copies), <b>check the result with scripts</b>, keep a copy <b>in another region</b>, restore a <b>random backup every month</b>, and run a <b>full timed drill every quarter</b>.",
    chips=[("Family", "recovering"), ("Lives in", "ops/continuity/restore-tests.md; the scripted checks in the repo"), ("Pairs with", "business impact analysis, game days, DR tiers")],
    itil=dict(groups=["service", "technical"], chain=["deliver", "improve"], practices=["service continuity management", "infrastructure and platform management"],
              sre="“nobody wants backups, everybody wants restores”", principles=["Progress iteratively with feedback"],
              older="ITIL v3: IT service continuity management (testing)"),
    problem_side="Larder, January 2028",
    problem="""  <p class="lead">Eli takes apart the <b>3 hours 40 minutes</b> of 10 January. <b>Copying</b> the backup to a new server: 1 h 10. <b>Restoring</b> and replaying the logs: 1 h 50. <b>Checking by hand</b> that the data looked right: 40 minutes. Backups had run every night since 2024 and shown green every morning. <span class="hl-pink">Nobody had ever restored one end to end.</span></p>
  <ul>
    <li>“Backup succeeded” measures writing, not recovering.</li>
    <li>The slowest parts (copying, checking) were never designed.</li>
    <li>All backups lived in the same region as the database.</li>
  </ul>""",
    problem_figs=[rs_problem],
    analogy_side="the spare tyre in the boot",
    analogy="""  <p>The <b>spare tyre</b> has been in the boot for years. The day you need it, it's <b>flat</b>, the jack is missing and the wheel nuts are too tight to undo. A spare only counts if you've checked it, and changed a wheel once, <b>on a dry afternoon</b>, when nothing depended on it.</p>""",
    analogy_figs=[rs_analogy],
    map=[("The spare in the boot", "Nightly backups, green every morning"),
         ("Finding it flat", "A 3 h 40 restore"),
         ("Checking the pressure", "Scripted checks on the restored data"),
         ("Changing a wheel once", "A monthly random restore, a quarterly drill"),
         ("A second spare at home", "A copy in the Paris region")],
    how_side="fast by design, checked by script, practised on a schedule",
    how="""  <p>Eli and Bram change four things from <b>February</b>:</p>
  <ul>
    <li><b>Fast by design</b>: restores use storage <b>snapshots plus logs</b>, not full dumps, so nothing large has to be copied.</li>
    <li><b>Checked by script</b>: row counts per table, yesterday's orders, the latest payment, the latest stock change. A restore passes or fails in minutes.</li>
    <li><b>Another region</b>: backups are copied to <b>Paris</b> daily (Ana's DR tiers).</li>
    <li><b>Practised</b>: every month a <b>random backup</b> of a tier 1 or 2 database is restored to a scratch server and checked automatically, with the time recorded. Every quarter there's a <b>full drill</b> onto fresh infrastructure, timed with a stopwatch.</li>
  </ul>
  <p>The times: <b>3 h 40</b> on 10 January, <b>48 minutes</b> at the February monthly test, <b>22 minutes</b> at the <b>18 April</b> drill. That's still outside tier 1's 15 minutes for a full rebuild, but a replica failover (under 2 minutes) covers tier 1 in almost every real failure. Restoring from scratch is now an hour's problem, not an afternoon's.</p>""",
    how_figs=[rs_how],
    steps=[("Time your first full restore", "On fresh infrastructure, end to end."),
           ("Find the slow parts", "Copying, replaying, checking."),
           ("Design them faster", "Snapshots and logs; scripted checks."),
           ("Keep a copy elsewhere", "Another region, another account."),
           ("Restore a random backup monthly", "Automatically checked, timed."),
           ("Drill quarterly", "Full rebuild, stopwatch, written result.")],
    vocab=[("Backup", "A copy of data kept to recover from loss."),
           ("Restore", "Bringing data back from a backup into a working system."),
           ("Snapshot", "A point-in-time copy of storage, fast to create and restore."),
           ("Write-ahead log (WAL)", "The database's record of changes, replayed to reach a point in time."),
           ("Point-in-time recovery", "Restoring to a chosen moment using a snapshot plus logs."),
           ("Restore drill", "A planned, timed restore onto fresh infrastructure.")],
    code=dict(file="ops/continuity/restore-tests.md", note="from February 2028", plain=True, src="""
# Restore tests

method      snapshots + WAL (point in time) · copies in Paris daily
checks      scripts/restore-check: row counts · yesterday's orders · last payment
            · last stock change · business orders for tomorrow   → PASS / FAIL
monthly     random tier 1–2 backup → scratch server → checks → time recorded
quarterly   full drill on fresh infrastructure · stopwatch · watcher

date        what                         time     checks
10 Jan      first full restore (dumps)   3 h 40   by hand
14 Feb      monthly, ordering DB          48 min   ✓
14 Mar      monthly, Dispatch DB          19 min   ✓
18 Apr      quarterly drill, ordering DB  22 min   ✓
"""),
    tools="tools: the database's snapshot and log features, a restore-check script, a scratch server, a calendar and a stopwatch.",
    ladder=[("green backups, never restored", ["Hope.", "Same region."]),
            ("restores tested and timed", ["Monthly random, quarterly drill.", "Scripted checks."]),
            ("restores automated end to end", ["A schedule restores and checks by itself.", "Alerts on failure or slowness."]),
            ("recovery is routine", ["Environments routinely built from backups.", "Restore time inside the tier."])],
    ladder_now=1,
    baseline="Each line compares <b>nightly green backups never restored</b> to <b>scripted, timed restores every month and a drill every quarter</b>.",
    ratings=[(3, 3, "Neutral day to day."),
             (3, 3, "Neutral."),
             (1, 4, "3 h 40 → 22 minutes for the worst case."),
             (3, 3, "Neutral."),
             (2, 4, "Every restore time written down."),
             (2, 3, "Checks scripted, not by hand."),
             (3, 3, "A scratch server a few hours a month."),
             (2, 3, "The worst night is now practised."),
             (3, 3, "Automatic monthly; an hour a quarter.")],
    pitfalls=[("Trusting “backup succeeded”", "It measures writing, not restoring.", "restore and time it."),
              ("Checking by eye", "Slow and unreliable.", "scripted checks."),
              ("Backups in the same place", "A region problem takes both.", "a copy elsewhere."),
              ("Testing only the newest backup", "Older ones may be broken.", "random backups.")],
    use=["Nobody has done a full restore.", "Recovery targets exist (tiers).", "Auditors or clients ask how you know backups work.", "After changing databases or backup tools."],
    skip=["Data you can rebuild from elsewhere in minutes."],
    related=["<b>What Matters Most If Everything Fails?</b> (this volume)", "<b>Backups & Disaster Recovery</b> (cloud, vol. 6)", "<b>DR Tiers</b> (Ana, vol. 5)", "<b>Breaking Things on Purpose</b> (this volume)"],
    quiz=[("Where did the 3 h 40 go?", "Copying the backup (1 h 10), restoring and replaying (1 h 50), checking by hand (40 min)."),
          ("What made restores faster?", "Snapshots plus logs instead of copies, and scripted checks."),
          ("How often are restores tested?", "A random tier 1–2 backup monthly; a full timed drill quarterly."),
          ("What was the April drill's time?", "22 minutes."),
          ("Why restore a random backup, not the newest?", "Older backups can be broken too; you may need one.")],
    quiz_sit=[("The monthly restore check fails: yesterday's orders are missing from the restored copy. What do you do?", "Treat it as an incident (SEV3, maybe SEV2): find why the backup is incomplete, check other backups, fix it, and run the test again. A failed restore test is a gift: you found it on a quiet day.")],
    try_it="Restore your most important database from last night's backup onto a fresh server, with a stopwatch. Where did the time go? Write one script that checks the result.",
    remember="Nobody needs backups; everybody needs <span class=\"hl\">restores</span>. Restore, check and time one <span class=\"hl\">every month</span>.",
    sources=["Betsy Beyer et al., <i>Site Reliability Engineering</i> (2016): chapter 26, data integrity.",
             "AXELOS, <i>ITIL 4: Service continuity management</i> practice guide (2020).",
             "PostgreSQL documentation: continuous archiving and point-in-time recovery."],
)

# ------------------------------------------------------------------ 03 When the Picker App Is Down
mf_problem = Doodle(760, 260, "Doodle of a question at the store leads' meeting in January 2028, after the restore: if the picker app's back end were down for three hours on a Friday, what would the stores do? The picker app works offline for about two hours. After that, nobody knows. Tomás remembers a paper process from 2024 that nobody has used since.",
                    "Offline mode lasts about two hours. After that? A 2024 paper process nobody has used since.")
mf_problem.box(14, 30, 300, 100, "offline mode", "green", sub="≈ 2 hours", size=20, subsize=15)
mf_problem.arrow(320, 80, 360, 80)
mf_problem.box(366, 30, 380, 100, "after that?", "pink", sub="a 2024 paper process, never used", size=20, subsize=13)
mf_problem.note(380, 180, "tier 2 says 1 hour; reality says “we'd improvise”", "red", size=17)

mf_analogy = Doodle(760, 220, "Doodle of a hospital during a computer outage: paper charts in a drawer at every ward, a printed list of today's patients and their medicines refreshed every few hours, and a nurse who has practised it. When the system comes back, someone types the paper into it.",
                    "Paper charts in every ward, a printed list refreshed every few hours, and the paper typed in afterwards.")
mf_analogy.icon("ledger", 60, 40, 1.4)
mf_analogy.row([("paper charts", "in a drawer", "y"), ("printed list", "refreshed often", "blue"), ("type it in", "afterwards", "green")], x=170, y=40, h=96, w=180, gap=18, size=17, subsize=13)
mf_analogy.note(450, 190, "practised, not improvised", "pen", size=18)

mf_how = Doodle(760, 400, "Larder's store fallback from February 2028. Every 15 minutes the store laptop saves the next two hours of pick lists as printable files, offline. If the picker app is down for more than 30 minutes or offline mode is about to run out, the store lead declares 'paper'. Print the lists, pick on paper, tick items, write substitutions by hand; Dispatch by phone from a printed courier list; Sam's team tells affected customers. Switch-back: scan each paper order when the app returns; a reconciliation list shows what's left. First drill at Zuid on Wednesday 16 February 2028 at 06:00 for 45 minutes: picking at 60 percent of normal speed, 3 errors per 100 orders. Each store drills twice a year; the drills are the lists' best test.",
                "Pick lists saved offline every 15 min; “paper” declared by the store lead; scanned back after. Zuid's drill: 60 % speed.")
mf_how.box(14, 14, 236, 110, "every 15 min", "blue", sub="next 2 h of pick lists saved offline", size=17, subsize=12)
mf_how.box(262, 14, 236, 110, "declare “paper”", "pink", sub="down > 30 min or offline running out", size=17, subsize=12)
mf_how.box(510, 14, 236, 110, "switch back", "green", sub="scan paper orders · reconcile", size=17, subsize=12)
mf_how.box(14, 150, 732, 64, "pick on paper · write swaps by hand · Dispatch by phone · Sam tells customers", "y", size=14)
mf_how.box(14, 230, 732, 64, "Zuid drill, Wed 16 Feb 06:00, 45 min: 60 % speed · 3 errors / 100", "paper", size=15)
mf_how.note(380, 330, "every store drills twice a year", "pen", size=17)
mf_how.note(380, 366, "the printed copy of the plan lives in the store, not in the cloud", "red", size=15)

MANUAL_FALLBACK = dict(
    slug="manual-fallback",
    kicker="a.k.a. “business continuity at the front line”",
    tldr="When a system the front line depends on is down longer than its offline mode lasts, people need a <b>practised way to keep working without it</b>. Prepare the information they'll need <b>in advance</b> (lists saved offline, refreshed often), say <b>who declares the switch</b> and when, keep the steps <b>on paper in the store</b>, plan the <b>switch back</b>, and <b>drill it</b> so it's a routine rather than an improvisation.",
    chips=[("Family", "recovering"), ("Lives in", "a printed binder in every store; ops/continuity/store-paper.md"), ("Pairs with", "business impact analysis, invoking the plan, the store network (vol. 1)")],
    itil=dict(groups=["service"], chain=["design", "deliver"], practices=["service continuity management", "service desk"],
              sre="(graceful degradation, extended to people)", principles=["Think and work holistically", "Keep it simple and practical"],
              older="ITIL v3: business continuity (manual workarounds)"),
    problem_side="Larder, January 2028",
    problem="""  <p class="lead">At the store leads' meeting after the restore, Eli asks: if the picker app's back end were down for <b>three hours on a Friday</b>, what would the stores do? The picker app works offline for <b>about two hours</b>. <span class="hl-pink">After that, nobody knows.</span> Tomás remembers a paper process from 2024 that nobody has used since. Tier 2 says the picker back end must be back within an hour. Reality says “we'd improvise”.</p>
  <ul>
    <li>Systems have recovery plans; the people using them don't.</li>
    <li>The information needed on paper (what to pick) is inside the broken system.</li>
    <li>Nobody knows who decides to stop waiting and switch.</li>
  </ul>""",
    problem_figs=[mf_problem],
    analogy_side="paper charts in the hospital",
    analogy="""  <p>When a hospital's computers go down, every ward has <b>paper charts in a drawer</b> and a <b>printed list of today's patients and their medicines</b>, refreshed every few hours. A nurse who has practised it leads the switch. When the system comes back, someone <b>types the paper in</b>. It's slower, and it's safe.</p>""",
    analogy_figs=[mf_analogy],
    map=[("Paper charts in a drawer", "The printed fallback binder in each store"),
         ("The printed patient list", "Pick lists saved offline every 15 minutes"),
         ("The nurse who leads", "The store lead declares “paper”"),
         ("Typing the paper in", "Scanning paper orders back; reconciliation"),
         ("Practised", "A drill twice a year per store")],
    how_side="information saved in advance, one person declares, paper steps, a switch back, drills",
    how="""  <p>Eli, Tomás and Dee design the store fallback in February:</p>
  <ul>
    <li><b>Information in advance</b>: every 15 minutes the store laptop saves the <b>next two hours of pick lists</b> as printable files, kept offline, so the lists exist even if the cloud doesn't.</li>
    <li><b>One person declares</b>: if the picker app is down for <b>more than 30 minutes</b>, or offline mode is about to run out, the <b>store lead declares “paper”</b>.</li>
    <li><b>Paper steps</b>, in a printed binder at the packing bench: print the lists, pick and tick on paper, write substitutions by hand, run Dispatch by phone from a printed courier list. Sam's team tells affected customers.</li>
    <li><b>Switch back</b>: when the app returns, each paper order is scanned, and a reconciliation list shows what's left.</li>
  </ul>
  <p>The first drill is at <b>Zuid, Wednesday 16 February, 06:00, for 45 minutes</b>. Picking runs at <b>60 %</b> of normal speed with <b>3 errors per 100 orders</b>. Two fixes come out of it: bigger print, and swaps written on a sticker, not in the margin. Every store now drills <b>twice a year</b>.</p>""",
    how_figs=[mf_how],
    steps=[("Ask what people do when the system is down for longer than offline mode", "At the front line, per role."),
           ("Save the information they'll need in advance", "Offline, refreshed often."),
           ("Name who declares the switch, and when", "A person and a trigger."),
           ("Put the steps on paper where the work is", "Not in the cloud."),
           ("Plan the switch back", "Reconcile what was done on paper."),
           ("Drill it", "Twice a year per site.")],
    vocab=[("Manual fallback", "A way to keep working by hand when a system is down."),
           ("Business continuity", "Keeping the business running through disruption, not just restoring IT."),
           ("Offline mode", "An app working without its back end for a while."),
           ("Declaring the switch", "One named person deciding to move to the fallback."),
           ("Reconciliation", "Matching what was done by hand with the system afterwards."),
           ("Drill", "A planned practice of the fallback.")],
    code=dict(file="stores/binder/paper-mode.md", note="printed in every store · from February 2028", plain=True, src="""
  PAPER MODE                                                   (store lead decides)

  when    picker app down > 30 min, or offline mode about to run out (≈ 2 h)
  1       say "paper" in the store leads' group + call on-call
  2       laptop → folder "pick lists (offline)" → print the next 2 hours
  3       pick on paper · tick each item · swaps on the yellow stickers
  4       Dispatch by phone: printed courier list (refreshed daily)
  5       Sam's team tells customers (on-call tells Sam)
  back    when the app returns: scan each paper order (barcode at the top)
          → reconciliation list → finish what's left
  drills  twice a year · Zuid 16 Feb 2028: 45 min, 60 % speed, 3 errors / 100
"""),
    tools="tools: a scheduled export to the store laptop, a printer, a binder, yellow stickers and a drill date.",
    ladder=[("improvise", ["Nobody knows what to do after offline mode.", "Lists trapped in the system."]),
            ("a practised paper mode", ["Lists saved offline, store lead declares.", "Drills twice a year."]),
            ("smarter degraded modes", ["The app itself falls back to local lists for longer.", "Paper rarely needed."]),
            ("designed in", ["Every front-line tool has a fallback chosen at design.", "Drills routine."])],
    ladder_now=1,
    baseline="Each line compares <b>improvising after offline mode runs out</b> to <b>a drilled paper mode with lists saved offline</b>.",
    ratings=[(2, 4, "Orders keep moving at 60 % instead of stopping."),
             (3, 3, "Neutral."),
             (2, 3, "Back to normal with a reconciliation list."),
             (3, 3, "Neutral."),
             (2, 3, "Everyone knows the trigger and who decides."),
             (3, 3, "Neutral."),
             (3, 4, "A printer and a binder."),
             (2, 3, "On-call isn't the only plan."),
             (3, 3, "45 minutes twice a year per store.")],
    pitfalls=[("Information trapped in the system", "No lists to print.", "save them offline in advance."),
              ("Nobody declares", "Everyone waits for the system.", "a named person and a trigger."),
              ("No way back", "Paper orders lost in the switch.", "scan and reconcile."),
              ("Never drilled", "The binder is wrong when it matters.", "twice a year, fix after each.")],
    use=["Front-line work stops when a system does.", "Offline modes have limits.", "Recovery targets can't cover every case.", "New stores or sites open."],
    skip=["Work that can simply wait a few hours."],
    related=["<b>What Matters Most If Everything Fails?</b> (this volume)", "<b>Is It the Network?</b> (vol. 1)", "<b>Offline-First</b> (frontend, vol. 2)", "<b>Who Decides to Invoke the Plan?</b> (this volume)"],
    quiz=[("What does the store lead do when the picker app is down for more than 30 minutes?", "Declares “paper”: prints the saved lists and switches to the paper steps."),
          ("Why save pick lists offline every 15 minutes?", "So the information needed on paper exists even when the system that holds it is down."),
          ("How do paper orders get back into the system?", "Each is scanned when the app returns; a reconciliation list shows what's left."),
          ("What did Zuid's drill show?", "45 minutes at 60 % speed, 3 errors per 100; bigger print and swap stickers added."),
          ("How often do stores drill?", "Twice a year.")],
    quiz_sit=[("At 18:10 on a Friday the picker app has been down 25 minutes and IT expects a fix “soon”. Does Yara declare paper?", "Not yet: the trigger is 30 minutes. At 18:15, if it's still down and “soon” has no time attached, she declares paper. Switching back early costs little; waiting too long costs orders.")],
    try_it="Pick a front-line role in your organisation. If their main system were down for three hours, what would they do? What information would they need on paper, and is it available now, offline?",
    remember="Systems get recovery plans; <span class=\"hl\">people need fallbacks</span>. Save the lists in advance, name who declares, and <span class=\"hl\">drill it</span>.",
    sources=["AXELOS, <i>ITIL 4: Service continuity management</i> practice guide (2020).",
             "ISO 22301:2019, Business continuity management systems (overview).",
             "Atul Gawande, <i>The Checklist Manifesto</i> (2009)."],
)

# ------------------------------------------------------------------ 04 Breaking Things on Purpose
gd_problem = Doodle(760, 260, "Doodle of what Larder knew in February 2028 about its own failures: the failover works (tested monthly), restores work (tested monthly). But what happens if one Core VM disappears at the busy hour? If WMS B stops sending events? If a store loses both its line and its 4G? Each answer is a belief, not something anyone has seen.",
                    "Failover and restores are tested. Everything else (a VM gone, WMS B silent, a store cut off) is belief.")
for i, t in enumerate(["a Core VM gone?", "WMS B silent?", "store: no line, no 4G?", "PSP slow?"]):
    gd_problem.box(14 + i * 186, 40, 172, 90, t, "y", size=15)
gd_problem.note(380, 180, "“it should be fine” × 4", "red", size=19)

gd_analogy = Doodle(760, 220, "Doodle of a fire brigade training: they set real fires in a training building, on a planned day, with a safety officer and water ready, and practise exactly what they'll do on a bad night. Afterwards they talk through what went well and what didn't. The training fire is small, controlled and announced.",
                    "A real fire in a training building: planned, small, a safety officer, and a debrief after.")
gd_analogy.row([("planned day", None, "blue"), ("small fire", None, "pink"), ("safety officer", None, "y"), ("debrief", None, "green")], y=50, h=80, gap=14, size=17)
gd_analogy.note(380, 176, "practise the bad night in daylight", "pen", size=18)

gd_how = Doodle(760, 400, "Larder's game days from March 2028, the second Thursday of each month at 10:00. Each experiment has a hypothesis ('if core-2 stops, checkout keeps working with no errors visible to customers'), a small blast radius, a stop button and a watcher, and is announced. Game day 1, Thursday 9 March: stop core-2: checkout fine, but its alert named the wrong runbook; stop WMS B events in staging-like conditions: the absence alert fired in 5 minutes as designed; pull Utrecht's line and 4G together: the 'store on 4G' alert had never been set up for Utrecht. Findings go into the action list. Game day 2, 13 April, practised the major-incident roles with a pretend region outage. The 18 April restore drill counted as a game day too.",
                "Second Thursday, 10:00: a hypothesis, a small blast radius, a stop button, a watcher. Game day 1 found two gaps.")
gd_how.row([("hypothesis", "what should happen", "blue"), ("small blast", "one VM, one store", "y"), ("stop button", "and a watcher", "pink"), ("review", "findings → actions", "green")], y=14, h=96, gap=12, size=17, subsize=12)
gd_how.box(14, 134, 732, 140, None, "paper")
gd_how.head(380, 162, "game day 1 · Thu 9 Mar 2028", size=17)
gd_how.text(30, 194, "core-2 stopped → checkout fine · alert linked the wrong runbook ✗", anchor="start", size=14)
gd_how.text(30, 222, "WMS B events stopped → absence alert in 5 min ✓", anchor="start", size=14)
gd_how.text(30, 250, "Utrecht line + 4G pulled → no “store on 4G” alert set up ✗", anchor="start", size=14)
gd_how.note(380, 312, "game day 2 (13 Apr): major-incident roles, pretend region outage", "pen", size=15)
gd_how.note(380, 348, "the 18 April restore drill counted as one too", "pen", size=15)

GAME_DAYS = dict(
    slug="game-days",
    kicker="a.k.a. “game days and chaos experiments”",
    tldr="Some failures can only be understood by causing them. A <b>game day</b> is a planned, announced session where you break something on purpose, <b>in daylight</b>: one experiment at a time, each with a <b>hypothesis</b> of what should happen, a <b>small blast radius</b>, a <b>stop button</b> and a watcher. Then you compare what happened with what you believed, and turn every gap into an action. It's the only way “it should be fine” becomes “we've seen it”.",
    chips=[("Family", "recovering"), ("Lives in", "second Thursday, 10:00; ops/gamedays/YYYY-MM.md"), ("Pairs with", "restore tests, major incidents (vol. 2), runbooks (vol. 1)")],
    itil=dict(groups=["service"], chain=["improve", "deliver"], practices=["service continuity management", "service validation and testing", "incident management"],
              sre="“game days”, “disaster role-playing”, “chaos engineering”", principles=["Progress iteratively with feedback"],
              older="ITIL v3: continuity testing"),
    problem_side="Larder, February 2028",
    problem="""  <p class="lead">By February Larder tests two failures every month: <b>database failover</b> and <b>restores</b>. Everything else is belief. What happens if a Core VM disappears at the busy hour? If WMS B stops sending events? If a store loses its line <b>and</b> its 4G? If the payment provider slows down? <span class="hl-pink">Each answer is “it should be fine”, and nobody has seen it.</span></p>
  <ul>
    <li>Alerts, runbooks and fallbacks are trusted without being exercised.</li>
    <li>People practise incidents only during real ones.</li>
    <li>New stores inherit gaps nobody has looked for.</li>
  </ul>""",
    problem_figs=[gd_problem],
    analogy_side="the fire brigade's training fire",
    analogy="""  <p>Fire brigades don't learn on the bad night. They set <b>real fires in a training building</b>, on a planned day, with a <b>safety officer</b> and water ready, and practise exactly what they'll do. Afterwards they <b>talk through</b> what went well and what didn't. The fire is small, controlled and announced, and it's real enough to teach.</p>""",
    analogy_figs=[gd_analogy],
    map=[("The training building", "A Core VM, one store, WMS B events"),
         ("A planned day", "Second Thursday of the month, 10:00"),
         ("The safety officer", "A watcher with a stop button"),
         ("A small, controlled fire", "A small blast radius, one experiment at a time"),
         ("Talking it through", "Findings → actions")],
    how_side="a hypothesis, a small blast radius, a stop button, a review",
    how="""  <p>From <b>March</b>, Larder holds a game day on the <b>second Thursday at 10:00</b>, announced to Sam and the stores. Each experiment has a <b>hypothesis</b> (“if core-2 stops, checkout keeps working with no errors customers can see”), a <b>small blast radius</b>, a <b>stop button</b> and a <b>watcher</b>. There's one experiment at a time.</p>
  <p><b>Game day 1, Thursday 9 March</b>:</p>
  <ul>
    <li><b>core-2 stopped</b>: checkout is fine, as believed, but the alert links the <b>wrong runbook</b>.</li>
    <li><b>WMS B events stopped</b>: the absence alert fires in <b>5 minutes</b>, as designed.</li>
    <li><b>Utrecht's line and 4G pulled together</b>: the heartbeat alert fires, but the <b>“store on 4G” alert was never set up for Utrecht</b>. The city runbook gets a check for it.</li>
  </ul>
  <p><b>Game day 2</b> (13 April) practises the major-incident roles with a pretend region outage. The <b>18 April restore drill</b> counts as a game day too. Each finding becomes an action with an owner.</p>""",
    how_figs=[gd_how],
    steps=[("Pick a failure you only believe you handle", "From the dependency map and the risk register."),
           ("Write the hypothesis", "What exactly should happen?"),
           ("Keep the blast radius small", "One VM, one store, a quiet hour."),
           ("Announce it and name a watcher", "With a stop button."),
           ("Run one experiment at a time", "Observe, write down."),
           ("Turn gaps into actions", "Owners, dates, next game day.")],
    vocab=[("Game day", "A planned session for practising failures and responses."),
           ("Chaos experiment", "Deliberately injecting a failure to test a hypothesis about resilience."),
           ("Hypothesis", "What you believe will happen when the failure occurs."),
           ("Blast radius", "How much could be affected if the experiment goes wrong."),
           ("Stop button", "A way to end the experiment immediately."),
           ("Tabletop exercise", "Talking through a scenario without breaking anything.")],
    code=dict(file="ops/gamedays/2028-03.md", note="game day 1 · Thu 9 March 2028, 10:00", plain=True, src="""
# Game day 1                                   watcher: Bram · stop: Eli · announced: Sam, stores

exp  failure                       hypothesis                          result
1    stop core-2 (10:05–10:20)     checkout fine, alert in 2 min       fine ✓ · alert → WRONG runbook ✗
2    stop WMS B events (staging-   absence alert in ≤ 5 min            fired in 5 min ✓
     like copy, 10:30)
3    Utrecht: line + 4G pulled     heartbeat alert + "store on 4G"     heartbeat ✓ · "on 4G" alert
     (10:50, 10 min, store told)   ticket                              never set up for Utrecht ✗
actions  fix alert link (Bram, 10 Mar) · "on 4G" alert for every store + city runbook check (Eli, 17 Mar)
next     13 Apr: major-incident roles, pretend region outage (tabletop + comms)
"""),
    tools="tools: the ability to stop things safely (VMs, event streams, store links), a watcher, a calendar slot and a one-page template.",
    ladder=[("“it should be fine”", ["Beliefs untested.", "Practice only in real incidents."]),
            ("monthly game days", ["Hypothesis, small blast radius, stop button.", "Findings → actions."]),
            ("automated experiments", ["Small experiments run on a schedule.", "Results tracked."]),
            ("resilience by default", ["New services join game days at launch.", "Surprises rare."])],
    ladder_now=1,
    baseline="Each line compares <b>believing failures are handled</b> to <b>monthly game days with hypotheses and a stop button</b>.",
    ratings=[(3, 3, "Neutral: experiments are small and announced."),
             (2, 4, "Gaps found and fixed before real failures."),
             (2, 4, "Runbooks and alerts checked by use."),
             (3, 3, "Neutral."),
             (2, 4, "What really happens is seen and written down."),
             (3, 3, "Neutral."),
             (3, 3, "A morning a month."),
             (2, 4, "On-call practises in daylight."),
             (3, 3, "A morning a month.")],
    pitfalls=[("Big experiments first", "A game day becomes an outage.", "small blast radius, one at a time."),
              ("No hypothesis", "You watch, but learn nothing.", "write what should happen first."),
              ("Not announced", "Stores and support think it's real.", "announce it, and say it's a test."),
              ("Findings not followed", "The same gaps next game day.", "actions with owners and dates.")],
    use=["You believe failures are handled but haven't seen it.", "New on-call people need practice.", "Before a peak or a handover.", "After building a fallback or alert."],
    skip=["When basic monitoring and runbooks don't exist yet: build those first."],
    related=["<b>Chaos Engineering</b> (cloud, vol. 6)", "<b>Can We Actually Restore?</b> (this volume)", "<b>When Is It a Major Incident?</b> (vol. 2)", "<b>Handing Over the Pager</b> (vol. 6)"],
    quiz=[("What does every experiment need?", "A hypothesis, a small blast radius, a stop button, a watcher, and an announcement."),
          ("What did game day 1 find?", "A wrong runbook link on core-2's alert, and no “store on 4G” alert for Utrecht."),
          ("Why one experiment at a time?", "So you know what caused what, and can stop cleanly."),
          ("What is a tabletop exercise?", "Talking through a scenario without breaking anything (game day 2's region outage)."),
          ("What happens to findings?", "They become actions with owners and dates.")],
    quiz_sit=[("During a game day, stopping core-2 unexpectedly makes checkout errors rise to 3 %. What does the watcher do?", "Press stop: start core-2 again, check errors drop, and record it. The hypothesis was wrong, which is exactly what game days are for. Find why before trying again.")],
    try_it="Write one belief about a failure you handle (“if X stops, Y happens”). Plan the smallest safe way to test it, with a watcher and a stop button. What would you need to fix if the belief were wrong?",
    remember="Turn “<span class=\"hl\">it should be fine</span>” into “<span class=\"hl\">we've seen it</span>”: small, announced, with a stop button, on a planned day.",
    sources=["Betsy Beyer et al., <i>Site Reliability Engineering</i> (2016): chapter 28, accelerating SREs to on-call (disaster role-playing).",
             "Casey Rosenthal and Nora Jones, <i>Chaos Engineering</i> (O'Reilly, 2020).",
             "AXELOS, <i>ITIL 4: Service continuity management</i> practice guide (2020)."],
)

# ------------------------------------------------------------------ 05 Who Decides to Invoke the Plan?
ip_problem = Doodle(760, 260, "Doodle of game day 2, Thursday 13 April 2028, a tabletop exercise: 'Frankfurt region down, it's Friday 17:30, nobody knows for how long.' ADR 0026 says a pilot-light copy in Paris can be running in about 4 hours, at a cost, if the region is out for more than an hour. In the exercise, the group spends 40 minutes discussing who may decide to start it. Femke is on a plane in the scenario. Nobody else is sure they're allowed.",
                    "A pretend region outage. The plan existed. 40 minutes went on “who's allowed to start it?”")
ip_problem.box(14, 30, 300, 100, "Frankfurt down", "pink", sub="Fri 17:30 (tabletop)", size=20, subsize=14)
ip_problem.box(346, 30, 400, 100, "Paris pilot light", "green", sub="≈ 4 h to run · ADR 0026", size=20, subsize=14)
ip_problem.note(380, 180, "40 minutes: who may decide? (Femke on a plane)", "red", size=18)

ip_analogy = Doodle(760, 220, "Doodle of a ship's captain and first officer. The decision to abandon ship belongs to the captain; if the captain can't, the first officer decides, by rule. The signs that force the decision are written down, and there's a time by which they must decide. Nobody holds a meeting about who's in charge while the water rises.",
                    "Abandon ship: the captain decides, or the first officer by rule, by written signs, within a set time.")
ip_analogy.icon("ship", 40, 60, 1.0)
ip_analogy.row([("captain", "decides", "y"), ("first officer", "if captain can't", "y"), ("written signs", "force the call", "pink")], x=170, y=40, h=96, w=180, gap=18, size=17, subsize=13)
ip_analogy.note(450, 190, "no meeting about who's in charge while the water rises", "pen", size=17)

ip_how = Doodle(760, 400, "Larder's crisis team and invocation rules, written after the 13 April tabletop. The crisis team: Femke decides; if she can't be reached in 15 minutes, Marco, then Joost. Advising: Eli (IT), Joost (operations), Sam (customers), Lena (legal), Mo (business clients). Triggers: region outage beyond 1 hour or no estimate; a city unable to operate for 2 hours; a suspected data breach; a key vendor out for a business day. Decision clock: at 30 minutes of a major incident the incident lead asks 'should we invoke?'; the decision is made by 60 minutes, written in the decision log. Invoking means: start the pilot light, declare paper mode in stores, switch customer messages. Practised again on 11 May: decision in 12 minutes.",
                "A named decider and two deputies, written triggers, and a decision clock: asked at 30 minutes, decided by 60.")
ip_how.row([("Femke", "decides", "y"), ("Marco", "if no answer in 15 min", "paper"), ("Joost", "then", "paper")], x=14, y=14, h=86, w=236, gap=12, size=18, subsize=12)
ip_how.box(14, 116, 732, 56, "advise: Eli · Joost · Sam · Lena · Mo", "blue", size=15)
ip_how.box(14, 186, 732, 90, None, "paper")
ip_how.text(380, 214, "triggers: region > 1 h or no estimate · a city stopped 2 h", size=14)
ip_how.text(380, 242, "suspected data breach · key vendor out a business day", size=14)
ip_how.row([("30 min", "lead asks “invoke?”", "y"), ("60 min", "decided, logged", "pink"), ("11 May", "re-run: 12 min", "green")], x=14, y=292, h=80, gap=40, size=17, subsize=13, arrows=True)

INVOKING = dict(
    slug="invoking-the-plan",
    kicker="a.k.a. “crisis management and invocation”",
    tldr="A continuity plan is useless if nobody feels allowed to start it. Name <b>one person who decides</b>, and <b>deputies in order</b> for when they can't be reached. Write the <b>triggers</b> that force the question, and set a <b>decision clock</b>: asked at a fixed point in a major incident, decided by another, logged either way. Then practise the decision itself, not only the technology.",
    chips=[("Family", "recovering"), ("Lives in", "ops/continuity/crisis-team.md; the major-incident procedure"), ("Pairs with", "major incidents (vol. 2), the living plans, Ana's multi-region ADR")],
    itil=dict(groups=["service", "general"], chain=["deliver", "engage"], practices=["service continuity management", "risk management"],
              sre="(incident command at the business level)", principles=["Collaborate and promote visibility", "Keep it simple and practical"],
              older="ITIL v3: ITSCM invocation, the crisis management team"),
    problem_side="Larder, Thursday 13 April 2028",
    problem="""  <p class="lead">Game day 2 is a tabletop exercise: <b>“The Frankfurt region is down. It's Friday 17:30. Nobody knows for how long.”</b> Ana's ADR 0026 says a <b>pilot-light copy in Paris</b> can be running in about <b>4 hours</b>, at a cost, if the region is out for more than an hour. <span class="hl-pink">The group spends 40 minutes discussing who is allowed to start it.</span> In the scenario Femke is on a plane, and nobody else is sure they may spend the money or tell the stores to go to paper.</p>
  <ul>
    <li>Plans describe how to switch, not who decides to.</li>
    <li>Every minute of “who's allowed?” is a minute of the four hours.</li>
    <li>The people who'd advise (legal, customers) aren't named.</li>
  </ul>""",
    problem_figs=[ip_problem],
    meanwhile=[("architect-5", "multi-region", "Ana's ADR 0026: a pilot light in Paris (≈ €1,200 a month, RTO 4 hours) instead of a second region; triggers include a region outage over an hour.",
                "Eli's side: who may decide to start it, by when, and what else happens when they do (paper mode, customer messages).")],
    analogy_side="the captain and the first officer",
    analogy="""  <p>On a ship, the decision to <b>abandon ship</b> belongs to the captain. If the captain can't make it, <b>the first officer decides, by rule</b>. The signs that force the question are written down, and there's a time by which it must be decided. Nobody holds a meeting about who's in charge <b>while the water rises</b>.</p>""",
    analogy_figs=[ip_analogy],
    map=[("The captain", "Femke"),
         ("The first officer, by rule", "Marco, then Joost, if Femke can't be reached in 15 minutes"),
         ("The written signs", "Triggers: region > 1 h, a city stopped 2 h, a breach, a vendor out a day"),
         ("Abandoning ship", "Starting the Paris pilot light, paper mode, customer messages"),
         ("Decided within a set time", "Asked at 30 minutes, decided by 60")],
    how_side="one decider, deputies, triggers, and a decision clock",
    how="""  <p>After the tabletop, Eli writes the <b>crisis team</b> page with Femke:</p>
  <ul>
    <li><b>Decides</b>: Femke. If she can't be reached within <b>15 minutes</b>: <b>Marco</b>, then <b>Joost</b>. Each has agreed in writing.</li>
    <li><b>Advises</b>: Eli (IT), Joost (operations), Sam (customers), Lena (legal), Mo (business clients).</li>
    <li><b>Triggers</b>: a region outage <b>beyond an hour</b> or with no estimate; a city <b>unable to operate for 2 hours</b>; a suspected <b>data breach</b>; a key vendor out for a <b>business day</b>.</li>
    <li><b>Decision clock</b>: at <b>30 minutes</b> of a major incident with a trigger, the incident lead asks “should we invoke?”, and the answer is decided <b>by 60 minutes</b> and written in the decision log, yes or no.</li>
    <li><b>Invoking means</b>: start the pilot light, declare paper mode in the affected stores, switch customer messages to the continuity templates, and tell Korenwolf through Mo.</li>
  </ul>
  <p>The tabletop is run again on <b>11 May</b>. The decision takes <b>12 minutes</b>, with Marco deciding because “Femke” is again on a plane.</p>""",
    how_figs=[ip_how],
    steps=[("Name one decider", "And agree it with them."),
           ("Name deputies in order", "With a time to try the decider first."),
           ("Write the triggers", "The signs that force the question."),
           ("Set a decision clock", "Asked at a fixed point, decided by another."),
           ("Say what invoking means", "Every action that follows, per team."),
           ("Practise the decision", "A tabletop with the real people.")],
    vocab=[("Invocation", "The decision to switch to a continuity plan."),
           ("Crisis team", "The small group that decides and coordinates in a serious disruption."),
           ("Deputy", "The person who decides if the decider can't."),
           ("Trigger", "A condition that forces the invocation question."),
           ("Decision clock", "Fixed times for asking and deciding."),
           ("Pilot light", "A minimal copy of the system in another region, ready to scale up.")],
    code=dict(file="ops/continuity/crisis-team.md", note="after the tabletop of 13 April 2028 · signed by Femke", plain=True, src="""
# Crisis team

decides      Femke · if not reached in 15 min: Marco · then Joost   (agreed 20 Apr)
advises      Eli (IT) · Joost (operations) · Sam (customers) · Lena (legal) · Mo (clients)
triggers     region outage > 1 h or no estimate · a city can't operate for 2 h
             · suspected data breach · key vendor out for a business day
clock        major incident + trigger: at 30 min the lead asks "invoke?"
             decided by 60 min · yes or no in the decision log
invoking =   Paris pilot light (≈ 4 h, ADR 0026) · paper mode in affected stores
             · continuity customer messages · Mo tells Korenwolf · Lena on notifications
practice     tabletop 13 Apr: 40 min "who decides?" · re-run 11 May: 12 min (Marco)
"""),
    tools="tools: one signed page, contact details that work out of hours, the decision log, and a tabletop twice a year.",
    ladder=[("a plan with no decider", ["Who's allowed?", "Minutes lost to doubt."]),
            ("a crisis team and a clock", ["Decider, deputies, triggers.", "Practised in tabletops."]),
            ("invocation rehearsed end to end", ["Decision and technology practised together.", "Timed."]),
            ("rarely needed", ["Most failures handled below the crisis level.", "Invocation a known, calm step."])],
    ladder_now=1,
    baseline="Each line compares <b>a plan nobody feels allowed to start</b> to <b>a named decider, deputies, triggers and a decision clock</b>.",
    ratings=[(2, 4, "The 4-hour switch starts in minutes, not after a debate."),
             (3, 3, "Neutral."),
             (2, 4, "Decision in 12 minutes instead of 40."),
             (3, 3, "Neutral."),
             (2, 4, "Everyone knows who decides and when."),
             (3, 3, "Neutral."),
             (2, 3, "Spending authority is clear in advance."),
             (2, 3, "The incident lead isn't left with a CEO-level call."),
             (3, 3, "A page and two tabletops a year.")],
    pitfalls=[("Only the technology practised", "The switch works; nobody starts it.", "practise the decision."),
              ("A single decider", "Unreachable on the day.", "deputies in order."),
              ("No triggers", "The question is never asked.", "written triggers and a clock."),
              ("Invoking means only IT", "Stores and clients aren't told.", "list every action that follows.")],
    use=["You have a continuity plan (a pilot light, paper mode).", "A tabletop stalled on “who decides?”.", "Leaders travel or are often unreachable.", "Before a peak or a contract with continuity terms."],
    skip=["When there's nothing to invoke: build the plan first."],
    related=["<b>When Is It a Major Incident?</b> (vol. 2)", "<b>When to Go Multi-Region</b> (Ana, vol. 5)", "<b>The Plan Nobody Has Read</b> (next note)", "<b>When the Picker App Is Down</b> (this volume)"],
    quiz=[("Who decides to invoke at Larder?", "Femke; if not reached in 15 minutes, Marco, then Joost."),
          ("What are the triggers?", "Region outage beyond an hour or no estimate, a city stopped 2 hours, a suspected breach, a key vendor out a business day."),
          ("What is the decision clock?", "At 30 minutes of a major incident with a trigger, the lead asks; decided by 60 minutes, logged."),
          ("What does invoking set in motion?", "The Paris pilot light, paper mode in stores, continuity messages, Mo telling Korenwolf, Lena on notifications."),
          ("What changed between the two tabletops?", "40 minutes on “who decides?” → a decision in 12 minutes.")],
    quiz_sit=[("A region has been down 50 minutes with an estimate of “30 more minutes”. Femke says wait. Is that allowed?", "Yes: deciding not to invoke is a decision, logged with the reason. The clock forces a decision, not a particular one; she can be asked again if the estimate slips.")],
    try_it="For your worst plausible outage, write who decides to switch to the fallback, who decides if they can't, what forces the question, and by when. Run a 30-minute tabletop with those people.",
    remember="A plan nobody may start is no plan. Name <span class=\"hl\">who decides</span>, who deputises, and <span class=\"hl\">by when</span>, and practise the decision.",
    sources=["AXELOS, <i>ITIL 4: Service continuity management</i> practice guide (2020): invocation.",
             "ISO 22301:2019 and ISO 22361:2022 (crisis management), overviews.",
             "Betsy Beyer et al., <i>Site Reliability Engineering</i> (2016): chapter 14, managing incidents."],
)

# ------------------------------------------------------------------ 06 The Plan Nobody Has Read
lp_problem = Doodle(760, 260, "Doodle of Larder's disaster recovery plan as Eli found it in January 2028: 31 pages, last edited in March 2026, describing StockPilot, Larder Core on VMs patched by hand, two stores and an on-call number that no longer exists. It lived in a shared drive in the same cloud it was meant to help recover. Nobody on the rota had read it.",
                    "31 pages, last edited March 2026, describing systems that no longer exist, stored in the cloud it should recover.")
lp_problem.icon("ledger", 50, 40, 1.6)
lp_problem.box(160, 30, 280, 110, "DR plan v1", "paper", sub="31 pages · Mar 2026", size=20, subsize=15)
lp_problem.box(470, 30, 276, 110, "mentions", "pink", sub="StockPilot · 2 stores · old number", size=18, subsize=13)
lp_problem.note(380, 190, "stored in the cloud it was meant to help recover", "red", size=18)
lp_problem.note(380, 226, "read by: nobody on the rota", "pen", size=17)

lp_analogy = Doodle(760, 220, "Doodle of the safety card in an aircraft seat pocket: one card, pictures more than words, updated whenever the aircraft changes, and read out loud before every flight. Compare a manual of a hundred pages in the cockpit nobody opens.",
                    "The seat-pocket safety card: one page, pictures, updated with the aircraft, read out before every flight.")
lp_analogy.box(14, 40, 340, 100, "100-page manual", "pink", sub="nobody opens it", size=18, subsize=14)
lp_analogy.box(406, 40, 340, 100, "one safety card", "green", sub="updated · read before every flight", size=18, subsize=13)
lp_analogy.note(380, 190, "short, current, and used", "pen", size=18)

lp_how = Doodle(760, 400, "Larder's continuity plans from February 2028: one or two pages per scenario, five scenarios. Ordering database lost; a cloud region down; a store cut off (paper mode); a key vendor out; the office and sign-in down. Each plan: the trigger, who decides, the steps with links to runbooks, how to switch back, the owner, and a 'last tested' date. Plans live in the repo, are printed in the stores' binders, and copied every week to laptops and a second cloud account, so they can be read when the cloud is down. Every test or real use changes the plan within a week. Review: each plan tested at least once a year; a plan untested for 12 months turns red on the monthly service review.",
                "Five short plans, each with an owner and a last-tested date, readable when the cloud is down, changed after every test.")
for i, t in enumerate(["ordering DB lost", "region down", "store cut off", "vendor out", "office + sign-in"]):
    lp_how.box(14 + i * 148, 14, 136, 70, t, "y", size=14)
lp_how.box(14, 104, 732, 64, "trigger · who decides · steps (→ runbooks) · switch back · owner · last tested", "blue", size=14)
lp_how.box(14, 186, 732, 64, "repo + printed in stores + weekly copy to laptops and a second account", "green", size=14)
lp_how.box(14, 268, 732, 56, "changed within a week of every test · untested 12 months → red on the review", "paper", size=14)
lp_how.note(380, 362, "31 pages → five plans of one or two pages", "pen", size=17)

LIVING_PLANS = dict(
    slug="living-plans",
    kicker="a.k.a. “keeping continuity plans alive”",
    tldr="Continuity plans rot quietly: systems change, people leave, and the plan describes a company that no longer exists. Keep them <b>short</b> (a page or two per scenario), <b>owned</b>, stamped with a <b>last-tested date</b>, <b>readable when your systems are down</b> (printed, offline, in another account), and <b>changed after every test or real use</b>. A plan untested for a year is a warning, not a comfort.",
    chips=[("Family", "recovering"), ("Lives in", "ops/continuity/plans/*.md, printed binders, offline copies"), ("Pairs with", "invoking the plan, game days, restore tests")],
    itil=dict(groups=["service", "general"], chain=["improve", "plan"], practices=["service continuity management", "knowledge management"],
              sre="(playbooks kept current by use)", principles=["Keep it simple and practical", "Progress iteratively with feedback"],
              older="ITIL v3: ITSCM plans, maintenance and review"),
    problem_side="Larder, January 2028",
    problem="""  <p class="lead">Looking for Larder's disaster recovery plan after the restore, Eli finds one: <b>31 pages</b>, last edited in <b>March 2026</b>. It describes StockPilot, Larder Core on hand-patched VMs, <b>two stores</b>, and an on-call number that no longer exists. It lives on a shared drive <b>in the same cloud it's meant to help recover</b>. <span class="hl-pink">Nobody on the on-call rota has read it.</span></p>
  <ul>
    <li>A long plan is written once and never read.</li>
    <li>A plan stored in the failed system can't be opened when it's needed.</li>
    <li>Without tests, nobody notices it's wrong.</li>
  </ul>""",
    problem_figs=[lp_problem],
    analogy_side="the seat-pocket safety card",
    analogy="""  <p>An aircraft's <b>safety card</b> is one page, mostly pictures, <b>updated whenever the aircraft changes</b>, and read out before every flight. Somewhere there's also a hundred-page manual nobody opens. When something goes wrong, people use the card.</p>""",
    analogy_figs=[lp_analogy],
    map=[("The hundred-page manual", "The 31-page DR plan from 2026"),
         ("The safety card", "A one- or two-page plan per scenario"),
         ("Updated with the aircraft", "Changed within a week of every test or change"),
         ("In every seat pocket", "Printed in stores, offline on laptops, in a second account"),
         ("Read before every flight", "Tested at least yearly; red if not")],
    how_side="short plans per scenario, readable offline, changed after every test",
    how="""  <p>In <b>February</b> Eli replaces the 31 pages with <b>five plans</b> of one or two pages each, one per scenario: the ordering database lost, a cloud region down, a store cut off (paper mode), a key vendor out, and the office and sign-in down (this volume). Each plan has the same parts: the <b>trigger</b>, <b>who decides</b>, the <b>steps</b> (linking to runbooks), how to <b>switch back</b>, an <b>owner</b> and a <b>last tested</b> date.</p>
  <ul>
    <li><b>Readable when systems are down</b>: in the repo, <b>printed</b> in the store binders, and copied every week to laptops and a <b>second cloud account</b>.</li>
    <li><b>Changed after every use</b>: every test or real invocation changes the plan within a week.</li>
    <li><b>Tested at least yearly</b>: a plan untested for 12 months turns <b>red</b> on the monthly service review.</li>
  </ul>
  <p>By June every plan has been tested once: two by game days, one by the April restore drill, one by Zuid's paper drill, and one for real (the office plan, in May).</p>""",
    how_figs=[lp_how],
    steps=[("Find every plan and check its date", "And what it describes."),
           ("Split into one plan per scenario", "One or two pages each."),
           ("Give each an owner and a last-tested date", "Visible on the plan."),
           ("Make them readable when systems are down", "Printed, offline, another account."),
           ("Change the plan after every test", "Within a week."),
           ("Turn untested plans red", "On the monthly review.")],
    vocab=[("Continuity plan", "The steps to keep the business running through a specific disruption."),
           ("Scenario", "A specific kind of disruption the plan is for."),
           ("Plan rot", "A plan drifting out of date as systems and people change."),
           ("Last tested", "The date a plan was last exercised for real or in a drill."),
           ("Offline copy", "A copy that can be read without the systems it's about."),
           ("Plan owner", "The person who keeps a plan current and tested.")],
    code=dict(file="ops/continuity/plans/README.md", note="from February 2028", plain=True, src="""
plan                         owner   pages  last tested             how
ordering database lost       Eli     2      18 Apr 2028 (drill)      restore drill, 22 min
cloud region down            Eli     2      13 Apr / 11 May          tabletop × 2
store cut off (paper mode)   Tomás   1      16 Feb 2028 (Zuid)       paper drill
key vendor out               Cho     1      9 Mar 2028 (game day 1)  WMS B events stopped
office + sign-in down        Sam     1      16 May 2028 (real)       sign-in provider outage

every plan: trigger · who decides · steps → runbooks · switch back · owner · last tested
copies:     repo · printed in store binders · weekly to laptops + second cloud account
rule:       changed ≤ 1 week after any test or use · untested 12 months → red
replaced:   "DR plan v1" (31 pages, Mar 2026) → archived
"""),
    tools="tools: markdown plans in the repo, a weekly export to laptops and another account, a printer, and the monthly review.",
    ladder=[("one long plan, never read", ["Out of date.", "Stored in the failing system."]),
            ("short plans, owned, tested", ["Readable offline.", "Changed after every test."]),
            ("plans linked to tests", ["The last-tested date filled in by the game day log.", "Red automatically."]),
            ("plans as practice", ["Every plan exercised several times a year.", "Changes routine."])],
    ladder_now=1,
    baseline="Each line compares <b>one 31-page plan from 2026</b> to <b>five short, owned, tested plans readable offline</b>.",
    ratings=[(2, 4, "Plans that work when needed."),
             (3, 3, "Neutral."),
             (2, 4, "People find the right steps quickly."),
             (3, 3, "Neutral."),
             (2, 4, "Owner and last-tested date on every plan."),
             (3, 3, "Neutral."),
             (3, 3, "Neutral."),
             (2, 3, "On-call has read them."),
             (3, 4, "Five short pages instead of thirty-one.")],
    pitfalls=[("One giant plan", "Nobody reads it.", "one short plan per scenario."),
              ("Stored only in the failing system", "Can't be opened when needed.", "printed and offline copies."),
              ("Never changed after tests", "Lessons lost.", "change within a week."),
              ("No owner", "It rots.", "an owner per plan.")],
    use=["You find a plan nobody has read.", "Systems have changed since the plan was written.", "After a test or real use.", "Before an audit or questionnaire."],
    skip=["Never, if you have anything to recover."],
    related=["<b>Who Decides to Invoke the Plan?</b> (this volume)", "<b>Where Is That Written Down?</b> (vol. 1)", "<b>Breaking Things on Purpose</b> (this volume)", "<b>When the Office Is the Outage</b> (this volume)"],
    quiz=[("What was wrong with the 2026 DR plan?", "31 pages, out of date (StockPilot, two stores, an old number), stored in the cloud it should recover, and unread."),
          ("What does each new plan contain?", "Trigger, who decides, steps linking to runbooks, switch back, owner, last-tested date."),
          ("Where are the plans kept?", "In the repo, printed in store binders, and copied weekly to laptops and a second cloud account."),
          ("When must a plan be changed?", "Within a week of any test or real use."),
          ("What happens to a plan untested for 12 months?", "It turns red on the monthly service review.")],
    quiz_sit=[("A game day shows the region plan's step 4 uses a command that no longer exists. Whose job is it, and by when?", "The plan's owner (Eli), within a week; and the test date goes on the plan. That's the plan doing its job: finding the rot before a real outage.")],
    try_it="Find your continuity or DR plan. When was it last changed, and does it describe today's systems? Could you open it if your main systems were down? Rewrite the most important scenario on one page.",
    remember="A plan is <span class=\"hl\">short, owned, tested and readable offline</span>, or it's a document about a company that no longer exists.",
    sources=["AXELOS, <i>ITIL 4: Service continuity management</i> practice guide (2020): maintaining plans.",
             "ISO 22301:2019: exercising and testing (overview).",
             "Atul Gawande, <i>The Checklist Manifesto</i> (2009)."],
)

NOTES = [BUSINESS_IMPACT, RESTORE_TESTS, MANUAL_FALLBACK, GAME_DAYS, INVOKING, LIVING_PLANS]
