# 6) A - Faça uma função que recebe 2 strings e informe se possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.

def verificar_string(str1, str2):
    print(f"Tamanho de \"{str1}\": {len(str1)} caracteres")
    print(f"Tamanho de \"{str2}\": {len(str2)} caracteres")

    if len(str1) == len(str2):
        print("As duas strings são de tamanhos iguais.")
    else:
        print("As duas strings são de tamanhos diferentes.")
    if str1 == str2:
        print("As duas strings possuem o mesmo conteúdo.")
    else:
        print("As duas strings possuem conteúdo diferente.")

verificar_string(input("String 1: "),input("String 2: "))
