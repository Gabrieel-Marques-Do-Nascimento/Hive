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

export function new_msg(message) {
    const msgs_container = document.getElementById("msgs");
    const msgs = document.createElement("p");
    const clone = msgs.cloneNode(true);
    clone.innerHTML = message;
    clone.id = "user-msg";
    msgs_container.appendChild(clone);
}

console.log("hello");
if (load("1463token-as-savekjg", "string")) {
    console.log("token já existe");

    let userInd = load("HiveSender");

    if (userInd) {
        const sendername = document.querySelector("#sendername");
        const username = document.getElementById("username");
        sendername.innerHTML = "";
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
            let message = messages[i];

            let userId = load("HiveSender");
            console.log(message["pessoa"], "  ", message["enviado"]);
            if (message["pessoa"] == message["enviado"]) {
                clone.innerHTML = messages[i]["message"];
                clone.id = "sender-msg";
                msgs_container.appendChild(clone);
            }
            if (
                JSON.parse(message["enviado"]) == 1 &&
                message["pessoa"] == userId
            ) {
                clone.innerHTML = messages[i]["message"];
                clone.id = "user-msg";
                msgs_container.appendChild(clone);
            }
        }
    }
} else {
    window.location.href = "login.html";
}
