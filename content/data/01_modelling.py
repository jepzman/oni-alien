# Vol. 3 · Modelling: Normalization, Surrogate Keys, Soft Delete, History Tables.

# ------------------------------------------------------------------ 01 Normalization
nf_problem = Doodle(760, 230, "Doodle of one wide orders table where the customer's name and email are copied onto every order. Ana changed her email, but only one of her three rows was updated, so the table now holds two different emails for the same person.",
                    "One wide table, the same fact copied three times, and now the copies disagree.")
nf_problem.table(20, 20, "orders (one big table)", ["#1 · Ana · ana@old.com · Lamp", "#2 · Ana · ana@new.com · Desk", "#3 · Ana · ana@old.com · Mug", "#4 · Ben · ben@mail.com · Pen"],
                 w=380, hl=(1,))
nf_problem.arrow(410, 85, 520, 60, color="red")
nf_problem.note(600, 52, "which email is right?", "red")
nf_problem.note(600, 120, "update = touch every copy", "red")
nf_problem.note(600, 150, "delete order #4 = lose Ben", "red")
nf_problem.note(600, 180, "new customer, no order yet?", "red")
nf_problem.note(600, 204, "nowhere to put them", "red")
nf_problem.note(210, 200, "the same fact, written 3 times", "pen")

nf_analogy = Doodle(760, 260, "Doodle of a school office. Instead of every teacher keeping parents' phone numbers in their own class lists, the school keeps one address book. Class lists only say the student number. When a family moves, the office updates one line.",
                    "One address book in the office; class lists point to it by student number.")
for i in range(3):
    nf_analogy.icon("ledger", 30 + i * 70, 40 + (i % 2) * 14, 1.0, fill="paper")
nf_analogy.note(120, 140, "class lists: just", "pen")
nf_analogy.note(120, 164, "student numbers", "pen")
nf_analogy.arrow(250, 80, 430, 100, label="look up #17", lx=340, ly=76)
nf_analogy.icon("book", 440, 50, 2.0, fill="y")
nf_analogy.note(505, 200, "one address book")
nf_analogy.note(505, 230, "family moves → fix one line", "green")

nf_how = Doodle(760, 300, "Normalized design. A customers table holds id, name and email once. An orders table holds id, customer_id and item, and customer_id points to customers. A separate dashed box shows a denormalized copy, orders_summary with customer_name, kept on purpose for a fast report and refreshed from the source.",
                "Each fact lives in one table; others point at it with a foreign key. Copies are made on purpose, and labelled.")
nf_how.table(20, 30, "customers", ["id  (PK)", "name", "email"], w=190, fill="green")
nf_how.table(330, 30, "orders", ["id  (PK)", "customer_id  (FK)", "item", "placed_at"], w=210, fill="y", hl=(1,))
nf_how.arrow(326, 100, 214, 76, label="points to", lx=270, ly=64)
nf_how.box(330, 200, 300, 80, "orders_summary", "blue", sub="customer_name copied on purpose", dash=True, size=18)
nf_how.arrow(330, 240, 120, 150, dash=True, label="refresh from source", lx=110, ly=240, anchor="start")
nf_how.note(680, 120, "1 fact,", "green")
nf_how.note(680, 144, "1 place", "green")

