s = input()
a = []
for i in s:
    a.append(i)
for i in range(len(a)):
    if a[i] == '1':
        a.insert(i,'one')
        a.remove('1')

for i in a:
    print(i,end='')
        
        