class Conta:

    def __init__(self, dono, taxa_de_juro=0, saldo=0):
        pass

    @property
    def dono(self):
        """ devolve o dono"""
        pass

    @dono.setter
    def dono(self, value):
        """ Guarda uma string formatada em "title" (e.g., 'luigi vercotti' -> 'Luigi Vercotti)"""
        pass

    @property
    def taxa_de_juro(self):
        """ devolve a taxa de juro """
        pass

    @taxa_de_juro.setter
    def taxa_de_juro(self, value):
        """ Guarda a taxa de juro. Deve ser float ou int em percentagem (0-100%).
        A taxa_de_juro e nao negativa, sendo que se for fornecido um valor negativo a taxa_de_juro e colocada a 0.
        """
        pass

    @property
    def saldo(self):
        """ Devolve o saldo"""
        pass

    @saldo.setter
    def saldo(self, value):
        """Guarda ao saldo. Deve ser float ou int. O Saldo e nao negativa, sendo que se for fornecido um valor negativo o saldo e colocada a 0.
        """
        pass

    def capitaliza(self):
        """ Acresencenta os juros ao saldo.
        E.g., se saldo = 1000 e taxa_juro = 2 entao saldo passa a 1020
        """
        pass

    def cobra_comissao(self, comissao):
        """ o valor da comissao e retirado ao saldo.
        Se o saldo for maior do que a comissao entao cobra tudo, senao cobra o equivalente ao existente em saldo. E.g.:
        saldo = 10 e comissao = 5 -> saldo = 5 e cobrado = 5
        saldo = 10 e comissao = 15 -> saldo = 0 e cobrado = 10

        :ensures: valor descontado ao saldo
        """
        pass

    def faz_levantamento(self, valor):
        """Subtrai ao saldo o valor desde que o saldo se mantenha positivo.
        :ensures: True se o levantamento foi possivel, False caso contrario
        """
        pass

    def faz_deposito(self, valor):
        """ Acrescenta ao saldo o valor """
        pass