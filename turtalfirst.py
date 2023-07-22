from turtle import *

t = Turtle()
wn=Screen()
wn.title("My First garaphics")
#wn.bgcolor("yellow")
wn.bgpic("")  # recamanded always .gif file
t.shape("turtle")
#t.shape("circle")
t.color("red","green")#pelcolar.fillcolor
t.hideturtle()
t.speed(1)

t.begin_fill()

'''
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
'''
for i in range(4):
    t.forward(100)
    t.left(90)
t.penup()
t.forward(200)
t.pendown()
for i in range(4):
    t.forward(100)
    t.left(90)

t.end_fill()
done()