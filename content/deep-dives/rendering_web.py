# Deep dive 11 · Rendering on the Web. Builds on Vol. 2 notes 09 (SSR & hydration), 10 (islands architecture) and
# 11 (code splitting & lazy loading). Example: the mug shop's product page for product 42, the mug at $24.50, the same
# page the Caching deep dive followed through its caches. Measured as Lighthouse measures a phone: a mid-range device
# (CPU four times slower than a laptop) on a slow 4G connection. The figures for the shop are illustrative.
# Helpers (mn, full, tbl, drill, code, fig, checklist) are injected by scripts/build_notes.py from scripts/dive.py.

# ------------------------------------------------------------------ 1 recap
spectrum_svg = '''
  <path class="ln" d="M20 120 H740"/>
  <rect class="bx-g" x="20" y="60" width="128" height="50" rx="8"/><text class="lbl" x="84" y="84" text-anchor="middle">static HTML</text><text class="soft" x="84" y="102" text-anchor="middle">built once</text>
  <rect class="bx-g" x="166" y="60" width="128" height="50" rx="8"/><text class="lbl" x="230" y="84" text-anchor="middle">islands</text><text class="soft" x="230" y="102" text-anchor="middle">a little JS</text>
  <rect class="bx-y" x="312" y="60" width="140" height="50" rx="8"/><text class="lbl" x="382" y="84" text-anchor="middle">server components</text><text class="soft" x="382" y="102" text-anchor="middle">JS where needed</text>
  <rect class="bx-y" x="470" y="60" width="128" height="50" rx="8"/><text class="lbl" x="534" y="84" text-anchor="middle">SSR + hydrate</text><text class="soft" x="534" y="102" text-anchor="middle">all JS, early HTML</text>
  <rect class="bx-r" x="616" y="60" width="124" height="50" rx="8"/><text class="lbl" x="678" y="84" text-anchor="middle">client only</text><text class="soft" x="678" y="102" text-anchor="middle">all JS, late HTML</text>
  <text class="soft" x="20" y="148">less JavaScript in the browser</text><text class="soft" x="740" y="148" text-anchor="end">more JavaScript in the browser</text>
  <text class="soft" x="20" y="36">documents: articles, product pages</text><text class="soft" x="740" y="36" text-anchor="end">apps: editors, dashboards</text>
'''
recap = '''
<p>The Caching deep dive followed the product page for product 42 through five layers of copies. This one follows the same page into the browser: how its HTML gets there, how much JavaScript comes with it, and when a shopper on a mid-range phone can see the mug and tap “Add to basket”. Three notes from the frontend volume set out the tools.</p>
''' + tbl(["Note", "In one line"], [
    ["SSR & Hydration", "render HTML on the server for a fast first view, then run the same code in the browser to make it interactive"],
    ["Islands Architecture", "ship static HTML and hydrate only the small interactive parts"],
    ["Code Splitting & Lazy Loading", "load only the code a screen needs now, fetch the rest when needed"],
]) + fig(760, 165, "A spectrum of rendering approaches from left to right: static HTML built once; islands with a little JavaScript; server components with JavaScript only where needed; server rendering with full hydration, which sends all the JavaScript but early HTML; and client-only rendering, all JavaScript and late HTML. The left end suits documents such as articles and product pages; the right end suits apps such as editors and dashboards.",
          spectrum_svg, "One question runs along this line: how much of the page's work happens in the shopper's browser?") + mn("The SSR note's going-deeper chapter covers reading a page-load timeline, streaming and caching rendered pages. This dive builds on it.") + '''
<p class="full">Each note presents one option. The real decision is which option for which page, measured on the phone your customers actually own. A developer's laptop on office wifi makes every approach look fast. A three-year-old Android phone on a train shows the differences, and that phone is the median customer. This deep dive measures one page four ways, follows the six ways rendering goes wrong, and ends with budgets the build can enforce.</p>
'''

