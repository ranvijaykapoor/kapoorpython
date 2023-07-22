import random
num=random.randint(10,40)
print(num)
count=0
chance=4
while count<5:
    a=print(input("enter any number between 10 and 40 :  "))
    if num==a:
        print("You Guessed || You Win")
    else:
        print("Try again || You have ",chance-count," Chance")
        count=count+1

if not count<5:
    print(" You Lose ")
