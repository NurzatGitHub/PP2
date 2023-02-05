n = int(input())
sum1 = 0
sum2 = 0
for i in range(1,n):
    a = int(input())
    sum1 += a
for i in range(1,n+1):
    sum2 += i
print(sum2 - sum1)

            