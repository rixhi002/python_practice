

for i in range(0,20):
    print("Enter the age: ")
    n=int(input())
    if n>0 and n<=3:
        print("Infant")
    elif n>3 and n<=12:
        print("Kid")
    elif n>12 and n<=19:
        print("Adolescence")
    elif n>20:
        print("Adult")
    else:
        print("invalid")
