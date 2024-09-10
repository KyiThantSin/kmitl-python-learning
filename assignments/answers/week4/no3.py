class LinearEquation:
    def __init__(self, a, b, c, d, e, f):
        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = d
        self.__e = e
        self.__f = f
    
    def get_a(self):
        return self.__a
    
    def get_b(self):
        return self.__b
    
    def get_c(self):
        return self.__c
    
    def get_d(self):
        return self.__d
    
    def get_e(self):
        return self.__e
    
    def get_f(self):
        return self.__f

    def isSolvable(self):
        if ((self.get_a() * self.get_d()) - (self.get_b() * self.get_c())) != 0:
            return True
        else:
            return False
    
    def getX(self):
        x = ((self.get_e() * self.get_d()) - (self.get_b() * self.get_f())) / ((self.get_a() * self.get_d()) - (self.get_b() * self.get_c()))
        return x
    
    def getY(self):
        y = ((self.get_a() * self.get_f()) - (self.get_e() * self.get_c())) / ((self.get_a() * self.get_d()) - (self.get_b() * self.get_c()))
        return y

a = LinearEquation(2,3,5,3,9,5)
print("Is solvable: ", a.isSolvable())
print("x: ", format(a.getX(), ".03"))
print("y: ", format(a.getY(), ".03"))