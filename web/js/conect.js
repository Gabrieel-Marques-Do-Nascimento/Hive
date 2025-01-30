export var socket = io.connect();
console.log("conectando...")

/*
** conecta a um cannal específico tipo a conversa de um amigo e tal
*/
export function join(room){
	socket.emit("join",{room:room })
}
/*
** desconecta a um cannal específico tipo a conversa de um amigo e tal
*/
export function leave(room){
	socket.emit("leave", {room: room})
}

export let userId = localStorage.getItem("HiveSender")