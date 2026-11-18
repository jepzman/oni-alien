# Vol. 8 · Inside the Application · Classic patterns: Strategy & Command as Functions, Decorator & Middleware,
# Adapter & Facade, The Pattern Museum. Source: Gamma, Helm, Johnson & Vlissides, Design Patterns (1994).

# ------------------------------------------------------------------ 15 Strategy & Command as Functions
sc_problem = Doodle(760, 270, "Doodle of class explosion for simple behaviour. To support five discount rules, the code has a DiscountStrategy interface, five classes of three lines each, a DiscountStrategyFactory with a switch, and a registry. For background jobs, every job is a Command class with an execute method and a CommandHandlerFactory. Reading one discount rule means opening four files.",
                    "An interface, five tiny classes, a factory and a registry, for five one-line discount rules.")
sc_problem.box(270, 20, 220, 50, "DiscountStrategy", "paper", size=16)
for i in range(5):
    sc_problem.box(20 + i * 148, 110, 132, 46, f"Rule{i + 1}", "paper", size=15)
    sc_problem.arrow(86 + i * 148, 106, 380, 74, dash=True)
sc_problem.box(220, 190, 320, 50, "DiscountStrategyFactory", "pink", stroke="red", size=16)
sc_problem.note(380, 262, "four files to read one rule", "red")

sc_analogy = Doodle(760, 250, "Doodle of a navigation app and a to-do slip. In the navigation app you pick how to travel: fastest, shortest or avoid tolls. The app just swaps the route rule. On a kitchen order slip, the waiter writes down the request, table four, one soup, and it waits in a queue until the chef picks it up, or gets torn up if cancelled.",
                     "Pick a route rule in the app (strategy); a written order slip waits in a queue (command).")
sc_analogy.box(20, 40, 340, 120, None, "y")
sc_analogy.head(190, 74, "route: fastest ▾")
sc_analogy.text(190, 112, "shortest · avoid tolls")
sc_analogy.box(400, 40, 340, 120, None, "paper")
sc_analogy.head(570, 74, "order slip")
sc_analogy.text(570, 112, "table 4: 1 soup")
sc_analogy.note(190, 200, "strategy: swap the rule", "pen")
sc_analogy.note(570, 200, "command: a request as data", "pen")

sc_how = Doodle(760, 320, "The modern forms. Strategy: a map from discount name to a function from basket to money; the checkout looks up and calls the function. Command: a plain data object, like a reserve stock command with an order ID, stored in a queue table, and one handler function per command type. Commands can be logged, retried, scheduled and undone because they are data.",
                 "Strategy = a function you pass or look up. Command = a data object plus a handler.")
sc_how.box(20, 30, 340, 150, None, "green")
sc_how.head(190, 62, "strategy")
sc_how.text(190, 100, "discounts[name](basket)")
sc_how.text(190, 136, "a map of functions")
sc_how.box(400, 30, 340, 150, None, "blue")
sc_how.head(570, 62, "command")
sc_how.text(570, 100, "{ type: \"ReserveStock\", … }")
sc_how.text(570, 136, "+ one handler")
sc_how.note(570, 220, "data → log, retry, schedule, undo", "green")
sc_how.note(190, 220, "no interface or factory needed", "green")

