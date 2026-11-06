def find_max_length(nums):
    balance = 0
    max_length = 0
    seen = {0: -1}

    for i in range(len(nums)):
        if nums[i] == 0:
            balance -= 1
        else:
            balance += 1

        if balance in seen:
            max_length = max(max_length, i - seen[balance])
        else:
            seen[balance] = i

    return max_length


nums = [0, 1, 0]

print("Maximum balanced subarray length:",
      find_max_length(nums))