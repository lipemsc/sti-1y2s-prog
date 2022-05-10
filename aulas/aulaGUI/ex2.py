# aplicação muito simples para gerar apenas uma janela vazia

# importar o pacote do kivy
from kivy.app import App
# Importar uma "label" (ou etiqueta). Basicamente uma simples área de texto.
from kivy.uix.label import Label 

# adicionar uma class que tem como base a class App do Kivy
class MyApp(App):
    # definir o método build que vai controlar o que vai aparecer na janela
    def build(self):
        return Label(text="Olá o SLB é o maior") # isso foi mesmo o que o prof escreveu



MyApp().run() # gerar a janela
