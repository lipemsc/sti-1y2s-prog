from kivy.app import App
from kivy.config import Config
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')


from torneio import TorneioLayout

class TorneiosApp(App):
    def build(self):
        return TorneioLayout()


TorneiosApp().run()