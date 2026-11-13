#!/usr/bin/env python3
"""Builds the Jef’s Notes bookshelf.

Each journal (see JOURNALS) lives in public/<key>/:
  - notes written as data in content/<key>/*.py are rendered into public/<key>/notes/<slug>.html
  - hand-made notes listed in `handmade` are left alone
  - index.html (the journal index) and all.html (the whole journal, for PDF) are rebuilt
public/index.html is the landing page (the shelf + future log), public/journals.json lists
everything for the PDF script, and a few redirect pages keep old links working.

Usage: python3 scripts/build_notes.py
"""
import hashlib
import importlib.util
import json
import re
import sys
from datetime import date, timedelta
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from doodle import Doodle, esc, highlight  # noqa: E402
import cheatsheet  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
PUBLIC = ROOT / "public"
CONTENT = ROOT / "content"
AUTHOR = "Jefrey Romel Tagunicar"

# ---------------------------------------------------------------- the nine ratings, per journal
DISTRIBUTED_ATTRS = [
    ("Simplicity", "easy to understand?", "Fewer moving parts, fewer surprises."),
    ("Low cost", "cheap to build &amp; run?", "Infrastructure, tooling and people. High = cheap."),
    ("Deployability", "safe, easy releases?", "Small, independent, safe releases."),
    ("Testability", "test with confidence?", "Isolated parts with clear contracts."),
    ("Scalability", "more users &amp; data?", "Handles more users and data by adding machines."),
    ("Elasticity", "sudden spikes?", "Scales up and back down quickly for spikes."),
    ("Fault tolerance", "failure stays contained?", "One failure stays contained."),
    ("Performance", "fast typical request?", "How fast a typical request is."),
    ("Evolvability", "easy to change?", "How easily the system can change shape."),
]
FRONTEND_ATTRS = [
    ("Simplicity", "easy to follow?", "A new teammate can read it and predict what happens."),
    ("Reusability", "use it in many places?", "The same piece works across screens, apps or brands."),
    ("Testability", "test with confidence?", "Logic and UI can be tested without a browser full of mocks."),
    ("Maintainability", "safe to change?", "A change in one place doesn't break five others."),
    ("Performance", "fast to load &amp; respond?", "Time to first content, time to interactive, smooth updates."),
    ("Bundle size", "ships little JS?", "How much code users download. High = small."),
    ("Accessibility", "works for everyone?", "Keyboard, screen readers, focus, motion and contrast."),
    ("Developer experience", "pleasant to build with?", "Fast feedback, clear errors, little boilerplate."),
    ("Team scalability", "many devs at once?", "Teams can work in parallel without stepping on each other."),
]
DATA_ATTRS = [
    ("Simplicity", "easy to reason about?", "A new teammate can read the schema and the queries and predict what happens."),
    ("Read speed", "fast queries?", "How quickly the typical reads come back."),
    ("Write speed", "cheap inserts &amp; updates?", "How much work each insert, update or delete costs."),
    ("Integrity", "data stays correct?", "Constraints and transactions that stop wrong, duplicate or lost rows."),
    ("Scalability", "10× more rows?", "Keeps working when tables and traffic grow by 10× or 100×."),
    ("Low storage cost", "cheap to keep?", "Disk, memory, indexes and backups. High = cheap."),
    ("Query flexibility", "answer new questions?", "New and ad-hoc questions are easy to ask with plain SQL."),
    ("Operability", "calm to run?", "Backups, migrations, monitoring and on-call stay boring."),
    ("Evolvability", "easy to change shape?", "Adding columns, tables and features without big rewrites."),
]
TESTING_ATTRS = [
    ("Simplicity", "easy to read &amp; write?", "A teammate can read a test and know what it checks and why."),
    ("Fast feedback", "quick to run?", "How soon you learn something broke: seconds, not an hour."),
    ("Confidence", "catches real bugs?", "A green run really means the feature works."),
    ("Reliability", "no flaky runs?", "Same code, same result, every time, on every machine."),
    ("Isolation", "pinpoints the fault?", "A red test points at one cause instead of fifty."),
    ("Maintainability", "survives refactors?", "Tests change when behaviour changes, not when internals move."),
    ("Realism", "close to production?", "Real databases, browsers, networks and data shapes."),
    ("Low cost", "cheap to write &amp; run?", "Authoring time, CI minutes and infrastructure. High = cheap."),
    ("Scalability", "grows with the code?", "Still fast and useful at 10× the code and 10× the team."),
]
SECURITY_ATTRS = [
    ("Simplicity", "easy to get right?", "Few moving parts, so the secure path is also the obvious one."),
    ("Usability", "little friction?", "Users and admins aren't pushed to work around it. High = smooth."),
    ("Confidentiality", "secrets stay secret?", "Data and credentials are only seen by those allowed to see them."),
    ("Integrity", "can't be tampered with?", "Data and actions can't be changed or forged without detection."),
    ("Availability", "stays up under attack?", "Keeps serving real users, even when someone is trying to break it."),
    ("Containment", "small blast radius?", "One stolen key or broken part only exposes a little. High = small."),
    ("Auditability", "can we tell what happened?", "Who did what, when and from where can be answered afterwards."),
    ("Low cost", "cheap to build &amp; run?", "Tools, infrastructure and people time. High = cheap."),
    ("Developer experience", "easy to build with?", "Developers can follow it without being security experts."),
]
ARCHITECT_ATTRS = [
    ("Clarity", "easy to understand?", "A newcomer can understand the system and the reasoning behind it."),
    ("Stakeholder alignment", "everyone agrees?", "Business, product and engineering share the same what and why."),
    ("Decision speed", "decide &amp; move on?", "How quickly the team can choose and get back to building."),
    ("Risk reduction", "unknowns found early?", "The big risks are surfaced and handled before they bite."),
    ("Adaptability", "easy to change course?", "How cheaply the direction can change later."),
    ("Traceability", "why did we do that?", "Months later, anyone can find why something was done."),
    ("Cost awareness", "cost visible when choosing?", "Money and effort are part of the decision, not a surprise."),
    ("Low overhead", "light to run?", "Time and ceremony it takes. High = light."),
    ("Team autonomy", "teams can act alone?", "Teams can decide and act without waiting for the architect."),
]
PRODUCT_ATTRS = [
    ("Customer value", "solves a real problem?", "Customers would notice it, and miss it if it went."),
    ("Business impact", "moves a driver?", "It shows up in a number the business already tracks."),
    ("Evidence", "based on facts?", "Decided on what we learned, not on opinion or rank."),
    ("Learning speed", "find out fast?", "How soon we know if we're wrong."),
    ("Focus", "fewer, better things?", "The team works on a few things at once, and knows which matter most."),
    ("Shared understanding", "team knows why?", "Everyone can explain what we're building, for whom and why."),
    ("Stakeholder trust", "they believe us?", "Leaders and partners trust the plan and the updates."),
    ("Flow", "small steps to customers?", "Value reaches customers in small, frequent steps."),
    ("Low overhead", "light to run?", "Time and ceremony it takes. High = light."),
]
CLOUD_ATTRS = [
    ("Simplicity", "easy to run &amp; explain?", "Few moving parts; the on-call person can understand it at 3 a.m."),
    ("Delivery speed", "fast from commit to prod?", "Short lead time and frequent, small releases."),
    ("Release safety", "low risk per deploy?", "A bad change reaches few users and is easy to undo."),
    ("Reliability", "stays up?", "Users get a working service; failures are rare and short."),
    ("Scalability", "handles 10× load?", "Capacity grows with demand without redesign."),
    ("Recoverability", "fast to restore?", "How quickly you get back after a failure or disaster."),
    ("Observability", "can we see inside?", "You can tell what's wrong, and where, from the outside."),
    ("Low cost", "cheap to run?", "Cloud bill, tooling and people time. High = cheap."),
    ("Developer experience", "pleasant to ship with?", "Self-service, fast feedback, little toil."),
]

