# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# for k in range(c,d + 1):
#     print(" ",k,sep='\t',end='')
# print()
# for i in range(a,b + 1):
#     print(i,end='\t')
#     for j in range(c,d + 1):
#         print(i*j,end='\t')
#     print()
# a = int(input())
# b = int(input())
# s = 0 
# k = 0
# for i in range(a,b + 1):
#     if i % 3 == 0:
#         s += i
#         k += 1
# print(s/k)
# s = input()
# t = ''.join(set(s))
# print(len(t)/len(s) *100)
# string = input()
# char_seen = []
# for char in string:
#     if char not in char_seen:
#         char_seen.append(char)
# print(''.join(char_seen))
#######################################
# s = str(input())
# cnt = 1
# x = 1
# t = s[x:x + 1]
# for i in s:
#     if i in t:
#         cnt += 1
#     else:
#         print(i, end='')
#         print(cnt, end='')
#         cnt = 1
#     x += 1
#     t = s[x:x + 1]
# a = [int(i) for i in input().split()]
# s = 0
# for i in a:
#     s += i
# print(s)
########################################
# a = [int(i) for i in input().split()]
# if len(a) == 1:
#     print(a[0])
# else:
#     for i in range(len(a)):
#         if i == len(a)-1:
#             print(a[i - 1] + a[0],end=' ')
#         else:
#             print(a[i - 1] + a[i + 1],end=" ")
#########################################
a = [int(i) for i in input().split()]
a.sort()
b = []
t = []
if len(a) == 1:
    for i in b:
        print(i)
else:
    for i in range(len(a)):
        if(a[i] == a[i - 1]):
            b.append(a[i])
    t = set(b) 
    for i in t:
        print(i,end=' ')