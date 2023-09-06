from tkinter import *
root =Tk()

def get_check():
    print(i.get())
    print(j.get())
root.title("check exa")
f=LabelFrame(root,text="Select your Known Language")
i=IntVar()

r1=Checkbutton(f,text="HINDI",variable=i)
j=StringVar()
r2=Checkbutton(f,text="ENGLISH",variable=j,offvalue="unchecked",onvalue="english"
                                                                        "")
btn=Button(root,text="Get checkvalue ",command=get_check)
r1.pack()
r2.pack()
btn.pack()
f.pack()
root.geometry("400x400+100+100")
root.mainloop()