# ------------------------------------------------------------------ 2 what fast means
timeline_svg = '''
  <path class="ln" d="M20 130 H740"/>
  <rect class="bx" x="20" y="96" width="70" height="28" rx="4"/><text class="soft" x="55" y="115" text-anchor="middle">request</text>
  <rect class="bx-g" x="90" y="96" width="150" height="28" rx="4"/><text class="soft" x="165" y="115" text-anchor="middle">HTML arrives</text>
  <rect class="bx-y" x="240" y="96" width="190" height="28" rx="4"/><text class="soft" x="335" y="115" text-anchor="middle">image, CSS, fonts</text>
  <rect class="bx-r" x="430" y="96" width="250" height="28" rx="4"/><text class="soft" x="555" y="115" text-anchor="middle">JavaScript runs: hydration</text>
  <path class="ln-d" d="M90 90 V60"/><text class="lbl" x="90" y="52" text-anchor="middle">TTFB</text>
  <path class="ln-d" d="M240 90 V60"/><text class="lbl" x="240" y="52" text-anchor="middle">FCP</text>
  <path class="ln-d" d="M430 90 V60"/><text class="lbl" x="430" y="52" text-anchor="middle">LCP</text>
  <path class="ln-d" d="M680 90 V60"/><text class="lbl" x="680" y="52" text-anchor="middle">interactive</text>
  <text class="soft bad" x="555" y="84" text-anchor="middle">a tap here waits: INP suffers</text>
  <text class="soft" x="20" y="160">0 s</text><text class="soft" x="740" y="160" text-anchor="end">about 4 s on a mid-range phone</text>
'''
fast = '''
<p>“The page is slow” means different things at different moments. Browsers and tools agree on a handful of named moments, and three of them, the Core Web Vitals, are what search engines and most teams use as the scoreboard.</p>
''' + fig(760, 175, "A page-load timeline. After the request, the HTML arrives: time to first byte. Then the image, CSS and fonts load, during which first contentful paint happens. Largest contentful paint marks when the main image appears. Then JavaScript runs to hydrate the page, until it becomes interactive. A tap during hydration has to wait, which hurts interaction to next paint.",
          timeline_svg, "Visible and usable are different moments. The gap between them is where shoppers tap and nothing happens.") + tbl(["Metric", "Measures", "Good at the 75th percentile"], [
    ["<b>LCP</b>, largest contentful paint", "when the main thing (the mug photo) appears", "2.5 s or less"],
    ["<b>INP</b>, interaction to next paint", "how long the page takes to respond to taps and keys, over the whole visit", "200 ms or less"],
    ["<b>CLS</b>, cumulative layout shift", "how much content jumps around while loading", "0.1 or less"],
    ["TTFB, time to first byte", "how long the server took to start answering", "about 0.8 s or less"],
    ["FCP, first contentful paint", "when anything at all appears", "1.8 s or less"],
], hot=(0, 1, 2)) + mn("INP replaced an older metric (first input delay) in 2024. It watches every interaction, not just the first.") + full('''<h3>Lab numbers and field numbers</h3>
<p>There are two ways to measure, and they disagree for good reasons.</p>
''' + tbl(["", "Lab", "Field"], [
    ["How", "one controlled load, in Lighthouse or WebPageTest, on a simulated phone", "real visits, measured in real browsers and sent to you"],
    ["Good for", "comparing two builds; finding why", "knowing what customers experience"],
    ["Misses", "real devices, real networks, real caches, and INP (a lab load has no shopper tapping)", "the cause: it tells you that, not why"],
]) + '''<p>Use the field numbers to decide whether there is a problem, and the lab to find and fix it. Report the field numbers at the 75th percentile, split by page type and by device class. An average across all visits mixes the fast office laptops with the slow phones and hides exactly the customers who leave.</p>
<h3>Who the median customer is</h3>
<p>For the shop's analytics, the most common device is a mid-range Android phone about three years old. Its processor runs JavaScript three to five times slower than a developer laptop, and in the evening, on mobile data, its connection is closer to slow 4G than to the office network. Every number in this deep dive is for that phone. If the page is good there, it is good everywhere.</p>''')

# ------------------------------------------------------------------ 3 four ways
fourways = '''
<p>The team built the product page four ways and measured each on the simulated mid-range phone. The page shows a photo, name, price, description, reviews, an “Add to basket” button and a size picker. The numbers are the shop's, rounded; yours will differ, but the pattern rarely does.</p>
''' + tbl(["", "Client only", "Server render + full hydration", "Static, rebuilt on change", "Islands"], [
    ["HTML sent", "1 KB, nearly empty", "40 KB with content", "40 KB with content", "40 KB with content"],
    ["JavaScript sent (compressed)", "310 KB", "310 KB", "310 KB, or less with islands", "38 KB"],
    ["Server work per visit", "none", "render every time: 120 ms", "none; served from the CDN", "none, or render once"],
    ["LCP", "4.1 s", "2.2 s", "1.6 s", "1.5 s"],
    ["Interactive (hydration done)", "4.6 s", "4.4 s", "4.3 s", "1.9 s"],
    ["Risk to INP", "high while loading", "high while loading", "high while loading", "low"],
    ["Price is current", "yes, fetched", "yes, rendered", "as of the last rebuild", "as of the last rebuild; live price can be an island"],
], hot=(3,)) + mn("Server rendering fixed when the mug appears. It did not fix when the button works. Only shipping less JavaScript did.") + '''
<h3>What the table says</h3>
<ul>
  <li><b>Client only</b> loses on LCP because nothing can appear until the JavaScript has downloaded, run and fetched the data, one after another.</li>
  <li><b>Server rendering</b> moves the mug photo two seconds earlier. The button still works at 4.4 s, because the same 310 KB of JavaScript must still download and run to hydrate the page.</li>
  <li><b>Static</b> wins on first byte, because the HTML comes straight from the CDN, but has the same hydration cost.</li>
  <li><b>Islands</b> hydrate only the size picker, the basket button and the review form. Everything else is HTML that needs no JavaScript at all.</li>
</ul>
''' + full('''<h3>Choosing per page, not per site</h3>
<p>A shop is not one kind of page. Each page type gets the approach that fits what it is.</p>
''' + tbl(["Page", "Nature", "Approach"], [
    ["home, category, product", "documents with a few controls; most visits from search and links", "static or cached server render, with islands"],
    ["search results", "a document whose content depends on the query", "server render, cached briefly per query; filters as an island"],
    ["basket and checkout", "personal, a form, must be current", "server render per request, small JavaScript, forms that work without it"],
    ["account pages", "personal, read mostly", "server render, not cached by the CDN"],
    ["the shop's admin tool", "an app used all day by staff on laptops", "client-rendered app; fine there"],
]) + '''<p>Most modern frameworks let different routes use different approaches in one codebase. The mistake is choosing once, for the whole site, based on the page type the team works on most, which is usually the admin tool.</p>''')

