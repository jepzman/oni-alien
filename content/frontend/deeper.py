# Vol. 2 · going deeper (November 2026): a longer chapter inside three key notes.
# Merged into the notes by scripts/build_notes.py (load_content).

# ------------------------------------------------------------------ State machines
sm_d1 = Doodle(760, 300, "A search box as a state machine. From idle, typing moves to debouncing. After 300 milliseconds without typing it moves to loading and sends a request. Typing again while loading cancels the request and goes back to debouncing. A response moves to results or error. Responses from cancelled requests are ignored, because the machine is no longer waiting for them.",
               "Typing during a request is just another arrow: cancel, wait, ask again.")
sm_d1.box(20, 110, 120, 60, "idle", "paper", size=18)
sm_d1.box(210, 110, 150, 60, "debouncing", "y", size=18)
sm_d1.box(470, 110, 130, 60, "loading", "blue", size=18)
sm_d1.box(640, 40, 104, 56, "results", "green", size=17)
sm_d1.box(640, 184, 104, 56, "error", "pink", size=17)
sm_d1.arrow(144, 140, 206, 140, label="TYPE", lx=175, ly=130)
sm_d1.arrow(364, 132, 466, 132, label="300 ms quiet", lx=415, ly=120)
sm_d1.arrow(535, 174, 290, 174, curve=(412, 244), color="red", label="TYPE · cancel", lx=412, ly=236)
sm_d1.arrow(604, 124, 636, 72, label="OK", lx=606, ly=88)
sm_d1.arrow(604, 156, 636, 206, label="FAIL", lx=596, ly=204)
sm_d1.note(286, 96, "TYPE again: restart the timer", size=16)
sm_d1.note(380, 286, "a late answer to a cancelled request has no arrow: it's ignored", "pen", size=17)

sm_d2 = Doodle(760, 250, "Parallel states in a video player. Instead of four combined states (playing and muted, playing and unmuted, paused and muted, paused and unmuted), the machine has two regions that run side by side: playback with playing and paused, and sound with muted and unmuted. Adding a third region, captions on or off, adds two states instead of doubling to eight.",
               "Two regions side by side: 2 + 2 states instead of 2 × 2.")
sm_d2.box(20, 20, 340, 170, None, "paper", dash=True)
sm_d2.head(190, 46, "playback", size=18)
sm_d2.box(40, 70, 130, 56, "playing", "green", size=17)
sm_d2.box(210, 70, 130, 56, "paused", "y", size=17)
sm_d2.arrow(174, 90, 206, 90)
sm_d2.arrow(206, 110, 174, 110)
sm_d2.box(400, 20, 340, 170, None, "paper", dash=True)
sm_d2.head(570, 46, "sound", size=18)
sm_d2.box(420, 70, 130, 56, "unmuted", "blue", size=17)
sm_d2.box(590, 70, 130, 56, "muted", "pink", size=17)
sm_d2.arrow(554, 90, 586, 90)
sm_d2.arrow(586, 110, 554, 110)
sm_d2.note(380, 226, "add captions on / off: 2 more states, not 8 in total", "pen", size=17)

