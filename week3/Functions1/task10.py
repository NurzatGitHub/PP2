def set(list):
    l = []
    for i in range(len(list)):
        if list[i] in l:
            continue
        else:
            l.append(list[i])
    print(l)

a = [int(i) for i in input().split()]
set(a)