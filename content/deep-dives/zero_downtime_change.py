# Deep dive 06 · Zero-Downtime Change. Builds on Vol. 3 note 10 (expand & contract) and Vol. 6 notes 01 (blue-green),
# 02 (canary) and 03 (feature flags). Example, from the expand & contract note: renaming users.name to
# users.full_name on a 200-million-row table, while 20 app instances keep serving traffic.
# Helpers (mn, full, tbl, drill, code, fig, checklist) are injected by scripts/build_notes.py from scripts/dive.py.

# ------------------------------------------------------------------ 1 recap
recap = '''
<p>The expand and contract note had one example: the <code>users</code> table has a column <code>name</code>, and it should be called <code>full_name</code>. The table has 200 million rows and the site may not go down. The note's answer was five small deploys. Three notes from the cloud volume described how code gets out.</p>
''' + tbl(["Note", "In one line", "It controls"], [
    ["Expand &amp; Contract", "add the new thing beside the old, move over in steps, remove the old thing last", "the shape of the data"],
    ["Blue–Green", "run the new version beside the old one, switch all traffic at once", "which version runs"],
    ["Canary", "send a small share of traffic to the new version and widen while it stays healthy", "how many users get it"],
    ["Feature Flags", "ship code switched off; turn it on later without a deploy", "which behaviour is on"],
]) + mn("Four notes, four dials. A real change turns all four, in a fixed order.") + '''
<p class="full">Each note is one tool. A real change, even one as dull as renaming a column, uses all of them over one or two weeks, and the order matters. This deep dive follows that single rename from the first <code>ALTER TABLE</code> to the last <code>DROP COLUMN</code>: what is deployed at each step, what must be true before the next, what can go wrong, and how to go back. The rename is trivial on purpose. Everything hard about it is hard for every change.</p>
'''

# ------------------------------------------------------------------ 2 mixed versions
window_svg = '''
  <text class="lbl" x="20" y="26">one rolling deploy of 20 instances</text>
  <rect class="bx" x="20" y="44" width="420" height="40" rx="6"/><text class="lbl" x="150" y="70" text-anchor="middle">version 1 running</text>
  <rect class="bx-g" x="260" y="96" width="480" height="40" rx="6"/><text class="lbl" x="600" y="122" text-anchor="middle">version 2 running</text>
  <rect class="bx-r" x="260" y="44" width="180" height="92" rx="0" fill-opacity=".5"/><text class="lbl bad" x="350" y="36" text-anchor="middle">both at once</text>
  <path class="ln" d="M20 152 H740"/>
  <text class="soft" x="20" y="174">12:00</text><text class="soft" x="260" y="174" text-anchor="middle">12:02</text><text class="soft" x="440" y="174" text-anchor="middle">12:12</text><text class="soft" x="740" y="174" text-anchor="end">later</text>
  <text class="soft" x="350" y="196" text-anchor="middle">ten minutes, on every deploy, with one database</text>
'''
window = '''
<p>The picture in most heads is: the old version stops, the new one starts. It has never been true. A deploy replaces instances a few at a time, so for a while both versions serve requests, and they share one database.</p>
''' + fig(760, 205, "A rolling deploy of 20 instances on a timeline. Version 1 runs from 12:00 until 12:12. Version 2 starts at 12:02 and continues. Between 12:02 and 12:12 both versions run at once against the same database.",
          window_svg, "The window is short, and it happens on every deploy. A rollback opens it again in the other direction.") + '''
<p>The window is longer than the deploy, because the old version lives on in other places.</p>
''' + tbl(["Where old code or old data still lives", "For how long"], [
    ["app instances not yet replaced", "minutes"],
    ["requests and jobs that started before the deploy", "seconds to hours"],
    ["messages in a queue, written by the old version", "until they are consumed, or replayed"],
    ["pages and API responses in a cache", "their TTL"],
    ["the previous version, if you roll back", "any time in the next days"],
    ["mobile apps that users have not updated", "months"],
    ["other teams' reports and scripts that read your tables", "until someone tells them"],
], hot=(4,)) + mn("Rollback is the one people forget. It means the OLD code must work with whatever the NEW code already did.") + '''
<h3>The rule everything follows from</h3>
<p><mark>At every moment, the database must work for the version that is running, the version about to run, and the version you might roll back to.</mark></p>
''' + full('''<p>Try the naive rename against that rule. One migration renames the column, one deploy ships code that uses the new name.</p>
''' + tbl(["", "Schema: <code>name</code>", "Schema: <code>full_name</code>"], [
    ["Code v1 (uses <code>name</code>)", "works", "<b>crashes</b>: column does not exist"],
    ["Code v2 (uses <code>full_name</code>)", "<b>crashes</b>: column does not exist", "works"],
], hot=(0, 1)) + '''<p>Whichever is changed first, schema or code, one of the tinted cells is live for the length of the window. There is no order that works, and rolling back the code lands in a tinted cell as well.</p>
<p>The fix is to never be in a column of that table that only one version understands. For a while the schema has <b>both</b> names, and every version works. That in-between schema is the whole idea of expand and contract. The cost is that one change becomes several, each of which is safe alone.</p>
<p>Three things carry a version: the <b>code</b>, the <b>schema</b>, and the <b>data</b> already in the rows. They change at different speeds. Code changes in minutes. A schema change takes seconds, or hours on a large table. Data follows last, as fast as a backfill can copy it. A plan is a sequence in which the three never disagree.</p>''')

