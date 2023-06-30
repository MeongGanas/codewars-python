def sum_pairs(ints, s):
    myset = set()
    for num in ints:
        required = s - num
        if required in myset:
            return [required, num]
        myset.add(num)


print(sum_pairs([11, 3, 7, 5], 10))
print(sum_pairs([4, 3, 2, 3, 4], 6))
print(sum_pairs([0, 0, -2, 3], 2))
print(sum_pairs([10, 5, 2, 3, 7, 5], 10))
