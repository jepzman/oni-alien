// Builds the ready-made PDFs in public/pdf/ using the site's own print stylesheet.
// Usage: node scripts/build-pdf.mjs   (needs Playwright + Chromium)
import { createServer } from 'node:http';
import { readFile } from 'node:fs/promises';
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

const jobs = [
  ['notes/circuit-breaker.html', 'pdf/01-circuit-breaker.pdf'],
  ['notes/saga.html', 'pdf/02-saga.pdf'],
  ['all.html', 'pdf/margin-notes.pdf'],
];

const browser = await chromium.launch();
for (const [url, out] of jobs) {
  const page = await browser.newPage({ colorScheme: 'light' });
  await page.goto(base + url, { waitUntil: 'networkidle' });
  if (url === 'all.html') await page.waitForFunction(() => document.querySelectorAll('article.sheet').length >= 2);
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
