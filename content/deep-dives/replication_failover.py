# Deep dive 08 · Replication, Failover & Leader Election. Builds on Vol. 1 notes 16 (leader-follower replication)
# and 18 (leader election). Example: the mug shop's orders database, a leader in zone A and followers in zones B and C,
# 1,500 writes and 8,000 reads a second; and the nightly invoice job from the leader election note, three instances
# competing for the lease /election/billing (15-second lease, renewed every 5 seconds).
# Helpers (mn, full, tbl, drill, code, fig, checklist) are injected by scripts/build_notes.py from scripts/dive.py.

# ------------------------------------------------------------------ 1 recap
setup_svg = '''
  <rect class="bx" x="10" y="74" width="100" height="56" rx="8"/><text class="lbl" x="60" y="107" text-anchor="middle">shop app</text>
  <rect class="bx-y" x="170" y="40" width="150" height="62" rx="8"/><text class="lbl" x="245" y="66" text-anchor="middle">leader</text><text class="soft" x="245" y="88" text-anchor="middle">zone A</text>
  <rect class="bx" x="420" y="16" width="140" height="54" rx="8"/><text class="lbl" x="490" y="40" text-anchor="middle">follower</text><text class="soft" x="490" y="60" text-anchor="middle">zone B</text>
  <rect class="bx" x="420" y="104" width="140" height="54" rx="8"/><text class="lbl" x="490" y="128" text-anchor="middle">follower</text><text class="soft" x="490" y="148" text-anchor="middle">zone C</text>
  <path class="ln" d="M110 96 L168 78" marker-end="url(#a)"/><text class="soft" x="138" y="66" text-anchor="middle">writes</text>
  <path class="ln" d="M320 62 L418 44" marker-end="url(#a)"/><path class="ln" d="M320 84 L418 126" marker-end="url(#a)"/>
  <text class="soft" x="372" y="84" text-anchor="middle">change log</text>
  <path class="ln-d" d="M110 116 Q260 190 418 140" marker-end="url(#a)"/><text class="soft" x="250" y="186" text-anchor="middle">most reads</text>
  <rect class="bx-g" x="610" y="16" width="140" height="58" rx="8"/><text class="lbl" x="680" y="42" text-anchor="middle">etcd</text><text class="soft" x="680" y="62" text-anchor="middle">3 nodes, consensus</text>
  <rect class="bx-y" x="606" y="140" width="44" height="34" rx="6"/><text class="lbl" x="628" y="163" text-anchor="middle">a</text>
  <rect class="bx" x="658" y="140" width="44" height="34" rx="6"/><text class="lbl" x="680" y="163" text-anchor="middle">b</text>
  <rect class="bx" x="710" y="140" width="44" height="34" rx="6"/><text class="lbl" x="732" y="163" text-anchor="middle">c</text>
  <path class="ln" d="M628 138 L660 78" marker-end="url(#a)"/><text class="soft" x="702" y="118" text-anchor="middle">holds the lease</text>
  <text class="soft" x="680" y="198" text-anchor="middle">invoice job</text>
'''
recap = '''
<p>The two notes describe one arrangement from two sides. The shop's orders database has a leader in zone A that takes every write, and two followers in zones B and C that copy its change log and serve most reads. Separately, a nightly invoice job runs on three instances, and a lease in etcd decides which one does the work.</p>
''' + tbl(["Note", "In one line"], [
    ["Leader–Follower Replication", "one node takes the writes and ships its log; followers replay it, serve reads and can take over"],
    ["Leader Election", "instances compete for a lease in a consensus store; the holder leads, renews, and is fenced if it goes stale"],
]) + fig(760, 210, "The setup for this deep dive. The shop app sends writes to the leader database in zone A. The leader ships its change log to followers in zones B and C, which serve most reads. On the right, etcd runs on three nodes with consensus. Three instances of the invoice job, a, b and c, compete for a lease in etcd; instance a holds it.",
          setup_svg, "Two kinds of leader: the database's, and the invoice job's. The same questions apply to both.") + mn("A database failover is a leader election. Most tools that run one use etcd or something like it underneath.") + '''
<p class="full">The notes explain the normal day. This deep dive is about the two moments that hurt: a follower that is behind when someone reads from it, and a leader that stops answering. The second is the hard one, because from outside a leader that is dead and a leader that is slow look the same, and acting on the wrong guess either loses writes or creates two leaders.</p>
'''