STRATEGY_COMMAND = dict(
    slug="strategy-command",
    kicker="a.k.a. “pick a route, write an order slip”",
    tldr="<b>Strategy</b>: choose behaviour at runtime by swapping an algorithm, such as a discount rule or a sort order. <b>Command</b>: turn a request into an <b>object</b> you can queue, log, retry or undo. In 1994 both needed an interface and a class per variant. With first-class functions, a strategy is just a <b>function</b> (often in a map), and a command is a <b>data object</b> plus a handler. Keep the ideas, drop the boilerplate.",
    chips=[("Family", "behavioural patterns (GoF)"), ("From", "Gamma et al., <i>Design Patterns</i> (1994)"), ("Today", "functions, lambdas, message objects"), ("Pairs with", "open–closed, job queues")],
    problem="""  <p class="lead">Applying 1994 class-based recipes in modern languages creates <span class="hl-pink">class explosions</span> for one-line behaviour.</p>
  <ul>
    <li>An interface, five classes, a factory and a registry for five discount rules.</li>
    <li>Command classes with an <code>execute()</code> that wraps one call.</li>
    <li>Reading one rule means opening four files.</li>
  </ul>""",
    problem_figs=[sc_problem],
    analogy_side="route choice and order slips",
    analogy="""  <p>In a <b>navigation app</b> you pick fastest, shortest or no tolls, and the app swaps its route rule. A waiter's <b>order slip</b> turns a spoken request into paper that can wait in a queue, be passed to another cook, or be torn up if the guest cancels.</p>
  <ul>
    <li>The route setting is a <b>strategy</b>.</li>
    <li>The slip is a <b>command</b>: a request turned into data.</li>
  </ul>""",
    analogy_figs=[sc_analogy],
    map=[("“Fastest / shortest / no tolls”", "A map of discount or pricing functions"),
         ("Swapping the route rule", "Passing a different function"),
         ("The order slip", "A command object: <code>{ type: \"ReserveStock\", orderId }</code>"),
         ("The queue of slips", "A job queue or outbox"),
         ("Tearing up a slip", "Cancelling or undoing a queued command")],
    how_side="functions and data, not class trees",
    how="""  <p>Peter Norvig showed in 1996 that 16 of the 23 GoF patterns become simpler or invisible in dynamic, functional languages. Strategy and Command are the clearest cases: <b>the language feature replaced the pattern</b>, but the need it names didn't go away.</p>""",
    how_figs=[sc_how],
    steps=[("Strategy: write each variant as a function", "<code>(basket) =&gt; Money</code>, named after the rule."),
           ("Choose by passing or looking up", "Pass the function in, or keep a map from key to function."),
           ("Use a class only for state", "If a variant needs configuration or caching, a small object is fine."),
           ("Command: make the request data", "A typed object with a <code>type</code> and its fields."),
           ("One handler per type", "A function that performs it; register handlers in a map."),
           ("Exploit that it's data", "Store, log, retry, schedule and audit commands.")],
    vocab=[("Strategy", "A family of interchangeable algorithms chosen at runtime."),
           ("Command", "A request turned into an object."),
           ("First-class function", "A function you can pass, store and return like any value."),
           ("Higher-order function", "A function that takes or returns functions."),
           ("Discriminated union", "A typed way to describe several command shapes."),
           ("Undo", "Reversing a command, possible when it's recorded as data.")],
    code=dict(file="discounts.ts", note="strategy as functions, command as data", src="""
// Strategy: a map of functions
type Discount = (b: Basket) => Money;
const discounts: Record<DiscountName, Discount> = {
  none:        ()  => Money.zero("EUR"),
  tenPercent:  (b) => b.total().percent(10),
  freeShipping:(b) => b.shippingCost(),
};
const total = basket.total().minus(discounts[customer.discount](basket));

// Command: data + a handler, so it can be queued, retried and audited
type Command =
  | { type: "ReserveStock"; orderId: OrderId }
  | { type: "SendInvoice";  orderId: OrderId; email: EmailAddress };

const handlers: { [K in Command["type"]]: (c: Extract<Command, { type: K }>) => Promise<void> } = {
  ReserveStock: async (c) => stock.reserve(c.orderId),
  SendInvoice:  async (c) => mailer.sendInvoice(c.orderId, c.email),
};
await jobs.enqueue({ type: "SendInvoice", orderId, email });   // runs later, retries on failure
"""),
    tools="tools: plain functions and maps, discriminated unions for command types, job queues (BullMQ, Sidekiq, Hangfire, Temporal for long workflows), MediatR-style handler registries.",
    gains=["<b>Much less code</b> for the same flexibility.",
           "<b>Rules readable in one place</b>.",
           "<b>Commands as data</b>: queue, retry, audit.",
           "<b>Easy to test</b>: call the function."],
    losses=["<b>Less structure</b> for big, stateful variants.",
            "<b>Unfamiliar</b> to teams trained on class diagrams.",
            "<b>Map lookups</b> can fail at runtime without types.",
            "<b>Handlers spread</b> without a registry."],
    baseline="Each line compares <b>GoF-style interfaces, classes and factories</b> to <b>functions for strategies and data plus handlers for commands</b>.",
    ratings=[(2, 4, "One function per rule instead of four files."),
             (3, 4, "Rules named directly in a map."),
             (3, 4, "Typed maps catch missing variants."),
             (3, 4, "Add a variant by adding one entry."),
             (3, 5, "Call the function with a value."),
             (3, 4, "Callers depend on a function type."),
             (3, 3, "Neutral."),
             (2, 5, "No interfaces, classes or factories."),
             (3, 3, "Neutral.")],
    pitfalls=[("Classes by habit", "A <code>Strategy</code> interface and factory for one-liners.", "functions and a map."),
              ("Untyped lookups", "<code>discounts[name]</code> is undefined for a new name.", "typed keys, and fail loudly on unknown ones."),
              ("Commands with behaviour inside", "Command objects that call services from <code>execute()</code>, so they can't be serialised.", "data in the command, behaviour in the handler."),
              ("Strategies that need everything", "A function taking twelve parameters.", "pass a small context object, or reconsider the split.")],
    use=["Several interchangeable rules chosen at runtime.",
         "Work that should be queued, retried, scheduled or audited.",
         "Replacing GoF boilerplate in a modern codebase."],
    skip=["One rule with no variants (just write it).",
          "Simple synchronous calls with nothing to queue."],
    related=["<b>Open–Closed</b>", "<b>Decorator &amp; Middleware</b>", "<b>The Pattern Museum</b>", "<b>Competing Consumers</b> (Vol. 1)", "<b>Domain Events</b> (Vol. 7)"],
    quiz=[("What does the Strategy pattern do?", "Lets you choose an algorithm at runtime by swapping interchangeable implementations."),
          ("What's the modern lightweight form of Strategy?", "A function, often chosen from a map keyed by name."),
          ("Why make a command a data object?", "So it can be queued, logged, retried, scheduled or undone."),
          ("Where should the command's behaviour live?", "In a handler, separate from the data, so the command stays serialisable.")],
    quiz_sit=[("A pull request adds <code>IShippingStrategy</code>, four strategy classes of two lines each, a factory and a DI registration, for four carrier price rules. What do you suggest in review?",
               "Replace them with a map from carrier to a pricing function in one file, typed so a missing carrier fails to compile. Keep a class only if a carrier needs configuration or state.")],
    try_it="Find a Strategy or Command class hierarchy in your code. Rewrite one as functions (or data plus a handler), run the tests, and compare the number of files and lines before and after.",
    then_now=dict(src="Gamma et al., 1994", verdict="built-in",
                  then="The GoF described Strategy and Command with interfaces and a class per variant, because C++ and Smalltalk-era Java had no convenient first-class functions.",
                  now="Lambdas and first-class functions are in every mainstream language, so a strategy is a function and a command is a message object. The needs (swap behaviour, queue work) are as real as ever; job queues and workflow engines are Command at scale.",
                  take="Built in now: the language does the pattern. Know the names, write the functions."),
    remember="Pick a <span class=\"hl\">route rule</span>; write an <span class=\"hl\">order slip</span>. Neither needs a factory.",
    sources=["Erich Gamma, Richard Helm, Ralph Johnson &amp; John Vlissides, <i>Design Patterns</i> (1994), “Strategy”, “Command”.",
             "Peter Norvig, “Design Patterns in Dynamic Languages” (1996).",
             "Mark Seemann, “Strategy and Command as functions” in <i>Code That Fits in Your Head</i> (2021).",
             "Scott Wlaschin, “Functional programming design patterns” (talk, 2014)."],
)

