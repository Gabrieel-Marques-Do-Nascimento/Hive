import { $profile_elemt } from "./profile.js";
import { socket } from "./conect.js";
import { myTag } from "./utils.js";



// =============== new structore =============================
import { theme, darkTheme, ligthTheme,user } from "./hivy.js";

// ================= theme =========================
theme.start();
const $theme = document.getElementById("theme-button");
$theme.addEventListener("click", () => {
  const dark_mode = darkTheme.value;
  if (document.body.classList.contains(dark_mode)) {
    document.body.classList.remove(dark_mode);
    document.body.classList.add(ligthTheme.value);
    theme.theme=ligthTheme;
    console.log(ligthTheme)
    return;
  }
  document.body.classList.add(dark_mode);
  document.body.classList.remove(ligthTheme.value);
  theme.theme=darkTheme;
  console.log(darkTheme);
});










// =============== fault structore =============================














const my_name = document.getElementById("my-name");
my_name.placeholder = user.name;
const my_username = document.getElementById("my-username");
my_username.placeholder = user.name;
const my_bio = document.getElementById("text-my-bio");
my_bio.placeholder = user.bio
  ? user.bio
  : "";

document.querySelector(".profile-form").addEventListener("submit", (event) => {
  event.preventDefault();
  console.log("profile atualizado ");
  // fetch();
});
// ============================================
export const $background = document.getElementById("background");
export let class_background = "background-visible";
$background.classList.add("background-invisible");
export let class_visible = "visible";

export function elemen_destaque(destaque_elemente, visible = true) {
  let class_background = "background-visible";
  $background.classList.add("background-invisible");
  let class_visible = "visible";
  if (visible) {
    $background.classList.add(class_background);
    destaque_elemente.classList.add(class_visible);
  } else {
    $background.classList.remove(class_background);
    destaque_elemente.classList.remove(class_visible);
  }
}

function show_setting_profile() {
  const $setting_profile = document.getElementById("my-setting-profile");
  if ($setting_profile.classList.contains("invisible")) {
    $setting_profile.classList.remove("invisible");
    elemen_destaque($setting_profile);
    return;
  }
  $setting_profile.classList.add("invisible");
  elemen_destaque($setting_profile, false);
}

const $photo = document.getElementById("profile-button");
$photo.addEventListener("click", () => {
  show_setting_profile();
});
document.querySelector(".exit-button-msp").addEventListener("click", () => {
  show_setting_profile();
});

const $contact_photo = document.getElementById("photo");

function show_setting_profile_contact() {
  const $setting_profile_contact = document.getElementById("setting-profile");

  if ($setting_profile_contact.classList.contains("invisible")) {
    $setting_profile_contact.classList.remove("invisible");
    elemen_destaque($setting_profile_contact);
    return;
  }

  $setting_profile_contact.classList.add("invisible");
  elemen_destaque($setting_profile_contact, false);
}

$contact_photo.addEventListener("click", () => {
  show_setting_profile_contact();
});
document.getElementById("exit-button").addEventListener("click", () => {
  show_setting_profile_contact();
});

const setting_form = document.querySelector(".profile-form");

setting_form.addEventListener("click", (event) => {
 
  event.preventDefault();
   const bio_element = document.getElementById("text-my-bio");
  console.log(document.getElementById("text-my-bio").value);
  if (document.getElementById("text-my-bio").value) {
    console.log("bio atualizado");
    let bio_value = bio_element.value
    socket.emit("bio", { bio: bio_value , id: localStorage.getItem(myTag) });
    user.bio=bio_value;
    
    bio_element.value = "";
    bio_element.placeholder = user.bio;
  }
});


