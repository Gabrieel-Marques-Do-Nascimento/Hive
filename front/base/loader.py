from kivy.lang import Builder
from kivy.clock import Clock
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from extend_base import BaseApp, BaseScreen, BaseName

KV_Loader = """

<LoaderScreen>:
    name: "loader"

    MDBoxLayout:
        orientation: "vertical"
        spacing: "10dp"
        padding: "20dp"
        pos_hint: {"center_x": 0.5, "center_y": 0.5}

        MDIcon:
            icon: "android"  # Substitua pelo ícone do seu app
            halign: "center"
            font_size: "100dp"

        MDLabel:
            text: "Carregando..."
            halign: "center"
            theme_text_color: "Secondary"

        MDSpinner:
            size_hint: None, None
            size: "48dp", "48dp"
            pos_hint: {"center_x": 0.5}
            active: True

<HomeScreenTeste>:
    name: "home"

    MDBoxLayout:
        orientation: "vertical"
        MDTopAppBar:
            title: "Home"
        
        MDLabel:
            text: "Bem-vindo ao App!"
            halign: "center"
"""


class Loader(BaseName):
    name = "loader"


loader = Loader()


class LoaderScreen(MDScreen):
    pass


class HomeScreenTeste(MDScreen):
    pass


class LoaderApp(BaseApp):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def build(self):
        self.app_builder.load_string(KV_Loader)
        self.sm.add_widget(LoaderScreen(name="loader"))
        self.sm.add_widget(HomeScreenTeste(name="home"))

        # Troca de tela após 3 segundos
        Clock.schedule_once(self.switch_to_home, 3)
        return self.sm

    def switch_to_home(self, dt):
        self.sm.current = self.home.name


if __name__ == "__main__":
    LoaderApp().run()
