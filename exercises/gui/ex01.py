from tkinter import *
from tkinter import ttk

def processOk():
    print("Ok")

window = Tk()

style = ttk.Style()

style.theme_use('clam')

style.configure('Pink.TButton', background = "pink", foreground="white")
style.configure('Red.TButton', background = "yellow", foreground="white")

btOk = ttk.Button(window, text="Ok", style='Pink.TButton', command=processOk)
btCancel = ttk.Button(window, text="Cancel", style='Red.TButton', command=processOk)
btCancel.pack(pady=20)
btOk.pack(pady=20)

window.mainloop()