# ------------------------------------------------------------------ 4 drills
drills = mn("Each of these has been seen on a real shop. Try to name the cause before reading it.") + '''
<ul class="drill-index" aria-label="The six drills">
  <li><a href="#drill-1">1 · mismatch</a></li><li><a href="#drill-2">2 · dead button</a></li><li><a href="#drill-3">3 · jumping page</a></li>
  <li><a href="#drill-4">4 · the waterfall</a></li><li><a href="#drill-5">5 · someone's basket</a></li><li><a href="#drill-6">6 · the creeping bundle</a></li>
</ul>
''' + drill(1, "The page that rendered twice", [
    ("Timeline", "The product page shows “Order in the next 3 hours for delivery tomorrow”. The server renders it at 14:00:00 in its own time zone. The browser hydrates at 14:00:03 in the shopper's time zone and gets a different text."),
    ("What you see", "A flicker as the text changes, a console warning about a hydration mismatch, and on some framework versions the whole section rendered again from scratch, or event handlers attached to the wrong elements.", True),
    ("Why", "Hydration assumes the browser's first render produces exactly the HTML the server sent. Anything that differs between the two runs breaks that: the clock, the time zone, random ids, the window size, data read from local storage.", True),
    ("What saves you", "Render the same thing on both sides, then change it after hydration. Send times as timestamps and format them in an effect that runs only in the browser, or render them as a small island. Use the framework's stable id helper, never random numbers. Log mismatch warnings from real visits so they are noticed."),
], "the first render in the browser must match the server's HTML exactly. Anything that can differ waits until after hydration.") + drill(2, "The button that did nothing", [
    ("Timeline", "The photo appears at 1.6 s. The shopper taps “Add to basket” at 2.0 s. Hydration finishes at 4.3 s. Nothing happened at the tap; they tap again, then again."),
    ("What you see", "Rage taps in the analytics, a poor INP, and sometimes three mugs in the basket once the queued taps are replayed. Customers describe the site as “broken”, not “slow”.", True),
    ("What saves you", "Make the important controls work before JavaScript arrives. A real form with a <code>POST</code> to the basket works the moment the HTML is there; JavaScript can improve it later. Hydrate the button first or make it an island. And keep the gap short, because every control cannot be a form."),
], "a page that looks ready must be ready. Use real links and forms for the actions that matter.") + drill(3, "The page that jumped", [
    ("Timeline", "The shopper starts reading the description. The reviews widget loads above it and pushes it down. A web font arrives and the text reflows. A promotion banner slides in at the top. They tap “Add to basket” just as it moves, and hit “Remove” on the line below."),
    ("What you see", "CLS of 0.35, and mis-taps that feel like the shop is fighting the customer.", True),
    ("What saves you", "Reserve space for everything that arrives late: width and height on images, a fixed-height placeholder for the reviews and the banner, and a fallback font sized to match the web font. Never insert content above what the reader is looking at unless they asked for it."),
], "everything that loads late gets its space reserved before it arrives.") + drill(4, "One thing after another", [
    ("Timeline", "The client-rendered page loads HTML, then the JavaScript bundle, then runs it, which requests the product, which, once it arrives, requests the reviews, which contain image addresses, which are then requested. Each step waits for the one before."),
    ("What you see", "Six round trips in a row on a connection where each costs 150 ms or more before any bytes arrive. The page is slow even though every single request is fast.", True),
    ("What saves you", "Break the chain. Fetch data on the server, where round trips to the database are short, and send it with the HTML. Start independent requests at the same time instead of one after another. Tell the browser early about the hero image with a preload hint, so it does not wait to discover it. The performance panel's network view shows a chain as a staircase."),
], "count the steps that wait for each other. On a phone, the chain is slower than any request in it.") + drill(5, "Someone else's basket", [
    ("Timeline", "The product page is server-rendered and cached at the CDN for 60 seconds to cut server load. Its header shows “Basket (3)” and the signed-in shopper's first name. The first visitor after each expiry decides what everyone sees for the next minute."),
    ("What you see", "Strangers greeted as “Hi Sam” with someone else's basket count. In the worst version the cached page included part of an address.", True),
    ("What saves you", "This is drill 6 of the Caching deep dive, at the rendering layer. Keep cached HTML free of anything personal: render the shared page for everyone, and fill the personal parts in the browser or at the edge, from a request that is never cached. Mark personal responses <code>private</code> so no shared cache keeps them."),
], "a page that is cached for everyone must contain nothing that belongs to anyone.") + drill(6, "The bundle that crept back", [
    ("Timeline", "In March the product page shipped 38 KB of JavaScript. A developer adds a date-formatting library to the shared component that shows delivery dates. Another adds an analytics helper to the layout. By September the page ships 290 KB, and nobody decided that."),
    ("What you see", "INP and LCP slowly worsening month after month in the field data, with no single change to blame.", True),
    ("What saves you", "A budget the build enforces: the product page's JavaScript may not exceed, say, 60 KB compressed, and the pull request that crosses it fails with the size difference shown. Check what a new dependency costs before adding it. Look at the bundle map once a quarter."),
], "JavaScript grows by default. Only a budget that fails the build keeps it small.") + full('''<h3>What the six drills add up to</h3>
''' + tbl(["Habit", "Drill"], [
    ["the first browser render matches the server; dates and ids wait for hydration", "1"],
    ["key actions work as plain links and forms before JavaScript", "2"],
    ["late content has its space reserved", "3"],
    ["data is fetched on the server or in parallel; the hero image is announced early", "4"],
    ["shared cached HTML holds nothing personal", "5"],
    ["JavaScript budgets per page fail the build", "6"],
]))

