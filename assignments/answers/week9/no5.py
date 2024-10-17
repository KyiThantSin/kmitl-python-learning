from abc import ABC, abstractmethod
import turtle

class Char(ABC):
    @abstractmethod
    def draw(self, x, y):
        pass

    @abstractmethod
    def getWidth(self):
        pass

class Char0(Char):
    def draw(self, x, y):
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.circle(50)

    def getWidth(self):
        return 100

class Char1(Char):
    def draw(self, x, y):
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.left(90)
        turtle.forward(100)
        turtle.right(90)

    def getWidth(self):
        return 50

class Char2(Char):
    def draw(self, x, y):
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.forward(50)
        turtle.right(90)
        turtle.forward(50)
        turtle.right(90)
        turtle.forward(50)
        turtle.left(90)
        turtle.forward(50)
        turtle.left(90)
        turtle.forward(50)

    def getWidth(self):
        return 50

class Char3(Char):
    def draw(self, x, y):
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.forward(50)
        turtle.right(90)
        turtle.forward(50)
        turtle.right(90)
        turtle.forward(50)
        turtle.left(180)
        turtle.forward(50)
        turtle.right(90)
        turtle.forward(50)
        turtle.right(90)
        turtle.forward(50)

    def getWidth(self):
        return 50

class Char4(Char):
    def draw(self, x, y):
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.right(90)
        for _ in range(3):
            turtle.forward(100)
            turtle.left(90)
        turtle.left(90)
        turtle.forward(200)
    


    def getWidth(self):
        return 50

class Char5(Char):
    def draw(self, x, y):
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.forward(50)
        turtle.left(90)
        turtle.forward(50)
        turtle.left(90)
        turtle.forward(50)
        turtle.right(90)
        turtle.forward(50)
        turtle.right(90)
        turtle.forward(50)

    def getWidth(self):
        return 50

class Char6(Char):
    def draw(self, x, y):
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        for _ in range(4):
            turtle.forward(100)
            turtle.right(90)
        turtle.left(90)
        
        turtle.forward(100)
        turtle.right(90)
        turtle.forward(100)

    def getWidth(self):
        return 50

class Char7(Char):
    def draw(self, x, y):
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.forward(50)
        turtle.right(90)
        turtle.forward(100)

    def getWidth(self):
        return 50

class Char8(Char):
    def draw(self, x, y):
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.circle(25, 360)
        turtle.penup()
        turtle.goto(x, y - 50)
        turtle.pendown()
        turtle.circle(25, 360)

    def getWidth(self):
        return 50

class Char9(Char):
    def draw(self, x, y):
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        for _ in range(4):
            turtle.forward(100)
            turtle.left(90)
        turtle.forward(100)
        turtle.right(90)
        turtle.forward(100)
        turtle.right(90)
        turtle.forward(100)

    def getWidth(self):
        return 50

def drawNum(x):
    digits = {
        '0': Char0(),
        '1': Char1(),
        '2': Char2(),
        '3': Char3(),
        '4': Char4(),
        '5': Char5(),
        '6': Char6(),
        '7': Char7(),
        '8': Char8(),
        '9': Char9(),
    }

    if isinstance(x, int):
        x = str(x)

    for digit in x:
        if digit in digits:
            digits[digit].draw(0, 0)
            turtle.setheading(0)

drawNum("5")
turtle.done()