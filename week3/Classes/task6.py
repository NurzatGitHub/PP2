li = [1,2,3,4,5,6,7,8,9,0]
odd = filter(lambda a: a % 2 != 0,li)
print(odd)
print(list(odd))
even = filter(lambda a: a % 2 == 0, li)
print(even)
print(list(even))