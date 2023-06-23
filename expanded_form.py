def expanded_form(num):
    num = list(str(num))
    return " + ".join(v + "0" * (len(num) - i) for i, v in enumerate(num, 1) if int(v) != 0)

    # if num >= 10:
    #     res = []
    #     for i, v in enumerate(str(num), 1):
    #         if int(v) > 0:
    #             res.append(v + "0" * (len(str(num)) - i))
    #     return ' + '.join(res)
    # return str(num)


print(expanded_form(2))
print(expanded_form(12))
print(expanded_form(42))
print(expanded_form(70304))
print(expanded_form(4982342))
