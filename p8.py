import math
print("Enter the number: ",end=' ')
num=int(input())
s= math.sqrt(num)
if math.ceil(s)==math.floor(s) :
    print("It is a perfect square")
else:
    print("It is not a perfect square")
        
