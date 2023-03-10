L1=[] 
L2=[] 
print('Enter 20 names and 20 telephone numbers into 2 lists ', end='\n') 
for i in range(0,20): 
    print('Enter name :', end=' ') 
    name=input() 
    print('Enter telephone number :', end=' ') 
    tele=input() 
    L1.append(name) 
    L2.append(tele)  
for i in range (0,20): 
    print(L1[i],'\t',L2[i]) 
print('Enter name to search') 
search=input() 
pos=-1 
for i in range (0, int(20)): 
    if L1[i]==search: 
        pos=i 
        break 
if pos>0: 
    print("position :", L2[posn]) 
else: 
    print(search,' was not found')
