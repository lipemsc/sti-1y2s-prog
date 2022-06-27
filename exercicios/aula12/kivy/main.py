from kivy.app import App
from kivy.config import Config
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.button import Label
from kivy.uix.popup import Popup

from torneio import TorneiosLayout

class TorneiosApp(App):
    def build(self):
        return TorneiosLayout()


TorneiosApp().run()