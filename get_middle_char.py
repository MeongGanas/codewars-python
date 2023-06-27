def get_middle(s):
    index = len(s)//2
    return s[index-1:index+1] if len(s) % 2 == 0 else s[index]


print(get_middle("test"))
print(get_middle("tst"))
print(get_middle("a"))
print(get_middle("of"))
