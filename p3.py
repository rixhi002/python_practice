import math
s=0
print("Enter the value :")
x=int(input())
for i in range(1,7):
    f=1
    for j in range(1,i+1):
        f*=j
    if i%2==0:
        s=s-math.pow(x,i)/f
    else:
        s=s+math.pow(x,i)/f
print(s)
