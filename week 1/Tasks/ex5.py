'''
Напишите программу, которая считывает с консоли числа (по одному в строке) до тех пор, пока сумма введённых чисел не будет равна 0 и сразу после этого выводит сумму квадратов всех считанных чисел.
'''
k =[]
s = 0
while(True):
    a = int(input())
    s += a
    k.append(a)
    if(s == 0):
        break

sum = 0
for i in range(len(k)):
    sum += ((k[i])**2)

print(sum)    