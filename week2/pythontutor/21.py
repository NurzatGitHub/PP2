#Яша плавает в бассейне
n = int(input())
m = int(input())
x = int(input())
y = int(input())
M = min(n,m)
m = min(x,y)
ma = max(x,y)
k = abs(M - m)
if k < m:
    print(k)
else:
    print(m)