# ------------------------------------------------------------------ 3 the plan
plan_svg = '''
  <text class="soft" x="150" y="24" text-anchor="middle">1</text><text class="soft" x="236" y="24" text-anchor="middle">2</text><text class="soft" x="322" y="24" text-anchor="middle">3</text><text class="soft" x="408" y="24" text-anchor="middle">4</text><text class="soft" x="494" y="24" text-anchor="middle">5</text><text class="soft" x="580" y="24" text-anchor="middle">6</text><text class="soft" x="666" y="24" text-anchor="middle">7</text>
  <text x="100" y="58" text-anchor="end">name exists</text><rect class="bx" x="108" y="40" width="602" height="26" rx="4"/>
  <text x="100" y="92" text-anchor="end">full_name exists</text><rect class="bx-g" x="108" y="74" width="640" height="26" rx="4"/>
  <text x="100" y="126" text-anchor="end">code writes</text><rect class="bx" x="108" y="108" width="430" height="11" rx="3"/><rect class="bx-g" x="194" y="121" width="554" height="11" rx="3"/>
  <text x="100" y="160" text-anchor="end">code reads</text><rect class="bx" x="108" y="142" width="344" height="26" rx="4"/><rect class="bx-g" x="452" y="142" width="296" height="26" rx="4"/>
  <text x="100" y="194" text-anchor="end">old rows filled</text><rect class="bx-y" x="280" y="176" width="86" height="26" rx="4"/><rect class="bx-g" x="366" y="176" width="382" height="26" rx="4"/>
  <path class="ln-r" d="M538 30 V212"/><text class="soft bad" x="538" y="232" text-anchor="middle">going back now needs a repair</text>
  <path class="ln-r" d="M710 30 V212"/><text class="soft bad" x="704" y="252" text-anchor="end">no way back</text>
'''
plan = '''
<p>Here is the rename as it is really done: seven steps over about two weeks. Each step is a small deploy or a script, and each leaves the system working for old and new code.</p>
''' + tbl(["#", "Step", "Kind", "Before you go on"], [
    ["1", "<b>Expand</b>: add <code>full_name</code>, empty and optional", "schema", "the column exists; nothing uses it"],
    ["2", "<b>Dual-write</b>: code writes <code>name</code> and <code>full_name</code>", "code deploy", "every instance runs it; new rows have both"],
    ["3", "<b>Backfill</b>: copy <code>name</code> into <code>full_name</code> for old rows", "script, hours", "it has finished"],
    ["4", "<b>Verify</b>: count rows where the two differ", "query", "the count is zero and stays zero"],
    ["5", "<b>Switch reads</b> to <code>full_name</code>, behind a flag, 1 % then all", "flag", "100 % for several days, no surprises"],
    ["6", "<b>Stop writing</b> <code>name</code>; code no longer mentions it", "code deploy", "a full release cycle passes; nobody else reads it"],
    ["7", "<b>Contract</b>: drop <code>name</code>", "schema", "done"],
]) + fig(760, 262, "A chart of the seven steps. The column name exists from the start until step 7. The column full_name exists from step 1 onward. Code writes name until step 6 and writes full_name from step 2 onward. Code reads name until step 5 and full_name after it. Old rows are filled during step 3 and complete from step 4. A dashed line before step 6 marks where going back needs a repair, and a dashed line at step 7 marks where there is no way back.",
          plan_svg, "White is old, green is new. Between steps 2 and 6 both are alive, which is what makes each step safe.") + mn("The note had five steps. Verify and the flag are the two it folded in, and they are where problems are caught.") + '''
<h3>How to go back, at each step</h3>
''' + tbl(["After step", "Going back means", "Cost"], [
    ["1", "nothing. An unused column harms no one", "none"],
    ["2", "redeploy the previous code. <code>full_name</code> goes stale, so the backfill must run again later", "low"],
    ["3, 4", "stop the script", "none"],
    ["5", "turn the flag off. Reads use <code>name</code> again, which is still being written", "seconds"],
    ["6", "redeploy dual-write code, <b>and</b> copy <code>full_name</code> back into <code>name</code> for every row written since", "a data repair"],
    ["7", "restore the column from a backup", "effectively impossible"],
], hot=(4, 5)) + full('''<p>The plan has the same shape as a saga. Steps 1 to 5 are easy to undo. Step 6 is the pivot: after it, the old column starts to rot, and going back needs a repair. Step 7 cannot be undone. So the time between steps is not idle. The days after step 5 are the soak period, in which rolling back is still a flag flip. Do not shorten them to finish the ticket.</p>
<h3>Why dual-write comes before the backfill</h3>
<p>It is tempting to backfill first, since it is the slow part. But a backfill copies rows as they are at that moment. If any code is still writing only <code>name</code>, rows it touches after the backfill passed them have a stale or empty <code>full_name</code>, and nothing will ever fix them (drill 3). With dual-write running everywhere first, every row written from then on is already right, and the backfill only has to catch up the past.</p>''')