STATE_MACHINES_DEEP = dict(
    side="timers and races, statecharts, testing the machine",
    intro="The note replaces booleans with one status and a list of allowed events. Real interfaces add three complications: things that happen over time (debounce, timeouts, cancelled requests), several things going on at once, and the question of how to test that the machine does what the drawing says. This chapter takes them in turn.",
    parts=[
        ("Time, cancellation and races", """  <p>Many UI bugs are races: the user types “lam”, then “lamp”, and the answer for “lam” arrives last and overwrites the right one. A machine removes the race by making <b>waiting a state</b>. The search box waits in <i>debouncing</i> until the user stops typing for 300 ms, then moves to <i>loading</i>. If the user types again while loading, the machine cancels the request (an <code>AbortController</code>) and goes back to debouncing.</p>
  <p>Late answers are handled by the same rule as everything else: <b>an event with no arrow is ignored</b>. Tag each request with an id, and in loading accept only the response for the current id. An old answer arriving after a new request has nothing to do.</p>
  <p>Timers belong to states too. “Show a spinner only if loading takes longer than 400 ms” is a delayed transition from <i>loading</i> to <i>loading-slow</i>; “give up after 10 s” is another one to <i>error</i>. When the machine leaves the state, its timers are cancelled with it, so a timer never fires into the wrong screen.</p>""", [sm_d1]),
        ("Statecharts: nesting and parallel regions", """  <p>A flat machine grows fast. A video player can be playing or paused, muted or unmuted, with captions on or off: 2 × 2 × 2 = 8 combined states, and every new feature doubles them. <b>Statecharts</b> (David Harel, 1987) add two ideas that keep the drawing small:</p>
  <ul>
    <li><b>Parallel regions.</b> Playback and sound are independent, so they get separate regions that run side by side. 2 + 2 + 2 states instead of 8.</li>
    <li><b>Nested states.</b> A checkout form is in <i>editing</i>, and inside editing it is <i>valid</i> or <i>invalid</i>. An event that applies to the whole of editing (CANCEL) is drawn once, on the outer state, instead of once per inner state.</li>
  </ul>
  <p>XState implements statecharts and draws them for you; with <code>useReducer</code> you can do nesting by hand with a status like <code>{ step: "editing", form: "invalid" }</code>. Reach for a library when you have parallel regions, delays and guards together. Below that, a reducer is easier for the next person to read.</p>""", [sm_d2]),
        ("Testing a machine", """  <p>A machine is easy to test because it is a pure function: <b>(state, event) → next state</b>. Test it without rendering anything.</p>
  <ul>
    <li><b>A transition table.</b> One test per row: “in loading, TYPE goes to debouncing”, “in results, OK does nothing”. The table is the drawing written down, so a missing row is a missing arrow.</li>
    <li><b>The ignored events.</b> Send every event in every state and check that only the drawn ones change anything. This catches the double-submit bug: PAY in <i>submitting</i> must do nothing.</li>
    <li><b>Paths.</b> Model-based testing tools (such as @xstate/test) walk every path through the machine and run your UI test steps along each one, so you get coverage of the flows, not just the screens.</li>
  </ul>
  <p>Then render tests only need to check that each state shows the right view, which is a short list.</p>""", []),
    ],
)

# ------------------------------------------------------------------ SSR & hydration
ssr_d1 = Doodle(760, 270, "A page load timeline on a mid-range phone. The first byte arrives at 0.4 seconds, the content paints at 0.9 seconds, the largest image at 1.6 seconds. JavaScript downloads and hydrates until 3.8 seconds. Between 0.9 and 3.8 seconds the page looks ready but taps do nothing: the uncanny valley.",
                "The gap between “looks ready” and “is ready” is where users tap and nothing happens.")
ssr_d1.arrow(20, 150, 744, 150)
ssr_d1.note(744, 176, "seconds →", anchor="end", size=16)
for k, (x, t, lab) in enumerate([(70, "0.4", "first byte"), (150, "0.9", "content (FCP)"), (250, "1.6", "largest image"), (600, "3.8", "hydrated")]):
    ssr_d1.line(f"M{x} 140 V160", thin=False)
    ssr_d1.text(x, 132, t, "t-head", size=16)
    ssr_d1.note(x, 186 if k % 2 == 0 else 208, lab, size=15)
ssr_d1.box(150, 40, 450, 60, "looks ready, isn't", "pink", stroke="red", sub="taps do nothing · JS downloading and hydrating", size=18, subsize=14)
ssr_d1.note(380, 240, "shrink it: less JS · hydrate what's visible first · leave static parts static", "pen", size=17)

ssr_d2 = Doodle(760, 280, "Streaming a product page. The server sends the header and product details at once. The price arrives 120 milliseconds later and the reviews, which are slow, 900 milliseconds later, each replacing a placeholder. Without streaming, the whole page would wait 900 milliseconds for the reviews.",
                "Send what's ready, stream the rest into placeholders.")
for i, (name, t, fill) in enumerate([("header + product", "sent at 0 ms", "green"), ("price", "streamed at 120 ms", "y"), ("reviews", "streamed at 900 ms", "blue")]):
    y = 20 + i * 76
    ssr_d2.box(40, y, 300, 60, name, fill, sub=t, size=17, subsize=14)
ssr_d2.box(430, 20, 300, 212, None, "paper")
ssr_d2.head(580, 48, "the browser", size=18)
for i, (s, fill) in enumerate([("header + product", "green"), ("price", "y"), ("reviews", "blue")]):
    ssr_d2.box(450, 64 + i * 54, 260, 42, s, fill, size=15)
ssr_d2.arrow(344, 50, 446, 85)
ssr_d2.arrow(344, 126, 446, 139, dash=True)
ssr_d2.arrow(344, 202, 446, 193, dash=True)
ssr_d2.note(380, 266, "without streaming: everyone waits 900 ms for the reviews", "red", size=17)

