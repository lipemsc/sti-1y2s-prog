nota1 = float(input("Insira a 1ª nota: "))
nota2 = float(input("Insira a 2ª nota: "))
media = (nota1 + nota2) / 2

if media > 19:
    print("Aprovado com distinção")
elif media >= 9.5:
    print("Aprovado")
else:
    print("Reprovado")
