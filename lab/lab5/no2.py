import turtle

n = int(input("Enter the number of rows amd columns: "))

size = 100 / n
turtle.speed(5)

for i in range(n):
    for j in range(n):
        for _ in range(n - 1):
            turtle.forward(size)
            turtle.right(90)
        turtle.forward(size)
    turtle.backward(size * n)
    turtle.right(90)
    turtle.forward(size)
    turtle.left(90)

turtle.done()