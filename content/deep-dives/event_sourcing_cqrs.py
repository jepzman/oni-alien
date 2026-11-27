# Deep dive 04 · Event Sourcing & CQRS. Builds on Vol. 1 notes 08 (event sourcing) and 09 (CQRS).
# Example, from the event sourcing note: bank account acc-1 (Deposited 100, Withdrew 30), with two read models,
# a balances table and a monthly statement.
# Helpers (mn, full, tbl, drill, code, fig, checklist) are injected by scripts/build_notes.py from scripts/dive.py.

# ------------------------------------------------------------------ 1 recap
flow_svg = '''
  <rect class="bx" x="10" y="70" width="110" height="50" rx="8"/><text class="lbl" x="65" y="92" text-anchor="middle">command</text><text class="soft" x="65" y="112" text-anchor="middle">Withdraw 50</text>
  <rect class="bx-y" x="160" y="40" width="150" height="110" rx="8"/><text class="lbl" x="235" y="64" text-anchor="middle">write side</text>
  <text x="235" y="90" text-anchor="middle">1 load + replay</text><text x="235" y="112" text-anchor="middle">2 decide</text><text x="235" y="134" text-anchor="middle">3 append</text>
  <rect class="bx" x="350" y="20" width="150" height="150" rx="8"/><text class="lbl" x="425" y="44" text-anchor="middle">stream acc-1</text>
  <text class="soft" x="425" y="70" text-anchor="middle">1 Opened</text><text class="soft" x="425" y="92" text-anchor="middle">2 Deposited 100</text><text class="soft" x="425" y="114" text-anchor="middle">3 Withdrew 30</text>
  <rect class="bx-g" x="364" y="126" width="122" height="30" rx="5"/><text x="425" y="147" text-anchor="middle">4 Withdrew 50</text>
  <rect class="bx" x="540" y="30" width="100" height="50" rx="8"/><text class="lbl" x="590" y="61" text-anchor="middle">projections</text>
  <rect class="bx-y" x="540" y="110" width="100" height="36" rx="6"/><text x="590" y="134" text-anchor="middle">balances</text>
  <rect class="bx-y" x="540" y="154" width="100" height="36" rx="6"/><text x="590" y="178" text-anchor="middle">statement</text>
  <rect class="bx" x="670" y="126" width="80" height="50" rx="8"/><text class="lbl" x="710" y="157" text-anchor="middle">query</text>
  <path class="ln" d="M120 95 H158" marker-end="url(#a)"/><path class="ln" d="M310 95 H348" marker-end="url(#a)"/>
  <path class="ln" d="M500 55 H538" marker-end="url(#a)"/><path class="ln" d="M590 80 V108" marker-end="url(#a)"/>
  <path class="ln" d="M670 150 H642" marker-end="url(#a)"/>
  <text class="soft" x="235" y="176" text-anchor="middle">rules live here</text><text class="soft" x="590" y="20" text-anchor="middle">a moment later</text>
'''
recap = '''
<p>The note used a bank passbook. Account <code>acc-1</code> has no “balance” cell that gets overwritten. It has lines: opened, deposited 100, withdrew 30. The balance, 70, is those lines added up.</p>
''' + tbl(["Note", "In one line"], [
    ["Event Sourcing", "store every change as an event that is never altered; work out the current state by replaying them"],
    ["CQRS", "one model for changing data, with the rules; separate models for reading, shaped for each screen"],
]) + fig(760, 200, "The flow of one command. A Withdraw 50 command reaches the write side, which loads and replays the stream for account acc-1, decides, and appends. The stream holds four events: Opened, Deposited 100, Withdrew 30 and the new Withdrew 50. A moment later, projections read the new event and update two read models, a balances table and a statement. Queries read only the read models.",
          flow_svg, "Writes go left to right through the stream. Reads never touch it.") + mn("The two patterns are separate ideas. They show up together because an event log is hard to query.") + '''
<p class="full">The notes explained why you might want this. They left out what it is like to live with: a table you may only add to, code that must still understand events written five years ago, read models that are always a little behind, and a privacy law that says “delete” to a design that never deletes. Those are the chapters.</p>
'''

