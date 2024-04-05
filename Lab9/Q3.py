# from tkinter import *

# class Paint:
#     def __init__(self):
#         window = Tk()
#         window.title("A simple paint program")
        
#         self.canvas = Canvas(window, width = 500, height = 500, bg ="white")
#         self.canvas.pack()
        
#         self.canvas.bilnd("<Botton-1>")
        
#         btClear = Button(window, text = "Clear", command = self.clearCanvas)
        
#         btClear.grid(row = 1, column = 7)
        
    
#     def clearCanvas(self):
        
        
# Paint()

from tkinter import *

class Painting:
    def __init__(self):
        window = Tk()
        window.title("Painting")
        self.canvas = Canvas(window, width = 400, height = 200,bg="white")
        self.canvas.bind('<B1-Motion>', self.draw)
        self.canvas.pack()

        label = Label(window, text="Drag the mouse to draw!")
        clearbtn = Button(window, text="Clear", command=self.clear)
        
        self.canvas.grid(row=1)
        label.grid(row=2,columnspan=10)
        clearbtn.grid(row=3,columnspan=10)

        window.mainloop()

    def clear(self):
        self.canvas.delete("drawing")

    def draw(self,event):
        x1, y1, x2, y2 = ( event.x - 3 ),( event.y - 3 ), ( event.x + 3 ),( event.y + 3 )
        color = "#000000"
        self.canvas.create_oval(x1,y1,x2,y2,fill=color,tags="drawing")
        print(event)

Painting()