from turtle import *
t=Turtle()
lu=Screen()
t.speed(10)

lu.title("LUDO game made by kapoor")
t.right(90)
t.forward(50)
for i in range(4):
    t.left(90)
    t.forward(120)
    i+=1


t.left(90)
# for colar box
def box(x,y):
    for i in range(4):
        t.right(x)
        t.forward(y)

# for pen up
def pen():
    t.penup()
    t.forward(120)
    t.left(90)
    t.down()


t.fillcolor("red")
t.begin_fill()
box(90,240)
t.end_fill()
pen()

t.fillcolor("green")
t.begin_fill()
box(90,240)
t.end_fill()
pen()

t.fillcolor("blue")
t.begin_fill()
box(90,240)
t.end_fill()
pen()

t.fillcolor("yellow")
t.begin_fill()
box(90,240)
t.end_fill()
t.color("black")

t.left(90)
t.forward(40)

# this loop is by
def middle_line():
    for i in range(4):
        t.left(90)
        t.forward(240)
        t.right(90)
        t.forward(40)
        t.right(90)
        t.forward(240)
        # for trangle
        t.left(90)
        t.forward(40)
        t.right(90)
        t.forward(40)

        i+=1


def lowertohight():
    t.penup()
    t.back(40)
    t.left(90)
    t.forward(240)
    t.down()

    t.right(90)
    t.forward(120)
    t.right(90)
    t.forward(40)


# for boxes

def small():
    for i in range(3):
        t.right(90)
        t.forward(120)
        t.left(90)
        t.forward(40)

        t.left(90)
        t.forward(120)
        t.right(90)
        t.forward(40)
        i+=1


middle_line()

lowertohight()
small()
lowertohight()
small()
lowertohight()
small()
lowertohight()
small()

t.back(40)
t.right(90)
t.forward(40)
t.left(90)

def colorline():
    for i in range(4):
        t.forward(40)
        box(90,40)

def colorbox(col):
    t.left(90)
    t.forward(40)
    t.right(90)
    t.forward(40)
    t.penup()
    t.back(40)
    t.left(90)
    t.forward(240)
    t.right(90)
    t.forward(120)
    t.right(90)
    t.forward(80)
    t.down()
    t.fillcolor(col)
    t.begin_fill()
    box(90, 40)
    t.right(90)
    t.forward(80)
    box(90, 40)
    t.back(40)
    t.left(90)
    t.end_fill()
    fillcolor(col)
    t.begin_fill()
    colorline()
    t.end_fill()

colorbox("blue")
colorbox("green")
colorbox("red")
colorbox("yellow")

done()