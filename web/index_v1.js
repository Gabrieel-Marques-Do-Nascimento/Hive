const http = require("http");
const fs = require("fs");
const path = require("path");

const server = http.createServer((req, res) => {
    if (req.url === "/" || req.url === "/index.html") {
        fs.readFile("index.html", (err, content) => {
            if (err) {
                res.writeHead(500);
                res.end("Erro ao carregar o arquivo");
                return;
            }
            res.writeHead(200, { "Content-Type": "text/html" });
            res.end(content);
        });
    } else {
        res.writeHead(404);
        res.end("Página não encontrada");
    }
});
let mercearia = "192.168.1.9";
let casa = "192.168.0.107";
const PORT = 8081;
server.listen(PORT, "0.0.0.0", () => {
    console.log(`Servidor rodando em http://<${mercearia}>:${PORT}`);
});
