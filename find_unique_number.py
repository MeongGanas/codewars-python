def find_uniq(arr):
    # your code here
    # n: unique number in the array

    # Solution 1
    arr.sort()
    return arr[0] if arr.count(arr[0]) == 1 else arr[len(arr)-1]

    # Solution 2
    arr.sort()
    return arr[0] if (arr[0] < arr[len(arr)-1] and arr[0] < arr[len(arr)-2]) else arr[len(arr)-1]


print(find_uniq([1, 1, 1, 2, 1, 1]))
