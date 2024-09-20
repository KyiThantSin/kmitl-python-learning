from tkinter import *
from tkinter import ttk

class Demo:
    def __init__(self):
        window = Tk()
        window.title("Grid Demo")

        frame_one = Frame(window)
        frame_one.pack()

        # variable
        self.v0 = IntVar()
        self.colorCode = IntVar()

        # initialize style
        style = ttk.Style()
        style.theme_use("clam") # to set background

        style.configure("Pink.TButton", background="pink", foreground = "grey")
        style.configure("Green.TButton", background="green", foreground = "grey")

        # checkbox
        checkBtn = Checkbutton(frame_one, text="Bold", variable= self.v0, command=self.processCheckButton) 
        checkBtn.grid(row=1, column=1)

        # radio btn so we need value 
        pinkRadioBtn = ttk.Radiobutton(frame_one, text="Pink", style='Pink.TButton', variable= self.colorCode, value= 0, command=self.processRadioButton)
        greenRadioBtn = ttk.Radiobutton(frame_one, text="green", style='Green.TButton', variable= self.colorCode, value= 2, command=self.processRadioButton)
        pinkRadioBtn.grid(row=1, column=2)
        greenRadioBtn.grid(row=1, column=3)
        window.mainloop()

    def processCheckButton(self):
       print("Check status", "checked" if self.v0.get() == 1 else "unchecked")
    
    def processRadioButton(self):
       print("Check color", "pink" if self.colorCode.get() == 0 else "green")

Demo()