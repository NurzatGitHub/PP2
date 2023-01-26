'''
Позиции нумеруются с нуля, если число 
�
x не встречается в списке, вывести строку "Отсутствует" (без кавычек, с большой буквы).
'''

a = [int(i) for i in input().split()]
x = int(input())
k = []
for i in range(len(a)):
    if(a[i] == x):
        k.append(i)
if len(k) == 0:
    print('Отсутствует')
else:
    for j in k:
        print(j,end=' ')