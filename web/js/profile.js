import { new_msg } from "./utils.js";
import { socket } from "./conect.js";

const $exit = document.getElementById("exitButton");
const $msg_container = document.getElementById("msgs");
const $send = document.getElementById("send");
const $input_msg = document.getElementById("msg-input");  
const $profile_elemt = document.getElementById("profile");

document.getElementById('serch').addEventListener('click', ()=> {
  document.getElementById('serch-container').style.display = 'block'
})
$exit.addEventListener("click", () => {
  // window.location.href = "/"
  console.log("clicked");

  const $home_elemet = document.getElementById("home");
  $profile_elemt.classList.remove("active");
  $profile_elemt.style.display = "none";
  $home_elemet.classList.remove("active");
  document.body.classList.remove("profile-page");
});

$send.addEventListener("click", () => {
  
  new_msg($input_msg.value);
 
  socket.emit('send_message',{destinatario_id: localStorage.getItem('HiveSender'), mensagem: $input_msg.value})
  $input_msg.value = null;
});

socket.on('message_privada', function(data) {
    console.log(data)
    new_msg(data.mensagem, "sender-msg");
})

// $input_msg.addEventListener('focus', () => {
//   x = window.matchMedia("(max-width: 768px)");
//   if (x.matches) {
//     $profile_elemt.style.height = "60vh";
//     document.body.style.height = "60vh";
//     document.head.style.height = "60vh";
//   }

// })