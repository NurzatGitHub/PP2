i = int(input())
k = int(input())
if i>k:
    for i in range(i,k- 1,-1):
        print(i,end=' ')
else:
    for i in range(i,k + 1):
        print(i,end=' ')