from tkinter import *


class MyGUI:
    def msg(self):
        print("Button is clicked")

    def __init__(self,window):
        self.button=Button(window,text="Click Me",command=self.msg)
        self.button.pack()
        self.quitBtn=Button(window,text="close",command=window.quit)
        self.quitBtn.pack(side=BOTTOM)
root=Tk()
root.title("creat GUI using OOPs")

Gui=MyGUI(root)

root.geometry("500x400+100+100")
root.mainloop()