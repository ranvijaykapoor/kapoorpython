from tkinter import *
from tkinter.ttk import Combobox
root=Tk()
def combo_get():
    print(c.get())
root.title("combo box exa ")
#l=["UP","BIHAR","RAJSTHAN","MADHAY PRADESH","TELANGANA","UTTARAKHAND"]
l=list(range(31))
c=Combobox(root,values=l,width=50,height="10")
c.set("Select Your State")
btn =Button(root,text="Your state",command=combo_get)

c.pack()
btn.pack()

root.geometry("600x500+100+100")
root.mainloop()