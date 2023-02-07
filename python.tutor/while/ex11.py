i,j = 0,0
b = 0
l = []
while True:
    a = int(input())
    if a == 0:
        break
    l.append(a)
l.sort()
print(l[len(l)-2])
