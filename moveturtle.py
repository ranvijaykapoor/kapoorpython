from turtle import *
t=Turtle()
wn=Screen()
wn.title("Control Tertle")
wn.setup(800,600)
t.write("use up down left right arrow",font=("Arieal",15,"normal"))
def up():
    t.forward(100)

def down():
    t.backward(100)

def right():
    t.right(90)
    t.forward(100)

def left():
    t.left(90)
    t.forward(100)


#wn.onkey(up,"Up")
wn.onkey(up,"D")
wn.onkey(down,"Down")
wn.onkey(right,"Right")
wn.onkey(left,"Left")


wn.listen()


done()