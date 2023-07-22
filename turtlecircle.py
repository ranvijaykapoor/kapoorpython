from turtle import *
t=Turtle()
t.pensize(5)

t.circle(50)  # antyclockwise
# #t.bk(100)
t.circle(-50)  # clockwise

t.reset() # clear screen
t.pensize(5)
t.circle(50,180)


t.undo()
t.circle(100,steps=12)


t.goto(-50,-50)
t.circle(60)
done()