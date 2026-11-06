nums = [18, 23, 5, 25, 28, 45, 7, 12]

small = nums[0]

for num in nums:
    if num < small:
        small = num

print("Smallest number:", small)