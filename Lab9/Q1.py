from tkinter import *

window = Tk()
window.title("Spinner")
value = IntVar(window, 0)

def add():
    global value
    value.set(value.get() + 1)
    return value
    
def subtract():
    global value
    value.set(value.get() - 1)
    return value

def reset():
    global value
    value.set(0)
    return value
    
message = Label(window, textvariable = value)
message.grid(row = 1, column = 1, rowspan = 3,  columnspan = 2)
Button(window, text = "+", command = add).grid(row = 1, column = 3, columnspan = 3)
Button(window, text = "-", command = subtract).grid(row = 2, column = 3, columnspan= 3 )
Button(window, text = "reset", command = reset).grid(row = 3, column = 3, columnspan= 3)

window.mainloop()

