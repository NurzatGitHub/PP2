i = 1
max  = 0
b = 1000
while True:
    a = int(input())
    if a == 0:
        break
    #i = 1
    while True:
        if b != a:
            b = a
            i = 1
            break
        else:
            i += 1
            b = a
            break
            
    if i > max:
        max = i

print(max)