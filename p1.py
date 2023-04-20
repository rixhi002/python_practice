sum1=0
sum2=0
pos=0
neg=0
for i in range(0,50):
 print("Enter integers: ")
 n=int(input())
    if n>=0:
        sum1+=n
        pos+=1
    elif n<0:
        sum2+=n
        neg+=1
print("Number of positive intergers: ",pos)
print("Number of negative intergers: ",neg)
print("Sum of positive intergers: ",sum1)
print("Sum of positive intergers: ",sum2)
    
