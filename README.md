# VipTools

Static tools site built by `build.py`, deployed by Cloudflare Pages.

## Layout
- `build.py`: generates the site into `dist/` (run `python3 build.py`).
- `src/`: site source. `config.json` holds settings edited from the admin panel. `tools-src/` holds the original tool pages. `content_*.py` holds tool text.
- `functions/api/`: Cloudflare Pages Functions (YouTube lookup, admin save, admin status).
- `dist/`: generated output (not committed).

## Cloudflare Pages settings
- Build command: `python3 build.py`
- Build output directory: `dist`
- Environment variables (encrypted): `GITHUB_TOKEN`, `GITHUB_REPO` (`mashmilo/viptools`), `YT_API_KEY`, `YT_API_KEY_2`
- Cloudflare Access: protect `/admin/*`, `/api/save` and `/api/status` (allow your email only).

## YouTube tools (added)
- Thumbnail downloader: `/api/thumb` (public, streams the JPG as a download, no quota used).
- Tag extractor and timestamp generator: video tags via `/api/yt-video` (1 quota unit per lookup).
- Channel ID finder: `/api/yt-channel` (1 unit per lookup; a bare custom name without a handle falls back to search at 100 units).
- Playlist length calculator: `/api/yt` (uses the playlist pages, cached one hour).
Results are cached at the edge for one hour, which keeps YouTube API quota low.

## Adding a tool
1. Add the tool page to `src/tools-src/<slug>/index.html` in the same format, and add its entry in `build.py` (`tool(...)`).
2. Add its text to `src/content_*.py`.
3. Run `python3 build.py` locally to check it builds (it prints the tool count).
4. Commit and push. Cloudflare rebuilds the site.
