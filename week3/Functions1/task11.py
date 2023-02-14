def palindrome(string):
    lst = list(string)
    l = []
    # for i in string:
    #     lst.append(i)
    l = lst[::-1]
    #print(l)
    #print(lst)
    if l == lst:
        print(True)
    else:print(False)
s = input()
palindrome(s)