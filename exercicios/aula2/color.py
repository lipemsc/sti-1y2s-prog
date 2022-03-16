class Color:
    def __init__(self, colorname, r, g, b):
        self._colorname = colorname
        self._r = r
        self._g = g
        self._b = b

    def __repr__(self):
        return f"Color {self.colorname}\nR:{self.r}\nG:{self.g}\nB:{self.b}"

    @property
    def colorname(self):
        return self._colorname
    
    @colorname.setter
    def r(self, colorname):
        self._colorname = colorname

    
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