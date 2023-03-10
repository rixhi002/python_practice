l=[] 

print('Enter 10 names :') 
for i in range(0,10): 
    l.append(input()) 
    
print('Enter first character to match ::', end=' ') 
char=input() 

for i in range(0,10): 
    str=l[i] 
    if str[0:1]==char: 
       print(l[i]) 
