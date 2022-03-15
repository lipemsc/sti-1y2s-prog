from color import Color

class Car:
    def __init__(self, brand, model, consumption, kms, owner, color: Color):
        self._brand = brand
        self._model = model
        self._consumption = consumption
        self._kms = kms
        self._owner = owner
        self._color = color

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, brand):
        self._brand = brand
    

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, model):
        self._model = model


    @property
    def consumption(self):
        return self._consumption

    @consumption.setter
    def consumption(self, consumption):
        self._consumption = consumption
    

    @property
    def kms(self):
        return self._kms

    @kms.setter
    def kms(self, kms):
        self._kms = kms


    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, owner):
        self._owner = owner


    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color: Color):
        self._color = color


    def addkms(self, kmstoadd):
        self.kms += kmstoadd
    
    