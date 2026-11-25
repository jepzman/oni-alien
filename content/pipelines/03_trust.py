# Vol. 9 · Keeping it trustworthy: Write–Audit–Publish, Data Contracts, Quality Checks & Quarantine,
# DAG Orchestration & Lineage. Same homeware shop.

# ------------------------------------------------------------------ 11 Write–Audit–Publish
wap_problem = Doodle(760, 260, "Doodle of a Monday morning. At 06:00 the load writes straight into the published sales table, but a truncated source export means half of Sunday's order lines are missing. At 07:00 the finance dashboard shows revenue down 40 percent. The tests run at 07:30 and fail, but the CFO has already seen the number at the 08:00 meeting.",
                     "Load, publish, then test: the tests are right, and an hour too late.")
wap_problem.line("M30 160 H730")
for x, t in [(90, "06:00"), (300, "07:00"), (480, "07:30"), (660, "08:00")]:
    wap_problem.line(f"M{x} 152 v16")
    wap_problem.note(x, 192, t)
wap_problem.box(20, 50, 150, 80, "load", "blue", sub="writes fct_sales", size=20, subsize=14)
wap_problem.box(220, 50, 160, 80, "dashboard", "pink", stroke="red", sub="revenue −40 %", size=20, subsize=14)
wap_problem.box(410, 50, 140, 80, "tests", "y", sub="fail", size=20, subsize=14)
wap_problem.box(590, 50, 150, 80, "CFO", "pink", stroke="red", sub="has seen it", size=20, subsize=14)
wap_problem.note(380, 240, "the source export was truncated: half of Sunday missing", "red")

wap_analogy = Doodle(760, 240, "Doodle of a newspaper. The edition is written, then a proofreader checks it, and only then is it printed and delivered. If the proofreader finds an error, yesterday's paper stays on the stand and nothing wrong goes out.",
                     "Write the edition, proofread it, then print. Never print and proofread afterwards.")
wap_analogy.row([("write", "draft edition", "blue"), ("proofread", "checks pass?", "y"), ("print", "on the stand", "green")], y=40, h=90, gap=60, size=21, subsize=15, arrows=True)
wap_analogy.icon("newspaper", 620, 150, 0.9)
wap_analogy.note(370, 200, "errors found → yesterday's paper stays out", "pen")

wap_how = Doodle(760, 300, "Write, audit, publish. The load writes into a hidden copy, fct_sales_next, while fct_sales stays published. Audits run on the hidden copy: unique keys, row counts against last week, reconciliation with the source. If they pass, an atomic swap makes the new copy the published table. If they fail, the old table stays published, an alert fires, and the dashboard shows data as of yesterday.",
                 "Build hidden, test hidden, then swap in one step. A failed audit leaves yesterday in place.")
wap_how.box(20, 40, 200, 80, "write", "blue", sub="fct_sales_next", size=21, subsize=15)
wap_how.arrow(226, 80, 280, 80)
wap_how.box(286, 40, 200, 80, "audit", "y", sub="keys · counts · sums", size=21, subsize=15)
wap_how.arrow(492, 64, 546, 40, label="pass", lx=518, ly=34)
wap_how.box(552, 10, 190, 64, "swap", "green", sub="atomic rename", size=21, subsize=15)
wap_how.arrow(492, 100, 546, 160, color="red", label="fail", lx=530, ly=118, anchor="start")
wap_how.box(552, 140, 190, 80, "keep yesterday", "pink", stroke="red", sub="alert · “as of Sun”", size=18, subsize=15)
wap_how.note(250, 200, "readers only ever see an audited table", "green")
wap_how.note(250, 230, "fct_sales stays published the whole time", "pen")