# ---------------------------------------------------------------- journals
JOURNALS = [
    dict(
        key="distributed", vol=1, title="Distributed Design Patterns", short="distributed design patterns",
        theme="", subject="distributed systems", term="Fall term · 2026", weekdays=(0, 2, 4), start=date(2026, 9, 7),
        kicker="property of a very caffeinated student",
        lead="My class notes on <span class=\"hl\">distributed design patterns</span>, written up properly. {n} patterns in {c} collections. Each note covers the problem a pattern solves, a real-life analogy with doodles, how it works, what you gain and lose, how it scores on nine architecture characteristics, and the mistakes people make with it.",
        blurb="Resilience, data consistency, communication, scaling data and coordination for systems that run on more than one machine.",
        attrs=DISTRIBUTED_ATTRS, attrs_title="The nine ratings", ratings_h2="Architecture ratings", attrs_side="architecture characteristics",
        handmade={"circuit-breaker", "saga"},
        collections=[
            ("resilience", "Resilience", "keep one failure from becoming everyone's failure"),
            ("consistency", "Data consistency", "keep data correct across services and databases"),
            ("communication", "Communication", "how services find and talk to each other"),
            ("data", "Scaling data", "store and read more data, faster"),
            ("coordination", "Coordination", "agree on who does what"),
        ],
        catalogue=[
            (1, "circuit-breaker", "Circuit Breaker", "resilience", "Stop calling a dependency that keeps failing; fail fast with a fallback, then test carefully."),
            (2, "retry-backoff", "Retry with Backoff", "resilience", "Try again after short failures, with timeouts, growing random waits and a limit."),
            (3, "bulkhead", "Bulkhead", "resilience", "Give each dependency its own pool of resources so one leak can't sink the ship."),
            (4, "rate-limiter", "Rate Limiter", "resilience", "Cap how many requests each client can make, so nobody can flood the service."),
            (5, "saga", "Saga", "consistency", "A transaction across services as local steps, with compensating “undo” steps when one fails."),
            (6, "transactional-outbox", "Transactional Outbox", "consistency", "Save the change and the event in one transaction, then publish the event reliably."),
            (7, "idempotent-consumer", "Idempotent Consumer", "consistency", "Handle the same message twice without doing the work twice."),
            (8, "event-sourcing", "Event Sourcing", "consistency", "Store every change as an event and rebuild the current state from the log."),
            (9, "cqrs", "CQRS", "consistency", "Use one model to change data and separate, fast models to read it."),
            (10, "api-gateway", "API Gateway", "communication", "One front door for clients that routes, authenticates and shapes requests."),
            (11, "publish-subscribe", "Publish–Subscribe", "communication", "Announce events once; anyone interested subscribes, nobody calls each other."),
            (12, "competing-consumers", "Competing Consumers", "communication", "Many workers pull from one queue so load is shared and spikes are smoothed."),
            (13, "sidecar", "Sidecar & Service Mesh", "communication", "Move networking chores into a helper process that runs next to every service."),
            (14, "service-discovery", "Service Discovery", "communication", "Look up where a service is running right now instead of hard-coding addresses."),
            (15, "sharding", "Sharding", "data", "Split data across many databases by a key, so each holds only a slice."),
            (16, "replication", "Leader–Follower Replication", "data", "Copy data to followers for reads and failover; one leader takes the writes."),
            (17, "cache-aside", "Cache-Aside", "data", "Check a fast cache first; on a miss, load from the database and keep a copy."),
            (18, "leader-election", "Leader Election", "coordination", "Pick exactly one node to do a job, and safely pick a new one when it dies."),
        ],
    ),
    dict(
        key="frontend", vol=2, title="Frontend Design Patterns", short="frontend design patterns",
        theme="theme-frontend", subject="web frontend", term="Fall term · 2026", weekdays=(1, 3), start=date(2026, 9, 8),
        kicker="sketched between lectures and code reviews",
        lead="My notes on <span class=\"hl\">frontend design patterns</span>: the shapes that keep UIs fast, accessible and easy to change. {n} patterns in {c} collections, with the same eight sections as volume 1, rated on nine <b>frontend</b> qualities like bundle size, accessibility and developer experience. Examples use React + TypeScript, but the ideas travel.",
        blurb="Components, state and data, rendering and performance, and architecture for UIs that stay fast and easy to change.",
        attrs=FRONTEND_ATTRS, attrs_title="The nine frontend ratings", ratings_h2="Ratings", attrs_side="qualities that matter in the browser",
        handmade=set(),
        collections=[
            ("components", "Components", "split the UI into pieces that are easy to reuse"),
            ("state", "State &amp; data", "where data lives and how it changes"),
            ("rendering", "Rendering &amp; performance", "get pixels on screen fast and keep them smooth"),
            ("architecture", "Architecture &amp; resilience", "scale the codebase, the teams and the failures"),
        ],
        catalogue=[
            (1, "container-presentational", "Container & Presentational", "components", "Split components that fetch and decide from components that only display."),
            (2, "compound-components", "Compound Components", "components", "A set of components that work together and share state, like select and option."),
            (3, "custom-hooks", "Custom Hooks", "components", "Pull reusable stateful logic out of components into small, testable functions."),
            (4, "headless-components", "Headless Components", "components", "Ship behaviour and accessibility without markup or styles; you bring the looks."),
            (5, "global-store", "Global Store (Flux)", "state", "One store for shared app state, changed only through named actions."),
            (6, "server-state-cache", "Server-State Cache", "state", "Treat API data as a cache: show it instantly, revalidate in the background."),
            (7, "optimistic-ui", "Optimistic UI", "state", "Show the result before the server confirms, and roll back if it fails."),
            (8, "state-machines", "State Machines", "state", "Model UI as explicit states and allowed transitions, so impossible states can't happen."),
            (9, "ssr-hydration", "SSR & Hydration", "rendering", "Render HTML on the server for a fast first view, then make it interactive in the browser."),
            (10, "islands", "Islands Architecture", "rendering", "Ship static HTML and hydrate only the small interactive parts of the page."),
            (11, "code-splitting", "Code Splitting & Lazy Loading", "rendering", "Load only the code a screen needs now; fetch the rest when it's needed."),
            (12, "virtualization", "List Virtualization", "rendering", "Render only the rows on screen, even when the list has 100,000 items."),
            (13, "micro-frontends", "Micro-Frontends", "architecture", "Split a big frontend into apps owned and deployed by separate teams."),
            (14, "design-tokens", "Design Tokens", "architecture", "Name every colour, size and font once, and use those names everywhere."),
            (15, "error-boundaries", "Error Boundaries", "architecture", "Catch a crashing part of the UI and show a fallback, instead of a blank page."),
        ],
    ),
    dict(
        key="data", vol=3, title="Data & Database Patterns", short="data &amp; database patterns",
        theme="theme-data", subject="databases", term="Fall term · 2026", weekdays=(0, 3), start=date(2026, 9, 7),
        kicker="written in a ledger, between EXPLAIN plans",
        lead="My notes on <span class=\"hl\">data &amp; database patterns</span>: how to shape tables, read them fast, change them safely and keep them healthy as they grow. {n} patterns in {c} collections, with the same eight sections as the other volumes, rated on nine <b>database</b> qualities like read speed, write speed, integrity and storage cost. Examples use PostgreSQL, but the ideas work in most SQL databases.",
        blurb="Modelling, fast reads, safe changes and growing tables: the patterns that keep a database correct, quick and calm to run.",
        attrs=DATA_ATTRS, attrs_title="The nine database ratings", attrs_side="what a DBA would ask about", ratings_h2="Database ratings",
        handmade=set(),
        collections=[
            ("modelling", "Modelling", "shape the tables before the data piles up"),
            ("reading", "Reading fast", "get answers back without scanning everything"),
            ("changing", "Changing safely", "write, migrate and share changes without losing data"),
            ("growing", "Growing", "keep it healthy at 100× the rows and tenants"),
        ],
        catalogue=[
            (1, "normalization", "Normalization", "modelling", "Store each fact once so it can't disagree with itself; copy it only on purpose."),
            (2, "surrogate-keys", "Surrogate Keys", "modelling", "Give every row a meaningless, stable id instead of keying on real-world values."),
            (3, "soft-delete", "Soft Delete", "modelling", "Mark rows as deleted instead of removing them, so they can be restored or audited."),
            (4, "history-tables", "History Tables (Audit Trail)", "modelling", "Keep every past version of a row, so you can answer “what was it on that day?”"),
            (5, "indexing", "Indexing", "reading", "Keep a sorted lookup next to the table so queries jump to rows instead of scanning."),
            (6, "n-plus-one", "Batch Loading (Fixing N+1)", "reading", "Fetch related rows in one query instead of one query per row."),
            (7, "keyset-pagination", "Keyset Pagination", "reading", "Page with “after this key”, not OFFSET, so page 1,000 is as fast as page 1."),
            (8, "materialized-views", "Materialized Views", "reading", "Save the result of an expensive query as a table and refresh it on a schedule."),
            (9, "optimistic-locking", "Optimistic Locking", "changing", "Detect when someone else changed a row first, instead of silently overwriting it."),
            (10, "expand-contract", "Expand & Contract Migrations", "changing", "Change the schema in small backward-compatible steps, with no downtime."),
            (11, "change-data-capture", "Change Data Capture", "changing", "Stream every committed change from the database log to other systems."),
            (12, "partitioning", "Table Partitioning", "growing", "Split one huge table into smaller pieces by date or key, inside one database."),
            (13, "multitenancy", "Multitenancy", "growing", "Serve many customers from one database while keeping each one's data apart."),
            (14, "connection-pooling", "Connection Pooling", "growing", "Reuse a small set of open connections instead of opening one per request."),
            (15, "star-schema", "Star Schema", "growing", "Shape analytics data as facts surrounded by dimensions, for fast reports."),
        ],
    ),
    dict(
        key="testing", vol=4, title="Testing Patterns", short="testing patterns",
        theme="theme-testing", subject="software testing", term="Winter term · 2026", weekdays=(1, 4), start=date(2026, 11, 3),
        kicker="lab notebook · results recorded as observed",
        lead="My lab notebook on <span class=\"hl\">testing patterns</span>: how to shape a test suite you can trust, isolate the slow and scary parts, catch the bugs example tests miss, and keep it all fast and boring. {n} patterns in {c} collections, with the same eight sections as the other volumes, rated on nine <b>testing</b> qualities like fast feedback, confidence, reliability and realism. Examples use TypeScript with Vitest and Playwright, but the ideas work in any language.",
        blurb="Structure, test doubles, smarter techniques and reliability: the patterns behind a test suite that is fast, honest and calm to keep green.",
        attrs=TESTING_ATTRS, attrs_title="The nine testing ratings", attrs_side="what a good test suite is judged on", ratings_h2="Test-suite ratings",
        handmade=set(),
        collections=[
            ("structure", "Structure", "shape the suite and every test in it"),
            ("doubles", "Doubles &amp; boundaries", "deal with databases, networks and other teams"),
            ("techniques", "Smarter techniques", "find the bugs example tests miss"),
            ("reliability", "Reliability &amp; speed", "keep the suite fast, green and trusted"),
        ],
        catalogue=[
            (1, "test-pyramid", "Test Pyramid", "structure", "Many fast unit tests, fewer integration tests, a handful of end-to-end tests."),
            (2, "arrange-act-assert", "Arrange–Act–Assert", "structure", "Every test in three clear blocks: set up, do one thing, check the result."),
            (3, "test-data-builders", "Test Data Builders", "structure", "Build valid test objects with sensible defaults; spell out only what matters."),
            (4, "page-objects", "Page Objects", "structure", "Hide selectors behind a class per page, so UI tests read like user stories."),
            (5, "test-doubles", "Test Doubles (Stubs, Spies, Mocks)", "doubles", "Stand-ins for slow or unpredictable dependencies, each with its own job."),
            (6, "fakes", "Fakes", "doubles", "A small working version of a dependency, like an in-memory repository."),
            (7, "testcontainers", "Throwaway Containers", "doubles", "Test against the real database or broker, started fresh in a container."),
            (8, "contract-testing", "Contract Testing", "doubles", "Check that a service and its clients still agree on the API, without a full deploy."),
            (9, "property-based", "Property-Based Testing", "techniques", "State a rule that must always hold and let the tool hunt for counter-examples."),
            (10, "snapshot-testing", "Snapshot (Approval) Testing", "techniques", "Save the approved output once; fail when it changes, and review the diff."),
            (11, "mutation-testing", "Mutation Testing", "techniques", "Plant small bugs in the code and check that the tests notice."),
            (12, "characterization-tests", "Characterization Tests", "techniques", "Pin down what legacy code does today before you dare to change it."),
            (13, "deterministic-tests", "Controlled Time & Randomness", "reliability", "Inject the clock, the random seed and the ids, so every run is the same."),
            (14, "flaky-tests", "Flaky Test Quarantine", "reliability", "Detect tests that pass and fail at random, isolate them and fix the cause."),
            (15, "parallel-selective", "Parallel & Selective Runs", "reliability", "Split the suite across workers and run only the tests a change can affect."),
        ],
    ),
    dict(
        key="security", vol=5, title="Security Patterns", short="security patterns",
        theme="theme-security", subject="application security", term="Winter term · 2026", weekdays=(0, 3), start=date(2026, 11, 2),
        kicker="field dossier · handle with care",
        lead="My dossier on <span class=\"hl\">security patterns</span> for people who build things: who gets in, where secrets live, how to treat input from strangers, and how to notice and contain the day something goes wrong. {n} patterns in {c} collections, with the same eight sections as the other volumes, rated on nine <b>security</b> qualities like confidentiality, integrity, containment and usability. Examples use TypeScript, SQL and cloud config, but the ideas work everywhere. Defensive only: nothing here teaches you to break in.",
        blurb="Identity and access, secrets and data, untrusted input, and running securely: the patterns that keep attackers out and mistakes small.",
        attrs=SECURITY_ATTRS, attrs_title="The nine security ratings", attrs_side="confidentiality, integrity, availability and friends", ratings_h2="Security ratings",
        handmade=set(),
        collections=[
            ("identity", "Identity &amp; access", "who are you, and what may you do?"),
            ("secrets", "Secrets &amp; data", "keep keys, passwords and personal data safe"),
            ("input", "Untrusted input", "treat everything from outside as hostile"),
            ("operations", "Building &amp; running", "design for attacks, notice them, contain them"),
        ],
        catalogue=[
            (1, "zero-trust", "Zero Trust", "identity", "Never trust a request because of where it comes from; verify every one."),
            (2, "least-privilege", "Least Privilege", "identity", "Give every person, service and key only the access it needs, for as long as it needs it."),
            (3, "oauth-pkce", "OAuth 2.0 with PKCE", "identity", "Let users sign in through a trusted provider without your app ever seeing their password."),
            (4, "short-lived-tokens", "Short-Lived Tokens", "identity", "Credentials that expire in minutes, refreshed safely, so a stolen one is soon useless."),
            (5, "secrets-management", "Secrets Management", "secrets", "Keep keys and passwords in a vault, not in code, and rotate them automatically."),
            (6, "envelope-encryption", "Envelope Encryption", "secrets", "Encrypt data with a data key, and encrypt that key with a master key you never export."),
            (7, "password-hashing", "Password Hashing", "secrets", "Store passwords as slow, salted hashes, so a leaked table doesn't leak passwords."),
            (8, "input-validation", "Validate at the Boundary", "input", "Check every input against an allow-list schema as it enters, and reject the rest."),
            (9, "parameterized-queries", "Parameterized Queries", "input", "Send SQL and values separately, so data can never be run as code."),
            (10, "output-encoding", "Output Encoding & CSP", "input", "Escape data for where it's shown, and let the browser block anything you didn't send."),
            (11, "csrf-protection", "CSRF Protection", "input", "Make sure a state-changing request really came from your own page, not another site."),
            (12, "threat-modeling", "Threat Modelling", "operations", "Ask “what can go wrong?” on a diagram before you build, and plan the defences."),
            (13, "audit-logging", "Audit Logging", "operations", "Record who did what, when and from where, in a log attackers can't quietly edit."),
            (14, "supply-chain", "Supply-Chain Hygiene", "operations", "Pin, scan and verify the packages and images you depend on."),
            (15, "defense-in-depth", "Defence in Depth", "operations", "Stack independent layers so one failure doesn't mean a breach."),
        ],
    ),
    dict(
        key="cloud", vol=6, title="Cloud & DevOps Patterns", short="cloud &amp; devops patterns",
        theme="theme-cloud", subject="cloud &amp; devops", term="Winter term · 2026", weekdays=(1, 4), start=date(2026, 11, 3),
        kicker="drawn on isometric paper, between deploys",
        lead="My notes on <span class=\"hl\">cloud &amp; DevOps patterns</span>: how to ship small changes safely, describe infrastructure as code, run services you can see into, and recover calmly when things break, without a runaway bill. {n} patterns in {c} collections, with the same eight sections as the other volumes, rated on nine <b>operations</b> qualities like release safety, recoverability, observability and cost. Examples use GitHub Actions, Terraform, Kubernetes and OpenTelemetry, but the ideas work on any cloud.",
        blurb="Shipping safely, infrastructure as code, running and observing, and resilience and cost: the patterns behind calm deploys and boring on-call.",
        attrs=CLOUD_ATTRS, attrs_title="The nine operations ratings", attrs_side="what an SRE would ask about", ratings_h2="Operations ratings",
        handmade=set(),
        collections=[
            ("shipping", "Shipping safely", "get changes to users in small, reversible steps"),
            ("infra", "Infrastructure as code", "describe every server, network and environment in files"),
            ("running", "Running &amp; observing", "keep services healthy and see what they're doing"),
            ("resilience", "Resilience &amp; cost", "recover from the worst day, learn from it, and pay less"),
        ],
        catalogue=[
            (1, "blue-green", "Blue–Green Deployment", "shipping", "Run the new version next to the old one and switch traffic in one step."),
            (2, "canary", "Canary Releases", "shipping", "Send a small share of traffic to the new version and widen it only if metrics stay healthy."),
            (3, "feature-flags", "Feature Flags", "shipping", "Ship code switched off, then turn features on for chosen users without a deploy."),
            (4, "build-once", "Build Once, Deploy Many", "shipping", "Build one immutable artefact and promote the exact same thing through every environment."),
            (5, "infrastructure-as-code", "Infrastructure as Code", "infra", "Describe cloud resources in reviewed, versioned files instead of clicking in consoles."),
            (6, "gitops", "GitOps", "infra", "Git holds the desired state; an agent keeps the cluster matching it."),
            (7, "immutable-infrastructure", "Immutable Infrastructure", "infra", "Never patch servers in place; replace them with fresh ones built from an image."),
            (8, "preview-environments", "Preview Environments", "infra", "Spin up a short-lived copy of the app for every pull request."),
            (9, "health-checks", "Health Checks & Probes", "running", "Let the platform ask each instance “are you alive? are you ready?” and act on it."),
            (10, "autoscaling", "Autoscaling", "running", "Add and remove capacity automatically as load rises and falls."),
            (11, "observability", "Logs, Metrics & Traces", "running", "Emit structured signals so you can answer new questions about production."),
            (12, "slo-error-budgets", "SLOs & Error Budgets", "running", "Agree how reliable is reliable enough, and spend the rest on shipping."),
            (13, "disaster-recovery", "Backups & Disaster Recovery", "resilience", "Keep tested backups and a rehearsed plan to restore service elsewhere."),
            (14, "postmortems", "Incident Response & Postmortems", "resilience", "Handle incidents with clear roles, then learn from them without blame."),
            (15, "finops", "Cost Visibility (FinOps)", "resilience", "Tag, measure and own cloud spend, so cost is a design input, not a surprise."),
        ],
    ),
    # ---- Series 2 · The Solution Architect's Notebook ----
    # Plan and handoff: docs/HANDOFF-solution-architect.md. Case study facts: docs/larder-casebook.md.
    dict(
        key="architect-1", vol=1, title="From Requirements to Architecture", short="from requirements to architecture",
        series=2, book="The Solution Architect's Notebook", narrator="Ana", brand="architect's notebook", title_block=True, sheet_doodles=True,
        theme="theme-architect", fonts="Architects+Daughter", subject="solution architecture",
        problem_h2="The situation", related_h3="Related notes", map_caption="Translating it to the job", map_col="On the project",
        term="Winter term · 2027", weekdays=(0, 3), start=date(2027, 1, 4),
        kicker="the solution architect's notebook · book 1 · vol. 1",
        story="<b>October 2025.</b> Larder delivers groceries in Amsterdam from two dark stores and has just promised its investors six cities by the end of 2027. Ana joins as its first solution architect, a week before Grace joins as product owner. This volume follows Ana's first four months, from a one-line brief to a walking skeleton for Rotterdam in January 2026.",
        lead="Volume 1 of <span class=\"hl\">The Solution Architect's Notebook</span>: how an architect gets from a vague business plan to a first architecture people can build, without guessing. {n} notes in {c} collections: understand the problem and the people, find the requirements that really shape the system, choose the first shapes, and test the riskiest ideas before they're expensive. Every note follows <b>Larder</b>, a grocery delivery start-up growing from one city to six, and ends with a <b>try it</b> exercise for your own project.",
        blurb="Stakeholders, drivers, context, the requirements that shape a system, first architecture shapes, and testing risky ideas early.",
        attrs=ARCHITECT_ATTRS, attrs_title="The nine architect ratings", attrs_side="what a good architecture practice is judged on", ratings_h2="Architect ratings",
        handmade=set(),
        collections=[
            ("understanding", "Understanding the problem", "who cares, what they want, and where the system ends"),
            ("requirements", "Requirements that shape architecture", "find the few needs that decide the design"),
            ("shapes", "First shapes", "pick a starting structure you can grow"),
            ("validating", "Validating early", "test the risky ideas while they're still cheap"),
        ],
        catalogue=[
            (1, "stakeholder-map", "Stakeholder Map", "understanding", "List everyone who can affect or is affected by the system, and plan how to work with each."),
            (2, "business-drivers", "Business Drivers & Goals", "understanding", "Turn the business plan into a few measurable goals that every design choice can be checked against."),
            (3, "system-context", "System Context Diagram", "understanding", "One picture of the system as a box, with the people and systems around it, so everyone agrees where it ends."),
            (4, "event-storming", "Domain Discovery (Event Storming)", "understanding", "Map the business as a timeline of events on sticky notes with the people who do the work."),
            (5, "asr", "Architecturally Significant Requirements", "requirements", "Find the few requirements that would change the architecture, and design for those first."),
            (6, "quality-attribute-scenarios", "Quality Attribute Scenarios", "requirements", "Turn “fast” and “reliable” into testable sentences: a stimulus, a context and a measurable response."),
            (7, "constraints-assumptions", "Constraints vs Assumptions", "requirements", "Separate the fixed rules you must obey from the beliefs you still have to check."),
            (8, "nfr-checklist", "NFR Checklist", "requirements", "A short list of quality questions to ask on every project, so nothing important is forgotten."),
            (9, "architecture-styles", "Architecture Styles Compared", "shapes", "Compare monolith, modular monolith, microservices, event-driven and serverless against your drivers."),
            (10, "modular-monolith", "Modular Monolith First", "shapes", "Start as one deployable app with strict internal modules; split out a service only when you must."),
            (11, "bounded-contexts", "Bounded Contexts", "shapes", "Draw boundaries where a word changes meaning, and give each area its own model and owner."),
            (12, "walking-skeleton", "Walking Skeleton", "shapes", "Build the thinnest end-to-end slice through every part first, then add flesh."),
            (13, "spike-prototype-poc", "Spike vs Prototype vs PoC", "validating", "Pick the right small experiment: a spike answers a question, a prototype tests an idea, a PoC proves it works."),
            (14, "fitness-functions", "Fitness Functions", "validating", "Turn architecture rules into automated checks that run in CI, so the design can't quietly decay."),
            (15, "risk-storming", "Risk-Storming", "validating", "The team marks risks on the architecture diagram together, then decides what to do about the biggest."),
        ],
    ),
    dict(
        key="architect-2", vol=2, title="Decisions & Trade-offs", short="decisions &amp; trade-offs",
        series=2, book="The Solution Architect's Notebook", narrator="Ana", brand="architect's notebook", title_block=True, sheet_doodles=True,
        theme="theme-architect", fonts="Architects+Daughter", subject="solution architecture",
        problem_h2="The situation", related_h3="Related notes", map_caption="Translating it to the job", map_col="On the project",
        term="Spring term · 2027", weekdays=(1, 3), start=date(2027, 3, 2),
        kicker="the solution architect's notebook · book 1 · vol. 2",
        story="<b>March 2026.</b> The modular monolith is taking shape, Dispatch is being pulled out into its own service, Rotterdam opens on 27 April and Korenwolf's pilot starts in May. Every week brings a decision someone will question a year from now. This volume follows Ana from March to September 2026: how she and the team choose, record and live with their decisions.",
        lead="Volume 2 of <span class=\"hl\">The Solution Architect's Notebook</span>: how architects choose between options, record why, and live with the consequences. {n} notes in {c} collections: write decisions down, choose well, make the big build-buy-and-platform calls, and keep living with what you chose. Every note follows <b>Ana</b> at <b>Larder</b> from March to September 2026, through the Rotterdam launch and the Korenwolf pilot, and ends with a <b>try it</b> exercise for your own project.",
        blurb="Decision records and rights, options analysis, reversible and irreversible choices, build vs buy, and living with technical debt.",
        attrs=ARCHITECT_ATTRS, attrs_title="The nine architect ratings", attrs_side="what a good architecture practice is judged on", ratings_h2="Architect ratings",
        handmade=set(),
        collections=[
            ("recording", "Recording decisions", "write down what was decided, why, and who decides"),
            ("choosing", "Choosing well", "compare options honestly, and decide at the right time"),
            ("big", "Big choices", "build or buy, which technology, which platform"),
            ("living", "Living with decisions", "track the debt, keep an exit, and look again on purpose"),
        ],
        catalogue=[
            (1, "adr", "Architecture Decision Records", "recording", "One short file per significant decision: context, options, the choice and its consequences."),
            (2, "decision-log", "Decision Log", "recording", "One line per decision, open or closed, with an owner and a date, so nothing is decided twice or never."),
            (3, "rfcs-design-docs", "RFCs & Design Docs", "recording", "Write big designs down and open them for comments by a date, before anyone builds."),
            (4, "decision-rights", "Decision Rights (RACI/DACI)", "recording", "Name who drives, who decides and who is heard, with exactly one approver."),
            (5, "options-analysis", "Options Analysis", "choosing", "Compare real options, including doing nothing, against weighted criteria taken from the drivers."),
            (6, "trade-off-sliders", "Trade-off Sliders", "choosing", "Agree up front which qualities give way when they collide, because they can't all be at maximum."),
            (7, "one-way-two-way-doors", "One-way vs Two-way Doors", "choosing", "Decide reversible things fast and close to the work; slow down only for the doors that lock behind you."),
            (8, "last-responsible-moment", "Last Responsible Moment", "choosing", "Decide when waiting starts to cost more than it saves, not earlier and not later."),
            (9, "build-vs-buy", "Build vs Buy vs Open Source", "big", "Build what makes you different, buy what doesn't, and know what open source really costs."),
            (10, "technology-evaluation", "Technology Evaluation", "big", "From long list to shortlist to a bake-off on your own data, scored against criteria set in advance."),
            (11, "cloud-service-model", "Choosing a Cloud Service Model", "big", "Pick how much of the stack you run yourself, from virtual machines to functions to SaaS."),
            (12, "technology-radar", "Technology Radar", "big", "Publish which technologies to adopt, trial, assess or hold, so teams choose fast and alike."),
            (13, "tech-debt-register", "Technical Debt Register", "living", "List the shortcuts you took on purpose, with their interest and a payback trigger."),
            (14, "exit-plans", "Exit Plans & Reversibility", "living", "For every vendor and platform, know how you'd leave, and keep the way out cheap."),
            (15, "revisiting-decisions", "Revisiting Decisions", "living", "Give every decision a review trigger, and check them on purpose instead of re-arguing at random."),
        ],
    ),
    dict(
        key="architect-3", vol=3, title="Communicating Architecture", short="communicating architecture",
        series=2, book="The Solution Architect's Notebook", narrator="Ana", brand="architect's notebook", title_block=True, sheet_doodles=True,
        theme="theme-architect", fonts="Architects+Daughter", subject="solution architecture",
        problem_h2="The situation", related_h3="Related notes", map_caption="Translating it to the job", map_col="On the project",
        term="Summer term · 2027", weekdays=(1, 3), start=date(2027, 5, 4),
        kicker="the solution architect's notebook · book 1 · vol. 3",
        story="<b>October 2026.</b> Larder runs two cities, Korenwolf has signed for three offices, and four more cities are planned for 2027. The team has grown to 18 engineers, and the architecture now lives in too many diagrams, documents and heads. This volume follows Ana from October 2026 to February 2027: drawing the system so people can read it, writing documents people use, explaining choices to people who don't build software, and keeping all of it current.",
        lead="Volume 3 of <span class=\"hl\">The Solution Architect's Notebook</span>: how architects make a system understandable to the people who build it, run it, pay for it and depend on it. {n} notes in {c} collections: diagrams with clear rules, documents people actually read, conversations with engineers and executives, and keeping it all current. Every note follows <b>Ana</b> at <b>Larder</b> from October 2026 to February 2027, and ends with a <b>try it</b> exercise for your own project.",
        blurb="C4 and other views, one-pagers, docs as code, presenting to executives, explaining trade-offs and keeping diagrams alive.",
        attrs=ARCHITECT_ATTRS, attrs_title="The nine architect ratings", attrs_side="what a good architecture practice is judged on", ratings_h2="Architect ratings",
        handmade=set(),
        collections=[
            ("diagrams", "Diagrams", "pictures with rules, for the question being asked"),
            ("documents", "Documents", "pages people read, kept next to the code"),
            ("conversations", "Conversations", "explain, present and practise, in the room"),
            ("current", "Keeping it current", "diagrams, plans and words that don't go stale"),
        ],
        catalogue=[
            (1, "c4-model", "C4 Model", "diagrams", "Four zoom levels (context, containers, components, code), with labelled boxes and arrows."),
            (2, "views-viewpoints", "Views & Viewpoints (4+1)", "diagrams", "A drawing for each stakeholder's question, tied together by a few scenarios."),
            (3, "sequence-flow", "Sequence & Flow Diagrams", "diagrams", "Lifelines across, time down: show what happens in what order, and on what trigger."),
            (4, "deployment-diagrams", "Deployment Diagrams", "diagrams", "Where everything runs and how it's reached: on-call's first page."),
            (5, "architecture-one-pager", "Architecture One-Pager", "documents", "The whole architecture on one page: purpose, picture, key decisions, numbers, risks."),
            (6, "arc42", "arc42 Template", "documents", "Twelve sections that give every architecture document the same shape; fill only what's needed."),
            (7, "docs-as-code", "Docs as Code", "documents", "Write docs and diagrams as text in the repo, review them in pull requests, publish from CI."),
            (8, "solution-design-document", "Solution Design Document Done Right", "documents", "Write the design document a client asks for around their questions, not the template's."),
            (9, "whiteboard-sessions", "Whiteboard Sessions", "conversations", "A question on top, one marker, a legend, a timebox and a photo that becomes a record."),
            (10, "presenting-to-executives", "Presenting to Executives", "conversations", "Answer first, options in money, risk and time, then the ask: in ten minutes."),
            (11, "explaining-trade-offs", "Explaining Trade-offs to Non-Engineers", "conversations", "Turn a technical trade-off into the things the listener cares about: money, minutes, risk."),
            (12, "architecture-katas", "Architecture Katas", "conversations", "Small teams practise designing a system in 90 minutes, then present and get feedback."),
            (13, "living-diagrams", "Living Diagrams", "current", "Generate diagrams from code, infrastructure and traces, so they can't drift."),
            (14, "architecture-roadmap", "Architecture Roadmap", "current", "The steps from today's architecture to the one the business needs, as transition states."),
            (15, "glossary", "Glossary & Ubiquitous Language", "current", "One list of the words that matter, what each means where, used in code, docs and meetings."),
        ],
    ),
    dict(
        key="architect-4", vol=4, title="Integration & the Enterprise Landscape", short="integration &amp; the enterprise",
        series=2, book="The Solution Architect's Notebook", narrator="Ana", brand="architect's notebook", title_block=True, sheet_doodles=True,
        theme="theme-architect", fonts="Architects+Daughter", subject="solution architecture",
        problem_h2="The situation", related_h3="Related notes", map_caption="Translating it to the job", map_col="On the project",
        term="Autumn term · 2027", weekdays=(1, 3), start=date(2027, 9, 7),
        kicker="the solution architect's notebook · book 1 · vol. 4",
        story="<b>March 2027.</b> Larder is moving its warehouses from StockPilot to WMS B, store by store, while Utrecht and The Hague open and Antwerp gets ready for September. Korenwolf wants to order from its own systems, a second billing flow is live, and the landscape now holds more than twenty applications. This volume follows Ana from March to September 2027: connecting systems without tangling them, drawing honest boundaries, mapping the landscape, and changing it while the business keeps running.",
        lead="Volume 4 of <span class=\"hl\">The Solution Architect's Notebook</span>: how architects connect systems, protect their boundaries, see the whole landscape and change it safely. {n} notes in {c} collections: integration styles, boundaries, the landscape, and changing it. Every note follows <b>Ana</b> at <b>Larder</b> from March to September 2027, through a warehouse migration and three city launches, and ends with a <b>try it</b> exercise for your own project.",
        blurb="Integration styles, anti-corruption layers, capability maps, portfolios, master data and strangler-fig migrations.",
        attrs=ARCHITECT_ATTRS, attrs_title="The nine architect ratings", attrs_side="what a good architecture practice is judged on", ratings_h2="Architect ratings",
        handmade=set(),
        collections=[
            ("styles", "Integration styles", "a style per need: events, APIs, files"),
            ("boundaries", "Boundaries", "keep other models out, and change contracts safely"),
            ("landscape", "The landscape", "see every capability, application and owner"),
            ("changing", "Changing the landscape", "move piece by piece while the business runs"),
        ],
        catalogue=[
            (1, "integration-style", "Choosing an Integration Style", "styles", "Shared database, files, APIs or events: choose per need, and mix them behind one adapter."),
            (2, "api-first", "API-First Design", "styles", "Write the contract first, in the consumer's words, review it with them, and build against it."),
            (3, "event-driven-integration", "Event-Driven Integration", "styles", "Treat events as owned, registered contracts with known consumers and compatible changes."),
            (4, "batch-file-transfer", "Batch & File Transfer", "styles", "Files on a schedule, done properly: checked, loaded once, and loud when late."),
            (5, "anti-corruption-layer", "Anti-Corruption Layer", "boundaries", "Translate another system's model at the border so it never leaks into yours."),
            (6, "backend-for-frontend", "Backend for Frontend", "boundaries", "One small backend per kind of client, shaped for what that client needs."),
            (7, "api-versioning", "API Versioning Strategy", "boundaries", "Add without breaking, version when you must, and retire old versions on a schedule."),
            (8, "canonical-data-model", "Canonical Data Model (and Its Traps)", "boundaries", "Why one model for everything fails, and the small shared language that works instead."),
            (9, "capability-map", "Capability Map", "landscape", "What the business must be able to do, mapped and coloured, independent of systems."),
            (10, "application-portfolio", "Application Portfolio (TIME)", "landscape", "Every application sorted into tolerate, invest, migrate or eliminate."),
            (11, "data-ownership", "Data Ownership & Master Data", "landscape", "One owner per kind of data, one master copy, and everyone else subscribes."),
            (12, "identity-federation", "Identity Federation & SSO", "landscape", "One identity per person, trusted across tools and partners, removed in one place."),
            (13, "strangler-fig", "Strangler Fig Migration", "changing", "Replace a system piece by piece behind a router, until the old one can be switched off."),
            (14, "transition-architectures", "Transition Architectures", "changing", "Design the in-between states of a migration, including the temporary bridges and their end dates."),
            (15, "saas-integration", "SaaS & Vendor Integration", "changing", "Integrate with services you don't control: webhooks, limits, sandboxes, outages and exits."),
        ],
    ),
    dict(
        key="architect-5", vol=5, title="Designing for Qualities", short="designing for qualities",
        series=2, book="The Solution Architect's Notebook", narrator="Ana", brand="architect's notebook", title_block=True, sheet_doodles=True,
        theme="theme-architect", fonts="Architects+Daughter", subject="solution architecture",
        problem_h2="The situation", related_h3="Related notes", map_caption="Translating it to the job", map_col="On the project",
        term="Winter term · 2028", weekdays=(1, 3), start=date(2028, 1, 4),
        kicker="the solution architect's notebook · book 1 · vol. 5",
        story="<b>October 2027.</b> The warehouse move is done, Antwerp opens in October and Eindhoven in November, and Larder heads into its busiest season with five times the orders of two years ago. Femke wants to know it will hold, Marco wants the cloud bill down, Lena wants Belgian data handled properly, and Korenwolf asks for an emissions figure. This volume follows Ana from October 2027 to March 2028: sizing, availability, security, compliance and cost, done with numbers instead of hope.",
        lead="Volume 5 of <span class=\"hl\">The Solution Architect's Notebook</span>: how architects design for the qualities that don't show up in a feature list. {n} notes in {c} collections: size and speed, availability, security and compliance, and cost and balance. Every note follows <b>Ana</b> at <b>Larder</b> from October 2027 to March 2028, through two city launches and a peak season, and ends with a <b>try it</b> exercise for your own project.",
        blurb="Back-of-the-envelope maths, capacity, availability, DR tiers, security reviews, data residency, TCO and cloud cost.",
        attrs=ARCHITECT_ATTRS, attrs_title="The nine architect ratings", attrs_side="what a good architecture practice is judged on", ratings_h2="Architect ratings",
        handmade=set(),
        collections=[
            ("size", "Size & speed", "estimate, plan and budget before the peak arrives"),
            ("availability", "Availability", "do the maths, find the failures, plan the recovery"),
            ("security", "Security & compliance", "review the design, know the data, build the rules in"),
            ("cost", "Cost & balance", "what it really costs, and which qualities matter most"),
        ],
        catalogue=[
            (1, "back-of-envelope", "Back-of-the-Envelope Estimation", "size", "Rough numbers from a few known facts, in minutes, to see which part of a design matters."),
            (2, "capacity-planning", "Capacity Planning", "size", "Forecast demand, find the first thing to run out, and add capacity before it does."),
            (3, "load-profiles", "Load Profiles", "size", "Test with the real mix and shape of traffic: the ramp, the spike, the push, not a flat line."),
            (4, "performance-budgets", "Performance Budgets", "size", "Agree limits on speed and size, check them in CI, and treat a breach like a failing test."),
            (5, "availability-maths", "Availability Maths", "availability", "Multiply the chain, add the spares, and turn nines into minutes a month."),
            (6, "failure-mode-analysis", "Failure Mode Analysis", "availability", "List how each part can fail, what happens then, and fix the worst first."),
            (7, "dr-tiers", "DR Tiers", "availability", "Sort systems into recovery tiers with RTO and RPO, and prove them with restore tests."),
            (8, "multi-region", "When to Go Multi-Region", "availability", "A second region is a big, ongoing cost: decide with numbers and agreed triggers."),
            (9, "security-architecture-review", "Security Architecture Review", "security", "Walk the design's trust boundaries with a checklist and threats, before attackers do."),
            (10, "data-classification", "Data Classification & Residency", "security", "Label data by sensitivity, know where every copy lives, and let the label set the rules."),
            (11, "compliance-by-design", "Compliance by Design", "security", "Turn legal rules into platform features and automatic evidence, not yearly scrambles."),
            (12, "total-cost-of-ownership", "Total Cost of Ownership", "cost", "Count every cost over years, people included, before comparing options."),
            (13, "cost-aware-architecture", "Cost-Aware Architecture", "cost", "Know the cost per order of each part, and design and tune with that number in view."),
            (14, "green-software", "Green Software", "cost", "Measure the platform's carbon, then use less, use it when it's cleaner, and use cleaner places."),
            (15, "utility-tree", "Quality Attribute Utility Tree", "cost", "Rank the qualities with concrete scenarios, so trade-offs follow what matters most."),
        ],
    ),
    dict(
        key="architect-6", vol=6, title="Delivery, Governance & Influence", short="delivery, governance &amp; influence",
        series=2, book="The Solution Architect's Notebook", narrator="Ana", brand="architect's notebook", title_block=True, sheet_doodles=True,
        theme="theme-architect", fonts="Architects+Daughter", subject="solution architecture",
        problem_h2="The situation", related_h3="Related notes", map_caption="Translating it to the job", map_col="On the project",
        term="Spring term · 2028", weekdays=(1, 3), start=date(2028, 3, 7),
        kicker="the solution architect's notebook · book 1 · vol. 6",
        story="<b>April 2028.</b> Larder has five product teams, thirty engineers, six cities and a board plan for eight by the end of the year, with 60,000 orders a day. Ana can no longer review every change, attend every design or carry every decision. This volume follows her from April to September 2028: designing just enough, governing with principles and guardrails instead of gates, taking risks and migrations to go-live and hand-over, and leading through influence, including growing the architects who come after her.",
        lead="Volume 6 of <span class=\"hl\">The Solution Architect's Notebook</span>, the last: how architects work at scale, through others. {n} notes in {c} collections: architecture in delivery, governance, risk and transition, and influence. Every note follows <b>Ana</b> at <b>Larder</b> from April to September 2028, as the platform grows to eight cities, and ends with a <b>try it</b> exercise for your own project.",
        blurb="Just-enough design, principles, guardrails, golden paths, risk, migrations, go-live, hand-over and influence.",
        attrs=ARCHITECT_ATTRS, attrs_title="The nine architect ratings", attrs_side="what a good architecture practice is judged on", ratings_h2="Architect ratings",
        handmade=set(),
        collections=[
            ("delivery", "Architecture in delivery", "design enough, evolve the rest, keep a backlog"),
            ("governance", "Governance", "principles and guardrails instead of gates"),
            ("risk", "Risk & transition", "from risk list to migration, go-live and hand-over"),
            ("influence", "Influence", "lead without authority, and grow the next architects"),
        ],
        catalogue=[
            (1, "just-enough-design", "Just-Enough Up-Front Design", "delivery", "Decide the hard-to-change things before building; leave the rest to learn while building."),
            (2, "evolutionary-architecture", "Evolutionary Architecture", "delivery", "Design for change: small steps, fitness functions that guard what matters, and room to turn."),
            (3, "architecture-backlog", "The Architecture Backlog", "delivery", "One ordered list of architecture work, planned with product, with capacity agreed."),
            (4, "architecture-principles", "Architecture Principles", "governance", "A handful of rules with reasons and implications, so teams decide alike without asking."),
            (5, "guardrails-not-gates", "Guardrails Not Gates", "governance", "Automate the checks that matter and review only one-way doors, so teams move without waiting."),
            (6, "lightweight-review", "Lightweight Architecture Review", "governance", "A short, written-first review for decisions that are hard to undo, with a clear outcome."),
            (7, "golden-paths", "Golden Paths", "governance", "Make the right way the easy way: templates and platforms that start a service well."),
            (8, "risk-register", "Risk Register", "risk", "A short, owned list of risks with likelihood, impact, actions and a date to look again."),
            (9, "migration-planning", "Migration Planning", "risk", "Move a live system in reversible steps, each with a test, a rollback and a stop point."),
            (10, "go-live-readiness", "Go-Live Readiness", "risk", "Agree in advance what “ready” means, check it with evidence, and decide go or no-go."),
            (11, "handover-to-operations", "Handover to Operations", "risk", "Hand a system to the people who'll run it with runbooks, alerts, practice and a warranty period."),
            (12, "influencing-without-authority", "Influencing Without Authority", "influence", "Change what teams do by making it their idea, their win and the easy path."),
            (13, "negotiating-with-stakeholders", "Negotiating with Stakeholders", "influence", "Trade on interests and options when architecture needs time, money or a change of plan."),
            (14, "discovery-workshops", "Discovery Workshops", "influence", "Bring business, product and engineering into one room to explore a new idea before deciding."),
            (15, "growing-architects", "Growing Other Architects", "influence", "Spread architecture thinking: pairing, katas, decision ownership and a path for engineers."),
        ],
    ),
    # ---- Series 2 · Book 2 · The Product Owner's Notebook (Grace). Plan: docs/HANDOFF-product-owner.md ----
    dict(
        key="product-1", vol=1, title="Discovering the Problem", short="discovering the problem",
        series=2, book="The Product Owner's Notebook", narrator="Grace", brand="product owner's notebook", book_no=2,
        title_block=True, sheet_doodles="product",
        theme="theme-product", fonts="Permanent+Marker", subject="product ownership",
        problem_h2="The situation", related_h3="Related notes", map_caption="Translating it to the job", map_col="On the product",
        term="Winter term · 2027", weekdays=(1, 4), start=date(2027, 1, 5),
        kicker="the product owner's notebook · book 2 · vol. 1",
        story="<b>October 2025.</b> Larder delivers groceries in Amsterdam and has promised its investors six cities by the end of 2027. Grace joins as product owner for ordering and the customer apps, a week after Ana joins as architect. Six percent of orders end in a refund ticket and nobody owns the problem. This volume follows Grace's first four months: finding out what customers really need before anyone builds anything.",
        lead="Volume 1 of <span class=\"hl\">The Product Owner's Notebook</span>: how a product owner finds the right problem before the team builds a solution. {n} notes in {c} collections: listen to customers, frame the problem, decide what to measure, and test ideas while they're still cheap. Every note follows <b>Grace</b> at <b>Larder</b>, in the same months and meetings as Ana's notebook, and ends with a <b>try it</b> exercise for your own product.",
        blurb="Customer interviews, jobs to be done, opportunity trees, the right metrics and cheap tests: finding the problem worth solving.",
        attrs=PRODUCT_ATTRS, attrs_title="The nine product ratings", attrs_side="what a good product practice is judged on", ratings_h2="Product ratings",
        handmade=set(),
        collections=[
            ("customers", "Understanding customers", "listen before you decide anything"),
            ("framing", "Framing the problem", "pick the problem worth solving, and say it clearly"),
            ("measuring", "Measuring what matters", "know what “better” means before you build"),
            ("testing", "Testing ideas cheaply", "find out if you're wrong in days, not months"),
        ],
        catalogue=[
            (1, "customer-interviews", "Customer Interviews", "customers", "Ask customers about what they did last time, not what they'd like, and listen for the pain."),
            (2, "jobs-to-be-done", "Jobs to Be Done", "customers", "Find the progress customers are trying to make; the product is just something they hire for the job."),
            (3, "proto-personas", "Proto-Personas", "customers", "Quick, evidence-based sketches of the main kinds of customer, kept honest and kept few."),
            (4, "journey-map", "Customer Journey Map", "customers", "Draw every step a customer takes, what they feel at each one, and where it breaks."),
            (5, "problem-statements", "Problem Statements", "framing", "Write the problem in one sentence, from the customer's side, before anyone proposes a fix."),
            (6, "opportunity-solution-tree", "Opportunity Solution Tree", "framing", "Link one outcome to the customer needs behind it, then to ideas, then to tests."),
            (7, "assumption-mapping", "Assumption Mapping", "framing", "List what must be true for an idea to work, and test the riskiest first."),
            (8, "outcomes-over-outputs", "Outcomes over Outputs", "framing", "Judge work by the change it makes for customers, not by the features shipped."),
            (9, "north-star-metric", "North Star Metric", "measuring", "One number that captures the value customers get, so every team pulls the same way."),
            (10, "leading-lagging", "Leading vs Lagging Indicators", "measuring", "Pair the slow result you care about with fast signals you can move this week."),
            (11, "baseline", "Baseline Before You Build", "measuring", "Measure today properly first, or you'll never know if the change worked."),
            (12, "hypotheses", "Testable Hypotheses", "testing", "Write each idea as a bet: we believe, so we'll, and we'll know when."),
            (13, "fake-door", "Fake Door Test", "testing", "Show the button before building the feature, and count who knocks."),
            (14, "concierge-mvp", "Concierge & Wizard-of-Oz MVP", "testing", "Deliver the value by hand first; build the software only once it's proven."),
            (15, "prototype-testing", "Prototype Testing with Users", "testing", "Put a clickable fake in front of five real users and watch where they stumble."),
        ],
    ),
    dict(
        key="product-2", vol=2, title="Deciding What to Build", short="deciding what to build",
        series=2, book="The Product Owner's Notebook", narrator="Grace", brand="product owner's notebook", book_no=2,
        title_block=True, sheet_doodles="product",
        theme="theme-product", fonts="Permanent+Marker", subject="product ownership",
        problem_h2="The situation", related_h3="Related notes", map_caption="Translating it to the job", map_col="On the product",
        term="Spring term · 2027", weekdays=(1, 4), start=date(2027, 3, 2),
        kicker="the product owner's notebook · book 2 · vol. 2",
        story="<b>January 2026.</b> Grace knows the problem now: substitutions, 6 % of orders ending in a refund ticket, and customers who mind not being asked. Her tests say approvals in the app will work. But Rotterdam opens on 27 April, Femke has met an office client at a trade fair, and every stakeholder has an idea for the next quarter. This volume follows Grace from January to April 2026: choosing what to build, saying no to the rest, and turning it into a strategy and a roadmap people trust.",
        lead="Volume 2 of <span class=\"hl\">The Product Owner's Notebook</span>: how a product owner decides what to build, and what not to. {n} notes in {c} collections: prioritise with evidence, say no without burning bridges, put strategy and roadmaps on a page, and make the case for the bets you choose. Every note follows <b>Grace</b> at <b>Larder</b> from January to April 2026, in the same weeks as Ana's notebook, and ends with a <b>try it</b> exercise for your own product.",
        blurb="Prioritising with evidence, saying no, strategy on a page, now / next / later roadmaps and business cases.",
        attrs=PRODUCT_ATTRS, attrs_title="The nine product ratings", attrs_side="what a good product practice is judged on", ratings_h2="Product ratings",
        handmade=set(),
        collections=[
            ("prioritising", "Prioritising", "compare ideas with evidence, and order them by time and value"),
            ("saying-no", "Saying no", "protect the focus, keep the relationships"),
            ("roadmaps", "Strategy & roadmaps", "one page of strategy, a roadmap people can trust"),
            ("case", "Making the case", "size it, price it, and bet instead of promising"),
        ],
        catalogue=[
            (1, "rice-ice-scoring", "RICE & ICE Scoring", "prioritising", "Score every idea the same way (reach, impact, confidence, effort), then argue about the numbers, not the sponsors."),
            (2, "cost-of-delay", "Cost of Delay", "prioritising", "Price each week of waiting and divide by duration, so short, valuable work doesn't queue behind long work."),
            (3, "kano-model", "Kano Model", "prioritising", "Ask customers which features are basic, more-is-better or delightful, instead of guessing."),
            (4, "moscow", "MoSCoW and Its Traps", "prioritising", "Must, Should, Could, Won't, with a strict Must test, room to spare and the Won'ts written down."),
            (5, "saying-no", "Saying No Without Burning Bridges", "saying-no", "A clear no with the reason, what you're doing instead, a small yes and a date to look again."),
            (6, "hippo", "Handling the HiPPO", "saying-no", "Turn the most senior opinion in the room into a hypothesis, and test it."),
            (7, "opportunity-cost", "Opportunity Cost", "saying-no", "Every yes is a no to the next best thing; name that thing and its price."),
            (8, "request-triage", "Feature Request Triage", "saying-no", "One front door for requests and a weekly triage, so everyone gets an answer within a week."),
            (9, "strategy-on-a-page", "Product Strategy on a Page", "roadmaps", "Where we are, who we serve, how we win, what we bet on and what we won't do, on one page."),
            (10, "now-next-later", "Now / Next / Later Roadmap", "roadmaps", "Three columns instead of a Gantt chart: sure now, likely next, possible later."),
            (11, "outcome-roadmaps", "Outcome-Based Roadmaps", "roadmaps", "Put the result you're after on the roadmap, with the features as current bets."),
            (12, "roadmap-vs-release-plan", "Roadmap vs Release Plan", "roadmaps", "Keep the why-and-order roadmap apart from the dated release plan, and update both."),
            (13, "opportunity-sizing", "Opportunity Sizing", "case", "Size a market bottom-up from customers you can count, not from a big top-down number."),
            (14, "business-case", "Business Case One-Pager", "case", "Problem, benefit, cost, payback, risks and the ask, on one page someone will read."),
            (15, "bets-not-promises", "Bets, Not Promises", "case", "Present plans as bets with confidence and signals, not promises you don't control."),
        ],
    ),
    dict(
        key="product-3", vol=3, title="From Idea to Backlog", short="from idea to backlog",
        series=2, book="The Product Owner's Notebook", narrator="Grace", brand="product owner's notebook", book_no=2,
        title_block=True, sheet_doodles="product",
        theme="theme-product", fonts="Permanent+Marker", subject="product ownership",
        problem_h2="The situation", related_h3="Related notes", map_caption="Translating it to the job", map_col="On the product",
        term="Summer term · 2027", weekdays=(1, 4), start=date(2027, 5, 4),
        kicker="the product owner's notebook · book 2 · vol. 3",
        story="<b>February 2026.</b> The business case for substitution approvals is approved, the “no swaps” flag ships in a fortnight, and Rotterdam opens on 27 April. Now an idea has to become software that pickers and customers actually use. This volume follows Grace from February to June 2026, with Noor, the new product designer, and the engineers: shaping the work, writing it down, working as one team, and shipping it safely, in Amsterdam and in a brand-new city.",
        lead="Volume 3 of <span class=\"hl\">The Product Owner's Notebook</span>: how a product owner turns a good idea into working software, with the team. {n} notes in {c} collections: shape the work into thin slices, write it down so everyone means the same thing, work as one team without meeting marathons, and ship it safely. Every note follows <b>Grace</b> at <b>Larder</b> from February to June 2026, through the approvals launch and Rotterdam's opening, and ends with a <b>try it</b> exercise for your own product.",
        blurb="Story maps, thin slices, example mapping, the product trio, tech-debt talks, launch checklists and safe rollouts.",
        attrs=PRODUCT_ATTRS, attrs_title="The nine product ratings", attrs_side="what a good product practice is judged on", ratings_h2="Product ratings",
        handmade=set(),
        collections=[
            ("shaping", "Shaping work", "turn an idea into slices that work end to end"),
            ("writing", "Writing it down", "so everyone means the same thing"),
            ("team", "Working with the team", "one team, short meetings, honest trade-offs"),
            ("shipping", "Shipping", "release safely, watch closely, tell people"),
        ],
        catalogue=[
            (1, "story-mapping", "Story Mapping", "shaping", "Lay the user's journey across the top, hang stories underneath, and draw release lines across."),
            (2, "thin-slices", "Thin Slices of Value", "shaping", "Cut features into thin slices that work end to end, riskiest first, not into layers."),
            (3, "mvp-vs-mlp", "MVP vs MLP", "shaping", "Ask “minimum for what?”: lovable where customers form trust, viable where only staff see it."),
            (4, "pre-mortem", "Pre-mortem", "shaping", "Imagine the launch failed, write down why, and turn the top reasons into actions."),
            (5, "user-stories", "User Stories that Work", "writing", "A real user, a real need and a reason, as a card, a conversation and a confirmation."),
            (6, "example-mapping", "Example Mapping", "writing", "Rules, examples and questions on coloured cards, in 25 minutes with the three amigos."),
            (7, "definition-ready-done", "Definition of Ready & Done", "writing", "Short, shared checklists for starting work and calling it finished: live, measured, supported."),
            (8, "product-trio", "The Product Trio", "team", "Product, design and engineering discover together, every week, instead of handing over."),
            (9, "sprint-goals", "Sprint Goals", "team", "One sentence of value per sprint, so the team can make trade-offs without asking."),
            (10, "refinement", "Refinement that Isn't a Meeting Marathon", "team", "Small groups, short sessions, pre-reads: refine just enough, just in time."),
            (11, "tech-debt-talks", "Talking Tech Debt with Engineers", "team", "Translate debt into product terms, agree a share of capacity, and track what it buys."),
            (12, "launch-checklist", "Launch Checklist", "shipping", "Everything a launch needs beyond the code, with owners, and a go / no-go."),
            (13, "dark-launches", "Dark Launches & Rollouts", "shipping", "Ship behind a flag, turn it on for a few, watch guardrails, then widen."),
            (14, "hypercare", "Hypercare after Launch", "shipping", "Two weeks of daily watching and fast fixes after a launch, with clear exit criteria."),
            (15, "release-notes", "Release Notes & Customer Comms", "shipping", "Tell customers and staff what changed, why, and what to do, before they ask."),
        ],
    ),
    dict(
        key="product-4", vol=4, title="Measuring & Learning", short="measuring &amp; learning",
        series=2, book="The Product Owner's Notebook", narrator="Grace", brand="product owner's notebook", book_no=2,
        title_block=True, sheet_doodles="product",
        theme="theme-product", fonts="Permanent+Marker", subject="product ownership",
        problem_h2="The situation", related_h3="Related notes", map_caption="Translating it to the job", map_col="On the product",
        term="Autumn term · 2027", weekdays=(1, 4), start=date(2027, 9, 7),
        kicker="the product owner's notebook · book 2 · vol. 4",
        story="<b>May 2026.</b> Approvals is live in Amsterdam and coming to Rotterdam, the “no swaps” flag is used every day, and the board has been promised a range, not a number. Now Grace has to find out what's really working. This volume follows her from May to October 2026: measuring properly, running honest experiments, listening to support, operations and customers, and setting goals the team can actually steer by, including stopping what doesn't work.",
        lead="Volume 4 of <span class=\"hl\">The Product Owner's Notebook</span>: how a product owner finds out what's working and learns from it. {n} notes in {c} collections: instrument the product, experiment honestly, listen to the people closest to customers, and set goals worth steering by. Every note follows <b>Grace</b> at <b>Larder</b> from May to October 2026, after the approvals launch, and ends with a <b>try it</b> exercise for your own product.",
        blurb="Tracking plans, funnels, cohorts, A/B tests, guardrails, listening loops, OKRs and knowing when to stop.",
        attrs=PRODUCT_ATTRS, attrs_title="The nine product ratings", attrs_side="what a good product practice is judged on", ratings_h2="Product ratings",
        handmade=set(),
        collections=[
            ("instrumenting", "Instrumenting", "measure properly before you judge"),
            ("experimenting", "Experimenting", "test changes fairly, and read the results honestly"),
            ("listening", "Listening", "hear support, operations and customers, regularly"),
            ("goals", "Goals", "steer by outcomes, review honestly, stop what doesn't work"),
        ],
        catalogue=[
            (1, "event-tracking-plan", "Event Tracking Plan", "instrumenting", "One table of events: name, when it fires, properties, owner, the same on every platform."),
            (2, "funnels", "Funnels", "instrumenting", "Count users at every step to see where they drop out, before guessing why."),
            (3, "cohorts-retention", "Cohorts & Retention Curves", "instrumenting", "Compare groups that share a starting point to see whether customers come back."),
            (4, "dashboards", "Dashboards That Get Used", "instrumenting", "One page with the north star, its inputs and guardrails, reviewed weekly."),
            (5, "ab-tests", "A/B Tests", "experimenting", "Split customers at random, change one thing, and compare on the metric you chose in advance."),
            (6, "sample-size", "Sample Size & Test Duration", "experimenting", "Work out how many and how long before you start, so the answer means something."),
            (7, "guardrail-metrics", "Guardrail Metrics", "experimenting", "The numbers that mustn't get worse while you chase the one you want to improve."),
            (8, "reading-results", "Reading Results Honestly", "experimenting", "No peeking, no fishing in segments, ranges not points, and decisions you set in advance."),
            (9, "support-tickets-data", "Support Tickets as Data", "listening", "Tag tickets consistently and read them as a weekly signal of what hurts customers."),
            (10, "operations-feedback", "Feedback Loops with Operations", "listening", "A regular, easy channel from pickers and couriers to the team, with answers going back."),
            (11, "advisory-panel", "Customer Advisory Panel", "listening", "A small, varied group of customers for depth and early reactions, not for votes."),
            (12, "okrs", "OKRs", "goals", "An objective in words and a few measurable key results per quarter, graded honestly."),
            (13, "vanity-metrics", "Vanity vs Actionable Metrics", "goals", "Prefer numbers that change decisions over numbers that only look good."),
            (14, "post-launch-review", "Post-Launch Review", "goals", "Compare what you expected with what happened, and decide what to do next."),
            (15, "killing-a-feature", "Killing a Feature", "goals", "Remove features that don't earn their keep, carefully and on purpose."),
        ],
    ),
    dict(
        key="product-5", vol=5, title="Stakeholders & Influence", short="stakeholders &amp; influence",
        series=2, book="The Product Owner's Notebook", narrator="Grace", brand="product owner's notebook", book_no=2,
        title_block=True, sheet_doodles="product",
        theme="theme-product", fonts="Permanent+Marker", subject="product ownership",
        problem_h2="The situation", related_h3="Related notes", map_caption="Translating it to the job", map_col="On the product",
        term="Winter term · 2028", weekdays=(1, 4), start=date(2028, 1, 4),
        kicker="the product owner's notebook · book 2 · vol. 5",
        story="<b>October 2026.</b> Korenwolf has signed for three offices from January, the board expects swap refunds at 2 % by December, and Grace's work now depends on Dispatch, billing, operations and legal as much as on her own team. This volume follows her from October 2026 to March 2027: keeping people informed, managing up and across, treating operations, legal and the architect as partners, and handling fixed dates, bad news and decisions she disagrees with.",
        lead="Volume 5 of <span class=\"hl\">The Product Owner's Notebook</span>: how a product owner works with the people around the product. {n} notes in {c} collections: communicate so people read it, manage up and across, partner with operations, legal and architecture, and handle the hard moments. Every note follows <b>Grace</b> at <b>Larder</b> from October 2026 to March 2027, in the same months as Ana's third notebook, and ends with a <b>try it</b> exercise for your own product.",
        blurb="Updates that get read, demos, one-page PRDs, managing up, pitching, partners inside, fixed dates and bad news.",
        attrs=PRODUCT_ATTRS, attrs_title="The nine product ratings", attrs_side="what a good product practice is judged on", ratings_h2="Product ratings",
        handmade=set(),
        collections=[
            ("communicating", "Communicating", "write and show so people actually take it in"),
            ("managing", "Managing up and across", "your manager, the CEO, and the teams you depend on"),
            ("partners", "Partners inside", "operations, legal and architecture as partners, not gates"),
            ("hard", "Hard moments", "scope, fixed dates, bad news and decisions you disagree with"),
        ],
        catalogue=[
            (1, "product-update", "Product Update that Gets Read", "communicating", "A short weekly update: outcomes first, then shipped, learned, next and the asks."),
            (2, "demos", "Demos that Land", "communicating", "Show the customer's story with real data, to the people it changes, and ask for reactions."),
            (3, "one-page-prd", "The One-Page PRD", "communicating", "Problem, outcome, users, scope in and out, and open questions, on a single page."),
            (4, "quarterly-review", "The Quarterly Product Review", "communicating", "Once a quarter, leaders see outcomes against goals, what was learned and the next bets."),
            (5, "managing-up", "Managing Up", "managing", "No surprises: a regular, short channel with decisions, risks and wins for your manager."),
            (6, "pitching-to-ceo", "Pitching to the CEO", "managing", "Answer first, in the CEO's terms, with a small ask and a way to learn fast."),
            (7, "dependencies", "Dependencies across Teams", "managing", "See them early, ask in person, agree dates both sides track, and remove them when you can."),
            (8, "operations-as-customer", "Operations as a Customer", "partners", "Treat the pickers' and couriers' tools as a product with its own outcomes and roadmap."),
            (9, "legal-privacy", "Working with Legal & Privacy", "partners", "Bring legal in early with a clear question, and design privacy in rather than bolting it on."),
            (10, "working-with-architect", "Working with the Architect", "partners", "The product owner brings the why and the outcome; the architect brings the constraints and options."),
            (11, "account-managers", "Working with Account Managers", "partners", "Turn a big client's requests into problems the whole product can solve, without a custom fork."),
            (12, "negotiating-scope", "Negotiating Scope", "hard", "Trade on interests, not lists: find what each side really needs and split the rest into later."),
            (13, "fixed-date", "When the Date Is Fixed", "hard", "Fix the date, flex the scope: cut lines, buffers and an early first release."),
            (14, "bad-news", "Delivering Bad News", "hard", "Early, in person, with the facts, the cause, the options and what you'll do."),
            (15, "disagree-and-commit", "Disagree and Commit", "hard", "Argue your case once, clearly; once decided, commit fully, and agree how you'll know."),
        ],
    ),
    dict(
        key="product-6", vol=6, title="Growing the Product", short="growing the product",
        series=2, book="The Product Owner's Notebook", narrator="Grace", brand="product owner's notebook", book_no=2,
        title_block=True, sheet_doodles="product",
        theme="theme-product", fonts="Permanent+Marker", subject="product ownership",
        problem_h2="The situation", related_h3="Related notes", map_caption="Translating it to the job", map_col="On the product",
        term="Spring term · 2028", weekdays=(1, 4), start=date(2028, 3, 7),
        kicker="the product owner's notebook · book 2 · vol. 6",
        story="<b>April 2027.</b> Utrecht opens, Antwerp is coming, Larder Plus is about to launch and business customers want more than standing orders. Grace's product has grown from one problem into several products, and she has grown with it. This volume follows her from April to December 2027: launching cities and a country, serving business and consumer customers without splitting the product, scaling it with principles and platforms, and finally hiring the product owner who takes part of it over.",
        lead="Volume 6 of <span class=\"hl\">The Product Owner's Notebook</span>, the last: how a product owner grows a product, and themselves. {n} notes in {c} collections: new markets, business customers, scaling the product, and growing yourself. Every note follows <b>Grace</b> at <b>Larder</b> from April to December 2027, in the same months as Ana's fourth and fifth notebooks, and ends with a <b>try it</b> exercise for your own product.",
        blurb="New cities and a new country, pricing, B2B vs B2C, service levels, platforms, accessibility, principles and handing over.",
        attrs=PRODUCT_ATTRS, attrs_title="The nine product ratings", attrs_side="what a good product practice is judged on", ratings_h2="Product ratings",
        handmade=set(),
        collections=[
            ("markets", "New markets", "a city, a country and a price"),
            ("business", "Business customers", "one product for offices and households"),
            ("scaling", "Scaling the product", "platforms, principles and a product for everyone"),
            ("growing", "Growing yourself", "judgment, a career, a hire and a hand-over"),
        ],
        catalogue=[
            (1, "launching-new-city", "Launching a New City", "markets", "A repeatable playbook: what's configuration, what's local, and what to measure in the first weeks."),
            (2, "localisation", "Localisation for a New Country", "markets", "More than translation: language, money, rules, habits and testing with local customers."),
            (3, "pricing-experiments", "Pricing Experiments", "markets", "Find the price with research and careful tests, and watch what customers do, not just say."),
            (4, "b2b-vs-b2c", "B2B vs B2C Products", "business", "Business customers buy differently: buyers, users, contracts and service levels."),
            (5, "account-needs-vs-vision", "Account Needs vs Product Vision", "business", "Serve a big client without letting them steer the whole product."),
            (6, "service-levels-as-features", "Service Levels as Features", "business", "Make promises visible and measurable in the product: status, reports and automatic credits."),
            (7, "business-self-service", "Self-Service for Business Customers", "business", "Let office managers do it themselves, and free the account manager for the relationship."),
            (8, "platform-thinking", "Platform Thinking", "scaling", "Turn a capability several products need into one shared, owned, documented platform."),
            (9, "accessibility", "Accessibility as Product Quality", "scaling", "Build for everyone from the start, test with real users, and meet the law as a minimum."),
            (10, "product-led-growth", "Product-Led Growth", "scaling", "Let the product win and keep customers: a great first order, a trial, and sharing that works."),
            (11, "product-principles", "Writing Product Principles", "scaling", "A few beliefs with trade-offs that help a growing team decide like you would."),
            (12, "product-sense", "Product Sense", "growing", "Judgment you can train: customer empathy, taste, and seeing the whole system."),
            (13, "growing-as-po", "Growing as a Product Owner", "growing", "Look back, ask for feedback, and choose what to get better at next."),
            (14, "hiring-a-po", "Hiring a Product Owner", "growing", "Hire for judgment and curiosity, with a work sample that looks like the real job."),
            (15, "handing-over", "Handing Over a Product Area", "growing", "Pass on the why, the people and the open bets, then step back on purpose."),
        ],
    ),
]

