from kivy.app import App
from kivy.config import Config
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.button import Label
from kivy.uix.popup import Popup
from kivy.lang.builder import Builder
from dateutil import parser
from datetime import datetime

import requests, json

Builder.load_file("torneio.kv")

class TorneioLayout(BoxLayout):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    id = -1

    def get(self):
        self.id = int(self.ids.tb_id.text)
        req = requests.get(f"http://localhost:8080/torneios/{self.id}")
        if req.status_code == 200:
            torneio = json.loads(req.text)
            data_inicio = parser.parse(torneio["data_inicio"])
            data_fim = parser.parse(torneio["data_fim"])
            self.ids.tb_nome.text = torneio["nome"]
            self.ids.tb_dt_fim.text = data_fim.strftime("%Y-%m-%d")
            self.ids.tb_dt_inicio.text = data_inicio.strftime("%Y-%m-%d")
            self.ids.tb_local.text = torneio["local"]
            self.ids.tb_nome.disabled = False
            self.ids.tb_dt_fim.disabled = False
            self.ids.tb_dt_inicio.disabled = False
            self.ids.tb_local.disabled = False
        else:
            self.ids.tb_nome.text = ""
            self.ids.tb_dt_fim.text = ""
            self.ids.tb_dt_inicio.text = ""
            self.ids.tb_local.text = ""
            # self.ids.tb_local.disabled = True
            # self.ids.tb_nome.disabled = True
            # self.ids.tb_dt_fim.disabled = True
            # self.ids.tb_dt_inicio.disabled = True


    def new(self):
        pass
    def update(self):
        upload = {}
        upload["nome"] = self.ids.tb_nome.text
        upload["data_fim"] = self.ids.tb_dt_fim.text
        upload["data_inicio"] = self.ids.tb_dt_inicio.text
        upload["local"] = self.ids.tb_local.text
        print(upload)
        response = requests.put(
            f"http://localhost:8080/torneios/{self.id}",
            data=json.dumps(upload),
            headers={"Content-Type": "application/json"})
        self.get()

    def delete(self):
        requests.delete(f"http://localhost:8080/torneios/{self.id}")
        self.get()