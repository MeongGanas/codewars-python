def encrypt_once(text):

    e_str = ""
    o_str = ""

    for i in range(0, len(text)):
        if i % 2 != 0:  # check if index is even
            e_str += text[i]  # creat string with odd indices
        else:
            o_str += text[i]  # creat string with even indices

    return e_str+o_str


print(encrypt_once("This is a test!"))


def encrypt(text, n):  # this function repeat encrypt_once n times

    s = [text]

    for i in range(1, n+1):
        s.append(encrypt_once(s[i-1]))

    return s[n]


print(encrypt("This is a test!", -1))


def decrypt_once(text):

    decry_one = ""
    decry_two = ""

    mid = int(len(text)/2)  # find mid index

    decry_one += text[0:mid]  # breaks string into two strings
    decry_two += text[mid:]

    s = ""

    for i in range(0, mid):
        # combine alternating even and odd indices
        s += decry_two[i]+decry_one[i]

    if len(text) % 2 != 0:
        # if length is odd , add the last index of decry_two
        s += decry_two[mid]

    return s


def decrypt(text, n):

    s = [text]

    for i in range(1, n+1):
        s.append(decrypt_once(s[i-1]))

    return s[n]
