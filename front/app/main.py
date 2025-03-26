import socketio
from kivymd.app import MDApp
from kivymd.uix.screenmanager import ScreenManager
from kivymd.uix.list import ThreeLineAvatarListItem, TwoLineListItem
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivy.clock import  Clock
from kivymd.uix.label import MDLabel
from kivymd.uix.dialog import  MDDialog
from kivymd.uix.button import  MDFlatButton
from kivymd.font_definitions import theme_font_styles
import sqlite3
from datetime import datetime
# testes
from app_testes.loggeuer_teste_init import ActivationTime
# from app_testes.users_teste import users10
users = []


# ==============  user ===============
class USER:
    def __init__(self, user):
        self.user: dict = user
        self.id: int = user["contact"]
        self.name: str = user["name"]
        self.update: str = user["update"]
        self.null: str = "null"
        self.user_id: int = user["id"]


# ============== data base ===============

class UserDB:
    def __init__(self):
        self.conn = sqlite3.connect('hivy.db')
        self.cursor = self.conn.cursor()

        # Criar tabela de usuários se não existir
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
                    id TEXT,
                    name TEXT,
                    contact TEXT,
                    update_time TEXT
                    )
                    ''')

    def create(self, user: USER):
        """
        Cria um novo usuário no banco de dados.
        """
        self.cursor.execute("INSERT INTO users (id, name, contact, update_time) VALUES (?, ?, ?, ?)",
                            (user.user_id, user.name, user.id, user.update))
        self.conn.commit()
        self.conn.close()
        return True
    
    def All(self):
        self.cursor.execute("SELECT * FROM users")
        return self.cursor.fetchall()
    
    def select(self, id):
        self.cursor.execute("SELECT * FROM users WHERE id=?", (id,))
        return self.cursor.fetchone()

# pass logguer time active app
# active = ActivationTime(__file__)
# active.file_name("Hive-messages-app", filetimename=True)
# active.clear()
# primeiro para iniciar
# active.debug(logg=False)
# ===========================================
# =====°===°====   BackEnd-API    =======°=°=====
# ===========================================
sio = socketio.AsyncClient()

@sio.event
def connect():
    print("connected")
sio.emit("registrar_usuario", {"id":4})
sio.connect("http://localhost:5000")
sio.wait()  # noqa: F704


# ===========================================
# =====°===°=====     FrontEnd     =======°=°======
# ===========================================

KV = """


<Contact>:
    #on_press: app.root.current = "messages"
    ImageLeftWidget:
        source: "assets/cogwheel (1).png"

<HomeScreen>:
	BoxLayout:
		orientation: "vertical"

		MDTopAppBar:
			title: "HIVE"
			elevation: 4
			pos_hint: {"top":1}

		ScrollView:
			MDList:
				id: contacts_list
				padding: 10
				spacing: 5
				
		BoxLayout:
		    size_hint_y: None
            height: "48dp"
		    adaptive_height: True
		    spacing: 5
		    padding: 5
		    orientation: "vertical"  # Para centralizar mais facilmente
		    MDIconButton:
		        id: addContact
		        icon: "plus"
		        pos_hint: {"center_x": 0.5}  # Centraliza horizontalmente
		        on_release: root.add()
		        
<Messages>:
	name: "messages"
	BoxLayout:
		orientation: "vertical"
		MDTopAppBar:
			title: "HIVE"
			elevation: 4
			pos_hint: {"top":1}
			id: topbar
			left_action_items: [["arrow-collapse-left", lambda x: app.callback()]]
			icon: "git"
		ScrollView:
			id: scroll_view2
			
			MDList:
				id: chat_list
				padding: 10
				spacing: 5
        BoxLayout:
            orientation: "horizontal"
            size_hint_y: 0.08
            adaptive_height: True
            spacing: 5
            padding: 5
            MDTextField:
                id: message_input
                hint_text: "Digite sua mensagem..."
                helper_text: "Pressione enviar ou o botão para enviar"
                helper_text_mode: "on_error"
                multiline: False
            MDIconButton:
                icon: "send"
                on_release: root.send_message()

<ADD>:
    name: "add_contact"

    MDBoxLayout:
        orientation: "vertical"
        padding: "20dp"
        spacing: "10dp"

        MDTopAppBar:
            title: "Adicionar Contato"

        ScrollView:
            MDBoxLayout:
                orientation: "vertical"
                spacing: "20dp"
                size_hint_y: None
                height: self.minimum_height
                padding: "20dp"

                MDTextField:
                    id: contact_name
                    hint_text: "Nome do Contato"
                    mode: "fill"

                MDTextField:
                    id: contact_id
                    hint_text: "ID do Contato"
                    mode: "fill"
                    input_filter: "int"

                MDRaisedButton:
                    text: "Adicionar Contato"
                    pos_hint: {"center_x": 0.5}
                    on_release: app.add_contact()
                    
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

<LoaderScreen>:
    name: "loader"

    MDBoxLayout:
        orientation: "vertical"
        spacing: "10dp"
        padding: "20dp"
        pos_hint: {"center_x": 0.5, "center_y": 0.5}

        MDIcon:
            icon: "android"  # Substitua pelo ícone do seu app
            halign: "center"
            font_size: "100dp"

        MDLabel:
            text: "Carregando..."
            halign: "center"
            theme_text_color: "Secondary"

        MDSpinner:
            size_hint: None, None
            size: "48dp", "48dp"
            pos_hint: {"center_x": 0.5}
            active: True


"""

class LoaderScreen(MDScreen):
    pass


class LoginScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class ADD(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Contact(ThreeLineAvatarListItem):
    """
    A custom list item representing a contact in the Hive messaging app.

    Displays a contact's name, last message, and online status with an avatar image.
    Inherits from KivyMD's ThreeLineAvatarListItem to provide a three-line list item 
    with an image on the left side.

    Attributes:
        text (str): Contact's name
        secondary_text (str): Last message from the contact
        tertiary_text (str): Contact's online status
    """

    def __init__(self, user: USER, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(MDLabel(text=user.name, font_size="20sp",
                        font_style=theme_font_styles[6], pos_hint={"x": .2, "center_y": .5}))
        self.add_widget(MDLabel(text=user.null, font_style=theme_font_styles[7],
                        font_size="16sp", pos_hint={"x": .5, "center_y": .75}))
        self.add_widget(MDLabel(text='indefinido', font_size="14sp",
                        font_style=theme_font_styles[7], pos_hint={"x": .8, "center_y": .75}))


class HomeScreen(MDScreen):
    """
    The home screen of the Hive messaging app, displaying a list of contacts.

    Responsible for loading and displaying contacts, and managing navigation 
    to the messages screen when a contact is selected.

    Methods:
        on_enter(): Loads contacts when the screen becomes active
        callback_screen(instance, user): Handles navigation to the messages screen
        create_contacts(user): Creates a contact list item for a given user
        load_contacts(): Populates the contacts list with user data
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.name = 'home'

    def on_enter(self):
        """
        espera o arquivo kv ser caregado antes de executar o cofigo abaixo
        """

        self.load_contacts()

    def callback_screen(self, instace, user: USER):
        """
        function calbeck:

        args:
                *args: recebe o parametros nao nomeados retorna uma lista,
                **kwargs: recebe parametros nomeados e retorna um dict
        """
        userdate = user
        screen = self.parent.get_screen("messages")
        screen.ids.topbar.title = userdate.name
        self.manager.transition.direction = "up"
        self.manager.current = "messages"

    def create_contacts(self, user: USER):
        """
        """

        user_item = Contact(user=user)
        # Adicionando labels personalizados
        # criar uma tela de msgs
        user_item.bind(
            on_press=lambda x:
            self.callback_screen(x, user))
        self.ids.contacts_list.add_widget(user_item)

    def load_contacts(self):
        """
        add os elementos da lista aos contatos
        """

        if hasattr(self.ids, "contacts_list"):
            self.ids.contacts_list.clear_widgets()
            for user in users:
                _user = USER(user)
                self.create_contacts(user=_user)

    def reseived_message(self):
        """
        resebe as mensssagens e lida com os novas mensages resebidas de pessoas que nunca enviarao
        """
        pass
       
    def add(self):
        screen = self.parent.get_screen("add_contact")
        self.manager.transition.direction = "up"
        self.manager.current = "add_contact"
    	

class Messages(MDScreen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.messages = []
        self.title = "HIVE"
        self.name = 'messages'

    def send_message(self):
        """
        Sends a message in the chat and updates the UI.

        Performs the following actions:
        1. Retrieves the message text from the input field
        2. Emits the message via SocketIO to the server
        3. Adds the message to the chat list with a timestamp
        4. Clears the input field
        5. Scrolls to the latest message

        Triggers only if the message is not an empty string.
        """
        message_text = self.ids.message_input.text.strip()
        if message_text:
            # envia a message ao socketio
            sio.emit('enviar_mensagem', {"id": 2, "message": message_text})
            # ----------------------------------------

            current_time = datetime.now().strftime("%H:%M")
            message_item = TwoLineListItem(
                text=message_text,
                secondary_text=f"Enviado às {current_time}",
            )
            self.ids.chat_list.add_widget(message_item)
            self.messages.append({
                'text': message_text,
                'time': current_time
            })
            self.ids.message_input.text = ""

            # Rola para a última mensagem
            self.ids.scroll_view2.scroll_to(message_item)


# class  MyApp(MDApp): # referente ao arquivo .kv

class HiveApp(MDApp):
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
        Builder.load_string(KV)

        sm = ScreenManager()
        self.sm = sm
        sm.add_widget(LoaderScreen(name="loader"))
        sm.add_widget(LoginScreen())
        sm.add_widget(HomeScreen())
        sm.add_widget(Messages())
        sm.add_widget(ADD())
        
        # Troca de tela após 3 segundos
        Clock.schedule_once(self.switch_to_home, 3)
        
        return sm


    def add_contact(self):
        name = self.root.get_screen("add_contact").ids.contact_name.text
        contact_id = self.root.get_screen("add_contact").ids.contact_id.text

        if name and contact_id:
            self.show_dialog("Contato adicionado!", f"Nome: {name}\nID: {contact_id}")
        else:
            self.show_dialog("Erro", "Preencha todos os campos!")

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
        self.root.transition.direction = "down"
        self.root.current = "home"

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
        username = self.root.get_screen("login").ids.username.text
        password = self.root.get_screen("login").ids.password.text

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
        self.sm.current = "home"

if __name__ == "__main__":
    HiveApp().run()
