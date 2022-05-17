from kivy.app import App

from kivy.uix.boxlayout import BoxLayout

class Formulario(BoxLayout):
    pass

class MyApp(App):
    def build(self):
        return Formulario()


MyApp().run()