i = 0
sum = 0
while True:
    a = int(input())
    if a == 0:
        break
    i += 1
    sum += a
print(sum/i)