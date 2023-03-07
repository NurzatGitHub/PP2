import math

def prod(numbers):
    return math.prod(numbers)

l = [int(i) for i in input().split()]

print(prod(l))