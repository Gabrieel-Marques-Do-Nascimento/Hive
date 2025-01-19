
/**
 * carrega dados salvos no navegador
 * @param {*} name nome do dado salvo localmente
 * @param {*} type `string ` ou `json`
 * @returns 
 */
function load(name, type){
    const data = localStorage.getItem(name);
    if (type === 'json') {
        return JSON.parse(data);
    }
    if (type === 'string') {
        return data;
    }
    return null;
}
/**
 * nome do dado a ser salvo localmente
 * @param {*} name nome do dado a ser salvo localmente
 * @param {*} data o dado que deve ser salvo
 */
function save(name, data){
    localStorage.setItem(name, data);
}

console.log('hello');
if (load('1463token-as-savekjg', 'string')) {
    console.log('token já existe');
  load("hiveid")
}
else {
    window.location.href = "login-page"
}