# ------------------------------------------------------------------ 4 drills
drills = mn("Each of these has turned a five-minute change into an incident. Guess before reading.") + '''
<ul class="drill-index" aria-label="The six drills">
  <li><a href="#drill-1">1 · the lock queue</a></li><li><a href="#drill-2">2 · the big update</a></li><li><a href="#drill-3">3 · the gap</a></li>
  <li><a href="#drill-4">4 · early contract</a></li><li><a href="#drill-5">5 · the quiet canary</a></li><li><a href="#drill-6">6 · the old flag</a></li>
</ul>
''' + drill(1, "The instant change that froze the site", [
    ("Timeline", "Step 1 is <code>ALTER TABLE users ADD COLUMN full_name text</code>. It takes a millisecond. But a report query has been reading <code>users</code> for four minutes. The <code>ALTER</code> needs the table to itself for that millisecond, so it waits. Every query that arrives after it now waits behind the <code>ALTER</code>."),
    ("What you see", "All requests that touch <code>users</code> hang. Connection pools fill. The site is down until the report finishes, and the “instant” migration is blamed, correctly.", True),
    ("Why", "A schema change needs an exclusive lock, even briefly. Locks are granted in order of arrival. A waiting exclusive request blocks everyone behind it, including plain reads that would otherwise have run alongside the report.", True),
    ("What saves you", "Tell the migration to give up quickly: <code>SET lock_timeout = '2s'</code>, and retry a few times. If it cannot get the lock in two seconds it fails and nothing queues behind it. Check for long-running transactions before starting."),
], "a fast schema change can still wait for a slow query, and everything waits behind it. Always set a lock timeout.") + drill(2, "One UPDATE for 200 million rows", [
    ("Timeline", "Step 3 is run as <code>UPDATE users SET full_name = name</code>. One statement, one transaction, 200 million rows."),
    ("What you see", "The statement runs for hours and holds a lock on every row it has touched, so sign-ups and profile edits start to time out. The replicas fall an hour behind, and pages that read from them show old data. If it is cancelled at 90 %, everything is rolled back and nothing was gained.", True),
    ("What saves you", "Copy in small batches, a few thousand rows at a time, each in its own short transaction, with a pause between them. Walk the table by primary key. Watch replica lag and slow down when it grows. Record the last id done so the script can be stopped and resumed (chapter 5)."),
], "backfill in small, resumable batches that the live traffic does not notice.") + drill(3, "The rows that fell through the gap", [
    ("Timeline", "The backfill is run first, to save time. It finishes on Tuesday. The dual-write code is deployed on Wednesday. On Tuesday night, 40,000 users signed up or edited their names."),
    ("What you see", "Nothing, for days. Then reads are switched to <code>full_name</code>, and 40,000 users have a blank name or an old one. The ones who changed their name after getting married are the ones who write in.", True),
    ("What saves you", "Order: dual-write on every instance first, then backfill. And step 4 exists for this: before any read is switched, count the rows where <code>full_name</code> differs from <code>name</code>. The count must be zero, and must still be zero the next day. A count that keeps growing means some writer is still not dual-writing: an old instance, a nightly job, an admin script, another service."),
], "dual-write before backfill, and verify with a count before trusting the new column.") + drill(4, "Someone was still using the old column", [
    ("Timeline", "The team's own code no longer mentions <code>name</code>, so the column is dropped. That night the finance team's export fails. So does a worker running last month's build. So do the old app instances in the middle of a deploy, even though they never show the name: their database library lists every column it knows in each query."),
    ("Why", "“Our code doesn't use it” was checked by searching one repository. The column had readers that the search could not see.", True),
    ("What saves you", "Before step 7, look at the database, not the code: its statistics show whether the column is still read. Tell the library to ignore the column one release <i>before</i> dropping it. Ask the other teams. Some teams first rename the column to <code>name_unused</code> for a week: anything that still needs it fails loudly, and the fix is a rename back, not a restore."),
], "contract only when the database itself shows that nothing reads the old thing.") + drill(5, "The canary that had nothing to say", [
    ("Timeline", "Reads are switched to <code>full_name</code> for 1 % of traffic. Error rate and response time on that 1 % are perfect for an hour, so it goes to 100 %. A week later support notices that accounts created before 2019 show no name."),
    ("What you see", "No error anywhere. A blank name is a valid string. The canary measured crashes and slowness, and this bug was neither.", True),
    ("What saves you", "Measure the thing that can go wrong. Before switching any read, read <b>both</b> columns in production and count the cases where they differ, without showing the new one to anybody. This is a shadow read. Zero mismatches over a few days of real traffic tells you more than any error graph. Then widen by groups that matter, such as old accounts and each country, not only by percentage."),
], "a canary only sees what it measures. For data changes, compare old and new values, not just error rates.") + drill(6, "The flag nobody removed", [
    ("Timeline", "The <code>read-full-name</code> flag has been at 100 % for five months. The code still has both branches. The column <code>name</code> was dropped in the spring. During an unrelated incident someone looks through the flag dashboard for things to turn off “to be safe”, and turns this one off."),
    ("What you see", "Every page that shows a name fails at once. The off branch reads a column that no longer exists. The incident now has a second cause, created by the response to the first.", True),
    ("What saves you", "A release flag has an owner and an end date. Removing the flag and its dead branch is a step of the plan, done after step 5 has soaked and <b>before</b> step 6. A flag whose off position no longer works is a trap, and the flag list should not contain any."),
], "delete the flag before you delete what its other branch depends on.") + full('''<h3>What the six drills add up to</h3>
''' + tbl(["Habit", "Drill"], [
    ["every schema change has a lock timeout and a retry", "1"],
    ["data is moved in small, resumable batches, watching the replicas", "2"],
    ["dual-write first, backfill second, then count the differences", "3"],
    ["the old thing is dropped only when the database shows no readers", "4"],
    ["old and new values are compared in production before any user sees the new one", "5"],
    ["flags are removed on schedule, before the contract step", "6"],
]))

