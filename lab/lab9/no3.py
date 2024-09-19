from tkinter import *
from tkinter import messagebox

class Spinner:
    def __init__(self) -> None:
        window = Tk()
        window.title = "A simple paint program"

        self.canvas = Canvas(window, width=600, height=300, bg="white")
        self.canvas.pack()
        button1 = Button(window, width=20, height=3, text="Drag the mouse to draw")
        button2 = Button(window, width=20, height=3, text="Clear", command=self.clear)

        button1.pack()
        button2.pack()

        self.canvas.bind("<Button-1>", self.click)
        self.canvas.bind("<B1-Motion>", self.move)

        window.mainloop()
        
    def click(self, click_event):
        self.prev_x = click_event.x
        self.prev_y = click_event.y

    def move(self, move_event):

        self.canvas.create_line(self.prev_x, self.prev_y, move_event.x, move_event.y, width=2)

        self.prev_x = move_event.x
        self.prev_y = move_event.y

    def clear(self):
        self.canvas.delete("all")
        

Spinner()