# ------------------------------------------------------------------ 16 Decorator & Middleware
dm_problem = Doodle(760, 260, "Doodle of cross-cutting code copied everywhere. Every method of the payment, stock and email clients starts with the same logging, a retry loop, a timeout and a metrics timer, copied by hand. One copy forgot the timeout and hung the checkout for thirty seconds. Changing the retry policy means editing forty places.",
                    "Logging, retries, timeouts and metrics copied into forty methods, and one copy forgot the timeout.")
for i, t in enumerate(["charge()", "refund()", "reserve()", "send()"]):
    y = 20 + i * 52
    dm_problem.box(20, y, 160, 42, t, "paper", size=15)
    dm_problem.text(420, y + 28, "log · retry · timeout · metrics · real call" if i != 2 else "log · retry · (no timeout!) · real call")
dm_problem.note(420, 240, "40 copies; change the retry policy everywhere", "red")

dm_analogy = Doodle(760, 250, "Doodle of wrapping a gift. The present is in a box. The box goes in wrapping paper, then a ribbon, then a padded envelope for posting. Each layer adds something and has the same shape on the outside: something you can hand over. You can add or remove a layer without touching the present.",
                    "A present, then paper, ribbon and a padded envelope: each layer adds one thing, same shape outside.")
for i, (t, f, h) in enumerate([("padded envelope", "paper", 210), ("ribbon", "pink", 150), ("wrapping paper", "y", 90)]):
    dm_analogy.box(120 + i * 60, 20 + i * 30, 520 - i * 120, h, None, f)
    dm_analogy.text(380, 42 + i * 30, t, cls="t-head")
dm_analogy.box(300, 110, 160, 46, "present", "green", size=17)

dm_how = Doodle(760, 320, "Decorators around a payment port. The real Stripe adapter implements PaymentPort. A timeout decorator implements the same port and wraps it, a retry decorator wraps that, and a logging and metrics decorator wraps the outside. The use case receives the outermost one and doesn't know about the layers. HTTP middleware is the same idea for requests: a pipeline of functions each calling next.",
                 "Same interface on every layer: log(retry(timeout(stripe))). HTTP middleware is the same idea for requests.")
layers = [("logging & metrics", "paper"), ("retry ×3", "y"), ("timeout 2 s", "blue"), ("Stripe adapter", "green")]
for i, (t, f) in enumerate(layers):
    dm_how.box(20 + i * 40, 20 + i * 44, 720 - i * 80, 230 - i * 88 if i < 3 else 50, None, f)
    dm_how.text(380, 46 + i * 44, t, cls="t-head")
dm_how.note(380, 296, "every layer implements PaymentPort", "green")

