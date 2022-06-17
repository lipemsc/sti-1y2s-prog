from galo import Galo
from kivy.app import App
from kivy.config import Config
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.button import Label


class GaloApp(App):
    def build(self):
        return GaloLayout()

class GaloLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.galo = Galo()
        self.lbl0 = Label(text="Jogador 1")
        self.lbl1 = Label(text="Jogador 2")
        self.ids.bl0.add_widget(self.lbl0)
        self.ids.bl0.add_widget(self.lbl1)
        self.posbtns = []
        for i in range(9):
            self.posbtns.append(Button())
            self.posbtns[i].bind(on_release=self.play)
            self.ids.gamegrid.add_widget(self.posbtns[i])
        self.show_current_player()

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
        self.show_current_player()
        self.check_win()

    def show_current_player(self):
        if self.galo.player == 1:
            self.lbl0.color = [1,1,1,1]
            self.lbl1.color = [1,1,1,.3]
        else:
            self.lbl0.color = [1,1,1,.3]
            self.lbl1.color = [1,1,1,1]

    def check_win(self):
        if self.galo.winner != 0:
            self.ids.bl0.remove_widget(self.lbl0)
            self.ids.bl0.remove_widget(self.lbl1)
            self.lblwinner = Label(text=f"Jogador {self.galo.winner} ganhou!")
            self.ids.bl0.add_widget(self.lblwinner)
            for btn in self.posbtns:
                btn.disabled = True
            #print(self.ids.lbl0)

GaloApp().run()