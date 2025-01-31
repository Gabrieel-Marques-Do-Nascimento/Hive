import { URL } from "../js/env.js";
import { request_messages, userId } from "./utils.js";

const lista = document.createElement("ul");
const item = document.createElement("li");
const user_info = document.createElement("div");

const avatar = document.createElement("div");

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

let socket = io.connect("//" + document.domain + ":" + 5000);

let token = localStorage.getItem("1463token-as-savekjg");
if (token) {
  request_messages();

  let users = localStorage.getItem("messages");
  
  users= JSON.parse(users);
  console.log(users);
  let idlist = [];
  let userlist = [];

  if (users) {
    for (let i = 0; i < users.length; i++) {
      let user = users[i];
      let userid = users[i]["pessoa"];
      console.log(user["enviado"],userId);
      if (user["enviado"] != userId) {
        console.log("user.inicio", user);
        if (!idlist.includes(userid)) {
          console.log("user list: ", idlist.toString());
          idlist.push(userid);
          userlist.push(user);

          let clone = item.cloneNode(true);
          // user = users[i];
          clone.addEventListener("click", () => {
            localStorage.setItem("HiveSender", String(user["enviado"]));

            window.location.href = `templates/profile.html`;
          });
          clone.children[0].children[0].innerHTML = "Hive"; // AVATAR
          //
          clone.children[0].children[1].children[0].innerHTML = "Hive user";
          clone.children[0].children[1].children[2].innerHTML = "preview";
          console.log('user.fim',user);
          clone.children[1].innerHTML = "08:00";
          lista.appendChild(clone);
        }
        console.log("ids: ", JSON.stringify(idlist));
      }
    }
  }
  document.querySelector(".container").appendChild(lista);
} else {
  window.location.href = "templates/login.html";
}

const add = document.getElementById("add");
add.addEventListener("click", () => {
  const new_contact = document.getElementById("new-contact");
  new_contact.style.display = "block";
  new_contact.addEventListener("submit", (e) => {
    e.preventDefault();
    const user = document.getElementById("name");
  });
});
