import { URL } from "./env.js";
import { new_msg } from "./script.js";
import { socket, join, leave } from "./conect.js";

function room(user_id, from_id) {
    if (parseInt(user_id) <= parseInt(from_id)) {
    	console.log("id: "+toString(user_id) + toString(from_id))
    	return toString("id: "+user_id) + toString(from_id);
    } else {
    	console.log(toString(from_id) + toString(user_id))
        return toString(from_id) + toString(user_id);
    }
}
let user = localStorage.getItem("hiveid");
    let from = localStorage.getItem("HiveSender");
join(room(user, from))
function sendMessage(message, room) {
    if (message.trim() === "") {
        return;
    }
    socket.emit("channel", { room: room, message: message, id: user, "d-id":from, });
    console.log(message)
}

const input = document.getElementById("msg-input");
const send_button = document.getElementById("send");
let token = localStorage.getItem("1463token-as-savekjg");
send_button.addEventListener("click", () => {
    new_msg(input.value);
    
    sendMessage(input.value, room(user, from));

    input.value = null;

    // fetch(`${URL}/send_msg`, {
    //     method: "POST",
    //     headers: {
    //         accept: "application/json",
    //         "Content-Type": "application/json",
    //         Authorization: `Bearer ${token}`,
    //         uid: 1
    //     },
    //     body: {
    //         id: 1,
    //         msg: input.value,
    //         "p-id": 2
    //     }
    // })
    //     .then(resp => {
    //         if (!resp.ok) {
    //             throw new Error(`HTTP ERRO! Status: ${resp.status}`);
    //         }
    //         return resp.json();
    //     })
    //     .then(data => {})
    //     .catch(error => {
    //         console.error(`erro a realizar a requisição: ${error}`);
    //     });
});
