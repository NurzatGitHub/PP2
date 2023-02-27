n = int(input('Input number of sides: '))
a = int(input('Input the length of a side: '))

import math
def Area_Ofthe_POLYGON(n,a):
    h = a/(2*math.tan(math.pi/n))
    p = a*n
    S = (1/2)*h*p
    return int(S)
print('The area of the polygon is:',Area_Ofthe_POLYGON(n,a))