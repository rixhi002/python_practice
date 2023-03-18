import math
import sys
print("m=")
m=int(input())
print("n=")
n=int(input())
print("Perfect squares are:")
if m<nand m!=0 and n!=0:
    for i in range(m,n+1):
        if math.sqrt(i**2)==i:
            print(i)
else:
    print("Invalid Input")
    sys.exit(0)