WAP = dict(
    slug="write-audit-publish",
    kicker="a.k.a. “WAP, blue-green for data”",
    tldr="Never load straight into the table people read. <b>Write</b> the new data into a hidden copy, <b>audit</b> it there (keys, counts, sums, reconciliation), and <b>publish</b> it with an atomic swap only if the audits pass. If they fail, readers keep yesterday's correct table, with a clear “data as of” note, instead of today's wrong one.",
    chips=[("Family", "keeping it trustworthy"), ("Origin", "Netflix and Iceberg (2017)"), ("Lives in", "Iceberg branches, Snowflake clones, lakeFS, Nessie"), ("Pairs with", "quality checks, blue-green (Vol. 6)")],
    problem="""  <p class="lead">On Monday the 06:00 load writes straight into <code>fct_sales</code>. The source export was truncated, so half of Sunday is missing. At 07:00 the finance dashboard shows revenue <span class="hl-pink">down 40 %</span>. The tests run at 07:30 and fail correctly, but the CFO has already taken the number to the 08:00 meeting.</p>
  <ul>
    <li>Tests that run after publishing only tell you what people have already seen.</li>
    <li>A half-loaded table is visible for as long as the load takes.</li>
    <li>Trust is lost faster than it's rebuilt: next week nobody believes the dashboard.</li>
  </ul>""",
    problem_figs=[wap_problem],
    analogy_side="the newspaper",
    analogy="""  <p>A newspaper is <b>written</b>, then <b>proofread</b>, then <b>printed</b>. If the proofreader finds a wrong headline, the presses wait and yesterday's paper stays on the stand. Nobody prints first and proofreads afterwards.</p>""",
    analogy_figs=[wap_analogy],
    map=[("Writing the edition", "Loading into a hidden copy or branch"),
         ("The proofreader", "Audits: tests on the hidden copy"),
         ("Printing", "An atomic swap or branch merge"),
         ("Yesterday's paper on the stand", "The previously published table stays"),
         ("“Late edition” notice", "A “data as of Sunday” banner on dashboards")],
    how_side="hidden copy, audits, atomic swap",
    how="""  <p>The load writes into a copy that readers can't see: a <code>_next</code> table, a zero-copy clone, or a branch in Iceberg, Nessie or lakeFS. Audits run against that copy. Publishing is one atomic step (a table swap, a view pointing at the new table, a branch fast-forward), so readers see the old version or the new one, never half of either.</p>""",
    how_figs=[wap_how],
    steps=[("Write hidden", "Build <code>fct_sales_next</code> (or a branch) from the same models."),
           ("Audit there", "Unique keys, not nulls, row counts and sums against the usual band, reconciliation with the source."),
           ("Publish atomically", "<code>ALTER TABLE … SWAP WITH</code>, a rename, a view switch, or a branch merge."),
           ("On failure, keep the old", "Alert the owner; dashboards show the data's real age."),
           ("Clean up", "Drop or keep the failed copy for debugging, with a short retention.")],
    vocab=[("WAP", "Write–audit–publish."),
           ("Audit", "Checks run on unpublished data."),
           ("Atomic swap", "Replacing a table in one step that readers can't see half-done."),
           ("Zero-copy clone", "A copy that shares storage until changed (Snowflake, Delta)."),
           ("Branch", "A named version of tables you can commit to and merge (Iceberg, Nessie, lakeFS)."),
           ("Data as of", "The age of the newest data, shown to readers.")],
    code=dict(file="publish_fct_sales.sql", note="Snowflake-style SQL", src="""
-- 1 · write: build the next version where nobody reads
CREATE OR REPLACE TABLE fct_sales_next CLONE fct_sales;
MERGE INTO fct_sales_next t USING stg_sales_changes s ON …;   -- the normal load

-- 2 · audit: every check must return zero rows
SELECT order_line_id FROM fct_sales_next GROUP BY 1 HAVING count(*) > 1;
SELECT 1 FROM (SELECT count(*) n FROM fct_sales_next WHERE order_date = :day) x
 WHERE n < 0.7 * (SELECT avg_lines FROM expected_volume WHERE weekday = dayofweek(:day));

-- 3 · publish: one atomic step
ALTER TABLE fct_sales SWAP WITH fct_sales_next;
"""),
    tools="tools: Apache Iceberg WAP and branches, Project Nessie, lakeFS, Delta Lake clones, Snowflake zero-copy clones and SWAP, BigQuery table snapshots, dbt <code>build</code> (tests before downstream models) and blue-green deployment macros.",
    gains=["<b>Readers never see unaudited data</b>.",
           "<b>Failures are quiet</b>: yesterday stays, an alert fires.",
           "<b>No half-loaded tables</b> during long loads.",
           "<b>Easy rollback</b>: swap back to the previous copy."],
    losses=["<b>Freshness pauses</b> when an audit fails.",
            "<b>Extra storage and compute</b> for the copy.",
            "<b>Audits to maintain</b>: too strict and every run fails.",
            "<b>Cross-table consistency</b> needs publishing several tables together."],
    baseline="Each line compares <b>loading straight into published tables and testing afterwards</b> to <b>write–audit–publish with an atomic swap</b>.",
    ratings=[(3, 3, "One more step and naming rule."),
             (4, 3, "A failed audit holds back fresh data."),
             (2, 5, "Nobody reads data that failed its checks."),
             (3, 4, "The previous version is always there to swap back."),
             (3, 3, "Neutral: clones and branches scale."),
             (4, 3, "A copy and its audits cost a little."),
             (3, 3, "Neutral."),
             (2, 5, "Audits run every load, before anyone looks."),
             (3, 4, "Changes ship behind the same gate.")],
    pitfalls=[("Audits after the swap", "The steps are in the wrong order, and readers see bad data first.", "publish is the last step, and only on success."),
              ("Swapping tables one by one", "Facts are new, dimensions still old; joins break for an hour.", "publish related tables together (a branch merge or a schema swap)."),
              ("Audits that always pass", "Only “table not empty” is checked.", "check counts and sums against a usual band, and reconcile with the source."),
              ("Silent staleness", "The audit fails every day for a week and nobody notices, because the dashboard looks fine.", "alert on failed publishes and show data age on every dashboard.")],
    use=["Tables that people make decisions from.",
         "Loads that take long enough to be seen half-done.",
         "Sources that sometimes send broken or partial data.",
         "Any table with an external audience."],
    skip=["Exploration sandboxes.",
          "Streaming tables where seconds matter: check in the stream instead.",
          "Small internal tables where a wrong hour does no harm."],
    related=["<b>Quality checks and quarantine</b>", "<b>Blue-green deployment</b> (Vol. 6)", "<b>Layered zones</b>", "<b>DAG orchestration and lineage</b>"],
    quiz=[("What are the three steps of WAP?", "Write into a hidden copy, audit it with checks, publish it with an atomic swap only if the checks pass."),
          ("What do readers see when an audit fails?", "The previously published, audited table, with its real age shown."),
          ("Why must publishing be atomic?", "So readers see either the old version or the new one, never half of each."),
          ("Why publish facts and dimensions together?", "So joins between them always see matching versions.")],
    quiz_sit=[("A partner's file sometimes arrives with only half its rows. Your load and tests both run at 06:00, and dashboards refresh at 06:05. What do you change?",
               "Load into a hidden copy, audit row counts and totals against the usual band for that weekday, and swap only on success. On failure keep yesterday's table, alert the owner, and show “data as of yesterday” on the dashboard until the partner resends.")],
    try_it="In any SQL database, build a <code>_next</code> copy of a table, insert a deliberately broken batch, write two audit queries that must return zero rows, and only rename the copy into place when they do. Then try it with a good batch.",
    remember="<span class=\"hl\">Write</span>, <span class=\"hl\">proofread</span>, then print. Yesterday's paper beats today's wrong one.",
    sources=["Ryan Blue, “Write-Audit-Publish” (Netflix, Apache Iceberg, 2017 talk).",
             "Apache Iceberg documentation, “Branching and tagging” and WAP.",
             "lakeFS and Project Nessie documentation on data branches.",
             "Snowflake documentation, “ALTER TABLE … SWAP WITH” and zero-copy cloning."],
)

