print("Enter the value of a")
a=int(input())
s =0
for i in range(2,21):
    a=a/i
    s+=a
    
print("Sum =",s)
