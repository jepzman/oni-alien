# Plan: ETL, data warehousing and reporting

Status **2026-11-25**: **deep dive 12 · From App Database to Warehouse** is written
(`content/deep-dives/app_db_to_warehouse.py`), and **Vol. 9 · Data Pipelines & Analytics** is written: 18 notes in
`content/pipelines/` (`01_in.py`, `02_model.py`, `03_trust.py`, `04_serve.py`).

Owner's decisions (25 Nov): the volume moves ahead of AI App Patterns (now Vol. 10); keep the homeware-shop example;
keep the green-bar printout look.

## 1. What is already on the shelf

Vol. 3 · Data & Database Patterns already covers the building blocks, and the new work links to them
rather than repeating them:

| Vol. 3 note | Used by |
| --- | --- |
| Change Data Capture (with a going-deeper chapter) | extract, deep dive 12 |
| Upserts | idempotent loads, deep dive 12 |
| Star Schema | every modelling note, deep dive 12 |
| Materialized Views | aggregates and rollups |
| History Tables, Bitemporal Data | slowly changing dimensions |
| Table Partitioning | partition overwrite, backfills |
| Multitenancy | multi-tenant reporting |

What is missing is the **pipeline** (how data gets from the app into the warehouse and stays right),
the **warehouse modelling** past one star, and **serving reports** (one number, everywhere).

## 2. Vol. 9 · Data Pipelines & Analytics (18 notes, Series 1)

Same note format as the other Series 1 volumes: problem, analogy, how it works, gains vs losses, nine
ratings, pitfalls, when to use it, quiz. Notes with a long history get a **then & now** box (as in Vols. 7–8).

- **Journal key** `pipelines`, URL `/pipelines/`.
- **Paper**: continuous-form *green-bar* printout paper, with sprocket holes down both sides, titles in a
  dot-matrix face (VT323) and a “RUN COMPLETE” stamp. Palette: green-bar green, ink navy, highlighter orange
  (`theme-pipelines` in `public/assets/bujo.css`; cover `--cover-pipelines` / `--band-pipelines`).
- **Then & now** boxes on the seven notes built on older books: ETL vs ELT, SCD, fact table types, conformed
  dimensions, data vault, one big table, lambda vs kappa. The journal has no `then_now` flag, so the index
  doesn't claim every note has one.
- **Ratings** (`PIPELINE_ATTRS`): simplicity, freshness, correctness, replayability, scalability, cost,
  query flexibility, observability, evolvability.

| # | Collection | Note | Slug | Links to |
| --- | --- | --- | --- | --- |
| 01 | Getting data in | ETL vs ELT (then & now) | `etl-vs-elt` | Vol. 3 star schema |
| 02 | Getting data in | Incremental Extract (high-water mark) | `incremental-extract` | Vol. 3 CDC |
| 03 | Getting data in | Idempotent Loads (partition overwrite, MERGE) | `idempotent-loads` | Vol. 3 upserts, partitioning |
| 04 | Getting data in | Layered Zones (raw → staging → marts, “medallion”) | `layered-zones` | |
| 05 | Getting data in | Late-Arriving Data (event time vs load time) | `late-arriving-data` | Vol. 3 bitemporal |
| 06 | Modelling the warehouse | Slowly Changing Dimensions (types 1, 2, 3, 6) | `slowly-changing-dimensions` | Vol. 3 history tables, bitemporal |
| 07 | Modelling the warehouse | Fact Table Types (transaction, periodic, accumulating, factless) | `fact-table-types` | Vol. 3 star schema |
| 08 | Modelling the warehouse | Conformed Dimensions and the Bus Matrix | `conformed-dimensions` | Vol. 7 bounded contexts |
| 09 | Modelling the warehouse | Data Vault (hubs, links, satellites) | `data-vault` | |
| 10 | Modelling the warehouse | One Big Table vs Star (then & now: Kimball, Inmon, columnar) | `one-big-table` | Vol. 3 normalization |
| 11 | Keeping it trustworthy | Write–Audit–Publish | `write-audit-publish` | Vol. 6 blue-green |
| 12 | Keeping it trustworthy | Data Contracts | `data-contracts` | Vol. 3 CDC (“tables are not a contract”) |
| 13 | Keeping it trustworthy | Quality Checks and Quarantine | `quality-checks` | Vol. 1 dead-letter queues |
| 14 | Keeping it trustworthy | DAG Orchestration and Lineage | `dag-orchestration` | |
| 15 | Serving reports | Semantic / Metrics Layer | `metrics-layer` | |
| 16 | Serving reports | Aggregates, Rollups and Cubes (OLAP) | `aggregates-rollups` | Vol. 3 materialized views |
| 17 | Serving reports | Lambda vs Kappa | `lambda-vs-kappa` | Vol. 1 event sourcing |
| 18 | Serving reports | Multi-tenant and Embedded Reporting | `embedded-reporting` | Vol. 3 multitenancy, Vol. 5 least privilege |

