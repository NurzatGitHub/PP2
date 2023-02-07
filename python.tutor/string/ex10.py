s = input()
a = []
if s.find('@') == -1:
    print(s)
else:
    for i in range(len(s)):
        a.append(s[i])
    for i in range(len(a)):
        if a[i] == '@':
            continue
        else:
            print(a[i],end='')
        