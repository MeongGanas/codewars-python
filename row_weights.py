def row_weights(array):
    # your code here
    return sum(array[::2]), sum(array[1::2])


print(row_weights([50, 60, 70, 80]))
