L=[] 
print('Enter 10 numbers into a list ', end='\n') 
for i in range(0,10): 
    inp=int(input()) 
    L.append(inp) 
print(L) 
for i in range(0,10): 
    for j in range(0, int(10-i-1)): 
        if L[j]>L[j+1]: 
            temp=L[j] 
            L[j]=L[j+1] 
            L[j+1]=temp 
print('The sorted list contains :',L)
