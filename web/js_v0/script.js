import { fromId, userId, create_msg_element } from "../js/utils.js";

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

if (load("1463token-as-savekjg", "string")) {
  console.log("token já existe");

  let userInd = load("HiveSender");

  if (userInd) {
    const sendername = document.querySelector("#sendername");
    const username = document.getElementById("username");
    let username_str = localStorage.getItem("hiveusername");
    if (username_str) {
      username.textContent = username_str;
    }
    sendername.innerHTML = "";
  }
  const msgs_container = document.getElementById("msgs");
  const msgs = document.createElement("p");

  let messages = JSON.parse(localStorage.getItem("messages"));
  if (messages) {
    for (let i = 0; i < messages.length; i++) {
      console.log(messages[i]);
      const clone = msgs.cloneNode(true);
      let message = messages[i];

      console.log(message);
      if (
        parseInt(message["pessoa"]) == parseInt(message["enviado"]) &&
        parseInt(message["enviado"]) == fromId
      ) {
        create_msg_element(
          msgs_container,
          messages[i]["message"],
          "sender-msg"
        );
      }
      if (
        parseInt(message["enviado"]) == userId &&
        parseInt(message["pessoa"]) == fromId
      ) {
        create_msg_element(msgs_container, messages[i]["message"], "user-msg");
      }
    }
  }
} else {
  window.location.href = "login.html";
}
