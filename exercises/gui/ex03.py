from tkinter import *
from tkinter import ttk

class Demo:
    def __init__(self):
        window = Tk()
        window.title("Grid Demo")

        frame_one = Frame(window)
        frame_one.pack()

        # variables
        self.v0 = IntVar()
        self.colorCode = IntVar()
        self.name = StringVar()

        # initialize style
        style = ttk.Style()
        style.theme_use("clam")  # to set background

        # configure radiobutton styles
        style.configure("Pink.TRadiobutton", background="pink", foreground="black")
        style.configure("Green.TRadiobutton", background="green", foreground="black")

        # configure button style using map for state-specific styling
        style.configure("Blue.TButton", background="lightblue")
        style.map("Blue.TButton",
                  foreground=[('pressed', 'white'), ('active', 'white'), ('!disabled', 'black')])

        # checkbox
        checkBtn = Checkbutton(frame_one, text="Bold", variable=self.v0, command=self.processCheckButton)
        checkBtn.grid(row=1, column=1)

        frame_two = Frame(window)
        frame_two.pack()

        # radio buttons with specific styles
        pinkRadioBtn = ttk.Radiobutton(frame_two, text="Pink", style='Pink.TRadiobutton', variable=self.colorCode, value=0, command=self.processRadioButton)
        greenRadioBtn = ttk.Radiobutton(frame_two, text="Green", style='Green.TRadiobutton', variable=self.colorCode, value=2, command=self.processRadioButton)
        
        pinkRadioBtn.grid(row=1, column=2)
        greenRadioBtn.grid(row=1, column=3)

        # input box and button
        entryName = Entry(frame_two, textvariable=self.name)
        btGetName = ttk.Button(frame_two, text="Get Name", style='Blue.TButton', command=self.getName)

        entryName.grid(row=2, column=1)
        btGetName.grid(row=2, column=2)

        window.mainloop()

    def processCheckButton(self):
        print("Check status", "checked" if self.v0.get() == 1 else "unchecked")

    def processRadioButton(self):
        print("Check color", "pink" if self.colorCode.get() == 0 else "green")

    def getName(self):
        print("Name is", self.name.get())

Demo()
