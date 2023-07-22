s='welcom in Python'
print(s)
'''print(s[0:])
print(len(s))
print(s[0:17])
print(s[0::2])



print(s.capitalize())
print(s.lower())
print(s.upper())
print(s.title())
print(s.swapcase())
st=s.split()
for i in st:
    print(i)


str='Her name is tamanna and tamanna is a good girl'
print(str)
x=input("enter the ward you want to find")
y=str.find(x)
if y==-1:
    print("item not find")
else:
    print("item found at location : ",y)
    rep=input("enter the ward you want to replace")
    str2=str.replace(x,rep)
    print(str2)
'''
name="humtum"
print(name.isdigit())
print(name.isalpha())

test="1234"
print(test.isdigit())
print(test.isalpha())


empid="MPP123"
print(empid.isalnum())


x=  "              hello           "
print(x,end="")
print("hi")
#print(x.strip(),end="spaceremoved")
print(x.lstrip(),end="spaceremoved")
print(x.rstrip(),end="spaceremoved")
print()
d="!!!!!!!!!!!notequal!!!!!!!!!!!!!"
print(d.strip('!'))