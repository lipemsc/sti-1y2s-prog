from galo import Galo
from kivy.app import App
from kivy.config import Config
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox

class GaloApp(App):
    def build(self):
        return GaloLayout()

class GaloLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.galo = Galo()
        self.posbtns = []
        for i in range(9):
            self.posbtns.append(Button())
            self.posbtns[i].bind(on_release=self.play)
            self.ids.gamegrid.add_widget(self.posbtns[i])

    def play(self, instance):
        instance.text = "wow"

GaloApp().run()