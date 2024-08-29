import turtle
import math
turtle.pensize(2)

# turtle.forward(100)
# turtle.left(90)
# turtle.forward(100)
# turtle.left(135)
# turtle.forward(100 * math.sqrt(2))

def square(n):
    for i in range(4):
        turtle.forward(n)
        turtle.right(90)

def draw_square(s,g):
    while s > 20:
        square(s)
        s -= (g * 2)
        turtle.penup()
        turtle.forward(g)
        turtle.right(90)
        turtle.forward(g)
        turtle.left(90)
        turtle.pendown()
    turtle.done()

draw_square(200,20)


