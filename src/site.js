(function(){
  var TK='vt-theme',KEY='vt-consent';
  var SUN='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg>';
  var MOON='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8z"/></svg>';

  /* Theme: dark by default, light on toggle */
  function theme(){return document.documentElement.getAttribute('data-theme')==='light'?'light':'dark'}
  function setTheme(t){
    document.documentElement.setAttribute('data-theme',t);
    try{localStorage.setItem(TK,t)}catch(e){}
    var m=document.querySelector('meta[name=theme-color]');if(m)m.content=t==='light'?'#ffffff':'#000000';
    var b=document.getElementById('tb');
    if(b){b.innerHTML=t==='light'?MOON:SUN;b.setAttribute('aria-label',t==='light'?'Switch to dark mode':'Switch to light mode')}
  }
  setTheme(theme());
  var tb=document.getElementById('tb');
  if(tb)tb.addEventListener('click',function(){setTheme(theme()==='light'?'dark':'light')});

  /* Mobile menu */
  var mb=document.getElementById('mb'),mm=document.getElementById('mm');
  if(mb&&mm)mb.addEventListener('click',function(){var o=mm.classList.toggle('open');mb.setAttribute('aria-expanded',o)});

  /* Home search: filters tool cards and hides empty categories */
  var si=document.getElementById('search');
  if(si){
    var cards=[].slice.call(document.querySelectorAll('.card[data-q]'));
    var cats=[].slice.call(document.querySelectorAll('.cat'));
    var none=document.getElementById('noMatch'),cnt=document.getElementById('toolCount');
    si.addEventListener('input',function(){
      var q=si.value.trim().toLowerCase(),n=0;
      cards.forEach(function(c){var ok=!q||c.getAttribute('data-q').indexOf(q)>-1;c.hidden=!ok;if(ok)n++});
      cats.forEach(function(s){s.hidden=!s.querySelector('.card:not([hidden])')});
      if(cnt)cnt.textContent=n+(n===1?' tool':' tools');
      if(none)none.hidden=n>0;
    });
  }

  /* Cookie notice */
  function updateConsent(yes){
    if(typeof window.gtag==='function'){var g=yes?'granted':'denied';window.gtag('consent','update',{analytics_storage:g,ad_storage:g,ad_user_data:g,ad_personalization:g})}
  }
  function setupConsentBanner(){
    var choice=null;try{choice=localStorage.getItem(KEY)}catch(e){}
    if(choice){updateConsent(choice==='yes');return}
    var cc=document.getElementById('cc');if(!cc)return;
    cc.hidden=false;cc.setAttribute('role','dialog');cc.setAttribute('aria-label','Cookie choices');
    cc.innerHTML='<p>We use cookies for analytics and to show ads. See our <a href="/privacy.html">Privacy Policy</a>.</p><div class="cc-btns"><button type="button" class="alt" data-c="no">Reject</button><button type="button" data-c="yes">Accept</button></div>';
    cc.addEventListener('click',function(e){
      var v=e.target.getAttribute&&e.target.getAttribute('data-c');if(!v)return;
      try{localStorage.setItem(KEY,v)}catch(err){}
      updateConsent(v==='yes');cc.hidden=true;cc.innerHTML='';
    });
  }

  /* AdSense: script is loaded once in <head>. Fill up to 3 slots with auto-sized units. */
  function placeAds(client){
    if(!client)return;
    var n=0;
    document.querySelectorAll('.ad').forEach(function(el){
      if(n>=3||el.getAttribute('data-filled'))return;
      n++;el.setAttribute('data-filled','1');
      var ins=document.createElement('ins');
      ins.className='adsbygoogle';ins.style.display='block';
      ins.setAttribute('data-ad-client',client);ins.setAttribute('data-ad-format','auto');ins.setAttribute('data-full-width-responsive','true');
      el.appendChild(ins);
      try{(window.adsbygoogle=window.adsbygoogle||[]).push({})}catch(e){}
    });
  }
  setupConsentBanner();
  var adMeta=document.querySelector('meta[name="google-adsense-account"]');
  if(adMeta)placeAds(adMeta.content);
})();
