'''def test():
    global x
    x=10
    print("inside x=",x)
test()

print("outside = x",x)
'''


x=40
print(id(x))

def msg():
    x=5
    print(x)
    # what if i want to print globle variable inside local
    p=globals()['x']
    print("global x=",p)

    print(id(p))
msg()