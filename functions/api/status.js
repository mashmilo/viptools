// GET /api/status (admin only): which providers exist and whether their secret is set. Never returns values.
import { loadConfig, isAdmin } from './_providers.js';

export async function onRequestGet(context) {
  if (!isAdmin(context.request)) return new Response('Sign-in required', { status: 401 });
  const config = await loadConfig(context);
  const list = (config.providers || []).map(p => ({
    id: p.id, label: p.label, tool: p.tool, secret: p.secret, enabled: !!p.enabled,
    secretSet: !!context.env[p.secret],
  }));
  return new Response(JSON.stringify({ providers: list }), { headers: { 'content-type': 'application/json', 'cache-control': 'no-store' } });
}