SSR_DEEP = dict(
    side="reading the timeline, streaming, caching rendered pages",
    intro="The note explains render, embed and hydrate. This chapter is about making it fast in practice: how to read a page load so you know which gap to close, how streaming stops one slow query from holding up a whole page, and how to cache server-rendered pages without serving one user's page to another.",
    parts=[
        ("Reading the timeline", """  <p>Record a page load in the browser's performance panel with the CPU slowed four times and a slow network, which is closer to a typical phone than your laptop is. Then find five moments:</p>
  <ul>
    <li><b>First byte (TTFB):</b> how long the server took. Slow here means slow data or slow rendering on the server.</li>
    <li><b>First content (FCP) and largest content (LCP):</b> when the user sees something, and when they see the main thing. SSR is what makes these early.</li>
    <li><b>Hydration done:</b> the long JavaScript tasks after the content appears. Until they finish, clicks wait.</li>
    <li><b>Interaction to next paint (INP):</b> how quickly the page responds to taps once it is running.</li>
  </ul>
  <p>The usual SSR problem is the gap between the second and third: the page <b>looks</b> ready for seconds before it <b>is</b>. Close it by shipping less JavaScript (server components, code splitting), hydrating what is visible first, and leaving static parts as plain HTML (see Islands, the next pattern).</p>""", [ssr_d1]),
        ("Streaming: don't wait for the slowest part", """  <p>Without streaming, the server waits for every query on the page before sending a byte. One slow call (reviews, 900 ms) delays the whole page.</p>
  <p>With <b>streaming</b>, the server sends the HTML it has right away (layout, header, product details) with placeholders for slow parts, keeps the connection open, and sends each slow part when its data arrives. In React this is a <code>&lt;Suspense&gt;</code> boundary with a fallback; Next.js, Remix, SvelteKit and Nuxt all support it.</p>
  <p>Two things to watch. Start slow requests <b>in parallel</b>, not one after another: three 300 ms calls in sequence are 900 ms even with streaming. And put the placeholder in a box of the final size, so content arriving later doesn't push the page around (layout shift).</p>""", [ssr_d2]),
        ("Caching rendered pages", """  <p>Rendering on every request costs server time. Much of it can be cached, but only if you are careful about what is personal.</p>
  <div class="table-scroll"><table class="map"><thead><tr><th scope="col">Page</th><th scope="col">How to render and cache</th></tr></thead><tbody>
    <tr><td>Same for everyone, rarely changes (about, docs)</td><td>Render at build time (static). Serve from a CDN.</td></tr>
    <tr><td>Same for everyone, changes sometimes (product page)</td><td>Render on the server, cache at the CDN for a few minutes, revalidate in the background (stale-while-revalidate, or incremental static regeneration).</td></tr>
    <tr><td>Different per user (cart, account)</td><td>Render per request, <code>Cache-Control: private, no-store</code>. Never in a shared cache.</td></tr>
    <tr><td>Mostly shared, a little personal (product page with “hi Ana” and a cart count)</td><td>Cache the shared page; fetch the personal bits in the browser after load, or render them in a separate uncached fragment.</td></tr>
  </tbody></table></div>
  <p>The classic incident is a personal page cached by a CDN and shown to the next visitor. Make the default for server-rendered responses <b>private</b>, and opt pages into shared caching one by one.</p>""", []),
    ],
)

# ------------------------------------------------------------------ Micro-frontends
mf_d1 = Doodle(760, 260, "Shared dependencies in micro-frontends. Without sharing, three apps each ship their own copy of React, 45 kilobytes each, 135 in total, and React state can break between copies. With React marked as a shared singleton in module federation, the shell loads one copy that all three apps use, 45 kilobytes in total.",
               "Share the framework once; everything else stays inside each app.")
mf_d1.head(180, 24, "not shared", size=18, color="red")
for i, name in enumerate(["search", "product", "checkout"]):
    x = 20 + i * 110
    mf_d1.box(x, 40, 100, 120, None, "paper")
    mf_d1.head(x + 50, 74, name, size=15)
    mf_d1.box(x + 10, 104, 80, 40, "React", "pink", size=14)
mf_d1.note(180, 196, "3 × 45 KB · two Reacts can clash", "red", size=16)
mf_d1.head(580, 24, "shared singleton", size=18, color="green")
for i, name in enumerate(["search", "product", "checkout"]):
    x = 420 + i * 110
    mf_d1.box(x, 40, 100, 70, name, "paper", size=15)
mf_d1.box(420, 130, 320, 40, "React (one copy, from the shell)", "green", size=15)
mf_d1.note(580, 196, "45 KB once", "green", size=16)
mf_d1.note(380, 240, "pin the shared version range; upgrade it in one planned step", "pen", size=17)

