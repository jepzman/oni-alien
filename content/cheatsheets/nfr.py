# NFR / quality-attribute checklists · a laminated reference card in four pages.
# Rendered by scripts/build_notes.py (render_cheatsheet); Graph, Diagram, cmd, code and box come from scripts/cheatsheet.py.
# Boxes flow into a 3-column grid (dense packing), so order them to fill rows: wide (2) + narrow (1).

SLUG = "nfr-checklists"
TITLE = "NFR Checklists"
SUBTITLE = "quality attributes: what to ask, how to measure, typical targets"
DESC = ("A four-page checklist for non-functional requirements: how to write a measurable quality-attribute scenario, "
        "and the questions, measures and typical targets for performance, scalability, availability, reliability, "
        "security, privacy, observability, deployability, maintainability, usability, cost and more.")
VERSION = "v1 · Nov 2026"
BLURB = ("Four laminated pages for solution architects: how to write a measurable NFR, then the questions to ask, "
         "the measure and a typical target for every quality, from performance to cost. Ends with the trade-offs.")
LOGO = ('<svg viewBox="0 0 34 34" aria-hidden="true"><rect width="34" height="34" rx="8" fill="#FFFFFF" fill-opacity=".1"/>'
        '<rect x="8" y="6" width="18" height="23" rx="2.5" fill="none" stroke="var(--b-dev)" stroke-width="2.2"/>'
        '<path d="M12 13l2 2 4-4M12 21l2 2 4-4" fill="none" stroke="var(--b-feat)" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>'
        '<path d="M20 14h3M20 22h3" stroke="var(--b-rel)" stroke-width="2.2" stroke-linecap="round"/></svg>')


def qa(title, tone, asks, measure, target, span="", tag=None):
    """One quality attribute: questions to ask (a checklist), how to measure it, a typical target."""
    items = "".join(f"<li>{q}</li>" for q in asks)
    return box(title, f'''
<ul class="checks">{items}</ul>
<dl class="kv qa">
<dt>measure</dt><dd>{measure}</dd>
<dt>typical</dt><dd>{target}</dd>
</dl>''', tone, span, tag)


# ---------------------------------------------------------------- page 1 · writing NFRs
def scenario():
    d = Diagram("A quality-attribute scenario has six parts: source, stimulus, artifact, environment, response and response "
                "measure. Example: 2,000 shoppers place orders on the checkout service during the Black Friday peak; orders "
                "are confirmed with p95 under 800 ms and none lost.", 880, 132)
    parts = [("Source", "2,000 shoppers", "ink"), ("Stimulus", "place an order", "dev"), ("Artifact", "checkout service", "bug"),
             ("Environment", "Black Friday peak", "rel"), ("Response", "order confirmed", "feat"),
             ("Measure", "p95 < 800 ms · 0 lost", "main")]
    x = 14
    for i, (label, sub, tone) in enumerate(parts):
        d.node(f"p{i}", x, 30, 134, 52, label, sub, tone)
        d.text(x + 67, 20, ["who", "does what", "to what", "when / where", "what happens", "how much"][i], "dt", "middle")
        if i:
            d.arrow(f"p{i - 1}", f"p{i}", None, tone="ink")
        x += 145
    d.text(14, 106, "Not “the checkout must be fast”. Every NFR names who, what, where, when, what should happen, and a "
                    "number you can test.")
    d.text(14, 124, "No number, no requirement: if nobody can say how it is measured, it can't be accepted, tested or monitored.")
    return d.svg()


