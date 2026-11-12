# Vol. 5 · Untrusted input: Validate at the Boundary, Parameterized Queries, Output Encoding & CSP, CSRF Protection.

# ------------------------------------------------------------------ 08 Validate at the Boundary
iv_problem = Doodle(760, 260, "Doodle of a request body passed straight into the app. It contains a negative quantity, a role field set to admin, a four megabyte name and a date of the year 99999. Each layer assumes another layer checked it, so the bad values reach the database and the billing code.",
                    "Raw input flows straight in. Every layer assumes someone else checked it.")
iv_problem.box(20, 30, 260, 190, None, "pink", stroke="red")
for i, t in enumerate(["qty: -5", "role: \"admin\"", "name: (4 MB)", "date: 99999-01-01", "price: \"free\""]):
    iv_problem.text(36, 62 + i * 34, t, "t t-red", anchor="start", size=16)
iv_problem.arrow(286, 125, 400, 125, color="red")
for i, t in enumerate(["handler", "service", "database"]):
    iv_problem.box(406, 30 + i * 70, 160, 54, t, "paper", size=17)
iv_problem.note(660, 60, "“the handler", "red")
iv_problem.note(660, 86, "checked it”", "red")
iv_problem.note(660, 140, "“the DB will", "red")
iv_problem.note(660, 166, "reject it”", "red")

iv_analogy = Doodle(760, 250, "Doodle of an airport security checkpoint with a strict list of what's allowed. Every bag is checked once, at the entrance, against the list. Anything not on the list is refused. Inside the terminal, shops and gates can trust that bags were checked.",
                    "Airport security: one checkpoint, a strict allowed list, everything else refused.")
iv_analogy.icon("guard", 300, 40, 1.8, fill="y")
for i in range(3):
    iv_analogy.icon("parcel", 40 + i * 70, 90, 0.9)
iv_analogy.arrow(250, 120, 290, 120)
iv_analogy.arrow(420, 100, 540, 70, color="green", label="on the list ✓", lx=480, ly=60)
iv_analogy.arrow(420, 140, 540, 190, color="red", label="not on the list ✗", lx=480, ly=210)
iv_analogy.note(640, 70, "terminal", "green")
iv_analogy.note(640, 190, "refused", "red")

iv_how = Doodle(760, 290, "Validation at the boundary. Every request passes through a schema at the API edge: quantity must be an integer from one to ninety-nine, name a string of at most one hundred characters, email a valid email, and unknown fields like role are stripped. Invalid input gets a 400 error with field messages. Inside, the code receives a typed, trusted object.",
                "One strict schema at the edge: allow-list types, ranges and lengths; drop unknown fields; reject the rest.")
iv_how.box(20, 100, 140, 70, "request", "pink", size=18)
iv_how.arrow(166, 135, 236, 135)
iv_how.box(242, 30, 260, 210, None, "y")
iv_how.head(372, 60, "schema (allow-list)", size=18)
for i, t in enumerate(["qty: int 1–99", "name: string ≤ 100", "email: email", "date: 2020–2030", "unknown fields: dropped"]):
    iv_how.text(256, 96 + i * 30, t, "t", anchor="start", size=16)
iv_how.arrow(508, 100, 580, 70, color="green", label="typed object", lx=600, ly=56, anchor="start")
iv_how.arrow(508, 180, 580, 210, color="red", label="400 + field errors", lx=600, ly=230, anchor="start")

