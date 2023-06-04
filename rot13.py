def rot13(message):
    res = []
    for i in list(message):
        if i.isalpha():
            if i.isupper():
                if (ord(i) - 64 + 13) > 26:
                    huruf = ord(i) - 64 + 13 - 26
                else:
                    huruf = ord(i) - 64 + 13
                res.append(chr(huruf + 64))
            else:
                if (ord(i) - 96 + 13) > 26:
                    huruf = ord(i) - 96 + 13 - 26
                else:
                    huruf = ord(i) - 96 + 13
                res.append(chr(huruf + 96))
        else:
            res.append(i)
    return ''.join(res)


print(rot13('aA bB zZ 1234 *!?%'))
