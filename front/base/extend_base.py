"""
modulo padrao de  criacao de telas
"""

from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.screenmanager import ScreenManager
from utils import  BaseName
KV = """

"""
class Base(BaseName):
	name = "home"
base = Base()

class BaseScreen(MDScreen):
    pass



class BaseApp(MDApp):
    app_builder = Builder
    sm = ScreenManager()
    home = base
    
    def build(self):
        return self.app_builder.load_string(KV)

    def fechar_app(self):
        """ fecha o aplicativo"""
        self.stop()  # Fecha o aplicativo
        
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
        self.root.transition.direction = self.home.down
        self.root.current = self.home.name

if __name__ == "__main__":
    BaseApp().run()