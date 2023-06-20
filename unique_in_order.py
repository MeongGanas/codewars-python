def unique_in_order(sequence):
    res = []
    for item in sequence:
        if len(res) == 0 or item != res[-1]:
            res.append(item)
    return res


print(unique_in_order("A"))
print(unique_in_order('AAAABBBCCDAABBB'))
print(unique_in_order('ABBCcAD'))
print(unique_in_order([1, 2, 2, 3, 3]))
