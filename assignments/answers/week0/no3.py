import turtle

length = float(input("Enter the length of the star's points: "))
angle = 180 - 36

for _ in range(5):
        turtle.pensize(2)
        turtle.forward(length)
        turtle.right(angle)

turtle.done()