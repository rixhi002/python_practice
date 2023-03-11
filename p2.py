print('How many circles ?')
n=int(input())
pi=3.14
i=1
while i<=n:
    print('Enter radius ')
    radius=float(input())
    circumference=pi*radius*2
    print('Circumference =',circumference)
    i+=1
