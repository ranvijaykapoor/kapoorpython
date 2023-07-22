def fact(n):

    if n==0:
        return 1
    else:
        print(n,"*")
        return n*fact(n-1)


x=int(input("enter a number"))
result=fact(x)
print(result)