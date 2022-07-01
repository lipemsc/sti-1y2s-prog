# (C) Pedro Cardoso

from abc import ABC, abstractmethod
import random


class Jogo(ABC):
    """ implementa uma classe para um jogo com 2 humanos"""

    def __init__(self):
        print('bom jogo...')
        self.inicializa_tabuleiro()

    @abstractmethod
    def joga_humano(self, jogador):
        """ metodo que solicita ao humano :jogador: a proxima jogada e coloca-a no tabuleiro
        :param jogador: numero do jogador (0 ou 1)
        """
        pass

    @abstractmethod
    def terminou(self):
        """ devolve `True` se foi verificada a condicao de paragem, i.e., um jogador ganhou.
        devolve `False` caso contrario """
        pass

    @abstractmethod
    def mostra_tabuleiro(self):
        """desenha o tabuleiro"""
        pass

    @abstractmethod
    def inicializa_tabuleiro(self):
        """ inicializa o tabuleiro de jogo"""
        pass

    @abstractmethod
    def ha_jogadas_possiveis(self):
        """ verifica se ainda ha jogadas possiveis ou se o jogo esta empatado"""
        pass

    def jogar(self):
        """ corre o jogo..."""

        # escolhe quem joga em primeiro
        jogador = random.randint(0, 1)

        while True:
            self.mostra_tabuleiro()
            self.joga_humano(jogador)
            if self.terminou():
                self.mostra_tabuleiro()
                print(f'o jogador {jogador} ganhou!!')
                return
            elif not self.ha_jogadas_possiveis():
                print(f'Empataram!!!')
                return
            # passa ao outro jogador
            jogador = (jogador + 1) % 2


