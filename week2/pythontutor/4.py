a = int(input())
h = m = 0
while a >= 60:
    a -= 60
    h += 1
m += a
if(h >= 24):
    print(24 - h,m)
else:
    print(h,m)