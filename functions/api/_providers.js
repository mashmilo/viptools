// Shared helpers for API functions. Provider list lives in src/config.json (edited from the admin panel).
// Secret VALUES only ever live in Cloudflare Pages environment variables, never in the repo.

export async function loadConfig(context) {
  const res = await context.env.ASSETS.fetch(new URL('/config.json', context.request.url));
  return res.ok ? res.json() : { providers: [] };
}

// Enabled providers for a tool, whose secret is actually set in the environment.
export function activeProviders(config, tool, env) {
  return (config.providers || []).filter(p => p.enabled && p.tool === tool && env[p.secret]);
}

export function isAdmin(request) {
  return !!request.headers.get('Cf-Access-Authenticated-User-Email');
}

// Calls a provider list in order. Quota and rate-limit errors move to the next key.
export async function callWithFailover(providers, env, buildUrl) {
  let lastStatus = 503;
  for (const p of providers) {
    const r = await fetch(buildUrl(env[p.secret]));
    if (r.ok) return { ok: true, data: await r.json(), provider: p.id };
    lastStatus = r.status;
    if (r.status === 403 || r.status === 429) continue;   // quota or rate limit: try the next key
    return { ok: false, status: r.status };                // other errors are not retried
  }
  return { ok: false, status: lastStatus, exhausted: true };
}
