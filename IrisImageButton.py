from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image

class IrisImageButton(ButtonBehavior,Image):
    def on_press(self):
        print("IrisImageButton - on_pressed(),")