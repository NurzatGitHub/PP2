s = str(input())
cnt = 1
x = 1
t = s[x:x + 1]
for i in s:
    if i in t:
        cnt += 1
    else:
        print(i, end='')
        print(cnt, end='')
        cnt = 1
    x += 1
    t = s[x:x + 1]
a = [int(i) for i in input().split()]
s = 0
for i in a:
    s += i
print(s)