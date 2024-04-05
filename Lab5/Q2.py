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
        turtle.goto(x, y)
        turtle.pendown()
        for k in range(4):
            turtle.pendown
            turtle.right(90)
            turtle.forward(l)
        x += l
    turtle.penup()
    x = -80
    y -= l
turtle.done()
# turtle.penup()
#         turtle.goto(-80 + l, y - l)
#         turtle.pendown()
# # turtle.penup()
#         turtle.goto(x,y)
#         turtle.pendown()
#         turtle.forward(l)
#         turtle.right(90)
#         turtle.forward(l)
#         turtle.right(90)
#         turtle.forward(l)
#         turtle.right(90)
#         turtle.forward(l)
#         turtle.right(90) 
#         turtle.penup()