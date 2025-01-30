let users = [
    { enviado: 2, message: "teste: bom dia", online: null, pessoa: 1 },
    { enviado: 1, message: "teste: com c ta", online: null, pessoa: 1 },
    { enviado: 1, message: "Oi", online: null, pessoa: 2 },
    { enviado: 1, message: "Oi", online: null, pessoa: 2 },
    { enviado: 1, message: "u", online: null, pessoa: 2 },
    { enviado: 3, message: "u", online: null, pessoa: 2 } ,   { enviado: 4, message: "u", online: null, pessoa: 2 }
];

const user = 2;
let added = [];
for (let i = 0; i < users.length; i++) {
    //console.log(users[i]);

    if (users[i].enviado != user) {
        if (!added.includes(users[i].enviado)) {
            added.push(users[i].enviado);
        }
        console.log(added.toString());
    }
}
