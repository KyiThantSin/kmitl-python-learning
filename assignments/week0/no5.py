import turtle

#for point 1
x1 = float(input("Enter x1 for point p1: "))
y1 = float(input("Enter y1 for point p1: "))

# for point p2
x2 = float(input("Enter x2 for point p2: "))
y2 = float(input("Enter y2 for point p2: "))

# for point p3
x3 = float(input("Enter x3 for point p3: "))
y3 = float(input("Enter y3 for point p3: "))

area =  0.5 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))

turtle.color("black")
turtle.pensize(2)
turtle.penup()
turtle.goto(x1, y1)
turtle.pendown()
turtle.goto(x2, y2)
turtle.goto(x3, y3)
turtle.goto(x1, y1)
turtle.penup()
turtle.goto(x1 + 50, y1 - 50)
turtle.write(f"Area of the Triangle: {area}")

turtle.done()

