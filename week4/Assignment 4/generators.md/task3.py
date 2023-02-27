def myfunc(number):
    for  i in range(number):
        if i % 3 == 0 and i % 4 == 0:
            yield i

n = int(input())
a = list(myfunc(n))
print(*a)