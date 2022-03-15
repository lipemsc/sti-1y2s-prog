class Color:
    def __init__(self, r, g, b):
        self._r = r
        self._g = g
        self._b = b

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


    @property
    def colorname(self):
        raise NotImplementedError()
    
    @colorname.setter
    def colorname(self, r, g, b):
        raise NotImplementedError()

    
cor = Color(1,1,1)

print(cor.rgb)