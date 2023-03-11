print("The value of n:")
n=int(input())
a=0
b=1
sum=0
for i in range(1,n-1):
    sum+=a+b
    a+=1
    b+=1
print("Sum =",sum)
    
