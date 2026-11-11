# Vol. 2 · Rendering & performance: SSR & Hydration, Islands, Code Splitting & Lazy Loading, List Virtualization.

# ------------------------------------------------------------------ 09 SSR & Hydration
ssr_problem = Doodle(760, 280, "Doodle of a client-side rendered page loading on a phone. The server sends an empty div and a 900 kilobyte JavaScript bundle. For 3.5 seconds the user sees a blank white screen while the bundle downloads, parses and fetches data. Search engine crawlers and link previews also see an empty page.",
                    "Client-only rendering: an empty page until all the JavaScript has downloaded, run and fetched data.")
ssr_problem.box(20, 30, 220, 200, None, "paper")
ssr_problem.head(130, 60, "index.html", size=18)
ssr_problem.text(130, 110, "<div id=\"root\">", size=16)
ssr_problem.text(130, 136, "</div>", size=16)
ssr_problem.text(130, 180, "app.js · 900 kB", size=16)
ssr_problem.line("M260 140 H720", color="soft")
for x, lab in [(270, "download"), (420, "parse + run"), (560, "fetch data")]:
    ssr_problem.box(x, 110, 136, 50, lab, "pink", size=15, rx=6)
ssr_problem.note(490, 90, "blank white screen for 3.5 s", "red")
ssr_problem.note(490, 200, "crawlers & link previews: empty page too", "red")

ssr_analogy = Doodle(760, 250, "Doodle of a lamp delivered already assembled. It looks finished the moment the box is opened, so you can see it straight away, but it only works once you plug it in. Plugging in is hydration.",
                    "The lamp arrives assembled, so it looks done at once. It works once you plug it in.")
ssr_analogy.icon("parcel", 40, 90, 1.6)
ssr_analogy.note(90, 210, "delivered assembled")
ssr_analogy.arrow(140, 130, 260, 130, label="open box", lx=200, ly=118)
ssr_analogy.icon("lamp", 280, 60, 2.2)
ssr_analogy.note(340, 230, "looks finished (HTML)")
ssr_analogy.arrow(420, 130, 540, 130, label="plug in", lx=480, ly=118)
ssr_analogy.icon("plug", 560, 90, 1.8)
ssr_analogy.note(620, 230, "now it works (hydrated)", "green")

ssr_how = Doodle(760, 300, "SSR timeline. The server fetches data and renders the page to HTML. The browser shows that HTML quickly: first contentful paint at about 1 second. Meanwhile JavaScript downloads; hydration attaches event handlers to the existing HTML, and the page becomes interactive at about 2.5 seconds. Between the two, the page is visible but not yet clickable.",
                    "HTML shows content early; hydration makes it interactive later. Mind the gap in between.")
ssr_how.box(20, 40, 220, 70, "server", "y", sub="fetch data → render HTML")
ssr_how.arrow(246, 75, 330, 75, label="HTML", lx=288, ly=63)
ssr_how.line("M330 170 H740", color="soft")
ssr_how.box(340, 140, 150, 56, "content visible", "green", size=16, rx=6)
ssr_how.box(500, 140, 120, 56, "JS loads", "paper", size=16, rx=6)
ssr_how.box(630, 140, 110, 56, "hydrate", "y", size=16, rx=6)
ssr_how.note(415, 230, "FCP ≈ 1.0 s", "green")
ssr_how.note(685, 230, "TTI ≈ 2.5 s", "pen")
ssr_how.note(560, 270, "the uncanny valley: visible, not clickable yet", "red")