# ------------------------------------------------------------------ 5 hydration
hydration = '''
<p>Chapter 3's table had one stubborn number: the page was visible at 1.6 s and usable at 4.3 s, and server rendering did not change the second number. That gap is the hard problem of modern rendering, and it comes from what hydration has to do.</p>
''' + tbl(["Hydration has to…", "Cost"], [
    ["download the code for every component on the page", "the 310 KB, even for paragraphs that never change"],
    ["download the data again, embedded as JSON in the page", "the product appears twice: as HTML and as data"],
    ["run every component again in the browser", "the same work the server already did"],
    ["attach event handlers to the existing elements", "small; the only part that was really needed"],
], hot=(3,)) + mn("Hydration is doing the server's work a second time, on the slowest computer in the system.") + '''
<h3>Four ways to do less of it</h3>
''' + tbl(["Approach", "Idea", "Trade-off"], [
    ["<b>Progressive hydration</b>", "hydrate the important parts first, the rest when idle or visible", "the total work is the same; it is just ordered better"],
    ["<b>Islands</b>", "only marked components get JavaScript at all", "sharing state between islands needs care; suits documents, not apps"],
    ["<b>Server components</b>", "components marked as server-only render to HTML and never send their code; client components hydrate as usual", "two kinds of component with rules about which can contain which; needs a framework that supports it"],
    ["<b>Resumability</b>", "the server records where it stopped; the browser resumes on the first interaction instead of re-running everything", "a different programming model; fewer frameworks"],
]) + full('''<p>They share one idea: most of a page is a document, and documents do not need code in the browser. The approaches differ in who decides which parts are interactive. With islands you mark the interactive parts. With server components you mark them too, from the other direction: everything is server-only unless it says it needs the browser. Progressive hydration keeps one kind of component and only changes the order.</p>
<h3>The product page with server components</h3>
''' + code("product-page.tsx", "only the marked parts send code to the browser", '''
// server component: runs on the server, sends HTML, sends no JavaScript
export default async function ProductPage({ id }: { id: string }) {
  const product = await db.product(id);                 // straight to the data, no API round trip
  return (
    <main>
      <ProductPhoto product={product} />               {/* server-only */}
      <h1>{product.name}</h1>
      <Price amount={product.price} />                 {/* server-only */}
      <SizePicker sizes={product.sizes} />             {/* "use client": hydrates */}
      <AddToBasket productId={id} />                   {/* "use client": hydrates */}
      <Reviews productId={id} />                       {/* server-only, streamed */}
    </main>
  );
}
''') + '''<p>The two client components are the only code the browser receives for this page, which is how the island column in chapter 3 got to 38 KB without a separate framework. Whichever approach you choose, measure the hydration gap on the median phone before and after. It is the number that tells you whether the choice worked.</p>''')

# ------------------------------------------------------------------ 6 less javascript
lessjs = '''
<p>JavaScript is the most expensive thing a page sends. An image of 300 KB is decoded quickly and mostly off the main thread. A script of 300 KB must be downloaded, parsed, compiled and run, on the main thread, before the page can respond to a tap. On the median phone, the running alone often takes over a second.</p>
<h3>Split by when it is needed</h3>
''' + tbl(["Split", "Loads", "For the product page"], [
    ["<b>by route</b>", "when the page is visited", "the product page never loads checkout's code"],
    ["<b>by interaction</b>", "when the shopper starts to use it", "the review form's editor loads when “Write a review” is tapped"],
    ["<b>by visibility</b>", "when it scrolls into view", "the “you might also like” carousel"],
    ["<b>after load</b>", "when the browser is idle", "analytics and the chat widget"],
]) + code("reviews.tsx", "the editor is downloaded only when someone wants to write", '''
const ReviewEditor = lazy(() => import("./ReviewEditor"));   // a separate chunk

function WriteReview() {
  const [open, setOpen] = useState(false);
  return open
    ? <Suspense fallback={<p>Loading the editor…</p>}><ReviewEditor /></Suspense>
    : <button onMouseEnter={() => import("./ReviewEditor")}   // start early on hover
              onClick={() => setOpen(true)}>Write a review</button>;
}
''') + mn("Prefetch on hover or when the link scrolls into view. The chunk then arrives in the 200 ms between pointing and tapping.") + full('''<h3>Don't split too finely</h3>
<p>Each chunk is a request, and chunks that import other chunks form the chain from drill 4. Forty tiny chunks for one screen can load slower than four sensible ones. Split along the lines in the table above, then check the network panel for a staircase.</p>
<h3>Third-party scripts</h3>
<p>On many shops the largest JavaScript is not the shop's own: a tag manager, two analytics tools, a chat widget, a reviews provider, an A/B testing script that hides the page until it has decided. They are added by other teams, outside the code review, and they run on the same main thread.</p>
''' + tbl(["Script", "Better"], [
    ["chat widget", "a static button that loads the real widget when tapped (a facade)"],
    ["analytics", "after load, or sent from the server where possible"],
    ["A/B test that hides the page", "decide on the server or at the edge, so the page arrives already chosen"],
    ["video embed", "a thumbnail image that becomes the player when tapped"],
    ["tag manager", "an owner, a review of every tag, and the same budget as your own code"],
]) + '''<h3>Smaller code, not just later code</h3>
<p>Splitting moves code later; deleting it is better. Check what each dependency costs before adding it; many have smaller alternatives or are replaced by features the browser now has. Send modern JavaScript to modern browsers instead of compiling everything for ten-year-old ones. And look at the bundle map: a treemap of what is in each chunk shows the 70 KB locale file that nobody knew was there.</p>''')