# ------------------------------------------------------------------ 2 the store
store = '''
<p>An event store can be a specialised database or one table. The table shows what the specialised products do for you.</p>
''' + code("events.sql", "the whole write model", '''
CREATE TABLE events (
  position   BIGSERIAL PRIMARY KEY,   -- order across all streams
  stream_id  TEXT NOT NULL,           -- 'acc-1'
  version    INT  NOT NULL,           -- 1, 2, 3... within the stream
  event_id   UUID NOT NULL,
  type       TEXT NOT NULL,           -- 'Withdrew'
  data       JSONB NOT NULL,          -- {"amount": 30}
  meta       JSONB NOT NULL,          -- who, when, which command
  UNIQUE (stream_id, version)
);
''') + tbl(["position", "stream", "version", "type", "data"], [
    ["1040", "acc-1", "1", "Opened", "{\"owner\": \"c-7\"}"],
    ["1041", "acc-1", "2", "Deposited", "{\"amount\": 100}"],
    ["1077", "acc-2", "1", "Opened", "{\"owner\": \"c-9\"}"],
    ["1102", "acc-1", "3", "Withdrew", "{\"amount\": 30}"],
], mono=(0, 1, 2, 4)) + mn("Two orderings: version inside one account, position across all of them. Writers care about the first, projections about the second.") + '''
<h3>The one constraint that does the work</h3>
<p><code>UNIQUE (stream_id, version)</code> is the concurrency control for the whole write side. A writer that loaded the account at version 3 appends its event as version 4. If someone else got there first, version 4 already exists and the insert fails. The writer never needs a lock. It reloads and decides again (drill 1).</p>
''' + code("append.sql", "append with an expected version", '''
INSERT INTO events (stream_id, version, event_id, type, data, meta)
VALUES ('acc-1', 4, 'e-71c2', 'Withdrew', '{"amount": 50}',
        '{"by": "c-7", "command": "cmd-88"}');
-- unique violation = someone else wrote version 4 first
''') + full('''<h3>What a stream is</h3>
<p>A stream holds the events of one <b>aggregate</b>: one thing whose rules must be checked together. For a bank that is one account, because “the balance may not go below zero” is a rule about one account. A transfer between two accounts is two streams and therefore two appends, which is the Saga deep dive's subject and not something an event store solves.</p>
''' + tbl(["Stream too big", "Stream too small"], [
    ["“all accounts of customer c-7” in one stream: every deposit conflicts with every other, and the stream grows without end", "“one stream per transaction”: no place where the balance rule can be checked"],
]) + '''<p>Rule of thumb: a stream is the smallest thing that can enforce its own rules, and it should have an end. An account that lives for thirty years is a problem that chapter 7 solves.</p>
<h3>Three rules of the table</h3>
<ul>
  <li><b>Insert only.</b> No <code>UPDATE</code>, no <code>DELETE</code>. Take the permission away from the application's database user so that it is a fact and not a habit.</li>
  <li><b>Events record what was decided, not what was asked.</b> <code>Withdrew 50</code>, not <code>WithdrawRequested 50</code>. A rejected command leaves no event in the account's stream.</li>
  <li><b>Put who, when and why in <code>meta</code>.</b> The user, the time and the id of the command that caused the event. This is the audit trail you were promised, and it only exists if you write it.</li>
</ul>''')

# ------------------------------------------------------------------ 3 decide and evolve
decide = '''
<p>The note's code had three steps in one function: replay, decide, append. In a real codebase the first two become two small functions with no database in them, and that separation is the best thing event sourcing gives a programmer.</p>
''' + code("account.ts", "the whole business logic of an account", '''
type State = { open: boolean; balance: number };
const initial: State = { open: false, balance: 0 };

// evolve: what an event does to the state. Never fails, never decides.
const evolve = (s: State, e: Event): State => {
  switch (e.type) {
    case "Opened":    return { open: true, balance: 0 };
    case "Deposited": return { ...s, balance: s.balance + e.amount };
    case "Withdrew":  return { ...s, balance: s.balance - e.amount };
    default:          return s;            // unknown event: ignore
  }
};

// decide: given the state, is this command allowed, and what happened?
const decide = (s: State, c: Command): Event[] => {
  if (!s.open) throw new Rejected("No such account");
  if (c.type === "Withdraw") {
    if (c.amount > s.balance) throw new Rejected("Insufficient funds");
    return [{ type: "Withdrew", amount: c.amount }];
  }
  return [{ type: "Deposited", amount: c.amount }];
};
''') + tbl(["", "<code>decide</code>", "<code>evolve</code>"], [
    ["Input", "state + command", "state + event"],
    ["Output", "new events, or a rejection", "new state"],
    ["May say no?", "yes, that is its job", "never. The event already happened"],
    ["Runs", "once, when the command arrives", "every time the stream is loaded, for ever"],
]) + mn("A command is a request and can be refused. An event is a fact and can't.") + full('''<h3>Why <code>evolve</code> must be boring</h3>
<p><code>evolve</code> will run on the same event thousands of times over the years: on every load, on every replay. It has to give the same answer each time. Three things are forbidden in it.</p>
''' + tbl(["Forbidden in <code>evolve</code>", "What goes wrong"], [
    ["Rejecting or throwing", "an account that loaded yesterday cannot be loaded today, and no command can fix it"],
    ["Reading the clock, a config value or another service", "replaying the same events gives a different state on Tuesday than on Monday"],
    ["Side effects: sending, calling, writing", "they happen again on every load (drill 6)"],
]) + '''<p>If a rule changes, say the bank now allows an overdraft of 200, the change goes in <code>decide</code>. Old events stay valid, because they were legal under the rule of their day. <code>evolve</code> does not re-judge the past.</p>
<h3>The handler around them</h3>
''' + code("handle.ts", "load, decide, append, retry on conflict", '''
export async function handle(streamId: string, command: Command) {
  for (let attempt = 1; attempt <= 3; attempt++) {
    const { events, version } = await store.load(streamId);
    const state = events.reduce(evolve, initial);
    const newEvents = decide(state, command);          // may throw Rejected
    try {
      return await store.append(streamId, newEvents, { expectedVersion: version });
    } catch (err) {
      if (!(err instanceof VersionConflict)) throw err;  // someone else wrote: go round again
    }
  }
  throw new Busy("Account is being changed, try again");
}
''') + '''<p>This function is the same for every aggregate in the system. All the thinking is in <code>decide</code> and <code>evolve</code>, which can be tested without a database (chapter 9).</p>''')

