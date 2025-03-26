from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen


from extend_base import  Base, BaseApp, BaseScreen
from utils import Requestist

requestt =  Requestist()


Login_KV = """
ScreenManager:
    LoginScreen:

<LoginScreen>:
    name: "login"

    MDBoxLayout:
        orientation: "vertical"
        padding: "20dp"
        spacing: "10dp"

        MDTopAppBar:
            title: "Login"
        
        ScrollView:
            MDBoxLayout:
                orientation: "vertical"
                size_hint_y: None
                height: self.minimum_height
                padding: "20dp"
                spacing: "20dp"
                pos_hint: {"center_x": 0.5, "center_y": 0.5}

                MDTextField:
                    id: username
                    hint_text: "Usuário"
                    mode: "fill"
                    icon_right: "account"

                MDTextField:
                    id: password
                    hint_text: "Senha"
                    password: True
                    mode: "fill"
                    icon_right: "eye-off"
                    on_touch_down: app.toggle_password_visibility(self)

                MDRaisedButton:
                    text: "Entrar"
                    pos_hint: {"center_x": 0.5}
                    on_release: app.login()
"""
class Login(Base):
	name = "login"

login = Login()
class LoginScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class LoginApp(BaseApp):
    def build(self):
        return Builder.load_string(Login_KV)

    def login(self):
        username = self.root.get_screen("login").ids.username.text
        password = self.root.get_screen("login").ids.password.text
        requestt.login(data={"email": username, "password": password}).json()
        if requestt.status_code == 200 and requestt.json["status"] == "ok":
            self.show_dialog("Login bem-sucedido", f"Bem-vindo, {username}!")
            self.sm.current = self.home.name

        if username == "admin" and password == "1234":
            self.show_dialog("Login bem-sucedido", "Bem-vindo, Admin!")
        # else:
        #     self.show_dialog("Erro", "Usuário ou senha inválidos!")

 

    def toggle_password_visibility(self, field):
        if field.password:
            field.password = False
            field.icon_right = "eye"
        else:
            field.password = True
            field.icon_right = "eye-off"

    def switch_to_login(self, dt):
        self.sm.current = login.name

if __name__ == "__main__":
    LoginApp().run()