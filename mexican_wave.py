def wave(str):
    # Code here
    return [str[:i] + str[i].upper() + str[i+1:] for i in range(len(str)) if str[i].isalpha()]


print(wave("hello"))
print(wave("codewars"))
