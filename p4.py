L=[5,9,13,17,23,35,40,43,47,50] 
l=len(L) 
print(L, end='\n') 
print('Enter a number to search ', end=' ') 
s=int(input())
pos=-1
min=0
max=l-1
while min<=max:
    mid=(max+min)//2
    if L[mid]==s:
        pos=mid+1
        break
    elif s>L[mid]:
        min=mid+1
    else:
        max=mid-1
if pos>0:
    print("position :",pos)
else: 
    print(s,' was not found ')

          
    
    
