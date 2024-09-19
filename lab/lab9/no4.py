from tkinter import *
from tkinter import messagebox
import random

class Spinner:
    def __init__(self) -> None:
        window = Tk()
        window.title = "A simple paint program"

        self.canvas = Canvas(window, width=600, height=300, bg="white")
        self.canvas.pack()

        self.x0, self.y0, self.x1, self.y1 = 100, 250, 450, 50

        self.canvas.create_rectangle(self.x0, self.y0, self.x1, self.y1, width=2)
        self.canvas.bind("<Button-1>", self.draw_oval)
        window.mainloop()
        

    def draw_oval(self, event):
        colors = ["yellow", "red", "black", "orange", "pink", "green"]
        
        if event.x <= self.x0 or event.x >= self.x1 or event.y <= self.y1 or event.y >= self.y0:
            messagebox.showwarning("Warning", "Mouse pointer is not in the rectangle.")
        else:
            self.canvas.create_oval(event.x, event.y, event.x - 5, event.y - 5, fill=random.choice(colors))
        
        

Spinner()