NORMAL = dict(
    slug="normalization",
    kicker="a.k.a. “say it once”",
    tldr="Store each fact in <b>exactly one place</b>, and let other tables <b>point to it</b> with a key. Then a change is one update, and the data <b>can't disagree with itself</b>. When reads get too slow, <b>denormalize on purpose</b>: copy a fact into a read-friendly shape, and keep a clear rule for how the copy stays fresh.",
    chips=[("Family", "data modelling"), ("Origin", "E. F. Codd, 1970–71 (normal forms)"), ("Usual target", "third normal form (3NF)"), ("Pairs with", "indexing, materialized views, star schema")],
    problem="""  <p class="lead">The quickest schema is one wide table that looks like a spreadsheet. It works on day one. Then the same fact, like a customer's email, is copied onto <span class="hl-pink">every row that mentions it</span>, and the copies start to drift.</p>
  <ul>
    <li><b>Update anomaly:</b> Ana changes her email, one row gets updated, two don't.</li>
    <li><b>Delete anomaly:</b> deleting Ben's only order also deletes everything you knew about Ben.</li>
    <li><b>Insert anomaly:</b> you can't store a new customer until they've ordered something.</li>
    <li>Storage and backups grow with every copy.</li>
  </ul>""",
    problem_figs=[nf_problem],
    analogy_side="the school's one address book",
    analogy="""  <p>A school doesn't let every teacher keep parents' phone numbers in their own class list. The office keeps <b>one address book</b>. Class lists just say <b>student #17</b>. When a family moves, the office fixes <b>one line</b>, and every class list is right again.</p>
  <ul>
    <li>The address book is the <b>customers</b> table; student #17 is a <b>foreign key</b>.</li>
    <li>The head teacher still keeps a printed summary for assemblies: a <b>deliberate copy</b>, reprinted each term.</li>
  </ul>""",
    analogy_figs=[nf_analogy],
    map=[("The office address book", "A table that owns one kind of fact (customers)"),
         ("Student #17 on a class list", "A foreign key column (customer_id)"),
         ("A family moves, one line changes", "One UPDATE, no copies to chase"),
         ("The printed assembly summary", "A denormalized copy: a view, cache or summary table"),
         ("Reprinted every term", "A refresh rule for the copy")],
    how_side="split until every fact has one home",
    how="""  <p>Normal forms are a checklist for “one fact, one place”. In practice, aiming for <b>third normal form</b> covers almost everything: every column describes <b>the key, the whole key, and nothing but the key</b>.</p>""",
    how_figs=[nf_how],
    steps=[("List the facts", "Write down the nouns (customer, order, product) and what you know about each."),
           ("1NF: one value per cell", "No comma lists like <code>tags = 'a,b,c'</code>; give repeating things their own rows or table."),
           ("2NF: depend on the whole key", "In a table keyed by (order_id, product_id), the product's name belongs in <code>products</code>, not in the line item."),
           ("3NF: nothing but the key", "If <code>city</code> depends on <code>zip</code>, not on the customer, it moves out (or you accept it, knowingly)."),
           ("Add constraints", "Foreign keys, NOT NULL and UNIQUE make the database enforce the design."),
           ("Denormalize with a reason", "Measure first. If a join is really too slow, copy the column into a read model and write down who refreshes it.")],
    vocab=[("Normal form", "A rule a schema can satisfy (1NF, 2NF, 3NF, BCNF…)."),
           ("Anomaly", "A bug caused by duplicated facts (update, insert, delete)."),
           ("Foreign key", "A column that must match a key in another table."),
           ("Functional dependency", "A → B: knowing A tells you B."),
           ("Denormalization", "Copying a fact on purpose to make reads cheaper."),
           ("Source of truth", "The one table that owns a fact; copies follow it.")],
    code=dict(file="schema.sql", note="PostgreSQL", src="""
-- each fact has one home
CREATE TABLE customers (
  id     bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  name   text NOT NULL,
  email  text NOT NULL UNIQUE
);

CREATE TABLE orders (
  id          bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  customer_id bigint NOT NULL REFERENCES customers (id),
  item        text   NOT NULL,
  placed_at   timestamptz NOT NULL DEFAULT now()
);

-- Ana's new email: one row, everywhere at once
UPDATE customers SET email = 'ana@new.com' WHERE id = 17;

-- the join brings the facts back together for reading
SELECT o.id, c.name, c.email, o.item
FROM orders o JOIN customers c ON c.id = o.customer_id;
"""),
    tools="tools: any relational database (PostgreSQL, MySQL, SQL Server, SQLite). ER diagram tools like dbdiagram.io or DBeaver help you see the shape. Document databases still benefit: embed what's read together, reference what changes on its own.",
    gains=["<b>No contradictions</b>: one fact, one place.",
           "<b>Cheap, safe updates</b>: change one row, not hundreds.",
           "<b>Smaller tables</b> and backups.",
           "<b>Flexible queries</b>: join the pieces any way you like.",
           "<b>The database guards the rules</b> with foreign keys."],
    losses=["<b>More joins</b> for everyday reads.",
            "<b>More tables</b> to understand at first.",
            "<b>Reporting queries get long</b> without views.",
            "<b>Over-normalizing</b> (a table for every attribute) hurts more than it helps."],
    baseline="Each line compares <b>one wide, copy-everything table</b> to the same data <b>normalized to 3NF</b>, with denormalized copies only where measured.",
    ratings=[(4, 3, "More tables and joins, but each one is obvious."),
             (4, 3, "Joins cost a little; indexes and read models win it back."),
             (2, 4, "Updates touch one row instead of every copy."),
             (1, 5, "Foreign keys and single facts stop contradictions."),
             (2, 4, "Smaller rows; hot read paths can be denormalized later."),
             (2, 4, "No repeated text on every row."),
             (3, 5, "Any question is a join away."),
             (3, 4, "Fewer “fix the copies” scripts at 2 a.m."),
             (2, 4, "New attributes go in one obvious place.")],
    pitfalls=[("Normalizing to the extreme", "A table for every attribute, and a 9-way join to show a name.", "stop at 3NF unless a real anomaly pushes you further."),
              ("Copies with no owner", "A denormalized <code>customer_name</code> on orders that nobody updates.", "every copy gets a written refresh rule: trigger, job or event."),
              ("Comma lists in a column", "<code>tags = 'red,blue'</code> can't be indexed, joined or constrained.", "use a join table (or a real array/JSON type with care)."),
              ("No foreign keys “for speed”", "Orphan rows appear and nobody notices for months.", "keep FKs; they're cheap with an index on the referencing column.")],
    use=["Any transactional (OLTP) system: orders, users, bookings, payments.",
         "Data that changes often and must stay consistent.",
         "You don't yet know every question you'll ask of the data."],
    skip=["Analytics warehouses where reads dominate (see star schema, note 15).",
          "Write-once logs and events, which never get updated.",
          "A measured hot path where a deliberate copy is clearly cheaper."],
    related=["<b>Surrogate keys</b>", "<b>Materialized views</b>", "<b>Star schema</b>", "<b>CQRS</b> (Vol. 1)"],
    quiz=[("What are the three classic anomalies?", "Update (copies disagree), insert (can't store a fact without another one) and delete (removing one fact loses another)."),
          ("Summarise 3NF in one sentence.", "Every non-key column depends on the key, the whole key, and nothing but the key."),
          ("When is denormalizing a good idea?", "When a measured read path is too slow, the copied data changes rarely, and there's a clear rule that keeps the copy fresh."),
          ("Why keep foreign keys?", "The database then refuses orphans and dangling references, so integrity doesn't depend on every app being perfect.")],
    remember="Say it <span class=\"hl\">once</span>. Point to it <span class=\"hl\">everywhere</span>. Copy it only <span class=\"hl\">on purpose</span>.",
    sources=["E. F. Codd, “A Relational Model of Data for Large Shared Data Banks” (1970).",
             "William Kent, “A Simple Guide to Five Normal Forms in Relational Database Theory” (1983).",
             "PostgreSQL docs, “Constraints” and “Foreign Keys”.",
             "Martin Kleppmann, <i>Designing Data-Intensive Applications</i>, ch. 2."],
)

