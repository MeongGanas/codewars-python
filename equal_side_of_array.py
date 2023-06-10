def find_even_index(arr):
    # your code here
    for i in range(0, len(arr)):
        left = sum(arr[:i])
        right = sum(arr[i+1:])

        if left == right:
            return i
    return -1


print(find_even_index([1, 2, 3, 4, 3, 2, 1]))
