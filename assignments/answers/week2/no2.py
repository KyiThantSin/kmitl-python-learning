import turtle

#constant variables
days_each_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days_each_week = ["Su", "Mo", "Tu", "We", "Th", "Fr", "Sa"]
day_start = [2, 5, 6, 2, 4, 7, 2, 5, 1, 3, 6, 1]
table_length = 250
box_width = table_length / 7
box_height = 25
table_gap = 70

def print_calendar():
    
    turtle.speed(0)
    turtle.penup()
    turtle.goto(-600, 400) # start position
    turtle.pendown()
    i = 0
    while i < 12:
        if i in [4, 8]: 
            turtle.penup()
            turtle.backward((table_length + table_gap) * 4)
            turtle.right(90)
            turtle.forward(box_height * 8 + table_gap)
            turtle.left(90)
            turtle.pendown()
        
        # print the header row with month name
        turtle.forward(table_length)
        turtle.right(90)
        turtle.forward(box_height)
        turtle.right(90)
        turtle.forward(table_length)
        turtle.right(90)
        turtle.forward(box_height)

        # adjust position to print text, then move back to the current position
        x, y = turtle.position()
        turtle.penup()
        turtle.goto(x + 40, y - box_height / 2 - 7)
        turtle.pendown()
        turtle.write(f"Month#{i + 1}", align="center", font=("Ariel", 10, "normal"))
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()

        turtle.backward(box_height)
        turtle.right(90)
        days = 1
        j = 0
        while j < 7:  # for loops be more preferable
            k = 0
            while k < 7:
                for _ in range(2):

                    turtle.forward(box_width)
                    turtle.right(90)
                    turtle.forward(box_height)
                    turtle.right(90)

                x, y = turtle.position()
                
                turtle.penup()
                if j == 0:
                    # print the row for 7 days
                    turtle.goto(x + 15, y - box_height / 2 - 7)
                    turtle.pendown()
                    turtle.write(f"{days_each_week[k]}", align="center", font=("Ariel", 10, "normal"))
                
                else:
                    turtle.goto(x + 10, y - box_height / 2 - 7)
                    turtle.pendown()
                    if days <= days_each_month[i] and (k >= day_start[i] - 1 or j >= 2):
                        turtle.write(f"{days}", align="left", font=("Ariel", 10, "normal"))
                        days += 1
                turtle.penup()
                turtle.goto(x, y)
                turtle.pendown()
                turtle.forward(box_width)
                k += 1
            
              
            turtle.backward(table_length)
            turtle.right(90)
            turtle.forward(box_height)
            turtle.left(90)
            j += 1
        

        turtle.penup()
        turtle.forward(table_length + table_gap)
        turtle.left(90)
        turtle.forward(box_height * 8)
        turtle.right(90)
        turtle.pendown()
        i += 1
    turtle.done()

print_calendar()