# ------------------------------------------------------------------ 02 Surrogate Keys
sk_problem = Doodle(760, 270, "Doodle of a users table keyed by email. Orders, sessions and invoices all store the email to point at the user. When the user changes their email, every referencing row in three tables has to be updated, and a missed one breaks the link.",
                    "Key on a real-world value, and changing that value means rewriting every table that points to it.")
sk_problem.table(20, 70, "users", ["email (PK)", "name"], w=200, fill="y", hl=(0,))
for i, t in enumerate(["orders.user_email", "sessions.user_email", "invoices.user_email"]):
    y = 20 + i * 80
    sk_problem.box(460, y, 260, 56, t, "paper", size=17)
    sk_problem.arrow(454, y + 28, 226, 110, color="red")
sk_problem.note(110, 210, "Ana changes her email…", "red")
sk_problem.note(110, 236, "…3 tables to rewrite", "red")

sk_analogy = Doodle(760, 260, "Doodle of a coat check. You hand over your coat and get a numbered ticket, 042. The ticket number means nothing about you or the coat. If you change your hat or your name, the ticket still finds the coat.",
                    "The coat check gives you ticket 042. It says nothing about you, so it never needs to change.")
sk_analogy.icon("ticket", 60, 70, 2.0, fill="y")
sk_analogy.head(104, 132, "042", size=28)
sk_analogy.note(130, 210, "a meaningless number")
sk_analogy.arrow(220, 120, 430, 120, label="finds", lx=325, ly=106)
sk_analogy.icon("door", 450, 50, 1.6)
sk_analogy.note(540, 90, "coat #042", "pen", anchor="start")
sk_analogy.note(560, 200, "new hat? new name?", "pen")
sk_analogy.note(560, 228, "same ticket", "green")

sk_how = Doodle(760, 280, "Surrogate key design. The users table has id 7 as its primary key and email as a separate unique column. Orders, sessions and invoices store user_id 7. Changing the email touches one row; all references stay valid.",
                "Point at a meaningless id; keep the real-world value as a UNIQUE column you're free to change.")
sk_how.table(20, 60, "users", ["id = 7  (PK)", "email  (UNIQUE)", "name"], w=210, fill="green", hl=(0,))
for i, t in enumerate(["orders.user_id = 7", "sessions.user_id = 7", "invoices.user_id = 7"]):
    y = 20 + i * 80
    sk_how.box(460, y, 260, 56, t, "paper", size=17)
    sk_how.arrow(454, y + 28, 236, 106, color="green")
sk_how.note(125, 225, "new email = 1 UPDATE", "green")
sk_how.note(125, 252, "ids never change", "pen")

