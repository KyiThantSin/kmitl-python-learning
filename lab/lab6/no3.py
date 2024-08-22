import turtle
x = 0
y = 0
def draw_polygon(type = 10, length = 100):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.circle(length / 2, steps = type)

def main():
    draw_polygon()
    turtle.done()

main()
