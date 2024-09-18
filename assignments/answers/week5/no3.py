import turtle

def calculate_char_frequency(text):
    text = text.replace(" ", "")
    unique_chars = []
    for char in text:
        if char not in unique_chars:
            unique_chars.append(char)
    frequencies = []
    for char in unique_chars:
        count = 0
        for c in text:
            if c == char:
                count += 1
        frequencies.append(count)
    return unique_chars, frequencies

def draw_bar_graph(chars, frequencies):
    turtle.setup(width=600, height=400)
    screen = turtle.Screen()
    screen.setworldcoordinates(0, 0, len(chars) * 40, max(frequencies) * 20 + 20)

    t = turtle.Turtle()
    t.penup()
    t.goto(20, 0)
    t.pendown()

    for i in range(len(chars)):
        height = frequencies[i] * 20
        t.begin_fill()
        t.forward(30)
        t.left(90)
        t.forward(height)
        t.left(90)
        t.forward(30)
        t.left(90)
        t.forward(height)
        t.left(90)
        t.end_fill()
        t.penup()
        t.forward(40)
        t.pendown()

    t.penup()
    t.goto(15, -15)
    for char in chars:
        t.write(char, align="center", font=("Arial", 12, "normal"))
        t.forward(40)

    turtle.done()

user_input = input("Enter some text: ")
chars, frequencies = calculate_char_frequency(user_input)
draw_bar_graph(chars, frequencies)
