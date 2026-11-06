nums = [12, 7, 15, 5, 23, 27, 9, 11, 20, 17, 0]

prime = []

for num in nums:
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            prime.append(num)

print("Prime numbers:", prime)