mf_d2 = Doodle(760, 260, "Independent deploys through a manifest. Each team's pipeline builds its app, uploads it under a new version, and runs a smoke test against the shell. Only then does it change its own line in the manifest, for example checkout from version 41 to 42. Rolling back is changing the line back.",
               "Deploy = upload, smoke-test, flip your line in the manifest. Rollback = flip it back.")
mf_d2.row([("build", "checkout v42", "y"), ("upload", "to the CDN", "blue"), ("smoke test", "shell + v42", "blue")], x=20, y=30, h=70, gap=40, w=150, size=17, subsize=13, arrows=True)
mf_d2.arrow(554, 65, 586, 65)
mf_d2.table(590, 20, "manifest", ["search → v17", "product → v63", "checkout → v42"], w=150, fill="green", hl=(2,), size=15)
mf_d2.note(300, 160, "the shell reads the manifest at start-up", "pen", size=17)
mf_d2.note(300, 194, "rollback: checkout → v41 (seconds, no rebuild)", "green", size=17)
mf_d2.note(300, 228, "other teams' lines are untouched", size=16)

MICRO_FRONTENDS_DEEP = dict(
    side="ways to compose, shared code, contracts and deploys",
    intro="The note says split by business area and keep a thin shell. The hard parts come after the split: choosing how the pieces are put together, keeping the shared code from multiplying, and making sure independent deploys don't break each other. This chapter covers the three.",
    parts=[
        ("Choosing how to compose", """  <p>There are five common ways to put micro-frontends on one screen. Start with the simplest that fits.</p>
  <div class="table-scroll"><table class="map"><thead><tr><th scope="col">Way</th><th scope="col">Good for · cost</th></tr></thead><tbody>
    <tr><td><b>Separate pages</b> (each app owns some URLs, links between them)</td><td>Most cases. Fully independent. Cost: a full page load between areas, so keep the shared header fast.</td></tr>
    <tr><td><b>Build-time packages</b> (apps published as npm packages into one build)</td><td>Easy to start. But every change needs a rebuild of the host: not independent deploys.</td></tr>
    <tr><td><b>Runtime loading</b> (module federation, import maps)</td><td>Several teams on one page with independent deploys. Cost: shared dependency management and runtime failures.</td></tr>
    <tr><td><b>Web components</b></td><td>Mixed frameworks, long-lived boundaries. Cost: styling and server rendering are harder.</td></tr>
    <tr><td><b>Server or edge composition</b> (fragments stitched into HTML)</td><td>Fast first paint and SEO. Cost: the composition layer is a service to run.</td></tr>
  </tbody></table></div>
  <p>Many teams mix them: separate pages per area, and one runtime-loaded widget (the mini-cart) that appears everywhere.</p>""", []),
        ("Shared code without five copies", """  <p>Each app bundling its own React, router and design system makes the page heavy, and two copies of React on one page can break hooks and context in confusing ways. With module federation, mark the framework as a <b>shared singleton</b>: the shell provides one copy and every app uses it.</p>
  <p>Keep the shared list short: the framework, the design system's runtime, maybe the router. Each shared library is a version every team must agree on, so give it a <b>version range</b>, upgrade it in one planned step for everyone, and check the range in CI so an app built against a newer major fails before it reaches users. Everything else (data fetching, forms, state) stays inside each app, even if two apps use the same library.</p>
  <p>Track a size budget per app and for the whole page. Micro-frontends fail quietly by getting heavier one dependency at a time.</p>""", [mf_d1]),
        ("Contracts and safe deploys", """  <p>Independent apps still talk: the product page tells the mini-cart an item was added; the shell tells everyone who is signed in. Keep those contracts small, written down and tested:</p>
  <ul>
    <li><b>Browser events</b> with a documented name and shape (<code>cart:item-added</code> with <code>{ sku, qty }</code>), versioned like an API. Add fields; never rename one.</li>
    <li><b>URLs</b> as contracts between pages: <code>/product/:sku</code> must keep working.</li>
    <li><b>A schema test</b> on each side: the sender's events match the schema, and the receiver handles every version still being sent.</li>
  </ul>
  <p>For deploys, use a <b>manifest</b> the shell reads at start-up (app name → version URL). A team's pipeline uploads the new version, runs a smoke test of the shell with it, and only then changes its own line. Rollback is changing the line back, in seconds, without touching anyone else.</p>""", [mf_d2]),
    ],
)

REVISIONS = {
    "state-machines": dict(deep_dive=STATE_MACHINES_DEEP),
    "ssr-hydration": dict(deep_dive=SSR_DEEP),
    "micro-frontends": dict(deep_dive=MICRO_FRONTENDS_DEEP),
}
