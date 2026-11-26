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
  /* AdSense: the script is already in <head> (build.py). Fill up to 3 ad slots with auto-sized units.
     Ads are never placed in the header, inside tool inputs, or in more than 3 spots per page. */
  function placeAds(client){
    if(!client||!window.adsbygoogle&&!document.querySelector('script[src*="adsbygoogle.js"]'))return;
    var n=0;
    document.querySelectorAll('.ad').forEach(function(el){
      if(n>=3||el.getAttribute('data-filled'))return;
      n++;el.setAttribute('data-filled','1');
      var ins=document.createElement('ins');
      ins.className='adsbygoogle';ins.style.display='block';
      ins.setAttribute('data-ad-client',client);
      ins.setAttribute('data-ad-format','auto');
      ins.setAttribute('data-full-width-responsive','true');
      el.appendChild(ins);
      try{(window.adsbygoogle=window.adsbygoogle||[]).push({})}catch(e){}
    });
  }
  var adMeta=document.querySelector('meta[name="google-adsense-account"]');
  setupConsentBanner();
  if(adMeta)placeAds(adMeta.content);

  /* Tool pages: optional YouTube playlist lookup is handled inline on that page */
})();
