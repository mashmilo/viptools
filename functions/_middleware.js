// Password check for the admin page and the two admin endpoints.
// Set ADMIN_USER and ADMIN_PASSWORD as encrypted variables in Cloudflare Pages. Nothing is stored in the repo.
const PROTECTED = [/^\/admin(\/|\.html|$)/, /^\/api\/(save|status)$/];

function same(a, b) {
  if (a.length !== b.length) return false;
  let diff = 0;
  for (let i = 0; i < a.length; i++) diff |= a.charCodeAt(i) ^ b.charCodeAt(i);
  return diff === 0;
}

export async function onRequest(context) {
  const url = new URL(context.request.url);
  if (!PROTECTED.some(r => r.test(url.pathname))) return context.next();

  const user = context.env.ADMIN_USER, pass = context.env.ADMIN_PASSWORD;
  if (!user || !pass) return new Response('Admin is not configured', { status: 503 });

  let ok = false, name = '';
  const h = context.request.headers.get('Authorization') || '';
  if (h.startsWith('Basic ')) {
    try {
      const decoded = atob(h.slice(6));
      const i = decoded.indexOf(':');
      const u = decoded.slice(0, i), p = decoded.slice(i + 1);
      ok = same(u, user) && same(p, pass);
      name = u;
    } catch (e) { ok = false; }
  }
  if (!ok) {
    return new Response('Sign-in required', {
      status: 401,
      headers: { 'WWW-Authenticate': 'Basic realm="VipTools Admin", charset="UTF-8"', 'cache-control': 'no-store' },
    });
  }
  context.data.isAdmin = true;
  context.data.user = name;
  const res = await context.next();
  const headers = new Headers(res.headers);
  headers.set('cache-control', 'no-store');
  return new Response(res.body, { status: res.status, statusText: res.statusText, headers });
}