# ------------------------------------------------------------------ 5 backfill and verify
backfill = '''
<p>Steps 3 and 4 are where a migration spends most of its calendar time and where the data is actually at risk. They deserve more care than the two <code>ALTER</code> statements people worry about.</p>
<h3>A backfill that production does not notice</h3>
''' + code("backfill.ts", "small batches, by id, resumable", '''
let lastId = await checkpoint.load("users.full_name") ?? 0;
const maxId = await db.value("SELECT max(id) FROM users");

while (lastId < maxId) {
  await db.query(
    `UPDATE users SET full_name = name
     WHERE id > $1 AND id <= $2 AND full_name IS NULL`,   // IS NULL: safe to run twice
    [lastId, lastId + 5_000]);

  lastId += 5_000;
  await checkpoint.save("users.full_name", lastId);       // stop any time, resume here
  while (await replicaLagSeconds() > 5) await sleep(1_000); // let the replicas catch up
  await sleep(100);
}
''') + tbl(["Choice", "Why"], [
    ["Batches of a few thousand rows", "each transaction is short, so locks are held for milliseconds"],
    ["Walk by primary key range", "each batch finds its rows directly. “The next 5,000 where <code>full_name</code> is empty” rescans from the start every time and gets slower as it goes"],
    ["<code>AND full_name IS NULL</code>", "the script can be rerun without undoing newer values written by dual-write"],
    ["A saved checkpoint", "a deploy, a crash or a nervous operator can stop it without losing progress"],
    ["Slow down on replica lag", "the backfill yields to live traffic, never the reverse"],
]) + mn("The note's version used LIMIT 1000 in a loop. Fine for a million rows. At 200 million, walk by id.") + '''
<h3>How long will it take?</h3>
''' + tbl(["Quantity", "Value"], [
    ["Rows", "200,000,000"],
    ["Batch", "5,000 rows, about 150 ms, plus a 100 ms pause"],
    ["Rate", "4 batches a second, 20,000 rows a second"],
    ["Total", "10,000 seconds: under 3 hours, if nothing slows it"],
    ["Plan for", "a working day, with replica pauses and peak hours"],
]) + full('''<p>Work this out before starting. If the answer is three weeks, the batch size, the hours it may run, or the approach needs to change, and it is better to learn that from arithmetic.</p>
<h3>Verify: the step people skip</h3>
''' + code("verify.sql", "run on a replica, in id ranges", '''
SELECT count(*)
FROM users
WHERE id > 0 AND id <= 1000000
  AND full_name IS DISTINCT FROM name;   -- also catches NULL on one side
''') + '''<p>The total must be zero. Then run it again a day later. A stable zero means every writer is dual-writing. A number that grows means one is not (drill 3), and the list of ids tells you which rows it touches, which usually tells you who.</p>
<h3>Shadow reads</h3>
<p>The count checks the data at rest. A shadow read checks it under real traffic, on the real code path.</p>
''' + code("get-user.ts", "read both, compare, show the old one", '''
const row = await db.one("SELECT name, full_name FROM users WHERE id = $1", [id]);

if (row.full_name !== row.name) {
  metrics.count("users.full_name.mismatch");        // nobody sees this; we just count
  log.warn("full_name mismatch", { id });
}
return flags.on("read-full-name", user) ? row.full_name : row.name;
''') + '''<p>For a week this costs nothing and proves the new column on every read. When the mismatch counter has been at zero for days, turning the flag on is a formality.</p>
<h3>When the data does not convert cleanly</h3>
<p>A rename is the easy case: copy the value. Most real changes transform it: dollars to cents, one name field into first and last, free text into a list of codes. Then some rows will not convert: empty names, a single word, a company where a person was expected. Decide the rule for those rows <i>before</i> the backfill, write them to a list, and have someone look at the list. A backfill that guesses silently has moved the problem to step 5, where customers find it.</p>
''')

# ------------------------------------------------------------------ 6 online schema changes
schema = '''
<p>Drill 1 showed that even an instant change can hurt. Not all changes are instant. Before any migration, know which kind it is. The table is for PostgreSQL; other databases differ in the details and the same questions apply.</p>
''' + tbl(["Change", "On a large, busy table", "Do this"], [
    ["Add an optional column", "instant", "as it is, with a lock timeout"],
    ["Add a column with a fixed default", "instant on current versions", "as it is"],
    ["Add an index", "blocks writes while it builds", "<code>CREATE INDEX CONCURRENTLY</code>"],
    ["Add <code>NOT NULL</code>", "scans the whole table under a lock", "add a <code>CHECK … NOT VALID</code>, then <code>VALIDATE</code> it separately"],
    ["Add a foreign key", "scans and locks both tables", "add it <code>NOT VALID</code>, then <code>VALIDATE</code>"],
    ["Change a column's type", "usually rewrites the table", "new column, expand and contract"],
    ["Rename a column or table", "instant, and breaks all running code", "expand and contract"],
    ["Drop a column", "instant", "only as a contract step (drill 4)"],
], hot=(5, 6)) + mn("“Instant” means the change itself. It still has to get the lock.") + code("0042_expand.sql", "a migration that cannot cause a pile-up", '''
SET lock_timeout = '2s';        -- give up, do not queue
SET statement_timeout = '10s';  -- and never run long by surprise

ALTER TABLE users ADD COLUMN full_name text;
''') + full('''<p>The two “not valid, then validate” rows are the same trick. The first statement is quick and makes the rule apply to new rows from now on. The second checks the old rows, and it does so while reads and writes carry on. One slow blocking step has become one instant step and one slow harmless step.</p>
<h3>Migrations are their own deploy</h3>
<p>Many frameworks run pending migrations when the app starts. With 20 instances starting together, 20 processes try to run the same migration, and the new code is live before anyone has looked at the result. Run migrations as a separate, single job in the pipeline, before the code that needs them, and after checking that the code currently running is happy with the new schema. It is by definition: expand steps are backward compatible.</p>
''' + tbl(["Pipeline step", "Contains"], [
    ["1 · migrate", "expand-only schema changes; one runner; lock timeout; stops the pipeline if it fails"],
    ["2 · deploy", "code that works with the schema both before and after step 1"],
    ["3 · later, separately", "backfills, as jobs you can watch, pause and resume"],
    ["4 · much later", "contract migrations, on their own, on a quiet day"],
]) + '''<h3>Let a linter say no</h3>
<p>Nobody remembers the table above under deadline. A migration linter in the build does: it fails a pull request that adds an index without <code>CONCURRENTLY</code>, sets <code>NOT NULL</code> in one step or renames a column. It is cheap to add, and it turns this chapter from knowledge into a rule.</p>''')

