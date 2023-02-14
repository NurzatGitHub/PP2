# import itertools
# s = 'ABC'
# nums = s
# # Output: ['ABC', 'ACB', 'BAC', 'BCA', 'CAB', 'CBA']
# print([''.join(permutation) for permutation in permutations])

def nextpermutation(string, i = 0):
    if i == len(string):
        #print(string)
        print("".join(string))
    for j in range(i,len(string)):
        chars = [k for k in string]
        chars[i],chars[j] = chars[j],chars[i]
        nextpermutation(chars,i + 1)

s = input()
nextpermutation(s)