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
from doodle import ICONS, Doodle, esc, highlight  # noqa: E402
import cheatsheet  # noqa: E402
import dive  # noqa: E402

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
PROJECT_ATTRS = [
    ("Value focus", "serves the outcome?", "Keeps the project aimed at the benefit, not at the paperwork."),
    ("Predictability", "dates and costs hold?", "Forecasts get closer to what really happens."),
    ("Risk reduction", "fewer surprises?", "Trouble is found while it is still cheap."),
    ("Transparency", "true status visible?", "Anyone can see where the project really is."),
    ("Stakeholder confidence", "they trust the plan?", "Sponsors and partners believe the updates."),
    ("Team ownership", "team decides and commits?", "The people doing the work own the plan."),
    ("Adaptability", "easy to change course?", "Change is absorbed without chaos."),
    ("Quality built in", "right first time?", "Problems are prevented, not inspected out at the end."),
    ("Low overhead", "light to run?", "Time and ceremony it takes. High = light."),
]
# PMBOK Guide, Eighth Edition: the seven performance domains (binder tabs) and the five focus areas.
PMBOK_DOMAINS = [("governance", "Governance"), ("scope", "Scope"), ("schedule", "Schedule"), ("finance", "Finance"),
                 ("stakeholders", "Stakeholders"), ("resources", "Resources"), ("risk", "Risk")]
