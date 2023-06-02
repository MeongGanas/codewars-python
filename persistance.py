import operator


def persistence(n):
    # your code
    res = []
    n = str(n)
    while len(n) > 1:
        total = 1
        for i in n:
            total *= int(i)
        n = str(total)
        res.append(n)
    return len(res)


print(persistence(39))
