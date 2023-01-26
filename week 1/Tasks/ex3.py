a = [int(i) for i in input().split()]
a.sort()
b = []
t = []
if len(a) == 1:
    for i in b:
        print(i)
else:
    for i in range(len(a)):
        if(a[i] == a[i - 1]):
            b.append(a[i])
    t = set(b) 
    for i in t:
        print(i,end=' ')