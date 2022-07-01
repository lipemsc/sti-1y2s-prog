from abc import ABC, abstractmethod
from classes import Jogo
import random


class QuatroLinha(Jogo):
    def inicializa_tabuleiro(self):
        # conta as jogadas, serve para saber se ainda ha jogadas validas
        self.numero_de_jogadas_realizadas = 0
        self.tabuleiro = {(l, c): ' ' for l in range(6)
                          for c in range(7)}  # o tabuleiro e um dicionario!
        # print(self.tabuleiro)

    def _le_linha_coluna_valida(self, s, axis='x'):
        """ metodo auxiliar para ler uma posicao que seja 0, 1 ou 2"""
        while True:
            x = input(s)
            if x in ['0', '1', '2', '3', '4', '5', '6'] and axis == 'x'\
                    or x in ['0', '1', '2', '3', '4', '5'] and axis == 'y':
                return int(x)

    def joga_humano(self, jogador):
        print(f'jogador {jogador} insira a sua jogada')
        while True:
            coluna = self._le_linha_coluna_valida('Coluna?', 'x')

            for i in range(6):
                if self.tabuleiro[(i, coluna)] != ' ':
                    self.tabuleiro[(i-1, coluna)] = 'X' if jogador == 1 else 'O'
                    break
            else:
                self.tabuleiro[(i, coluna)] = 'X' if jogador == 1 else 'O'
            break


            # # verifica se a posicao nao esta preenchida, i.e., e valida
            # if self.tabuleiro[(linha, coluna)] == ' ':
            #     self.tabuleiro[(linha, coluna)] = ['X', 'O'][jogador]
            #     self.numero_de_jogadas_realizadas += 1
            #     return
            # else:
            #     print('Jogada invalida. Tente de novo')

    def terminou(self):
        #debug(positions)
        count = [0, 0]

        # horizontal verification
        for line in range(5):
            for cell in range(6):
                if self.tabuleiro[(line, cell)] == ' ':
                    count = [0, 0]
                elif self.tabuleiro[(line, cell)] == 'X':
                    count[0] += 1
                    count[1] = 0
                elif self.tabuleiro[(line, cell)] == 'O':
                    count[1] += 1
                    count[0] = 0
                if count[0] >= 4:
                    return True
                if count[1] >= 4:
                    return True
            #print(count)
        
        count = [0, 0]

        for x in range(6):
            for y in range(5):
                if self.tabuleiro[(y, x)] == ' ':
                    count = [0, 0]
                elif self.tabuleiro[(y, x)] == 'X':
                    count[0] += 1
                    count[1] = 0
                elif self.tabuleiro[(y, x)] == 'O':
                    count[1] += 1
                    count[0] = 0
                if count[0] >= 4:
                    return True
                if count[1] >= 4:
                    return True
            #print(count)


        for y in range(6):
            for x in range(5):
                count = [0, 0]
                for i in range(4):
                    try:
                        if self.tabuleiro[(y+i, x+i)] == 'X':
                            count[0] += 1
                        if self.tabuleiro[(y+1, x+1)] == 'O':
                            count[1] += 1
                    except (IndexError, KeyError):
                        continue
                    if count[0] >= 4:
                        return True
                    if count[1] >= 4:
                        return True
                
                count = [0, 0]
                for i in range(4):
                    try:
                        if x-i < 0:
                            continue
                        if self.tabuleiro[(y+1, x-1)] == 'X':
                            count[0] += 1
                        if self.tabuleiro[(y+1, x-1)] == 'O':
                            count[1] += 1
                    except (IndexError, KeyError):
                        pass
                    if count[0] >= 4:
                        return True
                    if count[1] >= 4:
                        return True

        return False

    def mostra_tabuleiro(self):
        # print(self.tabuleiro)
        print((4*7+1) * '-')
        for l in range(6):
            for c in range(7):
                print(f'| {self.tabuleiro[(l, c)]} ', end='')
            print('|\n' + (4*7+1) * '-')

    def ha_jogadas_possiveis(self):
        return self.numero_de_jogadas_realizadas < 9


j4linha = QuatroLinha()
j4linha.jogar()
