def distinct(seq):
    res = []
    seen = set()
    for i in seq:
        if i not in seen:
            res.append(i)
            seen.append(i)
    return res


    # return list(dict.fromkeys(seq))
