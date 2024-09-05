import turtle
import math

class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def getArea(self):
        area = self.width * self.height
        return area
    
    def getPerimeter(self):
        perimeter = 2 * (self.width + self.height)
        return perimeter
    
    def move(self, x, y):
        self.x = x
        self.y = y
    
    def intersect(self, rec):
        if self.x + self.width > rec.x and self.y + self.height > rec.y:
            x_value = rec.x
            y_value = rec.y
            width = self.width - x_value
            height = self.height - y_value
            return Rectangle(x_value, y_value, width, height)

    def draw(self):
        turtle.pensize(2)
        turtle.goto(self.x, self.y)
        for _ in range(2):          
            turtle.forward(self.width)
            turtle.left(90)
            turtle.forward(self.height)
            turtle.left(90)
        
rectangle_a = Rectangle(0,0, 250, 250)
rectangle_b = Rectangle(50,50, 250, 250)
recter_rec = rectangle_a.intersect(rectangle_b)
print("Rectangle Area: ", format(rectangle_a.getArea(), ".2f"))
print("Rectangle Perimeter: ", format(rectangle_a.getPerimeter(), ".2f"))

turtle.fillcolor("yellow")
turtle.begin_fill()
rectangle_a.draw()
turtle.end_fill()

turtle.fillcolor("blue")
turtle.begin_fill()
rectangle_b.draw()
turtle.end_fill()

turtle.fillcolor("green")
turtle.begin_fill()
recter_rec.draw()
turtle.end_fill()
turtle.done()

class Circle:
    def __init__(self, x,y,radius):
        self.x = x
        self.y = y
        self.radius = radius
   
    def getArea(self):
        area = math.pi * self.radius ** 2
        return area
    
    def getPerimeter(self):
        perimeter = 2 * math.pi * self.radius
        return perimeter
    
    def move(self, x, y):
        self.x = x
        self.y = y
        turtle.reset()
        self.draw()

    def draw(self):
        turtle.pensize(2)
        turtle.penup()
        turtle.goto(self.x, self.y-self.radius)
        turtle.pendown()
        turtle.circle(self.radius)   

# circle = Circle(2,3, 60)
# print("-----------------------")
# print("Circle Area: ", format(circle.getArea(), ".2f"))
# print("Circle Perimeter: ", format(circle.getPerimeter(), ".2f"))
# circle.draw()
# circle.move(40,5)
# turtle.done()