# when a function call itself it is called recursion
import sys
print(sys.getrecursionlimit())
sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())


count=0
def msg():
    global count
    print( count,"good night")
    count = count + 1
    msg()


msg()