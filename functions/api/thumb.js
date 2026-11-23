// GET /api/thumb?id=VIDEO_ID&q=maxresdefault  -> the thumbnail as a file download
const QUALITIES = ['maxresdefault', 'sddefault', 'hqdefault', 'mqdefault', 'default'];

export async function onRequestGet(context) {
  const url = new URL(context.request.url);
  const id = url.searchParams.get('id') || '';
  const q = url.searchParams.get('q') || 'maxresdefault';
  if (!/^[A-Za-z0-9_-]{11}$/.test(id) || !QUALITIES.includes(q)) {
    return new Response('Invalid request', { status: 400 });
  }
  const r = await fetch('https://i.ytimg.com/vi/' + id + '/' + q + '.jpg');
  if (!r.ok) return new Response('Thumbnail not available', { status: 404 });
  return new Response(r.body, {
    headers: {
      'content-type': 'image/jpeg',
      'content-disposition': 'attachment; filename="youtube-thumbnail-' + id + '-' + q + '.jpg"',
      'cache-control': 'public, max-age=86400',
      'x-content-type-options': 'nosniff',
    },
  });
}