VALIDATE = dict(
    slug="input-validation",
    kicker="a.k.a. “airport security”",
    tldr="Treat every input from outside (bodies, query strings, headers, files, webhooks) as <b>hostile</b>. Check it <b>once, at the boundary</b>, against an <b>allow-list schema</b>: types, ranges, lengths, formats, and <b>drop unknown fields</b>. Reject anything else with a clear error. Inside, code works with <b>typed, trusted data</b>. Validation is your first filter, not your only defence.",
    chips=[("Family", "input handling"), ("Approach", "allow-list (positive) validation"), ("Tools", "Zod, Valibot, JSON Schema, Pydantic"), ("Pairs with", "parameterized queries, output encoding")],
    problem="""  <p class="lead">Without a clear checkpoint, every layer <span class="hl-pink">assumes another one checked</span>. Bad input slips through and breaks logic, data and sometimes security.</p>
  <ul>
    <li>A negative quantity gives the customer a refund.</li>
    <li>An extra <code>role: "admin"</code> field is copied straight into the user (mass assignment).</li>
    <li>A 4 MB “name” fills logs and slows the service.</li>
  </ul>""",
    problem_figs=[iv_problem],
    analogy_side="airport security",
    analogy="""  <p>An airport has <b>one checkpoint</b> with a <b>strict list</b> of what's allowed. Every bag is checked <b>at the entrance</b>; anything not on the list is refused. Inside, gates and shops can rely on the fact that bags were checked.</p>
  <ul>
    <li>The checkpoint is your <b>API boundary</b>.</li>
    <li>The list of allowed items is an <b>allow-list schema</b>.</li>
    <li>“Not on the list = refused” beats “on the banned list = refused”.</li>
  </ul>""",
    analogy_figs=[iv_analogy],
    map=[("The checkpoint", "Validation at the API edge"),
         ("The allowed-items list", "A schema of types, ranges, lengths, formats"),
         ("Unlisted item confiscated", "Unknown fields stripped"),
         ("Refused at the gate", "HTTP 400 with field errors"),
         ("Terminal trusts checked bags", "Inner code receives typed, valid objects")],
    how_side="one schema, at the edge",
    how="""  <p>Validate <b>syntax and shape</b> at the edge (is it a number 1–99?), and <b>business rules</b> in the domain (is this product in stock?). Both are needed; neither replaces safe output and queries.</p>""",
    how_figs=[iv_how],
    steps=[("Define a schema per endpoint", "Types, min/max, lengths, enums, formats, for body, query, params and headers."),
           ("Allow-list, don't block-list", "Describe what's valid; don't try to list every bad pattern."),
           ("Strip unknown fields", "Prevents mass assignment (<code>role</code>, <code>isAdmin</code>)."),
           ("Limit sizes", "Request body limits, array lengths, string lengths, file types and sizes."),
           ("Fail clearly", "400 with field errors; don't echo raw input back unescaped."),
           ("Validate webhooks and files too", "Check signatures, content types (by content, not extension) and sizes.")],
    vocab=[("Allow-list", "Only listed values/shapes are accepted."),
           ("Block-list", "Listed bad values are rejected; easy to bypass."),
           ("Mass assignment", "Copying request fields straight onto objects."),
           ("Schema", "A machine-checkable description of valid input."),
           ("Canonicalisation", "Normalising input (unicode, paths) before checks."),
           ("Trust boundary", "Where data crosses from untrusted to trusted.")],
    code=dict(file="orders.route.ts", note="Zod + Express", src="""
import { z } from "zod";

const CreateOrder = z.object({
  productId: z.string().uuid(),
  qty: z.number().int().min(1).max(99),
  note: z.string().trim().max(500).optional(),
  deliverOn: z.coerce.date().min(new Date("2020-01-01")).max(new Date("2030-12-31")),
}).strip();                                   // unknown fields (role, price…) are dropped

app.post("/orders", express.json({ limit: "10kb" }), async (req, res) => {
  const parsed = CreateOrder.safeParse(req.body);
  if (!parsed.success) {
    return res.status(400).json({ errors: parsed.error.flatten().fieldErrors });
  }
  const order = await orders.create(req.user.id, parsed.data);   // typed and trusted
  res.status(201).json(order);
});
"""),
    tools="tools: Zod, Valibot, Yup, Ajv / JSON Schema, OpenAPI request validators, Pydantic (Python), Bean Validation (Java), FluentValidation (.NET), file-type sniffing libraries.",
    gains=["<b>Bad data stopped at the door</b>.",
           "<b>No mass assignment</b>.",
           "<b>Typed data inside</b>: simpler code.",
           "<b>Clear errors</b> for honest clients."],
    losses=["<b>Schemas to write</b> and keep in sync.",
            "<b>False rejections</b> when rules are too strict (names, addresses).",
            "<b>Not a full defence</b>: still need safe queries and output."],
    baseline="Each line compares <b>ad-hoc checks scattered through the code</b> to <b>one strict allow-list schema per endpoint</b>.",
    ratings=[(2, 4, "One obvious place for input rules."),
             (3, 3, "Good errors help; over-strict rules annoy."),
             (3, 3, "Neutral."),
             (2, 4, "Impossible values and extra fields are blocked."),
             (2, 4, "Size limits stop oversized payload abuse."),
             (2, 3, "Narrows what an attacker can send."),
             (3, 3, "Rejections can be logged and counted."),
             (3, 3, "Schemas cost a little; bugs cost more."),
             (2, 5, "Typed objects after the edge.")],
    pitfalls=[("Block-lists", "Filtering out “&lt;script&gt;” and calling it safe.", "allow-list valid shapes; encode output separately."),
              ("Client-side validation only", "The browser checks; the API trusts.", "always validate on the server."),
              ("Passing req.body through", "<code>User.update(req.body)</code>.", "pick known fields via the schema."),
              ("Over-strict names and addresses", "Rejecting “O'Brien” or non-Latin names.", "validate length and type; don't guess what a name looks like.")],
    use=["Every API endpoint, form handler, webhook and message consumer.",
         "File uploads (type, size, content).",
         "Config and environment variables at start-up."],
    skip=["Never skip it; just keep business-rule checks in the domain layer."],
    related=["<b>Parameterized queries</b>", "<b>Output encoding &amp; CSP</b>", "<b>Defence in depth</b>", "<b>API gateway</b> (Vol. 1)"],
    quiz=[("Why prefer allow-lists over block-lists?", "It's impossible to list every bad input; describing valid input rejects everything else by default."),
          ("What is mass assignment?", "Copying request fields directly onto objects, letting attackers set fields like role or isAdmin."),
          ("Is client-side validation enough?", "No. It's for user experience; the server must validate everything."),
          ("Does validation make SQL injection impossible?", "No. Use parameterized queries as well; validation is one layer.")],
    remember="One <span class=\"hl\">checkpoint</span>, a strict <span class=\"hl\">list</span>, and everything else <span class=\"hl\">refused</span>.",
    sources=["OWASP, “Input Validation Cheat Sheet”.",
             "OWASP, “Mass Assignment Cheat Sheet”.",
             "OWASP ASVS v4, V5 “Validation, Sanitization and Encoding”.",
             "Zod documentation (zod.dev)."],
)