SURROGATE = dict(
    slug="surrogate-keys",
    kicker="a.k.a. “the coat-check ticket”",
    tldr="Make every table's primary key a <b>meaningless, stable id</b> (an identity number or a UUID), and keep real-world values like email or SKU as <b>UNIQUE columns</b>. References point at the id, so <b>real-world changes stay one-row updates</b>, and joins stay small and fast.",
    chips=[("Family", "data modelling"), ("Kinds", "identity / sequence, UUID v4, UUID v7, ULID"), ("Opposite", "natural keys"), ("Pairs with", "normalization, sharding")],
    problem="""  <p class="lead">A natural key, like an email, a username or a product code, feels free: it's already unique. But real-world values <span class="hl-pink">change</span>, get <span class="hl-pink">reused</span>, and turn out to be <span class="hl-pink">less unique than promised</span>.</p>
  <ul>
    <li>A user changes their email, and every table that stores it must change too.</li>
    <li>“Unique” national ids get typos, reissues and foreign formats.</li>
    <li>Wide text keys make every index and foreign key bigger.</li>
    <li>Keys show up in URLs and logs, leaking personal data.</li>
  </ul>""",
    problem_figs=[sk_problem],
    analogy_side="the coat-check ticket",
    analogy="""  <p>At a coat check you get <b>ticket 042</b>. The number tells nobody your name, your coat's colour or your phone number. That's the point: you can change your hat, your name or your mind, and <b>042 still finds the coat</b>.</p>
  <ul>
    <li>The ticket is the <b>surrogate key</b>; your name is a <b>natural key</b>.</li>
    <li>The staff still check your name on the list: keep the natural key <b>UNIQUE</b>.</li>
  </ul>""",
    analogy_figs=[sk_analogy],
    map=[("Ticket 042", "<code>id bigint</code> or a UUID primary key"),
         ("Your name on the list", "<code>email text UNIQUE</code>"),
         ("Coat found by ticket", "Foreign keys reference the id"),
         ("You change your name", "One UPDATE to users; references untouched"),
         ("Ticket says nothing about you", "No personal data in keys, URLs or logs")],
    how_side="ids for linking, natural values for rules",
    how="""  <p>Keep <b>two jobs separate</b>: the id is for <b>linking</b> rows; the natural key is a <b>business rule</b> (“no two users share an email”), enforced with UNIQUE.</p>""",
    how_figs=[sk_how],
    steps=[("Add an id to every table", "<code>bigint GENERATED ALWAYS AS IDENTITY</code> for one database, or a UUID if ids are made in many places."),
           ("Keep natural keys UNIQUE", "Email, SKU, slug: still unique, just not the primary key."),
           ("Reference the id", "Foreign keys point at <code>users.id</code>, never at <code>users.email</code>."),
           ("Pick the id type on purpose", "Sequential ids are small and index-friendly but guessable; random UUID v4 is safe to share but scatters inserts; UUID v7 / ULID are time-ordered and shareable."),
           ("Don't expose sequential ids carelessly", "Use a separate public id or slug if “user 1,042” leaks your growth or invites guessing.")],
    vocab=[("Natural key", "A real-world value that identifies a row (email, ISBN)."),
           ("Surrogate key", "An id with no meaning outside the database."),
           ("Identity column", "A column the database fills with 1, 2, 3…"),
           ("UUID", "A 128-bit id that can be generated anywhere."),
           ("UUID v7 / ULID", "Time-ordered unique ids: sortable and index-friendly."),
           ("Composite key", "A primary key made of several columns.")],
    code=dict(file="users.sql", note="PostgreSQL 13+", src="""
CREATE TABLE users (
  id         bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,  -- for linking
  public_id  uuid NOT NULL DEFAULT gen_random_uuid() UNIQUE,  -- safe for URLs
  email      text NOT NULL UNIQUE,                           -- business rule
  name       text NOT NULL
);

CREATE TABLE sessions (
  id       bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  user_id  bigint NOT NULL REFERENCES users (id)
);

-- a new email is one row; sessions don't care
UPDATE users SET email = 'ana@new.com' WHERE id = 7;
"""),
    tools="tools: identity columns (PostgreSQL, SQL Server, Oracle), AUTO_INCREMENT (MySQL), gen_random_uuid(), UUID v7 libraries, ULID. Many ORMs default to a surrogate <code>id</code>.",
    gains=["<b>Stable references</b>: real-world changes are one-row updates.",
           "<b>Small, fast joins</b> on 8-byte integers.",
           "<b>Uniform design</b>: every table has an <code>id</code>.",
           "<b>No personal data</b> in keys and URLs (with a public id)."],
    losses=["<b>An extra column</b> and an extra unique index.",
            "<b>Easy to forget the natural UNIQUE</b>, and then duplicates creep in.",
            "<b>Ids mean nothing</b> when you read raw data.",
            "<b>Random UUIDs scatter inserts</b> across the index."],
    baseline="Each line compares tables keyed by <b>natural values</b> (email, code) to tables with a <b>surrogate id</b> plus a UNIQUE natural key.",
    ratings=[(4, 4, "One more column, but one rule for every table."),
             (3, 4, "Integer joins and smaller indexes."),
             (3, 3, "One extra index to maintain per table."),
             (3, 4, "References never break when values change; keep the UNIQUE."),
             (3, 4, "Small keys; UUIDs help when ids come from many nodes."),
             (3, 4, "8 bytes instead of long text in every FK."),
             (3, 3, "Neutral."),
             (2, 4, "No mass rewrites when a code or email changes."),
             (2, 5, "Business rules about identity can change freely.")],
    pitfalls=[("Dropping the natural UNIQUE", "Two rows for <code>ana@mail.com</code> because only the id is unique.", "keep UNIQUE on the business identifier."),
              ("Random UUID v4 as a clustered key", "Inserts land all over the index, causing page splits and cache misses.", "use bigint, UUID v7 or ULID when insert order matters."),
              ("Sequential ids in public URLs", "<code>/invoice/1043</code> invites guessing the next one.", "add a random public id and check permissions anyway."),
              ("Meaning sneaks into the id", "“Ids starting with 9 are test users.”", "use a real column (<code>is_test</code>); ids stay meaningless.")],
    use=["Almost every OLTP table.",
         "Natural keys that can change, be reused or contain personal data.",
         "Ids generated in many services or offline clients (UUID / ULID)."],
    skip=["Join tables, where (user_id, group_id) is a fine composite key.",
          "Truly immutable codes like ISO country codes.",
          "Small lookup tables where the code is the meaning (<code>status = 'paid'</code>)."],
    related=["<b>Normalization</b>", "<b>Multitenancy</b>", "<b>Sharding</b> (Vol. 1)", "<b>Idempotent consumer</b> (Vol. 1)"],
    quiz=[("Why not use email as the primary key?", "Emails change and are personal data; every foreign key would need rewriting and would leak the email."),
          ("If the id is the PK, how do you stop duplicate users?", "Keep a UNIQUE constraint on email (often case-insensitive)."),
          ("Why are random UUID v4 keys slow for inserts?", "Each new key lands at a random spot in the B-tree, causing page splits and poor cache use; time-ordered ids append at the end."),
          ("When is a composite natural key fine?", "In join tables like (user_id, role_id), where the pair is the identity and never changes.")],
    remember="The <span class=\"hl\">ticket</span> finds the coat. Your <span class=\"hl\">name</span> is checked, not used as the hook.",
    sources=["PostgreSQL docs, “Identity Columns” and “UUID Type”.",
             "RFC 9562, “Universally Unique IDentifiers (UUIDs)” (UUID v7).",
             "Joe Celko, <i>SQL for Smarties</i>, chapter on keys.",
             "Buildkite engineering, “Goodbye to sequential integers, hello UUIDv7”."],
)

