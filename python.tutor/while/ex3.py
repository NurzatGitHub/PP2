n = int(input())
i = 0
while i <= n:
    if 2**i > n:
        break
    i+=1
print(i - 1,2**(i-1),sep = ' ')