# ------------------------------------------------------------------ 09 Parameterized Queries
pq_problem = Doodle(760, 250, "Doodle of a SQL query built by gluing strings: select star from users where email equals quote plus the input plus quote. When the input contains a quote character, the input stops being data and becomes part of the SQL command, changing what the query does.",
                    "Gluing input into SQL: a single quote turns data into code.")
pq_problem.box(20, 40, 720, 60, None, "paper", rx=4)
pq_problem.text(36, 78, "\"SELECT * FROM users WHERE email = '\" + input + \"'\"", "t", anchor="start", size=17)
pq_problem.arrow(380, 106, 380, 150, color="red")
pq_problem.box(150, 154, 460, 54, "input with a ' → becomes SQL", "pink", stroke="red", size=18)
pq_problem.note(380, 236, "data and code mixed in one string", "red")

pq_analogy = Doodle(760, 250, "Doodle of a printed bank form with labelled boxes: pay to, amount, date. Whatever you write in the amount box is read as an amount, even if you write instructions there. The form's wording can't be changed by what you write in the boxes.",
                    "A printed form: whatever you write in the box is read as a value, never as new instructions.")
pq_analogy.box(160, 30, 440, 190, None, "paper", rx=4)
pq_analogy.head(380, 62, "TRANSFER FORM", size=18)
for i, t in enumerate(["pay to:", "amount:", "date:"]):
    pq_analogy.text(180, 106 + i * 40, t, "t-head", anchor="start", size=16)
    pq_analogy.box(290, 84 + i * 40, 290, 30, None, "y", rx=2)
pq_analogy.text(300, 145, "€20 and also empty the account", "t t-red", anchor="start", size=14)
pq_analogy.note(380, 244, "still just a strange amount, not an order", "green")

pq_how = Doodle(760, 290, "Parameterized query. The application sends the SQL text with placeholders, select star from users where email equals dollar one, separately from the values. The database parses and plans the SQL first, then binds the values as pure data. A value full of quotes is just a strange email address that matches nobody.",
                "SQL text and values travel separately. The database parses the SQL first; values can only ever be data.")
pq_how.box(20, 40, 380, 60, None, "green")
pq_how.text(34, 76, "SELECT * FROM users WHERE email = $1", "t", anchor="start", size=16)
pq_how.box(20, 130, 380, 60, None, "y")
pq_how.text(34, 166, "values: [ \"x' OR '1'='1\" ]", "t", anchor="start", size=16)
pq_how.arrow(406, 70, 520, 110, label="1 · parse + plan", lx=470, ly=72)
pq_how.arrow(406, 160, 520, 130, label="2 · bind as data", lx=470, ly=170)
pq_how.db(600, 90, "database", w=110, h=60)
pq_how.note(380, 250, "result: no user with that strange email", "green")

