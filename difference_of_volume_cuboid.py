def find_difference(a, b):
    # Your code here!
    a = a[0] * a[1] * a[2]
    b = b[0] * b[1] * b[2]
    return abs(a-b)


print(find_difference([1, 2, 3], [4, 5, 6]))
