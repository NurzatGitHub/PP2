max,i = 0,0
while True:
    a = int(input())
    
    if a == 0:
        break
    elif a > max:
        max = a
        j = i
    i += 1
print(j)