PARAMS = dict(
    slug="parameterized-queries",
    kicker="a.k.a. “the printed form”",
    tldr="Never build SQL (or shell commands, or LDAP/NoSQL queries) by <b>gluing strings</b>. Send the <b>query text with placeholders</b> and the <b>values separately</b>; the database parses the query first and binds values as <b>pure data</b>, so input can never change the command. Use your driver's parameters or a query builder/ORM, and allow-list anything that can't be a parameter (column names, sort order).",
    chips=[("Family", "injection prevention"), ("Prevents", "SQL injection (OWASP A03)"), ("Also for", "shell, NoSQL, LDAP, XPath queries"), ("Pairs with", "input validation, least privilege")],
    problem="""  <p class="lead">When a query is built by <span class="hl-pink">concatenating input</span>, data and code share one string. A single quote in the input can end the value and turn the rest into SQL. Injection has been in the OWASP Top 10 for over twenty years.</p>
  <ul>
    <li>Login forms, search boxes and filters are the classic entry points.</li>
    <li>Escaping by hand misses edge cases (encodings, numeric contexts).</li>
    <li>The impact is whatever the database user can do.</li>
  </ul>""",
    problem_figs=[pq_problem],
    analogy_side="the printed form",
    analogy="""  <p>A bank transfer form has <b>printed wording</b> and <b>labelled boxes</b>. Whatever you write in the amount box is read as an <b>amount</b>, even if you write instructions there. The wording of the form can't be changed by what you put in the boxes.</p>
  <ul>
    <li>The printed wording is the <b>SQL text</b>.</li>
    <li>The boxes are <b>placeholders</b> (<code>$1</code>, <code>?</code>).</li>
    <li>What you write is always just a <b>value</b>.</li>
  </ul>""",
    analogy_figs=[pq_analogy],
    map=[("The printed form", "SQL with placeholders"),
         ("Labelled boxes", "<code>$1</code>, <code>$2</code> / <code>?</code>"),
         ("Writing in a box", "Binding a value"),
         ("Instructions in the amount box", "Malicious input, treated as data"),
         ("Bank reads the form first", "Database parses the query before binding values")],
    how_side="code and data never meet",
    how="""  <p>Parameters work because the database <b>knows the structure</b> before it sees the values. Escaping tries to make data look harmless; parameters make it impossible for data to be code.</p>""",
    how_figs=[pq_how],
    steps=[("Use placeholders everywhere", "<code>db.query(\"… WHERE email = $1\", [email])</code>, including LIMIT and numeric values."),
           ("Prefer a query builder or ORM", "They parameterize by default (Prisma, Drizzle, Kysely, SQLAlchemy)."),
           ("Watch the raw escape hatches", "<code>$queryRawUnsafe</code>, string-built <code>sql</code> fragments, <code>.raw()</code>."),
           ("Allow-list identifiers", "Column names and sort directions can't be parameters: map user choices to known values."),
           ("Same rule for shells", "Use argument arrays (<code>execFile</code>), never shell strings with input."),
           ("Limit the damage", "Run the app with a least-privilege database role.")],
    vocab=[("Injection", "Input interpreted as part of a command."),
           ("Placeholder", "A marker in the query for a value."),
           ("Bind parameter", "A value sent separately from the query text."),
           ("Prepared statement", "A query parsed once and run with different values."),
           ("Identifier", "A table or column name (can't be bound)."),
           ("Second-order injection", "Stored input later used unsafely in a query.")],
    code=dict(file="users.repo.ts", note="node-postgres", src="""
// ✗ string building: data can become code
// db.query(`SELECT * FROM users WHERE email = '${email}'`)

// ✓ placeholders: values are always data
const { rows } = await db.query(
  "SELECT id, name FROM users WHERE email = $1 AND tenant_id = $2",
  [email, tenantId],
);

// identifiers can't be parameters: allow-list them
const SORTS = { newest: "created_at DESC", name: "name ASC" } as const;
const order = SORTS[req.query.sort as keyof typeof SORTS] ?? SORTS.newest;
await db.query(`SELECT * FROM posts WHERE author_id = $1 ORDER BY ${order} LIMIT $2`,
  [authorId, 20]);

// shells too: arguments as an array, no shell string
execFile("convert", [inputPath, "-resize", "800x", outputPath]);
"""),
    tools="tools: every database driver's parameters, ORMs and query builders (Prisma, Drizzle, Kysely, TypeORM, SQLAlchemy, jOOQ), linters (eslint-plugin-security, Semgrep rules, CodeQL) to flag string-built queries.",
    gains=["<b>Injection becomes impossible</b> for bound values.",
           "<b>Simpler code</b> than manual escaping.",
           "<b>Prepared statements</b> can be faster.",
           "<b>Easy to enforce</b> with linters."],
    losses=["<b>Identifiers need allow-lists</b>.",
            "<b>Dynamic queries</b> take a little more care.",
            "<b>Raw escape hatches</b> remain a risk."],
    baseline="Each line compares <b>queries built by string concatenation</b> to <b>parameterized queries with allow-listed identifiers</b>.",
    ratings=[(3, 5, "Placeholders are simpler than escaping."),
             (3, 3, "Neutral."),
             (1, 5, "Input can't change the query."),
             (1, 5, "No attacker-controlled writes via injection."),
             (3, 4, "No injection-based data dumps or drops."),
             (1, 4, "Injection was a direct path to the whole database."),
             (3, 3, "Neutral."),
             (4, 5, "Free: it's how drivers work."),
             (3, 5, "ORMs and linters make it the default.")],
    pitfalls=[("Raw-query escape hatches", "<code>queryRawUnsafe(`… ${input}`)</code> in one admin report.", "ban unsafe APIs with a linter; review raw SQL."),
              ("User-chosen column names", "<code>ORDER BY ${req.query.sort}</code>.", "map choices to a fixed allow-list."),
              ("Second-order injection", "A stored value is later glued into a query.", "parameterize everywhere, not just at input time."),
              ("Shell commands with input", "<code>exec(`convert ${file}`)</code>.", "argument arrays (<code>execFile</code>) and validated paths.")],
    use=["Every database query that includes any variable.",
         "Shell commands, NoSQL filters, LDAP and XPath queries.",
         "Stored procedures that build dynamic SQL."],
    skip=["Never; there's no good reason to concatenate input into a query."],
    related=["<b>Validate at the boundary</b>", "<b>Least privilege</b>", "<b>Output encoding &amp; CSP</b>", "<b>Indexing</b> (Vol. 3)"],
    quiz=[("Why do parameters prevent SQL injection?", "The database parses the query before seeing values, and binds them as data only."),
          ("Can table or column names be parameters?", "No. Map user choices to an allow-list of known identifiers."),
          ("What's second-order injection?", "Input stored safely, later read and concatenated into another query."),
          ("How do you run an external program safely with user input?", "Pass arguments as an array (e.g. execFile), never through a shell string.")],
    remember="Print the <span class=\"hl\">form</span> first; whatever's in the <span class=\"hl\">box</span> is just a <span class=\"hl\">value</span>.",
    sources=["OWASP, “SQL Injection Prevention Cheat Sheet”.",
             "OWASP, “Query Parameterization Cheat Sheet”.",
             "OWASP Top 10 (2021), A03 “Injection”.",
             "PostgreSQL docs, “PREPARE” and libpq parameterized queries."],
)

