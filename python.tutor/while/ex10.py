i,j = 0,0
b = 0
while True:
    a = int(input())
    if a == 0:
        break
    
    if a > b:
        i += 1
    b = a
print(i-1)