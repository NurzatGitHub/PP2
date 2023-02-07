def find_fibonacci_index(A):
    if A <= 0:
        return -1
    elif A == 1:
        return 1
    else:
        n = 2
        fib1, fib2 = 1, 1
        while fib2 < A:
            fib1, fib2 = fib2, fib1 + fib2
            n += 1
        if fib2 == A:
            return n
        else:
            return -1
print(find_fibonacci_index(int(input())))