from datetime import datetime
from kivymd.uix.screen import MDScreen
from database import UserDB, USER
from socket_confg import  sio
from kivymd.uix.list import ThreeLineAvatarListItem, TwoLineListItem

from utils import  BaseName
from extend_base import  BaseApp, base, BaseScreen



Message_KV = """
<Messages>:
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

"""


class Message(BaseName):
	name= "messages"
	
message = Message()

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

class MessagesApp(BaseApp):
    def build(self):
        self.app_builder.load_string(Message_KV)
        self.sm.add_widget(Messages())
        return self.sm

if __name__ == "__main__":
    MessagesApp().run()