# ------------------------------------------------------------------ 03 Soft Delete
sd_problem = Doodle(760, 260, "Doodle of a support agent getting a call: I deleted my project by accident, can you bring it back? The DELETE statement already removed the row, the comments and the files. The only copy is in last night's backup, which would also roll back everyone else's work.",
                    "DELETE is forever. The only way back is a full restore that rewinds everyone.")
sd_problem.icon("phone", 30, 40, 1.6)
sd_problem.note(150, 50, "“I deleted my project", "red", anchor="start")
sd_problem.note(150, 76, "by accident! help!”", "red", anchor="start")
sd_problem.table(380, 30, "projects", ["#41 · Garden", "#42 · Thesis", "#43 · Taxes"], w=200, strike=(1,))
sd_problem.icon("bin", 640, 60, 1.4, fill="pink")
sd_problem.arrow(590, 98, 636, 98, color="red")
sd_problem.note(380, 200, "only copy: last night's backup", "red", anchor="start")
sd_problem.note(380, 226, "restore = rewind everyone", "red", anchor="start")

sd_analogy = Doodle(760, 250, "Doodle of a desktop recycle bin. Throwing a file away moves it to the bin, where it can be restored. Emptying the bin after 30 days deletes it for real.",
                    "The recycle bin: “deleted” files can come back, until the bin is emptied.")
sd_analogy.icon("frame", 40, 60, 1.6)
sd_analogy.note(90, 180, "file")
sd_analogy.arrow(160, 100, 320, 100, label="delete", lx=240, ly=86)
sd_analogy.icon("bin", 340, 50, 1.8, fill="y")
sd_analogy.note(395, 190, "in the bin (restorable)", "green")
sd_analogy.arrow(470, 100, 620, 100, dash=True, label="after 30 days", lx=545, ly=86)
sd_analogy.icon("cross", 640, 70, 1.0, color="red")
sd_analogy.note(670, 190, "gone for real", "red")

sd_how = Doodle(760, 290, "Soft delete flow. Deleting sets deleted_at to now instead of removing the row. A view called active_projects filters deleted_at is null, and the app reads from that view. A restore sets deleted_at back to null. A nightly purge job hard-deletes rows deleted more than 30 days ago.",
                "Delete = stamp a date. Reads go through a filter. A purge job really deletes old rows.")
sd_how.table(20, 40, "projects", ["#41 · Garden · null", "#42 · Thesis · 12 Nov", "#43 · Taxes · null"], w=250, soft=(1,))
sd_how.note(145, 30, "deleted_at", "pen")
sd_how.arrow(276, 100, 380, 70, label="WHERE deleted_at IS NULL", lx=300, ly=36, anchor="start")
sd_how.box(386, 46, 200, 60, "active_projects", "green", size=18)
sd_how.arrow(592, 76, 660, 76)
sd_how.icon("screen", 666, 50, 1.0)
sd_how.box(40, 200, 200, 54, "restore: set null", "y", size=17)
sd_how.box(300, 200, 260, 54, "purge after 30 days", "pink", stroke="red", size=17)
sd_how.arrow(140, 196, 140, 146, dash=True)
sd_how.arrow(430, 196, 260, 120, dash=True, color="red")

