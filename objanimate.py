from tkinter import *
import time
import random
root=Tk()
root.title("Moving ball")
can=Canvas(root,width=800,height=600)
can.pack()
class Ball:
    def __init__(self,color,size):
        self.ball = can.create_oval(10, 10, size, size, fill=color)
        self.xspeed = random.randrange(1,8)
        self.yspeed = random.randrange(1,8)

    def animate(self):
        can.move(self.ball, self.xspeed, self.yspeed)
        pos = can.coords(self.ball)
        #print(pos)

        if pos[3] >= 600 or pos[1] <= 0:
            self.yspeed = -self.yspeed
        if pos[2] >= 800 or pos[0] <= 0:
            self.xspeed = -self.xspeed

movingball=[]
color=["blue","red","green","orange","gold","grey","pink"]
for i in range(50):
    movingball.append(Ball(random.choice(color),random.randrange(50,100)))
while True:
    for j in movingball:
        j.animate()
    root.update()
    time.sleep(0.01)

#root.geometry("800x600+120+10")
root.mainloop()