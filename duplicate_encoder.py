def duplicate_encode(word):
    # your code here
    word = word.lower()
    return ''.join(["(" if word.count(i) == 1 else ")" for i in word])
