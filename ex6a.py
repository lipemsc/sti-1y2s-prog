def pedirnome():
  return input("Insira o seu nome: ")

def nomeaocontrario(nome):
    print(nome[::-1])
 
nomeaocontrario(pedirnome())
