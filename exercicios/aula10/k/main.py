from kivy.app import App
from kivy.config import Config
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
import random


class Guesser():
    def __init__(self, min, max):
        self._rand = random.randint(min, max)
        self._gaveup = False
        self._count = 0
        self._won = False

    @property
    def number(self):
        if self._won:
            return self._rand
        else:
            return "*" * len(str(self._rand))
    
    @property
    def count(self):
        return self._count

    def try_guess(self, guess):
        assert self._gaveup == False, "User gave up"
        assert self._won == False, "User already won"
        self._count += 1
        return guess == self._rand
    
    def hint(self, guess):
        assert self._gaveup == False, "User gave up"
        assert self._won == False, "User already won"
        self._count += 1
        if guess > self._rand:
            return 1
        elif guess < self._rand:
            return -1
        else:
            self._won = True
            return 0
    
    def giveup(self):
        assert self._won == False, "User already won"
        self._gaveup = True
        return self._rand
        
class KApp(App):
    def build(self):
        return MyLayout()

class MyLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.guesser = Guesser(1, 1000)
        self.ids.tbox0.text = str(self.guesser.number)

    def verify(self):
        hint = self.guesser.hint(int(self.ids.tbox1.text))
        self.ids.tbox0.text = str(self.guesser.number)
        if hint == 0:
            self.ids.btn0.disabled = True
            self.ids.tbox1.disabled = True
            self.ids.lbl0.text = f"Ganhaste após {self.guesser.count} jogadas!"
        if hint == -1:
            self.ids.lbl0.text = "Demasiado pequeno"
        if hint == 1:
            self.ids.lbl0.text = "Demasiado grande"


KApp().run()