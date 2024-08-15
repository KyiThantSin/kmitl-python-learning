import turtle

n = int(input("Enter the number of rows amd columns: "))

size = 100 / n
turtle.speed(5)

for i in range(n):
    for j in range(n):
        if (i + j)%2 == 0:
            turtle.fillcolor("black")
        else:
            turtle.fillcolor("white")
        turtle.begin_fill()

        for _ in range(n - 1):
            turtle.forward(size)
            turtle.right(90)
        turtle.end_fill()
        turtle.forward(size)

    turtle.backward(size * n)
    turtle.right(90)
    turtle.forward(size)
    turtle.left(90)

turtle.done()