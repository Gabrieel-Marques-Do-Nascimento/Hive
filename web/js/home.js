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
// teste user-msg
let users = [
    { username: "gabriel", id: 2, time: "15:00", preview: "hello world" },
    { username: "camila", id: 3, time: "15:00", preview: "hello world" },
    { username: "joao", id: 4, time: "15:00", preview: "hello world" },
    { username: "maria", id: 5, time: "16:00", preview: "good afternoon" },
    { username: "ana", id: 6, time: "16:30", preview: "how are you?" },
    { username: "lucas", id: 7, time: "17:00", preview: "what's up?" },
    { username: "carla", id: 8, time: "17:30", preview: "good evening" },
    { username: "paulo", id: 9, time: "18:00", preview: "hey there" },
    { username: "renato", id: 10, time: "18:30", preview: "long time no see" },
    { username: "larissa", id: 11, time: "19:00", preview: "good night" }
];

let messages = [
    {"id": 1, "senderId": 2, "pessoaId": 2, "message": "hello world", "created": "15/01/2025"},
    {"id": 2, "senderId": 1, "pessoaId": 2, "message": "hello world", "created": "16/01/2025"},
    {"id": 3, "senderId": 1, "pessoaId": 2, "message": "Mensagem enviada", "created": "17/01/2025"},
    {"id": 4, "senderId": 1, "pessoaId": 2, "message": "Mensagem enviada", "created": "19/01/2025"},
    {"id": 5, "senderId": 1, "pessoaId": 2, "message": "Mensagem enviada", "created": "20/01/2025"},
    {"id": 6, "senderId": 2, "pessoaId": 2, "message": "Mensagem recebida", "created": "22/01/2025"},
    {"id": 7, "senderId": 2, "pessoaId": 2, "message": "Mensagem recebida", "created": "25/01/2025"},
    {"id": 8, "senderId": 2, "pessoaId": 2, "message": "Mensagem recebida", "created": "26/01/2025"},
    {"id": 9, "senderId": 2, "pessoaId": 2, "message": "Mensagem recebida", "created": "28/01/2025"},
    {"id": 10, "senderId": 2, "pessoaId": 2, "message": "Mensagem recebida", "created": "30/01/2025"},
    {"id": 11, "senderId": 1, "pessoaId": 2, "message": "Mensagem enviada", "created": "01/02/2025"},
    {"id": 12, "senderId": 2, "pessoaId": 2, "message": "Mensagem recebida", "created": "02/02/2025"}
];

// deve ser feito no login-page
// apos o login o servidor envia todas as mensagens salvas do user
if (!localStorage.getItem("messages")){
	localStorage.setItem("messages", JSON.stringify(messages))
}





for (let i = 0; i < users.length; i++) {
    let clone = item.cloneNode(true);
    user = users[i]["username"]
    clone.addEventListener("click", () => {
    	localStorage.setItem("HiveSender", String(i))
    	
        window.location.href = `templates/profile.html`
    });
    clone.children[0].children[0].innerHTML = ""; // AVATAR
    //
    clone.children[0].children[1].children[0].innerHTML = user;
    clone.children[0].children[1].children[2].innerHTML = users[i]["preview"];
    clone.children[1].innerHTML = users[i]["time"];
    lista.appendChild(clone);
}
document.querySelector(".container").appendChild(lista);
