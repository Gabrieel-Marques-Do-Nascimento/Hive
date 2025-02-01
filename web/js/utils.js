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
                uid: parseInt(userId)
            },
            body: JSON.stringify({ id: parseInt(userId) })
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
}

export function room(user_id, from_id) {
    if (parseInt(user_id) <= parseInt(from_id)) {
        console.log(`channel:${user_id}${from_id}`);
        return `${user_id}${from_id}`;
    } else {
        console.log(`channe:${from_id} ${user_id}`);
        return `${from_id}${user_id}`;
    }
}

export function newUser(
    pessoaN,
    hiveUserid = "Hive user",
    avatarI = "Hive",
    previewT = "preview",
    hors = "08:00"
) {
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
    let clone = item.cloneNode(true);

    clone.addEventListener("click", () => {
        localStorage.setItem("HiveSender", String(pessoaN));

        window.location.href = `templates/profile.html`;
    });
    clone.children[0].children[0].textContent = avatarI; // AVATAR
    //
    clone.children[0].children[1].children[0].textContent = hiveUserid;
    clone.children[0].children[1].children[2].textContent = previewT;

    clone.children[1].textContent = hors;
    return clone;
}

export function create_msg_element(pai, text, cloneId) {
    console.log("new msg");
    const msgs = document.createElement("p");
    const clone = msgs.cloneNode(true);
    clone.textContent = text;
    clone.id = cloneId;
    pai.appendChild(clone);
}
