from kivymd.uix.list import ThreeLineAvatarListItem, TwoLineListItem
from kivymd.font_definitions import theme_font_styles
from kivymd.uix.label import MDLabel


class USER:
    def __init__(self, user):
        self.user: dict = user
        self.id: int = user["contact"]
        self.name: str = user["name"]
        self.update: str = user["update"]
        self.null: str = "null"
        self.user_id: int = user["id"]


class BaseName:
	name = "base"
	up = "up"
	down = "down"
	left = "left"
	right = "right"


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
     