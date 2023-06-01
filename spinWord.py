def spin_words(sentence):
    # Your code goes here
    # res = []
    # for i in sentence.split(" "):
    #     if len(i) >= 5:
    #         res.append(i[::-1])
    #     else:
    #         res.append(i)
    # return " ".join(res)

    return " ".join([x[::-1] if len(x) >= 5 else x for x in sentence.split(" ")])


print(spin_words("This is a test"))
