#import sys
#sys.path.append("classes")

import prints
import inputs
import classes.car as car
import classes.color as color
import classes.engine as engine
import classes.person as person

colors = []
people = []
engines = []
cars = []

while True:
    prints.main_menu()
    op = input("> ")
    #if op == "ac":
    #    cars.append(car.Car(inputs.add_carro())) 
    if op == "aco":
        inp = inputs.add_color()
        colors.append(color.Color(
            inp["name"],
            inp["r"],
            inp["g"],
            inp["b"]
        ))
    elif op == "eco":
        n = int(input("Color number to edit: "))-1
        inp = inputs.add_color(edit=True)
        if inp["r"] != "":
            colors[n].r = inp["r"]
        if inp["g"] != "":
            colors[n].g = inp["g"]
        if inp["b"] != "":
            colors[n].b = inp["b"]
        if inp["name"] != "":
            colors[n].name = inp["name"]
    elif op == "lco":
        for i in range(len(colors)):
            print(f"{i+1}: {colors[i]}")
    elif op == "dco":
        del colors[int(input("Color number to delete: "))-1]

    elif op == "ap":
        inp = inputs.add_person()
        people.append(person.Person(
            inp["forename"],
            inp["surname"],
            inp["address"],
            inp["cc"],
            inp["phonenumber"]
        ))
    elif op == "ep":
        n = int(input("Color number to edit: "))-1
        inp = inputs.add_person(edit=True)
        if inp["forename"] != "":
            people[n].forename = inp["forename"]
        if inp["surname"] != "":
            people[n].surname = inp["surname"]
        if inp["address"] != "":
            people[n].address = inp["address"]
        if inp["cc"] != "":
            people[n].cc = inp["cc"]
        if inp["phonenumber"] != "":
            people[n].phonenumber = inp["phonenumber"]
    elif op == "lp":
        for i in range(len(people)):
            print(f"{i+1}: {people[i]}")
    elif op == "dp":
        del people[int(input("Person number to delete: "))-1]
    
    elif op == "ae":
        inp = inputs.add_engine()
        engines.append(engine.Engine(
            inp["fuel"],
            inp["horsepower"],
            inp["torque"],
            inp["displacement"],
            inp["numbercilinders"],
            inp["startingsystem"],
            inp["dryweight"],
            inp["manufacturer"]
        ))
    elif op == "ee":
        n = int(input("Color number to edit: "))-1
        inp = inputs.add_engine()
        if inp["fuel"] != "":
            engines[n].fuel = inp["fuel"]
        if inp["horsepower"] != "":
            engines[n].horsepower = inp["horsepower"]
        if inp["torque"] != "":
            engines[n].torque = inp["torque"]
        if inp["displacement"] != "":
            engines[n].displacement = inp["displacement"]
        if inp["numbercilinders"] != "":
            engines[n].numbercilinders = inp["numbercilinders"]
        if inp["startingsystem"] != "":
            engines[n].startingsystem = inp["startingsystem"]
        if inp["dryweight"] != "":
            engines[n].dryweight = inp["dryweight"]
        if inp["manufacturer"] != "":
            engines[n].manufacturer = inp["manufacturer"]
    elif op == "le":
        for i in range(len(engines)):
            print(f"{i+1}: {engines[i]}")
    elif op == "de":
        del engines[int(input("Engine number to delete: "))-1]
    
    elif op == "ac":
        inp = inputs.add_car()
        cars.append(car.Car(
            inp["brand"],
            inp["model"],
            inp["consumption"],
            inp["kms"],
            people[inp["owner"]-1],
            colors[inp["color"]-1],
            engines[inp["engine"]-1]
        ))
    elif op == "ec":
        inp = inputs.add_car(edit=True)
        if inp["brand"] != "":
            cars[n].brand = inp["fuel"]
        if inp["model"] != "":
            cars[n].model = inp["horsepower"]
        if inp["consumption"] != "":
            cars[n].consumption = inp["consumption"]
        if inp["kms"] != "":
            cars[n].kms = inp["kms"]
        if inp["owner"] != "":
            cars[n].owner = people[inp["owner"]-1]
        if inp["color"] != "":
            cars[n].color = colors[inp["color"]-1]
        if inp["engine"] != "":
            cars[n].engine = engines[inp["engine"]-1]
    elif op == "lc":
        for i in range(len(cars)):
            print(f"{i+1}: {cars[i]}")
    elif op == "dc":
        del cars[int(input("Engine number to delete: "))-1]
    else:
        print(f"{op}: command not found")