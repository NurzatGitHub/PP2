h = int(input('Height: '))
v1 = int(input('Base, first value: '))
v2 = int(input('Base, second value: '))
import math

def trapezoid(h,a,b):
    len = a + b
    s = (len*h)/2
    return s

print('Expected Output:',trapezoid(h,v1,v2))