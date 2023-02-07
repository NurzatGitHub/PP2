n = int(input())
i = 1
while i <= n:
    k = 1
    while k <= n:
        a = k*k
        k += 1
        if a == i:
            print(i,end=' ')
    i += 1