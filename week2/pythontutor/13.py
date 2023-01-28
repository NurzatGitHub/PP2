a = int(input())
b = int(input())
c = int(input())
#print(min(a,b,c))
if a >= b and c >= b:
    print(b)
elif b >= a and c >= a:
    print(a)
elif b >= c and a >= c:
    print(c)