# Planned journals and other work, shown on the landing page.
PLANNED = [
    (7, "AI App Patterns", "Retrieval-augmented generation, agents and tools, evaluation, guardrails and cost-aware LLM apps."),
]
# Planned volumes of Series 2, book 1 (see docs/HANDOFF-solution-architect.md).
PLANNED_2 = [
]
PLANNED_PRODUCT = [
]
FUTURE_LOG = [
    ("Dec 2026", [("•", "Vol. 7 · AI App Patterns"), ("•", "Search across every journal")]),
    ("Jan 2027", [("•", "One-page printable cheat sheet per collection")]),
    ("Feb 2027", [("•", "Vol. 1 extra notes: Strangler Fig, Backpressure, Consistent Hashing")]),
    ("Mar 2027", [("★", "Book 3 · <b>The Project Manager's Notebook</b> (Sanne, the Rotterdam launch): planning, estimation, risks and dependencies, delivery rhythms, status that tells the truth"), ("•", "Vol. 3 extra notes: Upserts, Bitemporal Data, Vector Indexes")]),
    ("Apr 2027", [("★", "Book 4 · <b>The Client Manager's Notebook</b> (Mo and Korenwolf): expectations, scope change, reporting, workshops, difficult conversations"), ("•", "Vol. 4 extra notes: Fuzzing, Visual Regression, Chaos Experiments")]),
    ("Mid 2027", [("•", "A Series 2 index: every Larder note from both books in one timeline")]),
    ("Someday", [("•", "Extra notes for Vols. 2, 5 and 6: Debounce &amp; Throttle, Passkeys, Signed Webhooks, Chaos Engineering, Service Catalogues"), ("•", "Quiz mode that remembers your score"), ("•", "A “compare two patterns” page")]),
]


