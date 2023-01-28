a = int(input())
b = int(input())
k = max(a,b)
while k % min(a,b) != 0:
    k += k
    continue
print(k)