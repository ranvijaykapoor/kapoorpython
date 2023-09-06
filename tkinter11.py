from tkinter import *
from tkinter import messagebox
root=Tk()

def save():
    #result=messagebox.askyesno("File save dialog box","Do you want to save this file")
    #result = messagebox.askyesnocancel("File save dialog box", "Do you want to save this file")
    result = messagebox.askquestion("File save dialog box", "Do you want to save this file")
    print(result)
    if result==True:
        print("file save ho gaya")
root.title("Massage Box")

btn =Button(root,text="Save file",command=save).pack()
#btn.pack()
root.geometry("400x300+100+100")
root.mainloop()