// GET /api/yt-video?id=VIDEO_ID  (public, cached; API keys come from the environment)
import { loadConfig, activeProviders, callWithFailover } from './_providers.js';

const JSON_HEADERS = { 'content-type': 'application/json; charset=utf-8', 'cache-control': 'public, max-age=3600' };
const json = (d, s = 200) => new Response(JSON.stringify(d), { status: s, headers: JSON_HEADERS });
const API = 'https://www.googleapis.com/youtube/v3/';

export async function onRequestGet(context) {
  const { request, env } = context;
  const url = new URL(request.url);
  const id = (url.searchParams.get('id') || '').trim();
  if (!/^[A-Za-z0-9_-]{11}$/.test(id)) return json({ error: 'Invalid video ID' }, 400);

  const config = await loadConfig(context);
  const providers = activeProviders(config, 'youtube', env);
  if (!providers.length) return json({ error: 'Service is not configured' }, 500);

  const cache = caches.default;
  const cacheKey = new Request(url.origin + '/api/yt-video?id=' + id);
  const cached = await cache.match(cacheKey);
  if (cached) return cached;

  const r = await callWithFailover(providers, env, key =>
    API + 'videos?part=snippet,statistics&id=' + encodeURIComponent(id) + '&key=' + encodeURIComponent(key));
  if (!r.ok) {
    return r.exhausted
      ? json({ error: 'Daily YouTube quota reached on all keys. Try again later.' }, 503)
      : json({ error: 'YouTube API error', status: r.status }, 502);
  }
  const item = r.data.items && r.data.items[0];
  if (!item) return json({ error: 'Video not found or private' }, 404);

  const s = item.snippet || {};
  const hashtags = [...new Set(((s.title || '') + ' ' + (s.description || '')).match(/#[\p{L}\p{N}_]+/gu) || [])].slice(0, 40);
  const views = item.statistics && item.statistics.viewCount;
  const res = json({
    id,
    title: s.title || '',
    channelTitle: s.channelTitle || '',
    channelId: s.channelId || '',
    publishedAt: s.publishedAt || '',
    tags: Array.isArray(s.tags) ? s.tags : [],
    hashtags,
    viewCount: views != null ? Number(views) : null,
  });
  await cache.put(cacheKey, res.clone());
  return res;
}
