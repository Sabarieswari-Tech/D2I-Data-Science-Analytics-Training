def top_k_frequent(nums, k):
    frequency = {}

    for num in nums:
        frequency[num] = frequency.get(num, 0) + 1

    sorted_nums = sorted(
        frequency,
        key=lambda x: frequency[x],
        reverse=True
    )

    return sorted_nums[:k]


nums = [1, 1, 1, 2, 2, 3]
k = 2

print("Top", k, "frequent values:", top_k_frequent(nums, k))