import { URL } from "./env.js";

const socket = io.connect(URL);
export let token = localStorage.getItem("1463token-as-savekjg");
export let userId = parseInt(localStorage.getItem("hiveid"));
export let fromId = parseInt(localStorage.getItem("HiveSender"));
console.log("from", fromId, "userid", userId);
export let messages = JSON.parse(localStorage.getItem("messages"));

export function request_messages() {

  if (!localStorage.getItem("messages")) {
    fetch(`${URL}/my_msgs`, {
      method: "POST",
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json",
        Authorization: `Bearer ${token}`,
        uid: parseInt(userId),
      },
      body: JSON.stringify({ id: parseInt(userId) }),
    })
      .then((resp) => {
        if (!resp.ok) {
          throw new Error(`HTTP error! Status: ${resp.status}`);
        }
        return resp.json(); // Retorna a Promise contendo os dados
      })
      .then((data) => {
        localStorage.setItem("messages", JSON.stringify(data));
      })
      .catch((error) => {
        console.error("Erro ao realizar a requisição:", error);
      });
  }
}

export function room(user_id, from_id) {
  if (parseInt(user_id) <= parseInt(from_id)) {
    console.log("channel: " + user_id.toString() + from_id.toString());
    return user_id.toString() + from_id.toString();
  } else {
    console.log("channel: " + from_id.toString() + user_id.toString());
    return from_id.toString() + user_id.toString();
  }
}
