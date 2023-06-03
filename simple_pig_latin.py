import re


def pig_it(word):
    return " ".join(x[1:] + x[0] + "ay" if x.isalpha() else x for x in word.split())
    # isalpha return true if x is alphabet


print(pig_it('Hello world !'))
