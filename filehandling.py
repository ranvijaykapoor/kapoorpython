'''
open the file
    file name
    mode::read(r) write(w) append(a)

perform opration
    1.read
    2.write
    3.append
close
'''

f=open("collage.txt","r")
print(f)

# to read the content of file
#print(f.read())

for data in f:
    print(data,end="")

#f1=open("collage2.txt","w")
f1=open("collage2.txt","a")
print(f1)
name=input("enter your name")
f1.write(name)
#f1.close()
f1=open("collage2.txt","r")
print("content of f1 is ")
print(f1.read())
