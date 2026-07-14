
const scenarios={
 balanced:{values:[100,94,88,82,78],diagnosis:'Loss is bounded; ownership and evidence remain visible.',action:'Fund the next increment and preserve the learning record.'},
 architecture:{values:[100,90,58,52,46],diagnosis:'Integration, data, identity, or control debt is consuming expected value.',action:'Condition release; resolve architecture debt before adding delivery capacity.'},
 ownership:{values:[100,62,57,39,24],diagnosis:'The workflow has sponsorship but no durable outcome owner or decision authority.',action:'Hold funding until ownership, human authority, and baseline are explicit.'},
 adoption:{values:[100,94,86,43,28],diagnosis:'The solution shipped, but behavior, standard work, and reinforcement did not.',action:'Stop feature expansion; redesign the workflow and adoption mechanism.'}
};
const xs=[20,170,320,470,620,740];
let current=[100,94,88,82,78];
function points(vals){const all=[100,...vals];const top=all.map((v,i)=>`${xs[i]},${125-v}`);const bottom=all.slice().reverse().map((v,ri)=>{const i=all.length-1-ri;return `${xs[i]},${125+v}`});return [...top,...bottom].join(' ')}
function animateTo(target){const start=[...current],duration=500,t0=performance.now();if(matchMedia('(prefers-reduced-motion: reduce)').matches){current=[...target];draw();return}function frame(now){const p=Math.min(1,(now-t0)/duration);const e=1-Math.pow(1-p,3);current=start.map((v,i)=>v+(target[i]-v)*e);draw();if(p<1)requestAnimationFrame(frame)}requestAnimationFrame(frame)}
function draw(){const p=points(current);document.querySelector('#yield-band')?.setAttribute('points',p);document.querySelector('#yield-glow')?.setAttribute('points',p);current.forEach((v,i)=>{const el=document.querySelector(`#s${i}`);if(el)el.textContent=`${Math.round(v)}`});const num=document.querySelector('#yield-number');if(num)num.textContent=`${Math.round(current[4])}`}
const tabs=[...document.querySelectorAll('[data-scenario]')];tabs.forEach((tab,idx)=>{tab.addEventListener('click',()=>select(tab));tab.addEventListener('keydown',e=>{if(!['ArrowRight','ArrowLeft','Home','End'].includes(e.key))return;e.preventDefault();let n=idx;if(e.key==='ArrowRight')n=(idx+1)%tabs.length;if(e.key==='ArrowLeft')n=(idx-1+tabs.length)%tabs.length;if(e.key==='Home')n=0;if(e.key==='End')n=tabs.length-1;tabs[n].focus();select(tabs[n])})});
document.querySelector('#reset-baseline')?.addEventListener('click',()=>{const baseline=tabs[0];baseline.focus();select(baseline)});
function select(tab){const data=scenarios[tab.dataset.scenario];tabs.forEach(t=>t.setAttribute('aria-selected',String(t===tab)));const panel=document.querySelector('#scenario-panel');panel?.setAttribute('aria-labelledby',tab.id);document.querySelector('#diagnosis').textContent=data.diagnosis;document.querySelector('#portfolio-action').textContent=data.action;animateTo(data.values)}
draw();
