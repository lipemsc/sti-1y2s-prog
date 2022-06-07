from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput

class BApp(App):
    def build(self):
        return Layout()

class Layout(BoxLayout):
    def update_text(self):
        self.ids.textbox2.text = self.ids.textbox.text[::-1]


BApp().run()