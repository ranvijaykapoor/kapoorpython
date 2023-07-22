
try:

    a = int(input("enter a number to find to factorial "))

    fact = 1
    for i in range(a,0,-1):
        fact = fact * i
        if i==1:
            print(i,"=",fact)
        else:
            print(i, "* ", end="")
except Exception:
    print("You are press Something Wrong")

finally:
    print(" Thank You")