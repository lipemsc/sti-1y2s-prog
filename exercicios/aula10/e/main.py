from kivy.app import App
from kivy.config import Config
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class EApp(App):
    def build(self):
        return MyLayout()

class MyLayout(BoxLayout):
    def switch_text(self):
        tmp = self.ids.textbox.text
        self.ids.textbox.text = self.ids.textbox2.text
        self.ids.textbox2.text = tmp


EApp().run()