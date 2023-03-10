print("Enter number :")
num=int(input())
if num%3==0 and num%5==0:
    print("Divisible")
elif num%3==0 and num%5!=0:
    print("Divisible by 3 and not by 5")
elif num%5==0 and num%3!=0:
    print("Divisible by 5 and not by 3")
elif num%3!=0 and num%5!=0:
    print("Neither divisible by 5 or 3")
else:
    print('Invalid')
