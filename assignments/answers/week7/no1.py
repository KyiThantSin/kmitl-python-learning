import turtle
data = [3,1,3,3,2,3,3,2,3,2,4,3,3,3,3,3,4,3,4,3,3,3,3,4,3]

def pie_chart(data):
    unique_numbers = set(data)
    counts = {}
    colors = ["red", "blue", "pink", "yellow"]
    turtle.bgcolor("white")
    start_angle = 0

    for i in unique_numbers:
        counts[i] = data.count(i)
    
    for i, (number, count) in enumerate(counts.items()):
        angle = (count / len(data)) * 360
        turtle.fillcolor(colors[i % len(colors)])
        turtle.begin_fill()
        turtle.forward(100)
        turtle.left(90)
        turtle.circle(100, angle)
        turtle.left(90)
        turtle.forward(100)

        turtle.end_fill()
        start_angle += angle
        turtle.setheading(start_angle)

    turtle.hideturtle()
    turtle.done()

pie_chart(data)