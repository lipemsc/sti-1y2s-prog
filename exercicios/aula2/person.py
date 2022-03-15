class Person:
    def __init__(self, forename, surname, address, CC, phonenumber):
        self._forename = forename
        self._surname = surname
        self._address = address
        self._CC = CC
        self._phonenumber = phonenumber
    
    @property
    def forename(self):
        return self._forename

    @forename.setter
    def forename(self, forename):
        self._forename = forename
    
    @property
    def surname(self):
        return self._surname

    @surname.setter
    def surname(self, surname):
        self._surname = surname

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, address):
        self._address = address

    @property
    def CC(self):
        return self._CC

    @CC.setter
    def CC(self, CC):
        self._CC = CC

    @property
    def phonenumber(self):
        return self._phonenumber

    @phonenumber.setter
    def phonenumber(self, phonenumber):
        self._phonenumber = phonenumber

    