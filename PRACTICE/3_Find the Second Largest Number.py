nums = [18, 23, 5, 25, 28, 45, 7, 12]

large = nums[0]
second = nums[0]

for num in nums:
    if num > large:
        second = large
        large = num
    elif num > second and num != large:
        second = num

print("Second largest:", second)