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

    MAX_GAMES = 3

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.game = 0
        self.score = []
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

    def savescore(self):
        try:
            self.score.append(self.galo.winner)
        except AttributeError:
            print("no previous galo object, continuing")

    def newgame(self):
        self.galo = Galo()
        self.game += 1
        print(self.score)

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
            
            self.savescore()
            # from here to line 91 creates a popup that shows once each game ends
            winpopup = Popup(
                title=f"Jogador {self.galo.winner} ganhou!",
                size=(200, 200),
                size_hint=(None,None),
                auto_dismiss=False)
            winpopup_btn = Button(text="Continuar", size_hint_y = .3)
            winpopup_btn.bind(on_release=winpopup.dismiss)
            winpopup_bl = BoxLayout(orientation="vertical")
            winpopup_lbl = Label(text=f"Jogador 1: {self.score.count(1)}\nJogador 2: {self.score.count(2)}")
            winpopup_bl.add_widget(winpopup_lbl)
            if self.MAX_GAMES <= self.game:
                winpopup.title = "Fim do jogo"
                if self.score.count(1) >= self.score.count(2):
                    winner = 1
                else:
                    winner = 2
                winpopup_lbl.text = f"\nParabéns jogador {winner}\n" + winpopup_lbl.text
                
            winpopup_bl.add_widget(winpopup_btn)
            winpopup.content = winpopup_bl
            winpopup.bind(on_dismiss=self.reset)
            winpopup.open()
            #print(self.ids.lbl0)
    
    def reset(self, instance):
        if self.game < self.MAX_GAMES:
            for btn in self.posbtns:
                    btn.disabled = False
                    btn.text = ""
            self.newgame()
            self.show_current_player()

GaloApp().run()