def lecture_date(j, num):
    week, slot = divmod(num - 1, len(j["weekdays"]))
    wd = j["weekdays"][slot]
    return j["start"] + timedelta(weeks=week, days=wd - j["start"].weekday())


def day_label(j, num):
    d = lecture_date(j, num)
    return f"{d.strftime('%a')} · {d.strftime('%d.%m.%y')}"


def coll(j, key):
    return next(c for c in j["collections"] if c[0] == key)


def entry(j, slug):
    return next(c for c in j["catalogue"] if c[1] == slug)


def pdf_name(num, slug):
    return f"{num:02d}-{slug}.pdf"


def journal_pdf(j):
    return f"{j['key']}-journal.pdf"


# ---------------------------------------------------------------- page pieces
FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">\n'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
         '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Amatic+SC:wght@700&family=Caveat:wght@500;700&family=Courier+Prime:wght@400;700&family=Kalam:wght@400;700&family=Patrick+Hand&display=swap">')
DL = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" '
      'stroke-linejoin="round" aria-hidden="true"><path d="M12 3v12"/><path d="m7 10 5 5 5-5"/><path d="M5 21h14"/></svg>')
ROUGH = ('<svg width="0" height="0" style="position:absolute" aria-hidden="true" focusable="false">'
         '<filter id="rough" x="-5%" y="-5%" width="110%" height="110%"><feTurbulence type="fractalNoise" '
         'baseFrequency="0.028" numOctaves="2" seed="7" result="n"/><feDisplacementMap in="SourceGraphic" in2="n" '
         'scale="3.2"/></filter></svg>')
