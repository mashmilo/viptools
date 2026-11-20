(function(){
  // Load the current stylesheet with a version number and remove any old copy
  document.querySelectorAll('link[href^="/style.css"]').forEach(function(l){l.parentNode.removeChild(l)});
  var css=document.createElement('link');css.rel='stylesheet';css.href='/style.css?v=5';document.head.appendChild(css);

  var ICON_SUN='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg>';
  var ICON_MOON='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8z"/></svg>';
  var ICON_MENU='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M4 7h16M4 12h16M4 17h16"/></svg>';
  var LOGO='<svg width="32" height="32" viewBox="0 0 64 64" aria-hidden="true"><defs><linearGradient id="vtg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#6366f1"/><stop offset="1" stop-color="#06b6d4"/></linearGradient></defs><rect width="64" height="64" rx="16" fill="url(#vtg)"/><path d="M16 20l16 28 16-28" fill="none" stroke="#fff" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/></svg>';

  function currentTheme(){return document.documentElement.getAttribute('data-theme')==='dark'?'dark':'light'}
  function applyTheme(t){
    document.documentElement.setAttribute('data-theme',t);
    try{localStorage.setItem('vt-theme',t)}catch(e){}
    var m=document.querySelector('meta[name=theme-color]');if(m)m.content=t==='dark'?'#0b1020':'#6366f1';
    document.querySelectorAll('.theme-btn:not(.menu-btn)').forEach(function(b){b.innerHTML=t==='dark'?ICON_SUN:ICON_MOON;b.setAttribute('aria-label','Switch to '+(t==='dark'?'light':'dark')+' mode')});
  }

  function header(){
    var h=document.createElement('header');h.className='site-header';
    h.innerHTML=
      '<div class="w nav">'+
        '<a class="brand" href="/">'+LOGO+'<div>Vip<span>Tools</span></div></a>'+
        '<nav class="menu" aria-label="Main">'+
          '<a class="hide-m" href="/">Home</a>'+
          '<div class="dd" id="ddTools"><button type="button" aria-expanded="false">Tools &#9662;</button><div class="dd-panel" id="ddPanel"></div></div>'+
          '<a class="hide-m" href="/about.html">About</a>'+
          '<a class="hide-m" href="/contact.html">Contact</a>'+
          '<a class="hide-m" href="/privacy.html">Privacy</a>'+
          '<button class="theme-btn" type="button" aria-label="Toggle theme"></button>'+
          '<button class="theme-btn menu-btn" type="button" aria-label="Open menu" aria-expanded="false">'+ICON_MENU+'</button>'+
        '</nav>'+
      '</div>'+
      '<div class="mobile-menu" id="mm">'+
        '<a href="/">Home</a>'+
        '<a href="/about.html">About</a><a href="/contact.html">Contact</a><a href="/privacy.html">Privacy</a>'+
        '<div style="padding:12px 4px 4px;font-weight:600;color:var(--muted);font-size:13px">ALL TOOLS</div>'+
        '<div class="sub" id="mmTools"></div>'+
      '</div>';
    return h;
  }

  function footer(){
    var f=document.createElement('footer');f.className='site-footer';
    f.innerHTML='<div class="w foot"><div><a class="brand" href="/" style="font-size:17px">'+LOGO.replace('width="32" height="32"','width="26" height="26"')+'<div>Vip<span>Tools</span></div></a><p style="margin-top:8px">Free, fast and private online tools. Everything runs in your browser.</p></div>'+
      '<nav><a href="/">Home</a><a href="/about.html">About</a><a href="/contact.html">Contact</a><a href="/privacy.html">Privacy Policy</a><a href="/terms.html">Terms</a></nav>'+
      '<p>&copy; <span id="y"></span> VipTools.online</p></div>';
    f.querySelector('#y').textContent=new Date().getFullYear();
    return f;
  }

  function wireHeader(tools){
    var dd=document.getElementById('ddTools'),panel=document.getElementById('ddPanel'),mm=document.getElementById('mmTools');
    var list=tools.filter(function(t){return t.enabled});
    var links=list.map(function(t){return '<a href="'+(t.html?'/tool.html?s='+t.slug:'/tools/'+t.slug+'/')+'">'+t.name+'</a>'}).join('');
    panel.innerHTML=links+'<a href="/" style="grid-column:1/-1;text-align:center;color:var(--primary);font-weight:600">View all tools &rarr;</a>';
    mm.innerHTML=links;
    var b=dd.querySelector('button');
    b.addEventListener('click',function(e){e.stopPropagation();var o=dd.classList.toggle('open');b.setAttribute('aria-expanded',o)});
    document.addEventListener('click',function(e){if(!dd.contains(e.target)){dd.classList.remove('open');b.setAttribute('aria-expanded','false')}});
    var mb=document.querySelector('.menu-btn'),mmEl=document.getElementById('mm');
    mb.addEventListener('click',function(){var o=mmEl.classList.toggle('open');mb.setAttribute('aria-expanded',o)});
    document.querySelector('.theme-btn:not(.menu-btn)').addEventListener('click',function(){applyTheme(currentTheme()==='dark'?'light':'dark')});
    applyTheme(currentTheme());
  }

  var oldH=document.querySelector('body > header');if(oldH)oldH.replaceWith(header());else document.body.prepend(header());
  var oldF=document.querySelector('body > footer');if(oldF)oldF.replaceWith(footer());else document.body.append(footer());
  applyTheme(currentTheme());

  fetch('/config.json?'+Date.now()).then(function(r){return r.json()}).then(function(c){
    var h=document.head;
    if(c.gscVerification){var m=document.createElement('meta');m.name='google-site-verification';m.content=c.gscVerification;h.append(m)}
    if(c.bingVerification){var bm=document.createElement('meta');bm.name='msvalidate.01';bm.content=c.bingVerification;h.append(bm)}
    if(c.gaId){var s=document.createElement('script');s.async=1;s.src='https://www.googletagmanager.com/gtag/js?id='+c.gaId;h.append(s);window.dataLayer=window.dataLayer||[];window.gtag=function(){dataLayer.push(arguments)};gtag('js',new Date);gtag('config',c.gaId)}
    if(c.adsenseClient){var a=document.createElement('script');a.async=1;a.crossOrigin='anonymous';a.src='https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client='+c.adsenseClient;h.append(a)}
    document.querySelectorAll('.ad').forEach(function(a){if(c.adsHeader)a.innerHTML=c.adsHeader});
    wireHeader(c.tools);
    var g=document.getElementById('grid');
    if(g){
      var draw=function(q){
        var items=c.tools.filter(function(t){return t.enabled && (!q||(t.name+' '+t.desc).toLowerCase().indexOf(q)>-1)});
        g.innerHTML=items.map(function(t){return '<a class="card" href="'+(t.html?'/tool.html?s='+t.slug:'/tools/'+t.slug+'/')+'"><h3>'+t.name+'</h3><p>'+t.desc+'</p></a>'}).join('')||'<p class="muted">No tools match your search.</p>';
        var cnt=document.getElementById('toolCount');if(cnt)cnt.textContent=items.length+' tools';
      };
      draw('');
      var si=document.getElementById('search');
      if(si)si.addEventListener('input',function(){draw(this.value.trim().toLowerCase())});
    }
    var me=document.body.dataset.tool;
    if(me){var t=c.tools.find(function(x){return x.slug===me});if(t&&!t.enabled){var ap=document.getElementById('app');if(ap)ap.innerHTML='<p>This tool is temporarily unavailable.</p>'}}
  }).catch(function(){wireHeader([])});
})();
