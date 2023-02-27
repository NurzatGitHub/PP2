def square_a_b(a,b):
    for i in range(a,b + 1):
        yield i*i

a,b = map(int,input().split())
for i in square_a_b(a,b):
    print(i,end=' ')