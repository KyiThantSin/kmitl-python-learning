# moving tutle pen
import turtle
import tkinter as TK

turtle.goto(0, 50)
turtle.penup()
# x = 50, y = - 90
turtle.goto(50, -60)
turtle.pendown()
turtle.color("green")
turtle.circle(50)

turtle.color("white")

turtle.goto(50, -98)
turtle.color("blue")
turtle.write("Green Circle")

turtle.done()