from galo import Galo
from kivy.app import App
from kivy.config import Config
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.button import Label
from kivy.uix.popup import Popup

class GaloApp(App):
    def build(self):
        return GaloLayout()

class GaloLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.game = 0
        self.lbl0 = Label(text="Jogador 1")
        self.lbl1 = Label(text="Jogador 2")
        self.ids.bl0.add_widget(self.lbl0)
        self.ids.bl0.add_widget(self.lbl1)
        self.posbtns = []
        for i in range(9):
            self.posbtns.append(Button())
            self.posbtns[i].bind(on_release=self.play)
            self.ids.gamegrid.add_widget(self.posbtns[i])
        self.newgame()
        self.show_current_player()

    def newgame(self):
        self.galo = Galo()
        self.game += 1

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
            for btn in self.posbtns:
                btn.disabled = True
            winpopup = Popup(
                title=f"Jogador {self.galo.winner} ganhou!",
                size=(200, 100),
                size_hint=(None,None),
                auto_dismiss=False)
            winpopup_btn = Button(text="Continuar")
            winpopup_btn.bind(on_release=winpopup.dismiss)
            winpopup_bl = BoxLayout(orientation="vertical")
            winpopup_bl.add_widget(Label(text="score"))
            winpopup_bl.add_widget(winpopup_btn)
            winpopup.add_widget(winpopup_bl)
            winpopup.bind(on_dismiss=self.reset)
            winpopup.open()
            #print(self.ids.lbl0)
    
    def reset(self, instance):
        for btn in self.posbtns:
                btn.disabled = False
                btn.text = ""

GaloApp().run()