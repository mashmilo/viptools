import {cfg} from '../lib/layout.js';
export async function onRequestGet({env}){return new Response((await cfg(env)).adsTxt||'',{headers:{'content-type':'text/plain'}})}
