# Exercicio para exemplificar eventos.

# Importar o pacote do kivy
from kivy.app import App

from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

from kivy.uix.gridlayout import GridLayout

class LoginScreen(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.cols = 3

        textinput1 = TextInput(text="Nome", multiline=False)

        # associa o evento "on_text_validate" ao método "on_enter" da classe
        # neste caso o "on_text_validate" executa sempre que o user clica Enter no textinput
        # assim, sempre que o user clica Enter o método on_enter vai ser executado
        textinput1.bind(on_text_validate=self.on_enter)
        
        self.add_widget(textinput1)
        
    # A função on_enter vai mostrar o texto da instancia que o chamou. Neste caso o textinput.
    def on_enter(self, instance):
        print(instance.text)



# adicionar uma class que tem como base a class App do Kivy
class MyApp(App):
    # definir o método build que vai controlar o que vai aparecer na janela
    def build(self):
        # adiciona o conteúdo do LoginScreen para a janela
        return LoginScreen()


MyApp().run() # gerar a janela
