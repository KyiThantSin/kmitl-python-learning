import turtle

def draw_bar(height, char):
    width = 20
    turtle.fillcolor("purple")
    
    for i in range(2):
        turtle.begin_fill()

        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)

        turtle.end_fill()

    x, y = turtle.position()
    turtle.penup()
    turtle.goto(x + 5, y - 15)
    turtle.write(char)
    turtle.goto(x, y)
    turtle.pendown()
    turtle.forward(width)


def nums_frequency_histogram():
    arr = [1, 2, 2, 1, 3, 4, 6, 5, 3, 4, 5, 6, 4, 3, 5, 4, 5, 3, 4, 4, 3, 3, 4, 3, 3, 4, 4, 4]
    arr.sort()
    unique_nums = list()
    unique_nums_count = list()
    space = 35

    for i in arr:
        if i not in unique_nums:
            unique_nums.append(i)
    for i in unique_nums:
        unique_nums_count.append(arr.count(i))

    turtle.left(90)
    turtle.forward(max(unique_nums_count) * 20)
    turtle.backward(max(unique_nums_count) * 20)
    turtle.right(90)
    turtle.forward(space)
    
    for i in range(len(unique_nums)):
        draw_bar(unique_nums_count[i] * 20, unique_nums[i])
    turtle.forward(space)

    turtle.done()

nums_frequency_histogram()