# ------------------------------------------------------------------ 7 rolling out the code
rollout = '''
<p>The schema steps are covered. The code steps, 2, 5 and 6, each have to reach production, and there are three tools for that. They are often confused because all three “release gradually”. They control different things.</p>
''' + tbl(["Tool", "Controls", "Unit", "Undo"], [
    ["<b>Rolling or blue–green deploy</b>", "which build is running", "instances, or the whole environment", "redeploy or switch back: minutes"],
    ["<b>Canary</b>", "how much traffic the new build gets", "a share of requests", "shift traffic back: seconds to minutes"],
    ["<b>Feature flag</b>", "which behaviour is on, inside a build", "a user, a group, a percentage", "flip it: seconds, no deploy"],
]) + mn("Deploy: the code is on the servers. Release: users get the behaviour. The flag is what separates the two.") + '''
<h3>Which tool for which step</h3>
''' + tbl(["Step", "Risk", "Use"], [
    ["2 · dual-write", "a bug in the write path affects every write", "canary deploy: watch error rate and write latency on a small share first"],
    ["5 · switch reads", "wrong data shown, with no errors", "a flag, widened by group, after shadow reads show zero mismatches"],
    ["6 · stop writing the old column", "going back needs a repair", "ordinary deploy, after the soak; nothing to widen"],
]) + full('''<p>Step 5 uses a flag, not a deploy, for three reasons. Turning it off takes seconds and no pipeline. It can be widened by meaningful groups, such as staff, then accounts created before 2019, then one country. And it is independent of whatever else is being deployed that week.</p>
<h3>Blue–green and the shared database</h3>
<p>Blue–green gives each version its own servers and one shared database. The note called that “the catch”. With the plan from chapter 3 it stops being one, as long as two rules hold.</p>
<ul>
  <li><b>Before the switch, green's migrations are expand-only.</b> Blue is still serving, and must not notice them.</li>
  <li><b>Contract only after blue is gone for good.</b> While blue is kept warm as the way back, its schema needs are still live. Dropping a column blue reads turns the instant rollback into a crash.</li>
</ul>
<p>The same holds for anything else the two share: a queue, a cache, uploaded files. A message written by green and consumed by blue after a switch back is the mixed-version window again, in a different pipe.</p>
<h3>What a canary should compare</h3>
''' + tbl(["Signal", "Catches", "Misses"], [
    ["error rate, canary against stable", "crashes, failed queries", "wrong answers that are valid"],
    ["response time, typical and slow case", "a missing index, extra queries", "problems on rare paths"],
    ["database load per request", "an accidental full scan", ""],
    ["business numbers: sign-ups, checkouts completed", "broken flows that return 200", "slow-moving effects"],
    ["data comparison: mismatches between old and new", "wrong data (drill 5)", "needs to be built for each change"],
], hot=(4,)) + '''<p>Run the canary long enough to include the traffic that matters. Ten minutes at three in the afternoon says nothing about the nightly export or Monday's invoice run.</p>
''')

# ------------------------------------------------------------------ 8 beyond the database
beyond = '''
<p>Nothing in the plan was really about columns. It works for anything where producers and consumers of a shape are updated at different times. The steps keep their names. What changes is who still has the old shape, and for how long.</p>
''' + tbl(["What changes", "Who still has the old shape", "Expand", "Contract when"], [
    ["a database column", "running code, other teams' queries", "add the new column", "the database shows no reads"],
    ["an API field", "every client, including ones you do not own", "add the new field; keep sending the old", "request logs show no client using the old one"],
    ["a message or event", "consumers, and old messages in the log", "publish the new version beside the old", "consumers have moved and old messages can no longer be replayed"],
    ["a cache entry's format", "entries written by the old code", "put a version in the key", "old keys have expired"],
    ["a background job's arguments", "jobs already queued", "the worker accepts both shapes", "the queue holds no old jobs"],
    ["a configuration value", "instances not yet restarted", "code reads new, falls back to old", "all instances restarted"],
], hot=(1,)) + mn("The Reliable Messaging and Caching dives each had this rule for their own pipe. It is one rule.") + '''
<h3>Reader first, writer second</h3>
<p>For any new shape, the order is the same: <mark>teach every reader to accept it before any writer produces it.</mark></p>
''' + tbl(["Example", "Wrong order", "Right order"], [
    ["a new order status, <code>PAUSED</code>", "deploy code that sets it; old instances and old apps crash on the unknown value", "first a release that understands <code>PAUSED</code> everywhere; then one that sets it"],
    ["a new field in an event", "consumers that validate strictly reject the message", "consumers ignore unknown fields first"],
    ["a new job argument", "old workers fail jobs queued by new code", "workers accept it first; producers send it next release"],
]) + full('''<p>This is what makes rollback safe as well. If the writer is rolled back, readers that understand the new shape lose nothing. If readers were rolled back while new-shaped data already exists, the old readers meet data they cannot read. So a release that starts <i>writing</i> a new shape can only be rolled back to a version that can still <i>read</i> it, and that version must have gone out first.</p>
<h3>Mobile apps stretch the window to months</h3>
<p>A web client is replaced on the next page load. A mobile app is replaced when its owner feels like it. A version released today will still be sending requests in a year.</p>
''' + tbl(["Consequence", "Practice"], [
    ["the API's contract step may be a year away", "plan it as a date, not as “after the release”"],
    ["you need to know which versions are still alive", "every request carries the app version; a dashboard shows the share of each"],
    ["some day the old shape really must go", "a minimum supported version, and a polite “please update” screen that old versions already know how to show"],
]) + '''<p>The “please update” screen has to exist in the app <i>before</i> it is needed. It is the reader-first rule again, applied to the one message every old version must be able to understand.</p>
''')

