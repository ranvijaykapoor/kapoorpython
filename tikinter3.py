from tkinter import *
root=Tk()
root.title("From design using Place Method")
lbl=Label(root,text="Enter Your name",bg="yellow",fg="red",font=("Comic Sens Ms",15,"bold"))
lbl.place(x=50,y=50)
name=Entry(root,bg="yellow",fg="red",font=("Comic Sens Ms",15,"bold"),insertwidth=10,bd=3)
name.place(x=250,y=50)
btn=Button(root,text="register",bg="yellow",fg="red",font=("Comic Sens Ms",15,"bold"))
btn.place(x=175,y=100)


root.geometry("600x600+600+100")
root.resizable(0,0)
root.mainloop()