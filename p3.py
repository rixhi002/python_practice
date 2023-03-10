L=[]
print("Enter 10 numbers:",end=' ')
for i in range(0,10):
    inp=int(input()) 
    L.append(inp) 
print(L, end='\n') 
print('Enter a number to search ', end=' ') 
s=int(input()) 
pos=-1 
for i in range(0,10): 
    if L[i]==s: 
        pos=i+1 
        break 
print(" position : ", pos)

