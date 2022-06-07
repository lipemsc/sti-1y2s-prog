from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput

class EApp(App):
    def build(self):
        return Layout()

class Layout(BoxLayout):
    def switch_text(self):
        pass


EApp().run()