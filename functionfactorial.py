def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i

    return f





x=int(input("enter any  number for which u want factorial "))
print(" x ",x)
result=fact(x)
print(result)