# ------------------------------------------------------------------ 2 log and lag
lag = '''
<p>Every write the leader commits goes into its log (the write-ahead log in PostgreSQL, the binlog in MySQL). Followers receive that log and replay it in order. How long the leader waits for them before telling the app “committed” is the most important replication setting there is.</p>
''' + tbl(["Mode", "The leader waits for", "Commit time, followers in other zones", "If the leader dies"], [
    ["<b>Asynchronous</b>", "nobody", "local disk only: about 1 ms", "writes not yet shipped are lost"],
    ["<b>Synchronous, one follower</b>", "one named follower to confirm", "+ one round trip: about 2–3 ms", "nothing confirmed is lost; if that follower stops, writes stop"],
    ["<b>Quorum</b>", "any one of the two followers", "+ the faster round trip", "nothing confirmed is lost; one follower may be down"],
    ["<b>Synchronous, another region</b>", "a follower 70 ms away", "+ 70 ms on every commit", "survives losing a region; every checkout is slower"],
], hot=(2,)) + mn("Quorum is the usual answer inside one region: no lost writes, and one slow follower does not stall checkout.") + '''
<h3>Where lag comes from</h3>
<p>Even with a synchronous follower, “confirmed” usually means the log reached the follower's disk, not that the follower has replayed it. Reads from followers can be behind in every mode.</p>
''' + tbl(["Cause", "What it looks like"], [
    ["network between zones", "a steady few milliseconds"],
    ["a follower busier than the leader", "lag that grows during peak and shrinks at night"],
    ["one large transaction: a backfill, a mass update", "a sudden jump of seconds or minutes, then recovery"],
    ["a long report on the follower", "replay pauses so the report keeps its snapshot, or the report is cancelled; either way someone is surprised"],
    ["a follower restarting", "minutes behind, catching up from the log"],
]) + full('''<p>Measure lag two ways. In <b>bytes</b>: how much log the follower has not replayed. In <b>time</b>: how old the newest change on the follower is. Bytes tell you how far behind it is; time tells you what a user sees. A follower can be 2 MB behind and 50 ms old at peak, or 2 KB behind and four minutes old at three in the morning, when nothing has been written since.</p>
<p>And treat lag as a distribution, not a number. “Lag is 20 ms” is the median. The question for chapter 3 is how often it is three seconds, because that is when the customer who just paid sees an unpaid order.</p>''')

# ------------------------------------------------------------------ 3 reading from followers
reading = '''
<p>Reading from followers is why many teams add them, and it changes what the app may assume. Three anomalies appear, all with mugs.</p>
''' + tbl(["Anomaly", "What the customer sees"], [
    ["<b>Read your own write</b> fails", "customer 7 changes the delivery address and the confirmation page, read from a follower, shows the old one"],
    ["<b>Monotonic reads</b> fail", "refresh shows order 42 as PAID; refresh again, a different follower, it is PENDING. Time went backwards"],
    ["<b>Consistent prefix</b> fails", "with several databases or shards: a reply to a support message appears before the message"],
]) + '''
<h3>Four fixes, from crude to precise</h3>
''' + tbl(["Fix", "How", "Cost"], [
    ["<b>Read from the leader</b> for anything just changed", "for a few seconds after a write, that customer's reads go to the leader", "leader load; the few seconds are a guess"],
    ["<b>Sticky follower</b>", "a session always reads from the same follower", "fixes monotonic reads only; uneven load"],
    ["<b>Wait for the position</b>", "the write returns the log position; the next read waits until the follower has replayed it", "a short wait, rarely; needs a little code"],
    ["<b>Leader for decisions</b>", "anything a decision is made on is read from the leader, in the transaction", "none; this is just correct"],
], hot=(2,)) + mn("Same rule as the Caching dive: show from a copy, decide on the original.") + code("read-after-write.ts", "wait for the follower to catch up with my last write", '''
// after a write, remember where the log was
const { lsn } = await leader.one("SELECT pg_current_wal_lsn() AS lsn");
session.set("lastWrite", lsn);

// on a later read, use a follower only once it has replayed that far
async function readDb(session) {
  const want = session.get("lastWrite");
  if (!want) return followers.any();
  for (const f of followers.inRandomOrder()) {
    const ok = await f.value("SELECT pg_last_wal_replay_lsn() >= $1", [want]);
    if (ok) return f;
  }
  return leader;                       // nobody has caught up: ask the leader
}
''') + full('''<p>Checking the position costs a query, so real implementations cache each follower's replayed position for a few milliseconds, or put the check in the database proxy. The principle is what matters: the read carries “not older than this”, and any copy that meets it may answer.</p>
<h3>What may read from a follower</h3>
''' + tbl(["Read", "From"], [
    ["product pages, search, order history older than a minute", "any follower"],
    ["the page right after the customer changed something", "a follower that has reached their write, or the leader"],
    ["reports and exports", "a follower set aside for them, so long queries do not delay the others"],
    ["stock, balance or status checked before acting", "the leader, inside the transaction"],
])) + '''
<p>A follower that is too far behind should take itself out of rotation. A health check that answers “unhealthy” when lag exceeds, say, five seconds means the app stops reading badly old data automatically, and the dashboard shows why.</p>
'''

