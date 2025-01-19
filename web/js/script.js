/**
 * carrega dados salvos no navegador
 * @param {*} name nome do dado salvo localmente
 * @param {*} type `string ` ou `json`
 * @returns
 */
function load(name, type) {
    const data = localStorage.getItem(name);
    if (type === "json") {
        return JSON.parse(data);
    }
    if (type === "string" || typeof data == "string") {
        return data;
    }
    if (typeof data == "number") {
        return data;
    }
    return null;
}
/**
 * nome do dado a ser salvo localmente
 * @param {*} name nome do dado a ser salvo localmente
 * @param {*} data o dado que deve ser salvo
 */
function save(name, data) {
    localStorage.setItem(name, data);
}

console.log("hello");
if (load("1463token-as-savekjg", "string")) {
    console.log("token já existe");
    load("hiveid");
}

// teste user-msg
// simula os dados salvos lacalmente
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

if (true) {
    let userInd = load("HiveSender");

    if (userInd) {
        const sendername = document.querySelector("#sendername");
        const username = document.getElementById("username");
        sendername.innerHTML = users[parseInt(userInd)]["username"];
    }
    const msgs_container = document.getElementById("msgs");
    const msgs = document.createElement("p");

    // para o user
    // clone.id = "user-msg"
    // para o destinatário
    // clone.id = "sender-msg"
    let messages = JSON.parse(localStorage.getItem("messages"));
    if (messages) {
        for (let i = 0; i < messages.length; i++) {
            const clone = msgs.cloneNode(true);
            message = messages[i];
            
            userId = users[parseInt(userInd)]["id"];
            if (
                message["pessoaId"] == userId &&
                message["senderId"] == userId
            ) {
                
                clone.innerHTML = messages[i]["message"];
                clone.id = "sender-msg";
                msgs_container.appendChild(clone);
            }
            if (message["senderId"] == 1 && message["pessoaId"] == userId) {
                
                clone.innerHTML = messages[i]["message"];
                clone.id = "user-msg";
                msgs_container.appendChild(clone);
            }
        }
    }
} else {
    window.location.href = "login-page";
}
