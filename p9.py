L=[] 
print('Enter names of 10 cities ::') 
for i in range(0,11): 
    L.append(input()) 
print('Original list contains::',end='\n') 
print(L) 
for i in range(0,11): 
    for j in  range(0,11-i-1): 
        if L[j]>L[j+1]: 
            temp=L[j] 
            L[j]=L[j+1] 
            L[j+1]=temp 
print('The sorted list contains ::') 
print(L)
/*kolkata
lucknow
chennai
bangalore
mysore
jaipur
durgapur
pune
jamshedpur
mumbai
srinagar*/

