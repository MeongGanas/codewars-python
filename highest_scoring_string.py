def high(x):
    # Code here
    # x = x.split(" ")
    # res = []
    # for i in x:
    #     total = sum([ord(j) - 96 for j in i])
    #     res.append(total)
    # return x[res.index(max(res))]

    return max(x.split(), key=lambda k: sum(ord(c) - 96 for c in k))


print(high('aa b'))
print(high('b aa'))
print(high('take me to semynak'))
print(high('man i need a taxi up to ubud'))
