import abc
import turtle as t

class TwoDShape(abc.ABC):
    # def __init__(self, x= 0, y=0, l= 0, h= 0, r= 0):
    #     self.x = 0
    #     self.y = 0
    #     self.length = l
    #     self.height = h
    #     self.radius = r
    
    
    @abc.abstractclassmethod
    def draw(self):
        pass

class Line(TwoDShape):
    def __init__(self, x1, y1, x2, y2):
        # super().__init__(self, )
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        
    def draw(self):
        t.penup()
        t.goto(self.x1, self.y1)
        t.pendown()
        t.goto(self.x2, self.y2)
        t.penup()
        # t.forward(self.length)
        
class Rectangle(TwoDShape):
    def __init__(self, x1, y1, l, h):
        # super().__init__(self, l, h)
        self.length = l
        self.height = h
        self.x = x1
        self.y = y1
        
    def draw(self):
        t.penup()
        t.goto(self.x, self.y)
        t.pendown()
        t.goto(self.x + self.height , self.y )
        t.goto(self.x + self.height, self.y + self.length)
        t.goto(self.x, self.y + self.length)
        t.goto(self.x, self.y)
        t.penup()
        
    
class Circle(TwoDShape):
    def __init__(self, x1, y1, r):
        # super().__init__(self, r)
        self.radius = r
        self.x = x1
        self.y = y1
    
    def draw(self):
        t.penup()
        t.goto(self.x , self.y - self.radius)
        t.pendown()
        t.circle(self.radius)
        t.penup()

class Square(TwoDShape):
    def __init__(self, x1, y1, l):
        # super().__init__(self, l)
        self.length = l
        self.x = x1
        self.y = y1
    
    def draw(self):
        t.penup()
        t.goto(self.x, self.y)
        t.pendown()
        t.goto(self.x + self.length, self.y)
        t.goto(self.x + self.length, self.y + self.length)
        t.goto(self.x, self.y + self.length)
        t.goto(self.x, self.y)
        t.penup()
        
        
        
sq1 = Square(0,0, 50)
sq1.draw()
rec1 = Rectangle(70,0, 50, 80)
rec1.draw()


sq2 = Square(50,100, 50)
sq2.draw()
line = Line(50, 0, 100, 100)
line.draw()


sq3 = Square(100,0, 50)
sq3.draw()
circle = Circle(125, 25, 10)
circle.draw()

sq4 = Square(150,0, 50)
sq4.draw()
line2 = Line(160, 0, 190, 80)
line2.draw()

sq5 = Square(200,0, 50)
sq5.draw()
circle2 = Circle(225, 25, 10)
circle2.draw()


# for x in [l1, l2, c1, c2, r1, sq]:
#     x.draw()

# print(list)
t.done()
