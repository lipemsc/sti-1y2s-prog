pares = 0
impares  = 0

for i in range(10):
    if int(input(f"Insira o {i+1}º número: ")) % 2 == 0:
        pares += 1
    else:
        impares += 1


print(f"Pares: {pares}")
print(f"Impares: {impares}")
