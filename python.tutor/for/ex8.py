sum = 1
sum1= 0
n = int(input())
i = 1
j = 1
while i <= n:
    while j <= i:
        sum *= j
        j += 1
    i += 1
    sum1 += sum
    
print(sum1)