const root=document.documentElement;
function applyLanguage(lang){
 root.lang=lang;
 document.querySelectorAll('[data-href-en]').forEach(el=>el.href=el.dataset[lang==='ru'?'hrefRu':'hrefEn']);
 try{localStorage.setItem('portfolio-language',lang)}catch{}
 document.querySelectorAll('[data-label-en]').forEach(el=>el.setAttribute('aria-label',el.dataset[lang==='ru'?'labelRu':'labelEn']));
 document.querySelectorAll('[data-alt-en]').forEach(el=>el.alt=el.dataset[lang==='ru'?'altRu':'altEn']);
 const title=document.querySelector('title');document.title=title.dataset[lang==='ru'?'titleRu':'titleEn'];
 const description=document.querySelector('meta[name="description"]');description.content=description.dataset[lang==='ru'?'contentRu':'contentEn'];
 document.querySelectorAll('[data-nav]').forEach(a=>{const url=new URL(a.href);url.searchParams.set('lang',lang);a.href=url.href});
}
applyLanguage(root.lang);
document.querySelector('.language-toggle').addEventListener('click',()=>{
 const lang=root.lang==='ru'?'en':'ru';applyLanguage(lang);
 const url=new URL(location.href);url.searchParams.set('lang',lang);history.replaceState(null,'',url);
});
const motion=matchMedia('(prefers-reduced-motion: reduce)');
const videos=[...document.querySelectorAll('video[data-src]')];
const visible=new Set();
function updateVideo(video){
 if(motion.matches||!visible.has(video)||document.hidden){video.pause();return}
 if(!video.getAttribute('src'))video.src=video.dataset.src;
 video.muted=true;video.play().catch(()=>{});
}
if('IntersectionObserver' in window){
 const observer=new IntersectionObserver(entries=>entries.forEach(e=>{e.isIntersecting?visible.add(e.target):visible.delete(e.target);updateVideo(e.target)}),{threshold:0.05});
 videos.forEach(v=>observer.observe(v));
}
motion.addEventListener('change',()=>videos.forEach(updateVideo));
document.addEventListener('visibilitychange',()=>videos.forEach(updateVideo));
