'''
the canvas is a rectangular area intended for drawing pictures or other complex layouts .
You can place graphics ,text ,widgets or frame on a canvas.
'''

from tkinter import *
root=Tk()
root.title("creating the canvas adding shapes text image")
can=Canvas(root,height=1000,width=1000,bg="red")
can.create_text(500,50,text="welcome to python",font="Times 20 italic bold",fill="yellow")
can.create_line(10,10,500,500,fill="white",width=10)
can.create_rectangle(50,50,200,200,fill="blue")
can.create_oval(300,300,600,600,fill="yellow",outline="blue",width=5)
can.create_arc(300,500,600,200,extent=60)

point=[250,110,480,200,280,280,250,110]

poly=can.create_polygon(point,fill="blue",outline="gold",width=5)
can.pack()
photo=PhotoImage(file="E:\copy c\PycharmProjects\kapoorpython\geather.png")
can.create_image(200,200,image=photo,anchor=SE)
root.mainloop()