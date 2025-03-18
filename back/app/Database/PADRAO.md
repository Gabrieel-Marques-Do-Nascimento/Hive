## Padrão de Mensagens

### Cada mensagem deve seguir a estrutura abaixo, tanto no front quanto no backend:
```python
{
  "id": "id do dono da tabela",
  "other_id": "id do outro usuário ou contato",
  "to": "destinatário da mensagem",
  "mid": "id da mensagem",
  "message": "mensagen que sera salva e enviada ao destinatário "
}
```