# ------------------------------------------------------------------ 10 Output Encoding & CSP
oe_problem = Doodle(760, 260, "Doodle of a comment section. A user posts a comment containing a script tag. The page inserts the comment as raw HTML, so every visitor's browser runs the script, which reads their session and sends it to another site.",
                    "A comment shown as raw HTML: every visitor's browser runs the stranger's script.")
oe_problem.box(20, 30, 300, 80, "comment: <script>…</script>", "pink", stroke="red", size=15)
oe_problem.arrow(326, 70, 430, 70, color="red", label="innerHTML", lx=378, ly=56)
oe_problem.icon("window", 440, 30, 1.2)
oe_problem.note(600, 60, "runs in every", "red", anchor="start")
oe_problem.note(600, 86, "visitor's browser", "red", anchor="start")
oe_problem.arrow(470, 120, 470, 190, color="red", dash=True)
oe_problem.note(470, 220, "session sent elsewhere", "red")

oe_analogy = Doodle(760, 250, "Doodle of a museum exhibit label behind glass. Visitors can read any text, even text that says open the cases, but it's on the other side of the glass and can't do anything. And the museum only lets in guides wearing an official badge.",
                    "Text behind glass can be read, never act. And only guides with an official badge get in.")
oe_analogy.box(40, 40, 300, 150, None, "blue", rx=4)
oe_analogy.text(60, 110, "“open all the cases!”", "t", anchor="start", size=18)
oe_analogy.raw('<path class="d d-thin d-soft" d="M60 60 l40 -16 M280 180 l40 -16"/>')
oe_analogy.note(190, 220, "behind glass: shown, not obeyed", "green")
oe_analogy.icon("badge", 470, 50, 1.4, fill="y")
oe_analogy.note(560, 170, "only badged guides", "pen")
oe_analogy.note(560, 196, "(CSP: allowed sources)", "pen")

oe_how = Doodle(760, 290, "Two layers against cross-site scripting. Layer one: output encoding, data is escaped for its context, HTML text, attribute, URL or JavaScript, so a script tag becomes harmless visible text. Frameworks like React do this by default. Layer two: a Content Security Policy header tells the browser to run only scripts from your own origin with a per-request nonce, so even an injected script is blocked.",
                "Escape data for where it goes; then let CSP block any script you didn't send yourself.")
oe_how.box(20, 40, 200, 70, "<script>", "pink", stroke="red", size=18)
oe_how.arrow(226, 75, 316, 75, label="encode", lx=271, ly=61)
oe_how.box(322, 40, 220, 70, "&lt;script&gt;", "green", size=17)
oe_how.note(432, 140, "shown as text", "green")
oe_how.box(20, 180, 520, 70, "CSP: script-src 'self' 'nonce-r4nd0m'", "y", size=16)
oe_how.arrow(546, 215, 620, 215, color="red", label="blocked", lx=583, ly=200)
oe_how.note(690, 220, "injected script", "red")

