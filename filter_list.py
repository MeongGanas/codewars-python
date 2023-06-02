def filter_list(l):
    'return a new list with the strings filtered out'
    return [i for i in l if type(i) == int]


print(filter_list([1, 2, 'a', 'b']))