DECORATOR = dict(
    slug="decorator-middleware",
    kicker="a.k.a. “gift wrap, layer by layer”",
    tldr="A <b>decorator</b> wraps an object with another that has the <b>same interface</b>, adding one behaviour (logging, retries, timeouts, caching, metrics, authorisation) before or after passing the call on. Stack several: <code>log(retry(timeout(stripe)))</code>. Callers can't tell the difference. <b>HTTP middleware</b> and interceptors are the same idea for requests. Write cross-cutting code <b>once</b>, compose it per use.",
    chips=[("Family", "structural pattern (GoF)"), ("From", "Gamma et al. (1994)"), ("Everywhere as", "middleware, interceptors, higher-order functions"), ("Pairs with", "retry with backoff, circuit breaker (Vol. 1)")],
    problem="""  <p class="lead">Cross-cutting concerns copied into every method <span class="hl-pink">drift apart</span> and <span class="hl-pink">bury the real logic</span>.</p>
  <ul>
    <li>Logging, retries, timeouts and metrics copied into forty methods.</li>
    <li>One copy forgot the timeout and hung checkout.</li>
    <li>Changing the retry policy means forty edits.</li>
  </ul>""",
    problem_figs=[dm_problem],
    analogy_side="gift wrapping",
    analogy="""  <p>A <b>present</b> goes in paper, then a ribbon, then a padded envelope for posting. Each layer adds one thing, and from the outside it's still something you can hand over. Add or remove a layer without touching the present.</p>
  <ul>
    <li>The present is the <b>real implementation</b>.</li>
    <li>Each layer is a <b>decorator</b>.</li>
    <li>“Something you can hand over” is the <b>shared interface</b>.</li>
  </ul>""",
    analogy_figs=[dm_analogy],
    map=[("The present", "The Stripe adapter doing the real work"),
         ("Wrapping paper", "A timeout decorator"),
         ("Ribbon", "A retry decorator"),
         ("Padded envelope", "Logging and metrics"),
         ("Still something to hand over", "Every layer implements <code>PaymentPort</code>")],
    how_side="same shape, one extra behaviour per layer",
    how="""  <p>In functional style a decorator is a <b>higher-order function</b>: <code>withRetry(fn)</code> returns a new function with the same signature. Order matters: a retry outside a timeout retries timed-out calls; inside, it doesn't.</p>""",
    how_figs=[dm_how],
    steps=[("Identify the shared interface", "The port or function signature all layers will have."),
           ("Write one decorator per concern", "Timeout, retry, logging, caching, each small and tested alone."),
           ("Compose in the composition root", "Wrap the real adapter in the order you want."),
           ("Think about order", "Usually: metrics outside, then retry, then timeout, then the real call."),
           ("Use middleware for requests", "Auth, validation, correlation IDs as an HTTP or handler pipeline."),
           ("Keep business rules out", "Decorators handle cross-cutting concerns, not domain decisions.")],
    vocab=[("Decorator", "A wrapper with the same interface that adds behaviour."),
           ("Cross-cutting concern", "Behaviour needed in many places: logging, security, retries."),
           ("Middleware", "A pipeline of functions around request handling, each calling the next."),
           ("Interceptor", "A framework hook that wraps calls (Angular, gRPC, NestJS)."),
           ("Higher-order function", "A function that takes a function and returns a wrapped one."),
           ("AOP", "Aspect-oriented programming: framework-level decoration by rules.")],
    code=dict(file="payments.compose.ts", note="decorators as wrappers with the same interface", src="""
const withTimeout = (ms: number) => (p: PaymentPort): PaymentPort => ({
  charge: (a, c) => Promise.race([p.charge(a, c), rejectAfter(ms, "payment timeout")]),
});
const withRetry = (times: number) => (p: PaymentPort): PaymentPort => ({
  charge: (a, c) => retry(() => p.charge(a, c), { times, backoffMs: 200, jitter: true }),
});
const withMetrics = (p: PaymentPort): PaymentPort => ({
  charge: (a, c) => timed("payment.charge", () => p.charge(a, c)),
});

// composition root: the use case never knows
const payments = withMetrics(withRetry(3)(withTimeout(2000)(new StripeAdapter(key))));

// HTTP middleware: the same idea for requests
app.use(correlationId(), requestLogging(), authenticate(), rateLimit({ perMinute: 60 }));
"""),
    tools="tools: HTTP middleware (Express, Fastify hooks, ASP.NET Core middleware), interceptors (NestJS, gRPC, Angular HTTP), resilience libraries (Polly, resilience4j, cockatiel) that are decorators, Python and TypeScript decorators syntax.",
    gains=["<b>Write each concern once</b>.",
           "<b>Real logic stays clean</b>.",
           "<b>Compose per use</b>: different stacks for different callers.",
           "<b>Each layer tested alone</b>."],
    losses=["<b>Order bugs</b>: layers in the wrong order.",
            "<b>Debugging through layers</b>.",
            "<b>Hidden behaviour</b> if composition is buried.",
            "<b>Wrapping every method</b> of a big interface."],
    baseline="Each line compares <b>cross-cutting code copied into each method</b> to <b>decorators and middleware composed around the real implementation</b>.",
    ratings=[(2, 4, "Each method shows only its real job."),
             (3, 4, "Business code no longer buried in plumbing."),
             (2, 4, "No forgotten timeouts: one decorator, applied once."),
             (2, 5, "Change the retry policy in one place."),
             (3, 4, "Each decorator tested alone."),
             (3, 4, "The core knows nothing of retries or metrics."),
             (3, 3, "Neutral; tiny overhead per layer."),
             (3, 4, "Less repeated code overall."),
             (3, 4, "Platform teams supply shared decorators.")],
    pitfalls=[("Wrong order", "Retry inside the timeout, so a slow call is never retried, or retries exceed the caller's deadline.", "decide the order deliberately and test it."),
              ("Business rules in decorators", "A “discount decorator” around the price calculator.", "decorators for cross-cutting concerns; rules in the domain."),
              ("Invisible magic", "Annotations apply caching and transactions nobody can see.", "compose explicitly in one place, or document the rules."),
              ("Retrying non-idempotent calls", "A retry decorator charges a card twice.", "idempotency keys, or no retry for that call.")],
    use=["Logging, metrics, retries, timeouts, caching, auth around many calls.",
         "Request pipelines in web frameworks.",
         "Adding behaviour to a third-party client you can't change."],
    skip=["A concern needed in exactly one place (just write it there).",
          "Business decisions (those belong in the domain)."],
    related=["<b>Adapter &amp; Facade</b>", "<b>Strategy &amp; Command as Functions</b>", "<b>Retry with Backoff</b> (Vol. 1)", "<b>Circuit Breaker</b> (Vol. 1)", "<b>Dependency Inversion</b>"],
    quiz=[("What does a decorator do?", "Wraps an object with another that has the same interface and adds one behaviour."),
          ("How is HTTP middleware related?", "It's the same idea for requests: a pipeline of wrappers, each calling the next."),
          ("Why does order matter?", "Each layer sees what the inner layers do: a retry outside a timeout behaves differently from one inside."),
          ("What should never go in a decorator?", "Business rules; decorators are for cross-cutting concerns.")],
    quiz_sit=[("After adding a retry wrapper to all outgoing HTTP calls, some customers are charged twice when the payment provider is slow. What went wrong, and what do you change?",
               "The retry repeated a non-idempotent charge after a timeout that had actually succeeded. Send an idempotency key with each charge so the provider ignores duplicates, or exclude non-idempotent calls from the retry decorator.")],
    try_it="Find a cross-cutting concern copied into several methods (timing, logging, retries). Write it once as a wrapper with the same interface, apply it in the composition root, and delete the copies.",
    then_now=dict(src="Gamma et al., 1994", verdict="core",
                  then="The GoF's Decorator added responsibilities to objects dynamically, with examples like adding borders and scroll bars to GUI widgets, as a flexible alternative to subclassing.",
                  now="It's everywhere, often unnamed: HTTP middleware, gRPC and NestJS interceptors, resilience libraries like Polly and resilience4j, and higher-order functions. Language decorators (Python, TypeScript) put it in the syntax.",
                  take="Still core: one of the GoF patterns used more today than in 1994."),
    remember="Wrap the present <span class=\"hl\">layer by layer</span>; never <span class=\"hl\">open the box</span> to add a ribbon.",
    sources=["Erich Gamma et al., <i>Design Patterns</i> (1994), “Decorator”.",
             "Microsoft, “ASP.NET Core Middleware” documentation.",
             "Polly documentation, “Resilience pipelines” (pollydocs.org).",
             "Express documentation, “Using middleware”."],
)

# ------------------------------------------------------------------ 17 Adapter & Facade
af_problem = Doodle(760, 270, "Doodle of foreign interfaces spread through the code. Three shipping carriers each have their own SDK with different method names, units and error types, called directly from twenty places. A PDF library needs fifteen setup steps, repeated in every place that makes a document. Upgrading one SDK means editing every caller.",
                    "Three carrier SDKs called directly from 20 places, and a PDF library's 15 setup steps copied everywhere.")
