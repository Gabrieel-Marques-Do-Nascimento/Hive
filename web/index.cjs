// Importando os módulos necessários
const http = require("http"); // Para criar o servidor HTTP
const fs = require("fs"); // Para ler arquivos do sistema de arquivos
const path = require("path"); // Para manipulação de caminhos de arquivos

const os = require('os');




/**
 * Gets the local IPv4 address of the machine
 * Iterates through network interfaces to find the first non-internal IPv4 address
 * @returns {string} The local IPv4 address or 'IP não encontrado' if not found
 */
function getLocalIP() {
  const interfaces = os.networkInterfaces();
  for (const name of Object.keys(interfaces)) {
    for (const iface of interfaces[name]) {
      if (iface.family === 'IPv4' && !iface.internal) {
        return iface.address;
      }
    }
  }
  return 'IP não encontrado';
}
const localIP = getLocalIP();










// retorna o tipo de arquivo com base na extencao
function getContentType(extname) {
    switch (extname) {
        case ".html":
            return "text/html";
        case ".css":
            return "text/css";
        case ".js":
            return "application/javascript";
        case ".jpg":
        case ".jpeg":
            return "image/jpeg";
        case ".png":
            return "image/png";
        case ".gif":
            return "image/gif";
        default:
            return "application/octet-stream";
    }
}

// Criando o servidor HTTP
const server = http.createServer((req, res) => {
    // Obtendo o caminho do arquivo solicitado
    let filePath = path.join(
        __dirname,
        req.url === "/" ? "index.html" : req.url
    );
    // Obtendo a extensão do arquivo
    let extname = path.extname(filePath);

    // Lendo o arquivo solicitado
    fs.readFile(filePath, (err, content) => {
        if (err) {
            // Se o arquivo não for encontrado, retorna erro 404
            res.writeHead(404);
            res.end("Página ou arquivo não encontrado");
        } else {
            // Caso o arquivo seja encontrado, define o tipo de conteúdo baseado na extensão
            res.writeHead(200, { "Content-Type": getContentType(extname) });
            res.end(content); // Retorna o conteúdo do arquivo
        }
    });
});

// Definindo o IP e a porta do servidor
let casa = "192.168.0.107";
let mercearia = "192.168.1.9"; // Endereço IP configurado
const PORT = 8081; // Definindo a porta do servidor

// Iniciando o servidor para ouvir na porta configurada e no IP especificado
server.listen(PORT, "0.0.0.0", () => {
    // Exibindo no console que o servidor está rodando
    

console.log(`Servidor rodando em http://${localIP}:${PORT}`)
});


