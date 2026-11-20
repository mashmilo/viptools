import {cfg} from '../../../lib/layout.js';
export async function onRequest({request,env,params}){const a=((await cfg(env)).apis||{})[params.name];
if(!a||a.on===false)return new Response('Not found',{status:404});
const K=s=>String(s).replaceAll('{KEY}',a.key||''),u=new URL(K(a.url));new URL(request.url).searchParams.forEach((v,k)=>u.searchParams.set(k,v));
const h={};for(const k in a.headers||{})h[k]=K(a.headers[k]);
const r=await fetch(u,{method:request.method==='POST'?'POST':'GET',headers:h,body:request.method==='POST'?await request.text():undefined});
return new Response(r.body,{status:r.status,headers:{'content-type':r.headers.get('content-type')||'text/plain'}})}
