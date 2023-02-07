s=input()
for i in range(len(s)):
    if i % 3 == 0:
        continue
    else:
        print(s[i],end='')