f=1
s=1
print("Enter the value :")
n=int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
       f*=j
    s+=(1/f)
print(s)