# ------------------------------------------------------------------ 7 budgets
budgets = '''
<p>Targets become real when they are turned into budgets that the build can check. Here is the product page's, worked back from “LCP under 2.5 s for three customers in four”.</p>
''' + tbl(["Step on the median phone", "Budget", "Reasoning"], [
    ["DNS, connection, TLS", "0.5 s", "three round trips at about 150 ms on mobile; reused on later pages"],
    ["first byte from the CDN", "0.2 s", "cached HTML; a server render would need 0.3–0.6 s more"],
    ["HTML and critical CSS", "0.3 s", "about 40 KB of HTML, CSS inlined or one small file"],
    ["hero image", "0.9 s", "about 100 KB in a modern format at the size the screen needs, announced early"],
    ["margin", "0.6 s", "the 75th percentile is worse than the simulated phone"],
    ["<b>LCP</b>", "<b>2.5 s</b>", ""],
]) + mn("The budget shows why the hero image matters more than the framework: it is the biggest single item on the path to LCP.") + '''
<h3>The hero image and the fonts</h3>
''' + tbl(["Habit", "Why"], [
    ["serve the image at the size the screen shows it, in several widths (<code>srcset</code>)", "a phone 400 pixels wide does not need the 2,000-pixel photo"],
    ["use a modern format such as AVIF or WebP", "often half the bytes of a JPEG at the same quality"],
    ["mark the hero <code>fetchpriority=\"high\"</code>, and never lazy-load it", "lazy loading the largest image delays LCP by exactly the thing it was meant to speed up"],
    ["lazy-load images below the first screen", "they compete with the hero for the same slow connection"],
    ["one or two font files, subset to the characters you use, with a fallback sized to match", "fonts block text or make it jump (drill 3)"],
]) + '''
<h3>Budgets the build checks</h3>
''' + tbl(["Budget", "Product page", "Checkout", "Admin tool"], [
    ["JavaScript, compressed, on load", "60 KB", "120 KB", "500 KB"],
    ["largest image", "120 KB", "none on the path", "not checked"],
    ["lab LCP on the simulated phone", "2.0 s", "2.5 s", "not checked"],
    ["lab total blocking time", "150 ms", "200 ms", "not checked"],
    ["third-party scripts on load", "1", "0", "any"],
], hot=(0,)) + full('''<p>Budgets differ by page because pages differ. The admin tool is used on laptops by staff who load it once a day; a big bundle there costs little. The product page is the first contact with customers who came from a search result and will leave in three seconds.</p>
<h3>INP is a budget on long tasks</h3>
<p>The browser can respond to a tap only between tasks. Any piece of JavaScript that runs longer than 50 ms is a long task, and a tap that arrives during one waits for it to finish. Hydration, large re-renders, heavy event handlers and third-party scripts are the usual long tasks. The budget is therefore: no single task over 50 ms after the page appears, and expensive work split into pieces that let the browser respond in between, or moved off the main thread altogether.</p>
<h3>What a kilobyte costs</h3>
<p>As a rule of thumb from the shop's own measurements on the median phone: each 100 KB of compressed JavaScript on the critical path added about 0.3 s to download on slow 4G and about 0.5 s of main-thread work. The exact numbers depend on the code, but the shape does not: JavaScript costs twice, once on the network and once on the processor, and the second cost does not shrink with a faster connection.</p>''')

