class Color:
    def __init__(self, name, r, g, b):
        self._name = name
        self._r = r
        self._g = g
        self._b = b

    def __repr__(self):
        return f"Color {self.name}  R:{self.r} G:{self.g} B:{self.b}"

    @property
    def name(self):
        return self._name
    
    @name.setter
    def r(self, name):
        self._name = name

    
    @property
    def r(self):
        return self._r
    
    @r.setter
    def r(self, r):
        self._r = r


    @property
    def g(self):
        return self._g
    
    @g.setter
    def g(self, g):
        self._g = g


    @property
    def b(self):
        return self._b
    
    @b.setter
    def b(self, b):
        self._b = b


    @property
    def rgb(self):
        return self._r, self._g, self._b
    
    @rgb.setter
    def rgb(self, r, g, b):
        self._r = r
        self._g = g
        self._b = b



    
#cor = Color(1,1,1)

#print(cor.rgb)