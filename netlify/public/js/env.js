//require('dotenv').config();
//import {dotenv} from "./dotenv"
//dotenv.config()

const resp = await fetch(
  `http://${location.hostname}:${location.port}/.netlify/functions/api`
);
const json = await resp.json();
export const URL = json.url;

// Exemplo de uso das variáveis
/*
const port = process.env.PORT;
const dbUrl = process.env.DATABASE_URL;

console.log(`Aplicação rodando na porta ${port}`);
console.log(`Conectando ao banco de dados em: ${dbUrl}`);

   export let url = process.env.URL
// env.js (CommonJS)
*/
