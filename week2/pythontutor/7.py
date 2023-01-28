x = int(input())
y = int(input())
z = int(input())
s = 0
if(x % 2 != 0):
    s += x // 2
    s += 1
else:
    s += x // 2

if(y % 2 != 0):
    s += y // 2
    s += 1
else:
    s += y // 2

if(z % 2 != 0):
    s += z // 2
    s += 1
else:
    s += z // 2

print(s)