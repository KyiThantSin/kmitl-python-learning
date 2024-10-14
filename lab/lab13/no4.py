import turtle
import random

turtle.speed(0)
turtle.Turtle()

def cross(width, times):
    if times == 0:
        hexadecimal = "#" + ''.join([random.choice("ABCDEF0123456789") for i in range(6)])
        turtle.dot(3, hexadecimal)
        return 
    else:
        for i in range(4):
            turtle.forward(width)
            cross(width/2, times-1)
            turtle.right(180)
            turtle.forward(width)
            turtle.left(90)

cross(100, 4)
turtle.update()
turtle.done()