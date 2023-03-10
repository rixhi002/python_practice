L=[]
print('Enter 10 numbers into the list :',end=' ')
for i in range(0,10):
    inp=int(input())
    L.append(inp)
print(L)
max=min=L[0]
for i in range(0,10):
    if L[i]>max :
        max=L[i]
    elif L[i]<min :
        min=L[i]
print("\n max :",max,"min :",min)
    
