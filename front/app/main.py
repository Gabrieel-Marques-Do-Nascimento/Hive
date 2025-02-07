from kivymd.app import  MDApp
from kivymd.uix.screenmanager import  ScreenManager
from kivymd.uix.list import  ThreeLineAvatarListItem, TwoLineListItem
from kivymd.uix.screen import  MDScreen
from kivy.lang import  Builder
#from kivymd.font_definitions import theme_font_styles
from kivymd.uix.label import  MDLabel
from kivymd.font_definitions import theme_font_styles
#from kivymd.uix.list import ImageLeftWidget 

from functools import  partial
from datetime import  datetime

# testes
from app_testes.loggeuer_teste_init import ActivationTime
from app_testes.users_teste import users10
users = users10


# pass logguer time active app
active = ActivationTime()
active.file_name("Hive-messages-app", filetimename=True)
active.clear()
# primeiro para iniciar 
active.debug(logg=False)

#===========================================
#=====°===°====   BackEnd-API    =======°=°=====
#===========================================
import  socketio

sio = socketio.AsyncClient()

#@sio.event
#def connect():
#	print("connected")
#	sio.emit("registrar_usuario", {"id":4})
#sio.connect("http://localhost:5000")
#sio.wait()


#===========================================
#=====°===°=====     FrontEnd     =======°=°======
#===========================================

KV = """

	
<Contact>:
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
			
		ScrollView:
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
			title: "HIVE"
			elevation: 4
			pos_hint: {"top":1}
			id: topbar			
			left_action_items: [["arrow-collapse-left", lambda x: app.callback()]]
			icon: "git"
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
                on_release: root.send_message()
"""

class Contact(ThreeLineAvatarListItem):
    def __init__(self, user, **kwargs):
        super().__init__(**kwargs)
        active.debug("Contact-item")
        #self.add_widget(ImageLeftWidget(source="assets/cogwheel (1).png"))
        self.add_widget(MDLabel(text=user["name"], font_size="20sp",font_style=theme_font_styles[6], pos_hint= {"x": .2, "center_y": .5}))
        self.add_widget(MDLabel(text=user["message"],font_style=theme_font_styles[7], font_size="16sp", pos_hint= {"x": .5, "center_y": .75}))
        self.add_widget(MDLabel(text=user["online"], font_size="14sp",font_style=theme_font_styles[7] , pos_hint= {"x": .8, "center_y": .75}))
        

class ScreenManagement(ScreenManager):
     """
     Gerenciador de telas
     """
     def __init__(self,**kwargs):
     	super().__init__(**kwargs)
     	active.debug("ScreenManagement")
     	Builder.load_string(KV)


     

class HomeScreen(MDScreen):
	def __init__(self,**kwargs):
		super().__init__(**kwargs)
		active.debug("HomeScreen")
		self.name = 'home'
		
	
	def on_kv_post(self, base_widget):
		"""
		espera o arquivo kv ser caregado antes de executar o cofigo abaixo
		"""
		active.debug("HomeScreen-on_kv_post")
		self.load_contacts()

	def callback_screen(self,instace, user ):
		"""
		function calbeck:
		
		args:
			*args: recebe o parametros nao nomeados retorna uma lista,
			**kwargs: recebe parametros nomeados e retorna um dict
		"""
		userdate = user["user"]
		screen =self.parent.get_screen("messages")
		screen.ids.topbar.title = userdate["name"]
		self.manager.transition.direction = "up"
		self.manager.current = "messages"

	def create_contacts(self, user):
		active.debug("HomeScreen-create_contacts")
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
		preview = ""
		online = ""
		name = ""
		if users:
			if hasattr(self.ids, "contacts_list"):
				self.ids.contacts_list.clear_widgets()
			for user in users:
				self.create_contacts(user=user)
			active.debug("HomeScreen-load_contacts")
			
		

class Messages(MDScreen):
    
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        active.debug(msg="Messages")
        self.messages = []
        self.title = "HIVE"
        self.name = 'messages'
        
        
    def send_message(self):
        message_text = self.ids.message_input.text.strip()
        if message_text:
            # envia a message ao socketio
            sio.emit('enviar_mensagem', {"id":2, "message":message_text})
            #----------------------------------------
            
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
		active.debug(msg="HiveApp")
		
		
        
	
	def build(self):
		active.debug(msg="HiveApp-build")
		self.start_socket()
		# Create the screen manager
		sm = ScreenManager()
		sm.add_widget(HomeScreen())
		sm.add_widget(Messages())
	
	def callback(self):
		#self.root.transition.direction = "down"
		self.root.transition.direction = "down"
		self.root.current = "home"
	
	async def connect_socket(self):
		try:
			#print("socket conectado")
			await sio.connect("http://127.0.0.1:5000")
			await sio.emit('registrar_usuario', {'usuario_id': 'usuario123', "id": 1})
			#await sio.wait()
			await sio.on("enveto")
		
		except Exception as erro:
			pass
			
	def start_socket(self):
		from threading import Thread
		import  asyncio
		active.debug(msg="HiveApp-start_socket")
		def run():
			
			asyncio.run(self.connect_socket())
		Thread(target=run,daemon=True).start()



@sio.event
def connect():
	pass
	
	


if __name__ == "__main__":
	HiveApp().run()
	active.debug(msg="__main__")
	active.debug(msg="the and")