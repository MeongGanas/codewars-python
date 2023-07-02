def mxdiflg(a1, a2):
    # your code
    if len(a1) > 0 and len(a2) > 0:
        a1 = [len(i) for i in a1]
        a2 = [len(i) for i in a2]
        return max([max(a2) - min(a1), max(a1) - min(a2)])
    return -1
