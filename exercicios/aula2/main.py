import prints
import inputs
import car
import color
import engine
import person

colors = []

while True:
    prints.print_main_menu()
    op = input("> ")
    #if op == "ac":
    #    cars.append(car.Car(inputs.add_carro())) 
    if op == "aco":
        inp = inputs.add_color()
        colors.append(color.Color(inp[0], inp[1], inp[2], inp[3]))
    elif op == "lco":
        for color in colors:
            print(color)