from tkinter import *

root=Tk()
root.title("main window")

def open_window():
    top=Toplevel()
    top.title("new window ")
    top.geometry("400x500+150+100")
    btn_destroy = Button(top, text="close window", command=top.destroy).pack()
btn=Button(root,text="open new window",command=open_window).pack()

btn_quit=Button(root,text="close application",command=quit).pack()

root.geometry("400x500+150+100")
root.resizable(0,0)
root.mainloop()