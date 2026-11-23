/* Top Analysts — minimal static viewer. Reads sessions/index.json, then round JSON files on demand. */
(() => {
  const $ = (s, el = document) => el.querySelector(s);
  const side = $('#side'), view = $('#view'), q = $('#q');
  let INDEX = null, ROUND_CACHE = {}, FULLTEXT = null;

  const esc = s => String(s ?? '').replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
  const md = s => (window.marked ? marked.parse(String(s ?? '')) : `<p>${esc(s)}</p>`);
  const ename = slug => (INDEX.experts[slug]?.name) || slug;
  const fmtTs = ts => ts ? ts.replace('T', ' ').replace(/([+-]\d\d:\d\d|Z)$/, m => ` (${m})`) : '';

  async function loadIndex() {
    const r = await fetch('sessions/index.json', { cache: 'no-store' });
    INDEX = await r.json();
    $('#built').textContent = `index built ${fmtTs(INDEX.built_at)}`;
    $('#stats').textContent = `${INDEX.companies.length} 家公司 · ${INDEX.n_rounds} 轮讨论 · ${Object.keys(INDEX.experts).length} 位专家`;
    renderSide();
    route();
    prefetchAll();
  }

  function renderSide(filter = '') {
    const f = filter.trim().toLowerCase();
    const cos = INDEX.companies.filter(c => !f || (c.name + c.ts_code + c.industry).toLowerCase().includes(f));
    side.innerHTML = cos.length ? cos.map(c => `
      <div class="co" data-co="${c.ts_code}"><b>${esc(c.name)} <small>${c.ts_code}</small></b><small>${esc(c.industry)} · ${c.sessions.length} session(s)</small></div>
      ${c.sessions.map(s => `<div class="sess" data-co="${c.ts_code}" data-s="${s.session_id}">${s.session_id} · ${s.rounds.length} 轮 · ${s.status}</div>`).join('')}
    `).join('') : '<div class="muted">no sessions yet</div>';
    side.querySelectorAll('[data-co]').forEach(el => el.onclick = () => {
      location.hash = el.dataset.s ? `#/${el.dataset.co}/${el.dataset.s}` : `#/${el.dataset.co}`;
    });
  }

  function findSession(co, sid) {
    const c = INDEX.companies.find(x => x.ts_code === co);
    if (!c) return {};
    const s = sid ? c.sessions.find(x => x.session_id === sid) : c.sessions[0];
    return { c, s };
  }

  async function getRound(path) {
    if (!ROUND_CACHE[path]) ROUND_CACHE[path] = fetch(path, { cache: 'no-store' }).then(r => r.json());
    return ROUND_CACHE[path];
  }

  async function route() {
    const h = location.hash.replace(/^#\/?/, '');
    side.querySelectorAll('.active').forEach(e => e.classList.remove('active'));
    if (!h) return;
    const [co, sid, rn] = h.split('/');
    const { c, s } = findSession(co, sid);
    if (!c || !s) { view.innerHTML = '<div class="card">not found</div>'; return; }
    side.querySelector(`.co[data-co="${co}"]`)?.classList.add('active');
    side.querySelector(`.sess[data-co="${co}"][data-s="${s.session_id}"]`)?.classList.add('active');
    view.innerHTML = `<div class="crumbs"><a href="#">首页</a> › ${esc(c.name)} ${c.ts_code} › ${s.session_id}</div>
      <h1>${esc(c.name)} <span class="muted">${c.ts_code} · ${esc(c.industry)}</span></h1>
      <div class="card">
        <div class="cast">${s.experts.map(e => `<span class="chip" title="${esc(INDEX.experts[e]?.tagline || '')}">${avatar(e)}${esc(shortName(e))}</span>`).join('')}</div>
        <div class="muted" style="margin-top:6px">Session ${s.session_id} · <a href="https://github.com/chenjing002/top-analysts/tree/main/sessions/${co}/${s.session_id}" target="_blank">原始文件与数据</a></div>
      </div>
      <div id="rounds"></div>`;
    const wrap = $('#rounds');
    const rounds = rn ? s.rounds.filter(r => String(r.round) === rn) : s.rounds;
    for (const r of rounds) {
      const box = document.createElement('div'); box.className = 'card'; box.innerHTML = `<div class="muted">loading round ${r.round}…</div>`; wrap.appendChild(box);
      try { box.innerHTML = renderRound(await getRound(r.json), r); } catch (e) { box.innerHTML = `<div class="muted">failed to load ${r.json}</div>`; }
    }
  }

  // ---- avatars: monogram + colour per expert (generated, no image files)
  const AV = {
    'stephen-penman': ['#1f6feb', 'SP'], 'warren-buffett': ['#b3541e', 'WB'], 'michael-mauboussin': ['#7a42c8', 'MM'],
    'jeff-bezos': ['#d98a00', 'JB'], 'rockwood': ['#0f8a7a', 'RW'], 'joel-greenblatt': ['#2d7a3e', 'JG'],
    'li-lu': ['#c23b4a', 'LL'], 'joekray-mond': ['#5b6470', 'JM'],
  };
  const avatar = slug => {
    const [c, ini] = AV[slug] || ['#6b6b66', (slug || '?').slice(0, 2).toUpperCase()];
    return `<span class="av" style="--c:${c}" aria-hidden="true">${ini}</span>`;
  };
  const shortName = slug => ename(slug).split(' — ')[0].replace(/\s*\(.*?\)/, '');

  function renderRound(R, meta) {
    const seen = new Set();
    const msg = s => {
      const first = !seen.has(s.expert); seen.add(s.expert);
      const exp = INDEX.experts[s.expert] || {};
      return `<div class="msg">
        ${avatar(s.expert)}
        <div class="bub-wrap">
          <div class="who"><b>${esc(shortName(s.expert))}</b>${first && exp.tagline ? `<span class="role">${esc(exp.tagline.split(/[:.;]/)[0].slice(0, 70))}</span>` : ''}</div>
          <div class="bub md">${md(s.text)}</div>
        </div>
      </div>`;
    };
    const dis = (R.disagreements || []).filter(d => d.status !== 'resolved');
    return `
      <div class="round-h"><span class="tag">Round ${R.round}</span><h2>${esc(R.question)}</h2></div>
      <div class="cast">${R.participants.map(p => `<span class="chip">${avatar(p)}${esc(shortName(p))}</span>`).join('')}</div>
      <div class="chat">${R.statements.map(msg).join('')}</div>
      <div class="concl"><b>结论 · Conclusion</b> <span class="tag ${R.conclusion.confidence}">${R.conclusion.confidence}</span>
        <div class="md">${md(R.conclusion.answer)}</div>
        ${dis.length ? `<div class="md"><b>仍未解决的分歧</b><ul>${dis.map(d => `<li>${esc(d.topic)}</li>`).join('')}</ul></div>` : ''}
        ${R.conclusion.what_would_change_our_mind?.length ? `<details><summary>什么会改变我们的看法</summary><ul>${R.conclusion.what_would_change_our_mind.map(x => `<li>${esc(x)}</li>`).join('')}</ul></details>` : ''}
      </div>
      <div class="muted" style="margin-top:8px">完整记录（含依据）：<a href="${meta.md}" target="_blank">markdown</a> · <a href="${meta.json}" target="_blank">json</a>${meta.observer ? ` · <a href="${meta.observer}" target="_blank">observer</a>` : ''}</div>`;
  }

  // ---- search: index fields first, then full statement text once rounds are prefetched
  async function prefetchAll() {
    const all = [];
    for (const c of INDEX.companies) for (const s of c.sessions) for (const r of s.rounds) all.push({ c, s, r });
    if (all.length > 400) return; // keep it cheap; index-level search still works
    FULLTEXT = [];
    for (const x of all) {
      try {
        const R = await getRound(x.r.json);
        FULLTEXT.push({ ...x, text: R.statements.map(st => `${ename(st.expert)} ${st.text} ${(st.evidence || []).map(e => e.claim).join(' ')}`).join('\n').toLowerCase() });
      } catch (e) { /* skip */ }
    }
  }

  function search(term) {
    const t = term.trim().toLowerCase();
    if (!t) { route(); return; }
    const hits = [];
    for (const c of INDEX.companies) for (const s of c.sessions) for (const r of s.rounds) {
      const hay = [c.name, c.ts_code, c.industry, r.question, r.conclusion, ...r.participants.map(ename), ...(r.thinkers || [])].join(' ').toLowerCase();
      let snippet = '';
      let ok = hay.includes(t);
      if (!ok && FULLTEXT) {
        const ft = FULLTEXT.find(x => x.r.json === r.json);
        if (ft && ft.text.includes(t)) { ok = true; const i = ft.text.indexOf(t); snippet = ft.text.slice(Math.max(0, i - 80), i + 120); }
      }
      if (ok) hits.push({ c, s, r, snippet });
    }
    view.innerHTML = `<h2>搜索 “${esc(term)}” · ${hits.length} 条</h2>` + (hits.length ? hits.map(h => `
      <div class="result" onclick="location.hash='#/${h.c.ts_code}/${h.s.session_id}/${h.r.round}'">
        <b>${esc(h.c.name)}</b> <span class="muted">${h.c.ts_code} · ${h.s.session_id} · Round ${h.r.round} · ${fmtTs(h.r.ended_at || h.r.started_at)}</span>
        <div>${esc(h.r.question)}</div>
        <div class="muted">${esc(h.r.conclusion).slice(0, 200)}</div>
        ${h.snippet ? `<div class="muted">…${esc(h.snippet)}…</div>` : ''}
      </div>`).join('') : '<div class="muted">no matches</div>');
  }

  q.addEventListener('input', () => { renderSide(q.value); search(q.value); });
  window.addEventListener('hashchange', route);
  loadIndex().catch(e => { view.innerHTML = `<div class="card">Failed to load sessions/index.json: ${esc(e)}</div>`; });
})();
