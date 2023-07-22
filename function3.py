def add(x, y):
    c = x + y
    print(c)


add(55, 45)


# variable length argument
'''def friendadd(a, *b):
    print(a)
    print(b)
    sum=a
    for i in b:
        sum=sum+i
    print("final= ",sum)

friendadd(4, 5, 6, 7, 8, 9)'''

def dostadd(*b):

    print(b)
    sum=0
    for i in b:
        sum=sum+i
    print("final= ",sum)

dostadd(4, 5, 6, 7, 8, 9)
