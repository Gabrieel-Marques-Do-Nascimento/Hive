from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from kivymd.app import  MDApp
from extend_base import BaseApp, BaseScreen

Config_KV = """
#ScreenManager:
#    ConfigScreen:

<ConfigScreen>:
    name: "config"

    MDBoxLayout:
        orientation: "vertical"

        MDTopAppBar:
            title: "Configurações"
            left_action_items: [["arrow-left", lambda x: app.go_back()]]

        ScrollView:
            MDBoxLayout:
                orientation: "vertical"
                padding: "20dp"
                spacing: "20dp"
                size_hint_y: None
                height: self.minimum_height

                MDLabel:
                    text: "Ajustes Gerais"
                    bold: True
                    theme_text_color: "Primary"

                MDSeparator:

                MDSwitch:
                    id: dark_mode
                    text: "Modo Escuro"
                    pos_hint: {"center_x": 0.5}
                    on_active: app.toggle_theme(self)

                MDSeparator:

                MDRectangleFlatButton:
                    text: "Redefinir Configurações"
                    pos_hint: {"center_x": 0.5}
                    on_release: app.reset_settings()
"""

class Config():
	name = "config"

config = Config()

class ConfigScreen(BaseScreen):
    pass

class ConfigApp(BaseApp):
    def build(self):
        self.app_builder.load_string(Config_KV)
        self.sm.add_widget(ConfigScreen())
        return self.sm

    def go_back(self):
        print("Voltar para a tela anterior")

    def toggle_theme(self, switch):
        if switch.active:
            self.theme_cls.theme_style = "Dark"
        else:
            self.theme_cls.theme_style = "Light"

    def reset_settings(self):
        print("Configurações redefinidas para padrão")

if __name__ == "__main__":
    ConfigApp().run()