PAGE_WRITE = dict(
    title="Writing NFRs",
    kicker="from a vague wish to a testable number",
    figure=scenario(),
    boxes=[
        box("Vague → measurable", '''
<div class="tbl-wrap"><table class="tbl cmp">
<thead><tr><th>They say</th><th>Write it as</th></tr></thead>
<tbody>
<tr><td>“It must be fast”</td><td>search returns in <b>p95 &lt; 300 ms</b> at 200 req/s</td></tr>
<tr><td>“Always available”</td><td>checkout <b>99.95 %</b> monthly, excluding announced windows</td></tr>
<tr><td>“It must scale”</td><td>handles <b>3× today's peak</b> (600 orders/min) with p95 &lt; 1 s</td></tr>
<tr><td>“Secure”</td><td>staff sign in via <b>SSO + MFA</b>; no high OWASP findings at release</td></tr>
<tr><td>“Never lose data”</td><td><b>RPO 5 min, RTO 1 h</b>; restore tested quarterly</td></tr>
<tr><td>“Easy to change”</td><td>a new payment method ships in <b>≤ 2 sprints</b>, touching one service</td></tr>
<tr><td>“User-friendly”</td><td>new users finish checkout in <b>&lt; 2 min</b>; WCAG 2.2 AA</td></tr>
</tbody></table></div>''', "dev", "wide"),
        box("Questions for every NFR", '''
<ul class="checks">
<li><b>Who</b> needs it, and what happens if we miss it?</li>
<li><b>Which</b> journeys or services? Not “the system”.</li>
<li><b>When</b>: normal day, peak, during a failure, during a deploy?</li>
<li><b>How much</b>: a number, a percentile, a window</li>
<li><b>How measured</b>, by which tool, over which period?</li>
<li><b>Cost</b> to reach it vs the next step down?</li>
<li><b>Owner</b> who accepts it and watches it in production</li>
</ul>''', "warn"),
        box("Template", code('''
ID:          NFR-PERF-03
Quality:     Performance
Scenario:    2,000 concurrent shoppers place orders
             during the Black Friday peak
Measure:     p95 confirmation time < 800 ms,
             error rate < 0.1 %, 0 orders lost
Priority:    Must · business H · difficulty M
Verified by: load test in CI (k6), SLO dashboard
Owner:       Head of Ops · reviewed each quarter
'''), "ink", "wide", "copy me"),
        box("Prioritise: utility tree", '''
<p>Rate each scenario <b>(business value, technical difficulty)</b> as H / M / L.</p>
<dl class="kv">
<dt>(H, H)</dt><dd>drives the architecture: design and prototype first</dd>
<dt>(H, M/L)</dt><dd>must have; cheap wins, do them</dd>
<dt>(M/L, H)</dt><dd>challenge it: is it really needed?</dd>
<dt>(L, L)</dt><dd>note it, revisit later</dd>
</dl>
<p class="fine">Pick the top 3–5 quality attributes; they shape the design. Everything else is “good practice”.</p>''', "feat"),
        box("Verify it, keep it", '''
<dl class="kv">
<dt>Design</dt><dd>ATAM / design review against each scenario</dd>
<dt>Build</dt><dd>fitness functions in CI: latency, dependency rules, image size</dd>
<dt>Test</dt><dd>load, soak, chaos, failover, pen test, accessibility audit</dd>
<dt>Run</dt><dd>SLOs, dashboards and alerts on the same numbers</dd>
</dl>''', "main"),
    ],
)

# ---------------------------------------------------------------- page 2 · run-time qualities
PAGE_RUN = dict(
    title="Run-time qualities",
    kicker="performance, scale, availability, resilience",
    boxes=[
        qa("Performance", "dev", [
            "Latency per key operation: p50, <b>p95, p99</b>?",
            "Peak throughput: requests/s, messages/s, batch size?",
            "Payload sizes; slowest acceptable page or report?",
            "Batch windows: must finish by 06:00?",
            "Cold starts, first load, mobile on 4G?",
        ], "p95 / p99 latency at a stated load, from load tests and production metrics",
            "API p95 &lt; 300 ms · page LCP &lt; 2.5 s · report &lt; 10 s"),
        qa("Scalability", "feat", [
            "Growth in users, data, transactions: 1 and 3 years?",
            "Peak vs average ratio; seasonal spikes, campaigns?",
            "Stateless services? What has to be shared?",
            "Which data grows fastest; how is it partitioned?",
            "Elastic: how fast must capacity appear? Scale to zero? A cap on the bill?",
            "Third-party limits and quotas?",
        ], "throughput at 2–3× today's peak with latency still within target; time to scale out",
            "3× peak, ≤ 10 % latency degradation · scale out &lt; 2 min", "", "+ elasticity"),
        qa("Capacity &amp; data volume", "ink", [
            "Rows, files, events per day; total in 3 years?",
            "Retention: hot, warm, archive, delete?",
            "Largest single tenant or customer?",
            "Search, reporting, analytics on the same store?",
        ], "storage growth per month; query time at 3-year volume",
            "reports still &lt; 10 s on 3 years of data"),
        box("Availability: the nines", '''
<div class="tbl-wrap"><table class="tbl cmp">
<thead><tr><th>SLO</th><th>down / month</th><th>down / year</th></tr></thead>
<tbody>
<tr><th>99 %</th><td>7.3 h</td><td>3.65 days</td></tr>
<tr><th>99.9 %</th><td>43.8 min</td><td>8.77 h</td></tr>
<tr><th>99.95 %</th><td>21.9 min</td><td>4.38 h</td></tr>
<tr><th>99.99 %</th><td>4.4 min</td><td>52.6 min</td></tr>
<tr><th>99.999 %</th><td>26 s</td><td>5.3 min</td></tr>
</tbody></table></div>
<dl class="kv">
<dt>in series</dt><dd>multiply: 99.9 % × 99.9 % = <b>99.8 %</b></dd>
<dt>in parallel</dt><dd>1 − (1 − a)²: two 99 % copies = <b>99.99 %</b></dd>
</dl>
<p class="fine">Each extra nine costs roughly 10× more. Your SLO can't beat the dependencies you call in series.</p>''', "main"),
        qa("Availability", "main", [
            "SLO per <b>user journey</b> (checkout, search), not per server?",
            "Maintenance windows allowed? Announced how?",
            "Dependencies' SLAs; what if one is down?",
            "Business hours only, or 24/7? Which time zones?",
            "Single points of failure: database, DNS, one AZ?",
        ], "good requests ÷ all requests per journey over 30 days",
            "customer-facing 99.9–99.95 % · internal tools 99.5 %", "wide"),
        qa("Reliability &amp; fault tolerance", "hot", [
            "Timeouts, retries with backoff, circuit breakers?",
            "Idempotent writes and message handling?",
            "Degraded mode: what still works when X is down?",
            "Duplicate, late or out-of-order messages?",
            "Data integrity checks, reconciliation?",
        ], "error rate, failed-over requests, incidents per month, MTTR",
            "error rate &lt; 0.1 % · MTTR &lt; 1 h"),
        qa("Disaster recovery", "rel", [
            "<b>RPO</b>: how much data can we lose?",
            "<b>RTO</b>: how long may we be down?",
            "Region or cloud outage in scope?",
            "Backups encrypted, off-site, <b>restore tested</b>?",
            "Runbook, owner, last DR drill date?",
        ], "RPO / RTO achieved in a timed restore or failover drill",
            "tier 1: RPO 5 min, RTO 1 h · tier 3: RPO 24 h, RTO 3 days", "wide"),
    ],
)