# ------------------------------------------------------------------ 4 drills
drills = mn("Each of these has caused a real outage somewhere. Try to predict the ending first.") + '''
<ul class="drill-index" aria-label="The six drills">
  <li><a href="#drill-1">1 · lost writes</a></li><li><a href="#drill-2">2 · split brain</a></li><li><a href="#drill-3">3 · it wakes up</a></li>
  <li><a href="#drill-4">4 · the flapping failover</a></li><li><a href="#drill-5">5 · the old address</a></li><li><a href="#drill-6">6 · two invoices</a></li>
</ul>
''' + drill(1, "The failover that lost the last second", [
    ("Timeline", "Replication is asynchronous. At 14:02:10 the leader's host dies. Follower B is 400 ms behind and is promoted. The 600 writes in those 400 ms existed only on the dead leader."),
    ("What you see", "Orders whose customers saw “confirmed” do not exist. Payments were taken for them. Days later the old leader's disk is recovered and holds the missing rows, which now conflict with new rows using the same ids.", True),
    ("What saves you", "Decide the loss you accept, in writing. If the answer is “none”, use quorum commit (chapter 2), so a confirmed write is always on two machines. If some loss is acceptable, measure lag at the moment of failover, keep the old leader's disk, and have a plan to compare and recover what it held."),
], "asynchronous replication means a failover can lose confirmed writes. Choose that on purpose, or use quorum commit.") + drill(2, "Two leaders at once", [
    ("Timeline", "The network between zone A and the other zones fails. The failover tool in zone B cannot reach the leader, decides it is dead and promotes follower B. The leader in zone A is fine, and the app servers in zone A keep writing to it."),
    ("What you see", "Two databases accept writes for ten minutes. Order numbers are handed out twice. When the network returns, there is no automatic way to merge two histories of the same table.", True),
    ("What saves you", "Only promote with a majority. The failover decision lives in a consensus store with three or more members across zones, and a node cut off from the majority must stop accepting writes by itself. The old leader in zone A, unable to renew its lease, steps down. Chapter 5 explains why two members can never do this safely."),
], "a node that cannot reach the majority must stop. Promotion needs a quorum, never one observer.") + drill(3, "The old leader wakes up", [
    ("Timeline", "The invoice job's leader, instance a, stops for 23 seconds in a garbage-collection pause. Its 15-second lease expires and instance b becomes leader. Instance a wakes, still believing it leads, and finishes writing the batch it had started."),
    ("What you see", "Two instances writing invoices for the same customers. Nothing crashed and the lease worked exactly as designed. The process simply could not know that time had passed.", True),
    ("What saves you", "A fencing token. Each lease grant comes with a number that only grows: a had 33, b got 34. Every write carries the number, and the storage refuses any number lower than the highest it has seen. Instance a's late writes, with 33, are rejected."),
], "a leader can be paused at any moment without knowing. Let the storage reject stale leaders, not the leader itself.") + drill(4, "The failover that kept failing over", [
    ("Timeline", "The health check says “leader dead” after three missed checks one second apart. During a busy minute a checkpoint makes the leader slow for four seconds. It is declared dead and B is promoted. Clients reconnect, B is now the busy one, it slows down, and C is promoted."),
    ("What you see", "Three failovers in ten minutes, each with lost connections and a short write outage. The database was never actually down.", True),
    ("What saves you", "Detection slow enough to ignore a hiccup: tens of seconds, not three. A cool-down after a failover before another may happen. And an alert to a person when one occurs, so a second one in an hour is a decision, not a reflex."),
], "a failover is a disruption in itself. Detect patiently, and never let failovers chain.") + drill(5, "The app is still talking to the old leader", [
    ("Timeline", "Follower B is promoted at 14:02:15 and the database's DNS name now points to it. App servers resolved that name when they started and keep their connection pools open. Some keep writing to the old leader, which is now read-only, and get errors; others hang on dead connections."),
    ("What you see", "Failover took 15 seconds; the outage took 12 minutes, until someone restarted the app servers.", True),
    ("What saves you", "Make the switch something clients cannot miss. Short DNS lifetimes and pools that reconnect on error; a proxy in front of the database that follows the leader; or drivers that accept a list of hosts and look for the one that accepts writes. Test it as part of every failover drill (chapter 9)."),
], "a failover ends when the clients have moved, not when the database has.") + drill(6, "Two invoices, because the lock was a cache", [
    ("Timeline", "The invoice job was moved from etcd to a lock in a single Redis server, “because we already run Redis”. Redis restarts during the run and comes back empty. Instance b sees no lock, takes it, and starts the same run."),
    ("What you see", "Customers billed twice for November. The lock worked in every test, because no test restarted Redis halfway.", True),
    ("What saves you", "Use a store built for agreement (etcd, ZooKeeper, Consul, or a Kubernetes Lease, which sits on etcd) when a duplicate would cost money. A cache-based lock is fine for “don't waste effort”, not for “must never happen twice”. And make the job idempotent anyway: one invoice per customer per month, enforced by a unique key."),
], "a lock is only as reliable as the store it lives in. For correctness, use consensus and idempotency together.") + full('''<h3>What the six drills add up to</h3>
''' + tbl(["Decision", "Drill"], [
    ["the write loss you accept is chosen; quorum commit if it is zero", "1"],
    ["promotion needs a majority; a cut-off leader steps down", "2"],
    ["every write from a leader carries a fencing token the storage checks", "3"],
    ["detection is patient; failovers have a cool-down and wake a person", "4"],
    ["clients follow the new leader by design, and it is tested", "5"],
    ["coordination uses a consensus store, and the work is idempotent", "6"],
]))

