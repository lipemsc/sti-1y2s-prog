from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.checkbox import CheckBox
from kivy.uix.spinner import Spinner
from kivy.uix.button import Button


pessoas = [
            {"nome": "ze", "email": "ze@ualg.pt"},
            {"nome": "quim", "email": "quim@ualg.pt"},
        ]

class MyScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        grid = GridLayout(cols=2)
        self.add_widget(grid)
        self.orientation = "vertical"
        
        grid.add_widget(Label(text="Nome"))
        self.txtnome = TextInput(multiline=False)
        grid.add_widget(self.txtnome)

        grid.add_widget(Label(text="Email"))
        self.txtemail = TextInput(multiline=False)
        grid.add_widget(self.txtemail)

        grid.add_widget(Label(text="Tem carro"))
        self.cbcarro = CheckBox()
        grid.add_widget(self.cbcarro)

        grid.add_widget(Label(text="Genero"))
        grelhagenero = GridLayout(cols=2)
        grid.add_widget(grelhagenero)

        grelhagenero.add_widget(Label(text="Masculino"))
        grelhagenero.add_widget(Label(text="Feminino"))

        self.rbgenmasc = CheckBox(group="genero")
        self.rbgenfem = CheckBox(group="genero")

        grelhagenero.add_widget(self.rbgenmasc)
        grelhagenero.add_widget(self.rbgenfem)

        grid.add_widget(Label(text="Pais"))
        self.spais = Spinner(text="Escolha os paises", values=["Portugal", "Espanha"])
        grid.add_widget(self.spais)

        grelhabotoes = GridLayout(cols=5)
        self.add_widget(grelhabotoes)

        self.bnovo = Button(text="Novo")
        grelhabotoes.add_widget(self.bnovo)
        self.bnovo.bind(on_release=self.executa)

        self.bapagar = Button(text="Apagar")
        grelhabotoes.add_widget(self.bapagar)
        self.bapagar.bind(on_release=self.executa)

        self.bgravar = Button(text="Gravar")
        grelhabotoes.add_widget(self.bgravar)
        self.bgravar.bind(on_release=self.executa)

        self.banterior = Button(text="Anterior")
        grelhabotoes.add_widget(self.banterior)
        self.banterior.bind(on_release=self.executa)

        self.bproximo = Button(text="Próximo")
        grelhabotoes.add_widget(self.bproximo)
        self.bproximo.bind(on_release=self.executa)

        self.idx = 0

        self.preencherform()

    def executa(self, instance):
        if instance == self.bproximo:
            self.idx = (self.idx + 1) % len(pessoas)
        elif instance == self.banterior:
            self.idx = (self.idx - 1) % len(pessoas)
        elif instance == self.bnovo:
            pessoas.append({"nome": "?", "email": "?"})
            self.idx = -1
        elif instance == self.bgravar:
            pessoa = pessoas[self.idx]
            pessoa["nome"] = self.txtnome.text
            pessoa["email"] = self.txtemail.text
        elif instance == self.bapagar:
            del pessoas[self.idx]
            self.idx = min(self.idx, len(pessoas) -1)
        self.preencherform()

#    def proximo(self, instance):
#        self.idx = (self.idx + 1) % len(pessoas)
#        self.preencherform()
#
#    def anterior(self, instance):
#        self.idx = (self.idx - 1) % len(pessoas)
#        self.preencherform()

    def preencherform(self):
        pessoa = pessoas[self.idx]
        self.txtnome.text = pessoa["nome"]
        self.txtemail.text = pessoa["email"]


class MyApp(App):
    def build(self):
        return MyScreen()

MyApp().run()
