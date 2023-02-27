def decreasing(number):
    for i in range(number,-1,-1):
        yield i
n = int(input())
print(list(decreasing(n)))