# ------------------------------------------------------------------ 5 is it dead
fence_svg = '''
  <text x="140" y="44" text-anchor="end">instance a</text>
  <rect class="bx-g" x="150" y="26" width="60" height="26" rx="4"/>
  <rect class="bx-r" x="210" y="26" width="392" height="26" rx="4"/><text class="soft" x="406" y="45" text-anchor="middle">paused for 23 s, unaware</text>
  <rect class="bx" x="602" y="26" width="138" height="26" rx="4"/><text class="soft" x="671" y="45" text-anchor="middle">writes with 33</text>
  <text x="140" y="84" text-anchor="end">lease</text>
  <rect class="bx-y" x="150" y="66" width="354" height="26" rx="4"/><text class="soft" x="327" y="85" text-anchor="middle">held by a, token 33: last renewed at 3 s</text>
  <rect class="bx-g" x="504" y="66" width="236" height="26" rx="4"/><text class="soft" x="622" y="85" text-anchor="middle">held by b, token 34</text>
  <text x="140" y="124" text-anchor="end">instance b</text>
  <rect class="bx-g" x="510" y="106" width="230" height="26" rx="4"/><text class="soft" x="625" y="125" text-anchor="middle">leads, writes with 34</text>
  <text x="140" y="164" text-anchor="end">storage</text>
  <text class="soft good" x="516" y="164">accepts 34</text><text class="soft bad" x="606" y="164">refuses 33</text>
  <path class="ln" d="M150 186 H740"/>
  <text class="soft" x="150" y="206" text-anchor="middle">0 s</text><text class="soft" x="504" y="206" text-anchor="middle">18 s</text><text class="soft" x="602" y="206" text-anchor="middle">26 s</text>
'''
dead = '''
<p>Every failover starts with a guess: the leader is dead. The guess is always made the same way, by a message that did not get an answer in time. And a missing answer has many causes.</p>
''' + tbl(["Why no answer arrived", "Is the leader dead?"], [
    ["the machine crashed", "yes"],
    ["the process is in a long pause: garbage collection, a full disk, a frozen virtual machine", "no, and it will resume as if nothing happened"],
    ["the network between you and it is broken", "no, and others may still reach it"],
    ["it is overloaded and slow", "no, and failing over may move the overload (drill 4)"],
    ["your own clock or process paused", "it may be fine; you are the one who was away"],
], hot=(1, 2)) + mn("From outside, dead and slow are the same. Every safe design accepts that it cannot tell them apart.") + '''
<p>Since nobody can know for sure, the design has to stay safe when the guess is wrong. Three ideas do that, and they stack.</p>
<h3>1 · Decide by majority</h3>
<p>A decision is valid only if more than half of a fixed group agrees. With three members, two must agree; with five, three. Two different majorities of the same group always share at least one member, so two conflicting decisions can never both win. A member cut off from the others cannot form a majority and therefore cannot promote anyone, or keep leading.</p>
''' + tbl(["Members", "Majority", "Survives losing"], [
    ["2", "2", "nobody. Two is worse than one: either failure stops everything"],
    ["3", "2", "1 member"],
    ["5", "3", "2 members"],
], hot=(0,)) + full('''<p>That is why consensus stores are run with three or five members, in different zones, and why a two-zone database setup cannot fail over safely on its own: it needs a third member somewhere, even a small one that only votes.</p>
<h3>2 · Lead only on a lease</h3>
<p>The leader holds a lease that expires unless renewed: 15 seconds, renewed every 5. If the leader cannot renew, because it is cut off or paused, it must stop acting as leader before the lease runs out. Others wait for the full lease before taking over. On a normal day, the old leader has stopped before the new one starts.</p>
<p>But a lease is a promise about time, and a process cannot keep a promise during a pause it does not notice. Instance a in drill 3 checked its lease, saw 12 seconds left, and was frozen for 23 before its next instruction ran.</p>''') + '''
<h3>3 · Let the storage check: fencing tokens</h3>
''' + fig(760, 216, "Timeline of drill 3 with fencing. Instance a works with token 33, then pauses for 23 seconds without knowing. Its lease, last renewed at 3 seconds, expires at 18 seconds and is granted to instance b with token 34. Instance b writes with 34, which the storage accepts. At 26 seconds instance a wakes and writes with 33; the storage refuses it because it has already seen 34.",
          fence_svg, "The lease cannot stop a paused leader. The number on its writes can.") + code("write-invoice.sql", "the storage refuses a stale leader", '''
UPDATE invoice_runs
SET status = 'WRITING', fencing_token = $1, updated_at = now()
WHERE month = '2026-11'
  AND fencing_token <= $1;        -- 0 rows: a newer leader exists, stop at once
''') + full('''<p>The check has to happen where the damage would happen: in the database row, the storage bucket, the downstream service. A leader that checks its own lease before writing is still exposed to a pause between the check and the write. A storage that compares numbers is not.</p>
<p>Databases do the same internally. A promoted follower starts a new term or timeline, and the old leader, if it comes back, is told it belongs to an older one and must rejoin as a follower. That is a fencing token under another name.</p>''')

# ------------------------------------------------------------------ 6 failover step by step
failover = '''
<p>A failover is a short sequence of steps, and each one is a place where it can go wrong. Here is the shop's, from the moment the leader stops answering.</p>
''' + tbl(["#", "Step", "Done by", "Time"], [
    ["1", "<b>Detect</b>: the leader has not renewed its lease in the consensus store", "the failover tool on every node", "up to 15 s"],
    ["2", "<b>Choose</b>: the follower with the most of the log", "the tool, by majority", "1 s"],
    ["3", "<b>Fence</b>: make sure the old leader cannot accept writes, even if it is alive", "the old leader itself, on losing its lease; or by cutting its network", "already done"],
    ["4", "<b>Promote</b>: the chosen follower starts accepting writes", "the database", "2–5 s"],
    ["5", "<b>Repoint</b>: the other follower follows the new leader; clients move", "the tool, proxies, drivers", "5–30 s"],
    ["6", "<b>Rebuild</b>: the old leader rejoins as a follower, after discarding anything the new leader never had", "a person or the tool, later", "minutes to hours"],
], hot=(2,)) + mn("Step 3 is the one people skip. Without it, step 4 is how drill 2 starts.") + full('''<h3>Automatic or manual?</h3>
''' + tbl(["", "Automatic", "Manual"], [
    ["Write outage", "seconds to a minute", "until someone wakes up: often 20–40 minutes"],
    ["Risk of a wrong failover", "real (drill 4), managed by patient detection", "low"],
    ["Fits", "a team with a tested setup and good monitoring", "a team still learning the setup; very small systems"],
]) + '''<p>Most teams end up automatic, after having been manual long enough to trust it. Whichever you choose, the person on call must be able to see that a failover happened, why, and what the data loss was.</p>
<h3>Switchover is the friendly twin</h3>
<p>A planned switch, for patching or moving a server, uses the same steps with one difference: the old leader is healthy and can stop taking writes and wait until a follower has every last change. Nothing is lost and the write pause is a few seconds. Do this regularly, every month or with every patch round, and the unplanned failover will be a path the team has walked many times.</p>
<h3>After the failover</h3>
<p>The old leader may hold writes that never reached the new one (drill 1). Before it rejoins, those writes are rolled back on it, in PostgreSQL with <code>pg_rewind</code> or by copying it fresh. Keep a record of what was rolled back. Someone in finance may need that list.</p>''')

