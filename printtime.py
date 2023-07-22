from time import *
# it gives the output in seconds since 1970
print(time())
# it gives the output in tuple format
print(localtime(time()))

t= (2020,10,31,9,6,51,5,305,0)
print(mktime(t))
print(asctime())