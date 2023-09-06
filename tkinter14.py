from tkinter import *
root=Tk()
def get_select():
    get_data=l.curselection()
    print(get_data)
    for item in get_data:
        print(l.get(item))

def delete_select():
    res=l.curselection()
    for item in res:
        print(l.delete(item))

root.title(" List Example")
l=Listbox(root,width=50,height=10,selectmode=EXTENDED)  # four mode:- select ,browse,multiple,extended
l.insert(1,"PYTHON")
l.insert(2,"JAVA")
l.insert(3,"PHP")
l.insert(4,"C")
l.pack()

btn=Button(root,text="SELECTED ITEM IN LIST",command=get_select).pack()
btn1=Button(root,text="DELETE SELECTED ITEM IN LIST",command=delete_select).pack()
root.geometry("500x400+100+100")
root.mainloop()