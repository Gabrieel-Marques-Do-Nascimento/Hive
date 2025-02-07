from kivymd.app import MDApp
from kivymd.uix.screenmanager import ScreenManager
from kivymd.uix.list import ThreeLineAvatarListItem, TwoLineListItem, ImageLeftWidget
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivymd.uix.label import MDLabel
from kivymd.font_definitions import theme_font_styles
from functools import partial
from datetime import datetime

# Import your test modules
from app_testes.loggeuer_teste_init import ActivationTime
from app_testes.users_teste import users10

users = users10
active = ActivationTime()
active.file_name("Hive-messages-app", filetimename=True)
active.clear()
active.debug(logg=False)

import socketio
sio = socketio.AsyncClient()

KV = '''
<Contact>:
    ImageLeftWidget:
        source: "assets/cogwheel (1).png"

<HomeScreen>:
    BoxLayout:
        orientation: "vertical"
        
        MDTopAppBar:
            title: "HIVE"
            elevation: 4
            pos_hint: {"top": 1}
            
        ScrollView:
            MDList:
                id: contacts_list
                padding: 10
                spacing: 5    
        
        BoxLayout:
            size_hint_y: None
            height: "48dp"
            spacing: 5
            padding: 5
            
            MDIconButton:
                icon: "plus"
                pos_hint: {"center_x": 0.5}

<Messages>:
    BoxLayout:
        orientation: "vertical"        
        
        MDTopAppBar:
            title: "HIVE"
            elevation: 4
            pos_hint: {"top": 1}
            id: topbar            
            left_action_items: [["arrow-left", lambda x: app.callback()]]
        
        ScrollView:
            id: scroll_view2        
            MDList:
                id: chat_list
                padding: 10
                spacing: 5             
        
        BoxLayout:
            size_hint_y: None
            height: "56dp"
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
'''

class Contact(ThreeLineAvatarListItem):
    def __init__(self, user, **kwargs):
        super().__init__(**kwargs)
        active.debug("Contact-item")
        self.add_widget(ImageLeftWidget(source="assets/cogwheel (1).png"))
        self.text = user["name"]
        self.secondary_text = user["message"]
        self.tertiary_text = user["online"]

class HomeScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        active.debug("HomeScreen")
        self.name = 'home'
    
    def on_enter(self):
        """Called when screen is entered"""
        active.debug("HomeScreen-on_enter")
        self.load_contacts()
    
    def callback_screen(self, instance, user):
        messages_screen = self.parent.get_screen("messages")
        messages_screen.ids.topbar.title = user["name"]
        self.parent.transition.direction = "left"
        self.parent.current = "messages"

    def create_contacts(self, user):
        active.debug("HomeScreen-create_contacts")
        user_item = Contact(user=user)
        user_item.bind(on_press=lambda x: self.callback_screen(x, user))
        self.ids.contacts_list.add_widget(user_item)
    
    def load_contacts(self):
        active.debug("HomeScreen-load_contacts")
        if hasattr(self.ids, 'contacts_list'):
            self.ids.contacts_list.clear_widgets()
            for user in users:
                self.create_contacts(user)

class Messages(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        active.debug("Messages")
        self.name = 'messages'
        self.messages = []
    
    def send_message(self):
        message_text = self.ids.message_input.text.strip()
        if message_text:
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
            self.ids.scroll_view2.scroll_to(message_item)

class HiveApp(MDApp):
    def build(self):
        active.debug("HiveApp-build")
        self.theme_cls.primary_palette = "Blue"
        Builder.load_string(KV)
        
        # Create the screen manager
        sm = ScreenManager()
        sm.add_widget(HomeScreen())
        sm.add_widget(Messages())
        
        return sm
    
    def callback(self):
        self.root.transition.direction = "right"
        self.root.current = "home"
    
    async def connect_socket(self):
        try:
            await sio.connect("http://127.0.0.1:5000")
            await sio.emit('registrar_usuario', {'usuario_id': 'usuario123', "id": 1})
        except Exception as e:
            print(f"Socket connection error: {e}")
    
    def start_socket(self):
        from threading import Thread
        import asyncio
        active.debug("HiveApp-start_socket")
        
        def run():
            asyncio.run(self.connect_socket())
        
        Thread(target=run, daemon=True).start()

if __name__ == "__main__":
    HiveApp().run()