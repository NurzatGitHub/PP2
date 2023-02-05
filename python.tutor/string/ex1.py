s = input()
print(s[2])
print(s[-2])
print(s[:5])
print(s[:-2])
t = str()
for i in range(len(s)):
    if i % 2 == 0:
        t += str(s[i])
print(t)
x = str()
for i in range(len(s)):
    if i % 2 != 0:
        x += str(s[i])
print(x)
print(s[::-1])
for i in range(len(s) - 1,-1,-2):
    print(s[i],end='')
print()
print(len(s))