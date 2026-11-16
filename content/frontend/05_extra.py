# Vol. 2 · extra notes (November 2026): Debounce & Throttle, Web Workers, Offline-First Sync.
# Numbered 16–18 so earlier note URLs and PDF names stay the same.

# ------------------------------------------------------------------ 16 Debounce & throttle
dt_problem = Doodle(760, 250, "Doodle of a search box that fires on every keystroke. Typing running shoes, 13 characters, sends 13 search requests. Answers come back out of order, the results flicker, and the search service sees thirteen times the load it needs. A scroll handler on the same page runs 120 times a second and makes scrolling stutter.",
                    "One word typed, thirteen requests sent.")
dt_problem.box(20, 40, 220, 60, "“running shoes”", "y", sub="13 keystrokes", size=17, subsize=13)
for i in range(13):
    dt_problem.line(f"M244 70 L{301 + i * 34} 150", thin=True)
dt_problem.msgs(290, 152, 13, fill="pink", size=22, gap=12)
dt_problem.note(520, 60, "13 requests · answers out of order", "red", size=16)
dt_problem.note(520, 86, "results flicker", "red", size=16)
dt_problem.note(380, 222, "and onScroll runs 120× a second → janky scrolling", "red", size=16)

dt_analogy = Doodle(760, 250, "Doodle of a lift. The lift door waits until people stop walking in for a few seconds before it closes: that is debounce. A tram leaves the stop at most once every five minutes, however many people arrive: that is throttle.",
                    "The lift waits for a pause (debounce). The tram leaves at most every 5 minutes (throttle).")
dt_analogy.box(20, 40, 340, 150, None, "paper")
dt_analogy.head(190, 70, "lift door: debounce", size=18)
dt_analogy.note(190, 110, "someone steps in → wait 3 s again", size=15)
dt_analogy.note(190, 140, "closes after 3 s with no one new", "green", size=15)
dt_analogy.box(400, 40, 340, 150, None, "paper")
dt_analogy.head(570, 70, "tram: throttle", size=18)
dt_analogy.note(570, 110, "leaves at most every 5 minutes", size=15)
dt_analogy.note(570, 140, "however many people arrive", "green", size=15)

dt_how = Doodle(760, 280, "Events on a timeline and what each technique runs. The raw events arrive in two bursts. Debounce runs once after each burst, when the user has paused for 300 milliseconds. Throttle runs at most once every 200 milliseconds during the bursts, so it keeps responding while the events continue.",
                "Debounce: once, after the pause. Throttle: regularly, during the burst.")
ev = [40, 60, 80, 100, 120, 140, 160, 330, 350, 370, 390]
dt_how.text(20, 50, "events", "t-head", anchor="start", size=15)
for x in ev:
    dt_how.line(f"M{x + 200} 36 V60", thin=True)
dt_how.text(20, 130, "debounce 300 ms", "t-head", anchor="start", size=15)
for x in (160 + 200 + 60, 390 + 200 + 60):
    dt_how.circle(x, 124, 9, fill="green")
dt_how.text(20, 210, "throttle 200 ms", "t-head", anchor="start", size=15)
for x in (40, 120, 330, 390):
    dt_how.circle(x + 200, 204, 9, fill="blue")
dt_how.arrow(20, 250, 740, 250)
dt_how.note(740, 274, "time →", anchor="end", size=15)

