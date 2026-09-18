(function(){
  "use strict";
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---- header sticky ---- */
  var hdr = document.getElementById('hdr'), ticking = false;
  function onScroll(){
    if(ticking) return; ticking = true;
    requestAnimationFrame(function(){
      hdr.classList.toggle('stuck', window.scrollY > 24);
      ticking = false;
    });
  }
  if(hdr){ window.addEventListener('scroll', onScroll, {passive:true}); onScroll(); }

  /* ---- menú mobile ---- */
  var burger = document.getElementById('burger'),
      mnav = document.getElementById('mnav'),
      bIcon = document.getElementById('burger-i');
  function setMenu(open){
    mnav.classList.toggle('open', open);
    burger.setAttribute('aria-expanded', open ? 'true' : 'false');
    burger.setAttribute('aria-label', open ? 'Cerrar menú' : 'Abrir menú');
    bIcon.innerHTML = '<use href="#' + (open ? 'i-close' : 'i-menu') + '"/>';
  }
  if(burger && mnav){
    burger.addEventListener('click', function(){ setMenu(!mnav.classList.contains('open')); });
    mnav.addEventListener('click', function(e){ if(e.target.closest('a')) setMenu(false); });
    document.addEventListener('keydown', function(e){ if(e.key === 'Escape') setMenu(false); });
  }

  /* ---- scroll reveal ---- */
  var items = document.querySelectorAll('[data-reveal]');
  if(reduce || !('IntersectionObserver' in window)){
    items.forEach(function(el){ el.classList.add('in'); });
  } else {
    var io = new IntersectionObserver(function(entries){
      entries.forEach(function(en){
        if(en.isIntersecting){ en.target.classList.add('in'); io.unobserve(en.target); }
      });
    }, {rootMargin:'0px 0px -8% 0px', threshold:.12});
    items.forEach(function(el){ io.observe(el); });
  }

  /* ---- parallax 3D suave con el mouse ---- */
  if(!reduce && window.matchMedia('(pointer:fine)').matches){
    document.querySelectorAll('.scene').forEach(function(scene){
      var inner = scene.querySelector('.scene-in');
      if(!inner) return;
      scene.addEventListener('mousemove', function(e){
        var r = scene.getBoundingClientRect(),
            x = (e.clientX - r.left) / r.width - .5,
            y = (e.clientY - r.top) / r.height - .5;
        inner.style.transition = 'transform .18s linear';
        inner.style.transform = 'rotateY(' + (x * 11).toFixed(2) + 'deg) rotateX(' + (-y * 9).toFixed(2) + 'deg)';
      });
      scene.addEventListener('mouseleave', function(){
        inner.style.transition = 'transform .9s cubic-bezier(.22,1,.36,1)';
        inner.style.transform = '';
      });
    });
  }

  /* ---- mapas diferidos: se cargan al acercarse (no penalizan el LCP) ---- */
  function loadMap(card){
    if(card.dataset.loaded) return;
    card.dataset.loaded = '1';
    var f = document.createElement('iframe');
    f.src = 'https://maps.google.com/maps?q=' + encodeURIComponent(card.dataset.map) + '&z=16&output=embed';
    f.title = card.dataset.mapTitle || 'Mapa de ubicación';
    f.loading = 'lazy';
    f.referrerPolicy = 'no-referrer-when-downgrade';
    f.allowFullscreen = true;
    card.appendChild(f);
  }
  var maps = document.querySelectorAll('[data-map]');
  if(maps.length){
    if('IntersectionObserver' in window){
      var mio = new IntersectionObserver(function(entries){
        entries.forEach(function(en){
          if(en.isIntersecting){ loadMap(en.target); mio.unobserve(en.target); }
        });
      }, {rootMargin:'320px'});
      maps.forEach(function(m){ mio.observe(m); });
    } else {
      maps.forEach(loadMap);
    }
  }

  /* ---- link activo en el menú ---- */
  var secs = ['inicio','servicios','preparacion','domicilio','sedes','equipo','preguntas']
    .map(function(id){ return document.getElementById(id); }).filter(Boolean);
  if('IntersectionObserver' in window && secs.length){
    var links = document.querySelectorAll('.nav a');
    var sio = new IntersectionObserver(function(entries){
      entries.forEach(function(en){
        if(!en.isIntersecting) return;
        links.forEach(function(a){
          var on = a.getAttribute('href').split('#')[1] === en.target.id;
          a.style.color = on ? 'var(--cy-800)' : '';
          a.style.background = on ? 'var(--cy-50)' : '';
        });
      });
    }, {rootMargin:'-45% 0px -50% 0px'});
    secs.forEach(function(s){ sio.observe(s); });
  }
})();
