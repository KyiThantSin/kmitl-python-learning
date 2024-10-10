from abc import ABC, abstractmethod
import turtle

class TwoDShape(ABC):
    @abstractmethod
    def draw(self):
        pass

class Line(TwoDShape):
    def __init__(self, length):
        super().__init__()
        self.length = length

    def draw(self, ):
        turtle.clear()
        turtle.forward(self.length)

class Rectangle(TwoDShape):

    def __init__(self, w, l):
        super().__init__()
        self.width = w
        self.length = l

    def draw(self):
        turtle.clear()
        for _ in range(2):
            turtle.forward(self.length)
            turtle.right(90)
            turtle.forward(self.width)
            turtle.right(90)

class Circle(TwoDShape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius
    
    def draw(self):
        turtle.clear()
        turtle.circle(self.radius)


class Square(TwoDShape):

    def __init__(self, l):
        super().__init__()
        self.length = l

    def draw(self):
        turtle.clear()
        for _ in range(4):
            turtle.forward(self.length)
            turtle.right(90)

obj_list = [Line(300), Rectangle(100, 50), Circle(50), Square(100)]

for obj in obj_list:
    obj.draw()
turtle.done()