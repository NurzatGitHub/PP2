a = int(input())
b = int(input())
c = int(input())
if a == b and c == b:
    print(3)
elif b == a and c != a:
    print(2)
elif b == c and a != c:
    print(2)
elif a == c and a != b:
    print(2)
else:
    print(0)