# ------------------------------------------------------------------ 12 Data Contracts
dc_problem = Doodle(760, 260, "Doodle of a breaking change. The app team renames the column line_total to amount_gross in a normal Tuesday release. The warehouse pipeline still reads line_total, which is now always empty, and revenue shows as zero for a week until the finance meeting.",
                    "A normal Tuesday release renames one column. The warehouse finds out a week later.")
dc_problem.box(20, 50, 200, 90, "app release", "blue", sub="renames line_total", size=20, subsize=13)
dc_problem.arrow(226, 95, 300, 95)
dc_problem.table(306, 60, "stg_order_lines", ["line_total: NULL", "line_total: NULL"], w=210, fill="y", stroke="red")
dc_problem.arrow(522, 95, 580, 95, color="red")
dc_problem.box(586, 50, 160, 90, "revenue", "pink", stroke="red", sub="€0 for a week", size=20, subsize=15)
dc_problem.note(380, 220, "nobody told the app team the column was used", "red")

dc_analogy = Doodle(760, 240, "Doodle of a supplier's specification sheet. A bakery and a supermarket agree a spec: loaf weight 800 grams, label fields, delivery by 6 am. If the bakery wants to change the weight, it announces version 2 in advance and supplies both for a while.",
                    "A supplier spec: agreed fields and limits, and changes announced as a new version.")
dc_analogy.icon("recipe", 60, 40, 1.8, fill="y")
dc_analogy.note(110, 180, "spec v1: 800 g · by 06:00")
dc_analogy.arrow(190, 100, 300, 100, both=True)
dc_analogy.icon("store", 320, 50, 1.4)
dc_analogy.box(500, 60, 240, 90, "v2 announced", "green", sub="both supplied for a month", size=20, subsize=14)
dc_analogy.note(380, 220, "the shelf never empties because of a change", "pen")

dc_how = Doodle(760, 300, "A data contract. The producing team owns a contract file next to its code: the fields, types and nullability, what each field means, quality rules, freshness, the owner and a version. Their continuous integration checks every change against the contract and blocks breaking ones. The pipeline validates incoming data against the same contract and quarantines what doesn't fit.",
                 "One file, owned by the producer, checked in their CI and at the warehouse's door.")
dc_how.box(220, 20, 320, 120, "contract v2", "y", sub="fields · meaning · rules · SLA · owner", size=21, subsize=13)
dc_how.box(20, 170, 220, 80, "producer's CI", "blue", sub="blocks breaking changes", size=19, subsize=14)
dc_how.box(520, 170, 220, 80, "pipeline", "green", sub="validates on arrival", size=19, subsize=14)
dc_how.arrow(300, 144, 160, 166)
dc_how.arrow(460, 144, 610, 166)
dc_how.note(380, 280, "breaking change → v3 alongside v2, then deprecate", "pen")

