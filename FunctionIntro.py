# how to declare a function

def msg():
    print("good morning")


msg()
msg()


def add(x, y):
    c = x + y
    print("sum =", c)


add(4, 5)

a = int(input("enter First number"))
b = int(input("enter second number"))
add(a, b)


def r_add_sub(p, q):
    s = p + q
    t = p - q
    return s, t


result1, result2 = r_add_sub(50, 40)
print("sum = ", result1, "sub = ", result2)
