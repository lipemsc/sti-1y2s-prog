from kivy.app import App
from kivy.config import Config
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.button import Label
from kivy.uix.popup import Popup

import requests, json


class TorneiosLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def update(self):
        req = requests.get(f"http://localhost:8080/torneios/{int(self.ids.tb_id.text)}")
        if req.status_code == 200:
            torneios = json.loads(req.text)
            print(torneios)
        
        