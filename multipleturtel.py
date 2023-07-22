from turtle import *
l=["red","blue","gold","yellow","orange"]
t=Turtle()
we=Screen()
we.title("multicolored circle")
t.shape("turtle")
t.color("green","yellow")
t.speed(1)
t.up()
t.goto(200,0)
t.down()
t.pensize(10)

for i in range(5):
    t.pencolor(l[i])
    t.circle(50)
    t.up()
    t.back(100)
    t.down()


done()