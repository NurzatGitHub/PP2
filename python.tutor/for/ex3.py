i = int(input())
k = int(input())
if i % 2 == 0:
    i -= 1
for i in range(i,k - 1, -2):
    print(i,end=' ')