from kivy.app import App

from kivy.uix.boxlayout import BoxLayout

class Formulario(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.lista_pessoas = [
            Pessoa(nome="aaa", email="aaaa", tem_carro = True),
            Pessoa(nome="bbb", email="bbbb", tem_carro = False),
        ]
        self.idx = 0

    def clique(self, bt):
        if bt == "novo":
            pessoa = Pessoa("?", "?", False)
            self.lista_pessoas.append(pessoa)
            self.idx = len(self.lista_pessoas) - 1
        elif bt == "apaga":
            print(2)
        elif bt == "grava":
            pessoa = self.lista_pessoas[self.idx]
            pessoa.nome = self.ids.nome.text
            pessoa.email = self.ids.email.text
            pessoa.tem_carro = self.ids.tem_carro.active
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
    def __init__(self, nome, email, tem_carro):
        self.email = email
        self.nome = nome
        self.tem_carro = tem_carro


class MyApp(App):
    def build(self):
        return Formulario()

        

MyApp().run()