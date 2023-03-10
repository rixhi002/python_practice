l=[]
for i in range(10):
    e=int(input()) 
    l.append(e) 
     
s=0
for j in range(10):
    if l[j]%3==0 and l[j]%5==0: 
        s=s+l[j]
print("Sum of numbers in list divisible by 3 and 5 =",s) 
