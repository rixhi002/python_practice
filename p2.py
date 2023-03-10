l=[]
for i in range(10):
    e=int(input()) 
    l.append(e) 
  
max=l[0]
min=l[0]       
for i in l: 
    if i>max: 
        max=i
    elif i<min:
        min=i

print("The max is =",max)
print("The min is =",min) 
