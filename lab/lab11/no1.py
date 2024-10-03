import math

class Point(object):
    def __init__(self, xValue = 0, yValue = 0):
        self.x = xValue
        self.y = yValue

    def printinfo(self):
        print("Position:", self.x, self.y)

class Circle(Point):
    def __init__(self, xValue, yValue, radius = 0.00):
        super().__init__(xValue, yValue)
        self.radius = float(radius)
    
    def area(self):
        area = math.pi * ( self.radius * self.radius)
        return format(area, ".2f")
    
    def printinfo(self):
        print("Position:", self.x, self.y)
        print("Radius:", self.radius)
        print("Area:", self.area())

circle = Circle(2, 3, 9)
circle.area()
circle.printinfo()