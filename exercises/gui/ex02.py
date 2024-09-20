from tkinter import *
from tkinter import ttk

window = Tk()
style = ttk.Style()

style.theme_use('clam')
style.configure('Pink.TButton', background = "black", foreground="white")

btnShowOrHide = ttk.Button(window, text="show", style="Pink.TButton" )
btnShowOrHide["text"] = "Hide"
# btnShowOrHide["bg"] = "red"
# btnShowOrHide["fg"] = "#000"
btnShowOrHide["cursor"] = "plus"
# btnShowOrHide["justify"] = RIGHT
btnShowOrHide.pack(pady=20)

window.mainloop()
