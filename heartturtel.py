from turtle import *

pen = Turtle()

speed(10)
def corve():
    for i in range(200):
        pen.right(1)
        pen.forward(1)


pen.fillcolor("red")
pen.begin_fill()
pen.left(140)
pen.forward(113)
corve()
pen.left(120)
corve()
pen.forward(113)
pen.end_fill()

pen.penup()
pen.setpos(-60,90)
pen.down()
hideturtle()
pen.color('lightgreen')
pen.write("Ranvijay Kapoor", font=( "Veradhana", 12, "bold"))
pen.penup()
done()
