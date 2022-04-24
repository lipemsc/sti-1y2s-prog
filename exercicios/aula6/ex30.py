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

    #def ex21(self):
    #    self.cursor.execute("""
    #            SELECT encomendas.*
    #            FROM
    #                encomendas INNER JOIN clientes
    #                    ON encomendas.CódigoDoCliente = clientes.CódigoDoCliente
    #            WHERE
    #                clientes.NomeDaEmpresa = 'Hanari Carnes' AND
    #                encomendas.DataDaEncomenda = '1996-07-08'

    #    """)
    #    result = self.cursor.fetchall()
    #    return result

adam = Adamastor(config)

# ex1
# print(tabulate(adam.ex1(), headers="keys", tablefmt="psql"))

# ex3
# print(tabulate(adam.ex3(), headers="keys", tablefmt="psql"))

# ex6
# print(tabulate(adam.ex6(), headers="keys", tablefmt="psql"))

# ex10
# print(tabulate(adam.ex10(), headers="keys", tablefmt="psql"))

# ex12
# print(tabulate(adam.ex12(), headers="keys", tablefmt="psql"))

# ex15
# print(tabulate(adam.ex15(), headers="keys", tablefmt="psql"))