DEBOUNCE_THROTTLE = dict(
    slug="debounce-throttle",
    kicker="a.k.a. “not on every keystroke”",
    tldr="Some events fire far more often than you need to react: keystrokes, scroll, resize, mouse moves. <b>Debounce</b> runs the handler once, <b>after the events stop</b> for a moment (search-as-you-type, autosave). <b>Throttle</b> runs it <b>at most once per interval</b> while events keep coming (scroll position, drag, infinite scroll). Cancel the work that a newer event made obsolete, and clean up timers when the component goes away.",
    chips=[("Family", "rendering &amp; performance"), ("Debounce for", "search, autosave, validation, resize end"), ("Throttle for", "scroll, drag, pointer move, analytics"), ("Pairs with", "custom hooks, server-state cache, rate limiter")],
    problem="""  <p class="lead">A search box calls the API on every keystroke. Typing “running shoes” sends <span class="hl-pink">13 requests</span>; the answers come back out of order and the results flicker. On the same page a scroll handler runs 120 times a second, measuring the layout each time, and scrolling stutters.</p>
  <ul>
    <li>Each event triggers <b>expensive work</b> (a request, a layout read, a re-render) the user never sees.</li>
    <li>The server takes <b>many times the load</b> the feature needs.</li>
    <li>Slow handlers on high-frequency events block the main thread and make the page feel broken.</li>
  </ul>""",
    problem_figs=[dt_problem],
    analogy_side="the lift and the tram",
    analogy="""  <p>A <b>lift door</b> waits until nobody has stepped in for a few seconds, then closes: every new person restarts the wait. That's debounce. A <b>tram</b> leaves the stop at most every five minutes, however many people arrive: that's throttle. Both serve everyone, without moving for every single person.</p>""",
    analogy_figs=[dt_analogy],
    map=[("Someone steps into the lift", "A new event resets the debounce timer"),
         ("The door closes after a quiet moment", "The debounced handler runs once"),
         ("The tram timetable", "The throttle interval"),
         ("Passengers waiting for the next tram", "Events during the interval; the last one is used (trailing edge)"),
         ("The lift leaving without someone who just arrived", "Work for an old value, cancelled by a newer one")],
    how_side="two timers, two shapes",
    how="""  <p>Debounce keeps one timer and restarts it on every event; when it finally fires, it runs once with the latest value. Throttle runs at the first event, then ignores events until the interval passes, usually running once more at the end so the last value isn't lost. Neither one stops an old request that's already on its way, so cancel those with an <code>AbortController</code>.</p>""",
    how_figs=[dt_how],
    steps=[("Pick the shape", "React to the final value? Debounce. Need steady updates while it happens? Throttle."),
           ("Pick the time", "Debounce search at 200–300 ms, autosave at 1–2 s; throttle scroll and drag at 50–100 ms (or once per animation frame)."),
           ("Use the latest value", "The handler reads the newest input when it fires, not the one from the first event."),
           ("Cancel stale work", "Abort the previous request when a new one starts, so an old answer can't overwrite a newer one."),
           ("Clean up", "Cancel pending timers when the component unmounts; flush pending saves before navigating away.")],
    vocab=[("Debounce", "Run once after events stop for a set time."),
           ("Throttle", "Run at most once per interval while events continue."),
           ("Leading / trailing edge", "Run at the start of a burst, at the end, or both."),
           ("requestAnimationFrame", "Run once per screen frame: the natural throttle for visual work."),
           ("AbortController", "Cancels a fetch that is no longer needed."),
           ("Passive listener", "A scroll or touch listener that promises not to block scrolling.")],
    code=dict(file="useDebouncedSearch.ts", note="React + TypeScript", src="""
import { useEffect, useState } from "react";

export function useDebouncedValue<T>(value: T, ms = 250) {
  const [debounced, setDebounced] = useState(value);
  useEffect(() => {
    const t = setTimeout(() => setDebounced(value), ms);   // restart on every change
    return () => clearTimeout(t);                           // and on unmount
  }, [value, ms]);
  return debounced;
}

export function useSearch(query: string) {
  const q = useDebouncedValue(query.trim(), 250);
  const [results, setResults] = useState<Product[]>([]);
  useEffect(() => {
    if (!q) return setResults([]);
    const ctrl = new AbortController();                     // cancel the previous request
    fetch(`/api/search?q=${encodeURIComponent(q)}`, { signal: ctrl.signal })
      .then((r) => r.json()).then(setResults).catch(() => {});
    return () => ctrl.abort();
  }, [q]);
  return results;
}
"""),
    tools="tools: lodash <code>debounce</code> / <code>throttle</code>, <code>use-debounce</code> (React), RxJS <code>debounceTime</code> / <code>throttleTime</code>, TanStack Pacer, <code>requestAnimationFrame</code>, passive event listeners, IntersectionObserver (often replaces scroll handlers entirely).",
    gains=["<b>Far fewer requests</b> and re-renders.",
           "<b>Smoother scrolling</b> and typing.",
           "<b>Calmer results</b>: no flicker from out-of-order answers (with cancellation).",
           "<b>Less server load</b> for the same feature."],
    losses=["<b>A small delay</b> before the reaction.",
            "<b>Timers to manage</b>: stale closures, cleanup on unmount.",
            "<b>Harder tests</b>: need fake timers.",
            "<b>Wrong choice hurts</b>: debounced scroll feels dead; throttled search wastes calls."],
    baseline="Each line compares <b>a handler that runs on every event</b> to <b>the same handler debounced or throttled</b>.",
    ratings=[(4, 3, "A timer and a little cleanup."),
             (3, 4, "One hook or helper, used everywhere."),
             (4, 3, "Fake timers needed in tests."),
             (3, 4, "Rate is set in one place."),
             (2, 5, "Most events no longer do work."),
             (4, 4, "A few lines, or a tiny library."),
             (3, 4, "Screen readers aren't flooded with updates."),
             (3, 4, "Fewer “why is it so slow” bugs."),
             (3, 3, "Neutral.")],
    pitfalls=[("Debouncing scroll feedback", "A sticky header only updates after scrolling stops, and looks broken.", "throttle (or requestAnimationFrame) for anything that should follow the finger."),
              ("A new debounce on every render", "<code>debounce(fn)</code> inside a component creates a fresh timer each render, so nothing is ever debounced.", "create it once (useMemo / useRef) or debounce the value, as in the hook above."),
              ("Old answers win", "Debouncing fewer requests doesn't stop an old one landing after a newer one.", "abort the previous request, or ignore answers for an old query."),
              ("Losing the last value", "A leading-only throttle drops the final scroll position or the last keystroke.", "use trailing (or both) edges for anything that saves or shows the final state.")],
    use=["Search-as-you-type, filters and validation while typing.",
         "Autosave of forms and documents.",
         "Scroll, resize, drag and pointer-move handlers.",
         "Analytics events that fire continuously."],
    skip=["Discrete actions like a submit or a click (use a disabled state or idempotency instead).",
          "Visibility checks: IntersectionObserver does it without scroll handlers.",
          "The work is already cheap and synchronous."],
    related=["<b>Custom hooks</b>", "<b>Server-state cache</b>", "<b>Web workers</b>", "<b>Rate limiter</b> (Vol. 1)"],
    quiz=[("Debounce or throttle for search-as-you-type?", "Debounce: you want one request after the user pauses, with the final text."),
          ("Debounce or throttle for updating a progress bar while scrolling?", "Throttle (or requestAnimationFrame): it must keep updating while the scroll continues."),
          ("Why doesn't debouncing alone fix out-of-order search results?", "An earlier request can still finish after a later one; cancel it or ignore old answers."),
          ("Why can calling debounce(fn) inside a React component fail?", "A new debounced function is created on every render, so each event gets its own timer.")],
    quiz_sit=[("An autosave debounced at 2 seconds loses the user's last edit when they close the tab right after typing. What do you change?",
               "Flush the pending save when the page is hidden or the user navigates away (visibilitychange / pagehide, sendBeacon or keepalive fetch), and show “saving…” while a save is pending, so a debounced save is never silently dropped.")],
    try_it="Add a counter to a search box's input handler and type a few words: count the calls. Debounce it at 250 ms and count again. Then throttle a scroll handler that logs <code>scrollY</code> to 100 ms, compare the number of calls in the console, and check scrolling in the performance panel before and after.",
    remember="<span class=\"hl\">Debounce</span> waits for the pause. <span class=\"hl\">Throttle</span> keeps a steady beat.",
    sources=["David Corbacho, “Debouncing and Throttling Explained Through Examples” (CSS-Tricks, 2016).",
             "MDN Web Docs, “Debounce” and “Throttle” glossary entries; “AbortController”.",
             "web.dev, “Optimize Interaction to Next Paint”.",
             "Lodash documentation, <code>_.debounce</code> and <code>_.throttle</code>."],
)

