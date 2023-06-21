def accum(s):
    # your code
    return '-'.join([(s[i] * (i+1)).title() for i in range(len(s))])


print(accum("abcd"))
print(accum("ZpglnRxqenU"))
