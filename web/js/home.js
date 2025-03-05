import {
  request_messages,
  userId,
  newUser,
  contact_exist,
  save_msg,
  contact_listTag,
  messageTag
} from "./utils.js";
import { class_background, $background, class_visible } from "./setting-profile.js";
import { socket } from "./conect.js";
const label_name = document.getElementById("label-name");
const new_contact = document.getElementById("new-contact");
const lista = document.createElement("ul");
const item = document.createElement("li");
const user_info = document.createElement("div");

const avatar = document.createElement("div");

const username = document.createElement("span");

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

function label_name_status(
  text = "hello world",
  color = "red",
  timeout = 2000,
  exit = true
) {
  label_name.textContent = text;
  label_name.style.color = color;
  setTimeout(() => {
    label_name.textContent = "Nome ou id:";
    label_name.style.color = "black";
  }, timeout);
  if (exit) {
    setTimeout(() => {
      new_contact.style.display = "none";
    }, 2100);
  }
}

let contacts = JSON.parse(localStorage.getItem(contact_listTag));

function create_user_label(users, contacts) {
  console.log(users);

users.forEach((message)=> {
  let vr = false
  if (!contacts){ 
    contacts = []
   }
    contacts.forEach((contact) => {
      if (message.other_Id == contact.contact){
        vr = true
      }
    })

  if (!vr){
    console.log(contacts)
    contacts.push({"contact":message.other_Id ,"name":`contact id: ${message.other_Id }`})
    
  }
  
})
localStorage.setItem(contact_listTag, JSON.stringify(contacts))


  lista.innerHTML = "";
  contacts.forEach(contact => {
    console.log(contact);
    const clone = newUser(contact);
   
    clone ? lista.appendChild(clone) : null;
  });




}

socket.on("connect", () => {
  console.log("conectado com id:", userId);
  socket.emit("registrar_usuario", { id: userId });
});

let token = localStorage.getItem("1463token-as-savekjg");
if (token) {
  request_messages(create_user_label);

  let users = localStorage.getItem(messageTag);
  let contacts =  JSON.parse(localStorage.getItem(contact_listTag));
  users = JSON.parse(users);
  console.log(users);
  console.log(contacts);

  if (users) {
    create_user_label(users,contacts);
  }
  document.querySelector(".container").appendChild(lista);
} else {
  window.location.href = "templates/login.html";
}


function new_contact_status(){
  if (new_contact.style.display == "none") {
    new_contact.style.display = "block";
    new_contact.classList.add(class_visible)
    $background.classList.add(class_background)
    return;
  }
  $background.classList.remove(class_background)
  new_contact.classList.remove(class_visible)
  new_contact.style.display = "none";
}


const add = document.getElementById("add");
add.addEventListener("click", () => {
  new_contact_status();
  new_contact.addEventListener("submit", (e) => {
    e.preventDefault();

    const user = document.getElementById("username");
    const $customname = document.getElementById("customname");
    let contacts = JSON.parse(localStorage.getItem(contact_listTag));
    let includes = false;
    contacts.forEach((contact) => {
      includes = contact.contact == parseInt(user.value);
    });
    if (includes) {
      label_name_status("usuario ja adicionado", "red", 2000, false);

      //alert("usuario ja adicionado");

      return;
    }
    socket.emit("new-contact", {
      id: parseInt(user.value),
      userId: userId,
      custom_name: $customname.value,
    });
    user.value = "";
  });
});
document.getElementById("exit").addEventListener("click", () => {
 new_contact_status();
});
socket.on("new-contact", function (data) {
  console.log(data);
  if (data["contact"] && parseInt(data["contact"]) != userId) {
    // Definindo uma chave para o armazenamento, por exemplo o ID da pessoa
    const pessoa = data["pessoa"];
    const chave = `contato_${pessoa}`;

    let contact_list = JSON.parse(localStorage.getItem(contact_listTag));
    contact_list.push(data);
    localStorage.setItem(contact_listTag, JSON.stringify(contact_list));
    create_user_label([], contact_list);
    label_name_status("SUcesso!!", "green");
    return;
  }
  label_name_status("usuario invalido", "red", 2000, false);
});
socket.on("error", (data) => {
  console.log(data);
  label_name_status("usuario invalido: " + data.message, "red", 2000, false);
});

// socket.on(`channel`, function (data) {
//   console.log(data);
//   let messages = JSON.parse(localStorage.getItem("messages"));
//   messages.push(data);
//   localStorage.setItem("messages", JSON.stringify(messages));
//   create_user_label(messages);
// });

socket.on("message_privada", function (data) {
  contact_exist(data.message, data.id);
  let new_message = {
    message: data.message,
    to: data.to,
    other_Id: data.id,
    id: userId
  };
  save_msg(new_message);
  console.log(new_message);
});
