# def encode(st):
#     key = {"a": 1, "e": 2, "i":3, "o": 4, "u":5}
#     return ''.join([str(key[i]) if i in key else i for i in st])

# def decode(st):
#     key = {"1": "a", "2": "e", "3":"i", "4": "o", "5":"u"}
#     return ''.join([key[i] if i in key else i for i in st])


def encode(s, t=str.maketrans("aeiou", "12345")):
    return s.translate(t)


def decode(s, t=str.maketrans("12345", "aeiou")):
    return s.translate(t)


print(encode("hello"))
print(decode("h2ll4"))
