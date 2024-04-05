from tkinter import * 
from tkinter import messagebox
import random

from tkinter import *

class Paint:
    def __init__(self):
        window = Tk()
        window.title("A circle random color.")
        self.canvas = Canvas(window, bg="white", width=600, height=400)
        self.canvas.pack(fill=BOTH, expand=True)
        self.displayrec()
        self.canvas.bind("<Button-1>", self.draw)
        
        window.mainloop()

    def displayrec(self):
        self.canvas.create_rectangle(50, 50, 400, 250, outline="black", tags = "rec")
        
    def draw(self,event):
        x1, y1= event.x, event.y
        color = ["yellow", "black", "red", "green", "brown", "blue", "white", "brown", "pink", "purple"]
        if 50 <= x1 <= 400 and 50 <= y1 <= 250:
            self.canvas.create_oval(x1, y1, x1+10, y1+10, fill = random.choice(color))
        else:
            messagebox.showwarning("Warning", "Mouse pointer is not in the rectangle")

Paint()

