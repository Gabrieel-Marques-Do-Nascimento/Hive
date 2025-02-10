from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.screen import MDScreen
from kivymd.uix.list import OneLineAvatarListItem, ImageLeftWidget

KV = '''
ScreenManagement:
    id: managerid
    HomeScreen:
        name: "home"
    Messages:
        name: "messages"

<TopAppBar@MDTopAppBar>:
    title: "HIVE"
    elevation: 4
    pos_hint: {"top": 1}

<Contact@OneLineAvatarListItem>:
    on_press: app.root.current = "messages"
    ImageLeftWidget:
        source: "assets/cogwheel (1).png"

<HomeScreen>:
    MDBoxLayout:
        orientation: "vertical"

        TopAppBar:

        MDScrollView:
            id: scroll_view
            MDList:
                id: contacts_list
                padding: 10
                spacing: 5

        MDBoxLayout:
            adaptive_height: True
            spacing: 5
            padding: 5
            orientation: "vertical"
            MDIconButton:
                icon: "plus"
                pos_hint: {"center_x": 0.5}
                on_release: app.add_contact()

<Messages>:
    name: "messages"
    MDBoxLayout:
        orientation: "vertical"

        TopAppBar:
            left_action_items: [["arrow-left", lambda x: app.root.current = "home"]]

        MDScrollView:
            id: scroll_view2
            MDList:
                id: chat_list
                padding: 10
                spacing: 5

        MDBoxLayout:
            orientation: "horizontal"
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
                on_release: app.send_message()
'''

class ScreenManagement(MDScreenManager):
    pass

class HomeScreen(MDScreen):
    pass

class Messages(MDScreen):
    pass

class MyApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def add_contact(self):
        contact = OneLineAvatarListItem(text="Novo Contato")
        contact.add_widget(ImageLeftWidget(source="assets/cogwheel (1).png"))
        self.root.get_screen("home").ids.contacts_list.add_widget(contact)

    def send_message(self):
        chat_list = self.root.get_screen("messages").ids.chat_list
        message_input = self.root.get_screen("messages").ids.message_input
        if message_input.text:
            chat_list.add_widget(OneLineAvatarListItem(text=message_input.text))
            message_input.text = ""

if __name__ == '__main__':
    MyApp().run()