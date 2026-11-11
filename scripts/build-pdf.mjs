// Builds the ready-made PDFs in public/pdf/ using the site's own print stylesheet.
// Usage: node scripts/build-pdf.mjs   (needs Playwright + Chromium)
import { createServer } from 'node:http';
import { readFile, mkdir } from 'node:fs/promises';
import { extname, join, normalize } from 'node:path';
import { fileURLToPath } from 'node:url';
import { createRequire } from 'node:module';

const require = createRequire(import.meta.url);
const { chromium } = require('playwright');
const root = fileURLToPath(new URL('../public/', import.meta.url));
const types = { '.html': 'text/html', '.css': 'text/css', '.js': 'text/javascript', '.svg': 'image/svg+xml', '.pdf': 'application/pdf' };

const server = createServer(async (req, res) => {
  const path = normalize(decodeURIComponent(new URL(req.url, 'http://x').pathname)).replace(/^([/\\])+/, '');
  try {
    const body = await readFile(join(root, path || 'index.html'));
    res.writeHead(200, { 'content-type': types[extname(path)] || 'application/octet-stream' });
    res.end(body);
  } catch { res.writeHead(404); res.end(); }
});
await new Promise((ok) => server.listen(0, ok));
const base = `http://localhost:${server.address().port}/`;

// One PDF per note plus one per journal, from public/journals.json (written by scripts/build_notes.py).
const journals = JSON.parse(await readFile(join(root, 'journals.json'), 'utf8'));
const jobs = journals.flatMap((j) => [
  ...j.notes.map((n) => [n.page, n.pdf, 0]),
  [j.all, j.pdf, j.notes.length],
]);
await Promise.all(journals.map((j) => mkdir(join(root, j.key, 'pdf'), { recursive: true })));

const browser = await chromium.launch();
for (const [url, out, expect] of jobs) {
  const page = await browser.newPage({ colorScheme: 'light' });
  await page.goto(base + url, { waitUntil: 'networkidle' });
  if (expect) await page.waitForFunction((n) => document.querySelectorAll('article.sheet').length >= n, expect, { timeout: 90000 });
  await page.evaluate(async () => {
    await document.fonts.ready;
    document.querySelectorAll('.quiz details').forEach((d) => { d.open = true; });
  });
  await page.emulateMedia({ media: 'print' });
  await page.pdf({ path: join(root, out), format: 'A4', printBackground: true, preferCSSPageSize: true });
  console.log('wrote', out);
  await page.close();
}
await browser.close();
server.close();
