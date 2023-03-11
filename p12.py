print("Enter the value of n")
n=int(input())
print("Enter the factors are:")
for i in range(1,n+1):
    if n % i ==0:
        print(i)
