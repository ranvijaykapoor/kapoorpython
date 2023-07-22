lst = [1, 2, 3, 4, 5, 6, 7, 8]
def passlist(l):
    even_sum=0
    odd_sum=0
    for i in l:
        if i%2==0:
            even_sum=even_sum+i
        else:
            odd_sum=odd_sum+i
    return even_sum,odd_sum

x,y=passlist(lst)
print("even sum  ",x)
print("odd sum  ",y)
print("even sum :{}  and odd sum:{}".format(x,y))