# ------------------------------------------------------------------ 7 numbers
numbers = '''
<p>Two numbers describe what a failure costs, and the business should choose them before the engineers do.</p>
''' + tbl(["Term", "Means", "Shop's target"], [
    ["<b>RPO</b>, recovery point", "how much recent data you may lose", "zero confirmed orders"],
    ["<b>RTO</b>, recovery time", "how long writes may be unavailable", "one minute"],
]) + '''
<h3>Working them out for the shop</h3>
''' + tbl(["Question", "Reasoning", "Answer"], [
    ["Can asynchronous replication meet RPO zero?", "no: lag at failure is lost. At 200 ms and 1,500 writes a second, about 300 writes", "use quorum commit"],
    ["What does quorum commit cost?", "the faster of two cross-zone round trips on each commit", "about +2 ms per write"],
    ["How long to detect?", "the lease: 15 s, renewed every 5 s, so three missed renewals", "15 s"],
    ["How long to promote?", "replay what was received but not applied, then switch mode", "about 5 s"],
    ["How long for clients to move?", "proxy health checks every 2 s; pools reconnect on error", "about 10 s"],
    ["Total write outage", "15 + 5 + 10", "about 30 s: inside the minute"],
]) + mn("If the sum had been 90 s, the fix is a faster detection or a proxy, and a conversation about whether 90 s is acceptable.") + full('''<h3>The lease numbers</h3>
''' + tbl(["Setting", "Rule", "Shop"], [
    ["lease length", "longer than the longest normal hiccup (a checkpoint, a short network blip)", "15 s"],
    ["renew every", "a third of the lease, so two renewals can fail before it lapses", "5 s"],
    ["stop leading", "as soon as one renewal fails, not when the lease runs out", "at the first failure"],
    ["cool-down after a failover", "long enough for a person to look", "5 min"],
]) + '''<h3>Lag budget for reads</h3>
<p>The follower health check from chapter 3 needs a number too. Ask what the oldest acceptable answer is for the reads that go to followers. For order history, five seconds is fine. A follower beyond that leaves rotation, and if both are beyond it, reads go to the leader, which must be sized to take them for a while: 8,000 reads a second on top of 1,500 writes. Check that it can, or decide which reads may fail instead.</p>
<h3>Across regions</h3>
<p>A second region is 70 ms away. Synchronous commit there adds 70 ms to every write: a checkout that makes ten writes is 0.7 s slower. Most teams replicate asynchronously across regions and accept that a whole-region loss may lose seconds of data, with a much longer RTO, because a region failover also moves the app servers, caches and everything else. That is a disaster-recovery plan, not a failover, and it is practised as one.</p>''')

# ------------------------------------------------------------------ 8 leader election for jobs
jobs = '''
<p>The database usually has its leader election built in. Application jobs do not: the nightly invoice run, a scheduler, the one consumer that must process a partition alone. Here the team writes the election, and everything in chapter 5 applies.</p>
''' + code("invoice-leader.ts", "campaign, lead while the lease holds, carry the token", '''
const election = new Election(etcd, "/election/billing", { leaseSeconds: 15 });

for (;;) {
  const term = await election.campaign(instanceId);     // blocks until we win
  const token = term.revision;                          // only grows: our fencing token
  try {
    for (const batch of await pendingCustomers("2026-11")) {
      if (!term.isValid()) break;                       // lost the lease: stop now
      await writeInvoices(batch, token);                // storage checks the token
    }
  } finally {
    await term.resign();                                // hand over cleanly
  }
}
''') + tbl(["Habit", "Why"], [
    ["campaign with a lease, never “whoever starts first”", "a crashed leader must be replaced without a person"],
    ["check the lease between batches", "a leader that lost the lease stops within one batch"],
    ["pass the token to every write", "a paused leader cannot finish its batch (drill 3)"],
    ["resign on shutdown", "a deploy hands over in milliseconds instead of waiting 15 s"],
    ["make the work idempotent", "one invoice per customer per month, as a unique key, so a mistake costs nothing"],
]) + mn("Leader election makes duplicates rare. Idempotency makes them harmless. You want both.") + full('''<h3>Do you need a leader at all?</h3>
<p>Often not. Three cheaper designs cover many “only one may do it” jobs.</p>
''' + tbl(["Instead of a leader", "How", "Fits"], [
    ["a row lock in the database", "each instance runs <code>SELECT … FOR UPDATE SKIP LOCKED</code> on the next unit of work", "work that splits into many small items"],
    ["a scheduler that starts exactly one copy", "a Kubernetes CronJob with <code>concurrencyPolicy: Forbid</code>, or a managed scheduler", "a nightly job with no need for standby instances"],
    ["idempotent work run everywhere", "every instance tries; the unique key lets one succeed", "cheap work where duplicates are only wasted effort"],
]) + '''<p>Use real leader election when one instance must hold a role continuously, such as a scheduler or a partition owner, and the role must move quickly when that instance dies.</p>
<h3>Where to keep the lease</h3>
''' + tbl(["Store", "Fine for"], [
    ["etcd, ZooKeeper, Consul", "anything; this is what they are for"],
    ["a Kubernetes Lease object", "workloads already on Kubernetes; it is stored in etcd"],
    ["a row in the main database, with a lease time and a fencing column", "small systems; the database is the one place everyone can already reach"],
    ["a single Redis", "avoiding wasted effort only. Not for correctness (drill 6)"],
]))

