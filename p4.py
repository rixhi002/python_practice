print('Enter average score :',end=' ')
marks=int(input())
if marks<40:
    print("Prize is pencil")
elif marks>=40 and marks<=60:
    print("Prize is pen")
elif marks>=61 and marks<=80:
    print("Prize is tiffin box")
elif marks>=81 and marks<=90:
    print("Prize is story book")
elif marks>90:
    print('Prize is cricket bat')
else:
    print('Invalid')
