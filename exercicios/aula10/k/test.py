import random

class Guesser():
    def __init__(self, min, max):
        self._rand = random.randint(min, max)
        self._gaveup = False
        self.count = 0
    
    def try_guess(self, guess):
        assert self._gaveup == False, "User gave up"
        self.count += 1
        return guess == self._rand
    
    def hint(self, guess):
        assert self._gaveup == False, "User gave up"
        self.count += 1
        if guess > self._rand:
            return 1
        elif guess < self._rand:
            return -1
        else:
            return 0
    
    def giveup(self):
        self._gaveup = True
        return self._rand
        

g = Guesser(1,1000)
while True:
    try:
        tent = int(input("Tentativa: "))
    except ValueError:
        print("Erro, tente outra vez!")
    
    if tent == -1:
        print("Desististe! O número era " + str(g.giveup()))
        break
    hint = g.hint(tent)
    if hint == 0:
        print("Ganhaste!")
        break
    elif hint == 1:
        print("Nº demasiado grande")
    elif hint == -1:
        print("Nº demasiado pequeno")
        
