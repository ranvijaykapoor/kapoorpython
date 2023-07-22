def fact(n):
    f=1
    i=1
    while(i<=n):
        f=f*i
        i+=1
    print(f)


x=int(input("enter a number you find factorial number "))
fact(x)
