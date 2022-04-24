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

    #def ex6(self):
    #    self.cursor.execute("""
    #            SELECT * 
    #            FROM produtos
    #            ORDER BY PreçoUnitário, NomeDoProduto
    #    """)
    #    result = self.cursor.fetchall()
    #    return result


adam = Adamastor(config)

# ex1
# print(tabulate(adam.ex1(), headers="keys", tablefmt="psql"))

# ex3
print(tabulate(adam.ex3(), headers="keys", tablefmt="psql"))

# ex6