# Desk doodles drawn around an architect sheet (journals with sheet_doodles=True): a coffee ring,
# a drafting compass, and a pencil resting on a ruler. Decorative only; hidden on small screens.
SHEET_DOODLES = (
    '<div class="sheet-doodles" aria-hidden="true">'
    '<svg class="sd sd-coffee" viewBox="0 0 120 120"><g class="rough">'
    '<circle cx="60" cy="60" r="44" fill="none" style="stroke:var(--mustard);stroke-opacity:.35;stroke-width:7"/>'
    '<circle cx="60" cy="60" r="38" fill="none" style="stroke:var(--mustard);stroke-opacity:.22;stroke-width:2"/>'
    '<path d="M100 74 q8 6 4 14" fill="none" style="stroke:var(--mustard);stroke-opacity:.3;stroke-width:4;stroke-linecap:round"/></g></svg>'
    '<svg class="sd sd-compass" viewBox="0 0 70 110"><g class="rough">'
    '<path class="d" d="M33 4 v8"/><circle class="d f-y" cx="35" cy="18" r="8"/>'
    '<path class="d" d="M31 25 L14 98 M39 25 L56 98 M20 70 Q35 62 50 70"/>'
    '<path class="d d-pen" d="M56 98 l3 9"/><path class="d" d="M14 98 l-2 8"/>'
    '<path class="d d-thin d-dash" d="M12 106 Q35 120 59 107"/></g></svg>'
    '<svg class="sd sd-pencil" viewBox="0 0 240 80"><g class="rough">'
    '<rect class="d d-thin f-green" x="6" y="44" width="228" height="26" rx="3"/>'
    '<path class="d d-thin" d="M26 44 v10 M46 44 v6 M66 44 v10 M86 44 v6 M106 44 v10 M126 44 v6 M146 44 v10 M166 44 v6 M186 44 v10 M206 44 v6"/>'
    '<path class="d f-y" d="M40 30 L190 6 L196 18 L46 42 Z"/><path class="d f-pink" d="M190 6 l14 -2 l-8 14 z"/>'
    '<path class="d f-paper" d="M40 30 l-14 4 l20 8 z"/><path class="d d-thin" d="M58 27 l2 12"/></g></svg>'
    '</div>'
)
# Desk doodles around a product owner's sheet: a pad of sticky notes, a marker, and a pinned photo of the team wall.
PRODUCT_DOODLES = (
    '<div class="sheet-doodles" aria-hidden="true">'
    '<svg class="sd sd-coffee" viewBox="0 0 120 120"><g class="rough">'
    '<rect class="d d-thin f-y" x="14" y="20" width="84" height="84" rx="2" transform="rotate(8 56 62)"/>'
    '<rect class="d d-thin f-pink" x="22" y="12" width="84" height="84" rx="2" transform="rotate(-6 64 54)"/>'
    '<path class="d d-thin" d="M36 40 h44 M36 56 h36 M36 72 h40" transform="rotate(-6 64 54)"/></g></svg>'
    '<svg class="sd sd-compass" viewBox="0 0 70 110"><g class="rough">'
    '<rect class="d f-red" x="24" y="6" width="22" height="22" rx="4"/><rect class="d f-paper" x="22" y="26" width="26" height="62" rx="5"/>'
    '<path class="d" d="M22 46 h26"/><path class="d f-ink" d="M27 88 h16 l-5 14 h-6 z"/></g></svg>'
    '<svg class="sd sd-pencil" viewBox="0 0 240 80"><g class="rough">'
    '<rect class="d d-thin f-paper" x="20" y="8" width="200" height="66" rx="3"/>'
    '<path class="d d-thin d-soft" d="M40 30 h48 M100 30 h48 M160 30 h40"/>'
    '<rect class="d d-thin f-y" x="40" y="38" width="30" height="24"/><rect class="d d-thin f-green" x="100" y="38" width="30" height="24"/>'
    '<rect class="d d-thin f-blue" x="160" y="38" width="30" height="24"/><circle class="d f-red" cx="120" cy="10" r="6"/></g></svg>'
    '</div>'
)
DESK_DOODLES = {True: SHEET_DOODLES, "architect": SHEET_DOODLES, "product": PRODUCT_DOODLES}
KEY = '''  <aside class="key" aria-label="Key to the signifiers on this page">
    <h3>Key</h3>
    <ul>
      <li><span class="sig">–</span> note</li>
      <li><span class="sig">★</span> key idea</li>
      <li><span class="sig">!</span> watch out</li>
      <li><span class="sig">→</span> fix / leads to</li>
      <li><span class="sig">×</span> avoid</li>
      <li><span class="sig">✓</span> do this</li>
    </ul>
  </aside>
'''


