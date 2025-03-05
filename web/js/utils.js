import { URL } from "./env.js";


export const myTag = "hiveid";
export const senderTag = "HiveSender";
export const messageTag = "messages";
export const contact_listTag = "contact-list";

export let token = localStorage.getItem("1463token-as-savekjg");
export let userId = parseInt(localStorage.getItem(myTag));
export let fromId = parseInt(localStorage.getItem(senderTag));
console.log("from", fromId, "userid", userId);
export let messages = JSON.parse(localStorage.getItem(messageTag));

export function request_messages(create_user_label = null) {
  if (!localStorage.getItem(messageTag)) {
    fetch(`${URL}/my_msgs`, {
      method: "POST",
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json",
        Authorization: `Bearer ${token}`,
        uid: parseInt(userId)
      },
      body: JSON.stringify({ id: parseInt(userId) })
    })
      .then(resp => {
        if (!resp.ok) {
          throw new Error(`HTTP error! Status: ${resp.status}`);
        }
        return resp.json(); // Retorna a Promise contendo os dados
      })
      .then(data => {
        console.log("reseived: ", data);
        localStorage.setItem(messageTag, JSON.stringify(data[0]));
        localStorage.setItem(contact_listTag, JSON.stringify(data[1]));

        if (create_user_label) {
          create_user_label(data[0], data[1]);
        }
      })
      .catch(error => {
        console.error("Erro ao realizar a requisição:", error);
      });
  }
}

export function room(user_id, from_id) {
  if (parseInt(user_id) <= parseInt(from_id)) {
    console.log(`channel:${user_id}${from_id}`);
    return `${user_id}${from_id}`;
  } else {
    console.log(`channe:${from_id} ${user_id}`);
    return `${from_id}${user_id}`;
  }
}




// =============================================================

export function contact_setting_profile(contact) {
  document.getElementById("id-profile").innerHTML = contact.contact;
  document.getElementById("nome-profile").innerHTML = contact.name;
  document.getElementById("username-profile").innerHTML = contact.name;
  //document.getElementById('created').innerHTML = contact.created;
  document.getElementById("bio").innerHTML = !contact.bio? contact.bio : "Não informado";
  }

export function newUser(user) {
  let pessoaN = parseInt(user["other_Id"])
    ? parseInt(user["contact_Id"])
    : parseInt(user["contact"]);
  let hiveUserid = user["name"] ? user["name"] : "Hive user";
  let avatarUrl = "Hive";
  let previewT = "preview";
  let hors = "08:00";
  const lista = document.createElement("ul");
  const item = document.createElement("li");
  const user_info = document.createElement("div");

  const avatar = document.createElement("div");
  const image = document.createElement("img");
  image.classList.add("avatar");
  image.src = "./images/profile-min.png";
avatar.appendChild(image)
  const username = document.createElement("span");
  // username.setAttribute("translate", "yes");
  const br = document.createElement("br");
  const preview = document.createElement("span");

  const time = document.createElement("div");
  const noview = document.createElement("div");
  noview.classList.add("noview");
  const div = document.createElement("div");
  user_info.classList.add("user-info");
  avatar.classList.add("avatar");
  username.classList.add("username");

  preview.classList.add("message-preview");
  time.classList.add("time");

  div.appendChild(username);
  div.appendChild(br);
  div.appendChild(preview);
  user_info.appendChild(avatar);
  user_info.appendChild(div);
  item.appendChild(user_info);
  //item.appendChild(noview)
  item.appendChild(time);
  item.appendChild(noview);
  let clone = item.cloneNode(true);

  clone.addEventListener("click", () => {
   
    contact_setting_profile(user)

    let messages = JSON.parse(localStorage.getItem(messageTag));
    localStorage.setItem(senderTag, String(pessoaN));
    document.getElementById("div-custom-name").textContent = hiveUserid;
    profile();

    const $messages_list = document.getElementById("msgs");
    $messages_list.innerHTML = "";
    messages.forEach(msg => {
      if (msg) {
        if (parseInt(msg.other_Id) == pessoaN && parseInt(msg.to) == userId) {
          new_msg(msg.message, "sender-msg");
        } else if (parseInt(msg.to) == pessoaN) {
          new_msg(msg.message);
        }
      }
    });
  });
  //clone.children[0].children[0].textContent = avatarUrl; // AVATAR
  //
  clone.children[0].children[1].children[0].textContent = hiveUserid;
  clone.children[0].children[1].children[2].textContent = previewT;

  clone.children[1].textContent = hors;
  return clone;
}

export function create_msg_element(pai, text, cloneId) {
  console.log("new msg");
  const msgs = document.createElement("p");
  const clone = msgs.cloneNode(true);
  clone.textContent = text;
  clone.id = cloneId;
  pai.appendChild(clone);
}

export function new_msg(message, type = "user-msg") {
  if (!message) {
    return;
  }
  if (message.trim()) {
    const msgs_container = document.getElementById("msgs");
    const msgs = document.createElement("p");
    const clone = msgs.cloneNode(true);
    clone.textContent = message;
    clone.id = type;
    msgs_container.appendChild(clone);
    if (type == "user-msg") {
    }
  }
}

export function save_msg(message) {
  let __messages = JSON.parse(localStorage.getItem(messageTag));
  if (!__messages.length > 0) {
    __messages = [];
  }
  __messages.push(message);
  localStorage.setItem(messageTag, JSON.stringify(__messages));
}

export function profile() {
  const $profile_elemt = document.getElementById("profile");
  const $home_elemet = document.getElementById("home");
  $profile_elemt.classList.add("active");
  $profile_elemt.style.display = "flex";
  $home_elemet.classList.add("active");
  document.body.classList.add("profile-page");

  const $usernameSpan = document.getElementById("username");
  const $sendernameSpan = document.getElementById("sendername");
}

export function contact_exist(message, id) {
  let contact_exist_in = false;
  let __messages = JSON.parse(localStorage.getItem(messageTag));
  if (!__messages.length > 0) {
    __messages = [];
  }
  __messages.push();
  localStorage.setItem(messageTag, JSON.stringify(__messages));
  let constacts = JSON.parse(localStorage.getItem(contact_listTag));
  constacts.forEach(contact => {
    if (contact.contact == id) {
      contact_exist_in = true;
      console.log(contact);
    }
  });
  if (!contact_exist_in) {
    constacts.push({ contact: id, name: `contact id: ${id}` });
    localStorage.setItem(contact_listTag, constacts);
    location.reload();
  }
}
