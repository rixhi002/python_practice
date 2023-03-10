print('Enter three numbers:' )
n1=int(input())
n2=int(input())
n3=int(input())
if n1==n2==n3:
    print('All numbers are equal')
elif n1>n2 and n1>n3:
    print("Greatest number :",n1)
elif n2>n1 and n2>n3:
    print("Greatest number :",n2)
elif n3>n1 and n3>n2:
    print("Greatest number :",n3)
elif n3==n1 and n3>n2:
    print("Greatest number :",n3)
elif n2==n1 and n2>n3:
    print("Greatest number :",n1)
else:
    print('Invalid')