# ------------------------------------------------------------------ 17 Web workers
ww_problem = Doodle(760, 250, "Doodle of a frozen page. Parsing a 40 megabyte CSV file and computing statistics takes 2.8 seconds on the main thread. During that time the spinner stops spinning, clicks do nothing, and the browser shows a page unresponsive warning.",
                    "2.8 seconds of work on the main thread: 2.8 seconds of a frozen page.")
ww_problem.box(20, 50, 700, 60, None, "pink", stroke="red")
ww_problem.head(370, 88, "main thread: parse 40 MB CSV · 2,800 ms", size=17, color="red")
for x, lab in [(120, "tap"), (300, "scroll"), (480, "tap")]:
    ww_problem.arrow(x, 170, x, 116, color="red", dash=True)
    ww_problem.note(x, 192, f"{lab}: ignored", "red", size=15)
ww_problem.note(380, 232, "spinner frozen · “page unresponsive”", "red", size=16)

ww_analogy = Doodle(760, 250, "Doodle of a restaurant with a waiter and a kitchen. The waiter keeps talking to guests and taking orders. Long jobs, like baking bread, go to the kitchen, which works on them separately and sends a message back when the bread is ready. The waiter never stops serving to bake.",
                    "The waiter keeps serving; the kitchen bakes and sends word when it's done.")
