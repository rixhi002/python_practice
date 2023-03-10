l=[]
e=0
for i in range(10):
    e=int(input()) 
    l.append(e)
length=len(l)
for i in range(length-1):  
        minIndex = i  
        for j in range(i+1, length):  
            if l[j]<l[minIndex]:  
                minIndex = j  
                l[i]= l[minIndex]
                l[minIndex] =l[i]  
print("The sorted array is: ", l)  