OUTPUT = dict(
    slug="output-encoding",
    kicker="a.k.a. “text behind glass”",
    tldr="Cross-site scripting happens when <b>data is shown as code</b>. Prevent it with two layers: <b>encode output for its context</b> (HTML text, attribute, URL, JavaScript), which modern frameworks do by default, so avoid <code>innerHTML</code> and <code>dangerouslySetInnerHTML</code>; and send a strict <b>Content Security Policy</b> so the browser <b>refuses to run scripts you didn't send</b>. Sanitize the rare rich HTML with a proven library.",
    chips=[("Family", "XSS prevention"), ("Layers", "contextual encoding + CSP"), ("Tools", "framework escaping, DOMPurify, CSP nonces"), ("Pairs with", "input validation, CSRF protection")],
    problem="""  <p class="lead">Any place that shows user content (comments, names, search terms, error messages) can become a way to <span class="hl-pink">run a stranger's script in your users' browsers</span>, with their session and their permissions.</p>
  <ul>
    <li>A comment with a script tag runs for every visitor.</li>
    <li>A search term echoed into the page runs via a crafted link.</li>
    <li>Tokens in localStorage are read and sent away.</li>
  </ul>""",
    problem_figs=[oe_problem],
    analogy_side="text behind glass",
    analogy="""  <p>In a museum, an exhibit label can say anything, even “open all the cases!”, but it's <b>behind glass</b>: visitors can read it, it can't <b>do</b> anything. And the museum only lets in <b>guides wearing an official badge</b>.</p>
  <ul>
    <li>Glass is <b>output encoding</b>: shown, never executed.</li>
    <li>The badge rule is <b>CSP</b>: only scripts you approved may act.</li>
  </ul>""",
    analogy_figs=[oe_analogy],
    map=[("Text behind glass", "Escaped output (<code>&amp;lt;script&amp;gt;</code>)"),
         ("Different glass for different cases", "Contextual encoding: HTML, attribute, URL, JS"),
         ("Only badged guides allowed", "CSP <code>script-src</code> with nonces"),
         ("A curator checks donated exhibits", "Sanitizing rich HTML with DOMPurify"),
         ("Smashing the glass", "<code>innerHTML</code> / <code>dangerouslySetInnerHTML</code>")],
    how_side="encode, then restrict",
    how="""  <p>Encoding stops injected markup becoming code. CSP is the <b>safety net</b> for the bug you'll eventually ship anyway.</p>""",
    how_figs=[oe_how],
    steps=[("Let the framework escape", "React, Vue, Angular, Svelte and server templates escape text by default; keep it that way."),
           ("Avoid raw HTML sinks", "<code>innerHTML</code>, <code>dangerouslySetInnerHTML</code>, <code>v-html</code>, <code>document.write</code>."),
           ("Sanitize rich content", "If you must render user HTML or Markdown, sanitize with DOMPurify (or server-side equivalent)."),
           ("Check URLs", "Allow only <code>http(s)</code> in user links; block <code>javascript:</code>."),
           ("Add a strict CSP", "<code>script-src 'nonce-…' 'strict-dynamic'</code>, <code>object-src 'none'</code>, <code>base-uri 'none'</code>; start in report-only mode."),
           ("Keep tokens out of JS reach", "httpOnly cookies, so even a successful XSS can't read them.")],
    vocab=[("XSS", "Cross-site scripting: attacker's script runs on your page."),
           ("Output encoding", "Turning special characters into harmless text."),
           ("Context", "Where data is placed: HTML, attribute, URL, script."),
           ("CSP", "Header telling the browser which content may load and run."),
           ("Nonce", "Random value per response allowing specific scripts."),
           ("Sanitizer", "Removes dangerous parts from HTML.")],
    code=dict(file="comment.tsx + headers.ts", note="React + Express", src="""
// ✓ React escapes text automatically
<p className="comment">{comment.body}</p>

// rich text: sanitize first, then render
<div dangerouslySetInnerHTML={{ __html: DOMPurify.sanitize(markdownToHtml(c.body)) }} />

// links: allow only http(s)
const safeHref = /^https?:\\/\\//i.test(url) ? url : "#";

// strict CSP with a fresh nonce per response
app.use((req, res, next) => {
  res.locals.nonce = crypto.randomBytes(16).toString("base64");
  res.setHeader("Content-Security-Policy",
    `script-src 'nonce-${res.locals.nonce}' 'strict-dynamic'; ` +
    "object-src 'none'; base-uri 'none'; frame-ancestors 'none'");
  next();
});
"""),
    tools="tools: framework auto-escaping, DOMPurify, sanitize-html, Trusted Types, CSP Evaluator, report-uri / report-to endpoints, Helmet (Express), eslint-plugin-react rules for dangerous props.",
    gains=["<b>User content stays text</b>.",
           "<b>CSP blocks injected scripts</b> even when a bug slips through.",
           "<b>Framework defaults</b> do most of the work.",
           "<b>CSP reports</b> reveal attacks and mistakes."],
    losses=["<b>CSP takes tuning</b> (third-party scripts, inline handlers).",
            "<b>Rich text needs a sanitizer</b>.",
            "<b>Easy to bypass</b> with one raw HTML sink."],
    baseline="Each line compares <b>rendering user content as raw HTML with no CSP</b> to <b>contextual encoding, sanitized rich text and a strict nonce-based CSP</b>.",
    ratings=[(3, 4, "Framework defaults; CSP needs one-time care."),
             (3, 3, "Invisible to users."),
             (1, 4, "Scripts can't read sessions or page data."),
             (1, 5, "Injected code can't act as the user."),
             (3, 3, "Neutral."),
             (1, 4, "A missed escape is blocked by CSP."),
             (2, 4, "CSP violation reports show attempts."),
             (3, 4, "Mostly configuration."),
             (3, 4, "Safe by default; linters flag dangerous props.")],
    pitfalls=[("Raw HTML sinks", "<code>el.innerHTML = name</code> in one widget.", "use textContent / framework rendering; lint sinks."),
              ("Sanitizing with regex", "Stripping “&lt;script&gt;” misses event handlers and SVG.", "use DOMPurify."),
              ("A CSP with 'unsafe-inline'", "The policy allows exactly what attackers inject.", "nonces + strict-dynamic, no unsafe-inline."),
              ("javascript: links", "User-supplied URLs run code on click.", "allow only http(s) schemes.")],
    use=["Every page that shows user or third-party content.",
         "Admin panels (attackers love targeting admins).",
         "Any HTML email or PDF generated from user data."],
    skip=["Never skip encoding; CSP can be phased in with report-only mode."],
    related=["<b>Validate at the boundary</b>", "<b>CSRF protection</b>", "<b>Short-lived tokens</b>", "<b>Error boundaries</b> (Vol. 2)"],
    quiz=[("What makes XSS possible?", "User-controlled data is placed into a page in a way the browser interprets as code."),
          ("Why does encoding depend on context?", "Different places (HTML text, attributes, URLs, scripts) have different special characters."),
          ("What does a nonce-based CSP do?", "Only scripts carrying the per-response nonce may run, so injected scripts are blocked."),
          ("How do you render user-supplied HTML safely?", "Sanitize it with a proven library like DOMPurify before inserting it.")],
    remember="Put user text behind <span class=\"hl\">glass</span>, and only let <span class=\"hl\">badged</span> scripts in.",
    sources=["OWASP, “Cross Site Scripting Prevention Cheat Sheet”.",
             "Google, “Strict CSP” (csp.withgoogle.com).",
             "MDN, “Content Security Policy (CSP)”.",
             "DOMPurify documentation."],
)