# ------------------------------------------------------------------ 4 drills
drills = mn("Cover the bottom of each card. What would you expect to happen?") + '''
<ul class="drill-index" aria-label="The six drills">
  <li><a href="#drill-1">1 · two withdrawals</a></li><li><a href="#drill-2">2 · projection crash</a></li><li><a href="#drill-3">3 · stale read</a></li>
  <li><a href="#drill-4">4 · old event, new code</a></li><li><a href="#drill-5">5 · endless stream</a></li><li><a href="#drill-6">6 · replayed emails</a></li>
</ul>
''' + drill(1, "Two withdrawals at the same moment", [
    ("Timeline", "The balance is 70. The owner withdraws 50 at a cash machine while a card payment of 50 arrives. Both handlers load version 3, both see 70, both decide “allowed”."),
    ("Without the constraint", "Both append. The stream now says: deposited 100, withdrew 30, withdrew 50, withdrew 50. The balance is −30 and every rule was checked.", True),
    ("What saves you", "Both try to write version 4. One insert succeeds; the other hits <code>UNIQUE (stream_id, version)</code>. That handler reloads, sees a balance of 20, runs <code>decide</code> again and rejects the payment: insufficient funds."),
], "every append names the version it expects. A decision made on old state is never written.") + drill(2, "The projection crashes halfway", [
    ("Timeline", "The balances projection reads <code>Deposited 100</code> at position 1041, adds 100 to the balances table, and crashes before it records that 1041 is done. After the restart it reads 1041 again and adds another 100."),
    ("What you see", "The read model says 200. The event stream says 100. Nothing in the stream is wrong, which makes this confusing to investigate.", True),
    ("What saves you", "The projection keeps a <b>checkpoint</b>, the last position it applied, and writes it in the <b>same transaction</b> as the change to the read model. Either both happen or neither. It is the idempotent consumer from the Reliable Messaging deep dive, with a position where the event id was."),
], "a projection's checkpoint and its data are committed together.") + drill(3, "“I just paid in, where is my money?”", [
    ("Timeline", "The owner deposits 100. The command succeeds and the page reloads. The balances projection is 400 ms behind. The page shows the old balance."),
    ("Why", "The write went to the stream. The read came from a table that a separate process fills. Between the two there is always a gap; usually milliseconds, sometimes more.", True),
    ("The tempting mistake", "Make the projection synchronous “just for now”, or have the page read the stream directly. Both quietly undo the split, one screen at a time.", True),
    ("What saves you", "The command returns the position of the event it wrote. The page passes that position with its next query, and the read side waits briefly until its checkpoint has reached it. Chapter 5 has this and two other options."),
], "the lag is part of the design. Decide, screen by screen, what the user sees during it.") + drill(4, "A two-year-old event meets today's code", [
    ("Timeline", "Last spring the team changed amounts from dollars to cents and renamed the field: new events say <code>{\"amountCents\": 3000}</code>. Today someone rebuilds the statement projection from the beginning. It reads a 2025 event, <code>{\"amount\": 30}</code>, finds no <code>amountCents</code>, and writes a withdrawal of nothing."),
    ("What you see", "No error. Statements for the years before the change are wrong, and balances rebuilt from them are wrong by large amounts.", True),
    ("What saves you", "Old events are never rewritten, so the code must keep understanding them. An <b>upcaster</b> converts each old shape to the current one as events are read, before any other code sees them. And a test replays a sample of every event shape ever stored (chapters 6 and 9)."),
], "every event shape you have ever written is part of your codebase for ever.") + drill(5, "The stream that never ends", [
    ("Timeline", "A business account receives two thousand payments a day. After three years its stream holds two million events. Every command for that account now starts by loading and replaying all of them."),
    ("What you see", "One customer, your largest, has payments that take eight seconds. All other accounts are fast, so averages look healthy.", True),
    ("What saves you", "A <b>snapshot</b>: the state at version 2,000,000 stored on the side, so a load reads the snapshot and only the events after it. Better, where the business allows it, give streams an end: close the account's books each month and start a new stream from the closing balance (chapter 7)."),
], "load time grows with stream length. Plan the end of a stream when you design its beginning.") + drill(6, "The rebuild that emailed everyone", [
    ("Timeline", "A handler listens for <code>Deposited</code> and emails “you received a payment”. It was written like a projection. Someone resets its checkpoint to zero to fix a bug, and it replays three years of deposits."),
    ("What you see", "Every customer receives an email for every deposit they have ever had.", True),
    ("What saves you", "Keep two kinds of event handler apart. A <b>projection</b> only writes its own read model, so it can be replayed any number of times. A <b>reactor</b> does something in the outside world, so it must never be replayed: its checkpoint only moves forward, and it is idempotent in the way chapter 6 of the Reliable Messaging dive describes."),
], "projections are replayable and reactors are not. Never let one handler be both.") + full('''<h3>What the six drills add up to</h3>
''' + tbl(["Part", "Its duty", "Drill"], [
    ["Write side", "append with an expected version; retry by deciding again", "1"],
    ["Projection", "checkpoint and data in one transaction; no outside effects", "2, 6"],
    ["Reactor", "forward-only checkpoint; idempotent effects", "6"],
    ["Screens", "a chosen behaviour for the lag", "3"],
    ["Event shapes", "old versions upcast on read, and tested", "4"],
    ["Streams", "a snapshot, or an end", "5"],
]))

