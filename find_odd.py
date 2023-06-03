def find_it(seq):
    return [i for i in seq if seq.count(i) % 2 == 1][0]

# import operator
# import functools

# def find_it(xs):
#     return functools.reduce(operator.xor, xs)


print(find_it([1, 2, 2, 3, 3, 3, 4, 3, 3, 3, 2, 2, 1]))
