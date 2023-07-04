def multiple_of_index(arr):
    return [0] + [arr[i] for i in range(1, len(arr)) if arr[i] % i == 0] if arr[0] == 0 else [arr[i] for i in range(1, len(arr)) if arr[i] % i == 0]
