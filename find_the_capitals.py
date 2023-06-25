def capitals(word):
    # your code here
    return [i for i, v in enumerate(word) if v.isupper()]
