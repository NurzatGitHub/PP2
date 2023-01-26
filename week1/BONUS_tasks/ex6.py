'''
Например, если n = 7, то программа должна вывести 1 2 2 3 3 3 4.
'''

a = int(input())
k = []
for i in range(1,a + 1):
    for j in range(1,i + 1):
        k.append(i)

for i in range(a):
    print(k[i],end=' ')