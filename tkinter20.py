from tkinter import *
from tkinter import colorchooser
root=Tk()

def color_chooser():
    c=colorchooser.askcolor()
    print(c[1])
    root.config(background=c[1])
root.title(" Set Window Icon And color chooser ")
root.wm_iconbitmap("Notepad.ico")

btn=Button(root,text="Choose Color",command=color_chooser).pack()
root.geometry("600x500+100+100")
root.mainloop()