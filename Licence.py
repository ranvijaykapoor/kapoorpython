try :
    a=int(input("Enter a number "))
    if a>=18:
        print("You are elligible for licence")

    else:
        print("plese wait after ",18-a," year ")
        print(" You are Minor")

except Exception:
    print("You are enter wrong values")
finally:
    print("thank You ")