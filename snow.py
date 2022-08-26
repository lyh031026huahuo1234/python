import turtle

def snow(n,size):
    if(n==0):
        turtle.fd(size)
    else:
        for angle in [0,60,-120,60]:
            turtle.left(angle)
            snow(n-1,size/3)

turtle.setup(1800,1800)
turtle.speed(10000000)
turtle.penup()
turtle.goto(-200,-100)
turtle.pendown()
turtle.pensize(2)
snow(6,800)
turtle.right(120)
snow(6,800)
turtle.right(120)
snow(6,800)
turtle.done()
