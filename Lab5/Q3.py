import turtle
n = int(input("Enter the N: "))
l = 100/n
x = -80
y = 80
for i in range(1,n+1):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    for j in range(1,n+1):
        if (i+j) % 2 == 0:
            turtle.goto(x, y)
            turtle.pendown()
            turtle.fillcolor("#90b7be")
            turtle.begin_fill()
            for k in range(4):
                turtle.pendown
                turtle.right(90)
                turtle.forward(l)
        else:
            turtle.goto(x, y)
            turtle.pendown()
            for k in range(4):
                turtle.pendown
                turtle.right(90)
                turtle.forward(l)
        x += l
        turtle.end_fill()
    turtle.penup()
    x = -80
    y -= l
turtle.done()