# ------------------------------------------------------------------ 9 testing and running
testing = '''
<p>Failover code runs on the worst day of the year, so it has to be run on ordinary days too. The useful tests are not unit tests. They are small, deliberate breakages of a test environment that looks like production.</p>
''' + tbl(["Break", "How", "Expect"], [
    ["kill the leader", "stop the database process or the machine", "promotion in under 30 s; no confirmed write lost; clients reconnect by themselves"],
    ["cut the leader off", "block its network to the other zones, but not to some app servers", "it stops accepting writes; exactly one new leader (drill 2)"],
    ["pause the leader", "send SIGSTOP for 30 s, then SIGCONT", "the woken process steps down; its writes are refused (drill 3)"],
    ["slow the leader", "add 3 s of disk latency for 10 s", "no failover (drill 4)"],
    ["lag a follower", "run a large update", "the follower leaves read rotation; reads stay correct"],
    ["restart the lock store", "restart one etcd member, then the Redis if you have one", "no second job leader (drill 6)"],
], hot=(1, 2)) + mn("The pause test finds the most bugs. Almost nobody tests it, because nothing crashes.") + full('''<h3>Count the writes</h3>
<p>“No confirmed write lost” needs a way to check. During the test, a small client writes numbered rows and records each one the database confirmed. After the failover, every confirmed number must be present on the new leader. It is a ten-line script and the only honest measure of your RPO.</p>
''' + code("count-writes.ts", "the RPO, measured", '''
const confirmed: number[] = [];
for (let i = 1; testRunning(); i++) {
  try { await db.query("INSERT INTO rpo_probe (n) VALUES ($1)", [i]); confirmed.push(i); }
  catch { /* during the failover, some writes fail: that is fine */ }
}
const present = new Set(await db.column("SELECT n FROM rpo_probe"));
const lost = confirmed.filter((n) => !present.has(n));
console.log(`confirmed ${confirmed.length}, lost ${lost.length}`);   // must be 0
''')) + '''
<h3>What to watch</h3>
''' + tbl(["Metric", "Alert when"], [
    ["replication lag per follower, in bytes and in seconds", "seconds exceed the read budget; bytes keep growing"],
    ["a follower not connected", "at once: you are one failure from no copy"],
    ["leader changes, for the database and every job election", "any unplanned change; two in an hour"],
    ["time without a leader", "longer than the RTO"],
    ["fencing rejections", "any: a stale leader tried to write, and the design worked"],
]) + full('''<h3>Runbook: after an unplanned failover</h3>
<ol>
  <li><b>Confirm one leader.</b> Ask every node which role it has. Two answers of “leader” is an emergency: stop writes at the proxy.</li>
  <li><b>Check that clients moved.</b> Error rates by app server; any still failing are holding old connections (drill 5).</li>
  <li><b>Find the loss.</b> Compare the old leader's last log position with what the new leader received. Zero with quorum commit; if not zero, list the transactions.</li>
  <li><b>Rebuild the old leader</b> as a follower, after rolling back what the new leader never had, and keep that list.</li>
  <li><b>Find why.</b> A failover with no hardware fault is drill 4 until shown otherwise.</li>
</ol>''')

