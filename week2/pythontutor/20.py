#Шоколадка
n = int(input())
m = int(input())
k = int(input())
if k > n*m:
    print('NO')
elif k%n == 0 or k % m == 0:
    print('YES')
elif k < min(n,m):
    print('NO')
else:
    print('NO')