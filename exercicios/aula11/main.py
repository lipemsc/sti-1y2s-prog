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
        for btn_no in range(len(self.posbtns)): 
            if instance == self.posbtns[btn_no]:
                playno = btn_no
        player = self.galo.player
        #print(player)
        if self.galo.play(playno):
            if player == 1:
                instance.text = "X"
            elif player == 2:
                instance.text = "O"
        self.check_win()

    def check_win(self):
        print(self.galo.winner)

GaloApp().run()