# ------------------------------------------------------------------ 8 html at the edge
edge = '''
<p>A server-rendered page is only fast if the server is. The going-deeper chapter of the SSR note introduced streaming and caching rendered HTML; this chapter puts them together for the shop.</p>
<h3>Cache what is the same for everyone</h3>
''' + tbl(["Part of the product page", "Same for everyone?", "Served from"], [
    ["photo, name, description, sizes", "yes", "cached HTML at the CDN, refreshed when the product changes"],
    ["price", "yes, but changes", "cached with a short life, or a small island that fetches it"],
    ["reviews", "yes, slow to compute", "streamed in after the rest, cached separately"],
    ["“Basket (3)”, “Hi Sam”", "no", "the browser, from an uncached request after the page loads"],
    ["stock for the chosen size", "yes, but must be current at checkout", "shown from a short cache; checked for real when added to the basket"],
]) + mn("Same rule as the Caching dive: show from a copy, decide on the original.") + '''
<h3>Streaming: send the shell first</h3>
<p>With streaming, the server sends the top of the page as soon as it is ready, and slower parts follow in the same response as they complete. The photo and name go first; the reviews, which need a slow query, arrive half a second later and slot into a reserved space (drill 3).</p>
''' + full('''<h3>The status code is sent first</h3>
<p>Streaming has one consequence that surprises teams. The HTTP status code is part of the first bytes. Once the shell has been sent with <code>200 OK</code>, the server cannot change its mind if the reviews query fails or the product turns out not to exist. So decide everything that affects the status before streaming starts: does the product exist (404), is the shopper allowed to see it, should this be a redirect. Stream only the parts whose failure the page can survive, and give each a fallback that renders in its slot.</p>
<h3>Search engines and link previews</h3>
<p>Crawlers increasingly run JavaScript, but link previews in chat apps and many smaller crawlers do not, and those that do may not wait for slow data. A product page whose name, price and photo are in the first HTML is indexed and previewed correctly by everything. That alone is often the business reason for server rendering, separate from speed.</p>
<h3>Moving between pages</h3>
<p>The first page load gets the attention, but a shopper looks at five or six pages per visit. Two approaches handle the next page differently.</p>
''' + tbl(["", "Full page loads", "Client-side navigation"], [
    ["Next page", "the browser fetches new HTML, as on the first visit", "JavaScript fetches data and renders the new page in place"],
    ["Cost", "a new document each time; shared files come from cache", "the router and every route's code must be loaded first"],
    ["Strengths", "simple; the back button restores the old page instantly from the browser's page cache", "smooth transitions; state such as an open basket drawer survives"],
    ["Watch", "make it fast with prefetching and cached HTML", "scroll position, focus for screen readers, and memory over a long visit"],
]) + '''
<p>Browsers have closed much of the gap. Prefetching the likely next page on hover, and view transitions that animate between full page loads, give documents most of the smoothness of an app without its JavaScript. For a shop, full page loads with prefetching are usually the better default; the basket drawer can be an island.</p>
<h3>Where to render</h3>
''' + tbl(["Where", "Good for", "Watch"], [
    ["at build time", "pages that change rarely: help, about, most category pages", "rebuild time grows with page count; rebuild one page on change"],
    ["on a server near the data", "personal pages, anything that needs several queries", "distance to the shopper; cache what you can"],
    ["at the edge, near the shopper", "light personalisation: country, language, A/B variant", "the database is far away; one slow query from the edge is many round trips"],
]))

# ------------------------------------------------------------------ 9 testing and running
running = '''
<p>Rendering performance decays quietly: a few kilobytes here, an extra script there, a slower query. It stays good only when it is measured on every change and watched in the field.</p>
<h3>In the pull request</h3>
''' + tbl(["Check", "How", "Fails when"], [
    ["<b>bundle size</b>", "a size checker compares each page's JavaScript with its budget", "a budget from chapter 7 is crossed; the diff shows which import did it"],
    ["<b>lab run</b>", "Lighthouse in CI on the product, category and checkout pages, simulated phone, three runs, median", "LCP or total blocking time is over budget"],
    ["<b>no-JavaScript test</b>", "load the product page with JavaScript disabled; add to basket", "the key action needs JavaScript (drill 2)"],
    ["<b>hydration warnings</b>", "the end-to-end tests fail on any hydration mismatch in the console", "drill 1"],
    ["<b>layout shift</b>", "the lab run's CLS, plus a test that loads with a slow reviews response", "late content moves the page (drill 3)"],
]) + mn("Lab runs are noisy. Run three, take the median, and set budgets with a little room.") + '''
<h3>In the field</h3>
<p>A small script in every page measures the Core Web Vitals in real visits and sends them to your analytics, with the page type, device class and connection type. The dashboard shows the 75th percentile per page type, per week.</p>
''' + code("vitals.ts", "real numbers from real phones", '''
import { onLCP, onINP, onCLS } from "web-vitals";

function send(metric) {
  navigator.sendBeacon("/vitals", JSON.stringify({
    name: metric.name, value: metric.value,
    page: document.body.dataset.pageType,          // "product", "category", "checkout"
    device: navigator.hardwareConcurrency <= 4 ? "low" : "high",
  }));
}
onLCP(send); onINP(send); onCLS(send);
''') + full('''<h3>Runbook: “LCP got worse”</h3>
<ol>
  <li><b>Which pages and devices?</b> The field dashboard, split. One page type: a change to that page. All pages: something shared, like the layout, a font or a third-party script. Only low-end devices: JavaScript or image weight.</li>
  <li><b>Which part of the timeline?</b> A lab run of the same page: is the extra time in first byte (server or cache), in the hero image, or in waiting for scripts?</li>
  <li><b>First byte:</b> the CDN hit rate for HTML, then the server's render time. A page that stopped being cacheable shows up here.</li>
  <li><b>Hero image:</b> its size, format and whether it is still announced early. A redesign often swaps in a 2 MB image.</li>
  <li><b>Scripts:</b> the bundle map and the list of third-party scripts against last month's.</li>
</ol>
<h3>Watch the business number too</h3>
<p>Put conversion rate next to LCP and INP on the same dashboard, by device class. The point of all this is shoppers who stay and buy, and the shop found that phones in the slowest quarter converted at half the rate of the fastest. That graph is what keeps the budgets funded.</p>''')

