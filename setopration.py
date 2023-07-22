marks={11,12,13,14,15,44,44,11}
print(marks)
print(type(marks))

marks.add(454)
print(marks)

marks.remove(12)
print(marks)

fruit=frozenset(['apple','mango','apple'])
print(fruit)
#fruit.add('greaps')

# to creat an empty set

a={}
print(a)
print(type(a))

#set function
b=set()
print(b)
print(type(b))

c=set(marks)
print(c)

print(24 in marks)
print(24 not in marks)

p={1,2,3,4}
q={4,5,6,7}

# unian
print(p|q)

# intersection
print(p&q)

#difference
print(p-q) # which are in p but not in q

#symmetric diffrence
print(p^q)

print(p)
print(p.clear())
print(p)
