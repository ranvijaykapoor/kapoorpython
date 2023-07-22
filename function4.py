#keyword variable lendth argument
def person(name,**no):
    print(name)
    print(no)
    for i,j in no.items():
        print(i,j)


person(name='ram',age=23,contect=99935219720,city='gkp'
                                                  '')