# ------------------------------------------------------------------ 10 tools, lab, checklist
tools = '''
<h3>Tools</h3>
''' + tbl(["Need", "Examples"], [
    ["frameworks with per-route rendering choices", "Next.js, React Router (formerly Remix), Nuxt, SvelteKit, Angular"],
    ["documents with islands", "Astro, Fresh, Eleventy with is-land"],
    ["resumable rendering", "Qwik"],
    ["lab measurement", "Lighthouse and Lighthouse CI, WebPageTest, the browser's performance panel"],
    ["field measurement", "the web-vitals library, the Chrome User Experience Report, real-user monitoring products"],
    ["bundle size", "size-limit, bundle analyzers and treemaps for Vite, Rollup and webpack"],
]) + mn("The framework matters less than the page-by-page choice and the budget. Every one of these can ship a slow page.") + '''
<h3>Lab</h3>
<p>The shop's search results page shows 24 products for a query, with filters for size, colour and price, and a sort order. Most visits come from the shop's own search box; some from search engines. The page currently is client-rendered: LCP 4.3 s and INP 380 ms on the median phone.</p>
<ol class="keep">
  <li>Which approach from chapter 3 fits, and why not static?</li>
  <li>What can be cached, and for how long?</li>
  <li>How do the filters work before JavaScript has loaded?</li>
  <li>Where does the 380 ms INP probably come from, and what do you do?</li>
  <li>Set the JavaScript budget, and say what the pull-request check does when someone adds a 90 KB date picker for the delivery-date filter.</li>
</ol>
<div class="check quiz"><h3>model answer</h3>
<details><summary>1 · Approach</summary><p>Server render per query, with the filter panel and the sort control as the only hydrated parts. Static does not fit: the content depends on the query, and the combinations are endless.</p></details>
<details><summary>2 · Caching</summary><p>The HTML for a query and filter combination is the same for everyone, so it can be cached at the CDN for a minute, keyed by the normalised query string. The basket count and greeting are fetched separately in the browser (drill 5). Prices shown are display only; the basket checks them.</p></details>
<details><summary>3 · Filters without JavaScript</summary><p>The filter panel is a real form with <code>GET</code>, so choosing filters and pressing “Apply” loads the filtered page as a normal link. JavaScript later makes it update without the button. Every filtered state then also has its own address that can be shared and cached.</p></details>
<details><summary>4 · INP</summary><p>Most likely each filter change re-renders all 24 product cards and runs the whole client-side search logic in one long task. With server rendering, a filter change fetches new HTML for the list; the client work per tap becomes small. Check the performance panel for long tasks after a tap to confirm.</p></details>
<details><summary>5 · Budget</summary><p>About 50 KB compressed for the page. The date picker alone would almost double it, so the check fails and shows the import. The fix is to load the date picker only when that filter is opened (chapter 6), or to use the browser's own date input.</p></details>
</div>
<h3>The review checklist</h3>
''' + checklist([
    ("Choosing", ["Each page type has its own rendering approach, chosen for what it is", "Documents ship as HTML with JavaScript only for interactive parts", "Personal and current data is never inside shared cached HTML"]),
    ("Measuring", ["Field Core Web Vitals at the 75th percentile, by page type and device class", "Lab runs on a simulated mid-range phone, not a laptop", "Conversion is graphed next to speed"]),
    ("The first view", ["The hero image is sized, compressed, in a modern format and announced early", "Data is fetched on the server or in parallel, never in a chain", "Late content has reserved space; fonts have a matched fallback", "The status code is decided before streaming starts"]),
    ("Interaction", ["Key actions work as links and forms before JavaScript loads", "The first browser render matches the server's HTML", "No task over 50 ms after the page appears", "Interactive parts hydrate first, or are islands"]),
    ("JavaScript", ["Code is split by route, interaction and visibility, not into dozens of tiny chunks", "Third-party scripts have owners, budgets and facades", "Each new dependency's size is checked before it is added"]),
    ("In the build", ["Per-page JavaScript budgets fail the pull request", "Lighthouse CI checks LCP and blocking time on key pages", "End-to-end tests fail on hydration warnings and run once without JavaScript"]),
])

