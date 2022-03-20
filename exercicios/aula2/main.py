import sys
sys.path.append("classes")

import prints
import inputs
import car
import color
import engine
import person

colors = []
people = []
engines = []

while True:
    prints.main_menu()
    op = input("> ")
    #if op == "ac":
    #    cars.append(car.Car(inputs.add_carro())) 
    if op == "aco":
        inp = inputs.add_color()
        colors.append(color.Color(inp[0], inp[1], inp[2], inp[3]))
    elif op == "lco":
        for i in range(len(colors)):
            print(f"{i+1}: {colors[i]}")
    elif op == "dco":
        del colors[int(input("Color number to delete: "))-1]

    elif op == "ap":
        inp = inputs.add_person()
        people.append(person.Person(inp[0], inp[1], inp[2], inp[3], inp[4]))
    elif op == "lp":
        for i in range(len(people)):
            print(f"{i+1}: {people[i]}")
    elif op == "dp":
        del people[int(input("Person number to delete: "))-1]
    
    elif op == "ae":
        inp = inputs.add_engine()
        engines.append(engine.Engine(inp[0], inp[1], inp[2], inp[3], inp[4], inp[5], inp[6], inp[7]))
    elif op == "le":
        for i in range(len(engines)):
            print(f"{i+1}: {engines[i]}")
    elif op == "de":
        del engines[int(input("Engine number to delete: "))-1]
    
    