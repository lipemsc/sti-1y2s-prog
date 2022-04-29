#!/bin/python3

import mysql.connector
# from pprint import pprint
from tabulate import tabulate

config = {
    'host' : 'localhost',
    'user' : 'root',
    'password' : 'root',
    'db' : 'adamastor' 
}

class Adamastor:
    def __init__(self, config):
        self.connection = mysql.connector.connect(**config)
        self.cursor = self.connection.cursor(dictionary=True)

    def ex1(self):
        self.cursor.execute("""
                SELECT * 
                FROM produtos
                ORDER BY PreçoUnitário
        """)
        result = self.cursor.fetchall()
        return result

    def ex3(self):
        self.cursor.execute("""
                SELECT * 
                FROM produtos
                ORDER BY PreçoUnitário, NomeDoProduto
        """)
        result = self.cursor.fetchall()
        return result

    def ex6(self):
        self.cursor.execute("""
                SELECT * 
                FROM produtos
                WHERE Existências < ExistênciaMínima
        """)
        result = self.cursor.fetchall()
        return result

    def ex10(self):
        self.cursor.execute("""
                SELECT * 
                FROM encomendas
                WHERE DataDaEncomenda BETWEEN "1996-07-10" AND "1996-07-17"
        """)
        result = self.cursor.fetchall()
        return result

    def ex12(self):
        self.cursor.execute("""
                SELECT encomendas.*
                FROM
                    encomendas INNER JOIN clientes
                        ON encomendas.CódigoDoCliente = clientes.CódigoDoCliente
                WHERE
                    clientes.NomeDaEmpresa = 'Hanari Carnes'

        """)
        result = self.cursor.fetchall()
        return result

    def ex15(self):
        self.cursor.execute("""
                SELECT encomendas.*
                FROM
                    encomendas INNER JOIN clientes
                        ON encomendas.CódigoDoCliente = clientes.CódigoDoCliente
                WHERE
                    clientes.NomeDaEmpresa = 'Hanari Carnes' AND
                    encomendas.DataDaEncomenda = '1996-07-08'

        """)
        result = self.cursor.fetchall()
        return result

    def ex21(self):
        query = ("""
                INSERT INTO produtos(NomeDoProduto, Descontinuado)
                VALUES (%s, %s)
        """)
        self.cursor.execute(query, ("Batata Doce", "0"))
        self.connection.commit()
        return self.cursor.rowcount
        
    def ex26(self):
        self.cursor.execute("""
                SELECT MIN(PreçoUnitário) as min
                FROM
                    produtos
        """)
        result = self.cursor.fetchall()
        return result

    def ex31(self):
        self.cursor.execute("""
                SELECT DISTINCT Cidade
                FROM
                    fornecedores
        """)
        result = self.cursor.fetchall()
        return result

    def ex34(self):
        self.cursor.execute("""
                SELECT
        	        detalhes_da_encomenda.CódigoDaEncomenda as id, SUM(detalhes_da_encomenda.PreçoUnitário * Quantidade * (1-Desconto)) as soma
                FROM
                	detalhes_da_encomenda
                GROUP BY
                	detalhes_da_encomenda.CódigoDaEncomenda
                ORDER BY soma DESC
                LIMIT 0,1
        """)
        result = self.cursor.fetchall()
        return result
    
    def ex35(self):
        self.cursor.execute("""
                SELECT
        	        detalhes_da_encomenda.CódigoDaEncomenda as id, COUNT(*) as soma
                FROM
                	detalhes_da_encomenda
                GROUP BY
                	detalhes_da_encomenda.CódigoDaEncomenda
                ORDER BY soma DESC
                LIMIT 0,1
        """)
        result = self.cursor.fetchall()
        return result
    

adam = Adamastor(config)

# ex1
# print(tabulate(adam.ex1(), headers="keys", tablefmt="psql"))
# input()

# # ex3
# print(tabulate(adam.ex3(), headers="keys", tablefmt="psql"))

# input()
# # ex6
# print(tabulate(adam.ex6(), headers="keys", tablefmt="psql"))

# input()
# # ex10
# print(tabulate(adam.ex10(), headers="keys", tablefmt="psql"))

# input()
# # ex12
# print(tabulate(adam.ex12(), headers="keys", tablefmt="psql"))

# input()
# # ex15
# print(tabulate(adam.ex15(), headers="keys", tablefmt="psql"))

# input()
# # ex21
# print(f"{adam.ex21()} linhas inseridas")

# input()
# # ex26
# print(adam.ex26()[0]["min"])

# input()
# # ex31
# ex31 = adam.ex31()
# for linha in ex31:
#         print(linha["Cidade"].upper())

input()
#ex34
print("A encomenda com maior valor é a nº " + str(adam.ex34()[0]["id"]))

input()
# ex35
print("A encomenda com maior número de itens é a nº " + str(adam.ex35()[0]["id"]))

