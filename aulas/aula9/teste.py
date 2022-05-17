from pprint import pprint

from kivy.app import App

from kivy.uix.boxlayout import BoxLayout

class Formulario(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.lista_pessoas = [
            Pessoa(nome="aaaaaa", email="aaaaaaa", tem_carro = True, genero = "M", pais="EN"),
            Pessoa(nome="bbbbbb", email="bbbbbbb", tem_carro = False, genero = "M", pais="PT"),
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
            pessoa.pais = self.ids.sp.text
            pessoa.genero = "M" if self.ids.gen_m.active else "F"
        elif bt == "anterior":
            self.idx = (self.idx - 1) % len(self.lista_pessoas)
        elif bt == "proximo":
            self.idx = (self.idx + 1) % len(self.lista_pessoas)
        pprint(vars(self.lista_pessoas[self.idx]))
        self.preenche_formulario()

    def preenche_formulario(self):
        if len(self.lista_pessoas) >= 0:
            pessoa = self.lista_pessoas[self.idx]
            self.ids.nome.text = pessoa.nome
            self.ids.email.text = pessoa.email
            self.ids.tem_carro.active = pessoa.tem_carro
            self.ids.sp.text = pessoa.pais
            self.ids.gen_m.active = (pessoa.genero == "M")
            self.ids.gen_f.active = not (pessoa.genero == "M")
        else:
            self.ids.nome.disabled = True
            self.ids.email.disabled = True
            self.ids.tem_carro.disabled = True
            self.ids.sp.disabled = True
            self.ids.gen_m.disabled = True
            self.ids.gen_f.disabled = True

    

class Pessoa:
    def __init__(self, nome, email, tem_carro, genero, pais):
        self.email = email
        self.nome = nome
        self.tem_carro = tem_carro
        self.genero = genero
        self.pais = pais


class MyApp(App):
    def build(self):
        return Formulario()

        

MyApp().run()