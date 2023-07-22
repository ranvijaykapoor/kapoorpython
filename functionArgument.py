'''def add(x,y):# x and y are callded from formal argumenent
    c=x+y
    print(c)


add(55,45)#  55 and 45 are actual argument

'''
# positional argument
def person(name,age=18):
    print("name = ",name)
    age=age+10
    print("age",age)

person("Ranvijay ",23)

#person(23,"vijay")


# keyward argument
person(name="ram",age=10)
person(age=50,name="kapoor")


# default argument
person(name="mandeep")
person(name="sandeep",age=30)