DC = dict(
    slug="data-contracts",
    kicker="a.k.a. “an API for data”",
    tldr="When a pipeline reads another team's data, write down the agreement: <b>fields and types</b>, what each <b>means</b>, <b>quality rules</b>, <b>freshness</b>, the <b>owner</b> and a <b>version</b>. Keep the contract in the producer's repository, <b>check it in their CI</b> so breaking changes are blocked before release, and validate incoming data against it. Breaking changes become a new version that runs alongside the old one for a while.",
    chips=[("Family", "keeping it trustworthy"), ("Also called", "schema contract, data product interface"), ("Lives in", "dbt model contracts, ODCS, schema registries"), ("Pairs with", "change data capture, open host service")],
    problem="""  <p class="lead">The app team renames <code>line_total</code> to <code>amount_gross</code> in a normal Tuesday release. CDC carries the new column; the warehouse still reads the old one, which is now always empty. Revenue shows <span class="hl-pink">€0 for a week</span>, until the finance meeting.</p>
  <ul>
    <li>The app team didn't know anyone used that column.</li>
    <li>The warehouse found out from its users, not from a test.</li>
    <li>Every source change is a surprise, so the data team spends its weeks firefighting.</li>
  </ul>""",
    problem_figs=[dc_problem],
    analogy_side="the supplier's spec sheet",
    analogy="""  <p>A bakery and a supermarket agree a <b>spec</b>: an 800 g loaf, these label fields, delivered by 06:00. If the bakery wants to sell 750 g loaves, it announces <b>version 2</b> a month ahead and supplies both for a while. The shelf never empties because of a change.</p>""",
    analogy_figs=[dc_analogy],
    map=[("The spec sheet", "The contract file: schema, meaning, rules"),
         ("800 g, delivered by 06:00", "Quality rules and freshness SLA"),
         ("The bakery owns the spec", "The producing team owns the contract"),
         ("Announcing version 2", "A new contract version for breaking changes"),
         ("Supplying both for a month", "Old and new versions side by side, then deprecate")],
    how_side="written down, owned by the producer, checked twice",
    how="""  <p>The contract is a small file (YAML) in the producer's repository. Their CI compares every schema change with it: adding a nullable column passes; removing, renaming or retyping a field fails unless the version is bumped. At the warehouse door, the pipeline validates data against the same file and quarantines rows that don't fit.</p>
  <p>The best contracts aren't on raw tables at all. The producer publishes a designed interface (a view, an outbox event, a published dataset) so their tables stay private and free to change.</p>""",
    how_figs=[dc_how],
    steps=[("Find the critical inputs", "Which source fields do important reports depend on? Start with those."),
           ("Write the contract with the producer", "Fields, types, nullability, meaning, rules, freshness, owner, version."),
           ("Check it in their CI", "A breaking change fails the build unless it's a new version."),
           ("Validate on arrival", "The pipeline checks schema and rules; failures go to quarantine and alert both teams."),
           ("Version breaking changes", "Publish v3 alongside v2, migrate consumers, then retire v2 on a date.")],
    vocab=[("Data contract", "A versioned agreement on a dataset's shape, meaning and quality."),
           ("Producer / consumer", "The team that creates the data / the teams that use it."),
           ("Breaking change", "Removing, renaming or retyping a field, or tightening its meaning."),
           ("Schema registry", "A service storing message schemas and checking compatibility."),
           ("Deprecation", "Announcing that a version will be retired on a date."),
           ("Data product", "A dataset published for others with an owner and a contract.")],
    code=dict(file="contracts/order_lines.yaml", note="ODCS-style contract", src="""
dataset: shop.order_lines
version: 2.1.0
owner: team-checkout            # who to call, who approves changes
description: One row per order line, as charged to the customer.
freshness: { max_delay: 15m }
fields:
  - name: order_line_id   type: bigint   required: true   unique: true
  - name: order_id        type: bigint   required: true
  - name: sku             type: string   required: true
  - name: qty             type: int      required: true   min: 1
  - name: line_total      type: decimal(12,2)   required: true
    description: Gross amount charged in EUR, including VAT, after discounts.
  - name: updated_at      type: timestamp       required: true
breaking_changes: new major version, both served for 30 days
"""),
    tools="tools: Open Data Contract Standard (ODCS) and the Data Contract CLI, dbt model contracts (<code>contract: enforced</code>), Confluent Schema Registry with Avro or Protobuf compatibility modes, Soda and Great Expectations for the rules, Gable.",
    gains=["<b>Breaking changes caught before release</b>, in the producer's CI.",
           "<b>Clear ownership</b>: who to ask, who approves.",
           "<b>Meaning is written down</b>: “gross, incl. VAT” is no longer folklore.",
           "<b>Producers stay free</b> to change everything not in the contract."],
    losses=["<b>Upfront work and negotiation</b> between teams.",
            "<b>Producers take on a duty</b> they may resist.",
            "<b>Versioning effort</b>: serving two versions for a while.",
            "<b>Contracts can rot</b> if nobody checks them automatically."],
    baseline="Each line compares <b>pipelines reading other teams' tables with no agreement</b> to <b>a versioned contract checked in the producer's CI and at arrival</b>.",
    ratings=[(3, 3, "One more file per dataset."),
             (3, 4, "Fewer week-long outages from silent breaks."),
             (2, 5, "Breaking changes are blocked or versioned."),
             (3, 3, "Neutral."),
             (2, 4, "Works across many producing teams."),
             (3, 3, "Some upfront work saves firefighting."),
             (3, 3, "Neutral."),
             (2, 5, "Violations alert both teams at once."),
             (2, 4, "Producers change freely outside the contract.")],
    pitfalls=[("Contracts nobody checks", "A wiki page describes the schema; the next release ignores it.", "check it in CI and at arrival, automatically."),
              ("Contracts on raw tables", "Every internal refactor of the app becomes a contract change.", "publish a designed view or event, and contract that."),
              ("Imposed by the data team", "Producers see it as someone else's paperwork and route around it.", "agree it together; start with the few fields that matter."),
              ("Schema only", "Types match, but “amount” switched from net to gross.", "write meaning and rules too, and test ranges and sums.")],
    use=["Reports depend on another team's data.",
         "Several consumers use the same source.",
         "Sources change often or have broken pipelines before.",
         "Data leaves your company (partners, regulators)."],
    skip=["Your own team produces and consumes the data in one repository.",
          "Short-lived exploration.",
          "A source that never changes and has one consumer."],
    related=["<b>Change data capture</b> (Vol. 3)", "<b>Open host service</b> (Vol. 7)", "<b>Contract testing</b> (Vol. 4)", "<b>Quality checks and quarantine</b>"],
    quiz=[("What does a data contract contain?", "Fields and types, their meaning, quality rules, freshness, the owner and a version."),
          ("Where should the contract be checked first?", "In the producer's CI, so a breaking change fails before it's released."),
          ("How should a breaking change be handled?", "As a new version served alongside the old one, with a deprecation date."),
          ("Why contract a view or event rather than raw tables?", "So the producer can change its own tables freely while the published interface stays stable.")],
    quiz_sit=[("The checkout team says contracts will slow them down. Revenue broke three times this year from their changes. How do you start?",
               "Start small and together: a contract for the five order-line fields revenue depends on, checked in their CI with a tool that only fails on breaking changes to those fields. Everything else stays free. Show them the three incidents it would have caught.")],
    try_it="Write a contract for one source table your reports use: five fields, their meaning in one sentence each, two rules, a freshness limit and an owner. Show it to the team that owns the table and ask which line surprises them.",
    remember="A <span class=\"hl\">spec sheet</span> the producer owns. Changes come as a <span class=\"hl\">new version</span>, never a surprise.",
    sources=["Andrew Jones, <i>Driving Data Quality with Data Contracts</i> (2023).",
             "Bitol project, Open Data Contract Standard (ODCS).",
             "dbt documentation, “Model contracts”.",
             "Confluent documentation, “Schema evolution and compatibility”."],
)

