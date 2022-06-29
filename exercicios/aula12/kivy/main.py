from kivy.app import App
from kivy.config import Config
from kivy.uix.screenmanager import ScreenManager, Screen
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')


from torneio import TorneioLayout

# class BaseAppLayout(ScreenManager):
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)


class TorneiosApp(App):
    def build(self):
        sm = ScreenManager()
        torneiosscreen = Screen(name='Torneios')
        torneiosscreen.add_widget(TorneioLayout())
        sm.add_widget(torneiosscreen)

        # return TorneioLayout()
        return sm

TorneiosApp().run()