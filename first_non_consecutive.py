def first_non_consecutive(arr):
    # your code here
    i = 0
    while i < len(arr)-1:
        if arr[i] + 1 != arr[i+1]:
            return arr[i+1]
        i += 1


print(first_non_consecutive([1, 2, 3, 4, 5, 6, 7, 8]))
