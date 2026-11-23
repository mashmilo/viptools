// GET /api/yt-channel?kind=id|handle|user|custom|video&q=VALUE  (public, cached)
// Costs 1 quota unit per lookup. Only a bare custom name that is not a handle falls back to search (100 units).
import { loadConfig, activeProviders, callWithFailover } from './_providers.js';

const JSON_HEADERS = { 'content-type': 'application/json; charset=utf-8', 'cache-control': 'public, max-age=3600' };
const json = (d, s = 200) => new Response(JSON.stringify(d), { status: s, headers: JSON_HEADERS });
const API = 'https://www.googleapis.com/youtube/v3/';
const KINDS = ['id', 'handle', 'user', 'custom', 'video'];
const PART = 'channels?part=snippet,statistics&';

export async function onRequestGet(context) {
  const { request, env } = context;
  const url = new URL(request.url);
  const kind = url.searchParams.get('kind') || '';
  const q = (url.searchParams.get('q') || '').trim();
  if (!KINDS.includes(kind) || !q || q.length > 100) return json({ error: 'Invalid request' }, 400);
  if (kind === 'id' && !/^UC[A-Za-z0-9_-]{22}$/.test(q)) return json({ error: 'Invalid channel ID' }, 400);
  if (kind === 'video' && !/^[A-Za-z0-9_-]{11}$/.test(q)) return json({ error: 'Invalid video ID' }, 400);

  const config = await loadConfig(context);
  const providers = activeProviders(config, 'youtube', env);
  if (!providers.length) return json({ error: 'Service is not configured' }, 500);

  const cache = caches.default;
  const cacheKey = new Request(url.origin + '/api/yt-channel?kind=' + kind + '&q=' + encodeURIComponent(q.toLowerCase()));
  const cached = await cache.match(cacheKey);
  if (cached) return cached;

  const call = path => callWithFailover(providers, env, key => API + path + '&key=' + encodeURIComponent(key));
  const fail = r => (r.exhausted
    ? json({ error: 'Daily YouTube quota reached on all keys. Try again later.' }, 503)
    : json({ error: 'YouTube API error', status: r.status }, 502));
  const E = encodeURIComponent;

  let r, approximate = false;
  if (kind === 'id') {
    r = await call(PART + 'id=' + E(q));
  } else if (kind === 'user') {
    r = await call(PART + 'forUsername=' + E(q));
  } else if (kind === 'video') {
    const v = await call('videos?part=snippet&id=' + E(q));
    if (!v.ok) return fail(v);
    const cid = v.data.items && v.data.items[0] && v.data.items[0].snippet.channelId;
    if (!cid) return json({ error: 'Video not found or private' }, 404);
    r = await call(PART + 'id=' + E(cid));
  } else {
    r = await call(PART + 'forHandle=' + E('@' + q.replace(/^@/, '')));
    if (r.ok && (!r.data.items || !r.data.items.length) && kind === 'custom') {
      const sr = await call('search?part=snippet&type=channel&maxResults=1&q=' + E(q));
      if (!sr.ok) return fail(sr);
      const cid = sr.data.items && sr.data.items[0] && (sr.data.items[0].snippet.channelId || (sr.data.items[0].id && sr.data.items[0].id.channelId));
      if (cid) { approximate = true; r = await call(PART + 'id=' + E(cid)); }
    }
  }
  if (!r.ok) return fail(r);
  const c = r.data.items && r.data.items[0];
  if (!c) return json({ error: 'Channel not found' }, 404);

  const sn = c.snippet || {}, st = c.statistics || {};
  const th = sn.thumbnails || {};
  const res = json({
    channelId: c.id,
    title: sn.title || '',
    handle: sn.customUrl || '',
    thumbnail: (th.default && th.default.url) || '',
    subscribers: st.hiddenSubscriberCount ? null : (st.subscriberCount != null ? Number(st.subscriberCount) : null),
    videos: st.videoCount != null ? Number(st.videoCount) : null,
    views: st.viewCount != null ? Number(st.viewCount) : null,
    approximate,
  });
  await cache.put(cacheKey, res.clone());
  return res;
}
