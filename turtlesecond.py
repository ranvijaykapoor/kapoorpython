from turtle import *

def sq():
    for i in range(4):
        t.fd(100)
        t.left(90)


t = Turtle()
wn=Screen()
wn.title("My second garaphics")
#wn.bgcolor("yellow")
wn.bgpic("")  # recamanded always .gif file
t.shape("turtle")
#t.shape("circle")
t.color("red","green")#pelcolar.fillcolor
t.hideturtle()
t.begin_fill()

t.begin_fill()
sq()
t.up()
t.forward(200)
t.down()
sq()
t.end_fill()

t.speed(1)



done()