SOFT = dict(
    slug="soft-delete",
    kicker="a.k.a. “the recycle bin”",
    tldr="Instead of <code>DELETE</code>, set <b><code>deleted_at = now()</code></b>. Normal reads <b>filter deleted rows out</b> (ideally through a view or a default scope), a <b>restore</b> clears the stamp, and a <b>purge job</b> hard-deletes rows once the undo window has passed, which also keeps you honest about privacy laws.",
    chips=[("Family", "data lifecycle"), ("Column", "deleted_at timestamptz"), ("Variants", "archive table, status column"), ("Pairs with", "history tables, partial indexes")],
    problem="""  <p class="lead">Hard deletes are <span class="hl-pink">instant and permanent</span>. Users make mistakes, support needs to see what happened, and other rows still point at the one you removed.</p>
  <ul>
    <li>“I deleted it by accident” has no answer except restoring a backup.</li>
    <li>Foreign keys either block the delete or cascade and wipe related data too.</li>
    <li>Reports for last month change because their rows vanished.</li>
  </ul>""",
    problem_figs=[sd_problem],
    analogy_side="the recycle bin",
    analogy="""  <p>On your computer, “delete” moves a file to the <b>recycle bin</b>. It's out of sight, but one click brings it back. The bin is <b>emptied after 30 days</b>, and only then is the file truly gone.</p>
  <ul>
    <li>Moving to the bin is setting <b>deleted_at</b>.</li>
    <li>The desktop not showing binned files is your <b>filtered view</b>.</li>
    <li>Emptying the bin is the <b>purge job</b>, and you need one.</li>
  </ul>""",
    analogy_figs=[sd_analogy],
    map=[("Move to the bin", "<code>UPDATE … SET deleted_at = now()</code>"),
         ("The desktop hides binned files", "A view or default scope: <code>deleted_at IS NULL</code>"),
         ("Restore from the bin", "<code>SET deleted_at = NULL</code>"),
         ("Bin emptied after 30 days", "A scheduled purge with a real DELETE"),
         ("“Who deleted this?”", "An optional <code>deleted_by</code> column")],
    how_side="a stamp, a filter and a purge",
    how="""  <p>Soft delete is three small pieces. The column is easy; the <b>filter everywhere</b> and the <b>purge</b> are what make it safe.</p>""",
    how_figs=[sd_how],
    steps=[("Add the column", "<code>deleted_at timestamptz NULL</code> (a timestamp tells you <i>when</i>, which a boolean can't)."),
           ("Read through a filter", "A view like <code>active_projects</code>, a row-level policy, or an ORM default scope, so nobody forgets the WHERE."),
           ("Fix uniqueness", "Use a <b>partial unique index</b> so a deleted slug can be reused: <code>UNIQUE (slug) WHERE deleted_at IS NULL</code>."),
           ("Decide what cascades", "Soft-deleting a project may soft-delete its tasks too; write that rule down."),
           ("Purge on a schedule", "Hard-delete rows older than the undo window, and anything a user asked to be erased.")],
    vocab=[("Hard delete", "Physically removing the row with DELETE."),
           ("Soft delete", "Marking a row deleted but keeping it."),
           ("Tombstone", "A marker that says “this was deleted”."),
           ("Partial index", "An index over only the rows that match a WHERE."),
           ("Purge", "The real delete that happens later."),
           ("Right to erasure", "GDPR rule: personal data must really go when asked.")],
    code=dict(file="soft_delete.sql", note="PostgreSQL", src="""
ALTER TABLE projects ADD COLUMN deleted_at timestamptz;

-- slugs only need to be unique among live rows
CREATE UNIQUE INDEX projects_slug_live
  ON projects (slug) WHERE deleted_at IS NULL;

CREATE VIEW active_projects AS
  SELECT * FROM projects WHERE deleted_at IS NULL;

-- "delete" and "undo"
UPDATE projects SET deleted_at = now() WHERE id = 42;
UPDATE projects SET deleted_at = NULL  WHERE id = 42;

-- nightly purge: the bin really gets emptied
DELETE FROM projects WHERE deleted_at < now() - interval '30 days';
"""),
    tools="tools: Rails <code>discard</code>/<code>paranoia</code>, Laravel <code>SoftDeletes</code>, Django <code>django-safedelete</code>, Prisma middleware, Hibernate <code>@SoftDelete</code>. PostgreSQL row-level security can hide deleted rows for every query.",
    gains=["<b>Undo</b> for users and support.",
           "<b>Related rows stay valid</b>; no surprise cascades.",
           "<b>Audit and reports</b> keep their history.",
           "<b>Cheap deletes</b>: one small UPDATE."],
    losses=["<b>Every query must filter</b>, or deleted data leaks.",
            "<b>Unique constraints get tricky</b> (partial indexes needed).",
            "<b>Tables keep growing</b> until you purge.",
            "<b>Privacy risk</b>: “deleted” personal data that isn't."],
    baseline="Each line compares <b>hard DELETE</b> to <b>soft delete</b> with a filtered view, a partial unique index and a purge job.",
    ratings=[(5, 3, "Every query needs to remember the filter."),
             (4, 3, "Dead rows in tables and indexes; partial indexes help."),
             (3, 4, "An UPDATE is cheaper than a cascading DELETE."),
             (3, 4, "References stay valid; but forgotten filters show ghosts."),
             (4, 3, "Tables grow until the purge runs."),
             (4, 3, "Deleted rows still take space for a while."),
             (3, 4, "You can still ask “what was deleted last week?”"),
             (2, 4, "Undo without restoring a backup."),
             (3, 3, "Neutral: the filter must follow every new query.")],
    pitfalls=[("Forgetting the filter", "A new report counts deleted orders as real.", "read through a view, a default scope or row-level security."),
              ("A boolean is_deleted", "You know it's deleted, not when, so you can't purge after 30 days.", "use <code>deleted_at</code> (and maybe <code>deleted_by</code>)."),
              ("Never purging", "“Deleted” personal data lives forever and breaks GDPR.", "schedule a purge and honour erasure requests with a real DELETE."),
              ("Plain UNIQUE constraints", "A user can't recreate the slug they deleted yesterday.", "partial unique index on live rows only.")],
    use=["Users can delete things they may want back (projects, posts, files).",
         "Rows are referenced by history you need to keep (orders, invoices).",
         "Support needs to see what was deleted and when."],
    skip=["High-churn data like sessions, carts or caches.",
          "Personal data that must be erased on request (purge for real).",
          "You need full history anyway, so use history tables instead."],
    related=["<b>History tables</b>", "<b>Indexing</b> (partial indexes)", "<b>Event sourcing</b> (Vol. 1)", "<b>Multitenancy</b>"],
    quiz=[("Why is deleted_at better than is_deleted?", "It records when the row was deleted, which you need for undo windows, purge jobs and audits."),
          ("How do you stop deleted rows from appearing in reads?", "Read through a filtered view, an ORM default scope or a row-level security policy."),
          ("What breaks with a normal UNIQUE (slug)?", "Deleted rows still hold the slug, so it can't be reused; use a partial unique index WHERE deleted_at IS NULL."),
          ("Does soft delete satisfy “delete my data”?", "No. Personal data must be really erased (or anonymised), so a purge with a hard DELETE is still needed.")],
    remember="Delete means <span class=\"hl\">into the bin</span>. Someone must still <span class=\"hl\">empty the bin</span>.",
    sources=["Brandur Leach, “Soft Deletion Probably Isn't Worth It” (blog post).",
             "PostgreSQL docs, “Partial Indexes” and “Row Security Policies”.",
             "Laravel docs, “Eloquent: Soft Deleting”.",
             "GDPR Article 17, “Right to erasure”."],
)