# ------------------------------------------------------------------ 5 projections
projections = '''
<p>A projection is a loop: read the next event by position, change a table, save the position. Everything a user ever sees comes out of such loops, so their behaviour is the behaviour of the product.</p>
''' + code("balances-projection.sql", "one event, one transaction", '''
BEGIN;
UPDATE balances SET balance = balance - 50, version = 4
WHERE account_id = 'acc-1';

UPDATE checkpoints SET position = 1130
WHERE projection = 'balances' AND position = 1102;   -- 0 rows? someone else is running: stop
COMMIT;
''') + '''
<h3>Two ways to run one</h3>
''' + tbl(["", "Inline", "Asynchronous"], [
    ["Runs", "inside the transaction that appends the event", "in its own process, a moment later"],
    ["Read model is", "always up to date", "slightly behind"],
    ["Cost", "every write waits for every inline projection; only works in the same database", "the lag, and a process to run and watch"],
    ["Use for", "the one or two views that must never be stale, such as the balance shown before a withdrawal", "everything else: search, statements, reports, other databases"],
]) + mn("Inline is not cheating. One strictly consistent view plus ten lagging ones is a very common shape.") + '''
<h3>Living with the lag</h3>
<p>Drill 3 has three honest answers. Choose per screen.</p>
''' + tbl(["Option", "How", "Fits"], [
    ["<b>Wait for my write</b>", "the command returns its position; the query says “not before position 1130”; the read side waits up to half a second", "the screen straight after an action"],
    ["<b>Show it optimistically</b>", "the client already knows what it did, so it displays the new balance and reconciles on the next load", "simple changes with a predictable result"],
    ["<b>Say it is in progress</b>", "“Deposit received. Your balance will update in a moment.”", "slow or multi-step results"],
]) + full('''<h3>The superpower: throw it away and rebuild</h3>
<p>A read model contains nothing that is not in the events. So when a projection has a bug, or a screen needs a new column, you do not migrate the table. You fix the code and build the table again from position zero. This is the real reason to accept the rest of the cost.</p>
<p>A rebuild on a live system is done beside the old table, not in place.</p>
<ol>
  <li>Deploy the new projection as <code>balances_v2</code> with its own checkpoint at zero.</li>
  <li>Let it replay. The old table keeps serving queries.</li>
  <li>When <code>balances_v2</code> has caught up, point the queries at it.</li>
  <li>Stop the old projection and drop the old table a few days later.</li>
</ol>
<p>Know how long step 2 takes. A projection that handles 5,000 events a second replays 400 million events in about 22 hours. If that is too long to wait during an incident, the options are faster replay (batch the writes, run streams in parallel where order allows) or snapshots of the read model itself.</p>
<h3>Order and gaps</h3>
<p>A projection needs events in a stable order and must not skip any. Asking the table for “position greater than my checkpoint” has the same hole as the outbox relay in the Reliable Messaging dive: positions are handed out at insert and become visible at commit, so a slow transaction can surface behind your checkpoint. Purpose-built event stores handle this for you. On a plain table you must either serialise appends or read only up to a position that is known to be complete. It is the main reason a home-made store is harder than its one table suggests.</p>''')

# ------------------------------------------------------------------ 6 versioning
versioning = '''
<p>In an ordinary system, when the shape of the data changes you run a migration and the old shape is gone. Here the old shape is in the log for good, and the log is the source of truth. Changing your mind is the hardest part of event sourcing, and it comes to every system that lives longer than a year.</p>
''' + tbl(["Change", "What to do", "Risk"], [
    ["Add an optional field", "nothing in old events; the reader supplies a default when it is missing", "low"],
    ["Rename a field, change a unit", "new events use the new shape, with a version number; an upcaster converts old ones on read", "medium"],
    ["Split one event into two, or merge two", "an upcaster that turns one stored event into several, or the reverse", "medium"],
    ["The <i>meaning</i> changes", "a new event type with a new name. The old type keeps its old meaning for ever", "high if you reuse the name"],
    ["An event was simply wrong", "append a correcting event (chapter 8). Never edit", "low, if you resist the urge"],
], hot=(3,)) + code("upcast.ts", "runs on every event as it is read", '''
const upcast = (e: Stored): Stored => {
  if (e.type === "Withdrew" && e.v === 1) {
    // v1 stored dollars as "amount"; v2 stores cents as "amountCents"
    return { ...e, v: 2, data: { amountCents: e.data.amount * 100 } };
  }
  return e;
};
''') + mn("decide, evolve and every projection only ever see the newest shape. The mess stays in one file.") + full('''<p>Upcasters chain: a version 1 event is converted to 2, then 2 to 3. Each one is small and none is ever deleted, because the version 1 events are still in the table.</p>
<h3>Habits that make later changes cheaper</h3>
''' + tbl(["Habit", "Why"], [
    ["Name events after what happened in the business: <code>Withdrew</code>, <code>AccountFrozen</code>", "business facts change meaning rarely. <code>AccountUpdated</code> with a list of changed fields will need changing every sprint"],
    ["Store what was decided, with its inputs: the amount, the fee charged, the rate applied", "replay must not recompute the fee with today's price list"],
    ["Put a version number in every event from the first day", "the upcaster needs something to switch on"],
    ["Read tolerantly: ignore unknown fields and unknown event types", "old code survives new events during a rolling deploy"],
    ["Keep events small and specific", "a change touches one event type, not all of them"],
]) + '''<h3>Inside events and outside events</h3>
<p>The events in your store are your private data model. Other services should not read them directly, for the same reason they should not read your tables: you lose the freedom to change. Publish a separate, smaller set of <b>integration events</b>, translated from the internal ones by a reactor and sent through an outbox. The internal <code>Withdrew</code> v3 can then change shape without anyone outside noticing, and the contract rules of the Reliable Messaging dive apply only to what you chose to publish.</p>
<h3>The last resort</h3>
<p>Sometimes the upcasters become a tangle, or a design mistake runs through years of events. Then you can build a new store: read every event from the old one, transform it, write it to the new one, and switch. This is a project with a rehearsal and a rollback plan. Needing it once in the life of a system is normal. Needing it yearly means the events are modelled at the wrong level.</p>''')

