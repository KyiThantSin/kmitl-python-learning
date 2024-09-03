import turtle

month_names = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
week_days = ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"]
days_per_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
start_day_of_month = [1, 4, 5, 1, 3, 6, 1, 4, 0, 2, 5, 0]

calendar_size = 250
cell_width = calendar_size / 7
cell_height = calendar_size / 10

def box(width, height):
    turtle.pensize(2)
    for _ in range(2):
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)

def draw_calendar():
    turtle.pensize(2)
    month = int(input("Please enter month of the year(1-12): "))
    box(calendar_size, cell_height)

    turtle.penup()
    x, y = turtle.position()
    turtle.goto(x + 75, y - 20)
    turtle.write(f"{month_names[month - 1]} 2024", align="left", font=("Ariel", 14, "normal"))
    turtle.goto(x, y)
    turtle.pendown()
    turtle.right(90)
    turtle.forward(cell_height)
    turtle.left(90)

    day_count = 1 
    for row in range(7):
        for col in range(7):
            box(cell_width, cell_height)

            if row == 0:
                turtle.penup()
                x, y = turtle.position()
                turtle.goto(x + 8, y - 20)
                turtle.write(week_days[col], align="left", font=("Ariel", 14, "normal"))
                turtle.goto(x, y)
                turtle.pendown()

            else:
                if (row >= 2 or col + 1 >= start_day_of_month[month - 1]) and day_count <= days_per_month[month - 1]:
                    turtle.penup()
                    x, y = turtle.position()
                    turtle.goto(x + 25, y - 20)
                    turtle.write(day_count, align="right", font=("Ariel", 14, "normal"))
                    turtle.goto(x, y)
                    turtle.pendown()
                    day_count += 1
            turtle.forward(cell_width)
           
        turtle.backward(calendar_size)
        turtle.right(90)
        turtle.forward(cell_height)
        turtle.left(90)

    turtle.done()

draw_calendar()