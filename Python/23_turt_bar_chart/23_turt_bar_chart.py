
import turtle
import pandas as pd
stud = pd.read_excel('Grades.xlsx')
mar = stud["marks"]
stu = stud["students"]
dist = []
fclass = []
sclass = []
ps = []
fl = []
for i in stud["marks"]:
    try:
        int(i)
    except:
        quit()
    if i >= 80:
        dist.append(i)
    elif i >= 65 and i < 80:
        fclass.append(i)
    elif i >= 55 and i < 80:
        sclass.append(i)
    elif i >= 36 and i < 50:
        ps.append(i)
    elif i > 0 and i < 36:
        fl.append(i)
wn = turtle.Screen()
tt = turtle.Turtle()
turtle.speed(00)
wn.bgcolor("darkgrey")
border = 8
wn.setworldcoordinates(0-border, 0-border, 80*len(mar)+border, max(mar)+(border*10))
import random
tt.width(3)
colors = ["cyan", "purple", "green", "blue", "white", "grey","yellow", "orange", "red", "maroon","violet","magenta","purple","navyblue", "skyblue", "turquoise", "lightgreen", "green", "darkgreen", "chocolate", "brown", "gray", "white"]
def draw_grph(lst):
    tt.speed(0)
    i=0
    tt.color(random.choice(colors))
    tt.pencolor('Black')
    for iter in lst:
        i=i+1
        tt.begin_fill()
        tt.left(90)
        tt.forward(iter)
        tt.right(90)
        tt.forward(25)
        tt.write(str(iter), font=("Calibri", 12), align='left', move=True)
        if lst == dist:
            tt.write('Distinction', font=("Calibri", 8), align='left', move=False)
        if lst == fclass:
            tt.write('First class', font=("Calibri", 7),
                     align='left', move=False)
        if lst == sclass:
            tt.write('Second class', font=("Calibri", 7),
                     align='left', move=False)
        if lst == ps:
            tt.write('Pass', font=("Calibri", 7),
                     align='left', move=False)
        if lst == fl:
            tt.write('Fail', font=("Calibri", 7),
                     align='left', move=False)
        tt.right(90)
        tt.forward(iter)
        tt.left(90)
        tt.end_fill()
    tt.left(180)
    tt.forward(i*(45))
    tt.right(180)
    tt.forward(i*(45))
    tt.penup()
    tt.forward(5)
    tt.pendown()
    


draw_grph(dist)
draw_grph(fclass)
draw_grph(sclass)
draw_grph(ps)
draw_grph(fl)
tt.shape("turtle")
tt.penup()
tt.left(180)
tt.forward(5)
tt.width(5.5)
tt.color('black')
tt.pendown()
tt.forward(len(mar)*46.2)
tt.right(90)
tt.forward(max(mar)+45)
turtle.Screen().exitonclick()