# ------------------------------------------------------------------ 7 snapshots
snap_svg = '''
  <text class="lbl" x="20" y="28">stream acc-9 (a busy account)</text>
  <rect class="bx" x="20" y="44" width="540" height="40" rx="6"/>
  <text class="soft" x="290" y="70" text-anchor="middle">events 1 … 2,000,000</text>
  <rect class="bx-g" x="570" y="44" width="170" height="40" rx="6"/><text x="655" y="70" text-anchor="middle">2,000,001 … 2,000,340</text>
  <rect class="bx-y" x="440" y="120" width="240" height="46" rx="8"/><text class="lbl" x="560" y="140" text-anchor="middle">snapshot at 2,000,000</text><text class="soft" x="560" y="158" text-anchor="middle">balance 18,420.55</text>
  <path class="ln-d" d="M560 86 V118" marker-end="url(#a)"/>
  <path class="ln" d="M680 143 H716 V88" marker-end="url(#a)"/>
  <text class="soft" x="150" y="150" text-anchor="middle">without: replay 2,000,340 events</text><text class="soft" x="150" y="172" text-anchor="middle">with: read 1 row + replay 340</text>
'''
snapshots = '''
<p>Loading an account means replaying its stream. That is instant for 50 events and painful for two million (drill 5). There are two remedies, and the second is the better one.</p>
''' + fig(760, 190, "A stream with two million events followed by 340 newer ones. A snapshot stored on the side holds the state at event two million: a balance of 18,420.55. Loading the account reads the snapshot and then replays only the 340 events after it.",
          snap_svg, "A snapshot is a saved answer to “what does evolve give for the first two million events?”") + '''
<h3>Remedy 1: snapshots</h3>
''' + tbl(["Question", "Answer"], [
    ["What is it?", "the output of <code>evolve</code> at some version, stored in a separate table with that version"],
    ["Is it the truth?", "no. It is a cache. The events are the truth, and any snapshot can be deleted and recomputed"],
    ["When to take one?", "every few hundred or thousand events, in the background, never inside a command"],
    ["When does it go stale?", "when <code>evolve</code> or the shape of the state changes. Store a schema number with each snapshot and ignore snapshots from older code"],
]) + mn("Don't add snapshots on day one. Add them when a real stream is slow to load.") + full('''<p>Snapshots have a cost that is easy to miss. They are a second copy of the state with its own versioning problem, and a bug in snapshot code produces wrong state that looks correct. Keep the rule strict: loading with the snapshot and loading without it must give the same state, and a test checks it.</p>''') + '''
<h3>Remedy 2: close the books</h3>
<p>Accountants solved this long ago. At the end of a period they total the ledger, write the closing balance as the first line of a new book and put the old book on a shelf.</p>
''' + tbl(["Stream", "Events"], [
    ["<code>acc-9-2026-10</code>", "… <code>Withdrew</code>, <code>Deposited</code>, <b><code>PeriodClosed {balance: 18,420.55}</code></b>"],
    ["<code>acc-9-2026-11</code>", "<b><code>PeriodOpened {balance: 18,420.55}</code></b>, <code>Deposited</code>, …"],
], hot=(1,)) + full('''<p>The closing event is a real business fact, written by <code>decide</code>, not a technical cache. Every stream is now at most a month long. Old months can move to cheaper storage. And an event shape that changes only has to be understood for as long as open periods can contain it, which also softens chapter 6.</p>
<p>It needs one thing from the business: a natural period. Months for an account, a trip for a taxi, a visit for a patient, an order for a shop. Most things that run for a long time are really a series of shorter things, and modelling them that way removes the long stream instead of working around it.</p>
''' + tbl(["", "Snapshot", "Closing the books"], [
    ["Kind of thing", "a cache", "a business event"],
    ["Stream length", "still grows", "bounded"],
    ["Extra risk", "stale or wrong snapshots", "a period boundary to design"],
    ["Choose when", "streams are long and have no natural period", "the business already thinks in periods"],
]))

# ------------------------------------------------------------------ 8 deleting and correcting
deleting = '''
<p>The table may only be added to. Two everyday needs seem to contradict that: fixing a mistake, and erasing a person's data when the law requires it.</p>
<h3>Fixing a mistake</h3>
<p>A teller types a deposit of 1,000 where the slip said 100. In an ordinary system someone edits the row. Here the passbook rule applies: the wrong line stays, and a correcting line is added.</p>
''' + tbl(["version", "type", "data", "meta"], [
    ["7", "Deposited", "{\"amount\": 1000}", "by teller t-4"],
    ["8", "DepositReversed", "{\"amount\": 1000, \"reverses\": 7}", "by supervisor s-1, reason: keying error"],
    ["9", "Deposited", "{\"amount\": 100}", "by supervisor s-1"],
], hot=(1,), mono=(0, 2)) + mn("The audit trail now shows the error, who fixed it and why. An edited row would show none of that.") + '''
<p>The balance comes out right, the statement shows what happened, and every projection receives the correction through the normal path with no special rebuild.</p>
''' + full('''<p>The same applies when the mistake was a bug in <code>decide</code> that wrote wrong events for a week. Write a one-off script that appends correcting events through the normal command path, with <code>meta</code> saying which incident caused them. Editing the stored events to hide the bug would also change what every projection and every other service has already seen and acted on, without telling them.</p>''') + '''
<h3>Erasing personal data</h3>
<p>A customer closes their account and asks for their data to be erased. Their name and address are inside events that must never change. There are three approaches, in order of preference.</p>
''' + tbl(["Approach", "How", "Cost"], [
    ["<b>Keep it out</b>", "events carry a customer id only; name and address live in an ordinary table that can be updated and deleted", "none later. Needs the discipline from day one"],
    ["<b>Forget the key</b>", "personal fields in events are encrypted with a key kept per customer; erasing means deleting that key, and the fields become unreadable everywhere, backups included", "a key store to run; every reader must cope with “no longer readable”"],
    ["<b>Rewrite the stream</b>", "copy the stream without the personal data, replace the original", "breaks the rule of the table; every projection must be rebuilt; a last resort"],
], hot=(0,)) + full('''<p>The first approach is far the cheapest and is mostly a modelling habit: an event says <i>that</i> customer c-7 changed their address, and the address itself is stored where personal data normally lives. Money events rarely need a name in them at all.</p>
<p>Whether deleting a key satisfies the law in your situation is a question for your data protection officer, not for a design pattern. Ask it before the first personal field goes into an event, because afterwards only the expensive options remain.</p>
<p>Read models hold copies of personal data too. They are ordinary tables, so they are deleted in the ordinary way, and a rebuild must not bring the data back. With either of the first two approaches it cannot.</p>''')

