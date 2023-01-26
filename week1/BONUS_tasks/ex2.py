a = [int(i) for i in input().split()]
if len(a) == 1:
    print(a[0])
else:
    for i in range(len(a)):
        if i == len(a)-1:
            print(a[i - 1] + a[0],end=' ')
        else:
            print(a[i - 1] + a[i + 1],end=" ")