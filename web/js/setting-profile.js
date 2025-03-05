import { $profile_elemt } from "./profile.js";

const my_name = document.getElementById("my-name");
my_name.value = String(localStorage.getItem("hiveusername"));
const my_username = document.getElementById("my-username");
my_username.value = String(localStorage.getItem("hiveusername"));
const my_bio = document.getElementById("my-bio");
my_bio.value = localStorage.getItem("hivebio")? String(localStorage.getItem("hivebio")): "";
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