SSR = dict(
    slug="ssr-hydration",
    kicker="a.k.a. “send the page, then wake it up”",
    tldr="Render the page to <b>HTML on the server</b> (with its data) so the browser can <b>show content immediately</b>, and search engines and link previews see it. Then the same JavaScript runs in the browser and <b>hydrates</b> the HTML: it attaches event handlers and state so the page becomes <b>interactive</b>.",
    chips=[("Family", "rendering strategy"), ("Frameworks", "Next.js, Remix/React Router, Nuxt, SvelteKit, Angular SSR"), ("Variants", "streaming SSR, partial/progressive hydration"), ("Pairs with", "code splitting, islands, server-state cache")],
    problem="""  <p class="lead">A purely <b>client-side rendered</b> (CSR) app sends an almost empty HTML file and a large JavaScript bundle. Nothing appears until the JS has <span class="hl-pink">downloaded, run and fetched data</span>.</p>
  <ul>
    <li>On a mid-range phone and 4G, that's a blank screen for several seconds.</li>
    <li>Search crawlers and social link previews may see an empty page.</li>
    <li>Core Web Vitals (LCP) suffer, and so do conversions.</li>
  </ul>""",
    problem_figs=[ssr_problem],
    analogy_side="the lamp delivered assembled",
    analogy="""  <p>Some furniture shops deliver a lamp <b>already assembled</b>. The moment you open the box, it looks finished and you can put it where it belongs. It doesn't light up until you <b>plug it in</b>.</p>
  <ul>
    <li>Assembled in the warehouse: <b>rendered on the server</b>.</li>
    <li>Plugging in: <b>hydration</b> makes it work.</li>
    <li>If you press the switch before plugging in, nothing happens: the <b>gap between visible and interactive</b>.</li>
  </ul>""",
    analogy_figs=[ssr_analogy],
    map=[("Assembled in the warehouse", "HTML rendered on the server"),
         ("Opening the box: it looks done", "First contentful paint"),
         ("Plugging it in", "Hydration attaches handlers and state"),
         ("Switch does nothing before plugging in", "Visible but not yet interactive"),
         ("Same lamp, same parts", "Same components run on server and client")],
    how_side="render on the server, hydrate in the browser",
    how="""  <p>The server runs your components with real data and streams HTML. The browser paints it, downloads the JS, and React (or Vue, Svelte…) <b>re-runs the components</b> to attach to the existing DOM instead of rebuilding it.</p>""",
    how_figs=[ssr_how],
    steps=[("Fetch on the server", "Load data in a loader / server component so it's ready before HTML is sent."),
           ("Render to HTML (and stream it)", "Send the shell first and stream slower sections as they resolve (Suspense), so the top of the page appears fast."),
           ("Embed the data", "Serialise the data the client needs so hydration doesn't refetch it."),
           ("Hydrate", "The client renders the same tree and attaches event handlers. Output must match the server's HTML exactly."),
           ("Shrink the gap", "Ship less JS, hydrate important parts first, and avoid layout shifts while JS loads.")],
    vocab=[("CSR", "Client-side rendering: the browser builds the page with JS."),
           ("SSR", "Server-side rendering per request."),
           ("Hydration", "Attaching client JS to server-rendered HTML."),
           ("Hydration mismatch", "Client render differs from the server HTML."),
           ("FCP / LCP", "First / Largest Contentful Paint."),
           ("TTI / INP", "Time to Interactive / Interaction to Next Paint.")],
    code=dict(file="app/orders/page.tsx", note="Next.js App Router", src="""
// runs on the server: data + HTML, no client JS for this part
export default async function OrdersPage() {
  const orders = await db.order.findMany({ take: 20, orderBy: { createdAt: "desc" } });
  return (
    <main>
      <h1>Your orders</h1>
      <OrderTable orders={orders} />                 {/* plain HTML from the server */}
      <Suspense fallback={<p>Loading suggestions…</p>}>
        <Suggestions />                               {/* streamed in when ready */}
      </Suspense>
      <ReorderButton lastOrderId={orders[0]?.id} />  {/* "use client": hydrated */}
    </main>
  );
}

// ReorderButton.tsx
"use client";
export function ReorderButton({ lastOrderId }: { lastOrderId?: string }) {
  const [pending, start] = useTransition();
  return <button disabled={pending} onClick={() => start(() => reorder(lastOrderId))}>Reorder</button>;
}
"""),
    tools="frameworks: Next.js, React Router v7 (Remix), Nuxt, SvelteKit, SolidStart, Angular SSR, Astro; measure with Lighthouse, WebPageTest and the Chrome UX Report.",
    gains=["<b>Fast first paint</b> and better LCP.",
           "<b>SEO and link previews</b> see real content.",
           "<b>Works before JS</b> for reading (and forms, with progressive enhancement).",
           "<b>Data fetched close to the database</b>, not over slow mobile networks."],
    losses=["<b>Server cost and complexity</b>: a Node/edge server per request.",
            "<b>Hydration cost</b>: all that JS still runs on the client.",
            "<b>The uncanny valley</b>: visible but not yet clickable.",
            "<b>Hydration mismatches</b> (dates, random ids, window checks)."],
    baseline="Each line compares a <b>client-side rendered SPA</b> to the same app with <b>server-side rendering + hydration</b>.",
    ratings=[(4, 3, "Two environments (server and browser) to reason about."),
             (3, 3, "Neutral; components are shared."),
             (3, 3, "Need tests for server rendering and mismatches."),
             (3, 3, "Framework conventions help; server/client boundaries add rules."),
             (2, 4, "Much faster first content; interactivity depends on JS size."),
             (3, 3, "Same JS still ships for hydration (server components help)."),
             (3, 4, "Real HTML early; works better with assistive tech and slow devices."),
             (3, 3, "Great frameworks, but more concepts and build config."),
             (3, 3, "Neutral.")],
    pitfalls=[("Hydration mismatches", "<code>new Date()</code> or <code>Math.random()</code> renders differently on server and client, and React throws away the HTML.", "compute such values once on the server and pass them down, or render them only after mount."),
              ("SSR with a giant bundle", "Content shows at 1 s but buttons don't work until 6 s.", "code splitting, server components, islands for mostly static pages."),
              ("Accessing window on the server", "<code>window is not defined</code> crashes the render.", "browser-only code in effects or client components."),
              ("Slow data blocks the whole page", "One slow API delays the entire HTML.", "stream with Suspense; show the shell first.")],
    use=["Public pages where SEO, link previews or first paint matter (shops, content, marketing).",
         "Users on slow devices and networks.",
         "Data that's close to the server (database, internal APIs).",
         "You already use a framework that supports it."],
    skip=["Apps behind a login where SEO doesn't matter and users are on fast machines (internal dashboards).",
          "Mostly static content: pre-render at build time or use islands instead.",
          "You can't run or afford servers (static hosting only)."],
    related=["<b>Islands architecture</b>", "<b>Code splitting</b>", "<b>Server-state cache</b>", "<b>Container &amp; presentational</b> (server vs client)"],
    quiz=[("What does hydration do?", "It runs the components in the browser and attaches event handlers and state to the server-rendered HTML instead of rebuilding the DOM."),
          ("What causes a hydration mismatch?", "The client's first render differs from the server HTML, e.g. using dates, random values or window-only checks during render."),
          ("Does SSR reduce the JavaScript users download?", "Not by itself; the same components still hydrate. Server components, islands and code splitting reduce it."),
          ("What is the “uncanny valley” of SSR?", "The time when content is visible but not yet interactive because JS hasn't hydrated.")],
    remember="Deliver it <span class=\"hl\">assembled</span>, then <span class=\"hl\">plug it in</span> fast. Visible early is great; clickable soon after is the goal.",
    sources=["patterns.dev, “Server-side Rendering” and “Progressive Hydration”.",
             "web.dev, “Rendering on the Web” (Jason Miller &amp; Addy Osmani).",
             "React docs, “Server Components” and “hydrateRoot”.",
             "Next.js docs, “Rendering”."],
)

