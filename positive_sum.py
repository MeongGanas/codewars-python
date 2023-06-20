def positive_sum(arr):
    # Your code here
    return sum(i for i in arr if i > 0)


print(positive_sum([1, 2, 3, 4, 5, -1]))
