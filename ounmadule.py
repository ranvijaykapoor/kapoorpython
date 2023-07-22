def add(x,y):
    c=x+y
    print("sum= ",c)

def sub(x, y):
    c = x - y
    print("sub= ", c)

#add(4,5)
#sub(10,5)

#spacial variable
print(" name  =  ",__name__)

if __name__=="__main__":
    def msg():
        print("made by ran vijay kapoor")
    msg()
else:
    print("this function can not accessible")