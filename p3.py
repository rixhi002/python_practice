
l=[]
for i in range(10):
    e=int(input()) 
    l.append(e)
key=int(input())
for j in range(10):
    if l[j]==key:
        print("Found")