# ------------------------------------------------------------------ 13 Quality Checks & Quarantine
qc_problem = Doodle(760, 260, "Doodle of bad rows reaching the report. After a till firmware update, the Delft shop sends prices in cents instead of euros, so a 39 euro kettle arrives as 3,900 euros. Delft's revenue jumps by 1.2 million euros. In the same batch, rows with no shop id disappear in an inner join. Both reach the report unnoticed.",
                    "A kettle at €3,900 and rows that silently vanish: both reach the report.")
qc_problem.table(20, 40, "till batch · Delft", ["kettle · €39", "kettle · €3,900", "mugs · shop: NULL"], w=260, fill="y", hl=(1,))
qc_problem.arrow(286, 100, 400, 100)
qc_problem.box(406, 50, 180, 100, "fct_sales", "blue", sub="loaded as is", size=21, subsize=15)
qc_problem.arrow(592, 100, 640, 100, color="red")
qc_problem.box(646, 60, 100, 80, "+€1.2M", "pink", stroke="red", size=20)
qc_problem.note(380, 220, "the NULL shop rows vanished in an inner join", "red")

qc_analogy = Doodle(760, 240, "Doodle of a factory quality line. Items pass an inspector. Bad items are pulled into a side bin with a tag saying why, and the line keeps running. If too many items are bad, the inspector pulls the cord and stops the line.",
                    "Pull bad items into a tagged bin; if too many are bad, stop the line.")
qc_analogy.line("M20 110 H740")
qc_analogy.msgs(40, 92, 5, fill="green", size=26, gap=12)
qc_analogy.icon("eye", 260, 70, 0.9)
qc_analogy.msgs(360, 92, 4, fill="green", size=26, gap=12)
qc_analogy.arrow(300, 120, 300, 180, color="red")
qc_analogy.icon("bin", 274, 176, 0.9, color="red")
qc_analogy.note(390, 214, "tag: price out of range", "red", anchor="start")
qc_analogy.box(560, 30, 180, 60, "stop the line", "pink", stroke="red", sub="if > 1 % bad", size=17, subsize=14)

qc_how = Doodle(760, 300, "Two levels of checks. Row checks run on every row: not null, accepted values, ranges, foreign keys. Failing rows go to a quarantine table with the reason and the batch id, and good rows continue. Batch checks run on the whole batch: row count and revenue against the usual band for that weekday, share of quarantined rows, duplicates, freshness. A failed batch check stops the publish.",
                 "Rows that fail go to quarantine with a reason. A batch that fails stops the publish.")
qc_how.box(20, 100, 150, 80, "batch", "y", size=22)
qc_how.arrow(176, 140, 230, 140)
qc_how.box(236, 90, 190, 100, "row checks", "blue", sub="null · range · FK", size=20, subsize=14)
qc_how.arrow(432, 120, 500, 70)
qc_how.arrow(432, 160, 500, 220, color="red")
qc_how.box(506, 30, 234, 80, "batch checks", "green", sub="count · sum · % bad", size=20, subsize=14)
qc_how.box(506, 190, 234, 80, "quarantine", "pink", stroke="red", sub="row · reason · batch id", size=20, subsize=14)
qc_how.note(623, 140, "fail → stop publish", "red")