for i, (t, s) in enumerate([("DHL SDK", "kg, createShipment()"), ("PostNL SDK", "grams, label()"), ("DPD SDK", "lbs?, book()")]):
    af_problem.box(20, 20 + i * 70, 220, 56, t, "paper", sub=s, size=16, subsize=13)
    af_problem.arrow(244, 48 + i * 70, 320, 120, color="red", dash=True)
af_problem.box(330, 80, 180, 80, "20 callers", "pink", stroke="red", size=17)
af_problem.box(560, 60, 180, 120, "PDF lib", "pink", stroke="red", sub="15 steps × 9")
af_problem.note(380, 254, "an SDK upgrade touches every caller", "red")

af_analogy = Doodle(760, 250, "Doodle of a travel plug adapter and a hotel concierge. The plug adapter makes a foreign socket fit your charger, without changing either. The concierge hides the complexity of the city: you say I want dinner and a taxi at eight, and they deal with the restaurant, the taxi company and the timing.",
                     "A plug adapter makes one shape fit another; a concierge hides a whole city behind one desk.")
af_analogy.box(20, 40, 340, 120, None, "y")
af_analogy.head(190, 74, "plug adapter")
af_analogy.text(190, 112, "foreign socket → my plug")
af_analogy.box(400, 40, 340, 120, None, "green")
af_analogy.head(570, 74, "concierge")
af_analogy.text(570, 112, "“dinner + taxi at 8”")
af_analogy.note(190, 200, "adapter", "pen")
af_analogy.note(570, 200, "facade", "pen")

af_how = Doodle(760, 320, "Adapters and a facade. The core defines one ShippingPort with bookParcel in grams and its own errors. A DHL adapter, a PostNL adapter and a DPD adapter each implement it, converting units, names and errors. Separately, an InvoicePdf facade offers one method, render invoice, hiding the PDF library's fifteen setup steps. Callers use only the port and the facade.",
                 "Adapters make each carrier fit one port; a facade gives the PDF library one simple door.")
af_how.box(270, 20, 220, 70, "ShippingPort", "y", sub="bookParcel(grams)")
for i, t in enumerate(["DHL", "PostNL", "DPD"]):
    x = 20 + i * 250
    af_how.box(x, 140, 220, 56, f"{t} adapter", "green", size=16)
    af_how.arrow(x + 110, 136, 380, 94, dash=True)
af_how.box(200, 236, 360, 64, "InvoicePdf facade", "blue", sub="render(invoice) → hides 15 steps")

