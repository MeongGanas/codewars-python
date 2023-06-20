def basic_op(operator, value1, value2):
    # your code here
    # return {"+": value1 + value2, "-": value1 - value2, "*": value1 * value2, "/": value1 / value2}.get(operator)
    return eval("{}{}{}".format(value1, operator, value2))


print(basic_op("+", 1, 2))
