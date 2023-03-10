print('Enter the mass :',end=' ')
mass=int(input())
print('Enter the height :',end=' ')
height=int(input())
bmi= mass / (height ** 2)
if bmi>23:
    print('Overweight')
elif bmi>=18 and bmi<=23:
    print('Ok')
elif bmi<18:
    print('Underweight')
else:
    print('Invalid')