ww_analogy.box(20, 60, 260, 110, "waiter", "y", sub="talks to guests, never bakes", size=19, subsize=14)
ww_analogy.box(480, 60, 260, 110, "kitchen", "green", sub="long jobs, out of sight", size=19, subsize=14)
ww_analogy.arrow(284, 95, 476, 95, label="order: bake bread", lx=380, ly=84)
ww_analogy.arrow(476, 140, 284, 140, label="“bread is ready”", lx=380, ly=164)
ww_analogy.note(380, 222, "messages only: they don't share a counter", "pen", size=16)

ww_how = Doodle(760, 270, "Main thread and worker. The main thread keeps handling taps and drawing frames. It posts the file to a web worker, transferring the buffer instead of copying it. The worker parses and computes on its own thread, posts progress messages, and finally posts the result back, which the main thread renders.",
                "postMessage in, postMessage out; the main thread stays free.")
ww_how.box(20, 30, 300, 60, "main thread", "y", sub="taps · frames · rendering", size=18, subsize=13)
ww_how.box(440, 30, 300, 60, "web worker", "green", sub="parse · compute", size=18, subsize=13)
ww_how.line("M170 96 V240", thin=True)
ww_how.line("M590 96 V240", thin=True)
ww_how.arrow(174, 120, 586, 120, label="postMessage(file buffer, [transfer])", lx=380, ly=110)
ww_how.arrow(586, 165, 174, 165, dash=True, label="progress 40%", lx=380, ly=156)
ww_how.arrow(586, 210, 174, 210, color="green", label="result: stats", lx=380, ly=201)
ww_how.note(170, 262, "still answering taps", "green", size=15)

