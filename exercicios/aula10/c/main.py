from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput

class CApp(App):
    def build(self):
        return Layout()

class Layout(BoxLayout):
    def check_text(self):
        if self.ids.textbox2.text == self.ids.textbox.text[::-1]:
            self.ids.lbl.text = "Textos inversos"
            self.ids.lbl.color = [.2,1,.2,1]
        else:
            self.ids.lbl.text = "Textos não inversos"
            self.ids.lbl.color = [1,.2,.2,.7]


CApp().run()