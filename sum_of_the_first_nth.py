def series_sum(n):
    # Happy Coding ^_^
    series = [1/i for i in range(1, 3*n-1, 3)]
    return "{:.2f}".format(sum(series))


print(series_sum(3))
print(series_sum(5))
