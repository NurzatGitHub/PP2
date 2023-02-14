def spy_game(NUMS):
    flag = [0,0,7]
    lis = []
    for i in range(len(NUMS)):
        if NUMS[i] == 0 or NUMS[i] == 7:
            lis.append(NUMS[i])
    if flag == lis:
        print(True)
    else:print(False)

spy_game([1,2,4,0,0,7,5])
spy_game([1,0,2,4,0,5,7])
spy_game([1,7,2,0,4,5,0])