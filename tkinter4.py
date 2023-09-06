from tkinter import *

def msg(event="null"):
    print("welcome to my window")

root=Tk()
root.title("Calling a function on Button Click ")

root.bind("<Control-m>",msg) # create shortcut

btn=Button(root,text="Click to call msg ",bg="yellow",fg="blue",font=("Comic Sens Ms",15,"bold"),command=msg)
btn.place(x=175,y=100)
#btn.bind("<Button-1>",msg) # bind Button



root.geometry("600x500+600+150")
root.resizable(0,0)
root.mainloop()