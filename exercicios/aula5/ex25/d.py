try:
    string = "complementos de programacao"
    try:
        num = int(input("Insira um número: ")) - 1
    except ValueError:
        print("Número inválido")
    else:
        try:
            assert num >= 0
        except AssertionError:
            print("A posição não pode ser inferior a 1")
        else:
            try:
                print(string[num])
            except IndexError:
                print(f"Não existe {num}º caracter")

except (KeyboardInterrupt, EOFError):
    print("\nPrograma Interrompido.")