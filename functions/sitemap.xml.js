import {cfg,list,esc,D} from '../lib/layout.js';import {P} from '../lib/pages.js';
export async function onRequestGet({env}){const c=await cfg(env),t=(await list(env)).filter(x=>x.on!==false&&!x.noindex),d=new Date().toISOString().slice(0,10);
const pg=[...new Set([...Object.keys(P),...c._p.filter(p=>!p.noindex).map(p=>p.slug)])];
const u=[['/',d],...pg.map(k=>['/'+k,d]),...t.map(x=>['/tools/'+x.slug,(x.updated||d).slice(0,10)])];
return new Response(`<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">${u.map(([p,m])=>`<url><loc>${D}${esc(p)}</loc><lastmod>${m}</lastmod></url>`).join('')}</urlset>`,{headers:{'content-type':'application/xml','cache-control':'public,max-age=600'}})}
