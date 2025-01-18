Para receber informações do backend em tempo real sem fazer polling (requisições constantes), você pode usar WebSockets ou Server-Sent Events (SSE). Vou criar um exemplo simples usando WebSocket, que é a solução mais comum e amplamente suportada.

// Servidor (Node.js com ws)
const WebSocket = require('ws');
const wss = new WebSocket.Server({ port: 8080 });

// Armazenar todas as conexões ativas
const clients = new Set();

wss.on('connection', (ws) => {
    // Adicionar novo cliente ao conjunto
    clients.add(ws);
    
    console.log('Novo cliente conectado');
    
    ws.on('close', () => {
        // Remover cliente quando desconectar
        clients.delete(ws);
        console.log('Cliente desconectado');
    });
});

// Função para enviar mensagem para todos os clientes
function broadcastMessage(message) {
    clients.forEach(client => {
        if (client.readyState === WebSocket.OPEN) {
            client.send(JSON.stringify(message));
        }
    });
}

// Exemplo: quando receber uma nova informação no servidor
function onNovaInformacao(dados) {
    broadcastMessage({
        tipo: 'atualizacao',
        dados: dados
    });
}

// Frontend (JavaScript)
class WebSocketClient {
    constructor() {
        this.connect();
    }

    connect() {
        this.ws = new WebSocket('ws://localhost:8080');

        this.ws.onopen = () => {
            console.log('Conectado ao servidor');
        };

        this.ws.onmessage = (event) => {
            const mensagem = JSON.parse(event.data);
            
            switch(mensagem.tipo) {
                case 'atualizacao':
                    this.handleAtualizacao(mensagem.dados);
                    break;
                // Adicione outros casos conforme necessário
            }
        };

        this.ws.onclose = () => {
            console.log('Desconectado. Tentando reconectar em 5 segundos...');
            setTimeout(() => this.connect(), 5000);
        };
    }

    handleAtualizacao(dados) {
        // Exemplo de atualização do DOM
        const elemento = document.getElementById('atualizacoes');
        elemento.innerHTML = `Nova atualização: ${JSON.stringify(dados)}`;
    }
}

// Inicializar o cliente
const wsClient = new WebSocketClient();

Este exemplo mostra como implementar uma comunicação em tempo real entre servidor e cliente. Aqui está como funciona:

1. No servidor:
   - Criamos um servidor WebSocket que mantém uma lista de todos os clientes conectados
   - Quando uma nova informação chega, ela é enviada para todos os clientes conectados
   - O servidor gerencia conexões e desconexões automaticamente

2. No cliente:
   - Implementamos uma classe que gerencia a conexão WebSocket
   - Reconecta automaticamente se a conexão cair
   - Processa diferentes tipos de mensagens recebidas do servidor
   - Atualiza a interface do usuário quando necessário

Para usar este código, você precisará:

1. No servidor:
   - Instalar o pacote `ws`: `npm install ws`
   - Executar o servidor Node.js

2. No frontend:
   - Incluir o código do cliente no seu HTML
   - Garantir que a URL do WebSocket corresponda ao seu servidor

Você também pode considerar usar bibliotecas como Socket.IO, que oferece mais recursos e melhor suporte a diferentes navegadores, ou Server-Sent Events para comunicação unidirecional do servidor para o cliente.

Quer que eu mostre como implementar usando Socket.IO ou SSE como alternativa?