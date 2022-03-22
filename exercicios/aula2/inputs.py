def add_car():
    brand = input("Brand: ")
    model = input("Model: ")
    consumption = input("Consumption: ")
    kms = input("KM's: ")
    owner = int(input("Owner ID: "))
    color = int(input("Color ID: "))
    engine = int(input("Engine ID: "))
    return (brand, model, consumption, kms, owner, color, engine)

def add_color():
    name = input("Name: ")
    r = input("R: ")
    g = input("G: ")
    b = input("B: ")
    return (name, r, g, b)

def add_person():
    forename = input("Forename: ")
    surname = input("Surname: ")
    address = input("Address: ")
    cc = input("CC: ")
    phonenumber = input("Phone Number: ")
    return (forename, surname, address, cc, phonenumber)

def add_engine():
    fuel = input("Fuel: ")
    horsepower = input("Horsepower: ")
    torque = input("Torque: ")
    displacement = input("Displacement: ")
    numbercilinders = input("Number of Cilinders: ")
    startingsystem = input("Starting System: ")
    dryweight = input("Dry Weight: ")
    manufacturer = input("Manufacturer: ")
    return (fuel, horsepower, torque, displacement, numbercilinders, startingsystem, dryweight, manufacturer)
