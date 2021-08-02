from turtle import *
bgcolor("black")
color('white')
i=2
color("blue","red")
begin_fill()
speed(0)
ct=0
while True:
    ct=ct+0
    begin_fill()
    i=i+1.22
    forward(2+i)
    left(90)
    forward(2+i)
    left(90)
    forward(2+i)
    left(90)
    forward(2+i)
    if ct==5:
        quit()
        end_fill()
        done

