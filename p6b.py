L=[] 
print('Enter 10 numbers into a list ', end='\n') 
for i in range(0,10): 
    inp=int(input()) 
    L.append(inp) 
print(L) 
L.sort(reverse=True) 
print('The sorted list contains ::') 
print(L)

