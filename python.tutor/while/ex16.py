import math
def aver(l):
    sum = 0
    for i in l:
        sum += i
    return sum/len(l)
def std(l):
    sigma = 0
    k = len(l) - 1
    for i in l:
        sigma += ((i - aver(l))**2)
    
    return math.sqrt(sigma/k)
list = []
while True:
    a = int(input())
    if a == 0:
        break
    else:
        list.append(a)
print(std(list))