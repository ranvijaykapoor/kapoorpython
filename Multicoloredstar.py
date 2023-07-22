from turtle import *
l=["red","blue","gold","yellow","orange"]
t=Turtle()
we=Screen()
we.title("multicolored star")
t.shape("turtle")
t.color("green","yellow")
t.speed(5)



for i in range(20):
    t.pencolor(l[i%5])
    t.pensize(10)
    t.forward(200)
    t.right(144+i)

done()