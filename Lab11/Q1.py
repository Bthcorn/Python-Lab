import math
class Point(object):
    def __init__(self, x= 0.00, y= 0.00):
        self.x = x
        self.y = y
        
    def printInfo(self):
        print(f"Position: {self.x},{self.y};")
        
class Circle(Point):
    def __init__(self, x=0, y=0, radius = 0.00):
        super().__init__(x, y)
        self.radius = radius
        
    def area(self):
        return math.pi * self.radius ** 2
    
    def printInfo(self):
        a = self.area()
        print(f"Position: {self.x}, {self.y}; Radius: {self.radius}; Area: {a}")
        
point = Point(30, 50)
point.printInfo()
circle = Circle(120, 89, 2.7)
circle.printInfo()