# ------------------------------------------------------------------ the dive
DIVE = dict(
    slug="rendering-web", no=11, title="Rendering on the Web",
    sub="One product page built four ways and measured on the phone your customers actually own: when the mug appears, and when the button works.",
    summary="A deep dive on rendering web pages: Core Web Vitals, one page built client-only, server-rendered, static and as islands, six failure drills, the cost of hydration and how to cut it, loading less JavaScript, performance budgets, caching and streaming HTML, testing and monitoring.",
    builds_on="Vol. 2, notes 09, 10 and 11",
    builds_on_links=[("SSR & Hydration", "../../frontend/notes/ssr-hydration.html"), ("Islands Architecture", "../../frontend/notes/islands.html"),
                     ("Code Splitting & Lazy Loading", "../../frontend/notes/code-splitting.html")],
    notes=[("frontend", "ssr-hydration"), ("frontend", "islands"), ("frontend", "code-splitting")],
    facts=[("Example", "the product page for product 42, on a mid-range phone")],
    blurb="Core Web Vitals, one page built four ways, six failure drills, the cost of hydration, less JavaScript and budgets the build enforces.",
    chapters=[
        dict(id="recap", nav="Recap", title="Three notes in sixty seconds",
             gist="Server rendering sends HTML early and hydrates it, islands hydrate only the interactive parts, and code splitting loads code when it is needed. They sit on one line: how much of the page's work happens in the shopper's browser. The decision is which point on that line suits each page, measured on a mid-range phone.",
             body=recap),
        dict(id="fast", nav="What fast means", title="What “fast” means",
             gist="Three Core Web Vitals score a page: LCP for when the main content appears, INP for how quickly it responds to taps, and CLS for how much it jumps. Judge them on real visits at the 75th percentile, split by page and device; use lab runs on a simulated mid-range phone to find causes.",
             body=fast,
             check=[("Why can't a Lighthouse run measure INP?", "INP measures how the page responds to the shopper's taps and keys during a visit. A lab load has nobody interacting with it."),
                    ("Why report the 75th percentile and not the average?", "The average mixes fast laptops with slow phones and hides the customers having the worst experience.")]),
        dict(id="fourways", nav="Four ways", title="One page, four ways",
             gist="Client-only rendering shows the product late. Server rendering shows it early but becomes usable no sooner, because the same JavaScript must hydrate it. Static pages win on first byte with the same hydration cost. Islands ship a fraction of the JavaScript and are usable almost as soon as visible. Choose per page type, not per site.",
             body=fourways,
             check=[("Server rendering moved LCP from 4.1 s to 2.2 s but the page became usable only at 4.4 s. Why?", "The same 310 KB of JavaScript still had to download and run to hydrate the page."),
                    ("Why is a client-rendered admin tool acceptable when a client-rendered product page is not?", "Staff load the admin tool once a day on laptops; customers arrive at the product page on phones and leave within seconds.")]),
        dict(id="drills", nav="Failure drills", title="Failure drills",
             gist="Six ways rendering goes wrong: a hydration mismatch from dates and time zones, a button that looks ready but does nothing, a page that jumps as late content arrives, requests that wait for each other, a cached page showing someone else's basket, and a bundle that grows month by month.",
             body=drills,
             check=[("A delivery-time message flickers after the page loads. Which drill, and the fix?", "Drill 1, a hydration mismatch. Render something stable on both sides and fill in the local time after hydration."),
                    ("Shoppers tap “Add to basket” three times and get three mugs. What should the button be?", "A real form that posts to the basket, so it works before JavaScript loads; JavaScript then improves it.")]),
        dict(id="hydration", nav="Hydration", title="The cost of hydration: the hard problem",
             gist="Hydration downloads code for every component, downloads the data a second time, and reruns the server's work on the slowest computer in the system, all to attach event handlers. Progressive hydration reorders that work; islands, server components and resumability avoid most of it.",
             body=hydration,
             check=[("What does a server component send to the browser?", "Its HTML only. Its code is never downloaded, so it is not hydrated."),
                    ("Progressive hydration makes the page usable sooner. Why doesn't it reduce the total work?", "It still hydrates every component; it only changes the order, doing the important ones first.")]),
        dict(id="lessjs", nav="Less JavaScript", title="Loading less JavaScript",
             gist="JavaScript costs on the network and again on the processor. Split code by route, by interaction, by visibility and until idle, prefetch on intent, and avoid chains of tiny chunks. Third-party scripts are often the biggest cost and need owners, budgets and lightweight stand-ins.",
             body=lessjs,
             check=[("Why is a 300 KB script more expensive than a 300 KB image?", "The script must be parsed, compiled and run on the main thread before the page can respond; the image is mostly decoded off it."),
                    ("A chat widget adds 200 KB to every page. What is a facade?", "A lightweight button that looks like the widget and loads the real one only when tapped.")]),
        dict(id="budgets", nav="Budgets", title="Budgets, worked out",
             gist="Work back from LCP under 2.5 s on the median phone: connection, first byte, HTML and CSS, the hero image, and a margin. The hero image is the largest single item. Set per-page budgets for JavaScript, images and lab metrics that fail the build, and keep every task under 50 ms for INP.",
             body=budgets,
             check=[("Which single item usually dominates the path to LCP?", "The hero image: its size, format and how early the browser knows to fetch it."),
                    ("Why does a faster connection not fix a heavy JavaScript bundle?", "Half of its cost is running on the phone's processor, which the network does not change.")]),
        dict(id="edge", nav="Cache & stream", title="Caching and streaming HTML",
             gist="Cache the parts of a page that are the same for everyone, fetch personal parts separately, and check current values where decisions are made. Stream the shell first and slow parts later into reserved space, but decide the status code before streaming starts. Render at build time, near the data, or at the edge according to what the page needs.",
             body=edge,
             check=[("The product does not exist, but the page was already streaming with 200 OK. What went wrong?", "The existence check should have happened before streaming started, so the server could answer 404."),
                    ("Why render personalisation at the edge but not database-heavy pages?", "The edge is near the shopper but far from the database; several queries from there cost many long round trips.")]),
        dict(id="running", nav="Running it", title="Testing it and running it",
             gist="In every pull request, check bundle sizes against budgets, run Lighthouse on key pages, test the key action with JavaScript off and fail on hydration warnings. In production, collect Core Web Vitals from real visits by page and device, and graph conversion next to them.",
             body=running,
             check=[("LCP worsened only on low-end devices, on all page types. Where do you look first?", "Something shared and heavy: JavaScript or image weight in the layout, or a new third-party script."),
                    ("What does loading the page with JavaScript disabled prove?", "That the key actions, such as adding to the basket, work before scripts load, which is what shoppers on slow phones depend on.")]),
        dict(id="tools", nav="Tools & lab", title="Tools, a lab and the checklist",
             gist="Frameworks offer per-route choices; islands, server components and resumability cut hydration; Lighthouse, WebPageTest and the web-vitals library measure. The lab rebuilds the search results page, and the checklist turns the deep dive into review questions.",
             body=tools),
    ],
    sources="web.dev: “Web Vitals”, “Interaction to Next Paint”, “Rendering on the Web” (Jason Miller and Addy Osmani) and “Optimize Largest Contentful Paint”. Jason Miller, “Islands Architecture” (2020). The React documentation on Server Components and the Astro documentation on islands. Alex Russell, “The Performance Inequality Gap” (2024). The Lighthouse and web-vitals documentation.",
)