PMBOK_FOCUS = ["initiating", "planning", "executing", "monitoring", "closing"]
PMI_NOTE = ("Independent study notes, written in my own words. Not affiliated with or endorsed by the Project Management "
            "Institute. PMBOK is a registered mark of the Project Management Institute, Inc.")
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
            (19, "strangler-fig", "Strangler Fig", "communication", "Put a routing layer in front of the old system and move one route at a time to the new one."),
            (20, "backpressure", "Backpressure", "resilience", "When work arrives faster than you can finish it, push back instead of queueing without limit."),
            (21, "consistent-hashing", "Consistent Hashing", "data", "Spread keys across nodes so adding or removing a node moves only a small share of them."),
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
            (16, "debounce-throttle", "Debounce & Throttle", "rendering", "Run a handler once after the user pauses, or at most every so often, instead of on every event."),
            (17, "web-workers", "Web Workers", "rendering", "Move heavy work off the main thread so the page keeps responding to taps."),
            (18, "offline-first", "Offline-First Sync", "state", "Write to a local store first and sync with the server when the connection allows."),
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
            (16, "upserts", "Upserts", "changing", "Insert a row or update the one that's already there, in one atomic statement."),
            (17, "bitemporal-data", "Bitemporal Data", "modelling", "Record both when a fact was true and when you knew it, so corrections never erase history."),
            (18, "vector-indexes", "Vector Indexes", "reading", "Find the nearest items by meaning, not by exact value, without comparing against every row."),
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
            (16, "fuzzing", "Fuzzing", "techniques", "Feed a program huge numbers of generated, malformed inputs and watch for crashes."),
            (17, "visual-regression", "Visual Regression Tests", "techniques", "Compare screenshots with approved ones so layout and style bugs fail the build."),
            (18, "fault-injection", "Fault Injection Tests", "reliability", "Make dependencies slow, fail or drop connections in tests, and check the code copes."),
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
            (16, "passkeys", "Passkeys", "identity", "Sign in with a key pair kept on the user's device, so there is no password to steal or phish."),
            (17, "signed-webhooks", "Signed Webhooks", "input", "Check a signature and timestamp on every incoming webhook before trusting it."),
            (18, "login-throttling", "Rate-Limited Login", "identity", "Slow down and block password guessing per account, per IP and overall."),
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
            (16, "progressive-delivery", "Progressive Delivery", "shipping", "Roll a change out ring by ring, with automatic checks deciding each next step."),
            (17, "service-catalogue", "Service Catalogue", "running", "One place that says what each service is, who owns it, and how to run it."),
            (18, "chaos-engineering", "Chaos Engineering", "resilience", "Run planned experiments that break things on purpose, to learn before an incident does."),
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
    dict(
        key="project-1", vol=1, title="The Lay of the Land", short="the lay of the land",
        series=2, book="The Project Manager's Notebook", narrator="Sanne", brand="project manager's notebook", book_no=3,
        title_block=True, sheet_doodles="project",
        theme="theme-project", fonts="Patrick+Hand+SC", subject="project management",
        problem_h2="The situation", related_h3="Related notes", map_caption="Translating it to the job", map_col="On the project",
        term="Winter term · 2029", weekdays=(1, 3), start=date(2029, 1, 9),
        kicker="the project manager's notebook · book 3 · vol. 1",
        story="<b>January 2026.</b> Larder has promised its investors six cities by the end of 2027. The second city, Rotterdam, must open on <b>27 April 2026</b>: the store lease is signed. Ana is three months into the architecture and Grace into the product. There is a date, a building and a lot of goodwill, but no plan and nobody whose job is the launch. Sanne joins on 12 January as delivery manager. This volume follows her first seven weeks: working out what kind of thing she has been handed, what good project management rests on, and how much process Rotterdam needs.",
        lead="Volume 1 of <span class=\"hl\">The Project Manager's Notebook</span>, a plain-words walk through the whole <b>PMBOK Guide</b> (eighth edition). {n} notes in {c} collections: what a project is, the six principles, and the ways of working. Each note is one <b>question a project manager must answer</b>; the official PMBOK term is on the tag under the title. Every note follows <b>Sanne</b> at <b>Larder</b>, in the same months as Ana's and Grace's notebooks. Key notes go further with a <b>going deeper</b> chapter, and every note ends with a <b>try it</b> for your own project.",
        blurb="What a project is, the six principles, life cycles, focus areas, the seven domains and tailoring: the ground the rest of the PMBOK Guide stands on.",
        attrs=PROJECT_ATTRS, attrs_title="The nine project ratings", attrs_side="what a good project practice is judged on", ratings_h2="Project ratings",
        first_law="A project is finished when the benefit shows up, not when the plan is ticked off. Use as much process as the risk needs, and no more.",
        disclaimer=PMI_NOTE, pmbok=True,
        deep_dives={"value-delivery-system", "life-cycles", "focus-areas", "tailoring"},
        handmade=set(),
        collections=[
            ("what", "What a project is", "know what you have been handed before you plan it"),
            ("principles", "The six principles", "what good project management rests on, whatever the method"),
            ("ways", "Ways of working", "how the work is shaped, watched and sized"),
        ],
        catalogue=[
            (1, "project-product-operations", "Is This a Project?", "what", "Tell a project from a product and from operations, so each gets the right kind of management."),
            (2, "value-delivery-system", "What Is It All For?", "what", "Follow the chain from strategy to portfolio, programme, project and operations, and from output to benefit."),
            (3, "project-manager-role", "What Is My Job Here?", "what", "What a project manager does, what the sponsor does, and where the role ends."),
            (4, "project-environment", "What Was Here Before Me?", "what", "Read the surroundings a project lands in: rules, habits, people and what already exists."),
            (5, "holistic-view", "See the Whole", "principles", "Treat the project as one connected system, so a fix in one place doesn't break another."),
            (6, "focus-on-value", "Focus on Value", "principles", "Steer by the benefit the project exists for, not by the list of tasks."),
            (7, "embed-quality", "Build Quality In", "principles", "Put quality into how the work is done, instead of inspecting for it at the end."),
            (8, "accountable-leader", "Own the Outcome", "principles", "Lead by taking responsibility for the result, the truth of the status and the people."),
            (9, "sustainability", "Think Past the Finish", "principles", "Weigh the long-term effect on people, planet and money in every project decision."),
            (10, "empowered-culture", "Let the Team Decide", "principles", "Give the people doing the work the room, the facts and the trust to decide."),
            (11, "life-cycles", "Plan It All, or Learn As We Go?", "ways", "Choose a predictive, adaptive or hybrid approach for each part of the work."),
            (12, "focus-areas", "What Do I Do When?", "ways", "Initiating, planning, executing, monitoring and controlling, closing: five kinds of attention, not five phases."),
            (13, "performance-domains", "What Must I Keep an Eye On?", "ways", "The seven performance domains: seven things a project manager watches all the way through."),
            (14, "tailoring", "How Much Process Do We Need?", "ways", "Fit the approach, the documents and the meetings to this project, on purpose."),
            (15, "pmo", "Who Helps the Project Managers?", "ways", "What a project management office is for, and the lightest version that still helps."),
        ],
    ),
    dict(
        key="project-2", vol=2, title="Starting, Steering, Closing", short="starting, steering, closing",
        series=2, book="The Project Manager's Notebook", narrator="Sanne", brand="project manager's notebook", book_no=3,
        title_block=True, sheet_doodles="project",
        theme="theme-project", fonts="Patrick+Hand+SC", subject="project management",
        problem_h2="The situation", related_h3="Related notes", map_caption="Translating it to the job", map_col="On the project",
        term="Spring term · 2029", weekdays=(1, 3), start=date(2029, 3, 6),
        kicker="the project manager's notebook · book 3 · vol. 2",
        story="<b>Late February 2026.</b> Sanne has been at Larder for six weeks. Rotterdam opens on <b>27 April</b>; the team has made its own plan, there are seven workstreams, five shared milestones, a budget of €380k and a reserve of €6k. What the launch still lacks is governance: nobody has written down why it exists, who decides what, when it is allowed to move to the next step, how a change gets agreed, or what “finished” means. This volume follows the launch from its charter to its closing report on 22 May, through a scope misread, a late builder, a forgotten internet line and an opening day.",
        lead="Volume 2 of <span class=\"hl\">The Project Manager's Notebook</span>: the <b>Governance</b> domain of the PMBOK Guide (eighth edition), all nine of its processes. {n} notes in {c} collections: starting a project properly, making one plan, running and steering the work, and closing it. Each note is one <b>question a project manager must answer</b>, and its template card is a real page of <b>the Rotterdam project file</b>, which grows through the book. Four notes go further with a <b>going deeper</b> chapter.",
        blurb="The Governance domain: the charter, who decides, phase gates, one plan, sourcing, baselines, running the work, honest status, change control, lessons, handover and closing.",
        attrs=PROJECT_ATTRS, attrs_title="The nine project ratings", attrs_side="what a good project practice is judged on", ratings_h2="Project ratings",
        first_law="Governance is a few clear answers, agreed early: why, who decides, when we move on, how we change, and when we are done.",
        disclaimer=PMI_NOTE, pmbok=True,
        deep_dives={"project-charter", "project-management-plan", "status-reports", "change-control"},
        handmade=set(),
        collections=[
            ("starting", "Starting", "agree why, who decides, and when the next step may begin"),
            ("plan", "One plan", "one plan everyone works from, and what was promised"),
            ("running", "Running and steering", "do the work, see where it stands, change course on purpose"),
            ("closing", "Closing", "finish properly: learn, hand over, close"),
        ],
        catalogue=[
            (1, "project-charter", "Should This Project Exist?", "starting", "The project charter: one page that says why, what for, who is behind it and within what limits."),
            (2, "governance-structure", "Who Decides What?", "starting", "A sponsor, a steering group and decision levels, written down before the first hard decision."),
            (3, "phase-gates", "May We Take the Next Step?", "starting", "Phase gates and go / no-go: agreed criteria, checked at fixed points, with three possible answers."),
            (4, "project-management-plan", "What's the Plan?", "plan", "One plan that makes scope, dates, money, people and risks agree with each other."),
            (5, "sourcing-strategy", "Make It, Buy It, or Hire It?", "plan", "Decide what to do yourself and what to buy, and pick the contract that puts each risk in the right hands."),
            (6, "baselines", "What Exactly Did We Promise?", "plan", "A baseline is the approved version of the plan that progress and changes are measured against."),
            (7, "directing-the-work", "Is the Work Actually Happening?", "running", "A weekly rhythm that keeps seven workstreams moving and clears what blocks them."),
            (8, "issue-log", "What's in the Way Right Now?", "running", "An issue is a problem that has already happened: log it, give it an owner and a date, close it."),
            (9, "quality-assurance", "Is Our Way of Working Working?", "running", "Quality assurance checks the process; quality control checks the result. A project needs both."),
            (10, "status-reports", "Where Are We, Really?", "running", "Measure against the baseline, forecast the end, and report a colour that follows written rules."),
            (11, "change-control", "Can We Change That?", "running", "Every change to what was promised is written down, sized, decided by the right person and then built into the plan."),
            (12, "escalation", "When Do I Take It Upstairs?", "running", "Escalate early, with options and a recommendation, when a decision is above your limit."),
            (13, "lessons-learned", "What Did We Learn?", "closing", "Capture lessons while they are fresh, sort them, and put them where the next project will trip over them."),
            (14, "handover", "Who Looks After It Now?", "closing", "Hand the result to the people who will run it, with everything they need and nothing left hanging."),
            (15, "closing-a-project", "Are We Done?", "closing", "Close on purpose: results accepted, contracts and money settled, benefits handed to their owners, the team released."),
        ],
    ),
    dict(
        key="project-3", vol=3, title="What, and By When", short="what, and by when",
        series=2, book="The Project Manager's Notebook", narrator="Sanne", brand="project manager's notebook", book_no=3,
        title_block=True, sheet_doodles="project",
        theme="theme-project", fonts="Patrick+Hand+SC", subject="project management",
        problem_h2="The situation", related_h3="Related notes", map_caption="Translating it to the job", map_col="On the project",
        term="Summer term · 2029", weekdays=(1, 3), start=date(2029, 5, 8),
        kicker="the project manager's notebook · book 3 · vol. 3",
        story="<b>February → April 2026, again.</b> Vol. 2 followed the Rotterdam launch from its charter to its closing report: who decided, how it was steered, how it ended. This volume goes back over the same weeks for the two questions every plan rests on: <b>what exactly</b> will be delivered, and <b>by when</b>. Here are the 71 must-haves broken down, the estimates behind the plan of 20 February, the builder's network of twelve activities and the one path through it that set the handover date, and what happened to that path when an electrical inspector re-booked on 23 March.",
        lead="Volume 3 of <span class=\"hl\">The Project Manager's Notebook</span>: the <b>Scope</b> and <b>Schedule</b> domains of the PMBOK Guide (eighth edition), all nine of their processes. {n} notes in {c} collections: pinning down what will be delivered, estimating how big it is, turning work into dates, and holding scope and dates where they were promised. Every number comes from one worked example, the Rotterdam launch, and its template card is a page of <b>the Rotterdam project file</b>. Four notes go further with a <b>going deeper</b> chapter: the work breakdown structure, three-point estimates, the critical path and schedule tracking.",
        blurb="The Scope and Schedule domains: requirements, the scope statement, the work breakdown structure, estimates as ranges, the network, critical path, float, Gantt charts, crashing and fast-tracking, tracking dates, acceptance and scope creep.",
        attrs=PROJECT_ATTRS, attrs_title="The nine project ratings", attrs_side="what a good project practice is judged on", ratings_h2="Project ratings",
        first_law="A date is only as good as the list of work under it and the longest chain through that work. Find both before you promise.",
        disclaimer=PMI_NOTE, pmbok=True,
        deep_dives={"work-breakdown-structure", "three-point-estimates", "critical-path", "schedule-tracking"},
        handmade=set(),
        collections=[
            ("scope", "What, exactly?", "pin down what will be delivered, and what won't"),
            ("estimating", "How big is it?", "estimate honestly, as a range, with the people who do the work"),
            ("schedule", "By when?", "turn work and estimates into dates you can defend"),
            ("control", "Holding the line", "keep dates and scope where they were promised, or move them on purpose"),
        ],
        catalogue=[
            (1, "scope-schedule-approach", "How Will We Pin It Down?", "scope", "Decide, before you start, how scope and dates will be defined, detailed, measured and changed."),
            (2, "requirements", "What Do They Actually Need?", "scope", "Draw needs out of the people who will live with the result, and trace each one to something you'll deliver and check."),
            (3, "scope-statement", "What's In, and What's Out?", "scope", "One page that names the deliverables, how each will be accepted, and what is deliberately left out."),
            (4, "work-breakdown-structure", "How Do We Break It Down?", "scope", "Break the whole result into smaller deliverables until each piece can be owned, estimated and checked."),
            (5, "estimating-methods", "How Long, Roughly?", "estimating", "Three ways to estimate: from a similar past job, from a rate, or by adding up the parts."),
            (6, "three-point-estimates", "How Sure Are We?", "estimating", "Ask for the best case, the likely case and the worst case, and turn them into a range with odds."),
            (7, "estimating-with-the-team", "Who Should Guess?", "estimating", "Let the people who do the work estimate, independently first, so nobody's number anchors the rest."),
            (8, "network-diagram", "What Waits for What?", "schedule", "Draw which activities wait for which, including waits on things outside the project."),
            (9, "critical-path", "What Decides the Finish Date?", "schedule", "The longest chain of dependent activities sets the end date. Find it, and watch it."),
            (10, "float-and-buffers", "How Much Can This Slip?", "schedule", "Float is how late an activity can be without moving the end; a buffer is slack you put in on purpose."),
            (11, "gantt-and-milestones", "How Do We Show the Dates?", "schedule", "A milestone chart for the people who decide, a Gantt chart for the people who do the work."),
            (12, "crashing-and-fast-tracking", "Can We Go Faster?", "schedule", "Two ways to shorten a schedule: pay to speed up critical work, or overlap work that was meant to follow."),
            (13, "schedule-tracking", "Are We Still on Time?", "control", "Track predictive work by its milestones and float, adaptive work by a burn-up, and forecast both every week."),
            (14, "validate-scope", "Is This What We Asked For?", "control", "The people who asked for each deliverable formally accept it against criteria agreed in advance."),
            (15, "scope-creep", "Where Did That Come From?", "control", "Small, unapproved additions eat the schedule quietly. Make every addition a decision."),
        ],
    ),
    dict(
        key="project-4", vol=4, title="Money and People", short="money and people",
        series=2, book="The Project Manager's Notebook", narrator="Sanne", brand="project manager's notebook", book_no=3,
        title_block=True, sheet_doodles="project",
        theme="theme-project", fonts="Patrick+Hand+SC", subject="project management",
        problem_h2="The situation", related_h3="Related notes", map_caption="Translating it to the job", map_col="On the project",
        term="Autumn term · 2029", weekdays=(1, 3), start=date(2029, 9, 4),
        kicker="the project manager's notebook · book 3 · vol. 4",
        story="<b>January → May 2026, a third time.</b> Vol. 2 showed how the Rotterdam launch was governed and Vol. 3 what it delivered and when. This volume follows the same launch through the two things every plan spends: <b>money</b> and <b>people</b>. Here is how the €380k was built and set aside, when the cash actually left the bank, whether the money was buying progress (earned value said, on 20 March, that the reserve would be used to the last euro, and it was), and how forty pickers and couriers were found, trained and led by a project manager who was nobody's boss.",
        lead="Volume 4 of <span class=\"hl\">The Project Manager's Notebook</span>: the <b>Finance</b> and <b>Resources</b> domains of the PMBOK Guide (eighth edition), all nine of their processes. {n} notes in {c} collections: planning the money, watching it, getting the people and things, and leading and balancing them. The numbers are the Rotterdam launch's, and every template card is a page of <b>the Rotterdam project file</b>. Four notes go further with a <b>going deeper</b> chapter: the budget and its reserves, earned value, resource levelling, and leading without authority.",
        blurb="The Finance and Resources domains: cost estimates, the budget and its reserves, cash flow, committed vs spent, earned value, forecasting, payback, RACI, estimating and getting people, levelling, leading without authority, conflict and keeping resources available.",
        attrs=PROJECT_ATTRS, attrs_title="The nine project ratings", attrs_side="what a good project practice is judged on", ratings_h2="Project ratings",
        first_law="A plan spends two things: money and people's time. Know where both are going every week, and ask before you borrow either.",
        disclaimer=PMI_NOTE, pmbok=True,
        deep_dives={"budget-and-reserves", "earned-value", "resource-levelling", "leading-without-authority"},
        handmade=set(),
        collections=[
            ("money-plan", "Planning the money", "what it costs, what is set aside, and when the cash goes out"),
            ("money-watch", "Watching the money", "is the money buying progress, where will it end, and was it worth it?"),
            ("people-plan", "Getting the people and things", "who does what, how many, and where they come from"),
            ("people-lead", "Leading and balancing", "keep people from overload, pulling together, and available"),
        ],
        catalogue=[
            (1, "financial-management", "Whose Money Is It?", "money-plan", "Agree, before spending, what the budget covers, who may spend what, and how money is counted and reported."),
            (2, "cost-estimates", "What Will It Cost?", "money-plan", "Estimate each piece of work in money, from quotes, rates and past jobs, and say how sure each number is."),
            (3, "budget-and-reserves", "How Much Do We Set Aside?", "money-plan", "Add the estimates into a budget, put a visible reserve on top, and spread it over time."),
            (4, "cash-flow", "When Does the Money Leave?", "money-plan", "Spending is agreed when it's committed but leaves the bank later. Plan the cash, not just the total."),
            (5, "committed-and-spent", "How Much Have We Spent?", "money-watch", "Three different numbers: committed, actually spent, and forecast. Report all three, line by line."),
            (6, "earned-value", "Is the Money Buying Progress?", "money-watch", "Compare the value of the work done with what was planned and what it cost, in one set of numbers."),
            (7, "cost-forecasting", "Where Will the Money End Up?", "money-watch", "Forecast the final cost two ways, by formula and line by line, and compare them with the budget."),
            (8, "payback", "Was It Worth It?", "money-watch", "Put the money spent next to the money the result brings back, and say when it pays for itself."),
            (9, "raci", "Who Does What?", "people-plan", "A responsibility table: who does the work, who answers for it, who is asked and who is told."),
            (10, "estimating-resources", "How Many People, and What Else?", "people-plan", "Work out the people and equipment from the demand they must serve, not from habit."),
            (11, "acquiring-resources", "Where Do They Come From?", "people-plan", "Hire, borrow, lease or buy, and agree every loan with whoever owns the person or thing."),
            (12, "resource-levelling", "Who Is Overloaded?", "people-lead", "Spot people booked over 100 % and move work in time or to others before they break."),
            (13, "leading-without-authority", "How Do I Lead People Who Don't Report to Me?", "people-lead", "Lead with a shared goal, facts, favours and credit when you can't give orders."),
            (14, "team-conflict", "Why Is the Team Arguing?", "people-lead", "Teams go through stages and conflict is part of them. Work on the interests behind the positions."),
            (15, "monitoring-resources", "Are the People and Things Still There?", "people-lead", "Check every day that the people, equipment and suppliers the plan needs are actually available."),
        ],
    ),
    dict(
        key="project-5", vol=5, title="People Outside, and Surprises", short="people outside, and surprises",
        series=2, book="The Project Manager's Notebook", narrator="Sanne", brand="project manager's notebook", book_no=3,
        title_block=True, sheet_doodles="project",
        theme="theme-project", fonts="Patrick+Hand+SC", subject="project management",
        problem_h2="The situation", related_h3="Related notes", map_caption="Translating it to the job", map_col="On the project",
        term="Winter term · 2030", weekdays=(1, 3), start=date(2030, 1, 8),
        kicker="the project manager's notebook · book 3 · vol. 5",
        story="<b>October 2026 → October 2027: Antwerp.</b> Rotterdam opened on time and on budget, and Utrecht and The Hague open in 2027 from its playbook. Antwerp is different: <b>the first city abroad</b>, with Belgian rules, Flemish and French, a city permit office, a food-safety agency and a street of forty-six houses behind the loading yard. Sanne planned it for Monday 13 September 2027. It opened on <b>Monday 18 October</b>, five weeks late, and the reason had been on her risk register since November, rated low, with no owner. This volume is how that happened, and everything else that went right around it.",
        lead="Volume 5 of <span class=\"hl\">The Project Manager's Notebook</span>: the <b>Stakeholders</b> and <b>Risk</b> domains of the PMBOK Guide (eighth edition), all thirteen of their processes. {n} notes in {c} collections: finding everyone the project touches, working abroad, finding and sizing what could happen, and doing something about it. The worked example is the Antwerp launch, and every template card is a page of its <b>project file</b>. Four notes go further with a <b>going deeper</b> chapter: the engagement matrix, the risk register, simulation, and risk responses.",
        blurb="The Stakeholders and Risk domains: the stakeholder register, power and interest, the communications plan, managing expectations, meetings, stakeholders abroad, the risk register, probability and impact, expected monetary value, Monte Carlo simulation, risk responses, and risks becoming issues.",
        attrs=PROJECT_ATTRS, attrs_title="The nine project ratings", attrs_side="what a good project practice is judged on", ratings_h2="Project ratings",
        first_law="The people outside the project and the things that might happen to it are the same list seen twice. Whoever can stop you is a stakeholder and a risk: give them both an owner.",
        disclaimer=PMI_NOTE, pmbok=True,
        deep_dives={"power-and-interest", "risk-register", "monte-carlo", "risk-responses"},
        handmade=set(),
        collections=[
            ("involved", "Who's involved?", "find everyone the project touches, and decide how much of you each one needs"),
            ("abroad", "Abroad", "new rules, a new language, and knowing whether people are still with you"),
            ("could-happen", "What could happen?", "plan for risk, list it, and size it in days and euros"),
            ("doing", "Doing something about it", "choose responses, carry them out, and keep the list true"),
        ],
        catalogue=[
            (1, "stakeholder-register", "Who Cares About This?", "involved", "Find everyone the project affects or who can affect it, from more than one source, and write down what each one needs."),
            (2, "power-and-interest", "Who Matters Most, and How Much?", "involved", "Place stakeholders by power and interest, mark where they are and where you need them, and act on the gaps."),
            (3, "communications-plan", "Who Hears What, and When?", "involved", "One table: what each audience needs, how, how often, in which language and from whom."),
            (4, "managing-expectations", "How Do We Keep Them With Us?", "involved", "Meet people early, promise only what you control, and turn every concern into something the plan can see."),
            (5, "meetings-that-work", "Are We Being Understood?", "abroad", "A meeting is only finished when everyone leaves with the same decisions, in writing, in their language."),
            (6, "stakeholders-abroad", "Different Country, Different Rules", "abroad", "A new country brings new regulators, new laws and new habits. Map them with someone local, early."),
            (7, "monitoring-engagement", "Are They Still With Us?", "abroad", "Re-score every key stakeholder each month, from what they say and do, not from what you hope."),
            (8, "risk-approach", "How Will We Handle Risk?", "could-happen", "Agree, before listing risks, how much risk the sponsor will take, the scales, the owners and the rhythm."),
            (9, "risk-register", "What Could Happen?", "could-happen", "Write each risk as cause, event and effect, with an owner and a response, and include the good surprises."),
            (10, "probability-and-impact", "How Likely, and How Bad?", "could-happen", "Score each risk on scales everyone agreed, and re-score it whenever someone who knows more speaks up."),
            (11, "expected-monetary-value", "What Is It Worth?", "could-happen", "Put a likely cost on each risk, add them up, and size the contingency and the management reserve from it."),
            (12, "monte-carlo", "What If We Ran It a Thousand Times?", "could-happen", "Run the plan a thousand times with its uncertainties and read the date off as odds, not a single day."),
            (13, "risk-responses", "What Do We Do About It?", "doing", "Avoid, transfer, mitigate or accept a threat; exploit, enhance, share or accept an opportunity; escalate what isn't yours."),
            (14, "implementing-responses", "Did We Do What We Said?", "doing", "A response is only real when a named person does it by a date, and someone watches its trigger."),
            (15, "risk-monitoring", "Is the List Still True?", "doing", "Review risks on a rhythm, close the dead ones, and when one happens, move it to the issue log."),
        ],
    ),
    dict(
        key="project-6", vol=6, title="Making It Yours", short="making it yours",
        series=2, book="The Project Manager's Notebook", narrator="Sanne", brand="project manager's notebook", book_no=3,
        title_block=True, sheet_doodles="project",
        theme="theme-project", fonts="Patrick+Hand+SC", subject="project management",
        problem_h2="The situation", related_h3="Related notes", map_caption="Translating it to the job", map_col="On the project",
        term="Spring term · 2030", weekdays=(1, 3), start=date(2030, 4, 2),
        kicker="the project manager's notebook · book 3 · vol. 6",
        story="<b>September 2027 → September 2028.</b> Antwerp opened five weeks late and taught Larder that regulators are stakeholders. Eindhoven opened eight weeks after its first page, run from the playbook with a third of Rotterdam's paperwork. In 2028 Sanne runs a programme instead of a launch: Ghent in June and Haarlem in September, eight cities by the board of 28 September. She hires a second project manager, Nadia, coaches her, and hands Haarlem to her. This last volume is about fitting the method to the work, choosing tools and documents that earn their keep, and growing: yourself, and the next person.",
        lead="Volume 6 of <span class=\"hl\">The Project Manager's Notebook</span>, the last: the parts of the PMBOK Guide (eighth edition) around the forty processes. {n} notes in {c} collections: tailoring a whole project, the playbook, programmes and benefits; models, methods and artefacts, AI and sustainability; the PMO, servant leadership and ethics; and growing, hiring and handing over. Template cards are the <b>programme</b> pages of the project file. Four notes go further with a <b>going deeper</b> chapter: tailoring a whole project, the playbook, AI in project work, and growing as a project manager.",
        blurb="Tailoring a whole project, the city launch playbook, programmes and portfolios, benefits realisation, models and methods, artefacts, AI in project work, sustainability, the PMO, servant leadership, ethics, growing, hiring and handing over.",
        attrs=PROJECT_ATTRS, attrs_title="The nine project ratings", attrs_side="what a good project practice is judged on", ratings_h2="Project ratings",
        first_law="The plan is the team's, the truth is yours, and the thing that sets your date is usually outside the room.",
        disclaimer=PMI_NOTE, pmbok=True,
        deep_dives={"tailoring-a-whole-project", "city-launch-playbook", "ai-in-project-work", "growing-as-a-project-manager"},
        handmade=set(),
        collections=[
            ("fitting", "Fitting it to the work", "size the method, write the recipe, group the projects, check the benefits"),
            ("models", "Models, methods, artefacts", "choose tools by the question, keep the documents that are used, use AI and think long-term"),
            ("leading", "Leading others", "an office that helps, a colleague you coach, and the truth under pressure"),
            ("growing", "Growing", "get better on purpose, hire well, hand over, and look back"),
        ],
        catalogue=[
            (1, "tailoring-a-whole-project", "How Light Can We Go?", "fitting", "Set the whole method for one project on one page: keep, shorten, drop, and check the fit."),
            (2, "city-launch-playbook", "Can a Launch Be a Recipe?", "fitting", "Turn repeated projects into a versioned playbook: fixed, local, a kit, and changes after every launch."),
            (3, "programmes-and-portfolios", "One Project, or Many?", "fitting", "Run projects that share a benefit as a programme; choose what to fund as a portfolio."),
            (4, "benefits-realisation", "Did We Get What We Paid For?", "fitting", "Check each benefit, by its owner, on dates booked before the project closes."),
            (5, "models-and-methods", "Which Tools, When?", "models", "Choose models and methods by the question the project must answer, not by name."),
            (6, "artefact-review", "Which Documents Earn Their Keep?", "models", "Keep the documents that were used after they were written; make the rest examples."),
            (7, "ai-in-project-work", "Can AI Help?", "models", "Use AI for drafts, summaries and checks; check every fact, own every line, keep decisions human."),
            (8, "sustainability-in-practice", "What Does It Leave Behind?", "models", "Decide what a project leaves running while it's still on paper, priced over its life."),
            (9, "pmo-grown-up", "Who Helps the Project Managers Now?", "leading", "A supportive office with few mandatory rules, measured by what it makes easier."),
            (10, "servant-leadership", "Who Serves Whom?", "leading", "Coach what's new, delegate what's known, unblock, give credit, and don't grab the pan."),
            (11, "ethics", "What Would You Do?", "leading", "Never shade a report; offer the person under pressure a true version that helps."),
            (12, "growing-as-a-project-manager", "How Do I Get Better at This?", "growing", "A log, feedback, a weak thing, a stretch, someone to coach, and a standard."),
            (13, "hiring-a-project-manager", "Who Do We Hire?", "growing", "A role card, a real work sample, a scoring sheet written first, and a mixed panel."),
            (14, "handing-over-a-programme", "Can Someone Else Run This?", "growing", "Move decision rights, tell everyone who calls, step out on a date, and stop answering."),
            (15, "what-was-it-all-for", "What Was It All For?", "growing", "The six principles revisited: the day each one changed a decision."),
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
# Planned volumes of Series 2, book 3 (see docs/HANDOFF-project-manager.md).
PLANNED_PROJECT = [
]
FUTURE_LOG = [
    ("Dec 2026", [("•", "Vol. 7 · AI App Patterns"), ("•", "Search across every journal")]),
    ("Jan 2027", [("↓", "Deep dives, season 2: Replication &amp; Leader Election, Sharding &amp; Partitioning, Indexes &amp; Query Plans"), ("•", "One-page printable cheat sheet per collection")]),
    ("Mar 2027", [("•", "Cheat sheets for Book 3: PMBOK 8 on one page, earned value, critical path")]),
    ("Apr 2027", [("★", "Book 4 · <b>The Client Manager's Notebook</b> (Mo and Korenwolf): expectations, scope change, reporting, workshops, difficult conversations")]),
    ("Mid 2027", [("↓", "More deep dives: Sign-in &amp; Tokens, Observability &amp; SLOs, Rendering on the Web, Multitenancy"), ("•", "A Series 2 index: every Larder note from both books in one timeline")]),
    ("Someday", [("•", "Quiz mode that remembers your score"), ("•", "A “compare two patterns” page")]),
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
# Desk doodles around a project manager's sheet: a wall calendar, a binder clip, and a small Gantt chart.
PROJECT_DOODLES = (
    '<div class="sheet-doodles" aria-hidden="true">'
    '<svg class="sd sd-coffee" viewBox="0 0 120 120"><g class="rough">'
    '<rect class="d d-thin f-paper" x="14" y="22" width="92" height="84" rx="3"/><path class="d d-thin f-red" d="M14 25 a3 3 0 0 1 3 -3 h86 a3 3 0 0 1 3 3 v19 h-92 z"/>'
    '<path class="d d-thin" d="M34 14 v16 M86 14 v16"/><path class="d d-thin d-soft" d="M14 64 h92 M14 84 h92 M45 44 v62 M76 44 v62"/>'
    '<circle class="d d-red" cx="60" cy="74" r="9" fill="none"/></g></svg>'
    '<svg class="sd sd-compass" viewBox="0 0 70 110"><g class="rough">'
    '<path class="d f-ink" d="M12 40 h46 v52 h-46 z"/><path class="d" d="M22 40 q-6 -30 13 -32 q19 2 13 32" fill="none"/>'
    '<path class="d d-thin" d="M20 92 q-4 10 15 12 q19 -2 15 -12" fill="none"/></g></svg>'
    '<svg class="sd sd-pencil" viewBox="0 0 240 80"><g class="rough">'
    '<rect class="d d-thin f-paper" x="10" y="6" width="220" height="68" rx="3"/>'
    '<path class="d d-thin d-soft" d="M66 6 v68 M107 6 v68 M148 6 v68 M189 6 v68"/>'
    '<rect class="d d-thin f-blue" x="22" y="16" width="70" height="10"/><rect class="d d-thin f-y" x="66" y="32" width="84" height="10"/>'
    '<rect class="d d-thin f-green" x="120" y="48" width="74" height="10"/><path class="d f-red" d="M206 54 l8 8 l-8 8 l-8 -8 z"/></g></svg>'
    '</div>'
)
DESK_DOODLES = {True: SHEET_DOODLES, "architect": SHEET_DOODLES, "product": PRODUCT_DOODLES, "project": PROJECT_DOODLES}
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
    what = (f"{j['book']} · vol. {j['vol']}" if j.get("book") else
            f"Vol. {j['vol']} · a student's bullet journal on {j['short']}") if j and "vol" in j else "a shelf of student bullet journals on software design"
    note = f'\n<p class="foot-note">{j["disclaimer"]}</p>' if j and j.get("disclaimer") else ""
    return f'<footer class="foot"><span>Jef’s Notes · {what}</span><span>by {AUTHOR}</span></footer>{note}'


def asset(name):
    """assets/<name>?v=<content hash>: a new version tag whenever the file changes, so browsers and the Cloudflare
    mirror never keep serving an old stylesheet or script after a deploy."""
    digest = hashlib.sha256((PUBLIC / "assets" / name).read_bytes()).hexdigest()[:10]
    return f"assets/{name}?v={digest}"


def stamp_handmade(path, j=None):
    """Hand-made notes link the assets directly; give them the same version tags. With the journal, also bring
    them up to date like the generated notes: linked related notes, seen-at-Larder and cheat-sheet asides, and
    the additions from content/<key>/revisions.py (extra quiz questions, try it, revised stamp). Every injected
    block sits between <!-- gen:NAME --> markers, so a rebuild replaces it instead of adding it twice."""
    html = path.read_text(encoding="utf-8")
    new = re.sub(r'(href|src)="((?:\.\./)*)assets/(notebook\.css|bujo\.css|notebook\.js)(?:\?v=[0-9a-f]+)?"',
                 lambda m: f'{m.group(1)}="{m.group(2)}{asset(m.group(3))}"', html)
    if j is not None:
        slug = path.stem
        rev = REVISIONS.get(j["key"], {}).get(slug, {})
        new = re.sub(r"\n?<!-- gen:(\w+) -->.*?<!-- /gen:\1 -->", "", new, flags=re.S)

        def block(name, text):
            return f"\n<!-- gen:{name} -->{text}<!-- /gen:{name} -->" if text else ""
        new = re.sub(r'(<ul class="related">)(.*?)(</ul>)', lambda m: m.group(1) + related_items(
            j, slug, [re.sub(r"^\s*<li>|</li>\s*$", "", x) for x in re.findall(r"<li>.*?</li>", m.group(2), re.S)]) + m.group(3),
            new, count=1, flags=re.S)
        new = re.sub(r'(<p class="aside deeper">.*?</p>|</ul>(?=\s*<h2 id="quiz"))',
                     lambda m: m.group(1) + block("links", extra_links(j, slug)), new, count=1, flags=re.S)
        if rev.get("quiz_add"):
            qs = "".join(f"\n    <details><summary>{sit_q(q)}</summary><p>{a}</p></details>" for q, a in rev["quiz_add"])
            new = re.sub(r'(<div class="quiz">.*?)(\n  </div>)', lambda m: m.group(1) + block("quiz", qs) + m.group(2),
                         new, count=1, flags=re.S)
        if rev.get("try_it"):
            t = f'\n  <div class="tryit">\n    <span class="tag">try it</span>\n    <p>{rev["try_it"]}</p>\n  </div>'
            new = new.replace('\n  <div class="remember">', block("tryit", t) + '\n  <div class="remember">', 1)
        if rev.get("revised"):
            new = re.sub(r'(<div class="page-meta">.*?</div>)', lambda m: m.group(1) + block("revised", "\n" + revised_stamp(rev)),
                         new, count=1, flags=re.S)
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


def pmbok_tag(j, n):
    """The PMBOK tag under a project note's title: domain tab(s), the five focus areas (the ones this note touches
    filled in), the processes and principles it covers, and what older editions called it (note field `pmbok`)."""
    t = n.get("pmbok")
    if not t:
        return ""
    names = dict(PMBOK_DOMAINS)
    doms = "".join(f'<span class="dom dom-{d}">{names.get(d, d.title())}</span>' for d in t.get("domains", []))
    doms = doms or '<span class="dom dom-foundations">Foundations</span>'
    on = t.get("focus", [])
    focus = "".join(f'<li{" class=on" if f in on else ""}>{"monitoring &amp; controlling" if f == "monitoring" else f}</li>' for f in PMBOK_FOCUS)
    rows = [("covers", t["covers"])] if t.get("covers") else []
    if t.get("processes"):
        rows.append(("process" if len(t["processes"]) == 1 else "processes", " · ".join(t["processes"])))
    if t.get("principles"):
        rows.append(("principle", " · ".join(t["principles"])))
    if t.get("older"):
        rows.append(("in older editions", t["older"]))
    dl = "".join(f"<div><dt>{k}</dt><dd>{v}</dd></div>" for k, v in rows)
    return (f'  <aside class="pmbok" aria-label="Where this note sits in the PMBOK Guide">\n'
            f'    <p class="pmbok-top"><a class="pmbok-ed" href="../../pmbok/index.html">PMBOK 8 map</a>{doms}</p>\n'
            f'    <ol class="focus" aria-label="Focus areas this note touches">{focus}</ol>\n'
            f'    <dl>{dl}</dl>\n  </aside>')


def dial_block(n):
    """Light / standard / heavy: how much of this practice a small, a typical and a heavy project needs."""
    cols = "".join(f'    <div class="dial-{k}"><h3>{name}</h3><p class="dial-when">{when}</p>{li(items)}</div>\n'
                   for k, (name, when, items) in zip(("light", "standard", "heavy"), n["dial"]))
    return f'  <div class="dial">\n{cols}  </div>'


def deep_dive_block(n):
    """A deep dive: a longer chapter inside a key note. `deep_dive=dict(side=, intro=, parts=[(heading, html, [figs])])`."""
    d = n.get("deep_dive")
    if not d:
        return ""
    parts = "\n".join(f'  <h3 class="deep-h"><span>{i}</span>{t}</h3>\n{body}\n' + "\n".join(f.html() for f in figs)
                      for i, (t, body, figs) in enumerate(d["parts"], 1))
    return (f'  <section class="deep" id="deep" aria-label="Going deeper">\n'
            f'  <h2><span class="num">＋</span>Going deeper <span class="side">{d.get("side", "for when you need more than the note")}</span></h2>\n'
            f'  <p class="deep-intro">{d["intro"]}</p>\n{parts}\n  </section>')


# ------------------------------------------------------------ cross-links between notes
# “Related notes” are written as text (“<b>Load profiles</b> (this volume)”); the build turns each one it can
# match to a note into a link. Series 2 notes that name a pattern also show up on that pattern's note as
# “seen at Larder”. Notes listed in CARD_LINKS point at the cheat sheet that covers them.
TITLES = {}          # normalised title -> [(journal, slug)]
SEEN_AT_LARDER = {}  # (series-1 key, slug) -> [(journal, slug, title)]
UNRESOLVED = []      # (journal key, slug, text): related entries with no matching note (printed by the build)
CHEAT_TITLES = {}    # cheat sheet slug -> title
CARD_LINKS = {
    ("data", "indexing"): ["sql"], ("data", "keyset-pagination"): ["sql"], ("data", "n-plus-one"): ["sql"],
    ("data", "optimistic-locking"): ["sql"], ("data", "materialized-views"): ["sql"],
    ("cloud", "health-checks"): ["docker-kubernetes"], ("cloud", "autoscaling"): ["docker-kubernetes"],
    ("cloud", "build-once"): ["docker-kubernetes", "git-flow"], ("cloud", "preview-environments"): ["git-flow"],
    ("testing", "testcontainers"): ["docker-kubernetes"],
    ("distributed", "service-discovery"): ["shell-network", "docker-kubernetes"],
    ("architect-1", "nfr-checklist"): ["nfr-checklists"], ("architect-1", "quality-attribute-scenarios"): ["nfr-checklists"],
    ("architect-5", "availability-maths"): ["nfr-checklists"], ("architect-5", "performance-budgets"): ["nfr-checklists"],
}


# Related entries that name a note by another name (normalised with norm_title on load).
RELATED_ALIASES = {
    "consumer-driven contracts": ("testing", "contract-testing"), "idempotency keys": ("distributed", "idempotent-consumer"),
    "oauth 2.0 & openid connect": ("security", "oauth-pkce"), "retries with backoff": ("distributed", "retry-backoff"),
    "api gateway / bff": ("distributed", "api-gateway"), "tech-debt talks": ("product-3", "tech-debt-talks"),
    "user stories that aren't tasks": ("product-3", "user-stories"), "strategy on a page": ("product-2", "strategy-on-a-page"),
    "quality assurance vs control": ("project-2", "quality-assurance"), "status reports that tell the truth": ("project-2", "status-reports"),
    "phase gates and go / no-go": ("project-2", "phase-gates"), "lessons learned that get used": ("project-2", "lessons-learned"),
}


def norm_title(t):
    t = re.sub(r"<[^>]+>", "", t).replace("&amp;", "&").lower()
    t = re.sub(r"\(.*?\)", "", t).replace("&", " and ")
    t = re.sub(r"[^a-z0-9+]+", " ", t).strip()
    t = re.sub(r"^(the|a|an) ", "", t).replace(" vs ", " and ")
    t = re.sub(r"is(e|ed|ing)\b", r"iz\1", t)                      # British and American spellings
    return " ".join(w[:-1] if len(w) > 3 and w.endswith("s") and not w.endswith("ss") else w for w in t.split())


def index_titles(loaded):
    """Every note under its title, its title without the bracket, and the term in its “a.k.a.” kicker."""
    for o in JOURNALS:
        for num, slug, title, *_ in o["catalogue"]:
            names = {norm_title(title), norm_title(title.split(" (")[0])}
            n = loaded.get(o["key"], {}).get(slug)
            aka = re.match(r"a\.k\.a\. “([^”]+)”", n.get("kicker", "")) if n else None
            if aka:
                names.add(norm_title(aka.group(1)))
            for name in names:
                if (o, slug) not in TITLES.setdefault(name, []):
                    TITLES[name].append((o, slug))
    for name, (key, slug) in RELATED_ALIASES.items():
        TITLES.setdefault(norm_title(name), []).insert(0, (journal(key), slug))


def resolve_related(j, item):
    """(journal, slug) of the note a related entry names, or None. The text after the title narrows it down:
    “(this volume)”, “(Vol. 3)”, “(patterns, Vol. 6)”, “(Grace, vol. 4)”."""
    m = re.search(r"<b>(.*?)</b>", item)
    if not m:
        return None
    name = norm_title(m.group(1))
    cands = TITLES.get(name, []) or [c for t, cs in TITLES.items() if t.startswith(name + " ") for c in cs]
    cands = list(dict.fromkeys((o["key"], s) for o, s in cands))
    cands = [(journal(k), s) for k, s in cands]
    ctx = re.sub(r"<[^>]+>", "", item[m.end():]).lower()
    vol = re.search(r"vol\.?\s*(\d+)", ctx)
    filters = []
    who = [w for w in ("ana", "grace", "sanne", "mo") if re.search(rf"\b{w}\b", ctx)]
    if who:
        filters.append(lambda o: (o.get("narrator") or "").lower() in who)
    if "patterns" in ctx or (j.get("series", 1) == 1 and not who):
        filters.append(lambda o: o.get("series", 1) == 1)
    elif j.get("series") == 2 and not who:
        filters.append(lambda o: o.get("series") == 2 and o.get("book_no", 1) == j.get("book_no", 1))
    if vol:
        filters.append(lambda o: o["vol"] == int(vol.group(1)))
    if not vol and not who and "patterns" not in ctx:
        filters.append(lambda o: o["key"] == j["key"])
    for f in filters:
        narrowed = [c for c in cands if f(c[0])]
        if narrowed:
            cands = narrowed
    return cands[0] if len(cands) == 1 else None


def note_href(j, o, slug):
    """A link from a note page to another note. Always starts with ../ so the whole-journal page can rewrite it."""
    return f"../notes/{slug}.html" if o["key"] == j["key"] else f"../../{o['key']}/notes/{slug}.html"


def related_items(j, slug, items):
    out = []
    for r in items:
        r = re.sub(r"</?a\b[^>]*>", "", r)
        hit = resolve_related(j, r)
        if hit and hit[1] != slug:
            href = note_href(j, *hit)
            r = re.sub(r"<b>(.*?)</b>", lambda m: f'<a href="{href}"><b>{m.group(1)}</b></a>', r, count=1)
        elif not hit:
            UNRESOLVED.append((j["key"], slug, re.sub(r"<[^>]+>", "", r)))
        out.append(f"<li>{r}</li>")
    return "".join(out)


def find_seen_at_larder(loaded):
    for j in JOURNALS:
        if j.get("series") != 2:
            continue
        for slug, n in loaded[j["key"]].items():
            for r in n.get("related", []):
                hit = resolve_related(j, r)
                if hit and hit[0].get("series", 1) == 1:
                    title = entry(j, slug)[2]
                    SEEN_AT_LARDER.setdefault((hit[0]["key"], hit[1]), []).append((j, slug, title))


def extra_links(j, slug):
    """Asides under the related notes: seen at Larder, and the cheat sheet that covers this note."""
    out = []
    seen = SEEN_AT_LARDER.get((j["key"], slug), [])
    if seen:
        links = " · ".join(f'<a href="{note_href(j, o, s)}">{esc(t)}</a> <small>({o["narrator"]}, vol. {o["vol"]})</small>'
                           for o, s, t in seen)
        out.append(f'  <p class="aside seen">seen at Larder → {links}</p>')
    for cs in CARD_LINKS.get((j["key"], slug), []):
        if cs in CHEAT_TITLES:
            out.append(f'  <p class="aside deeper">on a card → <a href="../../cheatsheets/{cs}/index.html">{esc(CHEAT_TITLES[cs])}: the cheat sheet</a></p>')
    return "\n".join(out)


def revised_stamp(n):
    """`revised=("Nov 2026", "what changed")`: a small stamp under the date of a note that was updated."""
    r = n.get("revised")
    if not r:
        return ""
    return f'  <p class="revised"><span class="tag">revised</span> {r[0]} · {r[1]}</p>'


def render_note(j, n, back=()):
    num, slug, title, ckey, summary = entry(j, n["slug"])
    cname = coll(j, ckey)[1]
    vocab = "\n".join(f"    <div><dt>{t}</dt><dd>{d}</dd></div>" for t, d in n["vocab"])
    maprows = "\n".join(f"      <tr><td>{a}</td><td>{b}</td></tr>" for a, b in n["map"])
    steps = "\n".join(f"    <li><b>{t}</b><p>{d}</p></li>" for t, d in n["steps"])
    pits = "\n".join(f'    <li><h3>{t}</h3><p>{d} <span class="fix">Fix →</span> {f}</p></li>' for t, d, f in n["pitfalls"])
    quiz = "\n".join(f"    <details><summary>{q}</summary><p>{a}</p></details>" for q, a in n["quiz"])
    related = related_items(j, n["slug"], n["related"])
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
        revised_stamp(n),
        f'  <p class="kicker">{n["kicker"]}</p>',
        f'  <h1><span class="hl">{esc(title)}</span></h1>',
        f'  <div class="tldr">\n    <span class="tag">TL;DR</span>\n    <p>{n["tldr"]}</p>\n  </div>',
        f'  <ul class="chips" aria-label="At a glance">{chips}</ul>',
        pmbok_tag(j, n),
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
        deep_dive_block(n),
        h2(4, "tradeoffs", "Light, standard, heavy", "how much of this do you need?") if n.get("dial") else h2(4, "tradeoffs", "Gains vs losses", "nothing is free"),
        dial_block(n) if n.get("dial") else f'''  <div class="tchart">
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
        deeper_link(j["key"], slug),
        extra_links(j, slug),
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
            deep = ' <em class="deep-tag">+ goes deeper</em>' if slug in j.get("deep_dives", ()) else ""
            items.append(f'<li><a href="{href}"><span class="toc-n">{num:02d}</span><span class="toc-t">{esc(title)}{deep}'
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
    return "\n".join(x for x in [
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
        (f'  <p class="revised"><span class="tag">revised</span> {REVISION_NOTE[j["key"]][0]} · {REVISION_NOTE[j["key"]][1]}</p>'
         if j["key"] in REVISION_NOTE else ""),
        story_box(j),
        ('  <p class="map-link"><a href="../pmbok/index.html"><b>The PMBOK map</b>: every principle, domain and focus area of the guide, '
         'and the note that covers it →</a><br><a href="../rotterdam/index.html"><b>The project file</b>: every page from '
         'Sanne\'s binder, Rotterdam, Antwerp and the 2028 programme, in order →</a></p>') if j.get("pmbok") else "",
        KEY,
        '  <h2 id="index"><span class="num">✎</span>Index <span class="side">tap a note to open it</span></h2>',
        index_list(j),
        '  <h2 id="how-to-read"><span class="num">?</span>How every note is laid out <span class="side">same eight sections, every time</span></h2>',
        f'''  <ol class="how-to">
    <li><b>{j.get("problem_h2", "The problem")}</b>: {"a scene from the case study where it goes wrong" if j.get("book") else "what breaks without the pattern"}, with a doodle.</li>
    <li><b>Real-life analogy</b>: an everyday version, plus a “{j.get("map_caption", "translate to code").lower()}” table.</li>
    <li><b>How it solves it</b>: diagrams, steps, vocabulary and a {"template" if j.get("book") else "code"} card{". Key notes add a <b>going deeper</b> chapter here" if j.get("deep_dives") else ""}.</li>
    <li>{"<b>Light, standard, heavy</b>: how much of it a small, a typical and a heavy project needs." if j.get("pmbok") else "<b>Gains vs losses</b>: the trade-off spread."}</li>
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
    <p>FIRSTLAW</p>
  </div>'''.replace("FIRSTLAW", j.get("first_law", "Everything in architecture is a trade-off. If you think you've found one that isn't, you haven't found the cost yet.")),
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
    ] if x is not None)


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


AUTHOR_NOTE = """  <h2 id="author"><span class="num">✎</span>A note from the author <span class="side">why this shelf exists</span></h2>
  <aside class="author-note" aria-labelledby="author">
    <p class="lead">Your AI agent can write a saga orchestrator in eleven seconds. It cannot tell you whether you needed one.</p>
    <p>Everything on this shelf is for that second part.</p>
    <p>The classic books on this subject are excellent, 600 pages long and currently holding up a monitor. I wanted the same ideas in a form people finish. So there are four shapes here, sorted by how much time you have before the next meeting.</p>
    <ul>
      <li><b>Ten minutes: <a href="#shelf">a pattern note</a>.</b> One problem, one silly analogy, one diagram, and the column the agent never volunteers: <i>what we lose</i>.</li>
      <li><b>Thirty minutes: <a href="#deep-dives">a deep dive</a>.</b> The same pattern after it has met production. Failure drills, real numbers, and a checklist to take into a design review. There is a skim mode. I won't tell anyone.</li>
      <li><b>A story: <a href="#series-2">the practitioner's notebooks</a>.</b> Ana the architect and Grace the product owner join the same grocery start-up in the same month and write down what happens. It is the non-code half of the job: decisions, trade-offs, stakeholders and saying no politely.</li>
      <li><b>Thirty seconds: <a href="#cheatsheets">a cheat sheet</a>.</b> For the command you look up twice a week and will look up again on Thursday.</li>
    </ul>
    <p>What you get from any of them: better questions in the code review (<i>is this idempotent? where's the timeout?</i>), better prompts for the next ticket, and a sense of what each choice costs.</p>
    <p>The honest origin story: I had usage left before my weekly limit reset, and wasting it felt worse than wasting snacks. So I asked the agent to help me write notes about what agents get wrong. It found this very relatable.</p>
    <p class="author-sign">Read one a day. Argue with the ratings. Doodle in the margins.<br><span>by Jefrey Romel Tagunicar</span></p>
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


PMBOK_ITEM = '''    <li class="book book--pmbok">
      <a class="book-cover" href="pmbok/index.html" aria-label="Open the PMBOK map">
        <span class="book-band" aria-hidden="true"></span>
        <span class="book-label"><small>book 3 · find your way</small><b>The PMBOK Map</b><i>the guide on one page</i></span>
      </a>
      <div class="book-meta">
        <p>The whole PMBOK Guide (eighth edition) on one page: six principles, seven domains, five focus areas, and the note that covers each.</p>
        <p class="book-actions"><a class="btn" href="pmbok/index.html">Open the map</a><a class="btn btn--ghost" href="rotterdam/index.html">Project file</a></p>
      </div>
    </li>'''


# Cover artwork for the pattern volumes (owner's choice, Nov 2026: “option C”): a round paper sticker with one
# hand-drawn emblem, and the volume's own paper pattern pressed into the cloth in the band colour.
COVER_ART = {
    "distributed": ("server", "nodes"), "frontend": ("window", "grid"), "data": ("ledger", "rules"),
    "testing": ("flask", "cross"), "security": ("lock", "hatch"), "cloud": ("cloud", "iso"),
}
COVER_PATTERNS = {
    "grid": '<pattern id="{id}" width="14" height="14" patternUnits="userSpaceOnUse"><path d="M14 0H0V14" fill="none" stroke-width="1"/></pattern>',
    "rules": '<pattern id="{id}" width="20" height="12" patternUnits="userSpaceOnUse"><path d="M0 11.5H20" stroke-width="1"/></pattern>',
    "cross": '<pattern id="{id}" width="18" height="18" patternUnits="userSpaceOnUse"><path d="M9 5V13M5 9H13" stroke-width="1.4"/></pattern>',
    "hatch": '<pattern id="{id}" width="10" height="10" patternUnits="userSpaceOnUse"><path d="M0 10L10 0M-2 2L2 -2M8 12L12 8" stroke-width="1.2"/></pattern>',
    "iso": '<pattern id="{id}" width="24" height="14" patternUnits="userSpaceOnUse"><path d="M0 7L12 0L24 7L12 14Z" fill="none" stroke-width="1"/></pattern>',
}


def cover_art(key):
    if key not in COVER_ART:
        return ""
    icon, motif = COVER_ART[key]
    if motif == "nodes":
        cloth = ('<svg class="cover-cloth" viewBox="0 0 120 160" preserveAspectRatio="xMidYMid slice" aria-hidden="true">'
                 '<path class="cloth-line" d="M14 26 L62 52 L108 22 M62 52 L40 112 L98 128 M62 52 L98 128 M14 26 L40 112 M40 112 L20 150"/>'
                 '<g class="cloth-dot"><circle cx="14" cy="26" r="4"/><circle cx="62" cy="52" r="5"/><circle cx="108" cy="22" r="4"/>'
                 '<circle cx="40" cy="112" r="4"/><circle cx="98" cy="128" r="5"/><circle cx="20" cy="150" r="3"/></g></svg>')
    else:
        pid = f"cloth-{key}"
        cloth = (f'<svg class="cover-cloth" aria-hidden="true"><defs>{COVER_PATTERNS[motif].format(id=pid)}</defs>'
                 f'<rect width="100%" height="100%" fill="url(#{pid})"/></svg>')
    body = ICONS[icon].replace('class="F"', 'class="f-paper"')
    sticker = f'<span class="sticker" aria-hidden="true"><svg viewBox="-6 -6 72 72"><g class="d">{body}</g></svg></span>'
    return cloth + sticker


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
        {cover_art(k)}<span class="book-band" aria-hidden="true"></span>
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


# Short titles for book spines on the landing page (the full title shows on the pulled-out cover).
SPINE_TITLES = {
    "casefile": "Meet Larder",
    "architect-1": "Requirements", "architect-2": "Decisions", "architect-3": "Communicating",
    "architect-4": "Integration", "architect-5": "Qualities", "architect-6": "Delivery",
    "product-1": "Discovering", "product-2": "Deciding", "product-3": "Idea to Backlog",
    "product-4": "Measuring", "product-5": "Stakeholders", "product-6": "Growing",
    "pmbok": "PMBOK Map", "project-1": "Lay of the Land", "project-2": "Start, Steer, Close", "project-3": "What, By When", "project-4": "Money and People", "project-5": "People Outside", "project-6": "Making It Yours",
    "People Outside, and Surprises": "People &amp; Surprises",
    "Docker &amp; Kubernetes": "Docker &amp; K8s",   # cheat sheets are looked up by their full title
}


def spine_shelf(items_html, name, label):
    """Books stored spine-out: one row of spines, and the chosen volume pulled out underneath.
    items_html is what book_items()/cheatsheet_items() return; name makes the ids unique."""
    items = re.findall(r'<li class="book (book--[\w-]+)">(.*?)\n    </li>', items_html, flags=re.S)
    spines, panels = [], []
    for i, (cls, inner) in enumerate(items):
        key = cls.replace("book--", "")
        full = re.search(r"<b>(.*?)</b>", inner).group(1)
        title = SPINE_TITLES.get(key) or SPINE_TITLES.get(full, full)
        vol = "file" if key == "casefile" else "map" if key == "pmbok" else key.rsplit("-", 1)[1] if key.rsplit("-", 1)[-1].isdigit() else str(i + 1)
        planned_vol = re.search(r"vol\. (\d+)", inner) if key == "planned" else None
        vol = planned_vol.group(1) if planned_vol else vol
        on = i == 0
        spines.append(f'<button class="spine {cls}" type="button" role="tab" id="{name}-s{i}" aria-controls="{name}-p{i}" '
                      f'aria-selected="{"true" if on else "false"}" tabindex="{0 if on else -1}">'
                      f'<span class="spine-band" aria-hidden="true"></span><span class="spine-vol">{vol}</span>'
                      f'<span class="spine-title">{title}</span></button>')
        panels.append(f'    <div class="pulled book {cls}" role="tabpanel" id="{name}-p{i}" aria-labelledby="{name}-s{i}"'
                      f'{"" if on else " hidden"}>{inner}\n    </div>')
    return (f'  <div class="spine-shelf" data-spines>\n    <div class="spines" role="tablist" aria-label="{label}">'
            + "".join(spines) + "</div>\n" + "\n".join(panels) + "\n  </div>")


NUMBER_WORDS = ["none", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve"]


def render_landing(sheets=(), dives=()):
    series1 = [j for j in shelf() if j.get("series", 1) == 1]
    series2 = [j for j in shelf() if j.get("series", 1) == 2]
    months = []
    for month, items in FUTURE_LOG:
        lis = "".join(f'<li><span class="sig">{s}</span> {t}</li>' for s, t in items)
        months.append(f'    <div class="month"><h3>{month}</h3><ul>{lis}</ul></div>')
    total = sum(len(j["catalogue"]) for j in shelf())
    n1 = sum(len(j["catalogue"]) for j in series1)
    return "\n".join([
        head("Jef’s Notes", "Software design in sizes that fit a working day: ten-minute pattern notes with doodles and trade-offs, thirty-minute deep dives, two practitioner notebooks that follow one start-up, and printable cheat sheets.", 0, "Architects+Daughter&family=Permanent+Marker&family=IBM+Plex+Sans+Condensed:wght@700"),
        body_open(),
        '<a class="skip-link" href="#main">Skip to the shelf</a>',
        bar(None, 0, "shelf"),
        '<main id="main" class="desk">',
        '<article class="sheet landing">',
        '  <div class="page-meta"><span class="day">The shelf · 2026</span><span class="topic">series · <b>software design</b></span></div>',
        '  <p class="kicker">pattern notes, deep dives, two notebooks and a stack of cheat sheets</p>',
        '  <h1 class="cover-title"><span class="hl">Jef’s Notes</span></h1>',
        f'  <p class="lead">Software design, in sizes that fit a working day: <b>{n1} pattern notes, {len(dives)} deep dives, {total - n1} notes from three practitioners and {len(sheets)} cheat sheets</b>. More on the way.</p>',
        AUTHOR_NOTE,
        '  <h2 id="shelf"><span class="num">✎</span>Pattern notes <span class="side">ten minutes each</span></h2>',
        f'  <p class="hook">{len(series1)} notebooks, {n1} patterns. Each one fits in a coffee break and has a “what we lose” column, because something always is.</p>',
        f'  <ul class="shelf">\n{book_items(series1, PLANNED)}\n  </ul>',
        '  <h2 id="deep-dives"><span class="num">↓</span>Deep dives <span class="side">thirty minutes each</span></h2>',
        f'  <p class="hook">The textbook chapter you were supposed to read, with someone else\'s pencil notes in the margin. {NUMBER_WORDS[len(dives)].capitalize()} so far, each one a pattern after it has met production, with a skim mode for the honest.</p>',
        f'  <ul class="shelf shelf-series">\n{dive_items(dives)}\n  </ul>',
        '  <h2 id="series-2"><span class="num">✎</span>The Practitioner\'s Notebooks <span class="side">a story in three voices</span></h2>',
        '  <noscript><style>.pulled[hidden] { display: grid !important; } .spines { display: none !important; }</style></noscript>',
        '  <p class="hook">A soap opera about a grocery start-up, told by its architect, its product owner and its project manager. Nobody dies. Several roadmaps do.</p>',
        '  <p>The work <b>around</b> the code, following one company, <b>Larder</b>, as it grows from one city to six. Every note has a template to copy and a <b>try it</b> exercise for your own project. Tap a spine to pull a volume out; start with the case file.</p>',
        '  <h3 class="shelf-book">Book 1 · The Solution Architect\'s Notebook <span>narrated by Ana</span></h3>',
        spine_shelf(book_items([j for j in series2 if j.get("book_no", 1) == 1], PLANNED_2, series=2, book=1, casefile=True), "ana", "Book 1 volumes"),
        '  <h3 class="shelf-book">Book 2 · The Product Owner\'s Notebook <span>narrated by Grace</span></h3>',
        spine_shelf(book_items([j for j in series2 if j.get("book_no", 1) == 2], PLANNED_PRODUCT, series=2, book=2), "grace", "Book 2 volumes"),
        '  <h3 class="shelf-book">Book 3 · The Project Manager\'s Notebook <span>narrated by Sanne · the PMBOK Guide in plain words</span></h3>',
        spine_shelf(PMBOK_ITEM + "\n" + book_items([j for j in series2 if j.get("book_no", 1) == 3], PLANNED_PROJECT, series=2, book=3), "sanne", "Book 3 volumes"),
        '  <h2 id="cheatsheets"><span class="num">⌘</span>Cheat sheets <span class="side">thirty seconds each</span></h2>',
        '  <p class="hook">For when you know exactly what you want and have forgotten the flag.</p>',
        '  <p>The commands and decisions you look up twice a week, on a few printable A4 cards. They read fine on a phone too.</p>',
        spine_shelf(cheatsheet_items(sheets), "cheat", "Cheat sheets"),
        '  <h2 id="future"><span class="num">→</span>Future log <span class="side">plans, not promises</span></h2>',
        '  <p>In a bullet journal the <b>future log</b> is where next months\' plans go. Here\'s what I\'m planning to write next.</p>',
        '  <p class="aside">the architect\'s and the product owner\'s notebooks are complete, six volumes each, and the project manager\'s has begun (★): the whole PMBOK Guide, one domain per volume. After that: the client manager. The deep dives get a second season too.</p>',
        f'  <div class="future">\n{chr(10).join(months)}\n  </div>',
        '  <h2 id="inside"><span class="num">?</span>What\'s inside <span class="side">four formats, same idea</span></h2>',
        '''  <ol class="how-to">
    <li><b>A pattern note</b> has eight sections: the problem, a real-life analogy, how it works, gains vs losses, nine ratings, common pitfalls, when to use it, and a self-check quiz.</li>
    <li><b>A deep dive</b> has ten chapters: a recap of the notes, the real mechanism, failure drills, the hard problem, numbers, testing, running it, tools, a lab and a review checklist. Every chapter opens with its gist.</li>
    <li><b>A practitioner's note</b> has the same eight sections as a pattern note, set inside the Larder story, plus a template to copy and a “try it” exercise.</li>
    <li><b>A cheat sheet</b> is a few A4 cards: a map on top, boxed panels below, and a PDF to print.</li>
  </ol>''',
        '  <p class="folio">✦</p>',
        '</article>',
        foot(),
        '</main>',
        '</body>',
        '</html>',
        '',
    ])


# ---------------------------------------------------------------- deep dives (series 3)
# One long chaptered page per topic: content/deep-dives/<name>.py, rendered by scripts/dive.py.
DIVES = ["saga", "reliable_messaging", "resilience_stack", "event_sourcing_cqrs", "caching", "zero_downtime_change"]
DEEPER = {}   # (journal key, note slug) -> (dive slug, title); filled by load_dive


def load_dive(name):
    spec = importlib.util.spec_from_file_location(f"dive_{name}", CONTENT / "deep-dives" / f"{name}.py")
    mod = importlib.util.module_from_spec(spec)
    mod.__dict__.update(dive.HELPERS)
    spec.loader.exec_module(mod)
    d = mod.DIVE
    for key, slug in d.get("notes", []):
        DEEPER[(key, slug)] = (d["slug"], d["title"])
    return d


def deeper_link(key, slug):
    if (key, slug) not in DEEPER:
        return ""
    dslug, title = DEEPER[(key, slug)]
    return f'  <p class="aside deeper">go deeper → <a href="../../deep-dives/{dslug}/index.html">{esc(title)}: the deep dive</a></p>'


def dive_items(dives):
    out = []
    for d in dives:
        href = f"deep-dives/{d['slug']}/index.html"
        out.append(f'''    <li class="book book--dive">
      <a class="book-cover" href="{href}" aria-label="Open the deep dive: {esc(d['title'])}">
        <span class="book-band" aria-hidden="true"></span>
        <span class="book-label"><small>deep dive {d['no']:02d}</small><b>{esc(d['title'])}</b><i>{len(d['chapters'])} chapters</i></span>
      </a>
      <div class="book-meta">
        <p>{d['blurb']}</p>
        <p class="book-actions"><a class="btn" href="{href}">Open deep dive</a><a class="btn btn--ghost" href="deep-dives/{d['slug']}/pdf/{dive.pdf_name(d)}">{DL}PDF</a></p>
      </div>
    </li>''')
    return "\n".join(out)


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
        '  <p>Read one book from start to end, or follow the story in date order across books. <span class="sig-inline">★</span> story events · <span class="sig-inline">✎</span> Ana’s notebook · <span class="sig-inline sig-2">✎</span> Grace’s notebook · <span class="sig-inline sig-3">✎</span> Sanne’s notebook.</p>',
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


def load_pmbok_map():
    f = CONTENT / "pmbok" / "map.py"
    spec = importlib.util.spec_from_file_location("pmbok_map", f)
    mod = importlib.util.module_from_spec(spec)
    mod.__dict__["Doodle"] = Doodle
    spec.loader.exec_module(mod)
    return mod


def processes_block(m, link):
    """Process tables on the PMBOK map, one per domain that has been written (PROCESSES in content/pmbok/map.py)."""
    names = dict(PMBOK_DOMAINS)
    out = []
    for dom, rows in m.PROCESSES:
        trs = "\n".join(f'      <tr><td>{name}</td><td>{fa}</td><td>{plain}</td><td>{"<br>".join(link(r) for r in refs)}</td></tr>'
                        for name, fa, plain, refs in rows)
        out.append(f'  <h3 class="toc-coll"><span class="dom dom-{dom}">{names[dom]}</span> <span>{len(rows)} processes</span></h3>\n'
                   '  <div class="table-scroll"><table class="maptable">\n    <thead><tr><th scope="col">Process</th><th scope="col">Focus area</th>'
                   '<th scope="col">In plain words</th><th scope="col">Notes</th></tr></thead>\n    <tbody>\n' + trs + '\n    </tbody>\n  </table></div>')
    return "\n".join(out) + (f"\n{m.PROCESSES_NOTE}" if out else "")


# The project file's projects: (card folder, anchor, heading, period). A card joins the file when its file starts with one.
PROJECT_FILE_GROUPS = [
    (("rotterdam/", "larder/"), "rotterdam", "Rotterdam", "Jan → May 2026 · vols. 1–4"),
    (("antwerp/",), "antwerp", "Antwerp", "Oct 2026 → Oct 2027 · vol. 5"),
    (("programme/",), "programme", "Eindhoven and the 2028 programme", "Sep 2027 → Sep 2028 · vol. 6"),
]
PROJECT_FILE_PREFIXES = tuple(p for g in PROJECT_FILE_GROUPS for p in g[0])


def render_project_file(loaded):
    """The project file: every template card whose file is under a project's folder (rotterdam/, antwerp/), in book order,
    grouped by project. Served at /rotterdam/ (the first project's name; kept so older links still work)."""
    pages = []
    for j in JOURNALS:
        if not j.get("pmbok"):
            continue
        for num, slug, title, ckey, summary in j["catalogue"]:
            n = loaded[j["key"]].get(slug)
            if n and n["code"]["file"].startswith(PROJECT_FILE_PREFIXES):
                pages.append((j, num, slug, title, n["code"]))
    toc = "".join(f'<li><a href="#p{i}"><span class="toc-n">{i:02d}</span><span class="toc-t">{esc(c["file"].split("/")[-1])}'
                  f'<small>{esc(c["note"])}</small></span><span class="toc-p">vol. {j["vol"]} · {num:02d}</span></a></li>'
                  for i, (j, num, slug, title, c) in enumerate(pages, 1))
    def group(c):
        return next(g for g in PROJECT_FILE_GROUPS if c["file"].startswith(g[0]))

    def group_head(i, c):
        g = group(c)
        prev = pages[i - 2][4] if i > 1 else None
        if prev is not None and group(prev) is g:
            return ""
        return f'  <h2 class="file-group" id="{g[1]}"><span class="num">▤</span>{g[2]} <span class="side">{g[3]}</span></h2>\n'

    toc_groups = "".join(f'<li><a href="#{g[1]}"><b>{g[2]}</b> · {g[3]}</a></li>' for g in PROJECT_FILE_GROUPS
                         if any(group(c) is g for *_, c in pages))
    cards = "\n".join(
        group_head(i, c) +
        f'  <h3 class="file-h" id="p{i}"><span>{i:02d}</span>{esc(c["file"].split("/")[-1])} <small>explained in '
        f'<a href="../{j["key"]}/notes/{slug}.html">{esc(title)}</a> (vol. {j["vol"]} · {num:02d})</small></h3>\n'
        f'  <div class="card">\n    <div class="card-head"><span>{esc(c["file"])}</span><span>{esc(c["note"])}</span></div>\n'
        f'<pre><code>{esc(c["src"].strip(chr(10)))}</code></pre>\n  </div>'
        for i, (j, num, slug, title, c) in enumerate(pages, 1))
    j = dict(theme="theme-project pmbokmap projectfile", disclaimer=PMI_NOTE)
    return "\n".join([
        head("The Project File · Jef’s Notes", "Every page from Sanne's binder: Rotterdam, Antwerp and the 2028 programme, complete, worked sets of project documents.", 1, "Patrick+Hand+SC"),
        body_open(j),
        '<a class="skip-link" href="#main">Skip to the project file</a>',
        bar(None, 1),
        '<main id="main" class="desk">',
        '<article class="sheet">',
        f'  {ROUGH}',
        PROJECT_DOODLES,
        '  <div class="page-meta"><span class="day">Rotterdam 2026 · Antwerp 2026–27 · programme 2028</span><span class="topic">book 3 · <b>the worked example</b></span></div>',
        '  <p class="kicker">the project manager\'s notebook · Sanne\'s binder</p>',
        '  <h1 class="cover-title"><span class="hl">The Project File</span></h1>',
        f'  <p class="lead">Every note in <b>The Project Manager\'s Notebook</b> ends its “how” section with a page from Sanne\'s binder. Here they are together, in order: <b>{len(pages)} pages</b> so far, from two launches. <b>Rotterdam</b> (vols. 1–4) runs from its first week to its closing report; <b>Antwerp</b> (vol. 5), the first city abroad, adds the stakeholder and risk pages; <b>Eindhoven and the 2028 programme</b> (vol. 6) add the pages for tailoring, the playbook, programmes and growing. Within each project the numbers carry from page to page: the budget in the charter is the budget in the status report and in the closing report. Copy any page as a starting point; each links to the note that explains it.</p>',
        f'  <ul class="drivers">{toc_groups}</ul>',
        '  <p class="map-link"><a href="../pmbok/index.html"><b>The PMBOK map</b>: where each of these pages sits in the guide →</a></p>',
        '  <h2 id="index"><span class="num">✎</span>Contents <span class="side">tap a page to jump to it</span></h2>',
        f'  <ol class="toc">{toc}</ol>',
        '  <h2 id="pages"><span class="num">§</span>The pages <span class="side">project by project, in the order Sanne wrote them</span></h2>',
        cards,
        '  <p class="aside">this file grows with the book: each new volume adds its pages.</p>',
        '  <p class="folio">✦</p>',
        '</article>',
        foot(j),
        '</main>',
        '</body>',
        '</html>',
        '',
    ])


def render_pmbok_map(loaded):
    """The PMBOK map: the whole guide on one page, each item linked to the note that covers it."""
    m = load_pmbok_map()
    books = [j for j in JOURNALS if j.get("pmbok")]

    def link(ref):
        if not ref:
            return '<span class="todo">to come</span>'
        key, slug = ref
        o = journal(key)
        num, _, title, *_ = entry(o, slug)
        return f'<a href="../{key}/notes/{slug}.html">{esc(title)}</a> <small>vol. {o["vol"]} · {num:02d}</small>'

    principles = "\n".join(f'    <li><h3>{name}</h3><p>{plain}</p><p class="where">{link(ref)}</p></li>' for name, plain, ref in m.PRINCIPLES)
    focus = "\n".join(f'    <li><h3>{name}</h3><p>{plain}</p></li>' for name, plain in m.FOCUS)
    domains = "\n".join(
        f'      <tr><td><span class="dom dom-{k}">{name}</span></td><td>{q}</td><td class="n">{n}</td><td>{vol}</td></tr>'
        for k, name, q, n, vol in m.DOMAINS)
    total = sum(d[3] for d in m.DOMAINS)
    foundations = "\n".join(f'    <li><b>{what}</b>: {link(ref)}</li>' for what, ref in m.FOUNDATIONS)
    cross = "\n".join(f'      <tr><td>{a}</td><td>{b}</td><td>{c}</td><td>{d}</td></tr>' for a, b, c, d in m.CROSSWALK)
    vols = []
    for j in books:
        rows = []
        for num, slug, title, ckey, summary in j["catalogue"]:
            t = loaded[j["key"]].get(slug, {}).get("pmbok", {})
            names = dict(PMBOK_DOMAINS)
            doms = "".join(f'<span class="dom dom-{d}">{names[d]}</span>' for d in t.get("domains", [])) or '<span class="dom dom-foundations">Foundations</span>'
            deep = ' <em class="deep-tag">+ goes deeper</em>' if slug in j.get("deep_dives", ()) else ""
            rows.append(f'      <tr><td class="n">{num:02d}</td><td><a href="../{j["key"]}/notes/{slug}.html">{esc(title)}</a>{deep}</td>'
                        f'<td>{t.get("covers", "")}</td><td>{doms}</td></tr>')
        vols.append(f'  <h3 class="toc-coll">Vol. {j["vol"]} · {esc(j["title"])} <span>{len(j["catalogue"])} notes</span></h3>\n'
                    f'  <div class="table-scroll"><table class="maptable">\n    <thead><tr><th scope="col">#</th><th scope="col">The question</th>'
                    f'<th scope="col">What it covers in the guide</th><th scope="col">Domain</th></tr></thead>\n    <tbody>\n'
                    + "\n".join(rows) + '\n    </tbody>\n  </table></div>')
    planned = "".join(f"<li><b>Vol. {v} · {t}.</b> {b}</li>" for v, t, b in PLANNED_PROJECT)
    j = dict(theme="theme-project pmbokmap", disclaimer=PMI_NOTE)
    return "\n".join([
        head("The PMBOK Map · Jef’s Notes", "The PMBOK Guide, eighth edition, on one page: principles, domains, focus areas, and the note that covers each.", 1, "Patrick+Hand+SC"),
        body_open(j),
        '<a class="skip-link" href="#main">Skip to the map</a>',
        bar(None, 1),
        '<main id="main" class="desk">',
        '<article class="sheet">',
        f'  {ROUGH}',
        PROJECT_DOODLES,
        '  <div class="page-meta"><span class="day">PMBOK Guide · 8th edition</span><span class="topic">book 3 · <b>find your way</b></span></div>',
        '  <p class="kicker">the project manager\'s notebook · the guide on one page</p>',
        '  <h1 class="cover-title"><span class="hl">The PMBOK Map</span></h1>',
        f'  <p class="lead">{m.LEAD}</p>',
        '  <h2 id="shape"><span class="num">1</span>The shape of the guide <span class="side">6 · 7 · 5 · 40</span></h2>',
        m.shape.html(),
        m.SHAPE,
        '  <h2 id="principles"><span class="num">2</span>Six principles <span class="side">what good project management rests on</span></h2>',
        f'  <ol class="maplist">\n{principles}\n  </ol>',
        '  <h2 id="domains"><span class="num">3</span>Seven performance domains <span class="side">what you watch, all the way through</span></h2>',
        '  <div class="table-scroll"><table class="maptable">\n    <thead><tr><th scope="col">Domain</th><th scope="col">The question it answers</th>'
        '<th scope="col">Processes</th><th scope="col">In this book</th></tr></thead>\n    <tbody>\n' + domains +
        f'\n      <tr class="total"><td></td><td>all seven</td><td class="n">{total}</td><td></td></tr>\n    </tbody>\n  </table></div>',
        m.DOMAINS_NOTE,
        processes_block(m, link),
        '  <h2 id="focus"><span class="num">4</span>Five focus areas <span class="side">what kind of attention the work needs now</span></h2>',
        f'  <ol class="maplist maplist--focus">\n{focus}\n  </ol>',
        '  <h2 id="foundations"><span class="num">5</span>The ground under it <span class="side">ideas the guide builds on</span></h2>',
        f'  <ul class="drivers">\n{foundations}\n  </ul>',
        '  <h2 id="notes"><span class="num">6</span>Every note, by volume <span class="side">the question, and what it covers</span></h2>',
        "\n".join(vols),
        f'  <p>Still to come:</p>\n  <ul class="drivers">{planned}</ul>' if planned else '',
        '  <h2 id="editions"><span class="num">7</span>If you learned an older edition <span class="side">6th → 7th → 8th</span></h2>',
        m.EDITIONS,
        '  <div class="table-scroll"><table class="maptable">\n    <thead><tr><th scope="col"></th><th scope="col">6th (2017)</th><th scope="col">7th (2021)</th>'
        '<th scope="col">8th (2025)</th></tr></thead>\n    <tbody>\n' + cross + '\n    </tbody>\n  </table></div>',
        '  <p class="aside">this map grows with the book: each new volume fills in its domains.</p>',
        '  <p class="folio">✦</p>',
        '</article>',
        foot(j),
        '</main>',
        '</body>',
        '</html>',
        '',
    ])


# ---------------------------------------------------------------- cheat sheets (laminated reference cards)
CHEATSHEETS = ["git_flow", "docker_k8s", "sql", "nfr", "network"]
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


REVISIONS = {}       # journal key -> {slug: changes} from content/<key>/revisions.py (also used for hand-made notes)
REVISION_NOTE = {}   # journal key -> (month, what changed in this volume), shown on the index


def sit_q(q):
    """A situational question: tagged “what would you do?” above the question text."""
    return f'<span class="q-body"><span class="q-sit">what would you do?</span>{q}</span>'


def apply_revision(n, rev):
    """Merge a note's later additions into it: `quiz_add` appends questions, every other field replaces."""
    for k, v in rev.items():
        if k == "quiz_add":
            n["quiz"] = list(n["quiz"]) + [(sit_q(q), a) for q, a in v]
        else:
            n[k] = v


def load_content(key):
    notes = {}
    for f in sorted((CONTENT / key).glob("*.py")):
        spec = importlib.util.spec_from_file_location(f"{key}_{f.stem}", f)
        mod = importlib.util.module_from_spec(spec)
        mod.__dict__["Doodle"] = Doodle
        spec.loader.exec_module(mod)
        for n in getattr(mod, "NOTES", []):
            if n.get("quiz_sit"):   # situational questions, tagged “what would you do?” (notes written after Nov 2026)
                n["quiz"] = list(n["quiz"]) + [(sit_q(q), a) for q, a in n["quiz_sit"]]
            notes[n["slug"]] = n
        if hasattr(mod, "REVISIONS"):   # several files may add to the same note (revisions.py, deeper.py)
            for slug, rev in mod.REVISIONS.items():
                REVISIONS.setdefault(key, {}).setdefault(slug, {}).update(rev)
            if hasattr(mod, "REVISION_NOTE"):
                REVISION_NOTE[key] = mod.REVISION_NOTE
    for slug, rev in REVISIONS.get(key, {}).items():
        if slug in notes:
            apply_revision(notes[slug], rev)
            r = notes[slug].get("revised")
            if rev.get("deep_dive") and r and "going-deeper" not in r[1]:
                notes[slug]["revised"] = (r[0], r[1].replace(" and a try it", ", a try it") + " and a going-deeper chapter")
    return notes


def main():
    listing = []
    dives = [load_dive(name) for name in DIVES]   # first: notes link to their deep dive
    sheets = [load_cheatsheet(name) for name in CHEATSHEETS]
    CHEAT_TITLES.update((cs.SLUG, cs.TITLE) for cs in sheets)
    loaded = {j["key"]: load_content(j["key"]) for j in JOURNALS}
    index_titles(loaded)
    for j in JOURNALS:   # a note with a going-deeper chapter is tagged on the index
        j["deep_dives"] = set(j.get("deep_dives", ())) | {s for s, n in loaded[j["key"]].items() if n.get("deep_dive")}
    find_seen_at_larder(loaded)
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
            stamp_handmade(out / "notes" / f"{slug}.html", j)
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
    (PUBLIC / "pmbok").mkdir(exist_ok=True)
    (PUBLIC / "pmbok" / "index.html").write_text(render_pmbok_map(loaded), encoding="utf-8")
    (PUBLIC / "rotterdam").mkdir(exist_ok=True)
    (PUBLIC / "rotterdam" / "index.html").write_text(render_project_file(loaded), encoding="utf-8")
    for cs in sheets:
        out = PUBLIC / "cheatsheets" / cs.SLUG
        out.mkdir(parents=True, exist_ok=True)
        (out / "index.html").write_text(render_cheatsheet(cs), encoding="utf-8")
        listing.append(dict(key=f"cheatsheets/{cs.SLUG}", title=f"{cs.TITLE} cheat sheet", all=f"cheatsheets/{cs.SLUG}/index.html",
                            pdf=f"cheatsheets/{cs.SLUG}/pdf/{cheatsheet_pdf(cs)}", notes=[]))
        print(f"[cheatsheets] wrote {cs.SLUG} ({len(cs.PAGES)} cards)")
    for d in dives:
        out = PUBLIC / "deep-dives" / d["slug"]
        out.mkdir(parents=True, exist_ok=True)
        (out / "index.html").write_text(dive.render_dive(d, asset), encoding="utf-8")
        listing.append(dict(key=f"deep-dives/{d['slug']}", title=f"{d['title']} deep dive", all=f"deep-dives/{d['slug']}/index.html",
                            pdf=f"deep-dives/{d['slug']}/pdf/{dive.pdf_name(d)}", notes=[]))
        print(f"[deep-dives] wrote {d['slug']} ({len(d['chapters'])} chapters)")
    (PUBLIC / "index.html").write_text(render_landing(sheets, dives), encoding="utf-8")
    (PUBLIC / "journals.json").write_text(json.dumps(listing, indent=1), encoding="utf-8")
    # old links from before the shelf existed (everything was the distributed journal)
    old = PUBLIC / "notes"
    old.mkdir(exist_ok=True)
    for c in JOURNALS[0]["catalogue"]:
        (old / f"{c[1]}.html").write_text(redirect(f"../distributed/notes/{c[1]}.html"), encoding="utf-8")
    (PUBLIC / "all.html").write_text(redirect("distributed/all.html"), encoding="utf-8")
    print("wrote landing page, journals.json and redirects")
    if UNRESOLVED:
        print(f"[links] {len(UNRESOLVED)} related entries name no note (left as text); first ten:")
        for key, slug, text in UNRESOLVED[:10]:
            print(f"    {key}/{slug}: {text}")


if __name__ == "__main__":
    main()
