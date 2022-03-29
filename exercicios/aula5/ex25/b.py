try:
    try:
        num1 = int(input("Insira o 1º número: "))
        num2 = int(input("Insira o 2º número: "))
    except ValueError:
        print("Número inválido")
    else:
        try:
            result = num1 / num2
        except ZeroDivisionError:
            print("Não é possível dividir por zero.")
        else:
            print(result)
except (KeyboardInterrupt, EOFError):
    print("\nPrograma Interrompido.")