# ------------------------------------------------------------------ 04 History Tables
ht_problem = Doodle(760, 260, "Doodle of a product price row being overwritten: 20 euros becomes 25 euros. A customer complains they were charged 20 last Tuesday, but the table only knows the current price, so nobody can check who changed it or what it was.",
                    "UPDATE overwrites the past. “What was it last Tuesday?” has no answer.")
ht_problem.table(30, 40, "products", ["Lamp · €20"], w=200, strike=(0,))
ht_problem.arrow(236, 76, 330, 76, color="red", label="UPDATE", lx=283, ly=62)
ht_problem.table(340, 40, "products", ["Lamp · €25"], w=200, fill="green")
ht_problem.note(380, 160, "“I paid €20 on Tuesday!”", "red")
ht_problem.note(380, 190, "who changed it? when? from what?", "red")
ht_problem.note(380, 220, "the table only knows “now”", "pen")

ht_analogy = Doodle(760, 260, "Doodle of a medical chart. The doctor never erases old notes; each visit adds a new dated line with the new reading. To know a patient's blood pressure in March, you read the March line.",
                    "A medical chart: you never erase, you add a dated line.")
ht_analogy.icon("receipt", 40, 40, 2.4)
for i, (d, v) in enumerate([("3 Mar", "120/80"), ("9 Jun", "130/85"), ("1 Nov", "125/82")]):
    ht_analogy.note(250, 70 + i * 50, f"{d} · {v}", "pen", anchor="start")
ht_analogy.note(250, 230, "nothing erased, only added", "green", anchor="start")
ht_analogy.arrow(560, 120, 440, 120, label="“what was it in June?”", lx=620, ly=112)

ht_how = Doodle(760, 290, "History table design. The products table holds the current row. A trigger copies the old version into products_history with valid_from, valid_to and changed_by on every update or delete. Querying history for a date finds the version whose range contains it.",
                "The main table holds “now”; a trigger files every old version, with who and when.")
ht_how.table(20, 40, "products", ["id · name · price", "7 · Lamp · €25"], w=220, fill="green", hl=(1,))
ht_how.arrow(246, 90, 360, 90, label="trigger on UPDATE / DELETE", lx=300, ly=150)
ht_how.table(366, 20, "products_history", ["7 · €18 · Jan–Mar · ana", "7 · €20 · Mar–Nov · ben", "7 · €25 · Nov– · now"], w=360, fill="y", hl=(1,))
ht_how.note(546, 160, "valid_from · valid_to · changed_by", "pen")
ht_how.note(380, 230, "price on 4 Nov → WHERE '2026-11-04' within valid range", "green")

