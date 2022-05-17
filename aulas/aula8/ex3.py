# Aplicação simples que utiliza o GridLayout para apresentar uma Label na janela

# Importar o pacote do kivy
from kivy.app import App

# Importar uma "label" (ou etiqueta). Basicamente uma simples área de texto.
from kivy.uix.label import Label 

# Importar o GridLayout do Kivy.
# Permite organizar os conteúdos como uma grelha (ou tabela).
# Grid = Grelha (semelhante a uma tabela)
from kivy.uix.gridlayout import GridLayout

# Adiciona uma class LoginScreen que tem como base o GridLayout da linha 11
class LoginScreen(GridLayout):
    # define a função de inicialização
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        #define o número de colunas da Grid
        self.cols = 2
        # adiciona uma label à Grid
        label1 = Label(text="Nome")
        self.add_widget(label1)


# adicionar uma class que tem como base a class App do Kivy
class MyApp(App):
    # definir o método build que vai controlar o que vai aparecer na janela
    def build(self):
        # adiciona o conteúdo do LoginScreen para a janela
        return LoginScreen()


MyApp().run() # gerar a janela
