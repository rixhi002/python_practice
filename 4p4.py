print('How many circles ?')
n=int(input())
pi=3.14
for i in range(0,n):
    print('Enter radius ')
    radius=float(input())
    circumference=pi*radius*2
    print('circumference =',circumference)
