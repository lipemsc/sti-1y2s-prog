from kivy.app import App

from kivy.uix.boxlayout import BoxLayout

class Formulario(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.lista_pessoas = [
            Pessoa(nome="aaa", email="aaaa"),
            Pessoa(nome="bbb", email="bbbb"),
        ]
        self.idx = 0

    def clique(self, bt):
        if bt == "novo":
            print(1)
        elif bt == "apaga":
            print(2)
        elif bt == "anterior":
            self.idx = (self.idx - 1) % len(self.lista_pessoas)
        elif bt == "proximo":
            self.idx = (self.idx + 1) % len(self.lista_pessoas)
        
        self.preenche_formulario()

    def preenche_formulario(self):
        pessoa = self.lista_pessoas[self.idx]
        self.ids.nome.text = pessoa.nome
        self.ids.email.text = pessoa.email
    

class Pessoa:
    def __init__(self,nome,email):
        self.email = email
        self.nome = nome


class MyApp(App):
    def build(self):
        return Formulario()

        

MyApp().run()