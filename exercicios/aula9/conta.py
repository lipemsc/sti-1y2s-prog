class Conta:

    def __init__(self, dono, taxa_de_juro=0, saldo=0):
        self.dono = dono
        self.taxa_de_juro = taxa_de_juro
        self.saldo = saldo

    @property
    def dono(self):
        """ devolve o dono"""
        return self._dono

    @dono.setter
    def dono(self, value):
        """ Guarda uma string formatada em "title" (e.g., 'luigi vercotti' -> 'Luigi Vercotti)"""
        self._dono = value.title()

    @property
    def taxa_de_juro(self):
        """ devolve a taxa de juro """
        return self._taxa_de_juro

    @taxa_de_juro.setter
    def taxa_de_juro(self, value):
        """ Guarda a taxa de juro. Deve ser float ou int em percentagem (0-100%).
        A taxa_de_juro e nao negativa, sendo que se for fornecido um valor negativo a taxa_de_juro e colocada a 0.
        """
        if value < 0:
            self._taxa_de_juro = 0
        elif isinstance(value, int) or isinstance(value, float):
            self._taxa_de_juro = value

    @property
    def saldo(self):
        """ Devolve o saldo"""
        return self._saldo

    @saldo.setter
    def saldo(self, value):
        """Guarda ao saldo. Deve ser float ou int. O Saldo e nao negativa, sendo que se for fornecido um valor negativo o saldo e colocada a 0.
        """
        if value < 0:
            self._saldo = 0
        elif isinstance(value, int) or isinstance(value, float):
            self._saldo = value

    def capitaliza(self):
        """ Acresencenta os juros ao saldo.
        E.g., se saldo = 1000 e taxa_de_juro = 2 entao saldo passa a 1020
        """
        self.saldo += self.saldo * (self.taxa_de_juro / 100)

    def cobra_comissao(self, comissao):
        """ o valor da comissao e retirado ao saldo.
        Se o saldo for maior do que a comissao entao cobra tudo, senao cobra o equivalente ao existente em saldo. E.g.:
        saldo = 10 e comissao = 5 -> saldo = 5 e cobrado = 5
        saldo = 10 e comissao = 15 -> saldo = 0 e cobrado = 10

        :ensures: valor descontado ao saldo
        """
        if self.saldo < comissao:
            descontado = self.saldo
            self.saldo = 0
            return descontado
        else:
            self.saldo -= comissao
            return comissao

    def faz_levantamento(self, valor):
        """Subtrai ao saldo o valor desde que o saldo se mantenha positivo.
        :ensures: True se o levantamento foi possivel, False caso contrario
        """
        if self.saldo >= valor:
            self.saldo -= valor
            return True
        else:
            return False

    def faz_deposito(self, valor):
        """ Acrescenta ao saldo o valor """
        self.saldo += valor
        return True
        