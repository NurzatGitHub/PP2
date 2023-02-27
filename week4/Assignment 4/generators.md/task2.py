def odd_numbers(number):
    for i in range(1,number + 1):
        if i % 2 != 0:
            yield i

n = int(input())

print(list(odd_numbers(n)))