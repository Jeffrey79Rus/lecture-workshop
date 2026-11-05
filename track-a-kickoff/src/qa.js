const { chromium } = require('playwright');
const fs = require('fs');
(async () => {
  const [, , file, outdir] = process.argv;
  fs.mkdirSync(outdir, { recursive: true });
  const b = await chromium.launch();
  const pg = await b.newPage({ viewport: { width: 1400, height: 900 }, deviceScaleFactor: 1 });
  await pg.goto('file://' + file);
  await pg.waitForTimeout(300);
  const issues = [];
  for (const v of ['study', 'brief']) {
    await pg.evaluate(v => { location.hash = v; }, v);
    await pg.waitForTimeout(150);
    const n = await pg.$$eval(`#v-${v} .frame`, fs => fs.length);
    for (let i = 0; i < n; i++) {
      const res = await pg.evaluate(([v, i]) => {
        const f = document.querySelectorAll(`#v-${v} .frame`)[i];
        const s = f.querySelector('.slide');
        f.style.width = '1280px'; f.style.setProperty('--k', '1');
        const out = []; const IN = 96;
        s.querySelectorAll('.bx,.ph').forEach(e => {
          const name = (e.className + ' ' + (e.textContent || '').trim().slice(0, 26)).replace(/\s+/g, ' ');
          if (e.scrollHeight > e.clientHeight + 1) out.push(`OVERFLOW-V ${e.scrollHeight - e.clientHeight}px :: ${name}`);
          if (e.scrollWidth > e.clientWidth + 1) out.push(`OVERFLOW-H ${e.scrollWidth - e.clientWidth}px :: ${name}`);
          if (e.classList.contains('bx')) {
            const top = parseFloat(e.style.top) / IN, h = parseFloat(e.style.height) / IN, l = parseFloat(e.style.left) / IN, w = parseFloat(e.style.width) / IN;
            if (top + h > 6.751) out.push(`BELOW-B ${(top + h).toFixed(3)}in :: ${name}`);
            if (l < 0.457 || l + w > 12.959) out.push(`OUT-LR ${l.toFixed(3)}-${(l + w).toFixed(3)} :: ${name}`);
          }
        });
        const h = s.querySelector('.ph.head');
        const r = document.createRange(); r.selectNodeContents(h);
        const rects = [...r.getClientRects()]; const tops = new Set(rects.map(x => Math.round(x.top)));
        if (tops.size > 2) out.push(`HEADLINE ${tops.size} lines`);
        s.querySelectorAll('.bx, .bx *').forEach(e => {
          const fz = parseFloat(getComputedStyle(e).fontSize);
          const hasText = [...e.childNodes].some(c => c.nodeType === 3 && c.textContent.trim());
          if (hasText && fz < 15.9 && e.tagName !== 'SUP' && !e.closest('sup')) out.push(`FONT<12pt ${fz}px :: ${(e.textContent || '').trim().slice(0, 20)}`);
        });
        const ft = s.querySelector('.ph.foot div');
        if (ft && ft.offsetHeight > 3 * 12.8 + 2) out.push(`FOOTER >3 lines (${ft.offsetHeight}px)`);
        return out;
      }, [v, i]);
      const el = (await pg.$$(`#v-${v} .frame`))[i];
      await el.screenshot({ path: `${outdir}/${v}-${i + 1}.png` });
      await pg.evaluate(([v, i]) => { document.querySelectorAll(`#v-${v} .frame`)[i].style.width = ''; }, [v, i]);
      res.forEach(r => issues.push(`${v}-${i + 1}: ${r}`));
    }
  }
  console.log(issues.length ? issues.join('\n') : 'NO ISSUES');
  await b.close();
})();
