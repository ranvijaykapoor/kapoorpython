from tkinter import *
import time
root=Tk()
root.title("Moving ball")
can=Canvas(root,width=800,height=600)
can.pack()

ball=can.create_oval(10,10,60,60,fill="red")

ball1=can.create_oval(10,10,60,60,fill="blue")

'''for i in range(400):
    can.move(ball,1,0)
    root.update()
    time.sleep(0.01)
'''
xspeed=1
yspeed=2

xspeed1=4
yspeed1=3
while True:
    can.move(ball, xspeed, yspeed)
    pos=can.coords(ball)
    print(pos)
    '''
    pos=[left,top,right,bottom]
    '''
    if pos[3]>=600 or pos[1]<=0:
        yspeed=-yspeed
    if pos[2] >= 800 or pos[0] <= 0:
        xspeed = -xspeed

    can.move(ball1, xspeed1, yspeed1)
    pos = can.coords(ball1)
    print(pos)
    '''
    pos=[left,top,right,bottom]
    '''
    if pos[3] >= 600 or pos[1] <= 0:
        yspeed1 = -yspeed1
    if pos[2] >= 800 or pos[0] <= 0:
        xspeed1 = -xspeed1

    root.update()
    time.sleep(0.01)
#root.geometry("800x600+120+10")
root.mainloop()