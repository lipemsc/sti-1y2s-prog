def add_car(edit=False):
    editstring = ""
    if edit:
        editstring = " (leave empty to not change)"
    brand = input(f"Brand{editstring}: ")
    model = input(f"Model{editstring}: ")
    consumption = input(f"Consumption{editstring}: ")
    kms = input(f"KM's{editstring}: ")
    owner = int(input(f"Owner ID{editstring}: "))
    color = int(input(f"Color ID{editstring}: "))
    engine = int(input(f"Engine ID{editstring}: "))
    return (brand, model, consumption, kms, owner, color, engine)

def add_color(edit=False):
    editstring = ""
    if edit:
        editstring = " (leave empty to not change)"
    name = input(f"Name{editstring}: ")
    r = input(f"R{editstring}: ")
    g = input(f"G{editstring}: ")
    b = input(f"B{editstring}: ")
    return (name, r, g, b)

def add_person(edit=False):
    editstring = ""
    if edit:
        editstring = " (leave empty to not change)"
    forename = input(f"Forename{editstring}: ")
    surname = input(f"Surname{editstring}: ")
    address = input(f"Address{editstring}: ")
    cc = input(f"CC{editstring}: ")
    phonenumber = input(f"Phone Number{editstring}: ")
    return (forename, surname, address, cc, phonenumber)

def add_engine(edit=False):
    editstring = ""
    if edit:
        editstring = " (leave empty to not change)"
    fuel = input(f"Fuel{editstring}: ")
    horsepower = input(f"Horsepower{editstring}: ")
    torque = input(f"Torque{editstring}: ")
    displacement = input(f"Displacement{editstring}: ")
    numbercilinders = input(f"Number of Cilinders{editstring}: ")
    startingsystem = input(f"Starting System{editstring}: ")
    dryweight = input(f"Dry Weight{editstring}: ")
    manufacturer = input(f"Manufacturer{editstring}: ")
    return (fuel, horsepower, torque, displacement, numbercilinders, startingsystem, dryweight, manufacturer)
