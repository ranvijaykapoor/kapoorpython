from tkinter import *
from PIL import Image,ImageTk

root=Tk()
root.title("Insert Image ")

user_image=ImageTk.PhotoImage(Image.open('image\doctor_asian_male_coronavirus_people_avatar_mask_icon_141385.png'))
button_image=ImageTk.PhotoImage(Image.open('image\login.png'))
lable1=Label(root,text="Doctor Image",image=user_image,compound=BOTTOM,font=("comic sans ms",15,"bold"))
lable1.grid(row=1,column=0,columnspan=2)

btn=Button(root,image=button_image)
btn.grid(row=2,column=0,columnspan=2)



#root.geometry("400x400+120+120")
root.mainloop()