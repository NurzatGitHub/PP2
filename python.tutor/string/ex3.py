s = input()
if len(s)%2 != 0:
    a = len(s)//2 + 1
else:
    a = len(s)//2
for i in range(a,len(s)):
    print(s[i],end='')
for i in range(a):
    print(s[i],end='')
