def vert_mirror(strng):
    # your code
    return '\n'.join([i[::-1] for i in strng.split('\n')])


def hor_mirror(strng):
    # your code
    return '\n'.join(strng.split("\n")[::-1])


def oper(fct, s):
    # your code
    return fct(s)
