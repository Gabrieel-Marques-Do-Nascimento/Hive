fetch('http://192.168.0.103:5000/login', {
    method: 'POST', // ✅ Certifique-se de que a API aceita POST
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({ username: 'user', password: '12345' })
})
.then(res => {
    if (!res.ok) {
        return res.text().then(text => { throw new Error(`Erro ${res.status}: ${text}`); });
    }
    return res.json();
})
.then(data => console.log('Login bem-sucedido:', data))
.catch(err => console.error("Erro ao fazer login:", err));