# ---------------------------------------------------------------- page 3 · security, data & operations
PAGE_SEC = dict(
    title="Security, data &amp; operations",
    kicker="protect it, prove it, run it, change it",
    boxes=[
        qa("Security", "main", [
            "Authentication: SSO, MFA, passwordless? For staff and customers?",
            "Authorisation: roles, least privilege, row-level / tenant isolation?",
            "Data classification: public, internal, confidential, restricted?",
            "Encryption in transit (TLS 1.2+) and at rest; key management?",
            "Secrets in a vault, rotated; none in code or images?",
            "Threat model done? OWASP Top 10, dependency and image scanning in CI?",
            "Pen test before go-live; who fixes findings, how fast?",
        ], "open findings by severity; time to patch; MFA coverage",
            "0 critical / high open at release · critical CVEs patched &lt; 7 days", "wide", "CIA"),
        qa("Privacy &amp; compliance", "hot", [
            "Which personal data, where, why (legal basis)?",
            "Retention and deletion rules?",
            "Data residency: EU only?",
            "Rights: access, export, erase?",
            "Which rules: GDPR, PCI DSS, HIPAA, SOC 2, ISO 27001?",
        ], "data inventory complete; audit findings; erase requests on time",
            "erase within 30 days · audit trail kept 7 years"),
        qa("Observability", "dev", [
            "Structured logs with a correlation / trace ID?",
            "Metrics: RED for services, USE for resources?",
            "Distributed tracing across services and queues?",
            "A dashboard per user journey?",
            "Alerts on SLO burn rate, not on CPU?",
            "Log retention and PII masking?",
        ], "time to detect (MTTD) and to find the cause in an incident",
            "detect &lt; 5 min · every alert has a runbook"),
        qa("Deployability", "feat", [
            "How often do we want to release? Who approves?",
            "Zero-downtime deploys? DB migrations too?",
            "Rollback time? Feature flags?",
            "Environments: how many, how alike?",
            "Infrastructure as code, reproducible?",
        ], "DORA: deploy frequency, lead time, change failure rate, time to restore",
            "daily deploys · lead time &lt; 1 day · CFR &lt; 15 %"),
        qa("Maintainability &amp; evolvability", "bug", [
            "Clear module / service boundaries; who owns what?",
            "Tests on critical paths; coding standards, reviews?",
            "Dependency upgrade cadence; end-of-life dates?",
            "ADRs and docs kept with the code?",
            "Which changes do we expect (new market, new channel)?",
        ], "lead time for a typical change; files / services touched per change",
            "new dev ships to prod in week 1"),
        qa("Testability", "rel", [
            "Test data: synthetic, masked, refreshable?",
            "Third parties: sandboxes, mocks, contract tests?",
            "Can each service be tested alone?",
            "Load and failover testable before go-live?",
        ], "share of automated tests; time for a full regression run",
            "full regression &lt; 30 min, in CI"),
        qa("Supportability", "ink", [
            "Support hours and tiers (L1 / L2 / L3)?",
            "Incident priorities with response times?",
            "Who's on call; escalation path?",
            "Admin tools so support needs no database access?",
        ], "response and resolve times per priority",
            "P1 response 15 min, 24/7 · P3 next business day", "wide"),
    ],
)

