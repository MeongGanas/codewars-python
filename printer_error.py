import re


def printer_error(s):
    # your code
    return "{}/{}".format(len(re.findall("[n-z]", s)), len(s))


print(printer_error(
    ["aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz"]))
