try:
    a = int(input(" enter First number "))
    b = int(input(" enter Second number "))
    print("a = ",a,"\nb = ",b)
    div=a/b
    print("division ",a," / ",b," = ",div)
    print("Thank You")

except ZeroDivisionError:
    print(" Value of 'b' cannot be Zero")

except ValueError:

    print(" You have not enter a 'number' Exa: 1 2 3....")
except Exception:

    print(" Somthing went wrong ")

finally:
    print("Thank You bhai ji")