def foot(j=None):
    what = (f"{j['book']} · vol. {j['vol']}" if j and j.get("book") else
            f"Vol. {j['vol']} · a student's bullet journal on {j['short']}") if j else "a shelf of student bullet journals on software design"
    return f'<footer class="foot"><span>Jef’s Notes · {what}</span><span>by {AUTHOR}</span></footer>'


def asset(name):
    """assets/<name>?v=<content hash>: a new version tag whenever the file changes, so browsers and the Cloudflare
    mirror never keep serving an old stylesheet or script after a deploy."""
    digest = hashlib.sha256((PUBLIC / "assets" / name).read_bytes()).hexdigest()[:10]
    return f"assets/{name}?v={digest}"


def stamp_handmade(path):
    """Hand-made notes link the assets directly; give them the same version tags."""
    html = path.read_text(encoding="utf-8")
    new = re.sub(r'(href|src)="((?:\.\./)*)assets/(notebook\.css|bujo\.css|notebook\.js)(?:\?v=[0-9a-f]+)?"',
                 lambda m: f'{m.group(1)}="{m.group(2)}{asset(m.group(3))}"', html)
    if new != html:
        path.write_text(new, encoding="utf-8")


def head(title, desc, depth, fonts=None):
    """fonts: an optional extra Google Fonts family query for a journal's own heading font."""
    a = "../" * depth
    extra = (f'\n<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family={fonts}&display=swap">' if fonts else "")
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<meta name="theme-color" content="#E6E3DC">
{FONTS}{extra}
<link rel="stylesheet" href="{a}{asset("notebook.css")}">
<link rel="stylesheet" href="{a}{asset("bujo.css")}">
<link rel="icon" href="{a}assets/favicon.svg" type="image/svg+xml">
<script src="{a}{asset("notebook.js")}" defer></script>
</head>'''


def body_open(j=None):
    cls = "bujo" + (f" {j['theme']}" if j and j["theme"] else "")
    return f'<body class="{cls}">'


def bar(j, depth, current=None, print_button=True, disabled=False):
    """depth: 0 = landing, 1 = journal index/all, 2 = a note."""
    root = "../" * depth
    cur = lambda k: ' aria-current="page"' if current == k else ""
    if j is None:
        nav = (f'<a href="{root}index.html#shelf"{cur("shelf")}>Journals</a>\n'
               f'      <a class="hide-sm" href="{root}index.html#future">Future log</a>')
        brand_small = "a shelf of design notebooks"
        btn = ""
    else:
        jp = "" if depth == 1 else "../"
        nav = (f'<a href="{root}index.html#shelf">Shelf</a>\n'
               f'      <a href="{jp}index.html#index"{cur("index")}>Index</a>\n'
               f'      <a class="hide-sm" href="{jp}all.html"{cur("all")}>Whole journal</a>')
        brand_small = (f"{j.get('brand', 'notebook')} · vol. {j['vol']}" if j.get("book") else f"vol. {j['vol']} · {j['short']}")
        if print_button:
            btn = f'\n      <button class="btn" type="button" data-print{" disabled" if disabled else ""}>{DL}Export as PDF</button>'
        else:
            btn = f'\n      <a class="btn" href="{jp}all.html?print">{DL}Export as PDF</a>'
    return f'''<header class="bar">
  <div class="bar-in">
    <a class="brand" href="{root}index.html"><b>Jef’s<span>.</span>Notes</b><small>{brand_small}</small></a>
    <nav aria-label="Main">
      {nav}{btn}
    </nav>
  </div>
</header>'''


def ratings_table(j, rows):
    assert len(rows) == 9, "nine ratings per note"
    trs = "\n".join(
        f'      <tr data-before="{b}" data-after="{a}"><td>{n}<small>{q}</small></td><td class="dcell"></td>'
        f'<td class="score"></td><td class="why">{why}</td></tr>'
        for (n, q, _), (b, a, why) in zip(j["attrs"], rows))
    return f'''  <div class="ratings-wrap table-scroll">
  <table class="ratings">
    <thead><tr><th scope="col">Quality</th><th scope="col">With the pattern</th><th scope="col">Before → after</th><th scope="col">Why</th></tr></thead>
    <tbody>
{trs}
    </tbody>
  </table>
  </div>
  <div class="legend"><span><i class="dot on"></i> kept</span><span><i class="dot gain"></i> gained</span><span><i class="dot lost"></i> lost</span><span>ratings are relative guidance for a typical app, not laws</span></div>'''


def li(items, cls=""):
    c = f' class="{cls}"' if cls else ""
    return f"<ul{c}>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


def h2(n, id_, title, side):
    return f'  <h2 id="{id_}"><span class="num">{n}</span>{title} <span class="side">{side}</span></h2>'


def pager(j, num):
    cat = j["catalogue"]
    prev = cat[num - 2] if num > 1 else None
    nxt = cat[num] if num < len(cat) else None
    a = (f'<a href="{prev[1]}.html"><small>← previous note</small>{prev[0]:02d} · {esc(prev[2])}</a>' if prev
         else '<a href="../index.html"><small>← back to</small>Index</a>')
    b = (f'<a href="{nxt[1]}.html"><small>Next note →</small>{nxt[0]:02d} · {esc(nxt[2])}</a>' if nxt
         else '<a href="../index.html"><small>back to →</small>Index</a>')
    return f'<nav class="pager" aria-label="Notes">\n  {a}\n  {b}\n</nav>'


def title_block(j, num, n):
    """The engineer's title block in the corner of a sheet (journals with title_block=True)."""
    if not j.get("title_block"):
        return ""
    rows = [("book", j.get("book", "")), ("vol.", j["vol"]), ("sheet", f"{num:02d} / {len(j['catalogue']):02d}"),
            ("rev.", n.get("rev", "A")), ("drawn by", AUTHOR.split()[0])]
    cells = "".join(f'<span class="tb-k">{k}</span><span class="tb-v">{v}</span>' for k, v in rows)
    return f'  <div class="titleblock" aria-label="Sheet details">{cells}</div>'


def meanwhile_box(j, n, back):
    """“Meanwhile, in X's notebook”: links between books that tell the same scene (note field `meanwhile`, plus
    the reverse links other books' notes made to this one)."""
    items = []
    for key, slug, here, *_ in n.get("meanwhile", []):
        o = journal(key)
        num, _, title, *_ = entry(o, slug)
        items.append((o, slug, title, here))
    for o, slug, title, line in back:
        items.append((o, slug, title, line))
    if not items:
        return ""
    lis = "".join(f'<li><a href="../../{o["key"]}/notes/{slug}.html"><b>{esc(title)}</b></a> <small>({o.get("narrator", "")}, '
                  f'vol. {o["vol"]})</small>: {line}</li>' for o, slug, title, line in items)
    who = sorted({o.get("narrator", "") for o, *_ in items})
    return (f'  <aside class="meanwhile" aria-label="Meanwhile, in another notebook">\n    <span class="tag">meanwhile, in '
            f'{" &amp; ".join(w + "\u2019s" for w in who)} notebook</span>\n    <ul>{lis}</ul>\n  </aside>')


def journal(key):
    return next(x for x in JOURNALS if x["key"] == key)


def render_note(j, n, back=()):
    num, slug, title, ckey, summary = entry(j, n["slug"])
    cname = coll(j, ckey)[1]
    vocab = "\n".join(f"    <div><dt>{t}</dt><dd>{d}</dd></div>" for t, d in n["vocab"])
    maprows = "\n".join(f"      <tr><td>{a}</td><td>{b}</td></tr>" for a, b in n["map"])
    steps = "\n".join(f"    <li><b>{t}</b><p>{d}</p></li>" for t, d in n["steps"])
    pits = "\n".join(f'    <li><h3>{t}</h3><p>{d} <span class="fix">Fix →</span> {f}</p></li>' for t, d, f in n["pitfalls"])
    quiz = "\n".join(f"    <details><summary>{q}</summary><p>{a}</p></details>" for q, a in n["quiz"])
    related = "".join(f"<li>{r}</li>" for r in n["related"])
    chips = "".join(f"<li><b>{k}:</b> {v}</li>" for k, v in n["chips"])
    sources = "".join(f"<li>{s}</li>" for s in n["sources"])
    code = n["code"]
    figs = lambda key: "\n".join(f.html() for f in n.get(key, []))
    parts = [
        head(f"{title} · Jef’s Notes", summary, 2, j.get("fonts")),
        body_open(j),
        '<a class="skip-link" href="#main">Skip to the notes</a>',
        bar(j, 2),
        '',
        '<main id="main" class="desk">',
        f'<article class="sheet" id="{slug}">',
        f'  {ROUGH}',
        DESK_DOODLES.get(j.get("sheet_doodles"), "") if j.get("sheet_doodles") else "",
        f'  <div class="page-meta"><span class="day">{day_label(j, num)}</span><span class="topic">collection · <b>{cname.lower()}</b></span></div>',
        f'  <p class="kicker">{n["kicker"]}</p>',
        f'  <h1><span class="hl">{esc(title)}</span></h1>',
        f'  <div class="tldr">\n    <span class="tag">TL;DR</span>\n    <p>{n["tldr"]}</p>\n  </div>',
        f'  <ul class="chips" aria-label="At a glance">{chips}</ul>',
        KEY,
        h2(1, "problem", j.get("problem_h2", "The problem"), n.get("problem_side", "why do we even need this?")),
        n["problem"], figs("problem_figs"), n.get("problem_after", ""), meanwhile_box(j, n, back),
        h2(2, "analogy", "Real-life analogy", n["analogy_side"]),
        n["analogy"], figs("analogy_figs"),
        f'''  <div class="table-scroll">
  <table class="map">
    <caption>{j.get("map_caption", "Translating it to software")}</caption>
    <thead><tr><th scope="col">In real life</th><th scope="col">{j.get("map_col", "In your code")}</th></tr></thead>
    <tbody>
{maprows}
    </tbody>
  </table>
  </div>''',
        n.get("analogy_after", ""),
        h2(3, "how", "How it solves it", n["how_side"]),
        n["how"], figs("how_figs"),
        f'  <ol class="steps">\n{steps}\n  </ol>',
        n.get("how_after", ""),
        f'  <h3>Vocabulary for the exam</h3>\n  <dl class="vocab">\n{vocab}\n  </dl>',
        f'''  <div class="card">
    <div class="card-head"><span>{esc(code["file"])}</span><span>{esc(code["note"])}</span></div>
