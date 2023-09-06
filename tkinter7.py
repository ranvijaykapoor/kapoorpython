from tkinter import *
root=Tk()
root.title("Grid Layout")

name=Label(root,text="enter user name")
user=Entry(root)
password=Label(root,text="enter password")
pass_input=Entry(root)

name.grid(row=0,column=0)
user.grid(row=0,column=1)
password.grid(row=1,column=0)
pass_input.grid(row=1,column=1)

btn=Button(root,text="click to login")
btn.grid(row=2,columnspan=2)

#root.geometry("400x400+100+100")
root.mainloop()