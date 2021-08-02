#Use for loop, range and draw a spiral pattern using turtle
from turtle import *
for i in range(130):
    color('black')
    width(2)
    speed(0)
    circle(5+i,45)
exitonclick()