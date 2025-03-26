from kivymd.uix.screen import MDScreen

from database import UserDB, USER
from utils import USER, BaseName
from contact import message
from new_contact import  addcontact as add
from extend_base import  BaseApp
from kivymd.uix.list import ThreeLineAvatarListItem, TwoLineListItem
from kivymd.font_definitions import theme_font_styles
from kivymd.uix.label import MDLabel


users1 = [{"name": "Gabriel marques do nascimento",
           "contact": "1",
           "id": "2",
           "update": "8:00",
           }]
users = users1

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


Home_KV = """
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

"""





class Home(BaseName):
	name = "home"

home = Home()

class HomeScreen(MDScreen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.name = home.name

    def on_enter(self):
     

        self.load_contacts()

    def callback_screen(self, instace, user: USER):
        userdate = user
        screen = self.parent.get_screen(message.name)
        screen.ids.topbar.title = userdate.name
        self.manager.transition.direction = "up"
        self.manager.current = message.name

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
        screen = self.parent.get_screen(add.name)
        self.manager.transition.direction = add.up
        self.manager.current = add.name
    	

class HomeApp(BaseApp):
    def build(self):
        self.app_builder.load_string(Home_KV)
        sm = self.sm
        sm.add_widget(HomeScreen())
        return sm

if __name__ == "__main__":
    HomeApp().run()