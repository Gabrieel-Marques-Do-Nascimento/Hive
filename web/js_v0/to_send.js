import { URL } from "../js/env.js";
import { new_msg } from "./script.js";
import { leave } from "../js/conect.js";
import {
  userId,
  room,
  fromId,
  messages,
  create_msg_element,
} from "../js/utils.js";
const msgs_container = document.getElementById("msgs");
const socket = io.connect(URL);
export function join(room, name = "sender") {
  socket.emit("join", { room: room, name: name });
}
join(room(userId, fromId));
function sendMessage(message, room) {
  if (message.trim() === "") {
    return;
  }
  socket.emit("channel", {
    room: room,
    message: message,
    id: userId,
    "d-id": fromId,
  });
  console.log(message);
}

const input = document.getElementById("msg-input");
const send_button = document.getElementById("send");
let token = localStorage.getItem("1463token-as-savekjg");
send_button.addEventListener("click", () => {
  new_msg(input.value);

  sendMessage(input.value, room(userId, fromId));
  let new_msg_dict = {
    enviado: userId,
    message: input.value,
    pessoa: fromId,
    online: null,
    userid: userId,
  };
  messages.push(new_msg_dict);
  localStorage.setItem("messages", JSON.stringify(messages));
  console.log(new_msg_dict);
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
socket.on("channel", function (data) {
  console.log(data);
  if (data.id != userId) {
    create_msg_element(msgs_container, data["message"], "sender-msg");
    messages.push(data);
    localStorage.setItem("messages", JSON.stringify(messages));
  }
});
socket.on("join", function (data) {
  console.log(data);
});
