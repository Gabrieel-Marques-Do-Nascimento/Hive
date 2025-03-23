class User {
  constructor() {
    this.Id = "hiveid";
    this.otherid = "HiveSender";
    this.messageTag = "messages";
    this.contact_listTag = "contact-list";
    this.bioTag = "hivebio";
    this.nameTag="hiveusername"
  }
  get id() {
    return parseInt(localStorage.getItem(this.Id));
  }
  set id(value) {
    return localStorage.setItem(this.id, value);
  }
  get name() {
    return localStorage.getItem(this.nameTag);
  }
  set name(value) {
    return localStorage.setItem(this.nameTag, value);
  }
  get otherId() {
    return parseInt(localStorage.getItem(this.otherid));
  }
  set otherId(value) {
    return localStorage.setItem(this.otherId, value);
  }
  get messages() {
    return JSON.parse(localStorage.getItem(this.messageTag));
  }
  set messages(value) {
    return localStorage.setItem(this.messageTag, value);
  }
  get contacts() {
    return JSON.parse(localStorage.getItem(this.contact_listTag));
  }
  set contacts(value) {
    return localStorage.setItem(this.contact_listTag, value);
  }
  get bio() {
    return localStorage.getItem(this.bioTag);
  }
  set bio(value) {
    return localStorage.setItem(this.bioTag, value);
  }

  get token(){
    return localStorage.getItem("1463token-as-savekjg");
  }
  set token(value){
    return localStorage.setItem("1463token-as-savekjg",value);
  }
}

class ligth{
  constructor(){
    this.theme = "light-mode";
  }
  get value(){
    return this.theme;
  }
}
class dark{
  constructor(){
    this.theme = "dark-mode";
  }
  get value(){
    return this.theme;
  }
}
class Theme{
  constructor(){
    this.istheme;
  }
  verify(){
    if (localStorage.getItem("theme")){
      this.istheme =localStorage.getItem("theme");
    }
  }
  get theme(){

    return this.istheme;
  }
  set theme(theme){
    localStorage.setItem("theme",theme.value);
    this.istheme = theme.value;
  }
  start(){
    this.verify();
    document.body.classList.add(this.istheme);
  }

}


export const theme = new Theme();
export const ligthTheme = new ligth();
export const darkTheme = new dark();
export const user = new User();
