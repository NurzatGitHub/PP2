n = int(input())
a = [[0]*n for j in range(n)]
k = 1
for i in range((n + 1)//2):
    for j  in range(i,n - i):
        a[i][j] = k
        k += 1
    for j in range(i + 1, n - i):
        a[j][n - i - 1] = k
        k += 1
    for j in range(i + 1, n - i):
        a[n - i - 1][n - j - 1] = k
        k += 1
    for j in range(i + 1, n - i - 1):
        a[n - j - 1][i] = k
        k += 1

for i in range(n):
    for j in range(n):
        print(a[i][j],end=' ')
    print()
