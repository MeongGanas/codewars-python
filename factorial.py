def factorial(n):
    if n < 0 or n > 12:
        raise ValueError
    res = 1
    for i in range(1, n+1):
        res *= i
    return res


print(factorial(-2))
