def min_sum(arr):
    # Your code here
    arr = sorted(arr)
    return sum([arr[i] * arr[-i-1] for i in range(len(arr) // 2)])
