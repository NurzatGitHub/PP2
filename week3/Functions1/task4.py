a = [int(i) for i in input().split()]
def filter_prime(list):
    l = []
    for  i in range(len(list)):
        flag = True
        for j in range(2,list[i]):
            if list[i] % j == 0:
                flag = False
        if flag:
            l.append(list[i])
    print(l)
filter_prime(a)