WEB_WORKERS = dict(
    slug="web-workers",
    kicker="a.k.a. “do the heavy work off the main thread”",
    tldr="The browser's <b>main thread</b> runs your JavaScript, handles input and draws frames. A long task there (parsing a big file, image processing, crypto, search over thousands of items) <b>freezes the page</b>. A <b>Web Worker</b> runs code on another thread: you send it data with <code>postMessage</code>, it works, it posts the result back. Use it for CPU-heavy work over ~50 ms; transfer large buffers instead of copying them; keep DOM work on the main thread.",
    chips=[("Family", "rendering &amp; performance"), ("Kinds", "dedicated workers · shared workers · service workers (a different job)"), ("Can't touch", "the DOM"), ("Pairs with", "code splitting, debounce &amp; throttle, offline-first sync")],
    problem="""  <p class="lead">An import screen parses a 40 MB CSV and computes column statistics in the browser. It takes <span class="hl-pink">2.8 seconds on the main thread</span>: the spinner stops, taps are ignored, and the browser offers to kill the page.</p>
  <ul>
    <li>JavaScript, input handling and rendering share <b>one thread</b>. Anything over ~50 ms is noticeable; over a few hundred feels broken.</li>
    <li>Splitting the work with <code>setTimeout</code> helps a little but makes the code hard to follow.</li>
    <li>Interaction to Next Paint (INP), a Core Web Vital, gets worse with every long task.</li>
  </ul>""",
    problem_figs=[ww_problem],
    analogy_side="the waiter and the kitchen",
    analogy="""  <p>A <b>waiter</b> keeps talking to guests and taking orders. Baking bread would stop all of that, so it goes to the <b>kitchen</b>, which works out of sight and <b>sends word</b> when the bread is ready. They don't reach into each other's work; they pass orders and plates.</p>""",
    analogy_figs=[ww_analogy],
    map=[("The waiter", "The main thread: input, rendering, the DOM"),
         ("The kitchen", "A web worker on its own thread"),
         ("An order slip", "<code>postMessage(data)</code>"),
         ("“Bread is ready”", "The worker's <code>message</code> event with the result"),
         ("Not sharing a counter", "Separate memory: data is copied or transferred, not shared")],
    how_side="messages between two threads",
    how="""  <p>Create a worker from a separate module. Send it the input; it runs on its own thread with its own event loop and posts messages back. Large binary data (an <code>ArrayBuffer</code>) can be <b>transferred</b> instead of copied, which is instant. Libraries like Comlink make the messaging look like ordinary async function calls.</p>""",
    how_figs=[ww_how],
    steps=[("Find the long task", "Record in the performance panel; look for tasks over 50 ms that are pure computation."),
           ("Move it to a worker module", "<code>new Worker(new URL(\"./parse.worker.ts\", import.meta.url), { type: \"module\" })</code>. Bundlers handle the rest."),
           ("Send data, transfer buffers", "Pass the file's ArrayBuffer in the transfer list so it isn't copied."),
           ("Report progress, allow cancel", "Post progress messages; terminate the worker (or send a cancel message) if the user leaves."),
           ("Keep the DOM on the main thread", "The worker returns data; the main thread renders it.")],
    vocab=[("Main thread", "Runs JavaScript, input and rendering for the page."),
           ("Long task", "Main-thread work over 50 ms."),
           ("Web worker", "A script running on a separate thread."),
           ("postMessage", "Sends a copy (structured clone) of data to the other side."),
           ("Transferable", "Data like ArrayBuffer whose ownership moves instead of copying."),
           ("Comlink", "A library that wraps postMessage as async function calls.")],
    code=dict(file="parse.worker.ts + import.ts", note="Vite / any modern bundler", src="""
// parse.worker.ts: runs on its own thread
self.onmessage = (e: MessageEvent<ArrayBuffer>) => {
  const text = new TextDecoder().decode(e.data);
  const rows = text.split("\\n");
  const stats = computeStats(rows, (pct) => self.postMessage({ type: "progress", pct }));
  self.postMessage({ type: "done", stats });
};

// import.ts: on the main thread
export function parseInWorker(file: File, onProgress: (pct: number) => void) {
  const worker = new Worker(new URL("./parse.worker.ts", import.meta.url), { type: "module" });
  return new Promise<Stats>(async (resolve, reject) => {
    worker.onmessage = (e) => {
      if (e.data.type === "progress") onProgress(e.data.pct);
      else { resolve(e.data.stats); worker.terminate(); }
    };
    worker.onerror = reject;
    const buf = await file.arrayBuffer();
    worker.postMessage(buf, [buf]);       // transfer: no 40 MB copy
  });
}
"""),
    tools="tools: Web Workers API, Comlink, Vite / webpack worker imports, Partytown (third-party scripts in a worker), OffscreenCanvas (drawing in a worker), WebAssembly in workers for number crunching.",
    gains=["<b>The page stays responsive</b> during heavy work.",
           "<b>Better INP</b> and no “unresponsive” warnings.",
           "<b>Real parallelism</b> on multi-core devices.",
           "<b>Progress and cancel</b> become easy to add."],
    losses=["<b>No DOM</b> in the worker: results must come back.",
            "<b>Copying costs</b> for large non-transferable data.",
            "<b>More moving parts</b>: a second file, messages, errors.",
            "<b>Start-up cost</b> (tens of ms) for tiny jobs."],
    baseline="Each line compares <b>the heavy work on the main thread</b> to <b>the same work in a web worker</b>.",
    ratings=[(4, 3, "A message protocol to design."),
             (3, 4, "A worker module can serve several screens."),
             (3, 4, "Pure computation in a module is easy to unit-test."),
             (3, 3, "Neutral."),
             (2, 5, "No long tasks on the main thread."),
             (3, 3, "Neutral: the code moves, it doesn't grow."),
             (2, 4, "Keyboard and screen readers keep working during the work."),
             (3, 3, "Debugging across threads takes practice."),
             (3, 3, "Neutral.")],
    pitfalls=[("Chatty messages", "The worker posts a message per row, and the main thread drowns in messages.", "batch: post progress every few percent and one final result."),
              ("Copying huge data", "A 40 MB object is cloned into the worker and back, freezing both sides.", "transfer ArrayBuffers; send only what the worker needs."),
              ("A worker for 2 ms of work", "Worker start-up and messaging cost more than the work.", "measure first; use a worker for tasks over ~50 ms."),
              ("Forgetting to clean up", "Each import creates a worker that never ends.", "terminate when done, or reuse one long-lived worker.")],
    use=["Parsing, compressing or encrypting large files in the browser.",
         "Image, audio or video processing.",
         "Searching or sorting large lists on the client.",
         "Any pure computation over ~50 ms that blocks input."],
    skip=["The work is waiting on the network: async/await already frees the thread.",
          "The work is mostly DOM changes: optimise rendering instead.",
          "The job is tiny or rare."],
    related=["<b>Debounce &amp; throttle</b>", "<b>Code splitting &amp; lazy loading</b>", "<b>List virtualization</b>", "<b>Offline-first sync</b>"],
    quiz=[("Why does heavy JavaScript freeze the page?", "The main thread runs JavaScript, handles input and renders frames; while it computes, it can't do the other two."),
          ("What can't a web worker do?", "Touch the DOM; it must send results to the main thread to render."),
          ("What does transferring an ArrayBuffer save?", "The copy: ownership moves to the worker instantly, instead of cloning the bytes."),
          ("Does fetching data need a worker?", "No; network waits are already asynchronous and don't block the main thread.")],
    quiz_sit=[("Typing in a client-side search box over 20,000 products feels sluggish: each keystroke runs a fuzzy search that takes 120 ms. What do you do?",
               "Debounce the input (200 ms), and move the fuzzy search into a web worker that holds the index, so typing never waits on it. Show results when the worker answers, and ignore answers for an outdated query.")],
    try_it="Write a function that does 2 seconds of busy work and call it from a button: try clicking another button while it runs. Move the function into a web worker and post the result back, then try again. Record both runs in the performance panel and compare the long tasks.",
    remember="The main thread is for <span class=\"hl\">people</span>. Heavy lifting goes to the <span class=\"hl\">kitchen</span>.",
    sources=["MDN Web Docs, “Using Web Workers” and “Transferable objects”.",
             "web.dev, “Optimize long tasks” and “Interaction to Next Paint (INP)”.",
             "Surma, “When should you be using Web Workers?” (2019).",
             "Comlink (github.com/GoogleChromeLabs/comlink)."],
)

