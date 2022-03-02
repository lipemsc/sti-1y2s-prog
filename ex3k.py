op = int(input("Insira um numero: "))

n1 = 0
n2 = 1
n = 0
while n < op:
    n = n2 + n1
    print(n)
    n1 = n2
    n2 = n

