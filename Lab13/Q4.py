import turtle
def cross(l, t):
    if t == 0:
        turtle.dot()
        return
    else :
        for i in range(4):
            turtle.speed(1)
            turtle.forward(l)
            cross(l/2, t-1)
            turtle.backward(l)
            turtle.right(90)
        # turtle.backward(l/2)
    
cross(100, 4)

# for i in range(4):
#         turtle.forward(l)
#         cross(l/2, t-1)
#         turtle.backward(l)    
#         turtle.left(90)
#  so close
