def average_readings(*args):
    if len(args) == 0:
        return None

    return sum(args) / len(args)


result = average_readings(10, 20, 30, 40)

if result is None:
    print("No readings provided")
else:
    print("Average:", result)

result = average_readings()

if result is None:
    print("No readings provided")