def dig_pow(n, p):
    # your code
    res = 0
    for i in str(n):
        res += (int(i) ** p)
        p += 1

    return res // n if res % n == 0 else -1


print(dig_pow(89, 1))
print(dig_pow(92, 1))
print(dig_pow(46288, 3))
print(dig_pow(41, 5))
