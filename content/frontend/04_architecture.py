# Vol. 2 · Architecture & resilience: Micro-Frontends, Design Tokens, Error Boundaries.

# ------------------------------------------------------------------ 13 Micro-Frontends
mf_problem = Doodle(760, 280, "Doodle of one huge frontend repository shared by five teams: search, product, cart, checkout and account. Every release needs all teams to merge into one pipeline, a broken test from one team blocks the others, and a 40 minute build ships everything together.",
                    "Five teams, one frontend, one pipeline: everyone waits for everyone.")
mf_problem.box(20, 30, 420, 220, None, "pink", stroke="red")
mf_problem.head(230, 60, "one frontend monolith", size=19, color="red")
for i, t in enumerate(["search", "product", "cart", "checkout", "account"]):
    mf_problem.box(40 + (i % 3) * 132, 80 + (i // 3) * 64, 120, 46, t, "paper", size=16, rx=6)
mf_problem.text(230, 228, "1 repo · 1 build (40 min) · 1 release train", size=16)
mf_problem.note(600, 70, "cart's flaky test", "red")
mf_problem.note(600, 96, "blocks checkout's fix", "red")
mf_problem.note(600, 150, "upgrade React?", "red")
mf_problem.note(600, 176, "all 5 teams at once", "red")
mf_problem.note(600, 230, "release every 2 weeks", "red")

mf_analogy = Doodle(760, 260, "Doodle of a food court. Several independent stalls each have their own kitchen, menu and staff and open or change on their own schedule. They share the building, the seating, the trays and the signage, so customers feel it's one place.",
                    "Independent stalls with their own kitchens, sharing one building, seating and trays.")
for i, t in enumerate(["noodles", "tacos", "salads"]):
    mf_analogy.icon("store", 40 + i * 170, 40, 1.8)
    mf_analogy.note(100 + i * 170, 170, t + " team")
mf_analogy.icon("tray", 560, 80, 2.0)
mf_analogy.note(640, 60, "shared trays + seating", "pen")
mf_analogy.note(380, 240, "own kitchen, own hours · one building (the shell)", "green")

mf_how = Doodle(760, 320, "Micro-frontend architecture. An app shell owns the layout, routing, sign-in and the design system. It loads independently deployed micro-frontends by route: search, product and checkout, each owned by one team with its own repository and pipeline. They communicate through the URL and a few documented events.",
                "A thin shell routes to independently built and deployed apps; contracts are URLs, events and the design system.")
mf_how.box(20, 20, 720, 70, "app shell", "y", sub="layout · routing · auth · design system")
for i, (t, team) in enumerate([("/search", "Search team"), ("/product", "Product team"), ("/checkout", "Checkout team")]):
    x = 30 + i * 245
    mf_how.box(x, 140, 210, 90, t, "green", sub=team)
    mf_how.arrow(x + 105, 94, x + 105, 136)
    mf_how.note(x + 105, 260, "own repo + deploy", "pen", size=18)
mf_how.note(380, 306, "talk via URL + events like cart:updated", "pen")

MICRO = dict(
    slug="micro-frontends",
    kicker="a.k.a. “microservices for the UI”",
    tldr="Split a large frontend into <b>smaller apps owned end-to-end by separate teams</b> (usually by business area: search, product, checkout). Each is <b>built and deployed independently</b>; a thin <b>shell</b> composes them into one experience, sharing layout, routing, auth and the <b>design system</b>.",
    chips=[("Family", "frontend architecture / organisation"), ("Coined", "ThoughtWorks Tech Radar, 2016"), ("Techniques", "route-based, module federation, web components, server composition"), ("Pairs with", "design tokens, API gateway / BFF")],
    problem="""  <p class="lead">Backends were split into services so teams could move independently. Many frontends stayed <span class="hl-pink">one big monolith</span>, and became the bottleneck.</p>
  <ul>
    <li>Five teams merge into one repo and one release train; one team's broken test blocks everyone.</li>
    <li>Builds take 40 minutes; releases happen every two weeks.</li>
    <li>Upgrading a framework means coordinating every team at once.</li>
    <li>Ownership is blurry: who fixes the shared header?</li>
  </ul>""",
    problem_figs=[mf_problem],
    analogy_side="the food court",
    analogy="""  <p>A <b>food court</b> has independent stalls. Each has its own kitchen, menu and staff, and can change its recipes or opening hours without asking the others. They share the building, the seating, the trays and the signs, so customers experience <b>one place</b>.</p>
  <ul>
    <li>If the taco stall closes for a day, you can still get noodles: <b>isolation</b>.</li>
    <li>If every stall used different trays and signs, it would feel chaotic: you need a <b>shared design system</b>.</li>
    <li>Too many tiny stalls and it's hard to find dinner: <b>don't split too fine</b>.</li>
  </ul>""",
    analogy_figs=[mf_analogy],
    map=[("Each stall with its own kitchen", "A micro-frontend owned by one team"),
         ("Changing recipes without asking", "Independent build and deploy"),
         ("The building, seating, trays", "The app shell + design system"),
         ("Signs pointing to stalls", "Routing between micro-frontends"),
         ("One stall closed, others open", "Failure isolation between parts")],
    how_side="split by business area, compose in a shell",
    how="""  <p>Split <b>vertically by business capability</b> (a team owns checkout from database to button), not horizontally by layer. Then choose how to compose: separate routes/pages (simplest), runtime loading (module federation), web components, or server-side composition.</p>""",
    how_figs=[mf_how],
    steps=[("Split by domain, not by component", "Search, product, checkout, account. Each maps to one team and ideally its own backend services."),
           ("Build a thin shell", "Layout, top-level routing, authentication, error handling, and loading the right app."),
           ("Share a design system, not code", "Tokens and components as a versioned package so everything looks like one product."),
           ("Define small contracts", "URLs, a few documented browser events (<code>cart:updated</code>), and shared auth. No reaching into each other's state."),
           ("Deploy independently", "Each app has its own pipeline; the shell discovers versions from a manifest.")],
    vocab=[("Vertical slice", "A team owns a feature across all layers."),
           ("App shell", "The host that composes micro-frontends."),
           ("Module federation", "Loading code from separately deployed builds at runtime."),
           ("Web components", "Framework-agnostic custom elements as a boundary."),
           ("Server-side composition", "Assembling page fragments on the server / edge."),
           ("Import map", "Browser mapping from module names to URLs.")],
    code=dict(file="shell/routes.tsx", note="route-based composition (module federation)", src="""
// each remote is built and deployed by its own team; the shell only knows the contract
const SearchApp   = lazy(() => import("search/App"));     // remote: search.example.com/remoteEntry.js
const CheckoutApp = lazy(() => import("checkout/App"));   // remote: checkout.example.com/remoteEntry.js

export function Shell() {
  const user = useSession();                               // shared by the shell
  return (
    <DesignSystemProvider theme="brand">
      <Header user={user} />
      <ErrorBoundary fallback={<SectionDown />}>           {/* one app failing doesn't kill the page */}
        <Suspense fallback={<PageSkeleton />}>
          <Routes>
            <Route path="/search/*" element={<SearchApp />} />
            <Route path="/checkout/*" element={<CheckoutApp user={user} />} />
          </Routes>
        </Suspense>
      </ErrorBoundary>
    </DesignSystemProvider>
  );
}

// contract between apps: a documented browser event, not shared state
window.dispatchEvent(new CustomEvent("cart:updated", { detail: { count: 3 } }));
"""),
    tools="tools: Webpack / Rspack Module Federation, Vite federation plugins, single-spa, Piral, Nx / Turborepo monorepos, web components (Lit), edge/server composition (ESI, Podium); many teams start with simple route-based splitting across separate apps.",
    gains=["<b>Team autonomy</b>: build, test and deploy independently.",
           "<b>Faster, smaller releases</b> per area.",
           "<b>Isolated failures</b> and incremental upgrades.",
           "<b>Clear ownership</b> by business capability.",
           "<b>Gradual migration</b> from legacy frontends (strangler fig)."],
    losses=["<b>Inconsistent UX</b> without a strong design system.",
            "<b>Duplicate dependencies</b> and bigger bundles.",
            "<b>Complex tooling</b>: federation, versioning, shared deps.",
            "<b>Harder end-to-end testing</b> and debugging.",
            "<b>Overkill</b> for small teams."],
    baseline="Each line compares <b>one frontend monolith shared by several teams</b> to the same product split into <b>micro-frontends</b> with a shell.",
    ratings=[(3, 2, "Several apps, a shell and contracts to understand."),
             (3, 3, "Reuse moves to the design system; apps themselves are specific."),
             (3, 3, "Each app tests alone; cross-app flows get harder."),
             (2, 4, "Teams change their area without touching others."),
             (3, 2, "Risk of duplicated frameworks and extra requests."),
             (3, 2, "Shared dependencies are hard to dedupe perfectly."),
             (3, 3, "Consistent only if the design system enforces it."),
             (2, 3, "Faster local builds, more complex overall tooling."),
             (1, 5, "The main reason to do it: teams move independently.")],
    pitfalls=[("Splitting by component, not domain", "One team owns “buttons”, another “forms”, and every feature needs all of them.", "split vertically by business capability."),
              ("Shared global state between apps", "Apps read each other's Redux stores, so they're coupled again.", "communicate via URL, events and backend APIs."),
              ("No design system", "Five slightly different headers and buttons.", "a versioned design system and tokens owned by a platform team."),
              ("Doing it with two teams", "The tooling costs more than the coordination it saves.", "a modular monolith until team count makes it hurt."),
              ("Five copies of React", "Each app bundles its own framework.", "share core dependencies as singletons, or align versions.")],
    use=["Several teams (roughly 4+) work on one product frontend.",
         "Different areas release at different speeds.",
         "Migrating a legacy frontend piece by piece.",
         "Clear business areas map to teams."],
    skip=["One or two teams: a well-structured monolith is simpler.",
          "Performance budgets are tight and can't afford duplication.",
          "No capacity to run a shared design system and platform."],
    related=["<b>Design tokens</b>", "<b>Error boundaries</b>", "<b>Code splitting</b>", "<b>API gateway / BFF</b> (Vol. 1)"],
    quiz=[("Why split micro-frontends by business area rather than by UI layer?", "So one team can deliver a whole feature end to end without coordinating with others."),
          ("How should micro-frontends communicate?", "Through URLs, a few documented browser events, and backend APIs, not by sharing each other's state."),
          ("What keeps micro-frontends looking like one product?", "A shared, versioned design system with design tokens, plus a shell that owns layout."),
          ("When are micro-frontends overkill?", "With one or two teams, where tooling cost outweighs the coordination they'd save.")],
    remember="Split the <span class=\"hl\">teams'</span> work, not the <span class=\"hl\">user's</span> experience. Own stalls, one building.",
    sources=["Cam Jackson, “Micro Frontends” (martinfowler.com).",
             "Michael Geers, <i>Micro Frontends in Action</i>.",
             "Luca Mezzalira, <i>Building Micro-Frontends</i>.",
             "Webpack docs, “Module Federation”."],
)

# ------------------------------------------------------------------ 14 Design Tokens
dt_problem = Doodle(760, 260, "Doodle of a codebase with 47 slightly different blues: hex values like 1D4EB5, 1E4FB4 and 2050B8 copied into CSS, iOS and Android code. A rebrand to a new blue means a find-and-replace across hundreds of files and three platforms, and dark mode is impossible.",
                    "47 hard-coded blues across three platforms. Rebrand? Dark mode? Good luck.")
for i, (hexv, x, y) in enumerate([("#1D4EB5", 30, 40), ("#1E4FB4", 190, 70), ("#2050B8", 60, 120), ("#1C4DB2", 230, 150), ("#1D4FB6", 40, 190), ("#2151B9", 210, 210)]):
    dt_problem.box(x, y, 130, 36, hexv, "blue", size=15, rx=4)
dt_problem.note(560, 60, "47 blues in the codebase", "red")
dt_problem.note(560, 100, "web · iOS · Android", "red")
dt_problem.note(560, 150, "rebrand = 600 file edits", "red")
dt_problem.note(560, 200, "dark mode = impossible", "red")

dt_analogy = Doodle(760, 260, "Doodle of a paint shop palette with named swatches like Ocean 500 and Sand 100. A whole house is painted using only these names. To refresh the look, the shop changes what Ocean 500 means, and every room using that name updates.",
                    "Paint every room from named swatches. Change the swatch, and every room follows.")
dt_analogy.icon("palette", 60, 60, 2.2)
for i, (name, fill) in enumerate([("ocean-500", "blue"), ("sand-100", "y"), ("coral-400", "pink"), ("moss-300", "green")]):
    dt_analogy.box(280, 30 + i * 52, 170, 42, name, fill, size=17, rx=4)
dt_analogy.arrow(456, 130, 560, 130, label="used by name", lx=508, ly=118)
dt_analogy.icon("store", 580, 80, 1.6)
dt_analogy.note(640, 220, "rebrand: change the swatch", "green")

dt_how = Doodle(760, 300, "Three tiers of tokens. Primitive tokens hold raw values like blue 600 equals 1D4EB5. Semantic tokens give meaning: color action primary refers to blue 600 in light mode and blue 300 in dark mode. Component tokens apply them: button background uses color action primary. A build tool such as Style Dictionary turns the JSON into CSS variables, iOS and Android files.",
                "Primitive → semantic → component. One JSON source, compiled for every platform and theme.")
dt_how.box(20, 30, 210, 100, "primitive", "paper", sub="blue-600 = #1D4EB5")
dt_how.arrow(236, 80, 284, 80)
dt_how.box(290, 30, 230, 100, "semantic", "y", sub="action-primary → blue-600")
dt_how.arrow(526, 80, 574, 80)
dt_how.box(580, 30, 160, 100, "component", "green", sub="button-bg")
dt_how.note(405, 150, "dark theme: action-primary → blue-300", "pen")
dt_how.box(200, 190, 360, 50, "tokens.json → Style Dictionary", "y", size=17)
for i, t in enumerate(["CSS variables", "iOS (Swift)", "Android (XML)"]):
    dt_how.arrow(380, 244, 120 + i * 260, 270, dash=True)
    dt_how.note(120 + i * 260, 292, t, "pen", size=18)

TOKENS = dict(
    slug="design-tokens",
    kicker="a.k.a. “name it once, use it everywhere”",
    tldr="Store every design decision (colours, spacing, type sizes, radii, shadows, motion) as <b>named tokens</b> in one source, like <code>color.action.primary</code> or <code>space.4</code>. Components use the <b>names, never raw values</b>. A build step outputs them for every platform, and <b>themes</b> (dark mode, brands) are just different values for the same names.",
    chips=[("Family", "design systems"), ("Origin", "Salesforce Lightning (2014)"), ("Standard", "W3C Design Tokens format (DTCG)"), ("Pairs with", "headless components, micro-frontends")],
    problem="""  <p class="lead">Without tokens, design decisions are <span class="hl-pink">copied as raw values</span> everywhere: hex colours, pixel sizes, font stacks.</p>
  <ul>
    <li>A codebase ends up with 47 slightly different blues and 12 grey borders.</li>
    <li>A rebrand means find-and-replace across hundreds of files on web, iOS and Android.</li>
    <li>Dark mode or a second brand is almost impossible to add.</li>
    <li>Designers and developers talk past each other: “the blue” vs <code>#1E4FB4</code>.</li>
  </ul>""",
    problem_figs=[dt_problem],
    analogy_side="the paint swatches",
    analogy="""  <p>A paint shop names its colours: <b>Ocean 500</b>, <b>Sand 100</b>. Paint every room by <b>name</b>, never by mixing your own. Want a fresh look? Change what Ocean 500 means, and every room using it follows.</p>
  <ul>
    <li>Everyone (designer, decorator, owner) uses the <b>same words</b>.</li>
    <li>A “night” palette can map the same names to darker paints: <b>themes</b>.</li>
    <li>The rule “accent walls use Coral 400” is a <b>semantic</b> decision built on a raw swatch.</li>
  </ul>""",
    analogy_figs=[dt_analogy],
    map=[("Named paint swatches", "Primitive tokens (<code>blue.600</code>)"),
         ("“Accent walls use Coral 400”", "Semantic tokens (<code>color.action.primary</code>)"),
         ("Painting by name, not mixing", "Components use tokens, never raw values"),
         ("Changing what Ocean 500 means", "Rebrand by editing one token"),
         ("A night palette", "A dark theme mapping the same names")],
    how_side="three tiers, one source, many outputs",
    how="""  <p>Most systems use three tiers: <b>primitives</b> (the raw palette), <b>semantic</b> tokens (meaning and theme), and optional <b>component</b> tokens. Components only ever reference semantic or component tokens.</p>""",
    how_figs=[dt_how],
    steps=[("Collect the decisions", "Audit colours, spacing, type, radii, shadows, motion durations; merge near-duplicates."),
           ("Define primitives", "The raw scale: <code>blue.50 … blue.900</code>, <code>space.1 … space.12</code>."),
           ("Add semantic names", "<code>color.text.default</code>, <code>color.surface.raised</code>, <code>color.action.primary</code>: say what it's for, not what it looks like."),
           ("Generate per platform and theme", "Style Dictionary (or similar) turns one JSON source into CSS variables, Swift, Kotlin and Figma variables, per theme."),
           ("Enforce usage", "Lint rules forbid raw hex/px in components; contrast checks run on token pairs.")],
    vocab=[("Design token", "A named design decision with a value."),
           ("Primitive token", "Raw value in a scale (blue-600, space-4)."),
           ("Semantic token", "Purpose-based alias (action-primary)."),
           ("Theme", "A set of values for the same semantic names."),
           ("Style Dictionary", "Tool that builds tokens for many platforms."),
           ("DTCG format", "The W3C community group's JSON format for tokens.")],
    code=dict(file="tokens.json → tokens.css", note="DTCG-style JSON and generated CSS", src="""
{
  "blue":  { "300": { "$value": "#8EB5FF" }, "600": { "$value": "#1D4EB5" } },
  "color": {
    "action": { "primary": { "$value": "{blue.600}" } },
    "text":   { "default": { "$value": "#272B33" } }
  },
  "space": { "2": { "$value": "8px" }, "4": { "$value": "16px" } }
}

/* generated */
:root {
  --color-action-primary: #1D4EB5;
  --space-4: 16px;
}
[data-theme="dark"] {
  --color-action-primary: #8EB5FF;      /* same name, dark value */
}

/* components: names only, never raw values */
.button { background: var(--color-action-primary); padding: var(--space-2) var(--space-4); }
"""),
    tools="tools: Style Dictionary, Tokens Studio for Figma, Figma Variables, Theo, Terrazzo (DTCG), Tailwind theme config, Panda CSS / vanilla-extract themes; Stylelint rules to ban raw colour values.",
    gains=["<b>One change updates everything</b>: rebrands in hours.",
           "<b>Themes and dark mode</b> become value swaps.",
           "<b>Consistency</b> across web, iOS, Android and Figma.",
           "<b>Shared vocabulary</b> between design and code.",
           "<b>Accessible contrast</b> checked once, at the token level."],
    losses=["<b>Upfront audit and naming</b> work.",
            "<b>Naming is hard</b>: too many tokens or vague names.",
            "<b>Build tooling</b> to maintain.",
            "<b>Governance</b>: someone must own and review changes."],
    baseline="Each line compares <b>raw values copied into components</b> to the same UI built on <b>design tokens</b>.",
    ratings=[(3, 4, "Names explain intent better than hex codes."),
             (2, 5, "Same tokens across products, platforms and brands."),
             (3, 4, "Contrast and theme tests run on tokens."),
             (1, 5, "A rebrand or theme is a token change."),
             (3, 3, "Neutral (CSS variables are cheap)."),
             (3, 3, "Neutral."),
             (2, 4, "Contrast-checked pairs; themes like high contrast become possible."),
             (3, 4, "Autocomplete names instead of hunting hex codes."),
             (2, 5, "Every team and micro-frontend speaks the same design language.")],
    pitfalls=[("Naming by looks", "<code>color-blue</code> used for buttons, so the rebrand to green leaves a token called blue that's green.", "semantic names by purpose (<code>action-primary</code>)."),
              ("Components using primitives", "Buttons reference <code>blue-600</code> directly, so dark mode can't remap them.", "components use semantic tokens only."),
              ("Token explosion", "3,000 tokens, many used once, so nobody can find the right one.", "start small; add tokens when a decision repeats."),
              ("Raw values sneaking back", "A quick fix hard-codes <code>#333</code> and it spreads.", "lint for raw colours and sizes in CI.")],
    use=["More than one product, platform, brand or theme.",
         "Dark mode or high-contrast themes are needed.",
         "A design system is shared by several teams.",
         "Designers and developers keep drifting apart."],
    skip=["A small one-off site with a handful of styles (plain CSS variables are enough).",
          "Prototypes where the design isn't settled yet (add tokens when it stabilises)."],
    related=["<b>Headless components</b>", "<b>Compound components</b>", "<b>Micro-frontends</b>", "<b>Container &amp; presentational</b>"],
    quiz=[("Primitive vs semantic token?", "A primitive holds a raw value in a scale (blue-600); a semantic token names its purpose (color-action-primary) and points to a primitive."),
          ("Why should components avoid primitive tokens?", "Themes remap semantic tokens; components using primitives can't change with the theme."),
          ("How does dark mode work with tokens?", "The dark theme assigns different values to the same semantic token names."),
          ("What tool turns one token file into CSS, iOS and Android outputs?", "Style Dictionary (or similar tools like Terrazzo / Theo).")],
    remember="Paint by <span class=\"hl\">name</span>, never by hex. Change the swatch once and the whole house follows.",
    sources=["W3C Design Tokens Community Group, “Design Tokens Format Module”.",
             "Style Dictionary docs.",
             "Salesforce, “Living Design System” (origins of design tokens).",
             "Nathan Curtis, “Naming Tokens in Design Systems”."],
)

# ------------------------------------------------------------------ 15 Error Boundaries
eb_problem = Doodle(760, 260, "Doodle of a dashboard page where one small widget, a recommendations panel, throws an error because an API returned null. Without boundaries the whole React tree unmounts and the user sees a blank white page instead of the rest of the working dashboard.",
                    "One widget throws, the whole tree unmounts, and the user gets a blank white page.")
eb_problem.box(20, 30, 330, 200, None, "paper")
for i, (t, x, y, w) in enumerate([("header", 40, 50, 290), ("orders", 40, 100, 140), ("stats", 190, 100, 140)]):
    eb_problem.box(x, y, w, 40, t, "green", size=16, rx=4)
eb_problem.box(40, 156, 290, 54, "recs: null.map() ✗", "pink", stroke="red", size=16, rx=4)
eb_problem.arrow(356, 130, 440, 130, color="red")
eb_problem.box(446, 30, 290, 200, None, "paper", dash=True)
eb_problem.note(591, 130, "(blank white page)", "red")
eb_problem.note(591, 252, "everything gone for one widget", "red")

eb_analogy = Doodle(760, 250, "Doodle of a theatre stage. When one actor forgets their lines in a scene, the understudy steps in for that scene and the curtain stays up; the rest of the play goes on.",
                    "One actor stumbles; the understudy covers that scene and the show goes on.")
eb_analogy.icon("curtain", 40, 30, 2.4)
eb_analogy.box(260, 60, 200, 80, "scene 3", "pink", sub="actor forgot lines", stroke="red")
eb_analogy.arrow(466, 100, 560, 100)
eb_analogy.note(560, 172, "understudy steps in", "pen")
eb_analogy.box(566, 60, 170, 80, "scene 3", "green", sub="covered ✓")
eb_analogy.note(400, 220, "the rest of the play carries on", "green")

eb_how = Doodle(760, 300, "Error boundaries placed around regions. An app-level boundary shows a full-page error as a last resort. Route-level boundaries protect each page. Widget-level boundaries wrap risky widgets such as recommendations, so when that widget throws, only it is replaced by a small fallback with a retry button, and the error is reported to monitoring.",
                "Boundaries at app, route and widget level: a crash is caught by the nearest one.")
eb_how.box(20, 20, 720, 260, None, "paper", dash=True)
eb_how.note(120, 46, "app boundary (last resort)", "pen", size=18)
eb_how.box(40, 60, 680, 200, None, "paper", dash=True)
eb_how.note(150, 86, "route boundary", "pen", size=18)
eb_how.box(60, 100, 300, 140, "orders", "green")
eb_how.box(380, 100, 320, 140, None, "pink", stroke="red", dash=True)
eb_how.head(540, 130, "widget boundary", size=16)
eb_how.text(540, 166, "“Recommendations unavailable”", size=15)
eb_how.box(480, 186, 120, 36, "Retry", "y", size=15, rx=6)
eb_how.note(640, 292, "+ report to monitoring", "pen")

BOUNDARIES = dict(
    slug="error-boundaries",
    kicker="a.k.a. “the understudy”",
    tldr="Wrap regions of the UI in <b>error boundaries</b>: components that <b>catch rendering errors</b> in their children, show a <b>fallback</b> for just that region (with a retry), and <b>report</b> the error. One broken widget no longer turns the whole page white.",
    chips=[("Family", "resilience"), ("Mechanism", "React error boundaries, Vue onErrorCaptured, Angular ErrorHandler"), ("Frameworks", "Next.js error.tsx, React Router errorElement"), ("Pairs with", "code splitting, micro-frontends")],
    problem="""  <p class="lead">In React, an error thrown while rendering <span class="hl-pink">unmounts the entire tree</span> by default. The user sees a blank page, even if only one small widget was broken.</p>
  <ul>
    <li>An API returns <code>null</code> where an array was expected, and the recommendations panel throws.</li>
    <li>The whole dashboard disappears, including the parts that worked.</li>
    <li>A lazy chunk fails to download after a deploy, and the app is gone.</li>
    <li>Nobody knows it happened unless users complain.</li>
  </ul>""",
    problem_figs=[eb_problem],
    analogy_side="the theatre understudy",
    analogy="""  <p>In a theatre, if one actor forgets their lines, the <b>understudy</b> steps in for that scene. The curtain doesn't come down and the audience doesn't go home. The stage manager notes what happened for later.</p>
  <ul>
    <li>The problem is <b>contained</b> to one scene.</li>
    <li>The cover is simpler than the original performance: a <b>fallback UI</b>.</li>
    <li>Only if the whole theatre loses power does the show stop: the <b>app-level boundary</b>.</li>
  </ul>""",
    analogy_figs=[eb_analogy],
    map=[("An actor forgetting their lines", "A component throwing while rendering"),
         ("The understudy covering the scene", "The boundary's fallback UI"),
         ("The rest of the play continuing", "Other regions keep working"),
         ("Stage manager's notes", "Error reported to monitoring"),
         ("Power cut: show stops", "Top-level boundary: full-page error screen")],
    how_side="catch close to the problem",
    how="""  <p>Place boundaries in <b>layers</b>: one at the app root (last resort), one per route, and around risky or optional widgets (third-party embeds, recommendations, charts, lazy chunks).</p>""",
    how_figs=[eb_how],
    steps=[("Add a root boundary", "A friendly full-page error with a reload button, so users never see a white screen."),
           ("Add route boundaries", "Frameworks make this easy (<code>error.tsx</code>, <code>errorElement</code>); navigation and layout stay usable."),
           ("Wrap risky widgets", "Optional features get small inline fallbacks: “Recommendations unavailable. Retry”."),
           ("Offer recovery", "A retry resets the boundary (and refetches data); reset automatically when the route or key changes."),
           ("Report every catch", "Send the error and component stack to monitoring (Sentry, Datadog) with release info.")],
    vocab=[("Error boundary", "Component that catches errors in its children's rendering."),
           ("Fallback UI", "What's shown instead of the crashed region."),
           ("Reset keys", "Values that reset the boundary when they change."),
           ("Component stack", "Which components led to the error."),
           ("Graceful degradation", "Losing a feature instead of the whole page."),
           ("Event handler errors", "Not caught by boundaries; handle with try/catch.")],
    code=dict(file="Dashboard.tsx", note="react-error-boundary", src="""
function WidgetFallback({ resetErrorBoundary }: FallbackProps) {
  return (
    <div role="alert" className="widget-error">
      <p>Recommendations are unavailable right now.</p>
      <button onClick={resetErrorBoundary}>Try again</button>
    </div>
  );
}

export function Dashboard() {
  const { reset } = useQueryErrorResetBoundary();       // also refetch on retry
  return (
    <main className="dashboard">
      <Orders />
      <Stats />
      <ErrorBoundary FallbackComponent={WidgetFallback} onReset={reset}
                     onError={(error, info) => monitoring.capture(error, { extra: info })}>
        <Recommendations />                               {/* if this throws, only this box changes */}
      </ErrorBoundary>
    </main>
  );
}
"""),
    tools="tools: react-error-boundary, Next.js error.tsx / global-error.tsx, React Router errorElement, Vue onErrorCaptured, Angular ErrorHandler, Svelte +error.svelte; report to Sentry, Datadog RUM, Bugsnag.",
    gains=["<b>No more white screens</b>: failures stay local.",
           "<b>Users keep working</b> with the rest of the page.",
           "<b>Recovery</b> through retry without a full reload.",
           "<b>Visibility</b>: every caught error is reported."],
    losses=["<b>Doesn't catch everything</b>: event handlers, async code, SSR need their own handling.",
            "<b>Can hide bugs</b> if fallbacks aren't monitored.",
            "<b>Design work</b> for many fallback states.",
            "<b>Too many boundaries</b> clutter the tree."],
    baseline="Each line compares an app with <b>no error boundaries</b> (one error = blank page) to the same app with <b>layered boundaries</b>.",
    ratings=[(4, 4, "A wrapper component; easy to understand."),
             (3, 4, "One boundary + fallback component reused everywhere."),
             (3, 4, "Easy to test: render a child that throws."),
             (3, 4, "Failures are isolated and reported with context."),
             (3, 3, "Neutral."),
             (3, 3, "Tiny (a few hundred bytes)."),
             (2, 4, "Fallbacks with role=alert beat a blank page."),
             (3, 4, "Errors are visible and recoverable in dev and prod."),
             (3, 4, "A team's broken widget doesn't take down others' pages.")],
    pitfalls=[("Expecting it to catch everything", "An error in an onClick handler or a promise isn't caught, and nothing happens.", "try/catch in handlers, error states from data libraries, and a global unhandledrejection reporter."),
              ("Only one boundary at the root", "Any error still wipes the whole page, just with a nicer message.", "add route and widget boundaries."),
              ("Fallbacks that hide problems", "Errors are caught but never reported, so the widget has been broken for weeks.", "report every caught error with release info."),
              ("No way to recover", "The fallback stays until a full reload.", "retry buttons and reset keys tied to route/data changes.")],
    use=["Every React app (at least a root and route boundaries).",
         "Optional or risky widgets: third-party embeds, recommendations, charts.",
         "Lazy-loaded chunks and micro-frontends.",
         "Dashboards with many independent panels."],
    skip=["Wrapping every tiny component (too fine-grained to be useful).",
          "Expected states like “no results” or validation errors: render them normally.",
          "Errors you can handle where they happen (handlers, data hooks)."],
    related=["<b>Code splitting</b>", "<b>Micro-frontends</b>", "<b>Circuit breaker</b> (Vol. 1)", "<b>Bulkhead</b> (Vol. 1)"],
    quiz=[("What do error boundaries catch, and what not?", "They catch errors during rendering, lifecycle methods and constructors of their children; not errors in event handlers, async code (like setTimeout or promises) or server rendering."),
          ("Where should you place boundaries?", "At the app root, per route, and around risky or optional widgets."),
          ("How does a user recover from a caught error?", "A retry button that resets the boundary (and refetches data), or automatic reset when the route or key changes."),
          ("Which Vol. 1 pattern is the backend cousin of this?", "Bulkhead (and circuit breaker): contain failures so one part can't take down everything.")],
    remember="One stumble shouldn't <span class=\"hl\">drop the curtain</span>. Cover the scene, note it down, and let the show go on.",
    sources=["React docs, “Catching rendering errors with an error boundary”.",
             "react-error-boundary (Brian Vaughn) docs.",
             "Next.js docs, “Error Handling”.",
             "Kent C. Dodds, “Use react-error-boundary to handle errors in React”."],
)

NOTES = [MICRO, TOKENS, BOUNDARIES]
