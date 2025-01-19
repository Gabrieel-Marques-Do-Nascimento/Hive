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

user = users[0]
for (let i = 0; i < messages.length; i++) {
	message = messages[i]
        if (message["senderId"] == 1 && user["id"] == message["pessoaId"]){
        	console.log( "enviada",message)
        }
        if (message["senderId"] == user["id"]  && user["id"] == message["pessoaId"]){
        	console.log("recebida: ", message)
        }
        	
        }

