import { new_msg, save_msg } from "./utils.js";
import { socket } from "./conect.js";
console.log(typeof JSON.parse(localStorage.getItem("messages")));
const $exit = document.getElementById("exitButton");
const $msg_container = document.getElementById("msgs");
const $send = document.getElementById("send");
const $input_msg = document.getElementById("msg-input");
const $profile_elemt = document.getElementById("profile");

document.getElementById("serch").addEventListener("click", () => {
  const $input_serch = document.getElementById("serch-container");
  if ($input_serch.style.display == "none") {
    $input_serch.style.display = "block";
    return;
  }
  $input_serch.style.display = "none";
});
$exit.addEventListener("click", () => {
  // window.location.href = "/"
  console.log("clicked");

  const $home_elemet = document.getElementById("home");
  $profile_elemt.classList.remove("active");
  $profile_elemt.style.display = "none";
  $home_elemet.classList.remove("active");
  document.body.classList.remove("profile-page");
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
  const destinatario = localStorage.getItem("HiveSender");
  const id = localStorage.getItem("hiveid");
  save_msg({ message: $input_msg.value, id: id, to: destinatario });
  socket.emit("send_message", {
    to: destinatario,
    message: $input_msg.value,
    id: id
  });
  $input_msg.value = null;
  $input_msg.focus();
});

socket.on("message_privada", function (data) {
  console.log(data);
  new_msg(data.message, "sender-msg");
  //save_msg(data.mensagem);
});

// $input_msg.addEventListener('focus', () => {
//   x = window.matchMedia("(max-width: 768px)");
//   if (x.matches) {
//     $profile_elemt.style.height = "60vh";
//     document.body.style.height = "60vh";
//     document.head.style.height = "60vh";
//   }

// })
