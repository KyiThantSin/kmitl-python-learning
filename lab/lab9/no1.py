from tkinter import *

class Counting:
    def __init__(self, count):
        self.count = count
        window = Tk()
        btPlus = Button(window, text="+", fg="black", bg="whitesmoke", command=self.countUp)
        btMinus = Button(window, text="-",fg="black", bg="whitesmoke",  command=self.countDown)
        btreset = Button(window, text="Reset",fg="black", bg="yellow",  command=self.reset)
        self.label = Label(window, text=self.count)
        self.label.grid(row=0, column=0, padx=10, pady=10)
        btPlus.grid(row=0, column=1, padx=10, pady=10)
        btMinus.grid(row=1, column=1, padx=10, pady=10)
        btreset.grid(row=2, column=1, padx=10, pady=10)

        window.mainloop()

    def countUp(self):
        self.count += 1
        self.label['text'] = self.count
    
    def countDown(self):
        self.count -= 1
        self.label['text'] = self.count
    
    def reset(self):
        self.count = 0
        self.label['text'] = self.count



Counting(0)