QC = dict(
    slug="quality-checks",
    kicker="a.k.a. “data tests and a quarantine table”",
    tldr="Check data on every load, at two levels. <b>Row checks</b> (not null, accepted values, ranges, foreign keys) send failing rows to a <b>quarantine table</b> with a reason, so good rows keep flowing. <b>Batch checks</b> (row count, totals and the share of bad rows against the usual band) decide whether the batch may be <b>published at all</b>. Quarantined rows are fixed and replayed, never silently dropped.",
    chips=[("Family", "keeping it trustworthy"), ("Also called", "data tests, dead-letter table"), ("Lives in", "dbt tests, Great Expectations, Soda, Elementary"), ("Pairs with", "write–audit–publish, dead-letter queues")],
    problem="""  <p class="lead">After a till firmware update, the Delft shop sends prices <b>in cents</b>: the €39 kettle arrives as €3,900, and Delft's revenue jumps by <span class="hl-pink">€1.2 million</span>. In the same batch, rows with no shop id vanish in an inner join. Both problems reach the report, one loudly and one silently.</p>""",
    problem_figs=[qc_problem],
    analogy_side="the factory quality line",
    analogy="""  <p>On a factory line, an inspector pulls bad items into a <b>side bin with a tag</b> saying what's wrong, and the line keeps running. If too many items are bad, the inspector <b>pulls the cord and stops the line</b>, because something upstream is broken.</p>""",
    analogy_figs=[qc_analogy],
    map=[("The inspector", "Row checks on every incoming row"),
         ("The side bin", "The quarantine table"),
         ("The tag", "The failed rule, the batch id, the time"),
         ("Pulling the cord", "A batch check that stops publishing"),
         ("Reworking items from the bin", "Fixing and replaying quarantined rows")],
    how_side="rows to quarantine, batches to a gate",
    how="""  <p><b>Row checks</b> split each batch: good rows continue, bad rows go to quarantine with the reason. Nothing disappears silently. <b>Batch checks</b> look at the whole: is the row count or revenue far from the usual for this weekday, are more than 1 % of rows quarantined, are there duplicates, is the newest event recent? A failed batch check stops the publish (write–audit–publish), because a broken source is likely.</p>
  <p>Give each check a <b>severity</b>: warn (notify) or error (stop). Start with few, strong checks on what reports depend on.</p>""",
    how_figs=[qc_how],
    steps=[("List what reports depend on", "Keys, amounts, dates, shop and product ids."),
           ("Add row checks", "Not null, accepted values, ranges (0 &lt; price &lt; 2,000), foreign keys that resolve."),
           ("Route failures to quarantine", "Same columns plus reason, batch id, time; alert the owner."),
           ("Add batch checks with thresholds", "Count and sum within ±30 % of the same weekday's median; quarantined share &lt; 1 %."),
           ("Fix and replay", "Correct at the source or map in staging, then reprocess the quarantined rows.")],
    vocab=[("Row check", "A rule each row must pass."),
           ("Batch check", "A rule about the whole batch: volume, totals, duplicates."),
           ("Quarantine", "A table holding rejected rows and why."),
           ("Severity", "Warn (notify) or error (stop)."),
           ("Anomaly detection", "Flagging values far from their usual range."),
           ("Freshness check", "Is the newest data recent enough?")],
    code=dict(file="load_till_sales.sql + schema.yml", note="SQL · dbt tests", src="""
-- row checks: split the batch, never drop rows silently
INSERT INTO quarantine_till_sales
SELECT b.*, CASE WHEN b.shop_id IS NULL THEN 'shop_id missing'
                 WHEN b.unit_price NOT BETWEEN 0.01 AND 2000 THEN 'price out of range'
            END AS reason, :batch_id, now()
FROM   stg_till_batch b
WHERE  b.shop_id IS NULL OR b.unit_price NOT BETWEEN 0.01 AND 2000;

INSERT INTO stg_till_sales_clean
SELECT * FROM stg_till_batch
WHERE  shop_id IS NOT NULL AND unit_price BETWEEN 0.01 AND 2000;

# schema.yml · batch-level checks in dbt
models:
  - name: fct_sales
    tests:
      - dbt_utils.expression_is_true:
          expression: "(select count(*) from quarantine_till_sales where batch_id = '{{ var('batch_id') }}') < 0.01 * (select count(*) from stg_till_batch)"
    columns:
      - name: order_line_id
        tests: [unique, not_null]
"""),
    tools="tools: dbt tests and dbt-expectations, Great Expectations, Soda, Elementary and Monte Carlo (anomaly detection), Deequ for Spark, Dataform assertions.",
    gains=["<b>Bad rows don't reach reports</b>, and good rows aren't held back.",
           "<b>Nothing vanishes silently</b>: every rejected row has a reason.",
           "<b>Broken sources are caught</b> by volume and sum checks.",
           "<b>Fix and replay</b> instead of hand-editing facts."],
    losses=["<b>Checks to write and tune</b>: too loose misses, too strict cries wolf.",
            "<b>Quarantine needs an owner</b>, or it fills up unread.",
            "<b>Reports can be incomplete</b> while rows wait in quarantine.",
            "<b>Extra compute</b> on every load."],
    baseline="Each line compares <b>loading everything that arrives</b> to <b>row checks with quarantine and batch checks that gate publishing</b>.",
    ratings=[(3, 3, "A few rules and one extra table."),
             (3, 3, "Neutral, unless a batch check stops a publish."),
             (2, 5, "Bad rows are caught and nothing disappears."),
             (3, 4, "Quarantined rows replay through the same path."),
             (3, 3, "Neutral."),
             (4, 3, "Checks cost a little compute."),
             (3, 3, "Neutral."),
             (1, 5, "Every failure has a rule, a reason and an alert."),
             (3, 3, "New columns need new checks.")],
    pitfalls=[("Inner joins as filters", "Rows with a missing key vanish without a trace.", "check foreign keys explicitly; quarantine or use an unknown member."),
              ("Alert fatigue", "Fifty warnings a day, all ignored, including the real one.", "few checks, tuned thresholds, error only on what matters."),
              ("Quarantine nobody reads", "Thousands of rows rot there; revenue is quietly short.", "an owner, a daily count on the dashboard, and an age limit."),
              ("Fixed thresholds", "“At least 90,000 rows” fails every Sunday and every holiday.", "compare with the same weekday's median, or use anomaly detection.")],
    use=["Every load that feeds a report people act on.",
         "Sources you don't control: tills, partners, spreadsheets.",
         "Data with known valid ranges.",
         "Pipelines with write–audit–publish."],
    skip=["Raw landing: keep everything there, check downstream.",
          "Exploratory data where “bad” isn't defined yet.",
          "Duplicating checks the source already enforces with constraints you trust."],
    related=["<b>Write–audit–publish</b>", "<b>Idempotent loads</b>", "<b>Data contracts</b>", "<b>Late-arriving data</b>"],
    quiz=[("What is the difference between row checks and batch checks?", "Row checks judge each row and quarantine failures; batch checks judge the whole batch and can stop publishing."),
          ("Why quarantine instead of dropping bad rows?", "So nothing disappears silently: rows can be fixed and replayed, and counted."),
          ("Why compare volume with the same weekday rather than a fixed number?", "Volume varies by weekday and season; a fixed threshold either misses problems or fails every Sunday."),
          ("What should happen when 5 % of a batch is quarantined?", "A batch check should fail and stop the publish, because a source is probably broken.")],
    quiz_sit=[("A new shop opens and its till sends a product code the warehouse doesn't know. Its sales are missing from the report. What should have happened, and what do you build?",
               "The rows should have gone to quarantine with “unknown product” and alerted the owner, or loaded against an unknown-member product key. Add a foreign-key row check with quarantine, a daily quarantine count on the dashboard, and a replay once the product is added.")],
    try_it="Take a day of real data and write three row checks and two batch checks. Run them, and look at what the quarantine table catches. Then change one threshold to the same weekday's median and see which alerts disappear.",
    remember="Bad items to the <span class=\"hl\">tagged bin</span>. Too many? <span class=\"hl\">Stop the line</span>.",
    sources=["dbt documentation, “Data tests” and the dbt-expectations package.",
             "Great Expectations documentation, “Expectations”.",
             "Barr Moses, Lior Gavish and Molly Vorwerck, <i>Data Quality Fundamentals</i> (2022).",
             "Amazon Deequ, “Unit tests for data” (2018)."],
)

