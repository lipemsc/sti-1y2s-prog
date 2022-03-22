import math

try:
    try:
        num = float(input("Insira um número: "))
    except ValueError:
        print("Número inválido")
    else:
        try:
            raiz = math.sqrt(num)
        except ValueError:
            print(f"Impossível calcular raiz quadrada de {num}")
        else:
            print(raiz)
except (KeyboardInterrupt, EOFError):
    print("\nPrograma Interrompido.")