ADAPTER_FACADE = dict(
    slug="adapter-facade",
    kicker="a.k.a. “the plug adapter and the concierge”",
    tldr="Two structural patterns you'll use weekly. An <b>adapter</b> makes an existing interface <b>fit the one you need</b>: each carrier SDK is wrapped to implement your <code>ShippingPort</code>, converting names, units and errors. A <b>facade</b> puts a <b>simple door</b> in front of a complicated subsystem: <code>invoicePdf.render(invoice)</code> hides fifteen setup steps. Both keep foreign APIs <b>at the edge</b>, so an upgrade or a swap touches <b>one file</b>.",
    chips=[("Family", "structural patterns (GoF)"), ("From", "Gamma et al. (1994)"), ("Today as", "adapters in ports &amp; adapters, SDK wrappers, BFFs"), ("Pairs with", "anti-corruption layer (Vol. 7)")],
    problem="""  <p class="lead">Calling foreign APIs directly from many places spreads <span class="hl-pink">their shapes and quirks</span> through your code.</p>
  <ul>
    <li>Three carrier SDKs with different names, units and errors, used in twenty places.</li>
    <li>A PDF library's fifteen setup steps copied nine times.</li>
    <li>An SDK upgrade touches every caller.</li>
  </ul>""",
    problem_figs=[af_problem],
    analogy_side="the plug adapter and the concierge",
    analogy="""  <p>A <b>travel plug adapter</b> makes a foreign socket fit your charger, without changing either. A hotel <b>concierge</b> hides a whole city: you say “dinner and a taxi at eight” and they deal with the restaurant, the taxi company and the timing.</p>
  <ul>
    <li>The plug adapter is an <b>adapter</b>: one shape to another.</li>
    <li>The concierge is a <b>facade</b>: one simple door to a complicated system.</li>
  </ul>""",
    analogy_figs=[af_analogy],
    map=[("Foreign socket", "A carrier SDK's interface"),
         ("Your charger's plug", "Your <code>ShippingPort</code>"),
         ("The plug adapter", "<code>DhlShippingAdapter implements ShippingPort</code>"),
         ("The concierge desk", "<code>InvoicePdf.render(invoice)</code>"),
         ("Restaurant, taxi, timing", "The PDF library's fonts, pages, layout and streams")],
    how_side="fit a shape, or simplify a subsystem",
    how="""  <p>An adapter <b>converts</b> an interface; a facade <b>simplifies</b> one. An anti-corruption layer (Vol. 7) is adapters and facades with an extra job: translating a whole <b>model</b>, not just method names.</p>""",
    how_figs=[af_how],
    steps=[("Define what you need", "A port in your terms: <code>bookParcel(order, weight: Grams)</code>."),
           ("Adapt each provider", "One adapter per SDK, converting names, units and errors."),
           ("Translate errors", "Provider errors become your error types; callers never catch SDK exceptions."),
           ("Facade complex libraries", "One small class with the operations you use, hiding setup."),
           ("Keep them at the edge", "Only adapters and facades import the SDK."),
           ("Contract-test adapters", "The same tests against every adapter of a port.")],
    vocab=[("Adapter", "Converts one interface into another that clients expect."),
           ("Facade", "A simple interface to a complex subsystem."),
           ("Wrapper", "A loose term for either."),
           ("Anti-corruption layer", "Adapters and facades that also translate a foreign model."),
           ("SDK", "A provider's client library."),
           ("Leaky abstraction", "A wrapper that still exposes the wrapped API's details.")],
    code=dict(file="shipping/dhl.adapter.ts", note="adapter: their SDK, your port", src="""
export interface ShippingPort {
  bookParcel(p: { orderId: OrderId; weight: Grams; to: Address }): Promise<TrackingNo>;
}

export class DhlShippingAdapter implements ShippingPort {
  constructor(private dhl: DhlClient) {}
  async bookParcel({ orderId, weight, to }) {
    try {
      const res = await this.dhl.createShipment({
        reference: orderId, weightKg: weight.value / 1000, receiver: toDhlAddress(to) });
      return trackingNo(res.shipmentTrackingNumber);
    } catch (e) {
      if (e instanceof DhlValidationError) throw new InvalidAddress(to, e.message);
      throw new CarrierUnavailable("dhl", e);
    }
  }
}

// facade: one door to a complicated library
export const invoicePdf = { render: (inv: InvoiceView) => renderWithPdfLib(inv /* 15 steps inside */) };
"""),
    tools="tools: plain classes or functions; contract tests per port; SDK generators (OpenAPI generator) behind your own adapter; dependency-cruiser rules so only adapters import vendor SDKs.",
    gains=["<b>Foreign APIs at the edge</b>, in one file each.",
           "<b>Swap or upgrade</b> providers in one place.",
           "<b>Your own errors and units</b> everywhere else.",
           "<b>Simple calls</b> for complex libraries."],
    losses=["<b>More code</b>: one adapter per provider.",
            "<b>Lowest common denominator</b>: special features get hidden.",
            "<b>Leaky wrappers</b> if done carelessly.",
            "<b>Another layer</b> to step through when debugging."],
    baseline="Each line compares <b>calling vendor SDKs and complex libraries directly from many places</b> to <b>adapters behind ports and facades for complex libraries</b>.",
    ratings=[(2, 4, "Callers use one simple, consistent interface."),
             (3, 4, "Your names and units, not each vendor's."),
             (3, 4, "Unit and error conversions done once, correctly."),
             (2, 5, "An SDK upgrade touches one adapter."),
             (2, 4, "Fake the port; contract-test the adapters."),
             (1, 5, "Vendors are confined to their adapters."),
             (3, 3, "Neutral."),
             (4, 3, "An adapter per provider, a facade per library."),
             (3, 4, "Integration work happens in parallel per provider.")],
    pitfalls=[("Leaky adapters", "The port returns the SDK's response type.", "return your own types; convert inside."),
              ("Lowest common denominator", "A carrier's useful feature can't be reached through the port.", "add an optional capability, or a second port for it."),
              ("Facade that grows into a god class", "Every library feature added to the facade.", "only the operations your app uses."),
              ("Wrapping stable standard libraries", "A facade around <code>fetch</code> or <code>Date</code> with no added meaning.", "wrap only what's volatile or awkward.")],
    use=["Integrating several providers for the same job.",
         "A complicated library used in many places.",
         "Third-party APIs likely to change or be replaced."],
    skip=["Stable, well-designed standard libraries.",
          "A one-off call in a script."],
    related=["<b>Dependency Inversion</b>", "<b>Ports &amp; Adapters</b>", "<b>Decorator &amp; Middleware</b>", "<b>Anti-Corruption Layer</b> (Vol. 7)", "<b>DTOs &amp; Remote Facade</b>"],
    quiz=[("What's the difference between an adapter and a facade?", "An adapter converts one interface into another; a facade simplifies a complex subsystem behind a simple interface."),
          ("How does an anti-corruption layer relate?", "It's built from adapters and facades, with the extra job of translating a foreign model."),
          ("Why translate provider errors?", "So callers handle your own error types and never depend on an SDK's exceptions."),
          ("What's a leaky adapter?", "One whose interface still exposes the wrapped API's types or details.")],
    quiz_sit=[("Your company switches SMS provider. The old provider's client is imported in 31 files, each building messages slightly differently. What do you do first?",
               "Define an <code>SmsSender</code> port in your terms, write an adapter for the old provider, and move the 31 callers onto the port (behaviour unchanged). Then write an adapter for the new provider, contract-test both, and switch in the composition root.")],
    try_it="Search your code for imports of one vendor SDK. Count the files. Write a port and one adapter for it, move two callers over, and add a lint rule that only the adapter may import the SDK.",
    then_now=dict(src="Gamma et al., 1994", verdict="core",
                  then="The GoF described Adapter (make incompatible interfaces work together) and Facade (a unified interface to a subsystem) with examples from GUI toolkits and compilers.",
                  now="Both are daily tools: adapters are the “adapters” of ports and adapters, every SaaS integration needs one, and facades sit in front of SDKs, BFFs and complex libraries. The names stuck because the needs never went away.",
                  take="Still core, and more common than in 1994 because systems now talk to so many vendors."),
    remember="A <span class=\"hl\">plug adapter</span> for each foreign socket; a <span class=\"hl\">concierge</span> for each complicated city.",
    sources=["Erich Gamma et al., <i>Design Patterns</i> (1994), “Adapter”, “Facade”.",
             "Alistair Cockburn, “Hexagonal Architecture” (2005).",
             "Microsoft Azure Architecture Center, “Anti-corruption Layer pattern”.",
             "Eric Freeman &amp; Elisabeth Robson, <i>Head First Design Patterns</i>, 2nd ed. (2020), ch. 7."],
)

# ------------------------------------------------------------------ 18 The Pattern Museum
pm_problem = Doodle(760, 270, "Doodle of a codebase built from old tutorials. A ConfigManager singleton holds global state, so tests leak into each other. Code asks a ServiceLocator for its dependencies, so nobody can see what a class needs. A Visitor hierarchy for a five-case report forces three new methods for every new case. Server-side session state pins users to one server, so autoscaling breaks logins.",
                    "Singletons leaking between tests, a hidden service locator, a needless Visitor, and sessions pinned to one server.")
