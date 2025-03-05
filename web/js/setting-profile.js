import { $profile_elemt } from "./profile.js";





function show_setting_profile() {
  const $setting_profile = document.getElementById("my-setting-profile");
  if ($setting_profile.classList.contains('invisible')){
    $setting_profile.classList.remove('invisible')
    return;
  }
  $setting_profile.classList.add('invisible')
}

const $photo = document.getElementById("profile-button");
$photo.addEventListener("click", () => {
    show_setting_profile();
  });
document.querySelector('.exit-button-msp').addEventListener('click', () => {
  show_setting_profile();
});

 









const $contact_photo = document.getElementById("photo");



function show_setting_profile_contact() {
const $setting_profile_contact = document.getElementById("setting-profile");
console.log($setting_profile_contact.classList);

  if ($setting_profile_contact.classList.contains('invisible')){
    $setting_profile_contact.classList.remove('invisible')
    return;
  }
  $setting_profile_contact.classList.add('invisible')
}





$contact_photo.addEventListener("click", () => {
  show_setting_profile_contact();
});
document.getElementById('exit-button').addEventListener('click', () => {
  show_setting_profile_contact();
});