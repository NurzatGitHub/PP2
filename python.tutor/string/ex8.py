s = input()
for i in range(len(s)):
    if s[i] == 'h':
        j = i
a = s.find('h')
for i in range(a):
    print(s[i],end='')
for i in range(j,a - 1,-1):
    print(s[i],end='')
for i in range(j + 1,len(s)):
    print(s[i],end='')