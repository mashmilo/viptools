import {cfg,D} from '../lib/layout.js';
export async function onRequestGet({env}){const c=await cfg(env);return new Response(c.robotsTxt||`User-agent: *\nAllow: /\nDisallow: /admin/\nDisallow: /api/\nSitemap: ${D}/sitemap.xml`,{headers:{'content-type':'text/plain'}})}