# ------------------------------------------------------------------ 18 Offline-first sync
of_problem = Doodle(760, 250, "Doodle of a field app that needs the network. A warehouse worker counts stock in a basement with no signal. Every save shows a spinner and then an error, the counts typed so far are lost, and the worker writes them on paper to type in again later.",
                    "No signal in the basement: every save fails, and the work is lost.")
of_problem.box(20, 60, 200, 100, "stock count", "y", sub="typed in the basement", size=18, subsize=14)
of_problem.arrow(224, 110, 336, 110, color="red", dash=True, label="save…", lx=280, ly=100)
of_problem.box(340, 70, 160, 80, "no signal", "pink", stroke="red", size=18)
of_problem.note(620, 90, "spinner → error", "red", size=16)
of_problem.note(620, 120, "counts lost", "red", size=16)
of_problem.note(620, 150, "back to paper", "red", size=16)

of_analogy = Doodle(760, 250, "Doodle of a notebook and an office. A field worker writes everything in a notebook first, so work never waits for the office. When they pass a phone, they call the office and read out the new entries; if the office has a different note for the same item, they agree which one is right.",
                    "Write in your notebook first. Phone the office when you can.")
of_analogy.icon("book", 40, 60, 1.6, fill="y")
of_analogy.note(90, 200, "notebook: always works")
of_analogy.arrow(190, 110, 506, 110, dash=True, label="when there's signal: send new entries", lx=348, ly=98)
of_analogy.arrow(506, 140, 190, 140, dash=True, label="get the office's changes", lx=348, ly=164)
of_analogy.box(510, 70, 230, 100, "office", "blue", sub="settles any clash", size=19, subsize=14)

of_how = Doodle(760, 290, "Offline-first data flow. The UI reads and writes a local database in the browser, so it always responds. Each change is also written to an outbox. A sync process sends the outbox to the server when online, with retries, and pulls changes from other devices since the last sync. Conflicts are resolved by a rule, such as last writer wins per field, or shown to the user.",
                "The UI only talks to the local store. Sync does the network, whenever it can.")
of_how.box(20, 100, 140, 70, "UI", "y", size=19)
of_how.arrow(164, 135, 226, 135, both=True)
of_how.db(300, 100, "local store (IndexedDB)", w=120)
of_how.box(390, 200, 150, 60, "outbox", "paper", sub="pending changes", size=16, subsize=12)
of_how.arrow(330, 160, 400, 200, dash=True)
of_how.box(470, 70, 120, 70, "sync", "green", sub="retries", size=18, subsize=13)
of_how.arrow(540, 196, 540, 144, dash=True)
of_how.arrow(594, 90, 656, 90, label="push", lx=625, ly=80)
of_how.arrow(656, 120, 594, 120, label="pull", lx=625, ly=140)
of_how.box(660, 70, 90, 70, "server", "blue", size=16)
of_how.arrow(466, 105, 364, 120, dash=True)

