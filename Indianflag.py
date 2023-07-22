from turtle import *
f=Turtle()
wn=Screen()
wn.title("Indian Flag")
# for stick

f.color("red","blue")
f.speed(10)
f.begin_fill()
f.left(90)
f.forward(250)
f.left(90)
f.forward(30)
f.left(90)
f.forward(450)
f.right(90)
f.forward(50)
f.left(90)
f.forward(30)
f.right(90)
f.forward(50)
f.left(90)
f.forward(30)
f.left(90)
f.forward(230)
f.left(90)
f.forward(30)
f.left(90)
f.forward(50)
f.right(90)
f.forward(30)
f.left(90)
f.forward(50)
f.right(90)

f.end_fill()

f.penup()
f.forward(450)
f.down()

# for orange

f.color("red","orange")
f.begin_fill()
f.right(90)
f.forward(300)
f.right(90)
f.forward(50)
f.right(90)
f.forward(300)
f.left(90)

f.end_fill()

f.penup()
f.forward(50)
f.down()

#for green

f.color("red","green")
f.begin_fill()

f.left(90)
f.forward(300)
f.right(90)
f.forward(50)
f.right(90)
f.forward(300)
f.left(90)
f.end_fill()

# for wheel

f.penup()
f.back(75)
f.left(90)
f.forward(120)
f.left(90)
f.down()


# wheel steak
f.color("blue")
f.circle(-25)
f.right(90)
f.forward(50)

'''f.left(100)
f.forward(10)
f.left(100)
f.forward(50)
f.left(100)
f.forward(10)
f.left(100)
f.forward(50)
f.left(100)
f.forward(10)
f.left(100)
f.forward(50)
f.left(100)
f.forward(10)
f.left(100)
f.forward(50)
f.left(100)
f.forward(10)
f.left(100)
f.forward(50)
f.left(100)
f.forward(10)
f.left(100)
f.forward(50)
f.left(100)
f.forward(10)
f.left(100)
f.forward(50)'''

for i in range(22):
    f.left(94)
    f.forward(6)
    f.left(94)
    f.forward(50)
    i+=1




done()