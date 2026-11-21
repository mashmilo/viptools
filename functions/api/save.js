// PUT /api/save (admin only): validates and saves settings to src/config.json in GitHub.
// Cloudflare Pages then rebuilds and redeploys. Secret VALUES are never accepted or stored here.
// Required secrets (Pages settings): GITHUB_TOKEN, GITHUB_REPO (e.g. "mashmilo/viptools").
import { isAdmin } from './_providers.js';

const CATEGORIES = ['Text tools', 'Generators', 'Developer tools', 'Calculators and converters', 'Finance calculators', 'Media tools'];
const TOOL_KINDS = ['youtube'];   // add a new kind here when you add a new API function

const FIELD_RULES = {
  siteName: /^.{0,60}$/,
  ownerName: /^.{0,100}$/,
  adsenseClient: /^(ca-pub-\d{16})?$/,
  gaId: /^(G-[A-Z0-9]{4,20})?$/,
  gaPropertyId: /^(\d{5,15})?$/,
  gscVerification: /^[A-Za-z0-9_-]{0,100}$/,
  bingVerification: /^[A-Za-z0-9_-]{0,100}$/,
  adsHeader: /^[\s\S]{0,5000}$/,
};
const SECRET_NAME = /^[A-Z][A-Z0-9_]{2,63}$/;
const SLUG = /^[a-z0-9-]{3,60}$/;
const ID = /^[a-z0-9-]{3,40}$/;

const enc = s => btoa(String.fromCharCode(...new TextEncoder().encode(s)));
const dec = b64 => new TextDecoder().decode(Uint8Array.from(atob(b64.replace(/\n/g, '')), c => c.charCodeAt(0)));
const bad = (msg) => new Response(msg, { status: 400 });

function validate(body) {
  const out = {};
  for (const [k, rule] of Object.entries(FIELD_RULES)) {
    if (!(k in body)) continue;
    const v = String(body[k] ?? '').trim();
    if (!rule.test(v)) return { error: 'Invalid value for ' + k };
    out[k] = v;
  }
  if (body.toolOverrides !== undefined) {
    if (typeof body.toolOverrides !== 'object' || Array.isArray(body.toolOverrides)) return { error: 'toolOverrides must be an object' };
    out.toolOverrides = {};
    for (const [slug, o] of Object.entries(body.toolOverrides)) {
      if (!SLUG.test(slug) || !o || typeof o !== 'object') return { error: 'Invalid tool ' + slug };
      const item = {};
      if (typeof o.enabled === 'boolean') item.enabled = o.enabled;
      if (o.name !== undefined) { const n = String(o.name).trim(); if (!n || n.length > 60) return { error: 'Name for ' + slug + ' must be 1-60 characters' }; item.name = n; }
      if (o.desc !== undefined) { const d = String(o.desc).trim(); if (d.length > 160) return { error: 'Description for ' + slug + ' is too long' }; item.desc = d; }
      if (o.category !== undefined) { if (!CATEGORIES.includes(o.category)) return { error: 'Unknown category for ' + slug }; item.category = o.category; }
      out.toolOverrides[slug] = item;
    }
  }
  if (body.providers !== undefined) {
    if (!Array.isArray(body.providers) || body.providers.length > 20) return { error: 'providers must be a list' };
    out.providers = [];
    for (const p of body.providers) {
      if (!ID.test(p.id || '') || !TOOL_KINDS.includes(p.tool) || !SECRET_NAME.test(p.secret || '')) return { error: 'Invalid provider ' + (p.id || '') };
      out.providers.push({ id: p.id, label: String(p.label || p.id).slice(0, 80), tool: p.tool, secret: p.secret, enabled: !!p.enabled });
    }
    const secrets = out.providers.map(p => p.secret);
    if (new Set(secrets).size !== secrets.length) return { error: 'Each provider needs its own secret name' };
  }
  return { out };
}

export async function onRequestPut({ request, env }) {
  if (!isAdmin(request)) return new Response('Sign-in required', { status: 401 });
  if (!env.GITHUB_TOKEN || !env.GITHUB_REPO) return new Response('Server is not configured', { status: 500 });

  const body = await request.json().catch(() => null);
  if (!body || typeof body !== 'object') return bad('Bad request');
  const v = validate(body);
  if (v.error) return bad(v.error);

  const api = 'https://api.github.com/repos/' + env.GITHUB_REPO + '/contents/src/config.json';
  const headers = { Authorization: 'Bearer ' + env.GITHUB_TOKEN, Accept: 'application/vnd.github+json', 'User-Agent': 'viptools-admin' };
  const cur = await fetch(api, { headers });
  if (!cur.ok) return new Response('Could not read config', { status: 502 });
  const cj = await cur.json();
  const merged = { ...JSON.parse(dec(cj.content)), ...v.out };

  const put = await fetch(api, {
    method: 'PUT', headers,
    body: JSON.stringify({ message: 'Admin update by ' + request.headers.get('Cf-Access-Authenticated-User-Email'), content: enc(JSON.stringify(merged, null, 1) + '\n'), sha: cj.sha }),
  });
  if (!put.ok) return new Response('GitHub save failed (' + put.status + ')', { status: 502 });
  return new Response(JSON.stringify({ ok: true, saved: Object.keys(v.out) }), { headers: { 'content-type': 'application/json' } });
}