OFFLINE_FIRST = dict(
    slug="offline-first",
    kicker="a.k.a. “local first, sync later”",
    tldr="For apps used where the network is bad (warehouses, trains, field work), make the <b>local store the source the UI reads and writes</b>: IndexedDB in the browser, SQLite on mobile. Every change goes into an <b>outbox</b>; a <b>sync</b> step pushes it when online, pulls other devices' changes, and resolves <b>conflicts</b> by a rule you chose on purpose. The app never waits for the network, and no work is lost.",
    chips=[("Family", "state &amp; data"), ("Local store", "IndexedDB · SQLite · OPFS"), ("Sync tools", "Replicache, PowerSync, ElectricSQL, CouchDB/PouchDB, CRDT libraries"), ("Pairs with", "optimistic UI, idempotent consumer, service workers")],
    problem="""  <p class="lead">A warehouse worker counts stock in a basement with no signal. Each save spins, then fails; <span class="hl-pink">the counts typed so far are lost</span>, and the worker goes back to paper and types it all in again upstairs.</p>
  <ul>
    <li>Apps that call the server for every read and write <b>stop working</b> the moment the network does.</li>
    <li>Flaky connections are worse than none: requests time out halfway and users don't know what was saved.</li>
    <li>Two devices editing the same record offline will <b>disagree</b> when they reconnect.</li>
  </ul>""",
    problem_figs=[of_problem],
    analogy_side="the field notebook",
    analogy="""  <p>A field worker writes everything in a <b>notebook</b> first, so work never waits for the office. Whenever there's signal, they <b>phone the office</b>, read out the new entries and hear what changed there. If the office has a different note for the same item, they settle it with a rule both sides agreed on.</p>""",
    analogy_figs=[of_analogy],
    map=[("The notebook", "The local store the UI reads and writes"),
         ("New entries not yet phoned in", "The outbox of pending changes"),
         ("Phoning the office when there's signal", "Background sync: push, then pull"),
         ("“What changed at the office?”", "Pulling changes since the last sync (a cursor or version)"),
         ("Settling a clash", "The conflict rule: per-field last writer, merge, or ask the user")],
    how_side="local store, outbox, sync",
    how="""  <p>The UI never calls the server directly. Writes go to the local store and an outbox in one local transaction. A sync loop runs whenever there's a connection: it sends outbox entries (with ids, so retries are safe), then pulls changes since its last cursor and applies them locally. The server decides the final order and resolves conflicts by the agreed rule.</p>""",
    how_figs=[of_how],
    steps=[("Choose what works offline", "Which screens and data must work without a network; download that data ahead of time."),
           ("Read and write locally", "IndexedDB (via Dexie or a sync library) in the browser, SQLite on mobile. The UI updates instantly."),
           ("Queue changes in an outbox", "Each change with a unique id, so sending it twice is harmless."),
           ("Sync in both directions", "Push the outbox when online (retry with backoff), then pull changes since the last cursor."),
           ("Decide conflicts on purpose", "Per field last writer wins for simple data; counters as increments, not totals; CRDTs for shared documents; show the user when it matters.")],
    vocab=[("Offline-first", "The app works fully without a network and syncs when it can."),
           ("Local store", "The on-device database the UI uses (IndexedDB, SQLite)."),
           ("Outbox", "The queue of local changes not yet confirmed by the server."),
           ("Sync cursor", "A marker of the last server change this device has seen."),
           ("Conflict", "Two devices changed the same thing differently while apart."),
           ("CRDT", "A data type that merges concurrent edits without conflicts.")],
    code=dict(file="stock-db.ts", note="Dexie (IndexedDB) + a small sync loop", src="""
import Dexie from "dexie";
const db = new Dexie("stock");
db.version(1).stores({ counts: "sku, updatedAt", outbox: "++seq, id" });

export async function saveCount(sku: string, qty: number) {
  const change = { id: crypto.randomUUID(), sku, qty, at: Date.now() };
  await db.transaction("rw", db.counts, db.outbox, async () => {
    await db.counts.put({ sku, qty, updatedAt: change.at });   // the UI reads this at once
    await db.outbox.add(change);                                // and sync sends this later
  });
}

export async function sync() {
  for (const c of await db.outbox.orderBy("seq").toArray()) {
    const r = await fetch("/api/counts", { method: "POST", body: JSON.stringify(c),
                                          headers: { "Idempotency-Key": c.id } });
    if (!r.ok) return;                                          // try again on the next sync
    await db.outbox.delete(c.seq);
  }
  // then pull: GET /api/counts?since=<cursor> and put each change into db.counts
}
addEventListener("online", sync);
"""),
    tools="tools: Dexie.js (IndexedDB), SQLite (mobile, or WASM + OPFS in the browser), Replicache, PowerSync, ElectricSQL, RxDB, CouchDB/PouchDB, Automerge and Yjs (CRDTs), Workbox Background Sync.",
    gains=["<b>Always responsive</b>: no spinner for local reads and writes.",
           "<b>No lost work</b> on bad connections.",
           "<b>Works in the field</b>: basements, trains, planes.",
           "<b>Fewer requests</b>: batches instead of one call per action."],
    losses=["<b>Conflicts</b> must be designed for, not discovered.",
            "<b>Two copies of the data</b>: storage limits, schema migrations on the device.",
            "<b>Harder to reason about</b>: “saved” means saved locally.",
            "<b>Security</b>: data at rest on devices, and access that changes while offline."],
    baseline="Each line compares <b>an app that calls the server for every read and write</b> to <b>a local store with an outbox and sync</b>.",
    ratings=[(4, 2, "Sync, conflicts and local migrations are real work."),
             (3, 3, "Neutral."),
             (3, 3, "Sync logic needs its own tests: offline, retry, conflict."),
             (3, 2, "Schema changes reach every device's local store."),
             (2, 5, "Reads and writes are local and instant."),
             (3, 2, "A local database library and sync code."),
             (3, 3, "Neutral."),
             (3, 3, "Good libraries help a lot; hand-rolled sync is hard."),
             (3, 3, "Neutral.")],
    pitfalls=[("Conflicts discovered in production", "Two devices edit the same stock count offline; one silently wins.", "pick a rule per kind of data before building, and store changes as operations (+3) where you can."),
              ("Unsafe retries", "A sync that times out is sent again and doubles a change.", "a unique id per change, and an idempotent server endpoint."),
              ("“Saved” that isn't", "Users think a change reached the office while it's still in the outbox.", "show pending and synced states, and the last sync time."),
              ("Stale permissions and schema", "A device offline for a week syncs data it may no longer see, in an old shape.", "check permissions on the server for every change, and version the local schema.")],
    use=["Field, warehouse, travel or retail apps with bad connections.",
         "Note-taking, forms and documents where losing input is unacceptable.",
         "Apps that should feel instant everywhere."],
    skip=["Data that must be live and exact (bank balances, seat booking at checkout).",
          "Users are always online on fast connections; optimistic UI is enough.",
          "The data is too large or sensitive to keep on devices."],
    related=["<b>Optimistic UI</b>", "<b>Server-state cache</b>", "<b>Idempotent consumer</b> (Vol. 1)", "<b>Transactional outbox</b> (Vol. 1)"],
    quiz=[("In offline-first, what does the UI read and write?", "The local store on the device; the network is only used by sync."),
          ("Why does each change need a unique id?", "So a change sent twice (after a timeout) can be recognised and applied only once."),
          ("Why store a stock change as “+3” instead of “now 15”?", "Increments from two devices can both be applied; two totals conflict and one is lost."),
          ("When is offline-first a bad fit?", "When data must be live and exact, like a checkout or a seat booking, or too sensitive to keep on devices.")],
    quiz_sit=[("Two warehouse tablets counted the same shelf while offline: one says 12, the other 15. They sync an hour later and the server keeps whichever arrives last. Users complain counts “jump around”. What do you change?",
               "Make the conflict rule explicit: store each count with who and when, flag simultaneous counts of the same shelf for review instead of silently overwriting, and for adjustments send operations (+3, −2) rather than totals, so they can be merged.")],
    try_it="Take a small to-do or notes app. Store items in IndexedDB (with Dexie) and add an outbox table; make the UI read only from IndexedDB. Turn the network off in devtools, add and edit items, then turn it back on and watch the outbox drain. Edit the same item in two tabs while offline and see which rule your sync applies.",
    remember="Write to the <span class=\"hl\">notebook</span> first. Phone the office <span class=\"hl\">when you can</span>, and agree how to settle clashes.",
    sources=["Martin Kleppmann, Adam Wiggins, Peter van Hardenberg and Mark McGranaghan, “Local-first software” (Ink &amp; Switch, 2019).",
             "MDN Web Docs, “IndexedDB API” and “Using the Origin Private File System”.",
             "Replicache documentation, “How Replicache Works”.",
             "Marc Shapiro et al., “Conflict-free Replicated Data Types” (2011)."],
)

NOTES = [DEBOUNCE_THROTTLE, WEB_WORKERS, OFFLINE_FIRST]
