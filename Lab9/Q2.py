from tkinter import *
from tkinter import messagebox

class CurrencyConvert:
    def __init__(self):
        window = Tk()
        window.title("Currency Converter")
        self.v3 = IntVar()
    
        Entry(window, width = 5, textvariable = self.v3).grid(row=1,column=1,columnspan=10,rowspan=1)
        Button(window, text = "USD -> THB", command = self.thb).grid(row = 2, column = 1, columnspan = 3)
        Button(window, text = "THB -> USD", command = self.usd).grid(row = 3, column = 1, columnspan = 3)
        
        window.mainloop()
        
    def thb(self):
        usd = self.v3.get()
        thb = usd * 30
        messagebox.showinfo("USD -> THB", f"{usd:.2f} USD = {thb:.2f} THB")
    
    def usd(self):
        thb = self.v3.get()
        usd = thb / 30
        messagebox.showinfo("USD -> THB", f"{thb:.2f} THB = {usd:.2f} USD")
        
CurrencyConvert()
        