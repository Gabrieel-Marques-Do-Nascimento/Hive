from kivymd.app import  MDApp
from kivymd.uix.screenmanager import  ScreenManager
from kivymd.uix.list import  OneLineAvatarIconListItem, ThreeLineAvatarListItem
from kivymd.uix.screen import  MDScreen
from kivy.lang import  Builder
from kivymd.font_definitions import theme_font_styles
from kivymd.uix.label import  MDLabel
from kivymd.font_definitions import theme_font_styles





from app_testes.users_teste import users10

users = users10



#from  kivymd.uix.scrollview import  ScrollView
KV = """
<ScreenManagement>:
	HomeScreen:
	Messages:

<Contact>:
    
    ImageLeftWidget:
        source: "assets/cogwheel (1).png"	


<HomeScreen>:
	MDBoxLayout:
		orientation: "vertical"
		
		MDTopAppBar:
			title: "HIVE"
			elevation: 4
			pos_hint: {"top":1}
			
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
		    orientation: "vertical"  # Para centralizar mais facilmente
		
		    MDIconButton:
		        icon: "plus"
		        pos_hint: {"center_x": 0.5}  # Centraliza horizontalmente
				
			

"""

class Contact(ThreeLineAvatarListItem):
	pass


class ScreenManagement(ScreenManager):
     """
     Gerenciador de telas
     """
     pass
     
     
     
     

class HomeScreen(MDScreen):
	def on_kv_post(self, base_widget):
		"""
		espera o arquivo kv ser caregado antes de executar o cofigo abaixo
		"""
		self.load_contacts()
		

	
	def load_contacts(self):
		"""
		add os elementos da lista aos contatos
		"""
		preview = ""
		online = ""
		name = ""
		if users:
			for user in users:
				user_item = Contact()
				
				# Adicionando labels personalizados
				user_item.add_widget(MDLabel(text=user["name"], font_size="20sp",font_style=theme_font_styles[6], pos_hint= {"x": .2, "center_y": .5}))
				user_item.add_widget(MDLabel(text=user["message"],font_style=theme_font_styles[7], font_size="16sp", pos_hint= {"x": .5, "center_y": .75}))
				user_item.add_widget(MDLabel(text=user["online"], font_size="14sp",font_style=theme_font_styles[7] , pos_hint= {"x": .8, "center_y": .75}))
				self.ids.contacts_list.add_widget(user_item)
		

class Messages(MDScreen):
	pass


#class  MyApp(MDApp): # referente ao arquivo .kv
class  HiveApp(MDApp):
	"""
	class principal
	"""
	def build(self):
		Builder.load_string(KV)
		return ScreenManagement()


if __name__ == "__main__":
	HiveApp().run()