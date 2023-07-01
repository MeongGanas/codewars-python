def row_weights(array):
    # your code here
    res = [0, 0]
    for i, v in enumerate(array):
        if i % 2 == 0:
            res[0] += v
        else:
            res[1] += v
    return tuple(res)


print(row_weights([50, 60, 70, 80]))