<pre><code>{esc(code["src"].strip(chr(10))) if code.get("plain") else highlight(code["src"].strip(chr(10)))}</code></pre>
  </div>''',
        f'  <p class="aside">{n["tools"]}</p>' if n.get("tools") else "",
        h2(4, "tradeoffs", "Gains vs losses", "nothing is free"),
        f'''  <div class="tchart">
    <div class="gain">
      <h3>What we gain</h3>
      {li(n["gains"])}
    </div>
    <div class="loss">
      <h3>What we lose</h3>
      {li(n["losses"])}
    </div>
  </div>''',
        h2(5, "ratings", j["ratings_h2"], "1 = poor · 5 = great"),
        f'  <p>{n["baseline"]}</p>',
        ratings_table(j, n["ratings"]),
        h2(6, "pitfalls", "Common pitfalls", n.get("pitfalls_side", "the usual ways this goes wrong")),
        f'  <ul class="pits">\n{pits}\n  </ul>',
        h2(7, "when", "When to use it (and when not)", ""),
        f'''  <div class="grid2">
    <div>
      <h3 class="green">Use it when…</h3>
      {li(n["use"], "check yes")}
    </div>
    <div>
      <h3 class="red">Skip it when…</h3>
      {li(n["skip"], "check no")}
    </div>
  </div>''',
        f'  <h3>{j.get("related_h3", "Related patterns")}</h3>\n  <ul class="related">{related}</ul>',
        h2(8, "quiz", "Self-check quiz", ""),
        f'  <div class="quiz">\n{quiz}\n  </div>',
        f'  <div class="tryit">\n    <span class="tag">try it</span>\n    <p>{n["try_it"]}</p>\n  </div>' if n.get("try_it") else "",
        f'  <div class="remember">\n    <span class="tag">remember!!</span>\n    <p>{n["remember"]}</p>\n  </div>',
        f'''  <div class="export no-print">
    <button class="btn" type="button" data-print>{DL}Export this note as PDF</button>
    {"" if j.get("draft") else f'<a class="btn btn--ghost" href="../pdf/{pdf_name(num, slug)}">Download ready-made PDF</a>'}
    <span class="hint">In the print window choose “Save as PDF”. On a phone, the ready-made PDF is easiest.</span>
  </div>''',
        f'  <div class="sources">\n    <h3>Further reading</h3>\n    <ul>{sources}</ul>\n  </div>',
        title_block(j, num, n),
        f'  <p class="folio">{num:02d}</p>',
        '</article>',
        '',
        pager(j, num),
        foot(j),
        '</main>',
        '</body>',
        '</html>',
        '',
    ]
    return "\n".join(p for p in parts if p)


def index_list(j, anchors=False):
    out = []
    for key, name, blurb in j["collections"]:
        items = []
        for num, slug, title, ckey, summary in j["catalogue"]:
            if ckey != key:
                continue
            href = f"#{slug}" if anchors else f"notes/{slug}.html"
            items.append(f'<li><a href="{href}"><span class="toc-n">{num:02d}</span><span class="toc-t">{esc(title)}'
                         f'<small>{esc(summary)}</small></span><span class="toc-p">p. {num:02d}</span></a></li>')
        out.append(f'  <h3 class="toc-coll">{name} <span>{esc(blurb)}</span></h3>\n  <ol class="toc">{"".join(items)}</ol>')
    return "\n".join(out)


def attrs_block(j):
    dl = "\n".join(f"    <div><dt>{n}</dt><dd>{d}</dd></div>" for n, _, d in j["attrs"])
    return f'''  <dl class="vocab">
{dl}
  </dl>
  <div class="legend"><span><i class="dot on"></i> kept</span><span><i class="dot gain"></i> gained with the pattern</span><span><i class="dot lost"></i> lost with the pattern</span></div>'''


def story_box(j):
    """Series 2 books open with a short “story so far” that links to the Larder case file."""
    if not j.get("story"):
        return ""
    return (f'  <aside class="story" aria-label="The story so far">\n    <span class="tag">the story so far</span>\n'
            f'    <p>{j["story"]}</p>\n    <p class="story-link"><a href="../larder/index.html">Meet Larder: the case file, the cast '
            f'and the timeline →</a></p>\n  </aside>')


def counts(j):
    return dict(n=len(j["catalogue"]), c=["zero", "one", "two", "three", "four", "five", "six"][len(j["collections"])])


def render_index(j):
    return "\n".join([
        head(f"{j['title']} · Jef’s Notes", j["blurb"], 1, j.get("fonts")),
        body_open(j),
        '<a class="skip-link" href="#main">Skip to the index</a>',
        bar(j, 1, "index", print_button=False),
        '<main id="main" class="desk">',
        '<article class="sheet">',
        f'  <div class="page-meta"><span class="day">{j["term"]}</span><span class="topic">vol. {j["vol"]} · <b>{j["subject"]}</b></span></div>',
        f'  <p class="kicker">{j["kicker"]}</p>',
        f'  <h1 class="cover-title"><span class="hl">{esc(j["title"])}</span></h1>',
        f'  <p class="lead">{j["lead"].format(**counts(j))}</p>',
        story_box(j),
        KEY,
        '  <h2 id="index"><span class="num">✎</span>Index <span class="side">tap a note to open it</span></h2>',
        index_list(j),
        '  <h2 id="how-to-read"><span class="num">?</span>How every note is laid out <span class="side">same eight sections, every time</span></h2>',
        f'''  <ol class="how-to">
    <li><b>{j.get("problem_h2", "The problem")}</b>: {"a scene from the case study where it goes wrong" if j.get("book") else "what breaks without the pattern"}, with a doodle.</li>
    <li><b>Real-life analogy</b>: an everyday version, plus a “{j.get("map_caption", "translate to code").lower()}” table.</li>
    <li><b>How it solves it</b>: diagrams, steps, vocabulary and a {"template" if j.get("book") else "code"} card.</li>
    <li><b>Gains vs losses</b>: the trade-off spread.</li>
    <li><b>Ratings</b>: nine qualities, before → after.</li>
    <li><b>Common pitfalls</b>: each with its fix.</li>
    <li><b>When to use it</b>: and when to skip it.</li>
    <li><b>Self-check quiz</b>: tap a question to see the answer.</li>
  </ol>''',
        f'  <h2 id="ratings-key"><span class="num">★</span>{j["attrs_title"]} <span class="side">{j["attrs_side"]}</span></h2>',
        '  <p>Every note scores the pattern from 1 (poor) to 5 (great) on the same nine things, comparing an app <b>without</b> the pattern to the same app <b>with</b> it.</p>',
        attrs_block(j),
        '''  <div class="remember">
    <span class="tag">first law</span>
    <p>Everything in architecture is a trade-off. If you think you've found one that isn't, you haven't found the cost yet.</p>
  </div>''',
        f'''  <div class="export no-print">
    <a class="btn" href="all.html?print">{DL}Export the whole journal as PDF</a>
    {"" if j.get("draft") else f'<a class="btn btn--ghost" href="pdf/{journal_pdf(j)}">Download ready-made PDF</a>'}
    <span class="hint">On a phone, the ready-made PDF is the easiest way to save or share.</span>
  </div>''',
        '  <p class="folio">i</p>',
        '</article>',
        foot(j),
        '</main>',
        '</body>',
        '</html>',
        '',
    ])


def render_all(j):
    collect = " ".join(f"notes/{c[1]}.html" for c in j["catalogue"])
    return "\n".join([
        head(f"{j['title']} · Whole journal", "Every note on one page, ready to export as PDF.", 1, j.get("fonts")),
        body_open(j),
        '<a class="skip-link" href="#main">Skip to the notes</a>',
        bar(j, 1, "all", print_button=True, disabled=True),
        f'<main id="main" class="desk" data-collect="{collect}">',
        '<section class="sheet">',
        f'  <div class="page-meta"><span class="day">{j["term"]}</span><span class="topic">vol. {j["vol"]} · <b>{j["subject"]}</b></span></div>',
        '  <p class="kicker">the whole journal, one note per page</p>',
        f'  <h1 class="cover-title"><span class="hl">{esc(j["title"])}</span></h1>',
        f'  <p class="lead">{j["blurb"]}</p>',
        KEY,
        '  <h2 id="index"><span class="num">✎</span>Index <span class="side">page numbers match the notes</span></h2>',
        index_list(j, anchors=True),
        f'''  <div class="export no-print">
    <button class="btn" type="button" data-print disabled>{DL}Export as PDF</button>
    <span class="hint" data-collect-status role="status">Loading notes…</span>
  </div>
  <p class="aside no-print">in the print window pick “Save as PDF” as the destination. Each note starts on a new page.</p>''',
        '</section>',
        '</main>',
        f'<footer class="foot desk" style="padding-block:0 40px"><span>Jef’s Notes · Vol. {j["vol"]} · by {AUTHOR}</span></footer>',
        '</body>',
        '</html>',
        '',
    ])


AUTHOR_NOTE = """  <h2 id="author"><span class="num">✎</span>A note from the author <span class="side">why I made these journals</span></h2>
  <aside class="author-note" aria-labelledby="author">
    <p class="lead">Your AI agent can write a saga orchestrator in eleven seconds. It cannot tell you whether you needed one.</p>
    <p>These notebooks are for that second part. They're for new developers learning what all the arrows mean, and for experienced ones who've been nodding along in design reviews since 2019. They're short on purpose. Read one on the train, in a tunnel with no signal, or while the progress bar says “Thinking…” for the fourth minute.</p>
    <p>Each note gives you three things:</p>
    <ul>
      <li><b>Better questions for the code review.</b> When the agent says “Done! ✅”, you'll know to ask: <i>is this idempotent? Where's the timeout? What happens when it runs twice?</i> Ask before you tell your boss it's done. Not after.</li>
      <li><b>Better prompts for the next ticket.</b> “Add retries” gets you a loop. “Add capped retries with jitter and an idempotency key, only on 5xx” gets you a pattern. Vocabulary is leverage.</li>
      <li><b>A sense of the trade-offs.</b> Every pattern here has a “what we lose” column. The agent rarely volunteers that column. Somebody in the room should know it exists.</li>
    </ul>
    <p>The honest origin story: I had usage left before my weekly limit reset, and wasting it felt worse than wasting snacks. So I asked the agent to help me write notes about what agents get wrong. It found this very relatable.</p>
    <p class="author-sign">Read one note a day. Argue with the ratings. Doodle in the margins.<br><span>by Jefrey Romel Tagunicar</span></p>
  </aside>"""


def shelf():
    """Journals shown on the landing page and built into PDFs (drafts are rendered but unlisted)."""
    return [j for j in JOURNALS if not j.get("draft")]


CASEFILE_ITEM = '''    <li class="book book--casefile">
      <a class="book-cover" href="larder/index.html" aria-label="Open the case file: Meet Larder">
        <span class="book-band" aria-hidden="true"></span>
        <span class="book-label"><small>series 2 · read first</small><b>Meet Larder</b><i>the case file</i></span>
      </a>
      <div class="book-meta">
        <p>The company every Series 2 book follows: its history, where it stands, its goals, the cast, and a timeline of every note.</p>
        <p class="book-actions"><a class="btn" href="larder/index.html">Open the case file</a></p>
      </div>
    </li>'''


def book_items(journals, planned, series=1, book=1, casefile=False):
    books = [CASEFILE_ITEM] if casefile else []
    for j in journals:
        k = j["key"]
        vol = f"book {book} · vol. {j['vol']}" if series == 2 else f"vol. {j['vol']}"
        n = len(j["catalogue"])
        count = (f"{n} note{'s' if n != 1 else ''} · in progress" if j.get("in_progress")
                 else f"{n} notes · {len(j['collections'])} collections")
        books.append(f'''    <li class="book book--{k}">
      <a class="book-cover" href="{k}/index.html" aria-label="Open {vol}: {esc(j['title'])}">
        <span class="book-band" aria-hidden="true"></span>
        <span class="book-label"><small>{vol}</small><b>{esc(j['title'])}</b><i>{count}</i></span>
      </a>
      <div class="book-meta">
        <p>{j['blurb']}</p>
        <p class="book-actions"><a class="btn" href="{k}/index.html">Open journal</a><a class="btn btn--ghost" href="{k}/pdf/{journal_pdf(j)}">{DL}PDF</a></p>
      </div>
    </li>''')
    for vol, title, blurb in planned:
        label = f"book {book} · vol. {vol}" if series == 2 else f"vol. {vol}"
        books.append(f'''    <li class="book book--planned">
      <div class="book-cover" aria-hidden="true"><span class="book-label"><small>{label}</small><b>{title}</b><i>planned</i></span></div>
      <div class="book-meta"><p><b>{label[0].upper() + label[1:]} · {title}.</b> {blurb}</p></div>
    </li>''')
    return "\n".join(books)


def render_landing(sheets=()):
    series1 = [j for j in shelf() if j.get("series", 1) == 1]
    series2 = [j for j in shelf() if j.get("series", 1) == 2]
    months = []
    for month, items in FUTURE_LOG:
        lis = "".join(f'<li><span class="sig">{s}</span> {t}</li>' for s, t in items)
        months.append(f'    <div class="month"><h3>{month}</h3><ul>{lis}</ul></div>')
    total = sum(len(j["catalogue"]) for j in shelf())
    return "\n".join([
        head("Jef’s Notes", "A shelf of student bullet journals on software design patterns and the work around the code, with doodles, analogies, trade-offs and ratings.", 0, "Architects+Daughter&family=Permanent+Marker&family=IBM+Plex+Sans+Condensed:wght@700"),
        body_open(),
        '<a class="skip-link" href="#main">Skip to the shelf</a>',
        bar(None, 0, "shelf"),
        '<main id="main" class="desk">',
        '<article class="sheet landing">',
        '  <div class="page-meta"><span class="day">The shelf · 2026</span><span class="topic">series · <b>software design</b></span></div>',
        '  <p class="kicker">hand-written field journals, one subject per volume</p>',
        '  <h1 class="cover-title"><span class="hl">Jef’s Notes</span></h1>',
        f'  <p class="lead">A student\'s bullet journals on software design patterns, and now on the work around the code: what problem each idea solves, an everyday analogy with doodles, how it works, what it costs, how it rates, and how people get it wrong. <b>{len(shelf())} volumes, {total} notes</b> in two series so far, more on the way.</p>',
        '  <h2 id="shelf"><span class="num">✎</span>The shelf <span class="side">series 1 · design patterns</span></h2>',
        f'  <ul class="shelf">\n{book_items(series1, PLANNED)}\n  </ul>',
        '  <h2 id="series-2"><span class="num">✎</span>Series 2 · The Practitioner\'s Notebooks <span class="side">book 1 · the solution architect</span></h2>',
        '  <p>The second series is about the work <b>around</b> the code. Book 1, <b>The Solution Architect\'s Notebook</b>, follows one company, <b>Larder</b>, a grocery delivery start-up growing from one city to six, from a vague business plan to a running architecture. Same eight sections, a template to copy in every note, and a <b>try it</b> exercise for your own project.</p>',
        '  <h3 class="shelf-book">Book 1 · The Solution Architect\'s Notebook <span>narrated by Ana</span></h3>',
        f'  <ul class="shelf shelf-series">\n{book_items([j for j in series2 if j.get("book_no", 1) == 1], PLANNED_2, series=2, book=1, casefile=True)}\n  </ul>',
        '  <h3 class="shelf-book">Book 2 · The Product Owner\'s Notebook <span>narrated by Grace</span></h3>',
        f'  <ul class="shelf shelf-series">\n{book_items([j for j in series2 if j.get("book_no", 1) == 2], PLANNED_PRODUCT, series=2, book=2)}\n  </ul>',
        '  <h2 id="cheatsheets"><span class="num">⌘</span>Cheat sheets <span class="side">laminated reference cards</span></h2>',
        '  <p>Short, dense, printable: the commands and decisions you look up twice a week, on a few A4 cards. Reads fine on a phone too.</p>',
        f'  <ul class="shelf shelf-series">\n{cheatsheet_items(sheets)}\n  </ul>',
        AUTHOR_NOTE,
        '  <h2 id="future"><span class="num">→</span>Future log <span class="side">plans, not promises</span></h2>',
        '  <p>In a bullet journal the <b>future log</b> is where next months\' plans go. Here\'s what I\'m planning to write next.</p>',
        '  <p class="aside">series 2 (★) has begun with the solution architect\'s notebook. Next come notebooks for product managers, project managers and anyone who manages clients. Same format: the problem, an analogy, how it works, trade-offs, pitfalls and a quiz.</p>',
        f'  <div class="future">\n{chr(10).join(months)}\n  </div>',
        '  <h2 id="inside"><span class="num">?</span>What\'s inside every note <span class="side">same eight sections</span></h2>',
        '''  <ol class="how-to">
    <li><b>The problem</b> the pattern solves, with a doodle.</li>
    <li><b>A real-life analogy</b> and a “translate to code” table.</li>
    <li><b>How it works</b>: diagrams, steps, vocabulary, a code card.</li>
    <li><b>Gains vs losses</b>, side by side.</li>
    <li><b>Nine ratings</b> picked for each journal's subject.</li>
    <li><b>Common pitfalls</b> and their fixes.</li>
    <li><b>When to use it</b>, and when not to.</li>
    <li><b>A self-check quiz.</b></li>
  </ol>''',
        '  <p class="folio">✦</p>',
        '</article>',
        foot(),
        '</main>',
        '</body>',
        '</html>',
        '',
    ])


def load_casefile():
    f = CONTENT / "larder" / "casefile.py"
    spec = importlib.util.spec_from_file_location("larder_casefile", f)
    mod = importlib.util.module_from_spec(spec)
    mod.__dict__["Doodle"] = Doodle
    spec.loader.exec_module(mod)
    return mod


def render_casefile():
    """The Larder case file: the company, history, goals, cast, books and story timeline behind Series 2."""
    c = load_casefile()
    history = "\n".join(f'    <li><span class="when">{w}</span><p>{t}</p></li>' for w, t in c.HISTORY)
    stats = "\n".join(f'    <div class="stat"><b>{v}</b><span>{l}</span><small>{n}</small></div>' for v, l, n in c.STATS)
    drivers = "\n".join(f"    <li><b>{d}</b>: {m}</li>" for d, m in c.DRIVERS)
    cast = "\n".join(
        f'    <li class="person person--{col}"><span class="avatar" aria-hidden="true">{ini}</span>'
        f'<div><h3>{name}</h3><p class="role">{role}</p><p><b>Cares about:</b> {cares}</p><p><b>Fears:</b> {fears}</p>'
        f'<p class="books">{books}</p></div></li>'
        for ini, name, role, cares, fears, books, col in c.CAST)
    def book_card(b):
        num, title, who, when, status, summary, link = b
        head_ = f'<a href="{link}">{title}</a>' if link else title
        return (f'    <li class="bookcard{" bookcard--planned" if not link else ""}"><p class="bk">{num} · narrated by {who} · {when}'
                f'<span class="status">{status}</span></p><h3>{head_}</h3><p>{summary}</p></li>')
    books = "\n".join(book_card(b) for b in c.BOOKS)
    months = []
    for _, label, items in c.TIMELINE:
        lis = "".join(
            f'<li class="tl-{k}"><span class="sig">{"★" if k == "s" else "✎"}</span> '
            + (f'<a href="{href}">{t}</a>' if href else t) + '</li>' for t, href, k in items)
        months.append(f'    <div class="month"><h3>{label}</h3><ul>{lis}</ul></div>')
    j = dict(theme="theme-architect casefile")
    return "\n".join([
        head("Meet Larder · Jef’s Notes", "The case file for Series 2: Larder's history, goals, cast, books and story timeline.", 1, "Architects+Daughter"),
        body_open(j),
        '<a class="skip-link" href="#main">Skip to the case file</a>',
        bar(None, 1),
        '<main id="main" class="desk">',
        '<article class="sheet">',
        f'  {ROUGH}',
        SHEET_DOODLES,
        '  <div class="page-meta"><span class="day">Case file · Oct 2025</span><span class="topic">series 2 · <b>read this first</b></span></div>',
        '  <p class="kicker">the company behind the practitioner\'s notebooks</p>',
        '  <h1 class="cover-title"><span class="hl">Meet Larder</span></h1>',
        f'  <p class="lead">{c.LEAD}</p>',
        '  <h2 id="premise"><span class="num">1</span>The premise <span class="side">what Larder does</span></h2>',
        c.PREMISE,
        '  <h2 id="history"><span class="num">2</span>How it got here <span class="side">2024 → 2025</span></h2>',
        f'  <ol class="history">\n{history}\n  </ol>',
        '  <h2 id="now"><span class="num">3</span>Where things stand <span class="side">October 2025, Amsterdam</span></h2>',
        f'  <div class="stats">\n{stats}\n  </div>',
        '  <p>The systems: <b>Larder Core</b> (one Django app on PostgreSQL that runs the shop, orders, payments, stock, picking, '
        'dispatch and support), the customer apps and web shop, the picker app in the stores, <b>StockPilot</b> (a rented warehouse '
        'system), a payment provider and a helpdesk tool. See the <a href="../architect-1/notes/system-context.html">system context diagram</a>.</p>',
        '  <h2 id="goals"><span class="num">4</span>The goals <span class="side">six cities by the end of 2027</span></h2>',
        c.cities.html(),
        '  <p>Femke, Marco and Joost agreed four business drivers in October 2025. Every book measures its choices against them:</p>',
        f'  <ul class="drivers">\n{drivers}\n  </ul>',
        '  <h3>And a second business: Larder for Business</h3>',
        c.KORENWOLF,
        '  <h2 id="cast"><span class="num">5</span>The cast <span class="side">who\'s who, and who tells the story</span></h2>',
        f'  <ul class="cast">\n{cast}\n  </ul>',
        '  <h2 id="books"><span class="num">6</span>The books <span class="side">one company, four notebooks</span></h2>',
        c.two_books.html(),
        f'  <ul class="bookcards">\n{books}\n  </ul>',
        '  <h2 id="timeline"><span class="num">7</span>The story timeline <span class="side">every note, pinned to its date</span></h2>',
        '  <p>Read one book from start to end, or follow the story in date order across books. <span class="sig-inline">★</span> story events · <span class="sig-inline">✎</span> Ana’s notebook · <span class="sig-inline sig-2">✎</span> Grace’s notebook.</p>',
        f'  <div class="future timeline">\n{chr(10).join(months)}\n  </div>',
        '  <p class="aside">the facts on this page are the source of truth for every note. If a note and this page disagree, this page wins (and the note gets fixed).</p>',
        '  <p class="folio">✦</p>',
        '</article>',
        foot(),
        '</main>',
        '</body>',
        '</html>',
        '',
    ])


# ---------------------------------------------------------------- cheat sheets (laminated reference cards)
CHEATSHEETS = ["git_flow", "docker_k8s"]
CS_FONTS = "IBM+Plex+Mono:wght@400;600&family=IBM+Plex+Sans+Condensed:wght@600;700&family=IBM+Plex+Sans:ital,wght@0,400;0,500;0,600;0,700;1,400"
CS_LOGO = ('<svg viewBox="0 0 34 34" aria-hidden="true"><rect width="34" height="34" rx="8" fill="#FFFFFF" fill-opacity=".1"/>'
           '<path d="M10 7v20" stroke="var(--b-main)" stroke-width="3" stroke-linecap="round" fill="none"/>'
           '<path d="M10 22c0-6 14-4 14-11" stroke="var(--b-feat)" stroke-width="3" stroke-linecap="round" fill="none"/>'
           '<circle cx="10" cy="27" r="3.4" fill="var(--b-main)"/><circle cx="10" cy="8" r="3.4" fill="var(--b-main)"/>'
           '<circle cx="24" cy="10" r="3.4" fill="var(--b-feat)"/></svg>')


def load_cheatsheet(name):
    f = CONTENT / "cheatsheets" / f"{name}.py"
    spec = importlib.util.spec_from_file_location(f"cheatsheet_{name}", f)
    mod = importlib.util.module_from_spec(spec)
    mod.__dict__.update(Graph=cheatsheet.Graph, Diagram=cheatsheet.Diagram, cmd=cheatsheet.cmd, code=cheatsheet.code, box=cheatsheet.box)
    spec.loader.exec_module(mod)
    return mod


def cheatsheet_pdf(cs):
    return f"{cs.SLUG}-cheat-sheet.pdf"


def render_cheatsheet(cs):
    n = len(cs.PAGES)
    pages = []
    for i, p in enumerate(cs.PAGES, 1):
        body = []
        if p.get("figure"):
            body.append(f'<figure class="cs-fig">{p["figure"]}</figure>')
            body.append('<p class="cs-swipe">← swipe the diagram →</p>')
        if p.get("legend"):
            body.append('<ul class="cs-legend">' + "".join(
                f'<li><i style="--c:var(--b-{c})"></i><b>{esc(name)}</b> {esc(what)}</li>' for c, name, what in p["legend"]) + "</ul>")
        if p.get("strategies"):
            body.append(f'<h3 class="cs-strat-h">{p.get("strategies_title", "Merge strategies: pick per target branch")}</h3>')
            body.append('<div class="cs-strats">' + "".join(
                f'<section class="cs-strat"><h3>{t} <code>{esc(flag)}</code></h3>{svg}<p>{what}</p><p>{use}</p></section>'
                for t, flag, svg, what, use in p["strategies"]) + "</div>")
        body.append('<div class="cs-grid">\n' + "\n".join(p["boxes"]) + "\n</div>")
        html = "\n".join(body)
        # scenario lists: keep each question with its answer
        html = re.sub(r'<dl class="scen">(.*?)</dl>', lambda m: '<dl class="scen">' + re.sub(
            r"(<dt>.*?</dt>\s*<dd>.*?</dd>)", r"<div>\1</div>", m.group(1), flags=re.S) + "</dl>", html, flags=re.S)
        pages.append(f'''<article class="cs-page" id="p{i}" aria-labelledby="p{i}-h">
