import re


def order(sentence):
    # code here
    temp = sorted(re.findall(r'\d+', sentence))
    res = []
    for i in temp:
        for j in sentence.split(" "):
            if i in j:
                res.append(j)
    return ''.join(res)

    # return ' '.join(sorted(words.split(), key=lambda w:sorted(w)))


print(order("is2 Thi1s T4est 3a"))