# ------------------------------------------------------------------ 9 testing and running
testing = '''
<p>Because <code>decide</code> and <code>evolve</code> are plain functions, the business rules of an event-sourced system are easier to test than most. Tests read as three lines: given these events, when this command, then these events.</p>
''' + code("account.test.ts", "given, when, then", '''
test("cannot withdraw more than the balance", () => {
  given([opened(), deposited(100), withdrew(30)])
    .when(withdraw(80))
    .thenRejected("Insufficient funds");
});

test("a withdrawal within the balance is recorded", () => {
  given([opened(), deposited(100), withdrew(30)])
    .when(withdraw(50))
    .then([withdrew(50)]);
});
''') + mn("No database, no mocks, a few milliseconds each. Hundreds of these are cheap.") + tbl(["What", "Test", "Catches"], [
    ["Rules", "given events, when command, then events or a rejection", "wrong decisions"],
    ["Projections", "given events, then these rows in the read model", "wrong sums, missing cases"],
    ["Projection twice", "apply the same event twice with the same checkpoint", "drill 2"],
    ["Every event shape", "one stored sample of each type and version, loaded through the upcasters and <code>evolve</code>", "drill 4"],
    ["Snapshot", "state with snapshot equals state without", "stale or wrong snapshots"],
    ["Concurrency", "two commands on the same version: one is written, one decides again", "drill 1"],
]) + full('''<h3>The test that earns its keep</h3>
<p>Keep a folder of sample events: one real example of every type and every version that has ever been stored, with personal data removed. A test loads them all through the current code. The day someone changes <code>evolve</code> in a way that breaks a 2025 event, this test fails in the build, a year before a rebuild would have found it in production. Where it is allowed, also replay a full copy of production events through new projection code before each release.</p>
<h3>What to watch</h3>
''' + tbl(["Metric", "Healthy", "It means trouble when"], [
    ["<b>Projection lag</b>, per projection, in time", "under a second", "it grows: the projection is stuck on one event or too slow for the write rate"],
    ["<b>Version conflicts</b> as a share of commands", "well under 1 %", "it climbs: a stream is too coarse, and unrelated changes collide"],
    ["<b>Stream length</b>, the longest and the 99th percentile", "hundreds", "thousands and rising: drill 5 is on its way"],
    ["<b>Load time</b> of an aggregate, slow case", "milliseconds", "it tracks stream length"],
    ["<b>Rebuild time</b> of each projection", "known, and acceptable", "nobody knows it"],
]) + '''<h3>Runbook: “the read model is wrong”</h3>
<ol>
  <li><b>Compare with the stream.</b> Load the aggregate's events and work out the right answer by hand. The stream is the truth.</li>
  <li><b>Stream right, read model wrong?</b> It is a projection bug or a skipped event. Fix the projection, rebuild it beside the old one, switch (chapter 5).</li>
  <li><b>Stream wrong too?</b> It is a bug in <code>decide</code>, or wrong input. Fix the code, then append correcting events (chapter 8). The projections follow by themselves.</li>
  <li><b>Read model merely behind?</b> Check the lag graph. A projection stuck on one position usually means an event it cannot handle: look at that event before touching the checkpoint.</li>
</ol>
<p>Never fix a read model by editing its rows. The next rebuild will put the error back, and you will have lost the evidence of what caused it.</p>''')

