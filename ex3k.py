## 3) K - Fibonacci é até ao nºesimo termo, então talvez seja para imprimir
## n numeros em vez de parar so quando for maior do que o n


op = int(input("Insira um numero: "))

n1 = 0
n2 = 1
n = 0
while n < op:
    n = n2 + n1
    print(n)
    n1 = n2
    n2 = n

