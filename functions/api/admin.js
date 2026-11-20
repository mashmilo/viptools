export async function onRequest({request,env}){
if(!env.ADMIN_PASSWORD||request.headers.get('x-admin-token')!==env.ADMIN_PASSWORD)return new Response('Unauthorized',{status:401});
const K=env.VIPTOOLS,rd=async(k,d)=>JSON.parse(await K.get(k)||d),J=o=>new Response(JSON.stringify(o),{headers:{'content-type':'application/json'}}),ok=s=>/^[a-z0-9-]{2,80}$/.test(s||'');
if(request.method!=='POST'){const q=new URL(request.url).searchParams,s=q.get('slug'),p=q.get('page');
return s?J(await rd('tool:'+s,'null')):p?J(await rd('pg:'+p,'null')):J({config:await rd('config','{}'),tools:await rd('tools','[]'),pages:await rd('pages','[]')})}
const b=await request.json(),now=new Date().toISOString();let l=await rd('tools','[]'),g=await rd('pages','[]');
if(b.a==='tool'){const t=b.tool;if(!t||!ok(t.slug)||!t.name||!t.desc)return new Response('Need slug (a-z, 0-9, -), name and desc',{status:400});
const o=l.find(x=>x.slug===t.slug),e={slug:t.slug,name:t.name,cat:t.cat||'Tools',desc:t.desc,tags:t.tags||[],featured:!!t.featured,order:+t.order||0,noindex:!!t.noindex,on:o?o.on!==false:true,updated:now};
l=o?l.map(x=>x.slug===t.slug?e:x):[...l,e];await K.put('tool:'+t.slug,JSON.stringify(t));await K.put('tools',JSON.stringify(l))}
else if(b.a==='toggle'){l=l.map(x=>x.slug===b.slug?{...x,on:b.on}:x);await K.put('tools',JSON.stringify(l))}
else if(b.a==='del'){l=l.filter(x=>x.slug!==b.slug);await K.delete('tool:'+b.slug);await K.put('tools',JSON.stringify(l))}
else if(b.a==='page'){const p=b.pg;if(!p||!ok(p.slug)||!p.title||!p.body||['admin','api','tools'].includes(p.slug))return new Response('Need a valid slug, title and body',{status:400});
const e={slug:p.slug,title:p.title,footer:!!p.footer,noindex:!!p.noindex,updated:now};g=g.some(x=>x.slug===p.slug)?g.map(x=>x.slug===p.slug?e:x):[...g,e];await K.put('pg:'+p.slug,JSON.stringify(p));await K.put('pages',JSON.stringify(g))}
else if(b.a==='pdel'){g=g.filter(x=>x.slug!==b.slug);await K.delete('pg:'+b.slug);await K.put('pages',JSON.stringify(g))}
else if(b.a==='config'){await K.put('config',JSON.stringify(b.config))}
return J({ok:1,tools:l,pages:g})}
