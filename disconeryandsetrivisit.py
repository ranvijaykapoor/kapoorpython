# Exploring of dictionary and set revisited

temp={'ram':44,'shyam':45,'rohan':34,'ram':444}
print(temp)
print(type(temp))

d={}    # to creat a blank dictionary
print(d)
print(type(d))

collage=dict()  # to creat a blank dictionary
print(collage)
print(type(collage))

# to copy  the dictionary into another dictionary

test=dict(temp)
print(test)


# to create a dictionary in another way

a={}
a['samsung']='ram'
a['lg']='rohan'
a['nokia']='mohan'
print(a)

# find the length
print(len(a))

# print  all key
print(a.keys())

#print all values
print(a.values())

# membership in and  not in
print('nokia' in a)
print('nokia' not in a)
print('google' in a)


#delete a key in
print(a)
del a['nokia']
print(a)