# ------------------------------------------------------------------ 11 CSRF Protection
cs_problem = Doodle(760, 250, "Doodle of a user logged into their bank in one tab. In another tab they visit a malicious page which contains a hidden form that posts to the bank's transfer endpoint. The browser automatically attaches the bank's session cookie, so the bank thinks the user asked for the transfer.",
                    "A hidden form on another site posts to your bank, and the browser helpfully adds your cookie.")
cs_problem.box(20, 40, 200, 70, "evil.example", "pink", stroke="red", size=17)
cs_problem.note(120, 140, "hidden form", "red")
cs_problem.arrow(226, 75, 470, 75, color="red", label="POST /transfer + your cookie", lx=348, ly=60)
cs_problem.box(476, 40, 200, 70, "bank.example", "blue", size=17)
cs_problem.note(576, 150, "“looks like you!”", "red")
cs_problem.note(380, 220, "the browser attached the session automatically", "pen")

cs_analogy = Doodle(760, 250, "Doodle of a restaurant where waiters only accept orders written on the restaurant's own order pads, each with a unique stamp. A note slipped under the door saying table 5 wants champagne is ignored, even though it names a real table.",
                    "Only orders on the restaurant's own stamped pad count; a note under the door is ignored.")
cs_analogy.icon("menu", 60, 50, 1.4, fill="green")
cs_analogy.icon("stamp", 110, 110, 0.8)
cs_analogy.note(110, 210, "own pad + stamp ✓", "green")
cs_analogy.icon("envelope", 400, 70, 1.4, fill="pink")
cs_analogy.note(440, 170, "“table 5: champagne”", "red")
cs_analogy.note(440, 196, "under the door ✗", "red")

cs_how = Doodle(760, 290, "CSRF defences. Layer one: session cookies are set with SameSite Lax or Strict, so browsers don't send them on cross-site posts. Layer two: state-changing requests must carry a CSRF token that only your own page knows, or a custom header that cross-site forms can't add. Layer three: the server checks the Origin header. GET requests never change state.",
                "SameSite cookies, a token or custom header only your pages can send, an Origin check, and GET never changes state.")
for i, (t, sub, f) in enumerate([("SameSite=Lax", "cookie stays home", "green"), ("CSRF token", "only your page has it", "y"), ("Origin check", "must be your site", "blue")]):
    cs_how.box(20 + i * 250, 50, 220, 90, t, f, sub=sub, size=18)
cs_how.arrow(380, 200, 380, 150, color="red", label="cross-site POST", lx=400, ly=190, anchor="start")
cs_how.note(380, 240, "fails all three", "red")
cs_how.note(380, 274, "and GET never changes anything", "pen")