# ------------------------------------------------------------------ 9 testing and running
testing = '''
<p>A migration is production-only code that runs once. That makes it the least tested code a team writes, on the most valuable thing the team has. Four kinds of check close most of the gap.</p>
''' + tbl(["Check", "How", "Catches"], [
    ["<b>Old code, new schema</b>", "in the build, apply the pending expand migrations, then run the test suite of the version currently in production", "a migration that is not backward compatible (chapter 2)"],
    ["<b>Real size</b>", "run the migration and the backfill on a copy with production row counts; time them; watch locks", "drills 1 and 2: the ten-second step that takes four hours"],
    ["<b>Rollback rehearsal</b>", "deploy the new version to a test environment, write data, deploy the previous version, use the site", "old code that cannot read new data (chapter 8)"],
    ["<b>Twice</b>", "run every migration and backfill a second time", "scripts that fail or corrupt when rerun after a partial failure"],
]) + mn("“Old code, new schema” is one extra job in the pipeline. It would have caught the naive rename in chapter 2 before a human looked at it.") + '''
<h3>What to watch while it runs</h3>
''' + tbl(["Graph", "During", "Stop if"], [
    ["lock waits and blocked queries", "any schema step", "anything waits more than a few seconds"],
    ["replica lag", "backfill", "it climbs past your limit and the script is not slowing itself"],
    ["write latency and error rate, by app version", "dual-write deploy", "the new version is worse than the old"],
    ["mismatch count from verify and shadow reads", "from step 2 to step 6", "it is not zero, or it is growing"],
    ["reads of the old column, from database statistics", "before contract", "it is not zero"],
]) + full('''<h3>Write the plan down</h3>
<p>A change that takes two weeks and seven steps outlives one person's attention. Keep one short document per migration.</p>
''' + code("migration-plan.md", "one page, kept in the repository", '''
Rename users.name -> users.full_name          owner: Ana      started: 3 Nov

 #  step                 how      done    check before the next step
 1  add full_name        deploy   3 Nov   column exists
 2  dual-write           deploy   4 Nov   all instances on v212; canary clean
 3  backfill             job      5 Nov   checkpoint = max id
 4  verify               query    6 Nov   0 mismatches, again on 7 Nov
 5  read full_name       flag     7 Nov   100 % since 10 Nov; shadow mismatches 0
 -  remove the flag      deploy   14 Nov  flag deleted from code and dashboard
 6  stop writing name    deploy   17 Nov  one release cycle; no reads of name
 7  drop name            deploy   1 Dec   -

Go back: steps 1-5 see runbook; step 6 needs reverse backfill; step 7 cannot.
''', plain=True) + '''<p>It shows anyone where the change is, what has to be true to continue, and that step 7 exists. Half-finished migrations, with two columns kept for ever because nobody remembers whether the old one is safe to drop, are the usual way this pattern fails. The document is the cure.</p>
<h3>Runbook: a step went wrong</h3>
<ol>
  <li><b>Which step are you on?</b> The plan says. Steps 1 to 5 go back cheaply; do that first and investigate afterwards.</li>
  <li><b>Schema step hanging?</b> Cancel it. With a lock timeout it will have cancelled itself.</li>
  <li><b>Backfill hurting?</b> Stop it. The checkpoint keeps your place.</li>
  <li><b>Wrong data after the read switch?</b> Flag off. The old column is still correct, because you are still writing it.</li>
  <li><b>After step 6?</b> Do not improvise. Redeploy dual-write, run the reverse backfill from the plan, then decide.</li>
</ol>''')

