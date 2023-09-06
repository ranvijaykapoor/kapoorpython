from tkinter import *
from tkinter import simpledialog
root=Tk()

def input_marks():
    sum=0
    for i in range(5):
        s = simpledialog.askinteger("enter mask of student ", "enter Marks")
        sum=sum+s
    print("Sum of Marks",sum)

root.title("Simple dialog  Box  example  tkinter 11")
btn =Button(root,text="Input marks",command=input_marks).pack()
#btn.pack()
root.geometry("400x300+100+100")
root.mainloop()