# ------------------------------------------------------------------ 10 when, tools, lab
tools = '''
<h3>When to use which</h3>
<p>The two patterns are separate decisions, and neither is for a whole system.</p>
''' + tbl(["Level", "What it is", "Fits"], [
    ["0 · one model", "the same tables for writing and reading", "most screens in most systems"],
    ["1 · light CQRS", "same database; separate query code, views or a few read tables", "a few screens whose reads are heavy or oddly shaped"],
    ["2 · full CQRS", "separate read stores fed by events from an outbox", "search, dashboards, very uneven read and write load"],
    ["3 · event sourcing", "the events are the write model", "the core where history <i>is</i> the business: money, stock, bookings, anything audited"],
], hot=(3,)) + mn("One or two aggregates at level 3, the rest at level 0 or 1. That is a healthy system.") + full('''<p>Move up a level when a specific pain appears, and only for the part that has it. Signs that level 3 fits: people ask “how did it get into this state?” every week; regulators want the history; the business already talks in events (“deposited”, “shipped”, “cancelled”). Signs that it does not: the data is mostly edited forms, such as a profile or a product description, and nobody cares what it said last Tuesday.</p>
<h3>Tools</h3>
''' + tbl(["Kind", "Examples", "Gives you"], [
    ["Purpose-built event store", "KurrentDB (formerly EventStoreDB), Axon Server", "streams, expected-version appends, ordered subscriptions with no gaps"],
    ["Library on a relational database", "Marten (.NET on PostgreSQL), Eventuous", "the table, snapshots and projections managed for you"],
    ["Your own table", "chapter 2", "full control, and the gap problem from chapter 5 to solve"],
    ["A log broker such as Kafka", "", "a good way to <i>distribute</i> events; no per-stream expected version, so not a write model on its own"],
])) + '''
<h3>Lab</h3>
<p>The bank adds an <b>overdraft</b>. Each account may be given a limit; withdrawals may take the balance down to minus that limit. Overdrawn accounts pay a fee of 5 on the first day of each month. Support wants a screen listing every overdrawn account.</p>
<ol class="keep">
  <li>Which new events do you need? Name them as business facts.</li>
  <li>What changes in <code>decide</code>, and what in <code>evolve</code>?</li>
  <li>The limit for acc-1 is lowered from 200 to 100 while the balance is −150. What should happen?</li>
  <li>How is the support screen built, and may it lag?</li>
  <li>The fee later changes from 5 to 7. What must still be true when an old stream is replayed?</li>
</ol>
<div class="check quiz"><h3>model answer</h3>
<details><summary>1 · Events</summary><p><code>OverdraftLimitSet {limit}</code> and <code>OverdraftFeeCharged {amount, period}</code>. Not <code>AccountUpdated</code>. Each is a fact a bank employee would recognise.</p></details>
<details><summary>2 · decide and evolve</summary><p><code>evolve</code> remembers the limit and subtracts fees from the balance. <code>decide</code> for a withdrawal now checks <code>amount ≤ balance + limit</code>. Old events need no change: accounts without a limit event have a limit of zero, which is the old rule.</p></details>
<details><summary>3 · Lowering the limit</summary><p>The event is still accepted, because it is a fact that the bank lowered the limit. It does not undo past withdrawals, which were legal when made. <code>decide</code> simply refuses further withdrawals until the balance is above −100. If the bank wants to block the change instead, that is a rule in <code>decide</code> for the <code>SetOverdraftLimit</code> command.</p></details>
<details><summary>4 · The support screen</summary><p>A new projection, <code>overdrawn_accounts</code>, fed by deposits, withdrawals and fees. It is built by replaying from position zero, so it is complete on its first day. It may lag by seconds: support staff are not harmed by a short delay, so it runs asynchronously.</p></details>
<details><summary>5 · The fee change</summary><p>The amount is stored in each <code>OverdraftFeeCharged</code> event. Replaying a 2026 stream must still subtract 5 for the 2026 fees. If <code>evolve</code> looked the fee up in today's configuration, every historical balance would change the day the price list did.</p></details>
</div>
<h3>The review checklist</h3>
''' + checklist([
    ("Streams and the store", ["One stream per thing that enforces its own rules", "Every append carries an expected version; a conflict means decide again", "The events table is insert-only, enforced by database permissions", "Every event records who, when and which command", "Each kind of stream has a planned end, or a snapshot plan"]),
    ("Write logic", ["decide and evolve are plain functions with no database or clock", "evolve never rejects and has no side effects", "Events store what was decided, with the values used", "Events are named after business facts"]),
    ("Projections and reactors", ["Checkpoint and read model are committed together", "Projections only write their own read model", "Reactors move forward only and are idempotent", "Each screen has a chosen behaviour for the lag", "Every projection can be rebuilt beside the old one, and its rebuild time is known"]),
    ("Change over time", ["Every event has a version number", "Old shapes are upcast on read; nothing is rewritten", "A changed meaning gets a new event type", "Other services receive translated integration events, not the internal ones"]),
    ("Correcting and erasing", ["Mistakes are fixed with correcting events that say why", "Personal data is kept out of events, or encrypted with a per-person key", "The erasure approach has been agreed with whoever is responsible for privacy"]),
    ("Tests and operations", ["Rules are tested as given events, when command, then events", "A sample of every event type and version is replayed in the build", "Projection lag, version conflicts and stream length are on a dashboard", "Read models are never repaired by hand"]),
])

