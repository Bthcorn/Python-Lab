import turtle as t
def draw_polygon(x, y, a=4, b=100):
    t.penup()
    t.goto(x, y)
    t.pendown()
    for i in range(a): 
        t.lt(360/a)
        t.fd(b)

draw_polygon(0,0)
draw_polygon(10,10,6)
draw_polygon(10,10,5,200)
t.done()