class QuadraticEquation:
     def __init__(self, a, b, c):
         self.__a = a
         self.__b = b
         self.__c = c
     
     def get_a(self):
         return self.__a

     def get_b(self):
         return self.__b
     
     def get_c(self):
         return self.__c

     def getDiscriminant(self):
         value = self.__b ** 2 - 4 * self.__a * self.__c
         return value
      
     def getRoot1(self):
         if self.getDiscriminant() > 0:
             r = (-self.__b + (self.__b ** 2 - 4 * self.__a * self.__c) * 0.5) / 2 * self.__a
             return r
         else:
             return 0
     
     def getRoot2(self):
         if self.getDiscriminant() > 0:
             r = (- self.__b - (self.__b ** 2 - 4 * self.__a * self.__c) * 0.5) / 2 * self.__a
             return r
         else:
             return 0

value = QuadraticEquation(20,90,50)
print("discriminant: ",value.getDiscriminant())
print("root one: ",value.getRoot1())
print("root two: ",value.getRoot2())