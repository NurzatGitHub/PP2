n =int(input())
k = int(input())
s = 0
if(k % n == 0):
    print(k //n)
else:
    while k % n != 0:
        s += 1
        k -= 1
    print(k//n)
print(s)