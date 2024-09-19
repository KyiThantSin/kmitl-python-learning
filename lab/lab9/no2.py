from tkinter import *
from tkinter import messagebox

class CurrencyExchange:
    def __init__(self):
        window = Tk()
        window.title("Currency Exchange")
        
        self.value = IntVar()  
        self.result = 0
        
        Label(window, text="Enter value:").pack()
        self.entry = Entry(window, textvariable=self.value)  
        self.entry.pack()

        btnUsdToThb = Button(window, text="USD -> THB", fg="black", background="whitesmoke", command=self.usdToThb)
        btnThbToUsd = Button(window, text="THB -> USD", fg="black", background="whitesmoke", command=self.thbToUsd)

        btnUsdToThb.pack()
        btnThbToUsd.pack()

        window.mainloop()

    def usdToThb(self):
        try:
            value = float(self.value.get())
            self.result = format(value * 30, ".2f")
            messagebox.showinfo("USD to THB", f"{value} USD = {self.result} THB")
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid number")

    def thbToUsd(self):
        try:
            value = float(self.value.get()) 
            self.result = format(value / 30, ".2f")
            messagebox.showinfo("THB to USD", f"{value} THB = {self.result} USD")
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid number")

CurrencyExchange()
