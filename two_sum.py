def two_sum(numbers, target):
    res = {}
    for i, num in enumerate(numbers):
        if target-num in res:
            return [res[target-num], i]
        res[num] = i
    return []


print(two_sum([1, 2, 3], 4))
