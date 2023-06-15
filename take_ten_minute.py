def is_valid_walk(walk):
    # determine if walk is valid
    key = {"n": 2, "s": -2, "w": 1, "e": -1}
    return sum([key[i] for i in walk]) == 0 and len(walk) == 10


print(is_valid_walk(['n', 's', 'n', 's', 'n', 's', 'n', 's', 'n', 's']))
print(is_valid_walk(['e', 'w', 'e', 'w', 'n', 's', 'n', 's', 'e', 'w']))
print(is_valid_walk(['n', 's', 'e', 'w', 'n', 's', 'e', 'w', 'n', 's']))
print(is_valid_walk(['n', 's', 'n', 's', 'n', 's', 'n', 's', 'n', 'n']))
print(is_valid_walk(['e', 'e', 'e', 'w', 'n', 's', 'n', 's', 'e', 'w']))
