'use strict';
const $=s=>document.querySelector(s);
const search=$('#search'),list=$('[data-filter-list]');
if(search&&list){
 const query=new URLSearchParams(location.search).get('q')||'';search.value=query;
 const filter=()=>{const q=search.value.toLocaleLowerCase().trim(),domain=$('#domain')?.value||'',kind=$('#kind')?.value||'';let n=0;for(const row of list.children){const text=(row.dataset.search||row.textContent).toLocaleLowerCase();row.hidden=!(text.includes(q)&&(!domain||row.dataset.domain===domain)&&(!kind||row.dataset.kind===kind));if(!row.hidden)n++;}$('#result-count').textContent=`${n} ${location.pathname.startsWith('/papers')?'manuscripts':'records'} shown`;$('#empty').hidden=n!==0;};
 search.addEventListener('input',filter);$('#domain')?.addEventListener('change',filter);$('#kind')?.addEventListener('change',filter);filter();
}
if(location.hash){const target=document.getElementById(decodeURIComponent(location.hash.slice(1)));if(target?.tagName==='DETAILS'){target.open=true;if(target.hidden&&search){search.value='';$('#domain')&&($('#domain').value='');$('#kind')&&($('#kind').value='');search.dispatchEvent(new Event('input'));}target.scrollIntoView();}}
const effect=$('#effect');if(effect){const update=()=>{const x=Number(effect.value),b=2*x-x*x,l=2*x/(1+x);$('#effect-label').value=x.toFixed(3);$('#bliss').textContent=b.toFixed(3);$('#loewe').textContent=l.toFixed(3);$('#gap').textContent=(b-l).toFixed(3);$('#bliss-bar').setAttribute('width',String(360*b));$('#loewe-bar').setAttribute('width',String(360*l));};effect.addEventListener('input',update);update();}
const pool=$('#pool');if(pool){const update=()=>{const t=Number(pool.value),f=Number($('#fraction').value),n=Number($('#nadph').value);$('#pool-label').value=t.toFixed(2);$('#fraction-label').value=f.toFixed(2);$('#nadph-label').value=n.toFixed(2);$('#gsh').textContent=(t*f).toFixed(2);$('#budget').textContent=(t*f/2+n).toFixed(2);};for(const id of ['pool','fraction','nadph'])$('#'+id).addEventListener('input',update);update();}
