from turtle import *
bgcolor("black")
speed(0)
shape("turtle")
i=1
while i<125:
    i=i+1.5
    forward(20+i)
    color("magenta")
    left(60)
    forward(20+i)
    color("cyan")
    left(60)
    forward(20+i)
    color("white")
done()
