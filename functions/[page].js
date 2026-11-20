import {esc,page,cfg} from '../lib/layout.js';import {P} from '../lib/pages.js';
export async function onRequestGet({env,params,next}){const k=params.page,raw=await env.VIPTOOLS.get('pg:'+k);
if(!raw&&!P[k]){const r=await next();if(r.status!==404)return r}
const c=await cfg(env),S=c.siteName||'VipTools',b=raw&&JSON.parse(raw),p=P[k],path='/'+k;
if(b)return page(c,{title:`${b.title} | ${S}`,desc:b.desc,path,noindex:b.noindex,body:`<main><h1>${esc(b.title)}</h1>${b.body}</main>`});
if(!p)return page(c,{status:404,noindex:1,title:'Page not found | '+S,path:'/',body:'<main><h1>Page not found</h1><p><a href="/">Go to the homepage</a></p></main>'});
return page(c,{title:`${p.t} | ${S}`,desc:p.d,path,body:`<main><h1>${p.t}</h1>${p.b(c)}</main>`})}
