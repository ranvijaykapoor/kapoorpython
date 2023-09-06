from  tkinter import *
from tkinter import filedialog
from tkinter.font import *
class MyNotepad:
    current_file="no_file"
    def new_file(self):
        pass

    def saveas_file(self):
        f = filedialog.asksaveasfile(mode="w", defaultextension='.txt', title="Save File")
        data=self.txt_area.get(1.0,END)
        f.write(data)
        self.current_file=f.name
        f.close()

    def save_file(self):
        if self.current_file=="no-file":
            self.saveas_file()
        else:
            f=open(self.current_file,mode="w")
            f.write(self.txt_area.get(1.0,END))
            f.close()

    def open_file(self,event=""):
        result = filedialog.askopenfile(initialdir="/", title="Open File",
                                        filetypes=(("Text File", "*.txt"), ("All File", "*.*")))
        for data in result:
            self.txt_area.insert(INSERT,data)
            self.current_file=result.name


            #f = filedialog.asksaveasfile(mode="w", defaultextension='.txt', title="Save File")

    def exit_file(self):
        root.destroy()

    def copy(self):
        pass


    def __init__(self,master):
        self.master=master
        master.wm_iconbitmap("Notepad.ico")
        master.title(" My Notepad ")
        master.bind("<Control-o>",self.open_file)
        master.bind("<Control-O>", self.open_file)
        self.txt_area=Text(master,padx=5,pady=5,wrap=WORD,selectbackground="red",bd=2,insertwidth=3)
        self.txt_area.pack(fill=BOTH,expand=1)

        #creating file

        self.main_menu = Menu(self.master)
        self.master.config(menu=self.main_menu)
        self.file_menu = Menu(self.main_menu, tearoff=False)
        self.main_menu.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="New", accelerator="Ctrl+N")
        self.file_menu.add_command(label="Open...", accelerator="Ctrl+O" ,command=self.open_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Save", accelerator="Ctrl+S", command=self.save_file)
        self.file_menu.add_command(label="Save As...", accelerator="Ctrl+Shift+S",command=self.saveas_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit"''', command=exit_file''')


        self.edit_menu = Menu(self.main_menu, tearoff=False)
        self.main_menu.add_cascade(label="Edit", menu=self.edit_menu)
        self.edit_menu.add_command(label="Undo", accelerator="Ctrl+Z")
        self.edit_menu.add_command(label="Cut", accelerator="Ctrl+X")
        self.edit_menu.add_command(label="Copy", accelerator="Ctrl+C")
        self.edit_menu.add_command(label="Paste", accelerator="Ctrl+V")
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="Delete")


        self.format_menu = Menu(self.main_menu, tearoff=False)
        self.main_menu.add_cascade(label="Format", menu=self.format_menu)
        self.file_menu.add_command(label="Font")

root=Tk()
b=MyNotepad(root)
root.mainloop()