# ------------------------------------------------------------------ 10 when not, lab, checklist
tools = '''
<h3>When this is too much</h3>
<p>Seven steps over two weeks is a real cost, and not every change is worth it.</p>
''' + tbl(["Situation", "Do instead"], [
    ["a small table, a change that takes a second", "one migration with a lock timeout, at a quiet moment. Still expand-only if code is running"],
    ["an internal tool used in office hours", "announce ten minutes of downtime in the evening and do it in one step"],
    ["a product not launched yet", "change the schema freely. There is no old data and no old client"],
    ["a column nobody reads, added last week", "drop it. Check the statistics first"],
], hot=(1,)) + mn("Planned downtime is a legitimate tool. Ten announced minutes at night can be cheaper than two weeks of care.") + '''
<p>The full plan is for tables that are large or busy, systems that must stay up, and shapes that other people depend on. Use the question from chapter 2 to choose: who still has the old shape, and for how long? If the answer is “nobody, for no time”, you do not need seven steps.</p>
<h3>Lab</h3>
<p>The <code>orders</code> table stores <code>total</code> as a decimal number of dollars: 49.00. Rounding bugs keep appearing, so the team wants <code>total_cents</code> as a whole number: 4900. The table has 500 million rows. The finance team's nightly export reads <code>total</code>. The mobile app receives <code>total</code> in the order API.</p>
<ol class="keep">
  <li>List the steps. Which is the one where going back gets expensive?</li>
  <li>The backfill does 20,000 rows a second. How long does it take, and what do you check afterwards?</li>
  <li>What does the shadow read compare?</li>
  <li>When can <code>total</code> be dropped from the table? When from the API?</li>
  <li>A row has <code>total = 49.005</code>. What now?</li>
</ol>
<div class="check quiz"><h3>model answer</h3>
<details><summary>1 · The steps</summary><p>Add <code>total_cents</code>. Dual-write both. Backfill. Verify. Switch reads behind a flag, with shadow reads first. Remove the flag. Stop writing <code>total</code>. Drop it. Going back gets expensive at “stop writing <code>total</code>”, because from then on the old column is out of date.</p></details>
<details><summary>2 · The backfill</summary><p>500,000,000 ÷ 20,000 = 25,000 seconds, about seven hours of pure run time; plan for a day or two with pauses. Afterwards, count rows where <code>total_cents</code> is not equal to <code>round(total × 100)</code>. It must be zero now and zero tomorrow.</p></details>
<details><summary>3 · The shadow read</summary><p>On every order read in production, compare <code>total_cents</code> with <code>total × 100</code> and count mismatches, while still showing <code>total</code>. Also compare sums: the day's revenue computed from each column should be identical.</p></details>
<details><summary>4 · Dropping it</summary><p>From the table: when the finance export has moved to <code>total_cents</code> and the database's statistics show no reads of <code>total</code>. Ask finance early; their export is the hidden reader of drill 4. From the API: much later. The API sends both fields until the share of app versions that read <code>total</code> is close to zero, which may take a year.</p></details>
<details><summary>5 · The half cent</summary><p>It does not convert cleanly. Do not let the backfill round it silently. Decide the rule with finance first, list every such row, and have a person look at the list. Those rows are probably the rounding bugs that started the project.</p></details>
</div>
<h3>The review checklist</h3>
''' + checklist([
    ("The plan", ["The change is split into expand, migrate and contract steps, written down with an owner", "Each step works with the running version, the next one and the one you would roll back to", "The way back is stated for every step, and the step where it gets expensive is marked", "There is a soak period before that step", "The contract step has a date"]),
    ("Schema changes", ["Every migration sets a lock timeout and retries", "Each change is known to be instant, or uses the online form", "Migrations run as one job before the code deploy, not at app start", "A linter blocks unsafe migrations in the build"]),
    ("Data", ["Dual-write is on every instance before the backfill starts", "The backfill runs in small batches by key, is resumable and safe to rerun", "It slows down when replicas lag, and its duration was estimated", "Rows that do not convert are listed and reviewed, not guessed", "A mismatch count is zero, twice, before reads switch"]),
    ("Rolling out", ["Readers accept a new shape before any writer produces it", "Risky write-path code goes out as a canary", "Read switches use a flag, after shadow reads show zero mismatches", "The canary compares data and business numbers, not only errors", "The flag is removed before the contract step"]),
    ("Contract", ["The database's own statistics show no reads of the old thing", "Other teams, jobs, scripts and old app versions were checked", "The database library ignores the column one release before it is dropped", "Contract runs alone, early in the week, with the owner watching"]),
    ("Tests", ["The production version's tests pass against the new schema", "The migration was timed on production-size data", "A rollback was rehearsed with new data present", "Every script was run twice"]),
])

