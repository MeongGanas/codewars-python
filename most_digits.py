def find_longest(arr):
    # your code here
    return max(arr, key=lambda x: len(str(x)))

