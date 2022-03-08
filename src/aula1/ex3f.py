n = int(input("n="))
soma = 0

for i in range(n):
    soma += int(input(f"Insira o {i+1}º número: "))

media = soma / n

print(soma)
print(media)