CSRF = dict(
    slug="csrf-protection",
    kicker="a.k.a. “the restaurant's own order pad”",
    tldr="Browsers attach cookies to requests <b>even when another site triggers them</b>. If your app trusts the cookie alone, a hidden form elsewhere can act as the user. Defend in layers: <b>SameSite</b> session cookies, a <b>CSRF token</b> (or a custom header) on every state-changing request, an <b>Origin check</b> on the server, and <b>never change state on GET</b>.",
    chips=[("Family", "request forgery"), ("Defences", "SameSite cookies, synchronizer / double-submit tokens, Origin checks"), ("Not needed for", "APIs using Authorization headers only"), ("Pairs with", "output encoding & CSP")],
    problem="""  <p class="lead">Cookie-based sessions have a catch: the browser sends your cookie to your site <span class="hl-pink">no matter which site started the request</span>. A malicious page can make the user's browser submit a form to your app, fully authenticated.</p>
  <ul>
    <li>A hidden form transfers money or changes the account email.</li>
    <li>An image tag hits <code>GET /delete?id=5</code>.</li>
    <li>The server sees a valid session and does it.</li>
  </ul>""",
    problem_figs=[cs_problem],
    analogy_side="the restaurant's own order pad",
    analogy="""  <p>In a busy restaurant, waiters only accept orders written on the restaurant's <b>own order pads</b>, each with a <b>unique stamp</b>. A note slipped under the door saying “table 5 wants champagne” is ignored, even though table 5 is real.</p>
  <ul>
    <li>The stamped pad is a <b>CSRF token</b> only your pages have.</li>
    <li>The note under the door is a <b>cross-site request</b>.</li>
    <li>Checking it came from inside is the <b>Origin check</b>.</li>
  </ul>""",
    analogy_figs=[cs_analogy],
    map=[("Table 5 really exists", "The user really has a valid session cookie"),
         ("Note slipped under the door", "A form on another site posting to yours"),
         ("The restaurant's own stamped pad", "A CSRF token from your page"),
         ("Waiter checks it came from inside", "Server checks the <code>Origin</code> header"),
         ("Pads never leave the restaurant", "<code>SameSite</code> cookies stay on same-site requests")],
    how_side="prove the request came from you",
    how="""  <p>Modern browsers default cookies to <code>SameSite=Lax</code>, which blocks the classic attack, but set it explicitly and keep a token or header check as a second layer.</p>""",
    how_figs=[cs_how],
    steps=[("Set SameSite explicitly", "<code>Set-Cookie: session=…; HttpOnly; Secure; SameSite=Lax</code> (Strict where usable)."),
           ("Require a token on unsafe methods", "POST, PUT, PATCH, DELETE carry a per-session token in a hidden field or header."),
           ("Or require a custom header", "APIs called with <code>fetch</code> can require <code>X-Requested-With</code>/JSON content type, which cross-site forms can't send without CORS."),
           ("Check Origin", "Reject unsafe requests whose <code>Origin</code> isn't yours."),
           ("Keep GET safe", "GET and HEAD never change state."),
           ("Use the framework's built-in protection", "Rails, Django, Laravel, Spring and Next.js server actions include it.")],
    vocab=[("CSRF", "Cross-site request forgery: another site acts with the user's session."),
           ("SameSite", "Cookie attribute controlling cross-site sending (Strict, Lax, None)."),
           ("Synchronizer token", "Random token stored server-side and embedded in forms."),
           ("Double-submit cookie", "Token in a cookie and a header that must match."),
           ("Origin header", "Browser-set header naming the requesting site."),
           ("Safe method", "GET/HEAD/OPTIONS: must not change state.")],
    code=dict(file="csrf.ts", note="Express", src="""
// session cookie: never sent on cross-site POSTs
res.cookie("session", sid, { httpOnly: true, secure: true, sameSite: "lax" });

// second layer for every state-changing request
const UNSAFE = new Set(["POST", "PUT", "PATCH", "DELETE"]);
app.use((req, res, next) => {
  if (!UNSAFE.has(req.method)) return next();

  const origin = req.get("origin");
  if (origin && origin !== "https://bank.example") return res.sendStatus(403);

  const token = req.get("x-csrf-token") ?? req.body?._csrf;
  if (!token || !timingSafeEqual(token, req.session.csrfToken)) return res.sendStatus(403);
  next();
});

// pages embed the token:  <input type="hidden" name="_csrf" value="{{csrfToken}}">
"""),
    tools="tools: built-in CSRF protection in Rails, Django, Laravel, Spring Security, ASP.NET; csrf-csrf / lusca for Express; Next.js server actions (Origin checks); browser SameSite defaults.",
    gains=["<b>Forged requests rejected</b>.",
           "<b>Cookie sessions stay usable</b> safely.",
           "<b>Built into most frameworks</b>.",
           "<b>Cheap</b>: a few checks per request."],
    losses=["<b>Tokens to plumb</b> into forms and fetch calls.",
            "<b>SameSite=Strict</b> can break inbound links' logged-in state.",
            "<b>Cross-site embeds and SSO</b> need careful exceptions."],
    baseline="Each line compares <b>cookie sessions with no CSRF checks</b> to <b>SameSite cookies + token/header + Origin checks</b>.",
    ratings=[(3, 3, "A few extra checks to understand."),
             (4, 4, "Invisible with SameSite=Lax."),
             (3, 3, "Neutral."),
             (1, 5, "Other sites can't act as your users."),
             (3, 3, "Neutral."),
             (2, 4, "A malicious page can't trigger actions."),
             (3, 4, "Rejected forgeries can be logged."),
             (4, 4, "Mostly framework defaults."),
             (3, 4, "Frameworks handle tokens for you.")],
    pitfalls=[("State changes on GET", "<code>GET /logout</code> or <code>/delete?id=5</code>.", "use POST/DELETE for changes."),
              ("Disabling protection for “the API”", "The same cookie session is used by the API.", "if it uses cookies, it needs CSRF protection."),
              ("SameSite=None everywhere", "Set for one embed, applied to the session.", "only on cookies that truly need cross-site use."),
              ("Tokens in URLs", "Leak via logs and referrers.", "put tokens in bodies or headers.")],
    use=["Any app using cookie-based sessions.",
         "Forms and fetch calls that change state.",
         "Admin panels and account settings especially."],
    skip=["APIs authenticated only by Authorization headers (bearer tokens), which browsers don't attach automatically."],
    related=["<b>Output encoding &amp; CSP</b>", "<b>Short-lived tokens</b>", "<b>Validate at the boundary</b>", "<b>Optimistic UI</b> (Vol. 2)"],
    quiz=[("Why does CSRF work at all?", "Browsers automatically attach cookies to requests to your site, even when another site triggers them."),
          ("What does SameSite=Lax do?", "Stops the cookie being sent on cross-site POSTs and other unsafe cross-site requests."),
          ("Why must GET never change state?", "GET requests are easy to trigger cross-site (links, images) and aren't covered by token checks."),
          ("Do bearer-token APIs need CSRF tokens?", "Usually not, because browsers don't attach Authorization headers automatically.")],
    remember="Only orders on your own <span class=\"hl\">stamped pad</span> count. Notes under the <span class=\"hl\">door</span> are ignored.",
    sources=["OWASP, “Cross-Site Request Forgery Prevention Cheat Sheet”.",
             "MDN, “SameSite cookies”.",
             "RFC 6265bis, “Cookies: HTTP State Management Mechanism” (SameSite).",
             "web.dev, “SameSite cookies explained”."],
)

NOTES = [VALIDATE, PARAMS, OUTPUT, CSRF]
