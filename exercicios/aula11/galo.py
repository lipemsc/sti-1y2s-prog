# JOGO DO GALO
#
#  1 | 2 | 3
#  4 | 5 | 6
#  7 | 8 | 9
#
# Layout ^
#        |
#

class Galo:

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._positions = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    @property
    def positions(self):
        return self._positions

    def draw_positions(self):
        print("| ", sep="", end="")
        for i, j in enumerate(self._positions):
            if i == 3 or i == 6:
                print("\n| ", sep="", end="")
            if j == 1:
                print("X", sep="", end="")
            elif j == 2:
                print("O", sep="", end="")
            else:
                print(" ", sep="", end="")
            print(" | ", sep="", end="")
        print("")

    def check_win(self):
        if self._positions[0] == self._positions[1] == self._positions[2] != 0:
            return self._positions[0]
        elif self._positions[3] == self._positions[4] == self._positions[5] != 0:
            return self._positions[3]
        elif self._positions[6] == self._positions[7] == self._positions[8] != 0:
            return self._positions[6]
        elif self._positions[0] == self._positions[3] == self._positions[6] != 0:
            return self._positions[0]
        elif self._positions[1] == self._positions[4] == self._positions[7] != 0:
            return self._positions[1]
        elif self._positions[2] == self._positions[5] == self._positions[8] != 0:
            return self._positions[2]
        elif self._positions[0] == self._positions[4] == self._positions[8] != 0:
            return self._positions[0]
        elif self._positions[2] == self._positions[4] == self._positions[6] != 0:
            return self._positions[2]
        else:
            return 0

    def play(self, position, player):
        if self._positions[position] == 0 and (player == 1 or player == 2):
            self._positions[position] = player
            return True
        else:
            return False