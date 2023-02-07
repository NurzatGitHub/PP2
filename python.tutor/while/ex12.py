b = 0
l = []
while True:
    a = int(input())
    if a == 0:
        break
    l.append(a)
    if a > b:
        b = a
cnt = 0
for i in range(len(l)):
    if l[i] == b:
        cnt += 1

print(cnt)