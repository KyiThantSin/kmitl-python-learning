from tkinter import *

class GridManager:
    window = Tk()
    window.title("Gride Manager")
    message = Message(window, text="This is Message Widget")
    Label(window, text="First Name").grid(row=1, column=2)
    Entry(window).grid(row=1, column=8, padx=5, pady=5)

    Label(window, text="Last Name").grid(row=2, column=2)
    Entry(window).grid(row=2, column=8, padx=5, pady=5 )
    


    window.mainloop()

GridManager()