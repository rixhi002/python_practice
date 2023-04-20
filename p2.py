print("Enter the value of m:",end=' ')
m=int(input())
print("Enter the value of n:",end=' ')
n=int(input())
sum1=0
sum2=0
for i in range(m,n+1):
    if m%2==0:
        sum1+=i
    else:
        sum2+=i
print("Sum of even numbers:",sum1)
print("Sum of odd numbers:",sum2)

 
