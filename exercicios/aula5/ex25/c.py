try:
    name = input("Insira o seu nome:")
    try:
        name = name.split()[3]
    except IndexError:
        print("Não existe 4º nome")
    else:
        quarto_nome = list(name)
        print(quarto_nome)
except (KeyboardInterrupt, EOFError):
    print("\nPrograma Interrompido.")