# ------------------------------------------------------------------ 14 DAG Orchestration & Lineage
dag_problem = Doodle(760, 260, "Doodle of jobs scheduled by the clock. Extract is set for 01:00, transforms for 03:00, dashboard refresh for 06:00. One night the extract runs until 03:40, so the transforms run at 03:00 on half the data and the dashboards refresh with half a day. Nobody can tell which reports used the broken table.",
                     "Jobs on a clock: the extract runs late, and everything after it runs on half the data.")
dag_problem.line("M30 180 H730")
for x, t in [(60, "01:00"), (300, "03:00"), (380, "03:40"), (660, "06:00")]:
    dag_problem.line(f"M{x} 172 v16")
    dag_problem.note(x, 210, t)
dag_problem.box(60, 30, 320, 50, "extract", "blue", size=20)
dag_problem.box(300, 100, 160, 50, "transform", "pink", stroke="red", size=20)
dag_problem.box(600, 100, 140, 50, "refresh", "pink", stroke="red", size=20)
dag_problem.note(380, 245, "transform started on half the data · which dashboards are wrong?", "red")

dag_analogy = Doodle(760, 240, "Doodle of baking a cake. Bake, then cool, then ice. You ice when the cake has cooled, not at three o'clock. If the cake burns, you know exactly which steps after it to redo.",
                     "Ice the cake when it has cooled, not at three o'clock.")
dag_analogy.row([("bake", "40 min", "y"), ("cool", "until cold", "blue"), ("ice", "when cool", "green")], y=40, h=90, gap=60, size=22, subsize=15, arrows=True)
dag_analogy.icon("clock", 660, 150, 0.8, color="red")
dag_analogy.note(380, 200, "the trigger is “cool”, not “15:00”", "pen")

dag_how = Doodle(760, 300, "A dependency graph. Extract orders and extract products feed staging models, which feed fact sales and dim product, which feed the revenue dashboard and the stock report. The scheduler runs a step only when everything it depends on has succeeded for that day. The same graph is the lineage: from the dashboard you can trace back to the sources, and from a broken source forward to every affected report.",
                 "Each step runs when its inputs are ready. The same graph tells you what feeds what.")
nodes = {"x_orders": (20, 30), "x_products": (20, 190), "stg_orders": (210, 30), "stg_products": (210, 190),
         "fct_sales": (400, 30), "dim_product": (400, 190), "revenue": (590, 30), "stock report": (590, 190)}
for name, (x, y) in nodes.items():
    dag_how.box(x, y, 150, 56, name, "green" if x == 590 else ("y" if x == 20 else "blue"), size=17)
for a, b in [("x_orders", "stg_orders"), ("x_products", "stg_products"), ("stg_orders", "fct_sales"), ("stg_products", "dim_product"),
             ("stg_products", "fct_sales"), ("fct_sales", "revenue"), ("dim_product", "revenue"), ("dim_product", "stock report")]:
    (x1, y1), (x2, y2) = nodes[a], nodes[b]
    dag_how.arrow(x1 + 154, y1 + 28, x2 - 4, y2 + 28)
dag_how.note(380, 280, "run when inputs are ready · trace back to sources · trace forward to reports", "pen", size=16)

