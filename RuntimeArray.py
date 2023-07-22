from array import *
marks=array('i',[])
n=int(input("Enter the number of student in your class"))
print("no of Student = ",n)
for i in range(n):
    x=int(input("enter the marks of next student "))
    marks.append(x)
print(marks)
for k in marks:
    print(k,"\t",end="")

search=int(input("enter number you search   "))
i=0
for find in marks:
    if find == search :
        print(i)
        break
    i+=1
else:
    print("Not found  ")
#print(marks.index(search))

