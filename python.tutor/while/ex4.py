n = int(input())
m = int(input())
i = 1
if n == m:
    print(i)
else:
    while n < m:
        n += n/10
        i += 1
    print(i)