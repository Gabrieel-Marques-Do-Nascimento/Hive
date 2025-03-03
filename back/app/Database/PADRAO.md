## Padrão de Mensagens

### Cada mensagem deve seguir a estrutura abaixo, tanto no front quanto no backend:
```
{
  "id": "id do dono da tabela",
  "other_id": "id do outro usuário ou contato",
  "to": "destinatário da mensagem",
  "message": "mensagen que sera salva e enviada ao destinatário "
}
```