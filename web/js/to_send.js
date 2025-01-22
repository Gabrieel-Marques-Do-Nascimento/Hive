import { URL } from "./env.js";
import { new_msg } from "./script.js";

const input = document.getElementById("msg-input");
const send_button = document.getElementById("send");
let token = localStorage.getItem("1463token-as-savekjg");
send_button.addEventListener("click", () => {
	new_msg(input.value)
	input.value = null
    // fetch(`${URL}/send_msg`, {
    //     method: "POST",
    //     headers: {
    //         accept: "application/json",
    //         "Content-Type": "application/json",
    //         Authorization: `Bearer ${token}`,
    //         uid: 1
    //     },
    //     body: {
    //         id: 1,
    //         msg: input.value,
    //         "p-id": 2
    //     }
    // })
    //     .then(resp => {
    //         if (!resp.ok) {
    //             throw new Error(`HTTP ERRO! Status: ${resp.status}`);
    //         }
    //         return resp.json();
    //     })
    //     .then(data => {})
    //     .catch(error => {
    //         console.error(`erro a realizar a requisição: ${error}`);
    //     });
});
