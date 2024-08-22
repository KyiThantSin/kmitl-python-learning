import turtle
x = 50

def draw_square(x):
    turtle.pensize(2)
    turtle.forward(x)
    turtle.left(90)
    turtle.forward(x)
    turtle.left(90)
    turtle.forward(x)
    turtle.left(90)
    turtle.forward(x)
    turtle.left(90)

def second_square(x):
     turtle.pensize(2)
     for j in range(4):
         for i in range(4):
             draw_square(x)
             x += 50
         turtle.right(90)
         x=50     

     turtle.done()

second_square(x)