# ------------------------------------------------------------------ 10 Islands Architecture
is_problem = Doodle(760, 260, "Doodle of a blog article page that is 95 percent static text and images, with just a newsletter signup form and a like button that need JavaScript. A full single-page-app framework still ships and hydrates 400 kilobytes of JavaScript for the whole page.",
                    "Hydrating the whole page because two small parts need JavaScript.")
is_problem.box(20, 20, 380, 220, None, "paper")
is_problem.head(210, 50, "Blog article", size=19)
for i in range(5):
    is_problem.line(f"M50 {80 + i * 22} H{370 - (i % 2) * 60}", thin=True, color="soft")
is_problem.box(50, 192, 150, 34, "♥ like", "y", size=15, rx=6)
is_problem.box(220, 192, 150, 34, "signup form", "y", size=15, rx=6)
is_problem.arrow(410, 130, 480, 130, color="red")
is_problem.box(490, 80, 250, 100, "hydrate EVERYTHING", "pink", sub="400 kB JS", stroke="red")
is_problem.note(615, 220, "for 2 tiny interactive bits ✗", "red")

is_analogy = Doodle(760, 262, "Doodle of a museum room. Most exhibits are framed paintings that just hang there and need no power. A couple of interactive screens are plugged into their own sockets. Nobody wires the paintings.",
                    "Paintings just hang there. Only the interactive exhibits get their own power socket.")
for i, x in enumerate([30, 190, 510]):
    is_analogy.icon("frame", x, 60, 2.0)
is_analogy.icon("screen", 350, 60, 2.0)
is_analogy.icon("plug", 390, 160, 1.0)
is_analogy.icon("screen", 670, 60, 1.2)
is_analogy.note(160, 250, "static paintings: no power needed")
is_analogy.note(560, 250, "interactive exhibits: own socket", "green")

is_how = Doodle(760, 300, "Islands architecture. The server sends plain HTML for the whole page: header, article text and footer, with zero JavaScript. Two islands, a like button and a newsletter form, each load their own small script. The like button hydrates when it becomes visible; the form hydrates when the browser is idle.",
                "A sea of static HTML with small, independent islands of interactivity.")
is_how.box(20, 20, 720, 260, None, "blue")
is_how.head(36, 52, "static HTML · 0 kB JS", anchor="start", size=17)
is_how.box(50, 70, 660, 40, "header", "paper", size=16, rx=4)
for i in range(4):
    is_how.line(f"M60 {140 + i * 20} H{640 - (i % 2) * 120}", thin=True, color="soft")
is_how.box(60, 220, 220, 44, "♥ island · 3 kB", "y", size=16, rx=8)
is_how.box(420, 220, 280, 44, "signup island · 6 kB", "y", size=16, rx=8)
is_how.note(170, 210, "client:visible", "pen")
is_how.note(560, 210, "client:idle", "pen")

