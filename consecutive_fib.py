def productFib(prod):
    # your code
    fib = [0, 1]
    i = 0
    while fib[i] * fib[i+1] <= prod:
        fib.append(fib[i] + fib[i+1])
        if fib[i] * fib[i+1] == prod:
            return [fib[i], fib[i+1], True]
        i += 1
    return [fib[-2], fib[-1], False]

    # a, b = 0, 1
    # while a*b < prod:
    #     a, b = b, b + a
    # return [a, b, a*b == prod]


print(productFib(4895))
print(productFib(800))
print(productFib(714))
