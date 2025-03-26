from database import  Tabels

from contact import  Messages, message, Message_KV
from socket_confg import  sio
from home import  HomeApp, HomeScreen, home, Home_KV
from loader import LoaderApp, LoaderScreen, loader, KV_Loader
from new_contact import ContactApp, ContactScreen, addcontact, Add_Contact_KV
from login import  LoginApp, LoginScreen, Login_KV, login
from config import  ConfigApp, ConfigScreen, config,Config_KV




tabels = Tabels()


# class  MyApp(MDApp): # referente ao arquivo .kv

class HiveApp(LoaderApp, ContactApp, LoginApp, ConfigApp):
    def build(self):
        from kivy.clock import Clock
        sm = self.sm
        self.app_builder.load_string(KV_Loader)
        self.sm.add_widget(LoaderScreen(name=loader.name)) 
        
        self.app_builder.load_string(Home_KV)
        self.sm.add_widget(HomeScreen(name=home.name))
        # Troca de tela após 3 segundos
        
             
        self.app_builder.load_string(Add_Contact_KV)
        self.sm.add_widget(ContactScreen(name=addcontact.name))
        self.app_builder.load_string(Login_KV)
        self.sm.add_widget(LoginScreen(name=login.name))
        self.app_builder.load_string(Config_KV)
        self.sm.add_widget(ConfigScreen(name=config.name))
        self.app_builder.load_string(Message_KV)
        self.sm.add_widget(Messages(name=message.name))
        
        # retorna uma lista 
        #self.show_dialog("login", str(type(tabels.loginDB.all(tabels.login))))
        token = tabels.loginDB.all(tabels.login)
        if token:
        	Clock.schedule_once(self.switch_to_home, 5)
        	return sm
        
        return sm

if __name__ == "__main__":
	HiveApp().run()