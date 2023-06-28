def min_value(digits):
    # your code here
    return int(''.join(sorted(set(map(str, digits)))))
