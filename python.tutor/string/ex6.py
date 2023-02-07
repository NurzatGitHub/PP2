s = input()
cnt = 0
for i in range(len(s)):
    if s[i] == 'f':
        cnt += 1
if cnt == 1:
    print(-1)
elif cnt == 0:
    print(-2)
else:
    a = s.find('f')
    for i in range(a + 1,len(s)):
        if s[i] == 'f':
            j = i
            break
    print(j)
        