const open =document.getElementById('open');
const modal_containerx=document.getElementById('modal-containerx');
const close=document.getElementById('close');
const start=document.getElementById('start');

open.addEventListener('click',()=>{
    modal_containerx.classList.add('show');
})
close.addEventListener('click',()=>{
    modal_containerx.classList.remove('show');
})
