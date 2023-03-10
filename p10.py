l=[] 
print('Enter names of 10 cities ::') 
for i in range(0,11): 
    l.append(input()) 
print('Original list contains::',end='\n') 
print(l) 
for i in range(0,11): 
    for j in  range(0,11-i-1): 
        if l[j]>l[j+1]: 
            temp=l[j] 
            l[j]=l[j+1] 
            l[j+1]=temp 
print('The sorted (list)  contains ::') 
print(l)
