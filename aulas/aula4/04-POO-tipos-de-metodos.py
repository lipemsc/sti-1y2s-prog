# Pedro Cardoso (C) All rights reserved

class Pizza:
    
    # area de pizza por pessoa
    # parametro da classe
    area_por_pessoa = 750.
    
    def __init__(self, ingredientes):
        # parametro do objecto
        self.ingredientes = ingredientes

    def __repr__(self):
        return f'Pizza({self.ingredientes})'

    @classmethod # metodo da classe, em vez de receber o objecto (self) como 1º parametro recebe o cls que representa a classe
    def margherita(cls):
        """devolve um objeto, instancia de Pizza, com os ingredientes 
        da Pizza margherita"""
        return cls(['mozzarela', 'tomate']) # retorna uma classe (?), basicamente se executarmos a linha 45  o objeto "margherita" vai ter as caracteristicas deste return

    @classmethod
    def prosciutto(cls):
        """devolve um objeto, instancia de Pizza, com os ingredientes 
        da Pizza prosciutto"""
        return cls(['mozzarela', 'tomate', 'fiambre'])
    
    @staticmethod # metodo estático, nao depende de nada
    def para_quantas_pessoas(raio):
        """metodo (estatico) que estima e devolve para quantas pessoas 
        é uma pizza, sabendo o seu raio devolve area_pizza / area_por_pessoa
        """
        area_pizza = 3.14 * raio ** 2
        return area_pizza / Pizza.area_por_pessoa
    
    @staticmethod
    def qual_o_raio(numero_pessoas):
        """metodo (estatico) que estima o raio que a pizza deve ter dado
            o número de pessoas devolve 
        """
        area_total = numero_pessoas * Pizza.area_por_pessoa 
        return (area_total / 3.14) ** .5


margherita = Pizza.margherita()
print(margherita)
