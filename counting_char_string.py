def count(s):
    # The function code should be here
    return {i: s.count(i) for i in set(s)}


print(count('aba'))
