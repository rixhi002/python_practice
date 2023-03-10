L=[] 
print('Enter 10 numbers into a list ', end='\n') 
for i in range(0,10): 
    inp=int(input()) 
    L.append(inp) 
print(L) 
for i in range(0,10): 
    small=L[i] 
    posn=i 
    for j in range(int(i+1), int(10)): 
        if L[j]<small: 
            small=L[j] 
            posn=j 
    temp=L[i] 
    L[i]=small 
    L[posn]=temp 
print('The sorted list contains ::') 
print(L)