<header class="cs-head">
  <div class="cs-logo">{getattr(cs, "LOGO", CS_LOGO)}<span>{esc(cs.TITLE)}<br>cheat sheet</span></div>
  <h2 id="p{i}-h">{p["title"]}<small>{p["kicker"]}</small></h2>
  <div class="cs-num"><b>{i}/{n}</b>card</div>
</header>
<div class="cs-body">
{html}
</div>
<footer class="cs-foot"><span>Jef’s Notes · cheat sheets · {esc(cs.TITLE.lower())}</span><span>{esc(cs.VERSION)} · by {AUTHOR}</span></footer>
</article>''')
    toc = "".join(f'<li><a href="#p{i}"><b>{i}</b>{p["title"]}</a></li>' for i, p in enumerate(cs.PAGES, 1))
    return "\n".join([
        head(f"{cs.TITLE} cheat sheet · Jef’s Notes", cs.DESC, 2, CS_FONTS).replace(
            "</head>", f'<link rel="stylesheet" href="../../{asset("cheatsheet.css")}">\n</head>'),
        '<body class="bujo cheat">',
        '<a class="skip-link" href="#main">Skip to the cheat sheet</a>',
        f'''<header class="bar">
  <div class="bar-in">
    <a class="brand" href="../../index.html"><b>Jef’s<span>.</span>Notes</b><small>cheat sheet · {esc(cs.TITLE.lower())}</small></a>
    <nav aria-label="Main">
      <a href="../../index.html#shelf">Shelf</a>
      <a href="../../index.html#cheatsheets">Cheat sheets</a>
      <a class="btn" href="pdf/{cheatsheet_pdf(cs)}" download>{DL}PDF</a>
    </nav>
  </div>
</header>''',
        '<main id="main" class="desk">',
        '<div class="cs-main">',
        f'''<section class="cs-intro" aria-labelledby="cs-title">
  <p class="kicker">a laminated reference card · {n} pages · A4</p>
  <h1 id="cs-title"><span>{esc(cs.TITLE)}</span> cheat sheet</h1>
  <p class="lead">{esc(cs.SUBTITLE[0].upper() + cs.SUBTITLE[1:])}. Each card is one printed page: diagram on top, copy-paste commands below.</p>
  <div class="cs-actions"><a class="btn" href="pdf/{cheatsheet_pdf(cs)}" download>{DL}Download the PDF</a><button class="btn btn--ghost" type="button" data-print>Print</button></div>
  <ul class="cs-toc">{toc}</ul>
</section>''',
        *pages,
        '</div>',
        foot().replace("a shelf of student bullet journals on software design", f"cheat sheet · {esc(cs.TITLE.lower())}"),
        '</main>',
        '</body>',
        '</html>',
        '',
    ])


def cheatsheet_items(sheets):
    out = []
    for cs in sheets:
        href = f"cheatsheets/{cs.SLUG}/index.html"
        out.append(f'''    <li class="book book--cheat">
      <a class="book-cover" href="{href}" aria-label="Open the {esc(cs.TITLE)} cheat sheet">
        <span class="book-band" aria-hidden="true"></span>
        <span class="book-label"><small>cheat sheet</small><b>{esc(cs.TITLE)}</b><i>{len(cs.PAGES)} cards · A4</i></span>
      </a>
      <div class="book-meta">
        <p>{cs.BLURB}</p>
        <p class="book-actions"><a class="btn" href="{href}">Open cheat sheet</a><a class="btn btn--ghost" href="cheatsheets/{cs.SLUG}/pdf/{cheatsheet_pdf(cs)}">{DL}PDF</a></p>
      </div>
    </li>''')
    return "\n".join(out)


def redirect(to):
    return (f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Moved</title>'
            f'<meta http-equiv="refresh" content="0; url={to}"><link rel="canonical" href="{to}"></head>'
            f'<body><p>This page moved to <a href="{to}">{to}</a>.</p></body></html>\n')


def load_content(key):
    notes = {}
    for f in sorted((CONTENT / key).glob("*.py")):
        spec = importlib.util.spec_from_file_location(f"{key}_{f.stem}", f)
        mod = importlib.util.module_from_spec(spec)
        mod.__dict__["Doodle"] = Doodle
        spec.loader.exec_module(mod)
        for n in getattr(mod, "NOTES", []):
            notes[n["slug"]] = n
    return notes


def main():
    listing = []
    loaded = {j["key"]: load_content(j["key"]) for j in JOURNALS}
    back = {}
    for j in JOURNALS:
        for slug, n in loaded[j["key"]].items():
            num, _, title, *_ = entry(j, slug)
            for key, oslug, here, *there in n.get("meanwhile", []):
                back.setdefault((key, oslug), []).append((j, slug, title, there[0] if there else here))
    for j in JOURNALS:
        key = j["key"]
        out = PUBLIC / key
        (out / "notes").mkdir(parents=True, exist_ok=True)
        notes = loaded[key]
        missing = [c[1] for c in j["catalogue"] if c[1] not in notes and c[1] not in j["handmade"]]
        if missing:
            print(f"[{key}] no content yet for:", ", ".join(missing))
        for slug, n in notes.items():
            (out / "notes" / f"{slug}.html").write_text(render_note(j, n, back.get((key, slug), [])), encoding="utf-8")
        for slug in j["handmade"]:
            stamp_handmade(out / "notes" / f"{slug}.html")
        print(f"[{key}] wrote {len(notes)} notes")
        (out / "index.html").write_text(render_index(j), encoding="utf-8")
        (out / "all.html").write_text(render_all(j), encoding="utf-8")
        ready = [c for c in j["catalogue"] if c[1] in notes or c[1] in j["handmade"]]
        if j.get("draft"):
            print(f"[{key}] draft: unlisted, no PDFs")
            continue
        listing.append(dict(key=key, title=j["title"], all=f"{key}/all.html", pdf=f"{key}/pdf/{journal_pdf(j)}",
                            notes=[dict(num=c[0], slug=c[1], title=c[2], page=f"{key}/notes/{c[1]}.html",
                                        pdf=f"{key}/pdf/{pdf_name(c[0], c[1])}") for c in ready]))
    (PUBLIC / "larder").mkdir(exist_ok=True)
    (PUBLIC / "larder" / "index.html").write_text(render_casefile(), encoding="utf-8")
    sheets = [load_cheatsheet(name) for name in CHEATSHEETS]
    for cs in sheets:
        out = PUBLIC / "cheatsheets" / cs.SLUG
        out.mkdir(parents=True, exist_ok=True)
        (out / "index.html").write_text(render_cheatsheet(cs), encoding="utf-8")
        listing.append(dict(key=f"cheatsheets/{cs.SLUG}", title=f"{cs.TITLE} cheat sheet", all=f"cheatsheets/{cs.SLUG}/index.html",
                            pdf=f"cheatsheets/{cs.SLUG}/pdf/{cheatsheet_pdf(cs)}", notes=[]))
        print(f"[cheatsheets] wrote {cs.SLUG} ({len(cs.PAGES)} cards)")
    (PUBLIC / "index.html").write_text(render_landing(sheets), encoding="utf-8")
    (PUBLIC / "journals.json").write_text(json.dumps(listing, indent=1), encoding="utf-8")
    # old links from before the shelf existed (everything was the distributed journal)
    old = PUBLIC / "notes"
    old.mkdir(exist_ok=True)
    for c in JOURNALS[0]["catalogue"]:
        (old / f"{c[1]}.html").write_text(redirect(f"../distributed/notes/{c[1]}.html"), encoding="utf-8")
    (PUBLIC / "all.html").write_text(redirect("distributed/all.html"), encoding="utf-8")
    print("wrote landing page, journals.json and redirects")


if __name__ == "__main__":
    main()
