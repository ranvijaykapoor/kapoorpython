from turtle import *
from time import *
t=Turtle()
wn=Screen()
wn.title("Turtle satamp pattern")
wn.setup(800,600)
t.shape('turtle')
t.color('darkgoldenrod','black')
t.penup()
t.setposition(30,30)
s=10
for i in range(50):
    s=s+2
    t.stamp()
    t.forward(s)
    t.right(25)
    sleep(0.25)
