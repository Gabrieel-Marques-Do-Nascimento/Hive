from kivymd.app import  MDApp
from kivymd.uix.screenmanager import  ScreenManager
from kivymd.uix.list import  OneLineAvatarIconListItem, ThreeLineAvatarListItem, TwoLineListItem
from kivymd.uix.screen import  MDScreen
from kivy.lang import  Builder
from kivymd.font_definitions import theme_font_styles
from kivymd.uix.label import  MDLabel
from kivymd.font_definitions import theme_font_styles


from functools import  partial
from datetime import  datetime


from app_testes.users_teste import users10

users = users10



#from  kivymd.uix.scrollview import  ScrollView
KV = """
<ScreenManagement>:
	id: managerid
	HomeScreen:
		name: "home"
	Messages:
		name: "messages"
	

<Contact>:
    # exemplo, esta fora do contexto do manager gerenciador de telas
    # por isso usei o contexto do app
    #on_press: app.root.current = "messages" 
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





<Messages>:
	name: "messages"
	MDBoxLayout:
		orientation: "vertical"
		
		MDTopAppBar:
			id: topbar
			title: "HIVE"
			elevation: 4
			pos_hint: {"top":1}
			
			left_action_items: [["arrow-collapse-left", lambda x: app.callback()]]
			icon: "git"
			
			
		    

		MDScrollView:
			id: scroll_view2
			
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
			

"""

class Contact(ThreeLineAvatarListItem):
	pass


class ScreenManagement(ScreenManager):
     """
     Gerenciador de telas
     """
     def __init__(self,**kwargs):
     	super().__init__(**kwargs)
     	Builder.load_string(KV)
     
     
sm = ScreenManagement()     
     

class HomeScreen(MDScreen):
	def __init__(self,**kwargs):
		super().__init__(**kwargs)
		
	
	def on_kv_post(self, base_widget):
		"""
		espera o arquivo kv ser caregado antes de executar o cofigo abaixo
		"""
		self.load_contacts()

	def callback_screen(self,*args, **kwargs ):
		"""
		function calbeck:
		
		args:
			*args: recebe o parametros nao nomeados retorna uma lista,
			**kwargs: recebe parametros nomeados e retorna um dict
		"""
		userdate = kwargs["user"]
		ids =self.manager.get_screen("messages").ids
		ids.topbar.title = userdate["name"]
		self.manager.transition.direction = "up"
		self.manager.current = "messages"

	
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
				# criar uma tela de msgs
				user_item.bind(
				on_press=partial(
				self.callback_screen, user=user))
				
				self.ids.contacts_list.add_widget(user_item)
		

class Messages(MDScreen):
    
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.messages = []
        self.title = "HIVE"
        
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
            self.ids.scroll_view2.scroll_to(message_item)



#class  MyApp(MDApp): # referente ao arquivo .kv
class  HiveApp(MDApp):
	"""
	class principal
	"""
	def __init__(self,**kwargs):
		super().__init__(**kwargs)
		self.sm = ScreenManagement()
	
	def build(self):
		return self.sm
	
	def callback(self):
		#self.root.transition.direction = "down"
		self.sm.transition.direction = "down"
		self.sm.current = "home"


if __name__ == "__main__":
	HiveApp().run()