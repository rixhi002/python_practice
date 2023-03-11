print("Enter the value of n")
n=int(input())
sum=0
for i in range(1,n+1):
    s=1
    for j in range(1,i+1):
        s*=j
    sum+=s
print("Sum =",sum)
