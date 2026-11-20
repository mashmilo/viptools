# VipTools core: Cloudflare Pages
1. Upload this folder to GitHub. Cloudflare > Workers & Pages > Create > Pages > connect repo. Build command: empty. Output directory: static
2. Settings > Bindings: KV namespace, variable name VIPTOOLS. Settings > Variables and Secrets: secret ADMIN_PASSWORD. Redeploy once.
3. Add custom domain viptools.online. Open /admin/ and fill the site settings.
4. Submit https://viptools.online/sitemap.xml in Google Search Console.
Tool JSON fields: slug, name, cat, title (SEO title), h1, desc (meta description), tags[], image (social share image URL), featured, order, noindex, body (HTML text), faq [[q,a]], html, css, js.
Page JSON fields: slug, title, desc, body (HTML), footer (show in footer), noindex.
API connections: {"weather":{"url":"https://api.x.com/v1?key={KEY}","key":"SECRET"}} then fetch('/api/p/weather?q=London') in tool js.
