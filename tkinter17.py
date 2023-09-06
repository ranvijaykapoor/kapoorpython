from tkinter import  *
from  tkinter.font import *
root= Tk()
def get_data():
    print(text.get(1.0,END))

def get_selected_data():
    result=text.selection_get()
    print((result))

def clear_text():
    text.delete(1.0,END)

def get_selected_data_position():
    result = text.selection_get()
    pos=text.search(result,1.0,stopindex=END)
    print(pos)

root.title("My Notepad ")
myfont=Font(family="Comic Sans Ms",size=20,weight="bold",underline=1,slant='italic',overstrike=1)
text=Text(root,width=50,height=10,selectbackground="red",wrap=WORD,bd=5,insertwidth=4,padx=10,pady=10,font=myfont)
text.insert(INSERT,"welcome you all")

text.pack()
#text.pack(fill=BOTH,expand=1)


btn1=Button(root,text="get text data",command=get_data).pack()
btn2=Button(root,text="get selected text data",command=get_selected_data).pack()
btn3=Button(root,text="clear text",command=clear_text).pack()
btn4=Button(root,text="get selected Text Data Position",command=get_selected_data_position).pack()
root.geometry("500x600+100+100")
root.mainloop()