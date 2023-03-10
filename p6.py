l=[]
e=0
for i in range(10):
    e=int(input()) 
    l.append(e)
length=len(l)
for i in range(0,length-1): 
    for j in range(length-1):  
            if l[j]>l[j+1]:  
                temp = l[j]  
                l[j]= l[j+1]
                l[j+1] = temp 
print("The sorted array is: ", l)  
