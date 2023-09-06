from tkinter import *
root=Tk()

def msg():
    print("file is opened")

root.title("Menu bar and sub Menu")
main_menu=Menu(root)
root.config(menu=main_menu)

file_menu=Menu(main_menu,tearoff=False)
main_menu.add_cascade(label="FILE",menu=file_menu)
file_menu.add_command(label="New",command=msg,accelerator="Ctrl+N") # accelerator = Short cut key
file_menu.add_command(label="Open",accelerator="Ctrl+O")

#creating sub menu

save_menu=Menu(main_menu,tearoff=False)
file_menu.add_cascade(label="SAVE",menu=save_menu)
save_menu.add_command(label="Sane Now")
save_menu.add_command(label="Sane As")

file_menu.add_separator() # Separator
file_menu.add_command(label="Exit")



edit_menu=Menu(main_menu,tearoff=False)
main_menu.add_cascade(label="EDIT",menu=edit_menu)
edit_menu.add_command(label="Copy")
edit_menu.add_command(label="Cut")
edit_menu.add_command(label="Paste")
edit_menu.add_command(label="Delete")

root.geometry("500x400+100+100")
root.mainloop()