# Plan: ETL, data warehousing and reporting

Status **2026-11-25**: plan written; **deep dive 12 · From App Database to Warehouse** is drafted
(`content/deep-dives/app_db_to_warehouse.py`, `/deep-dives/app-db-to-warehouse/`). The volume below is
planned (`PLANNED` in `scripts/build_notes.py`), not started.

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

## 2. Vol. 10 · Data Pipelines & Analytics (18 notes, Series 1)

Same note format as the other Series 1 volumes: problem, analogy, how it works, gains vs losses, nine
ratings, pitfalls, when to use it, quiz. Notes with a long history get a **then & now** box (as in Vols. 7–8).

- **Journal key** `pipelines`, URL `/pipelines/`.
- **Paper** (proposal): continuous-form *green-bar* printout paper, with sprocket holes down both sides,
  titles in a dot-matrix face and a “RUN COMPLETE” stamp. Palette: green-bar green, ink navy, highlighter orange.
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
| 12 | **From App Database to Warehouse** | Vol. 3 CDC, Upserts, Star Schema (partitioning in passing) | drafted |
| — | **History in the Warehouse** (SCD and point-in-time) | Vol. 3 history tables, bitemporal, star schema; Vol. 10 SCD | ready to write |
| — | **Reruns and Backfills** (“rerun anything”) | Vol. 10 incremental extract, idempotent loads, late data | after Vol. 10 |
| — | **One Number Everywhere** (the metrics layer: fan and chasm traps, grain, caching, row-level security) | Vol. 10 metrics layer, aggregates | after Vol. 10 |
| — | **Data Quality and Pipeline Observability** | Vol. 10 WAP, contracts, quality checks; pairs with Observability & SLOs | after Vol. 10 |
| — | **Streaming Analytics** (windows, watermarks, exactly-once sinks) | Vol. 10 lambda vs kappa, late data | after Vol. 10 |
| — | **Lakehouse Tables** (Iceberg and Delta internals) | reserve note on open table formats | optional |

Deep dive 12 links only to the CDC, Upserts and Star Schema notes (`notes=`): the partitioning note
already links to Sharding & Partitioning, and a note has room for one “go deeper” link.

## 4. Cheat sheet

**Dimensional Modelling & Warehouse SQL** (4 pages, `content/cheatsheets/warehouse.py`): the grain → facts →
dimensions checklist with a bus-matrix figure; SCD types side by side; load patterns (append, partition
overwrite, MERGE with a newer-only guard, dedupe by key); dbt incremental and snapshot configs; reconciliation queries.

## 5. Order of work

1. Deep dive 12 (this branch). Owner reviews it on a phone and on desktop.
2. Vol. 10, one collection per PR, in the order above.
3. The cheat sheet, once collection B (modelling) exists.
4. Deep dives: History in the Warehouse, then Reruns and Backfills, then One Number Everywhere.

## 6. Questions for the owner

- Volume number: Vol. 10 after AI App Patterns (Vol. 9), or swap them?
- The green-bar printout skin, or another paper?
- Keep the shop example for the whole volume, or move the volume into the Larder story (Series 2)?
