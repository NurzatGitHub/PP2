s = input()
cnt = 0
for i in range(len(s)):
    if s.find('f') == -1:
        break
    elif s[i] == 'f':
        cnt += 1
        j = i

if cnt == 1:
    print(s.find('f'))
elif cnt == 0:
    pass
else:
    print(s.find('f'),j)