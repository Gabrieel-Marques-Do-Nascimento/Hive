# main.py
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.list import TwoLineListItem
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDIconButton
from kivymd.uix.scrollview import MDScrollView
from kivy.lang import Builder
from datetime import datetime

KV = '''
<ChatScreen>:
    MDBoxLayout:
        orientation: 'vertical'
        
        MDTopAppBar:
            title: "Chat App"
            elevation: 4
            pos_hint: {"top": 1}
            
        MDScrollView:
            id: scroll_view
            MDList:
                id: chat_list
                padding: 10
                spacing: 5
                
        MDBoxLayout:
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
'''


class ChatScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
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

            # Rola para a última mensagem
            self.ids.scroll_view.scroll_to(message_item)


class ChatApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.theme_style = "Light"
        Builder.load_string(KV)
        return ChatScreen()


if __name__ == '__main__':
    ChatApp().run()