ISLANDS = dict(
    slug="islands",
    kicker="a.k.a. “static sea, interactive islands”",
    tldr="Render the page as <b>plain HTML</b> (at build time or on the server) with <b>no JavaScript by default</b>. Mark only the interactive parts as <b>islands</b>; each one loads and hydrates <b>its own small script</b>, independently, often only when it's visible or the browser is idle.",
    chips=[("Family", "rendering strategy"), ("Coined by", "Katie Sylor-Miller, popularised by Jason Miller (2020)"), ("Frameworks", "Astro, Fresh, Eleventy + is-land"), ("Pairs with", "SSR, code splitting, design tokens")],
    problem="""  <p class="lead">Content sites (blogs, docs, marketing, shops' product pages) are mostly static. Yet many are built as single-page apps that ship and hydrate <span class="hl-pink">JavaScript for the entire page</span>.</p>
  <ul>
    <li>An article with one like button ships 400 kB of framework code.</li>
    <li>Phones spend seconds parsing and running JS for paragraphs that never change.</li>
    <li>One heavy widget delays interactivity for everything else.</li>
  </ul>""",
    problem_figs=[is_problem],
    analogy_side="the museum room",
    analogy="""  <p>In a museum, most exhibits are <b>paintings</b>: they hang on the wall and need nothing. A few exhibits are <b>interactive screens</b>, each plugged into its own socket. Nobody runs power cables to the paintings, and if one screen breaks, the rest of the room is fine.</p>""",
    analogy_figs=[is_analogy],
    map=[("Paintings on the wall", "Static HTML: zero JavaScript"),
         ("An interactive screen", "An island component"),
         ("Its own power socket", "Its own small script, hydrated independently"),
         ("Switched on when a visitor walks up", "Hydrate on visible / on idle / on interaction"),
         ("One broken screen, room still fine", "Islands fail and load independently")],
    how_side="opt in to JavaScript, island by island",
    how="""  <p>The framework renders every component to HTML. Only components you mark get their JS shipped, and you choose <b>when</b> each hydrates.</p>""",
    how_figs=[is_how],
    steps=[("Default to zero JS", "Every component renders to HTML; nothing hydrates unless asked."),
           ("Mark the islands", "<code>&lt;LikeButton client:visible /&gt;</code>, <code>&lt;SignupForm client:idle /&gt;</code>."),
           ("Choose a hydration trigger", "load (now), idle (when the browser is free), visible (scrolled into view), media (on a breakpoint)."),
           ("Keep islands small and independent", "Pass serialisable props; share state through tiny stores or custom events, not a global app tree."),
           ("Mix frameworks if needed", "Islands can even use different UI libraries on one page (sparingly).")],
    vocab=[("Island", "An interactive component hydrated on its own."),
           ("Partial hydration", "Hydrating only some components on a page."),
           ("Progressive hydration", "Hydrating parts over time, by priority."),
           ("Client directive", "Astro's <code>client:*</code> attribute that controls hydration."),
           ("MPA", "Multi-page app: each navigation loads a new HTML page."),
           ("View transitions", "Browser API for smooth animations between pages.")],
    code=dict(file="src/pages/blog/[slug].astro", note="Astro", src="""
---
import Layout from "../../layouts/Layout.astro";
import LikeButton from "../../components/LikeButton.tsx";
import SignupForm from "../../components/SignupForm.svelte";
const { post } = Astro.props;
---
<Layout title={post.title}>
  <article>
    <h1>{post.title}</h1>
    <Fragment set:html={post.html} />          <!-- static: 0 kB JS -->
  </article>

  <LikeButton client:visible postId={post.id} />  <!-- hydrates when scrolled into view -->
  <SignupForm client:idle />                      <!-- hydrates when the browser is idle -->
</Layout>
"""),
    tools="frameworks: Astro, Fresh (Deno), Eleventy with is-land, Marko, Qwik (resumability, a cousin idea), Enhance; React Server Components share the “ship less JS” goal.",
    gains=["<b>Tiny JS bundles</b> for content pages.",
           "<b>Fast load and interaction</b>, even on cheap phones.",
           "<b>Independent islands</b>: one slow widget doesn't block others.",
           "<b>Great SEO and accessibility</b> from real HTML.",
           "<b>Use the right tool per island</b>."],
    losses=["<b>Sharing state between islands</b> is awkward.",
            "<b>Not for app-like UIs</b> where most of the page is interactive.",
            "<b>Full page loads</b> on navigation (mitigated with view transitions).",
            "<b>Another mental model</b>: what runs where, and when."],
    baseline="Each line compares a content site built as a <b>fully hydrated SPA</b> to the same site using <b>islands</b>.",
    ratings=[(3, 4, "Most of the page is just HTML."),
             (3, 4, "Islands are self-contained and portable."),
             (3, 4, "Static parts need little testing; islands test in isolation."),
             (3, 4, "Changing one island doesn't affect the rest."),
             (2, 5, "Little JS to download, parse and run."),
             (2, 5, "Often 90%+ less JavaScript."),
             (3, 4, "Real HTML, works before (and without) JS."),
             (3, 4, "Simple pages, fast builds; cross-island state is the hard bit."),
             (3, 4, "Teams can own islands independently.")],
    pitfalls=[("Building an app as islands", "A dashboard with 40 interacting widgets turns into 40 islands passing events around.", "use an SPA/SSR framework for app-like UIs."),
              ("Everything client:load", "Every island hydrates immediately, and you're back to a heavy page.", "default to visible or idle; load only above-the-fold essentials."),
              ("Shared state through globals", "Islands poke each other's DOM or window variables.", "a tiny shared store (nanostores) or custom events with clear contracts."),
              ("Huge island props", "The whole post object is serialised into every island.", "pass ids and the few fields the island needs.")],
    use=["Content-heavy sites: blogs, docs, marketing, product pages.",
         "Mostly static pages with a few interactive widgets.",
         "Performance on low-end devices matters.",
         "Teams that want to mix or migrate UI frameworks."],
    skip=["Highly interactive apps (editors, dashboards, chat).",
          "Lots of shared client state across the page.",
          "You need SPA-style instant navigations everywhere."],
    related=["<b>SSR &amp; hydration</b>", "<b>Code splitting</b>", "<b>Micro-frontends</b>", "<b>Design tokens</b>"],
    quiz=[("What is an island?", "An interactive component on an otherwise static HTML page that loads and hydrates its own JavaScript independently."),
          ("What's partial hydration?", "Hydrating only the components that need interactivity instead of the whole page."),
          ("Name two hydration triggers.", "On load, on idle, on visible (in viewport), on media query, or on interaction."),
          ("When are islands a poor fit?", "App-like UIs where most of the page is interactive and shares state.")],
    remember="Most of the page is a <span class=\"hl\">painting</span>. Only wire up the <span class=\"hl\">screens</span>, and switch them on when someone walks up.",
    sources=["Jason Miller, “Islands Architecture” (jasonformat.com).",
             "Astro docs, “Islands architecture” and “Template directives”.",
             "patterns.dev, “Islands Architecture”.",
             "Deno Fresh docs, “Islands”."],
)

