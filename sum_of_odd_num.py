def row_sum_odd_numbers(n):
    # your code here
    return sum([i for i in range(n * n - n, n * n + n) if i % 2 == 1])


print(row_sum_odd_numbers(4))