# ------------------------------------------------------------------ 10 tools, lab, checklist
tools = '''
<h3>Tools</h3>
''' + tbl(["Need", "Examples", "Note"], [
    ["Managed database with failover", "Amazon RDS Multi-AZ and Aurora, Google Cloud SQL HA, Azure Database flexible server", "the cloud runs steps 1–5; you still own clients (drill 5), lag-aware reads and the drills"],
    ["Self-run PostgreSQL failover", "Patroni (on etcd, Consul or Kubernetes), pg_auto_failover", "Patroni is the common choice; it uses a consensus store for exactly chapter 5"],
    ["Self-run MySQL failover", "Orchestrator, MySQL Group Replication / InnoDB Cluster", "group replication uses its own consensus"],
    ["Following the leader", "PgBouncer or HAProxy with health checks, ProxySQL, multi-host connection strings", "the piece most often forgotten"],
    ["Consensus for your own jobs", "etcd, ZooKeeper, Consul, Kubernetes Lease", "use a client library's election API; do not write the protocol"],
]) + mn("Managed failover is excellent at the database part. The app part is still yours.") + '''
<h3>Lab</h3>
<p>The shop opens in a second country. Customers there are 70 ms from the current region. The team adds a follower in a new region near them, and wants the invoice job to keep running if the first region is lost.</p>
<ol class="keep">
  <li>Should the new follower be synchronous? What does each choice cost?</li>
  <li>Which reads may go to the new follower, and what stops a customer there from seeing their own order disappear after paying?</li>
  <li>The consensus store runs on three nodes in the first region. What happens to failover if that region is lost, and what do you change?</li>
  <li>The invoice job's instances now run in both regions. What prevents two invoice runs during a network split between the regions?</li>
  <li>Region one is lost entirely. Is this a failover or a disaster recovery, and what is the RPO?</li>
</ol>
<div class="check quiz"><h3>model answer</h3>
<details><summary>1 · Synchronous?</summary><p>No. Synchronous commit to a follower 70 ms away adds 70 ms to every write, for every customer in both countries. Keep it asynchronous and accept a few hundred milliseconds of possible loss if the first region is lost entirely; inside the first region, quorum commit still protects confirmed writes.</p></details>
<details><summary>2 · Reads there</summary><p>Product pages, search and older order history. After a customer writes, the next reads wait for the follower to reach their write position, or go to the leader for a few seconds (chapter 3). The payment and stock checks always use the leader, inside the transaction.</p></details>
<details><summary>3 · The consensus store</summary><p>With all three members in region one, losing that region loses the majority, so nothing can be promoted anywhere. Spread five members: two in each region and one in a third place, so either region plus the tie-breaker forms a majority.</p></details>
<details><summary>4 · Two invoice runs</summary><p>The lease lives in the consensus store, so during a split only the side with the majority can hold it. The other side's leader fails to renew and stops. Fencing tokens refuse any late write, and the unique key per customer and month makes a duplicate harmless anyway.</p></details>
<details><summary>5 · Losing region one</summary><p>A disaster recovery: the database, app servers and caches all move. The RPO is the cross-region lag at that moment, typically under a second, so some confirmed orders may be lost and must be reconciled with the payment provider. Practise it once a year, on a quiet day.</p></details>
</div>
<h3>The review checklist</h3>
''' + checklist([
    ("Replication", ["The data loss you accept (RPO) is written down and matches the replication mode", "Quorum commit if confirmed writes may never be lost", "Lag is measured in bytes and in seconds, per follower", "Large updates are batched so they do not lag every follower"]),
    ("Reads", ["Each kind of read is assigned to the leader or to followers", "Reads after a customer's own write wait for their position, or use the leader", "Decisions read from the leader inside the transaction", "A follower beyond the lag budget leaves read rotation", "The leader can carry the reads if every follower leaves"]),
    ("Failover", ["Promotion requires a majority of three or more members, across zones", "A leader that cannot renew its lease stops accepting writes", "Detection is patient; failovers have a cool-down and alert a person", "Clients follow the new leader through a proxy or multi-host connections", "The old leader is rewound or rebuilt, and what it lost is recorded"]),
    ("Leaders for jobs", ["Leases come from a consensus store, not a cache", "The leader checks its lease between batches and resigns on shutdown", "Every write carries a fencing token and the storage checks it", "The work is idempotent anyway"]),
    ("Tests", ["Kill, isolate, pause and slow the leader, in a production-like environment", "A probe counts confirmed writes across each failover", "Planned switchovers are done regularly"]),
    ("Operations", ["Lag, leader changes, time without a leader and fencing rejections are graphed", "There is a runbook for after a failover", "A two-leader situation can be stopped at the proxy in one step"]),
])