DAG = dict(
    slug="dag-orchestration",
    kicker="a.k.a. “run on readiness, not on the clock”",
    tldr="Describe the pipeline as a <b>graph of steps and their inputs</b> (a DAG), and let a scheduler run each step <b>when everything it depends on has succeeded</b> for that period, with retries and alerts. Runs are per period (logical date), so backfills are the same graph for old dates. The same graph is your <b>lineage</b>: trace a wrong number back to its source, and a broken source forward to every affected report.",
    chips=[("Family", "keeping it trustworthy"), ("DAG", "directed acyclic graph"), ("Lives in", "Airflow, Dagster, Prefect, dbt"), ("Pairs with", "idempotent loads, write–audit–publish")],
    problem="""  <p class="lead">Three cron jobs: extract at 01:00, transforms at 03:00, dashboard refresh at 06:00. One night the extract runs until 03:40. The transforms start at 03:00 on <span class="hl-pink">half the data</span>, the dashboards refresh with half a day, and when finance asks which reports are wrong, nobody can say.</p>
  <ul>
    <li>Timings are guesses; slack is added until the pipeline takes all night.</li>
    <li>A failure upstream doesn't stop the steps after it.</li>
    <li>There's no map of what feeds what.</li>
  </ul>""",
    problem_figs=[dag_problem],
    analogy_side="baking a cake",
    analogy="""  <p>You bake, then cool, then ice. You <b>ice when the cake has cooled</b>, not at three o'clock. If the cake burns, you know exactly which steps to redo, and which other dishes used the same oven batch.</p>""",
    analogy_figs=[dag_analogy],
    map=[("Bake, cool, ice", "Steps in a DAG"),
         ("“When it's cool”", "Run when upstream steps have succeeded"),
         ("Not at 15:00", "No fixed clock times between steps"),
         ("Redo the steps after the burnt cake", "Rerun downstream of a fixed step"),
         ("Which dishes used that oven batch", "Lineage: downstream impact")],
    how_side="steps, dependencies, periods",
    how="""  <p>Each step declares its inputs. The scheduler starts the graph on a schedule (or when new data arrives) and runs each step as soon as its inputs succeeded for the same period, with retries and backoff. If a step fails, nothing downstream runs, and the owner is alerted. Each run is for a <b>logical date</b>, so a backfill is the same graph run for old periods, which only works if every step is idempotent.</p>
  <p>Because dependencies are declared, the graph doubles as <b>lineage</b>: tools draw it, and you can ask “what feeds this dashboard?” or “what breaks if this source is late?”.</p>""",
    how_figs=[dag_how],
    steps=[("Declare inputs, not times", "Each step lists what it reads; only the first step has a schedule."),
           ("Run per period", "Pass the logical date to every step; no <code>now()</code>."),
           ("Retry, then alert", "Retries with backoff for flaky sources; a clear owner when retries run out."),
           ("Set deadlines", "Alert if the revenue dashboard isn't fresh by 07:00, whatever the reason."),
           ("Publish lineage", "Table- and column-level lineage from the DAG and SQL, so impact is one click away.")],
    vocab=[("DAG", "A directed acyclic graph: steps and dependencies, no cycles."),
           ("Task / asset", "One step, or the table it produces (Dagster's view)."),
           ("Logical date", "The period a run is for."),
           ("Sensor", "A step that waits for data to arrive."),
           ("Lineage", "Which datasets each dataset is derived from."),
           ("SLA miss", "A deadline passed without fresh data.")],
    code=dict(file="sales_daily.py", note="Airflow 2 TaskFlow", src="""
from airflow.decorators import dag, task
from pendulum import datetime

@dag(schedule="0 1 * * *", start_date=datetime(2026, 1, 1), catchup=False,
     default_args={"retries": 3, "retry_exponential_backoff": True})
def sales_daily():
    @task
    def extract(table, ds=None):          # ds = the logical date, passed in
        load_raw(table, day=ds)

    @task
    def transform(ds=None):               # dbt build for that day, tests included
        run_dbt("build --select fct_sales+", vars={"day": ds})

    @task
    def refresh_dashboards(ds=None):
        refresh("revenue", day=ds)

    [extract("orders"), extract("order_lines"), extract("products")] >> transform() >> refresh_dashboards()

sales_daily()
"""),
    tools="tools: Apache Airflow (datasets for data-aware scheduling), Dagster (software-defined assets, partitions), Prefect, dbt (the DAG from <code>ref()</code>), cloud schedulers; lineage with OpenLineage and Marquez, DataHub, dbt docs.",
    gains=["<b>Steps run when inputs are ready</b>: no guessing, no slack.",
           "<b>Failures stop downstream</b> instead of spreading.",
           "<b>Backfills are just runs</b> for old periods.",
           "<b>Lineage for free</b>: impact and root cause in a click."],
    losses=["<b>A scheduler to run</b> and keep upgraded.",
            "<b>Python and config</b> to learn.",
            "<b>One broken step blocks</b> everything after it (on purpose).",
            "<b>Graphs grow</b> into hundreds of steps without naming rules."],
    baseline="Each line compares <b>independent cron jobs at fixed times</b> to <b>a DAG run per period with dependencies, retries and lineage</b>.",
    ratings=[(3, 3, "A scheduler to learn, but the graph is visible."),
             (2, 4, "Steps start as soon as inputs are ready."),
             (2, 4, "Nothing runs on half-finished inputs."),
             (2, 5, "Backfill any period with the same graph."),
             (2, 4, "Many pipelines, parallel steps, one scheduler."),
             (3, 3, "Scheduler costs offset by less slack."),
             (3, 3, "Neutral."),
             (1, 5, "Failures, deadlines and lineage in one place."),
             (2, 4, "New steps declare their inputs and fit in.")],
    pitfalls=[("Times between steps", "Each task still has its own cron time inside the scheduler.", "schedule only the start; everything else waits on dependencies."),
              ("Non-idempotent tasks", "Retries and backfills duplicate data.", "make every task safe to run twice for the same period."),
              ("Work inside the scheduler", "Heavy transforms run on the scheduler's workers and starve it.", "the scheduler triggers; the warehouse or a job runner does the work."),
              ("Lineage that stops at the warehouse", "Nobody knows which dashboards use a table.", "include BI dashboards and exports in lineage.")],
    use=["More than two steps that depend on each other.",
         "Pipelines that are retried or backfilled.",
         "Several teams' pipelines sharing tables.",
         "Deadlines that matter (“fresh by 07:00”)."],
    skip=["One script that runs once a day and nothing depends on.",
          "Pure streaming pipelines; they run continuously.",
          "Replacing a scheduler you have with another for fashion."],
    related=["<b>Idempotent loads</b>", "<b>Write–audit–publish</b>", "<b>Layered zones</b>", "<b>Saga</b> (Vol. 1)"],
    quiz=[("What does a DAG scheduler use to decide when a step runs?", "Whether all the step's upstream dependencies succeeded for the same period."),
          ("Why pass a logical date to every task?", "So each run is for a specific period and backfills rerun the same code for old dates."),
          ("What does lineage let you answer?", "What a dataset is built from, and what is affected if a source is broken or late."),
          ("Why must tasks be idempotent?", "Schedulers retry them and backfills rerun them; they must not duplicate data.")],
    quiz_sit=[("Finance asks every Monday “is the dashboard right today?”. Your jobs are cron entries an hour apart. What do you build first?",
               "Put the jobs in one DAG with declared dependencies so nothing runs on half-finished inputs, add a freshness deadline alert for 07:00, and show “data as of” on the dashboard. Then finance sees the answer before asking.")],
    try_it="Draw your pipeline as boxes and arrows from sources to dashboards. Mark every arrow that is really a time gap between cron jobs. Pick one and replace it with a dependency in your scheduler.",
    remember="Ice it when it's <span class=\"hl\">cool</span>, not at three. The <span class=\"hl\">graph</span> is also the map.",
    sources=["Apache Airflow documentation, “DAGs”, “Data-aware scheduling” and “Backfill”.",
             "Dagster documentation, “Software-defined assets” and “Partitions”.",
             "OpenLineage specification.",
             "Maxime Beauchemin, “The Rise of the Data Engineer” (2017)."],
)

NOTES = [WAP, DC, QC, DAG]
