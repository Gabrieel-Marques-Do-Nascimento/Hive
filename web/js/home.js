import { URL } from "../js/env.js";

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
user_info.appendChild(div);
item.appendChild(user_info);
item.appendChild(time);

// exemplos
// let users = [

//     { username: "larissa", id: 11, time: "19:00", preview: "good night" }
// ];

// let messages = [

//     {"id": 12, "senderId": 2, "pessoaId": 2, "message": "Mensagem recebida", "created": "02/02/2025"}
// ];

// deve ser feito no login-page
// apos o login o servidor envia todas as mensagens salvas do user
// let users = [];
// let messages = [];
let token = localStorage.getItem('1463token-as-savekjg')
if (!localStorage.getItem("messages")) {

    fetch(`${URL}/my_msgs`, {
        method: "POST",
        headers: {
            Accept: "application/json",
            "Content-Type": "application/json",
            "Authorization": `Bearer ${token}`,
            'uid':1
        },
        body: JSON.stringify({ id: 1 })
    })
        .then(resp => {
            if (!resp.ok) {
                throw new Error(`HTTP error! Status: ${resp.status}`);
            }
            return resp.json(); // Retorna a Promise contendo os dados
        })
        .then(data => {
             localStorage.setItem("messages", JSON.stringify(data)); 
        })
        .catch(error => {
            console.error("Erro ao realizar a requisição:", error);
        });

    }

// if (!localStorage.getItem("users")) {
//     localStorage.setItem("users", JSON.stringify(users));
// }

// for (let i = 0; i < users.length; i++) {
//     let clone = item.cloneNode(true);
//     user = users[i]["username"];
//     clone.addEventListener("click", () => {
//         localStorage.setItem("HiveSender", String(i));

//         window.location.href = `templates/profile.html`;
//     });
//     clone.children[0].children[0].innerHTML = ""; // AVATAR
//     //
//     clone.children[0].children[1].children[0].innerHTML = user;
//     clone.children[0].children[1].children[2].innerHTML = users[i]["preview"];
//     clone.children[1].innerHTML = users[i]["time"];
//     lista.appendChild(clone);
// }

let users = localStorage.getItem("messages");
users = JSON.parse(users);
let userlist = [];
for (let i = 0; i < users.length; i++) {
    let clone = item.cloneNode(true);

    for (let j = 0; j < users.length; j++) {
        let user = users[i];
        if (user["senderId"] != 1) {
           
        }
    }

    // let user = users[i];
    clone.addEventListener("click", () => {
        localStorage.setItem("HiveSender", String(i));

        window.location.href = `templates/profile.html`;
    });

    // clone.children[0].children[0].innerHTML = ""; // AVATAR
    
    // clone.children[0].children[1].children[0].innerHTML = user;
    // clone.children[0].children[1].children[2].innerHTML = users[i]["preview"];
    // clone.children[1].innerHTML = users[i]["time"];
    // lista.appendChild(clone);
}
document.querySelector(".container").appendChild(lista);
