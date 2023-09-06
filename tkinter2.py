from tkinter import *
root=Tk()
root.title("pack method example")

btn1=Button(root,text="Button1",fg="yellow",bg="red",font=("comic Sens Ms",12,"bold"))
btn1.pack(side=TOP,fill=X)

btn2=Button(root,text="Button2",fg="yellow",bg="red",font=("comic Sens Ms",12,"bold"))
btn2.pack(side=LEFT,fill=Y)

btn3=Button(root,text="Button3",fg="yellow",bg="red",font=("comic Sens Ms",12,"bold"))
btn3.pack(side=RIGHT,fill=Y)

btn4=Button(root,text="Button4",fg="yellow",bg="red",font=("comic Sens Ms",12,"bold"))
btn4.pack(side=BOTTOM,fill=X)

root.geometry("400x500+600+200")
root.resizable(0,0)
root.mainloop()