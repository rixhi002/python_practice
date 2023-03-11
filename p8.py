print("Enter the value of a")
a=int(input())
s =0
for i in range(1,11):
    a=a ** i
    s+=1/a
print("Sum =",s)
