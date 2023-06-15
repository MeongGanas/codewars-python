def binary_array_to_number(arr):
    # your code
    return int(int(''.join(map(str, arr)), 2))


print(binary_array_to_number([0, 0, 0, 1]))
print(binary_array_to_number([0, 0, 1, 1]))
