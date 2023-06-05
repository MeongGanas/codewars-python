def is_pangram(s):
    # alpha = set()
    # for i in s:
    #     if i.isalpha():
    #         alpha.add(i.casefold())

    # return len(alpha) == 26

    return len({i.casefold() for i in s if i.isalpha()}) == 26


print(is_pangram("The quick, brown fox jumps over the lazy dog!"))
