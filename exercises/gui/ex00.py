from tkinter import *

def clickMe():
    print("Click me")

window = Tk()
label = Label(window, text="Welcome to Python")
button = Button(window, text="Click me", command=clickMe)

label.pack()
button.pack()

window.mainloop()