import { new_msg } from "./utils.js";

const $exit = document.getElementById("exitButton");
const $msg_container = document.getElementById("msgs");
const $send = document.getElementById("send");

export function profile() {
  const $profile_elemt = document.getElementById("profile");
  const $home_elemet = document.getElementById("home");
  $profile_elemt.classList.add("active");
  $profile_elemt.style.display = "block";
  $home_elemet.classList.add("active");
  document.body.classList.add("profile-page");

  const $usernameSpan = document.getElementById("username");
  const $sendernameSpan = document.getElementById("sendername");
}

$exit.addEventListener("click", () => {
  // window.location.href = "/"
  console.log("clicked");
  const $profile_elemt = document.getElementById("profile");
  const $home_elemet = document.getElementById("home");
  $profile_elemt.classList.remove("active");
  $profile_elemt.style.display = "none";
  $home_elemet.classList.remove("active");
  document.body.classList.remove("profile-page");
});

$send.addEventListener("click", () => {
  const $input_msg = document.getElementById("msg-input");
  new_msg($input_msg.value);
  $input_msg.value = null;
});
