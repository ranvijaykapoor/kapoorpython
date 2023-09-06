from tkinter import *
root =Tk()

def get_redio():
    #print(i.get())
    if i.get==1:
        print("male")

    else:
        print("female")

    print(j.get())
root.title("radio exa")
f=LabelFrame(root,text="Select your Gender")
i=IntVar()
r1=Radiobutton(f,text="male",value=1,variable=i)
r2=Radiobutton(f,text="female",value=2,variable=i)
btn=Button(root,text="Get Radio value",command=get_redio)
r1.pack()
r2.pack()
btn.pack()
f.pack()



ff=LabelFrame(root,text="Select your Rilesion")
j=StringVar()
d1=Radiobutton(ff,text="Hindu",value="hindu",variable=j)
d2=Radiobutton(ff,text="Muslim",value="muslim",variable=j)
d3=Radiobutton(ff,text="Sikh",value="sikh",variable=j)
d4=Radiobutton(ff,text="Eshai",value="Eshai",variable=j)


btn2=Button(root,text="Get Radio value",command=get_redio)
d1.pack()
d2.pack()
d3.pack()
d4.pack()
ff.pack()
btn2.pack()


root.geometry("400x400+100+100")
root.mainloop()