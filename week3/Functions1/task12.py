def histogram(nums):
    for items in nums:
        print('*'*items)
nums = [int(i) for i in input().split()]
histogram(nums)