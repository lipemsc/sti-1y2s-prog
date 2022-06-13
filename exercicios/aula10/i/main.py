from kivy.app import App
from kivy.config import Config
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox


class IApp(App):
    def build(self):
        return MyLayout()

class MyLayout(BoxLayout):
    def change_value(self):
        if self.ids.cbox0.active:
            self.ids.tbox0.text = str(int(self.ids.tbox0.text) + 1)
        else:
            self.ids.tbox0.text = str(int(self.ids.tbox0.text) - 1)


IApp().run()