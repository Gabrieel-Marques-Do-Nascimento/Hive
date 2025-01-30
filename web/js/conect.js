import { URL } from "../js/env.js";

export var socket = io.connect(URL);
console.log("conectando...")

/*
** conecta a um cannal específico tipo a conversa de um amigo e tal
*/
export function join(room,name='sender'){
	socket.emit("join",{room:room, name:name})
}
/*
** desconecta a um cannal específico tipo a conversa de um amigo e tal
*/
export function leave(room,name='sender'){
	socket.emit("leave", {room:room, name:name})
}

export let userId = localStorage.getItem("HiveSender")