# ------------------------------------------------------------------ the dive
DIVE = dict(
    slug="event-sourcing-cqrs", no=4, title="Event Sourcing & CQRS",
    sub="What it is like to live with a table you may only add to: old events, lagging read models, long streams and the right to be forgotten.",
    summary="A deep dive on event sourcing and CQRS: the event store, decide and evolve, six failure drills, projections and lag, versioning events, snapshots and closing the books, corrections and erasure, testing and operations.",
    builds_on="Vol. 1, notes 08 and 09",
    builds_on_links=[("Event Sourcing", "../../distributed/notes/event-sourcing.html"), ("CQRS", "../../distributed/notes/cqrs.html")],
    notes=[("distributed", "event-sourcing"), ("distributed", "cqrs")],
    facts=[("Example", "bank account acc-1 and its passbook")],
    blurb="The event store, decide and evolve, six failure drills, projections and their lag, versioning, snapshots, corrections and erasure.",
    chapters=[
        dict(id="recap", nav="Recap", title="Two notes in sixty seconds",
             gist="Event sourcing stores every change as an event and works out the current state by replaying them. CQRS reads from separate models that are filled from those events. The notes gave the reasons. This deep dive is about the long-term cost: old events, lagging views, long streams and deletion.",
             body=recap),
        dict(id="store", nav="The store", title="The event store, for real",
             gist="An event store is an insert-only table with two orderings: a version inside each stream and a position across all of them. One unique constraint on stream and version is the whole concurrency control. A stream holds one thing that enforces its own rules, and it should have an end.",
             body=store,
             check=[("Why is a money transfer between two accounts not a single append?", "It touches two streams, and the expected-version check protects one stream at a time. Coordinating the two is a saga."),
                    ("A rejected withdrawal: is there an event in the account's stream?", "No. Events record what was decided and happened. A refused command changes nothing.")]),
        dict(id="decide", nav="Decide & evolve", title="Decide and evolve",
             gist="The write side is two plain functions. decide takes the state and a command and returns new events or a rejection. evolve takes the state and an event and returns the next state, and it must never fail, read the clock or cause side effects, because it runs again on every load for ever.",
             body=decide,
             check=[("The bank raises the minimum balance from 0 to 10. Where does the change go, and what happens to accounts already below 10?", "In decide. Old events stay valid; those accounts simply cannot withdraw until they are above 10."),
                    ("Why may evolve not throw on an event it dislikes?", "The event is already stored and will be replayed on every load. If evolve throws, the aggregate can never be loaded again.")]),
        dict(id="drills", nav="Failure drills", title="Failure drills",
             gist="Six things that will happen: two commands on the same version, a projection that crashes halfway, a user who reads before the projection has caught up, an old event that today's code misreads, a stream with two million events, and a rebuild that repeats side effects.",
             body=drills,
             check=[("After drill 1's conflict, why does the handler run decide again and not simply retry the insert with version 5?", "The state changed. The decision was made on a balance of 70; it must be made again on 20, and this time it is a rejection."),
                    ("A handler updates a search index and also notifies a partner's API. What is wrong with it?", "It is a projection and a reactor in one. Rebuilding the index would notify the partner again for all of history. Split it in two.")]),
        dict(id="projections", nav="Projections", title="Projections and the lag",
             gist="A projection reads events by position, updates a read model and saves its checkpoint in the same transaction. Run the one or two views that must be current inline, and the rest asynchronously. Choose per screen how to handle the lag. Any read model can be thrown away and rebuilt beside the old one.",
             body=projections,
             check=[("Product wants a new column on the dashboard. What is the process?", "Change the projection, deploy it as a new version with a checkpoint at zero, let it replay beside the old table, switch queries when it has caught up."),
                    ("Why can't every projection be inline?", "Each one adds work to every write, and inline only works when the read model is in the same database. Search or a reporting store cannot join that transaction.")]),
        dict(id="versioning", nav="Versioning", title="Versioning: events are forever",
             gist="Old events are never rewritten, so code must keep understanding every shape ever stored. Give each event a version, convert old shapes to the newest with upcasters as they are read, and use a new event type when the meaning changes. Publish separate integration events so your internal ones stay free to change.",
             body=versioning,
             check=[("<code>Withdrew</code> used to mean cash only and now also covers card payments. Version bump or new type?", "A new type, such as <code>CardPaymentMade</code>. The meaning changed, and old <code>Withdrew</code> events must keep meaning cash."),
                    ("Why store the fee amount in the event when it could be looked up?", "Replay must reproduce what was decided then. A lookup would use today's fee and change history.")]),
        dict(id="snapshots", nav="Snapshots", title="Snapshots and closing the books",
             gist="Load time grows with stream length. A snapshot caches the state at some version so a load replays only what came after. Better where the business has natural periods: close the stream with its final balance and open a new one, so no stream grows for ever.",
             body=snapshots,
             check=[("A deploy changes evolve. What must happen to existing snapshots?", "They are ignored or deleted, because they were computed by the old code. A schema number stored with each snapshot makes that automatic."),
                    ("Why is closing the books a business event and a snapshot is not?", "The closing balance is decided and recorded as a fact that statements and auditors use. A snapshot is a private cache that can be deleted at any time without anyone noticing.")]),
        dict(id="deleting", nav="Fix & erase", title="Correcting and erasing",
             gist="Mistakes are fixed by appending a correcting event that says what it reverses and why, never by editing. Personal data is best kept out of events altogether; if it must be in them, encrypt it with a key per person and erase by deleting the key. Decide this before the first personal field is stored.",
             body=deleting,
             check=[("Why not edit the wrong event when nobody has noticed yet?", "Projections and other services have already consumed it. Editing it changes the source without telling them, and the audit trail no longer shows the error or its fix."),
                    ("A customer is erased and a read model is rebuilt next month. What stops their name coming back?", "The name was never in the events (approach one), or its key is gone and the field cannot be decrypted (approach two).")]),
        dict(id="testing", nav="Testing", title="Testing it and running it",
             gist="Rules are tested as given events, when command, then events, with no database. Keep a sample of every event type and version ever stored and replay it in every build. Watch projection lag, version conflicts and stream length, and never repair a read model by hand.",
             body=testing,
             check=[("Version conflicts jump from 0.1 % to 8 % after a release. Likely cause?", "Something now writes to the same streams much more often, or a stream was made coarser, so unrelated changes collide. Look at which streams conflict."),
                    ("The balances table is wrong for one account and the stream is right. Why not just correct the row?", "The projection bug that caused it remains, and the next rebuild will bring the error back. Fix the projection and rebuild.")]),
        dict(id="tools", nav="When & lab", title="When to use it, a lab and the checklist",
             gist="Most of a system needs one model. A few heavy screens need light CQRS. Event sourcing is for the core where history is the business, such as money or stock, and usually for one or two aggregates. The lab adds an overdraft to the account, and the checklist turns the deep dive into review questions.",
             body=tools),
    ],
    sources="Greg Young, “CQRS Documents” (2010) and <i>Versioning in an Event Sourced System</i> (2017). Martin Fowler, “Event Sourcing” (2005) and “CQRS” (2011). Jérémie Chassaing, “Functional Event Sourcing Decider” (2021), for decide and evolve. Oskar Dudycz, event-driven.io, on closing the books, projections and snapshots. Vaughn Vernon, <i>Implementing Domain-Driven Design</i> (2013), chapters on aggregates and event stores.",
)
