print("Enter the score")
for i in range(0,9):
    n=int(input())
    if n==0:
        print("Duck")
    elif n>=50 and n<=99:
        print("Half Century")
    elif n>99 and n<=199:
        print("Century")
    elif n>199 and n<300:
        print("Double Century")
    else:
        print("Invalid")
        
