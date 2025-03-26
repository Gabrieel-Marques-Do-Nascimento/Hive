from kivymd.app import  MDApp
from kivymd.uix.screenmanager import ScreenManager
from kivy.clock import  Clock
from kivy.lang import Builder
from kivymd.uix.dialog import  MDDialog
from kivymd.uix.button import  MDFlatButton


from database import UserDB, USER
from home import  HomeScreen, home
from contact import  Messages, message
from screens import LoaderScreen, loader, login, LoginScreen
from socket_confg import  sio
from new_contact import ContactApp, ContactScreen, add


# class  MyApp(MDApp): # referente ao arquivo .kv

class HiveApp(ContactApp):
    """
    class principal
    """

    def run2(self):

        def decorado():
            self.run()
        decorado()

    def build(self):
        """
        Builds the application's user interface.

        Configures the app by:
        1. Loading the KV language string
        2. Initializing the socket connection
        3. Creating a ScreenManager with HomeScreen and Messages screens

        Returns:
            ScreenManager: The main application screen manager
        """
        from kivy.clock import Clock
        Clock.schedule_once(lambda dt: self.start_socket(), 1)
        Builder.load_file("Lang-kivy.kv")

        sm = self.sm
        sm.add_widget(LoaderScreen(name=loader.name))
        sm.add_widget(LoginScreen(name=login.name))
        sm.add_widget(HomeScreen(name=home.name))
        sm.add_widget(Messages(name=message.name))
        sm.add_widget(ContactScreen(name=add.name))
        
        # Troca de tela após 3 segundos
        Clock.schedule_once(self.switch_to_home, 3)
        
        return sm




    def show_dialog(self, title, text):
        dialog = MDDialog(
            title=title,
            text=text,
            buttons=[MDFlatButton(text="OK", on_release=lambda x: dialog.dismiss())],
        )
        dialog.open()

 


    def callback(self):
        """
        Handles navigation back to the home screen.

        Transitions the screen manager to the home screen with a downward animation.
        """
        self.root.transition.direction = home.down
        self.root.current = home.name

    async def connect_socket(self):
        """
        Establishes an asynchronous socket connection to the server.

        Attempts to:
        1. Connect to the socket server at http://127.0.0.1:5000
        2. Register the user with a predefined user ID
        3. Set up event listeners

        Handles connection exceptions silently.
        """

        try:
            # print("socket conectado")
            await sio.connect("http://127.0.0.1:5000")
            await sio.emit('registrar_usuario', {'usuario_id': 'usuario123', "id": 1})
            # await sio.wait()
            await sio.on("enveto")

        except Exception:
            pass

    def start_socket(self):
        """
        Initializes the socket connection in a separate thread.

        Creates a daemon thread that runs the asynchronous socket connection method,
        preventing blocking of the main application thread.
        """
        from threading import Thread
        import asyncio

        def run():
            asyncio.run(self.connect_socket())
        Thread(target=run, daemon=True).start()

    def login(self):
        username = self.root.get_screen(login.name).ids.username.text
        password = self.root.get_screen(login.name).ids.password.text

        if username == "admin" and password == "1234":
            self.show_dialog("Login bem-sucedido", "Bem-vindo, Admin!")
        else:
            self.show_dialog("Erro", "Usuário ou senha inválidos!")



    def toggle_password_visibility(self, field):
        if field.password:
            field.password = False
            field.icon_right = "eye"
        else:
            field.password = True
            field.icon_right = "eye-off"

    def switch_to_home(self, dt):
        self.sm.current = home.name

if __name__ == "__main__":
    HiveApp().run()