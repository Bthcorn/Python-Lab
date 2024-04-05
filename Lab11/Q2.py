
class Calculator(object):
    def __init__(self):
        self.acc = 0.00
    
    def set_accumulator(self, acc):
        self.acc = acc
        
    def get_accumulator(self):
        return self.acc
    
    def add(self, x):
        self.acc += x
    
    def substract(self, x):
        self.acc -= x
    
    def multiply(self, x):
        self.acc *= x
    
    def divide(self, x):
        if x == 0:
            raise ValueError("Cannot divide by 0.")
        self.acc /= x
    
    def print_result(self):
        print(f"Result: {self.acc}")
        

class Sci_calc(Calculator):
    def __init__(self):
        super()
        self.acc = 0.00
    
    def square(self):
        self.acc = self.acc ** 0.5
        
    def exp(self, x):
        self.acc = self.acc ** x
        
    def factorial(self):
        n = self.acc
        while n > 1:
            self.acc *= (n - 1)
            n -= 1
        
    def print_result(self):
        print(f"Result: {self.acc:.2e}")
    
        
x = Calculator()
x.set_accumulator(20)
x.substract(10)
x.multiply(40)
x.divide(4)
x.print_result()

a = Sci_calc()
a.set_accumulator(5)
a.factorial()
a.add(20)
a.print_result()