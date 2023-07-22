'''def add(x,y):
    return (x+y)
print(add(4,5))

#function without name   : lambda


it can take any number arguments but will have only one expression
'''
from functools import *
f = lambda x, y: x + y

print(f(5, 10))
'''
filter map and reduce
'''
'''
def test_even(n):
    return n%2==0'''

l=[1,2,3,4,5,6,7,8]
print(l)
even_num=list(filter(lambda n:n%2==0,l))
print(even_num)

sq=list(map(lambda n:n*n,even_num))
print(sq)


total=reduce(lambda a,b:a+b,sq)
print(total)

