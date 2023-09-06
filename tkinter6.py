
from tkinter import *
'''def getdata():
    g=p.get()
    print(g)
'''
root=Tk()
root.title("My text box value")
def getdata():
    g=p.get()
    print(g)
    q.set(g)


lb=Label(root,text="Enter your name ",bg="red",fg="white",font=("Times New romen",15,"bold"))
lb.place(x=20,y=50)

p=StringVar()
txt=Entry(root,bg="red",fg="white",font=("Times New romen",15,"bold"),textvariable=p)
txt.place(x=200,y=50)

btn=Button(root,text="get name ",bg="red",fg="white",font=("Times New romen",15,"bold"),command=getdata)
btn.place(x=150,y=150)

q=StringVar()
lb1=Label(root,text=" Your name",bg="red",fg="white",font=("Times New romen",15,"bold"),textvariable=q)
lb1.place(x=150,y=200)

root.geometry("600x500+300+150")
root.mainloop()