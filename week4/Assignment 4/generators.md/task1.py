def square_numbers(number):
    for i in range(1,number + 1):
        yield (i*i)

n = int(input())
for i in square_numbers(n):
    print(i)