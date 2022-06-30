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
    return {
        "brand": brand,
        "model": model,
        "consumption": consumption,
        "kms": kms,
        "owner": owner,
        "color": color,
        "engine": engine
    }

def add_color(edit=False):
    editstring = ""
    if edit:
        editstring = " (leave empty to not change)"
    name = input(f"Name{editstring}: ")
    r = input(f"R{editstring}: ")
    g = input(f"G{editstring}: ")
    b = input(f"B{editstring}: ")
    return {
        "name": name,
        "r": r,
        "g": g,
        "b": b
    }

def add_person(edit=False):
    editstring = ""
    if edit:
        editstring = " (leave empty to not change)"
    forename = input(f"Forename{editstring}: ")
    surname = input(f"Surname{editstring}: ")
    address = input(f"Address{editstring}: ")
    cc = input(f"CC{editstring}: ")
    phonenumber = input(f"Phone Number{editstring}: ")
    return {
        "forename": forename,
        "surname": surname,
        "address": address,
        "cc": cc,
        "phonenumber": phonenumber
    }

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
    return {
        "fuel": fuel,
        "horsepower": horsepower,
        "torque": torque,
        "displacement": displacement,
        "numbercilinders": numbercilinders,
        "startingsystem": startingsystem,
        "dryweight": dryweight,
        "manufacturer": manufacturer
    }
