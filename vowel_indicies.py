def vowel_indices(word):
    # your code here
    return [i for i, v in enumerate(word, 1) if v.lower() in "aiueoy"]