# ---------------------------------------------------------------- page 4 · people, money, landscape + trade-offs
def tradeoffs():
    d = Diagram("Common trade-offs between qualities: security versus usability, performance versus cost, availability versus "
                "cost, consistency versus availability, performance versus maintainability, and time to market versus "
                "quality. Improving one usually costs some of the other.", 880, 184)
    pairs = [("Security", "Usability", "MFA, timeouts and checks add friction", "main", "feat"),
             ("Performance", "Cost", "more capacity, caches and replicas cost money", "dev", "rel"),
             ("Availability", "Cost", "each extra nine ≈ 10× the price", "main", "rel"),
             ("Consistency", "Availability", "in a partition, pick one (CAP / PACELC)", "bug", "main"),
             ("Performance", "Maintainability", "hand-tuned code is harder to change", "dev", "bug"),
             ("Time to market", "Quality", "shortcuts now, interest later (tech debt)", "hot", "feat")]
    for i, (a, b, why, ta, tb) in enumerate(pairs):
        col, row = divmod(i, 3)
        x, y = 14 + col * 440, 10 + row * 58
        d.node(f"a{i}", x, y, 116, 40, a, None, ta)
        d.node(f"b{i}", x + 300, y, 116, 40, b, None, tb)
        d.arrow(f"a{i}", f"b{i}", "vs", tone="ink", both=True, ly=y + 16)
        d.text(x + 208, y + 54, why, "dt", "middle")
    return d.svg()


PAGE_MORE = dict(
    title="People, money &amp; trade-offs",
    kicker="usability, cost, integration, and what pulls against what",
    figure=tradeoffs(),
    boxes=[
        qa("Usability &amp; accessibility", "feat", [
            "WCAG 2.2 AA (or legal duty: EAA, ADA)?",
            "Devices, browsers, screen sizes, offline?",
            "Languages, locales, currencies, time zones?",
            "Key tasks: time and steps to complete?",
        ], "audit results; task success rate and time in user tests",
            "WCAG AA · 90 % task success unaided"),
        qa("Cost", "rel", [
            "Budget per month: build, run, licences, people?",
            "Cost per order / user / tenant: the unit cost?",
            "Reserved vs on-demand vs spot? Egress?",
            "Tags per team / product; alerts at 80 % of budget?",
            "Who owns the bill (FinOps)?",
        ], "monthly cost vs budget; cost per business unit of work",
            "unit cost flat or falling as volume grows"),
        qa("Interoperability &amp; integration", "dev", [
            "Standards: REST + OpenAPI, events, files, EDI?",
            "Versioning and deprecation policy?",
            "Partners' rate limits, SLAs, sandboxes?",
            "Data formats, encodings, master data owner?",
        ], "partners onboarded; breaking changes per year",
            "no breaking change without a 6-month overlap"),
        qa("Portability &amp; lock-in", "ink", [
            "Which lock-in is acceptable: cloud, database, SaaS?",
            "Exit plan: data export, contract terms?",
            "Containers / open standards where it matters?",
        ], "effort to move a component; data export tested",
            "full data export in an open format, on request"),
        box("Before sign-off", '''
<ul class="checks">
<li>Every NFR has a <b>number</b>, a <b>measure</b> and an <b>owner</b></li>
<li>Top 3–5 qualities agreed and ranked</li>
<li>Each one traced to a design decision (ADR)</li>
<li>Trade-offs written down, with who accepted them</li>
<li>Each one has a test or a fitness function</li>
<li>Each one is on a dashboard or SLO in production</li>
<li>Review date set: NFRs change with the business</li>
</ul>''', "warn", "wide"),
        box("Ask the right people", '''
<dl class="kv">
<dt>Business</dt><dd>peak days, growth, cost of downtime</dd>
<dt>Users</dt><dd>devices, tasks, accessibility</dd>
<dt>Ops / SRE</dt><dd>SLOs, on-call, runbooks</dd>
<dt>Security</dt><dd>data classes, threats, rules</dd>
<dt>Legal / DPO</dt><dd>privacy, residency, retention</dd>
<dt>Finance</dt><dd>budget, unit cost</dd>
</dl>''', "main"),
    ],
)

PAGES = [PAGE_WRITE, PAGE_RUN, PAGE_SEC, PAGE_MORE]