# ------------------------------------------------------------------ the dive
DIVE = dict(
    slug="replication-failover", no=8, title="Replication, Failover & Leader Election",
    sub="Copies that lag, leaders that pause, and the one question no system can answer: is it dead, or just slow?",
    summary="A deep dive on replication, failover and leader election: synchronous, asynchronous and quorum commit, reading from followers, six failure drills, majorities, leases and fencing tokens, failover step by step, RPO and RTO, leaders for application jobs, testing and operations.",
    builds_on="Vol. 1, notes 16 and 18",
    builds_on_links=[("Leader–Follower Replication", "../../distributed/notes/replication.html"), ("Leader Election", "../../distributed/notes/leader-election.html")],
    notes=[("distributed", "replication"), ("distributed", "leader-election")],
    facts=[("Example", "the orders database in three zones, and the nightly invoice job")],
    blurb="Replication modes and lag, reading from followers, six failure drills, majorities, leases and fencing, failover step by step.",
    chapters=[
        dict(id="recap", nav="Recap", title="Two notes in sixty seconds",
             gist="Replication copies the leader's log to followers that serve reads and can take over. Leader election lets several instances agree which one does a job, through a lease in a consensus store. A database failover is a leader election, so the same questions apply to both, and the hard one is deciding that a leader is dead.",
             body=recap),
        dict(id="lag", nav="Log & lag", title="The log, and how far behind it is",
             gist="How long the leader waits before confirming a write decides what a failover can lose: asynchronous loses the unshipped tail, quorum commit loses nothing for the cost of one round trip. Followers can lag in every mode. Measure lag in bytes and in time, and look at its worst moments, not its median.",
             body=lag,
             check=[("Why is quorum commit usually better than a single synchronous follower?", "With quorum, either follower may confirm, so one slow or stopped follower does not stop writes. With one named follower, it does."),
                    ("A follower is 2 KB behind but its newest change is four minutes old. Is that a problem?", "Probably not: at a quiet hour nothing has been written. Lag in time is high only because there was nothing to copy.")]),
        dict(id="reading", nav="Reading", title="Reading from followers",
             gist="Reads from followers can miss the customer's own write, go backwards between refreshes, or show effects before causes. Send reads after a write to a follower that has reached it, or to the leader; read anything a decision depends on from the leader; and let a follower that is too far behind leave rotation.",
             body=reading,
             check=[("A customer refreshes and an order goes from PAID back to PENDING. Which anomaly, and the simplest fix?", "Monotonic reads failed: two refreshes hit followers at different points. A sticky follower per session, or reading at least the position the customer last saw."),
                    ("Why read stock from the leader, inside the transaction, before reserving it?", "A follower's stock may be out of date, and a decision made on old data reserves stock that is not there.")]),
        dict(id="drills", nav="Failure drills", title="Failure drills",
             gist="Six ways replication and failover go wrong: an asynchronous failover that loses confirmed writes, two leaders after a network split, a paused leader that wakes up and writes, failovers that trigger each other, clients still talking to the old leader, and a lock kept in a cache.",
             body=drills,
             check=[("The leader is cut off from the other zones but not from some app servers. What must it do, and why?", "Stop accepting writes once it cannot renew its lease. Otherwise those app servers keep writing to it while another leader is promoted: two leaders."),
                    ("A failover took 15 seconds but the outage lasted 12 minutes. Where do you look?", "The clients: connection pools and cached DNS still pointing at the old leader.")]),
        dict(id="dead", nav="Dead or slow?", title="Dead or slow? The hard problem",
             gist="A leader that is crashed, paused, cut off or overloaded looks the same from outside, so a safe design must survive a wrong guess. Decide by majority, so two leaders cannot both be chosen; lead only while a lease holds; and let the storage refuse writes that carry an older fencing token.",
             body=dead,
             check=[("Why does a two-member setup not help with failover?", "A majority of two is two. If either member fails, the other cannot form a majority, so nothing can be decided."),
                    ("The leader checks its lease right before every write. Why is a fencing token still needed?", "The process can pause between the check and the write. Only a check at the storage, at the moment of the write, is safe.")]),
        dict(id="failover", nav="Failover", title="Failover, step by step",
             gist="Detect, choose the most up-to-date follower, fence the old leader, promote, repoint clients, rebuild the old leader. Fencing is the step people skip, and the one that prevents two leaders. Practise with planned switchovers every month so the unplanned failover follows a familiar path.",
             body=failover,
             check=[("What is the difference between a switchover and a failover?", "In a switchover the old leader is healthy: it stops taking writes and waits until a follower has everything, so nothing is lost."),
                    ("Before the old leader rejoins, why must some of its writes be rolled back?", "It may hold writes the new leader never received. The new leader's history is now the truth, so those writes are removed and recorded.")]),
        dict(id="numbers", nav="Numbers", title="RPO, RTO and the lease, worked out",
             gist="The business chooses how much data may be lost and for how long writes may stop. Zero loss rules out asynchronous replication. The outage is detection plus promotion plus clients moving, about 30 seconds for the shop. Leases are longer than a normal hiccup and renewed three times per lease.",
             body=numbers,
             check=[("Asynchronous replication, 300 ms of lag, 1,500 writes a second. How many writes could a failover lose?", "About 450."),
                    ("Why renew a 15-second lease every 5 seconds rather than every 14?", "So two renewals can fail, for example during a short network blip, before the lease lapses.")]),
        dict(id="jobs", nav="Job leaders", title="Leaders for your own jobs",
             gist="Application jobs need their own election: campaign for a lease in a consensus store, check it between batches, pass the fencing token to every write, resign on shutdown, and make the work idempotent anyway. Often a row lock or a single scheduled run is enough and no leader is needed.",
             body=jobs,
             check=[("Why resign the lease on shutdown instead of letting it expire?", "A deploy then hands over at once instead of leaving the job without a leader for up to 15 seconds."),
                    ("When is a single Redis lock acceptable?", "When a duplicate only wastes effort. Not when it bills a customer twice.")]),
        dict(id="testing", nav="Testing", title="Testing it and running it",
             gist="Break a production-like environment on purpose: kill, isolate, pause and slow the leader, lag a follower, restart the lock store. Count confirmed writes across each failover to measure the real RPO. Graph lag, leader changes, time without a leader and fencing rejections.",
             body=testing,
             check=[("Which test is most often skipped, and what does it find?", "Pausing the leader. It finds code that assumes a leader knows when it has lost its role."),
                    ("A fencing rejection appears on the dashboard. Good news or bad?", "Both: a stale leader tried to write, which means something paused or split, and the design stopped it.")]),
        dict(id="tools", nav="Tools & lab", title="Tools, a lab and the checklist",
             gist="Managed databases and tools such as Patroni run the failover; you still own how clients find the new leader, which reads may lag, and the drills. Use a consensus store's election API for your own jobs. The lab adds a second region, and the checklist turns the deep dive into review questions.",
             body=tools),
    ],
    sources="Martin Kleppmann, <i>Designing Data-Intensive Applications</i> (2017), chapters 5, 8 and 9, and “How to do distributed locking” (2016). Diego Ongaro and John Ousterhout, “In Search of an Understandable Consensus Algorithm (Raft)” (2014). Burrows, “The Chubby lock service” (2006). The PostgreSQL documentation on high availability and replication, and the Patroni documentation. Google, <i>Site Reliability Engineering</i> (2016), chapter 23, “Managing Critical State”.",
)