# ------------------------------------------------------------------ the dive
DIVE = dict(
    slug="zero-downtime-change", no=6, title="Zero-Downtime Change",
    sub="One column rename, followed from the first ALTER TABLE to the last DROP COLUMN: seven steps, two weeks, and a way back at each one.",
    summary="A deep dive on changing a live system without downtime: the mixed-version window, a seven-step expand and contract plan, six failure drills, backfills and verification, online schema changes, canaries and flags, APIs and mobile clients, testing and operations.",
    builds_on="Vol. 3, note 10 and Vol. 6, notes 01–03",
    builds_on_links=[("Expand & Contract", "../../data/notes/expand-contract.html"), ("Blue–Green", "../../cloud/notes/blue-green.html"),
                     ("Canary", "../../cloud/notes/canary.html"), ("Feature Flags", "../../cloud/notes/feature-flags.html")],
    notes=[("data", "expand-contract"), ("cloud", "blue-green"), ("cloud", "canary"), ("cloud", "feature-flags")],
    facts=[("Example", "renaming <code>users.name</code> to <code>full_name</code>, 200 million rows")],
    blurb="One schema change through every deploy step: the mixed-version window, a seven-step plan, six failure drills, backfills, canaries and flags.",
    chapters=[
        dict(id="recap", nav="Recap", title="Four notes in sixty seconds",
             gist="Expand and contract changes the shape of data in small compatible steps. Blue–green, canary and feature flags control which version runs, for how many users, with which behaviour. A real change uses all four in a fixed order. This deep dive follows one column rename through every step.",
             body=recap),
        dict(id="window", nav="Mixed versions", title="A deploy is never instant",
             gist="During every deploy, old and new code run together against one database. Old code also lives on in queued jobs, caches, mobile apps and any rollback. So the database must always work for the running version, the next one, and the one you might go back to. That rule forces a change to be split into steps.",
             body=window,
             check=[("Why is there no safe order for “rename the column” and “deploy code that uses the new name”?", "Whichever goes first, one version of the code meets a schema it does not understand for the length of the deploy window, and again on a rollback."),
                    ("Name two places old code or data survives after all instances are replaced.", "Any of: jobs and messages already queued, cached responses, mobile apps not yet updated, other teams' scripts, and the previous version if you roll back.")]),
        dict(id="plan", nav="The plan", title="The change, step by step",
             gist="Seven steps: add the new column, write both, backfill old rows, verify, switch reads behind a flag, stop writing the old column, drop it. Going back is cheap through step 5, needs a data repair after step 6 and is impossible after step 7. Wait between steps on purpose.",
             body=plan,
             check=[("After step 5, a bug appears in how names are displayed. What do you do, and why is it safe?", "Turn the flag off. Reads go back to <code>name</code>, which is still correct because the code is still writing both columns."),
                    ("Why is step 6 the one to wait before?", "Once the old column is no longer written, it goes stale. Rolling back after that needs every newer row copied back.")]),
        dict(id="drills", nav="Failure drills", title="Failure drills",
             gist="Six ways a small change becomes an incident: an instant schema change that queues behind a slow query, one enormous update, rows written between the backfill and dual-write, a column dropped while something still read it, a canary that could not see wrong data, and a forgotten flag with a dead branch.",
             body=drills,
             check=[("An <code>ALTER TABLE</code> that takes a millisecond has blocked the site for three minutes. What was missing?", "A lock timeout. The statement was waiting for a long-running query, and every later query queued behind it."),
                    ("The mismatch count after the backfill is 12 and rises by a few each hour. What does that tell you?", "Some writer is still writing only the old column: an old instance, a job, a script or another service.")]),
        dict(id="backfill", nav="Backfill", title="Backfill and verify: the hard part",
             gist="Copy old rows in small batches by primary key, safe to rerun, resumable, and slowing down when replicas lag. Estimate the duration first. Then verify twice with a count of differences, and compare old and new values on real reads before any user sees the new column.",
             body=backfill,
             check=[("Why include <code>AND full_name IS NULL</code> in the backfill's update?", "So a rerun does not overwrite values that dual-write has already set, possibly with newer data."),
                    ("What does a shadow read tell you that the verify count does not?", "It checks the real read path under real traffic, continuously, including rows changed after the count was run.")]),
        dict(id="schema", nav="Schema changes", title="Schema changes that do not block",
             gist="Know for each change whether it is instant, blocks writes or rewrites the table. Adding an optional column is instant; indexes are built concurrently; NOT NULL and foreign keys are added unvalidated and validated separately; type changes and renames go through expand and contract. Always set a lock timeout, and run migrations as their own step.",
             body=schema,
             check=[("Why not run migrations when the application starts?", "Many instances start together and race to run the same migration, and the new code is live before anyone has checked the result."),
                    ("What does “add the constraint NOT VALID, then VALIDATE” buy you?", "The rule applies to new rows at once with an instant change; the slow check of old rows then runs without blocking reads and writes.")]),
        dict(id="rollout", nav="Rolling out", title="Rolling out the code: deploys, canaries, flags",
             gist="A deploy decides which build runs, a canary how much traffic it gets, and a flag which behaviour is on. Use a canary for risky write-path code and a flag for switching reads. With blue–green, migrate expand-only before the switch and contract only after the old environment is gone.",
             body=rollout,
             check=[("Why switch reads with a flag and not with a canary deploy?", "A flag turns off in seconds with no pipeline, can be widened by meaningful groups, and is independent of other deploys."),
                    ("Blue is kept warm for a week as the rollback. Can you drop the old column on day two?", "No. Blue still reads it. Dropping it makes the rollback crash.")]),
        dict(id="beyond", nav="Beyond SQL", title="Beyond the database",
             gist="The same steps apply to API fields, messages, cache formats, job arguments and configuration. Ask who still has the old shape and for how long. Teach every reader a new shape before any writer produces it. Mobile apps stretch the window to months, so the contract step needs a date and a minimum supported version.",
             body=beyond,
             check=[("You want to add a new order status. What ships first?", "A release in which every reader, including the apps, understands the new status. Only a later release starts setting it."),
                    ("When can an old API field be removed?", "When request logs show that no client version still reads it, or a minimum supported version has been enforced.")]),
        dict(id="testing", nav="Testing", title="Testing it and running it",
             gist="Run the production version's tests against the new schema. Time the migration on production-size data. Rehearse a rollback with new data present. Keep a one-page plan with the check before each step, watch locks, replica lag and mismatches while it runs, and ship contract steps alone, early in the week.",
             body=testing,
             check=[("What does running the production version's tests against the new schema prove?", "That the expand migration is backward compatible: the code running now will keep working once the schema changes."),
                    ("A migration has had two columns for eight months. What went wrong?", "Nobody owned the contract step. Without a written plan and a date, the last steps are forgotten.")]),
        dict(id="tools", nav="When & lab", title="When it is too much, a lab and the checklist",
             gist="For a small table, an internal tool or a product not yet launched, one step or a short announced downtime is cheaper and fine. Use the full plan when the table is large, the system must stay up or others depend on the shape. The lab converts an order total from dollars to cents.",
             body=tools),
    ],
    sources="Danilo Sato, “Parallel Change” (2014), on martinfowler.com. Pramod Sadalage and Martin Fowler, “Evolutionary Database Design” (2016). Scott Ambler and Pramod Sadalage, <i>Refactoring Databases</i> (2006). Jez Humble and David Farley, <i>Continuous Delivery</i> (2010), chapters 10 and 12. Pete Hodgson, “Feature Toggles” (2017), on martinfowler.com. The PostgreSQL documentation on <code>ALTER TABLE</code> and explicit locking.",
)
