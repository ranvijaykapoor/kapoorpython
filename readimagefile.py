f=open("weather.png","rb")
#print(f.read())

f2=open("geather.png","wb")
for data in f:
    print(data)
    f2.write(data)

f3=open("geather.png","rb")
print(f3.read())