# ------------------------------------------------------------------ 11 Code Splitting & Lazy Loading
cs_problem = Doodle(760, 260, "Doodle of a single 2.4 megabyte JavaScript bundle containing the home page, the admin panel, the chart library, the rich text editor and the PDF exporter. A visitor who only wants the home page downloads all of it.",
                    "One giant bundle: every visitor downloads every feature, even the ones they'll never open.")
cs_problem.box(20, 30, 400, 200, None, "pink", stroke="red")
cs_problem.head(220, 60, "app.js · 2.4 MB", size=20, color="red")
for i, (t, w) in enumerate([("home", 80), ("admin panel", 150), ("charts lib", 130), ("rich-text editor", 170), ("PDF export", 120)]):
    cs_problem.box(40 + (i % 2) * 190, 80 + (i // 2) * 48, w, 36, t, "paper", size=15, rx=4)
cs_problem.arrow(426, 130, 520, 130, color="red")
cs_problem.icon("phone", 530, 80, 1.6)
cs_problem.note(690, 110, "only wanted", "pen")
cs_problem.note(690, 134, "the home page", "pen")
cs_problem.note(560, 220, "6 s on 4G before anything works", "red")

cs_analogy = Doodle(760, 250, "Doodle of a TV streaming episodes. Instead of downloading the whole season before watching, you stream episode 1 now; the next episode loads while you watch, and you never download the episodes you don't watch.",
                    "Stream the episode you're watching now; fetch the next one just before you need it.")
cs_analogy.icon("tv", 60, 50, 2.0)
cs_analogy.note(130, 200, "episode 1: now")
for i, t in enumerate(["ep. 2 · next", "ep. 3", "ep. 4 … 10"]):
    cs_analogy.box(300 + i * 150, 70, 140, 60, t, "y" if i == 0 else "paper", size=15, dash=i > 0)
cs_analogy.note(450, 170, "only fetched if you keep watching", "pen")
cs_analogy.note(450, 230, "nobody downloads the whole season first", "green")

cs_how = Doodle(760, 300, "Code splitting. The bundler splits the app into a small entry chunk with the shell and home route, plus separate chunks for the admin route, the chart library and the editor. The home page loads only the entry chunk. Opening the admin route fetches its chunk on demand, and hovering a link prefetches the next chunk.",
                "Split by route and by heavy feature; load each chunk when it's needed (or about to be).")
cs_how.box(20, 100, 200, 90, "entry.js · 120 kB", "green", sub="shell + home")
for i, (t, trig) in enumerate([("admin.js · 300 kB", "on route /admin"), ("charts.js · 180 kB", "when chart scrolls in"), ("editor.js · 420 kB", "when “Edit” is clicked")]):
    y = 20 + i * 92
    cs_how.box(470, y, 260, 64, t, "y", size=16)
    cs_how.arrow(226, 145, 464, y + 32, dash=True, label=trig, lx=455, ly=(y + 16) if i < 2 else (y + 62), anchor="end")
cs_how.note(120, 230, "loaded first", "green")
cs_how.note(120, 260, "hover a link → prefetch", "pen")

SPLIT = dict(
    slug="code-splitting",
    kicker="a.k.a. “don't download the whole season”",
    tldr="Instead of one giant JavaScript bundle, let the bundler <b>split the code into chunks</b>: one per route and per heavy feature. Load the <b>small entry chunk first</b>, and <b>lazy-load</b> the others with dynamic <code>import()</code> when the user needs them (or <b>prefetch</b> them just before).",
    chips=[("Family", "performance / loading"), ("Mechanism", "dynamic import(), React.lazy, Suspense"), ("Bundlers", "Vite / Rollup, webpack, esbuild, Turbopack"), ("Pairs with", "SSR, islands, error boundaries")],
    problem="""  <p class="lead">Bundlers combine your code into files the browser can load. By default you often get <span class="hl-pink">one big bundle</span> containing every page and every library.</p>
  <ul>
    <li>A visitor to the home page downloads the admin panel, the charting library and the rich-text editor.</li>
    <li>JS is the most expensive byte: it must be downloaded, parsed, compiled and run.</li>
    <li>One small change invalidates the whole cached bundle, so returning users download it all again.</li>
  </ul>""",
    problem_figs=[cs_problem],
    analogy_side="streaming episodes",
    analogy="""  <p>You don't download a whole TV season before watching episode 1. You <b>stream the episode you're on</b>, the next one <b>preloads</b> while you watch, and the episodes you never watch are never downloaded.</p>""",
    analogy_figs=[cs_analogy],
    map=[("The whole season", "The full application code"),
         ("Episode 1 now", "The entry chunk for the current route"),
         ("Next episode preloading", "Prefetching the next likely chunk"),
         ("Episodes you never watch", "Features the user never opens, never downloaded"),
         ("A short buffering spinner", "Suspense fallback while a chunk loads")],
    how_side="split by route and by heavy feature",
    how="""  <p>Every dynamic <code>import()</code> tells the bundler “make this a separate chunk”. Frameworks split by route automatically; you add splits for heavy, rarely used features.</p>""",
    how_figs=[cs_how],
    steps=[("Measure first", "Use a bundle analyser to see what's big and who uses it."),
           ("Split by route", "Each page gets its own chunk (frameworks do this for you)."),
           ("Lazy-load heavy features", "Editors, charts, maps, PDF export: <code>React.lazy(() =&gt; import(\"./Editor\"))</code> behind a click or when visible."),
           ("Show a fallback", "Wrap lazy parts in <code>Suspense</code> with a skeleton; wrap in an error boundary in case the chunk fails to load."),
           ("Prefetch likely next steps", "On link hover, on idle, or with <code>&lt;link rel=\"prefetch\"&gt;</code>, so the split doesn't add waiting.")],
    vocab=[("Bundle / chunk", "A file of JavaScript produced by the bundler."),
           ("Entry chunk", "The code needed to start the app."),
           ("Dynamic import", "<code>import()</code> that loads a module on demand."),
           ("Lazy loading", "Loading something only when it's needed."),
           ("Prefetch / preload", "Fetch soon-needed / needed-now resources early."),
           ("Tree shaking", "Removing unused exports at build time.")],
    code=dict(file="routes.tsx", note="React + Vite", src="""
const AdminPage = lazy(() => import("./pages/AdminPage"));          // own chunk
const RichTextEditor = lazy(() => import("./components/RichTextEditor"));

export function App() {
  return (
    <ErrorBoundary fallback={<p>Couldn't load this part. <a href="">Reload</a></p>}>
      <Suspense fallback={<PageSkeleton />}>
        <Routes>
          <Route path="/" element={<HomePage />} />                  {/* in entry chunk */}
          <Route path="/admin/*" element={<AdminPage />} />          {/* loaded on visit */}
        </Routes>
      </Suspense>
    </ErrorBoundary>
  );
}

// heavy feature behind an interaction, prefetched on hover
function EditButton() {
  const [editing, setEditing] = useState(false);
  return editing
    ? <Suspense fallback={<EditorSkeleton />}><RichTextEditor /></Suspense>
    : <button onMouseEnter={() => import("./components/RichTextEditor")} onClick={() => setEditing(true)}>Edit</button>;
}
"""),
    tools="tools: Vite / Rollup manualChunks, webpack SplitChunks, Next.js / React Router route splitting, next/dynamic, rollup-plugin-visualizer or webpack-bundle-analyzer, Lighthouse “Reduce unused JavaScript”, loading=\"lazy\" for images and iframes.",
    gains=["<b>Much smaller first load</b> and faster interactivity.",
           "<b>Better caching</b>: unchanged chunks stay cached.",
           "<b>Pay only for what you use.</b>",
           "<b>Heavy libraries isolated</b> from the main path."],
    losses=["<b>Waiting later</b>: a spinner when a chunk is first needed.",
            "<b>More requests</b> and a waterfall if chunks load chunks.",
            "<b>Chunk load failures</b> after deploys (old chunk names gone).",
            "<b>More moving parts</b> in the build."],
    baseline="Each line compares <b>one big bundle</b> to the same app <b>split by route and heavy feature</b> with lazy loading and prefetch.",
    ratings=[(4, 3, "A few Suspense boundaries and loading states to design."),
             (3, 3, "Neutral."),
             (3, 3, "Need tests for loading and chunk-failure states."),
             (3, 4, "Features are isolated; dependencies are clearer."),
             (2, 4, "Much faster first load; small delays on first use."),
             (1, 5, "Initial JS can drop by half or more."),
             (3, 3, "Announce loading states; keep focus stable when content appears."),
             (3, 3, "Frameworks automate route splitting; manual splits need care."),
             (3, 4, "Teams' features don't bloat each other's pages.")],
    pitfalls=[("Splitting too small", "Hundreds of tiny chunks cause request overhead and waterfalls.", "split at routes and genuinely heavy features."),
              ("Lazy-loading what's above the fold", "The hero component is lazy, so the main content appears later than before.", "keep first-view components in the entry chunk."),
              ("No error handling for chunk loads", "After a deploy, old tabs request deleted chunks and the app breaks.", "error boundary + reload, and keep old assets for a while."),
              ("Waterfalls", "The route chunk loads, then requests its data, then another chunk.", "preload data and chunks in parallel (route loaders, prefetch).")],
    use=["Bundles over ~200 kB of JS (compressed).",
         "Apps with many routes or rarely used heavy features.",
         "Users on mobile or slow networks.",
         "Admin areas or tools only some users open."],
    skip=["Tiny apps where the whole bundle is small.",
          "Code needed on every screen (keep it in the entry).",
          "Static content pages (islands or plain HTML ship even less)."],
    related=["<b>SSR &amp; hydration</b>", "<b>Islands architecture</b>", "<b>Error boundaries</b>", "<b>Micro-frontends</b>"],
    quiz=[("What does a dynamic import() tell the bundler?", "To put that module (and its dependencies) into a separate chunk that's loaded on demand."),
          ("Prefetch vs preload?", "Preload fetches a resource needed for the current page right away; prefetch fetches something likely needed soon at low priority."),
          ("Why wrap lazy components in an error boundary?", "Chunk downloads can fail (network or deploys), and the boundary shows a fallback instead of crashing the app."),
          ("Name something you should not lazy-load.", "Above-the-fold content or code needed on every screen.")],
    remember="Stream the <span class=\"hl\">episode</span> they're watching, preload the next one, and never make them download the <span class=\"hl\">whole season</span>.",
    sources=["web.dev, “Reduce JavaScript payloads with code splitting”.",
             "React docs, “lazy” and “Suspense”.",
             "Vite docs, “Building for Production” (chunking).",
             "patterns.dev, “Dynamic Import” and “Import On Interaction”."],
)

# ------------------------------------------------------------------ 12 List Virtualization
vl_problem = Doodle(760, 260, "Doodle of a table with 100,000 rows all rendered into the page at once. The browser creates 600,000 DOM nodes, takes 4 seconds to render, uses 900 megabytes of memory, and scrolling stutters.",
                    "Rendering 100,000 rows means 600,000 DOM nodes, most of them far off screen.")
vl_problem.box(20, 20, 300, 220, None, "paper")
for i in range(9):
    vl_problem.line(f"M30 {44 + i * 22} H310", thin=True, color="soft")
vl_problem.head(170, 236, "… 99,991 more rows", size=15)
vl_problem.arrow(326, 130, 420, 130, color="red")
vl_problem.box(426, 40, 310, 180, None, "pink", stroke="red")
for i, t in enumerate(["600,000 DOM nodes", "first render: 4 s", "memory: 900 MB", "scrolling: janky"]):
    vl_problem.text(581, 84 + i * 36, t, size=18)

vl_analogy = Doodle(760, 260, "Doodle of a train window. The track is 500 kilometres long, but through the window you only ever see a few hundred metres of landscape at a time. The view changes as the train moves, and nobody paints the whole route in front of the window.",
                    "The route is 500 km long, but through the window you only ever see a few hundred metres.")
vl_analogy.line("M20 200 H740", thin=True)
vl_analogy.line("M20 210 H740", thin=True)
for x in range(30, 740, 40):
    vl_analogy.line(f"M{x} 196 v18", thin=True, color="soft")
vl_analogy.icon("window", 320, 40, 1.8)
vl_analogy.raw('<path class="d d-green" d="M330 120 q20 -30 40 0 t40 0"/>')
vl_analogy.note(150, 120, "500 km of track…", "pen")
vl_analogy.note(600, 120, "…you see this much", "pen")
vl_analogy.note(380, 250, "view updates as you move", "green")

vl_how = Doodle(760, 320, "List virtualization. A scroll container has the full height of 100,000 rows times 40 pixels, 4 million pixels, using a spacer. Only the roughly 20 rows inside the visible window plus a small overscan above and below are rendered and absolutely positioned. As you scroll, rows are recycled to show new items.",
                "A tall empty spacer keeps the scrollbar honest; only the visible rows (+ overscan) really exist.")
vl_how.box(40, 20, 200, 280, None, "paper", dash=True)
vl_how.note(140, 14, "full height: 4,000,000 px", "pen", size=17)
vl_how.box(56, 110, 168, 120, None, "green")
for i in range(5):
    vl_how.line(f"M66 {130 + i * 22} H214", thin=True)
vl_how.note(300, 120, "← viewport: ~20 rows rendered", "green", anchor="start")
vl_how.note(300, 96, "← overscan: 5 rows", "pen", anchor="start")
vl_how.note(300, 250, "← overscan: 5 rows", "pen", anchor="start")
vl_how.box(470, 150, 270, 90, "scroll →", "y", sub="recycle rows, new items")

VIRTUAL = dict(
    slug="virtualization",
    kicker="a.k.a. “windowing”",
    tldr="When a list or table has thousands of items, <b>render only the rows that are visible</b> (plus a few extra above and below). A spacer element keeps the <b>full scroll height</b>, and as the user scrolls, rows are <b>recycled</b> to show the new items. 100,000 items, ~30 DOM rows.",
    chips=[("Family", "rendering performance"), ("Libraries", "TanStack Virtual, react-window, Virtuoso"), ("CSS cousin", "content-visibility: auto"), ("Pairs with", "server-state cache (infinite queries), debounce")],
    problem="""  <p class="lead">Browsers are fast, but not at <span class="hl-pink">hundreds of thousands of DOM nodes</span>. Logs, transactions, chat history, spreadsheets and product grids easily get there.</p>
  <ul>
    <li>Rendering 100,000 rows × 6 cells creates 600,000 elements: seconds of rendering and huge memory.</li>
    <li>Scrolling stutters because layout and paint have so much to do.</li>
    <li>Every state update re-renders the whole list.</li>
  </ul>""",
    problem_figs=[vl_problem],
    analogy_side="the train window",
    analogy="""  <p>A train route is 500 km long, but <b>through the window you only ever see a few hundred metres</b>. Nobody builds the whole landscape in front of you; the view simply changes as you move. The timetable still tells you how long the whole journey is, like the <b>scrollbar</b>.</p>""",
    analogy_figs=[vl_analogy],
    map=[("The whole 500 km route", "All 100,000 items in the data"),
         ("What you see through the window", "The rendered rows in the viewport"),
         ("A bit of track just ahead", "Overscan rows above and below"),
         ("The view changing as you move", "Rows recycled on scroll"),
         ("The timetable's total length", "A spacer giving the true scroll height")],
    how_side="render the window, fake the rest",
    how="""  <p>The virtualizer knows the scroll position and each row's size (fixed or measured), so it can calculate which items are visible and where to place them.</p>""",
    how_figs=[vl_how],
    steps=[("Give the list a scroll container", "A fixed-height element with <code>overflow: auto</code>."),
           ("Add a spacer", "An inner element with the total height (count × row height) so the scrollbar is correct."),
           ("Compute the visible range", "From <code>scrollTop</code> and row sizes, find the first and last visible index, plus overscan."),
           ("Render only those rows", "Absolutely position them (or translate them) at their offsets."),
           ("Handle variable sizes and a11y", "Measure rows that vary; keep keyboard navigation and set <code>aria-rowcount</code>/<code>aria-rowindex</code> so screen readers know the real size.")],
    vocab=[("Virtualization / windowing", "Rendering only the visible part of a long list."),
           ("Overscan", "Extra rows rendered beyond the viewport to avoid blank flashes."),
           ("Spacer", "Element that holds the full scroll height."),
           ("Dynamic measurement", "Measuring rows whose height varies."),
           ("Infinite scroll", "Loading more data as the user nears the end."),
           ("content-visibility", "CSS that lets the browser skip rendering off-screen content.")],
    code=dict(file="TransactionList.tsx", note="TanStack Virtual", src="""
export function TransactionList({ rows }: { rows: Transaction[] }) {
  const scrollRef = useRef<HTMLDivElement>(null);
  const v = useVirtualizer({
    count: rows.length,                         // 100,000
    getScrollElement: () => scrollRef.current,
    estimateSize: () => 40,                     // px per row
    overscan: 5,
  });

  return (
    <div ref={scrollRef} role="table" aria-rowcount={rows.length} style={{ height: 600, overflow: "auto" }}>
      <div style={{ height: v.getTotalSize(), position: "relative" }}>   {/* spacer */}
        {v.getVirtualItems().map((item) => (
          <div key={item.key} role="row" aria-rowindex={item.index + 1}
               style={{ position: "absolute", top: 0, width: "100%", transform: `translateY(${item.start}px)` }}>
            <TransactionRow tx={rows[item.index]} />
          </div>
        ))}
      </div>
    </div>
  );
}
"""),
    tools="libraries: TanStack Virtual, react-window / react-virtualized, React Virtuoso, vue-virtual-scroller, Angular CDK virtual scroll, AG Grid / MUI DataGrid (built in); CSS content-visibility: auto for simpler long pages.",
    gains=["<b>Constant render cost</b> no matter how many items.",
           "<b>Smooth scrolling</b> and low memory.",
           "<b>Fast first render</b> of huge lists.",
           "<b>Cheap updates</b>: only visible rows re-render."],
    losses=["<b>Find in page (Ctrl+F) misses</b> off-screen rows.",
            "<b>Accessibility work</b>: row counts, focus and keyboard need care.",
            "<b>Variable row heights</b> make scrolling jumpy if estimated badly.",
            "<b>More complex code</b> than a plain map()."],
    baseline="Each line compares <b>rendering every row</b> of a very long list to the same list <b>virtualized</b>.",
    ratings=[(4, 3, "Positioning and measuring add complexity."),
             (3, 4, "One virtual list/table component reused everywhere."),
             (4, 3, "Tests must scroll to reach rows; jsdom has no layout."),
             (3, 3, "Neutral."),
             (1, 5, "Render cost no longer grows with list length."),
             (3, 3, "A small library (a few kB)."),
             (4, 3, "Needs aria-rowcount/rowindex and careful focus handling."),
             (3, 3, "Libraries help; variable heights are fiddly."),
             (3, 3, "Neutral.")],
    pitfalls=[("Virtualizing short lists", "A list of 50 items gets windowing and loses Ctrl+F for nothing.", "virtualize only when lists are long (hundreds+) or rows are heavy."),
              ("Losing focus on scroll", "The focused row is recycled away and keyboard users lose their place.", "keep the focused row rendered; manage focus by index."),
              ("Bad size estimates", "Rows are 120 px but estimated at 40 px, so the scrollbar jumps.", "measure rows dynamically or estimate realistically."),
              ("Breaking screen readers", "Assistive tech thinks the table has 30 rows.", "aria-rowcount and aria-rowindex, or use a grid library that handles it.")],
    use=["Lists or tables with hundreds to millions of rows.",
         "Chat history, logs, transaction tables, spreadsheets.",
         "Heavy rows (images, many cells) that make even 200 rows slow.",
         "Infinite scroll feeds."],
    skip=["Short lists where rendering everything is fast.",
          "Content that must be fully searchable with Ctrl+F or printable.",
          "Pagination is the better UX anyway (search results)."],
    related=["<b>Server-state cache</b> (infinite queries)", "<b>Code splitting</b>", "<b>Custom hooks</b>", "<b>Headless components</b> (TanStack Table)"],
    quiz=[("What does the spacer element do?", "It has the full height of all rows so the scrollbar size and position reflect the whole list."),
          ("What is overscan?", "Extra rows rendered just outside the viewport so fast scrolling doesn't show blank gaps."),
          ("Name an accessibility concern with virtualization.", "Screen readers only see rendered rows; use aria-rowcount/rowindex and keep focus stable."),
          ("What CSS property offers a lighter alternative for long pages?", "content-visibility: auto, which lets the browser skip rendering off-screen sections.")],
    remember="Only paint what's in the <span class=\"hl\">window</span>. The rest of the route exists, just not in the DOM.",
    sources=["web.dev, “Virtualize large lists with react-window”.",
             "TanStack Virtual docs.",
             "web.dev, “content-visibility: the new CSS property that boosts your rendering performance”.",
             "patterns.dev, “List Virtualization”."],
)

NOTES = [SSR, ISLANDS, SPLIT, VIRTUAL]
