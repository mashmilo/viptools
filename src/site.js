(function(){
  var KEY='vt-consent';
  var ICON_SUN='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg>';
  var ICON_MOON='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8z"/></svg>';

  function currentTheme(){return document.documentElement.getAttribute('data-theme')==='dark'?'dark':'light'}
  function applyTheme(t){
    document.documentElement.setAttribute('data-theme',t);
    try{localStorage.setItem('vt-theme',t)}catch(e){}
    var m=document.querySelector('meta[name=theme-color]');if(m)m.content=t==='dark'?'#0b1020':'#6366f1';
    document.querySelectorAll('.theme-btn:not(.menu-btn)').forEach(function(b){
      b.innerHTML=t==='dark'?ICON_SUN:ICON_MOON;
      b.setAttribute('aria-label','Switch to '+(t==='dark'?'light':'dark')+' mode');
    });
  }

  /* Header: tools dropdown, mobile menu, theme toggle */
  var dd=document.getElementById('ddTools');
  if(dd){
    var b=dd.querySelector('button');
    b.addEventListener('click',function(e){e.stopPropagation();var o=dd.classList.toggle('open');b.setAttribute('aria-expanded',o)});
    document.addEventListener('click',function(e){if(!dd.contains(e.target)){dd.classList.remove('open');b.setAttribute('aria-expanded','false')}});
  }
  var mb=document.querySelector('.menu-btn'),mm=document.getElementById('mm');
  if(mb&&mm)mb.addEventListener('click',function(){var o=mm.classList.toggle('open');mb.setAttribute('aria-expanded',o)});
  var tb=document.querySelector('.theme-btn:not(.menu-btn)');
  if(tb)tb.addEventListener('click',function(){applyTheme(currentTheme()==='dark'?'light':'dark')});
  applyTheme(currentTheme());

  /* Home page search: filters the static tool cards */
  var si=document.getElementById('search');
  if(si){
    var cards=[].slice.call(document.querySelectorAll('#catalog .card'));
    var secs=[].slice.call(document.querySelectorAll('#catalog .cat'));
    var cnt=document.getElementById('toolCount'),none=document.getElementById('noMatch');
    si.addEventListener('input',function(){
      var q=this.value.trim().toLowerCase(),n=0;
      cards.forEach(function(c){var ok=!q||c.getAttribute('data-q').indexOf(q)>-1;c.hidden=!ok;if(ok)n++});
      secs.forEach(function(s){s.hidden=!s.querySelector('.card:not([hidden])')});
      if(cnt)cnt.textContent=n+(n===1?' tool':' tools');
      if(none)none.hidden=n>0;
    });
  }

  /* Cookie choice and analytics/ads, driven by config.json so admin changes apply without a rebuild */
  function readChoice(){try{return localStorage.getItem(KEY)}catch(e){return null}}
  function saveChoice(v){try{localStorage.setItem(KEY,v)}catch(e){}}
  function updateConsent(yes){
    if(typeof window.gtag==='function'){
      var g=yes?'granted':'denied';
      window.gtag('consent','update',{analytics_storage:g,ad_storage:g,ad_user_data:g,ad_personalization:g});
    }
  }
  function setupConsentBanner(){
    var choice=readChoice();
    if(choice){updateConsent(choice==='yes');return}
    var cc=document.getElementById('cc');
    if(!cc)return;
    cc.hidden=false;
    cc.setAttribute('role','dialog');cc.setAttribute('aria-label','Cookie choices');
    cc.innerHTML='<p>We use cookies for analytics and to show ads. You can accept or reject them. See our <a href="/privacy.html">Privacy Policy</a>.</p>'+
      '<div class="cc-btns"><button type="button" class="alt" data-c="no">Reject</button><button type="button" data-c="yes">Accept</button></div>';
    cc.addEventListener('click',function(e){
      var v=e.target.getAttribute&&e.target.getAttribute('data-c');
      if(!v)return;
      saveChoice(v);updateConsent(v==='yes');cc.hidden=true;cc.innerHTML='';
    });
  }
  function loadSiteScripts(c){
    window.dataLayer=window.dataLayer||[];
    window.gtag=window.gtag||function(){dataLayer.push(arguments)};
    window.gtag('consent','default',{ad_storage:'denied',ad_user_data:'denied',ad_personalization:'denied',analytics_storage:'denied',wait_for_update:500});
    if(c.gaId){
      var s=document.createElement('script');s.async=1;s.src='https://www.googletagmanager.com/gtag/js?id='+encodeURIComponent(c.gaId);document.head.appendChild(s);
      window.gtag('js',new Date());window.gtag('config',c.gaId);
    }
    if(c.adsenseClient){
      var a=document.createElement('script');a.async=1;a.crossOrigin='anonymous';
      a.src='https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client='+encodeURIComponent(c.adsenseClient);
      document.head.appendChild(a);
    }
    if(c.adsHeader){document.querySelectorAll('.ad').forEach(function(el){el.innerHTML=c.adsHeader})}
  }
  fetch('/config.json?'+Date.now()).then(function(r){return r.json()}).then(function(c){
    loadSiteScripts(c);setupConsentBanner();
  }).catch(function(){setupConsentBanner()});

  /* Tool pages: optional YouTube playlist lookup is handled inline on that page */
})();
