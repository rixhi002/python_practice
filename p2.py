import math
list30=[ 'November','April','June','September' ]
list31= ['January','March','May','July','August','October','December']
print('Enter number of days')
days=int(input())
if days==30:
    print(list30)
elif days==31:
    print(list31)
elif days==28 or days==29:
    print('February')
else:
    print('Invalid Input')
    
