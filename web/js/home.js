const lista = document.createElement("ul");
const item = document.createElement("li");
const user_info = document.createElement("div");

const avatar = document.createElement("div");

const username = document.createElement("span");

const br = document.createElement("br");
const preview = document.createElement("span");

const time = document.createElement("div");

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
user_info.appendChild(div)
item.appendChild(user_info);
item.appendChild(time);
// teste user-msg
let users = [
    { username: "gabriel", time: "15:00", preview: "hello world" },
    { username: "camila", time: "15:00", preview: "hello world" },
    { username: "joao", time: "15:00", preview: "hello world" }
];

for (let i = 0; i < users.length; i++) {
    let clone = item.cloneNode(true);
    clone.children[0].children[0].innerHTML = ""; // AVATAR
    // 
    clone.children[0].children[1].children[0].innerHTML = users[i]["username"]
    clone.children[0].children[1].children[2].innerHTML = users[i]["preview"]
    clone.children[1].innerHTML = users[i]["time"]
    lista.appendChild(clone);
}
document.querySelector(".container").appendChild(lista);


