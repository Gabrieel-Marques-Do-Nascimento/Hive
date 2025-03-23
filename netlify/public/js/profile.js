import { fromId, new_msg, save_msg, userId } from "./utils.js";
import { socket } from "./conect.js";
console.log(typeof JSON.parse(localStorage.getItem("messages")));
const $exit = document.getElementById("exitButton");
const $msg_container = document.getElementById("msgs");
const $send = document.getElementById("send");
const $input_msg = document.getElementById("msg-input");
export const $profile_elemt = document.getElementById("profile");


document.getElementById("serch").addEventListener("click", () => {
  document.getElementById("serch-container").classList.toggle("active");
  
  });
$exit.addEventListener("click", () => {
  // window.location.href = "/"
  console.log("clicked");

  const $home_elemet = document.getElementById("home");
  $profile_elemt.classList.remove("active");
  $profile_elemt.style.display = "none";
  $home_elemet.classList.remove("active");
  document.body.classList.remove("profile-page");

// remove o perfil do usuario se estiver aberto referente ao modulo setting-profile.js
if (!document.getElementById("setting-profile").classList.contains('invisible')){
  document.getElementById("setting-profile").classList.add('invisible')
}
});

$send.addEventListener("click", event => {
  event.preventDefault();

  //   save_msg(  {
  //     "message": $input_msg.value,
  //     id: 1,
  //     "other_Id": 2,
  //     "to": null,
  //     "online": null,
  // });
  //save_msg({message});
  new_msg($input_msg.value);
  const destinatario = parseInt(localStorage.getItem("HiveSender"));
  const id = parseInt(localStorage.getItem("hiveid"));
  save_msg({ message: $input_msg.value, id: id, to: destinatario, other_Id: destinatario });
  socket.emit("send_message", {
    to: destinatario,
    message: $input_msg.value,
    id:id
  });
  $input_msg.value = null;
  $input_msg.focus();
});

socket.on("message_privada", function (data) {
  console.log(data);
  if (parseInt(data.to )== parseInt(userId) && parseInt(data.id )== parseInt(localStorage.getItem("HiveSender"))) {
    console.log(data);
    new_msg(data.message,data.created,  "sender-msg");
  }
  //save_msg(data.mensagem);
});
socket.on('contact-status', (data) => {
  console.log(data)
  const $status = document.getElementById('status')
  if (data.status == 'online') {
    $status.style.color = 'green'
    $status.innerHTML = 'online'
  } else {
    $status.style.color = 'red'
    $status.innerHTML = 'offline'
  }
})
// $input_msg.addEventListener('focus', () => {
//   x = window.matchMedia("(max-width: 768px)");
//   if (x.matches) {
//     $profile_elemt.style.height = "60vh";
//     document.body.style.height = "60vh";
//     document.head.style.height = "60vh";
//   }

// })
