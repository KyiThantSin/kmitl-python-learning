import turtle

days_each_week = ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"]
days_each_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
start_day_of_month = [1, 4, 5, 1, 3, 6, 1, 4, 7, 2, 5, 7] 
box_width = 50
box_height = 30
start_x = -150
start_y = 200

def draw_box(t, x, y, width, height):
    t.penup()
    t.goto(x, y)
    t.pendown()
    for _ in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)

def draw_calendar(month):
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()

    month_names = ["January", "February", "March", "April", "May", "June", 
                   "July", "August", "September", "October", "November", "December"]
    t.penup()
    t.goto(start_x + box_width * 3.5, start_y + 40)
    t.write(f"{month_names[month-1]} 2024", align="center", font=("Arial", 16, "bold"))
    t.goto(start_x, start_y)
    t.pendown()

    for i, day in enumerate(days_each_week):
        draw_box(t, start_x + i * box_width, start_y, box_width, box_height)
        t.penup()
        t.goto(start_x + i * box_width + box_width / 2, start_y - box_height / 2 - 10)
        t.write(day, align="center", font=("Arial", 12, "normal"))
        t.pendown()

    first_day_of_month = start_day_of_month[month - 1]
    num_days = days_each_month[month - 1]
    
    current_x = start_x + (first_day_of_month - 1) * box_width
    current_y = start_y - box_height

    for day in range(1, num_days + 1):
        draw_box(t, current_x, current_y, box_width, box_height)
        t.penup()
        t.goto(current_x + box_width / 2, current_y - box_height / 2 - 10)
        t.write(day, align="center", font=("Arial", 12, "normal"))
        t.pendown()
        
        current_x += box_width
        if (first_day_of_month + day - 1) % 7 == 0:
            current_x = start_x
            current_y -= box_height

    remaining_days = (7 - (num_days + first_day_of_month - 1) % 7) % 7
    for _ in range(remaining_days):
        draw_box(t, current_x, current_y, box_width, box_height)
        current_x += box_width
        if current_x > start_x + 6 * box_width:
            current_x = start_x
            current_y -= box_height

    turtle.done()

draw_calendar(8)
