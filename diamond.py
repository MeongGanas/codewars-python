def diamond(n):
    # Make some diamonds!
    if n % 2 == 0 or not str(n).isdigit():
        return None

    res = ""

    for i in range(1, n + 1, 2):
        res += " " * int((n - i)/2) + "*" * i + "\n"
    for i in range(n-2, 0, -2):
        res += " " * int((n - i)/2) + "*" * i + "\n"
    return res


print(diamond(3))
