// GET /api/yt?list=PLAYLIST_ID  (public, cached; API keys come from the environment)
import { loadConfig, activeProviders, callWithFailover } from './_providers.js';

const JSON_HEADERS = { 'content-type': 'application/json; charset=utf-8', 'cache-control': 'public, max-age=3600' };
const json = (d, s = 200) => new Response(JSON.stringify(d), { status: s, headers: JSON_HEADERS });
const API = 'https://www.googleapis.com/youtube/v3/';
const MAX_PAGES = 20;

function isoToSeconds(d) {
  const m = /^P(?:(\d+)D)?T?(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?$/.exec(d || '');
  if (!m) return 0;
  return (+m[1] || 0) * 86400 + (+m[2] || 0) * 3600 + (+m[3] || 0) * 60 + (+m[4] || 0);
}

export async function onRequestGet(context) {
  const { request, env } = context;
  const url = new URL(request.url);
  const id = (url.searchParams.get('list') || '').trim();
  if (!/^[A-Za-z0-9_-]{10,64}$/.test(id)) return json({ error: 'Invalid playlist ID' }, 400);

  const config = await loadConfig(context);
  const providers = activeProviders(config, 'youtube', env);
  if (!providers.length) return json({ error: 'Service is not configured' }, 500);

  const cache = caches.default;
  const cacheKey = new Request(url.origin + '/api/yt?list=' + id);
  const cached = await cache.match(cacheKey);
  if (cached) return cached;

  const call = path => callWithFailover(providers, env, key => API + path + '&key=' + encodeURIComponent(key));
  const fail = r => (r.exhausted
    ? json({ error: 'Daily YouTube quota reached on all keys. Try again later.' }, 503)
    : json({ error: 'YouTube API error', status: r.status }, 502));

  const pl = await call('playlists?part=snippet&id=' + encodeURIComponent(id));
  if (!pl.ok) return fail(pl);
  if (!pl.data.items || !pl.data.items.length) return json({ error: 'Playlist not found or private' }, 404);
  const title = pl.data.items[0].snippet?.title || '';

  const videoIds = [];
  let pageToken = '', pages = 0, truncated = false;
  do {
    const r = await call('playlistItems?part=contentDetails&maxResults=50&playlistId=' + encodeURIComponent(id) +
      (pageToken ? '&pageToken=' + pageToken : ''));
    if (!r.ok) return fail(r);
    for (const it of r.data.items || []) if (it.contentDetails?.videoId) videoIds.push(it.contentDetails.videoId);
    pageToken = r.data.nextPageToken || '';
    pages++;
    if (pageToken && pages >= MAX_PAGES) truncated = true;
  } while (pageToken && pages < MAX_PAGES);

  let totalSeconds = 0, counted = 0;
  for (let i = 0; i < videoIds.length; i += 50) {
    const r = await call('videos?part=contentDetails&id=' + videoIds.slice(i, i + 50).join(','));
    if (!r.ok) return fail(r);
    for (const v of r.data.items || []) { totalSeconds += isoToSeconds(v.contentDetails?.duration); counted++; }
  }

  const res = json({ title, playlistId: id, videos: counted, unavailable: videoIds.length - counted, truncated, totalSeconds }, 200);
  await cache.put(cacheKey, res.clone());
  return res;
}
