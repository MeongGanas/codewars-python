from functools import reduce


def grow(arr):
    return reduce(lambda a, b: a * b, arr)


print(grow([1, 2, 3, 4, 5]))
