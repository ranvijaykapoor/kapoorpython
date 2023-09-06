from tkinter import *
from tkinter import filedialog
from tkinter.font import *
root=Tk()
root.title("Notepad ranvijay")
main_menu=Menu(root)
root.config(menu=main_menu)
root.wm_iconbitmap("Notepad.ico")


def open_file():
    result=filedialog.askopenfile(initialdir="/",title="Open File",filetypes=(("Text File","*.txt"),("All File","*.*")))
    '''for data in result:
        print(data)'''

def save_file():
    f=filedialog.asksaveasfile(mode="w",defaultextension='.txt',title="Save File")

def exit_file():
    root.destroy()

def copy():
    c=filedialog.s

file_menu=Menu(main_menu,tearoff=False)
main_menu.add_cascade(label="File",menu=file_menu)
file_menu.add_command(label="New",accelerator="Ctrl+N")
file_menu.add_command(label="Open...",accelerator="Ctrl+O",command=open_file)
file_menu.add_command(label="Save",accelerator="Ctrl+S",command=save_file)
file_menu.add_command(label="Save As...",accelerator="Ctrl+Shift+S")
file_menu.add_separator()
file_menu.add_command(label="Exit",command=exit_file)




edit_menu=Menu(main_menu,tearoff=False)
main_menu.add_cascade(label="Edit",menu=edit_menu)
edit_menu.add_command(label="Undo",accelerator="Ctrl+Z")
edit_menu.add_command(label="Cut",accelerator="Ctrl+X")
edit_menu.add_command(label="Copy",accelerator="Ctrl+C")
edit_menu.add_command(label="Paste",accelerator="Ctrl+V")
edit_menu.add_separator()
edit_menu.add_command(label="Delete")


format_menu=Menu(main_menu,tearoff=False)
main_menu.add_cascade(label="Format",menu=format_menu)

help_menu=Menu(main_menu,tearoff=False)
main_menu.add_cascade(label="Help",menu=help_menu)

view_menu=Menu(main_menu,tearoff=False)
main_menu.add_cascade(label="View",menu=view_menu)
scrool=Scrollbar(root)
scrool.pack(side=RIGHT,fill=Y)
myfont=Font(family="Comic Sans Ms",size=12,weight="bold",underline=0,slant='italic',overstrike=0)
text=Text(root,width=1000,height=450,selectbackground="red",wrap=WORD,bd=5,insertwidth=4,padx=10,pady=10,font=myfont,yscrollcommand=scrool.set)
text.pack()




scrool.config(command=text.yview)
root.geometry("1000x450+125+125")
root.mainloop()