def has_33(NUMS):
    flag = False
    for i in range(len(NUMS)):
        if i + 1 < len(NUMS) and NUMS[i] == 3 and NUMS[i + 1] == 3:
            flag = True
    return flag
print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3])) 
print(has_33([3, 1, 3]))