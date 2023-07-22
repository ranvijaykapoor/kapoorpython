class A:
    def __init__(self):
        print("Iam class A  constructor")

class B:
    def __init__(self):
       # super().__init__()  to call the B constructor
        print("Iam class B constructor")

class C(A,B):
    def __init__(self):
        super().__init__()
        print("Iam class C  constructor")


#b=B()
c=C()