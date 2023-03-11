print("Enter the value of a")
a=int(input())
s =0
sign=1
for i in range(0,11):
    a=a ** i
    s+=a
    a*=sign
    sign=-1
print("Sum =",s)
    
