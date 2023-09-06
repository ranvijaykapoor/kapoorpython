from tkinter import *
root=Tk()

def get_data():
    print(sc.get())
    print(sp.get())
root.title("Create and use scale and spin Box")
sc=Scale(root,from_=0,to=100,orient=HORIZONTAL,length=200,width=25,sliderlength=60)

#sc.pack(side=LEFT,fill=Y)
sc.set(50)
sc.pack()

#spin

sp=Spinbox(root,from_=0,to=5)
sp.pack()
btn=Button(root,text="get Volume Data",command=get_data).pack()
root.geometry("500x400+100+100")
root.mainloop()