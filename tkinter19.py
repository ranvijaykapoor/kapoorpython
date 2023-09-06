from tkinter import *
from tkinter import filedialog
root = Tk()
root.title("File Dialog | open file & save file")
def open_file():
    result=filedialog.askopenfile(initialdir="/",title="Open File",filetypes=(("Text File","*.txt"),("All File","*.*")))
    print(result)
    for data in result:
        print(data)

btn=Button(root,text="Open file",command=open_file).pack()
def save_file():
    f=filedialog.asksaveasfile(mode="w",defaultextension='.txt',title="Save File")
    if f is None:
        return
    f.write("Welcome you all")
    f.close()
btn2=Button(root,text="Save file",command=save_file).pack()

root.geometry("300x300+120+100")
root.mainloop()
