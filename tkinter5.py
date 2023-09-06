from tkinter import *

def msg1(enent):
    print("good morning")

def msg2(enent):
    print("good afternoon")

def msg3(enent):
    print("good evening")

root=Tk()
root.title("mouse click events ")
btn1=Button(root,text="left click",fg="red",bg="yellow",font=("Comic Sans Ms",15,"bold"))
btn1.bind("<Button-1>",msg1)
btn1.place(x=50,y=60)


btn2=Button(root,text="middle click",fg="white",bg="black",font=("Comic Sans Ms",15,"bold"))
btn2.bind("<Button-2>",msg2)
btn2.place(x=50,y=120)

btn3=Button(root,text="right click",fg="blue",bg="yellow",font=("Comic Sans Ms",15,"bold"))
btn3.bind("<Button-3>",msg3)
btn3.place(x=50,y=180)

root.geometry("400x400+150+100")
root.mainloop()