HISTORY = dict(
    slug="history-tables",
    kicker="a.k.a. “the medical chart”",
    tldr="Keep the main table for <b>the current state</b>, and file every <b>old version</b> of a row in a <b>history table</b> with <code>valid_from</code>, <code>valid_to</code> and <b>who changed it</b>, usually via a trigger or built-in <b>system-versioned (temporal) tables</b>. Then “what was it on that day, and who changed it?” is a query, not an argument.",
    chips=[("Family", "data lifecycle / auditing"), ("Standard", "SQL:2011 system-versioned tables"), ("Built in", "SQL Server, MariaDB, Db2, Oracle Flashback"), ("Pairs with", "soft delete, change data capture")],
    problem="""  <p class="lead">An <code>UPDATE</code> <span class="hl-pink">overwrites the past</span>. That's fine for a typo, but terrible for prices, permissions, salaries or contracts, where someone will eventually ask what the value <i>was</i>.</p>
  <ul>
    <li>A customer disputes a charge, and you can't prove last week's price.</li>
    <li>An admin role appeared on an account, and nobody knows who granted it.</li>
    <li>Reports for last quarter change every time the data is corrected.</li>
  </ul>""",
    problem_figs=[ht_problem],
    analogy_side="the medical chart",
    analogy="""  <p>A doctor never rubs out an old reading. Each visit adds a <b>new dated line</b>. The chart shows today's numbers at the bottom, and the whole story above it.</p>
  <ul>
    <li>The bottom line is the <b>current row</b>.</li>
    <li>Every line above is a <b>history row</b> with a date range.</li>
    <li>The doctor's signature is <b>changed_by</b>.</li>
  </ul>""",
    analogy_figs=[ht_analogy],
    map=[("Today's reading", "The current row in <code>products</code>"),
         ("Older dated lines", "Rows in <code>products_history</code>"),
         ("“Valid from 3 Mar to 9 Jun”", "<code>valid_from</code> / <code>valid_to</code> (a time range)"),
         ("The doctor's signature", "<code>changed_by</code>"),
         ("Never erase, only add", "History is insert-only")],
    how_side="current table + versioned copies",
    how="""  <p>Each change closes the old version's time range and opens a new one. Then <b>any point in time</b> maps to exactly one version.</p>""",
    how_figs=[ht_how],
    steps=[("Create the history table", "Same columns as the main table, plus <code>valid_from</code>, <code>valid_to</code>, <code>changed_by</code> and the operation."),
           ("Capture every change", "A trigger on UPDATE and DELETE copies the old row; or use built-in system versioning."),
           ("Record who", "Pass the app user to the database (for example <code>SET LOCAL app.user = 'ana'</code>) so the trigger can store it."),
           ("Query by time", "<code>WHERE valid_from &lt;= :t AND :t &lt; valid_to</code>, or <code>FOR SYSTEM_TIME AS OF</code> where supported."),
           ("Plan retention", "History grows forever; partition it by month and archive or drop what you no longer need.")],
    vocab=[("Audit trail", "A record of who changed what and when."),
           ("System time", "When the database stored the change."),
           ("Valid (business) time", "When the fact was true in the real world."),
           ("Bitemporal", "Tracking both system time and valid time."),
           ("Temporal table", "A table the database versions for you."),
           ("Insert-only", "Rows are added, never updated or deleted.")],
    code=dict(file="history.sql", note="PostgreSQL trigger", src="""
CREATE TABLE products_history (
  LIKE products,
  valid_from  timestamptz NOT NULL,
  valid_to    timestamptz NOT NULL DEFAULT now(),
  changed_by  text,
  op          text NOT NULL
);

CREATE FUNCTION keep_history() RETURNS trigger AS $$
BEGIN
  INSERT INTO products_history
  SELECT OLD.*, OLD.updated_at, now(),            -- products has updated_at
         current_setting('app.user', true), TG_OP;
  RETURN NULL;
END $$ LANGUAGE plpgsql;

CREATE TRIGGER products_history AFTER UPDATE OR DELETE ON products
  FOR EACH ROW EXECUTE FUNCTION keep_history();

-- what did the lamp cost on 4 Nov?
SELECT price FROM products_history
WHERE id = 7 AND valid_from <= '2026-11-04' AND '2026-11-04' < valid_to;
"""),
    tools="tools: SQL Server and MariaDB system-versioned tables, Oracle Flashback, PostgreSQL <code>temporal_tables</code> extension or triggers, Django <code>simple-history</code>, Rails <code>paper_trail</code>, Hibernate Envers. Change data capture (note 11) can feed a history store too.",
    gains=["<b>Answer “what was it then?”</b> for any date.",
           "<b>Who changed what</b>: real audit trails.",
           "<b>Reproducible reports</b> for past periods.",
           "<b>Undo</b> by copying an old version back."],
    losses=["<b>Every write does extra work</b> (the trigger).",
            "<b>Storage grows</b> with every change.",
            "<b>Schema changes</b> must be applied to both tables.",
            "<b>Time-range queries</b> are trickier to write."],
    baseline="Each line compares a table that <b>overwrites in place</b> to the same table with a <b>trigger-filled history table</b>.",
    ratings=[(4, 3, "A trigger and a second table to understand."),
             (4, 4, "Current reads are untouched."),
             (4, 3, "Each update also writes a history row."),
             (3, 5, "Every change is recorded with who and when."),
             (4, 3, "History grows with write volume; partition it."),
             (4, 2, "Every version is kept."),
             (2, 5, "Time-travel questions become plain SQL."),
             (3, 4, "Disputes and incidents are easy to investigate."),
             (3, 3, "Schema changes touch two tables.")],
    pitfalls=[("History in the app only", "Some code paths (scripts, admin SQL) skip it.", "capture in the database (trigger or system versioning)."),
              ("No “who”", "You know it changed, but not by whom.", "pass the app user into the session and store it."),
              ("Forgetting schema changes", "A new column exists in products but not in history, so the trigger fails.", "migrate both tables together; test the trigger in CI."),
              ("Unbounded growth", "A hot table makes history 50× bigger than the data.", "partition history by month; archive old partitions.")],
    use=["Prices, permissions, contracts, salaries, medical or financial data.",
         "Auditors or regulators ask “who changed this?”",
         "You need reports “as of” a past date."],
    skip=["Write-heavy, low-value data (sessions, counters, caches).",
          "Data that's already insert-only (events, logs).",
          "You're already using event sourcing for that data."],
    related=["<b>Soft delete</b>", "<b>Change data capture</b>", "<b>Table partitioning</b>", "<b>Event sourcing</b> (Vol. 1)"],
    quiz=[("Why put history capture in a trigger rather than the app?", "Every write path, including scripts and admin SQL, then records history; the app can't forget."),
          ("How do you find the value at time t?", "Pick the version where valid_from ≤ t < valid_to (or use FOR SYSTEM_TIME AS OF)."),
          ("What's the difference between system time and valid time?", "System time is when the database recorded it; valid time is when it was true in the real world. Tracking both is bitemporal."),
          ("How do you stop history from growing forever?", "Partition it by time and archive or drop partitions past the retention period.")],
    remember="Never <span class=\"hl\">rub out</span> the chart. Add a <span class=\"hl\">dated line</span>, and sign it.",
    sources=["SQL:2011 standard, temporal features (Kulkarni &amp; Michels, SIGMOD Record 2012).",
             "Microsoft docs, “Temporal tables” (SQL Server).",
             "Richard Snodgrass, <i>Developing Time-Oriented Database Applications in SQL</i>.",
             "Martin Fowler, “Temporal Patterns” and “Bitemporal History”."],
)

NOTES = [NORMAL, SURROGATE, SOFT, HISTORY]
