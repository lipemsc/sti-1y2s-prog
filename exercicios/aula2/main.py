import prints
import inputs

while True:
    prints.print_main_menu()
    op = input("> ")
    if op == "ac":
        prints.print_cars_menu()
        inputs.input_carro()
