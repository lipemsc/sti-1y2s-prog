class Engine:
    def __init__(self, fuel, horsepower, torque, displacement,numbercilinders,
        startingsystem, dryweight, manufacturer):
        
        self._fuel = fuel
        self._horsepower = horsepower
        self._torque = torque
        self._displacement = displacement
        self._numbercilinders = numbercilinders
        self._startingsystem = startingsystem
        self._dryweight = dryweight
        self._manufacturer = manufacturer

    def __repr__(self):
        return f"""Fuel: {self.fuel}
Horsepower: {self.horsepower}
Torque: {self.torque}
Displacement: {self.displacement}
Number of Cilinders: {self.numbercilinders}
Starting System: {self.startingsystem}
Dry Weight: {self.dryweight}
Manufacturer: {self.manufacturer}
"""


    @property
    def fuel(self):
        return self._fuel

    @fuel.setter
    def fuel(self, fuel):
        self._fuel = fuel

    
    @property
    def horsepower(self):
        return self._horsepower

    @horsepower.setter
    def horsepower(self, horsepower):
        self._horsepower = horsepower


    @property
    def torque(self):
        return self._torque

    @torque.setter
    def torque(self, torque):
        self._torque = torque


    @property
    def displacement(self):
        return self._displacement

    @displacement.setter
    def displacement(self, displacement):
        self._displacement = displacement


    @property
    def numbercilinders(self):
        return self._numbercilinders

    @numbercilinders.setter
    def numbercilinders(self, numbercilinders):
        self._numbercilinders = numbercilinders


    @property
    def startingsystem(self):
        return self._startingsystem

    @startingsystem.setter
    def startingsystem(self, startingsystem):
        self._startingsystem = startingsystem


    @property
    def dryweight(self):
        return self._dryweight

    @dryweight.setter
    def dryweight(self, dryweight):
        self._dryweight = dryweight

        
    @property
    def manufacturer(self):
        return self._manufacturer

    @manufacturer.setter
    def manufacturer(self, manufacturer):
        self._manufacturer = manufacturer
    