for i, (t, s) in enumerate([("Singleton", "tests leak state"), ("Service Locator", "hidden needs"), ("Visitor", "3 methods per case"), ("session in RAM", "can't scale out")]):
    x = 20 + (i % 2) * 380
    y = 30 + (i // 2) * 100
    pm_problem.box(x, y, 340, 76, t, "pink", stroke="red", sub=s)
pm_problem.note(380, 250, "patterns from 1994–2002 tutorials, in a 2026 codebase", "red")

pm_analogy = Doodle(760, 250, "Doodle of a museum of technology. A typewriter, a fax machine and a slide rule sit in glass cases. They solved real problems in their day and are worth understanding: the typewriter's keyboard layout still shapes ours. But nobody sends this week's invoices by fax.",
                     "A typewriter, a fax and a slide rule behind glass: worth understanding, not for daily use.")
for i, t in enumerate(["typewriter", "fax", "slide rule"]):
    x = 30 + i * 240
    pm_analogy.box(x, 40, 210, 110, t, "paper", dash=True, sub="behind glass")
pm_analogy.note(380, 200, "solved real problems · shaped what came after", "pen")
pm_analogy.note(380, 230, "nobody faxes invoices today", "red")

pm_how = Doodle(760, 340, "A museum guide: each retired pattern next to its modern replacement. Singleton becomes a single instance created in the composition root and injected. Service Locator becomes constructor injection. Visitor becomes pattern matching over a union type. Page and Front Controller and Template View become the framework's router and components. Table Module and Row and Table Data Gateway become an ORM or query builder. Server Session State becomes stateless tokens and a shared store.",
                 "Each exhibit with what replaced it.")
rows = [("Singleton", "one instance, injected"), ("Service Locator", "constructor injection"), ("Visitor", "pattern matching"),
        ("Page/Front Controller", "framework router"), ("Table Module, Gateways", "ORM / query builder"), ("server session state", "tokens + shared store")]
for i, (old, new) in enumerate(rows):
    y = 20 + i * 52
    pm_how.box(20, y, 300, 42, old, "paper", size=15)
    pm_how.arrow(324, y + 21, 416, y + 21)
    pm_how.box(420, y, 320, 42, new, "green", size=15)

MUSEUM = dict(
    slug="pattern-museum",
    kicker="a.k.a. “worth a visit, not worth using”",
    tldr="Some famous patterns solved problems that <b>languages, frameworks and platforms now solve for you</b>, or caused problems we only saw later. Worth <b>recognising</b> in old code and interviews, rarely worth <b>writing</b> today: <b>Singleton</b> (use one injected instance), <b>Service Locator</b> (use constructor injection), <b>Visitor</b> (use pattern matching), <b>Page/Front Controller</b> and <b>Template View</b> (your framework), <b>Table Module</b> and <b>data gateways</b> (an ORM or query builder), and <b>server session state</b> (stateless tokens and a shared store).",
    chips=[("Family", "retired patterns"), ("From", "GoF (1994), PoEAA (2002), Fowler (2004)"), ("Use for", "reading old code, interviews, history"), ("Replace with", "DI, pattern matching, frameworks, ORMs")],
    problem="""  <p class="lead">Copying patterns from old books and tutorials brings their <span class="hl-pink">old costs</span> without their <span class="hl-pink">old reasons</span>.</p>
  <ul>
    <li>Singletons hold global state, so tests leak into each other.</li>
    <li>A service locator hides what each class depends on.</li>
    <li>Session state in server memory breaks autoscaling.</li>
  </ul>""",
    problem_figs=[pm_problem],
    analogy_side="the technology museum",
    analogy="""  <p>A <b>museum of technology</b> has a typewriter, a fax machine and a slide rule behind glass. They solved real problems, and they shaped what followed (our keyboards still use the typewriter's layout). But nobody <b>faxes this week's invoices</b>.</p>
  <ul>
    <li>The exhibits are the <b>retired patterns</b>.</li>
    <li>The plaques explain <b>what replaced them</b>.</li>
  </ul>""",
    analogy_figs=[pm_analogy],
    map=[("Typewriter", "Singleton: global access, now injected instances"),
         ("Fax machine", "Server session state: now stateless tokens"),
         ("Slide rule", "Visitor: double dispatch, now pattern matching"),
         ("The plaque", "Knowing what each solved and what replaced it"),
         ("Visiting the museum", "Recognising them in legacy code")],
    how_side="each exhibit and its replacement",
    how="""  <ul>
    <li><b>Singleton</b> (GoF): global access to one instance. Problems: hidden global state, hard-to-isolate tests. Now: create one instance in the composition root and inject it (a “singleton lifetime”, not a singleton class).</li>
    <li><b>Service Locator</b> (Fowler, 2004): ask a registry for dependencies. Problems: hidden dependencies, runtime failures. Now: constructor injection.</li>
    <li><b>Visitor</b> (GoF): add operations to a class hierarchy without editing it. Now: union types and exhaustive pattern matching (still useful in compilers and AST tools).</li>
    <li><b>Page Controller, Front Controller, Template View, Transform View</b> (PoEAA): how to build web pages by hand. Now: your framework's router and components.</li>
    <li><b>Table Module, Table and Row Data Gateway</b> (PoEAA): hand-written data access styles. Now: an ORM or a typed query builder.</li>
    <li><b>Server Session State</b> (PoEAA): user state in server memory. Now: stateless tokens and a shared store (Redis, a database), so any server can answer.</li>
  </ul>""",
    how_figs=[pm_how],
    steps=[("Recognise the exhibit", "In legacy code, name the pattern and the problem it was solving."),
           ("Check the reason still applies", "Sometimes it does: Visitor in a compiler, a true singleton for a hardware handle."),
           ("Pick the modern replacement", "From the guide above."),
           ("Replace at the edges first", "New code uses injection; old singletons get an injectable wrapper."),
           ("Migrate behind tests", "Characterization tests before removing global state."),
           ("Teach the history", "Knowing why a pattern existed helps people spot when its problem returns.")],
    vocab=[("Singleton", "A class that ensures only one instance and global access to it."),
           ("Service Locator", "A registry code calls to fetch its dependencies."),
           ("Visitor", "Double dispatch to add operations to a class hierarchy."),
           ("Front Controller", "One handler for all web requests that dispatches to commands."),
           ("Table Module", "One class handling all rows of a table."),
           ("Server Session State", "Keeping a user's session in server memory.")],
    code=dict(file="museum-to-modern.ts", note="Singleton and Visitor, then and now", src="""
// museum: Singleton with global state
class Config { private static instance?: Config; static get() { return this.instance ??= new Config(); } }
const tax = Config.get().vatRate;          // hidden dependency, shared across tests

// now: one instance, created once, injected
const config = loadConfig(process.env);    // composition root
const pricing = new Pricing(config);       // dependency is visible and replaceable in tests

// museum: Visitor for a small hierarchy -> now: a union + exhaustive switch
type Shape = { kind: "circle"; r: number } | { kind: "rect"; w: number; h: number };
const area = (s: Shape) => {
  switch (s.kind) { case "circle": return Math.PI * s.r ** 2; case "rect": return s.w * s.h; }
};
"""),
    tools="tools: DI containers or hand-written composition roots, TypeScript/Kotlin/Rust/Java 21 pattern matching, web frameworks' routers and components, ORMs and query builders, Redis or database-backed sessions and signed tokens.",
    gains=["<b>No global state</b> leaking between tests.",
           "<b>Visible dependencies</b>.",
           "<b>Less hand-written machinery</b>: frameworks do it.",
           "<b>Scalable services</b> without sticky sessions."],
    losses=["<b>Migration effort</b> in legacy code.",
            "<b>Some cases still need them</b> (compilers, hardware handles).",
            "<b>Interview questions</b> still ask about them.",
            "<b>Unlearning habits</b> takes time."],
    baseline="Each line compares <b>code built with the museum patterns</b> to <b>the same code using their modern replacements</b>.",
    ratings=[(2, 4, "Less machinery; frameworks and language features do the job."),
             (3, 3, "Neutral."),
             (3, 4, "No hidden global state; exhaustive matching catches missing cases."),
             (2, 4, "Dependencies and cases are explicit."),
             (1, 5, "No singletons or locators to reset between tests."),
             (2, 4, "Dependencies passed in, not grabbed globally."),
             (3, 4, "Stateless servers scale out freely."),
             (3, 4, "No hand-rolled controllers, gateways or visitors."),
             (3, 4, "Fewer hidden couplings between teams' code.")],
    pitfalls=[("Retiring by dogma", "Ripping out a working Visitor in a compiler.", "keep it where its problem still exists."),
              ("Singleton by another name", "A module-level mutable object imported everywhere.", "same problem: create once, inject."),
              ("Locator inside DI", "Classes take the container itself as a dependency.", "inject what the class needs, not the container."),
              ("Sticky sessions as a fix", "Load balancer pinning users to servers to keep session state.", "move state to a shared store or tokens.")],
    use=["Reviewing legacy code full of 2000s-era patterns.",
         "Preparing for interviews that still ask about them.",
         "Teaching why modern tools look the way they do."],
    skip=["Compilers and AST tools (Visitor still fits).",
          "True hardware or process singletons (but still inject them)."],
    related=["<b>Strategy &amp; Command as Functions</b>", "<b>Dependency Inversion</b>", "<b>Make Illegal States Unrepresentable</b> (Vol. 7)", "<b>Short-Lived Tokens</b> (Vol. 5)", "<b>Characterization Tests</b> (Vol. 4)"],
    quiz=[("What replaced the Singleton pattern in most code?", "Creating one instance in the composition root and injecting it (a singleton lifetime, not a singleton class)."),
          ("Why is Service Locator considered an anti-pattern?", "It hides a class's dependencies and fails at runtime instead of at construction."),
          ("Where is Visitor still a good fit?", "Compilers and tools walking syntax trees with many operations over a stable set of node types."),
          ("What replaced server session state?", "Stateless tokens and a shared store, so any server can handle any request.")],
    quiz_sit=[("Your test suite passes alone but fails when run in parallel. The cause is a <code>CurrencyRates.getInstance()</code> singleton that tests modify. How do you fix it without a big rewrite?",
               "Create CurrencyRates once in the composition root and pass it into the classes that use it, starting with the ones under test; give tests their own instances. Keep a temporary <code>getInstance()</code> delegating to the injected one for old callers, then remove it.")],
    try_it="Search your codebase for <code>getInstance()</code>, static mutable fields or a global container lookup. Pick one, make it a constructor parameter in two classes, and give their tests their own instance.",
    then_now=dict(src="GoF, 1994; Fowler, PoEAA 2002 and 2004", verdict="retired",
                  then="Each was a reasonable answer in its day: global access without globals (Singleton), decoupling without containers (Service Locator), new operations on fixed hierarchies (Visitor), and hand-built web and data layers before frameworks existed.",
                  now="DI with constructor injection, pattern matching over union types, full-stack web frameworks, ORMs and query builders, and stateless horizontally-scaled services made them unnecessary in most code. Singleton and Service Locator are now generally called anti-patterns.",
                  take="Mostly retired: learn to recognise them, and reach for their replacements."),
    remember="Visit the <span class=\"hl\">museum</span>, read the plaques, and <span class=\"hl\">don't fax the invoices</span>.",
    sources=["Erich Gamma et al., <i>Design Patterns</i> (1994), “Singleton”, “Visitor”.",
             "Martin Fowler, <i>Patterns of Enterprise Application Architecture</i> (2002), web presentation, data source and session state patterns.",
             "Mark Seemann, “Service Locator is an Anti-Pattern” (2010).",
             "Martin Fowler, “Inversion of Control Containers and the Dependency Injection pattern” (2004)."],
)

NOTES = [STRATEGY_COMMAND, DECORATOR, ADAPTER_FACADE, MUSEUM]
