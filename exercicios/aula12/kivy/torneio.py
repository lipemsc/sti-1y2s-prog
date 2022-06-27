from kivy.app import App
from kivy.config import Config
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.button import Label
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView

import requests, json


class TorneiosLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bl = BoxLayout(
            orientation="vertical",
            padding=(10, 10),
            
        )
        self.ids.scroller.add_widget(self.bl)
        self.update()
    
    def update(self):
        torneios = json.loads(requests.get("http://localhost:8080/torneios/").text)
        for torneio in torneios:
            self.bl.add_widget(Button(
                size_hint_y=40,
                text=torneio["nome"]
            ))