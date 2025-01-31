let users = [
  { enviado: 2, message: "hello world ", online: null, pessoa: 1, userid: 2 },
  { enviado: 1, message: "oi", online: null, pessoa: 1, userid: 2 },
  { enviado: 1, message: "oi", online: null, pessoa: 1, userid: 2 },
  {
    enviado: 1,
    message: "como c ta me responde",
    online: null,
    pessoa: 1,
    userid: 2,
  },
  {
    enviado: 2,
    message: "teste: fla com migo ",
    online: null,
    pessoa: 1,
    userid: 2,
  },
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
