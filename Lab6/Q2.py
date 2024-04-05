import turtle as t


def square(x):
    t.penup()
    t.goto(0, x)
    t.pendown()
    t.setheading(90)
    t.lt(90)
    t.fd(x)
    t.lt(90)
    t.fd(2*x)
    t.lt(90)
    t.fd(2*x)
    t.lt(90)
    t.fd(2*x)
    t.lt(90)
    t.fd(x)
    t.penup()

i = 1
j = 1
t.speed(0.5)
def main():
    global i
    global j
    y = 0
    x = int(input("Enter an integer: "))
    while i < 5:
        square(x*i)
        i += 1
    
    while j < 5:
        t.goto(0,0)
        t.lt(90 + y)
        t.pendown()
        t.fd(4*x)
        y += 90*y
        j += 1
    
main()
t.done()
