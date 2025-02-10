import { request_messages, userId, newUser } from "./utils.js";
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

let contacts = JSON.parse(localStorage.getItem("contact`s"));

function create_user_label(users, contacts) {
  console.log(users);
  let idlist = [];
  let userlist = [];
  lista.innerHTML = "";
  if (users.length > 0) {
    users[0].forEach((user) => {
      if (!idlist.includes(parseInt(user["pessoa"]))) {
        idlist.push(parseInt(user["pessoa"]));
        if (parseInt(user["pessoa"]) != userId) {
          const clone = newUser(user);
          clone ? lista.appendChild(clone) : null;
        }
      }
    });
    users.forEach((user) => {
      if (
        !idlist.includes(parseInt(user["enviado"])) &&
        user["enviado"] != null
      ) {
        idlist.push(parseInt(user["enviado"]));
        if (parseInt(user["enviado"]) != userId) {
          const clone = newUser(user);
          clone ? lista.appendChild(clone) : null;
        }
      }
    });
  }
  contacts.forEach((contact) => {
    const clone = newUser(contact);
    clone ? lista.appendChild(clone) : null;
  });
  localStorage.setItem("contact`s", JSON.stringify(idlist));
  console.log(idlist.toString());
}

socket.on("connect", () => {
  console.log("conectado com id:", userId);
  socket.emit("registrar_usuario", { id: userId });
});

let token = localStorage.getItem("1463token-as-savekjg");
if (token) {
  request_messages(create_user_label);

  let users = localStorage.getItem("messages");
let contacts = localStorage.getItem("contact-list");
  users = JSON.parse(users);
  console.log(users);

  if (users) {
    create_user_label(users, JSON.parse(contacts));
  }
  document.querySelector(".container").appendChild(lista);
} else {
  window.location.href = "templates/login.html";
}

const add = document.getElementById("add");
add.addEventListener("click", () => {
  new_contact.style.display = "block";
  new_contact.addEventListener("submit", (e) => {
    e.preventDefault();

    const user = document.getElementById("username");
    const $cunstoname = document.getElementById("cunstoname");
    let contacts = JSON.parse(localStorage.getItem("contact`s"));
    if (contacts.includes(parseInt(user.value))) {
      label_name_status("usuario ja adicionado", "red", 2000, false);

      //alert("usuario ja adicionado");

      return;
    }
    socket.emit("new-contact", {
      id: parseInt(user.value),
      userId: userId,
      custom_name: $cunstoname.value,
    });
    user.value = "";
  });
});
document.getElementById("exit").addEventListener("click", () => {
  new_contact.style.display = "none";
});
socket.on("new-contact", function (data) {
  console.log(data);
  if (data["pessoa"] && parseInt(data["pessoa"]) != userId) {
    // Definindo uma chave para o armazenamento, por exemplo o ID da pessoa
    const pessoa = data["pessoa"];
    const chave = `contato_${pessoa}`;

    let contact_list = JSON.parse(localStorage.getItem("contact-list"));
    contact_list .push(data);
    localStorage.setItem("contact-list", JSON.stringify(contact_list ));
    create_user_label( [],contact_list );
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
  console.log(data);
});
