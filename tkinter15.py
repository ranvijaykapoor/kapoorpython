from tkinter import *
root=Tk()
root.title("Creat and use scroll bar and frame ")
f=Frame(root)
scrool=Scrollbar(f)
scrool.pack(side=RIGHT,fill=Y)
l=Listbox(f,yscrollcommand=scrool.set)
root.geometry("500x500+100+100")
for i in range(1,15):
    l.insert(END,"List Data "+str(i))
f.pack()
l.pack(side=LEFT)
scrool.config(command=l.yview)
root.mainloop()