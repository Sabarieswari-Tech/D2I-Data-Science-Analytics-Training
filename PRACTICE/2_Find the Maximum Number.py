nums = [18, 23, 5, 25, 28, 45, 7, 12]

large = nums[0]

for num in nums:
    if num > large:
        large = num

print("Largest number:", large)