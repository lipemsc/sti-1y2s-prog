# Continuação da aplicação anterior que mas com uma label, um textinput e dois botões
# encapsulados num boxlayout

# _________________________________________________________
# |  Label          | TextInput:       | BoxLayout com 2bt |
# |                 | ________________ | __________________|
# |                 | | Nome           | |                 |
# |                 | |                | |                 |
# |                 | |                | |       Ok        |
# |                 | |                | |                 |
# |  Nome           | |                | |_________________|
# |                 | |                | |                 |
# |                 | |                | |                 |
# |                 | |                | |    Cancelar     |
# |                 | |                | |                 |
# |                 | |                | |_________________|
# |                 | |                |                   |
# ---------------------------------------------------------


# Importar o pacote do kivy
from kivy.app import App

# Importar uma "label", um "textinput" e um "button"
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

# Importar o GridLayout do Kivy.
# Permite organizar os conteúdos como uma grelha (ou tabela).
# Grid = Grelha (semelhante a uma tabela)
from kivy.uix.gridlayout import GridLayout

# Importa o boxlayout
# O boxlayout serve para "encapsular" vários elementos num só
from kivy.uix.boxlayout import BoxLayout

# Adiciona uma class LoginScreen que tem como base o GridLayout da linha 11
class LoginScreen(GridLayout):
    # define a função de inicialização
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        #define o número de colunas da Grid
        self.cols = 3
        # adiciona uma label à 1ª coluna da Grid 
        label1 = Label(text="Nome")
        self.add_widget(label1)

        # adiciona uma textinput à 2ª coluna da Grid
        textinput1 = TextInput(text="Nome")
        self.add_widget(textinput1)

        # adiciona uma boxlayout à 3ª coluna da Grid
        boxlayout = BoxLayout(orientation="vertical")
        self.add_widget(boxlayout)

        # adiciona um botão ao boxlayout
        buttonok = Button(text="Ok")
        boxlayout.add_widget(buttonok)

        # adiciona um segundo botão ao mesmo boxlayout
        buttoncancel = Button(text="Cancelar")
        boxlayout.add_widget(buttoncancel)


# adicionar uma class que tem como base a class App do Kivy
class MyApp(App):
    # definir o método build que vai controlar o que vai aparecer na janela
    def build(self):
        # adiciona o conteúdo do LoginScreen para a janela
        return LoginScreen()


MyApp().run() # gerar a janela