Reserve list (swap in, or add as extra notes later): open table formats (Iceberg, Delta: snapshots,
time travel), reverse ETL, the operational data store, data mesh.

**Example thread.** One homeware shop with a web store and 30 shops, the same as deep dive 12:
orders, order lines, products, customers. Notes may use their own small examples where the shop does not fit.

## 3. Deep dives (Series 3)

Each meets the three tests in `docs/HANDOFF-deep-dives.md` §1: real failure timelines, more than one
serious variant, an operations story.

| # | Deep dive | Builds on | Status |
| --- | --- | --- | --- |
| 12 | **From App Database to Warehouse** | Vol. 3 CDC, Upserts, Star Schema; Vol. 9 extract, loads, zones | written |
| — | **History in the Warehouse** (SCD and point-in-time) | Vol. 3 history tables, bitemporal, star schema; Vol. 9 SCD | written (13) |
| — | **Reruns and Backfills** (“rerun anything”) | Vol. 9 incremental extract, idempotent loads, late data | ready to write |
| — | **One Number Everywhere** (the metrics layer: fan and chasm traps, grain, caching, row-level security) | Vol. 9 metrics layer, aggregates | ready to write |
| — | **Data Quality and Pipeline Observability** | Vol. 9 WAP, contracts, quality checks; pairs with Observability & SLOs | ready to write |
| — | **Streaming Analytics** (windows, watermarks, exactly-once sinks) | Vol. 9 lambda vs kappa, late data | ready to write |
| — | **Lakehouse Tables** (Iceberg and Delta internals) | reserve note on open table formats | optional |

Deep dive 12 links from the CDC, Upserts and Star Schema notes and from Vol. 9's incremental extract,
idempotent loads and layered zones (`notes=`). The partitioning note already links to Sharding & Partitioning,
and a note has room for one “go deeper” link.

## 4. Cheat sheet

**Data Warehouse** (written 25 Nov, `content/cheatsheets/warehouse.py`, `/cheatsheets/warehouse/`), four cards: modelling
(design steps, fact table types, grain, additivity, bus matrix, keys, dim_date, naming), history (SCD types, type 2
columns and load, point-in-time lookup, three pasts, traps), loading (load patterns, latest row per key, MERGE newer-only,
watermark extract, late data, three clocks, dbt incremental, backfill) and trust & serving (reconciliation, data tests,
drill across, aggregates, metrics, row-level security, freshness). Linked from nine Vol. 9 notes and the star schema
note (`CARD_LINKS`).

## 5. Order of work

1. Deep dive 12 and Vol. 9 (done, one PR). Owner reviews on a phone and on desktop.
2. The cheat sheet and deep dive 13, History in the Warehouse (done, 25 Nov).
3. Deep dives: Reruns and Backfills, then One Number Everywhere.

## 6. Next

- Going-deeper chapters for Vol. 9 (in `content/pipelines/deeper.py`) once the deep dives above exist.
