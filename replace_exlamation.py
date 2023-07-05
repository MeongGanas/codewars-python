def replace_exclamation(s):
    return ''.join(["!" if i.lower() in "aiueo" else i for i in s])
