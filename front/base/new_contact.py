from kivy.lang import Builder
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton

from extend_base import BaseApp, BaseScreen, BaseName

Add_Contact_KV = """

<ContactScreen>:
    name: "add_contact"

    MDBoxLayout:
        orientation: "vertical"
        padding: "20dp"
        spacing: "10dp"

        MDTopAppBar:
            title: "Adicionar Contato"
            left_action_items: [["arrow-left", lambda x: app.fechar_app()]]

        ScrollView:
            MDBoxLayout:
                orientation: "vertical"
                spacing: "20dp"
                size_hint_y: None
                height: self.minimum_height
                padding: "20dp"

                MDTextField:
                    id: contact_name
                    hint_text: "Nome do Contato"
                    mode: "fill"

                MDTextField:
                    id: contact_id
                    hint_text: "ID do Contato"
                    mode: "fill"
                    input_filter: "int"

                MDRaisedButton:
                    text: "Adicionar Contato"
                    pos_hint: {"center_x": 0.5}
                    on_release: app.add_contact()

"""


class ADD(BaseName):
    name = "add_contact"


addcontact = ADD()


class ContactScreen(BaseScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class ContactApp(BaseApp):
    def build(self):
        self.app_builder.load_string(Add_Contact_KV)
        self.sm.add_widget(ContactScreen(name=addcontact.name))
        return self.sm

    def add_contact(self):
        name = self.root.get_screen(addcontact.name).ids.contact_name.text
        contact_id = self.root.get_screen(addcontact.name).ids.contact_id.text

        if name and contact_id:
            self.show_dialog("Contato adicionado!",
                             f"Nome: {name}\nID: {contact_id}")
        else:
            self.show_dialog("Erro", "Preencha todos os campos!")

#    def show_dialog(self, title, text):
#        dialog = MDDialog(
#            title=title,
#            text=text,
#            buttons=[MDFlatButton(text="OK", on_release=lambda x: dialog.dismiss())],
#        )
#        dialog.open()


if __name__ == "__main__":
    ContactApp().run()
