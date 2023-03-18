sign=-1
for i in range(2,7,3): 
    for j in range(9,7,4): 
        sum=sum+(i/j)*sign
        sign*=sign
print(sum)

